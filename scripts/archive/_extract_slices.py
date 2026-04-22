# -*- coding: utf-8 -*-
import json, os
CONFIGS = r"C:/Users/RomainBodiner/Downloads/biotech-model/configs"
for t in ["LLY","ABBV","GILD","UCB","ONC","ALNY","ARGX","BBIO"]:
    p = os.path.join(CONFIGS, t+".json")
    with open(p, encoding="utf-8") as f:
        c = json.load(f)
    print(f"\n===== {t} =====")
    for a in c.get("assets", []):
        for ind in a.get("indications", []):
            cs = ind.get("market", {}).get("company_slice", {})
            if not cs:
                continue
            us = cs.get("us", {}); eu = cs.get("eu", {}); row = cs.get("row", {})
            print(f"  {a['id']} / {ind['id']}  name={a.get('name','')[:40]} | {ind.get('name','')[:40]}")
            print(f"    US r={us.get('reachPct')} w={us.get('wtpPct')} p={us.get('priceK')}")
            print(f"    EU r={eu.get('reachPct')} w={eu.get('wtpPct')} p={eu.get('priceK')}")
            print(f"    ROW r={row.get('reachPct')} w={row.get('wtpPct')} p={row.get('priceK')}")
            sales = ind.get("market", {}).get("salesM")
            if sales: print(f"    salesM={sales}")
