# -*- coding: utf-8 -*-
"""Build configs for GLPG (Galapagos) + IDIA (Idorsia) EU specialty biotechs.

Both EU-domiciled specialty biotechs in restructuring mode:
- GLPG: Belgian; cell therapy WIND-DOWN announced Oct 2025 (SpinCo abandoned
  May 2025); now cash-rich shell (~EUR 3B) + GLPG3667 TYK2 + Jyseleca royalty
- IDIA: Swiss; heavily distressed but Quviviq (insomnia) sales doubled FY25;
  Tryvio (resistant HTN) REMS removed Mar 2025; CB restructuring Feb 2025

Run:
  py scripts/ops/build_eu_specialty.py
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
# GLPG - Galapagos NV (Belgian; cash shell + TYK2)
# ============================================================

def build_GLPG():
    co = od(
        ("ticker", "GLPG"),
        ("name", "Galapagos NV (renaming to Lakefront Biotherapeutics May 8 2026)"),
        ("currentPrice", 26.46),  # EUR Amsterdam (Mechelen HQ; primary listing GLPG.AS)
        ("sharesOut", 65.9),
        # Reported cash EUR 3.0B but market applies BD-deployment haircut.
        # Mar 2026 Gilead Ouro deal: GLPG funds 50% of $2.1B = ~$1.05B / EUR 970M
        # capital deployment now committed. Credited cash post deployment: EUR 1,700M.
        ("cash", 1700),  # EUR M
        ("currency", "EUR"),
        ("phase", "phase3"),
        ("subtitle", "Belgian biotech transformed to BD shell (renaming Lakefront Biotherapeutics May 8 2026). SpinCo split scrapped May 2025; cell therapy entirely WOUND DOWN (implementation began Jan 2026; no buyer found). Headcount targeting ~35-40 employees by end-2026. Reported cash EUR 3.0B YE25 (vs EUR 1.74B mcap). MARCH 2026: GLPG funds 50% of Gilead's $2.1B Ouro Medicines acquisition (~$1.05B / EUR 970M deployment in T-cell engagers). FY25 operating profit EUR 295M (vs -EUR 188M FY24; driven by Gilead deferred income release). Lead remaining: GLPG3667 selective TYK2 -- Phase 3-enabling topline DEC 18 2025: dermatomyositis HIT primary (p=0.0848, borderline; ARGX Vyvgart ALKIVIA competition), SLE MISSED primary (Wk48 final Q2 2026); only remaining immunology asset. Jyseleca royalty (Alfasigma Jan 2024; mid-single to mid-double-digit). GLPG5101 CD19 CAR-T (ATALANTA-1 MCL 100% ORR ASH 2025) terminal: no buyer, winding down."),
        ("yahooTicker", "GLPG.AS"),
    )

    assets = []

    # GLPG3667 - lead remaining asset (TYK2); readouts Dec 18 2025
    assets.append(asset(
        "glpg3667", "GLPG3667 - selective TYK2 inhibitor (oral; deuterium-modified pseudokinase domain selective)",
        "Phase 3 design pending (Ph2 dermatomyositis HIT primary p=0.0848 borderline Dec 2025; SLE MISSED primary; SLE Wk48 final Q2 2026)",
        "small_molecule.kinase.tyk2",
        [
            innov_ind("sle_3667", "Systemic lupus erythematosus moderate-severe (Ph2 missed primary 2025; Ph3 design pending)",
                      "immunology.autoimmune.sle",
                      regions((350, 75, 25), (450, 60, 12), (2000, 20, 3)),
                      slice_((1.5, 40, 25), (0.5, 30, 15), (0.05, 12, 5)),
                      {"us.priceK": "Estimated WAC $25K/yr (oral TYK2 in SLE; vs Saphnelo IV)",
                       "us.reachPct": "Niche oral TYK2 SLE entry post Ph2 miss"},
                      peakYear=2032, cagrPct=0, penPct=8),
            innov_ind("dermatomyositis_3667", "Dermatomyositis (Ph2 hit primary 2025; differentiated indication)",
                      "immunology.autoimmune.dermatomyositis",
                      regions((40, 70, 20), (60, 55, 12), (200, 18, 4)),
                      slice_((6, 50, 20), (3, 40, 12), (0.3, 18, 4)),
                      {"us.priceK": "Estimated WAC $20K/yr",
                       "us.reachPct": "First oral TYK2 in DM if Ph3 succeeds; competing with ARGX Vyvgart ALKIVIA"},
                      peakYear=2033, cagrPct=0, penPct=15),
        ]))

    # Jyseleca royalty stream from Alfasigma (post Jan 2024 transfer)
    assets.append(asset(
        "jyseleca_royalty", "Jyseleca (filgotinib) - JAK1 selective inhibitor; royalty stream from Alfasigma EU (sold Jan 2024)",
        "Commercial royalty (sold to Alfasigma Jan 2024; mid-single to mid-double-digit royalty on EU sales + EUR 120M sales milestones)",
        "small_molecule.kinase.jak1",
        [innov_ind("ra_uc_royalty", "RA + UC royalty stream (JAK1; EU only via Alfasigma)",
                   "immunology.inflammatory_systemic.rheumatoid_arthritis",
                   regions((1300, 60, 35), (2000, 50, 22), (10000, 8, 6)),
                   slice_((0, 0, 0), (0.3, 40, 5), (0, 0, 0)),
                   {"eu.priceK": "Galapagos blended royalty proxy ~EUR 5K/yr-equivalent",
                    "eu.reachPct": "Jyseleca ~3-5% EU JAK1 share; Galapagos receives mid-teens royalty"},
                   salesM=30, salesYear=2025, peakYear=2028, cagrPct=5, penPct=20)]))

    # CAR-T residual: WIND-DOWN implementation Jan 2026; no buyer found; terminal value ~zero
    assets.append(asset(
        "glpg5101", "GLPG5101 - CD19 CAR-T (Cellpoint decentralized 7-day vein-to-vein platform)",
        "Wind-down implementation Jan 2026 (no buyer/licensee found; ATALANTA-1 MCL ASH 2025 100% ORR / 96% CR data + FDA RMAT not monetized)",
        "cell_therapy.car_t.cd19",
        [innov_ind("mcl_cart", "Mantle cell lymphoma R/R (post-BTKi); also NHL DLBCL/FL",
                   "oncology.hematology.nhl.mcl",
                   regions((4, 80, 400), (6, 70, 280), (25, 18, 80)),
                   slice_((5, 50, 350), (3, 40, 250), (0.3, 18, 70)),
                   {"us.priceK": "Estimated WAC $350K one-time CAR-T",
                    "us.reachPct": "Niche post-BTKi MCL CAR-T (vs Tecartus, Carvykti adjacent)"},
                   peakYear=2033, cagrPct=0, penPct=10)]))

    # Non-SOTP scenarios -- cash-anchored shell
    # Mcap ~EUR 1.9B (29 × 65.9M); cash EUR 3B → negative implied EV
    weights = {"mega_bear": 12, "bear": 25, "base": 38, "bull": 20, "psychedelic_bull": 5}

    SCEN = ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]
    pos_grid = {
        # GLPG3667: Ph2 already readout (DM hit borderline, SLE missed); Ph3 design risk
        "glpg3667": {"mega_bear": 30, "bear": 45, "base": 60, "bull": 75, "psychedelic_bull": 85},
        # GLPG5101 CAR-T: wind-down, no buyer; near-zero terminal value
        "glpg5101": {"mega_bear": 1, "bear": 3, "base": 8, "bull": 18, "psychedelic_bull": 35},
    }
    apr_grid = {a: {"mega_bear": 60, "bear": 75, "base": 85, "bull": 92, "psychedelic_bull": 96} for a in pos_grid}
    pen_grid = {a: {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25} for a in pos_grid}
    ind_map_3667 = ["sle_3667", "dermatomyositis_3667"]

    # Non-SOTP: pipeline NPV + cash + small Jyseleca commercial royalty
    mult = {"mega_bear": 1.0, "bear": 2.0, "base": 4.0, "bull": 7.0, "psychedelic_bull": 12.0}
    dr =   {"mega_bear": 14, "bear": 12, "base": 10, "bull": 8, "psychedelic_bull": 7}
    cannib = {"mega_bear": 5, "bear": 3, "base": 1, "bull": 0, "psychedelic_bull": 0}

    scenarios = od()
    for sk in SCEN:
        asmps = od()
        # Jyseleca royalty: inert commercial assumption
        asmps["jyseleca_royalty"] = od(("ra_uc_royalty", od(("pos", 100), ("apr", 100), ("pen", 1))))
        # GLPG3667 multi-indication
        asmps["glpg3667"] = od()
        for iid in ind_map_3667:
            asmps["glpg3667"][iid] = od(
                ("pos", pos_grid["glpg3667"][sk]),
                ("apr", apr_grid["glpg3667"][sk]),
                ("pen", pen_grid["glpg3667"][sk]),
            )
        # GLPG5101 CAR-T (deeply discounted given wind-down)
        asmps["glpg5101"] = od(("mcl_cart", od(
            ("pos", pos_grid["glpg5101"][sk]),
            ("apr", apr_grid["glpg5101"][sk]),
            ("pen", pen_grid["glpg5101"][sk]),
        )))
        scenarios[sk] = od(
            ("wt", weights[sk]),
            ("val", od(
                ("mult", mult[sk]),
                ("dr", dr[sk]),
                ("cannib", cannib[sk]),
            )),
            ("assumptions", asmps),
        )

    catalysts = [
        od(("date", "Mar 2026"), ("dateSort", "2026-03-15"), ("asset", "glpg3667"),
           ("indication", "sle_3667"),
           ("title", "Gilead Ouro 50% co-investment ($1.05B; T-cell engager pipeline addition)"),
           ("type", "m_and_a"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Galapagos Mar 2026 announcement"), ("_confidence", "high")),
        od(("date", "May 8 2026"), ("dateSort", "2026-05-08"), ("asset", "glpg3667"),
           ("indication", "sle_3667"),
           ("title", "Renaming to Lakefront Biotherapeutics (shareholder-approved)"),
           ("type", "milestone"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "GLPG 2026 AGM resolutions"), ("_confidence", "high")),
        od(("date", "Q2 2026"), ("dateSort", "2026-06-30"), ("asset", "glpg3667"),
           ("indication", "sle_3667"),
           ("title", "GLPG3667 SLE Wk48 final data (Wk32 SRI-4 missed primary Dec 2025)"),
           ("type", "phase2_data"), ("binary", True),
           ("fail_pos", 20), ("fail_apr", 60), ("success_pos", 65), ("success_apr", 85),
           ("_source", "Galapagos Dec 18 2025 disclosure"), ("_confidence", "medium")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


# ============================================================
# IDIA - Idorsia (Swiss specialty; restructuring)
# ============================================================

def build_IDIA():
    co = od(
        ("ticker", "IDIA"),
        ("name", "Idorsia Pharmaceuticals Ltd."),
        ("currentPrice", 3.79),
        ("sharesOut", 250),
        # YE2025 actual: cash CHF 89M vs total indebtedness CHF 1,342M
        # (CB residual 49M + convertible loan 335M + debt notes 753M + term loan 18M)
        # = NET DEBT CHF -1,253M. Heavy debt overhang dominates valuation.
        ("cash", -1253),  # CHF M -- per Feb 26 2026 release
        ("currency", "CHF"),
        ("phase", "commercial"),
        ("subtitle", "Swiss specialty; emerging from CB restructuring but still heavily indebted (CHF -1,253M net debt: convertible loan 335M + debt notes 753M + CB residual 49M; cash only CHF 89M YE25). FY25 revenue CHF 221M (+2x): Quviviq daridorexant DORA insomnia CHF 134M (+>130%; FY26 guide CHF 200M; EU growth driver, US softer). Tryvio aprocitentan dual ETA/ETB resistant HTN (FDA Mar 2024; REMS removed Mar 2025) immaterial sales bundled. Contract revenue CHF 79M includes $100M Viatris CLAWBACK (Viatris RETURNED selatogrel + cenerimod rights -- both assets back to Idorsia). Lucerastat oral GCS inhibitor Fabry: FDA-agreed two-trial Ph3 design Feb 2026 (vs ERT comparator Fabrazyme/Replagal). CEO Srishti Gupta resigned Mar 16 2026; founder Jean-Paul Clozel interim CEO. ~487 FTE permanent post-restructuring. Tryvio partnership search ongoing -- exclusivity collapsed Feb 2025."),
        ("yahooTicker", "IDIA.SW"),
    )

    assets = []

    # Quviviq - flagship growth driver
    assets.append(asset(
        "quviviq", "Quviviq (daridorexant) - dual orexin receptor antagonist (DORA) for insomnia",
        "Commercial (FDA Apr 2022; EU 2022; FY25 sales CHF 134M +130% YoY; FY26 guide CHF 200M)",
        "small_molecule.gpcr.orexin_antagonist",
        [innov_ind("insomnia", "Insomnia chronic adult (DORA class; vs older Z-drugs + benzodiazepines)",
                   "cns.sleep.insomnia",
                   regions((35000, 18, 1.5), (50000, 12, 0.8), (200000, 4, 0.3)),
                   slice_((0.4, 30, 4), (1.0, 35, 2.5), (0.05, 8, 1)),
                   {"us.priceK": "Quviviq US WAC ~$4K/yr (parallel to Belsomra suvorexant + Dayvigo lemborexant)",
                    "eu.reachPct": "Quviviq EU growth driver; ~1% EU insomnia Rx penetration ramping"},
                   salesM=148, salesYear=2025, peakYear=2030, cagrPct=40, penPct=20)]))

    # Tryvio - resistant HTN
    assets.append(asset(
        "tryvio", "Tryvio (aprocitentan) - dual endothelin receptor antagonist (ETA/ETB) for treatment-resistant hypertension",
        "Commercial (FDA Mar 2024; REMS removed Mar 2025; ACC/AHA HTN guidelines included; partnership search ongoing)",
        "small_molecule.gpcr.endothelin_antagonist",
        [innov_ind("resistant_htn", "Treatment-resistant hypertension (3+ antihypertensive failure; novel mechanism)",
                   "cardio_metabolic.hypertension.resistant",
                   regions((10000, 30, 5), (15000, 25, 3), (60000, 8, 1)),
                   slice_((0.3, 35, 6), (0.1, 25, 4), (0.01, 8, 1.5)),
                   {"us.priceK": "Tryvio US WAC ~$6K/yr",
                    "us.reachPct": "Tryvio first new HTN MoA in 35 yrs; niche resistant HTN ramping"},
                   salesM=15, salesYear=2025, peakYear=2032, cagrPct=80, penPct=12)]))

    # Selatogrel (P2Y12 self-admin AMI) - back in Idorsia hands post Viatris return Mar 2025
    assets.append(asset(
        "selatogrel", "Selatogrel - oral self-administered P2Y12 inhibitor for AMI patient self-injection pre-hospital",
        "Phase 3 SOS-AMI (back in Idorsia hands post Viatris return Mar 2025; SPA + Fast Track; readout 2027)",
        "small_molecule.gpcr.p2y12_antagonist",
        [innov_ind("ami_self", "Acute myocardial infarction patient self-administration (pre-hospital)",
                   "cardio_metabolic.cardiovascular.myocardial_infarction",
                   regions((1500, 80, 8), (2000, 70, 5), (8000, 30, 2)),
                   slice_((10, 50, 1.5), (5, 40, 1), (0.5, 15, 0.4)),
                   {"us.reachPct": "Niche AMI pre-hospital self-admin ~5-15%",
                    "us.priceK": "Estimated WAC $1.5K/yr if approved"},
                   peakYear=2032, cagrPct=0, penPct=12)]))

    # Cenerimod (S1P1 SLE) - back in Idorsia hands post Viatris return
    assets.append(asset(
        "cenerimod", "Cenerimod - selective S1P1 receptor modulator for SLE",
        "Phase 3 OPUS-1/OPUS-2 SLE (back in Idorsia hands post Viatris return Mar 2025; readouts 2026/27)",
        "small_molecule.gpcr.s1p1_agonist",
        [innov_ind("sle", "Systemic lupus erythematosus moderate-severe",
                   "immunology.autoimmune.sle",
                   regions((350, 75, 25), (450, 60, 12), (2000, 20, 3)),
                   slice_((4, 50, 25), (2, 40, 15), (0.3, 15, 5)),
                   {"us.reachPct": "Cenerimod novel oral S1P1 in SLE; ~5-10% SLE Rx",
                    "us.priceK": "Estimated WAC $25K/yr"},
                   peakYear=2032, cagrPct=0, penPct=10)]))

    # Lucerastat - Fabry pipeline (Ph3 design FDA-agreed Feb 2026)
    assets.append(asset(
        "lucerastat", "Lucerastat - oral glucosylceramide synthase inhibitor for Fabry disease",
        "Phase 3 (FDA-agreed design Feb 2026; substrate-reduction therapy alternative to ERT)",
        "small_molecule.enzyme.gcs_inhibitor",
        [innov_ind("fabry", "Fabry disease (alpha-galactosidase A deficiency; substrate-reduction therapy)",
                   "endocrine.lysosomal_storage.fabry",
                   regions((6, 80, 250), (10, 70, 150), (40, 18, 35)),
                   slice_((10, 50, 200), (5, 40, 120), (0.3, 18, 30)),
                   {"us.priceK": "Estimated WAC $200K/yr oral SRT (vs ERT Fabrazyme/Replagal ~$300K)",
                    "us.reachPct": "Lucerastat first oral therapy for ALL Fabry patients (vs Galafold amenable subset only); FDA-agreed two-trial design Feb 2026: baseline-controlled biopsy + ERT-comparator"},
                   peakYear=2032, cagrPct=0, penPct=12)]))

    # SOTP scenarios -- distressed but improving; high debt reflected in low multiples
    weights = {"mega_bear": 18, "bear": 28, "base": 32, "bull": 17, "psychedelic_bull": 5}
    # FY25 CHF 221M total but CHF 79M was one-time Viatris clawback contract revenue.
    # FY26: only Quviviq CHF 200M is guided; Tryvio + Viatris assets ramp 2027+
    crev = {"mega_bear": 180, "bear": 220, "base": 280, "bull": 400, "psychedelic_bull": 600}
    # Quviviq doubling FY25; Tryvio post-REMS; market trades ~5-7x EV/sales
    # (mcap ~CHF 1.07B + net debt ~CHF 450M = CHF 1.52B EV vs FY25 CHF 221M)
    cmult = {"mega_bear": 2.5, "bear": 4.0, "base": 5.5, "bull": 7.5, "psychedelic_bull": 10.0}
    pmult = {"mega_bear": 2, "bear": 3, "base": 5, "bull": 8, "psychedelic_bull": 13}
    pdr = {"mega_bear": 12, "bear": 10, "base": 8, "bull": 7, "psychedelic_bull": 6}
    milestones = {"mega_bear": 0, "bear": 50, "base": 150, "bull": 350, "psychedelic_bull": 700}

    SCEN = ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]
    pos_grid = {
        "lucerastat": {"mega_bear": 30, "bear": 50, "base": 70, "bull": 85, "psychedelic_bull": 92},
        "selatogrel": {"mega_bear": 25, "bear": 40, "base": 55, "bull": 70, "psychedelic_bull": 82},
        "cenerimod":  {"mega_bear": 20, "bear": 35, "base": 50, "bull": 65, "psychedelic_bull": 78},
    }
    apr_grid = {a: {"mega_bear": 60, "bear": 75, "base": 85, "bull": 92, "psychedelic_bull": 96} for a in pos_grid}
    pen_grid = {a: {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25} for a in pos_grid}
    ind_map = {"lucerastat": "fabry", "selatogrel": "ami_self", "cenerimod": "sle"}

    scenarios = od()
    commercial_inert = [
        ("quviviq", "insomnia"), ("tryvio", "resistant_htn"),
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
        od(("date", "Mar 16 2026"), ("dateSort", "2026-03-16"), ("asset", "quviviq"),
           ("indication", "insomnia"),
           ("title", "CEO transition: Srishti Gupta resigned; founder Jean-Paul Clozel interim CEO"),
           ("type", "milestone"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Idorsia Mar 16 2026 disclosure"), ("_confidence", "high")),
        od(("date", "2026"), ("dateSort", "2026-06-30"), ("asset", "tryvio"),
           ("indication", "resistant_htn"),
           ("title", "Tryvio aprocitentan global partnership/licensing deal (post REMS removal Mar 2025)"),
           ("type", "partnership"), ("binary", True),
           ("fail_pos", 60), ("fail_apr", 70), ("success_pos", 95), ("success_apr", 95),
           ("_source", "Idorsia FY25 release; partnership search ongoing"), ("_confidence", "medium")),
        od(("date", "Q4 2026"), ("dateSort", "2026-12-15"), ("asset", "quviviq"),
           ("indication", "insomnia"),
           ("title", "Quviviq EU sales tracking toward CHF 200M+ FY26 guide; commercial profitability"),
           ("type", "milestone"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Idorsia FY25 results"), ("_confidence", "high")),
        od(("date", "2027"), ("dateSort", "2027-06-30"), ("asset", "lucerastat"),
           ("indication", "fabry"),
           ("title", "Lucerastat Ph3 Fabry start (FDA-agreed design Feb 2026)"),
           ("type", "phase3_start"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Idorsia Feb 2026 disclosure"), ("_confidence", "high")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


def main():
    write_config("GLPG", build_GLPG())
    write_config("IDIA", build_IDIA())

    manifest_path = CONFIGS / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for tk in ["GLPG", "IDIA"]:
        if tk not in manifest:
            manifest.append(tk)
    manifest = sorted(set(manifest))
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"\n  manifest -> {len(manifest)} tickers")


if __name__ == "__main__":
    main()
