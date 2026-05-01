# -*- coding: utf-8 -*-
"""Build configs for big generics + biosimilar makers.

Writes 10 configs (VTRS, SDZ, SUN, CELLTRION, CIPLA, DRREDDY, HIK, AUROBINDO,
HANMI, LUPIN) using:
- Generic-bucket assets with mixTemplate (auto-expanded later)
- Named branded products with company_slice
- Pipeline assets where applicable
- SOTP scenarios calibrated for high-debt/levered generic businesses

Run:
  py scripts/ops/build_generics_makers.py
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
    """Each region: (patientsK, wtpPct, priceK)."""
    return od(
        ("us", od(("patientsK", us[0]), ("wtpPct", us[1]), ("priceK", us[2]))),
        ("eu", od(("patientsK", eu[0]), ("wtpPct", eu[1]), ("priceK", eu[2]))),
        ("row", od(("patientsK", row[0]), ("wtpPct", row[1]), ("priceK", row[2]))),
    )


def slice_(us, eu, row):
    """Each region: (reachPct, wtpPct, priceK)."""
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
    a["indications"] = []  # filled by expand_generic_mixes.py
    return a


def sotp_scenarios(weights, vals, assumptions_by_scenario):
    """vals: {scen: {pipelineDR, pipelineMult, commercialMult, commercialRevM, milestones, dil}}
    assumptions_by_scenario: {scen: {asset_id: {ind_id: {pos,apr,pen}}}}"""
    SCEN = ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]
    out = od()
    for sk in SCEN:
        out[sk] = od(
            ("wt", weights[sk]),
            ("val", vals[sk]),
            ("assumptions", assumptions_by_scenario.get(sk, {})),
        )
    return out


def commercial_asmp_block(asset_inds_pairs):
    """For commercial commercial-only assets in SOTP mode -- inert assumptions
    just to satisfy the audit pipeline check (we set pos=100 apr=100)."""
    out = od()
    for aid, inds in asset_inds_pairs:
        out[aid] = od()
        for iid in inds:
            out[aid][iid] = od(("pos", 100), ("apr", 100), ("pen", 1))
    return out


def commercial_scenarios(commercial_revM_by_scen, mult_by_scen, pipeMult_by_scen,
                         dr_pipeline_by_scen, weights, asset_inds_pairs,
                         pipeline_asmp_by_scen=None, milestones=None):
    """Helper for commercial-heavy SOTP companies."""
    SCEN = ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]
    vals = {}
    asmps = {}
    if milestones is None:
        milestones = {"mega_bear": 0, "bear": 25, "base": 75, "bull": 200, "psychedelic_bull": 500}
    for sk in SCEN:
        vals[sk] = od(
            ("pipelineDR", dr_pipeline_by_scen[sk]),
            ("pipelineMult", pipeMult_by_scen[sk]),
            ("commercialMult", mult_by_scen[sk]),
            ("commercialRevM", commercial_revM_by_scen[sk]),
            ("milestones", milestones[sk]),
            ("dil", 0),
        )
        asmps[sk] = commercial_asmp_block(asset_inds_pairs)
        # Add pipeline pen scaling per scenario
        if pipeline_asmp_by_scen and sk in pipeline_asmp_by_scen:
            for aid, inds in pipeline_asmp_by_scen[sk].items():
                asmps[sk][aid] = inds
    return sotp_scenarios(weights, vals, asmps)


def write_config(ticker, cfg):
    path = CONFIGS / f"{ticker}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"  wrote {path.relative_to(ROOT)}")


# =====================================================================
# VTRS - Viatris
# =====================================================================

def build_VTRS():
    co = od(
        ("ticker", "VTRS"),
        ("name", "Viatris Inc."),
        ("currentPrice", 14.94),
        ("sharesOut", 1171),
        ("cash", -11160),
        ("currency", "USD"),
        ("phase", "commercial"),
        ("subtitle", "Spinout of Mylan + Pfizer Upjohn (Nov 2020). FY2025 revenue $14.25B (-2% cc) across Developed Markets ~$8.5B / Greater China ~$2.3B / Emerging Markets ~$2.2B / JANZ ~$1.2B. Top legacy brands: Lipitor $1.55B, Norvasc $710M, Lyrica $487M, EpiPen $470M, Viagra $408M, Creon $366M, Yupelri $267M. Idorsia partnership Ph3 pipeline (selatogrel, cenerimod). Heavy net debt ~$11.2B post-merger."),
        ("yahooTicker", "VTRS"),
    )

    # Named brands with disclosed FY25 sales
    brands = [
        # (id, name, stage, modality, ind_id, ind_name, area, regions, slice, sources, salesM, cagrPct, peakYear)
        ("lipitor", "Lipitor (atorvastatin) - HMG-CoA reductase inhibitor (Pfizer Upjohn legacy)", "small_molecule.enzyme.hmg_coa_reductase",
         "ldl_cv_risk", "LDL/CV risk reduction (post-LOE 2011 generic)", "cardio_metabolic.lipids.ldl_cv_risk",
         (40000, 30, 0.5), (60000, 25, 0.3), (350000, 8, 0.1),
         (0.7, 50, 0.7), (0.4, 35, 0.4), (0.05, 12, 0.15),
         {"us.reachPct": "Lipitor branded post-LOE residual ~3-4% LDL Rx volume", "us.priceK": "Branded WAC ~$700/yr; rebated"},
         1549, -8, 2026),
        ("norvasc", "Norvasc (amlodipine) - CCB (Pfizer Upjohn legacy)", "small_molecule.ion_channel.ccb",
         "htn", "Hypertension (post-LOE residual brand)", "cardio_metabolic.hypertension.outpatient_generic",
         (80000, 12, 0.3), (100000, 10, 0.2), (500000, 5, 0.05),
         (0.4, 50, 0.4), (0.3, 30, 0.25), (0.04, 10, 0.08),
         {"us.reachPct": "Norvasc residual brand ~2-3% antihypertensive Rx", "us.priceK": "Branded ~$400/yr"},
         710, -10, 2026),
        ("lyrica", "Lyrica (pregabalin) - alpha-2-delta calcium channel modulator (Pfizer Upjohn)", "small_molecule.ion_channel.cav_a2d",
         "neuropathic_pain", "Neuropathic pain (post-LOE residual brand; Japan key)", "cns.pain.neuropathic",
         (5000, 60, 1), (8000, 50, 0.8), (40000, 15, 0.3),
         (1.2, 60, 1.5), (0.8, 40, 1.0), (0.15, 12, 0.4),
         {"row.reachPct": "Lyrica Japan ~$300M residual brand pre-LOE", "us.priceK": "Branded WAC ~$1500/yr"},
         487, -12, 2026),
        ("epipen", "EpiPen (epinephrine auto-injector) - emergency anaphylaxis treatment", "small_molecule.gpcr.adrenergic",
         "anaphylaxis", "Anaphylaxis emergency rescue (auto-injector)", "immunology.allergy.anaphylaxis",
         (3000, 60, 0.6), (3500, 35, 0.4), (15000, 8, 0.2),
         (8, 60, 0.6), (3, 40, 0.4), (0.3, 10, 0.2),
         {"us.reachPct": "EpiPen ~50% US epi auto-injector share (vs Auvi-Q, generics)", "us.priceK": "EpiPen 2-pk WAC ~$650"},
         470, -3, 2027),
        ("viagra", "Viagra (sildenafil) - PDE5 inhibitor (Pfizer Upjohn legacy)", "small_molecule.enzyme.pde5",
         "ed", "Erectile dysfunction (post-LOE residual brand)", "_established_products.viatris_legacy",
         (30000, 25, 0.3), (40000, 18, 0.2), (200000, 5, 0.05),
         (1, 35, 0.5), (0.5, 25, 0.3), (0.2, 8, 0.1),
         {"us.priceK": "Viagra branded post-LOE residual ~$500/yr",
          "row.reachPct": "Viagra residual brand $408M FY25, mostly emerging markets"},
         408, -10, 2026),
        ("creon", "Creon (pancrelipase) - porcine-derived pancreatic enzyme replacement", "biological_extract.porcine.pancreatic_enzyme",
         "epi", "Pancreatic exocrine insufficiency (chronic pancreatitis, CF, post-Whipple)", "rare_disease.gi.exocrine_pancreatic_insufficiency",
         (200, 70, 5), (300, 60, 3), (1500, 15, 1),
         (40, 70, 5), (15, 60, 3), (1, 15, 1),
         {"us.reachPct": "Creon ~70% US PERT share (vs Zenpep, Pancreaze)", "us.priceK": "Creon WAC ~$5K/yr"},
         366, 3, 2030),
        ("yupelri", "Yupelri (revefenacin) - long-acting nebulized LAMA bronchodilator (partnered Theravance)", "small_molecule.gpcr.lama",
         "copd_neb", "COPD nebulized LAMA (severe/uncooperative patients)", "respiratory.inflammatory.copd",
         (15000, 60, 1.5), (20000, 35, 0.8), (200000, 6, 0.3),
         (0.4, 60, 5), (0.05, 30, 3), (0.01, 5, 1),
         {"us.reachPct": "Yupelri only nebulized LAMA in US; ~3-5% COPD nebulizer Rx", "us.priceK": "Yupelri WAC ~$5K/yr"},
         267, 12, 2030),
    ]

    assets = []
    for (aid, aname, modality, iid, iname, area, us_r, eu_r, row_r,
         us_s, eu_s, row_s, sources, salesM, cagr, peak) in brands:
        assets.append(asset(aid, aname, "Commercial (Viatris legacy brand)",
                            modality, [innov_ind(iid, iname, area,
                                                 regions(us_r, eu_r, row_r),
                                                 slice_(us_s, eu_s, row_s),
                                                 sources, salesM=salesM,
                                                 cagrPct=cagr, peakYear=peak,
                                                 penPct=30)]))

    # Generic buckets (FY25 segment revenue minus the named brands above)
    # Total FY25 = $14.25B; named brands total $4.26B; remainder ~$10B in generics
    # Developed Markets ex-named brands: ~$8.5B - $4.26B = $4.24B (US + EU + JANZ)
    #   Split: US generics ~$1.5B + EU generics ~$2.2B + JANZ $0.55B
    # Greater China: $2.3B (use EM template)
    # Emerging Markets: $2.2B (use EM template)
    assets.append(gen_bucket("vtrs_us_generics",
                             "Viatris US generics franchise",
                             "Commercial (FY25 ~$1.5B US generic SKUs ex-brands)",
                             1500, "us_generics_developed_v1"))
    assets.append(gen_bucket("vtrs_eu_generics",
                             "Viatris Europe generics + branded generics",
                             "Commercial (FY25 ~$2.2B Europe oral + injectable generics)",
                             2200, "eu_generics_developed_v1"))
    assets.append(gen_bucket("vtrs_janz",
                             "Viatris JANZ (Japan + AU+NZ) franchise",
                             "Commercial (FY25 ~$0.55B Japan + Australia + NZ)",
                             550, "eu_generics_developed_v1"))
    assets.append(gen_bucket("vtrs_china",
                             "Viatris Greater China branded generics",
                             "Commercial (FY25 ~$2.3B Greater China; legacy Pfizer Upjohn brands)",
                             2300, "emerging_markets_generics_v1"))
    assets.append(gen_bucket("vtrs_em",
                             "Viatris Emerging Markets franchise",
                             "Commercial (FY25 ~$2.2B EM ex-China)",
                             2200, "emerging_markets_generics_v1"))

    # Pipeline (Idorsia partnership)
    assets.append(asset(
        "selatogrel", "Selatogrel - oral self-administered P2Y12 inhibitor for AMI (Idorsia)",
        "Phase 3 (SOS-AMI; SPA + Fast Track; readout 2027)",
        "small_molecule.gpcr.p2y12_antagonist",
        [innov_ind("ami_self", "Acute myocardial infarction patient self-administration",
                   "cardio_metabolic.cardiovascular.myocardial_infarction",
                   regions((1500, 80, 8), (2000, 70, 5), (8000, 30, 2)),
                   slice_((10, 50, 1.5), (5, 40, 1), (0.5, 15, 0.4)),
                   {"us.reachPct": "Selatogrel niche AMI self-admin pre-hospital; ~5-15% post-MI Rx",
                    "us.priceK": "Estimated WAC $1500/yr"},
                   peakYear=2032, cagrPct=0, penPct=12)]))
    assets.append(asset(
        "cenerimod", "Cenerimod - selective S1P1 modulator for SLE (Idorsia)",
        "Phase 3 (OPUS-1/OPUS-2 SLE; readout 2026/27)",
        "small_molecule.gpcr.s1p1_agonist",
        [innov_ind("sle", "Systemic lupus erythematosus moderate-severe",
                   "immunology.autoimmune.sle",
                   regions((350, 75, 25), (450, 60, 12), (2000, 20, 3)),
                   slice_((5, 50, 25), (3, 40, 15), (0.5, 15, 5)),
                   {"us.reachPct": "Cenerimod novel oral S1P1 mechanism in SLE; ~5-10% SLE Rx if approved",
                    "us.priceK": "Estimated WAC $25K/yr"},
                   peakYear=2032, cagrPct=0, penPct=10)]))

    # Scenarios
    weights = {"mega_bear": 15, "bear": 25, "base": 35, "bull": 20, "psychedelic_bull": 5}
    crev = {"mega_bear": 13000, "bear": 13800, "base": 14000, "bull": 15000, "psychedelic_bull": 16500}
    cmult = {"mega_bear": 1.0, "bear": 1.4, "base": 1.8, "bull": 2.4, "psychedelic_bull": 3.2}
    pmult = {"mega_bear": 2, "bear": 3, "base": 4, "bull": 6, "psychedelic_bull": 9}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [
        ("lipitor", ["ldl_cv_risk"]), ("norvasc", ["htn"]), ("lyrica", ["neuropathic_pain"]),
        ("epipen", ["anaphylaxis"]), ("viagra", ["ed"]), ("creon", ["epi"]),
        ("yupelri", ["copd_neb"]),
    ]

    pipeline_asmps = {
        "mega_bear": {
            "selatogrel": {"ami_self": od(("pos", 25), ("apr", 50), ("pen", 0.4))},
            "cenerimod": {"sle": od(("pos", 20), ("apr", 50), ("pen", 0.3))},
        },
        "bear": {
            "selatogrel": {"ami_self": od(("pos", 35), ("apr", 70), ("pen", 0.6))},
            "cenerimod": {"sle": od(("pos", 30), ("apr", 70), ("pen", 0.5))},
        },
        "base": {
            "selatogrel": {"ami_self": od(("pos", 50), ("apr", 80), ("pen", 0.85))},
            "cenerimod": {"sle": od(("pos", 45), ("apr", 80), ("pen", 0.75))},
        },
        "bull": {
            "selatogrel": {"ami_self": od(("pos", 65), ("apr", 90), ("pen", 1.0))},
            "cenerimod": {"sle": od(("pos", 60), ("apr", 90), ("pen", 0.95))},
        },
        "psychedelic_bull": {
            "selatogrel": {"ami_self": od(("pos", 75), ("apr", 95), ("pen", 1.15))},
            "cenerimod": {"sle": od(("pos", 70), ("apr", 95), ("pen", 1.1))},
        },
    }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "Jul 2026"), ("dateSort", "2026-07-30"), ("asset", "vtrs_us_generics"),
           ("indication", "vtrs_us_generics_outpatient_generic"),
           ("title", "Contraceptive patch PDUFA (Jul 30, 2026)"),
           ("type", "pdufa"), ("binary", True),
           ("fail_pos", 0), ("fail_apr", 0), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Viatris FY25 release"), ("_confidence", "high")),
        od(("date", "Oct 2026"), ("dateSort", "2026-10-17"), ("asset", "vtrs_us_generics"),
           ("indication", "vtrs_us_generics_outpatient_generic"),
           ("title", "MR-141 (phentolamine ophthalmic) PDUFA (Oct 17, 2026)"),
           ("type", "pdufa"), ("binary", True),
           ("fail_pos", 0), ("fail_apr", 0), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Viatris FY25 release"), ("_confidence", "high")),
        od(("date", "H2 2027"), ("dateSort", "2027-09-30"), ("asset", "selatogrel"),
           ("indication", "ami_self"), ("title", "Selatogrel SOS-AMI Ph3 readout"),
           ("type", "phase3_data"), ("binary", True),
           ("fail_pos", 10), ("fail_apr", 30), ("success_pos", 70), ("success_apr", 90),
           ("_source", "Idorsia/Viatris collab"), ("_confidence", "medium")),
        od(("date", "2026-2027"), ("dateSort", "2027-06-30"), ("asset", "cenerimod"),
           ("indication", "sle"), ("title", "Cenerimod OPUS-1/OPUS-2 SLE Ph3 readouts"),
           ("type", "phase3_data"), ("binary", True),
           ("fail_pos", 10), ("fail_apr", 30), ("success_pos", 70), ("success_apr", 90),
           ("_source", "Idorsia/Viatris collab"), ("_confidence", "medium")),
    ]

    return od(("company", co), ("assets", assets), ("scenarios", scenarios),
              ("catalysts", catalysts))


# =====================================================================
# SDZ - Sandoz
# =====================================================================

def build_SDZ():
    co = od(
        ("ticker", "SDZ"),
        ("name", "Sandoz Group AG"),
        ("currentPrice", 50),
        ("sharesOut", 430),
        ("cash", -2700),
        ("currency", "CHF"),
        ("phase", "commercial"),
        ("subtitle", "Novartis spin-off (Oct 2023). FY2025 revenue ~$10.7B: Generics ~$7.2B, Biosimilars ~$3.5B (+40% cc). Top biosimilars: Hyrimoz (adalimumab) ~$750M, Pyzchiva (ustekinumab) ~$450M, Wyost/Jubbonti (denosumab) ~$300M. ~25 biosimilars in development incl Eylea (aflibercept) launched 2025, Keytruda (pembrolizumab) post-2028. Reports in USD; trades CHF on SIX."),
        ("yahooTicker", "SDZ.SW"),
    )

    # Named biosimilars with disclosed FY25 sales -- treated as innovative-style
    # since each has a defined disease tag
    bios = [
        ("hyrimoz", "Hyrimoz / adalimumab biosimilar (high-conc + low-conc)", "antibody.monoclonal.anti_tnf",
         "ra_psoriasis", "RA + psoriasis + Crohn's + UC + AS (TNF-alpha)",
         "immunology.inflammatory_systemic.rheumatoid_arthritis",
         (1300, 70, 50), (2000, 60, 25), (10000, 8, 8),
         (3, 60, 30), (1.5, 50, 18), (0.15, 12, 6),
         {"us.priceK": "Hyrimoz biosim US ~70% discount vs Humira ~$30K/yr"},
         750, 8, 2029),
        ("pyzchiva", "Pyzchiva (ustekinumab biosimilar)", "antibody.monoclonal.anti_il23p40",
         "psoriasis", "Plaque psoriasis + psoriatic arthritis + Crohn's + UC",
         "dermatology.inflammatory_derm.psoriasis_systemic",
         (3000, 50, 30), (4000, 40, 18), (15000, 5, 6),
         (1.5, 40, 22), (0.8, 35, 14), (0.1, 8, 4),
         {"us.priceK": "Pyzchiva biosim US ~50% discount vs Stelara ~$60K/yr"},
         450, 25, 2030),
        ("jubbonti", "Wyost/Jubbonti (denosumab biosimilar)", "antibody.monoclonal.anti_rankl",
         "osteoporosis", "Postmenopausal osteoporosis + bone metastases",
         "musculoskeletal.bone_cartilage.osteoporosis",
         (10000, 35, 1.5), (15000, 30, 0.8), (50000, 5, 0.3),
         (0.4, 35, 1.2), (0.2, 30, 0.7), (0.02, 5, 0.25),
         {"us.priceK": "Jubbonti biosim US ~50% discount vs Prolia"},
         300, 20, 2030),
        ("tyruko", "Tyruko (natalizumab biosimilar)", "antibody.monoclonal.anti_a4_integrin",
         "ms", "Relapsing-remitting MS (anti-integrin)",
         "immunology.demyelinating.multiple_sclerosis",
         (900, 60, 50), (1500, 40, 30), (1500, 12, 10),
         (0.3, 50, 30), (0.2, 35, 22), (0.02, 10, 8),
         {"us.priceK": "Tyruko biosim US ~30% discount vs Tysabri"},
         75, 30, 2030),
        ("omnitrope", "Omnitrope (somatropin biosimilar) - mature franchise", "recombinant_protein.hormone.gh",
         "ghd", "Growth hormone deficiency (peds + adult)",
         "endocrine.pituitary.gh_deficiency",
         (300, 60, 25), (500, 50, 15), (2500, 12, 5),
         (1, 60, 20), (0.7, 50, 12), (0.1, 12, 4),
         {"us.priceK": "Omnitrope mature ~$20K/yr biosim"},
         300, 0, 2026),
    ]

    assets = []
    for (aid, aname, modality, iid, iname, area, us_r, eu_r, row_r,
         us_s, eu_s, row_s, sources, salesM, cagr, peak) in bios:
        assets.append(asset(aid, aname, "Commercial (Sandoz biosimilar)",
                            modality, [innov_ind(iid, iname, area,
                                                 regions(us_r, eu_r, row_r),
                                                 slice_(us_s, eu_s, row_s),
                                                 sources, salesM=salesM,
                                                 cagrPct=cagr, peakYear=peak,
                                                 penPct=40)]))

    # Mature biosim bucket (Erelzi/Zarxio/Ziextenzo/Binocrit) -- $800M aggregated
    assets.append(asset(
        "mature_biosims", "Sandoz mature biosimilar bucket (Erelzi etanercept + Zarxio filgrastim + Ziextenzo pegfilgrastim + Binocrit epoetin)",
        "Commercial (mature biosims; declining slowly)",
        "antibody.various.biosimilar_bucket",
        [innov_ind("supportive_oncology", "Mature biosim portfolio - oncology supportive + autoimmune",
                   "oncology.supportive_care.neutropenia",
                   regions((300, 70, 8), (450, 60, 5), (2500, 18, 2)),
                   slice_((10, 50, 5), (8, 50, 3), (1, 18, 1)),
                   {"us.priceK": "Bucket avg ~$3-5K/yr blended biosim WAC"},
                   salesM=800, cagrPct=-5, peakYear=2026, penPct=35)]))

    # Generic franchises - $7.2B generics, regional split est: Europe 60% / NA 25% / Intl 15%
    # Ex-biosim revenue: $10.7B total - $1.875B biosim named - $0.8B mature bucket = $8.0B
    # Better: biosims total $3.5B, generics total $7.2B, sum $10.7B. Named biosims sum $1.875B, mature $0.8B = $2.675B; remaining $0.825B in "other biosim line items" — fold into mature bucket (already $800M) so generics buckets sum to $7.2B
    assets.append(gen_bucket("sdz_eu_generics",
                             "Sandoz Europe generics franchise",
                             "Commercial (FY25 ~$4.3B EU oral + injectable generics)",
                             4300, "eu_generics_developed_v1"))
    assets.append(gen_bucket("sdz_us_generics",
                             "Sandoz North America generics franchise",
                             "Commercial (FY25 ~$1.8B US oral + sterile generics)",
                             1800, "us_generics_developed_v1"))
    assets.append(gen_bucket("sdz_intl_generics",
                             "Sandoz International generics franchise",
                             "Commercial (FY25 ~$1.1B International ex-EU/NA)",
                             1100, "emerging_markets_generics_v1"))

    # Pipeline biosim: aflibercept (Eylea biosim launched 2025) + pembrolizumab (post-2028)
    assets.append(asset(
        "afli_biosim", "Aflibercept (Eylea biosimilar) - anti-VEGF intravitreal",
        "Commercial (launched 2025; ramping)",
        "antibody.fusion.vegf_trap",
        [innov_ind("nvamd_dme", "nvAMD + DME + DR + RVO (anti-VEGF retina)",
                   "ophthalmology.retina.nvamd",
                   regions((2500, 75, 12), (3500, 65, 7), (15000, 12, 3)),
                   slice_((1.5, 50, 8), (1, 50, 5), (0.1, 12, 2)),
                   {"us.priceK": "Aflibercept biosim ~30% discount vs Eylea ~$8K/yr"},
                   peakYear=2030, cagrPct=20, penPct=25)]))
    assets.append(asset(
        "pembro_biosim", "Pembrolizumab (Keytruda biosimilar) - anti-PD-1",
        "Phase 3 (post-2028 LOE in major markets; filing 2027/28)",
        "antibody.monoclonal.anti_pd1",
        [innov_ind("io_oncology", "IO-eligible solid tumors (multi-tumor PD-1/PD-L1)",
                   "oncology.multi_tumor_io.pd1_pdl1_eligible",
                   regions((500, 80, 150), (700, 70, 100), (3000, 12, 30)),
                   slice_((3, 50, 100), (2, 50, 70), (0.2, 12, 25)),
                   {"us.priceK": "Pembro biosim ~30-50% discount vs Keytruda ~$175K/yr",
                    "us.reachPct": "Post-2028 EU LOE first; US LOE 2030; modest share v originator"},
                   peakYear=2032, cagrPct=0, penPct=15)]))

    weights = {"mega_bear": 12, "bear": 23, "base": 38, "bull": 22, "psychedelic_bull": 5}
    crev = {"mega_bear": 10000, "bear": 10500, "base": 11000, "bull": 12000, "psychedelic_bull": 14000}
    cmult = {"mega_bear": 1.5, "bear": 2.0, "base": 2.6, "bull": 3.5, "psychedelic_bull": 4.5}
    pmult = {"mega_bear": 2, "bear": 3, "base": 4, "bull": 5, "psychedelic_bull": 7}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [
        ("hyrimoz", ["ra_psoriasis"]), ("pyzchiva", ["psoriasis"]),
        ("jubbonti", ["osteoporosis"]), ("tyruko", ["ms"]), ("omnitrope", ["ghd"]),
        ("mature_biosims", ["supportive_oncology"]), ("afli_biosim", ["nvamd_dme"]),
    ]

    pipeline_asmps = {
        "mega_bear": {"pembro_biosim": {"io_oncology": od(("pos", 30), ("apr", 60), ("pen", 0.3))}},
        "bear":      {"pembro_biosim": {"io_oncology": od(("pos", 45), ("apr", 75), ("pen", 0.5))}},
        "base":      {"pembro_biosim": {"io_oncology": od(("pos", 60), ("apr", 85), ("pen", 0.75))}},
        "bull":      {"pembro_biosim": {"io_oncology": od(("pos", 75), ("apr", 92), ("pen", 1.0))}},
        "psychedelic_bull": {"pembro_biosim": {"io_oncology": od(("pos", 85), ("apr", 95), ("pen", 1.2))}},
    }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "Q4 2026"), ("dateSort", "2026-12-15"), ("asset", "sdz_us_generics"),
           ("indication", "sdz_us_generics_outpatient_generic"),
           ("title", "Aflibercept biosimilar US ramp + EU coverage"),
           ("type", "launch"), ("binary", False),
           ("fail_pos", 0), ("fail_apr", 0), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Sandoz FY25 release"), ("_confidence", "high")),
        od(("date", "2027"), ("dateSort", "2027-06-30"), ("asset", "pembro_biosim"),
           ("indication", "io_oncology"),
           ("title", "Pembrolizumab biosimilar BLA filing (post-2028 EU LOE)"),
           ("type", "bla_submission"), ("binary", False),
           ("fail_pos", 30), ("fail_apr", 60), ("success_pos", 70), ("success_apr", 90),
           ("_source", "Sandoz pipeline disclosure"), ("_confidence", "medium")),
    ]

    return od(("company", co), ("assets", assets), ("scenarios", scenarios),
              ("catalysts", catalysts))


# =====================================================================
# SUN - Sun Pharma
# =====================================================================

def build_SUN():
    co = od(
        ("ticker", "SUN"),
        ("name", "Sun Pharmaceutical Industries Ltd."),
        ("currentPrice", 1700),
        ("sharesOut", 2399),
        ("cash", 1700),
        ("currency", "INR"),
        ("phase", "commercial"),
        ("subtitle", "Largest Indian pharma. FY25 (Mar25) revenue INR 525B / ~$6.3B. Specialty $1.04B led by Ilumya (tildrakizumab) ~$610M growing. Global Generics ex-specialty ~$5.3B: India $1.96B (#1 IPM), US $2.0B, Emerging Markets $1.07B, Western Europe + RoW $0.88B. Net cash ~$1.7B. Deuruxolitinib (Leqselvi alopecia areata) FDA-approved Jul 2024 but US launch delayed by Concert/Incyte injunction."),
        ("yahooTicker", "SUNPHARMA.NS"),
    )

    # Named specialty branded with disclosed FY25 sales (USD)
    spec = [
        ("ilumya", "Ilumya (tildrakizumab) - anti-IL-23p19 mAb (Sun-developed via SCH-2017 ex-Merck)", "antibody.monoclonal.anti_il23p19",
         "psoriasis", "Plaque psoriasis (PsA Ph3 INSPIRE filed)", "dermatology.inflammatory_derm.psoriasis_systemic",
         (3000, 50, 30), (4000, 40, 18), (15000, 5, 6),
         (2.5, 60, 80), (0.8, 35, 35), (0.05, 8, 12),
         {"us.reachPct": "Ilumya ~10% IL-23 class share (vs Skyrizi, Tremfya, Stelara)",
          "us.priceK": "Ilumya WAC ~$80K/yr"},
         610, 18, 2031),
        ("cequa", "Cequa (cyclosporine 0.09% nanomicellar) - dry eye", "small_molecule.calcineurin_inhibitor.cyclosporine",
         "dry_eye", "Chronic dry eye disease (Cequa nanomicellar formulation)", "ophthalmology.anterior_neuro.dry_eye",
         (40000, 25, 0.5), (50000, 20, 0.3), (200000, 5, 0.1),
         (0.6, 30, 1.2), (0.2, 20, 0.6), (0.02, 5, 0.2),
         {"us.priceK": "Cequa WAC ~$1.2K/yr"},
         170, 8, 2030),
        ("winlevi", "Winlevi (clascoterone 1%) - first topical androgen-receptor antagonist for acne (acquired from Cassiopea)", "small_molecule.nuclear_receptor.ar_antagonist",
         "acne", "Moderate-to-severe acne (topical anti-androgen)", "dermatology.inflammatory_derm.acne",
         (40000, 25, 0.4), (50000, 15, 0.2), (250000, 5, 0.1),
         (0.4, 30, 0.6), (0.1, 15, 0.3), (0.01, 5, 0.1),
         {"us.priceK": "Winlevi WAC ~$600/tube/mo"},
         110, 25, 2030),
        ("odomzo", "Odomzo (sonidegib) - SMO inhibitor (Hedgehog pathway)", "small_molecule.gpcr.smoothened_antagonist",
         "bcc", "Locally advanced basal cell carcinoma", "oncology.skin.bcc",
         (50, 80, 50), (60, 70, 30), (200, 18, 8),
         (10, 60, 40), (3, 50, 25), (0.3, 18, 8),
         {"us.priceK": "Odomzo WAC ~$10K/mo"},
         70, 5, 2030),
        ("absorica", "Absorica (isotretinoin) - severe acne", "small_molecule.retinoid.isotretinoin",
         "severe_acne", "Severe recalcitrant nodular acne", "dermatology.inflammatory_derm.acne",
         (300, 70, 1.5), (500, 60, 0.8), (3000, 12, 0.3),
         (3, 50, 1.5), (0.8, 30, 0.8), (0.05, 10, 0.3),
         {"us.priceK": "Absorica branded ~$1.5K/4mo"},
         50, -3, 2026),
        ("levulan", "Levulan Kerastick + BLU-U (5-ALA photodynamic therapy) - actinic keratosis", "small_molecule.photosensitizer.ala",
         "ak", "Actinic keratosis (face + scalp)", "dermatology.skin_lesions.actinic_keratosis",
         (5000, 50, 0.5), (8000, 40, 0.3), (30000, 10, 0.1),
         (0.4, 40, 1.0), (0.1, 25, 0.5), (0.01, 8, 0.2),
         {"us.priceK": "Levulan PDT session ~$1K"},
         60, 5, 2030),
    ]

    assets = []
    for (aid, aname, modality, iid, iname, area, us_r, eu_r, row_r,
         us_s, eu_s, row_s, sources, salesM, cagr, peak) in spec:
        assets.append(asset(aid, aname, "Commercial (Sun Specialty)",
                            modality, [innov_ind(iid, iname, area,
                                                 regions(us_r, eu_r, row_r),
                                                 slice_(us_s, eu_s, row_s),
                                                 sources, salesM=salesM,
                                                 cagrPct=cagr, peakYear=peak,
                                                 penPct=35)]))

    # Generic franchise buckets (USD; converted from INR)
    # FY25 ex-specialty: $6.3B total - $1.07B specialty named = $5.23B generics
    # India ~$1.96B, US ex-specialty ~$0.95B, EM ~$1.07B, EU+RoW ~$0.88B, API ~$0.32B
    # API treated as part of EU/RoW bucket
    assets.append(gen_bucket("sun_india_formulations",
                             "Sun India formulations franchise (#1 IPM, INR 163B / $1.96B)",
                             "Commercial (FY25 India branded Rx + generics)",
                             1960, "emerging_markets_generics_v1"))
    assets.append(gen_bucket("sun_us_generics",
                             "Sun US generics franchise (ex-specialty)",
                             "Commercial (FY25 ~$0.95B US complex generics)",
                             950, "us_generics_developed_v1"))
    assets.append(gen_bucket("sun_em_generics",
                             "Sun Emerging Markets generics franchise",
                             "Commercial (FY25 ~$1.07B EM ex-India)",
                             1070, "emerging_markets_generics_v1"))
    assets.append(gen_bucket("sun_eu_row",
                             "Sun Western Europe + RoW + API franchise",
                             "Commercial (FY25 ~$1.2B EU + RoW + API)",
                             1200, "eu_generics_developed_v1"))

    # Pipeline
    assets.append(asset(
        "leqselvi", "Leqselvi (deuruxolitinib) - oral selective TYK2/JAK1 inhibitor (acquired via Concert 2023)",
        "FDA-approved Jul 2024; US launch delayed by Concert/Incyte patent injunction (resolution 2026)",
        "small_molecule.kinase.jak1_tyk2",
        [innov_ind("alopecia", "Severe alopecia areata (adults)",
                   "dermatology.rare_skin.alopecia_areata",
                   regions((700, 30, 10), (1000, 25, 6), (5000, 5, 2)),
                   slice_((4, 35, 50), (1.5, 25, 30), (0.1, 8, 10)),
                   {"us.reachPct": "Leqselvi vs Olumiant + Litfulo class (severe AA)",
                    "us.priceK": "Leqselvi WAC ~$50K/yr"},
                   peakYear=2032, cagrPct=15, penPct=18)]))
    assets.append(asset(
        "nidlegy", "Nidlegy (daromun) - intratumoral IL-2 + TNF-alpha (Philogen partnership)",
        "Phase 3 PIVOTAL (melanoma) positive 2024; EU filing 2025/26",
        "recombinant_protein.cytokine.tumor_targeted",
        [innov_ind("melanoma_localcure", "Locally advanced fully-resectable stage IIIb-c melanoma (neoadjuvant intratumoral)",
                   "oncology.skin.melanoma",
                   regions((25, 80, 80), (35, 70, 50), (150, 20, 15)),
                   slice_((20, 50, 80), (10, 50, 50), (1, 15, 15)),
                   {"us.priceK": "Estimated WAC $80K/course; US launch 2027",
                    "us.reachPct": "Niche localized melanoma neoadjuvant ~20% of stage III"},
                   peakYear=2032, cagrPct=0, penPct=18)]))
    assets.append(asset(
        "scd_044", "SCD-044 - oral S1P1 modulator",
        "Phase 2 atopic dermatitis + psoriasis",
        "small_molecule.gpcr.s1p1_agonist",
        [innov_ind("ad_topical_fail", "Moderate-severe atopic dermatitis (post-topical)",
                   "dermatology.inflammatory_derm.atopic_dermatitis_systemic",
                   regions((6000, 35, 8), (10000, 25, 5), (40000, 5, 1.5)),
                   slice_((0.6, 35, 18), (0.2, 25, 12), (0.02, 6, 4)),
                   {"us.priceK": "Estimated WAC $18K/yr if approved"},
                   peakYear=2033, cagrPct=0, penPct=12)]))

    weights = {"mega_bear": 10, "bear": 22, "base": 38, "bull": 25, "psychedelic_bull": 5}
    # Multiples for India-listed pharma with strong franchise + INR pricing -- higher
    # multiples vs US generic peers given net cash + India IPM stickiness
    crev = {"mega_bear": 6000, "bear": 6300, "base": 6700, "bull": 7400, "psychedelic_bull": 8500}
    cmult = {"mega_bear": 3.5, "bear": 4.5, "base": 5.5, "bull": 7, "psychedelic_bull": 9}
    pmult = {"mega_bear": 3, "bear": 4, "base": 5, "bull": 7, "psychedelic_bull": 10}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [
        ("ilumya", ["psoriasis"]), ("cequa", ["dry_eye"]), ("winlevi", ["acne"]),
        ("odomzo", ["bcc"]), ("absorica", ["severe_acne"]), ("levulan", ["ak"]),
    ]

    pipeline_asmps = {
        "mega_bear": {
            "leqselvi": {"alopecia": od(("pos", 60), ("apr", 60), ("pen", 0.4))},
            "nidlegy": {"melanoma_localcure": od(("pos", 50), ("apr", 70), ("pen", 0.4))},
            "scd_044": {"ad_topical_fail": od(("pos", 15), ("apr", 50), ("pen", 0.3))},
        },
        "bear": {
            "leqselvi": {"alopecia": od(("pos", 80), ("apr", 80), ("pen", 0.6))},
            "nidlegy": {"melanoma_localcure": od(("pos", 65), ("apr", 80), ("pen", 0.6))},
            "scd_044": {"ad_topical_fail": od(("pos", 25), ("apr", 65), ("pen", 0.5))},
        },
        "base": {
            "leqselvi": {"alopecia": od(("pos", 95), ("apr", 90), ("pen", 0.85))},
            "nidlegy": {"melanoma_localcure": od(("pos", 80), ("apr", 88), ("pen", 0.8))},
            "scd_044": {"ad_topical_fail": od(("pos", 40), ("apr", 80), ("pen", 0.75))},
        },
        "bull": {
            "leqselvi": {"alopecia": od(("pos", 99), ("apr", 95), ("pen", 1.05))},
            "nidlegy": {"melanoma_localcure": od(("pos", 90), ("apr", 92), ("pen", 1.0))},
            "scd_044": {"ad_topical_fail": od(("pos", 55), ("apr", 88), ("pen", 1.0))},
        },
        "psychedelic_bull": {
            "leqselvi": {"alopecia": od(("pos", 100), ("apr", 98), ("pen", 1.2))},
            "nidlegy": {"melanoma_localcure": od(("pos", 95), ("apr", 95), ("pen", 1.15))},
            "scd_044": {"ad_topical_fail": od(("pos", 70), ("apr", 92), ("pen", 1.2))},
        },
    }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "2026"), ("dateSort", "2026-06-30"), ("asset", "leqselvi"),
           ("indication", "alopecia"), ("title", "Leqselvi US launch resolution (Concert/Incyte litigation)"),
           ("type", "launch"), ("binary", True),
           ("fail_pos", 30), ("fail_apr", 60), ("success_pos", 95), ("success_apr", 95),
           ("_source", "Concert/Incyte filings"), ("_confidence", "medium")),
        od(("date", "2026"), ("dateSort", "2026-09-30"), ("asset", "ilumya"),
           ("indication", "psoriasis"), ("title", "Ilumya psoriatic arthritis sBLA filing/approval (Ph3 INSPIRE)"),
           ("type", "bla_submission"), ("binary", True),
           ("fail_pos", 70), ("fail_apr", 80), ("success_pos", 98), ("success_apr", 95),
           ("_source", "Sun FY25 disclosure"), ("_confidence", "high")),
        od(("date", "2026"), ("dateSort", "2026-12-15"), ("asset", "nidlegy"),
           ("indication", "melanoma_localcure"), ("title", "Nidlegy EMA decision (locally advanced melanoma)"),
           ("type", "ema_approval"), ("binary", True),
           ("fail_pos", 60), ("fail_apr", 70), ("success_pos", 90), ("success_apr", 95),
           ("_source", "Philogen/Sun"), ("_confidence", "high")),
    ]

    return od(("company", co), ("assets", assets), ("scenarios", scenarios),
              ("catalysts", catalysts))


# =====================================================================
# CELLTRION
# =====================================================================

def build_CELLTRION():
    co = od(
        ("ticker", "CELLTRION"),
        ("name", "Celltrion Inc."),
        ("currentPrice", 175000),
        ("sharesOut", 217),
        ("cash", 1000),
        ("currency", "KRW"),
        ("phase", "commercial"),
        ("subtitle", "Korean biosimilars pure-play. FY25 revenue ~$3.2B (KRW 4.3T) +20% YoY post-merger with Celltrion Healthcare. Flagship: Remsima/Inflectra/Zymfentra (infliximab IV+SC) ~$1.25B; Yuflyma (adalimumab high-conc) ~$340M; Vegzelma (bevacizumab) ~$235M; Truxima (rituximab) ~$200M; Herzuma (trastuzumab) ~$150M; Steqeyma (ustekinumab) ~$160M (US launch Mar 2025); Eydenzelt (aflibercept) early. Vision 2030: 22 biosimilars by 2030."),
        ("yahooTicker", "068270.KS"),
    )

    bios = [
        ("remsima_zymfentra", "Remsima IV + Remsima SC / Zymfentra (infliximab biosim incl. subQ)",
         "antibody.monoclonal.anti_tnf",
         "ibd_ra", "Crohn's + UC + RA + AS + psoriasis (TNF-alpha)",
         "immunology.inflammatory_gi.crohns",
         (1500, 50, 35), (2000, 45, 22), (8000, 8, 8),
         (3, 60, 25), (3, 60, 18), (0.3, 12, 6),
         {"us.priceK": "Zymfentra US WAC ~$25K/yr; Remsima SC EU ~$18K/yr",
          "us.reachPct": "Zymfentra subQ unique formulation; ~3% IBD/RA TNF Rx"},
         1250, 12, 2030),
        ("yuflyma", "Yuflyma (adalimumab high-concentration biosimilar)",
         "antibody.monoclonal.anti_tnf",
         "ra_psoriasis", "RA + psoriasis + Crohn's + UC + AS",
         "immunology.inflammatory_systemic.rheumatoid_arthritis",
         (1300, 70, 50), (2000, 60, 25), (10000, 8, 8),
         (1.5, 60, 28), (0.7, 50, 18), (0.1, 12, 6),
         {"us.priceK": "Yuflyma US WAC ~$28K/yr biosim discount vs Humira"},
         340, 18, 2030),
        ("vegzelma", "Vegzelma (bevacizumab biosimilar) - anti-VEGF",
         "antibody.monoclonal.anti_vegf",
         "crc_nsclc_gbm", "Metastatic CRC + NSCLC + GBM + ovarian (anti-VEGF)",
         "oncology.gi.colorectal",
         (150, 80, 30), (250, 70, 20), (1500, 15, 6),
         (8, 50, 18), (5, 50, 12), (0.5, 15, 5),
         {"us.priceK": "Vegzelma US WAC ~$18K/course biosim vs Avastin"},
         235, 18, 2030),
        ("truxima", "Truxima (rituximab biosimilar) - anti-CD20",
         "antibody.monoclonal.anti_cd20",
         "nhl_cll_ra", "NHL (DLBCL+FL) + CLL + RA (anti-CD20)",
         "oncology.hematology.nhl.dlbcl",
         (40, 80, 25), (60, 70, 18), (350, 18, 6),
         (5, 60, 18), (4, 60, 12), (0.4, 18, 5),
         {"us.priceK": "Truxima US WAC ~$18K/course biosim"},
         200, -5, 2026),
        ("herzuma", "Herzuma (trastuzumab biosimilar) - anti-HER2",
         "antibody.monoclonal.anti_her2",
         "her2_breast", "HER2+ breast + gastric (anti-HER2)",
         "oncology.breast.her2_pos",
         (60, 80, 100), (90, 70, 70), (450, 18, 25),
         (3, 60, 70), (2, 60, 50), (0.2, 18, 18),
         {"us.priceK": "Herzuma US WAC ~$70K/course biosim"},
         150, -2, 2026),
        ("steqeyma", "Steqeyma (ustekinumab biosimilar)",
         "antibody.monoclonal.anti_il23p40",
         "psoriasis_ibd", "Plaque psoriasis + PsA + Crohn's + UC",
         "dermatology.inflammatory_derm.psoriasis_systemic",
         (3000, 50, 30), (4000, 40, 18), (15000, 5, 6),
         (0.5, 40, 22), (0.3, 35, 14), (0.05, 8, 4),
         {"us.priceK": "Steqeyma US WAC biosim ~50% discount vs Stelara"},
         160, 35, 2031),
        ("omlyclo", "Omlyclo (omalizumab biosimilar) - anti-IgE",
         "antibody.monoclonal.anti_ige",
         "asthma_csu", "Severe allergic asthma + chronic spontaneous urticaria",
         "respiratory.inflammatory.asthma_severe",
         (1500, 35, 12), (2500, 25, 8), (12000, 3, 3),
         (0.3, 35, 8), (0.2, 25, 5), (0.02, 5, 2),
         {"us.priceK": "Omlyclo US WAC biosim ~50% discount vs Xolair"},
         30, 50, 2031),
        ("eydenzelt", "Eydenzelt (aflibercept biosimilar) - anti-VEGF retinal",
         "antibody.fusion.vegf_trap",
         "nvamd_dme", "nvAMD + DME + DR + RVO",
         "ophthalmology.retina.nvamd",
         (2500, 75, 12), (3500, 65, 7), (15000, 12, 3),
         (0.5, 50, 7), (0.3, 50, 4), (0.05, 12, 1.5),
         {"us.priceK": "Eydenzelt biosim ~30% discount vs Eylea"},
         60, 60, 2031),
    ]

    assets = []
    for (aid, aname, modality, iid, iname, area, us_r, eu_r, row_r,
         us_s, eu_s, row_s, sources, salesM, cagr, peak) in bios:
        assets.append(asset(aid, aname, "Commercial (Celltrion biosimilar)",
                            modality, [innov_ind(iid, iname, area,
                                                 regions(us_r, eu_r, row_r),
                                                 slice_(us_s, eu_s, row_s),
                                                 sources, salesM=salesM,
                                                 cagrPct=cagr, peakYear=peak,
                                                 penPct=40)]))

    # Pipeline biosimilars
    pipeline_def = [
        ("ct_p47", "CT-P47 (tocilizumab biosimilar) - anti-IL-6R",
         "Filed/approved 2025; US/EU launch ramp 2026",
         "antibody.monoclonal.anti_il6r",
         "ra_giant_cell", "RA + giant cell arteritis + sJIA",
         "immunology.inflammatory_systemic.rheumatoid_arthritis",
         (1300, 30, 30), (2000, 25, 18), (10000, 4, 5),
         (0.3, 35, 18), (0.2, 30, 12), (0.02, 6, 4),
         "Filed", 2030, 25),
        ("ct_p51", "CT-P51 (denosumab biosimilar) - anti-RANKL",
         "Phase 3; US/EU approvals 2026",
         "antibody.monoclonal.anti_rankl",
         "osteoporosis_bone_mets", "Osteoporosis + bone metastases",
         "musculoskeletal.bone_cartilage.osteoporosis",
         (10000, 35, 1.5), (15000, 30, 0.8), (50000, 5, 0.3),
         (0.2, 35, 1.0), (0.15, 30, 0.6), (0.02, 5, 0.2),
         "Phase 3", 2031, 30),
        ("ct_p53", "CT-P53 (ocrelizumab biosimilar) - anti-CD20 for MS",
         "Phase 3 readout 2026/27",
         "antibody.monoclonal.anti_cd20",
         "ms", "Relapsing-remitting + primary-progressive MS",
         "immunology.demyelinating.multiple_sclerosis",
         (900, 60, 60), (1500, 40, 35), (1500, 12, 10),
         (0.3, 50, 35), (0.15, 40, 22), (0.02, 10, 6),
         "Phase 3", 2032, 0),
    ]

    pl_assets = []
    for (aid, aname, stage_, modality, iid, iname, area, us_r, eu_r, row_r,
         us_s, eu_s, row_s, _sx, peak, cagr) in pipeline_def:
        pl_assets.append(asset(aid, aname, stage_, modality,
                               [innov_ind(iid, iname, area,
                                          regions(us_r, eu_r, row_r),
                                          slice_(us_s, eu_s, row_s),
                                          {"us.priceK": "Biosimilar discount ~30-50% vs originator"},
                                          peakYear=peak, cagrPct=cagr,
                                          penPct=15)]))
    assets.extend(pl_assets)

    weights = {"mega_bear": 10, "bear": 22, "base": 38, "bull": 25, "psychedelic_bull": 5}
    # Korean biotech with high growth biosimilar story; multiples higher than US generics
    crev = {"mega_bear": 3000, "bear": 3200, "base": 3500, "bull": 4200, "psychedelic_bull": 5500}
    cmult = {"mega_bear": 3, "bear": 4.5, "base": 6, "bull": 8, "psychedelic_bull": 11}
    pmult = {"mega_bear": 3, "bear": 4, "base": 5.5, "bull": 8, "psychedelic_bull": 12}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [
        ("remsima_zymfentra", ["ibd_ra"]), ("yuflyma", ["ra_psoriasis"]),
        ("vegzelma", ["crc_nsclc_gbm"]), ("truxima", ["nhl_cll_ra"]),
        ("herzuma", ["her2_breast"]), ("steqeyma", ["psoriasis_ibd"]),
        ("omlyclo", ["asthma_csu"]), ("eydenzelt", ["nvamd_dme"]),
    ]

    pipeline_asmps = {}
    pipe_pos = {"mega_bear": 50, "bear": 70, "base": 88, "bull": 95, "psychedelic_bull": 99}
    pipe_apr = {"mega_bear": 70, "bear": 82, "base": 92, "bull": 96, "psychedelic_bull": 99}
    pipe_pen = {"mega_bear": 0.4, "bear": 0.6, "base": 0.85, "bull": 1.05, "psychedelic_bull": 1.2}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "ct_p47": {"ra_giant_cell": od(("pos", pipe_pos[sk]), ("apr", pipe_apr[sk]), ("pen", pipe_pen[sk]))},
            "ct_p51": {"osteoporosis_bone_mets": od(("pos", pipe_pos[sk]), ("apr", pipe_apr[sk]), ("pen", pipe_pen[sk]))},
            "ct_p53": {"ms": od(("pos", pipe_pos[sk]), ("apr", pipe_apr[sk]), ("pen", pipe_pen[sk]))},
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "2026"), ("dateSort", "2026-09-30"), ("asset", "ct_p51"),
           ("indication", "osteoporosis_bone_mets"),
           ("title", "Denosumab biosimilar (CT-P51) US/EU approvals"),
           ("type", "bla_submission"), ("binary", True),
           ("fail_pos", 60), ("fail_apr", 70), ("success_pos", 95), ("success_apr", 95),
           ("_source", "Celltrion Vision 2030"), ("_confidence", "high")),
        od(("date", "2026-2027"), ("dateSort", "2027-06-30"), ("asset", "ct_p53"),
           ("indication", "ms"), ("title", "Ocrelizumab biosimilar (CT-P53) Phase 3 readout"),
           ("type", "phase3_data"), ("binary", True),
           ("fail_pos", 50), ("fail_apr", 80), ("success_pos", 90), ("success_apr", 95),
           ("_source", "Celltrion pipeline"), ("_confidence", "medium")),
        od(("date", "Q4 2026"), ("dateSort", "2026-12-15"), ("asset", "remsima_zymfentra"),
           ("indication", "ibd_ra"), ("title", "Zymfentra US formulary expansion + 2026 inflection"),
           ("type", "launch"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Celltrion FY25 IR"), ("_confidence", "high")),
    ]

    return od(("company", co), ("assets", assets), ("scenarios", scenarios),
              ("catalysts", catalysts))


# =====================================================================
# CIPLA
# =====================================================================

def build_CIPLA():
    co = od(
        ("ticker", "CIPLA"),
        ("name", "Cipla Ltd."),
        ("currentPrice", 1500),
        ("sharesOut", 808),
        ("cash", 840),
        ("currency", "INR"),
        ("phase", "commercial"),
        ("subtitle", "Indian respiratory + complex generics specialist. FY25 (Mar25) revenue INR 277B / ~$3.3B. One-India ~44% (~$1.45B), North America ~28% (~$0.93B record gLanreotide), South Africa ~10%, Emerging Markets ~9%, Europe + API ~9%. Net cash $840M. Key US: gLanreotide depot (Mar 2024 launch). Pipeline: gAdvair, gAbraxane, gRevlimid (2026 ladder), peptide depots."),
        ("yahooTicker", "CIPLA.NS"),
    )

    # Cipla heavily generic-bucket; minimal named brand breakouts (gLanreotide as
    # specialty US complex generic deserves its own asset)
    assets = []
    assets.append(asset(
        "g_lanreotide", "gLanreotide Depot (lanreotide complex generic) - somatostatin analog peptide depot",
        "Commercial (US launch Mar 2024; flagship complex generic)",
        "peptide.somatostatin.lanreotide",
        [innov_ind("acromegaly_nets", "Acromegaly + neuroendocrine tumors (somatostatin analog)",
                   "oncology.neuroendocrine.gi_pancreatic_net",
                   regions((25, 90, 60), (35, 85, 40), (150, 25, 12)),
                   slice_((20, 70, 25), (5, 50, 18), (0.5, 18, 6)),
                   {"us.reachPct": "gLanreotide ~30% US lanreotide volume share post-launch",
                    "us.priceK": "gLanreotide WAC ~$25K/yr (~50% off branded Somatuline)"},
                   salesM=200, salesYear=2025, peakYear=2030, cagrPct=20, penPct=30)]))

    # Generic franchise buckets
    assets.append(gen_bucket("cipla_one_india",
                             "Cipla One-India franchise (branded Rx + trade generics + consumer)",
                             "Commercial (FY25 INR 122B / $1.45B India)",
                             1450, "emerging_markets_generics_v1",
                             {"respiratory.inflammatory.asthma_severe": 0.10,
                              "respiratory.inflammatory.copd": 0.10}))
    assets.append(gen_bucket("cipla_north_america",
                             "Cipla North America franchise (ex-gLanreotide)",
                             "Commercial (FY25 ~$730M US complex generics + injectables)",
                             730, "us_generics_developed_v1",
                             {"respiratory.inflammatory.asthma_severe": 0.10}))
    assets.append(gen_bucket("cipla_south_africa",
                             "Cipla South Africa franchise (private + tender)",
                             "Commercial (FY25 ~$330M)",
                             330, "emerging_markets_generics_v1"))
    assets.append(gen_bucket("cipla_em",
                             "Cipla Emerging Markets ex-SA franchise (HIV ARV + LATAM + MENA + APAC)",
                             "Commercial (FY25 ~$300M)",
                             300, "emerging_markets_generics_v1"))
    assets.append(gen_bucket("cipla_eu_api",
                             "Cipla Europe + API franchise",
                             "Commercial (FY25 ~$220M EU + API)",
                             220, "eu_generics_developed_v1"))

    # Pipeline
    assets.append(asset(
        "g_advair", "gAdvair Diskus (fluticasone-salmeterol DPI complex generic)",
        "Phase 3 / FDA review (CRL resolution expected CY2026)",
        "small_molecule.gpcr.laba_ics_combo",
        [innov_ind("asthma_copd", "Asthma + COPD (DPI inhaler complex generic)",
                   "respiratory.inflammatory.asthma_severe",
                   regions((20000, 35, 4), (35000, 25, 2.5), (150000, 5, 0.6)),
                   slice_((1.5, 35, 2), (0.5, 25, 1.2), (0.05, 5, 0.3)),
                   {"us.priceK": "gAdvair ~50% discount vs Advair Diskus ~$2K/yr",
                    "us.reachPct": "gAdvair ~10-15% Advair-class share post-launch (vs Wixela first-mover)"},
                   peakYear=2031, cagrPct=10, penPct=15)]))
    assets.append(asset(
        "g_revlimid_cipla", "gRevlimid (lenalidomide complex generic - Cipla allocation)",
        "Commercial allocation (Jan 2026 volume ladder step-up)",
        "small_molecule.imid.cereblon_modulator",
        [innov_ind("mm_4l", "Multiple myeloma 4L+ + MDS",
                   "oncology.hematology.myeloma.4l_plus",
                   regions((40, 90, 80), (60, 80, 50), (400, 18, 18)),
                   slice_((4, 50, 35), (1, 40, 18), (0.1, 12, 6)),
                   {"us.reachPct": "gRevlimid Cipla allocation ~5% volume",
                    "us.priceK": "gRevlimid ~70% discount vs branded ~$160K/yr"},
                   peakYear=2027, cagrPct=20, penPct=15)]))

    weights = {"mega_bear": 10, "bear": 22, "base": 38, "bull": 25, "psychedelic_bull": 5}
    # India pharma: net cash + India IPM stickiness -- moderate-high multiples
    crev = {"mega_bear": 3100, "bear": 3300, "base": 3500, "bull": 3900, "psychedelic_bull": 4500}
    cmult = {"mega_bear": 3, "bear": 4, "base": 5, "bull": 7, "psychedelic_bull": 9}
    pmult = {"mega_bear": 3, "bear": 4, "base": 5, "bull": 7, "psychedelic_bull": 10}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [("g_lanreotide", ["acromegaly_nets"])]

    pipeline_asmps = {
        "mega_bear": {
            "g_advair": {"asthma_copd": od(("pos", 50), ("apr", 60), ("pen", 0.4))},
            "g_revlimid_cipla": {"mm_4l": od(("pos", 100), ("apr", 100), ("pen", 0.4))},
        },
        "bear": {
            "g_advair": {"asthma_copd": od(("pos", 70), ("apr", 75), ("pen", 0.6))},
            "g_revlimid_cipla": {"mm_4l": od(("pos", 100), ("apr", 100), ("pen", 0.6))},
        },
        "base": {
            "g_advair": {"asthma_copd": od(("pos", 85), ("apr", 88), ("pen", 0.85))},
            "g_revlimid_cipla": {"mm_4l": od(("pos", 100), ("apr", 100), ("pen", 0.85))},
        },
        "bull": {
            "g_advair": {"asthma_copd": od(("pos", 95), ("apr", 95), ("pen", 1.05))},
            "g_revlimid_cipla": {"mm_4l": od(("pos", 100), ("apr", 100), ("pen", 1.05))},
        },
        "psychedelic_bull": {
            "g_advair": {"asthma_copd": od(("pos", 99), ("apr", 98), ("pen", 1.2))},
            "g_revlimid_cipla": {"mm_4l": od(("pos", 100), ("apr", 100), ("pen", 1.2))},
        },
    }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "2026"), ("dateSort", "2026-06-30"), ("asset", "g_advair"),
           ("indication", "asthma_copd"), ("title", "gAdvair Diskus FDA approval (CRL resolution)"),
           ("type", "pdufa"), ("binary", True),
           ("fail_pos", 60), ("fail_apr", 70), ("success_pos", 95), ("success_apr", 95),
           ("_source", "Cipla Q4FY25 concall"), ("_confidence", "medium")),
        od(("date", "Q4 2026"), ("dateSort", "2026-12-15"), ("asset", "cipla_north_america"),
           ("indication", "cipla_north_america_outpatient_generic"),
           ("title", "gAbraxane US launch"),
           ("type", "launch"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Cipla FY25 AR"), ("_confidence", "high")),
        od(("date", "Jan 2026"), ("dateSort", "2026-01-31"), ("asset", "g_revlimid_cipla"),
           ("indication", "mm_4l"), ("title", "gRevlimid volume ladder step-up"),
           ("type", "launch"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "settlement schedule"), ("_confidence", "high")),
    ]

    return od(("company", co), ("assets", assets), ("scenarios", scenarios),
              ("catalysts", catalysts))


# =====================================================================
# DRREDDY
# =====================================================================

def build_DRREDDY():
    co = od(
        ("ticker", "DRREDDY"),
        ("name", "Dr. Reddy's Laboratories Ltd."),
        ("currentPrice", 1180),
        ("sharesOut", 834),
        ("cash", 680),
        ("currency", "INR"),
        ("phase", "commercial"),
        ("subtitle", "Indian generics + biosimilars. FY25 (Mar25) revenue INR 325B / ~$3.85B (+17% YoY). NA 44% (~$1.7B; gRevlimid ~$750M peak), India 17%, EM 16%, Europe 7% (post-Haleon NRT acquisition Sep 2024), PSAI 10%. Net cash ~$680M. gRevlimid volume cap step-up Q1FY26, full LOE Jan 2026. Semaglutide India patent expiry Mar 2026 = major opportunity."),
        ("yahooTicker", "DRREDDY.NS"),
    )

    assets = []
    # gRevlimid as own asset (FY25 contribution ~$750M)
    assets.append(asset(
        "g_revlimid_drl", "gRevlimid (lenalidomide complex generic - DRL allocation)",
        "Commercial (peak FY25 ~$750M; full LOE Jan 2026 means competition step-up)",
        "small_molecule.imid.cereblon_modulator",
        [innov_ind("mm_2l_4l", "Multiple myeloma 2L-4L+ + MDS",
                   "oncology.hematology.myeloma.2l_3l",
                   regions((85, 90, 80), (130, 80, 50), (700, 18, 18)),
                   slice_((10, 60, 35), (3, 50, 18), (0.3, 15, 6)),
                   {"us.reachPct": "DRL gRevlimid ~22% US lenalidomide volume share at peak",
                    "us.priceK": "gRevlimid blended ~$35K/yr post-LOE"},
                   salesM=750, salesYear=2025, peakYear=2026, cagrPct=-15, penPct=30)]))

    # Toripalimab (Junshi license for India)
    assets.append(asset(
        "toripalimab", "Toripalimab (anti-PD-1 mAb) - India license from Junshi (Loqtorzi)",
        "Commercial (India launch FY25; ramping; Junshi-developed)",
        "antibody.monoclonal.anti_pd1",
        [innov_ind("npc_io", "NPC + IO-eligible solid tumors (India)",
                   "oncology.hematology.nhl.dlbcl",  # placeholder for IO; using closest
                   regions((0, 0, 0), (0, 0, 0), (3000, 12, 30)),
                   slice_((0, 0, 0), (0, 0, 0), (0.5, 12, 25)),
                   {"row.priceK": "Toripalimab India WAC ~$25K/yr",
                    "row.reachPct": "DRL India distribution; Junshi sourcing"},
                   salesM=20, salesYear=2025, peakYear=2031, cagrPct=30, penPct=15)]))

    # Generic buckets
    # FY25 ex-named: $3.85B - $750M (gRevlimid) - $20M (toripalimab) = ~$3.08B in buckets
    # NA ex-gRevlimid: $1.7B - $750M = $950M
    # India: $665M, EM: $635M, Europe: $260M, PSAI: $390M, Other: $230M -> roll into Europe/EM
    assets.append(gen_bucket("drl_north_america",
                             "Dr Reddy's North America generics franchise (ex-gRevlimid)",
                             "Commercial (FY25 ~$950M US complex generics)",
                             950, "us_generics_developed_v1"))
    assets.append(gen_bucket("drl_india",
                             "Dr Reddy's India branded + generics franchise",
                             "Commercial (FY25 ~$665M India formulations)",
                             665, "emerging_markets_generics_v1"))
    assets.append(gen_bucket("drl_em",
                             "Dr Reddy's Emerging Markets franchise",
                             "Commercial (FY25 ~$635M Russia + LATAM + APAC + MENA)",
                             635, "emerging_markets_generics_v1"))
    assets.append(gen_bucket("drl_europe",
                             "Dr Reddy's Europe + Haleon NRT franchise",
                             "Commercial (FY25 ~$490M EU; Haleon NRT consumer ex-US closed Sep24)",
                             490, "eu_generics_developed_v1"))
    assets.append(gen_bucket("drl_psai",
                             "Dr Reddy's API + contract franchise",
                             "Commercial (FY25 ~$390M API + custom synthesis)",
                             390, "us_generics_developed_v1"))

    # Pipeline biosimilars + semaglutide
    assets.append(asset(
        "drl_abatacept", "DRL abatacept biosimilar (Orencia biosim)",
        "Phase 3 (US/EU filing FY26)",
        "antibody.fusion.ctla4_ig",
        [innov_ind("ra_jia", "RA + JIA + PsA",
                   "immunology.inflammatory_systemic.rheumatoid_arthritis",
                   regions((1300, 60, 35), (2000, 50, 22), (10000, 8, 6)),
                   slice_((0.4, 50, 22), (0.2, 40, 14), (0.02, 8, 4)),
                   {"us.priceK": "Abatacept biosim ~30% discount vs Orencia ~$22K/yr"},
                   peakYear=2031, cagrPct=15, penPct=12)]))
    assets.append(asset(
        "drl_rituximab", "DRL rituximab biosimilar (US BLA path; bDA-21)",
        "Phase 3 (US BLA filing target)",
        "antibody.monoclonal.anti_cd20",
        [innov_ind("nhl_cll_ra2", "NHL + CLL + RA",
                   "oncology.hematology.nhl.dlbcl",
                   regions((40, 80, 25), (60, 70, 18), (350, 18, 6)),
                   slice_((0.5, 60, 16), (0.3, 60, 12), (0.05, 18, 4)),
                   {"us.priceK": "Rituximab biosim ~40% discount; late-mover"},
                   peakYear=2032, cagrPct=10, penPct=10)]))
    assets.append(asset(
        "drl_semaglutide", "DRL semaglutide generic (India 2026 LOE; obesity + T2D)",
        "Phase 3 / India launch March 2026 patent expiry",
        "peptide.glp1.semaglutide",
        [innov_ind("obesity_t2d", "T2D + obesity (India semaglutide LOE)",
                   "cardio_metabolic.obesity.weight_management",
                   regions((45000, 35, 12), (60000, 25, 8), (40000, 8, 1.5)),
                   slice_((0.1, 1, 0.1), (0.1, 1, 0.1), (1, 30, 1.0)),
                   {"row.reachPct": "DRL India semaglutide post-LOE ~5-10% India GLP-1 volume",
                    "row.priceK": "Generic semaglutide India ~$1K/yr (~95% off branded)"},
                   peakYear=2032, cagrPct=30, penPct=20)]))

    weights = {"mega_bear": 12, "bear": 25, "base": 35, "bull": 23, "psychedelic_bull": 5}
    crev = {"mega_bear": 3500, "bear": 3700, "base": 3850, "bull": 4100, "psychedelic_bull": 4500}
    cmult = {"mega_bear": 3, "bear": 4, "base": 5, "bull": 6.5, "psychedelic_bull": 8.5}
    pmult = {"mega_bear": 3, "bear": 4, "base": 5, "bull": 7, "psychedelic_bull": 10}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [("g_revlimid_drl", ["mm_2l_4l"]), ("toripalimab", ["npc_io"])]

    pipeline_asmps = {}
    pipe_pos = {"mega_bear": 50, "bear": 70, "base": 88, "bull": 95, "psychedelic_bull": 99}
    pipe_apr = {"mega_bear": 70, "bear": 82, "base": 92, "bull": 96, "psychedelic_bull": 99}
    pipe_pen = {"mega_bear": 0.4, "bear": 0.6, "base": 0.85, "bull": 1.05, "psychedelic_bull": 1.2}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "drl_abatacept": {"ra_jia": od(("pos", pipe_pos[sk]), ("apr", pipe_apr[sk]), ("pen", pipe_pen[sk]))},
            "drl_rituximab": {"nhl_cll_ra2": od(("pos", pipe_pos[sk]-10), ("apr", pipe_apr[sk]), ("pen", pipe_pen[sk]))},
            "drl_semaglutide": {"obesity_t2d": od(("pos", min(100, pipe_pos[sk]+10)), ("apr", pipe_apr[sk]), ("pen", pipe_pen[sk]))},
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "Mar 2026"), ("dateSort", "2026-03-31"), ("asset", "drl_semaglutide"),
           ("indication", "obesity_t2d"), ("title", "Semaglutide India patent expiry; DRL launch"),
           ("type", "loe"), ("binary", True),
           ("fail_pos", 80), ("fail_apr", 90), ("success_pos", 100), ("success_apr", 100),
           ("_source", "DRL pipeline disclosure"), ("_confidence", "high")),
        od(("date", "Jan 2026"), ("dateSort", "2026-01-31"), ("asset", "g_revlimid_drl"),
           ("indication", "mm_2l_4l"), ("title", "gRevlimid full LOE; volume cap removed"),
           ("type", "loe"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "settlement schedule"), ("_confidence", "high")),
        od(("date", "FY26"), ("dateSort", "2026-12-15"), ("asset", "drl_abatacept"),
           ("indication", "ra_jia"), ("title", "Abatacept biosimilar US/EU filing"),
           ("type", "bla_submission"), ("binary", True),
           ("fail_pos", 70), ("fail_apr", 80), ("success_pos", 95), ("success_apr", 92),
           ("_source", "DRL pipeline"), ("_confidence", "medium")),
    ]

    return od(("company", co), ("assets", assets), ("scenarios", scenarios),
              ("catalysts", catalysts))


# =====================================================================
# HIK - Hikma
# =====================================================================

def build_HIK():
    co = od(
        ("ticker", "HIK"),
        ("name", "Hikma Pharmaceuticals plc"),
        ("currentPrice", 2050),
        ("sharesOut", 220),
        ("cash", -750),
        ("currency", "GBP"),
        ("phase", "commercial"),
        ("subtitle", "MENA-rooted UK FTSE-100 generics specialist (Jordanian heritage). FY25 revenue ~$3.2B (USD reporting). Injectables ~$1.25B (#2 US generic injectables ~$800M + EU ~$300M); Generics US oral ~$850M; Branded MENA ~$1.1B (fastest-growing). Specialty: Kloxxado naloxone 8mg, Mitigare colchicine, sodium nitrite/thiosulfate (cyanide antidote)."),
        ("yahooTicker", "HIK.L"),
    )

    assets = []
    # Specialty branded
    assets.append(asset(
        "kloxxado", "Kloxxado (naloxone 8mg nasal spray) - opioid overdose rescue",
        "Commercial (Hikma specialty)",
        "small_molecule.gpcr.opioid_antagonist",
        [innov_ind("opioid_overdose", "Opioid overdose emergency rescue (high-dose nasal naloxone)",
                   "cns.psychiatry.substance_use.opioid",
                   regions((2500, 50, 0.4), (1500, 30, 0.2), (5000, 8, 0.1)),
                   slice_((0.5, 35, 0.3), (0, 0, 0), (0, 0, 0)),
                   {"us.priceK": "Kloxxado WAC ~$300/2pk"},
                   salesM=40, salesYear=2025, peakYear=2030, cagrPct=10, penPct=20)]))
    assets.append(asset(
        "mitigare", "Mitigare (colchicine 0.6mg) - gout flare prophylaxis",
        "Commercial (Hikma specialty branded)",
        "small_molecule.tubulin.colchicine",
        [innov_ind("gout", "Gout flare prophylaxis + acute treatment",
                   "musculoskeletal.crystal_arthropathy.gout",
                   regions((9000, 50, 0.5), (15000, 30, 0.2), (50000, 5, 0.05)),
                   slice_((0.3, 40, 4.0), (0, 0, 0), (0, 0, 0)),
                   {"us.priceK": "Mitigare WAC ~$600/yr (slice priceK inflated to capture broad-gout TAM not reflected in refractory-gout authoritative data)"},
                   salesM=60, salesYear=2025, peakYear=2030, cagrPct=2, penPct=20)]))

    # Generic buckets
    assets.append(gen_bucket("hik_us_injectables",
                             "Hikma US sterile injectables franchise (#2 US generic injectables)",
                             "Commercial (FY25 ~$800M US hospital injectables; ~130 products)",
                             800, "us_generics_developed_v1"))
    assets.append(gen_bucket("hik_eu_injectables",
                             "Hikma Europe injectables franchise",
                             "Commercial (FY25 ~$300M; UK + DE + PT manufacturing)",
                             300, "eu_generics_developed_v1"))
    assets.append(gen_bucket("hik_us_oral",
                             "Hikma US oral generics franchise",
                             "Commercial (FY25 ~$750M US oral solids; complex generics)",
                             750, "us_generics_developed_v1"))
    assets.append(gen_bucket("hik_mena_branded",
                             "Hikma MENA branded franchise (Saudi + Egypt + Algeria + UAE + Jordan)",
                             "Commercial (FY25 ~$1.1B MENA branded + in-licensed Lilly/Boehringer/Takeda)",
                             1100, "emerging_markets_generics_v1"))

    weights = {"mega_bear": 12, "bear": 23, "base": 38, "bull": 22, "psychedelic_bull": 5}
    # Heavy levered generics; injectables franchise more durable than oral
    crev = {"mega_bear": 3000, "bear": 3150, "base": 3300, "bull": 3500, "psychedelic_bull": 3900}
    cmult = {"mega_bear": 1.8, "bear": 2.4, "base": 3.2, "bull": 4.2, "psychedelic_bull": 5.5}
    pmult = {"mega_bear": 2, "bear": 3, "base": 4, "bull": 6, "psychedelic_bull": 8}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [("kloxxado", ["opioid_overdose"]), ("mitigare", ["gout"])]

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds)

    catalysts = [
        od(("date", "Mar 2026"), ("dateSort", "2026-03-15"), ("asset", "hik_us_injectables"),
           ("indication", "hik_us_injectables_outpatient_generic"),
           ("title", "FY2025 full-year results"),
           ("type", "investor_day"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Hikma IR calendar"), ("_confidence", "high")),
        od(("date", "H2 2026"), ("dateSort", "2026-09-30"), ("asset", "hik_us_oral"),
           ("indication", "hik_us_oral_outpatient_generic"),
           ("title", "Generic Symbicort + complex inhaler approvals"),
           ("type", "pdufa"), ("binary", True),
           ("fail_pos", 60), ("fail_apr", 70), ("success_pos", 95), ("success_apr", 95),
           ("_source", "Hikma pipeline disclosure"), ("_confidence", "medium")),
    ]

    return od(("company", co), ("assets", assets), ("scenarios", scenarios),
              ("catalysts", catalysts))


# =====================================================================
# AUROBINDO
# =====================================================================

def build_AUROBINDO():
    co = od(
        ("ticker", "AUROBINDO"),
        ("name", "Aurobindo Pharma Ltd."),
        ("currentPrice", 1180),
        ("sharesOut", 579),
        ("cash", -140),
        ("currency", "INR"),
        ("phase", "commercial"),
        ("subtitle", "Indian top-3 US generics player by Rx volume. FY25 (Mar25) revenue INR 317B / ~$3.78B. US 47% (~$1.78B), Europe 25% (~$0.95B fastest growth), Growth Markets 6%, ARV 4% (declining), API 13%. Eugia (specialty + biosimilars subsidiary): Avastin/Herceptin/Filgrastim/Pegfilgrastim biosimilars. Pen-G facility (Kakinada) commercial FY25 ramping. AuroVaccines PCV-13 early launch."),
        ("yahooTicker", "AUROPHARMA.NS"),
    )

    assets = []
    # Eugia biosimilars (named)
    assets.append(asset(
        "eugia_bevacizumab", "Eugia bevacizumab biosimilar (anti-VEGF)",
        "Commercial EU (CuraTeq); US filed",
        "antibody.monoclonal.anti_vegf",
        [innov_ind("crc_nsclc", "Metastatic CRC + NSCLC + ovarian + cervical (anti-VEGF)",
                   "oncology.gi.colorectal",
                   regions((150, 80, 30), (250, 70, 20), (1500, 15, 6)),
                   slice_((0.5, 50, 18), (1.5, 60, 12), (0.1, 15, 5)),
                   {"us.priceK": "Bevacizumab biosim ~30-50% discount vs Avastin"},
                   salesM=70, salesYear=2025, peakYear=2030, cagrPct=20, penPct=15)]))
    assets.append(asset(
        "eugia_trastuzumab", "Eugia trastuzumab biosimilar (anti-HER2)",
        "Commercial EU; US filed",
        "antibody.monoclonal.anti_her2",
        [innov_ind("her2_breast", "HER2+ breast + gastric (anti-HER2)",
                   "oncology.breast.her2_pos",
                   regions((60, 80, 100), (90, 70, 70), (450, 18, 25)),
                   slice_((0.3, 50, 60), (1, 60, 45), (0.1, 18, 16)),
                   {"us.priceK": "Trastuzumab biosim ~30-50% discount vs Herceptin"},
                   salesM=50, salesYear=2025, peakYear=2030, cagrPct=15, penPct=12)]))
    assets.append(asset(
        "eugia_pegfilgrastim", "Eugia pegfilgrastim biosimilar (G-CSF)",
        "Commercial EU; US development",
        "recombinant_protein.cytokine.gcsf",
        [innov_ind("neutropenia", "Chemotherapy-induced neutropenia",
                   "oncology.supportive_care.neutropenia",
                   regions((300, 70, 7), (450, 60, 5), (2500, 18, 2)),
                   slice_((0.2, 50, 4), (1, 50, 3), (0.1, 18, 1)),
                   {"us.priceK": "Pegfilgrastim biosim ~50% discount vs Neulasta"},
                   salesM=40, salesYear=2025, peakYear=2030, cagrPct=10, penPct=15)]))

    # Generic buckets
    assets.append(gen_bucket("auro_us_generics",
                             "Aurobindo US generics franchise (top-3 by Rx volume)",
                             "Commercial (FY25 ~$1.78B US oral + sterile + complex)",
                             1780, "us_generics_developed_v1"))
    assets.append(gen_bucket("auro_eu_generics",
                             "Aurobindo Europe generics franchise (CuraTeq commercialization)",
                             "Commercial (FY25 ~$790M EU; fastest growing geo ex-Eugia biosims)",
                             790, "eu_generics_developed_v1"))
    assets.append(gen_bucket("auro_growth_em",
                             "Aurobindo Growth Markets + ARV franchise",
                             "Commercial (FY25 ~$310M Growth + ARV declining on tender pricing)",
                             310, "emerging_markets_generics_v1"))
    assets.append(gen_bucket("auro_api",
                             "Aurobindo API + Pen-G franchise",
                             "Commercial (FY25 ~$490M API; Pen-G Kakinada commercial FY25)",
                             490, "us_generics_developed_v1"))

    # Pipeline
    assets.append(asset(
        "eugia_aflibercept", "Eugia aflibercept biosimilar (Eylea biosim)",
        "Phase 3 / US filing",
        "antibody.fusion.vegf_trap",
        [innov_ind("nvamd_dme_eu", "nvAMD + DME + DR (anti-VEGF retinal)",
                   "ophthalmology.retina.nvamd",
                   regions((2500, 75, 12), (3500, 65, 7), (15000, 12, 3)),
                   slice_((0.3, 50, 7), (0.5, 50, 4), (0.1, 12, 1.5)),
                   {"us.priceK": "Aflibercept biosim ~30% discount vs Eylea"},
                   peakYear=2031, cagrPct=20, penPct=12)]))
    assets.append(asset(
        "auro_g_semaglutide", "Aurobindo semaglutide complex generic (India + EM)",
        "Pre-launch; India 2026 LOE opportunity",
        "peptide.glp1.semaglutide",
        [innov_ind("obesity_t2d", "T2D + obesity (semaglutide post-LOE)",
                   "cardio_metabolic.obesity.weight_management",
                   regions((45000, 35, 12), (60000, 25, 8), (40000, 8, 1.5)),
                   slice_((0.1, 1, 0.1), (0.1, 1, 0.1), (0.5, 30, 0.8)),
                   {"row.priceK": "Generic semaglutide India ~$0.8K/yr"},
                   peakYear=2032, cagrPct=30, penPct=18)]))

    weights = {"mega_bear": 12, "bear": 25, "base": 38, "bull": 20, "psychedelic_bull": 5}
    crev = {"mega_bear": 3500, "bear": 3700, "base": 3800, "bull": 4100, "psychedelic_bull": 4600}
    cmult = {"mega_bear": 2.0, "bear": 3.0, "base": 4.0, "bull": 5.5, "psychedelic_bull": 7.5}
    pmult = {"mega_bear": 3, "bear": 4, "base": 5, "bull": 7, "psychedelic_bull": 10}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [
        ("eugia_bevacizumab", ["crc_nsclc"]), ("eugia_trastuzumab", ["her2_breast"]),
        ("eugia_pegfilgrastim", ["neutropenia"]),
    ]

    pipeline_asmps = {}
    pipe_pos = {"mega_bear": 55, "bear": 75, "base": 90, "bull": 96, "psychedelic_bull": 99}
    pipe_apr = {"mega_bear": 75, "bear": 85, "base": 92, "bull": 96, "psychedelic_bull": 99}
    pipe_pen = {"mega_bear": 0.4, "bear": 0.6, "base": 0.85, "bull": 1.05, "psychedelic_bull": 1.2}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "eugia_aflibercept": {"nvamd_dme_eu": od(("pos", pipe_pos[sk]), ("apr", pipe_apr[sk]), ("pen", pipe_pen[sk]))},
            "auro_g_semaglutide": {"obesity_t2d": od(("pos", min(100, pipe_pos[sk]+5)), ("apr", pipe_apr[sk]), ("pen", pipe_pen[sk]))},
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "FY26"), ("dateSort", "2026-09-30"), ("asset", "eugia_aflibercept"),
           ("indication", "nvamd_dme_eu"), ("title", "Aflibercept biosimilar US filing/approval"),
           ("type", "bla_submission"), ("binary", True),
           ("fail_pos", 70), ("fail_apr", 80), ("success_pos", 95), ("success_apr", 92),
           ("_source", "Aurobindo pipeline"), ("_confidence", "medium")),
        od(("date", "Mar 2026"), ("dateSort", "2026-03-31"), ("asset", "auro_g_semaglutide"),
           ("indication", "obesity_t2d"),
           ("title", "Semaglutide India LOE; Aurobindo launch"),
           ("type", "loe"), ("binary", True),
           ("fail_pos", 80), ("fail_apr", 90), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Aurobindo pipeline"), ("_confidence", "high")),
    ]

    return od(("company", co), ("assets", assets), ("scenarios", scenarios),
              ("catalysts", catalysts))


# =====================================================================
# HANMI - innovative-leaning, NOT mostly generics
# =====================================================================

def build_HANMI():
    co = od(
        ("ticker", "HANMI"),
        ("name", "Hanmi Pharmaceutical Co. Ltd."),
        ("currentPrice", 295000),
        ("sharesOut", 12.6),
        ("cash", 180),
        ("currency", "KRW"),
        ("phase", "commercial"),
        ("subtitle", "Korean innovative pharma. FY25 revenue KRW 1.65T / ~$1.20B: Korea Rx 58% (Rosuzet, Amosartan, Esomezol franchises); Beijing Hanmi pediatric JV 22%; royalties 8%; OTC + exports 12%. LAPS platform (long-acting peptide). Pipeline: efpeglenatide GLP-1 obesity Ph3 H.O.P.E., efocipegtrutide MASH Ph2, HM15136 CHI Ph2, HM15912 SBS Ph2. Belvarafenib partnered Roche."),
        ("yahooTicker", "128940.KS"),
    )

    # Korea franchise as one EM bucket (since named brands are in INR-ish small amount each)
    assets = []
    assets.append(gen_bucket("hanmi_korea_rx",
                             "Hanmi Korea Rx franchise (Rosuzet+Amosartan+Esomezol+Pidogul+Naxozole+OTC)",
                             "Commercial (FY25 KRW 960B / ~$700M Korea + KRW 200B / ~$150M OTC)",
                             850, "emerging_markets_generics_v1",
                             {"cardio_metabolic.lipids.ldl_cv_risk": 0.20,
                              "cardio_metabolic.hypertension.outpatient_generic": 0.16,
                              "immunology.inflammatory_gi.gerd_peptic": 0.10}))
    assets.append(gen_bucket("hanmi_china_jv",
                             "Beijing Hanmi pediatric JV (China)",
                             "Commercial (FY25 KRW 365B / ~$270M China pediatric)",
                             270, "emerging_markets_generics_v1"))

    # Pipeline assets (innovative LAPS portfolio)
    assets.append(asset(
        "efpeglenatide", "Efpeglenatide (LAPS-GLP1) - long-acting GLP-1 receptor agonist (Hanmi-only post-Sanofi return)",
        "Phase 3 H.O.P.E. obesity (readout 2H26); also T2D",
        "peptide.glp1.long_acting",
        [innov_ind("obesity", "Obesity weight management (LAPS-GLP-1 once-weekly)",
                   "cardio_metabolic.obesity.weight_management",
                   regions((45000, 35, 12), (60000, 25, 8), (250000, 5, 1.5)),
                   slice_((0.5, 35, 8), (0.3, 25, 5), (0.05, 5, 1)),
                   {"us.priceK": "Estimated WAC ~$8K/yr if approved (vs Wegovy $14K/yr; Hanmi-priced lower)",
                    "us.reachPct": "Niche entry post-Wegovy/Mounjaro/CagriSema dominance"},
                   peakYear=2032, cagrPct=0, penPct=10)]))
    assets.append(asset(
        "efocipegtrutide", "Efocipegtrutide (HM15211) - LAPS triple agonist GLP-1/GIP/glucagon",
        "Phase 2 MASH (biopsy readout 2H26)",
        "peptide.multi_agonist.glp1_gip_glucagon",
        [innov_ind("mash", "Metabolic dysfunction-associated steatohepatitis (MASH F2-F3)",
                   "cardio_metabolic.liver.mash",
                   regions((6000, 30, 30), (10000, 20, 18), (35000, 5, 5)),
                   slice_((0.5, 35, 25), (0.3, 25, 15), (0.03, 5, 5)),
                   {"us.priceK": "Estimated WAC $25K/yr if approved (post-Resmetirom)",
                    "us.reachPct": "Niche post-Resmetirom + GLP-1-class competition"},
                   peakYear=2033, cagrPct=0, penPct=10)]))
    assets.append(asset(
        "hm15136", "HM15136 (efpegerglucagon) - long-acting glucagon analog",
        "Phase 2 congenital hyperinsulinism (FDA Fast Track + orphan)",
        "peptide.hormone.glucagon_analog",
        [innov_ind("chi", "Congenital hyperinsulinism (rare pediatric ultra-orphan)",
                   "rare_disease.endocrine.congenital_hyperinsulinism",
                   regions((1, 80, 800), (1.5, 70, 500), (5, 18, 150)),
                   slice_((30, 70, 600), (15, 60, 400), (1, 18, 120)),
                   {"us.priceK": "Estimated WAC ultra-orphan $500-700K/yr",
                    "us.reachPct": "First disease-modifying CHI; ~30% diagnosed treated"},
                   peakYear=2032, cagrPct=0, penPct=18)]))
    assets.append(asset(
        "hm15912", "HM15912 (efpeglutide) - long-acting GLP-2 analog",
        "Phase 2 short bowel syndrome (FDA orphan)",
        "peptide.hormone.glp2",
        [innov_ind("sbs", "Short bowel syndrome (intestinal failure; SBS-IF parenteral support)",
                   "rare_disease.gi.short_bowel_syndrome",
                   regions((15, 80, 250), (20, 70, 150), (50, 18, 40)),
                   slice_((10, 50, 200), (5, 40, 120), (0.3, 18, 30)),
                   {"us.priceK": "Estimated WAC $200K/yr (vs Gattex $400K/yr)",
                    "us.reachPct": "Post-Gattex 2nd-gen GLP-2 ~10% SBS-IF Rx"},
                   peakYear=2033, cagrPct=0, penPct=12)]))
    assets.append(asset(
        "belvarafenib", "Belvarafenib - pan-RAF inhibitor (Roche/Genentech-partnered)",
        "Phase 1b/2 NRAS-mutant melanoma combos (Genentech-led)",
        "small_molecule.kinase.pan_raf",
        [innov_ind("nras_melanoma", "NRAS-mutant + KRAS-mutant solid tumors",
                   "oncology.skin.melanoma",
                   regions((20, 80, 80), (30, 70, 50), (120, 18, 18)),
                   slice_((3, 50, 60), (1, 40, 40), (0.1, 15, 12)),
                   {"us.priceK": "Estimated WAC $60K/mo if approved",
                    "us.reachPct": "Hanmi royalty stream; Roche commercial"},
                   peakYear=2033, cagrPct=0, penPct=10)]))

    weights = {"mega_bear": 12, "bear": 25, "base": 38, "bull": 20, "psychedelic_bull": 5}
    # Korean innovative pharma; currentPrice 295000 KRW × 12.6M shares = mcap ~3.7T KRW (~$2.7B)
    # commercialRevM in KRW M after FX = ~1.7T; need mult ~1.5-2 for mega_bear to land below price
    crev = {"mega_bear": 1100, "bear": 1180, "base": 1250, "bull": 1400, "psychedelic_bull": 1700}
    cmult = {"mega_bear": 1.5, "bear": 2.2, "base": 3.0, "bull": 4.0, "psychedelic_bull": 5.5}
    pmult = {"mega_bear": 2, "bear": 3, "base": 5, "bull": 8, "psychedelic_bull": 13}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = []  # All commercial revenue is in mixTemplate buckets

    pipeline_asmps = {}
    pos_grid = {
        "efpeglenatide":     {"mega_bear": 25, "bear": 40, "base": 55, "bull": 70, "psychedelic_bull": 80},
        "efocipegtrutide":   {"mega_bear": 12, "bear": 22, "base": 38, "bull": 55, "psychedelic_bull": 70},
        "hm15136":           {"mega_bear": 18, "bear": 30, "base": 50, "bull": 65, "psychedelic_bull": 78},
        "hm15912":           {"mega_bear": 15, "bear": 28, "base": 45, "bull": 60, "psychedelic_bull": 75},
        "belvarafenib":      {"mega_bear": 12, "bear": 20, "base": 35, "bull": 50, "psychedelic_bull": 65},
    }
    apr_grid = {a: {"mega_bear": 50, "bear": 65, "base": 80, "bull": 90, "psychedelic_bull": 95}
                for a in pos_grid}
    pen_grid = {a: {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25}
                for a in pos_grid}

    ind_map = {
        "efpeglenatide": "obesity",
        "efocipegtrutide": "mash",
        "hm15136": "chi",
        "hm15912": "sbs",
        "belvarafenib": "nras_melanoma",
    }

    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {}
        for aid, iid in ind_map.items():
            pipeline_asmps[sk][aid] = {iid: od(
                ("pos", pos_grid[aid][sk]),
                ("apr", apr_grid[aid][sk]),
                ("pen", pen_grid[aid][sk]),
            )}

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "H2 2026"), ("dateSort", "2026-09-30"), ("asset", "efpeglenatide"),
           ("indication", "obesity"), ("title", "Efpeglenatide H.O.P.E. Ph3 obesity topline"),
           ("type", "phase3_data"), ("binary", True),
           ("fail_pos", 25), ("fail_apr", 60), ("success_pos", 75), ("success_apr", 90),
           ("_source", "Hanmi pipeline"), ("_confidence", "medium")),
        od(("date", "H2 2026"), ("dateSort", "2026-12-15"), ("asset", "efocipegtrutide"),
           ("indication", "mash"), ("title", "Efocipegtrutide MASH Ph2 biopsy readout"),
           ("type", "phase2_data"), ("binary", True),
           ("fail_pos", 12), ("fail_apr", 50), ("success_pos", 50), ("success_apr", 80),
           ("_source", "Hanmi pipeline"), ("_confidence", "medium")),
        od(("date", "H1 2027"), ("dateSort", "2027-04-30"), ("asset", "hm15136"),
           ("indication", "chi"), ("title", "HM15136 CHI Ph2 readout"),
           ("type", "phase2_data"), ("binary", True),
           ("fail_pos", 18), ("fail_apr", 65), ("success_pos", 65), ("success_apr", 88),
           ("_source", "Hanmi pipeline"), ("_confidence", "medium")),
        od(("date", "H2 2026"), ("dateSort", "2026-11-30"), ("asset", "hm15912"),
           ("indication", "sbs"), ("title", "HM15912 SBS Ph2 readout"),
           ("type", "phase2_data"), ("binary", True),
           ("fail_pos", 15), ("fail_apr", 60), ("success_pos", 60), ("success_apr", 85),
           ("_source", "Hanmi pipeline"), ("_confidence", "medium")),
    ]

    return od(("company", co), ("assets", assets), ("scenarios", scenarios),
              ("catalysts", catalysts))


# =====================================================================
# LUPIN
# =====================================================================

def build_LUPIN():
    co = od(
        ("ticker", "LUPIN"),
        ("name", "Lupin Limited"),
        ("currentPrice", 2050),
        ("sharesOut", 456),
        ("cash", 220),
        ("currency", "INR"),
        ("phase", "commercial"),
        ("subtitle", "Indian respiratory + complex generics. FY25 (Mar25) revenue INR 227B / ~$2.7B. India branded 37% (~$1.0B; Cidmus sacubitril/valsartan flagship), US generics+specialty 36% (~$0.98B; gAlbuterol, gSpiriva flagship inhaled), EMEA 9%, Growth Markets 7%, API 6%. Net cash $220M. Inhalation respiratory pipeline = strategic franchise. Biosimilars: Nepexto etanercept EU, ranibizumab in development."),
        ("yahooTicker", "LUPIN.NS"),
    )

    assets = []
    # Named: gAlbuterol HFA (key US flagship)
    assets.append(asset(
        "g_albuterol", "gAlbuterol HFA (ProAir HFA generic) - SABA bronchodilator inhaler",
        "Commercial (FY25 ~$200M+ run-rate; market-leading US generic share)",
        "small_molecule.gpcr.saba",
        [innov_ind("asthma_acute", "Asthma + COPD acute bronchodilator (SABA pMDI)",
                   "respiratory.inflammatory.asthma_severe",
                   regions((20000, 50, 0.4), (35000, 35, 0.2), (150000, 8, 0.1)),
                   slice_((30, 60, 1.5), (0.1, 1, 0.1), (0.1, 1, 0.1)),
                   {"us.priceK": "gAlbuterol HFA generic ~$50/mo blended (~$1500/yr full Rx incl. multiple inhalers)",
                    "us.reachPct": "Lupin ~30%+ US gAlbuterol HFA volume share (severe asthma proxy uses broader denominator)"},
                   salesM=210, salesYear=2025, peakYear=2030, cagrPct=2, penPct=30)]))
    # gSpiriva (recent complex inhaler win)
    assets.append(asset(
        "g_spiriva", "gSpiriva (tiotropium HandiHaler complex generic)",
        "Commercial (recently launched; complex DPI generic)",
        "small_molecule.gpcr.lama",
        [innov_ind("copd_lama", "COPD long-acting muscarinic antagonist (DPI)",
                   "respiratory.inflammatory.copd",
                   regions((15000, 60, 1.5), (20000, 35, 0.8), (200000, 6, 0.3)),
                   slice_((1, 50, 1.0), (0, 0, 0), (0, 0, 0)),
                   {"us.priceK": "gSpiriva ~$1K/yr (~50% off branded Spiriva)",
                    "us.reachPct": "Lupin first-to-launch gSpiriva HandiHaler ~10-15% share"},
                   salesM=120, salesYear=2025, peakYear=2030, cagrPct=15, penPct=18)]))
    # Solosec (women's health specialty)
    assets.append(asset(
        "solosec", "Solosec (secnidazole 2g single-dose) - bacterial vaginosis specialty",
        "Commercial (US specialty branded)",
        "small_molecule.antimicrobial.nitroimidazole",
        [innov_ind("bv", "Bacterial vaginosis (single-dose oral)",
                   "infectious_disease.bacterial.vaginosis",
                   regions((20000, 40, 0.4), (30000, 25, 0.2), (200000, 5, 0.05)),
                   slice_((0.4, 35, 0.35), (0, 0, 0), (0, 0, 0)),
                   {"us.priceK": "Solosec WAC ~$350/dose"},
                   salesM=40, salesYear=2025, peakYear=2030, cagrPct=8, penPct=22)]))

    # Generic franchise buckets
    # Total $2.7B; named brands above ~$370M; remaining ~$2.33B in buckets
    # India $1.0B; US ex-named $565M; EMEA $250M; Growth $190M; API $160M; Other $165M
    assets.append(gen_bucket("lupin_india",
                             "Lupin India branded formulations franchise (Cidmus + Ondero + cardio + respi + women's)",
                             "Commercial (FY25 ~$1.0B India branded Rx; Cidmus INR 700+ Cr flagship)",
                             1000, "emerging_markets_generics_v1",
                             {"cardio_metabolic.cardiovascular.heart_failure": 0.10,
                              "respiratory.inflammatory.asthma_severe": 0.08}))
    assets.append(gen_bucket("lupin_us_generics",
                             "Lupin US generics franchise (ex-specialty)",
                             "Commercial (FY25 ~$565M US generics ex-gAlbuterol/gSpiriva/Solosec)",
                             565, "us_generics_developed_v1"))
    assets.append(gen_bucket("lupin_emea",
                             "Lupin EMEA franchise (Europe + MENA)",
                             "Commercial (FY25 ~$250M EMEA + Nepexto etanercept biosim EU)",
                             250, "eu_generics_developed_v1",
                             {"immunology.inflammatory_systemic.rheumatoid_arthritis": 0.08}))
    assets.append(gen_bucket("lupin_growth_em",
                             "Lupin Growth Markets franchise (APAC + LATAM + AU)",
                             "Commercial (FY25 ~$190M)",
                             190, "emerging_markets_generics_v1"))
    assets.append(gen_bucket("lupin_api",
                             "Lupin API + contract franchise",
                             "Commercial (FY25 ~$330M API + LATAM + other)",
                             330, "us_generics_developed_v1"))

    # Pipeline
    assets.append(asset(
        "g_advair_lupin", "Lupin gAdvair Diskus (fluticasone-salmeterol DPI complex generic)",
        "FDA review (high-value complex inhaler approval pending)",
        "small_molecule.gpcr.laba_ics_combo",
        [innov_ind("asthma_copd", "Asthma + COPD (DPI inhaler complex generic)",
                   "respiratory.inflammatory.asthma_severe",
                   regions((20000, 35, 4), (35000, 25, 2.5), (150000, 5, 0.6)),
                   slice_((1.5, 35, 2), (0.4, 25, 1.2), (0.05, 5, 0.3)),
                   {"us.priceK": "gAdvair ~50% discount vs Advair Diskus ~$2K/yr",
                    "us.reachPct": "Lupin gAdvair Diskus ~15-20% Advair-class share if approved"},
                   peakYear=2031, cagrPct=8, penPct=15)]))
    assets.append(asset(
        "lupin_ranibizumab", "Lupin ranibizumab biosimilar (Lucentis biosim)",
        "Phase 3 (EU/EM launch progressing)",
        "antibody.fragment.anti_vegf",
        [innov_ind("nvamd", "nvAMD + DME (anti-VEGF retinal)",
                   "ophthalmology.retina.nvamd",
                   regions((2500, 75, 12), (3500, 65, 7), (15000, 12, 3)),
                   slice_((0.2, 50, 7), (0.4, 50, 4), (0.05, 12, 1.5)),
                   {"us.priceK": "Ranibizumab biosim ~30% discount vs Lucentis"},
                   peakYear=2031, cagrPct=15, penPct=10)]))

    weights = {"mega_bear": 10, "bear": 22, "base": 38, "bull": 25, "psychedelic_bull": 5}
    crev = {"mega_bear": 2500, "bear": 2650, "base": 2800, "bull": 3100, "psychedelic_bull": 3500}
    cmult = {"mega_bear": 3, "bear": 4, "base": 5, "bull": 6.5, "psychedelic_bull": 8.5}
    pmult = {"mega_bear": 3, "bear": 4, "base": 5, "bull": 7, "psychedelic_bull": 10}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [
        ("g_albuterol", ["asthma_acute"]), ("g_spiriva", ["copd_lama"]),
        ("solosec", ["bv"]),
    ]

    pipeline_asmps = {}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pos_g = {"mega_bear": 60, "bear": 78, "base": 90, "bull": 95, "psychedelic_bull": 99}[sk]
        pos_b = {"mega_bear": 50, "bear": 70, "base": 85, "bull": 92, "psychedelic_bull": 97}[sk]
        apr = {"mega_bear": 70, "bear": 82, "base": 90, "bull": 95, "psychedelic_bull": 98}[sk]
        pen = {"mega_bear": 0.4, "bear": 0.6, "base": 0.85, "bull": 1.05, "psychedelic_bull": 1.2}[sk]
        pipeline_asmps[sk] = {
            "g_advair_lupin": {"asthma_copd": od(("pos", pos_g), ("apr", apr), ("pen", pen))},
            "lupin_ranibizumab": {"nvamd": od(("pos", pos_b), ("apr", apr), ("pen", pen))},
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "FY26"), ("dateSort", "2026-09-30"), ("asset", "g_advair_lupin"),
           ("indication", "asthma_copd"), ("title", "gAdvair Diskus FDA approval"),
           ("type", "pdufa"), ("binary", True),
           ("fail_pos", 60), ("fail_apr", 70), ("success_pos", 95), ("success_apr", 95),
           ("_source", "Lupin pipeline"), ("_confidence", "medium")),
        od(("date", "Q4 2026"), ("dateSort", "2026-12-15"), ("asset", "g_spiriva"),
           ("indication", "copd_lama"), ("title", "gSpiriva US share ramp"),
           ("type", "launch"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Lupin Q4 IR"), ("_confidence", "high")),
    ]

    return od(("company", co), ("assets", assets), ("scenarios", scenarios),
              ("catalysts", catalysts))


# =====================================================================
# Main
# =====================================================================

# FX rates: USD -> local. cash and commercialRevM are scaled by these.
# Rationale: currentPrice is in local currency (e.g., 1500 INR), sharesOut in
# millions; computeScenario does ev/sharesOut so EV must be in local-currency
# millions to yield local-currency price per share.
FX = {
    "VTRS": 1.0,         # USD
    "SDZ": 0.90,         # CHF
    "SUN": 84.0,         # INR
    "CELLTRION": 1370.0, # KRW
    "CIPLA": 84.0,       # INR
    "DRREDDY": 84.0,     # INR
    "HIK": 78.0,         # GBp (pence) -- currentPrice quoted in pence on LSE
    "AUROBINDO": 84.0,   # INR
    "HANMI": 1370.0,     # KRW
    "LUPIN": 84.0,       # INR
}


def apply_fx(cfg, fx):
    """Scale cash and val.commercialRevM by fx (USD -> local). Idempotent."""
    if fx == 1.0:
        return cfg
    co = cfg["company"]
    co["cash"] = round(co["cash"] * fx)
    for sk, scen in cfg["scenarios"].items():
        v = scen.get("val", {})
        if "commercialRevM" in v:
            v["commercialRevM"] = round(v["commercialRevM"] * fx)
    return cfg


BUILDERS = [
    ("VTRS", build_VTRS),
    ("SDZ", build_SDZ),
    ("SUN", build_SUN),
    ("CELLTRION", build_CELLTRION),
    ("CIPLA", build_CIPLA),
    ("DRREDDY", build_DRREDDY),
    ("HIK", build_HIK),
    ("AUROBINDO", build_AUROBINDO),
    ("HANMI", build_HANMI),
    ("LUPIN", build_LUPIN),
]


def main():
    for ticker, builder in BUILDERS:
        cfg = builder()
        cfg = apply_fx(cfg, FX[ticker])
        write_config(ticker, cfg)

    # Update manifest
    manifest_path = CONFIGS / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for ticker, _ in BUILDERS:
        if ticker not in manifest:
            manifest.append(ticker)
    manifest = sorted(set(manifest))
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"\n  manifest updated -> {len(manifest)} tickers")


if __name__ == "__main__":
    main()
