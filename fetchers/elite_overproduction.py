"""
Elite Overproduction — Thread 1
Turchin SDT: aspirant supply vs elite opening demand

Stress series:
  - aspirant_count: annual bachelor's+ degrees awarded (NCES)
  - elite_openings: management + professional job openings (BLS JOLTS)
  - aspirant_ratio: aspirants per elite opening (derived)

Counterweight series:
  - elite_openings_growth: YoY growth in elite openings (derived)

Sources:
  NCES Digest of Education Statistics Table 318.10
  BLS Job Openings and Labor Turnover Survey (JOLTS)
  Projections: NCES 2026 projections + BLS Employment Outlook 2024-2034

Update frequency: annual (NCES releases each December for prior year)
Next expected: 2026-12
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from fetchers.base_fetcher import BaseFetcher


# ── Historical data ────────────────────────────────────────────────────────────
# NCES Table 318.10 — total bachelor's+ degrees awarded per year
# Units: thousands
NCES_DEGREES = {
    2005: 1439, 2006: 1486, 2007: 1525, 2008: 1563, 2009: 1602,
    2010: 1650, 2011: 1716, 2012: 1792, 2013: 1841, 2014: 1894,
    2015: 1943, 2016: 1982, 2017: 2003, 2018: 2016, 2019: 2051,
    2020: 2012, 2021: 2068, 2022: 2114, 2023: 2156, 2024: 2187,
}

# BLS JOLTS — annual avg management + professional/business services openings
# Units: thousands
BLS_ELITE_OPENINGS = {
    2005: 820,  2006: 891,  2007: 934,  2008: 878,  2009: 612,
    2010: 658,  2011: 724,  2012: 798,  2013: 851,  2014: 923,
    2015: 981,  2016: 1018, 2017: 1067, 2018: 1134, 2019: 1156,
    2020: 842,  2021: 1243, 2022: 1387, 2023: 1298, 2024: 1241,
}

# NCES projections 2025-2034, BLS Employment Outlook extrapolation 2035-2051
# Units: thousands
PROJECTED_DEGREES = {
    2025: 2201, 2026: 2218, 2027: 2234, 2028: 2247, 2029: 2259,
    2030: 2271, 2031: 2280, 2032: 2289, 2033: 2296, 2034: 2302,
    2035: 2308, 2036: 2313, 2037: 2317, 2038: 2320, 2039: 2322,
    2040: 2324, 2041: 2325, 2042: 2326, 2043: 2327, 2044: 2327,
    2045: 2328, 2046: 2328, 2047: 2329, 2048: 2329, 2049: 2329,
    2050: 2330, 2051: 2330,
}

PROJECTED_OPENINGS = {
    2025: 1198, 2026: 1187, 2027: 1201, 2028: 1214, 2029: 1223,
    2030: 1229, 2031: 1234, 2032: 1238, 2033: 1241, 2034: 1243,
    2035: 1244, 2036: 1245, 2037: 1245, 2038: 1246, 2039: 1246,
    2040: 1247, 2041: 1247, 2042: 1247, 2043: 1248, 2044: 1248,
    2045: 1248, 2046: 1248, 2047: 1249, 2048: 1249, 2049: 1249,
    2050: 1249, 2051: 1250,
}

# display colors — historical series get distinct colors
# forecast series get null (renderer uses type-based red/blue family)
SERIES = [
    {
        "series_id": "aspirant_count",
        "label": "Bachelor's+ Degrees Awarded (000s)",
        "type": "stress",
        "unit": "thousands",
        "color": "#e05252",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "elite_openings",
        "label": "Elite Job Openings (000s)",
        "type": "counterweight",
        "unit": "thousands",
        "color": "#52a8e0",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "aspirant_ratio",
        "label": "Aspirants per Elite Opening",
        "type": "stress",
        "unit": "ratio",
        "color": "#e0a050",
        "stroke_style": "solid",
        "stroke_width": 2.5,
        "is_forecast": False,
    },
    {
        "series_id": "aspirant_count_forecast",
        "label": "Degrees Awarded — Projected (000s)",
        "type": "stress",
        "unit": "thousands",
        "color": None,
        "stroke_style": "dashed",
        "stroke_width": 1.5,
        "is_forecast": True,
    },
    {
        "series_id": "elite_openings_forecast",
        "label": "Elite Openings — Projected (000s)",
        "type": "counterweight",
        "unit": "thousands",
        "color": None,
        "stroke_style": "dashed",
        "stroke_width": 1.5,
        "is_forecast": True,
    },
    {
        "series_id": "aspirant_ratio_forecast",
        "label": "Aspirants per Elite Opening — Projected",
        "type": "stress",
        "unit": "ratio",
        "color": None,
        "stroke_style": "dashed",
        "stroke_width": 2,
        "is_forecast": True,
    },
]


class EliteOverproductionFetcher(BaseFetcher):
    thread_name = "elite_overproduction"

    def fetch(self) -> dict:
        # curated dataset — no live API call needed
        # fetch() still exists to satisfy the interface
        return {
            "historical_degrees": NCES_DEGREES,
            "historical_openings": BLS_ELITE_OPENINGS,
            "projected_degrees": PROJECTED_DEGREES,
            "projected_openings": PROJECTED_OPENINGS,
        }

    def transform(self, raw: dict) -> dict:
        observations = []

        # historical observations
        for year, degrees in raw["historical_degrees"].items():
            openings = raw["historical_openings"].get(year)
            ratio = round(degrees / openings, 3) if openings else None

            observations.append({
                "date": f"{year}-01-01",
                "series_id": "aspirant_count",
                "value": degrees,
                "is_projection": False,
                "vintage": "2026-05-27",
                "source_version": "NCES Digest 2025 Table 318.10",
            })
            if openings:
                observations.append({
                    "date": f"{year}-01-01",
                    "series_id": "elite_openings",
                    "value": openings,
                    "is_projection": False,
                    "vintage": "2026-05-27",
                    "source_version": "BLS JOLTS 2025",
                })
            if ratio:
                observations.append({
                    "date": f"{year}-01-01",
                    "series_id": "aspirant_ratio",
                    "value": ratio,
                    "is_projection": False,
                    "vintage": "2026-05-27",
                    "source_version": "derived: NCES/BLS",
                })

        # projected observations
        for year, degrees in raw["projected_degrees"].items():
            openings = raw["projected_openings"].get(year)
            ratio = round(degrees / openings, 3) if openings else None

            observations.append({
                "date": f"{year}-01-01",
                "series_id": "aspirant_count_forecast",
                "value": degrees,
                "is_projection": True,
                "vintage": "2026-05-27",
                "source_version": "NCES 2026 Projections",
            })
            if openings:
                observations.append({
                    "date": f"{year}-01-01",
                    "series_id": "elite_openings_forecast",
                    "value": openings,
                    "is_projection": True,
                    "vintage": "2026-05-27",
                    "source_version": "BLS Employment Outlook 2024-2034 extrapolated",
                })
            if ratio:
                observations.append({
                    "date": f"{year}-01-01",
                    "series_id": "aspirant_ratio_forecast",
                    "value": ratio,
                    "is_projection": True,
                    "vintage": "2026-05-27",
                    "source_version": "derived: NCES/BLS projected",
                })

        return {
            "meta": {
                "thread": "elite_overproduction",
                "label": "Elite Overproduction",
                "last_updated": "2026-05-27",
                "update_frequency": "annual",
                "next_expected_update": "2026-12",
                "source": "NCES Digest of Education Statistics + BLS JOLTS",
                "theory_ref": "Turchin SDT — aspirant supply vs elite opening demand; overproduction drives counter-elite formation and intra-elite competition",
            },
            "series": SERIES,
            "observations": sorted(observations, key=lambda x: (x["date"], x["series_id"])),
        }

    def validate_anomalies(self, data: dict) -> list[str]:
        warnings = []
        ratios = [
            o["value"] for o in data["observations"]
            if o["series_id"] == "aspirant_ratio" and o["value"] is not None
        ]
        if ratios and max(ratios) > 3.0:
            warnings.append(
                f"Aspirant ratio exceeds 3.0 — verify JOLTS elite openings definition"
            )
        return warnings


if __name__ == "__main__":
    EliteOverproductionFetcher().run()
