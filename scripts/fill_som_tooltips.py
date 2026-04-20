# -*- coding: utf-8 -*-
"""
Fill missing SOM (company_slice_sources) tooltips with contextual, drug-aware
notes generated from existing config data (drug name, stage, region, slider
values, disease area).

Preserves existing hand-written tooltips; only fills gaps.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIGS = ROOT / "configs"

def stage_tag(stage):
    s = stage.lower()
    if 'commercial' in s: return 'commercial'
    if 'nda filed' in s or 'bla filed' in s or 'nda submitted' in s or 'snda' in s: return 'nda_filed'
    if 'phase 3' in s or 'ph3' in s: return 'phase3'
    if 'phase 2/3' in s: return 'phase3'
    if 'phase 2' in s or 'ph2' in s: return 'phase2'
    if 'phase 1' in s or 'ph1' in s: return 'phase1'
    if 'preclinical' in s or 'discovery' in s: return 'preclinical'
    return 'pipeline'

def is_rare_area(area):
    return 'rare' in area or 'neuromuscular' in area or 'orphan' in area

def region_wtp_context(region, stage):
    """Explain drug-specific WTP based on region + stage."""
    stg = stage_tag(stage)
    if region == 'us':
        if stg == 'commercial':    return 'established payor adoption + formulary coverage'
        if stg == 'nda_filed':     return 'anticipated commercial payor coverage at launch'
        if stg == 'phase3':        return 'estimated launch WTP pending Phase 3 + label'
        if stg == 'phase2':        return 'early forecast; awaits Phase 3 confirmatory data'
        if stg == 'phase1':        return 'speculative -- Phase 1 proof-of-concept only'
        return 'early-stage estimate'
    if region == 'eu':
        if stg == 'commercial':    return 'HTA-negotiated uptake (NICE/G-BA/ASMR)'
        if stg == 'nda_filed':     return 'EMA filing planned; post-HTA launch trajectory'
        if stg == 'phase3':        return 'EMA path pending Phase 3; HTA gating expected'
        return 'EU access TBD; EMA pathway unclear at stage'
    # row
    if stg == 'commercial':        return 'Japan PMDA reimbursed; emerging markets patchy'
    return 'ROW access limited to Japan + select APAC at launch'

def region_reach_context(region, stage, pts_K, reach_pct, area):
    """Explain drug-specific reach."""
    stg = stage_tag(stage)
    addressable = round(pts_K * reach_pct / 100, 1)
    rare = is_rare_area(area)
    if region == 'us':
        if stg == 'commercial':
            return f'Reaches {reach_pct}% of {pts_K}K US patients ({addressable}K); current commercial capture + growth capacity'
        if stg == 'nda_filed':
            return f'Launch reach {reach_pct}% of {pts_K}K at initial label; expansion post-approval'
        if stg == 'phase3':
            return f'Est. {reach_pct}% reach at approval of {pts_K}K US patients; Phase 3 target population'
        if stg == 'phase2':
            return f'Preliminary {reach_pct}% reach assumption; pending Phase 3 readout'
        if stg == 'phase1':
            return f'Early-stage {reach_pct}% reach estimate; highly speculative'
        if stg == 'preclinical':
            return f'Preclinical {reach_pct}% reach placeholder; long timeline'
    if region == 'eu':
        if stg == 'commercial':
            return f'EU reach {reach_pct}% of {pts_K}K patients; lower than US due to HTA gating + biosimilar pressure' if not rare else f'EU reach {reach_pct}% of {pts_K}K; rare disease access via specialist centers'
        if stg == 'nda_filed':
            return f'EU launch reach {reach_pct}% of {pts_K}K; EMA filing lagging US typically ~6-12mo'
        return f'EU reach {reach_pct}% of {pts_K}K; EMA pathway at {stg}'
    # row
    if stg == 'commercial':
        return f'ROW reach {reach_pct}% of {pts_K}K -- Japan + select markets; limited ex-Japan access'
    return f'ROW reach {reach_pct}% of {pts_K}K; ex-US/EU access lags by years at {stg}'

def price_context(region, stage, price_K, area):
    """Explain drug-specific price."""
    if price_K >= 1000:
        pstr = f'${price_K/1000:.1f}M' + ('/yr' if 'gene_therapy' not in area else ' one-time (amortized)')
    elif price_K >= 50:
        pstr = f'${price_K}K/yr'
    elif price_K >= 1:
        pstr = f'${price_K}K/yr'
    else:
        pstr = f'${price_K*1000:.0f}/course'
    if region == 'us':
        return f'US WAC {pstr} at this stage; payor negotiation expected'
    if region == 'eu':
        return f'EU net {pstr} post-HTA (~50-60% of US list typical)'
    return f'ROW blended {pstr} -- Japan near EU, emerging markets lower via tiered pricing'

def run():
    manifest = json.loads((CONFIGS / "manifest.json").read_text())
    filled = 0
    touched = 0
    for t in manifest:
        path = CONFIGS / (t + ".json")
        d = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for a in d["assets"]:
            stage = a.get("stage", "")
            for ind in a["indications"]:
                m = ind.get("market", {})
                cs = m.get("company_slice")
                if not cs:
                    continue
                area = ind.get("area", "")
                regions = m.get("regions", {})
                css = m.setdefault("company_slice_sources", {})

                ind_changed = False
                for rk in ("us", "eu", "row"):
                    if rk not in cs:
                        continue
                    c = cs[rk]
                    r = regions.get(rk, {})
                    pts = r.get("patientsK", 0)

                    # Reach tooltip
                    rk_key = f"{rk}.reachPct"
                    if rk_key not in css or not css[rk_key].get("note"):
                        css[rk_key] = {"note": region_reach_context(rk, stage, pts, c.get("reachPct", 0), area)}
                        filled += 1; ind_changed = True

                    # WTP tooltip
                    wk = f"{rk}.wtpPct"
                    if wk not in css or not css[wk].get("note"):
                        css[wk] = {"note": f"{rk.upper()} drug-specific WTP {c.get('wtpPct',0)}% -- {region_wtp_context(rk, stage)}"}
                        filled += 1; ind_changed = True

                    # Price tooltip
                    pk = f"{rk}.priceK"
                    if pk not in css or not css[pk].get("note"):
                        css[pk] = {"note": price_context(rk, stage, c.get("priceK", 0), area)}
                        filled += 1; ind_changed = True
                if ind_changed:
                    changed = True
                    touched += 1
        if changed:
            path.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Filled {filled} missing SOM tooltips across {touched} indications.")

if __name__ == "__main__":
    run()
