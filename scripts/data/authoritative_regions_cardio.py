# -*- coding: utf-8 -*-
# Authoritative slider values extracted from tooltips_cardio.py
# patientsK: primary treated/eligible number (M -> K, 1M = 1000K)
# wtpPct: first market-level WTP percentage
# priceK: blended dollar figure (M -> K, 1M = 1000K)

REGIONS = {
    # ==================== ATTR ====================
    "cardio_metabolic.attr.attr_cm": {
        "us":  {"patientsK": 120,   "wtpPct": 70, "priceK": 250},
        "eu":  {"patientsK": 90,    "wtpPct": 55, "priceK": 140},
        "row": {"patientsK": 60,    "wtpPct": 40, "priceK": 90},
    },
    "cardio_metabolic.attr.attr_pn": {
        "us":  {"patientsK": 10,    "wtpPct": 75, "priceK": 460},
        "eu":  {"patientsK": 10,    "wtpPct": 65, "priceK": 280},
        "row": {"patientsK": 8,     "wtpPct": 50, "priceK": 180},
    },

    # ==================== DIABETES ====================
    "cardio_metabolic.diabetes.t1d": {
        "us":  {"patientsK": 1900,  "wtpPct": 85, "priceK": 5},
        "eu":  {"patientsK": 1500,  "wtpPct": 80, "priceK": 2.5},
        "row": {"patientsK": 8000,  "wtpPct": 40, "priceK": 1},
    },
    "cardio_metabolic.diabetes.t2d": {
        "us":  {"patientsK": 25000, "wtpPct": 90, "priceK": 4},
        "eu":  {"patientsK": 22000, "wtpPct": 85, "priceK": 2},
        "row": {"patientsK": 150000,"wtpPct": 45, "priceK": 0.6},
    },

    # ==================== HYPERTENSION ====================
    "cardio_metabolic.hypertension.agt_knockdown": {
        "us":  {"patientsK": 10000, "wtpPct": 25, "priceK": 8},
        "eu":  {"patientsK": 8000,  "wtpPct": 15, "priceK": 4},
        "row": {"patientsK": 60000, "wtpPct": 5,  "priceK": 2},
    },

    # ==================== LIPIDS ====================
    "cardio_metabolic.lipids.ldl_cv_risk": {
        "us":  {"patientsK": 20000, "wtpPct": 70, "priceK": 5},
        "eu":  {"patientsK": 25000, "wtpPct": 60, "priceK": 2.5},
        "row": {"patientsK": 40000, "wtpPct": 30, "priceK": 0.8},
    },
    "cardio_metabolic.lipids.lpa": {
        "us":  {"patientsK": 100,   "wtpPct": 40, "priceK": 8},
        "eu":  {"patientsK": 60,    "wtpPct": 25, "priceK": 4},
        "row": {"patientsK": 80,    "wtpPct": 10, "priceK": 2},
    },
    "cardio_metabolic.lipids.triglycerides": {
        "us":  {"patientsK": 4,     "wtpPct": 60, "priceK": 300},
        "eu":  {"patientsK": 5,     "wtpPct": 50, "priceK": 180},
        "row": {"patientsK": 15,    "wtpPct": 20, "priceK": 100},
    },

    # ==================== LIVER ====================
    "cardio_metabolic.liver.a1at": {
        "us":  {"patientsK": 10,    "wtpPct": 70, "priceK": 150},
        "eu":  {"patientsK": 20,    "wtpPct": 55, "priceK": 90},
        "row": {"patientsK": 8,     "wtpPct": 30, "priceK": 50},
    },
    "cardio_metabolic.liver.hbv_functional_cure": {
        "us":  {"patientsK": 800,   "wtpPct": 60, "priceK": 15},
        "eu":  {"patientsK": 1500,  "wtpPct": 50, "priceK": 8},
        "row": {"patientsK": 50000, "wtpPct": 15, "priceK": 0.3},
    },
    "cardio_metabolic.liver.mash": {
        "us":  {"patientsK": 6000,  "wtpPct": 45, "priceK": 47},
        "eu":  {"patientsK": 4000,  "wtpPct": 30, "priceK": 25},
        "row": {"patientsK": 15000, "wtpPct": 10, "priceK": 12},
    },
    "cardio_metabolic.liver.pld_adpkd": {
        "us":  {"patientsK": 20,    "wtpPct": 65, "priceK": 13},
        "eu":  {"patientsK": 25,    "wtpPct": 55, "priceK": 7},
        "row": {"patientsK": 30,    "wtpPct": 25, "priceK": 4},
    },

    # ==================== OBESITY ====================
    "cardio_metabolic.obesity.general": {
        "us":  {"patientsK": 40000, "wtpPct": 50, "priceK": 15},
        "eu":  {"patientsK": 30000, "wtpPct": 35, "priceK": 8},
        "row": {"patientsK": 50000, "wtpPct": 8,  "priceK": 3},
    },
    "cardio_metabolic.obesity.rare_genetic.hypothalamic_obesity": {
        "us":  {"patientsK": 10,    "wtpPct": 70, "priceK": 325},
        "eu":  {"patientsK": 8,     "wtpPct": 55, "priceK": 200},
        "row": {"patientsK": 15,    "wtpPct": 30, "priceK": 120},
    },
    "cardio_metabolic.obesity.rare_genetic.monogenic_mc4r": {
        "us":  {"patientsK": 4.3,   "wtpPct": 80, "priceK": 325},
        "eu":  {"patientsK": 4,     "wtpPct": 65, "priceK": 200},
        "row": {"patientsK": 8,     "wtpPct": 35, "priceK": 120},
    },
    "cardio_metabolic.obesity.rare_genetic.prader_willi": {
        "us":  {"patientsK": 15,    "wtpPct": 75, "priceK": 300},
        "eu":  {"patientsK": 15,    "wtpPct": 60, "priceK": 180},
        "row": {"patientsK": 30,    "wtpPct": 30, "priceK": 80},
    },

    # ==================== RARE METABOLIC ====================
    "cardio_metabolic.rare_metabolic.homocystinuria": {
        "us":  {"patientsK": 1.5,   "wtpPct": 70, "priceK": 400},
        "eu":  {"patientsK": 2,     "wtpPct": 55, "priceK": 250},
        "row": {"patientsK": 3,     "wtpPct": 25, "priceK": 120},
    },
    "cardio_metabolic.rare_metabolic.hyperoxaluria": {
        "us":  {"patientsK": 0.4,   "wtpPct": 80, "priceK": 495},
        "eu":  {"patientsK": 0.5,   "wtpPct": 65, "priceK": 300},
        "row": {"patientsK": 1,     "wtpPct": 35, "priceK": 180},
    },
    "cardio_metabolic.rare_metabolic.porphyria": {
        "us":  {"patientsK": 1,     "wtpPct": 75, "priceK": 575},
        "eu":  {"patientsK": 4,     "wtpPct": 60, "priceK": 350},
        "row": {"patientsK": 2,     "wtpPct": 30, "priceK": 200},
    },

    # ==================== THROMBOSIS ====================
    "cardio_metabolic.thrombosis.anticoagulation": {
        "us":  {"patientsK": 8000,  "wtpPct": 85, "priceK": 5},
        "eu":  {"patientsK": 7000,  "wtpPct": 75, "priceK": 2.5},
        "row": {"patientsK": 40000, "wtpPct": 40, "priceK": 0.8},
    },

    # ==================== ENDOCRINE: ADRENAL ====================
    "endocrine.adrenal.cah": {
        "us":  {"patientsK": 15,    "wtpPct": 75, "priceK": 160},
        "eu":  {"patientsK": 25,    "wtpPct": 60, "priceK": 90},
        "row": {"patientsK": 40,    "wtpPct": 30, "priceK": 40},
    },

    # ==================== ENDOCRINE: CALCIUM ====================
    "endocrine.calcium.adh1": {
        "us":  {"patientsK": 10,    "wtpPct": 70, "priceK": 250},
        "eu":  {"patientsK": 12,    "wtpPct": 55, "priceK": 150},
        "row": {"patientsK": 15,    "wtpPct": 25, "priceK": 80},
    },

    # ==================== ENDOCRINE: PITUITARY ====================
    "endocrine.pituitary.acromegaly": {
        "us":  {"patientsK": 8,     "wtpPct": 75, "priceK": 80},
        "eu":  {"patientsK": 10,    "wtpPct": 65, "priceK": 45},
        "row": {"patientsK": 15,    "wtpPct": 35, "priceK": 20},
    },

    # ==================== ENDOCRINE: THYROID ====================
    "endocrine.thyroid.graves": {
        "us":  {"patientsK": 100,   "wtpPct": 70, "priceK": 350},
        "eu":  {"patientsK": 80,    "wtpPct": 50, "priceK": 200},
        "row": {"patientsK": 150,   "wtpPct": 20, "priceK": 100},
    },
    # source: NORD HoFH prevalence ~1 in 250K (US ~1.3K, EU ~2K), Evkeeza WAC ~$450K/yr
    "cardio_metabolic.lipids.hofh": {
        "us":  {"patientsK": 1.5,   "wtpPct": 75, "priceK": 450},
        "eu":  {"patientsK": 2,     "wtpPct": 60, "priceK": 300},
        "row": {"patientsK": 10,    "wtpPct": 8,  "priceK": 80},
    },
}

PEN_PCT = {
    "cardio_metabolic.attr.attr_cm": 45,
    "cardio_metabolic.attr.attr_pn": 55,
    "cardio_metabolic.diabetes.t1d": 12,
    "cardio_metabolic.diabetes.t2d": 10,
    "cardio_metabolic.hypertension.agt_knockdown": 8,
    "cardio_metabolic.lipids.ldl_cv_risk": 6,
    "cardio_metabolic.lipids.lpa": 3,
    "cardio_metabolic.lipids.triglycerides": 25,
    "cardio_metabolic.liver.a1at": 15,
    "cardio_metabolic.liver.hbv_functional_cure": 4,
    "cardio_metabolic.liver.mash": 8,
    "cardio_metabolic.liver.pld_adpkd": 15,
    "cardio_metabolic.obesity.general": 5,
    "cardio_metabolic.obesity.rare_genetic.hypothalamic_obesity": 30,
    "cardio_metabolic.obesity.rare_genetic.monogenic_mc4r": 35,
    "cardio_metabolic.obesity.rare_genetic.prader_willi": 40,
    "cardio_metabolic.rare_metabolic.homocystinuria": 30,
    "cardio_metabolic.rare_metabolic.hyperoxaluria": 50,
    "cardio_metabolic.rare_metabolic.porphyria": 40,
    "cardio_metabolic.thrombosis.anticoagulation": 4,
    "endocrine.adrenal.cah": 35,
    "endocrine.calcium.adh1": 25,
    "endocrine.pituitary.acromegaly": 20,
    "endocrine.thyroid.graves": 15,
    "cardio_metabolic.lipids.hofh": 35,
}
