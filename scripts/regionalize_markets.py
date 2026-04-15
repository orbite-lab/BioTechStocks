# -*- coding: utf-8 -*-
"""
Decompose every indication's market into US/EU/ROW regional blocks.

For each indication's market:
  - If `regions` already exists: skip (already regionalized).
  - If `patientsK` + `pricingK` (bottom-up): split patients by epidemiological share,
    assign region-specific WTP% and price multipliers (rare vs non-rare).
  - If `tamB` (top-down): back out implied patient count using a typical $/patient anchor
    (rare: $200K/yr, non-rare: $10K/yr), then decompose.
  - If `commercial` asset / no market fields: skip.

Preserves approximate addressable (implicit TAM) within ~10%, not exact peak revenue.
Adds a generic `sources` map that flags the decomposition assumption.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT / "configs"
MANIFEST = CONFIG_DIR / "manifest.json"

# Regional splits
# patient share, wtp%, price multiplier (vs pricingK or anchor $/pt)
RARE = {
    "us":  {"share": 0.30, "wtp": 75, "priceMult": 1.25},
    "eu":  {"share": 0.35, "wtp": 55, "priceMult": 0.55},
    "row": {"share": 0.35, "wtp": 15, "priceMult": 0.20},
}
NON_RARE = {
    "us":  {"share": 0.28, "wtp": 55, "priceMult": 1.20},
    "eu":  {"share": 0.30, "wtp": 40, "priceMult": 0.50},
    "row": {"share": 0.42, "wtp": 12, "priceMult": 0.15},
}

# $/patient/yr anchors for top-down → patient back-out
ANCHOR_RARE = 200       # $K/yr
ANCHOR_NONRARE = 10     # $K/yr

GENERIC_SOURCES_RARE = {
    "us.patientsK":  {"note": "Auto-decomposed from legacy config. US ~30% of global diagnosed (rare); refine with Orphanet/NORD/company epi deck."},
    "eu.patientsK":  {"note": "Auto-decomposed. EU5 ~35% of diagnosed (rare); refine with Orphanet."},
    "row.patientsK": {"note": "Auto-decomposed. ROW ~35% -- Japan higher, LatAm/APAC diagnosis much lower."},
    "us.wtpPct":     {"note": "Rare disease default -- strong commercial payor coverage analog (75%)."},
    "eu.wtpPct":     {"note": "Rare disease default -- HTA-gated uptake (55%)."},
    "row.wtpPct":    {"note": "Rare disease default -- limited reimbursement ex-Japan (15%)."},
    "us.priceK":     {"note": "US list price anchor -- typically ~1.25x global avg for rare."},
    "eu.priceK":     {"note": "EU rare-disease net price -- ~55% of US list after HTA discount."},
    "row.priceK":    {"note": "Blended ROW -- Japan near EU, emerging far lower (~20% of US)."},
    "penPct":        {"note": "Peak penetration inherited from legacy config -- refine per competitive landscape."},
}
GENERIC_SOURCES_NONRARE = {
    "us.patientsK":  {"note": "Auto-decomposed. US ~28% of diagnosed (non-rare)."},
    "eu.patientsK":  {"note": "Auto-decomposed. EU5 ~30% of diagnosed."},
    "row.patientsK": {"note": "Auto-decomposed. ROW ~42% -- dominant in large-market diseases."},
    "us.wtpPct":     {"note": "Non-rare default -- commercial formulary gating (~55%)."},
    "eu.wtpPct":     {"note": "Non-rare default -- HTA + budget impact (~40%)."},
    "row.wtpPct":    {"note": "Non-rare default -- mostly self-pay ex-Japan (~12%)."},
    "us.priceK":     {"note": "US price anchor -- ~1.20x global avg."},
    "eu.priceK":     {"note": "EU net ~50% of US list."},
    "row.priceK":    {"note": "ROW blended ~15% of US list."},
    "penPct":        {"note": "Peak penetration inherited from legacy config -- refine per competitive landscape."},
}


def decompose_bottom_up(patientsK: float, pricingK: float, is_rare: bool) -> dict:
    prof = RARE if is_rare else NON_RARE
    regions = {}
    for rk, cfg in prof.items():
        regions[rk] = {
            "patientsK": round(patientsK * cfg["share"], 1),
            "wtpPct": cfg["wtp"],
            "priceK": round(pricingK * cfg["priceMult"]),
        }
    return regions


def decompose_top_down(tamB: float, is_rare: bool) -> dict:
    anchor = ANCHOR_RARE if is_rare else ANCHOR_NONRARE
    # Total patients implied at full WTP and list price: patients = tamB * 1000 / anchor
    implied_total_K = (tamB * 1000) / anchor
    # Back-solve so sum(patient x wtp x priceMult x anchor) ≈ tamB * 1000 ($M)
    prof = RARE if is_rare else NON_RARE
    blend = sum(c["share"] * (c["wtp"] / 100) * c["priceMult"] for c in prof.values())
    if blend <= 0:
        return {}
    scale = 1 / blend
    regions = {}
    for rk, cfg in prof.items():
        regions[rk] = {
            "patientsK": round(implied_total_K * scale * cfg["share"], 1),
            "wtpPct": cfg["wtp"],
            "priceK": round(anchor * cfg["priceMult"]),
        }
    return regions


def process_market(market: dict, is_rare: bool) -> bool:
    if not isinstance(market, dict):
        return False
    if "regions" in market:
        return False  # already regionalized
    regions = None
    if market.get("patientsK") and market.get("pricingK"):
        regions = decompose_bottom_up(market["patientsK"], market["pricingK"], is_rare)
        # keep legacy fields but regions becomes source of truth
    elif market.get("tamB"):
        regions = decompose_top_down(market["tamB"], is_rare)
    if not regions:
        return False
    market["regions"] = regions
    market["sources"] = GENERIC_SOURCES_RARE if is_rare else GENERIC_SOURCES_NONRARE
    return True


def process_config(path: Path) -> tuple[int, int]:
    cfg = json.loads(path.read_text(encoding="utf-8"))
    touched = 0
    total = 0
    for asset in cfg.get("assets", []):
        if asset.get("id") == "commercial":
            continue
        for ind in asset.get("indications", []):
            total += 1
            is_rare = bool(ind.get("rare"))
            if process_market(ind.get("market", {}), is_rare):
                touched += 1
    if touched:
        path.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8")
    return touched, total


def main():
    tickers = json.loads(MANIFEST.read_text(encoding="utf-8"))
    grand_touched = 0
    grand_total = 0
    for t in tickers:
        p = CONFIG_DIR / f"{t}.json"
        if not p.exists():
            print(f"SKIP {t} (no config)")
            continue
        touched, total = process_config(p)
        grand_touched += touched
        grand_total += total
        print(f"{t:6s}  {touched}/{total} indications regionalized")
    print("-" * 40)
    print(f"TOTAL: {grand_touched}/{grand_total} indications regionalized")


if __name__ == "__main__":
    main()
