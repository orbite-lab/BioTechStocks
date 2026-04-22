#!/usr/bin/env python3
"""
Regenerate taxonomy.json from all company configs.
Supports L1.L2.L3 and L1.L2.L3.L4 hierarchical tags.
Run after adding/modifying configs: python scripts/rebuild_taxonomy.py
"""
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS = ROOT / "configs"
OUT = ROOT / "data" / "taxonomy.json"

def rebuild():
    manifest = json.loads((CONFIGS / "manifest.json").read_text(encoding="utf-8"))

    areas = defaultdict(lambda: {"companies": set(), "rare": False})
    mods = defaultdict(lambda: {"companies": set()})

    for tk in manifest:
        d = json.loads((CONFIGS / f"{tk}.json").read_text(encoding="utf-8"))
        for a in d["assets"]:
            if a.get("modality"):
                mods[a["modality"]]["companies"].add(tk)
            for ind in a["indications"]:
                if ind.get("area"):
                    area = ind["area"]
                    areas[area]["companies"].add(tk)
                    if ind.get("rare"):
                        areas[area]["rare"] = True
                    # Also register L3 parent if this is an L4 area
                    parts = area.split(".")
                    if len(parts) == 4:
                        l3_parent = ".".join(parts[:3])
                        areas[l3_parent]["companies"].add(tk)
                        if ind.get("rare"):
                            areas[l3_parent]["rare"] = True

    def build_tree(flat, is_area=False):
        tree = {}
        for key in sorted(flat.keys()):
            parts = key.split(".")
            if len(parts) == 3:
                l1, l2, l3 = parts
                node = {
                    "companies": sorted(flat[key]["companies"]),
                    "count": len(flat[key]["companies"]),
                    **({"rare": flat[key]["rare"]} if is_area else {})
                }
                # Check for L4 children
                l4_children = {k: v for k, v in flat.items() if k.startswith(key + ".") and len(k.split(".")) == 4}
                if l4_children:
                    subs = {}
                    for l4_key, l4_val in sorted(l4_children.items()):
                        l4_name = l4_key.split(".")[3]
                        subs[l4_name] = {
                            "companies": sorted(l4_val["companies"]),
                            "count": len(l4_val["companies"]),
                            **({"rare": l4_val["rare"]} if is_area else {})
                        }
                    node["sub"] = subs
                tree.setdefault(l1, {}).setdefault(l2, {})[l3] = node
            # L4 entries are handled as sub-nodes above, skip standalone
        return tree

    l3_count = len([k for k in areas if len(k.split(".")) == 3])
    l4_count = len([k for k in areas if len(k.split(".")) == 4])
    mod3_count = len([k for k in mods if len(k.split(".")) == 3])

    taxonomy = {
        "_meta": {
            "description": "Master taxonomy for BioTechStocks screener -- L1.L2.L3(.L4) hierarchical tags",
            "format": "L1.L2.L3 with optional L4 sub-segments",
            "rules": [
                "Every L3 term must appear under exactly ONE L1.L2 parent (no duplicates across branches)",
                "L4 sub-segments nest under L3 when a market has distinct drug niches (e.g. dmd.gene_therapy, dmd.exon51)",
                "Disease classification follows the organ/system affected, not the treatment mechanism",
                "No 'multi_indication' catch-alls -- use the lead/primary indication",
                "Rare diseases get 'rare: true' on the indication object, not the area tag",
                "Commercial products need penPct set to actual market share (revenue / TAM)"
            ],
            "area_count_l3": l3_count,
            "area_count_l4": l4_count,
            "modality_count": mod3_count,
            "companies": len(manifest)
        },
        "therapeutic_areas": build_tree(areas, is_area=True),
        "modalities": build_tree(mods)
    }

    OUT.write_text(json.dumps(taxonomy, indent=2))

    a_tree = taxonomy["therapeutic_areas"]
    m_tree = taxonomy["modalities"]
    print(f"[OK] taxonomy.json rebuilt")
    print(f"   Areas:      {len(a_tree)} L1 -> {sum(len(v) for v in a_tree.values())} L2 -> {l3_count} L3 -> {l4_count} L4")
    print(f"   Modalities: {len(m_tree)} L1 -> {sum(len(v) for v in m_tree.values())} L2 -> {mod3_count} L3")
    print(f"   Rare L3s:   {sum(1 for k,v in areas.items() if v['rare'] and len(k.split('.'))==3)}")
    print(f"   Companies:  {len(manifest)}")

if __name__ == "__main__":
    rebuild()
