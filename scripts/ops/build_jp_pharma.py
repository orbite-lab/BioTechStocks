# -*- coding: utf-8 -*-
"""Build configs for SHIONOGI (4507.T) + ONO (4528.T) Japanese mid-cap pharma.

Both are innovative-leaning (own discovery + royalty franchises), NOT
generics-makers; modeled with full named-asset breakouts + pipeline.

Run:
  py scripts/ops/build_jp_pharma.py
  py scripts/ops/reconcile_sliders.py
  py scripts/ops/audit_configs.py
  py scripts/recurring/rebuild_taxonomy.py
  py scripts/ops/snapshot_scenarios.py --update
"""
import json
from pathlib import Path
from collections import OrderedDict

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS = ROOT / "configs"


def od(*kvs):
    return OrderedDict(kvs)


def regions(us, eu, row):
    return od(
        ("us", od(("patientsK", us[0]), ("wtpPct", us[1]), ("priceK", us[2]))),
        ("eu", od(("patientsK", eu[0]), ("wtpPct", eu[1]), ("priceK", eu[2]))),
        ("row", od(("patientsK", row[0]), ("wtpPct", row[1]), ("priceK", row[2]))),
    )


def slice_(us, eu, row):
    return od(
        ("us", od(("reachPct", us[0]), ("wtpPct", us[1]), ("priceK", us[2]))),
        ("eu", od(("reachPct", eu[0]), ("wtpPct", eu[1]), ("priceK", eu[2]))),
        ("row", od(("reachPct", row[0]), ("wtpPct", row[1]), ("priceK", row[2]))),
    )


def innov_ind(id_, name, area, regs, slc, sources, salesM=0, salesYear=2025,
              peakYear=2030, cagrPct=0, penPct=20, generic_bucket=False):
    m = od(
        ("regions", regs),
        ("company_slice", slc),
        ("company_slice_sources", sources),
        ("penPct", penPct),
        ("cagrPct", cagrPct),
        ("peakYear", peakYear),
    )
    if salesM:
        m["salesM"] = salesM
        m["salesYear"] = salesYear
    if generic_bucket:
        m["_genericBucket"] = True
    return od(("id", id_), ("name", name), ("area", area), ("market", m))


def asset(id_, name, stage, modality, indications, targets=None):
    return od(
        ("id", id_), ("name", name), ("stage", stage),
        ("modality", modality), ("targets", targets or []),
        ("indications", indications),
    )


def write_config(ticker, cfg):
    path = CONFIGS / f"{ticker}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"  wrote {path.relative_to(ROOT)}")


# ============================================================
# SHIONOGI (4507.T)
# ============================================================

def build_4507():
    co = od(
        ("ticker", "4507"),
        ("name", "Shionogi & Co. Ltd."),
        ("currentPrice", 2150),
        ("sharesOut", 298),
        ("cash", 350000),  # JPY M; net cash ~¥350B
        ("currency", "JPY"),
        ("phase", "commercial"),
        ("subtitle", "Japanese pharma + ViiV royalty franchise. FY25 (Mar25) revenue ~¥450B / ~$3.0B: own products ~¥190B (Xocova ensitrelvir COVID, Mulpleta thrombocytopenia, Fetroja cefiderocol MDR Gram-neg, Symproic OIC, Intuniv ADHD JP) + ViiV royalty stream ~¥185B (10% equity stake in ViiV; dolutegravir/cabotegravir HIV) + contract ~¥30B. Net cash ~¥350B. Pipeline: Ensitrelvir SCORPIO global Ph3, S-892216 next-gen antiviral, Sangamo ST-501 tau, fosmanogepix invasive fungal Ph3, redasemtide stroke Ph3."),
        ("yahooTicker", "4507.T"),
    )

    assets = []

    # ViiV royalty franchise -- treated as a single asset with HIV indication
    # The ¥185B annual royalty stream from GSK ViiV (dolutegravir + cabotegravir)
    assets.append(asset(
        "viiv_royalty", "ViiV Healthcare 10% equity stake + dolutegravir/cabotegravir royalty stream (GSK 78.3% / Pfizer 11.7% / Shionogi 10%)",
        "Commercial (preferred dividends + royalty income on Tivicay/Triumeq/Dovato/Apretude/Cabenuva)",
        "small_molecule.enzyme.integrase_inhibitor",
        [innov_ind("hiv_ins", "HIV (integrase strand transfer inhibitor + long-acting cabotegravir LAI)",
                   "infectious_disease.viral.hiv",
                   regions((1200, 80, 35), (1500, 75, 22), (35000, 55, 6)),
                   slice_((10, 50, 8), (8, 50, 5), (1.5, 50, 1.5)),
                   {"us.priceK": "ViiV royalty income proxy: blended ~$8K/yr/patient at Shionogi share",
                    "us.reachPct": "Dolutegravir-based regimens ~50% global HIV ARV market share"},
                   salesM=1233, salesYear=2025, peakYear=2030, cagrPct=3, penPct=40)],
        targets=["INSTI"]))

    # Xocova (ensitrelvir) -- COVID antiviral
    assets.append(asset(
        "xocova", "Xocova (ensitrelvir) - oral 3CL protease inhibitor SARS-CoV-2 (Shionogi-discovered)",
        "Commercial (Japan emergency authorization Nov 2022; commercial launch Mar 2024; SCORPIO global Ph3 ongoing)",
        "small_molecule.enzyme.protease_inhibitor",
        [innov_ind("covid_treat", "COVID-19 mild-to-moderate symptomatic + post-exposure prophylaxis",
                   "infectious_disease.viral.respiratory",
                   regions((50000, 25, 0.5), (75000, 20, 0.4), (400000, 5, 0.1)),
                   slice_((0.4, 30, 1.2), (0.1, 20, 0.6), (0.02, 8, 0.2)),
                   {"row.reachPct": "Xocova Japan post-pandemic commercial demand ~5-10% symptomatic COVID Rx",
                    "row.priceK": "Xocova WAC ~¥50K/course (~$350)"},
                   salesM=233, salesYear=2025, peakYear=2028, cagrPct=10, penPct=15)]))

    # Cefiderocol (Fetroja/Fetcroja)
    assets.append(asset(
        "fetroja", "Fetroja / Fetcroja (cefiderocol) - siderophore cephalosporin for MDR Gram-negative infections (carbapenem-resistant)",
        "Commercial (FDA Nov 2019 cUTI; HABP/VABP 2020; ex-US via GSK partnership)",
        "small_molecule.antimicrobial.cephalosporin",
        [innov_ind("mdr_gramneg", "MDR Gram-negative infections (CR-Acinetobacter, CR-Pseudomonas, ESBL/CRE-Enterobacterales)",
                   "infectious_disease.bacterial.mdr_resistant",
                   regions((150, 80, 20), (200, 70, 12), (500, 25, 4)),
                   slice_((25, 60, 18), (15, 50, 10), (1, 25, 4)),
                   {"us.priceK": "Fetroja WAC ~$18K/course",
                    "us.reachPct": "Fetroja ~25% MDR Gram-neg directed therapy share (vs polymyxins, Recarbrio, Xerava)"},
                   salesM=180, salesYear=2025, peakYear=2031, cagrPct=12, penPct=30)]))

    # Mulpleta (lusutrombopag) - thrombocytopenia
    assets.append(asset(
        "mulpleta", "Mulpleta (lusutrombopag) - oral thrombopoietin receptor agonist for chronic liver disease thrombocytopenia",
        "Commercial (FDA Jul 2018; ex-US partnership)",
        "small_molecule.gpcr.tpo_agonist",
        [innov_ind("itp_cld", "Thrombocytopenia in chronic liver disease (procedure-related)",
                   "rare_disease.hematology.thrombocytopenia",
                   regions((25, 70, 30), (35, 60, 18), (200, 18, 6)),
                   slice_((20, 55, 25), (10, 45, 15), (1, 18, 5)),
                   {"us.priceK": "Mulpleta WAC ~$25K/course"},
                   salesM=73, salesYear=2025, peakYear=2030, cagrPct=5, penPct=22)]))

    # Symproic (naldemedine) - OIC
    assets.append(asset(
        "symproic", "Symproic (naldemedine) - peripherally-acting mu-opioid antagonist for opioid-induced constipation (BMS US partner)",
        "Commercial (FDA Mar 2017; BMS commercializes US)",
        "small_molecule.gpcr.opioid_antagonist",
        [innov_ind("oic", "Opioid-induced constipation (chronic non-cancer pain)",
                   "cns.pain.opioid_induced_constipation",
                   regions((4000, 35, 1.2), (6000, 25, 0.6), (15000, 8, 0.2)),
                   slice_((0.3, 35, 1.5), (0.1, 25, 0.8), (0.02, 8, 0.3)),
                   {"us.priceK": "Symproic WAC ~$1.5K/yr"},
                   salesM=60, salesYear=2025, peakYear=2028, cagrPct=2, penPct=18)]))

    # Intuniv (guanfacine) -- Japan ADHD
    assets.append(asset(
        "intuniv_jp", "Intuniv (guanfacine) - alpha-2A adrenergic agonist for ADHD (Japan rights from Takeda)",
        "Commercial (Japan only; ex-Takeda)",
        "small_molecule.gpcr.alpha2a_agonist",
        [innov_ind("adhd_jp", "ADHD pediatric + adult (Japan)",
                   "cns.psychiatry.adhd",
                   regions((6000, 60, 4), (8000, 40, 2.5), (40000, 12, 0.6)),
                   slice_((0, 0, 0), (0, 0, 0), (0.2, 30, 1.0)),
                   {"row.reachPct": "Intuniv JP ~10% ADHD Rx; Shionogi exclusive Japan",
                    "row.priceK": "Intuniv JP WAC ~¥150K/yr"},
                   salesM=100, salesYear=2025, peakYear=2028, cagrPct=2, penPct=15)]))

    # JP heritage portfolio (Crestor JP residual + Differin + Pirespa + Cymbalta JP authorized generic + others)
    assets.append(asset(
        "jp_heritage", "Shionogi Japan heritage portfolio (Crestor JP, Pirespa, Differin JP, Cymbalta JP authorized generic, Irbetan, etc.)",
        "Commercial (mature JP portfolio ~¥55B)",
        "small_molecule.various.heritage",
        [innov_ind("jp_heritage_mix", "Japan mature portfolio (cardio + dermatology + GI + IPF)",
                   "_established_products.shionogi_jp_heritage",
                   regions((1, 1, 0.1), (1, 1, 0.1), (1000, 50, 0.1)),
                   slice_((0, 0, 0), (0, 0, 0), (10, 50, 0.1)),
                   {"row.priceK": "Bucket avg ~¥50-100K/yr blended"},
                   salesM=367, salesYear=2025, peakYear=2026, cagrPct=-3,
                   penPct=20, generic_bucket=True)]))

    # Pipeline
    assets.append(asset(
        "ensitrelvir_global", "Ensitrelvir global expansion (SCORPIO-PEP post-exposure prophylaxis Ph3 + SCORPIO-SR severe-risk Ph3)",
        "Phase 3 (SCORPIO-PEP positive topline late 2024; FDA filing path 2026; SCORPIO-SR ongoing)",
        "small_molecule.enzyme.protease_inhibitor",
        [innov_ind("covid_pep", "COVID post-exposure prophylaxis (household contacts; high-risk severe disease prevention)",
                   "infectious_disease.viral.respiratory",
                   regions((50000, 30, 0.6), (75000, 25, 0.4), (400000, 8, 0.1)),
                   slice_((0.3, 35, 0.8), (0.2, 30, 0.5), (0.05, 12, 0.2)),
                   {"us.priceK": "Ensitrelvir PEP WAC ~$500/course",
                    "us.reachPct": "Niche post-exposure prophylaxis market (vs Paxlovid)"},
                   peakYear=2032, cagrPct=10, penPct=15)]))
    assets.append(asset(
        "s892216", "S-892216 - second-generation oral 3CL protease inhibitor SARS-CoV-2 (improved PK + RVPV resistance coverage)",
        "Phase 1/2 (next-gen antiviral; readouts 2026/27)",
        "small_molecule.enzyme.protease_inhibitor",
        [innov_ind("covid_next", "COVID-19 next-gen oral antiviral (improved PK)",
                   "infectious_disease.viral.respiratory",
                   regions((50000, 25, 0.5), (75000, 20, 0.4), (400000, 5, 0.1)),
                   slice_((0.2, 30, 0.6), (0.1, 25, 0.4), (0.02, 8, 0.15)),
                   {"us.priceK": "Estimated $400/course follow-on antiviral"},
                   peakYear=2033, cagrPct=0, penPct=12)]))
    assets.append(asset(
        "redasemtide", "Redasemtide (S-005151) - peptide neuroprotectant for acute ischemic stroke (post-rTPA)",
        "Phase 3 (post-stroke; readout 2026/27)",
        "peptide.synthetic.neuroprotectant",
        [innov_ind("ais_neuro", "Acute ischemic stroke neuroprotection (post-thrombolysis)",
                   "cns.cerebrovascular.acute_ischemic_stroke",
                   regions((800, 50, 8), (1200, 40, 5), (15000, 12, 1.2)),
                   slice_((1, 35, 5), (0.5, 30, 3), (0.05, 12, 1)),
                   {"us.priceK": "Estimated WAC $5K/course"},
                   peakYear=2032, cagrPct=0, penPct=10)]))
    assets.append(asset(
        "fosmanogepix", "Fosmanogepix - GWT1 inhibitor antifungal (Basilea-licensed JP; broad-spectrum invasive fungal)",
        "Phase 3 invasive candidiasis + aspergillosis",
        "small_molecule.antimicrobial.antifungal",
        [innov_ind("invasive_fungal", "Invasive candidiasis + aspergillosis (broad-spectrum systemic antifungal)",
                   "infectious_disease.fungal.invasive_systemic",
                   regions((50, 80, 25), (70, 70, 15), (200, 25, 5)),
                   slice_((10, 60, 18), (5, 50, 12), (0.5, 25, 4)),
                   {"us.priceK": "Estimated WAC $18K/course"},
                   peakYear=2032, cagrPct=0, penPct=15)]))
    assets.append(asset(
        "st501_tau", "Sangamo ST-501 - zinc-finger transcription factor (ZFP-TF) repressor for tau lowering (Sangamo collaboration)",
        "Phase 1 (Alzheimer's tauopathies; AAV-delivered ZFP-TF)",
        "gene_therapy.aav.zfp_tf",
        [innov_ind("tauopathy_ad", "Alzheimer's disease tauopathies (one-time AAV ZFP-TF tau repression)",
                   "cns.neurodegeneration.alzheimer",
                   regions((6500, 35, 50), (10000, 25, 30), (40000, 5, 8)),
                   slice_((0.3, 30, 350), (0.1, 25, 200), (0.01, 5, 50)),
                   {"us.priceK": "Estimated AAV gene therapy WAC ~$350K one-time"},
                   peakYear=2034, cagrPct=0, penPct=8)]))

    # SOTP scenarios -- big royalty franchise + diverse own + pipeline
    weights = {"mega_bear": 10, "bear": 22, "base": 38, "bull": 25, "psychedelic_bull": 5}
    crev = {"mega_bear": 420000, "bear": 440000, "base": 460000,
            "bull": 500000, "psychedelic_bull": 580000}
    # Shionogi trades at low EV/sales (~0.6-0.8x) due to Xocova one-time stockpile
    # roll-off + ViiV royalty maturing. Calibrate multiples accordingly.
    cmult = {"mega_bear": 0.5, "bear": 0.9, "base": 1.4, "bull": 2.2, "psychedelic_bull": 3.5}
    pmult = {"mega_bear": 2, "bear": 3, "base": 5, "bull": 8, "psychedelic_bull": 12}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}
    milestones = {"mega_bear": 0, "bear": 3000, "base": 10000, "bull": 25000, "psychedelic_bull": 50000}

    SCEN = ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]
    pos_grid = {
        "ensitrelvir_global": {"mega_bear": 35, "bear": 55, "base": 75, "bull": 88, "psychedelic_bull": 95},
        "s892216":            {"mega_bear": 15, "bear": 25, "base": 40, "bull": 55, "psychedelic_bull": 70},
        "redasemtide":        {"mega_bear": 10, "bear": 18, "base": 30, "bull": 45, "psychedelic_bull": 60},
        "fosmanogepix":       {"mega_bear": 30, "bear": 50, "base": 70, "bull": 85, "psychedelic_bull": 92},
        "st501_tau":          {"mega_bear": 5,  "bear": 10, "base": 22, "bull": 38, "psychedelic_bull": 55},
    }
    apr_grid = {a: {"mega_bear": 60, "bear": 75, "base": 85, "bull": 92, "psychedelic_bull": 96} for a in pos_grid}
    pen_grid = {a: {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25} for a in pos_grid}
    ind_map = {
        "ensitrelvir_global": "covid_pep",
        "s892216": "covid_next",
        "redasemtide": "ais_neuro",
        "fosmanogepix": "invasive_fungal",
        "st501_tau": "tauopathy_ad",
    }

    scenarios = od()
    commercial_inert = [
        ("viiv_royalty", "hiv_ins"), ("xocova", "covid_treat"),
        ("fetroja", "mdr_gramneg"), ("mulpleta", "itp_cld"),
        ("symproic", "oic"), ("intuniv_jp", "adhd_jp"),
        ("jp_heritage", "jp_heritage_mix"),
    ]
    for sk in SCEN:
        asmps = od()
        for aid, iid in commercial_inert:
            asmps[aid] = od((iid, od(("pos", 100), ("apr", 100), ("pen", 1))))
        for aid, iid in ind_map.items():
            asmps[aid] = od((iid, od(
                ("pos", pos_grid[aid][sk]),
                ("apr", apr_grid[aid][sk]),
                ("pen", pen_grid[aid][sk]),
            )))
        scenarios[sk] = od(
            ("wt", weights[sk]),
            ("val", od(
                ("pipelineDR", pdr[sk]),
                ("pipelineMult", pmult[sk]),
                ("commercialMult", cmult[sk]),
                ("commercialRevM", crev[sk]),
                ("milestones", milestones[sk]),
                ("dil", 0),
            )),
            ("assumptions", asmps),
        )

    catalysts = [
        od(("date", "2026"), ("dateSort", "2026-09-30"), ("asset", "ensitrelvir_global"),
           ("indication", "covid_pep"),
           ("title", "Ensitrelvir SCORPIO-PEP FDA filing decision"),
           ("type", "bla_submission"), ("binary", True),
           ("fail_pos", 35), ("fail_apr", 60), ("success_pos", 85), ("success_apr", 90),
           ("_source", "Shionogi pipeline disclosure"), ("_confidence", "medium")),
        od(("date", "H2 2027"), ("dateSort", "2027-09-30"), ("asset", "ensitrelvir_global"),
           ("indication", "covid_pep"),
           ("title", "Ensitrelvir SCORPIO-SR severe-risk Ph3 readout"),
           ("type", "phase3_data"), ("binary", True),
           ("fail_pos", 30), ("fail_apr", 55), ("success_pos", 80), ("success_apr", 88),
           ("_source", "Shionogi pipeline"), ("_confidence", "medium")),
        od(("date", "H2 2026"), ("dateSort", "2026-12-15"), ("asset", "redasemtide"),
           ("indication", "ais_neuro"),
           ("title", "Redasemtide post-stroke Ph3 readout"),
           ("type", "phase3_data"), ("binary", True),
           ("fail_pos", 8), ("fail_apr", 50), ("success_pos", 60), ("success_apr", 85),
           ("_source", "Shionogi pipeline"), ("_confidence", "medium")),
        od(("date", "H1 2027"), ("dateSort", "2027-04-30"), ("asset", "fosmanogepix"),
           ("indication", "invasive_fungal"),
           ("title", "Fosmanogepix invasive candidiasis Ph3 readout"),
           ("type", "phase3_data"), ("binary", True),
           ("fail_pos", 30), ("fail_apr", 65), ("success_pos", 85), ("success_apr", 90),
           ("_source", "Basilea/Shionogi"), ("_confidence", "medium")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


# ============================================================
# ONO (4528.T)
# ============================================================

def build_4528():
    co = od(
        ("ticker", "4528"),
        ("name", "Ono Pharmaceutical Co. Ltd."),
        ("currentPrice", 2300),
        ("sharesOut", 470),
        ("cash", 175000),  # JPY M; net cash post-Deciphera ~¥175B
        ("currency", "JPY"),
        ("phase", "commercial"),
        ("subtitle", "Japanese innovative pharma; Opdivo originator (BMS-licensed). FY24 (Mar25) revenue ~¥487B / ~$3.3B: Opdivo JP ~¥80B + Opdivo BMS ex-JP royalty ~¥115B + Forxiga JP ~¥62B (AZ co-promo) + Kyprolis JP ~¥18B + Qinlock ~¥15B (Deciphera close Jun24) + Romvimza pre-launch + tirabrutinib JP + heritage ~¥197B. Acquired Deciphera $2.4B Jun 2024: gained Qinlock GIST 4L + Romvimza (vimseltinib) TGCT FDA Feb 2025. Pipeline: ONO-4685 PD-1xCD3 bispecific Ph1 TCL, ONO-2920 TYK2/JAK1 psoriasis Ph2, DCC-3116 ULK1/2 Ph1."),
        ("yahooTicker", "4528.T"),
    )

    assets = []

    # Opdivo Japan rights -- nivolumab JP/KR/TW (Ono retained); BMS rest-of-world
    assets.append(asset(
        "opdivo_jp", "Opdivo (nivolumab) - anti-PD-1 mAb; JP/KR/TW commercialization (Ono originator; BMS ex-JP partner)",
        "Commercial (multi-tumor IO; Japan label expansion lifecycle)",
        "antibody.monoclonal.anti_pd1",
        [innov_ind("io_japan", "PD-1 IO multi-tumor (NSCLC + melanoma + RCC + GI + HCC + esophageal in Japan/KR/TW)",
                   "oncology.multi_tumor_io.pd1_pdl1_eligible",
                   regions((0.1, 1, 0.1), (0.1, 1, 0.1), (3000, 30, 70)),
                   slice_((0, 0, 0), (0, 0, 0), (1.5, 40, 60)),
                   {"row.reachPct": "Opdivo JP/KR/TW ~50% PD-1 share competing with Keytruda + Tecentriq",
                    "row.priceK": "Opdivo JP WAC ~¥3M/yr (~$20K)"},
                   salesM=870, salesYear=2025, peakYear=2029, cagrPct=2, penPct=35)],
        targets=["PDCD1"]))

    # Opdivo BMS royalty stream (ex-JP)
    assets.append(asset(
        "opdivo_royalty", "Opdivo (nivolumab) BMS ex-JP royalty stream - global ex-JP/KR/TW license to Bristol Myers Squibb",
        "Commercial (royalty income; BMS commercializes globally; Ono receives ~12% net royalty)",
        "antibody.monoclonal.anti_pd1",
        [innov_ind("io_global_royalty", "PD-1 IO global royalty (BMS ex-JP commercialization)",
                   "oncology.multi_tumor_io.pd1_pdl1_eligible",
                   regions((600, 80, 200), (800, 75, 130), (3000, 25, 40)),
                   slice_((6, 50, 15), (5, 50, 10), (0.3, 25, 5)),
                   {"us.priceK": "Royalty proxy: ~12% of BMS Opdivo $9B = ~$1B Ono share",
                    "us.reachPct": "Opdivo holds ~30% global PD-1 share (vs Keytruda dominant)"},
                   salesM=767, salesYear=2025, peakYear=2027, cagrPct=-3, penPct=40)]))

    # Forxiga JP (dapagliflozin) - co-promote with AZ
    assets.append(asset(
        "forxiga_jp", "Forxiga (dapagliflozin) - SGLT2 inhibitor; JP co-promotion with AstraZeneca",
        "Commercial (T2D + HFrEF + HFpEF + CKD JP labels)",
        "small_molecule.transporter.sglt2_inhibitor",
        [innov_ind("sglt2_jp", "T2D + HFrEF + HFpEF + CKD (multi-indication SGLT2 JP)",
                   "cardio_metabolic.diabetes.t2d",
                   regions((0, 0, 0), (0, 0, 0), (40000, 60, 1.2)),
                   slice_((0, 0, 0), (0, 0, 0), (1.5, 50, 1.3)),
                   {"row.reachPct": "Forxiga JP ~40% SGLT2 class share (vs Jardiance, Kanaglu, Suglat)",
                    "row.priceK": "Forxiga JP WAC ~¥40K/yr blended"},
                   salesM=413, salesYear=2025, peakYear=2030, cagrPct=10, penPct=25)]))

    # Kyprolis JP (carfilzomib)
    assets.append(asset(
        "kyprolis_jp", "Kyprolis (carfilzomib) - selective proteasome inhibitor; Japan rights from Amgen",
        "Commercial (relapsed/refractory multiple myeloma JP)",
        "small_molecule.enzyme.proteasome_inhibitor",
        [innov_ind("rrmm_jp", "Relapsed/refractory multiple myeloma (R/R MM 2L+) Japan",
                   "oncology.hematology.myeloma.2l_3l",
                   regions((0, 0, 0), (0, 0, 0), (130, 80, 50)),
                   slice_((0, 0, 0), (0, 0, 0), (15, 50, 35)),
                   {"row.reachPct": "Kyprolis JP ~25% R/R MM 2L+ proteasome share",
                    "row.priceK": "Kyprolis JP WAC ~¥4M/yr"},
                   salesM=120, salesYear=2025, peakYear=2028, cagrPct=3, penPct=25)]))

    # Qinlock (ripretinib) - GIST 4L ex-Deciphera
    assets.append(asset(
        "qinlock", "Qinlock (ripretinib) - switch-control KIT/PDGFRA inhibitor (Deciphera origin; Ono acquired Jun 2024)",
        "Commercial (4L GIST FDA May 2020; INTRIGUE 2L missed primary; INSIGHT 2L+ ongoing)",
        "small_molecule.kinase.kit_pdgfra",
        [innov_ind("gist_4l", "Gastrointestinal stromal tumor 4L+ (post-imatinib + sunitinib + regorafenib)",
                   "oncology.musculoskeletal.gist",
                   regions((10, 80, 80), (15, 70, 50), (60, 18, 18)),
                   slice_((25, 60, 60), (10, 50, 40), (1, 18, 12)),
                   {"us.reachPct": "Qinlock ~40% 4L GIST share (only approved 4L)",
                    "us.priceK": "Qinlock WAC ~$60K/yr"},
                   salesM=100, salesYear=2025, peakYear=2030, cagrPct=10, penPct=35)]))

    # Romvimza (vimseltinib) - TGCT, FDA Feb 2025
    assets.append(asset(
        "romvimza", "Romvimza (vimseltinib) - selective CSF1R inhibitor for tenosynovial giant cell tumor (Deciphera origin; FDA Feb 2025)",
        "Commercial (US launched Feb 2025; EU approved Sep 2025)",
        "small_molecule.kinase.csf1r",
        [innov_ind("tgct", "Tenosynovial giant cell tumor (diffuse-type symptomatic)",
                   "oncology.musculoskeletal.tgct",
                   regions((6, 70, 100), (8, 60, 60), (30, 18, 20)),
                   slice_((25, 60, 80), (15, 50, 50), (1, 18, 15)),
                   {"us.reachPct": "Romvimza vs Turalio (CSF1R class) -- Romvimza no liver tox box warning",
                    "us.priceK": "Romvimza WAC ~$80K/yr"},
                   salesM=13, salesYear=2025, peakYear=2031, cagrPct=60, penPct=20)]))

    # Tirabrutinib (Velexbru) - BTK; PCNSL/WM Japan + US Ph2
    assets.append(asset(
        "tirabrutinib", "Tirabrutinib (Velexbru / ONO-4059) - 2nd-gen selective BTK inhibitor",
        "Commercial JP (PCNSL Mar 2020; WM Aug 2020); US Ph2 PROSPECT PCNSL",
        "small_molecule.kinase.btk",
        [innov_ind("pcnsl", "Primary CNS lymphoma + Waldenstrom macroglobulinemia",
                   "oncology.hematology.nhl.dlbcl",
                   regions((6, 80, 100), (8, 70, 60), (40, 18, 20)),
                   slice_((1, 50, 60), (0.5, 40, 40), (4, 50, 25)),
                   {"row.reachPct": "Tirabrutinib JP ~40% PCNSL share; Ono first BTK approved for PCNSL",
                    "row.priceK": "Tirabrutinib JP WAC ~¥4M/yr"},
                   salesM=53, salesYear=2025, peakYear=2030, cagrPct=15, penPct=22)]))

    # JP heritage portfolio (Reyvow + Onureg + Recarbrio + Romiplate + imatinib generic + others)
    assets.append(asset(
        "jp_heritage_ono", "Ono Japan heritage portfolio (Reyvow, Onureg, Recarbrio, Romiplate, imatinib generic, Velcade, etc.)",
        "Commercial (mature JP licensed/in-licensed portfolio)",
        "small_molecule.various.heritage",
        [innov_ind("ono_jp_mix", "Japan mature portfolio (migraine, AML maintenance, anti-infective, ITP)",
                   "_established_products.ono_jp_heritage",
                   regions((1, 1, 0.1), (1, 1, 0.1), (1500, 50, 0.1)),
                   slice_((0, 0, 0), (0, 0, 0), (10, 50, 0.1)),
                   {"row.priceK": "Bucket avg ~¥100K/yr blended"},
                   salesM=1200, salesYear=2025, peakYear=2027, cagrPct=0,
                   penPct=20, generic_bucket=True)]))

    # Pipeline assets
    assets.append(asset(
        "ono_4685", "ONO-4685 - PD-1 x CD3 bispecific T-cell engager",
        "Phase 1 (T-cell lymphoma; first-in-human; expansion 2026)",
        "antibody.bispecific.tce_pd1_cd3",
        [innov_ind("tcl_rr", "Relapsed/refractory T-cell lymphoma (PTCL + CTCL)",
                   "oncology.hematology.nhl.tcell",
                   regions((10, 80, 60), (15, 70, 40), (60, 18, 12)),
                   slice_((8, 50, 80), (3, 40, 50), (0.3, 18, 15)),
                   {"us.priceK": "Estimated bispecific WAC $80K/yr"},
                   peakYear=2033, cagrPct=0, penPct=12)]))
    assets.append(asset(
        "ono_2920", "ONO-2920 - oral selective TYK2/JAK1 dual inhibitor",
        "Phase 2 (psoriasis + atopic dermatitis)",
        "small_molecule.kinase.tyk2_jak1",
        [innov_ind("psoriasis_systemic", "Moderate-severe plaque psoriasis (oral systemic)",
                   "dermatology.inflammatory_derm.psoriasis_systemic",
                   regions((3000, 50, 30), (4000, 40, 18), (15000, 5, 6)),
                   slice_((0.5, 35, 25), (0.2, 25, 15), (0.05, 8, 5)),
                   {"us.priceK": "Estimated WAC $25K/yr if approved (oral psoriasis class)"},
                   peakYear=2033, cagrPct=0, penPct=10)]))
    assets.append(asset(
        "olverembatinib_jp", "Olverembatinib (Ascentage AP-Pharma origin) - 3rd-gen BCR-ABL T315I-mutant CML inhibitor (JP rights)",
        "Phase 2 (T315I CML JP)",
        "small_molecule.kinase.bcr_abl",
        [innov_ind("cml_t315i", "Chronic myeloid leukemia T315I-mutant resistant",
                   "oncology.hematology.cml",
                   regions((30, 80, 60), (45, 70, 40), (120, 18, 12)),
                   slice_((0.5, 50, 80), (0.2, 40, 50), (5, 50, 18)),
                   {"row.priceK": "Olverembatinib JP WAC ~¥5M/yr",
                    "row.reachPct": "Niche T315I-mutant CML ~5% CML population"},
                   peakYear=2031, cagrPct=10, penPct=15)]))
    assets.append(asset(
        "dcc_3116", "DCC-3116 - selective ULK1/2 inhibitor (autophagy modulator; ex-Deciphera)",
        "Phase 1 (combinations with KRAS G12C inhibitors in pancreatic / NSCLC)",
        "small_molecule.kinase.ulk1_2",
        [innov_ind("kras_combo", "KRAS-mutant solid tumors (pancreatic + NSCLC + CRC; combo with KRAS G12C/G12D)",
                   "oncology.gi.pancreatic",
                   regions((50, 80, 100), (75, 70, 60), (350, 18, 18)),
                   slice_((1, 50, 80), (0.5, 40, 50), (0.05, 18, 15)),
                   {"us.priceK": "Estimated WAC $80K/yr in combination"},
                   peakYear=2034, cagrPct=0, penPct=8)]))
    assets.append(asset(
        "velsipity_jp", "Velsipity (ozanimod) JP - S1P1/5 modulator (JP UC filing; Pfizer ex-JP)",
        "JP filed (UC moderate-severe; pending PMDA decision)",
        "small_molecule.gpcr.s1p_modulator",
        [innov_ind("uc_jp", "Ulcerative colitis moderate-severe Japan",
                   "immunology.inflammatory_gi.ulcerative_colitis",
                   regions((0, 0, 0), (0, 0, 0), (350, 60, 35)),
                   slice_((0, 0, 0), (0, 0, 0), (3, 40, 25)),
                   {"row.priceK": "Velsipity JP WAC ~¥2.5M/yr"},
                   peakYear=2030, cagrPct=15, penPct=18)]))

    # SOTP scenarios
    weights = {"mega_bear": 10, "bear": 22, "base": 38, "bull": 25, "psychedelic_bull": 5}
    crev = {"mega_bear": 460000, "bear": 480000, "base": 500000,
            "bull": 540000, "psychedelic_bull": 620000}
    cmult = {"mega_bear": 1.6, "bear": 2.2, "base": 3.0, "bull": 4.0, "psychedelic_bull": 5.5}
    pmult = {"mega_bear": 3, "bear": 4, "base": 6, "bull": 9, "psychedelic_bull": 14}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}
    milestones = {"mega_bear": 0, "bear": 5000, "base": 15000, "bull": 35000, "psychedelic_bull": 70000}

    SCEN = ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]
    pos_grid = {
        "ono_4685":            {"mega_bear": 8,  "bear": 18, "base": 32, "bull": 48, "psychedelic_bull": 65},
        "ono_2920":            {"mega_bear": 18, "bear": 30, "base": 48, "bull": 65, "psychedelic_bull": 78},
        "olverembatinib_jp":   {"mega_bear": 35, "bear": 55, "base": 75, "bull": 88, "psychedelic_bull": 95},
        "dcc_3116":            {"mega_bear": 5,  "bear": 12, "base": 25, "bull": 40, "psychedelic_bull": 55},
        "velsipity_jp":        {"mega_bear": 70, "bear": 85, "base": 95, "bull": 99, "psychedelic_bull": 100},
    }
    apr_grid = {a: {"mega_bear": 60, "bear": 75, "base": 85, "bull": 92, "psychedelic_bull": 96} for a in pos_grid}
    pen_grid = {a: {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25} for a in pos_grid}
    ind_map = {
        "ono_4685": "tcl_rr",
        "ono_2920": "psoriasis_systemic",
        "olverembatinib_jp": "cml_t315i",
        "dcc_3116": "kras_combo",
        "velsipity_jp": "uc_jp",
    }

    scenarios = od()
    commercial_inert = [
        ("opdivo_jp", "io_japan"), ("opdivo_royalty", "io_global_royalty"),
        ("forxiga_jp", "sglt2_jp"), ("kyprolis_jp", "rrmm_jp"),
        ("qinlock", "gist_4l"), ("romvimza", "tgct"),
        ("tirabrutinib", "pcnsl"), ("jp_heritage_ono", "ono_jp_mix"),
    ]
    for sk in SCEN:
        asmps = od()
        for aid, iid in commercial_inert:
            asmps[aid] = od((iid, od(("pos", 100), ("apr", 100), ("pen", 1))))
        for aid, iid in ind_map.items():
            asmps[aid] = od((iid, od(
                ("pos", pos_grid[aid][sk]),
                ("apr", apr_grid[aid][sk]),
                ("pen", pen_grid[aid][sk]),
            )))
        scenarios[sk] = od(
            ("wt", weights[sk]),
            ("val", od(
                ("pipelineDR", pdr[sk]),
                ("pipelineMult", pmult[sk]),
                ("commercialMult", cmult[sk]),
                ("commercialRevM", crev[sk]),
                ("milestones", milestones[sk]),
                ("dil", 0),
            )),
            ("assumptions", asmps),
        )

    catalysts = [
        od(("date", "2026"), ("dateSort", "2026-12-15"), ("asset", "romvimza"),
           ("indication", "tgct"),
           ("title", "Romvimza US + EU launch ramp (TGCT first full year)"),
           ("type", "launch"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Ono FY25 IR"), ("_confidence", "high")),
        od(("date", "H2 2026"), ("dateSort", "2026-09-30"), ("asset", "tirabrutinib"),
           ("indication", "pcnsl"),
           ("title", "Tirabrutinib US PCNSL Ph2 PROSPECT readout (ASCO 2025/26)"),
           ("type", "phase2_data"), ("binary", True),
           ("fail_pos", 60), ("fail_apr", 75), ("success_pos", 92), ("success_apr", 92),
           ("_source", "Ono pipeline"), ("_confidence", "medium")),
        od(("date", "2026"), ("dateSort", "2026-12-30"), ("asset", "velsipity_jp"),
           ("indication", "uc_jp"),
           ("title", "Velsipity JP UC PMDA approval"),
           ("type", "registration"), ("binary", True),
           ("fail_pos", 60), ("fail_apr", 70), ("success_pos", 98), ("success_apr", 95),
           ("_source", "Ono FY25 IR"), ("_confidence", "high")),
        od(("date", "H1 2027"), ("dateSort", "2027-04-30"), ("asset", "ono_4685"),
           ("indication", "tcl_rr"),
           ("title", "ONO-4685 PD-1xCD3 Ph1 expansion data (T-cell lymphoma)"),
           ("type", "phase1_data"), ("binary", True),
           ("fail_pos", 5), ("fail_apr", 50), ("success_pos", 50), ("success_apr", 80),
           ("_source", "Ono pipeline"), ("_confidence", "low")),
        od(("date", "2027"), ("dateSort", "2027-06-30"), ("asset", "qinlock"),
           ("indication", "gist_4l"),
           ("title", "Qinlock label expansion Ph3 (INSIGHT 2L+ GIST)"),
           ("type", "phase3_data"), ("binary", True),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Ono/Deciphera pipeline"), ("_confidence", "medium")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


def main():
    write_config("4507", build_4507())
    write_config("4528", build_4528())

    # Update manifest
    manifest_path = CONFIGS / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for tk in ["4507", "4528"]:
        if tk not in manifest:
            manifest.append(tk)
    manifest = sorted(set(manifest))
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"\n  manifest -> {len(manifest)} tickers")


if __name__ == "__main__":
    main()
