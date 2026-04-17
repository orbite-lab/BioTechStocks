# -*- coding: utf-8 -*-
"""Add company_slice to all ABBV indications."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
path = ROOT / "configs" / "ABBV.json"
d = json.loads(path.read_text(encoding="utf-8"))

# Company slice definitions keyed by (asset_id, indication_id)
SLICES = {
    # Skyrizi
    ("skyrizi", "pso"): {"us": {"reachPct": 15, "wtpPct": 65, "priceK": 70}, "eu": {"reachPct": 10, "wtpPct": 50, "priceK": 35}, "row": {"reachPct": 3, "wtpPct": 12, "priceK": 15}},
    ("skyrizi", "ibd"): {"us": {"reachPct": 10, "wtpPct": 60, "priceK": 70}, "eu": {"reachPct": 7, "wtpPct": 45, "priceK": 35}, "row": {"reachPct": 2, "wtpPct": 10, "priceK": 15}},
    # Rinvoq
    ("rinvoq", "ra"): {"us": {"reachPct": 8, "wtpPct": 65, "priceK": 65}, "eu": {"reachPct": 6, "wtpPct": 50, "priceK": 35}, "row": {"reachPct": 2, "wtpPct": 12, "priceK": 15}},
    ("rinvoq", "ad"): {"us": {"reachPct": 12, "wtpPct": 60, "priceK": 55}, "eu": {"reachPct": 8, "wtpPct": 45, "priceK": 30}, "row": {"reachPct": 3, "wtpPct": 10, "priceK": 12}},
    ("rinvoq", "uc_rinvoq"): {"us": {"reachPct": 10, "wtpPct": 55, "priceK": 65}, "eu": {"reachPct": 7, "wtpPct": 42, "priceK": 35}, "row": {"reachPct": 2, "wtpPct": 10, "priceK": 12}},
    ("rinvoq", "crohns_rinvoq"): {"us": {"reachPct": 8, "wtpPct": 55, "priceK": 65}, "eu": {"reachPct": 5, "wtpPct": 42, "priceK": 35}, "row": {"reachPct": 2, "wtpPct": 10, "priceK": 12}},
    # Humira (declining)
    ("humira", "ra_humira"): {"us": {"reachPct": 5, "wtpPct": 40, "priceK": 55}, "eu": {"reachPct": 3, "wtpPct": 30, "priceK": 25}, "row": {"reachPct": 2, "wtpPct": 10, "priceK": 10}},
    ("humira", "ibd_humira"): {"us": {"reachPct": 5, "wtpPct": 35, "priceK": 55}, "eu": {"reachPct": 3, "wtpPct": 28, "priceK": 25}, "row": {"reachPct": 1, "wtpPct": 8, "priceK": 10}},
    ("humira", "pso_humira"): {"us": {"reachPct": 3, "wtpPct": 30, "priceK": 55}, "eu": {"reachPct": 2, "wtpPct": 25, "priceK": 25}, "row": {"reachPct": 1, "wtpPct": 8, "priceK": 10}},
    # Vraylar
    ("vraylar", "schizo_vraylar"): {"us": {"reachPct": 15, "wtpPct": 60, "priceK": 28}, "eu": {"reachPct": 10, "wtpPct": 45, "priceK": 14}, "row": {"reachPct": 3, "wtpPct": 10, "priceK": 6}},
    ("vraylar", "bipolar_vraylar"): {"us": {"reachPct": 10, "wtpPct": 55, "priceK": 28}, "eu": {"reachPct": 7, "wtpPct": 40, "priceK": 14}, "row": {"reachPct": 2, "wtpPct": 8, "priceK": 6}},
    ("vraylar", "mdd_adj_vraylar"): {"us": {"reachPct": 3, "wtpPct": 50, "priceK": 28}, "eu": {"reachPct": 2, "wtpPct": 35, "priceK": 14}, "row": {"reachPct": 0.5, "wtpPct": 8, "priceK": 6}},
    # Botox Therapeutic
    ("botox_neuro", "migraine"): {"us": {"reachPct": 12, "wtpPct": 55, "priceK": 18}, "eu": {"reachPct": 8, "wtpPct": 40, "priceK": 10}, "row": {"reachPct": 3, "wtpPct": 10, "priceK": 4}},
    # Qulipta
    ("qulipta", "mig_prev"): {"us": {"reachPct": 8, "wtpPct": 50, "priceK": 12}, "eu": {"reachPct": 4, "wtpPct": 35, "priceK": 6}, "row": {"reachPct": 1, "wtpPct": 8, "priceK": 3}},
    # Imbruvica
    ("imbruvica", "cll"): {"us": {"reachPct": 12, "wtpPct": 55, "priceK": 200}, "eu": {"reachPct": 8, "wtpPct": 45, "priceK": 120}, "row": {"reachPct": 3, "wtpPct": 10, "priceK": 45}},
    # Venclexta
    ("venclexta", "cll_ven"): {"us": {"reachPct": 25, "wtpPct": 60, "priceK": 180}, "eu": {"reachPct": 18, "wtpPct": 48, "priceK": 110}, "row": {"reachPct": 5, "wtpPct": 12, "priceK": 50}},
    ("venclexta", "aml_ven"): {"us": {"reachPct": 45, "wtpPct": 65, "priceK": 150}, "eu": {"reachPct": 35, "wtpPct": 52, "priceK": 90}, "row": {"reachPct": 8, "wtpPct": 15, "priceK": 35}},
    # Elahere
    ("elahere", "ovarian"): {"us": {"reachPct": 15, "wtpPct": 50, "priceK": 180}, "eu": {"reachPct": 8, "wtpPct": 35, "priceK": 100}, "row": {"reachPct": 2, "wtpPct": 8, "priceK": 40}},
    # Botox Cosmetic
    ("botox_cosm", "wrinkles"): {"us": {"reachPct": 30, "wtpPct": 80, "priceK": 0.7}, "eu": {"reachPct": 25, "wtpPct": 70, "priceK": 0.5}, "row": {"reachPct": 15, "wtpPct": 50, "priceK": 0.4}},
    # Juvederm
    ("juvederm", "fillers"): {"us": {"reachPct": 25, "wtpPct": 75, "priceK": 0.6}, "eu": {"reachPct": 20, "wtpPct": 65, "priceK": 0.4}, "row": {"reachPct": 10, "wtpPct": 45, "priceK": 0.3}},
    # Emraclidine
    ("emraclidine", "schizo_new"): {"us": {"reachPct": 8, "wtpPct": 40, "priceK": 25}, "eu": {"reachPct": 5, "wtpPct": 30, "priceK": 13}, "row": {"reachPct": 2, "wtpPct": 8, "priceK": 5}},
    # ABBV-400
    ("abbv400", "nsclc"): {"us": {"reachPct": 20, "wtpPct": 45, "priceK": 200}, "eu": {"reachPct": 12, "wtpPct": 35, "priceK": 110}, "row": {"reachPct": 3, "wtpPct": 8, "priceK": 45}},
}

added = 0
for a in d["assets"]:
    for ind in a["indications"]:
        key = (a["id"], ind["id"])
        if key in SLICES:
            ind["market"]["company_slice"] = SLICES[key]
            added += 1

# Verify all SOM > salesM
issues = []
for a in d["assets"]:
    for ind in a["indications"]:
        m = ind["market"]
        cs = m.get("company_slice", {})
        r = m.get("regions", {})
        salesM = m.get("salesM", 0)
        if not cs or not r:
            continue
        som = sum(
            r.get(rk, {}).get("patientsK", 0)
            * (cs.get(rk, {}).get("reachPct", 0) / 100)
            * (cs.get(rk, {}).get("wtpPct", 0) / 100)
            * cs.get(rk, {}).get("priceK", 0)
            for rk in ["us", "eu", "row"]
        )
        flag = "OK" if som >= salesM or salesM == 0 else "SALES > SOM"
        print(f"{a['id']:15s} {ind['id']:18s} sales=${salesM:>6.0f}M  SOM=${som:>8.0f}M  [{flag}]")
        if salesM > 0 and som < salesM:
            issues.append((a["id"], ind["id"], salesM, som))

path.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\n{added} company_slice entries added")
if issues:
    print(f"\n{len(issues)} SALES > SOM issues to fix:")
    for aid, iid, s, som in issues:
        print(f"  {aid}.{iid}: sales=${s}M > SOM=${som:.0f}M")
else:
    print("All SOM >= sales -- clean!")
