#!/usr/bin/env python3
"""
Rebuild data/targets.json from asset.targets[] across all configs.

Produces an inverted index: target -> { companies, modalities, areas,
assetCount, modalityClassCount, areaCount }.

Parallels scripts/recurring/rebuild_taxonomy.py. Targets are NOT held in a
separate authoritative file; this script treats configs as source of truth
and derives the index.

Run locally before committing, or let CI regenerate + auto-commit on main.
"""
from __future__ import annotations
import json, sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS = ROOT / "configs"
OUT = ROOT / "data" / "targets.json"


def build_index():
    manifest = json.loads((CONFIGS / "manifest.json").read_text(encoding="utf-8"))
    # target -> {companies:set, modalities:set, areas:set, assets:[]}
    idx: dict[str, dict] = defaultdict(lambda: {
        "companies":  set(),
        "modalities": set(),
        "areas":      set(),
        "assets":     [],
    })
    total_assets = 0
    assets_with_targets = 0
    for t in manifest:
        path = CONFIGS / f"{t}.json"
        if not path.exists():
            continue
        cfg = json.loads(path.read_text(encoding="utf-8"))
        for a in cfg.get("assets", []):
            total_assets += 1
            targets = a.get("targets") or []
            if not targets:
                continue
            assets_with_targets += 1
            # Collect the disease areas this asset covers
            areas = sorted({ind.get("area", "") for ind in a.get("indications", [])
                            if ind.get("area")})
            modality = a.get("modality", "")
            for tgt in targets:
                entry = idx[tgt]
                entry["companies"].add(t)
                if modality:
                    entry["modalities"].add(modality)
                for area in areas:
                    entry["areas"].add(area)
                entry["assets"].append({
                    "ticker":   t,
                    "asset":    a.get("id", ""),
                    "name":     a.get("name", ""),
                    "modality": modality,
                    "areas":    areas,
                })

    # Freeze sets into sorted lists and compute derived counts
    out_targets = {}
    for tgt in sorted(idx.keys()):
        entry = idx[tgt]
        companies  = sorted(entry["companies"])
        modalities = sorted(entry["modalities"])
        areas      = sorted(entry["areas"])
        # Count distinct modality L1 classes (small_molecule, peptide, antibody, etc.)
        modality_l1s = sorted({m.split(".")[0] for m in modalities if m})
        out_targets[tgt] = {
            "companies":          companies,
            "modalities":         modalities,
            "areas":              areas,
            "assets":             entry["assets"],
            "assetCount":         len(entry["assets"]),
            "modalityCount":      len(modalities),
            "modalityClassCount": len(modality_l1s),
            "areaCount":          len(areas),
            "modalityClasses":    modality_l1s,
        }

    return out_targets, total_assets, assets_with_targets


def main():
    targets, total, tagged = build_index()
    meta = {
        "generated":             datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "target_count":          len(targets),
        "total_assets":          total,
        "assets_with_targets":   tagged,
        "multi_modality_count":  sum(1 for v in targets.values() if v["modalityClassCount"] >= 2),
        "multi_disease_count":   sum(1 for v in targets.values() if v["areaCount"] >= 2),
    }
    payload = {"_meta": meta, "targets": targets}
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"[OK] targets.json rebuilt")
    print(f"   Targets: {meta['target_count']}")
    print(f"   Multi-modality (>=2 classes):     {meta['multi_modality_count']}")
    print(f"   Multi-disease (>=2 areas):        {meta['multi_disease_count']}")
    print(f"   Assets tagged: {tagged}/{total}")


if __name__ == "__main__":
    sys.exit(main())
