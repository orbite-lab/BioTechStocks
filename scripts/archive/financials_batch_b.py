# -*- coding: utf-8 -*-
"""
Batch B -- TTM and 5-year valuation data (approx. Q4 2025 consensus).
Companies: ALNY, SRPT, MDGL, LEGN, AXSM, BBIO, CAMX, TVTX
"""

FINANCIALS = {
    "ALNY": {
        "pe_ttm": 95,
        "ev_sales_ttm": 14,
        "net_income_ttm_M": 450,
        "revenue_ttm_M": 2970,
        "pe_5y": {
            "min": None,
            "median": None,
            "max": None,
            "current_pctl": None,
            "note": "unprofitable until 2024",
        },
        "ev_sales_5y": {"min": 8, "median": 14, "max": 22, "current_pctl": 55},
        "subsector": "rare_disease",
        "peer_group": ["ARWR", "IONS", "BMRN"],
        "notes": (
            "Amvuttra CM label drives TTR franchise ~$2.5B; inflected to "
            "profitability 2024; early-profitability P/E; premium rare-disease multiple."
        ),
    },
    "SRPT": {
        "pe_ttm": None,
        "ev_sales_ttm": 1.5,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 1840,
        "pe_5y": {
            "min": None,
            "median": None,
            "max": None,
            "current_pctl": None,
            "note": "unprofitable throughout; 2025 safety crisis crushed mcap",
        },
        "ev_sales_5y": {"min": 5, "median": 7, "max": 10, "current_pctl": 5},
        "subsector": "gene_therapy",
        "peer_group": ["BMRN", "RGNX", "PTCT"],
        "notes": (
            "Elevidys safety events 2025 halved mcap to ~$2.3B; EV/S at "
            "multi-year low vs 5-10x historical; recovery hinges on FDA path."
        ),
    },
    "MDGL": {
        "pe_ttm": None,
        "ev_sales_ttm": 9,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 1280,
        "pe_5y": {
            "min": None,
            "median": None,
            "max": None,
            "current_pctl": None,
            "note": "unprofitable; Rezdiffra launched 2024 -- history too short",
        },
        "ev_sales_5y": {"min": None, "median": None, "max": None, "current_pctl": None},
        "subsector": "liver_mash",
        "peer_group": ["NOVO", "ACAD", "INVA"],
        "notes": (
            "Rezdiffra first-in-class MASH approval Apr 2024; Q4 run-rate ~$1.3B; "
            "cash burn narrowing; no direct public peers; high-growth launch multiple."
        ),
    },
    "LEGN": {
        "pe_ttm": None,
        "ev_sales_ttm": 2,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 1060,
        "pe_5y": {
            "min": None,
            "median": None,
            "max": None,
            "current_pctl": None,
            "note": "unprofitable; Carvykti revenue split with J&J",
        },
        "ev_sales_5y": {"min": None, "median": None, "max": None, "current_pctl": None},
        "subsector": "oncology",
        "peer_group": ["BLUE", "BCRX", "FATE"],
        "notes": (
            "Carvykti BCMA CAR-T ~$1.1B; J&J profit-share compresses margin; "
            "EV/S depressed at 2x; scale + earlier lines key re-rating catalyst."
        ),
    },
    "AXSM": {
        "pe_ttm": None,
        "ev_sales_ttm": 11,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 660,
        "pe_5y": {
            "min": None,
            "median": None,
            "max": None,
            "current_pctl": None,
            "note": "unprofitable throughout 5y; approaching breakeven Q4 2025",
        },
        "ev_sales_5y": {"min": 6, "median": 10, "max": 18, "current_pctl": 48},
        "subsector": "neurology_psych",
        "peer_group": ["SAGE", "CERE", "INVA"],
        "notes": (
            "Auvelity MDD + Sunosi + Symbravo portfolio ~$660M; approaching "
            "profitability; EV/S 11x reflects pipeline optionality in CNS."
        ),
    },
    "BBIO": {
        "pe_ttm": None,
        "ev_sales_ttm": 24,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 600,
        "pe_5y": {
            "min": None,
            "median": None,
            "max": None,
            "current_pctl": None,
            "note": "unprofitable; Attruby launched late 2023",
        },
        "ev_sales_5y": {"min": None, "median": None, "max": None, "current_pctl": None},
        "subsector": "rare_disease",
        "peer_group": ["ALNY", "BMRN", "RARE"],
        "notes": (
            "Attruby ATTR-CM + royalty income ~$600M TTM; premium 24x EV/S on "
            "launch trajectory + broad genetic medicine pipeline; still cash-burning."
        ),
    },
    "CAMX": {
        "pe_ttm": 32,
        "ev_sales_ttm": 7,
        "net_income_ttm_M": 85,
        "revenue_ttm_M": 340,
        "pe_5y": {
            "min": 20,
            "median": 28,
            "max": 45,
            "current_pctl": 60,
        },
        "ev_sales_5y": {"min": 4, "median": 6, "max": 10, "current_pctl": 58},
        "subsector": "neurology_psych",
        "peer_group": ["INDV", "ORXN", "RBGPF"],
        "notes": (
            "Camurus -- Buvidal long-acting buprenorphine OUD; ~SEK 3.6B rev "
            "($340M USD); profitable; mcap ~$2.7B USD; SEK-reported Swedish mid-cap."
        ),
    },
    "TVTX": {
        "pe_ttm": None,
        "ev_sales_ttm": 5,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 400,
        "pe_5y": {
            "min": None,
            "median": None,
            "max": None,
            "current_pctl": None,
            "note": "unprofitable; approaching breakeven as FILSPARI scales",
        },
        "ev_sales_5y": {"min": None, "median": None, "max": None, "current_pctl": None},
        "subsector": "rare_disease",
        "peer_group": ["DCPH", "CHNR", "BPTH"],
        "notes": (
            "FILSPARI (sparsentan) IgAN + FSGS -- first dual ET/AT antagonist; "
            "~$400M TTM; mcap ~$2.5B; EV/S 5x; profitability expected 2026."
        ),
    },
}


if __name__ == "__main__":
    print(f"financials_batch_b: {len(FINANCIALS)} companies loaded")
    for ticker, data in FINANCIALS.items():
        rev = data["revenue_ttm_M"]
        pe = data["pe_ttm"]
        evs = data["ev_sales_ttm"]
        pe_str = f"{pe}x" if pe is not None else "N/A (unprofitable)"
        print(f"  {ticker:6s}  rev=${rev:>7,.0f}M  P/E={pe_str:>24s}  EV/S={evs}x")
