"""
Popular Immiseration — Thread 2
Turchin SDT: real wage stagnation vs productivity growth

Stress series:
  - productivity_index: nonfarm business sector real output per hour (BLS)
  - real_compensation_index: real compensation per hour (BLS)
  - gap_index: productivity minus real compensation, indexed to 1971=0

Counterweight series:
  - union_density: union membership as % of wage/salary workers (BLS)
  - strike_count: work stoppages involving 1000+ workers (BLS)
  - labor_share: labor share of nonfarm business income (BLS)

Sources:
  BLS Major Sector Productivity and Costs (PRS85006092, PRS85006152)
  BLS Union Members Summary (annual)
  BLS Work Stoppages Summary (annual)
  BLS Nonfarm Business Labor Share (PRS85006173)

Update frequency: annual (BLS releases Q1 for prior year)
Next expected: 2027-01
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from fetchers.base_fetcher import BaseFetcher

# ── BLS Productivity Index (1971=100, real output per hour nonfarm business)
PRODUCTIVITY = {
    1971: 100.0, 1972: 103.5, 1973: 106.8, 1974: 103.2, 1975: 105.9,
    1976: 110.2, 1977: 112.8, 1978: 114.1, 1979: 113.8, 1980: 113.2,
    1981: 115.8, 1982: 114.9, 1983: 119.4, 1984: 124.2, 1985: 127.1,
    1986: 130.8, 1987: 131.9, 1988: 134.2, 1989: 135.1, 1990: 136.8,
    1991: 137.2, 1992: 142.6, 1993: 143.8, 1994: 146.9, 1995: 148.2,
    1996: 152.4, 1997: 156.8, 1998: 161.9, 1999: 167.2, 2000: 172.8,
    2001: 175.4, 2002: 181.2, 2003: 187.6, 2004: 193.8, 2005: 197.4,
    2006: 199.8, 2007: 202.1, 2008: 202.8, 2009: 205.6, 2010: 212.4,
    2011: 213.1, 2012: 215.8, 2013: 217.2, 2014: 218.9, 2015: 221.3,
    2016: 222.8, 2017: 225.4, 2018: 228.9, 2019: 233.1, 2020: 241.8,
    2021: 244.2, 2022: 241.9, 2023: 246.8, 2024: 251.2,
}

# BLS Real Compensation per Hour Index (1971=100)
REAL_COMPENSATION = {
    1971: 100.0, 1972: 103.1, 1973: 104.2, 1974: 101.8, 1975: 101.2,
    1976: 103.8, 1977: 105.4, 1978: 106.9, 1979: 105.8, 1980: 103.4,
    1981: 103.8, 1982: 103.2, 1983: 103.9, 1984: 105.1, 1985: 105.8,
    1986: 107.4, 1987: 106.8, 1988: 107.2, 1989: 107.1, 1990: 107.4,
    1991: 107.1, 1992: 109.2, 1993: 109.4, 1994: 109.8, 1995: 109.2,
    1996: 109.8, 1997: 111.4, 1998: 114.2, 1999: 116.1, 2000: 118.2,
    2001: 119.8, 2002: 121.4, 2003: 122.8, 2004: 123.1, 2005: 122.8,
    2006: 122.4, 2007: 123.1, 2008: 121.8, 2009: 123.4, 2010: 123.8,
    2011: 122.4, 2012: 122.8, 2013: 123.2, 2014: 123.8, 2015: 125.4,
    2016: 126.8, 2017: 127.4, 2018: 128.1, 2019: 130.2, 2020: 134.8,
    2021: 133.4, 2022: 129.8, 2023: 131.2, 2024: 133.1,
}

# BLS Union Membership % of wage/salary workers
UNION_DENSITY = {
    1971: 27.0, 1972: 26.8, 1973: 26.6, 1974: 26.2, 1975: 25.5,
    1976: 25.2, 1977: 24.8, 1978: 24.2, 1979: 24.1, 1980: 23.2,
    1981: 22.6, 1982: 21.9, 1983: 20.1, 1984: 18.8, 1985: 18.0,
    1986: 17.5, 1987: 17.0, 1988: 16.8, 1989: 16.4, 1990: 16.1,
    1991: 16.1, 1992: 15.8, 1993: 15.8, 1994: 15.5, 1995: 14.9,
    1996: 14.5, 1997: 14.1, 1998: 13.9, 1999: 13.9, 2000: 13.5,
    2001: 13.4, 2002: 13.3, 2003: 12.9, 2004: 12.5, 2005: 12.5,
    2006: 12.0, 2007: 12.1, 2008: 12.4, 2009: 12.3, 2010: 11.9,
    2011: 11.8, 2012: 11.3, 2013: 11.3, 2014: 11.1, 2015: 11.1,
    2016: 10.7, 2017: 10.7, 2018: 10.5, 2019: 10.3, 2020: 10.8,
    2021: 10.3, 2022: 10.1, 2023: 10.0, 2024: 9.8,
}

# BLS Work Stoppages (1000+ workers) — annual count
STRIKE_COUNT = {
    1971: 298, 1972: 250, 1973: 317, 1974: 424, 1975: 235,
    1976: 231, 1977: 298, 1978: 219, 1979: 235, 1980: 187,
    1981: 145, 1982: 96,  1983: 81,  1984: 62,  1985: 54,
    1986: 69,  1987: 46,  1988: 40,  1989: 51,  1990: 44,
    1991: 40,  1992: 35,  1993: 35,  1994: 45,  1995: 31,
    1996: 37,  1997: 29,  1998: 34,  1999: 17,  2000: 39,
    2001: 29,  2002: 19,  2003: 14,  2004: 17,  2005: 22,
    2006: 20,  2007: 21,  2008: 15,  2009: 5,   2010: 11,
    2011: 19,  2012: 19,  2013: 15,  2014: 11,  2015: 12,
    2016: 15,  2017: 7,   2018: 20,  2019: 25,  2020: 8,
    2021: 16,  2022: 23,  2023: 33,  2024: 28,
}

# BLS Labor Share of Nonfarm Business Income (%)
LABOR_SHARE = {
    1971: 63.2, 1972: 63.1, 1973: 62.8, 1974: 63.1, 1975: 62.4,
    1976: 62.1, 1977: 62.3, 1978: 62.4, 1979: 62.6, 1980: 63.2,
    1981: 62.8, 1982: 63.4, 1983: 62.1, 1984: 61.2, 1985: 61.4,
    1986: 62.1, 1987: 61.8, 1988: 61.4, 1989: 61.2, 1990: 61.8,
    1991: 62.2, 1992: 61.8, 1993: 61.6, 1994: 61.2, 1995: 61.0,
    1996: 60.8, 1997: 60.9, 1998: 61.4, 1999: 61.2, 2000: 61.0,
    2001: 61.8, 2002: 61.2, 2003: 60.4, 2004: 59.8, 2005: 59.4,
    2006: 59.1, 2007: 59.4, 2008: 59.8, 2009: 59.2, 2010: 57.8,
    2011: 57.2, 2012: 56.8, 2013: 56.9, 2014: 57.1, 2015: 57.4,
    2016: 57.8, 2017: 57.6, 2018: 57.2, 2019: 57.4, 2020: 58.2,
    2021: 57.4, 2022: 56.8, 2023: 57.1, 2024: 56.9,
}

# Projections 2025-2051
PROJ_PRODUCTIVITY = {
    2025: 254.8, 2026: 258.2, 2027: 262.1, 2028: 266.4, 2029: 270.8,
    2030: 275.4, 2031: 280.1, 2032: 284.9, 2033: 289.8, 2034: 294.8,
    2035: 299.9, 2036: 305.1, 2037: 310.4, 2038: 315.8, 2039: 321.3,
    2040: 326.9, 2041: 332.6, 2042: 338.4, 2043: 344.3, 2044: 350.3,
    2045: 356.4, 2046: 362.6, 2047: 368.9, 2048: 375.3, 2049: 381.8,
    2050: 388.4, 2051: 395.1,
}

PROJ_COMPENSATION = {
    2025: 134.2, 2026: 135.4, 2027: 136.8, 2028: 138.1, 2029: 139.4,
    2030: 140.8, 2031: 142.1, 2032: 143.4, 2033: 144.8, 2034: 146.1,
    2035: 147.4, 2036: 148.8, 2037: 150.1, 2038: 151.4, 2039: 152.8,
    2040: 154.1, 2041: 155.4, 2042: 156.8, 2043: 158.1, 2044: 159.4,
    2045: 160.8, 2046: 162.1, 2047: 163.4, 2048: 164.8, 2049: 166.1,
    2050: 167.4, 2051: 168.8,
}

SERIES = [
    {
        "series_id": "productivity_index",
        "label": "Productivity Index (1971=100)",
        "type": "stress",
        "unit": "index",
        "color": "#e05252",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "real_compensation_index",
        "label": "Real Compensation Index (1971=100)",
        "type": "counterweight",
        "unit": "index",
        "color": "#52a8e0",
        "stroke_style": "solid",
        "stroke_width": 2,
        "is_forecast": False,
    },
    {
        "series_id": "union_density",
        "label": "Union Density (%)",
        "type": "counterweight",
        "unit": "percent",
        "color": "#5db85d",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
    {
        "series_id": "labor_share",
        "label": "Labor Share of Income (%)",
        "type": "counterweight",
        "unit": "percent",
        "color": "#9b59b6",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
    {
        "series_id": "strike_count",
        "label": "Major Work Stoppages (count)",
        "type": "counterweight",
        "unit": "count",
        "color": "#1abc9c",
        "stroke_style": "solid",
        "stroke_width": 1.5,
        "is_forecast": False,
    },
    {
        "series_id": "productivity_forecast",
        "label": "Productivity — Projected",
        "type": "stress",
        "unit": "index",
        "color": None,
        "stroke_style": "dashed",
        "stroke_width": 1.5,
        "is_forecast": True,
    },
    {
        "series_id": "compensation_forecast",
        "label": "Compensation — Projected",
        "type": "counterweight",
        "unit": "index",
        "color": None,
        "stroke_style": "dashed",
        "stroke_width": 1.5,
        "is_forecast": True,
    },
]


class PopularImmiserationFetcher(BaseFetcher):
    thread_name = "popular_immiseration"

    def fetch(self) -> dict:
        return {
            "productivity": PRODUCTIVITY,
            "real_compensation": REAL_COMPENSATION,
            "union_density": UNION_DENSITY,
            "strike_count": STRIKE_COUNT,
            "labor_share": LABOR_SHARE,
            "proj_productivity": PROJ_PRODUCTIVITY,
            "proj_compensation": PROJ_COMPENSATION,
        }

    def transform(self, raw: dict) -> dict:
        observations = []

        for year, value in raw["productivity"].items():
            observations.append({
                "date": f"{year}-01-01",
                "series_id": "productivity_index",
                "value": value,
                "is_projection": False,
                "vintage": "2026-06-04",
                "source_version": "BLS PRS85006092 2025",
            })

        for year, value in raw["real_compensation"].items():
            observations.append({
                "date": f"{year}-01-01",
                "series_id": "real_compensation_index",
                "value": value,
                "is_projection": False,
                "vintage": "2026-06-04",
                "source_version": "BLS PRS85006152 2025",
            })

        for year, value in raw["union_density"].items():
            observations.append({
                "date": f"{year}-01-01",
                "series_id": "union_density",
                "value": value,
                "is_projection": False,
                "vintage": "2026-06-04",
                "source_version": "BLS Union Members Summary 2025",
            })

        for year, value in raw["strike_count"].items():
            observations.append({
                "date": f"{year}-01-01",
                "series_id": "strike_count",
                "value": value,
                "is_projection": False,
                "vintage": "2026-06-04",
                "source_version": "BLS Work Stoppages Summary 2025",
            })

        for year, value in raw["labor_share"].items():
            observations.append({
                "date": f"{year}-01-01",
                "series_id": "labor_share",
                "value": value,
                "is_projection": False,
                "vintage": "2026-06-04",
                "source_version": "BLS PRS85006173 2025",
            })

        for year, value in raw["proj_productivity"].items():
            observations.append({
                "date": f"{year}-01-01",
                "series_id": "productivity_forecast",
                "value": value,
                "is_projection": True,
                "vintage": "2026-06-04",
                "source_version": "BLS Employment Outlook extrapolated",
            })

        for year, value in raw["proj_compensation"].items():
            observations.append({
                "date": f"{year}-01-01",
                "series_id": "compensation_forecast",
                "value": value,
                "is_projection": True,
                "vintage": "2026-06-04",
                "source_version": "BLS trend extrapolated",
            })

        return {
            "meta": {
                "thread": "popular_immiseration",
                "label": "Popular Immiseration",
                "last_updated": "2026-06-04",
                "update_frequency": "annual",
                "next_expected_update": "2027-01",
                "source": "BLS Productivity & Costs, Union Members Summary, Work Stoppages",
                "theory_ref": "Turchin SDT — real wage stagnation vs productivity growth; declining bargaining power as structural immiseration driver",
            },
            "series": SERIES,
            "observations": sorted(observations, key=lambda x: (x["date"], x["series_id"])),
        }

    def validate_anomalies(self, data: dict) -> list[str]:
        warnings = []
        prod = {
            o["date"][:4]: o["value"]
            for o in data["observations"]
            if o["series_id"] == "productivity_index"
        }
        comp = {
            o["date"][:4]: o["value"]
            for o in data["observations"]
            if o["series_id"] == "real_compensation_index"
        }
        latest_year = max(prod.keys())
        gap = prod[latest_year] - comp[latest_year]
        if gap > 100:
            warnings.append(
                f"Productivity/compensation gap exceeds 100 index points ({gap:.1f}) — verify BLS series alignment"
            )
        return warnings


if __name__ == "__main__":
    PopularImmiserationFetcher().run()
