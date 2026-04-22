# -*- coding: utf-8 -*-
"""
Batch C -- TTM and 5-year valuation data (approx. Q4 2025 consensus).
Companies: 6990, KRYS, IONS, ARQT, ARWR, RYTM, VLA, CRSP
"""

FINANCIALS = {
    "6990": {
        "pe_ttm": None,
        "ev_sales_ttm": 30,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 350,
        "pe_5y": {"min": None, "median": None, "max": None, "current_pctl": None},
        "ev_sales_5y": {"min": 12, "median": 22, "max": 45, "current_pctl": 78},
        "subsector": "oncology",
        "peer_group": ["1876.HK", "2616.HK"],
        "notes": (
            "Kelun-Biotech HK-listed ADC; Sac-TMT + A166 China launch; "
            "approaching profitability; hyper-growth HK premium; RMB/HKD reporting."
        ),
    },
    "KRYS": {
        "pe_ttm": 48,
        "ev_sales_ttm": 22,
        "net_income_ttm_M": 160,
        "revenue_ttm_M": 350,
        "pe_5y": {"min": 30, "median": 55, "max": 120, "current_pctl": 35},
        "ev_sales_5y": {"min": 18, "median": 35, "max": 60, "current_pctl": 20},
        "subsector": "gene_therapy",
        "peer_group": ["BMRN", "RGNX", "PTCT"],
        "notes": (
            "VYJUVEK rare DEB franchise profitable + pipeline; "
            "trading below 5y median post small-cap derating."
        ),
    },
    "IONS": {
        "pe_ttm": None,
        "ev_sales_ttm": 15,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 330,
        "pe_5y": {"min": None, "median": None, "max": None, "current_pctl": None},
        "ev_sales_5y": {"min": 6, "median": 12, "max": 22, "current_pctl": 55},
        "subsector": "rare_disease",
        "peer_group": ["ALNY", "ARWR", "NVOT"],
        "notes": (
            "TRYNGOLZA + DAWNZERA + eplontersen royalties; ASO platform optionality; "
            "unprofitable on R&D spend despite growing commercial revenues."
        ),
    },
    "ARQT": {
        "pe_ttm": None,
        "ev_sales_ttm": 12,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 250,
        "pe_5y": {"min": None, "median": None, "max": None, "current_pctl": None},
        "ev_sales_5y": {"min": 5, "median": 10, "max": 20, "current_pctl": 48},
        "subsector": "immunology",
        "peer_group": ["DERM", "INCY", "ANAB"],
        "notes": (
            "ZORYVE derm franchise (pso, AD, seb derm) approaching profitability; "
            "EV/S near 5y median; pipeline label expansions key 2026 catalyst."
        ),
    },
    "ARWR": {
        "pe_ttm": None,
        "ev_sales_ttm": 44,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 200,
        "pe_5y": {"min": None, "median": None, "max": None, "current_pctl": None},
        "ev_sales_5y": {"min": 15, "median": 35, "max": 70, "current_pctl": 62},
        "subsector": "rare_disease",
        "peer_group": ["ALNY", "IONS", "DCPH"],
        "notes": (
            "REDEMPLO FCS launch + pipeline milestones; high EV/S reflects "
            "RNAi platform optionality; unprofitable on heavy pipeline investment."
        ),
    },
    "RYTM": {
        "pe_ttm": None,
        "ev_sales_ttm": 29,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 195,
        "pe_5y": {"min": None, "median": None, "max": None, "current_pctl": None},
        "ev_sales_5y": {"min": 10, "median": 22, "max": 45, "current_pctl": 65},
        "subsector": "rare_disease",
        "peer_group": ["RARE", "BMRN"],
        "notes": (
            "Imcivree rare obesity franchise; approaching profitability 2026E; "
            "premium EV/S on MC4R pathway exclusivity and durable orphan pricing."
        ),
    },
    "VLA": {
        "pe_ttm": None,
        "ev_sales_ttm": 2,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 200,
        "pe_5y": {"min": None, "median": None, "max": None, "current_pctl": None},
        "ev_sales_5y": {"min": 1, "median": 3, "max": 8, "current_pctl": 18},
        "subsector": "vaccines",
        "peer_group": ["BNTX", "NVAX"],
        "notes": (
            "Valneva EUR-reported; IXIARO+DUKORAL travel + IXCHIQ chikungunya; "
            "depressed EV/S post VALOR Lyme setback; small net loss TTM."
        ),
    },
    "CRSP": {
        "pe_ttm": None,
        "ev_sales_ttm": 34,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 116,
        "pe_5y": {"min": None, "median": None, "max": None, "current_pctl": None},
        "ev_sales_5y": {"min": 12, "median": 40, "max": 120, "current_pctl": 28},
        "subsector": "gene_therapy",
        "peer_group": ["BLUE", "EDIT", "NTLA"],
        "notes": (
            "Casgevy still ramping with Vertex partnership; high EV/S on cardio "
            "edit pipeline optionality; unprofitable; mcap ~$4.2B."
        ),
    },
}


if __name__ == "__main__":
    print(f"financials_batch_c: {len(FINANCIALS)} companies loaded")
    for ticker, data in FINANCIALS.items():
        rev = data["revenue_ttm_M"]
        pe = data["pe_ttm"]
        evs = data["ev_sales_ttm"]
        pe_str = f"{pe}x" if pe is not None else "N/A (unprofitable)"
        print(f"  {ticker:6s}  rev=${rev:>7,.0f}M  P/E={pe_str:>20s}  EV/S={evs}x")
