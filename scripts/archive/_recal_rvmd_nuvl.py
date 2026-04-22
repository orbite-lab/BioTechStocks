# -*- coding: utf-8 -*-
"""Targeted recalibration for RVMD + NUVL: bump SOM reachPct to align peak
revenue with sell-side consensus, and bump PoS for NDA-filed assets.

Diagnosis: scenario TPs were 50-70% below current price because the
company_slice peak revenue was set far below consensus expectations
(e.g. RVMD darax PDAC at $1.1B vs $5-8B consensus). Multiples and DR
were not the issue.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS = ROOT / "configs"


def som_of(m):
    if "company_slice" not in m or "regions" not in m: return 0
    t = 0
    for rk, cs in m["company_slice"].items():
        tr = m["regions"].get(rk)
        if not tr or not cs: continue
        t += (tr.get("patientsK", 0) or 0) * (cs.get("reachPct", 0) / 100) \
             * (cs.get("wtpPct", 0) / 100) * (cs.get("priceK", 0) or 0)
    return t


def rescale_reach(m, target_som):
    cur = som_of(m)
    if cur <= 0 or target_som <= 0: return
    sc = target_som / cur
    for rk, cs in m["company_slice"].items():
        new_reach = cs.get("reachPct", 0) * sc
        cs["reachPct"] = round(min(new_reach, 100), 1)


# Target peak revenues per asset (sell-side consensus midpoint, $M WW)
RVMD_TARGETS = {
    ("darax_pdac", "pdac"):  6000,   # daraxonrasib in PDAC -- consensus $5-8B peak
    ("darax_nsclc", "nsclc"): 2500,  # darax in 2L+ KRAS-mut NSCLC
    ("zoldon", "g12d"):      1500,   # zoldonrasib RAS G12D in CRC + PDAC
    ("eliron", "g12c"):       400,   # G12C niche after sotorasib/adagrasib
    ("pipeline", "other_ras"): 200,  # speculative additional RAS programs
}

NUVL_TARGETS = {
    ("zides", "ros1"):  700,   # zidesamtinib ROS1 (NDA filed, best-in-class)
    ("nelad", "alk"):   1300,  # neladalkib ALK resistant
    ("nvl330", "her2"):  350,  # NVL-330 HER2 NSCLC (early stage)
}

# PoS bumps for NDA-filed / late-Phase-3 assets (was too conservative)
RVMD_POS = {
    # asset_id, ind_id : {scenario: (pos, apr)}  -- only override where bumping
    ("darax_pdac", "pdac"): {
        "mega_bear": (25, 35), "bear": (60, 70), "base": (82, 90),
        "bull": (88, 92), "psychedelic_bull": (92, 95),
    },
    ("darax_nsclc", "nsclc"): {
        "mega_bear": (20, 30), "bear": (50, 60), "base": (75, 82),
        "bull": (82, 88), "psychedelic_bull": (88, 92),
    },
    ("zoldon", "g12d"): {
        "mega_bear": (15, 25), "bear": (40, 55), "base": (70, 78),
        "bull": (78, 85), "psychedelic_bull": (85, 90),
    },
}

NUVL_POS = {
    ("zides", "ros1"): {  # NDA filed PDUFA Sep 2026 -- nearly approved
        "mega_bear": (88, 70), "bear": (92, 88), "base": (97, 95),
        "bull": (98, 97), "psychedelic_bull": (99, 98),
    },
    ("nelad", "alk"): {  # NDA planned H1 2026
        "mega_bear": (75, 50), "bear": (82, 80), "base": (90, 90),
        "bull": (94, 94), "psychedelic_bull": (97, 96),
    },
}


def apply(tk, sales_targets, pos_overrides):
    p = CONFIGS / f"{tk}.json"
    c = json.loads(p.read_text(encoding="utf-8"))
    print(f"\n=== {tk} ===")

    # Scale SOMs
    for a in c["assets"]:
        for ind in a["indications"]:
            key = (a["id"], ind["id"])
            if key in sales_targets:
                m = ind["market"]
                old_som = som_of(m)
                target = sales_targets[key]
                rescale_reach(m, target)
                new_som = som_of(m)
                print(f"  SOM {key[0]:14s}.{key[1]:14s}  ${old_som:>5.0f}M  ->  ${new_som:>5.0f}M  (target ${target}M)")

    # Apply PoS bumps
    for (aid, iid), per_scen in pos_overrides.items():
        for sk, (pos, apr) in per_scen.items():
            asmp = c["scenarios"][sk]["assumptions"]
            asmp.setdefault(aid, {}).setdefault(iid, {"pen": 1.0})
            asmp[aid][iid]["pos"] = pos
            asmp[aid][iid]["apr"] = apr
        print(f"  PoS {aid}.{iid}: rescaled across all scenarios (mega/bear/base/bull/psy)")

    p.write_text(json.dumps(c, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"  [WROTE] configs/{tk}.json")


def main():
    apply("RVMD", RVMD_TARGETS, RVMD_POS)
    apply("NUVL", NUVL_TARGETS, NUVL_POS)


if __name__ == "__main__":
    main()
