# -*- coding: utf-8 -*-
"""
Authoritative slider values for immunology and dermatology disease areas.
Parsed from scripts/tooltips_immuno_derm.py.

patientsK: treated/eligible count in thousands (M converted to K).
           For aesthetics, procedures/yr used as patientsK.
wtpPct:    first "~XX%" market-level willingness-to-pay figure.
priceK:    blended annualized price per patient, in USD thousands
           (for aesthetics, per-syringe/session price in $K).
"""

REGIONS = {
    # ============================================================
    # IMMUNOLOGY - AUTOIMMUNE
    # ============================================================
    "immunology.autoimmune.fsgs": {
        "us":  {"patientsK": 40,   "wtpPct": 45, "priceK": 90},
        "eu":  {"patientsK": 45,   "wtpPct": 30, "priceK": 45},
        "row": {"patientsK": 200,  "wtpPct": 8,  "priceK": 8},
    },
    "immunology.autoimmune.hereditary_angioedema": {
        "us":  {"patientsK": 7,    "wtpPct": 75, "priceK": 450},
        "eu":  {"patientsK": 10,   "wtpPct": 55, "priceK": 280},
        "row": {"patientsK": 20,   "wtpPct": 15, "priceK": 100},
    },
    "immunology.autoimmune.iga_nephropathy": {
        "us":  {"patientsK": 130,  "wtpPct": 50, "priceK": 65},
        "eu":  {"patientsK": 150,  "wtpPct": 35, "priceK": 32},
        "row": {"patientsK": 1500, "wtpPct": 10, "priceK": 6},
    },
    "immunology.autoimmune.sjogrens": {
        "us":  {"patientsK": 1000,  "wtpPct": 25, "priceK": 8},
        "eu":  {"patientsK": 2000,  "wtpPct": 18, "priceK": 4},
        "row": {"patientsK": 15000, "wtpPct": 5,  "priceK": 1},
    },
    "immunology.autoimmune.sle": {
        "us":  {"patientsK": 300,  "wtpPct": 55, "priceK": 45},
        "eu":  {"patientsK": 350,  "wtpPct": 38, "priceK": 22},
        "row": {"patientsK": 4000, "wtpPct": 10, "priceK": 5},
    },

    # ============================================================
    # IMMUNOLOGY - INFLAMMATORY GI
    # ============================================================
    "immunology.inflammatory_gi.crohns": {
        "us":  {"patientsK": 800,  "wtpPct": 65, "priceK": 62},
        "eu":  {"patientsK": 1300, "wtpPct": 48, "priceK": 30},
        "row": {"patientsK": 2000, "wtpPct": 12, "priceK": 10},
    },
    "immunology.inflammatory_gi.ulcerative_colitis": {
        "us":  {"patientsK": 700,  "wtpPct": 62, "priceK": 55},
        "eu":  {"patientsK": 1500, "wtpPct": 45, "priceK": 28},
        "row": {"patientsK": 3000, "wtpPct": 12, "priceK": 8},
    },

    # ============================================================
    # IMMUNOLOGY - INFLAMMATORY SYSTEMIC
    # ============================================================
    "immunology.inflammatory_systemic.rheumatoid_arthritis": {
        "us":  {"patientsK": 1500,  "wtpPct": 55, "priceK": 55},
        "eu":  {"patientsK": 2900,  "wtpPct": 42, "priceK": 28},
        "row": {"patientsK": 18000, "wtpPct": 10, "priceK": 10},
    },

    # ============================================================
    # IMMUNOLOGY - NEUROMUSCULAR AUTOIMMUNE
    # ============================================================
    "immunology.neuromuscular_autoimmune.itp": {
        "us":  {"patientsK": 60,  "wtpPct": 60, "priceK": 80},
        "eu":  {"patientsK": 80,  "wtpPct": 45, "priceK": 45},
        "row": {"patientsK": 500, "wtpPct": 12, "priceK": 12},
    },
    "immunology.neuromuscular_autoimmune.mmn": {
        "us":  {"patientsK": 5,  "wtpPct": 70, "priceK": 150},
        "eu":  {"patientsK": 7,  "wtpPct": 55, "priceK": 80},
        "row": {"patientsK": 20, "wtpPct": 20, "priceK": 30},
    },
    "immunology.neuromuscular_autoimmune.myasthenia_gravis": {
        "us":  {"patientsK": 60,  "wtpPct": 65, "priceK": 280},
        "eu":  {"patientsK": 130, "wtpPct": 48, "priceK": 150},
        "row": {"patientsK": 800, "wtpPct": 12, "priceK": 25},
    },

    # ============================================================
    # DERMATOLOGY - AESTHETICS (procedures/yr as patientsK)
    # ============================================================
    "dermatology.aesthetics.filler": {
        "us":  {"patientsK": 3000,  "wtpPct": 90, "priceK": 0.8},
        "eu":  {"patientsK": 4000,  "wtpPct": 85, "priceK": 0.5},
        "row": {"patientsK": 15000, "wtpPct": 80, "priceK": 0.3},
    },
    "dermatology.aesthetics.neurotoxin": {
        "us":  {"patientsK": 5000,  "wtpPct": 92, "priceK": 0.55},
        "eu":  {"patientsK": 6000,  "wtpPct": 88, "priceK": 0.35},
        "row": {"patientsK": 25000, "wtpPct": 80, "priceK": 0.2},
    },

    # ============================================================
    # DERMATOLOGY - INFLAMMATORY
    # ============================================================
    "dermatology.inflammatory_derm.atopic_dermatitis_systemic": {
        "us":  {"patientsK": 1500,  "wtpPct": 65, "priceK": 38},
        "eu":  {"patientsK": 2500,  "wtpPct": 48, "priceK": 22},
        "row": {"patientsK": 20000, "wtpPct": 15, "priceK": 8},
    },
    "dermatology.inflammatory_derm.atopic_dermatitis_topical": {
        "us":  {"patientsK": 8000,    "wtpPct": 55, "priceK": 2},
        "eu":  {"patientsK": 12000,   "wtpPct": 45, "priceK": 0.8},
        "row": {"patientsK": 100000,  "wtpPct": 20, "priceK": 0.2},
    },
    "dermatology.inflammatory_derm.hidradenitis_suppurativa": {
        "us":  {"patientsK": 200,  "wtpPct": 55, "priceK": 45},
        "eu":  {"patientsK": 300,  "wtpPct": 40, "priceK": 22},
        "row": {"patientsK": 2000, "wtpPct": 10, "priceK": 5},
    },
    "dermatology.inflammatory_derm.psoriasis_systemic": {
        "us":  {"patientsK": 1500,  "wtpPct": 68, "priceK": 52},
        "eu":  {"patientsK": 2500,  "wtpPct": 52, "priceK": 26},
        "row": {"patientsK": 15000, "wtpPct": 15, "priceK": 8},
    },
    "dermatology.inflammatory_derm.psoriasis_topical": {
        "us":  {"patientsK": 6000,   "wtpPct": 50, "priceK": 1.5},
        "eu":  {"patientsK": 10000,  "wtpPct": 40, "priceK": 0.5},
        "row": {"patientsK": 80000,  "wtpPct": 18, "priceK": 0.1},
    },

    # ============================================================
    # DERMATOLOGY - RARE SKIN
    # ============================================================
    "dermatology.rare_skin.alopecia_areata": {
        "us":  {"patientsK": 300,  "wtpPct": 45, "priceK": 42},
        "eu":  {"patientsK": 450,  "wtpPct": 32, "priceK": 22},
        "row": {"patientsK": 4000, "wtpPct": 10, "priceK": 4},
    },
    "dermatology.rare_skin.deb": {
        "us":  {"patientsK": 3,   "wtpPct": 80, "priceK": 800},
        "eu":  {"patientsK": 4,   "wtpPct": 65, "priceK": 300},
        "row": {"patientsK": 20,  "wtpPct": 15, "priceK": 25},
    },
    "dermatology.rare_skin.hailey_hailey": {
        "us":  {"patientsK": 2,   "wtpPct": 30, "priceK": 3},
        "eu":  {"patientsK": 3,   "wtpPct": 25, "priceK": 1.5},
        "row": {"patientsK": 15,  "wtpPct": 8,  "priceK": 0.3},
    },
    "dermatology.rare_skin.vitiligo": {
        "us":  {"patientsK": 1500,  "wtpPct": 50, "priceK": 8},
        "eu":  {"patientsK": 2000,  "wtpPct": 35, "priceK": 3},
        "row": {"patientsK": 60000, "wtpPct": 12, "priceK": 0.5},
    },
    # source: Dellon 2022 EoE diagnosed prevalence ~150K US (rising); Dupixent EoE WAC ~$35K
    "immunology.inflammatory_gi.eoe": {
        "us":  {"patientsK": 150,  "wtpPct": 55, "priceK": 35},
        "eu":  {"patientsK": 120,  "wtpPct": 35, "priceK": 20},
        "row": {"patientsK": 250,  "wtpPct": 6,  "priceK": 5},
    },
    # source: Boozalis 2018 PN US prevalence ~150K severe; Dupixent PN approval 2022, WAC ~$35K
    "dermatology.inflammatory_derm.prurigo_nodularis": {
        "us":  {"patientsK": 150,  "wtpPct": 55, "priceK": 35},
        "eu":  {"patientsK": 180,  "wtpPct": 35, "priceK": 20},
        "row": {"patientsK": 800,  "wtpPct": 5,  "priceK": 4},
    },
    # source: Lee 2022 cGVHD prevalence ~14K incident/yr post-allo-SCT US;
    # actively-treated active disease ~30K prevalent. Imbruvica + Jakafi + ECP.
    "immunology.transplant.cgvhd": {
        "us":  {"patientsK": 30,  "wtpPct": 70, "priceK": 150},
        "eu":  {"patientsK": 28,  "wtpPct": 50, "priceK": 90},
        "row": {"patientsK": 60,  "wtpPct": 10, "priceK": 30},
    },
}

# Peak penetration (%) per disease area, from the penPct tooltip note.
PEN_PCT = {
    "immunology.autoimmune.fsgs": 25,
    "immunology.autoimmune.hereditary_angioedema": 70,
    "immunology.autoimmune.iga_nephropathy": 30,
    "immunology.autoimmune.sjogrens": 15,
    "immunology.autoimmune.sle": 25,
    "immunology.inflammatory_gi.crohns": 38,
    "immunology.inflammatory_gi.ulcerative_colitis": 35,
    "immunology.inflammatory_systemic.rheumatoid_arthritis": 28,
    "immunology.neuromuscular_autoimmune.itp": 35,
    "immunology.neuromuscular_autoimmune.mmn": 65,
    "immunology.neuromuscular_autoimmune.myasthenia_gravis": 40,
    "dermatology.aesthetics.filler": 5,
    "dermatology.aesthetics.neurotoxin": 12,
    "dermatology.inflammatory_derm.atopic_dermatitis_systemic": 35,
    "dermatology.inflammatory_derm.atopic_dermatitis_topical": 12,
    "dermatology.inflammatory_derm.hidradenitis_suppurativa": 25,
    "dermatology.inflammatory_derm.psoriasis_systemic": 40,
    "dermatology.inflammatory_derm.psoriasis_topical": 10,
    "dermatology.rare_skin.alopecia_areata": 20,
    "dermatology.rare_skin.deb": 60,
    "dermatology.rare_skin.hailey_hailey": 10,
    "dermatology.rare_skin.vitiligo": 15,
    "immunology.inflammatory_gi.eoe": 30,
    "dermatology.inflammatory_derm.prurigo_nodularis": 30,
    "immunology.transplant.cgvhd": 35,
}
