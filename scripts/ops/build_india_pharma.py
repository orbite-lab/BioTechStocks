# -*- coding: utf-8 -*-
"""Build configs for ZYDUSLIFE + BIOCON + TORNTPHARM + GLENMARK Indian pharma.

Four Indian pharma companies with mix of generics + innovative branded
+ biosimilars + selective specialty pipelines:
- ZYDUSLIFE (532321): generics + Saroglitazar PBC/MASH + Desidustat + DNA vaccine
- BIOCON (532523): biosimilars pure-play + insulin franchise; heavy debt post-Viatris
- TORNTPHARM (500420): branded India + EU/Brazil + JB Chem acq Jan 2026
- GLENMARK (532296): branded India + Ryaltris EU + ISB 2001 AbbVie deal

Run:
  py scripts/ops/build_india_pharma.py
  py scripts/ops/expand_generic_mixes.py
  py scripts/ops/reconcile_sliders.py
  py scripts/ops/audit_configs.py
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
              peakYear=2030, cagrPct=0, penPct=20):
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
    return od(("id", id_), ("name", name), ("area", area), ("market", m))


def asset(id_, name, stage, modality, indications, targets=None):
    return od(
        ("id", id_), ("name", name), ("stage", stage),
        ("modality", modality), ("targets", targets or []),
        ("indications", indications),
    )


def gen_bucket(id_, name, stage, total, template, overrides=None):
    a = od(
        ("id", id_), ("name", name), ("stage", stage),
        ("modality", "small_molecule.various.heritage"), ("targets", []),
        ("totalSalesM", total), ("mixTemplate", template),
    )
    if overrides:
        a["mixOverrides"] = overrides
    a["indications"] = []
    return a


def write_config(ticker, cfg):
    path = CONFIGS / f"{ticker}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"  wrote {path.relative_to(ROOT)}")


# FX: 1 USD = 84 INR (approx 2025/26)
FX = 84.0


def commercial_inert_block(asset_inds_pairs):
    out = od()
    for aid, inds in asset_inds_pairs:
        out[aid] = od()
        for iid in inds:
            out[aid][iid] = od(("pos", 100), ("apr", 100), ("pen", 1))
    return out


def commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds_pairs,
                         pipeline_asmp_by_scen=None, milestones=None):
    SCEN = ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]
    if milestones is None:
        milestones = {"mega_bear": 0, "bear": 25, "base": 75, "bull": 200, "psychedelic_bull": 500}
    scenarios = od()
    for sk in SCEN:
        asmps = commercial_inert_block(asset_inds_pairs)
        if pipeline_asmp_by_scen and sk in pipeline_asmp_by_scen:
            for aid, inds in pipeline_asmp_by_scen[sk].items():
                asmps[aid] = inds
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
    return scenarios


# ============================================================
# ZYDUSLIFE (532321) -- US generics heavy + innovative pipeline
# ============================================================

def build_ZYDUSLIFE():
    co = od(
        ("ticker", "ZYDUSLIFE"),
        ("name", "Zydus Lifesciences Ltd."),
        ("currentPrice", 901.65),
        ("sharesOut", 1010),
        ("cash", round(350 * FX)),  # +$350M net cash
        ("currency", "INR"),
        ("phase", "commercial"),
        ("subtitle", "Indian pharma with strong US generics franchise + innovative pipeline. FY25 consolidated revenue INR 23,242 Cr / ~$2.78B (+19% YoY): US generics ~50% (~$1.39B; gVyvanse internal estimate ~$300M), India branded ~$700M (#6 IPM; +11% Q4), Consumer Wellness ~$390M (+17%), Emerging Markets + Europe + API ~$300M. Net cash ~$350M; debt-free. INNOVATION: Saroglitazar (Lipaglyn/Bilypsa) PPAR-α/γ EPICS-III Ph2b/3 HIT primary Aug 29 2025 in PBC (48.5% treatment difference vs placebo p<0.001 + ALP normalization); US NDA filing planned Q1 2026 (vs Iqirvo elafibranor + Livdelzi seladelpar already approved). MASH Ph2b ongoing. Desidustat (Oxemia) HIF-PHI CKD anemia: India 2022; China NMPA approved Mar 13 2026 (CMS Holdings royalty). ZYIL1 NLRP3 Ph2 ALS/CAPS. NEW: Zylidac Bio LLC US biologics CDMO via Agenus facility acquisition + $141M BOT/BAL (botensilimab/balstilimab) collab. Dec 2025 Formycon partnership for biosimilar pembrolizumab US/Canada. Biosimilars: bevacizumab (Lucent), trastuzumab, ranibizumab (LucentDx), adalimumab (Exemptia ~32% India share). ZyCoV-D DNA COVID vaccine wound down."),
        ("yahooTicker", "ZYDUSLIFE.NS"),
    )

    assets = []

    # Named: gVyvanse (lisdexamfetamine US generic - major contributor)
    assets.append(asset(
        "g_vyvanse", "gVyvanse (lisdexamfetamine) - amphetamine prodrug for ADHD; US authorized generic + own ANDA",
        "Commercial (FDA Aug 2023; ~$300M FY25 contribution; 6-mo exclusivity exhausted)",
        "small_molecule.gpcr.amphetamine_prodrug",
        [innov_ind("adhd_stim", "ADHD stimulant therapy (US generic share)",
                   "cns.psychiatry.adhd",
                   regions((6000, 60, 4), (8000, 40, 2.5), (40000, 12, 0.6)),
                   slice_((4, 60, 1.5), (0, 0, 0), (0, 0, 0)),
                   {"us.priceK": "gVyvanse blended ~$1.5K/yr post-LOE",
                    "us.reachPct": "Zydus ~15-20% gVyvanse volume share"},
                   salesM=300, salesYear=2025, peakYear=2027, cagrPct=-15, penPct=20)]))

    # Generic buckets
    # US ex-Vyvanse: $1.39B - $300M = $1.09B
    assets.append(gen_bucket("zydus_us_generics",
                             "Zydus US generics franchise ex-gVyvanse",
                             "Commercial (FY25 ~$1.09B US oral + injectable + complex generics ex-Vyvanse)",
                             1090, "us_generics_developed_v1"))
    assets.append(gen_bucket("zydus_india",
                             "Zydus India branded formulations + ATM franchise",
                             "Commercial (FY25 ~$700M India; #6 in IPM)",
                             700, "emerging_markets_generics_v1"))
    assets.append(gen_bucket("zydus_consumer",
                             "Zydus Consumer Wellness franchise (Zydus Wellness consol)",
                             "Commercial (FY25 ~$390M consumer)",
                             390, "emerging_markets_generics_v1"))
    assets.append(gen_bucket("zydus_em_eu",
                             "Zydus Emerging Markets + Europe + API franchise",
                             "Commercial (FY25 ~$300M)",
                             300, "emerging_markets_generics_v1"))

    # Innovative pipeline
    assets.append(asset(
        "saroglitazar", "Saroglitazar (Lipaglyn / Bilypsa) - PPAR-alpha/gamma dual agonist (Zydus discovery)",
        "Phase 2b/3 PBC EPICS-III HIT primary Aug 29 2025; US NDA filing planned Q1 2026; MASH Ph2b; India approved NASH/dyslipidemia",
        "small_molecule.nuclear_receptor.ppar_dual",
        [
            innov_ind("pbc", "Primary biliary cholangitis (anti-cholestatic)",
                      "cardio_metabolic.liver.pbc",
                      regions((30, 80, 80), (45, 70, 50), (200, 18, 12)),
                      slice_((10, 60, 70), (5, 50, 40), (0.5, 18, 10)),
                      {"us.priceK": "Estimated WAC $70K/yr (vs Ocaliva obeticholic acid ~$92K)",
                       "us.reachPct": "Saroglitazar PBC if approved ~10% PBC Rx (vs Ocaliva, Iqirvo elafibranor)"},
                      peakYear=2031, cagrPct=0, penPct=15),
            innov_ind("mash", "Metabolic dysfunction-associated steatohepatitis (MASH F2-F3)",
                      "cardio_metabolic.liver.mash",
                      regions((6000, 30, 30), (10000, 20, 18), (35000, 5, 5)),
                      slice_((0.3, 35, 25), (0.1, 25, 15), (0.02, 8, 5)),
                      {"us.priceK": "Estimated WAC $25K/yr if approved (post-Resmetirom + GLP-1 class competition)"},
                      peakYear=2033, cagrPct=0, penPct=10),
        ]))
    assets.append(asset(
        "desidustat", "Desidustat (Oxemia) - HIF-prolyl hydroxylase inhibitor for CKD anemia",
        "Commercial India 2022; China NMPA approval Mar 2026",
        "small_molecule.enzyme.hif_phi",
        [innov_ind("ckd_anemia", "CKD anemia (HIF-PHI oral; vs ESA injectable)",
                   "nephrology.ckd.anemia",
                   regions((300, 70, 7), (450, 60, 5), (2500, 18, 2)),
                   slice_((0.1, 1, 0.1), (0.1, 1, 0.1), (1, 30, 1.0)),
                   {"row.priceK": "Desidustat India + China WAC ~$1K/yr",
                    "row.reachPct": "Niche India + China HIF-PHI; ~1% CKD anemia Rx"},
                   salesM=15, salesYear=2025, peakYear=2030, cagrPct=20, penPct=12)]))
    assets.append(asset(
        "zyil1", "ZYIL1 - selective oral NLRP3 inflammasome inhibitor",
        "Phase 2 (CAPS rare autoinflammatory + ALS exploratory)",
        "small_molecule.various.nlrp3_inhibitor",
        [innov_ind("als", "Amyotrophic lateral sclerosis (NLRP3 inflammasome neuroinflammation)",
                   "cns.neurodegeneration.als",
                   regions((30, 80, 50), (45, 70, 30), (150, 25, 8)),
                   slice_((1, 35, 20), (0.5, 30, 12), (0.05, 18, 4)),
                   {"us.priceK": "Estimated WAC $20K/yr"},
                   peakYear=2033, cagrPct=0, penPct=8)]))

    weights = {"mega_bear": 12, "bear": 25, "base": 38, "bull": 20, "psychedelic_bull": 5}
    crev = {"mega_bear": 2600, "bear": 2750, "base": 2900, "bull": 3200, "psychedelic_bull": 3700}
    crev = {k: round(v * FX) for k, v in crev.items()}  # convert to INR M
    cmult = {"mega_bear": 4, "bear": 5.5, "base": 7, "bull": 9, "psychedelic_bull": 12}
    pmult = {"mega_bear": 3, "bear": 4, "base": 5, "bull": 7, "psychedelic_bull": 10}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [("g_vyvanse", ["adhd_stim"]), ("desidustat", ["ckd_anemia"])]

    pos_grid = {
        "saroglitazar.pbc":  {"mega_bear": 60, "bear": 75, "base": 88, "bull": 95, "psychedelic_bull": 99},
        "saroglitazar.mash": {"mega_bear": 15, "bear": 25, "base": 40, "bull": 55, "psychedelic_bull": 70},
        "zyil1":             {"mega_bear": 8,  "bear": 18, "base": 32, "bull": 48, "psychedelic_bull": 65},
    }
    apr_default = {"mega_bear": 60, "bear": 75, "base": 85, "bull": 92, "psychedelic_bull": 96}
    pen_default = {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25}

    pipeline_asmps = {}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "saroglitazar": OrderedDict([
                ("pbc", od(("pos", pos_grid["saroglitazar.pbc"][sk]),
                           ("apr", apr_default[sk]),
                           ("pen", pen_default[sk]))),
                ("mash", od(("pos", pos_grid["saroglitazar.mash"][sk]),
                            ("apr", apr_default[sk]),
                            ("pen", pen_default[sk]))),
            ]),
            "zyil1": OrderedDict([("als", od(("pos", pos_grid["zyil1"][sk]),
                                    ("apr", apr_default[sk]),
                                    ("pen", pen_default[sk])))]),
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "Aug 29 2025"), ("dateSort", "2025-08-29"), ("asset", "saroglitazar"),
           ("indication", "pbc"), ("title", "Saroglitazar PBC EPICS-III Ph2b/3 HIT primary (48.5% treatment diff p<0.001)"),
           ("type", "phase3_data"), ("binary", True),
           ("fail_pos", 30), ("fail_apr", 65), ("success_pos", 88), ("success_apr", 90),
           ("_source", "Zydus PR Aug 29 2025; BioSpace"), ("_confidence", "high")),
        od(("date", "Q1 2026"), ("dateSort", "2026-03-31"), ("asset", "saroglitazar"),
           ("indication", "pbc"), ("title", "Saroglitazar PBC US NDA filing (planned)"),
           ("type", "nda_submission"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Zydus FY25 release"), ("_confidence", "high")),
        od(("date", "Mar 13 2026"), ("dateSort", "2026-03-13"), ("asset", "desidustat"),
           ("indication", "ckd_anemia"), ("title", "Desidustat China NMPA approval (CMS Holdings royalty trigger)"),
           ("type", "ema_approval"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "GlobeNewswire CMS Mar 13 2026"), ("_confidence", "high")),
        od(("date", "2026-2027"), ("dateSort", "2027-06-30"), ("asset", "saroglitazar"),
           ("indication", "mash"), ("title", "Saroglitazar MASH Ph2b biopsy readout"),
           ("type", "phase2_data"), ("binary", True),
           ("fail_pos", 15), ("fail_apr", 60), ("success_pos", 50), ("success_apr", 85),
           ("_source", "Zydus pipeline"), ("_confidence", "low")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


# ============================================================
# BIOCON (532523) -- biosimilars heavy + insulin franchise
# ============================================================

def build_BIOCON():
    co = od(
        ("ticker", "BIOCON"),
        ("name", "Biocon Ltd."),
        ("currentPrice", 362),
        ("sharesOut", 1780),  # post-Jun 2025 QIP + Dec 2025 Viatris equity buyout
        ("cash", round(-1400 * FX)),  # net debt ~$1.4B by Mar 2026 (S&P; post-deleveraging from $2.9B Sep 2025 peak)
        ("currency", "INR"),
        ("phase", "commercial"),
        ("subtitle", "Indian biosimilars + insulin pure-play. FY25 CONSOLIDATED revenue INR 16,500 Cr / ~$1.97B (NOT 1.08B): Biocon Biologics ~$1.10B + Biocon Pharma generics ~$400M (Q4 +46% on lenalidomide US launch) + Syngene CRO ~$435M (separately listed). MAJOR 2025/26 EVENTS: Jun 2025 QIP $525M for debt reduction; Dec 2025 Viatris convertible buyout $815M ($400M cash + $415M new equity, closes Q1 CY2026); Biocon Biologics IPO CANCELLED, full merger into BIOCON parent by Mar 31 2026. S&P expects debt $2.9B (Sep 2025) -> ~$1.4B (Mar 2026). Biosimilars: Hulio adalimumab (FKB 2023 global rights), Semglee/Rezvoglar (first US interchangeable Lantus), Fulphila pegfilgrastim, Ogivri trastuzumab, Abevmy/Kirsty bevacizumab, Yesintek ustekinumab (US launched Feb 24 2025; 100M+ lives May 2025), Yesafili aflibercept (FDA May 2024 first interchangeable; UK launched Jan 2026, RoW Mar 2026, US H2 2026 per Regeneron settlement). Insulin Aspart/Lispro/Tresiba franchise. Pipeline: trastuzumab SC, nivolumab biosim, pembrolizumab biosim, denosumab, omalizumab, rituximab, ocrelizumab."),
        ("yahooTicker", "BIOCON.NS"),
    )

    assets = []

    # Named biosimilars with disclosed sales
    bios = [
        ("hulio", "Hulio (adalimumab biosimilar) - full global rights from FKB 2023",
         "antibody.monoclonal.anti_tnf",
         "ra_psoriasis", "RA + psoriasis + Crohn's + UC + AS (TNF-alpha)",
         "immunology.inflammatory_systemic.rheumatoid_arthritis",
         (1300, 70, 50), (2000, 60, 25), (10000, 8, 8),
         (1.5, 60, 30), (1, 50, 18), (0.1, 12, 6),
         {"us.priceK": "Hulio biosim ~70% discount vs Humira"},
         200, 8, 2029),
        ("semglee", "Semglee / Rezvoglar (insulin glargine biosimilar) - first US interchangeable to Lantus",
         "recombinant_protein.insulin.glargine",
         "diabetes_t1_t2", "T1D + T2D insulin therapy (basal long-acting glargine)",
         "endocrine.diabetes.t2d",
         (40000, 60, 1.2), (60000, 50, 0.8), (250000, 12, 0.3),
         (3, 50, 0.6), (2, 40, 0.4), (0.2, 12, 0.2),
         {"us.priceK": "Semglee biosim ~60% off Lantus"},
         210, 5, 2030),
        ("ogivri", "Ogivri (trastuzumab biosimilar) - anti-HER2",
         "antibody.monoclonal.anti_her2",
         "her2_breast", "HER2+ breast + gastric (anti-HER2)",
         "oncology.breast.her2_pos",
         (60, 80, 100), (90, 70, 70), (450, 18, 25),
         (3, 60, 60), (2, 60, 45), (0.2, 18, 16),
         {"us.priceK": "Ogivri biosim ~30% discount vs Herceptin"},
         210, 0, 2027),
        ("abevmy", "Abevmy / Kirsty (bevacizumab biosimilar) - anti-VEGF",
         "antibody.monoclonal.anti_vegf",
         "crc_nsclc", "Metastatic CRC + NSCLC + ovarian (anti-VEGF)",
         "oncology.gi.colorectal",
         (150, 80, 30), (250, 70, 20), (1500, 15, 6),
         (3, 50, 18), (2, 50, 12), (0.2, 15, 5),
         {"us.priceK": "Abevmy biosim ~30-50% discount vs Avastin"},
         200, 5, 2028),
        ("fulphila", "Fulphila (pegfilgrastim biosimilar) - long-acting G-CSF",
         "recombinant_protein.cytokine.gcsf",
         "neutropenia", "Chemotherapy-induced neutropenia (PEGylated G-CSF)",
         "oncology.supportive_care.neutropenia",
         (300, 70, 7), (450, 60, 5), (2500, 18, 2),
         (1.5, 50, 4), (1, 50, 3), (0.1, 18, 1),
         {"us.priceK": "Fulphila biosim ~50% discount vs Neulasta"},
         150, -3, 2027),
        ("yesintek", "Yesintek (ustekinumab biosimilar) - fifth Biocon biosim US launched FY25",
         "antibody.monoclonal.anti_il23p40",
         "psoriasis_ibd", "Plaque psoriasis + PsA + Crohn's + UC",
         "dermatology.inflammatory_derm.psoriasis_systemic",
         (3000, 50, 30), (4000, 40, 18), (15000, 5, 6),
         (0.3, 40, 22), (0.2, 35, 14), (0.05, 8, 4),
         {"us.priceK": "Yesintek biosim ~50% discount vs Stelara"},
         60, 50, 2030),
    ]

    for (aid, aname, modality, iid, iname, area, us_r, eu_r, row_r,
         us_s, eu_s, row_s, sources, salesM, cagr, peak) in bios:
        assets.append(asset(aid, aname, "Commercial (Biocon biosimilar)",
                            modality, [innov_ind(iid, iname, area,
                                                 regions(us_r, eu_r, row_r),
                                                 slice_(us_s, eu_s, row_s),
                                                 sources, salesM=salesM,
                                                 cagrPct=cagr, peakYear=peak,
                                                 penPct=35)]))

    # Yesafili (aflibercept) - flagship pipeline; US launch H2 2026
    assets.append(asset(
        "yesafili", "Yesafili (aflibercept biosimilar) - first interchangeable to Eylea (FDA May 2024)",
        "Commercial (FDA May 2024 first interchangeable; Canada launch Jul 2025; US launch H2 2026 per Regeneron settlement)",
        "antibody.fusion.vegf_trap",
        [innov_ind("nvamd_dme_yesafili", "nvAMD + DME + DR + RVO (anti-VEGF retina)",
                   "ophthalmology.retina.nvamd",
                   regions((2500, 75, 12), (3500, 65, 7), (15000, 12, 3)),
                   slice_((2, 50, 8), (1, 50, 5), (0.1, 12, 2)),
                   {"us.priceK": "Yesafili biosim ~30% discount vs Eylea ~$8K/yr",
                    "us.reachPct": "Yesafili first US interchangeable; large $9B+ Eylea TAM"},
                   peakYear=2031, cagrPct=40, penPct=20)]))

    # Insulin franchise (Aspart, Lispro, Tresiba bucket)
    assets.append(asset(
        "insulin_franchise", "Biocon insulin franchise (Aspart + Lispro + Tresiba mealtime + long-acting biosimilars)",
        "Commercial (Biocon-Mylan/Viatris partnership; ex-US emerging markets primarily)",
        "recombinant_protein.insulin.various",
        [innov_ind("insulin_t1_t2", "T1D + T2D mealtime + long-acting insulin (Aspart + Lispro + Tresiba biosim)",
                   "endocrine.diabetes.t2d",
                   regions((40000, 60, 1.2), (60000, 50, 0.8), (250000, 12, 0.3)),
                   slice_((0.2, 50, 0.5), (0.5, 40, 0.4), (0.3, 12, 0.2)),
                   {"row.priceK": "Insulin biosim emerging markets $200/yr blended",
                    "row.reachPct": "Biocon ~3% global insulin biosim share"},
                   salesM=200, salesYear=2025, peakYear=2030, cagrPct=10, penPct=15)]))

    # Generic buckets (Biocon Pharma generics)
    assets.append(gen_bucket("biocon_pharma_generics",
                             "Biocon Pharma generics franchise (statins + immunosuppressants)",
                             "Commercial (FY25 ~$200M Biocon Pharma generics)",
                             200, "us_generics_developed_v1"))

    weights = {"mega_bear": 12, "bear": 25, "base": 38, "bull": 20, "psychedelic_bull": 5}
    # Consolidated FY25 ~$1.97B; FY26 expected ~$2.2B with biosim ramp + Yesafili
    crev = {"mega_bear": 1850, "bear": 2000, "base": 2200, "bull": 2500, "psychedelic_bull": 3000}
    crev = {k: round(v * FX) for k, v in crev.items()}
    cmult = {"mega_bear": 3, "bear": 4.5, "base": 6, "bull": 8, "psychedelic_bull": 11}
    pmult = {"mega_bear": 2, "bear": 3, "base": 4, "bull": 6, "psychedelic_bull": 9}
    pdr = {"mega_bear": 10, "bear": 9, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [
        ("hulio", ["ra_psoriasis"]), ("semglee", ["diabetes_t1_t2"]),
        ("ogivri", ["her2_breast"]), ("abevmy", ["crc_nsclc"]),
        ("fulphila", ["neutropenia"]), ("yesintek", ["psoriasis_ibd"]),
        ("yesafili", ["nvamd_dme_yesafili"]), ("insulin_franchise", ["insulin_t1_t2"]),
    ]

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds)

    catalysts = [
        od(("date", "H2 2026"), ("dateSort", "2026-09-30"), ("asset", "yesafili"),
           ("indication", "nvamd_dme_yesafili"),
           ("title", "Yesafili US launch (post Regeneron settlement; first interchangeable Eylea biosim)"),
           ("type", "launch"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Biocon FY25 IR + Regeneron settlement"), ("_confidence", "high")),
        od(("date", "Q4 2026"), ("dateSort", "2026-12-15"), ("asset", "yesintek"),
           ("indication", "psoriasis_ibd"),
           ("title", "Yesintek (ustekinumab) US share ramp + EU launch"),
           ("type", "milestone"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Biocon FY25 IR"), ("_confidence", "high")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


# ============================================================
# TORNTPHARM (500420) -- branded India + JB Chem acq
# ============================================================

def build_TORNTPHARM():
    co = od(
        ("ticker", "TORNTPHARM"),
        ("name", "Torrent Pharmaceuticals Ltd. (post JB Chem amalgamation)"),
        ("currentPrice", 4231.50),
        ("sharesOut", 344),
        ("cash", round(-1700 * FX)),  # post bond issue INR 12,500 Cr (~$1.5B) + existing debt = ~-$1.7B
        ("currency", "INR"),
        ("phase", "commercial"),
        ("subtitle", "Indian branded + EU/Brazil specialty (#5 in IPM, #4 in cardio). FY25 standalone revenue INR 11,516 Cr / ~$1.39B (+9%): India 55% (~$770M; cardio + CNS + diabetes + GI dominant; Nikoran/Cilnidipine/Veloz/Glycomet/Pan/Pantop + Vonoprazan PCAB Takeda-licensed Jun 2024), US 10% (~$130M), Germany 10% (~$140M), Brazil ~$48M (5% +cc; not 10%), RoW + CDMO ~$210M. #2 Indian pharma post JB Chem amalgamation: announced 29-Jun-2025 ($1.39B for 46.39% KKR block; 48.80% post Feb 3 2026 open offer); closed 21-Jan-2026; SH approvals Apr 28 2026; NCLT pending H2 2026. JB adds Cilacar/Razel/Rantac/Metrogyl/Nicardia (heavily cardio). Funded via INR 12,500 Cr (~$1.5B) NCD/CP bonds AA+ 7.15-7.5%. Net debt/EBITDA 0.6x pre -> ~2.5-3x post-deal. NO innovative R&D pipeline."),
        ("yahooTicker", "TORNTPHARM.NS"),
    )

    assets = []

    # Pure mixTemplate buckets - no named brands; no pipeline
    # FY25 revenue $1.39B; post JB Chem add-on ~$300M = ~$1.7B run-rate
    # India 55% = $770M (with JB Chem add ~$1.0B post-amalgamation)
    assets.append(gen_bucket("torrent_india",
                             "Torrent India branded formulations + JB Chem add (cardio + CNS + diabetes + GI)",
                             "Commercial (FY25 ~$770M India ex-JB; +$300M JB Chem post Jan 2026 amalgamation = ~$1.07B run-rate)",
                             1070, "emerging_markets_generics_v1",
                             {"cardio_metabolic.hypertension.outpatient_generic": 0.25,
                              "cardio_metabolic.lipids.ldl_cv_risk": 0.18,
                              "cns.psychiatry.depression": 0.06,
                              "immunology.inflammatory_gi.gerd_peptic": 0.10}))
    assets.append(gen_bucket("torrent_brazil",
                             "Torrent Brazil branded generics franchise",
                             "Commercial (FY25 BRL 234M / ~$48M; +5% cc)",
                             48, "emerging_markets_generics_v1"))
    assets.append(gen_bucket("torrent_us",
                             "Torrent US generics franchise",
                             "Commercial (FY25 ~$140M; Q4 +10% cc)",
                             140, "us_generics_developed_v1"))
    assets.append(gen_bucket("torrent_germany",
                             "Torrent Germany branded generics + EU franchise",
                             "Commercial (FY25 ~$140M)",
                             140, "eu_generics_developed_v1"))
    assets.append(gen_bucket("torrent_row_cdmo",
                             "Torrent RoW + CDMO (top-5 global lozenge mfr)",
                             "Commercial (FY25 ~$210M)",
                             210, "emerging_markets_generics_v1"))

    weights = {"mega_bear": 10, "bear": 22, "base": 38, "bull": 25, "psychedelic_bull": 5}
    # FY25 standalone $1.39B + JB Chem $300M = post-amalg run-rate ~$1.7B
    # Brazil cut to ~$48M trims base slightly
    crev = {"mega_bear": 1450, "bear": 1600, "base": 1750, "bull": 2000, "psychedelic_bull": 2400}
    crev = {k: round(v * FX) for k, v in crev.items()}
    # Premium multiples reflecting #5 IPM + cardio dominance + JB synergies + dividend
    cmult = {"mega_bear": 6, "bear": 8, "base": 10, "bull": 13, "psychedelic_bull": 17}
    pmult = {"mega_bear": 3, "bear": 4, "base": 5, "bull": 7, "psychedelic_bull": 10}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    # No named branded assets; all in mixTemplate
    asset_inds = []

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds)

    catalysts = [
        od(("date", "H2 2026"), ("dateSort", "2026-09-30"), ("asset", "torrent_india"),
           ("indication", "torrent_india_outpatient_generic"),
           ("title", "JB Chemicals NCLT amalgamation completion (#2 Indian pharma)"),
           ("type", "ma_close"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Torrent IR; CCI cleared Oct 2025; SH vote Apr 2026"), ("_confidence", "high")),
        od(("date", "FY26"), ("dateSort", "2027-03-31"), ("asset", "torrent_india"),
           ("indication", "torrent_india_outpatient_generic"),
           ("title", "JB Chem cost + revenue synergies (mgmt guide INR 350 Cr)"),
           ("type", "milestone"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Torrent JB integration plan"), ("_confidence", "medium")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


# ============================================================
# GLENMARK (532296) -- pure formulations + AbbVie ISB-2001 deal
# ============================================================

def build_GLENMARK():
    co = od(
        ("ticker", "GLENMARK"),
        ("name", "Glenmark Pharmaceuticals Ltd."),
        ("currentPrice", 2403.7),
        ("sharesOut", 282.3),
        ("cash", round(-60 * FX)),  # net debt $60M (cash $206M - debt $264M Mar 2025)
        ("currency", "INR"),
        ("phase", "commercial"),
        ("subtitle", "Indian formulations specialist (post-Glenmark Life Sciences API divestment to Nirma 2024 INR 5,651 Cr; 7.84% residual). FY25 revenue INR 13,322 Cr / ~$1.60B (+13%): India ~$540M (+32% YoY; derm + respi + cardio; outstanding +14% IPM growth), Europe ~$337M (+18% YoY; Ryaltris driver), RoW ~$333M (+1.7% YoY; flat), North America ~$317M (Q4 -5% pricing pressure). Net debt ~$60M post-Nirma. INNOVATION: ISB 2001 (CD38xBCMAxCD3 trispecific TCE via Ichnos Glenmark Innovation IGI NJ subsidiary) -- ASCO 2025 Ph1 r/r MM 79% ORR / 30% CR (n=33 evaluable); FDA Fast Track May 2025; Orphan. ABBVIE LICENSING DEAL Jul 10 2025: $700M upfront + up to $1.225B milestones + tiered double-digit royalties, TERRITORY = NA + EU + Japan + Greater China (NOT global; IGI retains RoW commercialization). Total $1.925B + royalties; oncology + autoimmune indications. Ryaltris (mometasone+olopatadine FDC nasal allergic rhinitis) FDA Jan 2022; commercialized 45+ markets. Q1 FY26 PAT -86% on one-time US settlement charge."),
        ("yahooTicker", "GLENMARK.NS"),
    )

    assets = []

    # Ryaltris (mometasone + olopatadine FDC) - allergic rhinitis EU/US
    assets.append(asset(
        "ryaltris", "Ryaltris (mometasone furoate + olopatadine HCl FDC nasal spray) - Glenmark's first US NDA",
        "Commercial (FDA Jan 2022; commercialized 45+ markets; key EU growth driver +18% FY25)",
        "small_molecule.combo.intranasal_steroid_antihistamine",
        [innov_ind("allergic_rhinitis", "Allergic rhinitis (seasonal + perennial; FDC topical nasal)",
                   "respiratory.allergy.allergic_rhinitis",
                   regions((25000, 25, 0.4), (40000, 20, 0.3), (200000, 5, 0.1)),
                   slice_((0.5, 30, 0.6), (1, 35, 0.5), (0.1, 8, 0.2)),
                   {"us.priceK": "Ryaltris US WAC ~$600/yr",
                    "eu.reachPct": "Ryaltris EU 45+ market commercialization; Glenmark first NDA driving ex-US royalty + direct sales"},
                   salesM=180, salesYear=2025, peakYear=2030, cagrPct=18, penPct=22)]))

    # ISB 2001 (CD38xBCMAxCD3 trispecific) - AbbVie deal Jul 2025
    assets.append(asset(
        "isb_2001", "ISB 2001 - CD38 x BCMA x CD3 trispecific T-cell engager (Ichnos Glenmark Innovation BEAT platform)",
        "Phase 1/2 (ASCO 2025 r/r MM 79% ORR / 30% CR/sCR; FDA Fast Track May 2025; AbbVie global licensing Jul 2025)",
        "antibody.bispecific.tce_trispecific",
        [innov_ind("rrmm_isb", "Relapsed/refractory multiple myeloma 4L+ (post BCMA CAR-T + bispecific)",
                   "oncology.hematology.myeloma.4l_plus",
                   regions((40, 90, 80), (60, 80, 50), (400, 18, 18)),
                   slice_((4, 60, 80), (2, 50, 50), (0.2, 18, 18)),
                   {"us.priceK": "Estimated WAC $80K/yr (vs Carvykti BCMA CAR-T $465K + Tecvayli bispecific $42K)",
                    "us.reachPct": "ISB 2001 ~10-15% R/R MM trispecific share if approved; AbbVie commercializes"},
                   peakYear=2032, cagrPct=0, penPct=15)]))

    # Generic franchise buckets
    # Total $1.60B; named ~$180M Ryaltris; remaining ~$1.42B in buckets
    # India $540M, EU ex-Ryaltris $200M, RoW $339M, NA $310M, Other $30M
    assets.append(gen_bucket("glenmark_india",
                             "Glenmark India branded formulations (derm + respi + cardio leadership)",
                             "Commercial (FY25 ~$540M India; +32% YoY; ~14% IPM growth)",
                             540, "emerging_markets_generics_v1",
                             {"dermatology.inflammatory_derm.psoriasis_systemic": 0.10,
                              "respiratory.inflammatory.asthma_severe": 0.10}))
    assets.append(gen_bucket("glenmark_eu_ex_ryaltris",
                             "Glenmark Europe ex-Ryaltris franchise",
                             "Commercial (FY25 ~$157M EU ex-Ryaltris; total EU $337M +18% YoY)",
                             157, "eu_generics_developed_v1"))
    assets.append(gen_bucket("glenmark_row",
                             "Glenmark RoW + Emerging Markets franchise",
                             "Commercial (FY25 ~$333M; +1.7% YoY)",
                             333, "emerging_markets_generics_v1"))
    assets.append(gen_bucket("glenmark_na",
                             "Glenmark North America generics franchise",
                             "Commercial (FY25 ~$317M; Q4 -5% on pricing pressure; 51 ANDAs pending)",
                             317, "us_generics_developed_v1"))

    weights = {"mega_bear": 10, "bear": 22, "base": 38, "bull": 25, "psychedelic_bull": 5}
    crev = {"mega_bear": 1500, "bear": 1650, "base": 1800, "bull": 2050, "psychedelic_bull": 2400}
    crev = {k: round(v * FX) for k, v in crev.items()}
    cmult = {"mega_bear": 5, "bear": 7, "base": 9, "bull": 12, "psychedelic_bull": 16}
    pmult = {"mega_bear": 4, "bear": 6, "base": 9, "bull": 13, "psychedelic_bull": 18}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [("ryaltris", ["allergic_rhinitis"])]

    pos_grid = {
        "isb_2001": {"mega_bear": 25, "bear": 40, "base": 55, "bull": 70, "psychedelic_bull": 82},
    }
    apr_default = {"mega_bear": 60, "bear": 75, "base": 85, "bull": 92, "psychedelic_bull": 96}
    pen_default = {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25}

    pipeline_asmps = {}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "isb_2001": OrderedDict([("rrmm_isb", od(
                ("pos", pos_grid["isb_2001"][sk]),
                ("apr", apr_default[sk]),
                ("pen", pen_default[sk]),
            ))]),
        }

    # Bigger milestones for AbbVie deal flow
    milestones = {"mega_bear": 50, "bear": 150, "base": 350, "bull": 700, "psychedelic_bull": 1200}
    milestones = {k: round(v * FX) for k, v in milestones.items()}

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps,
                                     milestones=milestones)

    catalysts = [
        od(("date", "H2 2026"), ("dateSort", "2026-09-30"), ("asset", "isb_2001"),
           ("indication", "rrmm_isb"),
           ("title", "ISB 2001 Ph2 expansion data + AbbVie Ph2 start (CD38xBCMAxCD3 trispecific)"),
           ("type", "phase2_data"), ("binary", True),
           ("fail_pos", 30), ("fail_apr", 70), ("success_pos", 75), ("success_apr", 90),
           ("_source", "ASCO 2025 + AbbVie deal Jul 2025"), ("_confidence", "medium")),
        od(("date", "Q4 2026"), ("dateSort", "2026-12-15"), ("asset", "ryaltris"),
           ("indication", "allergic_rhinitis"),
           ("title", "Ryaltris ex-US royalty + 45+ market expansion ramp"),
           ("type", "milestone"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Glenmark FY25 IR"), ("_confidence", "high")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


def main():
    write_config("ZYDUSLIFE", build_ZYDUSLIFE())
    write_config("BIOCON", build_BIOCON())
    write_config("TORNTPHARM", build_TORNTPHARM())
    write_config("GLENMARK", build_GLENMARK())

    manifest_path = CONFIGS / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for tk in ["ZYDUSLIFE", "BIOCON", "TORNTPHARM", "GLENMARK"]:
        if tk not in manifest:
            manifest.append(tk)
    manifest = sorted(set(manifest))
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"\n  manifest -> {len(manifest)} tickers")


if __name__ == "__main__":
    main()
