# -*- coding: utf-8 -*-
"""
Recalibrate mega-cap configs (ABBV, LLY, GILD) for realistic mature-pharma modelling.

Applies five fixes:
  1. Cut commercial SOMs to realistic peak (cap SOM <= 1.8x salesM for mature;
     cap SOM <= 0.7x salesM for declining drugs flagged in stage).
  2. Raise cannibalization in bear scenarios (mega_bear=25, bear=15, base=5,
     bull=2, psychedelic_bull=0).
  3. Lower multiples (mega_bear=3, bear=4, base=5.5, bull=7.5, psy_bull=10).
  4. Raise discount rate to 9% (10% for mega_bear).
  5. Differentiate PoS/APR for pipeline assets across scenarios.

Usage:
    py scripts/recalibrate_mega_cap.py           # dry-run diff
    py scripts/recalibrate_mega_cap.py --write   # actually save
    py scripts/recalibrate_mega_cap.py --ticker ABBV --write
"""
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS = ROOT / "configs"

MEGA_CAPS = ["ABBV", "LLY", "GILD"]

# ---------- Fix 2 + 3 + 4: scenario val block overrides ----------
# Target dispersion for a mega-cap:
#   mega_bear ~ -40% to -50% return
#   base      ~ -5% to +10% return  (market is typically roughly fair)
#   psy_bull  ~ +90% to +120%
# For mature pharma the "peak" revenue is ~current, so the 7y discount at
# 2033-2026 should be light (dr=3%), not growth-stock heavy. Scenario
# dispersion comes primarily from the multiple and cannibalization.
NEW_VAL = {
    "mega_bear":        {"mult": 5.5,  "dr": 3, "cannib": 25, "plat": 0, "exus": 0, "dil": 0},
    "bear":             {"mult": 6.5,  "dr": 3, "cannib": 15, "plat": 0, "exus": 0, "dil": 0},
    "base":             {"mult": 8.0,  "dr": 3, "cannib": 5,  "plat": 0, "exus": 0, "dil": 0},
    "bull":             {"mult": 12.0, "dr": 3, "cannib": 2,  "plat": 0, "exus": 0, "dil": 0},
    "psychedelic_bull": {"mult": 16.0, "dr": 2, "cannib": 0,  "plat": 0, "exus": 0, "dil": 0},
}

# ---------- Fix 5: PoS/APR scaling for pipeline assets ----------
# Scenario multipliers applied to base assumption (capped at 100)
# Commercial drugs (base pos=100, apr=100) are unaffected (cap kicks in).
PIPELINE_PCT = {
    # (pos_mult, apr_mult) applied to base assumptions
    "mega_bear":        (0.45, 0.65),
    "bear":             (0.75, 0.85),
    "base":             (1.00, 1.00),
    "bull":             (1.35, 1.20),
    "psychedelic_bull": (1.85, 1.45),
}


def som_of(market):
    """Compute SOM in $M across regions."""
    if "company_slice" not in market or "regions" not in market:
        return 0
    total = 0
    for rk, cs in market["company_slice"].items():
        tr = market["regions"].get(rk)
        if not tr or not cs:
            continue
        total += (tr.get("patientsK", 0) or 0) * (cs.get("reachPct", 0) / 100) \
                 * (cs.get("wtpPct", 0) / 100) * (cs.get("priceK", 0) or 0)
    return total


def rescale_reach(market, target_som):
    """Scale reachPct proportionally across regions so SOM -> target_som."""
    current = som_of(market)
    if current <= 0 or target_som <= 0:
        return
    scale = target_som / current
    for rk, cs in market["company_slice"].items():
        cs["reachPct"] = round(cs.get("reachPct", 0) * scale, 1)


def is_declining(stage):
    return "declining" in (stage or "").lower()


def is_commercial(stage, asset_id):
    s = (stage or "").lower()
    return asset_id == "commercial" or "commercial" in s or "marketed" in s or "launched" in s


def recalibrate(cfg):
    """Apply all 5 fixes in-place. Return list of change strings."""
    changes = []

    # Detect SOTP: any val block has pipelineDR field
    is_sotp = any("pipelineDR" in s.get("val", {}) for s in cfg["scenarios"].values())

    # ----- Fix 2+3+4: scenario val blocks -----
    # Only for non-SOTP configs. SOTP configs (LLY) have hand-tuned per-segment
    # multiples/DR and should be left alone; their mature-pharma calibration is
    # typically already correct.
    if is_sotp:
        changes.append("  [SOTP detected -- skipping val-block override; relying on existing commercialMult/pipelineMult/pipelineDR tuning]")
    else:
        for sk, new_val in NEW_VAL.items():
            if sk not in cfg["scenarios"]:
                continue
            old = cfg["scenarios"][sk].get("val", {})
            preserved = {k: v for k, v in old.items() if k not in new_val}
            new_full = {**new_val, **preserved}
            for k in ("mult", "dr", "cannib"):
                if old.get(k) != new_full.get(k):
                    changes.append(f"  {sk}.val.{k}: {old.get(k)} -> {new_full.get(k)}")
            cfg["scenarios"][sk]["val"] = new_full

    # ----- Fix 1: cap commercial SOMs -----
    for a in cfg["assets"]:
        stage = a.get("stage", "")
        declining = is_declining(stage)
        comm = is_commercial(stage, a.get("id", ""))
        if not comm:
            continue
        for ind in a["indications"]:
            m = ind.get("market", {})
            sales = m.get("salesM")
            if sales is None or sales <= 0:
                continue  # no reported sales reference
            if "company_slice" not in m or "regions" not in m:
                continue
            current_som = som_of(m) / 1000.0  # in $B? No, SOM is in $M in our math (patientsK * priceK)
            # Actually patientsK is in thousands and priceK is in $K, so product is in $M
            # Let me recompute: (patientsK * 1000 patients) * priceK ($1000/pt) = $M
            # So som_of returns $M.
            current_som_M = som_of(m)
            if declining:
                target_M = sales * 0.6   # declining: peak is BELOW current
            else:
                target_M = sales * 1.5   # mature: allow modest growth
            if current_som_M > target_M * 1.15:  # only adjust if materially over
                rescale_reach(m, target_M)
                new_som_M = som_of(m)
                changes.append(f"  SOM {a['id']}.{ind['id']}: ${current_som_M:.0f}M -> ${new_som_M:.0f}M (sales=${sales:.0f}M, {'declining 0.6x' if declining else 'mature 1.5x'})")

    # ----- Fix 5: PoS/APR scaling for pipeline assets -----
    # Identify pipeline assets (non-commercial)
    pipeline_ids = {a["id"] for a in cfg["assets"]
                    if not is_commercial(a.get("stage", ""), a.get("id", ""))}
    if not pipeline_ids:
        return changes

    # Capture BASE assumptions as anchor
    base_asmp = cfg["scenarios"].get("base", {}).get("assumptions", {})
    scenario_keys = list(cfg["scenarios"].keys())

    # For each pipeline asset.indication, keep existing scenario-specific
    # PoS/APR only if they form a proper monotonic progression:
    # mega_bear <= bear <= base <= bull <= psy_bull (allowing equality).
    # If FLAT across all scenarios, or NON-MONOTONIC (i.e. bear < mega_bear,
    # or psy_bull < bull), apply the scaling fix.
    order = ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]

    def is_well_tuned(aid, ind_id):
        pos_seq = []
        apr_seq = []
        for sk in order:
            sa = cfg["scenarios"].get(sk, {}).get("assumptions", {}).get(aid, {}).get(ind_id, {})
            pos_seq.append(sa.get("pos"))
            apr_seq.append(sa.get("apr"))
        # Must be fully populated, non-decreasing, AND have some spread
        if any(v is None for v in pos_seq + apr_seq):
            return False
        if len(set(pos_seq)) <= 1 and len(set(apr_seq)) <= 1:
            return False  # flat
        for seq in (pos_seq, apr_seq):
            for a, b in zip(seq, seq[1:]):
                if a > b:
                    return False  # non-monotonic -> not well-tuned
        return True

    for aid in pipeline_ids:
        ba = base_asmp.get(aid, {})
        if not ba:
            continue
        for ind_id, vals in ba.items():
            if is_well_tuned(aid, ind_id):
                changes.append(f"  [pipeline {aid}.{ind_id}: monotonic differentiation OK, skipping]")
                continue
            base_pos = vals.get("pos", 0)
            base_apr = vals.get("apr", 0)
            base_pen = vals.get("pen", 1)
            for sk, (pos_mult, apr_mult) in PIPELINE_PCT.items():
                if sk == "base":
                    continue
                scen_asmp = cfg["scenarios"].get(sk, {}).get("assumptions", {})
                scen_asmp.setdefault(aid, {})
                new_pos = max(0, min(100, round(base_pos * pos_mult)))
                new_apr = max(0, min(100, round(base_apr * apr_mult)))
                old = dict(scen_asmp[aid].get(ind_id, {}))
                scen_asmp[aid][ind_id] = {"pos": new_pos, "apr": new_apr, "pen": base_pen}
                if old.get("pos") != new_pos or old.get("apr") != new_apr:
                    changes.append(f"  {sk}.{aid}.{ind_id}: pos {old.get('pos')}->{new_pos}, apr {old.get('apr')}->{new_apr}")

    return changes


def main():
    argv = sys.argv[1:]
    write = "--write" in argv
    tick_arg = None
    if "--ticker" in argv:
        i = argv.index("--ticker")
        tick_arg = argv[i+1].upper()

    targets = [tick_arg] if tick_arg else MEGA_CAPS

    for tk in targets:
        path = CONFIGS / f"{tk}.json"
        if not path.exists():
            print(f"[SKIP] {tk}: config not found")
            continue
        cfg = json.loads(path.read_text(encoding="utf-8"))
        print(f"\n=== {tk} ===")
        changes = recalibrate(cfg)
        if not changes:
            print("  (no changes)")
            continue
        for ch in changes:
            print(ch)
        if write:
            path.write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"  [WROTE] {path.name}")
        else:
            print(f"  [DRY-RUN] use --write to save")


if __name__ == "__main__":
    main()
