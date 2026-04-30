#!/usr/bin/env python3
"""
Validate all company configs against taxonomy.json.
Run before committing: python scripts/validate.py
Exit code 0 = clean, 1 = errors found.

Checks performed (in order of severity):
  1. Structural: required fields present, scenarios well-formed
  2. Cross-reference integrity: every catalyst / assumption references an
     asset.id / indication.id that actually exists in this config
  3. Taxonomy integrity: every ind.area / a.modality resolves to taxonomy.json.
     Unknown tags are ERRORS if a close fuzzy match exists in taxonomy
     (likely typo), WARNINGS if genuinely new (taxonomy auto-rebuild covers).
  4. Market data sanity: has TAM data unless explicitly pseudo-area
  5. Cross-config integrity: no L3 area orphans parents
"""
import json, sys
from collections import defaultdict
from difflib import get_close_matches
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS = ROOT / "configs"
TAXONOMY = ROOT / "data" / "taxonomy.json"
TARGETS = ROOT / "data" / "targets.json"

# Target strings must be all-caps alphanumeric + underscore.
# Examples: TNF, NLRP3, GLP1R, KRAS_G12C, HIV_INTEGRASE, AMYLOID_BETA.
import re
TARGET_PATTERN = re.compile(r"^[A-Z][A-Z0-9_]{1,30}$")

# If a config's area/modality tag isn't in taxonomy BUT a known tag is within
# this similarity ratio, flag it as a suspected typo (ERROR not WARNING).
# 0.85 catches "tnbcc" -> "tnbc" (0.89) but lets "triple_neg" vs "tnbc" pass
# as distinct (0.3).
FUZZY_MATCH_THRESHOLD = 0.85


def load_taxonomy():
    if not TAXONOMY.exists():
        print("[WARN]  taxonomy.json not found -- generating from configs (first run)")
        return None, None
    t = json.loads(TAXONOMY.read_text(encoding="utf-8"))
    areas = set()
    for l1, l2s in t["therapeutic_areas"].items():
        for l2, l3s in l2s.items():
            for l3, l3_val in l3s.items():
                areas.add(f"{l1}.{l2}.{l3}")
                if isinstance(l3_val, dict) and "sub" in l3_val:
                    for l4 in l3_val["sub"]:
                        areas.add(f"{l1}.{l2}.{l3}.{l4}")
    mods = set()
    for l1, l2s in t["modalities"].items():
        for l2, l3s in l2s.items():
            for l3 in l3s:
                mods.add(f"{l1}.{l2}.{l3}")
    return areas, mods


def load_known_targets():
    """Load the derived target index, if present. Returns the set of target
    strings used anywhere in configs (same role as taxonomy's 'areas' / 'mods'
    sets -- serves as the fuzzy-match reference corpus)."""
    if not TARGETS.exists():
        return None
    t = json.loads(TARGETS.read_text(encoding="utf-8"))
    return set(t.get("targets", {}).keys())


def fuzzy_suggest(unknown, known_set):
    """Return the closest known string if ratio >= threshold, else None."""
    if not known_set:
        return None
    matches = get_close_matches(unknown, known_set, n=1, cutoff=FUZZY_MATCH_THRESHOLD)
    return matches[0] if matches else None


def validate():
    errors = []
    warnings = []
    known_areas, known_mods = load_taxonomy()
    known_targets = load_known_targets()

    manifest = json.loads((CONFIGS / "manifest.json").read_text())

    # Track L3 -> parent mapping for duplicate detection
    l3_area_parents = defaultdict(set)
    l3_mod_parents = defaultdict(set)

    for tk in manifest:
        cfg_path = CONFIGS / f"{tk}.json"
        if not cfg_path.exists():
            errors.append(f"{tk}: config file missing")
            continue

        try:
            d = json.loads(cfg_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errors.append(f"{tk}: invalid JSON -- {e}")
            continue

        co = d.get("company", {})

        # Company-level checks
        if not co.get("currentPrice"):
            errors.append(f"{tk}: missing currentPrice")
        if not co.get("sharesOut"):
            errors.append(f"{tk}: missing sharesOut")
        if not co.get("phase"):
            warnings.append(f"{tk}: missing company.phase")

        # Scenario checks
        scenarios = d.get("scenarios", {})
        if "base" not in scenarios:
            errors.append(f"{tk}: missing 'base' scenario")

        # Build asset + indication id maps for cross-reference integrity
        asset_ids = {a["id"] for a in d.get("assets", [])}
        asset_ind_map = {}  # asset_id -> set of indication ids
        for a in d.get("assets", []):
            asset_ind_map[a["id"]] = {ind["id"] for ind in a.get("indications", [])}

        # =========== Cross-reference integrity: assumptions ===========
        # Every scenarios.<sk>.assumptions.<aid>.<iid> must resolve to a real
        # asset and indication in this config. Catches refactor drift where an
        # asset/indication was renamed or removed but its assumption block
        # lingered.
        for sk, s in scenarios.items():
            for aid, ind_block in s.get("assumptions", {}).items():
                if aid not in asset_ids:
                    errors.append(f"{tk}.{sk}: assumption references non-existent asset '{aid}'")
                    continue
                if not isinstance(ind_block, dict):
                    continue
                for iid in ind_block:
                    if iid not in asset_ind_map.get(aid, set()):
                        errors.append(f"{tk}.{sk}: assumption references non-existent indication '{aid}.{iid}'")

        # =========== Cross-reference integrity: catalysts ===========
        # Every catalyst's asset + indication pointer must resolve. Otherwise
        # the model can't compute materiality / shift-weights against a ghost
        # program and the catalyst tab silently shows nothing.
        for i, cat in enumerate(d.get("catalysts", []) or []):
            cat_aid = cat.get("asset")
            cat_iid = cat.get("indication")
            cat_title = cat.get("title", f"catalyst[{i}]")
            if not cat_aid:
                errors.append(f"{tk}: catalyst '{cat_title[:50]}' missing asset pointer")
                continue
            if cat_aid not in asset_ids:
                errors.append(f"{tk}: catalyst '{cat_title[:50]}' references non-existent asset '{cat_aid}'")
                continue
            if cat_iid and cat_iid not in asset_ind_map.get(cat_aid, set()):
                errors.append(f"{tk}: catalyst '{cat_title[:50]}' references non-existent indication '{cat_aid}.{cat_iid}'")

        # =========== Asset & indication checks ===========
        for a in d.get("assets", []):
            mod = a.get("modality", "")

            # Modality depth + taxonomy check with fuzzy match
            if mod:
                parts = mod.split(".")
                if len(parts) != 3:
                    errors.append(f"{tk}.{a['id']}: modality '{mod}' is not L1.L2.L3 (depth={len(parts)})")
                elif known_mods is not None and mod not in known_mods:
                    suggestion = fuzzy_suggest(mod, known_mods)
                    if suggestion:
                        errors.append(f"{tk}.{a['id']}: modality '{mod}' looks like a typo -- did you mean '{suggestion}'?")
                    else:
                        warnings.append(f"{tk}.{a['id']}: NEW modality '{mod}' not in taxonomy.json -- taxonomy rebuild will pick it up")
                if len(parts) == 3:
                    l3_mod_parents[parts[2]].add(f"{parts[0]}.{parts[1]}")
            else:
                warnings.append(f"{tk}.{a['id']}: missing modality tag")

            # Target tag checks: format + fuzzy-match against known.
            # `targets` field is a list of target strings (HGNC symbols or
            # standard pathway names). Empty list is acceptable (platform /
            # mechanism-only assets). Missing field is a warning during the
            # rollout; once all configs have it, can be upgraded to error.
            targets = a.get("targets")
            if targets is None:
                warnings.append(f"{tk}.{a['id']}: missing targets[] field -- run scripts/ops/seed_targets.py --write")
            elif not isinstance(targets, list):
                errors.append(f"{tk}.{a['id']}: targets must be a list, got {type(targets).__name__}")
            else:
                for tgt in targets:
                    if not isinstance(tgt, str):
                        errors.append(f"{tk}.{a['id']}: target entry must be a string, got {type(tgt).__name__}")
                        continue
                    if not TARGET_PATTERN.match(tgt):
                        errors.append(f"{tk}.{a['id']}: target '{tgt}' must be uppercase alphanumeric + underscore (e.g. TNF, KRAS_G12C)")
                        continue
                    if known_targets is not None and tgt not in known_targets:
                        suggestion = fuzzy_suggest(tgt, known_targets)
                        if suggestion:
                            errors.append(f"{tk}.{a['id']}: target '{tgt}' looks like a typo -- did you mean '{suggestion}'?")
                        else:
                            warnings.append(f"{tk}.{a['id']}: NEW target '{tgt}' -- rebuild_targets will add it")

            for ind in a.get("indications", []):
                area = ind.get("area", "")
                market = ind.get("market", {})

                # Area depth + taxonomy check with fuzzy match.
                # _* prefix denotes pseudo-area (platform / discovery / metadata) -- exempt.
                if not area:
                    errors.append(f"{tk}.{a['id']}.{ind['id']}: missing area tag")
                elif area.startswith("_"):
                    pass  # platform/discovery indication; no depth requirement
                else:
                    parts = area.split(".")
                    if len(parts) not in (3, 4):
                        errors.append(f"{tk}.{a['id']}.{ind['id']}: area '{area}' must be L1.L2.L3 or L1.L2.L3.L4 (depth={len(parts)})")
                    elif known_areas is not None and area not in known_areas:
                        suggestion = fuzzy_suggest(area, known_areas)
                        if suggestion:
                            errors.append(f"{tk}.{a['id']}.{ind['id']}: area '{area}' looks like a typo -- did you mean '{suggestion}'?")
                        else:
                            warnings.append(f"{tk}.{a['id']}.{ind['id']}: NEW area '{area}' not in taxonomy.json -- taxonomy rebuild will pick it up")
                    if len(parts) >= 3:
                        l3_area_parents[parts[2]].add(f"{parts[0]}.{parts[1]}")

                # Market data checks (skip for _* pseudo-areas)
                has_tam = market.get("tamB", 0) > 0
                has_patients = market.get("patientsK", 0) > 0 and market.get("pricingK", 0) > 0
                has_regions = isinstance(market.get("regions"), dict) and len(market.get("regions", {})) > 0
                is_platform = area.startswith("_")
                if not has_tam and not has_patients and not has_regions and a["id"] != "commercial" and not is_platform:
                    warnings.append(f"{tk}.{a['id']}.{ind['id']}: no TAM data (tamB, patientsKxpricingK, or regions)")

                if has_tam and "penPct" not in market and "patientsK" not in market:
                    errors.append(f"{tk}.{a['id']}.{ind['id']}: has tamB but missing penPct -- will cause NaN")

                # Check assumptions exist in base scenario
                base_a = scenarios.get("base", {}).get("assumptions", {}).get(a["id"], {}).get(ind["id"])
                if base_a is None and a["id"] != "commercial":
                    warnings.append(f"{tk}.{a['id']}.{ind['id']}: no base scenario assumptions")

                # Multi-indication catch-all check
                if "multi_indication" in area or "multi_therapeutic" in area:
                    errors.append(f"{tk}.{a['id']}.{ind['id']}: catch-all tag '{area}' -- use lead indication instead")

    # Cross-config duplicate L3 check
    for l3, parents in l3_area_parents.items():
        if len(parents) > 1:
            errors.append(f"DUPLICATE area L3 '{l3}' under multiple parents: {sorted(parents)}")

    # market_status_overrides hygiene: flag override entries that are now redundant
    # because a covered drug ships commercially at that leaf (auto-derived
    # branded_incumbent already wins, so the override is dead weight).
    try:
        from pathlib import Path as _P
        ov_path = _P(__file__).resolve().parents[2] / "data" / "market_status_overrides.json"
        if ov_path.exists():
            ov = json.loads(ov_path.read_text(encoding="utf-8"))
            # Build set of leaves that have any commercial drug across coverage
            commercial_leaves = set()
            for tk in manifest:
                cfg_path = CONFIGS / f"{tk}.json"
                if not cfg_path.exists(): continue
                try:
                    c = json.loads(cfg_path.read_text(encoding="utf-8"))
                except Exception:
                    continue
                for a in c.get("assets", []):
                    stg = (a.get("stage", "") or "").lower()
                    is_commercial_stage = any(k in stg for k in ("commercial", "nda_filed", "approved"))
                    for ind in a.get("indications", []):
                        sales = (ind.get("market", {}) or {}).get("salesM", 0) or 0
                        if sales > 0 or is_commercial_stage:
                            ar = ind.get("area", "")
                            if ar: commercial_leaves.add(ar)
            for cat in ("generic_incumbent", "branded_incumbent_external"):
                for leaf in (ov.get(cat) or {}):
                    if leaf in commercial_leaves:
                        warnings.append(f"market_status_overrides[{cat}]: '{leaf}' is now redundant -- a covered drug ships commercially at this leaf (auto-derived 'branded_incumbent' already wins). Remove the override entry.")
    except Exception as e:
        warnings.append(f"market_status_overrides check skipped: {e}")

    for l3, parents in l3_mod_parents.items():
        if len(parents) > 1:
            warnings.append(f"Modality L3 '{l3}' under multiple parents: {sorted(parents)} -- verify intentional")

    # Print results
    print(f"\n{'='*60}")
    print(f"  Validated {len(manifest)} configs")
    print(f"  {len(errors)} errors  |  {len(warnings)} warnings")
    print(f"{'='*60}\n")

    if errors:
        print("[ERROR] ERRORS (must fix):\n")
        for e in sorted(errors):
            print(f"  {e}")
        print()

    if warnings:
        print("[WARN]  WARNINGS (review):\n")
        for w in sorted(warnings):
            print(f"  {w}")
        print()

    if not errors and not warnings:
        print("[OK] All configs consistent with taxonomy!\n")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(validate())
