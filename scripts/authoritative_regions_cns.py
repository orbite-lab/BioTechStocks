# -*- coding: utf-8 -*-
"""
Authoritative slider values for CNS disease areas, extracted from tooltips_cns.py.
patientsK = treated/eligible K (addressable subset, not population prevalence).
wtpPct = market-level WTP percent.
priceK = blended price in $K.
"""

REGIONS = {
    # EPILEPSY
    "cns.epilepsy.dee": {
        "us":  {"patientsK": 30,    "wtpPct": 75, "priceK": 45},
        "eu":  {"patientsK": 35,    "wtpPct": 55, "priceK": 25},
        "row": {"patientsK": 150,   "wtpPct": 20, "priceK": 8},
    },
    "cns.epilepsy.focal": {
        "us":  {"patientsK": 1200,  "wtpPct": 85, "priceK": 4},
        "eu":  {"patientsK": 2500,  "wtpPct": 70, "priceK": 2},
        "row": {"patientsK": 18000, "wtpPct": 35, "priceK": 0.8},
    },
    "cns.epilepsy.generalized": {
        "us":  {"patientsK": 400,   "wtpPct": 85, "priceK": 3},
        "eu":  {"patientsK": 900,   "wtpPct": 70, "priceK": 1.5},
        "row": {"patientsK": 9000,  "wtpPct": 35, "priceK": 0.5},
    },

    # MOVEMENT DISORDERS
    "cns.movement.essential_tremor": {
        "us":  {"patientsK": 500,   "wtpPct": 60, "priceK": 1.5},
        "eu":  {"patientsK": 1000,  "wtpPct": 45, "priceK": 0.8},
        "row": {"patientsK": 60000, "wtpPct": 15, "priceK": 0.3},
    },
    "cns.movement.tardive_dyskinesia": {
        "us":  {"patientsK": 600,   "wtpPct": 65, "priceK": 70},
        "eu":  {"patientsK": 400,   "wtpPct": 35, "priceK": 40},
        "row": {"patientsK": 2000,  "wtpPct": 15, "priceK": 15},
    },

    # NEURODEGENERATION
    "cns.neurodegeneration.alexander": {
        "us":  {"patientsK": 0.5,   "wtpPct": 85, "priceK": 400},
        "eu":  {"patientsK": 0.6,   "wtpPct": 70, "priceK": 250},
        "row": {"patientsK": 3,     "wtpPct": 30, "priceK": 80},
    },
    "cns.neurodegeneration.als": {
        "us":  {"patientsK": 30,    "wtpPct": 70, "priceK": 40},
        "eu":  {"patientsK": 40,    "wtpPct": 45, "priceK": 20},
        "row": {"patientsK": 220,   "wtpPct": 20, "priceK": 5},
    },
    "cns.neurodegeneration.alzheimer": {
        "us":  {"patientsK": 2000,  "wtpPct": 50, "priceK": 28},
        "eu":  {"patientsK": 1500,  "wtpPct": 35, "priceK": 15},
        "row": {"patientsK": 25000, "wtpPct": 8,  "priceK": 5},
    },
    "cns.neurodegeneration.caa": {
        "us":  {"patientsK": 500,   "wtpPct": 25, "priceK": 1},
        "eu":  {"patientsK": 600,   "wtpPct": 15, "priceK": 0.5},
        "row": {"patientsK": 3000,  "wtpPct": 5,  "priceK": 0.3},
    },
    "cns.neurodegeneration.dlb": {
        "us":  {"patientsK": 1400,  "wtpPct": 55, "priceK": 2.5},
        "eu":  {"patientsK": 1600,  "wtpPct": 40, "priceK": 1},
        "row": {"patientsK": 7000,  "wtpPct": 12, "priceK": 0.5},
    },
    "cns.neurodegeneration.parkinson_disease": {
        "us":  {"patientsK": 1000,  "wtpPct": 80, "priceK": 8},
        "eu":  {"patientsK": 1200,  "wtpPct": 65, "priceK": 4},
        "row": {"patientsK": 10000, "wtpPct": 30, "priceK": 1.5},
    },
    "cns.neurodegeneration.ppa": {
        "us":  {"patientsK": 30,    "wtpPct": 30, "priceK": 3},
        "eu":  {"patientsK": 40,    "wtpPct": 20, "priceK": 1.5},
        "row": {"patientsK": 200,   "wtpPct": 8,  "priceK": 0.5},
    },
    "cns.neurodegeneration.stroke": {
        "us":  {"patientsK": 800,   "wtpPct": 90, "priceK": 12},
        "eu":  {"patientsK": 1100,  "wtpPct": 80, "priceK": 7},
        "row": {"patientsK": 12000, "wtpPct": 35, "priceK": 2},
    },

    # PAIN
    "cns.pain.migraine": {
        "us":  {"patientsK": 4000,  "wtpPct": 65, "priceK": 6},
        "eu":  {"patientsK": 6000,  "wtpPct": 45, "priceK": 3},
        "row": {"patientsK": 50000, "wtpPct": 15, "priceK": 1},
    },

    # PSYCHIATRY
    "cns.psychiatry.adhd": {
        "us":  {"patientsK": 6000,  "wtpPct": 75, "priceK": 2.5},
        "eu":  {"patientsK": 4000,  "wtpPct": 55, "priceK": 1.2},
        "row": {"patientsK": 35000, "wtpPct": 25, "priceK": 0.4},
    },
    "cns.psychiatry.anxiety": {
        "us":  {"patientsK": 6000,   "wtpPct": 75, "priceK": 0.8},
        "eu":  {"patientsK": 8000,   "wtpPct": 65, "priceK": 0.4},
        "row": {"patientsK": 300000, "wtpPct": 25, "priceK": 0.2},
    },
    "cns.psychiatry.asd": {
        "us":  {"patientsK": 2000,  "wtpPct": 40, "priceK": 3},
        "eu":  {"patientsK": 2500,  "wtpPct": 30, "priceK": 1.5},
        "row": {"patientsK": 75000, "wtpPct": 10, "priceK": 0.5},
    },
    "cns.psychiatry.depression": {
        "us":  {"patientsK": 8000,   "wtpPct": 80, "priceK": 1.5},
        "eu":  {"patientsK": 12000,  "wtpPct": 65, "priceK": 0.7},
        "row": {"patientsK": 280000, "wtpPct": 25, "priceK": 0.3},
    },
    "cns.psychiatry.opioid_dependence": {
        "us":  {"patientsK": 2000,  "wtpPct": 70, "priceK": 5},
        "eu":  {"patientsK": 1300,  "wtpPct": 60, "priceK": 2.5},
        "row": {"patientsK": 40000, "wtpPct": 15, "priceK": 0.8},
    },
    "cns.psychiatry.pain_fibromyalgia": {
        "us":  {"patientsK": 4000,  "wtpPct": 60, "priceK": 1.5},
        "eu":  {"patientsK": 5000,  "wtpPct": 40, "priceK": 0.6},
        "row": {"patientsK": 80000, "wtpPct": 15, "priceK": 0.3},
    },
    "cns.psychiatry.schizophrenia": {
        "us":  {"patientsK": 1500,  "wtpPct": 75, "priceK": 10},
        "eu":  {"patientsK": 2500,  "wtpPct": 60, "priceK": 5},
        "row": {"patientsK": 24000, "wtpPct": 25, "priceK": 1.5},
    },

    # SLEEP
    "cns.sleep.narcolepsy": {
        "us":  {"patientsK": 200,   "wtpPct": 80, "priceK": 45},
        "eu":  {"patientsK": 250,   "wtpPct": 60, "priceK": 25},
        "row": {"patientsK": 3000,  "wtpPct": 20, "priceK": 6},
    },
}

PEN_PCT = {
    "cns.epilepsy.dee": 40,
    "cns.epilepsy.focal": 70,
    "cns.epilepsy.generalized": 65,
    "cns.movement.essential_tremor": 25,
    "cns.movement.tardive_dyskinesia": 30,
    "cns.neurodegeneration.alexander": 60,
    "cns.neurodegeneration.als": 25,
    "cns.neurodegeneration.alzheimer": 12,
    "cns.neurodegeneration.caa": 8,
    "cns.neurodegeneration.dlb": 20,
    "cns.neurodegeneration.parkinson_disease": 50,
    "cns.neurodegeneration.ppa": 15,
    "cns.neurodegeneration.stroke": 40,
    "cns.pain.migraine": 35,
    "cns.psychiatry.adhd": 55,
    "cns.psychiatry.anxiety": 70,
    "cns.psychiatry.asd": 10,
    "cns.psychiatry.depression": 60,
    "cns.psychiatry.opioid_dependence": 25,
    "cns.psychiatry.pain_fibromyalgia": 30,
    "cns.psychiatry.schizophrenia": 60,
    "cns.sleep.narcolepsy": 45,
}
