"""
Base fetcher class. All thread fetchers inherit from this.
Handles retry logic, logging, and the validate-then-write contract.
Subclasses implement fetch() and transform() only.
"""

import logging
import sys
import time
from abc import ABC, abstractmethod
from datetime import datetime, timezone
from pathlib import Path

import httpx

# make scripts/validate_schema importable from fetchers/
sys.path.insert(0, str(Path(__file__).parent.parent))
from scripts.validate_schema import validate_and_write

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class BaseFetcher(ABC):
    """
    Subclass this for each thread fetcher.

    Required overrides:
        thread_name  — matches the data filename, e.g. "elite_overproduction"
        fetch()      — pull raw data from source, return raw response
        transform()  — convert raw response to validated schema dict

    Optional overrides:
        validate_anomalies() — add domain-specific soft warnings to data dict
    """

    thread_name: str = NotImplemented
    max_retries: int = 3
    retry_delay: float = 2.0  # seconds, doubles on each retry

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.client = httpx.Client(
            timeout=30.0,
            headers={"User-Agent": "convergence-analysis/1.0 (github.com/debcapadona/convergence-analysis)"},
        )

    @abstractmethod
    def fetch(self) -> dict | list | str:
        """Pull raw data from source. Return whatever the source gives you."""
        ...

    @abstractmethod
    def transform(self, raw: dict | list | str) -> dict:
        """Convert raw source data to schema-conformant dict."""
        ...

    def validate_anomalies(self, data: dict) -> list[str]:
        """
        Override to add domain-specific soft warnings.
        e.g. 'ratio exceeds historical max', 'source data gap > 2 years'
        Returns list of warning strings. Empty = no anomalies.
        """
        return []

    def get(self, url: str, **kwargs) -> httpx.Response:
        """
        HTTP GET with retry and exponential backoff.
        Raises on final failure.
        """
        delay = self.retry_delay
        last_error = None

        for attempt in range(1, self.max_retries + 1):
            try:
                self.logger.info(f"GET {url} (attempt {attempt}/{self.max_retries})")
                response = self.client.get(url, **kwargs)
                response.raise_for_status()
                return response
            except httpx.HTTPStatusError as e:
                self.logger.warning(f"HTTP {e.response.status_code} on attempt {attempt}")
                last_error = e
            except httpx.RequestError as e:
                self.logger.warning(f"Request error on attempt {attempt}: {e}")
                last_error = e

            if attempt < self.max_retries:
                self.logger.info(f"Retrying in {delay}s...")
                time.sleep(delay)
                delay *= 2

        raise RuntimeError(
            f"Failed to GET {url} after {self.max_retries} attempts"
        ) from last_error

    def run(self) -> None:
        """
        Main entry point. Called by GitHub Actions.
        fetch → transform → anomaly check → validate → write
        """
        if self.thread_name is NotImplemented:
            raise NotImplementedError("Subclass must define thread_name")

        self.logger.info(f"Starting fetch for thread: {self.thread_name}")

        try:
            raw = self.fetch()
            self.logger.info("Fetch complete, transforming...")

            data = self.transform(raw)

            warnings = self.validate_anomalies(data)
            if warnings:
                data["warnings"] = warnings
                for w in warnings:
                    self.logger.warning(f"Data anomaly: {w}")

            validate_and_write(data, self.thread_name)
            self.logger.info(f"Done. {self.thread_name}.json updated.")

        except Exception as e:
            self.logger.error(f"Fetcher failed: {e}")
            raise

        finally:
            self.client.close()


if __name__ == "__main__":
    print("BaseFetcher is a base class — run a specific thread fetcher instead.")
