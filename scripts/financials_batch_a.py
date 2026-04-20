# -*- coding: utf-8 -*-
"""
Batch A -- TTM and 5-year valuation data (approx. Q4 2025 consensus).
Companies: LLY, ABBV, GILD, 4568, UCB, ONC, ARGX, NBIX
"""

FINANCIALS = {
    "LLY": {
        "pe_ttm": 54,
        "ev_sales_ttm": 14.2,
        "net_income_ttm_M": 12500,
        "revenue_ttm_M": 53800,
        "pe_5y": {"min": 22, "median": 45, "max": 75, "current_pctl": 78},
        "ev_sales_5y": {"min": 7, "median": 11, "max": 18, "current_pctl": 80},
        "subsector": "obesity_glp1",
        "peer_group": ["NVO", "PFE", "AMGN"],
        "notes": (
            "GLP-1 hypergrowth premium -- Mounjaro+Zepbound ~$40B 2025E; "
            "multiple compression expected as pipeline matures."
        ),
    },
    "ABBV": {
        "pe_ttm": 32,
        "ev_sales_ttm": 7.1,
        "net_income_ttm_M": 6000,
        "revenue_ttm_M": 56000,
        "pe_5y": {"min": 8, "median": 18, "max": 34, "current_pctl": 88},
        "ev_sales_5y": {"min": 4, "median": 6, "max": 8, "current_pctl": 82},
        "subsector": "immunology",
        "peer_group": ["JNJ", "MRK", "BMY"],
        "notes": (
            "Skyrizi+Rinvoq offsetting Humira biosimilar erosion; "
            "P/E elevated vs history on durable franchise re-rating."
        ),
    },
    "GILD": {
        "pe_ttm": 13,
        "ev_sales_ttm": 6.1,
        "net_income_ttm_M": 5500,
        "revenue_ttm_M": 28000,
        "pe_5y": {"min": 7, "median": 13, "max": 28, "current_pctl": 42},
        "ev_sales_5y": {"min": 4, "median": 6, "max": 9, "current_pctl": 48},
        "subsector": "large_cap",
        "peer_group": ["VRTX", "BIIB"],
        "notes": (
            "HIV cash cow (Biktarvy $14B); oncology drag from Trodelvy; "
            "Livdelzi/MASH optionality not yet in multiple."
        ),
    },
    "4568": {
        "pe_ttm": 36,
        "ev_sales_ttm": 4.5,
        "net_income_ttm_M": 1100,
        "revenue_ttm_M": 12000,
        "pe_5y": {"min": 20, "median": 30, "max": 55, "current_pctl": 58},
        "ev_sales_5y": {"min": 2, "median": 3, "max": 6, "current_pctl": 68},
        "subsector": "oncology",
        "peer_group": ["4523", "4503"],
        "notes": (
            "Daiichi Sankyo -- Enhertu ADC franchise ~$4.6B; "
            "pipeline premium from broad ADC platform; JPY reporting."
        ),
    },
    "UCB": {
        "pe_ttm": 25,
        "ev_sales_ttm": 6.0,
        "net_income_ttm_M": 1100,
        "revenue_ttm_M": 6800,
        "pe_5y": {"min": 15, "median": 20, "max": 32, "current_pctl": 65},
        "ev_sales_5y": {"min": 3, "median": 5, "max": 7, "current_pctl": 70},
        "subsector": "immunology",
        "peer_group": ["NOVN", "ROG"],
        "notes": (
            "Bimzelx IL-17A/F ramp ~$1.5B; legacy neuro EUR 976M stable; "
            "EUR-reported; mid-cap EU biotech premium."
        ),
    },
    "ONC": {
        "pe_ttm": 55,
        "ev_sales_ttm": 7.2,
        "net_income_ttm_M": 450,
        "revenue_ttm_M": 4700,
        "pe_5y": {"min": None, "median": None, "max": None, "current_pctl": None},
        "ev_sales_5y": {"min": 4, "median": 6, "max": 10, "current_pctl": 60},
        "subsector": "oncology",
        "peer_group": ["EXEL", "INCY"],
        "notes": (
            "BeOne/BeiGene -- Brukinsa $3.9B+; recently turned profitable; "
            "early P/E high; dual-listed HK+US; China execution risk."
        ),
    },
    "ARGX": {
        "pe_ttm": 75,
        "ev_sales_ttm": 10.1,
        "net_income_ttm_M": 350,
        "revenue_ttm_M": 4200,
        "pe_5y": {"min": None, "median": None, "max": None, "current_pctl": None},
        "ev_sales_5y": {"min": 5, "median": 8, "max": 14, "current_pctl": 72},
        "subsector": "immunology",
        "peer_group": ["RETA", "KRTX", "NBIX"],
        "notes": (
            "Vyvgart franchise scaling -- gMG + CIDP; FcRn class leader; "
            "first full profitable year; P/E compressing as earnings ramp."
        ),
    },
    "NBIX": {
        "pe_ttm": 18,
        "ev_sales_ttm": 4.6,
        "net_income_ttm_M": 800,
        "revenue_ttm_M": 3000,
        "pe_5y": {"min": 22, "median": 35, "max": 60, "current_pctl": 12},
        "ev_sales_5y": {"min": 4, "median": 7, "max": 12, "current_pctl": 15},
        "subsector": "neurology_psych",
        "peer_group": ["ACAD", "SGMO", "BIIB"],
        "notes": (
            "Ingrezza $2.5B tardive dyskinesia; Crenessity + VYKAT growth; "
            "P/E at 5y low -- pipeline concerns weigh on multiple."
        ),
    },
}


if __name__ == "__main__":
    print(f"financials_batch_a: {len(FINANCIALS)} companies loaded")
    for ticker, data in FINANCIALS.items():
        rev = data["revenue_ttm_M"]
        pe = data["pe_ttm"]
        evs = data["ev_sales_ttm"]
        pe_str = f"{pe}x" if pe is not None else "N/A (unprofitable)"
        print(f"  {ticker:6s}  rev=${rev:>7,.0f}M  P/E={pe_str:>20s}  EV/S={evs}x")
