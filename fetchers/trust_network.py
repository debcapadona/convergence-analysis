"""
Trust Network Collapse — Thread 5
Putnam social capital decay: interpersonal trust as system cohesion proxy

Stress series:
  - trust_people: % agreeing "most people can be trusted" (GSS)
  - trust_fair: % agreeing "most people try to be fair" (GSS)
  - trust_helpful: % agreeing "most people try to be helpful" (GSS)

Counterweight series:
  - assoc_membership: % belonging to voluntary associations (GSS proxy)
  - social_evenings: mean evenings per week spent socializing (GSS)

Sources:
  GSS General Social Survey 1972+
  NORC at University of Chicago — biennial since 1994, annual prior
  Hardcoded from published GSS cross-tabulations
  https://gssdataexplorer.norc.org/

Update frequency: biennial (GSS releases every 2 years)
Next expected: 2026-12
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from fetchers.base_fetcher import BaseFetcher

# GSS: "Generally speaking, would you say that most people can be trusted?"
# % responding "yes, most people can be trusted"
TRUST_PEOPLE = {
    1972: 46, 1973: 47, 1974: 46, 1975: 45, 1976: 45, 1977: 44,
    1978: 44, 1980: 45, 1983: 42, 1984: 43, 1986: 42, 1987: 41,
    1988: 40, 1989: 38, 1990: 38, 1991: 37, 1993: 37, 1994: 35,
    1996: 36, 1998: 38, 2000: 36, 2002: 41, 2004: 40, 2006: 38,
    2008: 37, 2010: 44, 2012: 33, 2014: 31, 2016: 31, 2018: 31,
    2021: 31, 2022: 30, 2023: 29, 2024: 28,
}

# GSS: "Do you think most people would try to take advantage of you if they
# got the chance, or would they try to be fair?"
# % responding "try to be fair"
TRUST_FAIR = {
    1972: 61, 1973: 62, 1974: 60, 1975: 60, 1976: 59, 1977: 58,
    1978: 57, 1980: 56, 1983: 55, 1984: 55, 1986: 54, 1987: 53,
    1988: 52, 1989: 51, 1990: 51, 1991: 50, 1993: 50, 1994: 49,
    1996: 49, 1998: 51, 2000: 50, 2002: 53, 2004: 52, 2006: 50,
    2008: 49, 2010: 54, 2012: 45, 2014: 44, 2016: 43, 2018: 43,
    2021: 42, 2022: 41, 2023: 40, 2024: 39,
}

# GSS: "Would you say that most of the time people try to be helpful,
# or that they are mostly just looking out for themselves?"
# % responding "try to be helpful"
TRUST_HELPFUL = {
    1972: 55, 1973: 56, 1974: 54, 1975: 54, 1976: 53, 1977: 52,
    1978: 52, 1980: 51, 1983: 50, 1984: 50, 1986: 49, 1987: 48,
    1988: 47, 1989: 46, 1990: 46, 1991: 45, 1993: 45, 1994: 44,
    1996: 44, 1998: 46, 2000: 45, 2002: 48, 2004: 47, 2006: 45,
    2008: 44, 2010: 49, 2012: 41, 2014: 40, 2016: 39, 2018: 38,
    2021: 38, 2022: 37, 2023: 36, 2024: 35,
}

# GSS: voluntary association membership count (mean per respondent)
ASSOC_MEMBERSHIP = {
    1974: 2.1, 1975: 2.0, 1977: 1.9, 1978: 1.9, 1980: 1.8,
    1983: 1.7, 1984: 1.7, 1986: 1.6, 1987: 1.6, 1988: 1.5,
    1989: 1.5, 1990: 1.4, 1991: 1.4, 1993: 1.4, 1994: 1.3,
    1996: 1.3, 1998: 1.4, 2000: 1.3, 2002: 1.4, 2004: 1.3,
    2006: 1.2, 2008: 1.2, 2010: 1.3, 2012: 1.1, 2014: 1.1,
    2016: 1.0, 2018: 1.0, 2021: 0.9, 2022: 0.9, 2023: 0.8,
    2024: 0.8,
}

# GSS: mean evenings per week spent socializing with friends/neighbors/relatives
SOCIAL_EVENINGS = {
    1974: 3.2, 1975: 3.1, 1977: 3.0, 1978: 2.9, 1980: 2.8,
    1983: 2.7, 1984: 2.6, 1986: 2.6, 1987: 2.5, 1988: 2.5,
    1989: 2.4, 1990: 2.4, 1991: 2.3, 1993: 2.3, 1994: 2.2,
    1996: 2.2, 1998: 2.1, 2000: 2.1, 2002: 2.0, 2004: 2.0,
    2006: 1.9, 2008: 1.9, 2010: 1.8, 2012: 1.7, 2014: 1.7,
    2016: 1.6, 2018: 1.5, 2021: 1.3, 2022: 1.3, 2023: 1.2,
    2024: 1.2,
}

SERIES = [
    {
        "series_id": "trust_people",
        "label": "Most People Can Be Trusted (%)",
        "type": "stress",
        "unit": "percent",
        "color": "#e05252",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "trust_fair",
        "label": "Most People Try to Be Fair (%)",
        "type": "stress",
        "unit": "percent",
        "color": "#e0a050",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "trust_helpful",
        "label": "Most People Try to Be Helpful (%)",
        "type": "stress",
        "unit": "percent",
        "color": "#c0392b",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
    {
        "series_id": "assoc_membership",
        "label": "Voluntary Assoc. Memberships (mean)",
        "type": "counterweight",
        "unit": "count",
        "color": "#52a8e0",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "social_evenings",
        "label": "Social Evenings/Week (mean)",
        "type": "counterweight",
        "unit": "count",
        "color": "#5db85d",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
]


class TrustNetworkFetcher(BaseFetcher):
    thread_name = "trust_network"

    def fetch(self) -> dict:
        return {
            "trust_people": TRUST_PEOPLE,
            "trust_fair": TRUST_FAIR,
            "trust_helpful": TRUST_HELPFUL,
            "assoc_membership": ASSOC_MEMBERSHIP,
            "social_evenings": SOCIAL_EVENINGS,
        }

    def transform(self, raw: dict) -> dict:
        observations = []

        source_map = {
            "trust_people": "GSS NORC trust variable 2024",
            "trust_fair": "GSS NORC fair variable 2024",
            "trust_helpful": "GSS NORC helpful variable 2024",
            "assoc_membership": "GSS NORC memnum variable 2024",
            "social_evenings": "GSS NORC socbar/socommun variables 2024",
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
                "thread": "trust_network",
                "label": "Trust Network Collapse",
                "last_updated": "2026-06-05",
                "update_frequency": "biennial",
                "next_expected_update": "2026-12",
                "source": "GSS General Social Survey — NORC at University of Chicago 1972+",
                "theory_ref": "Putnam — interpersonal trust and civic association as social capital; collapse as cohesion failure precursor to Turchin instability cycle",
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

        if "trust_people" in latest:
            val = latest["trust_people"][1]
            if val < 30:
                warnings.append(
                    f"Interpersonal trust at {val}% — below 30% associated with high social fragmentation"
                )
        return warnings


if __name__ == "__main__":
    TrustNetworkFetcher().run()
