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


# ─── Catalyst dedup pass ─────────────────────────────────────────────
# Catalogs accumulate near-duplicate catalyst rows when both monitor.py
# (high-frequency news) and check_catalysts.py (bi-monthly LLM sweep) add
# events that describe the same readout/PDUFA/BLA in slightly different
# terms (e.g. NTLA Sep 30 'partnership'-typed BLA + Nov 1 'bla_submission'
# for the same Lonvo-z BLA).
#
# Auto-merge requires (asset, indication) match + dates within window AND
# EITHER:
#   (a) same `type` field (the LLM agrees this is the same event class), OR
#   (b) very-high title similarity >= 0.85 AND tight date window <= 45 days
#       (catches the NTLA case: BLA submission mis-typed as 'partnership'
#       vs correctly typed 'bla_submission' — titles >= 0.90 similar)
#
# Distinct trials sharing asset+indication (e.g. CAMX SORENTO Ph2 vs Ph3,
# BBIO Infigratinib NDA vs Ph2 data, LLY Retatrutide T2D vs obesity) survive
# because they have different `type` fields AND title similarity stays under
# the 0.85 ceiling.
from datetime import datetime as _dt
from difflib import SequenceMatcher as _SM
DEDUP_WINDOW_WIDE = 90       # for same-type merges (LLM consensus on event class)
DEDUP_WINDOW_TIGHT = 45      # for cross-type merges (require very high title sim)
DEDUP_TITLE_SIM_SAME_TYPE  = 0.75  # same type but different asset/trial -> still distinct
DEDUP_TITLE_SIM_CROSS_TYPE = 0.85  # different types -- need near-identical titles


def _title_sim(a, b):
    return _SM(None, (a or "").lower(), (b or "").lower()).ratio()


print("\nCatalyst dedup pass...")
total_merged = 0
for t in manifest:
    path = CONFIGS / (t + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    cats = d.get("catalysts", []) or []
    if len(cats) < 2:
        continue
    parsed = []
    for c in cats:
        try:
            dt = _dt.fromisoformat((c.get("dateSort") or "").replace("Z", "+00:00")).replace(tzinfo=None)
        except (ValueError, AttributeError, TypeError):
            dt = None
        parsed.append(dt)
    keep = [True] * len(cats)
    merges = []
    for i, ci in enumerate(cats):
        if not keep[i]:
            continue
        for j in range(i + 1, len(cats)):
            if not keep[j]:
                continue
            cj = cats[j]
            if ci.get("asset") != cj.get("asset"):
                continue
            if ci.get("indication") != cj.get("indication"):
                continue
            if parsed[i] is None or parsed[j] is None:
                continue
            days = abs((parsed[i] - parsed[j]).days)
            same_type = ci.get("type") == cj.get("type") and ci.get("type")
            sim = _title_sim(ci.get("title", ""), cj.get("title", ""))
            # Same-type path: same asset+indication+type → still need decent
            #   title similarity to merge, since many configs have multiple
            #   parallel trials sharing all three (e.g. RVMD RASolute 305
            #   vs 309 are both phase3_start for the same asset/indication).
            # Cross-type path: very high title similarity required (e.g.
            #   NTLA BLA mis-typed as 'partnership' vs correctly 'bla_submission').
            if same_type and days <= DEDUP_WINDOW_WIDE and sim >= DEDUP_TITLE_SIM_SAME_TYPE:
                pass
            elif (not same_type) and days <= DEDUP_WINDOW_TIGHT and sim >= DEDUP_TITLE_SIM_CROSS_TYPE:
                pass
            else:
                continue
            i_res = bool(ci.get("_resolvedAt") or ci.get("resolved"))
            j_res = bool(cj.get("_resolvedAt") or cj.get("resolved"))
            if i_res and not j_res:
                keep[j] = False
                merges.append((ci.get("title", "")[:50], cj.get("title", "")[:50], f"i resolved · sim {sim:.2f}"))
            elif j_res and not i_res:
                keep[i] = False
                merges.append((cj.get("title", "")[:50], ci.get("title", "")[:50], f"j resolved · sim {sim:.2f}"))
                break
            else:
                i_score = sum(1 for v in ci.values() if v not in (None, "", [], {}))
                j_score = sum(1 for v in cj.values() if v not in (None, "", [], {}))
                if i_score >= j_score:
                    keep[j] = False
                    merges.append((ci.get("title", "")[:50], cj.get("title", "")[:50], f"i fuller · sim {sim:.2f}"))
                else:
                    keep[i] = False
                    merges.append((cj.get("title", "")[:50], ci.get("title", "")[:50], f"j fuller · sim {sim:.2f}"))
                    break
    if merges:
        new_cats = [c for k, c in zip(keep, cats) if k]
        d["catalysts"] = new_cats
        path.write_text(json.dumps(d, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        total_merged += len(merges)
        for kept, dropped, reason in merges:
            print(f"  {t}: kept '{kept}' / dropped '{dropped}' ({reason})")

print(f"Catalyst dedup: {total_merged} duplicate(s) auto-merged.")
