# -*- coding: utf-8 -*-
"""
Fix obesity taxonomy: obesity L3s were mechanism-based (kv7, rnai_obesity,
glp1_incretin) when they should be disease/patient-pool-based.

Merges:
  cardio_metabolic.obesity.kv7          -> cardio_metabolic.obesity.general
  cardio_metabolic.obesity.rnai_obesity -> cardio_metabolic.obesity.general
  cardio_metabolic.obesity.glp1_incretin-> cardio_metabolic.obesity.general
  cardio_metabolic.obesity.mc4r         -> cardio_metabolic.obesity.rare_genetic

The first three all target mass-market obesity (same 40M+ US eligible pool).
MC4R pathway is a distinct rare genetic subset, renamed for clarity.
Mechanisms remain distinguished via the modality tag on each asset.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIGS = ROOT / "configs"

MIGRATIONS = {
    "cardio_metabolic.obesity.kv7":           "cardio_metabolic.obesity.general",
    "cardio_metabolic.obesity.rnai_obesity":  "cardio_metabolic.obesity.general",
    "cardio_metabolic.obesity.glp1_incretin": "cardio_metabolic.obesity.general",
    "cardio_metabolic.obesity.mc4r":          "cardio_metabolic.obesity.rare_genetic",
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
                if old in MIGRATIONS:
                    new = MIGRATIONS[old]
                    ind["area"] = new
                    changed = True
                    updated += 1
                    print(f"{t:5s} {a['id']:15s} {ind['id']:15s}  {old}  ->  {new}")
            # Also fix BHVN's Opakalim modality — it's Kv7 for epilepsy, drug doesn't need area change (already cns.epilepsy.focal)
            # But the taldefgrobep asset had wrong area .kv7 (handled by migration above)
        if changed:
            path.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nTotal: {updated} indications migrated")

if __name__ == "__main__":
    run()
