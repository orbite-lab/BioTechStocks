# -*- coding: utf-8 -*-
"""
Fix lipids taxonomy: disease-based buckets, not trial-endpoint or
mechanism-based. Also move anticoagulation out of lipids entirely
(thrombosis is not a lipid disease).

Migrations:
  lipids.ldl_lowering    -> lipids.ldl_cv_risk  (ASCVD risk reduction)
  lipids.cv_outcomes     -> lipids.ldl_cv_risk  (trial endpoint = same pool)
  lipids.anticoagulation -> thrombosis.anticoagulation  (new L2, different disease)

Also fix mis-tagged drugs (broad ASCVD tagged as lpa-specific):
  ARWR aro_dimer  lipids.lpa -> lipids.ldl_cv_risk  (PCSK9+APOC3 dual)
  CRSP ctx310     lipids.lpa -> lipids.ldl_cv_risk  (ANGPTL3 editing)

Keep as-is:
  lipids.lpa           (IONS pelacarsen -- truly Lp(a)-specific patients)
  lipids.triglycerides (FCS/sHTG -- distinct rare severe HTG pool)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIGS = ROOT / "configs"

# Bulk L3 migrations
AREA_MIGRATIONS = {
    "cardio_metabolic.lipids.ldl_lowering":    "cardio_metabolic.lipids.ldl_cv_risk",
    "cardio_metabolic.lipids.cv_outcomes":     "cardio_metabolic.lipids.ldl_cv_risk",
    "cardio_metabolic.lipids.anticoagulation": "cardio_metabolic.thrombosis.anticoagulation",
}

# Drug-specific re-tagging (mis-labeled as lpa when actually broad ASCVD)
DRUG_SPECIFIC = {
    ("ARWR", "aro_dimer"): "cardio_metabolic.lipids.ldl_cv_risk",
    ("CRSP", "ctx310"):    "cardio_metabolic.lipids.ldl_cv_risk",
}

def run():
    manifest = json.loads((CONFIGS / "manifest.json").read_text())
    updated = 0
    for t in manifest:
        path = CONFIGS / (t + ".json")
        d = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for a in d["assets"]:
            for ind in a["indications"]:
                old = ind.get("area", "")
                new = None
                if (t, a["id"]) in DRUG_SPECIFIC:
                    new = DRUG_SPECIFIC[(t, a["id"])]
                elif old in AREA_MIGRATIONS:
                    new = AREA_MIGRATIONS[old]
                if new and new != old:
                    ind["area"] = new
                    changed = True
                    updated += 1
                    print(f"{t:5s} {a['id']:15s} {ind['id']:15s}  {old}  ->  {new}")
        if changed:
            path.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nTotal: {updated} indications migrated")

if __name__ == "__main__":
    run()
