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
        ("name", "Galapagos NV"),
        ("currentPrice", 29),  # EUR Brussels (Mechelen HQ; ADR ~$33)
        ("sharesOut", 65.9),
        # Reported cash EUR 3.0B but market applies ~40% haircut on BD-deployment
        # risk (mcap EUR 1.91B vs full cash EUR 3.0B). Use credited cash EUR 1,700M
        # so mega_bear scenario lands below current price (cash-anchored shell).
        ("cash", 1700),  # EUR M -- credited cash post BD-deployment haircut
        ("currency", "EUR"),
        ("phase", "phase3"),
        ("subtitle", "Belgian biotech in radical restructuring. SpinCo split announced Jan 2025 then SCRAPPED May 2025; cell therapy entirely WOUND DOWN announced Oct 2025 (implementation Jan 2026 post works council). Now cash-rich shell: EUR 3.0B cash YE25 (vs ~EUR 2.0B mcap; deeply negative EV). FY25 revenue ~EUR 1.06B (one-time Gilead deferred income release EUR 1,069M; underlying small). FY26 guide: cash flow neutral-to-positive ex-BD. Lead assets post-wind-down: GLPG3667 (selective TYK2 oral; Ph2 SLE missed primary, dermatomyositis hit; Ph3-enabling readout early 2026), Jyseleca royalty (sold to Alfasigma Jan 2024; mid-single to mid-double-digit royalties), CAR-T residual (GLPG5101 ATALANTA-1 MCL 100% ORR / 96% CR ASH 2025; FDA RMAT; being out-licensed/sold). Strategic posture: cash redeployment via BD/M&A."),
        ("yahooTicker", "GLPG"),
    )

    assets = []

    # GLPG3667 - lead remaining asset (TYK2)
    assets.append(asset(
        "glpg3667", "GLPG3667 - selective TYK2 inhibitor (oral; deuterium-modified pseudokinase domain selective)",
        "Phase 3-enabling (Ph2 SLE missed primary; Ph2 dermatomyositis hit; topline early 2026)",
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

    # CAR-T residual being wound down
    assets.append(asset(
        "glpg5101", "GLPG5101 - CD19 CAR-T (Cellpoint decentralized 7-day vein-to-vein platform)",
        "Phase 2 (ATALANTA-1 MCL 100% ORR + 96% CR ASH 2025; FDA RMAT; Galapagos winding down cell therapy -- seeking buyer/out-license)",
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
        "glpg3667": {"mega_bear": 25, "bear": 40, "base": 55, "bull": 70, "psychedelic_bull": 82},
        "glpg5101": {"mega_bear": 15, "bear": 28, "base": 45, "bull": 60, "psychedelic_bull": 72},
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
        od(("date", "Q1 2026"), ("dateSort", "2026-03-31"), ("asset", "glpg3667"),
           ("indication", "dermatomyositis_3667"),
           ("title", "GLPG3667 TYK2 Ph2 dermatomyositis topline + Ph3 design"),
           ("type", "phase2_data"), ("binary", True),
           ("fail_pos", 25), ("fail_apr", 65), ("success_pos", 75), ("success_apr", 88),
           ("_source", "Galapagos pipeline; Q3 2025 update"), ("_confidence", "high")),
        od(("date", "H1 2026"), ("dateSort", "2026-06-30"), ("asset", "glpg5101"),
           ("indication", "mcl_cart"),
           ("title", "GLPG5101 CAR-T out-licensing/sale (cell therapy wind-down implementation)"),
           ("type", "partnership"), ("binary", True),
           ("fail_pos", 15), ("fail_apr", 60), ("success_pos", 70), ("success_apr", 90),
           ("_source", "Galapagos Oct 2025 wind-down announcement"), ("_confidence", "medium")),
        od(("date", "2026"), ("dateSort", "2026-12-15"), ("asset", "glpg3667"),
           ("indication", "sle_3667"),
           ("title", "Strategic BD/M&A capital deployment ($3B cash optionality)"),
           ("type", "milestone"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Galapagos FY25 release; CEO commentary"), ("_confidence", "medium")),
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
        ("currentPrice", 3.62),
        ("sharesOut", 295),
        # Net debt CHF M after Feb 2025 CB restructuring + new financings.
        # CB face ~CHF 800M restructured; cash ~CHF 350M post Oct 2025 raise; net ~-450
        ("cash", -450),  # CHF M
        ("currency", "CHF"),
        ("phase", "commercial"),
        ("subtitle", "Swiss specialty; emerging from heavy CB restructuring (Feb 2025: CHF 800M CB amendments + new money). FY25 revenue CHF 221M (+2x): Quviviq (daridorexant DORA insomnia FDA Apr 2022) CHF 134M (+>130%; EU growth driver), Tryvio (aprocitentan dual ETA/ETB resistant HTN FDA Mar 2024) ramping post REMS removal Mar 2025. Selatogrel + cenerimod outlicensed to Viatris Mar 2024 (USD 350M up + royalties; FY25 reduced milestones USD 250M). Lucerastat (Fabry GCS inhibitor) Ph3 design FDA-agreed Feb 2026. CEO Srishti Gupta. Cash runway extended to 2028 post Oct 2025 financing. Commercial profitability target 2026; overall profitability end 2027. ~636 FTE post-restructuring."),
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

    # Selatogrel + Cenerimod royalty stream from Viatris
    assets.append(asset(
        "viatris_royalty", "Viatris collaboration - selatogrel (P2Y12 self-admin AMI Ph3) + cenerimod (S1P1 SLE Ph3) royalty stream",
        "Royalty (Mar 2024 deal: USD 350M up + tiered mid-single to low-double-digit royalties + dev services contribution)",
        "small_molecule.gpcr.various",
        [innov_ind("viatris_pipeline_royalty", "Idorsia royalty share on Viatris-led Ph3 selatogrel + cenerimod (assets in VTRS config)",
                   "_established_products.idia_viatris_royalty",
                   regions((0.1, 1, 0.1), (0.1, 1, 0.1), (1, 50, 0.1)),
                   slice_((0, 0, 0), (0, 0, 0), (10, 50, 0.1)),
                   {"row.priceK": "Royalty proxy: low-double-digit on Viatris selatogrel + cenerimod sales"},
                   salesM=5, salesYear=2025, peakYear=2030, cagrPct=10, penPct=15,
                   generic_bucket=True)]))

    # Lucerastat - Fabry pipeline (Ph3 design FDA-agreed Feb 2026)
    assets.append(asset(
        "lucerastat", "Lucerastat - oral glucosylceramide synthase inhibitor for Fabry disease",
        "Phase 3 (FDA-agreed design Feb 2026; substrate-reduction therapy alternative to ERT)",
        "small_molecule.enzyme.gcs_inhibitor",
        [innov_ind("fabry", "Fabry disease (alpha-galactosidase A deficiency; substrate-reduction therapy)",
                   "endocrine.lysosomal_storage.fabry",
                   regions((6, 80, 250), (10, 70, 150), (40, 18, 35)),
                   slice_((10, 50, 200), (5, 40, 120), (0.3, 18, 30)),
                   {"us.priceK": "Estimated WAC $200K/yr oral SRT (vs Galafold migalastat ~$300K, ERT ~$300K)",
                    "us.reachPct": "Lucerastat oral non-amenable Fabry; Sanofi Cerdelga competition (different LSD)"},
                   peakYear=2032, cagrPct=0, penPct=12)]))

    # SOTP scenarios -- distressed but improving; high debt reflected in low multiples
    weights = {"mega_bear": 18, "bear": 28, "base": 32, "bull": 17, "psychedelic_bull": 5}
    # FY25 CHF 221M; FY26 guide CHF 200M Quviviq + Tryvio + royalty ~CHF 230-250M
    crev = {"mega_bear": 200, "bear": 250, "base": 320, "bull": 450, "psychedelic_bull": 700}
    # Quviviq doubling FY25; Tryvio post-REMS; market trades ~5-7x EV/sales
    # (mcap ~CHF 1.07B + net debt ~CHF 450M = CHF 1.52B EV vs FY25 CHF 221M)
    cmult = {"mega_bear": 2.5, "bear": 4.0, "base": 5.5, "bull": 7.5, "psychedelic_bull": 10.0}
    pmult = {"mega_bear": 2, "bear": 3, "base": 5, "bull": 8, "psychedelic_bull": 13}
    pdr = {"mega_bear": 12, "bear": 10, "base": 8, "bull": 7, "psychedelic_bull": 6}
    milestones = {"mega_bear": 0, "bear": 50, "base": 150, "bull": 350, "psychedelic_bull": 700}

    SCEN = ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]
    pos_grid = {
        "lucerastat": {"mega_bear": 30, "bear": 50, "base": 70, "bull": 85, "psychedelic_bull": 92},
    }
    apr_grid = {a: {"mega_bear": 60, "bear": 75, "base": 85, "bull": 92, "psychedelic_bull": 96} for a in pos_grid}
    pen_grid = {a: {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25} for a in pos_grid}
    ind_map = {"lucerastat": "fabry"}

    scenarios = od()
    commercial_inert = [
        ("quviviq", "insomnia"), ("tryvio", "resistant_htn"),
        ("viatris_royalty", "viatris_pipeline_royalty"),
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
        od(("date", "2026"), ("dateSort", "2026-06-30"), ("asset", "tryvio"),
           ("indication", "resistant_htn"),
           ("title", "Tryvio aprocitentan global partnership/licensing deal (post REMS removal)"),
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
