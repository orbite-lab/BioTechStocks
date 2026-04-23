# -*- coding: utf-8 -*-
"""
Reconcile company.phase to the most advanced asset stage.

`company.phase` is a summary tag ("commercial" | "nda_filed" | "phase3" |
"phase2" | "phase1") used for UI chips and the phase filter. It is
hand-set and drifts as assets progress. This script derives the correct
phase from every asset's `stage` string and overwrites the company tag.

Usage
-----
    py scripts/ops/reconcile_phase.py           # dry-run, report diffs
    py scripts/ops/reconcile_phase.py --write   # apply in place

Wired into .github/workflows/validate.yml, so drift is auto-corrected on
main pushes via a github-actions[bot] commit (same pattern as the
taxonomy auto-rebuild).
"""
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS = ROOT / "configs"

# Rank order: higher = more advanced. `company.phase` = max rank across assets.
RANK = {"phase1": 1, "phase2": 2, "phase3": 3, "nda_filed": 4, "commercial": 5}
INV = {v: k for k, v in RANK.items()}


DEAD_WORDS = ("discontinued", "dormant", "shelved", "terminated", "de-prioritized",
              "de-prioritised", "halted", "paused indefinitely")


def stage_to_phase(stage: str) -> str:
    """Map a free-form asset.stage string to a canonical phase tier.

    Rules are applied top-down (first match wins). Assets marked as dead
    (contains DEAD_WORDS) never promote the company.phase regardless of
    the phase word present in the string.
    """
    s = (stage or "").lower().strip()
    if not s:
        return "phase1"
    # Dead programs don't count toward the company phase tier
    if any(w in s for w in DEAD_WORDS):
        return "phase1"
    # Commercial — already marketed, launched, approved with sales
    if any(k in s for k in ("commercial", "launched", "marketed", "approved")):
        return "commercial"
    # NDA / BLA / MAA filed = near-approval
    if any(k in s for k in ("nda filed", "nda submit", "bla filed", "bla submit",
                            "maa filed", "maa submit", "filed")):
        return "nda_filed"
    # Phase 3 / registrational / pivotal -- all treated as late-stage
    if any(k in s for k in ("phase 3", "phase3", "ph3", "p3",
                            "registrational", "pivotal", "2/3")):
        return "phase3"
    if any(k in s for k in ("phase 2", "phase2", "ph2", "p2", "1b/2")):
        return "phase2"
    # Everything else (phase 1, preclinical, discovery, IND-enabling) -> phase1
    return "phase1"


def expected_phase(cfg: dict) -> str:
    """Return the phase tag matching the most advanced asset in cfg.assets."""
    ranks = []
    for asset in cfg.get("assets", []):
        stage = asset.get("stage", "")
        phase = stage_to_phase(stage)
        ranks.append(RANK[phase])
    if not ranks:
        return "phase1"
    return INV[max(ranks)]


def reconcile(write: bool = False) -> list[tuple[str, str, str]]:
    """Scan all configs and correct `company.phase` drift.

    Returns a list of (ticker, old_phase, new_phase) for every config that
    needed a correction (whether applied or not).
    """
    manifest = json.loads((CONFIGS / "manifest.json").read_text(encoding="utf-8"))
    changes: list[tuple[str, str, str]] = []
    for t in manifest:
        path = CONFIGS / f"{t}.json"
        if not path.exists():
            continue
        cfg = json.loads(path.read_text(encoding="utf-8"))
        co = cfg.get("company", {})
        old = co.get("phase", "")
        new = expected_phase(cfg)
        if old == new:
            continue
        changes.append((t, old, new))
        if write:
            co["phase"] = new
            path.write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n",
                            encoding="utf-8")
    return changes


def main():
    write = "--write" in sys.argv
    changes = reconcile(write=write)
    if not changes:
        print("[OK] All company.phase tags match their most advanced asset stage.")
        return 0
    print(f"Phase drift detected on {len(changes)} config(s):")
    for t, old, new in changes:
        arrow = "->" if write else "would be"
        print(f"  {t:6}  {old:11} {arrow} {new}")
    if write:
        print(f"\n[WROTE] {len(changes)} configs updated.")
    else:
        print(f"\nDry run. Re-run with --write to apply.")
    return 0 if write else 1


if __name__ == "__main__":
    sys.exit(main())
