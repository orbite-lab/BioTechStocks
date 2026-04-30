#!/usr/bin/env python
import sys, io
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

"""Find all assets/indications for a disease synonym group.

Usage:
    py scripts/ops/find_disease_family.py sle_spectrum
    py scripts/ops/find_disease_family.py --list

Reads `disease_synonym_groups` from data/taxonomy.json and aggregates
all assets across the linked L3 areas. Useful for cross-organ disease
spectra (SLE, IBD, prostate, NSCLC, etc.) where the clinical taxonomy
intentionally splits indications across multiple L1s.
"""
import json, sys, glob, os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def load_taxonomy():
    return json.loads((ROOT / "data" / "taxonomy.json").read_text(encoding="utf-8"))

def list_groups():
    groups = load_taxonomy().get("disease_synonym_groups", {})
    print(f"\nAvailable disease synonym groups ({len(groups)}):\n")
    for name, meta in sorted(groups.items()):
        desc = meta.get("description", "")
        n_areas = len(meta.get("areas", []))
        print(f"  {name:35s} -- {n_areas} areas -- {desc}")
    print("\nUsage: py scripts/ops/find_disease_family.py <group_name>\n")

def find(group_name):
    groups = load_taxonomy().get("disease_synonym_groups", {})
    if group_name not in groups:
        print(f"ERROR: '{group_name}' not in disease_synonym_groups.")
        print(f"Available: {sorted(groups.keys())}")
        sys.exit(1)
    meta = groups[group_name]
    areas = set(meta.get("areas", []))
    print(f"\n=== {group_name} ===")
    print(f"Description: {meta.get('description', '')}")
    print(f"Areas ({len(areas)}):")
    for a in sorted(areas):
        print(f"  - {a}")
    print()

    by_area = {a: [] for a in areas}
    total_sales = 0
    for cfg_path in sorted(glob.glob(str(ROOT / "configs" / "*.json"))):
        if "manifest" in cfg_path: continue
        tk = os.path.basename(cfg_path).replace(".json", "")
        try:
            c = json.loads(Path(cfg_path).read_text(encoding="utf-8"))
        except Exception:
            continue
        for ast in c.get("assets", []):
            for ind in ast["indications"]:
                area = ind.get("area")
                if area in areas:
                    sales = ind["market"].get("salesM", 0)
                    total_sales += sales
                    by_area[area].append({
                        "ticker": tk,
                        "asset_id": ast["id"],
                        "asset_name": ast.get("name", "")[:60],
                        "modality": ast.get("modality", ""),
                        "targets": ast.get("targets", []),
                        "ind_id": ind["id"],
                        "salesM": sales,
                        "stage": ast.get("stage", ""),
                    })

    n_assets = sum(len(v) for v in by_area.values())
    print(f"Total: {n_assets} indication-entries; combined visible salesM ${total_sales/1000:.1f}B\n")

    for area in sorted(areas):
        entries = by_area[area]
        if not entries:
            print(f"  [{area}] -- (no assets tagged)\n")
            continue
        print(f"  [{area}] -- {len(entries)} entries:")
        for e in sorted(entries, key=lambda x: -x["salesM"]):
            tgts = ", ".join(e["targets"]) if e["targets"] else "-"
            sales_str = f"${e['salesM']}M" if e["salesM"] > 0 else "(pipeline)"
            print(f"    {e['ticker']:6s} {e['asset_id']:25s} {e['asset_name']:50s} {sales_str:10s} targets=[{tgts}]")
        print()

if __name__ == "__main__":
    if len(sys.argv) == 1 or sys.argv[1] in ("--list", "-l"):
        list_groups()
    else:
        find(sys.argv[1])
