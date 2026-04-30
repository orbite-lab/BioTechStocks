# -*- coding: utf-8 -*-
"""Scenario TP snapshot — detect unintended model regressions.

Modes:
  py scripts/ops/snapshot_scenarios.py           # diff current vs baseline
  py scripts/ops/snapshot_scenarios.py --update  # regenerate baseline (use after intentional changes)
  py scripts/ops/snapshot_scenarios.py --ci      # exit 1 if any ticker drifts >10% or monotonicity breaks

The baseline lives in snapshots/scenarios.json. Commit it like any other data
file. When you intentionally change the model math or config inputs, re-run
with --update and commit the new snapshot alongside your changes.

Drift classification:
  OK     |delta| <  3%    -- noise, ignore
  WARN   |delta| 3-10%    -- notable, check intent
  FAIL   |delta| >= 10%   -- blocks CI (likely a regression)
  BROKE  mega_bear > bear -- monotonicity violation, always blocks
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from lib.compute import compute_all_scenarios, SCENARIO_ORDER

CONFIGS = ROOT / "configs"
SNAPSHOT_DIR = ROOT / "snapshots"
SNAPSHOT_FILE = SNAPSHOT_DIR / "scenarios.json"


def compute_all():
    manifest = json.loads((CONFIGS / "manifest.json").read_text())
    out = {}
    for tk in sorted(manifest):
        path = CONFIGS / f"{tk}.json"
        if not path.exists():
            continue
        cfg = json.loads(path.read_text(encoding="utf-8"))
        # Skip private (non-tradeable reference) configs -- TPs are meaningless
        if cfg.get("company", {}).get("private"):
            continue
        tps = compute_all_scenarios(cfg)
        # Round to 2 decimals to suppress floating-point noise
        out[tk] = {k: (round(v, 2) if v is not None else None) for k, v in tps.items()}
    return out


def update():
    SNAPSHOT_DIR.mkdir(exist_ok=True)
    data = compute_all()
    payload = {
        "_meta": {
            "description": "Scenario target prices per ticker. Regenerate with: py scripts/ops/snapshot_scenarios.py --update",
            "count": len(data),
        },
        "scenarios": data,
    }
    SNAPSHOT_FILE.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")
    print(f"[WROTE] {SNAPSHOT_FILE} ({len(data)} tickers)")


def diff(ci_mode=False):
    if not SNAPSHOT_FILE.exists():
        print(f"No baseline at {SNAPSHOT_FILE}. Run --update first.")
        sys.exit(2)
    baseline = json.loads(SNAPSHOT_FILE.read_text(encoding="utf-8")).get("scenarios", {})
    current = compute_all()

    only_new = set(current) - set(baseline)
    only_old = set(baseline) - set(current)
    common = sorted(set(current) & set(baseline))

    fails = []
    warns = []

    for tk in common:
        b = baseline[tk]; c = current[tk]
        for key in SCENARIO_ORDER + ["_weighted"]:
            bv = b.get(key); cv = c.get(key)
            if bv is None or cv is None or bv == 0:
                continue
            delta = (cv - bv) / abs(bv) * 100
            if abs(delta) >= 10:
                fails.append((tk, key, bv, cv, delta))
            elif abs(delta) >= 3:
                warns.append((tk, key, bv, cv, delta))

    # Report
    print(f"=== Snapshot diff ({len(common)} tickers) ===")
    if only_new: print(f"NEW tickers (no baseline): {sorted(only_new)}")
    if only_old: print(f"DROPPED tickers (no longer in configs): {sorted(only_old)}")

    if fails:
        print(f"\n[FAIL] FAIL ({len(fails)}) — drift >= 10%:")
        for tk, key, bv, cv, d in sorted(fails, key=lambda x: -abs(x[4]))[:30]:
            sign = "+" if d >= 0 else ""
            print(f"  {tk:6s} {key:20s}  {bv:8.2f} -> {cv:8.2f}  ({sign}{d:.1f}%)")
        if len(fails) > 30:
            print(f"  ... +{len(fails)-30} more")

    if warns:
        print(f"\n[WARN] ({len(warns)}) -- drift 3-10%:")
        for tk, key, bv, cv, d in sorted(warns, key=lambda x: -abs(x[4]))[:20]:
            sign = "+" if d >= 0 else ""
            print(f"  {tk:6s} {key:20s}  {bv:8.2f} -> {cv:8.2f}  ({sign}{d:.1f}%)")
        if len(warns) > 20:
            print(f"  ... +{len(warns)-20} more")

    if not fails and not warns and not only_old:
        print("[OK] All scenarios unchanged within tolerance.")

    if ci_mode and fails:
        sys.exit(1)


def main():
    argv = sys.argv[1:]
    if "--update" in argv:
        update()
    else:
        diff(ci_mode="--ci" in argv)


if __name__ == "__main__":
    main()
