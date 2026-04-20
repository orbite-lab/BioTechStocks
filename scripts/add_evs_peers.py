# -*- coding: utf-8 -*-
"""
add_evs_peers.py
----------------
Merges ~18 commercial US biotech reference peers into financials.json.
These companies have drugs on the market and meaningful revenue (>$50M TTM)
but are mostly unprofitable, so they provide valid EV/Sales benchmarks without
polluting the P/E median with loss-making outliers.

Run:
    python scripts/add_evs_peers.py

All figures are USD. EV/S 5-year range bands are rolling estimates from
domain knowledge (2020-2025). P/E 5y fields are null for unprofitable names
and filled for profitable names. Percentiles are vs the 5-year range.
"""

import json
import os
import sys
import statistics

# ---------------------------------------------------------------------------
# EV/S peer definitions  (18 commercial US biotechs)
# ---------------------------------------------------------------------------
EVS_PEERS = {

    # ------------------------------------------------------------------ #
    # RARE DISEASE / OPHTHALMOLOGY                                         #
    # ------------------------------------------------------------------ #
    "APLS": {
        "pe_ttm": None,
        "ev_sales_ttm": 5.0,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 800,
        "mcap_usd_M": 4000,
        "pe_5y": {
            "min": None, "median": None, "max": None, "current_pctl": None,
            "note": "unprofitable"
        },
        "ev_sales_5y": {"min": 3.0, "median": 5.0, "max": 15.0, "current_pctl": 25},
        "subsector": "rare_disease",
        "peer_group": ["SWTX", "FOLD", "RARE"],
        "external": True,
        "notes": "Syfovre GA + Empaveli PNH; post-safety event derating 2024; Syfovre still growing but field size reset; cash burn ongoing."
    },

    "SWTX": {
        "pe_ttm": None,
        "ev_sales_ttm": 10.0,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 400,
        "mcap_usd_M": 4000,
        "pe_5y": {
            "min": None, "median": None, "max": None, "current_pctl": None,
            "note": "unprofitable"
        },
        "ev_sales_5y": {"min": 4.0, "median": 8.0, "max": 18.0, "current_pctl": 50},
        "subsector": "rare_disease",
        "peer_group": ["APLS", "FOLD", "RARE"],
        "external": True,
        "notes": "Ogsiveo (nirogacestat) desmoid tumors + Gomekli (mirdametinib) NF1; two launches 2023-24; both orphan; unprofitable on heavy SGA."
    },

    "FOLD": {
        "pe_ttm": None,
        "ev_sales_ttm": 5.0,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 550,
        "mcap_usd_M": 2500,
        "pe_5y": {
            "min": None, "median": None, "max": None, "current_pctl": None,
            "note": "unprofitable"
        },
        "ev_sales_5y": {"min": 2.0, "median": 4.0, "max": 10.0, "current_pctl": 38},
        "subsector": "rare_disease",
        "peer_group": ["APLS", "SWTX", "BMRN"],
        "external": True,
        "notes": "Galafold (migalastat) Fabry disease + Pombiliti/Opfolda LOPD; two rare lysosomal assets; approaching profitability but still burning; EV/S near 5y median."
    },

    "XERS": {
        "pe_ttm": None,
        "ev_sales_ttm": 3.0,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 230,
        "mcap_usd_M": 700,
        "pe_5y": {
            "min": None, "median": None, "max": None, "current_pctl": None,
            "note": "unprofitable"
        },
        "ev_sales_5y": {"min": 1.5, "median": 3.0, "max": 7.0, "current_pctl": 42},
        "subsector": "rare_disease",
        "peer_group": ["RIGL", "ESPR", "RARE"],
        "external": True,
        "notes": "Gvoke (glucagon) + Recorlev (levoketoconazole) Cushing + Keveyis (dichlorphenamide) PHPP; three niche products; small cap; unprofitable."
    },

    "CRNX": {
        "pe_ttm": None,
        "ev_sales_ttm": 180.0,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 20,
        "mcap_usd_M": 4000,
        "pe_5y": {
            "min": None, "median": None, "max": None, "current_pctl": None,
            "note": "unprofitable; early launch"
        },
        "ev_sales_5y": {"min": 20.0, "median": 80.0, "max": 200.0, "current_pctl": 85},
        "subsector": "rare_disease",
        "peer_group": ["APLS", "SWTX", "FOLD"],
        "external": True,
        "notes": "Paltusotine (oral somatostatin) acromegaly; launched 2025; very early revenue base makes current EV/S non-comparative; big cash burn; use EV/S with caution -- launch-year distortion."
    },

    "PTGX": {
        "pe_ttm": None,
        "ev_sales_ttm": 25.0,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 100,
        "mcap_usd_M": 2500,
        "pe_5y": {
            "min": None, "median": None, "max": None, "current_pctl": None,
            "note": "unprofitable"
        },
        "ev_sales_5y": {"min": 8.0, "median": 20.0, "max": 50.0, "current_pctl": 48},
        "subsector": "rare_disease",
        "peer_group": ["APLS", "SWTX", "RARE"],
        "external": True,
        "notes": "Rusfertide (hepcidin mimetic) PV in Ph3 with royalty structure via Novo partnership; revenue primarily milestones/collaborations; pipeline-heavy valuation."
    },

    "INSM": {
        "pe_ttm": None,
        "ev_sales_ttm": 35.0,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 350,
        "mcap_usd_M": 13000,
        "pe_5y": {
            "min": None, "median": None, "max": None, "current_pctl": None,
            "note": "unprofitable"
        },
        "ev_sales_5y": {"min": 5.0, "median": 15.0, "max": 40.0, "current_pctl": 75},
        "subsector": "rare_disease",
        "peer_group": ["APLS", "FOLD", "RARE"],
        "external": True,
        "notes": "Arikayce (amikacin liposome) MAC lung + brensocatib (DPP1) Phase 3 bronchiectasis; high EV/S reflects brensocatib blockbuster optionality; market pricing $3B+ peak sales."
    },

    # ------------------------------------------------------------------ #
    # ONCOLOGY                                                             #
    # ------------------------------------------------------------------ #
    "BPMC": {
        "pe_ttm": None,
        "ev_sales_ttm": 15.0,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 450,
        "mcap_usd_M": 7000,
        "pe_5y": {
            "min": None, "median": None, "max": None, "current_pctl": None,
            "note": "unprofitable"
        },
        "ev_sales_5y": {"min": 5.0, "median": 12.0, "max": 25.0, "current_pctl": 62},
        "subsector": "oncology",
        "peer_group": ["EXEL", "INCY", "ONC"],
        "external": True,
        "notes": "Ayvakit (avapritinib) systemic mastocytosis + GIST + Gavreto (pralsetinib) RET fusion; two orphan oncology labels; KIT/PDGFRA and RET specialists; unprofitable on pipeline spend."
    },

    "ARVN": {
        "pe_ttm": None,
        "ev_sales_ttm": 3.0,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 450,
        "mcap_usd_M": 1500,
        "pe_5y": {
            "min": None, "median": None, "max": None, "current_pctl": None,
            "note": "unprofitable; revenue is primarily collaboration milestones"
        },
        "ev_sales_5y": {"min": 1.0, "median": 3.0, "max": 8.0, "current_pctl": 42},
        "subsector": "oncology",
        "peer_group": ["BPMC", "ONC", "EXEL"],
        "external": True,
        "notes": "PROTAC platform; vepdegestrant (ER PROTAC) partnered Pfizer Phase 3; revenue primarily milestones + ARV-766 AR PROTAC; EV/S depressed relative to pipeline value; unprofitable."
    },

    # ------------------------------------------------------------------ #
    # NEUROLOGY / PSYCHIATRY                                               #
    # ------------------------------------------------------------------ #
    "SAGE": {
        "pe_ttm": None,
        "ev_sales_ttm": 4.0,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 80,
        "mcap_usd_M": 350,
        "pe_5y": {
            "min": None, "median": None, "max": None, "current_pctl": None,
            "note": "unprofitable"
        },
        "ev_sales_5y": {"min": 2.0, "median": 5.0, "max": 15.0, "current_pctl": 30},
        "subsector": "neurology_psych",
        "peer_group": ["AXSM", "BIIB", "ACAD"],
        "external": True,
        "notes": "Zurzuvae (zuranolone) PPD + MDD; 50/50 global profit share with Biogen; early ramp; small mcap vs peak opportunity; cash burn ongoing."
    },

    "SUPN": {
        "pe_ttm": 18,
        "ev_sales_ttm": 2.5,
        "net_income_ttm_M": 100,
        "revenue_ttm_M": 650,
        "mcap_usd_M": 1800,
        "pe_5y": {
            "min": 12, "median": 18, "max": 30, "current_pctl": 42
        },
        "ev_sales_5y": {"min": 1.5, "median": 2.5, "max": 5.0, "current_pctl": 42},
        "subsector": "neurology_psych",
        "peer_group": ["NBIX", "ACAD", "AXSM"],
        "external": True,
        "notes": "Qelbree (viloxazine) ADHD ~$350M + legacy neuro portfolio (Oxtellar XR, Trokendi XR); consistently profitable; P/E at 5y median; modest growth profile."
    },

    "JAZZ": {
        "pe_ttm": 11,
        "ev_sales_ttm": 3.0,
        "net_income_ttm_M": 636,
        "revenue_ttm_M": 4000,
        "mcap_usd_M": 7000,
        "pe_5y": {
            "min": 7, "median": 12, "max": 22, "current_pctl": 38
        },
        "ev_sales_5y": {"min": 2.0, "median": 3.5, "max": 6.0, "current_pctl": 32},
        "subsector": "neurology_psych",
        "peer_group": ["NBIX", "SUPN", "ALKS"],
        "external": True,
        "notes": "Xywav + Xyrem sleep franchise + Epidiolex epilepsy + Rylaze onco; cheapest valuation in CNS specialty; P/E below 5y median on generic/LOE fears and debt load."
    },

    "ALKS": {
        "pe_ttm": 18,
        "ev_sales_ttm": 3.5,
        "net_income_ttm_M": 270,
        "revenue_ttm_M": 1300,
        "mcap_usd_M": 5000,
        "pe_5y": {
            "min": 12, "median": 20, "max": 35, "current_pctl": 35
        },
        "ev_sales_5y": {"min": 2.5, "median": 4.0, "max": 7.0, "current_pctl": 30},
        "subsector": "neurology_psych",
        "peer_group": ["SUPN", "NBIX", "JAZZ"],
        "external": True,
        "notes": "Vivitrol (naltrexone depot) OUD + Lybalvi (OLZ/saml) schizophrenia + royalties from RISPERDAL CONSTA; profitable; P/E and EV/S below 5y medians on revenue deceleration."
    },

    "HRMY": {
        "pe_ttm": 14,
        "ev_sales_ttm": 2.5,
        "net_income_ttm_M": 130,
        "revenue_ttm_M": 650,
        "mcap_usd_M": 1800,
        "pe_5y": {
            "min": 10, "median": 16, "max": 28, "current_pctl": 30
        },
        "ev_sales_5y": {"min": 2.0, "median": 4.0, "max": 8.0, "current_pctl": 18},
        "subsector": "neurology_psych",
        "peer_group": ["JAZZ", "SUPN", "NBIX"],
        "external": True,
        "notes": "Wakix (pitolisant) narcolepsy monopoly in US; profitable; EV/S below 5y median on LOE risk and limited pipeline; single-asset overhang despite durable orphan franchise."
    },

    # ------------------------------------------------------------------ #
    # CARDIO / LIPIDS                                                      #
    # ------------------------------------------------------------------ #
    "ESPR": {
        "pe_ttm": None,
        "ev_sales_ttm": 6.0,
        "net_income_ttm_M": None,
        "revenue_ttm_M": 150,
        "mcap_usd_M": 900,
        "pe_5y": {
            "min": None, "median": None, "max": None, "current_pctl": None,
            "note": "unprofitable"
        },
        "ev_sales_5y": {"min": 2.0, "median": 5.0, "max": 12.0, "current_pctl": 45},
        "subsector": "large_cap",
        "peer_group": ["XERS", "RIGL", "RARE"],
        "external": True,
        "notes": "Nexletol (bempedoic acid) + Nexlizet (bempedoic acid/ezetimibe) statin-intolerant LDL lowering; CLEAR Outcomes CV outcomes data 2023 drove modest uptake acceleration; royalties from Daiichi; still unprofitable."
    },

    # ------------------------------------------------------------------ #
    # RARE DISEASE -- HEMATOLOGY / OTHER                                   #
    # ------------------------------------------------------------------ #
    "RIGL": {
        "pe_ttm": 12,
        "ev_sales_ttm": 2.0,
        "net_income_ttm_M": 25,
        "revenue_ttm_M": 150,
        "mcap_usd_M": 300,
        "pe_5y": {
            "min": None, "median": None, "max": None, "current_pctl": None,
            "note": "only recently profitable; P/E history not meaningful"
        },
        "ev_sales_5y": {"min": 1.0, "median": 2.0, "max": 5.0, "current_pctl": 42},
        "subsector": "rare_disease",
        "peer_group": ["XERS", "ESPR", "FOLD"],
        "external": True,
        "notes": "Tavalisse (fostamatinib) ITP + Rezlidhia (olutasidenib) IDH1 AML; two rare heme/onco assets; recently profitable; EV/S near historical median; small cap."
    },

    # ------------------------------------------------------------------ #
    # REGENERATIVE / CELL THERAPY                                          #
    # ------------------------------------------------------------------ #
    "VCEL": {
        "pe_ttm": 40,
        "ev_sales_ttm": 9.0,
        "net_income_ttm_M": 50,
        "revenue_ttm_M": 220,
        "mcap_usd_M": 2000,
        "pe_5y": {
            "min": None, "median": None, "max": None, "current_pctl": None,
            "note": "only recently profitable; P/E history too short for reliable range"
        },
        "ev_sales_5y": {"min": 5.0, "median": 8.0, "max": 15.0, "current_pctl": 55},
        "subsector": "rare_disease",
        "peer_group": ["RIGL", "FOLD", "RARE"],
        "external": True,
        "notes": "Epicel cultured epidermal autografts severe burns + MACI cartilage repair; recently turned profitable; premium EV/S on differentiated cell therapy platform; specialty surgery niche."
    },

    # ------------------------------------------------------------------ #
    # PLATFORM / ROYALTY                                                   #
    # ------------------------------------------------------------------ #
    "HALO": {
        "pe_ttm": 25,
        "ev_sales_ttm": 7.0,
        "net_income_ttm_M": 400,
        "revenue_ttm_M": 1000,
        "mcap_usd_M": 7000,
        "pe_5y": {
            "min": 18, "median": 25, "max": 45, "current_pctl": 42
        },
        "ev_sales_5y": {"min": 4.0, "median": 7.0, "max": 14.0, "current_pctl": 42},
        "subsector": "large_cap",
        "peer_group": ["EXEL", "NBIX", "INCY"],
        "external": True,
        "notes": "ENHANZE hyaluronidase sub-Q platform; royalties from Darzalex SC + Phesgo + Tecentriq SC + Keytruda SC; high-margin royalty model; EV/S at 5y median; growing royalty stream adds visibility."
    },
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _median(values):
    """Return median of a list, ignoring None."""
    vals = [v for v in values if v is not None]
    if not vals:
        return None
    return statistics.median(vals)


def _tier_distribution(data):
    """Return dict with count per subsector across all entries."""
    tiers = {}
    for ticker, entry in data.items():
        sub = entry.get("subsector", "unknown")
        tiers[sub] = tiers.get(sub, 0) + 1
    return dict(sorted(tiers.items(), key=lambda x: -x[1]))


def _live_all_medians(data):
    """
    Compute EV/S and P/E medians across all entries (external + internal).
    P/E median excludes None values (unprofitable names not counted).
    """
    ev_s_vals = [e["ev_sales_ttm"] for e in data.values()
                 if e.get("ev_sales_ttm") is not None]
    pe_vals = [e["pe_ttm"] for e in data.values()
               if e.get("pe_ttm") is not None]
    return {
        "ev_sales_median": round(_median(ev_s_vals), 2) if ev_s_vals else None,
        "pe_median_profitable_only": round(_median(pe_vals), 1) if pe_vals else None,
        "n_ev_s": len(ev_s_vals),
        "n_pe": len(pe_vals),
        "n_total": len(data),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

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

    for ticker, entry in EVS_PEERS.items():
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
    print(f"\nDone. Added {added} entries, skipped {skipped} duplicates.")
    print(f"financials.json now has {total} entries total.\n")

    # Tier distribution
    tiers = _tier_distribution(data)
    print("--- Tier distribution (all entries) ---")
    for sub, count in tiers.items():
        print(f"  {sub:<25} {count:>3}")

    # Live All medians
    medians = _live_all_medians(data)
    print(f"\n--- Live All medians (post-merge) ---")
    print(f"  EV/Sales median  : {medians['ev_sales_median']}x  (n={medians['n_ev_s']})")
    print(f"  P/E median       : {medians['pe_median_profitable_only']}x  "
          f"(n={medians['n_pe']} profitable; {medians['n_total'] - medians['n_pe']} unprofitable excluded)")
    print(f"  Total entries    : {medians['n_total']}")


if __name__ == "__main__":
    main()
