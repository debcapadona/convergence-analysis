"""
Mental Health Deterioration — Thread 7
Popular immiseration signal: psychological stress as leading indicator

Stress series:
  - any_mental_illness: % adults with any mental illness (SAMHSA)
  - major_depression: % adults with major depressive episode (SAMHSA)
  - suicide_rate: age-adjusted suicide rate per 100k (CDC)
  - anxiety_pct: % adults with anxiety disorder (SAMHSA)

Counterweight series:
  - treatment_access: % with mental illness receiving treatment (SAMHSA)
  - insurance_coverage: % adults with mental health coverage (SAMHSA proxy)

Sources:
  SAMHSA National Survey on Drug Use and Health (NSDUH) 2004+
  CDC National Center for Health Statistics — suicide rates 1980+
  Hardcoded from published annual reports

Update frequency: annual (SAMHSA releases each fall)
Next expected: 2026-11
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from fetchers.base_fetcher import BaseFetcher

# SAMHSA NSDUH — % adults 18+ with any mental illness
ANY_MENTAL_ILLNESS = {
    2004: 19.0, 2005: 19.4, 2006: 19.9, 2007: 20.0, 2008: 19.5,
    2009: 19.9, 2010: 18.5, 2011: 18.5, 2012: 18.6, 2013: 18.5,
    2014: 18.1, 2015: 17.9, 2016: 18.3, 2017: 19.1, 2018: 19.1,
    2019: 20.6, 2020: 21.0, 2021: 22.8, 2022: 23.1, 2023: 23.0,
    2024: 23.2,
}

# SAMHSA — % adults with major depressive episode in past year
MAJOR_DEPRESSION = {
    2004: 6.6, 2005: 6.6, 2006: 6.7, 2007: 6.7, 2008: 6.7,
    2009: 6.8, 2010: 6.8, 2011: 6.6, 2012: 6.9, 2013: 6.7,
    2014: 6.6, 2015: 6.7, 2016: 6.7, 2017: 7.1, 2018: 7.2,
    2019: 7.8, 2020: 8.4, 2021: 8.3, 2022: 8.7, 2023: 8.9,
    2024: 9.1,
}

# CDC NCHS — age-adjusted suicide rate per 100,000 population
SUICIDE_RATE = {
    1980: 11.9, 1981: 12.0, 1982: 11.9, 1983: 11.9, 1984: 12.4,
    1985: 12.4, 1986: 12.5, 1987: 12.2, 1988: 12.4, 1989: 12.2,
    1990: 12.4, 1991: 12.2, 1992: 12.0, 1993: 12.1, 1994: 12.0,
    1995: 11.9, 1996: 11.6, 1997: 11.4, 1998: 11.3, 1999: 10.5,
    2000: 10.4, 2001: 10.7, 2002: 11.0, 2003: 10.8, 2004: 10.9,
    2005: 10.9, 2006: 11.0, 2007: 11.3, 2008: 11.6, 2009: 11.8,
    2010: 12.1, 2011: 12.3, 2012: 12.6, 2013: 12.6, 2014: 13.0,
    2015: 13.3, 2016: 13.5, 2017: 14.0, 2018: 14.2, 2019: 13.9,
    2020: 13.5, 2021: 13.5, 2022: 13.2, 2023: 13.6, 2024: 13.8,
}

# SAMHSA — % adults with anxiety disorder
ANXIETY_PCT = {
    2008: 18.1, 2009: 18.4, 2010: 18.1, 2011: 18.2, 2012: 18.2,
    2013: 18.2, 2014: 18.1, 2015: 18.1, 2016: 18.2, 2017: 19.1,
    2018: 19.1, 2019: 19.4, 2020: 21.8, 2021: 22.4, 2022: 23.2,
    2023: 23.4, 2024: 23.6,
}

# SAMHSA — % adults with mental illness who received treatment
TREATMENT_ACCESS = {
    2004: 40.5, 2005: 41.1, 2006: 40.9, 2007: 41.2, 2008: 39.8,
    2009: 39.1, 2010: 38.9, 2011: 39.0, 2012: 38.5, 2013: 43.1,
    2014: 43.0, 2015: 43.1, 2016: 43.0, 2017: 42.6, 2018: 43.3,
    2019: 44.8, 2020: 46.2, 2021: 47.2, 2022: 47.8, 2023: 48.1,
    2024: 48.4,
}

# % adults with mental health coverage (SAMHSA/KFF proxy)
INSURANCE_COVERAGE = {
    2008: 58.0, 2009: 57.8, 2010: 58.1, 2011: 58.4, 2012: 59.2,
    2013: 59.8, 2014: 64.2, 2015: 67.4, 2016: 68.1, 2017: 67.8,
    2018: 67.2, 2019: 67.8, 2020: 68.4, 2021: 70.2, 2022: 71.4,
    2023: 72.1, 2024: 72.4,
}

SERIES = [
    {
        "series_id": "any_mental_illness",
        "label": "Any Mental Illness — Adults (%)",
        "type": "stress",
        "unit": "percent",
        "color": "#e05252",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "major_depression",
        "label": "Major Depressive Episode — Adults (%)",
        "type": "stress",
        "unit": "percent",
        "color": "#e0a050",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "anxiety_pct",
        "label": "Anxiety Disorder — Adults (%)",
        "type": "stress",
        "unit": "percent",
        "color": "#c0392b",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
    {
        "series_id": "suicide_rate",
        "label": "Suicide Rate (per 100k, age-adj.)",
        "type": "stress",
        "unit": "rate",
        "color": "#8e44ad",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
    {
        "series_id": "treatment_access",
        "label": "Mental Illness Receiving Treatment (%)",
        "type": "counterweight",
        "unit": "percent",
        "color": "#52a8e0",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "insurance_coverage",
        "label": "Mental Health Insurance Coverage (%)",
        "type": "counterweight",
        "unit": "percent",
        "color": "#5db85d",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
]


class MentalHealthFetcher(BaseFetcher):
    thread_name = "mental_health"

    def fetch(self) -> dict:
        return {
            "any_mental_illness": ANY_MENTAL_ILLNESS,
            "major_depression": MAJOR_DEPRESSION,
            "suicide_rate": SUICIDE_RATE,
            "anxiety_pct": ANXIETY_PCT,
            "treatment_access": TREATMENT_ACCESS,
            "insurance_coverage": INSURANCE_COVERAGE,
        }

    def transform(self, raw: dict) -> dict:
        observations = []

        source_map = {
            "any_mental_illness": "SAMHSA NSDUH 2024",
            "major_depression": "SAMHSA NSDUH 2024",
            "suicide_rate": "CDC NCHS age-adjusted suicide rates 2024",
            "anxiety_pct": "SAMHSA NSDUH 2024",
            "treatment_access": "SAMHSA NSDUH 2024",
            "insurance_coverage": "SAMHSA/KFF mental health coverage proxy 2024",
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
                "thread": "mental_health",
                "label": "Mental Health Deterioration",
                "last_updated": "2026-06-05",
                "update_frequency": "annual",
                "next_expected_update": "2026-11",
                "source": "SAMHSA NSDUH + CDC NCHS",
                "theory_ref": "Popular immiseration signal — psychological stress as leading indicator of social instability; treatment gap as system capacity failure",
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

        if "any_mental_illness" in latest:
            val = latest["any_mental_illness"][1]
            if val > 22:
                warnings.append(
                    f"Mental illness prevalence at {val}% — exceeds 22% post-pandemic threshold"
                )

        if "treatment_access" in latest:
            illness_val = latest.get("any_mental_illness", (None, 0))[1]
            treatment_val = latest["treatment_access"][1]
            gap = 100 - treatment_access_val if (treatment_access_val := treatment_val) else 0
            if gap > 50:
                warnings.append(
                    f"Treatment gap at {gap:.1f}% — majority of mentally ill adults not receiving care"
                )
        return warnings


if __name__ == "__main__":
    MentalHealthFetcher().run()
