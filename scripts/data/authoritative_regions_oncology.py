# -*- coding: utf-8 -*-
"""Authoritative region values extracted from tooltips_oncology.py.

For each taxonomy area, the {us, eu, row} x {patientsK, wtpPct, priceK}
values represent the single authoritative slider value reconciled from
the narrative tooltips (prevalent/treated/on-tx preferred; blended price
preferred; market-level WTP %).
"""

REGIONS = {
    # ------------------------------------------------------------
    # BREAST
    # ------------------------------------------------------------
    "oncology.breast.her2_pos": {
        "us":  {"patientsK": 120, "wtpPct": 70, "priceK": 165},
        "eu":  {"patientsK": 140, "wtpPct": 50, "priceK": 95},
        "row": {"patientsK": 200, "wtpPct": 18, "priceK": 35},
    },
    "oncology.breast.hr_her2_neg": {
        "us":  {"patientsK": 400, "wtpPct": 75, "priceK": 95},
        "eu":  {"patientsK": 450, "wtpPct": 55, "priceK": 55},
        "row": {"patientsK": 550, "wtpPct": 20, "priceK": 20},
    },
    "oncology.breast.tnbc": {
        "us":  {"patientsK": 60,  "wtpPct": 65, "priceK": 140},
        "eu":  {"patientsK": 65,  "wtpPct": 48, "priceK": 80},
        "row": {"patientsK": 120, "wtpPct": 15, "priceK": 30},
    },

    # ------------------------------------------------------------
    # GENITOURINARY
    # ------------------------------------------------------------
    "oncology.genitourinary.bladder": {
        "us":  {"patientsK": 25, "wtpPct": 62, "priceK": 185},
        "eu":  {"patientsK": 28, "wtpPct": 45, "priceK": 105},
        "row": {"patientsK": 80, "wtpPct": 14, "priceK": 35},
    },
    "oncology.genitourinary.prostate": {
        "us":  {"patientsK": 100, "wtpPct": 70, "priceK": 95},
        "eu":  {"patientsK": 110, "wtpPct": 52, "priceK": 55},
        "row": {"patientsK": 200, "wtpPct": 18, "priceK": 18},
    },
    "oncology.genitourinary.rcc": {
        "us":  {"patientsK": 25, "wtpPct": 68, "priceK": 215},
        "eu":  {"patientsK": 30, "wtpPct": 50, "priceK": 125},
        "row": {"patientsK": 70, "wtpPct": 16, "priceK": 40},
    },

    # ------------------------------------------------------------
    # GI
    # ------------------------------------------------------------
    "oncology.gi.cholangiocarcinoma": {
        "us":  {"patientsK": 10, "wtpPct": 55, "priceK": 155},
        "eu":  {"patientsK": 12, "wtpPct": 42, "priceK": 90},
        "row": {"patientsK": 60, "wtpPct": 12, "priceK": 30},
    },
    "oncology.gi.colorectal": {
        "us":  {"patientsK": 55,  "wtpPct": 65, "priceK": 95},
        "eu":  {"patientsK": 70,  "wtpPct": 48, "priceK": 55},
        "row": {"patientsK": 320, "wtpPct": 16, "priceK": 22},
    },
    "oncology.gi.gastric_esoph": {
        "us":  {"patientsK": 25,  "wtpPct": 58, "priceK": 135},
        "eu":  {"patientsK": 35,  "wtpPct": 44, "priceK": 78},
        "row": {"patientsK": 800, "wtpPct": 20, "priceK": 32},
    },
    "oncology.gi.hcc": {
        "us":  {"patientsK": 20,  "wtpPct": 60, "priceK": 135},
        "eu":  {"patientsK": 25,  "wtpPct": 46, "priceK": 78},
        "row": {"patientsK": 650, "wtpPct": 22, "priceK": 28},
    },
    "oncology.gi.pancreatic": {
        "us":  {"patientsK": 45,  "wtpPct": 55, "priceK": 70},
        "eu":  {"patientsK": 60,  "wtpPct": 42, "priceK": 40},
        "row": {"patientsK": 250, "wtpPct": 14, "priceK": 15},
    },

    # ------------------------------------------------------------
    # GYNECOLOGIC
    # ------------------------------------------------------------
    "oncology.gynecologic.ovarian": {
        "us":  {"patientsK": 35, "wtpPct": 65, "priceK": 125},
        "eu":  {"patientsK": 50, "wtpPct": 50, "priceK": 72},
        "row": {"patientsK": 90, "wtpPct": 16, "priceK": 25},
    },

    # ------------------------------------------------------------
    # HEMATOLOGY
    # ------------------------------------------------------------
    "oncology.hematology.aml": {
        "us":  {"patientsK": 22, "wtpPct": 62, "priceK": 185},
        "eu":  {"patientsK": 27, "wtpPct": 45, "priceK": 105},
        "row": {"patientsK": 90, "wtpPct": 14, "priceK": 35},
    },
    # ------------------------------------------------------------
    # HEMATOLOGIC MALIGNANCIES -- CLL split from NHL (medically distinct);
    # NHL groups all B-cell + T-cell lymphomas with disease-specific L4s.
    # Patient counts are annual treated cohorts (not raw incidence) because
    # most drugs are continuous chronic therapy.
    # source: SEER, NORD, Lymphoma Research Foundation
    # ------------------------------------------------------------

    # CLL: chronic lymphocytic leukemia. ~21K US incident, ~80K actively-treated
    # prevalent (5-10yr median OS on BTK/BCL2). Supports the ~$10B WW BTK+BCL2 spend.
    "oncology.hematology.cll": {
        "us":  {"patientsK": 80,  "wtpPct": 70, "priceK": 100},
        "eu":  {"patientsK": 95,  "wtpPct": 50, "priceK": 60},
        "row": {"patientsK": 150, "wtpPct": 12, "priceK": 25},
    },

    # NHL parent (legacy aggregate). Sub-segments below.
    "oncology.hematology.nhl": {
        "us":  {"patientsK": 80, "wtpPct": 60, "priceK": 150},
        "eu":  {"patientsK": 90, "wtpPct": 45, "priceK": 90},
        "row": {"patientsK": 200, "wtpPct": 12, "priceK": 35},
    },
    # DLBCL: diffuse large B-cell lymphoma. Most common aggressive NHL.
    # Curative intent 1L (R-CHOP); 2L+ market for CAR-T + bispecifics + Polivy combos.
    "oncology.hematology.nhl.dlbcl": {
        "us":  {"patientsK": 40,  "wtpPct": 68, "priceK": 195},
        "eu":  {"patientsK": 38,  "wtpPct": 50, "priceK": 115},
        "row": {"patientsK": 120, "wtpPct": 15, "priceK": 40},
    },
    # FL + iNHL: indolent B-cell lymphoma; many on watch-and-wait initially.
    # Treatment mix: rituximab/lenalidomide/bispecifics/CAR-T.
    "oncology.hematology.nhl.fl": {
        "us":  {"patientsK": 14, "wtpPct": 65, "priceK": 80},
        "eu":  {"patientsK": 17, "wtpPct": 48, "priceK": 50},
        "row": {"patientsK": 30, "wtpPct": 12, "priceK": 20},
    },
    # MCL: mantle cell lymphoma; aggressive but treatable.
    # BTK first-line, CAR-T (Tecartus) post-BTKi.
    "oncology.hematology.nhl.mcl": {
        "us":  {"patientsK": 5, "wtpPct": 70, "priceK": 120},
        "eu":  {"patientsK": 6, "wtpPct": 52, "priceK": 75},
        "row": {"patientsK": 10, "wtpPct": 10, "priceK": 30},
    },
    # WM: Waldenstrom macroglobulinemia / lymphoplasmacytic lymphoma. Rare;
    # BTK inhibitors are 1L standard (Brukinsa, Imbruvica), rituximab combos.
    "oncology.hematology.nhl.wm": {
        "us":  {"patientsK": 5,  "wtpPct": 70, "priceK": 180},
        "eu":  {"patientsK": 6,  "wtpPct": 52, "priceK": 110},
        "row": {"patientsK": 12, "wtpPct": 10, "priceK": 35},
    },
    # MZL: marginal zone lymphoma (splenic, nodal, MALT).
    # BTK + lenalidomide-rituximab + CAR-T expanding.
    "oncology.hematology.nhl.mzl": {
        "us":  {"patientsK": 7,  "wtpPct": 65, "priceK": 100},
        "eu":  {"patientsK": 9,  "wtpPct": 48, "priceK": 60},
        "row": {"patientsK": 18, "wtpPct": 12, "priceK": 25},
    },
    # T-cell lymphomas (PTCL, CTCL, etc). Smaller market; Soquelitinib (CRVS)
    # + Adcetris + romidepsin + CAR-T pipeline.
    "oncology.hematology.nhl.tcell": {
        "us":  {"patientsK": 8,  "wtpPct": 60, "priceK": 130},
        "eu":  {"patientsK": 10, "wtpPct": 42, "priceK": 75},
        "row": {"patientsK": 20, "wtpPct": 10, "priceK": 28},
    },
    "oncology.hematology.myeloma": {
        "us":  {"patientsK": 160, "wtpPct": 65, "priceK": 235},
        "eu":  {"patientsK": 180, "wtpPct": 48, "priceK": 140},
        "row": {"patientsK": 300, "wtpPct": 16, "priceK": 50},
    },
    # MM line-of-therapy L4 sub-segments. Patient counts approximate the
    # cohort actively treated in that line annually (incidence x line-share x survival).
    # 1L = newly diagnosed, frontline regimens (RVd, dara-RVd combos)
    # 2l_3l = early relapse after 1-2 prior lines (Carvykti current label, daratumumab combos)
    # 4l_plus = heavily pre-treated R/R, where bispecifics + cell therapies live
    "oncology.hematology.myeloma.1l": {
        "us":  {"patientsK": 32, "wtpPct": 75, "priceK": 220},
        "eu":  {"patientsK": 36, "wtpPct": 58, "priceK": 130},
        "row": {"patientsK": 80, "wtpPct": 18, "priceK": 55},
    },
    "oncology.hematology.myeloma.2l_3l": {
        "us":  {"patientsK": 24, "wtpPct": 65, "priceK": 280},
        "eu":  {"patientsK": 28, "wtpPct": 50, "priceK": 165},
        "row": {"patientsK": 50, "wtpPct": 14, "priceK": 60},
    },
    "oncology.hematology.myeloma.4l_plus": {
        "us":  {"patientsK": 12, "wtpPct": 55, "priceK": 380},
        "eu":  {"patientsK": 14, "wtpPct": 42, "priceK": 220},
        "row": {"patientsK": 20, "wtpPct": 10, "priceK": 80},
    },
    # (oncology.hematology.tcell_lymphoma renamed to oncology.hematology.nhl.tcell above)

    # ------------------------------------------------------------
    # LUNG - NSCLC DRIVER SUBTYPES
    # ------------------------------------------------------------
    "oncology.lung.nsclc_driver.alk": {
        "us":  {"patientsK": 6,  "wtpPct": 72, "priceK": 205},
        "eu":  {"patientsK": 7,  "wtpPct": 55, "priceK": 120},
        "row": {"patientsK": 15, "wtpPct": 22, "priceK": 55},
    },
    "oncology.lung.nsclc_driver.cmet": {
        "us":  {"patientsK": 3,  "wtpPct": 60, "priceK": 195},
        "eu":  {"patientsK": 4,  "wtpPct": 45, "priceK": 115},
        "row": {"patientsK": 10, "wtpPct": 16, "priceK": 45},
    },
    "oncology.lung.nsclc_driver.her2": {
        "us":  {"patientsK": 4,  "wtpPct": 62, "priceK": 195},
        "eu":  {"patientsK": 5,  "wtpPct": 46, "priceK": 115},
        "row": {"patientsK": 12, "wtpPct": 15, "priceK": 50},
    },
    "oncology.lung.nsclc_driver.her3": {
        "us":  {"patientsK": 15, "wtpPct": 55, "priceK": 195},
        "eu":  {"patientsK": 20, "wtpPct": 40, "priceK": 115},
        "row": {"patientsK": 60, "wtpPct": 14, "priceK": 45},
    },
    "oncology.lung.nsclc_driver.kras": {
        "us":  {"patientsK": 20, "wtpPct": 62, "priceK": 185},
        "eu":  {"patientsK": 28, "wtpPct": 46, "priceK": 110},
        "row": {"patientsK": 60, "wtpPct": 15, "priceK": 45},
    },
    "oncology.lung.nsclc_driver.other": {
        "us":  {"patientsK": 8,  "wtpPct": 65, "priceK": 210},
        "eu":  {"patientsK": 10, "wtpPct": 48, "priceK": 125},
        "row": {"patientsK": 25, "wtpPct": 16, "priceK": 50},
    },
    "oncology.lung.nsclc_driver.ros1": {
        "us":  {"patientsK": 3, "wtpPct": 70, "priceK": 215},
        "eu":  {"patientsK": 3, "wtpPct": 52, "priceK": 125},
        "row": {"patientsK": 7, "wtpPct": 20, "priceK": 55},
    },
    "oncology.lung.nsclc_driver.trop2": {
        "us":  {"patientsK": 40,  "wtpPct": 58, "priceK": 175},
        "eu":  {"patientsK": 55,  "wtpPct": 42, "priceK": 105},
        "row": {"patientsK": 180, "wtpPct": 14, "priceK": 40},
    },
    "oncology.lung.nsclc_undruggable": {
        "us":  {"patientsK": 30,  "wtpPct": 65, "priceK": 135},
        "eu":  {"patientsK": 45,  "wtpPct": 48, "priceK": 80},
        "row": {"patientsK": 180, "wtpPct": 18, "priceK": 30},
    },

    # ------------------------------------------------------------
    # LUNG - SCLC
    # ------------------------------------------------------------
    "oncology.lung.sclc": {
        "us":  {"patientsK": 22,  "wtpPct": 60, "priceK": 125},
        "eu":  {"patientsK": 28,  "wtpPct": 44, "priceK": 72},
        "row": {"patientsK": 180, "wtpPct": 14, "priceK": 28},
    },

    # ------------------------------------------------------------
    # (oncology.multi_tumor.* removed -- platform/discovery indications without
    # specific lead diseases now use the _platform.* pseudo-area, which the
    # Market Explorer filters out by convention. These are visible in the
    # Technology Explorer where platforms belong.)

    # ------------------------------------------------------------
    # NEUROENDOCRINE
    # ------------------------------------------------------------
    "oncology.neuroendocrine.gepnet": {
        "us":  {"patientsK": 12, "wtpPct": 62, "priceK": 110},
        "eu":  {"patientsK": 15, "wtpPct": 48, "priceK": 65},
        "row": {"patientsK": 40, "wtpPct": 16, "priceK": 22},
    },

    # ------------------------------------------------------------
    # HEMATOLOGY - RARE BLOOD
    # ------------------------------------------------------------
    "hematology.rare_blood.hemoglobinopathy": {
        "us":  {"patientsK": 20,   "wtpPct": 45, "priceK": 2200},
        "eu":  {"patientsK": 75,   "wtpPct": 32, "priceK": 1600},
        "row": {"patientsK": 5200, "wtpPct": 6,  "priceK": 200},
    },

    # ------------------------------------------------------------
    # SKIN ONCOLOGY (cscc / bcc / melanoma) -- IO regimens dominate
    # ------------------------------------------------------------
    # source: SEER advanced/metastatic melanoma incidence ~30K US/yr;
    # IO regimen avg ~$180K (Opdivo+Yervoy / pembro)
    "oncology.skin.melanoma": {
        "us":  {"patientsK": 30,  "wtpPct": 75, "priceK": 180},
        "eu":  {"patientsK": 35,  "wtpPct": 60, "priceK": 100},
        "row": {"patientsK": 80,  "wtpPct": 12, "priceK": 40},
    },
    # source: Karia 2013 advanced cSCC US ~20K; Libtayo WAC ~$200K
    "oncology.skin.cscc": {
        "us":  {"patientsK": 20,  "wtpPct": 70, "priceK": 200},
        "eu":  {"patientsK": 25,  "wtpPct": 55, "priceK": 110},
        "row": {"patientsK": 50,  "wtpPct": 10, "priceK": 40},
    },
    # source: NCI advanced/metastatic BCC US ~12K; Libtayo / sonidegib pricing ~$200K
    "oncology.skin.bcc": {
        "us":  {"patientsK": 12,  "wtpPct": 70, "priceK": 200},
        "eu":  {"patientsK": 15,  "wtpPct": 55, "priceK": 110},
        "row": {"patientsK": 30,  "wtpPct": 10, "priceK": 40},
    },
}


PEN_PCT = {
    "oncology.breast.her2_pos": 65,
    "oncology.breast.hr_her2_neg": 58,
    "oncology.breast.tnbc": 55,
    "oncology.genitourinary.bladder": 50,
    "oncology.genitourinary.prostate": 60,
    "oncology.genitourinary.rcc": 58,
    "oncology.gi.cholangiocarcinoma": 42,
    "oncology.gi.colorectal": 50,
    "oncology.gi.gastric_esoph": 48,
    "oncology.gi.hcc": 45,
    "oncology.gi.pancreatic": 40,
    "oncology.gynecologic.ovarian": 52,
    "oncology.hematology.aml": 48,
    "oncology.hematology.cll": 65,
    "oncology.hematology.nhl": 35,
    "oncology.hematology.nhl.dlbcl": 55,
    "oncology.hematology.nhl.fl": 45,
    "oncology.hematology.nhl.mcl": 50,
    "oncology.hematology.nhl.wm": 55,
    "oncology.hematology.nhl.mzl": 40,
    "oncology.hematology.nhl.tcell": 40,
    "oncology.hematology.myeloma": 58,
    "oncology.hematology.myeloma.1l": 70,
    "oncology.hematology.myeloma.2l_3l": 55,
    "oncology.hematology.myeloma.4l_plus": 35,
    # tcell_lymphoma renamed -> nhl.tcell (above)
    "oncology.lung.nsclc_driver.alk": 68,
    "oncology.lung.nsclc_driver.cmet": 50,
    "oncology.lung.nsclc_driver.her2": 48,
    "oncology.lung.nsclc_driver.her3": 42,
    "oncology.lung.nsclc_driver.kras": 50,
    "oncology.lung.nsclc_driver.other": 55,
    "oncology.lung.nsclc_driver.ros1": 65,
    "oncology.lung.nsclc_driver.trop2": 45,
    "oncology.lung.nsclc_undruggable": 55,
    "oncology.lung.sclc": 48,
    # (multi_tumor.* removed -- now _platform.*)
    "oncology.neuroendocrine.gepnet": 50,
    "hematology.rare_blood.hemoglobinopathy": 18,
    "oncology.skin.melanoma": 65,
    "oncology.skin.cscc": 50,
    "oncology.skin.bcc": 45,
}


if __name__ == "__main__":
    print(f"Total areas: {len(REGIONS)}")
    assert set(REGIONS.keys()) == set(PEN_PCT.keys()), "REGIONS and PEN_PCT keys must match"
    for key in sorted(REGIONS.keys()):
        print(f"  {key}: pen={PEN_PCT[key]}%")
