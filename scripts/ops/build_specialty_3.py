# -*- coding: utf-8 -*-
"""Build configs for APLS (Apellis) + ASND (Ascendis) + INDV (Indivior).

Three specialty / rare-disease focused commercial biotechs each anchoring a
distinct disease franchise:
- APLS: complement (C3) -- Syfovre GA + Empaveli PNH/C3G/IC-MPGN
- ASND: TransCon platform -- Yorvipath hypoparathyroidism + Skytrofa GHD +
  Yuviwel achondroplasia (FDA Feb 2026) + IL-2/TLR7-8 oncology pipeline
- INDV: opioid use disorder franchise -- Sublocade + Suboxone + Opvee +
  AUD/CUD pipeline

Run:
  py scripts/ops/build_specialty_3.py
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


def write_config(ticker, cfg):
    path = CONFIGS / f"{ticker}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"  wrote {path.relative_to(ROOT)}")


# ============================================================
# APLS - Apellis Pharmaceuticals
# ============================================================

def build_APLS():
    co = od(
        ("ticker", "APLS"),
        ("name", "Apellis Pharmaceuticals, Inc."),
        ("currentPrice", 41),
        ("sharesOut", 128),
        ("cash", 11),  # net cash ~flat: $466M cash - $455M debt (converts + credit facility)
        ("currency", "USD"),
        ("phase", "commercial"),
        ("subtitle", "Complement C3 platform leader. FY25 reported revenue $1.0B (incl. $275M one-time Sobi royalty monetization Jul 2025; underlying product $689M). Syfovre GA $587M (FDA Feb 2023; ~60% GA share vs Astellas Izervay $440M run-rate post-FDA Feb 2025 dose-duration label expansion). Empaveli US $102M (PNH + new C3G/IC-MPGN ramp FDA Jul 2025; vs Novartis Fabhalta iptacopan in C3G). Sold 90% ex-US Aspaveli royalties to Sobi Jul 2025 for $275M up + $25M EC milestone. FY25 first profitable year: net income +$22.4M. Pipeline: APL-3007 siRNA C3 Ph2 combo with Syfovre (readout 2027), APL-90992 FcRn gene-editing IND H2 2026, Syfovre PFS sBLA H1 2026, Empaveli FSGS + DGF Ph3."),
        ("yahooTicker", "APLS"),
    )

    assets = []

    # Syfovre - geographic atrophy AMD
    assets.append(asset(
        "syfovre", "Syfovre (pegcetacoplan intravitreal) - PEGylated cyclic peptide C3 inhibitor for geographic atrophy",
        "Commercial (FDA Feb 2023; intravitreal q1mo or q2mo)",
        "peptide.cyclic.complement_c3",
        [innov_ind("ga_amd", "Geographic atrophy secondary to AMD",
                   "ophthalmology.retina.ga",
                   regions((1500, 70, 25), (2000, 50, 15), (8000, 8, 5)),
                   slice_((10, 65, 25), (4, 50, 15), (0.3, 8, 5)),
                   {"us.reachPct": "Syfovre ~60-65% US GA market share vs Astellas Izervay (avacincaptad C5)",
                    "us.priceK": "Syfovre WAC ~$2.1K/dose × 12/yr = ~$25K/yr"},
                   salesM=587, salesYear=2025, peakYear=2030, cagrPct=8, penPct=35)],
        targets=["C3"]))

    # Empaveli PNH
    assets.append(asset(
        "empaveli_pnh", "Empaveli (pegcetacoplan SC) - subcutaneous C3 inhibitor for PNH",
        "Commercial (FDA May 2021; SC infusion 2-3x/week; Sobi ex-US partner as Aspaveli)",
        "peptide.cyclic.complement_c3",
        [innov_ind("pnh", "Paroxysmal nocturnal hemoglobinuria (proximal C3 inhibition; PEGASUS Ph3 superiority over eculizumab)",
                   "hematology.rare_blood.pnh",
                   regions((6, 80, 600), (8, 70, 400), (40, 18, 100)),
                   slice_((20, 60, 450), (15, 60, 280), (1, 20, 80)),
                   {"us.reachPct": "Empaveli ~10-15% PNH share vs Soliris/Ultomiris (~85% AZ Alexion C5 dominance)",
                    "us.priceK": "Empaveli WAC ~$450K/yr (parallel to Ultomiris ~$540K)"},
                   salesM=82, salesYear=2025, peakYear=2030, cagrPct=12, penPct=20)],
        targets=["C3"]))

    # Empaveli C3G - new launch (FDA Jul 2025)
    assets.append(asset(
        "empaveli_c3g", "Empaveli (pegcetacoplan SC) - C3G + IC-MPGN expansion (FDA Jul 2025 sBLA)",
        "Commercial (FDA Jul 2025 C3G + primary IC-MPGN; first SC complement therapy in nephrology)",
        "peptide.cyclic.complement_c3",
        [innov_ind("c3g", "C3 glomerulopathy (rare progressive glomerular disease; complement-driven)",
                   "nephrology.glomerular.c3g",
                   regions((6, 80, 350), (10, 70, 220), (40, 18, 60)),
                   slice_((25, 50, 350), (10, 50, 220), (1, 18, 60)),
                   {"us.reachPct": "Empaveli vs Novartis Fabhalta iptacopan (oral factor B) -- SC dosing competitive disadvantage but proximal C3",
                    "us.priceK": "Empaveli C3G WAC ~$350K/yr"},
                   salesM=20, salesYear=2025, peakYear=2031, cagrPct=80, penPct=30)],
        targets=["C3"]))

    # APL-3007 siRNA pipeline (now Ph2 combo)
    assets.append(asset(
        "apl_3007", "APL-3007 - siRNA targeting complement C3 (q-quarterly/biannual dosing)",
        "Phase 2 (combo with Syfovre in GA; topline 2027; next-gen complement convenience)",
        "nucleic_acid.sirna.c3_silencer",
        [innov_ind("c3_sirna", "Complement-driven diseases (PNH + C3G + GA potential; SC q3-6mo dosing)",
                   "hematology.rare_blood.pnh",
                   regions((6, 80, 600), (8, 70, 400), (40, 18, 100)),
                   slice_((10, 50, 350), (5, 50, 220), (0.5, 18, 80)),
                   {"us.priceK": "Estimated WAC $350K/yr q-quarterly siRNA",
                    "us.reachPct": "APL-3007 broad complement franchise share if approved"},
                   peakYear=2034, cagrPct=0, penPct=15)]))

    # SOTP scenarios -- mid-cap commercial biotech with growing rare/ophtho franchise
    weights = {"mega_bear": 12, "bear": 25, "base": 38, "bull": 20, "psychedelic_bull": 5}
    crev = {"mega_bear": 700, "bear": 800, "base": 900, "bull": 1100, "psychedelic_bull": 1500}
    cmult = {"mega_bear": 2.0, "bear": 3.0, "base": 4.5, "bull": 6.0, "psychedelic_bull": 9.0}
    pmult = {"mega_bear": 2, "bear": 3, "base": 5, "bull": 8, "psychedelic_bull": 13}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}
    milestones = {"mega_bear": 0, "bear": 25, "base": 75, "bull": 200, "psychedelic_bull": 500}

    SCEN = ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]
    pos_grid = {"apl_3007": {"mega_bear": 15, "bear": 25, "base": 40, "bull": 55, "psychedelic_bull": 70}}
    apr_grid = {a: {"mega_bear": 60, "bear": 75, "base": 85, "bull": 92, "psychedelic_bull": 96} for a in pos_grid}
    pen_grid = {a: {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25} for a in pos_grid}
    ind_map = {"apl_3007": "c3_sirna"}

    scenarios = od()
    commercial_inert = [
        ("syfovre", "ga_amd"), ("empaveli_pnh", "pnh"),
        ("empaveli_c3g", "c3g"),
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
        od(("date", "H2 2026"), ("dateSort", "2026-09-30"), ("asset", "empaveli_c3g"),
           ("indication", "c3g"),
           ("title", "Empaveli C3G/IC-MPGN EU CHMP opinion + US ramp"),
           ("type", "ema_approval"), ("binary", True),
           ("fail_pos", 70), ("fail_apr", 80), ("success_pos", 95), ("success_apr", 95),
           ("_source", "Apellis pipeline disclosure"), ("_confidence", "high")),
        od(("date", "Sept 2026"), ("dateSort", "2026-09-15"), ("asset", "syfovre"),
           ("indication", "ga_amd"),
           ("title", "Convertible note refinancing ($402.5M 2026 notes maturity)"),
           ("type", "milestone"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "APLS 10-K"), ("_confidence", "high")),
        od(("date", "2026-2027"), ("dateSort", "2027-06-30"), ("asset", "apl_3007"),
           ("indication", "c3_sirna"),
           ("title", "APL-3007 siRNA C3 Ph1 PK/PD data"),
           ("type", "phase1_data"), ("binary", True),
           ("fail_pos", 15), ("fail_apr", 60), ("success_pos", 50), ("success_apr", 85),
           ("_source", "Apellis pipeline"), ("_confidence", "low")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


# ============================================================
# ASND - Ascendis Pharma
# ============================================================

def build_ASND():
    co = od(
        ("ticker", "ASND"),
        ("name", "Ascendis Pharma A/S"),
        ("currentPrice", 229.40),
        ("sharesOut", 60.5),
        ("cash", 665),  # net cash: €616M @ 1.08
        ("currency", "USD"),  # post Apr 20 2026 ADR conversion to direct Nasdaq listing
        ("phase", "commercial"),
        ("subtitle", "Danish-domiciled rare-disease specialty (Nasdaq direct listing post Apr 20 2026 ADR conversion). FY25 revenue €720M / ~$778M (+98%): Yorvipath palopegteriparatide adult hypoparathyroidism €477M (FDA Aug 2024; first long-acting PTH post-Takeda Natpara recall), Skytrofa lonapegsomatropin pediatric GHD €206M (vs Pfizer Ngenla weekly), royalty/license €37M. Yuviwel/navepegritide CNP achondroplasia FDA APPROVED Feb 27 2026 accelerated + 7-yr orphan exclusivity + Rare Pediatric Disease PRV; Q2 2026 US launch; EU CHMP Q4 2026 (vs BMRN Voxzogo daily). Q4 2025 first profitable qtr (€10M op profit). TransCon platform pipeline: IL-2 β/γ Ph1/2 IL-Believe (mono+pembro+chemo combos), TLR7/8 intratumoral combo Cohort 4 (post-PD-1 melanoma). Net cash €616M / ~$665M; €120M buyback FY26; $575M 2028 convertible redemption pending (up to 3.6M dilutive)."),
        ("yahooTicker", "ASND"),
    )

    assets = []

    # Yorvipath - hypoparathyroidism
    assets.append(asset(
        "yorvipath", "Yorvipath (palopegteriparatide) - long-acting PTH(1-34) prodrug for adult hypoparathyroidism",
        "Commercial (FDA Aug 2024; EU Nov 2023; pediatric submission targeted Q1 2027)",
        "peptide.long_acting.pth_analog",
        [innov_ind("hypoparathyroidism", "Adult chronic hypoparathyroidism (insufficient PTH; calcium/phosphate dysregulation)",
                   "rare_disease.endocrine.hypoparathyroidism",
                   regions((90, 70, 200), (130, 60, 130), (300, 18, 35)),
                   slice_((25, 65, 180), (8, 55, 110), (0.3, 18, 30)),
                   {"us.reachPct": "Yorvipath only long-acting PTH post-Takeda Natpara recall 2019; first-in-class adult HP",
                    "us.priceK": "Yorvipath WAC ~$180K/yr (parallel to Natpara historical pricing)"},
                   salesM=515, salesYear=2025, peakYear=2031, cagrPct=35, penPct=30)]))

    # Skytrofa - pediatric GHD
    assets.append(asset(
        "skytrofa", "Skytrofa (lonapegsomatropin) - long-acting weekly GH analog (TransCon hGH)",
        "Commercial (FDA Aug 2021; EU 2022; adult GHD label expansion in development)",
        "peptide.long_acting.gh_analog",
        [innov_ind("ped_ghd", "Pediatric growth hormone deficiency (TransCon weekly hGH)",
                   "endocrine.pituitary.gh_deficiency",
                   regions((300, 60, 25), (500, 50, 15), (2500, 12, 5)),
                   slice_((10, 60, 35), (4, 50, 22), (0.3, 12, 8)),
                   {"us.reachPct": "Skytrofa ~15% pediatric GHD share vs Pfizer Ngenla weekly + daily GHs (Genotropin/Norditropin/Humatrope)",
                    "us.priceK": "Skytrofa WAC ~$35K/yr blended pediatric"},
                   salesM=222, salesYear=2025, peakYear=2030, cagrPct=10, penPct=22)]))

    # Yuviwel (TransCon CNP) - achondroplasia, FDA Feb 27 2026
    assets.append(asset(
        "yuviwel_cnp", "Yuviwel (navepegritide) - long-acting weekly CNP analog (TransCon CNP)",
        "Commercial FDA Feb 27 2026 accelerated approval (Q2 2026 US launch); EU CHMP H2 2026",
        "peptide.long_acting.cnp_analog",
        [innov_ind("achondroplasia", "Achondroplasia age 2+ (vs BMRN Voxzogo daily; weekly dosing convenience)",
                   "musculoskeletal.bone_cartilage.achondroplasia",
                   regions((6, 80, 250), (10, 70, 150), (50, 18, 35)),
                   slice_((40, 65, 250), (15, 55, 150), (1, 18, 35)),
                   {"us.reachPct": "Yuviwel weekly vs Voxzogo daily; ~30-40% achondroplasia share post-launch",
                    "us.priceK": "Yuviwel WAC ~$250K/yr (parallel to Voxzogo)"},
                   salesM=15, salesYear=2025, peakYear=2032, cagrPct=80, penPct=30)]))

    # TransCon IL-2 (oncology IO) - Phase 1/2
    assets.append(asset(
        "transcon_il2", "TransCon IL-2 β/γ - long-acting biased IL-2 cytokine (TransCon platform)",
        "Phase 1/2 IL-Believe (RP2D 120ug/kg q3w; mono + pembro + chemo combos)",
        "recombinant_protein.cytokine.il2",
        [innov_ind("io_combo", "IO-eligible solid tumors (multi-tumor IL-2 + checkpoint combos)",
                   "oncology.multi_tumor_io.pd1_pdl1_eligible",
                   regions((500, 80, 150), (700, 70, 100), (3000, 12, 30)),
                   slice_((1, 50, 100), (0.5, 50, 70), (0.05, 12, 25)),
                   {"us.priceK": "Estimated WAC $100K/yr in IO combo"},
                   peakYear=2033, cagrPct=0, penPct=10)]))

    # TransCon TLR7/8 - oncology IO
    assets.append(asset(
        "transcon_tlr78", "TransCon TLR7/8 - intratumoral long-acting innate immunity agonist",
        "Phase 2 transcendIT-101 (HNSCC + cSCC + melanoma + HPV+ tumors)",
        "small_molecule.tlr_agonist.intratumoral",
        [innov_ind("io_intratumoral", "Intratumoral immunotherapy in advanced solid tumors (HNSCC + cSCC + melanoma)",
                   "oncology.head_neck.hnscc",
                   regions((30, 80, 100), (45, 70, 65), (250, 18, 18)),
                   slice_((1, 50, 80), (0.5, 50, 50), (0.05, 18, 15)),
                   {"us.priceK": "Estimated WAC $80K/course intratumoral"},
                   peakYear=2033, cagrPct=0, penPct=8)]))

    # SOTP scenarios -- premium rare-disease growth biotech
    weights = {"mega_bear": 8, "bear": 22, "base": 40, "bull": 25, "psychedelic_bull": 5}
    # FY25 revenue $778M; FY26 guidance implies ~$1.0-1.2B with Yorvipath + Skytrofa + Yuviwel ramp
    crev = {"mega_bear": 850, "bear": 1000, "base": 1200, "bull": 1500, "psychedelic_bull": 2200}
    # Premium multiples: rare-disease growth + first-profitable + buyback
    cmult = {"mega_bear": 4.0, "bear": 6.0, "base": 8.5, "bull": 11.0, "psychedelic_bull": 15.0}
    pmult = {"mega_bear": 3, "bear": 5, "base": 7, "bull": 10, "psychedelic_bull": 15}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}
    milestones = {"mega_bear": 0, "bear": 50, "base": 150, "bull": 400, "psychedelic_bull": 800}

    SCEN = ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]
    pos_grid = {
        "transcon_il2":   {"mega_bear": 12, "bear": 22, "base": 35, "bull": 50, "psychedelic_bull": 65},
        "transcon_tlr78": {"mega_bear": 10, "bear": 20, "base": 32, "bull": 48, "psychedelic_bull": 62},
    }
    apr_grid = {a: {"mega_bear": 60, "bear": 75, "base": 85, "bull": 92, "psychedelic_bull": 96} for a in pos_grid}
    pen_grid = {a: {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25} for a in pos_grid}
    ind_map = {"transcon_il2": "io_combo", "transcon_tlr78": "io_intratumoral"}

    scenarios = od()
    commercial_inert = [
        ("yorvipath", "hypoparathyroidism"), ("skytrofa", "ped_ghd"),
        ("yuviwel_cnp", "achondroplasia"),
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
        od(("date", "Q2 2026"), ("dateSort", "2026-06-30"), ("asset", "yuviwel_cnp"),
           ("indication", "achondroplasia"),
           ("title", "Yuviwel (TransCon CNP) US commercial launch"),
           ("type", "launch"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Ascendis FY25 results; FDA approval Feb 27 2026"), ("_confidence", "high")),
        od(("date", "Q4 2026"), ("dateSort", "2026-11-30"), ("asset", "yuviwel_cnp"),
           ("indication", "achondroplasia"),
           ("title", "Yuviwel EU CHMP opinion (TransCon CNP achondroplasia)"),
           ("type", "ema_approval"), ("binary", True),
           ("fail_pos", 80), ("fail_apr", 85), ("success_pos", 98), ("success_apr", 95),
           ("_source", "Ascendis pipeline"), ("_confidence", "high")),
        od(("date", "Q4 2025"), ("dateSort", "2025-12-31"), ("asset", "yorvipath"),
           ("indication", "hypoparathyroidism"),
           ("title", "PaTHway Adolescent trial initiation (pediatric label expansion in 12-<18yr)"),
           ("type", "phase3_start"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Ascendis Q3 2025 results"), ("_confidence", "high")),
        od(("date", "2026-2027"), ("dateSort", "2027-06-30"), ("asset", "transcon_il2"),
           ("indication", "io_combo"),
           ("title", "TransCon IL-2 β/γ Ph2 readouts (mono + pembro combos)"),
           ("type", "phase2_data"), ("binary", True),
           ("fail_pos", 12), ("fail_apr", 60), ("success_pos", 50), ("success_apr", 85),
           ("_source", "Ascendis pipeline"), ("_confidence", "low")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


# ============================================================
# INDV - Indivior
# ============================================================

def build_INDV():
    co = od(
        ("ticker", "INDV"),
        ("name", "Indivior Pharmaceuticals, Inc."),
        ("currentPrice", 37.80),
        ("sharesOut", 122),
        ("cash", 50),  # net cash post $295M DOJ payment + $400M buyback authorized
        ("currency", "USD"),
        ("phase", "commercial"),
        ("subtitle", "Opioid use disorder franchise (re-domiciled US + renamed Jan 2026 from Indivior plc; NASDAQ since Jun 2024). FY25 revenue $1.239B (+10%): Sublocade SC monthly buprenorphine ER $856M (+13%; ~70% US LAI share, ceding to Brixadi which crossed 30% YE25 from Camurus/Braeburn) + Suboxone film $300M post-LOE residual (declining 15%/yr) + Opvee nalmefene nasal $12M (marketing halted Sep 30 2025 post NY AG settlement; divestiture exploration). FDA Feb 2025 Sublocade label expansion: 1-hour rapid induction + alt injection sites. FY26 guidance: net revenue $1,125-1,195M (DOWN 5-9% on continued Suboxone decline + Brixadi share). FY25 capital return: $295M DOJ payment + $400M buyback. Pipeline: INDV-2000 orexin OX1R Ph2 OUD non-opioid maintenance (NOT alcohol; first patient Jun 2024). AEF0117 CB1 NAM CUD Ph2b FAILED Sep 2024 (Indivior unlikely to opt in)."),
        ("yahooTicker", "INDV"),
    )

    assets = []

    # Sublocade - flagship LAI buprenorphine
    assets.append(asset(
        "sublocade", "Sublocade (buprenorphine extended-release SC monthly) - depot LAI for opioid use disorder",
        "Commercial (FDA Nov 2017; flagship growth driver; ~85% LAI buprenorphine share)",
        "small_molecule.opioid.partial_agonist_depot",
        [innov_ind("oud_lai", "Opioid use disorder maintenance (long-acting injectable buprenorphine)",
                   "cns.psychiatry.substance_use.opioid",
                   regions((2500, 25, 8), (1500, 18, 5), (5000, 5, 2)),
                   slice_((20, 35, 18), (3, 25, 12), (0.2, 5, 5)),
                   {"us.reachPct": "Sublocade ~10-15% US OUD treated population on LAI vs daily Suboxone film",
                    "us.priceK": "Sublocade WAC ~$1.6K/mo × 12 = $18K/yr"},
                   salesM=856, salesYear=2025, peakYear=2030, cagrPct=8, penPct=18)],
        targets=["OPRM1"]))

    # Suboxone film - residual post-LOE
    assets.append(asset(
        "suboxone", "Suboxone film (buprenorphine + naloxone sublingual) - daily MAT for opioid use disorder",
        "Commercial (post-LOE residual brand + AG economics; declining ~20%/yr)",
        "small_molecule.opioid.partial_agonist",
        [innov_ind("oud_daily", "Opioid use disorder daily MAT (post-LOE branded share + AG)",
                   "cns.psychiatry.substance_use.opioid",
                   regions((2500, 25, 8), (1500, 18, 5), (5000, 5, 2)),
                   slice_((3, 30, 8), (0.5, 18, 5), (0, 0, 0)),
                   {"us.priceK": "Suboxone film WAC ~$8K/yr; AG/branded blended"},
                   salesM=300, salesYear=2025, peakYear=2025, cagrPct=-15, penPct=18)]))

    # Opvee - marketing halted Sep 30 2025 post NY AG settlement; divestiture exploration
    assets.append(asset(
        "opvee", "Opvee (nalmefene nasal spray) - long-acting opioid antagonist for opioid overdose reversal",
        "Commercial-discontinued (FDA May 2023; marketing halted Sep 30 2025 post NY AG settlement; divestiture exploration)",
        "small_molecule.opioid.antagonist",
        [innov_ind("opioid_overdose", "Opioid overdose emergency rescue (mostly BARDA orders post Sept 2025 marketing halt)",
                   "cns.psychiatry.substance_use.opioid",
                   regions((2500, 50, 0.4), (1500, 30, 0.2), (5000, 8, 0.1)),
                   slice_((0.05, 20, 0.4), (0, 0, 0), (0, 0, 0)),
                   {"us.priceK": "Opvee WAC ~$400/2pk; pending divestiture"},
                   salesM=12, salesYear=2025, peakYear=2025, cagrPct=-30, penPct=10)]))

    # INDV-2000: Phase 2 in OPIOID USE DISORDER (not AUD as originally tagged)
    # First patient dosed Jun 2024; 3-month dose-ranging in OUD post-buprenorphine withdrawal
    assets.append(asset(
        "indv_2000", "INDV-2000 - selective orexin-1 OX1R antagonist (Aelis Farma acquisition)",
        "Phase 2 (opioid use disorder non-opioid maintenance; first patient Jun 2024; readout 2026/27)",
        "small_molecule.gpcr.orexin_antagonist",
        [innov_ind("oud_orexin", "Opioid use disorder maintenance (novel orexin-1 mechanism; non-opioid-based MAT)",
                   "cns.psychiatry.substance_use.opioid",
                   regions((2500, 25, 8), (1500, 18, 5), (5000, 5, 2)),
                   slice_((0.5, 30, 8), (0.1, 18, 5), (0.01, 5, 2)),
                   {"us.reachPct": "INDV-2000 novel non-opioid MAT for OUD; differentiated from buprenorphine class",
                    "us.priceK": "Estimated WAC $8K/yr if approved (parallel to oral OUD Rx)"},
                   peakYear=2032, cagrPct=0, penPct=10)]))

    # NOTE: AEF0117 (CB1 NAM, cannabis use disorder) Ph2b FAILED Sep 2024
    # (primary endpoint missed; final Mar 2025 confirmed 1mg trended -16% but p=0.077).
    # Indivior PR'd it does not expect to opt-in. Asset removed from this config.
    # Aelis Farma pursuing higher doses independently.

    # SOTP scenarios -- single-franchise commercial w/ Brixadi competition overhang
    # FY26 guide $1,125-1,195M (DECLINING); use as anchor
    weights = {"mega_bear": 12, "bear": 25, "base": 38, "bull": 20, "psychedelic_bull": 5}
    crev = {"mega_bear": 1080, "bear": 1130, "base": 1180, "bull": 1300, "psychedelic_bull": 1500}
    # Multiples reflect: post-rerating to ~$37 mcap, Brixadi at 30% LAI share, declining
    # FY26 guide, plus offsetting label expansion + buyback yield. Market ~3x EV/sales.
    cmult = {"mega_bear": 1.8, "bear": 2.5, "base": 3.2, "bull": 4.2, "psychedelic_bull": 5.5}
    pmult = {"mega_bear": 2, "bear": 3, "base": 5, "bull": 8, "psychedelic_bull": 12}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}
    milestones = {"mega_bear": 0, "bear": 0, "base": 25, "bull": 100, "psychedelic_bull": 250}

    SCEN = ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]
    pos_grid = {
        "indv_2000": {"mega_bear": 10, "bear": 20, "base": 35, "bull": 50, "psychedelic_bull": 65},
    }
    apr_grid = {a: {"mega_bear": 55, "bear": 70, "base": 82, "bull": 90, "psychedelic_bull": 95} for a in pos_grid}
    pen_grid = {a: {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25} for a in pos_grid}
    ind_map = {"indv_2000": "oud_orexin"}

    scenarios = od()
    commercial_inert = [
        ("sublocade", "oud_lai"), ("suboxone", "oud_daily"), ("opvee", "opioid_overdose"),
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
        od(("date", "Feb 2025"), ("dateSort", "2025-02-24"), ("asset", "sublocade"),
           ("indication", "oud_lai"),
           ("title", "Sublocade label expansion: 1-hour rapid induction + alt injection sites (FDA approved)"),
           ("type", "label_expansion"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "FDA label 209819s031; Indivior PR Feb 24 2025"), ("_confidence", "high")),
        od(("date", "H2 2026"), ("dateSort", "2026-12-15"), ("asset", "indv_2000"),
           ("indication", "oud_orexin"),
           ("title", "INDV-2000 orexin-1 OUD Ph2 readout (3-mo dose-ranging post-buprenorphine withdrawal)"),
           ("type", "phase2_data"), ("binary", True),
           ("fail_pos", 10), ("fail_apr", 55), ("success_pos", 50), ("success_apr", 82),
           ("_source", "Indivior pipeline; first patient Jun 2024"), ("_confidence", "low")),
        od(("date", "Q4 2026"), ("dateSort", "2026-12-15"), ("asset", "sublocade"),
           ("indication", "oud_lai"),
           ("title", "Sublocade vs Brixadi US LAI share dynamics (Brixadi crossed 30% YE25)"),
           ("type", "milestone"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Camurus FY25 report; IQVIA tracking"), ("_confidence", "high")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


def main():
    write_config("APLS", build_APLS())
    write_config("ASND", build_ASND())
    write_config("INDV", build_INDV())

    manifest_path = CONFIGS / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for tk in ["APLS", "ASND", "INDV"]:
        if tk not in manifest:
            manifest.append(tk)
    manifest = sorted(set(manifest))
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"\n  manifest -> {len(manifest)} tickers")


if __name__ == "__main__":
    main()
