#!/usr/bin/env python3
"""
Validate all company configs against taxonomy.json.
Run before committing: python scripts/validate.py
Exit code 0 = clean, 1 = errors found.
"""
import json, sys, os
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIGS = ROOT / "configs"
TAXONOMY = ROOT / "taxonomy.json"

def load_taxonomy():
    if not TAXONOMY.exists():
        print("[WARN]  taxonomy.json not found -- generating from configs (first run)")
        return None, None
    t = json.loads(TAXONOMY.read_text())
    areas = set()
    for l1, l2s in t["therapeutic_areas"].items():
        for l2, l3s in l2s.items():
            for l3, l3_val in l3s.items():
                areas.add(f"{l1}.{l2}.{l3}")
                # L4 sub-segments
                if isinstance(l3_val, dict) and "sub" in l3_val:
                    for l4 in l3_val["sub"]:
                        areas.add(f"{l1}.{l2}.{l3}.{l4}")
    mods = set()
    for l1, l2s in t["modalities"].items():
        for l2, l3s in l2s.items():
            for l3 in l3s:
                mods.add(f"{l1}.{l2}.{l3}")
    return areas, mods

def validate():
    errors = []
    warnings = []
    known_areas, known_mods = load_taxonomy()
    
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
            d = json.loads(cfg_path.read_text())
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
        
        asset_ids = {a["id"] for a in d.get("assets", [])}
        
        for sk, s in scenarios.items():
            for aid in s.get("assumptions", {}):
                if aid not in asset_ids:
                    errors.append(f"{tk}.{sk}: assumption references non-existent asset '{aid}'")
        
        # Asset & indication checks
        for a in d.get("assets", []):
            mod = a.get("modality", "")
            
            # Modality depth check
            if mod:
                parts = mod.split(".")
                if len(parts) != 3:
                    errors.append(f"{tk}.{a['id']}: modality '{mod}' is not L1.L2.L3 (depth={len(parts)})")
                elif known_mods is not None and mod not in known_mods:
                    warnings.append(f"{tk}.{a['id']}: NEW modality '{mod}' not in taxonomy.json -- add it or check spelling")
                if len(parts) == 3:
                    l3_mod_parents[parts[2]].add(f"{parts[0]}.{parts[1]}")
            else:
                warnings.append(f"{tk}.{a['id']}: missing modality tag")
            
            for ind in a.get("indications", []):
                area = ind.get("area", "")
                market = ind.get("market", {})
                
                # Area depth check
                if area:
                    parts = area.split(".")
                    if len(parts) not in (3, 4):
                        errors.append(f"{tk}.{a['id']}.{ind['id']}: area '{area}' must be L1.L2.L3 or L1.L2.L3.L4 (depth={len(parts)})")
                    elif known_areas is not None and area not in known_areas:
                        warnings.append(f"{tk}.{a['id']}.{ind['id']}: NEW area '{area}' not in taxonomy.json -- add it or check spelling")
                    if len(parts) >= 3:
                        l3_area_parents[parts[2]].add(f"{parts[0]}.{parts[1]}")
                else:
                    errors.append(f"{tk}.{a['id']}.{ind['id']}: missing area tag")
                
                # Market data checks
                has_tam = market.get("tamB", 0) > 0
                has_patients = market.get("patientsK", 0) > 0 and market.get("pricingK", 0) > 0
                has_regions = isinstance(market.get("regions"), dict) and len(market.get("regions", {})) > 0
                if not has_tam and not has_patients and not has_regions and a["id"] != "commercial":
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
    
    for l3, parents in l3_mod_parents.items():
        if len(parents) > 1:
            # Allow some legitimate duplicates (e.g., same mechanism in different modality classes)
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
