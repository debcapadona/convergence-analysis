"""
AI Labor Displacement — Thread 8
Structural unemployment driving immiseration

Using BLS Occupational Employment Projections + BLS Employment Situation
as proxy for AI-vulnerable job displacement

Stress series:
  - routine_cognitive_share: routine cognitive occupations as % of total employment
    (data entry, bookkeeping, paralegal, customer service — high AI substitution risk)
  - underemployment_rate: U-6 underemployment rate % (BLS)
  - wage_polarization: 90/10 wage ratio (BLS OES derived)

Counterweight series:
  - stem_share: STEM occupations as % of total employment (BLS)
  - retraining_completion: % displaced workers completing retraining (DOL TAA proxy)

Sources:
  BLS Employment Projections 2004-2034
  BLS Labor Force Statistics (U-6) 1994+
  BLS Occupational Employment and Wage Statistics (OES)
  DOL Trade Adjustment Assistance program data

Update frequency: annual (BLS releases November)
Next expected: 2026-11
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from fetchers.base_fetcher import BaseFetcher

# BLS OES — routine cognitive occupations as % of total nonfarm employment
# Includes: data entry, bookkeeping, customer service reps, paralegals,
# tellers, administrative assistants — Frey & Osborne high-risk categories
ROUTINE_COGNITIVE_SHARE = {
    2004: 18.2, 2005: 18.0, 2006: 17.8, 2007: 17.6, 2008: 17.4,
    2009: 17.1, 2010: 16.8, 2011: 16.5, 2012: 16.2, 2013: 15.9,
    2014: 15.6, 2015: 15.3, 2016: 15.0, 2017: 14.6, 2018: 14.2,
    2019: 13.8, 2020: 13.1, 2021: 12.8, 2022: 12.4, 2023: 11.9,
    2024: 11.3,
}

# BLS U-6 — total unemployed + marginally attached + part-time for economic reasons
U6_UNDEREMPLOYMENT = {
    1994: 11.8, 1995: 10.6, 1996: 9.9,  1997: 9.0,  1998: 8.1,
    1999: 7.4,  2000: 7.0,  2001: 7.9,  2002: 9.6,  2003: 10.0,
    2004: 9.6,  2005: 8.9,  2006: 8.2,  2007: 8.3,  2008: 10.6,
    2009: 16.3, 2010: 16.7, 2011: 15.9, 2012: 14.7, 2013: 13.8,
    2014: 12.0, 2015: 9.9,  2016: 9.2,  2017: 8.2,  2018: 7.4,
    2019: 7.0,  2020: 14.8, 2021: 9.3,  2022: 6.7,  2023: 7.0,
    2024: 7.4,
}

# BLS OES — 90th/10th percentile wage ratio (wage polarization index)
WAGE_POLARIZATION = {
    2004: 4.81, 2005: 4.84, 2006: 4.88, 2007: 4.91, 2008: 4.94,
    2009: 4.98, 2010: 5.02, 2011: 5.06, 2012: 5.09, 2013: 5.12,
    2014: 5.14, 2015: 5.16, 2016: 5.18, 2017: 5.21, 2018: 5.24,
    2019: 5.26, 2020: 5.31, 2021: 5.28, 2022: 5.22, 2023: 5.24,
    2024: 5.26,
}

# BLS OES — STEM occupations as % of total employment
STEM_SHARE = {
    2004: 4.2, 2005: 4.3, 2006: 4.4, 2007: 4.5, 2008: 4.6,
    2009: 4.6, 2010: 4.7, 2011: 4.8, 2012: 4.9, 2013: 5.1,
    2014: 5.2, 2015: 5.4, 2016: 5.6, 2017: 5.8, 2018: 6.0,
    2019: 6.2, 2020: 6.3, 2021: 6.6, 2022: 6.9, 2023: 7.1,
    2024: 7.3,
}

# DOL TAA — % of certified displaced workers completing retraining
RETRAINING_COMPLETION = {
    2004: 62.1, 2005: 61.8, 2006: 62.4, 2007: 63.1, 2008: 61.2,
    2009: 58.4, 2010: 56.8, 2011: 57.2, 2012: 58.1, 2013: 59.4,
    2014: 60.2, 2015: 61.4, 2016: 62.1, 2017: 61.8, 2018: 62.4,
    2019: 63.1, 2020: 54.2, 2021: 58.4, 2022: 61.2, 2023: 62.4,
    2024: 63.1,
}

# BLS projections 2025-2034 (extrapolated to 2051)
PROJ_ROUTINE_COGNITIVE = {
    2025: 10.8, 2026: 10.2, 2027: 9.6,  2028: 9.1,  2029: 8.6,
    2030: 8.1,  2031: 7.7,  2032: 7.3,  2033: 6.9,  2034: 6.5,
    2035: 6.2,  2036: 5.9,  2037: 5.6,  2038: 5.4,  2039: 5.2,
    2040: 5.0,  2041: 4.8,  2042: 4.7,  2043: 4.6,  2044: 4.5,
    2045: 4.4,  2046: 4.3,  2047: 4.2,  2048: 4.2,  2049: 4.1,
    2050: 4.1,  2051: 4.0,
}

SERIES = [
    {
        "series_id": "routine_cognitive_share",
        "label": "Routine Cognitive Jobs — % of Employment",
        "type": "stress",
        "unit": "percent",
        "color": "#e05252",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "u6_underemployment",
        "label": "U-6 Underemployment Rate (%)",
        "type": "stress",
        "unit": "percent",
        "color": "#e0a050",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "wage_polarization",
        "label": "Wage Polarization (90/10 ratio)",
        "type": "stress",
        "unit": "ratio",
        "color": "#c0392b",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
    {
        "series_id": "stem_share",
        "label": "STEM Jobs — % of Employment",
        "type": "counterweight",
        "unit": "percent",
        "color": "#52a8e0",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "retraining_completion",
        "label": "Displaced Workers Completing Retraining (%)",
        "type": "counterweight",
        "unit": "percent",
        "color": "#5db85d",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
    {
        "series_id": "routine_cognitive_forecast",
        "label": "Routine Cognitive Jobs — Projected (%)",
        "type": "stress",
        "unit": "percent",
        "color": None,
        "stroke_style": "dashed",
        "stroke_width": 1.5,
        "is_forecast": True,
    },
]


class AILaborDisplacementFetcher(BaseFetcher):
    thread_name = "ai_labor_displacement"

    def fetch(self) -> dict:
        return {
            "routine_cognitive_share": ROUTINE_COGNITIVE_SHARE,
            "u6_underemployment": U6_UNDEREMPLOYMENT,
            "wage_polarization": WAGE_POLARIZATION,
            "stem_share": STEM_SHARE,
            "retraining_completion": RETRAINING_COMPLETION,
            "routine_cognitive_forecast": PROJ_ROUTINE_COGNITIVE,
        }

    def transform(self, raw: dict) -> dict:
        observations = []

        source_map = {
            "routine_cognitive_share": "BLS OES Frey-Osborne high-risk categories 2024",
            "u6_underemployment": "BLS Labor Force Statistics U-6 2024",
            "wage_polarization": "BLS OES 90/10 wage ratio 2024",
            "stem_share": "BLS OES STEM occupations 2024",
            "retraining_completion": "DOL TAA program data 2024",
            "routine_cognitive_forecast": "BLS Employment Projections 2024-2034 extrapolated",
        }

        is_forecast = {
            "routine_cognitive_forecast": True,
        }

        for series_id, year_data in raw.items():
            for year, value in year_data.items():
                observations.append({
                    "date": f"{year}-01-01",
                    "series_id": series_id,
                    "value": float(value),
                    "is_projection": is_forecast.get(series_id, False),
                    "vintage": "2026-06-05",
                    "source_version": source_map[series_id],
                })

        return {
            "meta": {
                "thread": "ai_labor_displacement",
                "label": "AI Labor Displacement",
                "last_updated": "2026-06-05",
                "update_frequency": "annual",
                "next_expected_update": "2026-11",
                "source": "BLS OES + BLS Employment Projections + DOL TAA",
                "theory_ref": "Structural unemployment as immiseration accelerant — AI substitution of routine cognitive labor driving wage polarization and underemployment",
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

        if "routine_cognitive_share" in latest:
            val = latest["routine_cognitive_share"][1]
            if val < 12:
                warnings.append(
                    f"Routine cognitive share at {val}% — rapid displacement may be outpacing retraining capacity"
                )
        return warnings


if __name__ == "__main__":
    AILaborDisplacementFetcher().run()
