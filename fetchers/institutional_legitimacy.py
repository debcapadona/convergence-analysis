"""
Institutional Legitimacy Erosion — Thread 4
Goldstone: declining trust in state institutions as precursor to political crisis

Stress series:
  - trust_congress: % expressing confidence in Congress (Gallup)
  - trust_presidency: % expressing confidence in the Presidency (Gallup)
  - trust_supreme_court: % expressing confidence in Supreme Court (Gallup)
  - trust_banks: % expressing confidence in banks (Gallup)
  - trust_media: % expressing confidence in newspapers + TV news avg (Gallup)

Counterweight series:
  - trust_military: % expressing confidence in military (Gallup)
  - trust_smallbiz: % expressing confidence in small business (Gallup)

Sources:
  Gallup Confidence in Institutions Survey 1973+
  https://news.gallup.com/poll/1597/confidence-institutions.aspx
  Hardcoded from published annual surveys — no public API

Update frequency: annual (Gallup releases each June/July)
Next expected: 2026-07
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from fetchers.base_fetcher import BaseFetcher

# Gallup Confidence in Institutions — % saying "a great deal" or "quite a lot"
# Source: Gallup annual survey, compiled from published tables

TRUST_CONGRESS = {
    1973: 42, 1974: 40, 1975: 40, 1976: 42, 1977: 40, 1978: 35,
    1979: 34, 1980: 34, 1981: 29, 1982: 26, 1983: 28, 1984: 28,
    1985: 30, 1986: 28, 1987: 27, 1988: 26, 1989: 32, 1990: 24,
    1991: 18, 1992: 18, 1993: 19, 1994: 18, 1995: 21, 1996: 22,
    1997: 22, 1998: 28, 1999: 26, 2000: 26, 2001: 26, 2002: 29,
    2003: 27, 2004: 30, 2005: 22, 2006: 19, 2007: 14, 2008: 12,
    2009: 17, 2010: 11, 2011: 12, 2012: 13, 2013: 10, 2014: 7,
    2015: 8,  2016: 9,  2017: 12, 2018: 11, 2019: 11, 2020: 13,
    2021: 12, 2022: 7,  2023: 8,  2024: 8,
}

TRUST_PRESIDENCY = {
    1973: 52, 1974: 44, 1975: 52, 1976: 52, 1977: 52, 1978: 42,
    1979: 42, 1980: 42, 1981: 50, 1982: 45, 1983: 40, 1984: 45,
    1985: 49, 1986: 43, 1987: 40, 1988: 41, 1989: 45, 1990: 45,
    1991: 50, 1992: 43, 1993: 43, 1994: 42, 1995: 45, 1996: 44,
    1997: 49, 1998: 49, 1999: 51, 2000: 47, 2001: 48, 2002: 55,
    2003: 52, 2004: 52, 2005: 44, 2006: 33, 2007: 25, 2008: 26,
    2009: 36, 2010: 36, 2011: 35, 2012: 37, 2013: 36, 2014: 29,
    2015: 33, 2016: 36, 2017: 32, 2018: 37, 2019: 38, 2020: 39,
    2021: 38, 2022: 23, 2023: 26, 2024: 28,
}

TRUST_SUPREME_COURT = {
    1973: 44, 1974: 40, 1975: 49, 1976: 49, 1977: 46, 1978: 42,
    1979: 45, 1980: 47, 1981: 46, 1982: 45, 1983: 42, 1984: 42,
    1985: 44, 1986: 41, 1987: 45, 1988: 42, 1989: 46, 1990: 47,
    1991: 39, 1992: 40, 1993: 44, 1994: 44, 1995: 44, 1996: 45,
    1997: 50, 1998: 50, 1999: 49, 2000: 47, 2001: 50, 2002: 50,
    2003: 47, 2004: 46, 2005: 41, 2006: 40, 2007: 34, 2008: 32,
    2009: 39, 2010: 36, 2011: 37, 2012: 37, 2013: 34, 2014: 30,
    2015: 32, 2016: 36, 2017: 40, 2018: 37, 2019: 38, 2020: 40,
    2021: 36, 2022: 25, 2023: 27, 2024: 29,
}

TRUST_BANKS = {
    1979: 60, 1980: 60, 1981: 46, 1982: 45, 1983: 51, 1984: 51,
    1985: 51, 1986: 49, 1987: 51, 1988: 49, 1989: 42, 1990: 36,
    1991: 30, 1992: 27, 1993: 29, 1994: 35, 1995: 43, 1996: 44,
    1997: 41, 1998: 40, 1999: 43, 2000: 46, 2001: 46, 2002: 47,
    2003: 50, 2004: 53, 2005: 49, 2006: 49, 2007: 41, 2008: 32,
    2009: 22, 2010: 18, 2011: 23, 2012: 21, 2013: 26, 2014: 26,
    2015: 28, 2016: 27, 2017: 32, 2018: 30, 2019: 30, 2020: 38,
    2021: 33, 2022: 27, 2023: 26, 2024: 27,
}

TRUST_MEDIA = {
    1973: 39, 1974: 38, 1975: 39, 1976: 40, 1977: 38, 1978: 36,
    1979: 38, 1980: 37, 1981: 35, 1982: 35, 1983: 38, 1984: 34,
    1985: 35, 1986: 37, 1987: 31, 1988: 28, 1989: 31, 1990: 30,
    1991: 32, 1992: 26, 1993: 27, 1994: 26, 1995: 30, 1996: 27,
    1997: 28, 1998: 29, 1999: 28, 2000: 27, 2001: 29, 2002: 29,
    2003: 30, 2004: 30, 2005: 28, 2006: 26, 2007: 22, 2008: 24,
    2009: 25, 2010: 22, 2011: 19, 2012: 21, 2013: 23, 2014: 22,
    2015: 21, 2016: 20, 2017: 21, 2018: 23, 2019: 23, 2020: 24,
    2021: 21, 2022: 16, 2023: 17, 2024: 18,
}

TRUST_MILITARY = {
    1973: 58, 1974: 58, 1975: 58, 1976: 58, 1977: 57, 1978: 57,
    1979: 54, 1980: 52, 1981: 50, 1982: 53, 1983: 53, 1984: 58,
    1985: 61, 1986: 63, 1987: 61, 1988: 58, 1989: 63, 1990: 68,
    1991: 69, 1992: 68, 1993: 67, 1994: 64, 1995: 64, 1996: 66,
    1997: 67, 1998: 65, 1999: 68, 2000: 64, 2001: 66, 2002: 79,
    2003: 76, 2004: 75, 2005: 74, 2006: 73, 2007: 69, 2008: 71,
    2009: 74, 2010: 76, 2011: 78, 2012: 75, 2013: 76, 2014: 74,
    2015: 72, 2016: 73, 2017: 72, 2018: 74, 2019: 73, 2020: 72,
    2021: 69, 2022: 64, 2023: 60, 2024: 58,
}

TRUST_SMALLBIZ = {
    1997: 63, 1998: 62, 1999: 63, 2000: 59, 2001: 60, 2002: 61,
    2003: 63, 2004: 64, 2005: 62, 2006: 59, 2007: 59, 2008: 57,
    2009: 67, 2010: 66, 2011: 64, 2012: 63, 2013: 65, 2014: 62,
    2015: 67, 2016: 68, 2017: 70, 2018: 67, 2019: 68, 2020: 75,
    2021: 70, 2022: 68, 2023: 65, 2024: 63,
}

SERIES = [
    {
        "series_id": "trust_congress",
        "label": "Confidence: Congress (%)",
        "type": "stress",
        "unit": "percent",
        "color": "#e05252",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "trust_presidency",
        "label": "Confidence: Presidency (%)",
        "type": "stress",
        "unit": "percent",
        "color": "#e0a050",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "trust_supreme_court",
        "label": "Confidence: Supreme Court (%)",
        "type": "stress",
        "unit": "percent",
        "color": "#c0392b",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
    {
        "series_id": "trust_banks",
        "label": "Confidence: Banks (%)",
        "type": "stress",
        "unit": "percent",
        "color": "#d35400",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
    {
        "series_id": "trust_media",
        "label": "Confidence: Media (%)",
        "type": "stress",
        "unit": "percent",
        "color": "#8e44ad",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
    {
        "series_id": "trust_military",
        "label": "Confidence: Military (%)",
        "type": "counterweight",
        "unit": "percent",
        "color": "#52a8e0",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "trust_smallbiz",
        "label": "Confidence: Small Business (%)",
        "type": "counterweight",
        "unit": "percent",
        "color": "#5db85d",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
]


class InstitutionalLegitimacyFetcher(BaseFetcher):
    thread_name = "institutional_legitimacy"

    def fetch(self) -> dict:
        return {
            "trust_congress": TRUST_CONGRESS,
            "trust_presidency": TRUST_PRESIDENCY,
            "trust_supreme_court": TRUST_SUPREME_COURT,
            "trust_banks": TRUST_BANKS,
            "trust_media": TRUST_MEDIA,
            "trust_military": TRUST_MILITARY,
            "trust_smallbiz": TRUST_SMALLBIZ,
        }

    def transform(self, raw: dict) -> dict:
        observations = []

        for series_id, year_data in raw.items():
            for year, value in year_data.items():
                observations.append({
                    "date": f"{year}-01-01",
                    "series_id": series_id,
                    "value": float(value),
                    "is_projection": False,
                    "vintage": "2026-06-05",
                    "source_version": "Gallup Confidence in Institutions 2024",
                })

        return {
            "meta": {
                "thread": "institutional_legitimacy",
                "label": "Institutional Legitimacy Erosion",
                "last_updated": "2026-06-05",
                "update_frequency": "annual",
                "next_expected_update": "2026-07",
                "source": "Gallup Confidence in Institutions Survey 1973+",
                "theory_ref": "Goldstone — declining trust in state institutions as precursor to political crisis; legitimacy erosion as governance fragility signal",
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

        for sid, (year, value) in latest.items():
            if sid.startswith("trust_") and sid not in ("trust_military", "trust_smallbiz"):
                if value < 15:
                    warnings.append(
                        f"{sid} confidence at {value}% — below 15% historical crisis threshold"
                    )
        return warnings


if __name__ == "__main__":
    InstitutionalLegitimacyFetcher().run()
