# -*- coding: utf-8 -*-
"""Quick audit across all configs -- flag inconsistencies, out-of-place values."""
import json, os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from lib.compute import compute_tp, som_of, tam_of, SCENARIO_ORDER as SCEN_ORDER

CONFIGS = ROOT / "configs"


def audit_one(tk, cfg):
    issues = []
    co = cfg["company"]
    price = co["currentPrice"]
    is_private = bool(co.get("private", False))
    if not is_private and price <= 0:
        issues.append(("CRIT", "price <= 0"))
        return issues

    # 1. Scenario weight sum
    wts = [cfg["scenarios"].get(sk, {}).get("wt", 0) for sk in SCEN_ORDER]
    s = sum(wts)
    if abs(s - 100) > 1:
        issues.append(("WARN", f"scenario weights sum to {s}, not 100"))

    # 2. Scenario TP monotonic? (after sorting by label order, TPs should increase)
    tps = [compute_tp(cfg, sk) for sk in SCEN_ORDER]
    for i, (a, b) in enumerate(zip(tps, tps[1:])):
        if a is None or b is None: continue
        if a > b * 1.02:  # allow 2% slop
            issues.append(("WARN", f"scenario TPs non-monotonic: {SCEN_ORDER[i]}={a:.1f} > {SCEN_ORDER[i+1]}={b:.1f}"))

    # 3. mega_bear > current price (bearish case that's still upside)
    if not is_private and tps[0] is not None and tps[0] > price * 1.05:
        issues.append(("FLAG", f"mega_bear TP ${tps[0]:.1f} > price ${price} (+{(tps[0]-price)/price*100:.0f}%) -- bear isn't bearish"))

    # 4. All scenarios > price (never a downside)
    if not is_private and all(t is not None and t > price * 1.05 for t in tps):
        issues.append(("FLAG", f"every scenario is +5%+ upside -- probably miscalibrated"))

    # 5. psy_bull < bear (pure inversion)
    if tps[-1] is not None and tps[1] is not None and tps[-1] < tps[1]:
        issues.append(("CRIT", f"psychedelic_bull TP ${tps[-1]:.1f} < bear TP ${tps[1]:.1f}"))

    # 6. Wild weighted-TP upside
    if not is_private:
        norm_wts = [w/s for w in wts] if s > 0 else [0]*5
        wtp = sum((t or 0) * w for t, w in zip(tps, norm_wts))
        up = (wtp - price) / price * 100
        if up > 300:
            issues.append(("FLAG", f"weighted TP upside +{up:.0f}% -- extreme, likely over-optimistic"))
        elif up < -50:
            issues.append(("FLAG", f"weighted TP downside {up:.0f}% -- extreme, likely over-pessimistic"))

    # 7. Per indication: SOM > TAM, SOM missing, missing regions
    for a in cfg["assets"]:
        for ind in a["indications"]:
            m = ind.get("market", {})
            if not m:
                issues.append(("WARN", f"{a['id']}.{ind['id']}: no market object"))
                continue
            tam = tam_of(m); som = som_of(m)
            if tam > 0 and som > tam * 1.05:
                issues.append(("CRIT", f"{a['id']}.{ind['id']}: SOM ${som/1000:.1f}B > TAM ${tam/1000:.1f}B"))
            sales = m.get("salesM")
            if sales and som > 0 and som < sales * 0.9:
                issues.append(("CRIT", f"{a['id']}.{ind['id']}: SOM ${som/1000:.1f}B < reported sales ${sales/1000:.1f}B (model says peak already exceeded)"))
            if sales and som > sales * 5 and sales > 100:
                stg = (a.get("stage", "") or "").lower()
                if "phase" not in stg and "pre" not in stg:
                    issues.append(("FLAG", f"{a['id']}.{ind['id']}: SOM ${som/1000:.1f}B is {som/sales:.1f}x sales ${sales/1000:.1f}B (commercial drug, aspirational?)"))
            # Regions malformed
            if "regions" in m:
                for rk, r in m["regions"].items():
                    if not r: continue
                    for f in ("patientsK", "wtpPct", "priceK"):
                        v = r.get(f)
                        if v is None or v == 0:
                            if f == "wtpPct" and rk == "row":  # row wtp=0 occasionally
                                continue
                            issues.append(("WARN", f"{a['id']}.{ind['id']}.regions.{rk}.{f} = {v}"))

    # 8. Pipeline assumptions flat across scenarios (no differentiation)
    for a in cfg["assets"]:
        stgL = (a.get("stage", "") or "").lower()
        if "commercial" in stgL or "launched" in stgL or "marketed" in stgL or a["id"] == "commercial":
            continue
        for ind in a["indications"]:
            pos_vals = set(); apr_vals = set()
            for sk in SCEN_ORDER:
                sa = cfg["scenarios"].get(sk, {}).get("assumptions", {}).get(a["id"], {}).get(ind["id"], {})
                if "pos" in sa: pos_vals.add(sa["pos"])
                if "apr" in sa: apr_vals.add(sa["apr"])
            if len(pos_vals) == 1 and len(apr_vals) == 1 and list(pos_vals)[0] > 0:
                issues.append(("WARN", f"pipeline {a['id']}.{ind['id']}: PoS/APR flat across all scenarios (no risk dispersion)"))

    # 9. Val block sanity
    for sk in SCEN_ORDER:
        v = cfg["scenarios"].get(sk, {}).get("val", {})
        mult = v.get("mult"); dr = v.get("dr")
        if mult is not None:
            if dr is not None and dr < 1:
                issues.append(("WARN", f"{sk}: discount rate {dr}% unusually low"))
            if mult > 30:
                issues.append(("FLAG", f"{sk}: multiple {mult}x extremely high"))
            if mult < 1:
                issues.append(("WARN", f"{sk}: multiple {mult}x unusually low"))

    return issues


def main():
    manifest = json.loads((CONFIGS / "manifest.json").read_text())
    totals = {"CRIT": 0, "FLAG": 0, "WARN": 0}
    company_summary = []
    for tk in sorted(manifest):
        path = CONFIGS / f"{tk}.json"
        if not path.exists(): continue
        cfg = json.loads(path.read_text(encoding="utf-8"))
        issues = audit_one(tk, cfg)
        if issues:
            crits = [i for i in issues if i[0] == "CRIT"]
            flags = [i for i in issues if i[0] == "FLAG"]
            warns = [i for i in issues if i[0] == "WARN"]
            for lvl, c in [("CRIT", crits), ("FLAG", flags), ("WARN", warns)]:
                totals[lvl] += len(c)
            company_summary.append((tk, len(crits), len(flags), len(warns), issues))

    # Print summary header
    print(f"=== AUDIT SUMMARY ({len(manifest)} configs) ===")
    print(f"CRIT: {totals['CRIT']}  FLAG: {totals['FLAG']}  WARN: {totals['WARN']}\n")

    # Detailed findings
    for tk, nc, nf, nw, issues in sorted(company_summary, key=lambda x: -(x[1]*100 + x[2]*10 + x[3])):
        if nc + nf == 0 and nw <= 2:
            continue  # quiet on minor
        print(f"--- {tk} (CRIT={nc} FLAG={nf} WARN={nw}) ---")
        for lvl, msg in issues:
            if lvl in ("CRIT", "FLAG") or nw < 10:
                print(f"  [{lvl}] {msg}")
        print()


if __name__ == "__main__":
    main()
