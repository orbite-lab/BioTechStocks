# -*- coding: utf-8 -*-
"""Build configs for AKESO (9926.HK) + HCM Hutchmed (NASDAQ ADR) + JUNSHI (1877.HK).

Three China IO leaders:
- AKESO: Cadonilimab PD-1/CTLA-4 + Ivonescimab PD-1/VEGF (HARMONi-2 beat
  Keytruda PFS HR 0.49 Sep 2024; HARMONi-3 readout 2025/2026; Summit
  ex-China $500M+$4.5B partnership)
- HCM: Fruquintinib (Takeda Fruzaqla ex-China; FDA Nov 2023 + EU/UK 2024;
  $366M global in-market FY25 +26%) + savolitinib (AZ; SAFFRON H1 2026)
  + surufatinib + sovleplenib SYK + Tagrisso China royalty (post SHPL
  divest Apr 2025 $608M)
- JUNSHI: Toripalimab China 12 indications (Tuoyi) ~$285M + Coherus
  Loqtorzi US royalty + JS207 PD-1xVEGF + tifcemalimab anti-BTLA
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
# AKESO (9926.HK) - PD-1/VEGF + PD-1/CTLA-4 bispecific platform
# ============================================================

def build_AKESO():
    # FX: 1 USD = 7.8 HKD; 1 USD = 7.25 RMB; HKD/RMB ~1.1
    co = od(
        ("ticker", "AKESO"),
        ("name", "Akeso, Inc."),
        ("currentPrice", 135.80),
        ("sharesOut", 897),
        # FY24 ending cash ~RMB 11B ~= $1.5B = HKD ~11,700M
        ("cash", 11700),  # HKD M
        ("currency", "HKD"),
        ("phase", "commercial"),
        ("subtitle", "China IO bispecific platform leader. FY25 revenue RMB 3,056M (+44% YoY) / ~$425M / ~HKD 3,400M: commercial product RMB 3,033M (+51%; ivonescimab + cadonilimab) + license RMB 23M residual. Net loss RMB 1,141M; R&D RMB 1,575M. Two flagship bispecifics: CADONILIMAB (AK104, PD-1/CTLA-4) approved China cervical 2022 + gastric 2024 1L combo + HCC + NSCLC label expansion (~120K patients cumulative); IVONESCIMAB (AK112, PD-1/VEGF) approved China May 2024 1L EGFRm NSCLC (HARMONi-A + chemo) + Mar 2025 1L PD-L1+ NSCLC monotherapy. HARMONi-2 (1L PD-L1+ NSCLC mono vs Keytruda) Sep 2024: PFS HR 0.49 (game-changer; first PD-1 mono comparator beat). HARMONi US BLA accepted; FDA decision pending 2026. SUMMIT THERAPEUTICS Dec 2022 ex-China deal: $500M up + $4.5B milestones + low double-digit royalties; territory US/Canada/EU/Japan/LatAm/MENA/Africa. Feb 2025: Summit-Pfizer collab to study ivonescimab + Pfizer ADCs. PIPELINE: 15 ivonescimab Ph3 (5 global, 7 head-to-head); HARMONi-3 (1L NSCLC + chemo all-comer) readout 2025/2026; HARMONi-6 (1L sqNSCLC); HARMONi-7 (1L PDL1 high mono). Cadonilimab gastric IO-resistant + cervical international H2H vs nivo. Pipeline: AK109 anti-VEGFR2, AK129 PD-1/LAG3, AK117 anti-CD47, AK111 IL-17, penpulimab (PD-1), ebdarokimab, ebronucimab."),
        ("yahooTicker", "9926.HK"),
    )

    assets = []

    # Cadonilimab (AK104) - PD-1/CTLA-4 bispecific
    assets.append(asset(
        "cadonilimab", "Cadonilimab (AK104) - PD-1 x CTLA-4 bispecific (first global PD-1/CTLA-4 bispecific approved)",
        "Commercial China (cervical 2022 + gastric 2024 1L combo + HCC; ~120K patients cumulative)",
        "antibody.bispecific.pd1_ctla4",
        [
            innov_ind("gastric_cad", "Gastric/GEJ 1L combo (NRDL-listed China 2024)",
                      "oncology.gi.gastric",
                      regions((50, 80, 100), (75, 70, 65), (1500, 18, 18)),
                      slice_((0.1, 1, 0.1), (0.1, 1, 0.1), (8, 50, 10)),
                      {"row.priceK": "Cadonilimab China NRDL ~RMB 70K/yr (~$10K)",
                       "row.reachPct": "Cadonilimab ~8% gastric 1L IO China share post-NRDL"},
                      salesM=120, salesYear=2025, peakYear=2030, cagrPct=30, penPct=22),
            innov_ind("cervical_cad", "Cervical 2L+ (China approved 2022)",
                      "oncology.gynecologic.cervical",
                      regions((10, 80, 100), (15, 70, 70), (200, 18, 15)),
                      slice_((0.1, 1, 0.1), (0.1, 1, 0.1), (15, 50, 10)),
                      {"row.priceK": "Cadonilimab cervical NRDL ~$10K/yr",
                       "row.reachPct": "Cadonilimab cervical 2L+ China leading IO option"},
                      salesM=50, salesYear=2025, peakYear=2028, cagrPct=10, penPct=20),
        ],
        targets=["PDCD1", "CTLA4"]))

    # Ivonescimab (AK112) - PD-1/VEGF bispecific - flagship
    assets.append(asset(
        "ivonescimab", "Ivonescimab (AK112) - PD-1 x VEGF bispecific (HARMONi-2 BEAT Keytruda PFS HR 0.49 Sep 2024)",
        "Commercial China (1L EGFRm NSCLC May 2024 HARMONi-A; 1L PD-L1+ NSCLC mono Mar 2025 HARMONi-2)",
        "antibody.bispecific.pd1_vegf",
        [
            innov_ind("nsclc_egfrm", "1L EGFR-mutant NSCLC + chemo (HARMONi-A; post-EGFR TKI failure)",
                      "oncology.lung.nsclc_driver",
                      regions((10, 80, 200), (15, 70, 130), (500, 18, 30)),
                      slice_((0.1, 1, 0.1), (0.1, 1, 0.1), (5, 50, 15)),
                      {"row.priceK": "Ivonescimab China NRDL ~$15K/yr",
                       "row.reachPct": "Ivonescimab 1L EGFRm NSCLC + chemo China rapidly expanding share post May 2024"},
                      salesM=140, salesYear=2025, peakYear=2030, cagrPct=50, penPct=22),
            innov_ind("nsclc_pdl1", "1L PD-L1+ NSCLC monotherapy (HARMONi-2 beat Keytruda PFS HR 0.49)",
                      "oncology.lung.nsclc_io",
                      regions((500, 80, 150), (700, 70, 100), (3000, 12, 30)),
                      slice_((0.1, 1, 0.1), (0.1, 1, 0.1), (3, 50, 15)),
                      {"row.priceK": "Ivonescimab China NRDL ~$15K/yr",
                       "row.reachPct": "Ivonescimab 1L PD-L1+ NSCLC China mono niche post Mar 2025 approval"},
                      salesM=100, salesYear=2025, peakYear=2030, cagrPct=60, penPct=20),
        ],
        targets=["PDCD1", "VEGFA"]))

    # HARMONi US (Summit ex-China; Akeso receives royalty)
    assets.append(asset(
        "summit_royalty", "Summit Therapeutics ivonescimab ex-China royalty stream (Dec 2022 $500M up + $4.5B milestones + low double-digit royalty)",
        "Phase 3 HARMONi (BLA accepted FDA; HARMONi-3 1L NSCLC + chemo readout 2025/2026; territory US/EU/Japan/LATAM)",
        "antibody.bispecific.pd1_vegf",
        [innov_ind("ivone_ex_china", "Ivonescimab ex-China (Summit; royalty stream)",
                   "oncology.lung.nsclc_io",
                   regions((500, 80, 150), (700, 70, 100), (3000, 12, 30)),
                   slice_((1, 50, 100), (0.5, 50, 70), (0, 0, 0)),
                   {"us.priceK": "Royalty proxy: low-double-digit on Summit ivonescimab ex-China sales",
                    "us.reachPct": "Akeso receives ~12% royalty on Summit ivonescimab US/EU sales"},
                   peakYear=2032, cagrPct=0, penPct=12)]))

    # Pipeline: AK129 PD-1/LAG3 bispecific
    assets.append(asset(
        "ak129", "AK129 - PD-1/LAG-3 bispecific antibody",
        "Phase 1/2 (next-gen IO bispecific)",
        "antibody.bispecific.pd1_lag3",
        [innov_ind("io_lag3_combo", "Multi-tumor IO + LAG-3 (post-PD1 progression)",
                   "oncology.multi_tumor_io.pd1_pdl1_eligible",
                   regions((500, 80, 150), (700, 70, 100), (3000, 12, 30)),
                   slice_((0.1, 1, 0.1), (0.1, 1, 0.1), (1, 50, 12)),
                   {"row.priceK": "Estimated WAC $12K/yr China launch"},
                   peakYear=2034, cagrPct=0, penPct=8)]))

    # Pipeline: AK117 anti-CD47
    assets.append(asset(
        "ak117", "AK117 (ligufalimab) - anti-CD47 mAb",
        "Phase 2/3 (myeloid checkpoint; combo with PD-1 in solid tumors + HCC + leukemia)",
        "antibody.monoclonal.anti_cd47",
        [innov_ind("io_cd47", "Solid tumors + leukemia (CD47 myeloid checkpoint; combo with cadonilimab/ivonescimab)",
                   "oncology.multi_tumor_io.pd1_pdl1_eligible",
                   regions((500, 80, 150), (700, 70, 100), (3000, 12, 30)),
                   slice_((0.1, 1, 0.1), (0.1, 1, 0.1), (1, 40, 10)),
                   {"row.priceK": "Estimated WAC $10K/yr"},
                   peakYear=2033, cagrPct=0, penPct=6)]))

    # Premium scenarios -- ivonescimab is the value driver
    weights = {"mega_bear": 8, "bear": 18, "base": 38, "bull": 28, "psychedelic_bull": 8}
    # FY25 HKD 3,400M; FY26 expected ~HKD 5-6B with ivonescimab ramp + new approvals
    crev = {"mega_bear": 4500, "bear": 5500, "base": 7000, "bull": 9500, "psychedelic_bull": 14000}
    cmult = {"mega_bear": 4, "bear": 7, "base": 12, "bull": 18, "psychedelic_bull": 30}
    pmult = {"mega_bear": 5, "bear": 10, "base": 18, "bull": 25, "psychedelic_bull": 30}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}
    # Big milestones from Summit deal
    milestones = {"mega_bear": 200, "bear": 800, "base": 2500, "bull": 6000, "psychedelic_bull": 12000}

    asset_inds = [
        ("cadonilimab", ["gastric_cad", "cervical_cad"]),
        ("ivonescimab", ["nsclc_egfrm", "nsclc_pdl1"]),
    ]

    pos_grid = {
        "summit_royalty": {"mega_bear": 50, "bear": 70, "base": 85, "bull": 93, "psychedelic_bull": 97},
        "ak129":          {"mega_bear": 8,  "bear": 18, "base": 32, "bull": 48, "psychedelic_bull": 65},
        "ak117":          {"mega_bear": 12, "bear": 22, "base": 38, "bull": 55, "psychedelic_bull": 70},
    }
    apr_default = {"mega_bear": 60, "bear": 75, "base": 85, "bull": 92, "psychedelic_bull": 96}
    pen_default = {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25}

    pipeline_asmps = {}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "summit_royalty": OrderedDict([("ivone_ex_china", od(("pos", pos_grid["summit_royalty"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
            "ak129":          OrderedDict([("io_lag3_combo",  od(("pos", pos_grid["ak129"][sk]),          ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
            "ak117":          OrderedDict([("io_cd47",        od(("pos", pos_grid["ak117"][sk]),          ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps,
                                     milestones=milestones)

    catalysts = [
        od(("date", "Sep 2024"), ("dateSort", "2024-09-15"), ("asset", "ivonescimab"),
           ("indication", "nsclc_pdl1"),
           ("title", "HARMONi-2: ivonescimab beat Keytruda 1L PD-L1+ NSCLC mono PFS HR 0.49 (game-changer)"),
           ("type", "phase3_data"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Akeso Sep 2024 PR; HARMONi-2"), ("_confidence", "high")),
        od(("date", "H2 2026"), ("dateSort", "2026-09-30"), ("asset", "summit_royalty"),
           ("indication", "ivone_ex_china"),
           ("title", "Summit ivonescimab HARMONi US FDA decision (BLA accepted)"),
           ("type", "pdufa"), ("binary", True),
           ("fail_pos", 60), ("fail_apr", 80), ("success_pos", 92), ("success_apr", 95),
           ("_source", "Summit-Akeso Dec 2022 partnership; HARMONi BLA"), ("_confidence", "medium")),
        od(("date", "2026"), ("dateSort", "2026-12-15"), ("asset", "ivonescimab"),
           ("indication", "nsclc_pdl1"),
           ("title", "HARMONi-3 (1L NSCLC + chemo all-comer) Ph3 readout 2025/2026"),
           ("type", "phase3_data"), ("binary", True),
           ("fail_pos", 50), ("fail_apr", 75), ("success_pos", 90), ("success_apr", 92),
           ("_source", "Akeso pipeline"), ("_confidence", "high")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


# ============================================================
# HCM Hutchmed (NASDAQ ADR)
# ============================================================

def build_HCM():
    co = od(
        ("ticker", "HCM"),
        ("name", "HUTCHMED (China) Limited"),
        ("currentPrice", 14.78),
        ("sharesOut", 172),  # ADR (1 ADR = 5 ordinary)
        ("cash", 1367),  # USD M YE2025; net cash positive post SHPL divest
        ("currency", "USD"),
        ("phase", "commercial"),
        ("subtitle", "China oncology + Takeda Fruzaqla ex-China royalty. FY25 revenue $548.5M (vs $630M FY24 -- lumpy milestones); oncology/immunology consolidated $285.5M; FY26 oncology guide $330-450M. Products: FRUZAQLA (Takeda ex-China royalty + manufacturing + milestones) HCM rev $89.4M; global in-market $366.2M (+26% YoY). ELUNATE (fruquintinib China) $76.9M (-11%). SULANDA (surufatinib NETs) $27M (-45%). ORPATHYS (savolitinib AZ-partnered) $18.6M + AZ milestones $11M. TAZVERIK (tazemetostat) $2.5M (+158%). R&D services + milestones $71M. April 2025: SHPL JV divestment $608M ($416M after-tax gain) -- refocused on innovation; cash $1.367B (vs $836M YE24). Net profit FY25 $456.9M (one-time aided). PIPELINE: SAFFRON Ph3 (savolitinib + osimertinib post-Tagrisso MET-amp/over-expressed EGFRm NSCLC) -- enrollment complete Oct 2025; topline H1 2026 KEY CATALYST. SANOVO Ph3 (savolitinib + osimertinib 1L EGFRm/MET+ NSCLC) within 12 mo. FRUSICA-2 RCC 2L Ph3 POSITIVE PFS HR 0.37 ESMO 2025. Fanregratinib FGFR ihCC NDA accepted China priority. Sovleplenib (HMPL-523 SYK) ITP NDA accepted Feb 2026. Surufatinib PDAC Ph3 initiated. ATTC platform (PI3K/PIKK conjugates) HMPL-A251/A580 Ph1."),
        ("yahooTicker", "HCM"),
    )

    assets = []

    # Fruquintinib Takeda Fruzaqla royalty (ex-China)
    assets.append(asset(
        "fruzaqla", "FRUZAQLA (fruquintinib) Takeda ex-China royalty + manufacturing + milestones (FDA Nov 2023; EU/UK 2024; Japan Sep 2024)",
        "Commercial royalty (Takeda licensed Jan 2023: $400M up + $730M milestones + tiered double-digit royalty; 38 countries launched)",
        "small_molecule.kinase.multi_tki",
        [innov_ind("crc_fruzaqla", "Metastatic CRC 4L+ (post-FOLFIRI/Stivarga/Lonsurf; oral VEGFR TKI)",
                   "oncology.gi.colorectal",
                   regions((150, 80, 30), (250, 70, 20), (1500, 15, 6)),
                   slice_((6, 50, 30), (3, 50, 20), (0.5, 18, 8)),
                   {"us.reachPct": "Fruzaqla ~8% 4L+ mCRC niche post-Stivarga/Lonsurf",
                    "us.priceK": "Fruzaqla US WAC ~$30K/yr"},
                   salesM=89, salesYear=2025, peakYear=2030, cagrPct=30, penPct=18,
                   generic_bucket=True)]))

    # Elunate (fruquintinib China)
    assets.append(asset(
        "elunate", "ELUNATE (fruquintinib) - China commercial 2018; multi-TKI VEGFR for mCRC + label expansions",
        "Commercial China (-11% FY25 vs FY24 on competitive dynamics)",
        "small_molecule.kinase.multi_tki",
        [innov_ind("crc_elunate", "China mCRC 3L+ (oral VEGFR TKI; pricing pressure NRDL)",
                   "oncology.gi.colorectal",
                   regions((1, 1, 0.1), (1, 1, 0.1), (1500, 18, 6)),
                   slice_((0, 0, 0), (0, 0, 0), (8, 50, 6)),
                   {"row.priceK": "Elunate China NRDL ~$6K/yr",
                    "row.reachPct": "Elunate ~8% China mCRC 3L+ share post-NRDL"},
                   salesM=77, salesYear=2025, peakYear=2027, cagrPct=-5, penPct=18)]))

    # Surufatinib (Sulanda) - NETs China
    assets.append(asset(
        "sulanda", "SULANDA (surufatinib) - VEGFR/FGFR/CSF1R multi-TKI for neuroendocrine tumors China",
        "Commercial China (-45% FY25 vs FY24 on competitive PDAC failure + pricing)",
        "small_molecule.kinase.multi_tki",
        [innov_ind("net_sulanda", "China neuroendocrine tumors (pNET + epNET; oral TKI)",
                   "oncology.neuroendocrine.gi_pancreatic_net",
                   regions((1, 1, 0.1), (1, 1, 0.1), (200, 25, 12)),
                   slice_((0, 0, 0), (0, 0, 0), (15, 50, 8)),
                   {"row.priceK": "Sulanda China NRDL ~$8K/yr"},
                   salesM=27, salesYear=2025, peakYear=2027, cagrPct=-15, penPct=20)]))

    # Orpathys (savolitinib) - AZ partnered, MET inhibitor
    assets.append(asset(
        "orpathys", "ORPATHYS (savolitinib) - selective MET inhibitor (AstraZeneca partnered; China NSCLC EGFR-resistant 2021)",
        "Commercial China (HCM rev $18.6M FY25 + AZ milestones $11M; SAFFRON/SANOVO Ph3 ongoing)",
        "small_molecule.kinase.met",
        [innov_ind("nsclc_met", "China NSCLC MET-amplified (post-Tagrisso EGFRm) + 1L MET+",
                   "oncology.lung.nsclc_driver",
                   regions((1, 1, 0.1), (1, 1, 0.1), (500, 18, 30)),
                   slice_((0, 0, 0), (0, 0, 0), (2, 50, 25)),
                   {"row.priceK": "Orpathys China NRDL ~$25K/yr"},
                   salesM=30, salesYear=2025, peakYear=2030, cagrPct=20, penPct=15)]))

    # Pipeline: SAFFRON Ph3 - critical near-term catalyst H1 2026
    assets.append(asset(
        "saffron", "SAFFRON Ph3 (savolitinib + osimertinib post-Tagrisso MET-amp/over-expressed EGFRm NSCLC)",
        "Phase 3 (enrollment complete Oct 31 2025; topline H1 2026 KEY CATALYST; AZ-partnered)",
        "small_molecule.kinase.met",
        [innov_ind("nsclc_saffron", "Post-Tagrisso MET-amp/over-expressed EGFRm NSCLC (vs platinum chemo)",
                   "oncology.lung.nsclc_driver",
                   regions((10, 80, 200), (15, 70, 130), (60, 18, 35)),
                   slice_((10, 60, 100), (5, 50, 70), (0.5, 18, 30)),
                   {"us.reachPct": "Savolitinib + Tagrisso post-Tagrisso MET-amp niche (~30% post-osimertinib MET-amp resistance)",
                    "us.priceK": "Estimated WAC $100K/yr (combo; HCM royalty share via AZ)"},
                   peakYear=2032, cagrPct=0, penPct=15)]))

    # Sovleplenib SYK (ITP)
    assets.append(asset(
        "sovleplenib", "Sovleplenib (HMPL-523) - SYK inhibitor for chronic ITP",
        "Commercial-pending China (NDA accepted Feb 2026; warm AIHA Ph3 positive)",
        "small_molecule.kinase.syk",
        [innov_ind("itp_syk", "Chronic immune thrombocytopenia (SYK; oral)",
                   "rare_disease.hematology.thrombocytopenia",
                   regions((25, 70, 30), (35, 60, 18), (200, 18, 6)),
                   slice_((0, 0, 0), (0, 0, 0), (15, 50, 8)),
                   {"row.priceK": "Sovleplenib China estimated WAC $8K/yr"},
                   peakYear=2031, cagrPct=0, penPct=12)]))

    # Fanregratinib FGFR ihCC
    assets.append(asset(
        "fanregratinib", "Fanregratinib (HMPL-453) - selective FGFR inhibitor for intrahepatic cholangiocarcinoma",
        "NDA accepted China priority review (FGFR2-fusion ihCC)",
        "small_molecule.kinase.fgfr",
        [innov_ind("ihcc_fgfr", "Intrahepatic cholangiocarcinoma FGFR2-fusion (vs Pemazyre, Truseltiq)",
                   "oncology.gi.cholangiocarcinoma",
                   regions((3, 80, 150), (5, 70, 100), (30, 18, 25)),
                   slice_((0, 0, 0), (0, 0, 0), (10, 50, 30)),
                   {"row.priceK": "Fanregratinib China estimated $30K/yr"},
                   peakYear=2031, cagrPct=0, penPct=12)]))

    weights = {"mega_bear": 12, "bear": 25, "base": 38, "bull": 20, "psychedelic_bull": 5}
    # FY25 oncology $285M one-time-aided; FY26 guide $330-450M; recurring run-rate
    crev = {"mega_bear": 280, "bear": 340, "base": 400, "bull": 500, "psychedelic_bull": 700}
    cmult = {"mega_bear": 3, "bear": 5, "base": 7, "bull": 10, "psychedelic_bull": 14}
    pmult = {"mega_bear": 3, "bear": 5, "base": 7, "bull": 11, "psychedelic_bull": 16}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [
        ("fruzaqla", ["crc_fruzaqla"]),
        ("elunate", ["crc_elunate"]),
        ("sulanda", ["net_sulanda"]),
        ("orpathys", ["nsclc_met"]),
    ]

    pos_grid = {
        "saffron":       {"mega_bear": 35, "bear": 55, "base": 75, "bull": 88, "psychedelic_bull": 95},
        "sovleplenib":   {"mega_bear": 70, "bear": 85, "base": 95, "bull": 99, "psychedelic_bull": 100},
        "fanregratinib": {"mega_bear": 60, "bear": 78, "base": 90, "bull": 96, "psychedelic_bull": 99},
    }
    apr_default = {"mega_bear": 65, "bear": 78, "base": 88, "bull": 93, "psychedelic_bull": 97}
    pen_default = {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25}

    pipeline_asmps = {}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "saffron":       OrderedDict([("nsclc_saffron",  od(("pos", pos_grid["saffron"][sk]),       ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
            "sovleplenib":   OrderedDict([("itp_syk",        od(("pos", pos_grid["sovleplenib"][sk]),   ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
            "fanregratinib": OrderedDict([("ihcc_fgfr",      od(("pos", pos_grid["fanregratinib"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "H1 2026"), ("dateSort", "2026-06-30"), ("asset", "saffron"),
           ("indication", "nsclc_saffron"),
           ("title", "SAFFRON Ph3 topline (savolitinib+osimertinib post-Tagrisso MET-amp NSCLC; AZ-partnered)"),
           ("type", "phase3_data"), ("binary", True),
           ("fail_pos", 35), ("fail_apr", 70), ("success_pos", 88), ("success_apr", 92),
           ("_source", "HCM enrollment complete Oct 31 2025"), ("_confidence", "high")),
        od(("date", "Feb 2026"), ("dateSort", "2026-02-28"), ("asset", "sovleplenib"),
           ("indication", "itp_syk"),
           ("title", "Sovleplenib SYK ITP NDA accepted China"),
           ("type", "nda_submission"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "HCM Feb 2026"), ("_confidence", "high")),
        od(("date", "Apr 2025"), ("dateSort", "2025-04-15"), ("asset", "fruzaqla"),
           ("indication", "crc_fruzaqla"),
           ("title", "SHPL JV divestment $608M ($416M after-tax gain; refocused on innovation)"),
           ("type", "ma_close"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "HCM Apr 2025 PR"), ("_confidence", "high")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


# ============================================================
# JUNSHI (1877.HK) - Toripalimab originator + Coherus US royalty
# ============================================================

def build_JUNSHI():
    co = od(
        ("ticker", "JUNSHI"),
        ("name", "Shanghai Junshi Biosciences Co. Ltd."),
        ("currentPrice", 20.96),
        ("sharesOut", 1030),
        # Cash RMB 3,195M ~= HKD 3,500M / $440M
        ("cash", 3500),  # HKD M
        ("currency", "HKD"),
        ("phase", "commercial"),
        ("subtitle", "China PD-1 originator (toripalimab; Loqtorzi US via Coherus). FY25 revenue RMB 2,498M / ~$345M / ~HKD 2,750M (+28% YoY): Tuoyi (toripalimab China) RMB 2,068M (+38%) ~$285M dominant; VV116 oral COVID antiviral + Coherus Loqtorzi US royalty 20% (~$8M FY25 from Coherus' $40.8M) + LEO Pharma EU/UK distribution deal 2025. Toripalimab China: 12 approved indications -- NPC (2L+ + 1L combo), ESCC 1L combo, NSCLC 1L combo (sq+non-sq), urothelial 2L, melanoma 2L, perioperative NSCLC (neoadjuvant+adjuvant), HCC, RCC, TNBC, SCLC, GC/GEJ. R&D RMB 1,384M (+9%); net loss narrowing materially toward profitability inflection 2027/2028. PIPELINE: Tifcemalimab (TAB001 anti-BTLA, first-in-class checkpoint; sublicensed to Coherus US/Canada Mar 2024); JS001sc toripalimab subcutaneous Ph3 met primary 2025; JS207 PD-1xVEGF bispecific (competing Akeso ivonescimab) Ph2/3; JS212 EGFR/HER3 bispecific ADC FDA IND clearance Dec 2025; JS213 PD-1/IL-2 fusion; JS018-1 anti-IL-21; JT118 monkeypox vaccine NMPA-approved."),
        ("yahooTicker", "1877.HK"),
    )

    assets = []

    # Toripalimab China (Tuoyi) - dominant
    assets.append(asset(
        "tuoyi", "Tuoyi (toripalimab) - anti-PD-1 mAb (originator; 12 approved China indications)",
        "Commercial China (multi-tumor PD-1 backbone; 1L+ NPC/ESCC/NSCLC/urothelial/melanoma/HCC/RCC/TNBC/SCLC/GC perioperative)",
        "antibody.monoclonal.anti_pd1",
        [
            innov_ind("npc_tori", "Nasopharyngeal carcinoma 2L+ + 1L combo (China NRDL)",
                      "oncology.head_neck.npc",
                      regions((1, 1, 0.1), (1, 1, 0.1), (130, 80, 25)),
                      slice_((0, 0, 0), (0, 0, 0), (40, 60, 10)),
                      {"row.priceK": "Toripalimab China NRDL ~$10K/yr",
                       "row.reachPct": "Toripalimab ~50% China NPC IO share"},
                      salesM=80, salesYear=2025, peakYear=2030, cagrPct=15, penPct=25),
            innov_ind("escc_nsclc_tori", "ESCC + NSCLC 1L combo + urothelial + melanoma + HCC + RCC + TNBC + SCLC + GC",
                      "oncology.lung.nsclc_io",
                      regions((1, 1, 0.1), (1, 1, 0.1), (3000, 12, 30)),
                      slice_((0, 0, 0), (0, 0, 0), (5, 50, 10)),
                      {"row.priceK": "Toripalimab China NRDL ~$10K/yr blended multi-tumor",
                       "row.reachPct": "Toripalimab ~5% China multi-tumor PD-1 share (vs Tislelizumab + Sintilimab + Camrelizumab)"},
                      salesM=205, salesYear=2025, peakYear=2030, cagrPct=30, penPct=20),
        ],
        targets=["PDCD1"]))

    # Coherus Loqtorzi US royalty
    assets.append(asset(
        "loqtorzi_royalty", "Loqtorzi (toripalimab US) Coherus royalty - 20% net sales US/Canada",
        "Commercial royalty (Coherus license $150M up + $380M milestones + 20% royalty; Loqtorzi US $40.8M FY25 -> $8M JS royalty)",
        "antibody.monoclonal.anti_pd1",
        [innov_ind("us_loqtorzi_royalty", "Loqtorzi US/Canada royalty stream (Coherus markets)",
                   "_platform.junshi_coherus_royalty",
                   regions((1, 1, 0.1), (1, 1, 0.1), (1, 50, 0.1)),
                   slice_((0, 0, 0), (0, 0, 0), (10, 50, 0.1)),
                   {"row.priceK": "20% royalty on Coherus Loqtorzi US/CA net sales"},
                   salesM=8, salesYear=2025, peakYear=2030, cagrPct=30, penPct=20,
                   generic_bucket=True)]))

    # VV116 oral COVID antiviral
    assets.append(asset(
        "vv116", "VV116 (deuremidevir hydrobromide) - oral RdRp inhibitor SARS-CoV-2",
        "Commercial China (NMPA approved 2023; partnered with Vigonvita)",
        "small_molecule.antiviral.rdrp",
        [innov_ind("covid_vv116", "COVID-19 mild-to-moderate symptomatic (China)",
                   "infectious_disease.viral.respiratory",
                   regions((1, 1, 0.1), (1, 1, 0.1), (400000, 5, 0.1)),
                   slice_((0, 0, 0), (0, 0, 0), (0.5, 30, 0.4)),
                   {"row.priceK": "VV116 China WAC ~$400/course"},
                   salesM=30, salesYear=2025, peakYear=2027, cagrPct=-10, penPct=12)]))

    # Tifcemalimab (TAB001 anti-BTLA)
    assets.append(asset(
        "tifcemalimab", "Tifcemalimab (TAB001) - first-in-class anti-BTLA checkpoint mAb (Coherus US/CA license Mar 2024)",
        "Phase 2/3 (China + US development; combo with toripalimab)",
        "antibody.monoclonal.anti_btla",
        [innov_ind("io_btla", "Solid tumors + lymphoma (BTLA checkpoint; combo with PD-1)",
                   "oncology.multi_tumor_io.pd1_pdl1_eligible",
                   regions((500, 80, 150), (700, 70, 100), (3000, 12, 30)),
                   slice_((1, 50, 100), (0.5, 40, 70), (1, 40, 12)),
                   {"us.priceK": "Estimated WAC $100K/yr in IO combo",
                    "row.priceK": "China NRDL ~$12K/yr"},
                   peakYear=2033, cagrPct=0, penPct=10)]))

    # JS207 PD-1/VEGF bispecific (competing ivonescimab)
    assets.append(asset(
        "js207", "JS207 - PD-1 x VEGF bispecific (Junshi's ivonescimab competitor)",
        "Phase 2/3 (NSCLC + multi-tumor; competing with Akeso AK112)",
        "antibody.bispecific.pd1_vegf",
        [innov_ind("nsclc_js207", "1L NSCLC PD-1/VEGF (China; competing with ivonescimab)",
                   "oncology.lung.nsclc_io",
                   regions((1, 1, 0.1), (1, 1, 0.1), (3000, 12, 30)),
                   slice_((0, 0, 0), (0, 0, 0), (1.5, 50, 12)),
                   {"row.priceK": "JS207 China estimated $12K/yr if approved",
                    "row.reachPct": "JS207 niche vs Akeso ivonescimab + Hutchmed-Astra savolitinib in NSCLC"},
                   peakYear=2033, cagrPct=0, penPct=8)]))

    # JS212 EGFR/HER3 bispecific ADC
    assets.append(asset(
        "js212", "JS212 - EGFR/HER3 bispecific ADC",
        "Phase 1 (FDA IND clearance Dec 2025; solid tumors)",
        "adc.bispecific.egfr_her3",
        [innov_ind("solid_js212", "Solid tumors (EGFR + HER3 bispecific ADC)",
                   "oncology.multi_tumor_io.pd1_pdl1_eligible",
                   regions((500, 80, 150), (700, 70, 100), (3000, 12, 30)),
                   slice_((0.3, 50, 150), (0.1, 40, 100), (0.5, 40, 25)),
                   {"us.priceK": "Estimated WAC $150K/yr (ADC class)"},
                   peakYear=2034, cagrPct=0, penPct=6)]))

    weights = {"mega_bear": 12, "bear": 25, "base": 35, "bull": 22, "psychedelic_bull": 6}
    # FY25 HKD 2,750M; FY26 expected ~HKD 3,500M (+28%)
    crev = {"mega_bear": 2700, "bear": 3000, "base": 3500, "bull": 4500, "psychedelic_bull": 6000}
    cmult = {"mega_bear": 3, "bear": 5, "base": 7, "bull": 10, "psychedelic_bull": 14}
    pmult = {"mega_bear": 3, "bear": 5, "base": 8, "bull": 12, "psychedelic_bull": 18}
    pdr = {"mega_bear": 10, "bear": 9, "base": 8, "bull": 7, "psychedelic_bull": 6}

    asset_inds = [
        ("tuoyi", ["npc_tori", "escc_nsclc_tori"]),
        ("loqtorzi_royalty", ["us_loqtorzi_royalty"]),
        ("vv116", ["covid_vv116"]),
    ]

    pos_grid = {
        "tifcemalimab": {"mega_bear": 18, "bear": 30, "base": 48, "bull": 65, "psychedelic_bull": 78},
        "js207":        {"mega_bear": 15, "bear": 28, "base": 45, "bull": 60, "psychedelic_bull": 75},
        "js212":        {"mega_bear": 5,  "bear": 12, "base": 25, "bull": 40, "psychedelic_bull": 55},
    }
    apr_default = {"mega_bear": 60, "bear": 75, "base": 85, "bull": 92, "psychedelic_bull": 96}
    pen_default = {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25}

    pipeline_asmps = {}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "tifcemalimab": OrderedDict([("io_btla",      od(("pos", pos_grid["tifcemalimab"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
            "js207":        OrderedDict([("nsclc_js207",  od(("pos", pos_grid["js207"][sk]),        ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
            "js212":        OrderedDict([("solid_js212",  od(("pos", pos_grid["js212"][sk]),        ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "2025"), ("dateSort", "2025-12-15"), ("asset", "tuoyi"),
           ("indication", "escc_nsclc_tori"),
           ("title", "Toripalimab China NRDL expansion (12 indications cumulative; perioperative + GC + RCC + TNBC)"),
           ("type", "label_expansion"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Junshi FY25 release"), ("_confidence", "high")),
        od(("date", "Dec 2025"), ("dateSort", "2025-12-15"), ("asset", "js212"),
           ("indication", "solid_js212"),
           ("title", "JS212 EGFR/HER3 bispecific ADC FDA IND clearance"),
           ("type", "phase1_start"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Junshi Dec 2025 PR"), ("_confidence", "high")),
        od(("date", "2026-2027"), ("dateSort", "2027-06-30"), ("asset", "js207"),
           ("indication", "nsclc_js207"),
           ("title", "JS207 PD-1xVEGF bispecific Ph2/3 readouts (vs Akeso ivonescimab)"),
           ("type", "phase3_data"), ("binary", True),
           ("fail_pos", 15), ("fail_apr", 60), ("success_pos", 60), ("success_apr", 88),
           ("_source", "Junshi pipeline"), ("_confidence", "low")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


def main():
    write_config("AKESO", build_AKESO())
    write_config("HCM", build_HCM())
    write_config("JUNSHI", build_JUNSHI())

    manifest_path = CONFIGS / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for tk in ["AKESO", "HCM", "JUNSHI"]:
        if tk not in manifest:
            manifest.append(tk)
    manifest = sorted(set(manifest))
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"\n  manifest -> {len(manifest)} tickers")


if __name__ == "__main__":
    main()
