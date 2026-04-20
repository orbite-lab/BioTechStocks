# -*- coding: utf-8 -*-
"""
add_external_peers.py
---------------------
Merges ~20 external big-pharma / large-cap biotech reference entries into
financials.json so the "Live All" and "Live Cap" medians are representative
of the broader pharma/biotech space and not just our 24 covered names.

Run:
    python scripts/add_external_peers.py

Non-USD companies (NVO, ROG, NVS, SNY, AZN) have been converted to USD
using approximate current (Apr 2026) FX rates:
  DKK/USD  0.146   (NVO reports in DKK)
  CHF/USD  1.13    (ROG, NVS report in CHF)
  EUR/USD  1.09    (SNY reports in EUR)
  USD/USD  1.00    (AZN reports in USD -- LSE listed but USD-denominated)

P/E and EV/S 5-year range bands (2020-2025 rolling medians from domain
knowledge; percentiles are vs that 5-year range).
"""

import json
import os
import sys

# ---------------------------------------------------------------------------
# External peer definitions
# ---------------------------------------------------------------------------
EXTERNAL_PEERS = {
    # ------------------------------------------------------------------
    # Big Pharma -- mega-cap
    # ------------------------------------------------------------------
    "JNJ": {
        "pe_ttm": 26,
        "ev_sales_ttm": 4.2,
        "net_income_ttm_M": 14000,
        "revenue_ttm_M": 88000,
        "mcap_usd_M": 370000,
        "pe_5y": {"min": 14, "median": 20, "max": 30, "current_pctl": 62},
        "ev_sales_5y": {"min": 3.5, "median": 4.0, "max": 5.2, "current_pctl": 55},
        "subsector": "large_cap",
        "peer_group": ["MRK", "PFE", "BMY", "NVS"],
        "external": True,
        "notes": "Reference peer; diversified pharma + medtech; MedTech spin (Kenvue) narrowed the multiple premium vs pure-play pharma peers."
    },
    "MRK": {
        "pe_ttm": 15,
        "ev_sales_ttm": 4.0,
        "net_income_ttm_M": 17000,
        "revenue_ttm_M": 65000,
        "mcap_usd_M": 260000,
        "pe_5y": {"min": 11, "median": 16, "max": 26, "current_pctl": 30},
        "ev_sales_5y": {"min": 3.0, "median": 4.2, "max": 6.0, "current_pctl": 45},
        "subsector": "large_cap",
        "peer_group": ["JNJ", "BMY", "PFE", "AZN"],
        "external": True,
        "notes": "Reference peer; Keytruda ~$25B+ dominating oncology I-O; Winrevair PAH + MK-1654 pipeline; P/E below 5y median on Keytruda LOE cliff fears 2028+."
    },
    "PFE": {
        "pe_ttm": 21,
        "ev_sales_ttm": 2.9,
        "net_income_ttm_M": 8000,
        "revenue_ttm_M": 58000,
        "mcap_usd_M": 170000,
        "pe_5y": {"min": 10, "median": 16, "max": 28, "current_pctl": 52},
        "ev_sales_5y": {"min": 2.0, "median": 3.2, "max": 6.5, "current_pctl": 32},
        "subsector": "large_cap",
        "peer_group": ["JNJ", "MRK", "BMY", "SNY"],
        "external": True,
        "notes": "Reference peer; post-COVID rev normalization ($58B vs $100B peak); Seagen oncology integration; EV/S near 5y low; pipeline rebuild optionality."
    },
    "BMY": {
        "pe_ttm": 12,
        "ev_sales_ttm": 2.1,
        "net_income_ttm_M": 8000,
        "revenue_ttm_M": 48000,
        "mcap_usd_M": 100000,
        "pe_5y": {"min": 8, "median": 14, "max": 22, "current_pctl": 28},
        "ev_sales_5y": {"min": 1.8, "median": 2.8, "max": 4.2, "current_pctl": 25},
        "subsector": "large_cap",
        "peer_group": ["JNJ", "MRK", "PFE", "ABBV"],
        "external": True,
        "notes": "Reference peer; Opdivo + Eliquis LOE cliff ~2026-28; Revlimid generics fully hit; deeply discounted to peers on patent overhang; pipeline not yet offsetting."
    },
    "NVS": {
        # CHF -> USD: revenue ~CHF 47B * 1.13 = ~$53B; net inc ~CHF 11B * 1.13 = ~$12B
        # mcap ~CHF 204B * 1.13 = ~$230B
        "pe_ttm": 19,
        "ev_sales_ttm": 4.6,
        "net_income_ttm_M": 12000,
        "revenue_ttm_M": 53000,
        "mcap_usd_M": 230000,
        "pe_5y": {"min": 13, "median": 18, "max": 28, "current_pctl": 45},
        "ev_sales_5y": {"min": 3.5, "median": 4.8, "max": 6.5, "current_pctl": 48},
        "subsector": "large_cap",
        "peer_group": ["ROG", "AZN", "SNY", "JNJ"],
        "external": True,
        "notes": "Reference peer; Sandoz generic spin completed 2023; Kisqali breast cancer + Cosentyx + Leqvio pipeline; CHF-reported converted to USD at 1.13."
    },
    "NVO": {
        # DKK -> USD: revenue ~DKK 290B * 0.146 = ~$42B; net inc ~DKK 97B * 0.146 = ~$14B
        # mcap ~DKK 2.6T * 0.146 = ~$380B
        "pe_ttm": 27,
        "ev_sales_ttm": 8.8,
        "net_income_ttm_M": 14000,
        "revenue_ttm_M": 42000,
        "mcap_usd_M": 380000,
        "pe_5y": {"min": 22, "median": 35, "max": 60, "current_pctl": 32},
        "ev_sales_5y": {"min": 8.0, "median": 18.0, "max": 35.0, "current_pctl": 22},
        "subsector": "obesity_glp1",
        "peer_group": ["LLY", "AZN", "SNY"],
        "external": True,
        "notes": "Reference peer; Ozempic + Wegovy GLP-1 duopoly; ~DKK 290B rev; multiple compressed sharply from 50x+ as market share risk from oral GLP-1 and AMG-133 competes; DKK-reported converted at 0.146."
    },
    "ROG": {
        # CHF -> USD: revenue ~CHF 58B * 1.13 = ~$65B; net inc ~CHF 12B * 1.13 = ~$14B
        # mcap ~CHF 199B * 1.13 = ~$225B
        "pe_ttm": 16,
        "ev_sales_ttm": 3.5,
        "net_income_ttm_M": 14000,
        "revenue_ttm_M": 65000,
        "mcap_usd_M": 225000,
        "pe_5y": {"min": 12, "median": 16, "max": 22, "current_pctl": 42},
        "ev_sales_5y": {"min": 2.8, "median": 3.8, "max": 5.2, "current_pctl": 38},
        "subsector": "large_cap",
        "peer_group": ["NVS", "AZN", "JNJ"],
        "external": True,
        "notes": "Reference peer; Roche Holding; diagnostics + pharma (Vabysmo, Tecentriq, HER2 franchise); biosimilar erosion on legacy biologics; CHF-reported at 1.13."
    },
    "SNY": {
        # EUR -> USD: revenue ~EUR 44B * 1.09 = ~$48B; net inc ~EUR 6.4B * 1.09 = ~$7B
        # mcap ~EUR 110B * 1.09 = ~$120B
        "pe_ttm": 17,
        "ev_sales_ttm": 2.5,
        "net_income_ttm_M": 7000,
        "revenue_ttm_M": 48000,
        "mcap_usd_M": 120000,
        "pe_5y": {"min": 10, "median": 16, "max": 22, "current_pctl": 40},
        "ev_sales_5y": {"min": 2.0, "median": 3.0, "max": 4.5, "current_pctl": 28},
        "subsector": "large_cap",
        "peer_group": ["JNJ", "NVS", "ROG", "BMY"],
        "external": True,
        "notes": "Reference peer; Dupixent ~$14B+ largest growth driver; CHC consumer spin optionality; EUR-reported converted at 1.09; P/E discounted on Lantus/Lovenox loss."
    },
    "AZN": {
        # USD-denominated reporting on NYSE/LSE ADR
        "pe_ttm": 30,
        "ev_sales_ttm": 4.3,
        "net_income_ttm_M": 7500,
        "revenue_ttm_M": 52000,
        "mcap_usd_M": 220000,
        "pe_5y": {"min": 22, "median": 32, "max": 48, "current_pctl": 48},
        "ev_sales_5y": {"min": 3.5, "median": 5.5, "max": 8.0, "current_pctl": 38},
        "subsector": "large_cap",
        "peer_group": ["MRK", "NVS", "ROG", "JNJ"],
        "external": True,
        "notes": "Reference peer; Tagrisso + Lynparza + Imfinzi + CVRM portfolio; premium to sector on consistent double-digit growth; USD-denominated ADR; China exposure ~20% rev."
    },

    # ------------------------------------------------------------------
    # Large-cap biotech
    # ------------------------------------------------------------------
    "AMGN": {
        "pe_ttm": 24,
        "ev_sales_ttm": 5.0,
        "net_income_ttm_M": 7000,
        "revenue_ttm_M": 33000,
        "mcap_usd_M": 165000,
        "pe_5y": {"min": 11, "median": 17, "max": 28, "current_pctl": 68},
        "ev_sales_5y": {"min": 3.8, "median": 5.2, "max": 7.5, "current_pctl": 48},
        "subsector": "large_cap",
        "peer_group": ["GILD", "BIIB", "VRTX", "REGN"],
        "external": True,
        "notes": "Reference peer; Repatha + Evenity + Tezspire growth; MariTide obesity Phase 3 re-rating potential; Horizon acquisition adds rare disease; P/E above 5y median on obesity optionality."
    },
    "VRTX": {
        "pe_ttm": 34,
        "ev_sales_ttm": 11.0,
        "net_income_ttm_M": 3500,
        "revenue_ttm_M": 10500,
        "mcap_usd_M": 120000,
        "pe_5y": {"min": 22, "median": 30, "max": 50, "current_pctl": 62},
        "ev_sales_5y": {"min": 8.0, "median": 12.0, "max": 20.0, "current_pctl": 48},
        "subsector": "rare_disease",
        "peer_group": ["ALNY", "BMRN", "REGN"],
        "external": True,
        "notes": "Reference peer; Trikafta CF franchise near-monopoly ~$9.5B; Casgevy sickle cell; pain NaV1.8 (suzetrigine) potential new pillar; premium rare-disease quality multiple."
    },
    "REGN": {
        "pe_ttm": 20,
        "ev_sales_ttm": 6.0,
        "net_income_ttm_M": 4000,
        "revenue_ttm_M": 13000,
        "mcap_usd_M": 80000,
        "pe_5y": {"min": 12, "median": 18, "max": 30, "current_pctl": 45},
        "ev_sales_5y": {"min": 4.5, "median": 7.0, "max": 12.0, "current_pctl": 40},
        "subsector": "immunology",
        "peer_group": ["VRTX", "AMGN", "BIIB"],
        "external": True,
        "notes": "Reference peer; Dupixent collaboration revenues + Eylea franchise; Kevzara + Inmazeb; P/E below 5y median on Eylea biosimilar pressure; Dupixent YTD growth sustains premium."
    },
    "BIIB": {
        "pe_ttm": 20,
        "ev_sales_ttm": 2.3,
        "net_income_ttm_M": 1100,
        "revenue_ttm_M": 9700,
        "mcap_usd_M": 22000,
        "pe_5y": {"min": 8, "median": 14, "max": 30, "current_pctl": 55},
        "ev_sales_5y": {"min": 1.5, "median": 2.5, "max": 5.0, "current_pctl": 38},
        "subsector": "neurology_psych",
        "peer_group": ["NBIX", "ALNY", "REGN"],
        "external": True,
        "notes": "Reference peer; Leqembi Alzheimer modest uptake; legacy MS (Tysabri, Tecfidera biosimilar impact); Skyclarys Friedreich ataxia; EV/S compressed vs biotech peers; P/E mid-range on declining revenue."
    },
    "MRNA": {
        "pe_ttm": None,
        "ev_sales_ttm": 4.5,
        "net_income_ttm_M": -4000,
        "revenue_ttm_M": 3500,
        "mcap_usd_M": 18000,
        "pe_5y": {"min": None, "median": None, "max": None, "current_pctl": None,
                  "note": "unprofitable post-COVID revenue collapse; P/E not meaningful"},
        "ev_sales_5y": {"min": 1.5, "median": 6.0, "max": 30.0, "current_pctl": 20},
        "subsector": "vaccines",
        "peer_group": ["BNTX", "VLA", "AZN"],
        "external": True,
        "notes": "Reference peer; mRNA COVID vaccine rev collapsed from $18B; RSV + flu mRNA pipeline key re-rating; heavy cash burn; EV/S near 5y low reflecting post-COVID hangover."
    },
    "BNTX": {
        "pe_ttm": None,
        "ev_sales_ttm": 7.5,
        "net_income_ttm_M": -500,
        "revenue_ttm_M": 3200,
        "mcap_usd_M": 30000,
        "pe_5y": {"min": None, "median": None, "max": None, "current_pctl": None,
                  "note": "unprofitable; COVID windfall lapped; not meaningful"},
        "ev_sales_5y": {"min": 2.0, "median": 8.0, "max": 60.0, "current_pctl": 18},
        "subsector": "vaccines",
        "peer_group": ["MRNA", "VLA"],
        "external": True,
        "notes": "Reference peer; BNT111 melanoma + BNT323 ADC oncology pipeline; EUR-headquartered but USD-ADR; cash-rich balance sheet from COVID windfall sustains R&D burn; EV/S at 5y low."
    },

    # ------------------------------------------------------------------
    # Mid/large growth biotech
    # ------------------------------------------------------------------
    "INCY": {
        "pe_ttm": 28,
        "ev_sales_ttm": 3.8,
        "net_income_ttm_M": 600,
        "revenue_ttm_M": 4200,
        "mcap_usd_M": 17000,
        "pe_5y": {"min": 18, "median": 30, "max": 55, "current_pctl": 38},
        "ev_sales_5y": {"min": 3.0, "median": 5.5, "max": 9.0, "current_pctl": 28},
        "subsector": "oncology",
        "peer_group": ["ONC", "EXEL", "ARQT"],
        "external": True,
        "notes": "Reference peer; Jakafi myelofibrosis + PV mature franchise; Opzelura (ruxolitinib cream) derm ramp ~$1.2B; pipeline diversification via Zynyz; P/E below 5y median on Jakafi patent cliff 2028."
    },
    "EXEL": {
        "pe_ttm": 33,
        "ev_sales_ttm": 4.2,
        "net_income_ttm_M": 300,
        "revenue_ttm_M": 2200,
        "mcap_usd_M": 10000,
        "pe_5y": {"min": 20, "median": 32, "max": 60, "current_pctl": 48},
        "ev_sales_5y": {"min": 3.0, "median": 5.0, "max": 8.0, "current_pctl": 42},
        "subsector": "oncology",
        "peer_group": ["ONC", "INCY"],
        "external": True,
        "notes": "Reference peer; cabozantinib (Cabometyx/Cometriq) RCC + HCC franchise; royalties from cobimetinib/COTELLIC; zanzalintinib XL092 Phase 3 pipeline; consistently profitable at modest but growing margin."
    },
    "BMRN": {
        "pe_ttm": 52,
        "ev_sales_ttm": 4.5,
        "net_income_ttm_M": 250,
        "revenue_ttm_M": 2800,
        "mcap_usd_M": 13000,
        "pe_5y": {"min": None, "median": None, "max": None, "current_pctl": None,
                  "note": "only recently turned profitable 2023; meaningful P/E history too short"},
        "ev_sales_5y": {"min": 3.0, "median": 5.0, "max": 10.0, "current_pctl": 40},
        "subsector": "rare_disease",
        "peer_group": ["ALNY", "BBIO", "VRTX", "ARWR"],
        "external": True,
        "notes": "Reference peer; Voxzogo achondroplasia + Roctavian hemophilia + Palynziq PKU; recently profitability inflection; high P/E on early earnings ramp; mid-cap rare-disease quality premium."
    },
    "UTHR": {
        "pe_ttm": 15,
        "ev_sales_ttm": 5.3,
        "net_income_ttm_M": 1100,
        "revenue_ttm_M": 2900,
        "mcap_usd_M": 17000,
        "pe_5y": {"min": 10, "median": 14, "max": 22, "current_pctl": 40},
        "ev_sales_5y": {"min": 3.5, "median": 5.5, "max": 8.5, "current_pctl": 45},
        "subsector": "rare_disease",
        "peer_group": ["BMRN", "VRTX", "RARE"],
        "external": True,
        "notes": "Reference peer; Tyvaso + Orenitram PAH franchise; Unituxin neuroblastoma; Tyvaso DPI ramp sustains revenue; profitable and cash-generative; P/E below sector median on perceived franchise concentration."
    },
    "RARE": {
        "pe_ttm": None,
        "ev_sales_ttm": 8.0,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 600,
        "mcap_usd_M": 5000,
        "pe_5y": {"min": None, "median": None, "max": None, "current_pctl": None,
                  "note": "unprofitable throughout; heavy rare-disease R&D investment"},
        "ev_sales_5y": {"min": 4.0, "median": 8.0, "max": 18.0, "current_pctl": 42},
        "subsector": "rare_disease",
        "peer_group": ["BBIO", "BMRN", "ARWR"],
        "external": True,
        "notes": "Reference peer (Ultragenyx); Crysvita (burosumab) XLH + Dojolvi LC-FAOD + GTX-102 Angelman Phase 3 pipeline; unprofitable; EV/S inline with rare-disease peers despite smaller scale."
    },
    "ACAD": {
        "pe_ttm": 40,
        "ev_sales_ttm": 4.1,
        "net_income_ttm_M": 100,
        "revenue_ttm_M": 950,
        "mcap_usd_M": 4000,
        "pe_5y": {"min": None, "median": None, "max": None, "current_pctl": None,
                  "note": "only recently profitable 2024; P/E history not meaningful"},
        "ev_sales_5y": {"min": 3.0, "median": 6.0, "max": 14.0, "current_pctl": 22},
        "subsector": "neurology_psych",
        "peer_group": ["NBIX", "AXSM", "BIIB"],
        "external": True,
        "notes": "Reference peer; Daybue Rett syndrome launch ramp + Nuplazid PDP; recently profitable; high P/E on early earnings; EV/S at 5y low -- Daybue churn rates overhang; CNS specialist premium."
    }
}


def main():
    repo_root = os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    )
    financials_path = os.path.join(repo_root, "financials.json")

    if not os.path.exists(financials_path):
        print(f"ERROR: cannot find {financials_path}", file=sys.stderr)
        sys.exit(1)

    with open(financials_path, "r", encoding="utf-8") as fh:
        data = json.load(fh)

    added = 0
    skipped = 0

    for ticker, entry in EXTERNAL_PEERS.items():
        if ticker in data:
            print(f"  WARN: {ticker} already exists in financials.json -- skipping (not overwriting).")
            skipped += 1
        else:
            data[ticker] = entry
            added += 1
            print(f"  + added {ticker}")

    with open(financials_path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)

    total = len(data)
    print(f"\nDone. Added {added} entries, skipped {skipped} duplicates. "
          f"financials.json now has {total} entries total.")


if __name__ == "__main__":
    main()
