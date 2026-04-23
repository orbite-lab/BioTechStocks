# -*- coding: utf-8 -*-
"""
Reconcile slider values to match tooltip citations.

Reads authoritative_regions_*.py modules (one per therapeutic L1 batch),
applies their REGIONS and PEN_PCT to all configs. Then recalibrates
company_slice.reachPct per drug so SOM >= salesM invariant holds.
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS = ROOT / "configs"
DATA = ROOT / "scripts" / "data"
sys.path.insert(0, str(DATA))

# Merge all authoritative regions
REGIONS = {}
PEN_PCT = {}
for mod_name in [
    "authoritative_regions_oncology",
    "authoritative_regions_cardio",
    "authoritative_regions_cns",
    "authoritative_regions_immuno_derm",
    "authoritative_regions_rare_other",
]:
    try:
        mod = __import__(mod_name)
        if hasattr(mod, "REGIONS"):
            REGIONS.update(mod.REGIONS)
            print(f"  {mod_name}: {len(mod.REGIONS)} areas")
        if hasattr(mod, "PEN_PCT"):
            PEN_PCT.update(mod.PEN_PCT)
    except Exception as e:
        print(f"  SKIP {mod_name}: {e}")

print(f"\nTotal areas: {len(REGIONS)}")

manifest = json.loads((CONFIGS / "manifest.json").read_text())

# Pass 1: apply new regions + penPct; capture old slider values for delta
changes = []
for t in manifest:
    path = CONFIGS / (t + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    for a in d["assets"]:
        for ind in a["indications"]:
            area = ind.get("area", "")
            if area not in REGIONS:
                continue
            new_regions = REGIONS[area]
            m = ind.setdefault("market", {})
            old = m.get("regions", {})
            # Track delta for diagnostic
            for rk in ("us", "eu", "row"):
                if rk in new_regions:
                    old_pts = old.get(rk, {}).get("patientsK", 0)
                    new_pts = new_regions[rk].get("patientsK", 0)
                    if old_pts > 0 and abs(new_pts - old_pts) / old_pts > 0.5:
                        changes.append((t, area, rk, "pts", old_pts, new_pts))
            m["regions"] = {rk: dict(v) for rk, v in new_regions.items()}
            if area in PEN_PCT:
                m["penPct"] = PEN_PCT[area]
            changed = True
    if changed:
        path.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print(f"\nApplied new regions. {len(changes)} patient-count changes with >50% delta.")

# Pass 2: recalibrate company_slice.reachPct to preserve SOM >= salesM
print("\nRecalibrating SOM where needed...")
adjusted = 0
for t in manifest:
    path = CONFIGS / (t + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    for a in d["assets"]:
        for ind in a["indications"]:
            m = ind.get("market", {})
            regions = m.get("regions")
            cs = m.get("company_slice")
            salesM = m.get("salesM", 0)
            if not regions or not cs:
                continue
            # Current SOM
            som = sum(
                regions.get(rk, {}).get("patientsK", 0)
                * (cs.get(rk, {}).get("reachPct", 0) / 100)
                * (cs.get(rk, {}).get("wtpPct", 0) / 100)
                * cs.get(rk, {}).get("priceK", 0)
                for rk in ["us", "eu", "row"]
            )
            # Target: 1.5x sales for room-to-grow (or keep if already >=)
            target_som = max(salesM * 1.5, som) if salesM > 0 else som
            if salesM > 0 and som < salesM * 1.1:
                # Need to raise reach; scale uniformly to hit target_som
                if som > 0:
                    scale = target_som / som
                    for rk in ["us", "eu", "row"]:
                        if rk in cs:
                            # Cap reach at 95% (can't reach more than 95% of pts realistically)
                            cs[rk]["reachPct"] = min(95, round(cs[rk].get("reachPct", 0) * scale, 1))
                else:
                    # SOM was 0 -- need to set reasonable defaults
                    for rk, share in [("us", 0.65), ("eu", 0.25), ("row", 0.10)]:
                        if rk in cs and rk in regions:
                            pts = regions[rk].get("patientsK", 0)
                            cwtp = cs[rk].get("wtpPct", 50)
                            cprice = cs[rk].get("priceK", 0)
                            if pts > 0 and cprice > 0 and cwtp > 0:
                                cs[rk]["reachPct"] = min(95, round(target_som * share / (pts * (cwtp/100) * cprice) * 100, 1))
                adjusted += 1
                changed = True
    if changed:
        path.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print(f"Adjusted company_slice on {adjusted} indications.")

# Final scan for SOM >= sales invariant
issues = []
for t in manifest:
    d = json.loads((CONFIGS / (t + ".json")).read_text(encoding="utf-8"))
    for a in d["assets"]:
        for ind in a["indications"]:
            m = ind.get("market", {})
            salesM = m.get("salesM", 0)
            cs = m.get("company_slice", {})
            regions = m.get("regions", {})
            if not cs or not regions or salesM == 0:
                continue
            som = sum(
                regions.get(rk, {}).get("patientsK", 0)
                * (cs.get(rk, {}).get("reachPct", 0) / 100)
                * (cs.get(rk, {}).get("wtpPct", 0) / 100)
                * cs.get(rk, {}).get("priceK", 0)
                for rk in ["us", "eu", "row"]
            )
            if salesM > som:
                issues.append(f"{t} {a['id']}.{ind['id']}: sales=${salesM}M > SOM=${som:.0f}M")

print(f"\nFinal SOM >= sales check: {len(issues)} issues")
for i in issues[:20]:
    print(f"  {i}")
