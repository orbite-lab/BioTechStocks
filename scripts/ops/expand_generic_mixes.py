# -*- coding: utf-8 -*-
"""Expand generic-maker mix templates into indications[].

Big generics + biosimilar makers (Teva, Viatris, Sandoz, Sun, Cipla, Aurobindo,
Hikma, Celltrion, etc.) sell hundreds of SKUs across every therapeutic area.
Per-company per-disease attribution at granularity sufficient for Market
Explorer is impractical to curate manually.

This script reads each config asset that has:
  {"mixTemplate": "us_generics_developed_v1", "totalSalesM": 3500,
   "mixOverrides": {"cns.psychiatry.depression": 0.13}}

and auto-generates an indications[] list with salesM split per area:
  - For each area in template: salesM = totalSalesM * weight
  - Apply mixOverrides if present (override + renormalize remaining)
  - "_other_minor" residual goes to pseudo-area
    "_established_products.<ticker>_<segment>_other"
  - Each generated indication gets _genericBucket: true so the audit skips
    the SOM >= salesM check (generic franchises have low branded SOM by design)

Run after editing a config and before audit:
  py scripts/ops/expand_generic_mixes.py

Idempotent: re-running with the same template + totalSalesM regenerates the
same indications array.
"""
import json, sys
from pathlib import Path
from collections import OrderedDict

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS_DIR = ROOT / "configs"
TEMPLATES_PATH = ROOT / "data" / "generic_mix_templates.json"


def load_templates():
    with open(TEMPLATES_PATH, encoding="utf-8") as f:
        return json.load(f)


def normalize_weights(weights):
    """Ensure weights sum to 1.0 (idempotent if already normalized)."""
    total = sum(w for k, w in weights.items() if not k.startswith("_"))
    if total == 0:
        return weights
    if abs(total - 1.0) < 0.001:
        return weights
    # renormalize all real-area weights to sum to (1 - other_minor)
    other = weights.get("_other_minor", 0)
    target = max(0, 1.0 - other)
    factor = target / total if total > 0 else 0
    out = OrderedDict()
    for k, w in weights.items():
        if k.startswith("_"):
            out[k] = w
        else:
            out[k] = round(w * factor, 4)
    return out


def expand_asset(asset, ticker, templates):
    """Generate indications[] for an asset that has mixTemplate + totalSalesM."""
    template_name = asset.get("mixTemplate")
    total = asset.get("totalSalesM")
    if not template_name or total is None:
        return None

    if template_name not in templates:
        print(f"  [WARN] {ticker}.{asset['id']}: unknown template '{template_name}'")
        return None

    template = dict(templates[template_name])
    template.pop("_description", None)

    # Apply per-asset overrides
    overrides = asset.get("mixOverrides", {})
    for area, weight in overrides.items():
        template[area] = weight

    template = normalize_weights(template)

    indications = []
    seg_id = asset["id"]
    for area, weight in template.items():
        if weight <= 0:
            continue
        sales = round(total * weight)
        if area == "_other_minor":
            # Residual goes to a pseudo-area heritage tail
            ind_id = f"{seg_id}_other"
            ind_area = f"_established_products.{ticker.lower()}_{seg_id}_other"
            ind_name = f"{seg_id} other / un-mappable generics residual"
        else:
            # Disease-tagged real area
            leaf = area.split(".")[-1]
            ind_id = f"{seg_id}_{leaf}"[:60]  # cap id length
            ind_area = area
            ind_name = f"{seg_id} - {leaf.replace('_', ' ')} (generic share)"
        indications.append(OrderedDict([
            ("id", ind_id),
            ("name", ind_name),
            ("area", ind_area),
            ("market", OrderedDict([
                ("regions", {}),
                ("company_slice", {}),
                ("company_slice_sources", {}),
                ("salesM", sales),
                ("salesYear", 2025),
                ("peakYear", 2027),
                ("cagrPct", 0),
                ("penPct", 0),
                ("_genericBucket", True),
                ("_genericTemplate", template_name),
            ])),
        ]))
    return indications


def process_config(path, templates):
    with open(path, encoding="utf-8") as f:
        cfg = json.load(f, object_pairs_hook=OrderedDict)

    changed = False
    ticker = cfg.get("company", {}).get("ticker", path.stem)
    for asset in cfg.get("assets", []):
        if "mixTemplate" not in asset:
            continue
        new_inds = expand_asset(asset, ticker, templates)
        if new_inds is None:
            continue
        # Replace indications wholesale (idempotent regeneration)
        old_count = len(asset.get("indications", []))
        asset["indications"] = new_inds
        changed = True
        print(f"  {ticker}.{asset['id']}: expanded -> {len(new_inds)} indications "
              f"(template={asset['mixTemplate']}, total=${asset['totalSalesM']}M)")

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(cfg, f, indent=2, ensure_ascii=False)
            f.write("\n")
    return changed


def main():
    templates = load_templates()
    print(f"Loaded {sum(1 for k in templates if not k.startswith('_'))} mix templates from "
          f"{TEMPLATES_PATH.relative_to(ROOT)}")

    manifest = json.loads((CONFIGS_DIR / "manifest.json").read_text(encoding="utf-8"))
    expanded = 0
    for tk in sorted(manifest):
        path = CONFIGS_DIR / f"{tk}.json"
        if not path.exists():
            continue
        if process_config(path, templates):
            expanded += 1

    print(f"\nExpanded {expanded} config(s).")
    print("Run reconcile_sliders + audit + snapshot next.")


if __name__ == "__main__":
    main()
