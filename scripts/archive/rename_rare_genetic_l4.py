# -*- coding: utf-8 -*-
"""
Simplify rare_genetic L4 labels into 3 clean disease buckets:

  bbs_pomc_lepr + other_mc4r  ->  monogenic_mc4r
    (all monogenic MC4R pathway: BBS, POMC/LEPR/PCSK1, SRC1, SH2B1, Alstrom
     -- Imcivree's expanding label targets all of these)

  acquired_ho  ->  hypothalamic_obesity
    (post-craniopharyngioma/tumor -- NOT genetic, distinct from monogenic)

  pws  ->  prader_willi
    (Prader-Willi syndrome -- distinct genetic syndrome, not strictly MC4R)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIGS = ROOT / "configs"

RENAMES = {
    "cardio_metabolic.obesity.rare_genetic.bbs_pomc_lepr": "cardio_metabolic.obesity.rare_genetic.monogenic_mc4r",
    "cardio_metabolic.obesity.rare_genetic.other_mc4r":    "cardio_metabolic.obesity.rare_genetic.monogenic_mc4r",
    "cardio_metabolic.obesity.rare_genetic.acquired_ho":   "cardio_metabolic.obesity.rare_genetic.hypothalamic_obesity",
    "cardio_metabolic.obesity.rare_genetic.pws":           "cardio_metabolic.obesity.rare_genetic.prader_willi",
}

# Merged monogenic_mc4r pool (combines bbs_pomc_lepr 1.8K + other_mc4r 2.5K)
MERGED_EPI = {
    "cardio_metabolic.obesity.rare_genetic.monogenic_mc4r": {
        # BBS 1.5K + POMC/PCSK1/LEPR 0.3K + SRC1/SH2B1/Alstrom 2.5K = ~4.3K US
        "us":  {"patientsK": 4.3, "wtpPct": 65, "priceK": 420},
        "eu":  {"patientsK": 3.5, "wtpPct": 48, "priceK": 260},
        "row": {"patientsK": 5.5, "wtpPct": 11, "priceK": 110},
    },
    "cardio_metabolic.obesity.rare_genetic.hypothalamic_obesity": {
        "us":  {"patientsK": 10, "wtpPct": 65, "priceK": 400},
        "eu":  {"patientsK": 9,  "wtpPct": 45, "priceK": 250},
        "row": {"patientsK": 12, "wtpPct": 10, "priceK": 100},
    },
    "cardio_metabolic.obesity.rare_genetic.prader_willi": {
        "us":  {"patientsK": 15, "wtpPct": 70, "priceK": 90},
        "eu":  {"patientsK": 12, "wtpPct": 50, "priceK": 55},
        "row": {"patientsK": 20, "wtpPct": 12, "priceK": 22},
    },
}

def run():
    manifest = json.loads((CONFIGS / "manifest.json").read_text())
    for t in manifest:
        path = CONFIGS / (t + ".json")
        d = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for a in d["assets"]:
            for ind in a["indications"]:
                old = ind.get("area", "")
                if old in RENAMES:
                    new = RENAMES[old]
                    ind["area"] = new
                    changed = True
                    print(f"{t:5s} {a['id']:15s}  {old.split('.')[-1]} -> {new.split('.')[-1]}")
                # Apply merged epi (monogenic_mc4r gets combined pool)
                if ind.get("area") in MERGED_EPI:
                    ind["market"]["regions"] = MERGED_EPI[ind["area"]]
                    changed = True
        if changed:
            path.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")

    # Verify
    print("\nVerification:")
    for t in manifest:
        d = json.loads((CONFIGS / (t + ".json")).read_text(encoding="utf-8"))
        for a in d["assets"]:
            for ind in a["indications"]:
                area = ind.get("area", "")
                if ".rare_genetic." not in area:
                    continue
                m = ind["market"]
                r = m.get("regions", {})
                cs = m.get("company_slice", {})
                salesM = m.get("salesM", 0)
                som = sum(r.get(rk,{}).get("patientsK",0)*(cs.get(rk,{}).get("reachPct",0)/100)*(cs.get(rk,{}).get("wtpPct",0)/100)*cs.get(rk,{}).get("priceK",0) for rk in ["us","eu","row"])
                tam = sum(r.get(rk,{}).get("patientsK",0)*(r.get(rk,{}).get("wtpPct",0)/100)*r.get(rk,{}).get("priceK",0) for rk in ["us","eu","row"])
                sub = area.split(".")[-1]
                flag = "OK" if som >= salesM else "SALES>SOM"
                print(f"  {t:5s} {a['id']:15s} {sub:22s}  TAM=${tam:>5.0f}M  SOM=${som:>5.0f}M  sales=${salesM:>4.0f}M  [{flag}]")

if __name__ == "__main__":
    run()
