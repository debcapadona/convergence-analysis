"""
Fiscal State Decline — Thread 3
Tainter complexity cost inflection: debt service crowding out state capacity

Stress series:
  - debt_gdp: federal debt held by public as % of GDP (FRED: GFDGDPA188S)
  - net_interest_pct: net interest as % of federal revenue (FRED: derived)
  - mandatory_pct: mandatory spending as % of total outlays (FRED: derived)

Counterweight series:
  - revenue_gdp: federal revenue as % of GDP (FRED: FYFRGDA188S)
  - real_gdp_growth: real GDP growth YoY % (FRED: A191RL1A225NBEA)

Sources:
  FRED API — Federal Reserve Bank of St. Louis
  Series: GFDGDPA188S, FYFRGDA188S, A191RL1A225NBEA
  Supplemental: OMB Historical Tables for mandatory/interest breakdowns

Update frequency: annual (CBO Budget Outlook releases Feb/March)
Next expected: 2027-03
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

sys.path.insert(0, str(Path(__file__).parent.parent))
from fetchers.base_fetcher import BaseFetcher

FRED_API_KEY = os.getenv("FRED_API_KEY")
FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"

# OMB Historical Tables — mandatory spending % of total outlays
# Table 8.1 — hardcoded, OMB doesn't have a clean API
MANDATORY_PCT = {
    1980: 47.0, 1981: 47.6, 1982: 46.5, 1983: 47.8, 1984: 45.8,
    1985: 45.4, 1986: 45.5, 1987: 45.4, 1988: 46.1, 1989: 46.5,
    1990: 47.5, 1991: 49.0, 1992: 50.6, 1993: 51.4, 1994: 52.4,
    1995: 53.2, 1996: 53.6, 1997: 53.2, 1998: 53.0, 1999: 53.0,
    2000: 52.4, 2001: 53.7, 2002: 54.8, 2003: 54.2, 2004: 53.9,
    2005: 53.4, 2006: 53.3, 2007: 53.4, 2008: 55.0, 2009: 60.4,
    2010: 59.9, 2011: 59.5, 2012: 60.2, 2013: 59.0, 2014: 60.5,
    2015: 61.2, 2016: 61.9, 2017: 61.6, 2018: 61.3, 2019: 61.8,
    2020: 64.0, 2021: 63.2, 2022: 61.8, 2023: 62.4, 2024: 63.1,
}

# OMB Historical Tables — net interest as % of federal revenue
NET_INTEREST_PCT = {
    1980: 12.3, 1981: 14.8, 1982: 17.0, 1983: 18.8, 1984: 20.4,
    1985: 21.4, 1986: 21.7, 1987: 21.0, 1988: 20.9, 1989: 22.0,
    1990: 23.1, 1991: 23.9, 1992: 23.8, 1993: 23.0, 1994: 22.6,
    1995: 23.7, 1996: 23.7, 1997: 22.8, 1998: 20.9, 1999: 19.4,
    2000: 17.4, 2001: 16.8, 2002: 14.9, 2003: 13.9, 2004: 13.0,
    2005: 13.1, 2006: 14.0, 2007: 14.8, 2008: 14.6, 2009: 12.8,
    2010: 12.4, 2011: 13.4, 2012: 13.4, 2013: 12.5, 2014: 12.3,
    2015: 12.1, 2016: 12.0, 2017: 12.5, 2018: 13.8, 2019: 15.4,
    2020: 12.8, 2021: 10.8, 2022: 13.6, 2023: 19.2, 2024: 22.4,
}

# CBO projections 2025-2051
PROJ_DEBT_GDP = {
    2025: 100.1, 2026: 102.8, 2027: 105.2, 2028: 107.4, 2029: 109.8,
    2030: 112.4, 2031: 115.1, 2032: 117.8, 2033: 120.6, 2034: 123.4,
    2035: 126.2, 2036: 129.1, 2037: 132.0, 2038: 135.0, 2039: 138.0,
    2040: 141.0, 2041: 144.1, 2042: 147.2, 2043: 150.4, 2044: 153.6,
    2045: 156.8, 2046: 160.1, 2047: 163.4, 2048: 166.8, 2049: 170.2,
    2050: 173.7, 2051: 177.2,
}

PROJ_NET_INTEREST = {
    2025: 24.1, 2026: 25.8, 2027: 27.2, 2028: 28.4, 2029: 29.6,
    2030: 30.8, 2031: 32.1, 2032: 33.4, 2033: 34.7, 2034: 36.1,
    2035: 37.4, 2036: 38.8, 2037: 40.2, 2038: 41.7, 2039: 43.1,
    2040: 44.6, 2041: 46.1, 2042: 47.7, 2043: 49.2, 2044: 50.8,
    2045: 52.4, 2046: 54.1, 2047: 55.8, 2048: 57.5, 2049: 59.2,
    2050: 61.0, 2051: 62.8,
}

SERIES = [
    {
        "series_id": "debt_gdp",
        "label": "Federal Debt / GDP (%)",
        "type": "stress",
        "unit": "percent",
        "color": "#e05252",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "net_interest_pct",
        "label": "Net Interest / Revenue (%)",
        "type": "stress",
        "unit": "percent",
        "color": "#e0a050",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "mandatory_pct",
        "label": "Mandatory Spending / Outlays (%)",
        "type": "stress",
        "unit": "percent",
        "color": "#c0392b",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
    {
        "series_id": "revenue_gdp",
        "label": "Federal Revenue / GDP (%)",
        "type": "counterweight",
        "unit": "percent",
        "color": "#52a8e0",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "real_gdp_growth",
        "label": "Real GDP Growth (%)",
        "type": "counterweight",
        "unit": "percent",
        "color": "#5db85d",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
    {
        "series_id": "debt_gdp_forecast",
        "label": "Debt / GDP — Projected (%)",
        "type": "stress",
        "unit": "percent",
        "color": None,
        "stroke_style": "dashed",
        "stroke_width": 1.5,
        "is_forecast": True,
    },
    {
        "series_id": "net_interest_forecast",
        "label": "Net Interest / Revenue — Projected (%)",
        "type": "stress",
        "unit": "percent",
        "color": None,
        "stroke_style": "dashed",
        "stroke_width": 1.5,
        "is_forecast": True,
    },
]


class FiscalDeclineFetcher(BaseFetcher):
    thread_name = "fiscal_decline"

    def _fred(self, series_id: str, frequency: str = "a") -> dict:
        """Fetch a single FRED series, return {year: value} dict."""
        response = self.get(
            FRED_BASE,
            params={
                "series_id": series_id,
                "api_key": FRED_API_KEY,
                "file_type": "json",
                "frequency": frequency,
                "observation_start": "1980-01-01",
            },
        )
        data = response.json()
        result = {}
        for obs in data.get("observations", []):
            if obs["value"] == ".":
                continue
            year = int(obs["date"][:4])
            result[year] = round(float(obs["value"]), 2)
        return result

    def fetch(self) -> dict:
        self.logger.info("Fetching FRED series...")
        return {
            "debt_gdp": self._fred("GFDGDPA188S"),
            "revenue_gdp": self._fred("FYFRGDA188S"),
            "real_gdp_growth": self._fred("A191RL1A225NBEA"),
            "mandatory_pct": MANDATORY_PCT,
            "net_interest_pct": NET_INTEREST_PCT,
            "proj_debt_gdp": PROJ_DEBT_GDP,
            "proj_net_interest": PROJ_NET_INTEREST,
        }

    def transform(self, raw: dict) -> dict:
        observations = []

        series_map = {
            "debt_gdp": ("debt_gdp", False, "FRED GFDGDPA188S 2026"),
            "revenue_gdp": ("revenue_gdp", False, "FRED FYFRGDA188S 2026"),
            "real_gdp_growth": ("real_gdp_growth", False, "FRED A191RL1A225NBEA 2026"),
            "mandatory_pct": ("mandatory_pct", False, "OMB Historical Tables 2026"),
            "net_interest_pct": ("net_interest_pct", False, "OMB Historical Tables 2026"),
            "proj_debt_gdp": ("debt_gdp_forecast", True, "CBO Budget Outlook 2026"),
            "proj_net_interest": ("net_interest_forecast", True, "CBO Budget Outlook 2026"),
        }

        for raw_key, (series_id, is_proj, source) in series_map.items():
            for year, value in raw[raw_key].items():
                observations.append({
                    "date": f"{year}-01-01",
                    "series_id": series_id,
                    "value": value,
                    "is_projection": is_proj,
                    "vintage": "2026-06-04",
                    "source_version": source,
                })

        return {
            "meta": {
                "thread": "fiscal_decline",
                "label": "Fiscal State Decline",
                "last_updated": "2026-06-04",
                "update_frequency": "annual",
                "next_expected_update": "2027-03",
                "source": "FRED API + OMB Historical Tables + CBO Budget Outlook",
                "theory_ref": "Tainter — debt service crowding out state capacity; complexity cost inflection point as governance failure precursor",
            },
            "series": SERIES,
            "observations": sorted(observations, key=lambda x: (x["date"], x["series_id"])),
        }

    def validate_anomalies(self, data: dict) -> list[str]:
        warnings = []
        debt = {
            o["date"][:4]: o["value"]
            for o in data["observations"]
            if o["series_id"] == "debt_gdp" and not o["is_projection"]
        }
        if debt:
            latest = max(debt.keys())
            if debt[latest] > 100:
                warnings.append(
                    f"Debt/GDP exceeds 100% ({debt[latest]}%) — verify FRED series"
                )
        interest = {
            o["date"][:4]: o["value"]
            for o in data["observations"]
            if o["series_id"] == "net_interest_pct" and not o["is_projection"]
        }
        if interest:
            latest = max(interest.keys())
            if interest[latest] > 20:
                warnings.append(
                    f"Net interest/revenue exceeds 20% ({interest[latest]}%) — historically associated with fiscal crisis"
                )
        return warnings


if __name__ == "__main__":
    FiscalDeclineFetcher().run()
