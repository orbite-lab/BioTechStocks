#!/usr/bin/env python
import sys, io
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

"""Find disease end-leaves that have NO commercial product -- pure pipeline only.

Usage:
    py scripts/ops/find_pipeline_only_leaves.py
    py scripts/ops/find_pipeline_only_leaves.py --l1 oncology
    py scripts/ops/find_pipeline_only_leaves.py --csv reports/pipeline_only_leaves.csv

A "leaf" is a deepest-level area path that has at least one indication tagged
to it. A leaf is "pipeline-only" if every indication tagged there has:
  - salesM == 0 or absent, AND
  - asset.stage not in {commercial, nda_filed}

For each pipeline-only leaf the script lists the candidates competing there
(ticker, asset, stage, modality, targets), sorted by stage maturity.

Pseudo-areas (`_*` prefix) are excluded -- they are platform/discovery tags,
not real markets.
"""
import json, glob, os, argparse, csv
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[2]

STAGE_RANK = {
    "commercial": 0, "nda_filed": 1, "phase3": 2, "phase2": 3,
    "phase1": 4, "preclinical": 5, "": 6,
}

def stage_key(s: str) -> int:
    s = (s or "").lower()
    for k, v in STAGE_RANK.items():
        if k and k in s: return v
    return 6

def load_configs():
    out = {}
    for cfg in glob.glob(str(ROOT / "configs" / "*.json")):
        if "manifest" in cfg: continue
        tk = os.path.basename(cfg).replace(".json", "")
        try:
            out[tk] = json.loads(Path(cfg).read_text(encoding="utf-8"))
        except Exception:
            continue
    return out

def collect_leaves(configs, l1_filter=None):
    """Return {area: [entry, ...]} for every leaf with >=1 indication."""
    leaves = defaultdict(list)
    for tk, c in configs.items():
        for a in c.get("assets", []):
            stage = a.get("stage", "")
            modality = a.get("modality", "")
            targets = a.get("targets", [])
            for ind in a.get("indications", []):
                area = ind.get("area", "")
                if not area or area.startswith("_"): continue
                if l1_filter and not area.startswith(l1_filter + "."): continue
                m = ind.get("market", {}) or {}
                sales = m.get("salesM", 0) or 0
                leaves[area].append({
                    "ticker": tk,
                    "asset_id": a.get("id", ""),
                    "asset_name": a.get("name", "")[:60],
                    "stage": stage,
                    "modality": modality,
                    "targets": targets,
                    "ind_id": ind.get("id", ""),
                    "ind_name": ind.get("name", "")[:60],
                    "salesM": sales,
                })
    return leaves

def is_pipeline_only(entries):
    for e in entries:
        if (e["salesM"] or 0) > 0: return False
        st = (e["stage"] or "").lower()
        if "commercial" in st or "nda_filed" in st or "approved" in st: return False
    return True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--l1", help="Filter to one L1 (e.g. oncology, immunology)")
    ap.add_argument("--csv", help="Write results to CSV")
    ap.add_argument("--counts", action="store_true", help="Print summary counts only")
    args = ap.parse_args()

    configs = load_configs()
    leaves = collect_leaves(configs, l1_filter=args.l1)
    pipeline_leaves = {a: es for a, es in leaves.items() if is_pipeline_only(es)}

    n_total = len(leaves)
    n_pipe = len(pipeline_leaves)
    n_indications = sum(len(es) for es in pipeline_leaves.values())

    print()
    if args.l1:
        print(f"=== Pipeline-only leaves under L1='{args.l1}' ===")
    else:
        print("=== Pipeline-only leaves (all L1s) ===")
    print(f"Total leaves with any indication:    {n_total}")
    print(f"Pipeline-only leaves (no commercial): {n_pipe}  ({100*n_pipe/max(1,n_total):.0f}%)")
    print(f"Total pipeline indication entries:   {n_indications}")
    print()

    # By L1 breakdown
    by_l1 = defaultdict(int)
    by_l1_total = defaultdict(int)
    for a in leaves: by_l1_total[a.split(".")[0]] += 1
    for a in pipeline_leaves: by_l1[a.split(".")[0]] += 1
    print("By L1:")
    for l1 in sorted(by_l1_total.keys()):
        pipe = by_l1[l1]; tot = by_l1_total[l1]
        bar = "#" * int(20 * pipe / max(1, tot))
        print(f"  {l1:25s} {pipe:3d}/{tot:3d}  {bar}")
    print()

    if args.counts: return

    # Detail
    sorted_leaves = sorted(pipeline_leaves.items(),
                           key=lambda kv: (-len(kv[1]), kv[0]))
    for area, entries in sorted_leaves:
        depth = area.count(".") + 1
        entries_sorted = sorted(entries, key=lambda e: stage_key(e["stage"]))
        print(f"  [{area}] (L{depth}) -- {len(entries)} pipeline candidate(s):")
        for e in entries_sorted:
            tgts = ", ".join(e["targets"]) if e["targets"] else "-"
            mod = e["modality"] or "-"
            stage = e["stage"] or "(no stage)"
            print(f"    {e['ticker']:6s} {e['asset_id']:25s} {e['asset_name']:50s}  {stage:14s} mod={mod:35s} targets=[{tgts}]")
        print()

    if args.csv:
        out = Path(args.csv); out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["area","depth","ticker","asset_id","asset_name","stage","modality","targets","indication_id","indication_name"])
            for area, entries in sorted_leaves:
                depth = area.count(".") + 1
                for e in sorted(entries, key=lambda x: stage_key(x["stage"])):
                    w.writerow([area, depth, e["ticker"], e["asset_id"], e["asset_name"],
                                e["stage"], e["modality"], "|".join(e["targets"]),
                                e["ind_id"], e["ind_name"]])
        print(f"\n[OK] CSV written to {out}")

if __name__ == "__main__":
    main()
