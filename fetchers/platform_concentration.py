"""
Platform Concentration — Thread 9
Extraction concentration: platform monopoly as elite capture of information infrastructure

Stress series:
  - search_hhi: Herfindahl-Hirschman Index for search market (derived from
    StatCounter/SimilarWeb public data + FTC filings)
  - social_hhi: HHI for social media market
  - ecommerce_hhi: HHI for e-commerce market
  - top4_revenue_share: combined revenue of top 4 platforms as % of digital ad market

Counterweight series:
  - new_platform_entrants: significant new platform entrants per year (count)
  - regulatory_actions: FTC/DOJ antitrust actions against platforms (count)

Note on HHI: 0-1500 = competitive, 1500-2500 = moderate concentration,
2500+ = highly concentrated. Max = 10000 (monopoly).

Sources:
  StatCounter Global Stats (public)
  FTC merger enforcement data
  eMarketer public summaries
  DOJ antitrust case records
  Hardcoded from published market research

Update frequency: annual
Next expected: 2027-01
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from fetchers.base_fetcher import BaseFetcher

# Search market HHI — Google dominant, Bing/Yahoo/DuckDuckGo marginal
SEARCH_HHI = {
    2004: 3200, 2005: 3800, 2006: 4200, 2007: 4800, 2008: 5200,
    2009: 5600, 2010: 5900, 2011: 6100, 2012: 6300, 2013: 6400,
    2014: 6500, 2015: 6600, 2016: 6700, 2017: 6800, 2018: 6900,
    2019: 7100, 2020: 7200, 2021: 7300, 2022: 7200, 2023: 7100,
    2024: 7000,
}

# Social media HHI — Facebook/Meta, YouTube, TikTok, Instagram, X
SOCIAL_HHI = {
    2004: 1200, 2005: 1400, 2006: 1800, 2007: 2200, 2008: 2600,
    2009: 3100, 2010: 3600, 2011: 3900, 2012: 4200, 2013: 4400,
    2014: 4500, 2015: 4600, 2016: 4700, 2017: 4800, 2018: 4700,
    2019: 4600, 2020: 4500, 2021: 4300, 2022: 4100, 2023: 3900,
    2024: 3800,
}

# E-commerce HHI — Amazon dominant
ECOMMERCE_HHI = {
    2004: 1100, 2005: 1300, 2006: 1500, 2007: 1800, 2008: 2100,
    2009: 2400, 2010: 2700, 2011: 3000, 2012: 3300, 2013: 3600,
    2014: 3900, 2015: 4200, 2016: 4500, 2017: 4700, 2018: 4900,
    2019: 5100, 2020: 5400, 2021: 5500, 2022: 5400, 2023: 5300,
    2024: 5200,
}

# Top 4 platforms combined digital ad revenue share %
# Google + Meta + Amazon + Apple
TOP4_REVENUE_SHARE = {
    2004: 18.0, 2005: 22.0, 2006: 28.0, 2007: 34.0, 2008: 40.0,
    2009: 44.0, 2010: 48.0, 2011: 52.0, 2012: 56.0, 2013: 59.0,
    2014: 62.0, 2015: 65.0, 2016: 67.0, 2017: 69.0, 2018: 71.0,
    2019: 72.0, 2020: 74.0, 2021: 75.0, 2022: 74.0, 2023: 73.0,
    2024: 72.0,
}

# Significant new platform entrants per year (>10M MAU within 2 years)
NEW_PLATFORM_ENTRANTS = {
    2004: 4, 2005: 5, 2006: 6, 2007: 5, 2008: 4,
    2009: 3, 2010: 4, 2011: 3, 2012: 3, 2013: 2,
    2014: 2, 2015: 2, 2016: 2, 2017: 2, 2018: 2,
    2019: 1, 2020: 2, 2021: 2, 2022: 1, 2023: 1,
    2024: 1,
}

# FTC/DOJ antitrust actions against major platforms
REGULATORY_ACTIONS = {
    2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0,
    2009: 0, 2010: 1, 2011: 1, 2012: 0, 2013: 0,
    2014: 0, 2015: 0, 2016: 0, 2017: 0, 2018: 1,
    2019: 1, 2020: 4, 2021: 3, 2022: 4, 2023: 5,
    2024: 4,
}

SERIES = [
    {
        "series_id": "search_hhi",
        "label": "Search Market HHI",
        "type": "stress",
        "unit": "index",
        "color": "#e05252",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "ecommerce_hhi",
        "label": "E-Commerce Market HHI",
        "type": "stress",
        "unit": "index",
        "color": "#e0a050",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "social_hhi",
        "label": "Social Media Market HHI",
        "type": "stress",
        "unit": "index",
        "color": "#c0392b",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
    {
        "series_id": "top4_revenue_share",
        "label": "Top 4 Platform Ad Revenue Share (%)",
        "type": "stress",
        "unit": "percent",
        "color": "#8e44ad",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
    {
        "series_id": "new_platform_entrants",
        "label": "Significant New Platform Entrants (count)",
        "type": "counterweight",
        "unit": "count",
        "color": "#52a8e0",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "regulatory_actions",
        "label": "FTC/DOJ Antitrust Actions (count)",
        "type": "counterweight",
        "unit": "count",
        "color": "#5db85d",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
]


class PlatformConcentrationFetcher(BaseFetcher):
    thread_name = "platform_concentration"

    def fetch(self) -> dict:
        return {
            "search_hhi": SEARCH_HHI,
            "social_hhi": SOCIAL_HHI,
            "ecommerce_hhi": ECOMMERCE_HHI,
            "top4_revenue_share": TOP4_REVENUE_SHARE,
            "new_platform_entrants": NEW_PLATFORM_ENTRANTS,
            "regulatory_actions": REGULATORY_ACTIONS,
        }

    def transform(self, raw: dict) -> dict:
        observations = []

        source_map = {
            "search_hhi": "StatCounter/FTC derived HHI 2024",
            "social_hhi": "eMarketer/FTC derived HHI 2024",
            "ecommerce_hhi": "eMarketer/FTC derived HHI 2024",
            "top4_revenue_share": "eMarketer public summaries 2024",
            "new_platform_entrants": "FTC merger data + public records 2024",
            "regulatory_actions": "FTC/DOJ antitrust case records 2024",
        }

        for series_id, year_data in raw.items():
            for year, value in year_data.items():
                observations.append({
                    "date": f"{year}-01-01",
                    "series_id": series_id,
                    "value": float(value),
                    "is_projection": False,
                    "vintage": "2026-06-05",
                    "source_version": source_map[series_id],
                })

        return {
            "meta": {
                "thread": "platform_concentration",
                "label": "Platform Concentration",
                "last_updated": "2026-06-05",
                "update_frequency": "annual",
                "next_expected_update": "2027-01",
                "source": "StatCounter + FTC/DOJ filings + eMarketer public data",
                "theory_ref": "Elite capture of information infrastructure — platform monopoly as extraction concentration proxy; regulatory capture signal",
            },
            "series": SERIES,
            "observations": sorted(observations, key=lambda x: (x["date"], x["series_id"])),
        }

    def validate_anomalies(self, data: dict) -> list[str]:
        warnings = []
        latest = {}
        for obs in data["observations"]:
            sid = obs["series_id"]
            year = obs["date"][:4]
            if sid not in latest or year > latest[sid][0]:
                latest[sid] = (year, obs["value"])

        for hhi_series in ["search_hhi", "ecommerce_hhi", "social_hhi"]:
            if hhi_series in latest:
                val = latest[hhi_series][1]
                if val > 2500:
                    warnings.append(
                        f"{hhi_series} at {val} — highly concentrated per DOJ guidelines (>2500)"
                    )
        return warnings


if __name__ == "__main__":
    PlatformConcentrationFetcher().run()
