# -*- coding: utf-8 -*-
"""One-shot: split Imbruvica + Brukinsa into multiple disease indications
and retag all heme configs to the new cll / nhl.* taxonomy."""
import json
from pathlib import Path

CONFIGS = Path(__file__).resolve().parent.parent.parent / "configs"

def load(tk):
    return json.loads((CONFIGS / f"{tk}.json").read_text(encoding="utf-8"))

def save(tk, c):
    (CONFIGS / f"{tk}.json").write_text(
        json.dumps(c, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")

# ------------------------------------------------------------------
# ABBV: split Imbruvica into 5 indications (CLL + MCL + WM + MZL + cGVHD)
# ------------------------------------------------------------------
c = load("ABBV")
for a in c["assets"]:
    if a["id"] == "imbruvica":
        a["indications"] = [
            {"id":"cll","name":"Chronic lymphocytic leukemia","area":"oncology.hematology.cll","rare":False,
             "market":{"regions":{},"company_slice":{
                 "us":{"reachPct":25,"wtpPct":55,"priceK":180},
                 "eu":{"reachPct":18,"wtpPct":45,"priceK":110},
                 "row":{"reachPct":5,"wtpPct":10,"priceK":45}},
                 "company_slice_sources":{"us.reachPct":"Imbruvica BTKi share ~25% US CLL post-Brukinsa entry"},
                 "penPct":65,"cagrPct":-3,"peakYear":2027,"salesM":1450,"salesYear":2025,
                 "notes":"CLL portion (~52% of $2.8B Imbruvica franchise WW)"}},
            {"id":"mcl","name":"Mantle cell lymphoma","area":"oncology.hematology.nhl.mcl","rare":False,
             "market":{"regions":{},"company_slice":{
                 "us":{"reachPct":35,"wtpPct":65,"priceK":180},
                 "eu":{"reachPct":28,"wtpPct":48,"priceK":110},
                 "row":{"reachPct":6,"wtpPct":10,"priceK":45}},
                 "company_slice_sources":{"us.reachPct":"Imbruvica MCL share ~35%, declining vs Brukinsa"},
                 "penPct":50,"cagrPct":-5,"peakYear":2027,"salesM":420,"salesYear":2025}},
            {"id":"wm","name":"Waldenstrom macroglobulinemia","area":"oncology.hematology.nhl.wm","rare":True,
             "market":{"regions":{},"company_slice":{
                 "us":{"reachPct":50,"wtpPct":70,"priceK":180},
                 "eu":{"reachPct":35,"wtpPct":52,"priceK":110},
                 "row":{"reachPct":8,"wtpPct":10,"priceK":45}},
                 "company_slice_sources":{"us.reachPct":"Imbruvica first BTKi for WM, ~50% share eroding to Brukinsa (ASPEN trial)"},
                 "penPct":55,"cagrPct":-4,"peakYear":2027,"salesM":390,"salesYear":2025}},
            {"id":"mzl","name":"Marginal zone lymphoma","area":"oncology.hematology.nhl.mzl","rare":False,
             "market":{"regions":{},"company_slice":{
                 "us":{"reachPct":18,"wtpPct":60,"priceK":180},
                 "eu":{"reachPct":12,"wtpPct":45,"priceK":110},
                 "row":{"reachPct":3,"wtpPct":10,"priceK":45}},
                 "company_slice_sources":{"us.reachPct":"Imbruvica MZL approval"},
                 "penPct":40,"cagrPct":-3,"peakYear":2027,"salesM":140,"salesYear":2025}},
            {"id":"cgvhd","name":"Chronic graft-versus-host disease","area":"immunology.transplant.cgvhd","rare":False,
             "market":{"regions":{},"company_slice":{
                 "us":{"reachPct":25,"wtpPct":70,"priceK":180},
                 "eu":{"reachPct":18,"wtpPct":50,"priceK":110},
                 "row":{"reachPct":4,"wtpPct":10,"priceK":45}},
                 "company_slice_sources":{"us.reachPct":"First FDA-approved cGVHD therapy 2017; Jakafi competing"},
                 "penPct":35,"cagrPct":-2,"peakYear":2027,"salesM":280,"salesYear":2025}}
        ]
    if a["id"] == "venclexta":
        for ind in a["indications"]:
            if ind["id"] == "cll_ven":
                ind["area"] = "oncology.hematology.cll"
                ind["market"]["regions"] = {}

# Update scenario assumptions for new Imbruvica indications
for sk in c["scenarios"]:
    asmp = c["scenarios"][sk]["assumptions"]
    if "imbruvica" in asmp:
        scen_pen = {"mega_bear":0.85,"bear":0.95,"base":1.0,"bull":1.05,"psychedelic_bull":1.1}
        asmp["imbruvica"] = {iid: {"pos":100,"apr":100,"pen":scen_pen[sk]}
                             for iid in ["cll","mcl","wm","mzl","cgvhd"]}
save("ABBV", c)
print("ABBV: Imbruvica split + venclexta retag")

# ------------------------------------------------------------------
# ONC (BeOne): split Brukinsa into 4 indications + retag pipeline
# ------------------------------------------------------------------
c = load("ONC")
for a in c["assets"]:
    if a["id"] == "commercial":
        a["indications"] = [
            {"id":"cll","name":"Chronic lymphocytic leukemia","area":"oncology.hematology.cll","rare":False,
             "market":{"regions":{},"company_slice":{
                 "us":{"reachPct":40,"wtpPct":65,"priceK":195},
                 "eu":{"reachPct":30,"wtpPct":50,"priceK":115},
                 "row":{"reachPct":10,"wtpPct":12,"priceK":50}},
                 "company_slice_sources":{"us.reachPct":"Brukinsa BTKi leader US CLL ~40%, taking share via better tolerability/PFS"},
                 "penPct":65,"cagrPct":12,"peakYear":2030,"salesM":2900,"salesYear":2025,
                 "notes":"CLL is largest Brukinsa indication (~75% of $3.9B WW)"}},
            {"id":"mcl","name":"Mantle cell lymphoma","area":"oncology.hematology.nhl.mcl","rare":False,
             "market":{"regions":{},"company_slice":{
                 "us":{"reachPct":45,"wtpPct":70,"priceK":195},
                 "eu":{"reachPct":30,"wtpPct":52,"priceK":115},
                 "row":{"reachPct":8,"wtpPct":12,"priceK":50}},
                 "company_slice_sources":{"us.reachPct":"Brukinsa MCL post-BTK approval"},
                 "penPct":50,"cagrPct":5,"peakYear":2028,"salesM":400,"salesYear":2025}},
            {"id":"wm","name":"Waldenstrom macroglobulinemia","area":"oncology.hematology.nhl.wm","rare":True,
             "market":{"regions":{},"company_slice":{
                 "us":{"reachPct":45,"wtpPct":75,"priceK":195},
                 "eu":{"reachPct":30,"wtpPct":55,"priceK":115},
                 "row":{"reachPct":8,"wtpPct":12,"priceK":50}},
                 "company_slice_sources":{"us.reachPct":"Brukinsa first BTKi to show superior PFS vs Imbruvica in WM (ASPEN trial)"},
                 "penPct":55,"cagrPct":6,"peakYear":2028,"salesM":400,"salesYear":2025}},
            {"id":"mzl","name":"Marginal zone lymphoma","area":"oncology.hematology.nhl.mzl","rare":False,
             "market":{"regions":{},"company_slice":{
                 "us":{"reachPct":22,"wtpPct":65,"priceK":195},
                 "eu":{"reachPct":15,"wtpPct":48,"priceK":115},
                 "row":{"reachPct":4,"wtpPct":12,"priceK":50}},
                 "company_slice_sources":{"us.reachPct":"Brukinsa MZL approval"},
                 "penPct":40,"cagrPct":5,"peakYear":2028,"salesM":200,"salesYear":2025}}
        ]
    if a["id"] == "sonro":
        for ind in a["indications"]:
            if ind["id"] == "bcl2":
                ind["area"] = "oncology.hematology.cll"; ind["market"]["regions"] = {}
    if a["id"] == "btk_cdac":
        for ind in a["indications"]:
            if ind["id"] == "btk_deg":
                ind["area"] = "oncology.hematology.cll"; ind["market"]["regions"] = {}

for sk in c["scenarios"]:
    asmp = c["scenarios"][sk]["assumptions"]
    if "commercial" in asmp:
        scen_pen = {"mega_bear":0.85,"bear":0.95,"base":1.0,"bull":1.15,"psychedelic_bull":1.3}
        asmp["commercial"] = {iid: {"pos":100,"apr":100,"pen":scen_pen[sk]}
                              for iid in ["cll","mcl","wm","mzl"]}
save("ONC", c)
print("ONC: Brukinsa split + sonro/btk_cdac retag")

# ------------------------------------------------------------------
# Other simple retags
# ------------------------------------------------------------------
SIMPLE = {
    ("ALLO","cema_cel","lbcl_1l"): "oncology.hematology.nhl.dlbcl",
    ("CRVS","soq_ptcl","ptcl"):    "oncology.hematology.nhl.tcell",
    ("GILD","yescarta","dlbcl_2l"):"oncology.hematology.nhl.dlbcl",
    ("GILD","yescarta","fl_inhl"): "oncology.hematology.nhl.fl",
    ("GILD","tecartus","mcl_2l"):  "oncology.hematology.nhl.mcl",
    ("LEGN","lucar","nhl"):        "oncology.hematology.nhl.dlbcl",
    ("NKTR","nktr255","onc"):      "oncology.hematology.nhl",
    ("REGN","odronextamab","fl_dlbcl"): "oncology.hematology.nhl.fl",
}
for (tk, aid, iid), new_area in SIMPLE.items():
    c = load(tk)
    for a in c["assets"]:
        if a["id"] != aid: continue
        for ind in a["indications"]:
            if ind["id"] == iid:
                old = ind.get("area","")
                ind["area"] = new_area
                ind["market"]["regions"] = {}
                print(f"{tk}.{aid}.{iid}: {old}  ->  {new_area}")
    save(tk, c)

print("\nDONE")
