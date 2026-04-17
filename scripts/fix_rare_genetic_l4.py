# -*- coding: utf-8 -*-
"""
Split cardio_metabolic.obesity.rare_genetic into L4 sub-populations.

Distinct patient pools:
  .bbs_pomc_lepr  Bardet-Biedl + POMC/PCSK1/LEPR deficiency (Imcivree original label)
  .acquired_ho    Acquired hypothalamic obesity (craniopharyngioma, tumor)
  .pws            Prader-Willi syndrome (NBIX VYKAT + RYTM pws)
  .other_mc4r     EMANATE rare MC4R pathway (SRC1, SH2B1, Alstrom)

Drug assignments:
  RYTM commercial (Imcivree BBS+POMC/LEPR franchise) -> .bbs_pomc_lepr
  RYTM acq_ho (Imcivree acquired HO sNDA)            -> .acquired_ho
  RYTM bivam (oral Imcivree for acq_ho)              -> .acquired_ho
  RYTM pws (Imcivree + RM-718 for PWS)               -> .pws
  NBIX vykat (diazoxide choline for PWS)             -> .pws
  RYTM emanate (4 additional rare MC4R pathway)      -> .other_mc4r

Also corrects rare_genetic patient counts (500K was way too high -- actual
MC4R pathway rare diseases are <35K US combined).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIGS = ROOT / "configs"

DRUG_MIGRATIONS = {
    ("RYTM", "commercial"): "cardio_metabolic.obesity.rare_genetic.bbs_pomc_lepr",
    ("RYTM", "acq_ho"):     "cardio_metabolic.obesity.rare_genetic.acquired_ho",
    ("RYTM", "bivam"):      "cardio_metabolic.obesity.rare_genetic.acquired_ho",
    ("RYTM", "pws"):        "cardio_metabolic.obesity.rare_genetic.pws",
    ("RYTM", "emanate"):    "cardio_metabolic.obesity.rare_genetic.other_mc4r",
    ("NBIX", "vykat"):      "cardio_metabolic.obesity.rare_genetic.pws",
}

# New L4 epi data (replaces the inflated 500K L3 estimate)
L4_EPI = {
    "cardio_metabolic.obesity.rare_genetic.bbs_pomc_lepr": {
        # BBS ~1.5K US + POMC/PCSK1/LEPR ~0.3K = ~1.8K; Imcivree original label
        "us":  {"patientsK": 1.8, "wtpPct": 75, "priceK": 420},
        "eu":  {"patientsK": 1.5, "wtpPct": 55, "priceK": 260},
        "row": {"patientsK": 2.5, "wtpPct": 12, "priceK": 110},
    },
    "cardio_metabolic.obesity.rare_genetic.acquired_ho": {
        # Acquired hypothalamic obesity (post-craniopharyngioma, tumor) ~10K US
        "us":  {"patientsK": 10, "wtpPct": 65, "priceK": 400},
        "eu":  {"patientsK": 9,  "wtpPct": 45, "priceK": 250},
        "row": {"patientsK": 12, "wtpPct": 10, "priceK": 100},
    },
    "cardio_metabolic.obesity.rare_genetic.pws": {
        # Prader-Willi ~15K US diagnosed (most treated)
        "us":  {"patientsK": 15, "wtpPct": 70, "priceK": 90},
        "eu":  {"patientsK": 12, "wtpPct": 50, "priceK": 55},
        "row": {"patientsK": 20, "wtpPct": 12, "priceK": 22},
    },
    "cardio_metabolic.obesity.rare_genetic.other_mc4r": {
        # SRC1, SH2B1, Alstrom, remaining MC4R pathway ~2-3K US (EMANATE basket)
        "us":  {"patientsK": 2.5, "wtpPct": 55, "priceK": 420},
        "eu":  {"patientsK": 2,   "wtpPct": 40, "priceK": 260},
        "row": {"patientsK": 3,   "wtpPct": 10, "priceK": 110},
    },
}

# Drug-specific company_slice recalibrations to stay within each L4 TAM
SLICE_OVERRIDES = {
    # RYTM commercial (BBS+POMC/LEPR) -- $195M 2025 sales, near-saturation
    ("RYTM", "commercial", "rare_ob"): {
        "us":  {"reachPct": 55, "wtpPct": 70, "priceK": 420},
        "eu":  {"reachPct": 40, "wtpPct": 50, "priceK": 260},
        "row": {"reachPct": 10, "wtpPct": 12, "priceK": 110},
    },
    # RYTM acq_ho Imcivree sNDA -- PDUFA Mar 2026, larger pop than BBS
    ("RYTM", "acq_ho", "ho"): {
        "us":  {"reachPct": 35, "wtpPct": 55, "priceK": 400},
        "eu":  {"reachPct": 25, "wtpPct": 40, "priceK": 250},
        "row": {"reachPct": 5,  "wtpPct": 10, "priceK": 100},
    },
    # RYTM bivam oral -- Phase 2 OLE, future switch/new starts
    ("RYTM", "bivam", "oral_mc4r"): {
        "us":  {"reachPct": 15, "wtpPct": 40, "priceK": 180},
        "eu":  {"reachPct": 10, "wtpPct": 30, "priceK": 110},
        "row": {"reachPct": 2,  "wtpPct": 8,  "priceK": 45},
    },
    # RYTM pws -- Imcivree PWS Phase 2/3 exploratory
    ("RYTM", "pws", "pws"): {
        "us":  {"reachPct": 20, "wtpPct": 45, "priceK": 400},
        "eu":  {"reachPct": 14, "wtpPct": 32, "priceK": 250},
        "row": {"reachPct": 3,  "wtpPct": 8,  "priceK": 100},
    },
    # RYTM emanate -- 4 new rare MC4R indications
    ("RYTM", "emanate", "mc4r_rare"): {
        "us":  {"reachPct": 40, "wtpPct": 55, "priceK": 420},
        "eu":  {"reachPct": 28, "wtpPct": 42, "priceK": 260},
        "row": {"reachPct": 5,  "wtpPct": 10, "priceK": 110},
    },
    # NBIX VYKAT PWS -- $190M 2025 sales, growing +50%
    ("NBIX", "vykat", "pws"): {
        "us":  {"reachPct": 30, "wtpPct": 60, "priceK": 90},
        "eu":  {"reachPct": 18, "wtpPct": 40, "priceK": 55},
        "row": {"reachPct": 4,  "wtpPct": 10, "priceK": 22},
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
                k = (t, a["id"])
                if k in DRUG_MIGRATIONS:
                    new_area = DRUG_MIGRATIONS[k]
                    old_area = ind.get("area", "")
                    if old_area != new_area:
                        ind["area"] = new_area
                        changed = True
                        print(f"{t:5s} {a['id']:15s} area: {old_area.split('.')[-1] if old_area else '?'} -> {new_area.split('.')[-1]}")

                # Apply L4 epi + slice overrides
                ksi = (t, a["id"], ind["id"])
                if ind.get("area") in L4_EPI:
                    ind["market"]["regions"] = L4_EPI[ind["area"]]
                    changed = True
                if ksi in SLICE_OVERRIDES:
                    ind["market"]["company_slice"] = SLICE_OVERRIDES[ksi]
                    changed = True
        if changed:
            path.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")

    # Verify SOM >= sales
    print("\nValidation:")
    for t in manifest:
        d = json.loads((CONFIGS / (t + ".json")).read_text(encoding="utf-8"))
        for a in d["assets"]:
            for ind in a["indications"]:
                area = ind.get("area", "")
                if ".rare_genetic" not in area:
                    continue
                m = ind["market"]
                r = m.get("regions", {})
                cs = m.get("company_slice", {})
                salesM = m.get("salesM", 0)
                som = sum(r.get(rk,{}).get("patientsK",0)*(cs.get(rk,{}).get("reachPct",0)/100)*(cs.get(rk,{}).get("wtpPct",0)/100)*cs.get(rk,{}).get("priceK",0) for rk in ["us","eu","row"])
                tam = sum(r.get(rk,{}).get("patientsK",0)*(r.get(rk,{}).get("wtpPct",0)/100)*r.get(rk,{}).get("priceK",0) for rk in ["us","eu","row"])
                flag = "OK" if som >= salesM else "SALES>SOM"
                print(f"  {t:5s} {a['id']:15s} {area.split('.')[-1]:15s}  TAM=${tam:>5.0f}M  SOM=${som:>5.0f}M  sales=${salesM:>4.0f}M  [{flag}]")

if __name__ == "__main__":
    run()
