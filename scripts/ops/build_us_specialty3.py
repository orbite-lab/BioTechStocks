# -*- coding: utf-8 -*-
"""Build configs for HALO (Halozyme) + EXEL (Exelixis) + ALKS (Alkermes).

Three US specialty biotechs each anchoring a distinct franchise:
- HALO: ENHANZE rHuPH20 SC delivery royalty platform + Elektrofi Hypercon
  (Nov 2025 $750M acq); royalty stream Darzalex/Phesgo/Vyvgart Hytrulo/
  Opdivo Qvantig/Tecentriq SC/Hyqvia + pending Keytruda+Imfinzi SC
- EXEL: Cabometyx multi-tumor TKI ($2.1B FY25 + $180M Ipsen royalty);
  zanzalintinib XL092 next-gen Ph3 STELLAR-303 CRC PDUFA Dec 3 2026
- ALKS: CNS LAI specialty (Vivitrol/Aristada/Lybalvi) + Vumerity royalty
  + Avadel acq Feb 2026 LUMRYZ sodium oxybate ER ($2.1B+CVR);
  alixorexton OX2R agonist Ph3 narcolepsy starts Q1 2026

Run:
  py scripts/ops/build_us_specialty3.py
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
# HALO - Halozyme (ENHANZE royalty platform)
# ============================================================

def build_HALO():
    co = od(
        ("ticker", "HALO"),
        ("name", "Halozyme Therapeutics, Inc."),
        ("currentPrice", 64.29),
        ("sharesOut", 118.47),
        # Net debt post Elektrofi $750M close + $1.5B convert refi: cash $145M
        # vs ~$2B+ converts -> net debt ~-$1,800M
        ("cash", -1800),
        ("currency", "USD"),
        ("phase", "commercial"),
        ("subtitle", "ENHANZE rHuPH20 SC delivery royalty platform + Hypercon (Elektrofi acq Nov 18 2025 $750M+$150M) + Surf Bio (Dec 2025 add'l platform). FY25 record revenue $1.397B (+38% YoY): royalty $868M (+52% on Darzalex Faspro/Phesgo/Vyvgart Hytrulo) + product/other $529M (Hylenex, XYOSTED, OTREXUP via Antares 2022 $960M acq, manufacturing). Approved ENHANZE partner programs: J&J Darzalex Faspro (myeloma), Roche Phesgo (HER2) + Tecentriq SC, argenx Vyvgart Hytrulo (gMG/CIDP), Takeda Hyqvia (PI/CIDP), BMS Opdivo Qvantig (FDA Dec 2024; Q1'25 only $9M pre-J-code, permanent J-code Jul 2025). LITIGATION: Halozyme sued Merck Apr 2025 alleging 15 MDASE patent infringement on Keytruda Qlex SC (FDA approved Sep 19 2025; uses ALTEOGEN Hybrozyme NOT ENHANZE) -- treat as litigation upside, not royalty asset. Imfinzi SC: no AZ filing exists. 2026 guide: +23-30% revenue; >$2B by 2028. 3 new ENHANZE deals 2025 (Takeda + Merus + Skye Bio); Surf Bio acq Dec 2025."),
        ("yahooTicker", "HALO"),
    )

    assets = []

    # ENHANZE royalty stream -- aggregated across partner programs
    assets.append(asset(
        "enhanze_royalty", "ENHANZE rHuPH20 SC delivery royalty platform (Darzalex Faspro + Phesgo + Vyvgart Hytrulo + Opdivo Qvantig + Tecentriq SC + Hyqvia)",
        "Commercial (royalty stream from 6+ approved partner SC formulations; growing pipeline of pending Keytruda + Imfinzi SC)",
        "formulation_modifier.subcutaneous_enhancer.rhuph20",
        [innov_ind("enhanze_io_oncology", "Multi-tumor IO + oncology + immunology SC formulations royalty exposure",
                   "_platform.enhanze_royalty",
                   regions((1, 1, 0.1), (1, 1, 0.1), (1, 50, 0.1)),
                   slice_((0, 0, 0), (0, 0, 0), (10, 50, 0.1)),
                   {"row.priceK": "ENHANZE royalty rate ~3-7% on partner SC product net sales (blended ~5%)"},
                   salesM=868, salesYear=2025, peakYear=2032, cagrPct=25, penPct=30,
                   generic_bucket=True)],
        targets=["SC_DELIVERY"]))

    # XYOSTED (testosterone autoinjector; Antares legacy)
    assets.append(asset(
        "xyosted", "XYOSTED (testosterone enanthate weekly SC autoinjector) - hypogonadism",
        "Commercial (FDA Sep 2018; Antares Pharma acq May 2022)",
        "small_molecule.steroid.testosterone",
        [innov_ind("hypogonadism", "Adult male hypogonadism (low T replacement therapy)",
                   "endocrine.gonadal.hypogonadism",
                   regions((4000, 35, 1.5), (5000, 25, 0.8), (15000, 8, 0.3)),
                   slice_((0.5, 35, 2), (0, 0, 0), (0, 0, 0)),
                   {"us.priceK": "XYOSTED WAC ~$2K/yr",
                    "us.reachPct": "XYOSTED ~3% testosterone Rx volume share"},
                   salesM=120, salesYear=2025, peakYear=2028, cagrPct=5, penPct=18)]))

    # OTREXUP (methotrexate autoinjector; Antares legacy)
    assets.append(asset(
        "otrexup", "OTREXUP (methotrexate weekly SC autoinjector) - RA + JIA + psoriasis",
        "Commercial (FDA Oct 2013; Antares Pharma acq May 2022)",
        "small_molecule.antimetabolite.methotrexate",
        [innov_ind("ra_methotrexate", "RA + JIA + severe psoriasis (SC methotrexate convenience)",
                   "immunology.inflammatory_systemic.rheumatoid_arthritis",
                   regions((1300, 60, 35), (2000, 50, 22), (10000, 8, 6)),
                   slice_((0.3, 30, 1.5), (0, 0, 0), (0, 0, 0)),
                   {"us.priceK": "OTREXUP WAC ~$1.5K/yr",
                    "us.reachPct": "OTREXUP ~2% MTX Rx volume share"},
                   salesM=70, salesYear=2025, peakYear=2027, cagrPct=2, penPct=15)]))

    # Hypercon (Elektrofi platform) - pre-revenue
    assets.append(asset(
        "hypercon", "Hypercon ultra-high-concentration microparticle SC platform (Elektrofi acq Nov 2025; argenx + Lilly + J&J partnered programs)",
        "Pre-revenue (royalties expected 2030+; up to $275M milestones from 2 programs entering clinic by YE2026)",
        "formulation_modifier.microparticle.hypercon",
        [innov_ind("hypercon_pipeline", "Multi-product SC microparticle delivery (long-acting oncology + autoimmune)",
                   "_platform.hypercon_royalty",
                   regions((1, 1, 0.1), (1, 1, 0.1), (1, 50, 0.1)),
                   slice_((0, 0, 0), (0, 0, 0), (5, 30, 0.1)),
                   {"row.priceK": "Hypercon royalty rate similar to ENHANZE ~3-7%"},
                   peakYear=2034, cagrPct=0, penPct=10)]))

    # SOTP scenarios
    weights = {"mega_bear": 10, "bear": 22, "base": 38, "bull": 25, "psychedelic_bull": 5}
    crev = {"mega_bear": 1450, "bear": 1600, "base": 1750, "bull": 2000, "psychedelic_bull": 2500}
    cmult = {"mega_bear": 4, "bear": 6, "base": 8, "bull": 11, "psychedelic_bull": 15}
    pmult = {"mega_bear": 3, "bear": 5, "base": 7, "bull": 10, "psychedelic_bull": 14}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [
        ("enhanze_royalty", ["enhanze_io_oncology"]),
        ("xyosted", ["hypogonadism"]),
        ("otrexup", ["ra_methotrexate"]),
    ]

    pos_grid = {
        "hypercon": {"mega_bear": 25, "bear": 40, "base": 55, "bull": 70, "psychedelic_bull": 82},
    }
    apr_default = {"mega_bear": 60, "bear": 75, "base": 85, "bull": 92, "psychedelic_bull": 96}
    pen_default = {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25}

    pipeline_asmps = {}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "hypercon": OrderedDict([("hypercon_pipeline", od(
                ("pos", pos_grid["hypercon"][sk]),
                ("apr", apr_default[sk]),
                ("pen", pen_default[sk]),
            ))]),
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "H1 2026"), ("dateSort", "2026-06-30"), ("asset", "enhanze_royalty"),
           ("indication", "enhanze_io_oncology"),
           ("title", "Merck Keytruda Qlex SC FDA decision (pembrolizumab SC; major royalty unlock)"),
           ("type", "pdufa"), ("binary", True),
           ("fail_pos", 70), ("fail_apr", 80), ("success_pos", 95), ("success_apr", 95),
           ("_source", "Merck Keytruda SC filing"), ("_confidence", "high")),
        od(("date", "2026"), ("dateSort", "2026-12-15"), ("asset", "enhanze_royalty"),
           ("indication", "enhanze_io_oncology"),
           ("title", "AZ Imfinzi SC durvalumab + new ENHANZE deal flow"),
           ("type", "milestone"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Halozyme FY25 IR"), ("_confidence", "medium")),
        od(("date", "2027"), ("dateSort", "2027-06-30"), ("asset", "hypercon"),
           ("indication", "hypercon_pipeline"),
           ("title", "Hypercon first 2 partner programs enter clinic (milestone trigger up to $275M)"),
           ("type", "phase1_start"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Halozyme Elektrofi integration"), ("_confidence", "medium")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


# ============================================================
# EXEL - Exelixis (Cabometyx + zanzalintinib)
# ============================================================

def build_EXEL():
    co = od(
        ("ticker", "EXEL"),
        ("name", "Exelixis, Inc."),
        ("currentPrice", 44.46),
        ("sharesOut", 254),
        ("cash", 1660),  # net cash $1.66B; no debt of note
        ("currency", "USD"),
        ("phase", "commercial"),
        ("subtitle", "Multi-tumor TKI specialty. FY25 revenue $2.32B (+7%): Cabometyx US net product ~$2.12B (+17% YoY; ~99% of product) + Cabometyx Ipsen ex-US + Takeda Japan royalties $179M. Indication mix US: RCC ~80% (1L combo with Opdivo + 2L+ mono) / HCC ~10% / DTC 3-4% / NET 4% (CABINET FDA Mar 2025 pNET+epNET ramping). Net cash $1.66B; ~24M shares repurchased FY25 ($954M of $1.5B+ authorization); 254M shares (was ~278M). NOT selected for IPAY 2027 (small biotech exception); IPAY 2028+ risk. PIPELINE: Zanzalintinib (XL092) next-gen VEGFR/MET/AXL TKI: STELLAR-303 (2L+ mCRC + atezo) NDA accepted, PDUFA Dec 3 2026 (CRITICAL CATALYST); STELLAR-304 (1L nccRCC + nivo) topline H1 2026; STELLAR-305 HNSCC discontinued. XL309 (USP1 BRCA-mut Ph1)."),
        ("yahooTicker", "EXEL"),
    )

    assets = []

    # Cabometyx RCC (largest)
    assets.append(asset(
        "cabometyx_rcc", "Cabometyx (cabozantinib) - multi-target TKI (VEGFR/MET/AXL); RCC franchise",
        "Commercial (FDA RCC 2L+ Apr 2016; 1L combo with Opdivo Jan 2021; Ipsen ex-US partner)",
        "small_molecule.kinase.multi_tki",
        [
            innov_ind("rcc_1l", "Renal cell carcinoma 1L (combo with Opdivo)",
                      "oncology.genitourinary.rcc",
                      regions((30, 80, 200), (45, 70, 130), (200, 18, 35)),
                      slice_((25, 60, 200), (12, 50, 130), (1, 18, 35)),
                      {"us.reachPct": "Cabometyx ~30% 1L RCC TKI share (vs Lenvima+Keytruda + Inlyta+Pembro)",
                       "us.priceK": "Cabometyx WAC ~$200K/yr"},
                      salesM=1100, salesYear=2025, peakYear=2028, cagrPct=5, penPct=35),
            innov_ind("rcc_2l", "Renal cell carcinoma 2L+ (post-IO/TKI; mono)",
                      "oncology.genitourinary.rcc",
                      regions((30, 80, 200), (45, 70, 130), (200, 18, 35)),
                      slice_((20, 60, 200), (10, 50, 130), (1, 18, 35)),
                      {"us.reachPct": "Cabometyx ~50% 2L+ RCC mono share post-IO failure"},
                      salesM=600, salesYear=2025, peakYear=2027, cagrPct=-5, penPct=35),
        ]))

    # Cabometyx HCC + DTC + NET (combined non-RCC)
    assets.append(asset(
        "cabometyx_other", "Cabometyx other indications (HCC + DTC + pNET/epNET)",
        "Commercial (HCC 2018; DTC 2021; NET CABINET FDA Mar 2025 pNET+epNET expansion)",
        "small_molecule.kinase.multi_tki",
        [
            innov_ind("hcc_2l", "Hepatocellular carcinoma 2L (post-sorafenib)",
                      "oncology.gi.hcc",
                      regions((25, 70, 150), (40, 60, 90), (300, 18, 25)),
                      slice_((4, 50, 150), (2, 40, 90), (0.3, 18, 25)),
                      {"us.priceK": "Cabometyx HCC WAC ~$150K/yr"},
                      salesM=200, salesYear=2025, peakYear=2027, cagrPct=2, penPct=20),
            innov_ind("net_pnet", "Pancreatic + extra-pancreatic neuroendocrine tumors (CABINET pivotal)",
                      "oncology.neuroendocrine.gi_pancreatic_net",
                      regions((25, 90, 60), (35, 85, 40), (150, 25, 12)),
                      slice_((10, 60, 100), (3, 50, 60), (0.2, 18, 18)),
                      {"us.reachPct": "Cabometyx NET first systemic post-Lutathera/Sandostatin",
                       "us.priceK": "Cabometyx NET WAC ~$100K/yr"},
                      salesM=80, salesYear=2025, peakYear=2030, cagrPct=40, penPct=20),
            innov_ind("dtc_2l", "Differentiated thyroid cancer 2L (post-RAI refractory)",
                      "oncology.endocrine.thyroid",
                      regions((10, 80, 100), (15, 70, 60), (60, 25, 18)),
                      slice_((8, 60, 100), (4, 50, 60), (0.5, 25, 18)),
                      {"us.priceK": "Cabometyx DTC WAC ~$100K/yr"},
                      salesM=60, salesYear=2025, peakYear=2027, cagrPct=2, penPct=15),
        ]))

    # Cabometyx ex-US royalty (Ipsen + Takeda)
    assets.append(asset(
        "cabometyx_royalty", "Cabometyx ex-US royalty stream (Ipsen Europe + Takeda Japan)",
        "Commercial royalty (Ipsen ex-US partnership 2016; Takeda Japan)",
        "small_molecule.kinase.multi_tki",
        [innov_ind("cabo_ex_us_royalty", "Cabometyx ex-US royalty (Ipsen + Takeda) on global net sales",
                   "_platform.exelixis_cabo_royalty",
                   regions((1, 1, 0.1), (1, 1, 0.1), (1, 50, 0.1)),
                   slice_((0, 0, 0), (0, 0, 0), (5, 50, 0.1)),
                   {"row.priceK": "Royalty proxy: ~22% ex-US Cabometyx net sales"},
                   salesM=179, salesYear=2025, peakYear=2028, cagrPct=5, penPct=25,
                   generic_bucket=True)]))

    # Zanzalintinib (XL092) - next-gen TKI; STELLAR-303 PDUFA Dec 3 2026
    assets.append(asset(
        "zanzalintinib", "Zanzalintinib (XL092) - next-gen VEGFR/MET/AXL/MER multi-target TKI (Cabometyx successor)",
        "Phase 3 (STELLAR-303 mCRC NDA accepted PDUFA Dec 3 2026; STELLAR-304 nccRCC topline H1 2026)",
        "small_molecule.kinase.multi_tki",
        [
            innov_ind("crc_2l", "2L+ mCRC + atezolizumab combo (STELLAR-303 OS hit ITT 10.9m vs 9.4m regorafenib; NDA accepted Feb 2 2026; PDUFA Dec 3 2026)",
                      "oncology.gi.colorectal",
                      regions((150, 80, 30), (250, 70, 20), (1500, 15, 6)),
                      slice_((15, 65, 150), (8, 55, 100), (0.5, 18, 25)),
                      {"us.priceK": "Zanzalintinib WAC ~$150K/yr blended (parallel to Cabometyx ~$200K)",
                       "us.reachPct": "Zanza CRC ~12-15% 2L+ mCRC post-FOLFIRI/Stivarga/Lonsurf; mgmt guides $5B US peak by 2033 across CRC+RCC; William Blair $875M risk-adj US CRC peak alone"},
                      peakYear=2031, cagrPct=0, penPct=18),
            innov_ind("nccrcc_1l", "1L non-clear cell RCC + nivolumab combo (STELLAR-304 topline H1 2026)",
                      "oncology.genitourinary.rcc",
                      regions((6, 75, 200), (10, 65, 130), (40, 18, 35)),
                      slice_((25, 55, 200), (10, 45, 130), (1, 15, 35)),
                      {"us.reachPct": "Zanza+Nivo nccRCC ~25-30% 1L share if approved (vs current TKI mono)",
                       "us.priceK": "Zanza WAC ~$200K/yr"},
                      peakYear=2031, cagrPct=0, penPct=15),
        ]))

    # XL309 USP1 inhibitor
    assets.append(asset(
        "xl309", "XL309 - USP1 inhibitor (BRCA1/2-mutant tumors; PARP/topo combo)",
        "Phase 1 (BRCA-mutant ovarian + breast + prostate; mono + combo)",
        "small_molecule.enzyme.usp1_inhibitor",
        [innov_ind("brca_ovarian", "BRCA1/2-mutant ovarian + breast cancer (USP1 inhibitor)",
                   "oncology.gynecologic.ovarian",
                   regions((20, 80, 150), (30, 70, 100), (120, 25, 30)),
                   slice_((4, 50, 100), (2, 40, 60), (0.2, 25, 20)),
                   {"us.priceK": "Estimated WAC $100K/yr"},
                   peakYear=2033, cagrPct=0, penPct=10)]))

    weights = {"mega_bear": 10, "bear": 22, "base": 38, "bull": 25, "psychedelic_bull": 5}
    # FY25 $2.32B; FY26 guide range; zanza launch H1 2027 post Dec 2026 PDUFA
    crev = {"mega_bear": 2200, "bear": 2400, "base": 2600, "bull": 3000, "psychedelic_bull": 3700}
    cmult = {"mega_bear": 4, "bear": 5.5, "base": 7, "bull": 9, "psychedelic_bull": 12}
    pmult = {"mega_bear": 3, "bear": 5, "base": 7, "bull": 10, "psychedelic_bull": 14}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [
        ("cabometyx_rcc", ["rcc_1l", "rcc_2l"]),
        ("cabometyx_other", ["hcc_2l", "net_pnet", "dtc_2l"]),
        ("cabometyx_royalty", ["cabo_ex_us_royalty"]),
    ]

    pos_grid = {
        "zanzalintinib_crc":  {"mega_bear": 60, "bear": 75, "base": 88, "bull": 95, "psychedelic_bull": 99},
        "zanzalintinib_rcc":  {"mega_bear": 35, "bear": 55, "base": 75, "bull": 88, "psychedelic_bull": 95},
        "xl309":              {"mega_bear": 15, "bear": 25, "base": 40, "bull": 55, "psychedelic_bull": 70},
    }
    apr_default = {"mega_bear": 65, "bear": 78, "base": 88, "bull": 93, "psychedelic_bull": 97}
    pen_default = {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25}

    pipeline_asmps = {}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "zanzalintinib": OrderedDict([
                ("crc_2l", od(("pos", pos_grid["zanzalintinib_crc"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk]))),
                ("nccrcc_1l", od(("pos", pos_grid["zanzalintinib_rcc"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk]))),
            ]),
            "xl309": OrderedDict([("brca_ovarian", od(
                ("pos", pos_grid["xl309"][sk]),
                ("apr", apr_default[sk]),
                ("pen", pen_default[sk]),
            ))]),
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "Mid 2026"), ("dateSort", "2026-07-15"), ("asset", "zanzalintinib"),
           ("indication", "nccrcc_1l"),
           ("title", "Zanzalintinib STELLAR-304 nccRCC + nivo Ph3 topline (mid-2026; enrollment complete May 2025)"),
           ("type", "phase3_data"), ("binary", True),
           ("fail_pos", 35), ("fail_apr", 70), ("success_pos", 88), ("success_apr", 92),
           ("_source", "Exelixis Jan 2026 prelim FY25 release"), ("_confidence", "high")),
        od(("date", "Mid 2026"), ("dateSort", "2026-08-15"), ("asset", "zanzalintinib"),
           ("indication", "crc_2l"),
           ("title", "STELLAR-316 (CRC adjuvant MRD+ Natera ctDNA; DFS primary) + STELLAR-201 (recurrent meningioma) Ph3 initiations"),
           ("type", "phase3_start"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Exelixis Q4 2025 IR + Natera collaboration"), ("_confidence", "high")),
        od(("date", "Dec 3 2026"), ("dateSort", "2026-12-03"), ("asset", "zanzalintinib"),
           ("indication", "crc_2l"),
           ("title", "Zanzalintinib STELLAR-303 mCRC + atezo PDUFA (NDA accepted Feb 2 2026; OS 10.9m vs 9.4m regorafenib ITT)"),
           ("type", "pdufa"), ("binary", True),
           ("fail_pos", 70), ("fail_apr", 80), ("success_pos", 96), ("success_apr", 96),
           ("_source", "FDA NDA acceptance Feb 2 2026"), ("_confidence", "high")),
        od(("date", "Mar 2025"), ("dateSort", "2025-03-15"), ("asset", "cabometyx_other"),
           ("indication", "net_pnet"),
           ("title", "Cabometyx CABINET NET FDA approval (pNET + epNET expansion)"),
           ("type", "label_expansion"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Exelixis Mar 2025 PR"), ("_confidence", "high")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


# ============================================================
# ALKS - Alkermes (CNS LAI specialty + Avadel Lumryz)
# ============================================================

def build_ALKS():
    co = od(
        ("ticker", "ALKS"),
        ("name", "Alkermes plc"),
        ("currentPrice", 34.53),
        ("sharesOut", 166),
        # YE25 cash+inv $1.32B; Avadel $2.1B financing = $775M cash + $1.525B new
        # term loans -> post-close net debt ~ -$980M
        ("cash", -980),
        ("currency", "USD"),
        ("phase", "commercial"),
        ("subtitle", "CNS specialty (LAI psychiatry + addiction + sleep). FY25 revenue ~$1.5B: Vivitrol naltrexone monthly LAI (OUD+AUD) $467.9M; Aristada/Initio aripiprazole LAI $370.0M (schizo); Lybalvi olanzapine+samidorphan $346.7M (schizo+bipolar I); Vumerity Biogen MS royalty $130.5M; Invega Sustenna/Trinza J&J royalty $109.6M (declining XEPLION LOE); Risperdal Consta + other ~$50M. Avadel acq closed Feb 12 2026 ($2.1B = $775M cash + $1.525B new term loans + $1.50/sh CVR on FDA approval of LUMRYZ for IH by end-2028) added LUMRYZ sodium oxybate ER ($275M FY25 narco; FY26 guide $315-335M; once-nightly differentiated vs Xyrem twice-nightly). Mural Oncology fully spun off Nov 2023 (no economic interest retained). FY26 guide $1.73-1.84B incl Lumryz. CEO transition: Richard Pops retires Jul 31 2026; Blair Jackson (COO) becomes CEO Aug 1 2026. PIPELINE: alixorexton (ALKS 2680) selective OX2R agonist -- VIBRANCE-1 NT1 Ph2 hit primary 2025; VIBRANCE-2 NT2 hit dual primary (MWT + ESS) 2025; FDA Breakthrough Therapy Designation NT1 Jan 6 2026; BRILLIANCE Ph3 program initiated Apr 1 2026 (3 studies: 302+304 NT1, 303 NT2; topline 2027/2028)."),
        ("yahooTicker", "ALKS"),
    )

    assets = []

    # Vivitrol (naltrexone monthly LAI)
    assets.append(asset(
        "vivitrol", "Vivitrol (naltrexone monthly extramuscular depot) - opioid antagonist for OUD + AUD",
        "Commercial (FDA AUD 2006; OUD 2010; monthly IM injection)",
        "small_molecule.opioid.antagonist_depot",
        [innov_ind("aud_oud_lai", "Alcohol use disorder + opioid use disorder (long-acting injectable naltrexone)",
                   "cns.psychiatry.substance_use.opioid",
                   regions((2500, 25, 8), (1500, 18, 5), (5000, 5, 2)),
                   slice_((6, 35, 18), (1, 25, 12), (0.1, 5, 5)),
                   {"us.reachPct": "Vivitrol ~5% AUD/OUD treated population on monthly LAI",
                    "us.priceK": "Vivitrol WAC ~$1.5K/mo × 12 = $18K/yr"},
                   salesM=468, salesYear=2025, peakYear=2030, cagrPct=2, penPct=15)],
        targets=["OPRM1"]))

    # Aristada (aripiprazole lauroxil monthly + bi-monthly LAI)
    assets.append(asset(
        "aristada", "Aristada / Aristada Initio (aripiprazole lauroxil) - dopamine partial agonist monthly + bi-monthly LAI for schizophrenia",
        "Commercial (FDA Oct 2015 monthly; Initio start 2018)",
        "small_molecule.gpcr.atypical_antipsychotic_depot",
        [innov_ind("schizo_lai", "Schizophrenia long-acting injectable (1-2 monthly)",
                   "cns.psychiatry.schizophrenia",
                   regions((1500, 75, 10), (2500, 60, 5), (24000, 25, 1.5)),
                   slice_((4, 60, 25), (0.5, 50, 15), (0.05, 12, 5)),
                   {"us.reachPct": "Aristada ~12% US schizo LAI share (vs Invega Sustenna/Trinza, Risperdal Consta, Uzedy)",
                    "us.priceK": "Aristada WAC ~$25K/yr"},
                   salesM=370, salesYear=2025, peakYear=2028, cagrPct=2, penPct=15)],
        targets=["DRD2"]))

    # Lybalvi (olanzapine + samidorphan)
    assets.append(asset(
        "lybalvi", "Lybalvi (olanzapine + samidorphan) - olanzapine + opioid antagonist combo for schizo + bipolar I",
        "Commercial (FDA May 2021; addresses olanzapine weight gain via samidorphan)",
        "small_molecule.gpcr.atypical_combo",
        [
            innov_ind("schizo_oral", "Schizophrenia oral (olanzapine reformulation with weight-mitigating samidorphan)",
                      "cns.psychiatry.schizophrenia",
                      regions((1500, 75, 10), (2500, 60, 5), (24000, 25, 1.5)),
                      slice_((1.5, 50, 10), (0, 0, 0), (0, 0, 0)),
                      {"us.priceK": "Lybalvi WAC ~$10K/yr"},
                      salesM=240, salesYear=2025, peakYear=2030, cagrPct=15, penPct=18),
            innov_ind("bipolar_lybalvi", "Bipolar I disorder (acute + maintenance)",
                      "cns.psychiatry.bipolar",
                      regions((6000, 60, 5), (10000, 45, 3), (50000, 12, 1)),
                      slice_((0.2, 50, 10), (0, 0, 0), (0, 0, 0)),
                      {"us.priceK": "Lybalvi WAC ~$10K/yr"},
                      salesM=107, salesYear=2025, peakYear=2030, cagrPct=15, penPct=15),
        ],
        targets=["DRD2", "OPRM1"]))

    # LUMRYZ (sodium oxybate ER) - Avadel acq Feb 2026
    assets.append(asset(
        "lumryz", "LUMRYZ (sodium oxybate ER) - GHB receptor agonist once-nightly for narcolepsy (Avadel acq Feb 2026)",
        "Commercial (FDA NT1+NT2 2023; IH filing pursued; CVR $1.50/sh tied to IH approval by 2028)",
        "small_molecule.gpcr.gabab_agonist",
        [innov_ind("narcolepsy_lumryz", "Narcolepsy type 1+2 (cataplexy + EDS); IH expansion pursued",
                   "cns.sleep.narcolepsy",
                   regions((50, 80, 30), (80, 65, 18), (300, 18, 5)),
                   slice_((10, 60, 60), (2, 40, 40), (0.1, 18, 12)),
                   {"us.reachPct": "Lumryz once-nightly differentiated vs Xyrem twice-nightly; ~10% narcolepsy GHB share",
                    "us.priceK": "Lumryz WAC ~$60K/yr blended"},
                   salesM=275, salesYear=2025, peakYear=2031, cagrPct=25, penPct=22)]))

    # Vumerity Biogen royalty
    assets.append(asset(
        "vumerity_royalty", "Vumerity (diroximel fumarate) Biogen MS royalty stream (Tecfidera follow-on)",
        "Commercial royalty (Biogen license; FDA Oct 2019)",
        "small_molecule.fumarate.dimethyl_fumarate",
        [innov_ind("ms_vumerity", "Relapsing MS Vumerity Biogen royalty",
                   "_platform.alks_biogen_royalty",
                   regions((1, 1, 0.1), (1, 1, 0.1), (1, 50, 0.1)),
                   slice_((0, 0, 0), (0, 0, 0), (5, 50, 0.1)),
                   {"row.priceK": "ALKS receives blended ~15% royalty on Biogen Vumerity net sales"},
                   salesM=131, salesYear=2025, peakYear=2027, cagrPct=-3, penPct=20,
                   generic_bucket=True)]))

    # Invega Sustenna/Trinza JNJ royalty (mature, declining post-LOE)
    assets.append(asset(
        "invega_royalty", "Invega Sustenna + Trinza (paliperidone palmitate) - J&J royalty stream (LAI schizo)",
        "Commercial royalty (mature; XEPLION generic competition; royalty phasing out H2 2026)",
        "small_molecule.gpcr.atypical_antipsychotic_depot",
        [innov_ind("schizo_invega_royalty", "Invega Sustenna/Trinza J&J LAI schizo royalty",
                   "_platform.alks_jnj_royalty",
                   regions((1, 1, 0.1), (1, 1, 0.1), (1, 50, 0.1)),
                   slice_((0, 0, 0), (0, 0, 0), (5, 50, 0.1)),
                   {"row.priceK": "ALKS Invega royalty winding down on XEPLION LOE"},
                   salesM=110, salesYear=2025, peakYear=2026, cagrPct=-30, penPct=20,
                   generic_bucket=True)]))

    # Alixorexton (ALKS 2680) - OX2R agonist; BRILLIANCE Ph3 NT1+NT2 initiated Apr 1 2026
    assets.append(asset(
        "alixorexton", "Alixorexton (ALKS 2680) - selective orexin-2 receptor (OX2R) agonist; BRILLIANCE Ph3 program",
        "Phase 3 BRILLIANCE (initiated Apr 1 2026; Studies 302+304 NT1 + Study 303 NT2; FDA Breakthrough NT1 Jan 6 2026; VIBRANCE-1 NT1 + VIBRANCE-2 NT2 Ph2 both hit primary 2025)",
        "small_molecule.gpcr.orexin_2_agonist",
        [
            innov_ind("nt1_alix", "Narcolepsy type 1 (with cataplexy; selective OX2R agonist; FDA Breakthrough Designation Jan 2026)",
                      "cns.sleep.narcolepsy",
                      regions((25, 80, 50), (40, 65, 30), (150, 18, 8)),
                      slice_((15, 70, 100), (3, 50, 60), (0.2, 18, 15)),
                      {"us.reachPct": "Alixorexton vs Lumryz/Xywav/Xyrem; first selective OX2R disease-modifying for cataplexy",
                       "us.priceK": "Estimated WAC $100K/yr (vs Lumryz $90K)"},
                      peakYear=2032, cagrPct=0, penPct=20),
            innov_ind("nt2_alix", "Narcolepsy type 2 (without cataplexy; VIBRANCE-2 hit dual primary MWT+ESS)",
                      "cns.sleep.narcolepsy",
                      regions((30, 70, 50), (50, 55, 30), (200, 15, 8)),
                      slice_((8, 60, 100), (2, 45, 60), (0.1, 15, 15)),
                      {"us.priceK": "Estimated WAC $100K/yr"},
                      peakYear=2033, cagrPct=0, penPct=15),
        ]))

    weights = {"mega_bear": 10, "bear": 22, "base": 38, "bull": 25, "psychedelic_bull": 5}
    # FY26 guide $1.73-1.84B incl Lumryz; market trades ALKS ~3-4x EV/sales
    # (mcap ~$5.7B + net debt $0.8B = $6.5B EV / FY26 $1.78B = 3.7x)
    crev = {"mega_bear": 1700, "bear": 1850, "base": 2000, "bull": 2300, "psychedelic_bull": 2800}
    cmult = {"mega_bear": 1.8, "bear": 2.5, "base": 3.5, "bull": 5.0, "psychedelic_bull": 7.0}
    pmult = {"mega_bear": 2, "bear": 3, "base": 5, "bull": 7, "psychedelic_bull": 10}
    pdr = {"mega_bear": 10, "bear": 9, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [
        ("vivitrol", ["aud_oud_lai"]),
        ("aristada", ["schizo_lai"]),
        ("lybalvi", ["schizo_oral", "bipolar_lybalvi"]),
        ("lumryz", ["narcolepsy_lumryz"]),
        ("vumerity_royalty", ["ms_vumerity"]),
        ("invega_royalty", ["schizo_invega_royalty"]),
    ]

    pos_grid = {
        # NT1 PoS bumped post Breakthrough Designation Jan 2026 + dual Ph2 hits
        "alixorexton_nt1":  {"mega_bear": 55, "bear": 75, "base": 88, "bull": 95, "psychedelic_bull": 98},
        "alixorexton_nt2":  {"mega_bear": 40, "bear": 60, "base": 78, "bull": 90, "psychedelic_bull": 95},
    }
    apr_default = {"mega_bear": 65, "bear": 78, "base": 88, "bull": 93, "psychedelic_bull": 97}
    pen_default = {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25}

    pipeline_asmps = {}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "alixorexton": OrderedDict([
                ("nt1_alix", od(("pos", pos_grid["alixorexton_nt1"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk]))),
                ("nt2_alix", od(("pos", pos_grid["alixorexton_nt2"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk]))),
            ]),
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "Feb 12 2026"), ("dateSort", "2026-02-12"), ("asset", "lumryz"),
           ("indication", "narcolepsy_lumryz"),
           ("title", "Avadel acquisition closed ($2.1B + $1.50 CVR; Lumryz sodium oxybate ER added)"),
           ("type", "ma_close"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Alkermes Feb 12 2026 PR"), ("_confidence", "high")),
        od(("date", "Jan 6 2026"), ("dateSort", "2026-01-06"), ("asset", "alixorexton"),
           ("indication", "nt1_alix"),
           ("title", "FDA Breakthrough Therapy Designation -- alixorexton in narcolepsy type 1 (de-risking event)"),
           ("type", "regulatory"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Alkermes Jan 6 2026 PR"), ("_confidence", "high")),
        od(("date", "Apr 1 2026"), ("dateSort", "2026-04-01"), ("asset", "alixorexton"),
           ("indication", "nt1_alix"),
           ("title", "BRILLIANCE Ph3 program initiated (Studies 302+304 NT1, Study 303 NT2)"),
           ("type", "phase3_start"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Alkermes Apr 2026 PR"), ("_confidence", "high")),
        od(("date", "2027-2028"), ("dateSort", "2028-06-30"), ("asset", "lumryz"),
           ("indication", "narcolepsy_lumryz"),
           ("title", "Lumryz IH (idiopathic hypersomnia) approval (CVR $1.50/sh trigger)"),
           ("type", "pdufa"), ("binary", True),
           ("fail_pos", 50), ("fail_apr", 75), ("success_pos", 90), ("success_apr", 92),
           ("_source", "Avadel deal CVR mechanics"), ("_confidence", "medium")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


def main():
    write_config("HALO", build_HALO())
    write_config("EXEL", build_EXEL())
    write_config("ALKS", build_ALKS())

    manifest_path = CONFIGS / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for tk in ["HALO", "EXEL", "ALKS"]:
        if tk not in manifest:
            manifest.append(tk)
    manifest = sorted(set(manifest))
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"\n  manifest -> {len(manifest)} tickers")


if __name__ == "__main__":
    main()
