#!/usr/bin/env python3
"""
Regenerate taxonomy.json from all company configs.
Run after adding/modifying configs: python scripts/rebuild_taxonomy.py
"""
import json
from collections import defaultdict
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent.parent
CONFIGS = ROOT / "configs"
OUT = ROOT / "taxonomy.json"

def rebuild():
    manifest = json.loads((CONFIGS / "manifest.json").read_text())
    
    areas = defaultdict(lambda: {"companies": set(), "rare": False})
    mods = defaultdict(lambda: {"companies": set()})
    
    for tk in manifest:
        d = json.loads((CONFIGS / f"{tk}.json").read_text())
        for a in d["assets"]:
            if a.get("modality"):
                mods[a["modality"]]["companies"].add(tk)
            for ind in a["indications"]:
                if ind.get("area"):
                    areas[ind["area"]]["companies"].add(tk)
                    if ind.get("rare"):
                        areas[ind["area"]]["rare"] = True
    
    def build_tree(flat, is_area=False):
        tree = {}
        for key in sorted(flat.keys()):
            parts = key.split(".")
            if len(parts) != 3: continue
            l1, l2, l3 = parts
            tree.setdefault(l1, {}).setdefault(l2, {})[l3] = {
                "companies": sorted(flat[key]["companies"]),
                "count": len(flat[key]["companies"]),
                **({"rare": flat[key]["rare"]} if is_area else {})
            }
        return tree
    
    taxonomy = {
        "_meta": {
            "description": "Master taxonomy for BioTechStocks screener -- L1.L2.L3 hierarchical tags",
            "generated": str(date.today()),
            "format": "L1.L2.L3 hierarchical tags",
            "rules": [
                "Every L3 term must appear under exactly ONE L1.L2 parent (no duplicates across branches)",
                "Disease classification follows the organ/system affected, not the treatment mechanism",
                "No 'multi_indication' catch-alls -- use the lead/primary indication",
                "Rare diseases get 'rare: true' on the indication object, not the area tag",
                "Commercial products need penPct set to actual market share (revenue / TAM)"
            ],
            "area_count": len([k for k in areas if len(k.split(".")) == 3]),
            "modality_count": len([k for k in mods if len(k.split(".")) == 3]),
            "companies": len(manifest)
        },
        "therapeutic_areas": build_tree(areas, is_area=True),
        "modalities": build_tree(mods)
    }
    
    OUT.write_text(json.dumps(taxonomy, indent=2))
    
    a_tree = taxonomy["therapeutic_areas"]
    m_tree = taxonomy["modalities"]
    print(f"[OK] taxonomy.json rebuilt")
    print(f"   Areas:      {len(a_tree)} L1 -> {sum(len(v) for v in a_tree.values())} L2 -> {taxonomy['_meta']['area_count']} L3")
    print(f"   Modalities: {len(m_tree)} L1 -> {sum(len(v) for v in m_tree.values())} L2 -> {taxonomy['_meta']['modality_count']} L3")
    print(f"   Rare L3s:   {sum(1 for k,v in areas.items() if v['rare'] and len(k.split('.'))==3)}")
    print(f"   Companies:  {len(manifest)}")

if __name__ == "__main__":
    rebuild()
