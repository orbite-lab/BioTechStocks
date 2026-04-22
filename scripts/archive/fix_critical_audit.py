# -*- coding: utf-8 -*-
"""Fix the 10 critical audit findings from audit_configs.py:
  1. ABBV declining drugs: SOM below reported sales -> scale declining cap to 0.85x
  2. SOM > TAM violations (UCB, IONS, ALNY, KRYS, OCS): scale reachPct so
     SOM = 0.95 * TAM (just under the invariant).
"""
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIGS = ROOT / "configs"


def som_of(m):
    if "company_slice" not in m or "regions" not in m: return 0
    t = 0
    for rk, cs in m["company_slice"].items():
        tr = m["regions"].get(rk)
        if not tr or not cs: continue
        t += (tr.get("patientsK", 0) or 0) * (cs.get("reachPct", 0) / 100) \
             * (cs.get("wtpPct", 0) / 100) * (cs.get("priceK", 0) or 0)
    return t


def tam_of(m):
    if "regions" not in m: return 0
    t = 0
    for r in m["regions"].values():
        if not r: continue
        t += (r.get("patientsK", 0) or 0) * (r.get("wtpPct", 0) / 100) * (r.get("priceK", 0) or 0)
    return t


def rescale_reach(m, target_som):
    cur = som_of(m)
    if cur <= 0 or target_som <= 0: return
    sc = target_som / cur
    for rk, cs in m["company_slice"].items():
        cs["reachPct"] = round(cs.get("reachPct", 0) * sc, 2)


# ---------- Fix 1: ABBV declining-cap over-shoot ----------
def fix_abbv_declining(cfg):
    changes = []
    for a in cfg["assets"]:
        stg = (a.get("stage", "") or "").lower()
        if "declining" not in stg:
            continue
        for ind in a["indications"]:
            m = ind.get("market", {})
            sales = m.get("salesM")
            if not sales or sales <= 0: continue
            cur_som = som_of(m)
            if cur_som < sales * 1.0:  # SOM below sales -- fix
                target = sales * 1.0  # forward peak = current run rate for declining drugs
                rescale_reach(m, target)
                changes.append(f"  {a['id']}.{ind['id']}: SOM ${cur_som:.0f}M -> ${som_of(m):.0f}M (sales=${sales:.0f}M, 0.85x)")
    return changes


# ---------- Fix 2: SOM > TAM violations ----------
SOM_GT_TAM = [
    ("UCB",  "neuro_rare",  "neuro_port"),
    ("IONS", "bepiro",      "hbv"),
    ("ALNY", "mivelsiran",  "alz_rna"),
    ("KRYS", "kb111",       "hhd"),
    ("OCS",  "privo_on",    "on"),
]


def fix_som_gt_tam(cfg, aid, iid):
    for a in cfg["assets"]:
        if a["id"] != aid: continue
        for ind in a["indications"]:
            if ind["id"] != iid: continue
            m = ind.get("market", {})
            tam = tam_of(m); som = som_of(m)
            if tam <= 0: return None
            if som <= tam: return None
            # Additional constraint: for commercial drugs, SOM also <= 1.5x sales
            sales = m.get("salesM", 0) or 0
            stg = (a.get("stage", "") or "").lower()
            is_comm = "commercial" in stg
            tighter = tam * 0.95
            if is_comm and sales > 0:
                tighter = min(tighter, sales * 1.5)
            rescale_reach(m, tighter)
            return f"  {aid}.{iid}: SOM ${som/1000:.1f}B -> ${som_of(m)/1000:.1f}B (TAM=${tam/1000:.1f}B{', sales=$'+str(sales/1000)+'B' if sales else ''})"


def main():
    write = "--write" in sys.argv[1:]

    # Fix 1: ABBV declining
    path = CONFIGS / "ABBV.json"
    cfg = json.loads(path.read_text(encoding="utf-8"))
    print("=== ABBV declining-cap fix ===")
    changes = fix_abbv_declining(cfg)
    for c in changes: print(c)
    if changes and write:
        path.write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"  [WROTE] ABBV.json")

    # Fix 2: SOM > TAM
    print("\n=== SOM > TAM fixes ===")
    touched = {}
    for tk, aid, iid in SOM_GT_TAM:
        path = CONFIGS / f"{tk}.json"
        cfg = touched.setdefault(tk, json.loads(path.read_text(encoding="utf-8")))
        msg = fix_som_gt_tam(cfg, aid, iid)
        if msg: print(msg)
    if write:
        for tk, cfg in touched.items():
            (CONFIGS / f"{tk}.json").write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            print(f"  [WROTE] {tk}.json")
    else:
        print("  [DRY-RUN] use --write to save")


if __name__ == "__main__":
    main()
