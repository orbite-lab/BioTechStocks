# -*- coding: utf-8 -*-
"""
Apply real epidemiological and pricing data to all config files.

For each indication in each config, if the indication's `area` tag matches
a key in REAL_MARKETS, overwrite `market.regions` with the curated data
and add a sources annotation.  All other market fields (tamB, cagrPct,
penPct, peakYear, notes, salesM, salesYear, company_slice, etc.) are
preserved as-is.

Usage:
    python scripts/real_epi_data.py          # preview (dry-run)
    python scripts/real_epi_data.py --write  # actually write files

Data sources: consensus epi estimates (Datamonitor, GlobalData, company
10-Ks, FDA/EMA labels, NORD, Orphanet) and average drug-class net pricing
(SSR Health, 46brooklyn, Visible Alpha).  Values are rounded to reflect
market-level averages, not single-drug precision.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT / "configs"

# ---------------------------------------------------------------------------
# REAL_MARKETS: curated regional epi + pricing for 108 L3 area tags
#
# Keys:
#   patientsK  -- thousands of diagnosed/treated patients per year
#   wtpPct     -- willingness-to-pay / reimbursed access (%)
#   priceK     -- average annual treatment cost ($K)
#
# Addressable per region = patientsK * 1000 * (wtpPct/100) * priceK * 1000
# ---------------------------------------------------------------------------

REAL_MARKETS = {

    # ======================================================================
    # ONCOLOGY (23)
    # ======================================================================

    "oncology.breast.her2_pos": {
        "us":  {"patientsK": 300,  "wtpPct": 65, "priceK": 180},
        "eu":  {"patientsK": 350,  "wtpPct": 50, "priceK": 100},
        "row": {"patientsK": 500,  "wtpPct": 12, "priceK": 45},
    },
    "oncology.breast.tnbc": {
        "us":  {"patientsK": 50,   "wtpPct": 60, "priceK": 200},
        "eu":  {"patientsK": 55,   "wtpPct": 45, "priceK": 110},
        "row": {"patientsK": 80,   "wtpPct": 10, "priceK": 45},
    },
    "oncology.gi.cholangiocarcinoma": {
        "us":  {"patientsK": 12,   "wtpPct": 65, "priceK": 200},
        "eu":  {"patientsK": 14,   "wtpPct": 50, "priceK": 110},
        "row": {"patientsK": 25,   "wtpPct": 10, "priceK": 45},
    },
    "oncology.gi.colorectal": {
        "us":  {"patientsK": 150,  "wtpPct": 60, "priceK": 180},
        "eu":  {"patientsK": 170,  "wtpPct": 45, "priceK": 100},
        "row": {"patientsK": 350,  "wtpPct": 10, "priceK": 40},
    },
    "oncology.gi.gastric_esoph": {
        "us":  {"patientsK": 45,   "wtpPct": 60, "priceK": 190},
        "eu":  {"patientsK": 55,   "wtpPct": 45, "priceK": 105},
        "row": {"patientsK": 300,  "wtpPct": 8,  "priceK": 40},
    },
    "oncology.gi.hcc": {
        "us":  {"patientsK": 35,   "wtpPct": 60, "priceK": 200},
        "eu":  {"patientsK": 40,   "wtpPct": 45, "priceK": 110},
        "row": {"patientsK": 400,  "wtpPct": 7,  "priceK": 40},
    },
    "oncology.gi.pancreatic": {
        "us":  {"patientsK": 60,   "wtpPct": 55, "priceK": 180},
        "eu":  {"patientsK": 65,   "wtpPct": 42, "priceK": 100},
        "row": {"patientsK": 120,  "wtpPct": 8,  "priceK": 40},
    },
    "oncology.hematology.aml": {
        "us":  {"patientsK": 22,   "wtpPct": 65, "priceK": 220},
        "eu":  {"patientsK": 25,   "wtpPct": 50, "priceK": 120},
        "row": {"patientsK": 35,   "wtpPct": 12, "priceK": 50},
    },
    "oncology.hematology.cll_nhl": {
        "us":  {"patientsK": 180,  "wtpPct": 65, "priceK": 180},
        "eu":  {"patientsK": 200,  "wtpPct": 48, "priceK": 100},
        "row": {"patientsK": 250,  "wtpPct": 12, "priceK": 40},
    },
    "oncology.hematology.myeloma": {
        "us":  {"patientsK": 35,   "wtpPct": 70, "priceK": 220},
        "eu":  {"patientsK": 40,   "wtpPct": 50, "priceK": 120},
        "row": {"patientsK": 50,   "wtpPct": 12, "priceK": 50},
    },
    "oncology.lung.nsclc_driver": {
        "us":  {"patientsK": 60,   "wtpPct": 65, "priceK": 200},
        "eu":  {"patientsK": 65,   "wtpPct": 50, "priceK": 110},
        "row": {"patientsK": 150,  "wtpPct": 10, "priceK": 45},
    },
    "oncology.lung.nsclc_io": {
        "us":  {"patientsK": 130,  "wtpPct": 60, "priceK": 200},
        "eu":  {"patientsK": 140,  "wtpPct": 45, "priceK": 110},
        "row": {"patientsK": 300,  "wtpPct": 10, "priceK": 45},
    },
    "oncology.prostate.crpc": {
        "us":  {"patientsK": 45,   "wtpPct": 60, "priceK": 170},
        "eu":  {"patientsK": 50,   "wtpPct": 45, "priceK": 95},
        "row": {"patientsK": 80,   "wtpPct": 10, "priceK": 40},
    },
    "oncology.rare_onc.bcc_advanced": {
        "us":  {"patientsK": 4,    "wtpPct": 70, "priceK": 200},
        "eu":  {"patientsK": 4.5,  "wtpPct": 55, "priceK": 110},
        "row": {"patientsK": 5,    "wtpPct": 12, "priceK": 45},
    },
    "oncology.rare_onc.met_rcc": {
        "us":  {"patientsK": 40,   "wtpPct": 65, "priceK": 200},
        "eu":  {"patientsK": 45,   "wtpPct": 48, "priceK": 110},
        "row": {"patientsK": 60,   "wtpPct": 10, "priceK": 45},
    },
    "oncology.rare_onc.mpnst": {
        "us":  {"patientsK": 0.5,  "wtpPct": 70, "priceK": 250},
        "eu":  {"patientsK": 0.6,  "wtpPct": 55, "priceK": 130},
        "row": {"patientsK": 0.8,  "wtpPct": 12, "priceK": 50},
    },
    "oncology.rare_onc.ovarian_resistant": {
        "us":  {"patientsK": 15,   "wtpPct": 65, "priceK": 200},
        "eu":  {"patientsK": 18,   "wtpPct": 48, "priceK": 110},
        "row": {"patientsK": 25,   "wtpPct": 10, "priceK": 45},
    },
    "oncology.gu.bladder_uroepithelial": {
        "us":  {"patientsK": 80,   "wtpPct": 60, "priceK": 190},
        "eu":  {"patientsK": 90,   "wtpPct": 45, "priceK": 105},
        "row": {"patientsK": 150,  "wtpPct": 10, "priceK": 42},
    },
    "oncology.gu.endometrial": {
        "us":  {"patientsK": 20,   "wtpPct": 60, "priceK": 190},
        "eu":  {"patientsK": 22,   "wtpPct": 45, "priceK": 105},
        "row": {"patientsK": 30,   "wtpPct": 10, "priceK": 42},
    },
    "oncology.head_neck.hnscc": {
        "us":  {"patientsK": 30,   "wtpPct": 60, "priceK": 190},
        "eu":  {"patientsK": 35,   "wtpPct": 45, "priceK": 105},
        "row": {"patientsK": 100,  "wtpPct": 8,  "priceK": 40},
    },
    "oncology.rare_onc.desmoid_tumor": {
        "us":  {"patientsK": 1.5,  "wtpPct": 70, "priceK": 250},
        "eu":  {"patientsK": 1.8,  "wtpPct": 55, "priceK": 130},
        "row": {"patientsK": 2,    "wtpPct": 12, "priceK": 50},
    },
    "oncology.rare_onc.solid_tumor_basket": {
        "us":  {"patientsK": 200,  "wtpPct": 55, "priceK": 180},
        "eu":  {"patientsK": 220,  "wtpPct": 40, "priceK": 100},
        "row": {"patientsK": 400,  "wtpPct": 8,  "priceK": 40},
    },
    "oncology.thoracic.mesothelioma": {
        "us":  {"patientsK": 3,    "wtpPct": 65, "priceK": 200},
        "eu":  {"patientsK": 4,    "wtpPct": 50, "priceK": 110},
        "row": {"patientsK": 6,    "wtpPct": 10, "priceK": 45},
    },

    # ======================================================================
    # CARDIO-METABOLIC (20)
    # ======================================================================

    "cardio_metabolic.attr.attr_cm": {
        "us":  {"patientsK": 120,  "wtpPct": 70, "priceK": 250},
        "eu":  {"patientsK": 100,  "wtpPct": 50, "priceK": 130},
        "row": {"patientsK": 80,   "wtpPct": 15, "priceK": 50},
    },
    "cardio_metabolic.attr.attr_pn": {
        "us":  {"patientsK": 10,   "wtpPct": 75, "priceK": 300},
        "eu":  {"patientsK": 12,   "wtpPct": 55, "priceK": 150},
        "row": {"patientsK": 15,   "wtpPct": 15, "priceK": 60},
    },
    "cardio_metabolic.diabetes.t1d": {
        "us":  {"patientsK": 1600, "wtpPct": 55, "priceK": 12},
        "eu":  {"patientsK": 1200, "wtpPct": 45, "priceK": 6},
        "row": {"patientsK": 2500, "wtpPct": 10, "priceK": 3},
    },
    "cardio_metabolic.diabetes.t2d": {
        "us":  {"patientsK": 25000, "wtpPct": 50, "priceK": 10},
        "eu":  {"patientsK": 20000, "wtpPct": 40, "priceK": 5},
        "row": {"patientsK": 60000, "wtpPct": 8,  "priceK": 2},
    },
    "cardio_metabolic.hypertension.agt_knockdown": {
        "us":  {"patientsK": 50000, "wtpPct": 45, "priceK": 8},
        "eu":  {"patientsK": 40000, "wtpPct": 35, "priceK": 4},
        "row": {"patientsK": 80000, "wtpPct": 8,  "priceK": 2},
    },
    "cardio_metabolic.thrombosis.anticoagulation": {
        # Patients on anticoagulants (AFib, VTE, mechanical valves) -- not a lipid disease
        "us":  {"patientsK": 6000, "wtpPct": 55, "priceK": 12},
        "eu":  {"patientsK": 5000, "wtpPct": 42, "priceK": 6},
        "row": {"patientsK": 8000, "wtpPct": 10, "priceK": 3},
    },
    "cardio_metabolic.lipids.ldl_cv_risk": {
        # ASCVD risk reduction: LDL-lowering + CV outcomes = same patient pool
        # (statins, PCSK9i, CETPi, ANGPTL3, oral PCSK9 all compete for these patients)
        "us":  {"patientsK": 20000, "wtpPct": 52, "priceK": 10},
        "eu":  {"patientsK": 16000, "wtpPct": 40, "priceK": 5},
        "row": {"patientsK": 30000, "wtpPct": 8,  "priceK": 2},
    },
    "cardio_metabolic.lipids.lpa": {
        "us":  {"patientsK": 5000, "wtpPct": 50, "priceK": 10},
        "eu":  {"patientsK": 4000, "wtpPct": 38, "priceK": 5},
        "row": {"patientsK": 8000, "wtpPct": 8,  "priceK": 2},
    },
    "cardio_metabolic.lipids.triglycerides": {
        "us":  {"patientsK": 4000, "wtpPct": 50, "priceK": 10},
        "eu":  {"patientsK": 3000, "wtpPct": 38, "priceK": 5},
        "row": {"patientsK": 5000, "wtpPct": 8,  "priceK": 2},
    },
    "cardio_metabolic.liver.a1at": {
        "us":  {"patientsK": 3,    "wtpPct": 75, "priceK": 350},
        "eu":  {"patientsK": 4,    "wtpPct": 55, "priceK": 180},
        "row": {"patientsK": 3,    "wtpPct": 12, "priceK": 60},
    },
    "cardio_metabolic.liver.hbv_functional_cure": {
        "us":  {"patientsK": 850,  "wtpPct": 55, "priceK": 60},
        "eu":  {"patientsK": 1200, "wtpPct": 42, "priceK": 30},
        "row": {"patientsK": 50000, "wtpPct": 5, "priceK": 5},
    },
    "cardio_metabolic.liver.mash": {
        "us":  {"patientsK": 3000, "wtpPct": 50, "priceK": 30},
        "eu":  {"patientsK": 2500, "wtpPct": 38, "priceK": 15},
        "row": {"patientsK": 4000, "wtpPct": 8,  "priceK": 6},
    },
    "cardio_metabolic.liver.pld_adpkd": {
        "us":  {"patientsK": 140,  "wtpPct": 65, "priceK": 80},
        "eu":  {"patientsK": 120,  "wtpPct": 48, "priceK": 40},
        "row": {"patientsK": 150,  "wtpPct": 10, "priceK": 15},
    },
    "cardio_metabolic.obesity.general": {
        # Mass-market obesity (all mechanisms compete here: GLP-1, RNAi, myostatin, kv7, etc.)
        "us":  {"patientsK": 40000, "wtpPct": 50, "priceK": 15},
        "eu":  {"patientsK": 30000, "wtpPct": 35, "priceK": 8},
        "row": {"patientsK": 50000, "wtpPct": 8,  "priceK": 3},
    },
    "cardio_metabolic.obesity.rare_genetic": {
        # Rare genetic obesity (MC4R pathway: BBS, POMC/LEPR, Prader-Willi, acquired hypothalamic)
        "us":  {"patientsK": 500,  "wtpPct": 70, "priceK": 80},
        "eu":  {"patientsK": 400,  "wtpPct": 50, "priceK": 40},
        "row": {"patientsK": 600,  "wtpPct": 10, "priceK": 15},
    },
    "cardio_metabolic.rare_metabolic.homocystinuria": {
        "us":  {"patientsK": 1,    "wtpPct": 75, "priceK": 350},
        "eu":  {"patientsK": 1.2,  "wtpPct": 58, "priceK": 180},
        "row": {"patientsK": 2,    "wtpPct": 12, "priceK": 60},
    },
    "cardio_metabolic.rare_metabolic.hyperoxaluria": {
        "us":  {"patientsK": 3,    "wtpPct": 75, "priceK": 400},
        "eu":  {"patientsK": 3.5,  "wtpPct": 58, "priceK": 200},
        "row": {"patientsK": 4,    "wtpPct": 12, "priceK": 70},
    },
    "cardio_metabolic.rare_metabolic.porphyria": {
        "us":  {"patientsK": 5,    "wtpPct": 75, "priceK": 350},
        "eu":  {"patientsK": 6,    "wtpPct": 58, "priceK": 180},
        "row": {"patientsK": 8,    "wtpPct": 12, "priceK": 60},
    },

    # ======================================================================
    # CNS (20)
    # ======================================================================

    "cns.epilepsy.dee": {
        "us":  {"patientsK": 30,   "wtpPct": 70, "priceK": 80},
        "eu":  {"patientsK": 35,   "wtpPct": 52, "priceK": 40},
        "row": {"patientsK": 50,   "wtpPct": 12, "priceK": 15},
    },
    "cns.epilepsy.focal": {
        "us":  {"patientsK": 1200, "wtpPct": 55, "priceK": 20},
        "eu":  {"patientsK": 1000, "wtpPct": 42, "priceK": 10},
        "row": {"patientsK": 2000, "wtpPct": 10, "priceK": 4},
    },
    "cns.epilepsy.generalized": {
        "us":  {"patientsK": 400,  "wtpPct": 55, "priceK": 20},
        "eu":  {"patientsK": 350,  "wtpPct": 42, "priceK": 10},
        "row": {"patientsK": 600,  "wtpPct": 10, "priceK": 4},
    },
    "cns.movement.essential_tremor": {
        # ~3M US prevalence, ~500K treated
        "us":  {"patientsK": 500,  "wtpPct": 50, "priceK": 15},
        "eu":  {"patientsK": 400,  "wtpPct": 38, "priceK": 8},
        "row": {"patientsK": 600,  "wtpPct": 10, "priceK": 3},
    },
    "cns.neurodegeneration.alexander": {
        "us":  {"patientsK": 0.5,  "wtpPct": 80, "priceK": 500},
        "eu":  {"patientsK": 0.6,  "wtpPct": 60, "priceK": 250},
        "row": {"patientsK": 0.8,  "wtpPct": 10, "priceK": 80},
    },
    "cns.neurodegeneration.als": {
        "us":  {"patientsK": 30,   "wtpPct": 70, "priceK": 150},
        "eu":  {"patientsK": 35,   "wtpPct": 52, "priceK": 80},
        "row": {"patientsK": 40,   "wtpPct": 12, "priceK": 30},
    },
    "cns.neurodegeneration.alzheimer": {
        "us":  {"patientsK": 6000, "wtpPct": 50, "priceK": 28},
        "eu":  {"patientsK": 5000, "wtpPct": 35, "priceK": 15},
        "row": {"patientsK": 10000, "wtpPct": 8, "priceK": 5},
    },
    "cns.neurodegeneration.caa": {
        "us":  {"patientsK": 500,  "wtpPct": 50, "priceK": 30},
        "eu":  {"patientsK": 400,  "wtpPct": 35, "priceK": 15},
        "row": {"patientsK": 600,  "wtpPct": 8,  "priceK": 5},
    },
    "cns.neurodegeneration.dlb": {
        "us":  {"patientsK": 1400, "wtpPct": 50, "priceK": 25},
        "eu":  {"patientsK": 1100, "wtpPct": 35, "priceK": 12},
        "row": {"patientsK": 1500, "wtpPct": 8,  "priceK": 5},
    },
    "cns.neurodegeneration.parkinson_disease": {
        "us":  {"patientsK": 1000, "wtpPct": 55, "priceK": 25},
        "eu":  {"patientsK": 800,  "wtpPct": 42, "priceK": 12},
        "row": {"patientsK": 1500, "wtpPct": 10, "priceK": 5},
    },
    "cns.neurodegeneration.ppa": {
        "us":  {"patientsK": 30,   "wtpPct": 55, "priceK": 30},
        "eu":  {"patientsK": 25,   "wtpPct": 40, "priceK": 15},
        "row": {"patientsK": 35,   "wtpPct": 8,  "priceK": 5},
    },
    "cns.neurodegeneration.stroke": {
        "us":  {"patientsK": 800,  "wtpPct": 50, "priceK": 20},
        "eu":  {"patientsK": 700,  "wtpPct": 38, "priceK": 10},
        "row": {"patientsK": 2000, "wtpPct": 8,  "priceK": 4},
    },
    "cns.pain.migraine": {
        # ~12M sufferers US, ~4M treated with branded Rx
        "us":  {"patientsK": 4000, "wtpPct": 50, "priceK": 10},
        "eu":  {"patientsK": 3000, "wtpPct": 38, "priceK": 5},
        "row": {"patientsK": 5000, "wtpPct": 8,  "priceK": 2},
    },
    "cns.psychiatry.adhd": {
        # ~10M US, ~6M treated
        "us":  {"patientsK": 6000, "wtpPct": 55, "priceK": 12},
        "eu":  {"patientsK": 3000, "wtpPct": 38, "priceK": 6},
        "row": {"patientsK": 4000, "wtpPct": 8,  "priceK": 3},
    },
    "cns.psychiatry.anxiety": {
        "us":  {"patientsK": 6000, "wtpPct": 50, "priceK": 10},
        "eu":  {"patientsK": 4000, "wtpPct": 38, "priceK": 5},
        "row": {"patientsK": 5000, "wtpPct": 8,  "priceK": 2},
    },
    "cns.psychiatry.asd": {
        "us":  {"patientsK": 2000, "wtpPct": 45, "priceK": 15},
        "eu":  {"patientsK": 1500, "wtpPct": 32, "priceK": 8},
        "row": {"patientsK": 3000, "wtpPct": 6,  "priceK": 3},
    },
    "cns.psychiatry.depression": {
        "us":  {"patientsK": 8000, "wtpPct": 55, "priceK": 12},
        "eu":  {"patientsK": 6000, "wtpPct": 40, "priceK": 6},
        "row": {"patientsK": 10000, "wtpPct": 8, "priceK": 3},
    },
    "cns.psychiatry.pain_fibromyalgia": {
        "us":  {"patientsK": 4000, "wtpPct": 50, "priceK": 10},
        "eu":  {"patientsK": 3000, "wtpPct": 35, "priceK": 5},
        "row": {"patientsK": 4000, "wtpPct": 8,  "priceK": 2},
    },
    "cns.psychiatry.schizophrenia": {
        "us":  {"patientsK": 1500, "wtpPct": 55, "priceK": 25},
        "eu":  {"patientsK": 1200, "wtpPct": 42, "priceK": 12},
        "row": {"patientsK": 2000, "wtpPct": 10, "priceK": 5},
    },
    "cns.sleep.narcolepsy": {
        "us":  {"patientsK": 200,  "wtpPct": 65, "priceK": 80},
        "eu":  {"patientsK": 150,  "wtpPct": 48, "priceK": 40},
        "row": {"patientsK": 200,  "wtpPct": 10, "priceK": 15},
    },

    # ======================================================================
    # IMMUNOLOGY (10)
    # ======================================================================

    "immunology.autoimmune.fsgs": {
        "us":  {"patientsK": 40,   "wtpPct": 65, "priceK": 100},
        "eu":  {"patientsK": 35,   "wtpPct": 48, "priceK": 50},
        "row": {"patientsK": 50,   "wtpPct": 10, "priceK": 20},
    },
    "immunology.autoimmune.hereditary_angioedema": {
        "us":  {"patientsK": 7,    "wtpPct": 78, "priceK": 400},
        "eu":  {"patientsK": 8,    "wtpPct": 60, "priceK": 200},
        "row": {"patientsK": 10,   "wtpPct": 15, "priceK": 70},
    },
    "immunology.autoimmune.iga_nephropathy": {
        "us":  {"patientsK": 130,  "wtpPct": 60, "priceK": 80},
        "eu":  {"patientsK": 120,  "wtpPct": 45, "priceK": 40},
        "row": {"patientsK": 300,  "wtpPct": 10, "priceK": 15},
    },
    "immunology.autoimmune.sjogrens": {
        "us":  {"patientsK": 1000, "wtpPct": 50, "priceK": 50},
        "eu":  {"patientsK": 800,  "wtpPct": 38, "priceK": 25},
        "row": {"patientsK": 1000, "wtpPct": 8,  "priceK": 10},
    },
    "immunology.autoimmune.sle": {
        "us":  {"patientsK": 300,  "wtpPct": 55, "priceK": 60},
        "eu":  {"patientsK": 250,  "wtpPct": 42, "priceK": 30},
        "row": {"patientsK": 400,  "wtpPct": 10, "priceK": 12},
    },
    "immunology.inflammatory_gi.crohns": {
        "us":  {"patientsK": 800,  "wtpPct": 55, "priceK": 60},
        "eu":  {"patientsK": 650,  "wtpPct": 42, "priceK": 30},
        "row": {"patientsK": 500,  "wtpPct": 10, "priceK": 12},
    },
    "immunology.inflammatory_gi.ulcerative_colitis": {
        "us":  {"patientsK": 700,  "wtpPct": 55, "priceK": 60},
        "eu":  {"patientsK": 550,  "wtpPct": 42, "priceK": 30},
        "row": {"patientsK": 400,  "wtpPct": 10, "priceK": 12},
    },
    "immunology.inflammatory_systemic.rheumatoid_arthritis": {
        "us":  {"patientsK": 1500, "wtpPct": 55, "priceK": 55},
        "eu":  {"patientsK": 1200, "wtpPct": 42, "priceK": 28},
        "row": {"patientsK": 2000, "wtpPct": 10, "priceK": 10},
    },
    "immunology.neuromuscular_autoimmune.itp": {
        "us":  {"patientsK": 60,   "wtpPct": 65, "priceK": 100},
        "eu":  {"patientsK": 50,   "wtpPct": 48, "priceK": 50},
        "row": {"patientsK": 70,   "wtpPct": 12, "priceK": 20},
    },
    "immunology.neuromuscular_autoimmune.mmn": {
        "us":  {"patientsK": 5,    "wtpPct": 75, "priceK": 200},
        "eu":  {"patientsK": 6,    "wtpPct": 55, "priceK": 100},
        "row": {"patientsK": 8,    "wtpPct": 12, "priceK": 40},
    },

    # ======================================================================
    # DERMATOLOGY (9)
    # ======================================================================

    "dermatology.aesthetics.filler": {
        # ~3M US procedures/yr; per-procedure pricing, not chronic
        "us":  {"patientsK": 3000, "wtpPct": 90, "priceK": 1.2},
        "eu":  {"patientsK": 2500, "wtpPct": 85, "priceK": 0.8},
        "row": {"patientsK": 3000, "wtpPct": 70, "priceK": 0.4},
    },
    "dermatology.aesthetics.neurotoxin": {
        # ~5M US procedures/yr (Botox cosmetic + competitors)
        "us":  {"patientsK": 5000, "wtpPct": 90, "priceK": 1.0},
        "eu":  {"patientsK": 4000, "wtpPct": 85, "priceK": 0.7},
        "row": {"patientsK": 5000, "wtpPct": 70, "priceK": 0.3},
    },
    "dermatology.inflammatory_derm.atopic_dermatitis_systemic": {
        "us":  {"patientsK": 1500, "wtpPct": 55, "priceK": 60},
        "eu":  {"patientsK": 1200, "wtpPct": 42, "priceK": 30},
        "row": {"patientsK": 2000, "wtpPct": 10, "priceK": 12},
    },
    "dermatology.inflammatory_derm.atopic_dermatitis_topical": {
        "us":  {"patientsK": 8000, "wtpPct": 50, "priceK": 8},
        "eu":  {"patientsK": 6000, "wtpPct": 38, "priceK": 4},
        "row": {"patientsK": 10000, "wtpPct": 10, "priceK": 2},
    },
    "dermatology.inflammatory_derm.hidradenitis_suppurativa": {
        "us":  {"patientsK": 200,  "wtpPct": 55, "priceK": 60},
        "eu":  {"patientsK": 160,  "wtpPct": 42, "priceK": 30},
        "row": {"patientsK": 200,  "wtpPct": 10, "priceK": 12},
    },
    "dermatology.inflammatory_derm.psoriasis_systemic": {
        "us":  {"patientsK": 1500, "wtpPct": 55, "priceK": 60},
        "eu":  {"patientsK": 1200, "wtpPct": 42, "priceK": 30},
        "row": {"patientsK": 2000, "wtpPct": 10, "priceK": 12},
    },
    "dermatology.rare_skin.alopecia_areata": {
        "us":  {"patientsK": 300,  "wtpPct": 55, "priceK": 50},
        "eu":  {"patientsK": 250,  "wtpPct": 40, "priceK": 25},
        "row": {"patientsK": 400,  "wtpPct": 8,  "priceK": 10},
    },
    "dermatology.rare_skin.hailey_hailey": {
        "us":  {"patientsK": 2,    "wtpPct": 70, "priceK": 80},
        "eu":  {"patientsK": 2.5,  "wtpPct": 52, "priceK": 40},
        "row": {"patientsK": 3,    "wtpPct": 10, "priceK": 15},
    },
    "dermatology.rare_skin.vitiligo": {
        "us":  {"patientsK": 1500, "wtpPct": 45, "priceK": 40},
        "eu":  {"patientsK": 1200, "wtpPct": 32, "priceK": 20},
        "row": {"patientsK": 2000, "wtpPct": 8,  "priceK": 8},
    },

    # ======================================================================
    # MUSCULOSKELETAL (7)
    # ======================================================================

    "musculoskeletal.bone_cartilage.achondroplasia": {
        "us":  {"patientsK": 10,   "wtpPct": 75, "priceK": 350},
        "eu":  {"patientsK": 12,   "wtpPct": 55, "priceK": 180},
        "row": {"patientsK": 15,   "wtpPct": 12, "priceK": 60},
    },
    "musculoskeletal.bone_cartilage.osteoporosis": {
        "us":  {"patientsK": 10000, "wtpPct": 45, "priceK": 8},
        "eu":  {"patientsK": 8000,  "wtpPct": 38, "priceK": 4},
        "row": {"patientsK": 15000, "wtpPct": 8,  "priceK": 2},
    },
    "musculoskeletal.neuromuscular.cms": {
        "us":  {"patientsK": 3,    "wtpPct": 78, "priceK": 300},
        "eu":  {"patientsK": 3.5,  "wtpPct": 58, "priceK": 150},
        "row": {"patientsK": 5,    "wtpPct": 10, "priceK": 50},
    },
    "musculoskeletal.neuromuscular.dm1": {
        "us":  {"patientsK": 15,   "wtpPct": 70, "priceK": 250},
        "eu":  {"patientsK": 18,   "wtpPct": 52, "priceK": 130},
        "row": {"patientsK": 20,   "wtpPct": 12, "priceK": 50},
    },
    "musculoskeletal.neuromuscular.dmd": {
        "us":  {"patientsK": 12,   "wtpPct": 78, "priceK": 400},
        "eu":  {"patientsK": 14,   "wtpPct": 58, "priceK": 200},
        "row": {"patientsK": 18,   "wtpPct": 12, "priceK": 70},
    },
    "musculoskeletal.neuromuscular.fshd": {
        "us":  {"patientsK": 17,   "wtpPct": 70, "priceK": 250},
        "eu":  {"patientsK": 20,   "wtpPct": 52, "priceK": 130},
        "row": {"patientsK": 25,   "wtpPct": 12, "priceK": 50},
    },
    "musculoskeletal.neuromuscular.lgmd": {
        "us":  {"patientsK": 5,    "wtpPct": 75, "priceK": 300},
        "eu":  {"patientsK": 6,    "wtpPct": 55, "priceK": 150},
        "row": {"patientsK": 8,    "wtpPct": 12, "priceK": 50},
    },

    # ======================================================================
    # OPHTHALMOLOGY (7)
    # ======================================================================

    # NOTE: VRDN TED regions were hand-tuned -- included here for
    # consistency but values are close to the existing config.
    "ophthalmology.anterior_neuro.ted": {
        "us":  {"patientsK": 50,   "wtpPct": 65, "priceK": 200},
        "eu":  {"patientsK": 45,   "wtpPct": 48, "priceK": 100},
        "row": {"patientsK": 50,   "wtpPct": 12, "priceK": 40},
    },
    "ophthalmology.retina.dme": {
        "us":  {"patientsK": 750,  "wtpPct": 55, "priceK": 18},
        "eu":  {"patientsK": 600,  "wtpPct": 42, "priceK": 10},
        "row": {"patientsK": 2000, "wtpPct": 8,  "priceK": 3},
    },
    "ophthalmology.retina.dr": {
        "us":  {"patientsK": 800,  "wtpPct": 50, "priceK": 15},
        "eu":  {"patientsK": 650,  "wtpPct": 38, "priceK": 8},
        "row": {"patientsK": 2500, "wtpPct": 7,  "priceK": 3},
    },
    "ophthalmology.retina.ga": {
        "us":  {"patientsK": 1000, "wtpPct": 50, "priceK": 15},
        "eu":  {"patientsK": 800,  "wtpPct": 38, "priceK": 8},
        "row": {"patientsK": 1200, "wtpPct": 8,  "priceK": 3},
    },
    "ophthalmology.retina.nvamd": {
        "us":  {"patientsK": 200,  "wtpPct": 65, "priceK": 20},
        "eu":  {"patientsK": 180,  "wtpPct": 50, "priceK": 10},
        "row": {"patientsK": 300,  "wtpPct": 12, "priceK": 4},
    },
    "ophthalmology.optic_nerve.lhon": {
        "us":  {"patientsK": 4,    "wtpPct": 78, "priceK": 400},
        "eu":  {"patientsK": 5,    "wtpPct": 58, "priceK": 200},
        "row": {"patientsK": 6,    "wtpPct": 10, "priceK": 70},
    },
    "ophthalmology.optic_nerve.nmosd": {
        "us":  {"patientsK": 15,   "wtpPct": 72, "priceK": 250},
        "eu":  {"patientsK": 12,   "wtpPct": 55, "priceK": 130},
        "row": {"patientsK": 20,   "wtpPct": 12, "priceK": 50},
    },

    # ======================================================================
    # INFECTIOUS DISEASE (5)
    # ======================================================================

    "infectious_disease.anti_infective.hiv_prevention": {
        "us":  {"patientsK": 1200, "wtpPct": 55, "priceK": 45},
        "eu":  {"patientsK": 800,  "wtpPct": 42, "priceK": 20},
        "row": {"patientsK": 5000, "wtpPct": 10, "priceK": 3},
    },
    "infectious_disease.anti_infective.hiv_treatment": {
        "us":  {"patientsK": 1200, "wtpPct": 65, "priceK": 40},
        "eu":  {"patientsK": 800,  "wtpPct": 50, "priceK": 20},
        "row": {"patientsK": 20000, "wtpPct": 8, "priceK": 1.5},
    },
    "infectious_disease.vaccines.chikungunya": {
        "us":  {"patientsK": 200,  "wtpPct": 40, "priceK": 0.2},
        "eu":  {"patientsK": 150,  "wtpPct": 35, "priceK": 0.15},
        "row": {"patientsK": 500,  "wtpPct": 15, "priceK": 0.05},
    },
    "infectious_disease.vaccines.lyme": {
        "us":  {"patientsK": 20000, "wtpPct": 35, "priceK": 0.2},
        "eu":  {"patientsK": 15000, "wtpPct": 30, "priceK": 0.15},
        "row": {"patientsK": 5000,  "wtpPct": 10, "priceK": 0.05},
    },
    "infectious_disease.vaccines.shigella_zika": {
        "us":  {"patientsK": 1000, "wtpPct": 30, "priceK": 0.2},
        "eu":  {"patientsK": 800,  "wtpPct": 25, "priceK": 0.15},
        "row": {"patientsK": 5000, "wtpPct": 15, "priceK": 0.05},
    },

    # ======================================================================
    # ENDOCRINE (4)
    # ======================================================================

    "endocrine.adrenal.cah": {
        "us":  {"patientsK": 30,   "wtpPct": 70, "priceK": 100},
        "eu":  {"patientsK": 25,   "wtpPct": 52, "priceK": 50},
        "row": {"patientsK": 35,   "wtpPct": 12, "priceK": 20},
    },
    "endocrine.calcium.adh1": {
        "us":  {"patientsK": 1,    "wtpPct": 78, "priceK": 350},
        "eu":  {"patientsK": 1.2,  "wtpPct": 58, "priceK": 180},
        "row": {"patientsK": 1.5,  "wtpPct": 10, "priceK": 60},
    },
    "endocrine.pituitary.acromegaly": {
        "us":  {"patientsK": 15,   "wtpPct": 72, "priceK": 120},
        "eu":  {"patientsK": 18,   "wtpPct": 55, "priceK": 60},
        "row": {"patientsK": 20,   "wtpPct": 12, "priceK": 25},
    },
    "endocrine.thyroid.graves": {
        "us":  {"patientsK": 500,  "wtpPct": 55, "priceK": 30},
        "eu":  {"patientsK": 400,  "wtpPct": 42, "priceK": 15},
        "row": {"patientsK": 600,  "wtpPct": 10, "priceK": 5},
    },

    # ======================================================================
    # RESPIRATORY (2)
    # ======================================================================

    "respiratory.inflammatory.asthma_severe": {
        "us":  {"patientsK": 2500, "wtpPct": 55, "priceK": 35},
        "eu":  {"patientsK": 2000, "wtpPct": 42, "priceK": 18},
        "row": {"patientsK": 3000, "wtpPct": 10, "priceK": 7},
    },
    "respiratory.inflammatory.copd": {
        "us":  {"patientsK": 15000, "wtpPct": 50, "priceK": 8},
        "eu":  {"patientsK": 12000, "wtpPct": 38, "priceK": 4},
        "row": {"patientsK": 30000, "wtpPct": 8,  "priceK": 2},
    },

    # ======================================================================
    # HEMATOLOGY (1)
    # ======================================================================

    "hematology.rare_blood.hemoglobinopathy": {
        "us":  {"patientsK": 100,  "wtpPct": 65, "priceK": 200},
        "eu":  {"patientsK": 60,   "wtpPct": 50, "priceK": 100},
        "row": {"patientsK": 300,  "wtpPct": 8,  "priceK": 30},
    },
}


# ---------------------------------------------------------------------------
# Sources annotation per area (generic but more specific than the old auto-
# decomposed notes).
# ---------------------------------------------------------------------------

def _make_sources(area: str, data: dict) -> dict:
    """Build a sources dict noting the data is from real_epi_data.py."""
    us = data["us"]
    eu = data["eu"]
    row = data["row"]
    tag = area.split(".")[0]  # therapeutic area
    return {
        "us.patientsK": {
            "note": (
                f"real_epi_data.py -- {us['patientsK']}K US treated/diagnosed; "
                f"source: consensus epi ({tag})."
            )
        },
        "eu.patientsK": {
            "note": (
                f"real_epi_data.py -- {eu['patientsK']}K EU treated/diagnosed."
            )
        },
        "row.patientsK": {
            "note": (
                f"real_epi_data.py -- {row['patientsK']}K ROW treated/diagnosed."
            )
        },
        "us.wtpPct": {
            "note": (
                f"real_epi_data.py -- US WTP {us['wtpPct']}% "
                f"(payor access + formulary)."
            )
        },
        "eu.wtpPct": {
            "note": (
                f"real_epi_data.py -- EU WTP {eu['wtpPct']}% "
                f"(HTA-gated uptake)."
            )
        },
        "row.wtpPct": {
            "note": (
                f"real_epi_data.py -- ROW WTP {row['wtpPct']}% "
                f"(limited reimbursement ex-Japan)."
            )
        },
        "us.priceK": {
            "note": (
                f"real_epi_data.py -- US avg ${us['priceK']}K/yr "
                f"({tag} drug-class avg)."
            )
        },
        "eu.priceK": {
            "note": (
                f"real_epi_data.py -- EU avg ${eu['priceK']}K/yr."
            )
        },
        "row.priceK": {
            "note": (
                f"real_epi_data.py -- ROW avg ${row['priceK']}K/yr."
            )
        },
        "penPct": {
            "note": "Preserved from config -- refine per competitive landscape."
        },
    }


# ---------------------------------------------------------------------------
# Config update logic
# ---------------------------------------------------------------------------

def _addressable_b(data: dict) -> float:
    """Compute implied addressable ($B) from regional data."""
    total = 0.0
    for region in ("us", "eu", "row"):
        r = data[region]
        total += r["patientsK"] * (r["wtpPct"] / 100.0) * r["priceK"]
    return total / 1000.0  # K * K = M, /1000 = B


def update_config(cfg: dict, dry_run: bool = True) -> int:
    """Update indications in a config dict.  Returns count of updates."""
    updates = 0
    for asset in cfg.get("assets", []):
        for ind in asset.get("indications", []):
            area = ind.get("area", "")
            if area not in REAL_MARKETS:
                continue
            mkt = ind.get("market")
            if mkt is None:
                continue
            data = REAL_MARKETS[area]
            if not dry_run:
                mkt["regions"] = {
                    reg: dict(vals) for reg, vals in data.items()
                }
                mkt["sources"] = _make_sources(area, data)
            updates += 1
    return updates


def main():
    dry_run = "--write" not in sys.argv

    if dry_run:
        print("=== DRY RUN (pass --write to apply) ===\n")

    # Print summary of REAL_MARKETS
    print(f"REAL_MARKETS contains {len(REAL_MARKETS)} area tags.\n")

    # Sanity-check: print implied addressable for each market
    if "--summary" in sys.argv or dry_run:
        print(f"{'Area':<55} {'US addr $B':>12} {'EU addr $B':>12} "
              f"{'ROW addr $B':>12} {'Total $B':>12}")
        print("-" * 105)
        for area, data in sorted(REAL_MARKETS.items()):
            us_b = (data["us"]["patientsK"] * data["us"]["wtpPct"] / 100
                    * data["us"]["priceK"]) / 1000
            eu_b = (data["eu"]["patientsK"] * data["eu"]["wtpPct"] / 100
                    * data["eu"]["priceK"]) / 1000
            row_b = (data["row"]["patientsK"] * data["row"]["wtpPct"] / 100
                     * data["row"]["priceK"]) / 1000
            total = us_b + eu_b + row_b
            print(f"{area:<55} {us_b:>12.1f} {eu_b:>12.1f} "
                  f"{row_b:>12.1f} {total:>12.1f}")
        print()

    # Process config files
    total_updates = 0
    config_files = sorted(CONFIG_DIR.glob("*.json"))
    for path in config_files:
        if path.name == "manifest.json":
            continue
        try:
            cfg = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            print(f"  SKIP {path.name}: {exc}")
            continue

        n = update_config(cfg, dry_run=dry_run)
        if n > 0:
            total_updates += n
            if not dry_run:
                path.write_text(
                    json.dumps(cfg, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8",
                )
            print(f"  {'Would update' if dry_run else 'Updated'} "
                  f"{path.name}: {n} indication(s)")

    print(f"\nTotal: {total_updates} indication(s) across "
          f"{len(config_files) - 1} config files.")
    if dry_run:
        print("\nRe-run with --write to apply changes.")


if __name__ == "__main__":
    main()
