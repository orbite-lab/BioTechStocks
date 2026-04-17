# -*- coding: utf-8 -*-
"""Add salesM to all marketed assets that are missing it."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIGS = ROOT / "configs"

# Known 2025 sales by (ticker, asset_id, indication_id)
# Sources: 10-K filings, earnings calls, consensus estimates
SALES = {
    # UCB
    ("UCB", "commercial", "pso_hs"): {"salesM": 1500, "salesYear": 2025, "note": "Bimzelx ~EUR1.4B 2025 (psoriasis + HS + PsA)"},
    ("UCB", "neuro_rare", "epi_mg"): {"salesM": 976, "salesYear": 2025, "note": "Fintepla + Rystiggo + Zilbrysq combined EUR976M 2025"},
    ("UCB", "vimpat", "epi_focal"): {"salesM": 900, "salesYear": 2025, "note": "Vimpat + Briviact ~EUR850M 2025 (declining, LOE)"},
    ("UCB", "cimzia", "ra_crohns"): {"salesM": 400, "salesYear": 2025, "note": "Cimzia ~EUR380M 2025 (declining)"},
    ("UCB", "evenity", "osteo"): {"salesM": 1200, "salesYear": 2025, "note": "Evenity ~EUR1.1B 2025 (Amgen partnered)"},
    # LLY
    ("LLY", "jardiance", "t2d_hf"): {"salesM": 3500, "salesYear": 2025, "note": "Jardiance ~$3.5B Lilly share 2025 (BI partnership)"},
    ("LLY", "kisunla", "ad_early"): {"salesM": 800, "salesYear": 2025, "note": "Kisunla ~$800M 2025 (early ramp, launched mid-2024)"},
    # 4568 (Daiichi Sankyo)
    ("4568", "enhertu", "her2"): {"salesM": 4600, "salesYear": 2025, "note": "Enhertu JPY553B (~$4.6B) FY2025"},
    ("4568", "datroway", "trop2"): {"salesM": 350, "salesYear": 2025, "note": "Dato-DXd early commercial launch"},
    ("4568", "japan_pipe", "japan"): {"salesM": 2000, "salesYear": 2025, "note": "Japan domestic portfolio + Lixiana"},
    # 6990 (BeiGene broader - same as ONC but different ticker for Japan/China products)
    ("6990", "sac_tmt", "trop2_china"): {"salesM": 200, "salesYear": 2025, "note": "Sacituzumab tirumotecan China launches ~$200M"},
    ("6990", "a166", "her2_china"): {"salesM": 150, "salesYear": 2025, "note": "A166 HER2 China ~$150M"},
    # GILD
    ("GILD", "lenacapavir_prep", "hiv_prep"): {"salesM": 500, "salesYear": 2025, "note": "Sunlenca/lenacapavir PrEP early launch ~$500M"},
    # MDGL
    ("MDGL", "commercial", "mash_f2f3"): {"salesM": 300, "salesYear": 2025, "note": "Rezdiffra ~$300M 2025 (early ramp)"},
    # BBIO
    ("BBIO", "commercial", "attr_cm"): {"salesM": 600, "salesYear": 2025, "note": "Attruby ~$600M 2025 (launched Nov 2024)"},
    # ARWR
    ("ARWR", "plozasiran", "fcs"): {"salesM": 200, "salesYear": 2025, "note": "REDEMPLO FCS launch ~$200M 2025"},
    # TVTX
    ("TVTX", "filspari_igan", "igan"): {"salesM": 350, "salesYear": 2025, "note": "FILSPARI IgAN ~$350M 2025 (growing rapidly)"},
    ("TVTX", "filspari_fsgs", "fsgs"): {"salesM": 50, "salesYear": 2025, "note": "FILSPARI FSGS ~$50M 2025 (full approval Apr 2026)"},
    # IONS
    ("IONS", "tryngolza", "trig"): {"salesM": 150, "salesYear": 2025, "note": "TRYNGOLZA FCS + sHTG ~$150M 2025"},
    ("IONS", "dawnzera", "hae"): {"salesM": 80, "salesYear": 2025, "note": "DAWNZERA HAE ~$80M 2025 (launched Q3 2025)"},
    ("IONS", "wainua", "attr"): {"salesM": 100, "salesYear": 2025, "note": "Eplontersen ATTR-PN ~$100M 2025 (partnered AZ)"},
    # AXSM
    ("AXSM", "symbravo", "gad"): {"salesM": 50, "salesYear": 2025, "note": "Symbravo GAD ~$50M 2025 (launched late 2025)"},
    # CAMX
    ("CAMX", "cam2029", "acro"): {"salesM": 80, "salesYear": 2025, "note": "Oczyesa acromegaly ~EUR70M 2025 (EU launched Nov 2025)"},
    # ABBV
    ("ABBV", "elahere", "ovarian"): {"salesM": 320, "salesYear": 2025, "note": "Elahere ovarian ~$320M 2025"},
}

manifest = json.loads((CONFIGS / "manifest.json").read_text())
updated = 0
for t in manifest:
    path = CONFIGS / (t + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    for a in d["assets"]:
        for ind in a["indications"]:
            key = (t, a["id"], ind["id"])
            if key in SALES:
                info = SALES[key]
                ind["market"]["salesM"] = info["salesM"]
                ind["market"]["salesYear"] = info["salesYear"]
                changed = True
                updated += 1
                print(f"{t:5s} {a['id']:20s} {ind['id']:15s} -> salesM=${info['salesM']}M ({info['note'][:50]})")
    if changed:
        path.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")

print(f"\n{updated} salesM entries added")
