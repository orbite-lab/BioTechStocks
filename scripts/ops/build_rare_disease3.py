# -*- coding: utf-8 -*-
"""Build configs for CORT (Corcept) + AUPH (Aurinia) + FOLD (Amicus) US rare-disease.

Three US specialty biotechs:
- CORT: Korlym Cushing's franchise + relacorilant (Lifyorli FDA Mar 2026 ovarian
  cancer; Cushing's CRL Dec 30 2025 - resubmission TBD); dazucorilant ALS
- AUPH: Lupkynis (voclosporin) lupus nephritis $271M FY25; AUR200 BAFF/APRIL
  Ph2 SLE+IgAN H1 2026; net cash $398M
- FOLD: Galafold Fabry $522M + Pombiliti+Opfolda Pompe $113M; DMX-200 FSGS Ph3
  (Dimerix-licensed Apr 2025); BIOMARIN ACQ ANNOUNCED Dec 2025 at $14.50/share
  (FTC HSR cleared Feb 11 2026; close mid-2026 - treat as deal arb)
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
# CORT - Corcept Therapeutics
# ============================================================

def build_CORT():
    co = od(
        ("ticker", "CORT"),
        ("name", "Corcept Therapeutics, Inc."),
        ("currentPrice", 45.04),
        ("sharesOut", 107.4),
        ("cash", 532),  # net cash $532M; no LT debt
        ("currency", "USD"),
        ("phase", "commercial"),
        ("subtitle", "Cortisol modulator specialty (Korlym Cushing's franchise + relacorilant pivot). FY25 revenue $761.4M (+13% YoY): Korlym (mifepristone + AG) entire franchise -- only approved drug for Cushing's syndrome hyperglycemia (FDA 2012); tablets sold +37%. Profitable: Net income $99.7M ($0.82 EPS); $246M buybacks FY25; cash $532M no debt. RELACORILANT (selective oral GR antagonist; non-steroidal cortisol modulator): (1) CUSHING'S NDA -> FDA CRL Dec 30 2025 (additional efficacy evidence required; resubmission path TBD); GRACE Ph3 + GRADIENT confirmatory both positive. (2) PLATINUM-RESISTANT OVARIAN CANCER: relacorilant + nab-paclitaxel ROSELLA Ph3 positive (PFS + OS); FDA APPROVED Mar 25 2026 as 'LIFYORLI' (PDUFA originally Jul 11 2026; early approval). DAZUCORILANT (CORT113176) -- DAZALS Ph2 ALS missed primary endpoint Dec 2024 but 300mg survival HR 0.13 (p<0.0001) at 2-yr; ENCALS Jun 2025 follow-up. Earlier-stage GR antagonist platform CORT125281, CORT125329."),
        ("yahooTicker", "CORT"),
    )

    assets = []

    # Korlym (mifepristone) - Cushing's franchise
    assets.append(asset(
        "korlym", "Korlym (mifepristone) - GR/PR antagonist for Cushing's syndrome hyperglycemia (only FDA-approved Rx for endogenous Cushing's)",
        "Commercial (FDA Feb 2012; Korlym + authorized generic)",
        "small_molecule.nuclear_receptor.gr_antagonist",
        [innov_ind("cushings_korlym", "Cushing's syndrome hyperglycemia (endogenous; only FDA-approved Rx)",
                   "endocrine.pituitary.cushings",
                   regions((20, 80, 200), (30, 70, 130), (120, 25, 35)),
                   slice_((80, 80, 400), (15, 55, 200), (1, 25, 50)),
                   {"us.priceK": "Korlym WAC ~$400K/yr blended including auth-generic + cumulative dose dependent; FY25 tablets sold +37%",
                    "us.reachPct": "Korlym ~80% diagnosed treated Cushing's hyperglycemia US (only approved Rx); ramping"},
                   salesM=761, salesYear=2025, peakYear=2028, cagrPct=10, penPct=35)],
        targets=["NR3C1"]))

    # Relacorilant - PROC (Lifyorli; FDA approved Mar 25 2026)
    assets.append(asset(
        "lifyorli", "Lifyorli (relacorilant) - selective GR antagonist + nab-paclitaxel for platinum-resistant ovarian cancer",
        "Commercial (FDA approved Mar 25 2026; ROSELLA Ph3 PFS + OS positive; combo with nab-paclitaxel)",
        "small_molecule.nuclear_receptor.gr_antagonist",
        [innov_ind("ovarian_proc", "Platinum-resistant ovarian cancer (combo with nab-paclitaxel)",
                   "oncology.gynecologic.ovarian",
                   regions((25, 80, 100), (40, 70, 65), (200, 18, 18)),
                   slice_((10, 60, 200), (5, 50, 130), (0.5, 18, 35)),
                   {"us.priceK": "Lifyorli WAC ~$200K/yr (combo branded oncology)",
                    "us.reachPct": "Lifyorli ~10% PROC niche; first GR antagonist approved oncology"},
                   salesM=10, salesYear=2025, peakYear=2031, cagrPct=80, penPct=20)]))

    # Relacorilant Cushing's - CRL Dec 30 2025; resubmission TBD
    assets.append(asset(
        "relacorilant_cushings", "Relacorilant - selective GR antagonist for Cushing's syndrome (CRL Dec 30 2025)",
        "Phase 3 NDA pending resubmission (FDA CRL Dec 30 2025; GRACE + GRADIENT both positive; additional efficacy evidence required)",
        "small_molecule.nuclear_receptor.gr_antagonist",
        [innov_ind("cushings_rela", "Cushing's syndrome (next-gen non-steroidal selective GR antagonist; safer than mifepristone)",
                   "endocrine.pituitary.cushings",
                   regions((20, 80, 200), (30, 70, 130), (120, 25, 35)),
                   slice_((20, 70, 250), (8, 60, 150), (0.5, 25, 40)),
                   {"us.priceK": "Estimated WAC $250K/yr if approved",
                    "us.reachPct": "Relacorilant Cushing's ~20% share post-launch (vs Korlym + Recorlev/levoketoconazole)"},
                   peakYear=2032, cagrPct=0, penPct=20)]))

    # Dazucorilant - ALS Ph2 (mixed; 300mg survival hit)
    assets.append(asset(
        "dazucorilant", "Dazucorilant (CORT113176) - selective GR antagonist for ALS",
        "Phase 2 DAZALS (missed ALSFRS-R primary Dec 2024 but 300mg survival HR 0.13 p<0.0001 2-yr; ENCALS Jun 2025)",
        "small_molecule.nuclear_receptor.gr_antagonist",
        [innov_ind("als_dazu", "Amyotrophic lateral sclerosis (selective GR antagonist; survival benefit signal)",
                   "cns.neurodegeneration.als",
                   regions((30, 80, 50), (45, 70, 30), (150, 25, 8)),
                   slice_((2, 35, 100), (1, 30, 60), (0.05, 18, 15)),
                   {"us.priceK": "Estimated WAC $100K/yr ALS"},
                   peakYear=2033, cagrPct=0, penPct=10)]))

    # Profitable single-franchise commercial; Korlym recurring + Lifyorli ramp + pipeline optionality
    weights = {"mega_bear": 10, "bear": 22, "base": 38, "bull": 25, "psychedelic_bull": 5}
    crev = {"mega_bear": 700, "bear": 800, "base": 950, "bull": 1200, "psychedelic_bull": 1700}
    cmult = {"mega_bear": 4, "bear": 6, "base": 8, "bull": 11, "psychedelic_bull": 15}
    pmult = {"mega_bear": 3, "bear": 5, "base": 7, "bull": 10, "psychedelic_bull": 14}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [
        ("korlym", ["cushings_korlym"]),
        ("lifyorli", ["ovarian_proc"]),
    ]

    pos_grid = {
        # Cushing's CRL post Dec 2025 -- resubmission risk
        "relacorilant_cushings": {"mega_bear": 25, "bear": 40, "base": 55, "bull": 70, "psychedelic_bull": 82},
        # Dazucorilant ALS -- mixed Ph2; survival signal but missed primary
        "dazucorilant":          {"mega_bear": 6,  "bear": 14, "base": 25, "bull": 40, "psychedelic_bull": 55},
    }
    apr_default = {"mega_bear": 60, "bear": 75, "base": 85, "bull": 92, "psychedelic_bull": 96}
    pen_default = {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25}

    pipeline_asmps = {}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "relacorilant_cushings": OrderedDict([("cushings_rela", od(("pos", pos_grid["relacorilant_cushings"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
            "dazucorilant":          OrderedDict([("als_dazu",      od(("pos", pos_grid["dazucorilant"][sk]),          ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "Mar 25 2026"), ("dateSort", "2026-03-25"), ("asset", "lifyorli"),
           ("indication", "ovarian_proc"),
           ("title", "Lifyorli (relacorilant + nab-paclitaxel) FDA approval platinum-resistant ovarian cancer"),
           ("type", "pdufa"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Corcept Mar 25 2026 PR"), ("_confidence", "high")),
        od(("date", "Dec 30 2025"), ("dateSort", "2025-12-30"), ("asset", "relacorilant_cushings"),
           ("indication", "cushings_rela"),
           ("title", "Relacorilant Cushing's CRL (additional efficacy evidence required; resubmission TBD)"),
           ("type", "pdufa"), ("binary", True),
           ("fail_pos", 25), ("fail_apr", 65), ("success_pos", 80), ("success_apr", 90),
           ("_source", "Corcept Dec 30 2025 PR"), ("_confidence", "high")),
        od(("date", "2026-2027"), ("dateSort", "2027-06-30"), ("asset", "relacorilant_cushings"),
           ("indication", "cushings_rela"),
           ("title", "Relacorilant Cushing's NDA resubmission post-CRL (path TBD)"),
           ("type", "nda_submission"), ("binary", True),
           ("fail_pos", 30), ("fail_apr", 70), ("success_pos", 85), ("success_apr", 92),
           ("_source", "Corcept pipeline"), ("_confidence", "low")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


# ============================================================
# AUPH - Aurinia Pharmaceuticals
# ============================================================

def build_AUPH():
    co = od(
        ("ticker", "AUPH"),
        ("name", "Aurinia Pharmaceuticals Inc."),
        ("currentPrice", 14.21),
        ("sharesOut", 133),
        ("cash", 398),  # $398M YE25; no debt; net cash positive
        ("currency", "USD"),
        ("phase", "commercial"),
        ("subtitle", "Lupkynis lupus nephritis pure-play. FY25 revenue $283.1M (+20% YoY): Lupkynis US net product $271.3M (+25%) + Otsuka EU royalty/license ~$11.8M. Net income $287.2M (boosted $173M deferred tax allowance release); operating CF $135.7M (+206%); $98.2M buybacks FY25. FY26 guide: total revenue $315-325M / Lupkynis US $305-315M. Lupkynis (voclosporin) calcineurin inhibitor; FDA Jan 2021 first oral therapy specifically for active LN; standard regimen Lupkynis + MMF + low-dose steroids ('triple therapy') supported by 2024 KDIGO guideline updates driving 2025 acceleration. Competes with generic mycophenolate (Cellcept SoC backbone); GSK Benlysta/belimumab (LN labelled 2020); AZ Saphnelo/anifrolumab (SLE only). Cash $398M no debt. PIPELINE: AUR200 / aritinercept (dual BAFF/APRIL inhibitor TACI-Fc-like) -- Ph1 SAD complete (5-300mg n=61); Ph2 SLE + IgAN H1 2026 KEY CATALYST. AUR300 (CD206/M2 macrophage modulator) deprioritized. Strategic review 2024 concluded standalone; recurring buyout chatter (Sun Pharma rumors)."),
        ("yahooTicker", "AUPH"),
    )

    assets = []

    # Lupkynis - flagship LN
    assets.append(asset(
        "lupkynis", "Lupkynis (voclosporin) - calcineurin inhibitor for active lupus nephritis (first oral specifically for LN)",
        "Commercial (FDA Jan 2021; triple therapy Lupkynis+MMF+steroids; KDIGO 2024 guidelines driving 2025 acceleration)",
        "small_molecule.calcineurin_inhibitor.voclosporin",
        [innov_ind("ln_lupkynis", "Active lupus nephritis (oral cyclosporine derivative; vs MMF SoC)",
                   "nephrology.glomerular.lupus_nephritis",
                   regions((45, 75, 100), (60, 60, 65), (250, 18, 20)),
                   slice_((25, 70, 100), (8, 55, 65), (0.5, 18, 20)),
                   {"us.priceK": "Lupkynis WAC ~$100K/yr",
                    "us.reachPct": "Lupkynis ~25% LN treated population on triple therapy"},
                   salesM=271, salesYear=2025, peakYear=2030, cagrPct=18, penPct=22)]))

    # Otsuka EU royalty
    assets.append(asset(
        "otsuka_royalty", "Otsuka EU/Japan Lupkynis royalty stream",
        "Commercial royalty (Otsuka commercializes Lupkynis EU + Japan; collaboration deepening)",
        "small_molecule.calcineurin_inhibitor.voclosporin",
        [innov_ind("ln_otsuka_royalty", "Lupkynis EU + Japan royalty (Otsuka commercializes)",
                   "_platform.auph_otsuka_royalty",
                   regions((1, 1, 0.1), (1, 1, 0.1), (1, 50, 0.1)),
                   slice_((0, 0, 0), (0, 0, 0), (10, 50, 0.1)),
                   {"row.priceK": "Otsuka royalty + license tail on Lupkynis EU/Japan"},
                   salesM=12, salesYear=2025, peakYear=2030, cagrPct=20, penPct=20,
                   generic_bucket=True)]))

    # AUR200 / aritinercept - BAFF/APRIL dual inhibitor; Ph2 SLE + IgAN H1 2026
    assets.append(asset(
        "aur200", "AUR200 (aritinercept) - dual BAFF/APRIL inhibitor (TACI-Fc-like fusion protein)",
        "Phase 1 SAD complete (well tolerated 5-300mg n=61); Ph2 SLE + IgAN starts H1 2026",
        "recombinant_protein.fusion.taci_fc",
        [
            innov_ind("sle_aur200", "SLE moderate-severe (B-cell depletion via BAFF/APRIL)",
                      "immunology.autoimmune.sle",
                      regions((350, 75, 25), (450, 60, 12), (2000, 20, 3)),
                      slice_((0.3, 35, 30), (0.1, 25, 18), (0.02, 12, 5)),
                      {"us.priceK": "Estimated WAC $30K/yr SC dosing"},
                      peakYear=2033, cagrPct=0, penPct=10),
            innov_ind("igan_aur200", "IgA nephropathy (BAFF/APRIL central pathophysiology)",
                      "nephrology.glomerular.iga_nephropathy",
                      regions((25, 80, 50), (40, 65, 30), (200, 18, 10)),
                      slice_((1, 45, 40), (0.3, 35, 25), (0.03, 18, 8)),
                      {"us.priceK": "Estimated WAC $40K/yr (vs Filspari sparsentan + Tarpeyo budesonide)"},
                      peakYear=2033, cagrPct=0, penPct=10),
        ]))

    weights = {"mega_bear": 10, "bear": 22, "base": 38, "bull": 25, "psychedelic_bull": 5}
    crev = {"mega_bear": 280, "bear": 310, "base": 350, "bull": 430, "psychedelic_bull": 600}
    cmult = {"mega_bear": 3, "bear": 5, "base": 7, "bull": 10, "psychedelic_bull": 14}
    pmult = {"mega_bear": 3, "bear": 4, "base": 6, "bull": 9, "psychedelic_bull": 13}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [
        ("lupkynis", ["ln_lupkynis"]),
        ("otsuka_royalty", ["ln_otsuka_royalty"]),
    ]

    pos_grid = {
        "aur200_sle":  {"mega_bear": 12, "bear": 22, "base": 38, "bull": 55, "psychedelic_bull": 70},
        "aur200_igan": {"mega_bear": 15, "bear": 25, "base": 42, "bull": 58, "psychedelic_bull": 72},
    }
    apr_default = {"mega_bear": 60, "bear": 75, "base": 85, "bull": 92, "psychedelic_bull": 96}
    pen_default = {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25}

    pipeline_asmps = {}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "aur200": OrderedDict([
                ("sle_aur200",  od(("pos", pos_grid["aur200_sle"][sk]),  ("apr", apr_default[sk]), ("pen", pen_default[sk]))),
                ("igan_aur200", od(("pos", pos_grid["aur200_igan"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk]))),
            ]),
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "H1 2026"), ("dateSort", "2026-06-30"), ("asset", "aur200"),
           ("indication", "sle_aur200"),
           ("title", "AUR200 (aritinercept BAFF/APRIL) Ph2 SLE + IgAN initiation"),
           ("type", "phase2_start"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Aurinia FY25 release"), ("_confidence", "high")),
        od(("date", "FY 2026"), ("dateSort", "2026-12-31"), ("asset", "lupkynis"),
           ("indication", "ln_lupkynis"),
           ("title", "Lupkynis FY26 guide $305-315M US (mid-teens growth on KDIGO 2024 triple therapy adoption)"),
           ("type", "milestone"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Aurinia FY26 guidance"), ("_confidence", "high")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


# ============================================================
# FOLD - Amicus Therapeutics (BIOMARIN ACQ ANNOUNCED Dec 2025)
# ============================================================

def build_FOLD():
    co = od(
        ("ticker", "FOLD"),
        ("name", "Amicus Therapeutics, Inc."),
        ("currentPrice", 14.27),
        ("sharesOut", 308),
        # Cash $293.5M minus ~$400M Blackstone term loan = net debt ~-$107M
        ("cash", -107),
        ("currency", "USD"),
        ("phase", "commercial"),
        ("subtitle", "Lysosomal storage disease specialty (Fabry + Pompe). **BIOMARIN ACQUISITION ANNOUNCED Dec 2025 at $14.50/share cash**; FTC HSR cleared Feb 11 2026; close mid-2026 expected (deal arb at ~$14.27 vs $14.50). Per SLNO/APLS precedent, will archive once close confirmed. FY25 revenue $634.2M (+20% YoY, +17% CER): Galafold (migalastat oral chaperone for amenable Fabry mutations; FDA Aug 2018; ~50% Fabry pts amenable) $521.7M (+14%; +12% CER); Pombiliti+Opfolda (cipaglucosidase alfa + miglustat 2nd-gen ERT for late-onset Pompe; FDA Sep 2023, EU 2023) $112.5M ramping. Profitability inflection 2025 (near-GAAP profitable). Cash $293M minus Blackstone ~$400M term loan = net debt ~$107M. PIPELINE: DMX-200 (CCR2 inhibitor; Dimerix-licensed Apr 30 2025 US rights only) Ph3 ACTION3 in FSGS; deal terms $30M up + $75M reg + $35M first-sale + $410M sales milestones + low-teens/low-20s royalties."),
        ("yahooTicker", "FOLD"),
    )

    assets = []

    # Galafold - Fabry oral chaperone
    assets.append(asset(
        "galafold", "Galafold (migalastat) - oral pharmacological chaperone for amenable Fabry mutations",
        "Commercial (FDA Aug 2018; ~50% Fabry pts amenable; IP defended composition-of-matter to ~2038 US)",
        "small_molecule.chaperone.gla",
        [innov_ind("fabry_galafold", "Fabry disease (alpha-galactosidase A deficiency; oral chaperone 50% amenable)",
                   "endocrine.lysosomal_storage.fabry",
                   regions((6, 80, 250), (10, 70, 150), (40, 18, 35)),
                   slice_((50, 70, 350), (25, 60, 220), (1.5, 18, 50)),
                   {"us.priceK": "Galafold WAC ~$350K/yr",
                    "us.reachPct": "Galafold ~50% amenable Fabry US treated; Sanofi Fabrazyme ERT for non-amenable"},
                   salesM=522, salesYear=2025, peakYear=2030, cagrPct=10, penPct=35)]))

    # Pombiliti + Opfolda - 2nd-gen ERT for late-onset Pompe
    assets.append(asset(
        "pombiliti_opfolda", "Pombiliti + Opfolda (cipaglucosidase alfa + miglustat) - 2nd-gen ERT for late-onset Pompe disease",
        "Commercial (FDA Sep 2023; EU 2023; vs Sanofi Lumizyme/Nexviazyme)",
        "recombinant_protein.enzyme.gaa",
        [innov_ind("pompe_lopd", "Late-onset Pompe disease (LOPD; 2nd-gen ERT vs Sanofi Lumizyme/Nexviazyme)",
                   "endocrine.lysosomal_storage.pompe",
                   regions((4, 80, 500), (6, 70, 320), (25, 18, 80)),
                   slice_((25, 65, 600), (12, 55, 380), (1, 18, 100)),
                   {"us.priceK": "Pombiliti+Opfolda WAC ~$600K/yr (vs Lumizyme $300K, Nexviazyme $650K)",
                    "us.reachPct": "Pombiliti+Opfolda ~25% LOPD US share post-launch"},
                   salesM=113, salesYear=2025, peakYear=2030, cagrPct=40, penPct=22)]))

    # DMX-200 - CCR2 FSGS Ph3 (Dimerix-licensed)
    assets.append(asset(
        "dmx_200", "DMX-200 (repagermanium) - CCR2 inhibitor for FSGS (Dimerix-licensed Apr 30 2025 US rights only)",
        "Phase 3 ACTION3 (focal segmental glomerulosclerosis; deal $30M up + $75M reg + $35M first-sale + $410M sales milestones + low-teens/low-20s royalties)",
        "small_molecule.gpcr.ccr2_antagonist",
        [innov_ind("fsgs_dmx200", "Focal segmental glomerulosclerosis (rare progressive kidney; CCR2 monocyte/macrophage)",
                   "nephrology.glomerular.fsgs",
                   regions((40, 75, 80), (60, 60, 50), (200, 18, 12)),
                   slice_((5, 45, 80), (2, 40, 50), (0.2, 18, 12)),
                   {"us.priceK": "Estimated WAC $80K/yr if approved (vs Filspari sparsentan)",
                    "us.reachPct": "DMX-200 niche FSGS post-Filspari; CCR2 mechanism differentiated"},
                   peakYear=2032, cagrPct=0, penPct=12)]))

    # FOLD trades as deal arb -> heavy weight on $14.50 close
    weights = {"mega_bear": 5, "bear": 10, "base": 65, "bull": 15, "psychedelic_bull": 5}
    # FY25 $634M; FY26 expected ~$700M absent deal close
    crev = {"mega_bear": 600, "bear": 660, "base": 720, "bull": 850, "psychedelic_bull": 1100}
    cmult = {"mega_bear": 4, "bear": 5.5, "base": 7, "bull": 9, "psychedelic_bull": 13}
    pmult = {"mega_bear": 2, "bear": 3, "base": 5, "bull": 8, "psychedelic_bull": 12}
    pdr = {"mega_bear": 9, "bear": 8, "base": 7, "bull": 6, "psychedelic_bull": 5}

    asset_inds = [
        ("galafold", ["fabry_galafold"]),
        ("pombiliti_opfolda", ["pompe_lopd"]),
    ]

    pos_grid = {
        "dmx_200": {"mega_bear": 30, "bear": 50, "base": 70, "bull": 85, "psychedelic_bull": 92},
    }
    apr_default = {"mega_bear": 60, "bear": 75, "base": 85, "bull": 92, "psychedelic_bull": 96}
    pen_default = {"mega_bear": 0.3, "bear": 0.5, "base": 0.8, "bull": 1.05, "psychedelic_bull": 1.25}

    pipeline_asmps = {}
    for sk in ["mega_bear", "bear", "base", "bull", "psychedelic_bull"]:
        pipeline_asmps[sk] = {
            "dmx_200": OrderedDict([("fsgs_dmx200", od(("pos", pos_grid["dmx_200"][sk]), ("apr", apr_default[sk]), ("pen", pen_default[sk])))]),
        }

    scenarios = commercial_scenarios(crev, cmult, pmult, pdr, weights, asset_inds,
                                     pipeline_asmp_by_scen=pipeline_asmps)

    catalysts = [
        od(("date", "Mid 2026"), ("dateSort", "2026-07-15"), ("asset", "galafold"),
           ("indication", "fabry_galafold"),
           ("title", "BioMarin acquisition close at $14.50/share cash (FTC HSR cleared Feb 11 2026)"),
           ("type", "ma_close"), ("binary", True),
           ("fail_pos", 80), ("fail_apr", 90), ("success_pos", 100), ("success_apr", 100),
           ("_source", "BioMarin Dec 2025 PR"), ("_confidence", "high")),
        od(("date", "Apr 30 2025"), ("dateSort", "2025-04-30"), ("asset", "dmx_200"),
           ("indication", "fsgs_dmx200"),
           ("title", "Dimerix DMX-200 FSGS license $30M up + $75M reg + $410M sales milestones (US rights)"),
           ("type", "partnership"), ("binary", False),
           ("fail_pos", 100), ("fail_apr", 100), ("success_pos", 100), ("success_apr", 100),
           ("_source", "Amicus-Dimerix Apr 30 2025 PR"), ("_confidence", "high")),
        od(("date", "2026-2027"), ("dateSort", "2027-06-30"), ("asset", "dmx_200"),
           ("indication", "fsgs_dmx200"),
           ("title", "DMX-200 ACTION3 Ph3 FSGS readout"),
           ("type", "phase3_data"), ("binary", True),
           ("fail_pos", 35), ("fail_apr", 70), ("success_pos", 88), ("success_apr", 92),
           ("_source", "Dimerix ACTION3 Ph3"), ("_confidence", "medium")),
    ]

    return od(("company", co), ("assets", assets),
              ("scenarios", scenarios), ("catalysts", catalysts))


def main():
    write_config("CORT", build_CORT())
    write_config("AUPH", build_AUPH())
    write_config("FOLD", build_FOLD())

    manifest_path = CONFIGS / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for tk in ["CORT", "AUPH", "FOLD"]:
        if tk not in manifest:
            manifest.append(tk)
    manifest = sorted(set(manifest))
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"\n  manifest -> {len(manifest)} tickers")


if __name__ == "__main__":
    main()
