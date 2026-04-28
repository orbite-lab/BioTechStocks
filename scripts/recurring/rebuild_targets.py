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


def _ind_tam_som(market):
    """TAM + SOM in $M for one indication using the regions/company_slice math."""
    regs = (market or {}).get("regions") or {}
    cs   = (market or {}).get("company_slice") or {}
    tam = sum(((regs.get(rk) or {}).get("patientsK", 0))
              * (((regs.get(rk) or {}).get("wtpPct", 0)) / 100)
              * ((regs.get(rk) or {}).get("priceK", 0))
              for rk in ("us", "eu", "row"))
    som = sum(((regs.get(rk) or {}).get("patientsK", 0))
              * (((cs.get(rk) or {}).get("reachPct", 0)) / 100)
              * (((cs.get(rk) or {}).get("wtpPct", 0)) / 100)
              * ((cs.get(rk) or {}).get("priceK", 0))
              for rk in ("us", "eu", "row"))
    return tam, som


def build_index():
    manifest = json.loads((CONFIGS / "manifest.json").read_text(encoding="utf-8"))
    # target -> {companies:set, modalities:set, areas:set, assets:[],
    #            tam_by_area: dict, total_som, total_sales, weighted_cagr_num,
    #            weighted_cagr_denom, weighted_peak_num, weighted_peak_denom}
    idx: dict[str, dict] = defaultdict(lambda: {
        "companies":           set(),
        "modalities":          set(),
        "areas":               set(),
        "assets":              [],
        "tam_by_area":         {},   # area -> tam ($M); first-seen wins (dedupe)
        "total_som":           0.0,
        "total_sales":         0.0,
        "weighted_cagr_num":   0.0,
        "weighted_cagr_denom": 0.0,
        "weighted_peak_num":   0.0,
        "weighted_peak_denom": 0.0,
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
                # Aggregate TAM/SOM/sales/CAGR/peakYear per indication
                for ind in a.get("indications", []):
                    m = ind.get("market") or {}
                    area = ind.get("area", "")
                    tam, som = _ind_tam_som(m)
                    if area and area not in entry["tam_by_area"]:
                        entry["tam_by_area"][area] = tam
                    entry["total_som"] += som
                    entry["total_sales"] += float(m.get("salesM") or 0)
                    cg = float(m.get("cagrPct") or 0)
                    pk = float(m.get("peakYear") or 2033)
                    entry["weighted_cagr_num"] += cg * som
                    entry["weighted_cagr_denom"] += som
                    entry["weighted_peak_num"] += pk * som
                    entry["weighted_peak_denom"] += som

    # Freeze sets into sorted lists and compute derived counts
    out_targets = {}
    for tgt in sorted(idx.keys()):
        entry = idx[tgt]
        companies  = sorted(entry["companies"])
        modalities = sorted(entry["modalities"])
        areas      = sorted(entry["areas"])
        # Count distinct modality L1 classes (small_molecule, peptide, antibody, etc.)
        modality_l1s = sorted({m.split(".")[0] for m in modalities if m})
        # Aggregate TAM (deduped by area), SOM, sales, CAGR/peak (SOM-weighted)
        total_tam = sum(entry["tam_by_area"].values())
        total_som = entry["total_som"]
        total_sales = entry["total_sales"]
        wcd = entry["weighted_cagr_denom"]
        cagr = (entry["weighted_cagr_num"] / wcd) if wcd > 0 else 0.0
        wpd = entry["weighted_peak_denom"]
        peak_year = round(entry["weighted_peak_num"] / wpd) if wpd > 0 else 2033
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
            # Market-size aggregates ($M; deduped TAM, additive SOM/sales)
            "totalTAM":           round(total_tam, 1),
            "totalSOM":           round(total_som, 1),
            "totalSales":         round(total_sales, 1),
            "cagrPct":            round(cagr, 1),
            "peakYear":           int(peak_year),
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
