# -*- coding: utf-8 -*-
"""Build configs for PTCT (PTC Therapeutics) + TGTX (TG Therapeutics) + CHRS (Coherus Oncology).

Three US specialty biotechs each anchoring distinct franchises:
- PTCT: rare-disease + Evrysdi royalty + Novartis PTC518 HD deal Dec 2024 $1B+$1.9B
- TGTX: Briumvi anti-CD20 MS franchise; SC Ph3 enrollment complete Apr 2026
- CHRS: pivoted to "Coherus Oncology" pure IO play post-Udenyca/Cimerli/Yusimry divests
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
# PTCT - PTC Therapeutics
# ============================================================

def build_PTCT():
    co = od(
        ("ticker", "PTCT"),
        ("name", "PTC Therapeutics, Inc."),
        ("currentPrice", 70),
        ("sharesOut", 83),
        ("cash", 1950),  # $1.95B YE25 post Royalty Pharma Evrysdi sale Dec 2025
        ("currency", "USD"),
        ("phase", "commercial"),
        ("subtitle", "Rare-disease specialty + Novartis HD deal. FY25 revenue $1.731B includes $1.0B Novartis PTC518 upfront one-time; recurring product + royalty $831M: Translarna $235M (EMA CHMP NON-RENEWAL Apr 2025; EU residual wind-down + US NDA withdrawn; was $321M FY24), Emflaza $146M (deflazacort DMD; generics LOE; was $207M), Evrysdi (risdiplam SMA) Roche royalty $244M (PTC SOLD remaining royalty to Royalty Pharma Dec 2025: $240M up + $60M milestones; retained $150M earnout if Evrysdi reaches $2.5B), Sephience (sepiapterin PKU; FDA Jul 2025) $111M (Q4'25 alone $92M steep ramp), Upstaza (eladocagene exuparvovec AAV gene therapy AADC deficiency; EU 2022 + US Nov 2024) + Tegsedi/Waylivra small. PIPELINE: PTC518/votoplam (huntingtin lowering oral splice modulator) -- NOVARTIS Dec 2 2024 deal $1.0B upfront + $1.9B milestones + 40/60 US profit share + ex-US double-digit royalties; PIVOT-HD 24-mo data Apr 2026 showed 52% slowing of disease progression. Vatiquinone (Friedreich ataxia) -- FDA CRL Aug 19 2025; additional adequate study needed."),
        ("yahooTicker", "PTCT"),
    )

    assets = []

    # Translarna - declining EU only post EMA non-renewal
    assets.append(asset(
        "translarna", "Translarna (ataluren) - nonsense-mutation read-through for nmDMD",
        "Commercial-declining (EMA CHMP non-renewal Apr 2025; EU residual wind-down; US NDA withdrawn)",
        "small_molecule.various.readthrough_agent",
        [innov_ind("nmdmd", "Nonsense-mutation Duchenne muscular dystrophy (EU only)",
                   "musculoskeletal.neuromuscular.dmd_nonsense",
                   regions((1, 1, 0.1), (3, 70, 200), (15, 18, 50)),
                   slice_((0, 0, 0), (40, 60, 200), (5, 18, 40)),
                   {"eu.priceK": "Translarna EU WAC ~$200K/yr (~13% nmDMD subset of DMD; 1L approved)",
                    "eu.reachPct": "EMA non-renewal Apr 2025 -- existing patients only; commercial wind-down"},
                   salesM=235, salesYear=2025, peakYear=2025, cagrPct=-40, penPct=25)]))

    # Emflaza - generics LOE
    assets.append(asset(
        "emflaza", "Emflaza (deflazacort) - corticosteroid for DMD (generics post-LOE)",
        "Commercial-declining (deflazacort generics post-LOE; was $207M FY24 -> $146M FY25)",
        "small_molecule.steroid.glucocorticoid",
        [innov_ind("dmd_steroid", "Duchenne muscular dystrophy corticosteroid (residual brand post-LOE)",
                   "musculoskeletal.neuromuscular.dmd",
                   regions((20, 70, 30), (30, 60, 18), (120, 18, 6)),
                   slice_((10, 50, 30), (3, 40, 18), (0.3, 18, 6)),
                   {"us.priceK": "Emflaza WAC ~$30K/yr; generics taking share"},
                   salesM=146, salesYear=2025, peakYear=2025, cagrPct=-25, penPct=20)]))

    # Evrysdi royalty - sold to Royalty Pharma Dec 2025; $150M retained earnout
    assets.append(asset(
        "evrysdi_royalty", "Evrysdi (risdiplam) - SMA splice modulator; PTC retains $150M earnout if Roche Evrysdi hits $2.5B (royalty stream sold to Royalty Pharma Dec 2025)",
        "Commercial royalty (Roche partnership; royalty SOLD to Royalty Pharma Dec 2025 for $240M + $60M; PTC retained $150M Roche milestone right)",
        "small_molecule.various.splice_modulator",
        [innov_ind("sma_evrysdi", "Spinal muscular atrophy (SMN2 splice modifier; oral)",
                   "musculoskeletal.neuromuscular.sma",
                   regions((1, 1, 0.1), (1, 1, 0.1), (1, 50, 0.1)),
                   slice_((0, 0, 0), (0, 0, 0), (5, 50, 0.1)),
                   {"row.priceK": "PTC retained earnout: $150M one-time if Evrysdi hits $2.5B annual; otherwise zero recurring"},
                   salesM=244, salesYear=2025, peakYear=2026, cagrPct=-50, penPct=20,
                   generic_bucket=True)]))

    # Sephience - PKU launch Jul 2025
    assets.append(asset(
        "sephience", "Sephience (sepiapterin) - oral synthetic BH4 precursor for phenylketonuria (PKU)",
        "Commercial (FDA Jul 2025; EU earlier 2025; FY25 $111M of which Q4'25 alone $92M steep ramp)",
        "small_molecule.cofactor.bh4_precursor",
        [innov_ind("pku", "Phenylketonuria (PAH deficiency; alternative to Kuvan/sapropterin)",
                   "endocrine.metabolic.pku",
                   regions((50, 80, 60), (75, 70, 35), (300, 18, 8)),
                   slice_((20, 65, 80), (8, 55, 50), (0.5, 18, 12)),
                   {"us.reachPct": "Sephience BH4-responsive PKU (improved efficacy + dosing convenience vs Kuvan generics)",
                    "us.priceK": "Sephience WAC ~$80K/yr"},
                   salesM=111, salesYear=2025, peakYear=2030, cagrPct=80, penPct=22)]))

    # Upstaza - AAV gene therapy AADC
    assets.append(asset(
        "upstaza", "Upstaza (eladocagene exuparvovec) - AAV2 gene therapy for AADC deficiency",
        "Commercial (EU 2022; FDA Nov 2024; one-time direct intracerebral infusion)",
        "gene_therapy.aav.aav2_aadc",
        [innov_ind("aadc_def", "AADC deficiency (rare ultra-orphan pediatric; AAV gene therapy)",
                   "rare_disease.metabolic.aadc_deficiency",
                   regions((0.5, 80, 1500), (0.8, 70, 800), (3, 18, 200)),
                   slice_((40, 70, 1500), (15, 60, 800), (1, 18, 200)),
                   {"us.priceK": "Upstaza WAC $3.4M one-time (similar to Zolgensma scale)",
                    "us.reachPct": "Upstaza first AADC gene therapy; ultra-orphan ~30 patients/yr globally"},
                   salesM=15, salesYear=2025, peakYear=2030, cagrPct=30, penPct=15)]))

    # Heritage tail (Tegsedi, Waylivra, others)
    assets.append(asset(
        "ptct_heritage", "PTC Therapeutics heritage portfolio (Tegsedi inotersen, Waylivra volanesorsen, Emflaza JIA, others)",
        "Commercial (Akcea/Ionis legacy; small contribution)",
        "nucleic_acid.aso.various",
        [innov_ind("ptct_heritage_tail", "Tegsedi/Waylivra inherited Akcea/Ionis ASO portfolio (peripheral neuropathy ATTR + FCS)",
                   "_established_products.ptct_heritage",
                   regions((1, 1, 0.1), (1, 1, 0.1), (5, 50, 0.1)),
                   slice_((0, 0, 0), (0, 0, 0), (10, 50, 0.1)),
                   {"row.priceK": "Bucket avg ~$200K/yr blended"},
                   salesM=70, salesYear=2025, peakYear=2026, cagrPct=-10, penPct=20,
                   generic_bucket=True)]))

    # PTC518 / votoplam - Novartis HD partnership
    assets.append(asset(
        "ptc518", "PTC518 / votoplam (huntingtin lowering oral splice modulator; Novartis Dec 2024 deal $1B+$1.9B)",
        "Phase 3 (PIVOT-HD 24-mo Apr 2026: 52% slowing of disease progression; Novartis ex-US + 40/60 US profit split)",
        "small_molecule.various.splice_modulator",
        [innov_ind("hd_votoplam", "Huntington's disease (huntingtin protein lowering; oral)",
                   "cns.neurodegeneration.huntington",
                   regions((30, 80, 50), (45, 70, 30), (150, 18, 8)),
                   slice_((30, 60, 100), (15, 50, 60), (1, 18, 15)),
                   {"us.reachPct": "PTC518 first oral huntingtin-lowering; vs ASO competitors (uniQure AMT-130, Roche tominersen)",
                    "us.priceK": "Estimated WAC $100K/yr"},
                   peakYear=2032, cagrPct=0, penPct=20)]))

    # Vatiquinone - post FDA CRL Aug 2025; deprioritized
    assets.append(asset(
        "vatiquinone", "Vatiquinone (15-LO inhibitor) - mitochondrial disease + Friedreich ataxia",
        "Phase 3 (FDA CRL Aug 19 2025 -- additional adequate/well-controlled study needed; resubmission TBD)",
        "small_molecule.enzyme.lipoxygenase_inhibitor",
        [innov_ind("fa_vatiquinone", "Friedreich ataxia (mitochondrial dysfunction; vs Skyclarys omaveloxolone)",
                   "cns.neurodegeneration.friedreich",
                   regions((5, 80, 50), (7, 70, 30), (25, 18, 8)),
                   slice_((5, 50, 60), (2, 40, 40), (0.1, 18, 10)),
                   {"us.priceK": "Estimated WAC $60K/yr if eventually approved (vs Skyclarys $370K)"},
                   peakYear=2033, cagrPct=0, penPct=8)]))

    weights = {"mega_bear": 12, "bear": 25, "base": 35, "bull": 22, "psychedelic_bull": 6}
    # Recurring revenue ex-Novartis-upfront ~$830M FY25; FY26 expects ~$700M
    # (Translarna decline + Sephience ramp ~ flat); commercialMult premium for rare
    crev = {"mega_bear": 600, "bear": 700, "base": 800, "bull": 950, "psychedelic_bull": 1200}
    cmult = {"mega_bear": 2.5, "bear": 3.5, "base": 5, "bull": 7, "psychedelic_bull": 10}
    pmult = {"mega_bear": 3, "bear": 4, "base": 6, "bull": 9, "psychedelic_bull": 14}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}
    # Big milestones potential: $1.9B Novartis + $150M Royalty Pharma earnout
    milestones = {"mega_bear": 0, "bear": 100, "base": 300, "bull": 750, "psychedelic_bull": 1500}

    asset_inds = [
        ("translarna", ["nmdmd"]),
        ("emflaza", ["dmd_steroid"]),
        ("evrysdi_royalty", ["sma_evrysdi"]),
        ("sephience", ["pku"]),
        ("upstaza", ["aadc_def"]),
        ("ptct_heritage", ["ptct_heritage_tail"]),
    ]

    pos_grid = {
        "ptc518":      {"mega_bear": 30, "bear": 50, "base": 70, "bull": 85, "psychedelic_bull": 93},
        "vatiquinone": {"mega_bear": 5,  "bear": 12, "base": 25, "bull": 40, "psychedelic_bull": 55},
    }
    apr_default = {"mega_bear": 60, "bear": 75, "base": 85, "bull": 92, "psychedelic_bull": 96}
    pen_default = {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25}

    pipeline_asmps = {}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "ptc518": OrderedDict([("hd_votoplam", od(("pos", pos_grid["ptc518"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
            "vatiquinone": OrderedDict([("fa_vatiquinone", od(("pos", pos_grid["vatiquinone"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps,
                                     milestones=milestones)

    catalysts = [
        od(("date", "Apr 2026"), ("dateSort", "2026-04-30"), ("asset", "ptc518"),
           ("indication", "hd_votoplam"),
           ("title", "PIVOT-HD 24-mo data: 52% slowing of disease progression (votoplam HD)"),
           ("type", "phase2_data"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "PTC Apr 2026 PR"), ("_confidence", "high")),
        od(("date", "H2 2026"), ("dateSort", "2026-09-30"), ("asset", "ptc518"),
           ("indication", "hd_votoplam"),
           ("title", "PTC518 PIVOT-HD Ph3 enrollment progress + Novartis ex-US development"),
           ("type", "phase3_start"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Novartis Dec 2024 deal"), ("_confidence", "medium")),
        od(("date", "2026-2027"), ("dateSort", "2027-06-30"), ("asset", "sephience"),
           ("indication", "pku"),
           ("title", "Sephience PKU US/EU launch trajectory + label expansions"),
           ("type", "launch"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "PTC FY25 IR"), ("_confidence", "high")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


# ============================================================
# TGTX - TG Therapeutics
# ============================================================

def build_TGTX():
    co = od(
        ("ticker", "TGTX"),
        ("name", "TG Therapeutics, Inc."),
        ("currentPrice", 33.78),
        ("sharesOut", 147.7),
        ("cash", 200),  # $199.5M Dec 2025 net cash; new $100M buyback authorized
        ("currency", "USD"),
        ("phase", "commercial"),
        ("subtitle", "Briumvi anti-CD20 MS pure-play. FY25 revenue $616.3M (+vs $239M FY24): Briumvi US net $594.1M (Q4'25 $182.7M +92% YoY) + Briumvi ex-US Neuraxpharm supply $12.8M + license/royalty ~$9M. FY26 guidance $875-900M total (Briumvi US $825-850M). Differentiator: 1-hour rapid IV infusion (vs Ocrevus 2.5-4hr), twice-yearly maintenance. Competing in $10B+ MS B-cell-depleter market vs Roche Ocrevus ($7B+) + Novartis Kesimpta SC ($3B+). Two consecutive $100M buybacks (Q3 2025 completed at $28.55 avg + Q1 2026 new authorization). Neuraxpharm ex-US deal: $140M up + $12.5M first launch + up to $492.5M milestones + royalties. PIPELINE: SC Briumvi Ph3 enrollment complete Apr 15 2026 (PK non-inferiority RMS, every 8w/12w dosing; topline YE2026/early 2027; potential approval 2028); azer-cel allogeneic CD19 CAR-T (Precision Bio license; Ph1 MS + autoimmune neuro)."),
        ("yahooTicker", "TGTX"),
    )

    assets = []

    # Briumvi - flagship anti-CD20 MS
    assets.append(asset(
        "briumvi", "Briumvi (ublituximab-xiiy) - glycoengineered anti-CD20 mAb for relapsing MS (1-hour IV infusion; q6mo maintenance)",
        "Commercial (FDA Dec 2022; EU 2023 via Neuraxpharm)",
        "antibody.monoclonal.anti_cd20",
        [innov_ind("rms_briumvi", "Relapsing multiple sclerosis (RMS) anti-CD20 (vs Ocrevus + Kesimpta)",
                   "immunology.demyelinating.multiple_sclerosis",
                   regions((900, 60, 60), (1500, 40, 35), (1500, 12, 10)),
                   slice_((4, 60, 65), (1, 50, 35), (0.1, 12, 10)),
                   {"us.reachPct": "Briumvi ~6-8% RMS B-cell-depleter share vs Ocrevus (~$7B), Kesimpta (~$3B), Tysabri legacy",
                    "us.priceK": "Briumvi WAC ~$65K/yr (12% discount vs Ocrevus; 1-hr infusion advantage)"},
                   salesM=607, salesYear=2025, peakYear=2030, cagrPct=25, penPct=20)],
        targets=["MS4A1"]))

    # SC Briumvi - Ph3 enrollment complete Apr 2026
    assets.append(asset(
        "briumvi_sc", "SC Briumvi - subcutaneous formulation (q8w/q12w dosing)",
        "Phase 3 (enrollment complete Apr 15 2026; PK non-inferiority RMS; topline YE2026/early 2027; potential approval 2028)",
        "antibody.monoclonal.anti_cd20",
        [innov_ind("rms_briumvi_sc", "RMS subcutaneous anti-CD20 (less frequent dosing vs IV)",
                   "immunology.demyelinating.multiple_sclerosis",
                   regions((900, 60, 60), (1500, 40, 35), (1500, 12, 10)),
                   slice_((2.5, 55, 55), (0.6, 45, 32), (0.05, 10, 8)),
                   {"us.priceK": "Estimated SC WAC $55K/yr (parity with IV; net of SC convenience premium)",
                    "us.reachPct": "SC Briumvi extends franchise; ~2.5% incremental MS B-cell-depleter share via dosing convenience vs Kesimpta SC"},
                   peakYear=2032, cagrPct=15, penPct=15)]))

    # Azer-cel - allogeneic CD19 CAR-T MS Ph1
    assets.append(asset(
        "azer_cel", "Azer-cel (azercabtagene zapreleucel) - allogeneic CD19 CAR-T (Precision Bio license)",
        "Phase 1 MS + autoimmune neuro (IND clearance 2025)",
        "cell_therapy.car_t.allogeneic_cd19",
        [innov_ind("ms_azercel", "MS + autoimmune neuro indications (allogeneic CAR-T potential one-time treatment)",
                   "immunology.demyelinating.multiple_sclerosis",
                   regions((900, 60, 60), (1500, 40, 35), (1500, 12, 10)),
                   slice_((0.3, 50, 150), (0.1, 40, 100), (0.02, 12, 40)),
                   {"us.priceK": "Estimated WAC $250K one-time CAR-T (vs $400K+ branded autologous)",
                    "us.reachPct": "Allogeneic off-the-shelf for autoimmune; novel approach"},
                   peakYear=2034, cagrPct=0, penPct=8)]))

    # SOTP scenarios
    weights = {"mega_bear": 10, "bear": 22, "base": 38, "bull": 25, "psychedelic_bull": 5}
    # FY26 guide $875-900M; FY27 expects ~$1.1B with SC ramp + label expansion
    # TGTX market cap ~$5.0B (33.78 × 147.7M); FY26 guide $875-900M; trades ~5.5x EV/sales
    crev = {"mega_bear": 800, "bear": 900, "base": 1050, "bull": 1300, "psychedelic_bull": 1700}
    cmult = {"mega_bear": 2.5, "bear": 3.5, "base": 5, "bull": 7, "psychedelic_bull": 10}
    pmult = {"mega_bear": 2, "bear": 3, "base": 5, "bull": 7, "psychedelic_bull": 11}
    pdr = {"mega_bear": 10, "bear": 9, "base": 8, "bull": 7, "psychedelic_bull": 6}

    asset_inds = [("briumvi", ["rms_briumvi"])]

    pos_grid = {
        "briumvi_sc": {"mega_bear": 60, "bear": 75, "base": 88, "bull": 95, "psychedelic_bull": 99},
        "azer_cel":   {"mega_bear": 8,  "bear": 18, "base": 32, "bull": 48, "psychedelic_bull": 65},
    }
    apr_default = {"mega_bear": 65, "bear": 78, "base": 88, "bull": 93, "psychedelic_bull": 97}
    pen_default = {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25}

    pipeline_asmps = {}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "briumvi_sc": OrderedDict([("rms_briumvi_sc", od(("pos", pos_grid["briumvi_sc"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
            "azer_cel": OrderedDict([("ms_azercel", od(("pos", pos_grid["azer_cel"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "Apr 15 2026"), ("dateSort", "2026-04-15"), ("asset", "briumvi_sc"),
           ("indication", "rms_briumvi_sc"),
           ("title", "SC Briumvi Ph3 enrollment complete (PK non-inferiority RMS)"),
           ("type", "phase3_start"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "TGTX Apr 15 2026 PR"), ("_confidence", "high")),
        od(("date", "YE 2026"), ("dateSort", "2026-12-15"), ("asset", "briumvi_sc"),
           ("indication", "rms_briumvi_sc"),
           ("title", "SC Briumvi Ph3 PK non-inferiority topline (YE2026/early 2027)"),
           ("type", "phase3_data"), ("binary", True),
           ("fail_pos", 60), ("fail_apr", 80), ("success_pos", 92), ("success_apr", 95),
           ("_source", "TGTX pipeline"), ("_confidence", "medium")),
        od(("date", "2027"), ("dateSort", "2027-06-30"), ("asset", "briumvi"),
           ("indication", "rms_briumvi"),
           ("title", "Briumvi label expansions (frontline 1L + pediatric); EU launches via Neuraxpharm"),
           ("type", "label_expansion"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "TGTX pipeline + Neuraxpharm"), ("_confidence", "medium")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


# ============================================================
# CHRS - Coherus Oncology (post-divestments pure IO play)
# ============================================================

def build_CHRS():
    co = od(
        ("ticker", "CHRS"),
        ("name", "Coherus Oncology, Inc."),
        ("currentPrice", 1.66),
        ("sharesOut", 121),
        # Pro-forma ~$200M cash post Udenyca close Apr 2025; debt cut from $480M to $38.8M
        ("cash", 161),
        ("currency", "USD"),
        ("phase", "commercial"),
        ("subtitle", "Pure-play IO (rebranded 'Coherus Oncology' post-divestments). FY25 revenue mostly Loqtorzi $40.8M (toripalimab; PD-1 mAb licensed from Junshi for North America; FDA Oct 2023 NPC + frontline NSCLC + ESCC label expansion; +114% vs $19.1M FY24). Major restructuring 2024-2025: Cimerli (ranibizumab biosim) sold to Sandoz Mar 2024 ~$170M; Yusimry (adalimumab biosim) divested 2024; Udenyca (pegfilgrastim biosim) sold to Intas/Accord Apr 11 2025 for $483M up + $75M milestones. Convertible/secured debt cut ~90% from $480M to $38.8M YE2025. ~30% headcount reduction Apr 2025. PIPELINE: Casdozokitug (CHS-388) anti-IL-27 mAb (Surface Oncology acq Sept 2023) -- Ph2 HCC ASCO-GI 2025 ORR 38% / CR 17.2% in combo with atezo+bev; also Ph2 NSCLC. CHS-114 selective anti-CCR8 cytolytic mAb (Treg-depleting) -- Ph1b/2a HNSCC + gastric (combo with toripalimab); HNSCC dose-opt data H1 2026 KEY CATALYST. CHS-1000 anti-ILT4 (LILRB2) IND cleared Q2 2024."),
        ("yahooTicker", "CHRS"),
    )

    assets = []

    # Loqtorzi (toripalimab)
    assets.append(asset(
        "loqtorzi", "Loqtorzi (toripalimab) - anti-PD-1 mAb (Junshi license for North America)",
        "Commercial (FDA Oct 2023 NPC + frontline NSCLC + ESCC; FY25 $40.8M +114% YoY; Junshi originator)",
        "antibody.monoclonal.anti_pd1",
        [
            innov_ind("npc_io", "Nasopharyngeal carcinoma 1L+ (combo gemcitabine/cisplatin); FDA Oct 2023",
                      "oncology.head_neck.npc",
                      regions((1, 80, 200), (2, 70, 130), (10, 18, 35)),
                      slice_((40, 60, 200), (15, 50, 130), (1, 18, 35)),
                      {"us.reachPct": "Loqtorzi ~30% NPC US share (post Junshi-derived FDA approval)",
                       "us.priceK": "Loqtorzi WAC ~$200K/yr (parallel to Keytruda/Opdivo)"},
                      salesM=25, salesYear=2025, peakYear=2030, cagrPct=30, penPct=22),
            innov_ind("nsclc_io", "NSCLC + ESCC + other label expansions (frontline IO combo)",
                      "oncology.lung.nsclc_io",
                      regions((500, 80, 150), (700, 70, 100), (3000, 12, 30)),
                      slice_((0.4, 50, 150), (0.2, 50, 100), (0.05, 12, 30)),
                      {"us.priceK": "Loqtorzi NSCLC + ESCC WAC ~$150K/yr blended",
                       "us.reachPct": "Niche post-Keytruda/Opdivo entry; ~1% NSCLC IO share"},
                      salesM=16, salesYear=2025, peakYear=2031, cagrPct=40, penPct=15),
        ],
        targets=["PDCD1"]))

    # Casdozokitug - anti-IL-27 (Surface Oncology origin)
    assets.append(asset(
        "casdozokitug", "Casdozokitug (CHS-388) - anti-IL-27 mAb (Surface Oncology acq Sept 2023)",
        "Phase 2 (HCC ORR 38% CR 17.2% ASCO-GI 2025 in combo with atezo+bev; NSCLC Ph2 ongoing)",
        "antibody.monoclonal.anti_il27",
        [innov_ind("hcc_casdozo", "Hepatocellular carcinoma (1L combo with atezolizumab + bevacizumab)",
                   "oncology.gi.hcc",
                   regions((25, 70, 150), (40, 60, 90), (300, 18, 25)),
                   slice_((1.5, 50, 100), (0.6, 40, 70), (0.1, 18, 18)),
                   {"us.priceK": "Estimated WAC $100K/yr (combo with atezo+bev)",
                    "us.reachPct": "Casdozo HCC niche; first-in-class IL-27 mAb but small player vs IO duopolists"},
                   peakYear=2032, cagrPct=0, penPct=10)]))

    # CHS-114 - selective anti-CCR8 (Treg-depleting); H1 2026 catalyst
    assets.append(asset(
        "chs_114", "CHS-114 - selective anti-CCR8 cytolytic mAb (Treg-depleting; tumor-restricted)",
        "Phase 1b/2a HNSCC + gastric (combo with toripalimab); HNSCC dose-opt data H1 2026",
        "antibody.monoclonal.anti_ccr8",
        [innov_ind("hnscc_ccr8", "HNSCC + gastric (post-PD-1 progression; CCR8-selective Treg depletion)",
                   "oncology.head_neck.hnscc",
                   regions((30, 80, 100), (45, 70, 65), (250, 18, 18)),
                   slice_((1.0, 45, 80), (0.4, 35, 55), (0.05, 18, 15)),
                   {"us.priceK": "Estimated WAC $100K/yr (combo with PD-1)",
                    "us.reachPct": "CHS-114 vs other CCR8 programs (Bristol BMS-986340, Pfizer-Sanofi)"},
                   peakYear=2033, cagrPct=0, penPct=10)]))

    # CHS-1000 - anti-ILT4 (LILRB2)
    assets.append(asset(
        "chs_1000", "CHS-1000 - anti-ILT4 (LILRB2) mAb (myeloid checkpoint)",
        "Pre-clinical/Ph1 (IND cleared Q2 2024; FIH gated on portfolio prioritization)",
        "antibody.monoclonal.anti_ilt4",
        [innov_ind("solid_ilt4", "Solid tumors (myeloid checkpoint; ILT4/LILRB2)",
                   "oncology.multi_tumor_io.pd1_pdl1_eligible",
                   regions((500, 80, 150), (700, 70, 100), (3000, 12, 30)),
                   slice_((0.5, 50, 100), (0.2, 40, 70), (0.02, 12, 25)),
                   {"us.priceK": "Estimated WAC $100K/yr in IO combo"},
                   peakYear=2034, cagrPct=0, penPct=6)]))

    # Distressed micro-cap ~$200M mcap; market deeply skeptical of pipeline.
    # Heavily down-weight bullish scenarios and slash multiples.
    weights = {"mega_bear": 25, "bear": 30, "base": 25, "bull": 15, "psychedelic_bull": 5}
    # FY25 Loqtorzi $41M; FY26 expects $60-80M; pure pipeline-anchored
    crev = {"mega_bear": 50, "bear": 70, "base": 90, "bull": 130, "psychedelic_bull": 200}
    cmult = {"mega_bear": 0.5, "bear": 1.2, "base": 2.5, "bull": 4, "psychedelic_bull": 6}
    pmult = {"mega_bear": 1, "bear": 1.5, "base": 2.5, "bull": 4, "psychedelic_bull": 7}
    pdr = {"mega_bear": 16, "bear": 14, "base": 12, "bull": 10, "psychedelic_bull": 8}
    milestones = {"mega_bear": 0, "bear": 0, "base": 10, "bull": 30, "psychedelic_bull": 100}

    asset_inds = [("loqtorzi", ["npc_io", "nsclc_io"])]

    pos_grid = {
        "casdozokitug": {"mega_bear": 12, "bear": 22, "base": 38, "bull": 55, "psychedelic_bull": 70},
        "chs_114":      {"mega_bear": 8,  "bear": 18, "base": 32, "bull": 48, "psychedelic_bull": 65},
        "chs_1000":     {"mega_bear": 4,  "bear": 10, "base": 22, "bull": 38, "psychedelic_bull": 55},
    }
    apr_default = {"mega_bear": 55, "bear": 70, "base": 82, "bull": 90, "psychedelic_bull": 95}
    pen_default = {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25}

    pipeline_asmps = {}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "casdozokitug": OrderedDict([("hcc_casdozo", od(("pos", pos_grid["casdozokitug"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
            "chs_114": OrderedDict([("hnscc_ccr8", od(("pos", pos_grid["chs_114"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
            "chs_1000": OrderedDict([("solid_ilt4", od(("pos", pos_grid["chs_1000"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps,
                                     milestones=milestones)

    catalysts = [
        od(("date", "H1 2026"), ("dateSort", "2026-06-30"), ("asset", "chs_114"),
           ("indication", "hnscc_ccr8"),
           ("title", "CHS-114 (anti-CCR8) HNSCC dose-opt data + toripalimab combo (KEY CATALYST)"),
           ("type", "phase2_data"), ("binary", True),
           ("fail_pos", 8), ("fail_apr", 50), ("success_pos", 50), ("success_apr", 80),
           ("_source", "Coherus Oncology pipeline; CHS-114 program"), ("_confidence", "low")),
        od(("date", "Q4 2026"), ("dateSort", "2026-12-15"), ("asset", "loqtorzi"),
           ("indication", "nsclc_io"),
           ("title", "Loqtorzi NSCLC + ESCC label expansion ramp; FY26 guide $60-80M"),
           ("type", "milestone"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Coherus IR"), ("_confidence", "medium")),
        od(("date", "2027"), ("dateSort", "2027-06-30"), ("asset", "casdozokitug"),
           ("indication", "hcc_casdozo"),
           ("title", "Casdozokitug HCC pivotal Ph3 design / NSCLC Ph2 readout"),
           ("type", "phase2_data"), ("binary", True),
           ("fail_pos", 12), ("fail_apr", 60), ("success_pos", 50), ("success_apr", 85),
           ("_source", "Coherus pipeline"), ("_confidence", "low")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


def main():
    write_config("PTCT", build_PTCT())
    write_config("TGTX", build_TGTX())
    write_config("CHRS", build_CHRS())

    manifest_path = CONFIGS / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for tk in ["PTCT", "TGTX", "CHRS"]:
        if tk not in manifest:
            manifest.append(tk)
    manifest = sorted(set(manifest))
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"\n  manifest -> {len(manifest)} tickers")


if __name__ == "__main__":
    main()
