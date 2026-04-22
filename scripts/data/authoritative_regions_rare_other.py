# -*- coding: utf-8 -*-
"""
Authoritative slider values extracted from tooltips_rare_other.py.

Conventions:
- patientsK: treated/eligible/addressable pool (K patients), or annual addressable
  doses for vaccines. M converted to K.
- wtpPct: market-level willingness-to-pay %.
- priceK: blended/headline drug price in $K. One-time gene therapies use the
  net one-time price (not amortized). Vaccines use per-dose $K (e.g. $300/dose
  = 0.3).
- PEN_PCT: peak penetration % (area-level).
"""

REGIONS = {
    # =====================================================================
    # MUSCULOSKELETAL - BONE & CARTILAGE
    # =====================================================================
    "musculoskeletal.bone_cartilage.achondroplasia": {
        "us":  {"patientsK": 10,   "wtpPct": 70, "priceK": 320},
        "eu":  {"patientsK": 12,   "wtpPct": 55, "priceK": 210},
        "row": {"patientsK": 8,    "wtpPct": 25, "priceK": 150},
    },
    "musculoskeletal.bone_cartilage.osteoporosis": {
        "us":  {"patientsK": 10000, "wtpPct": 35, "priceK": 25},
        "eu":  {"patientsK": 22000, "wtpPct": 28, "priceK": 16},
        "row": {"patientsK": 15000, "wtpPct": 15, "priceK": 1.5},
    },

    # =====================================================================
    # MUSCULOSKELETAL - NEUROMUSCULAR
    # =====================================================================
    "musculoskeletal.neuromuscular.cms": {
        "us":  {"patientsK": 3,  "wtpPct": 55, "priceK": 400},
        "eu":  {"patientsK": 4,  "wtpPct": 40, "priceK": 280},
        "row": {"patientsK": 3,  "wtpPct": 15, "priceK": 150},
    },
    "musculoskeletal.neuromuscular.dm1": {
        "us":  {"patientsK": 15, "wtpPct": 60, "priceK": 450},
        "eu":  {"patientsK": 20, "wtpPct": 40, "priceK": 300},
        "row": {"patientsK": 15, "wtpPct": 15, "priceK": 150},
    },
    "musculoskeletal.neuromuscular.dmd.exon45": {
        "us":  {"patientsK": 1.4, "wtpPct": 50, "priceK": 750},
        "eu":  {"patientsK": 1.4, "wtpPct": 25, "priceK": 500},
        "row": {"patientsK": 3,   "wtpPct": 15, "priceK": 400},
    },
    "musculoskeletal.neuromuscular.dmd.exon51": {
        "us":  {"patientsK": 2,  "wtpPct": 50, "priceK": 750},
        "eu":  {"patientsK": 2,  "wtpPct": 20, "priceK": 500},
        "row": {"patientsK": 4,  "wtpPct": 15, "priceK": 400},
    },
    "musculoskeletal.neuromuscular.dmd.exon53": {
        "us":  {"patientsK": 1.2, "wtpPct": 50, "priceK": 750},
        "eu":  {"patientsK": 1.2, "wtpPct": 20, "priceK": 500},
        "row": {"patientsK": 2,   "wtpPct": 20, "priceK": 600},
    },
    "musculoskeletal.neuromuscular.dmd.gene_therapy": {
        "us":  {"patientsK": 7,  "wtpPct": 55, "priceK": 2600},
        "eu":  {"patientsK": 9,  "wtpPct": 35, "priceK": 1800},
        "row": {"patientsK": 12, "wtpPct": 10, "priceK": 800},
    },
    "musculoskeletal.neuromuscular.fshd": {
        "us":  {"patientsK": 17, "wtpPct": 55, "priceK": 400},
        "eu":  {"patientsK": 22, "wtpPct": 35, "priceK": 260},
        "row": {"patientsK": 15, "wtpPct": 15, "priceK": 130},
    },
    "musculoskeletal.neuromuscular.lgmd": {
        "us":  {"patientsK": 5, "wtpPct": 50, "priceK": 2500},
        "eu":  {"patientsK": 7, "wtpPct": 30, "priceK": 1600},
        "row": {"patientsK": 4, "wtpPct": 10, "priceK": 700},
    },

    # =====================================================================
    # INFECTIOUS DISEASE - ANTI-INFECTIVE
    # =====================================================================
    "infectious_disease.anti_infective.hiv_prevention": {
        "us":  {"patientsK": 1200, "wtpPct": 65, "priceK": 22},
        "eu":  {"patientsK": 600,  "wtpPct": 45, "priceK": 15},
        "row": {"patientsK": 8000, "wtpPct": 25, "priceK": 0.1},
    },
    "infectious_disease.anti_infective.hiv_treatment": {
        "us":  {"patientsK": 1200,  "wtpPct": 85, "priceK": 45},
        "eu":  {"patientsK": 900,   "wtpPct": 80, "priceK": 25},
        "row": {"patientsK": 25000, "wtpPct": 65, "priceK": 0.1},
    },

    # =====================================================================
    # INFECTIOUS DISEASE - VACCINES
    # =====================================================================
    "infectious_disease.vaccines.chikungunya": {
        "us":  {"patientsK": 500,  "wtpPct": 45, "priceK": 0.3},
        "eu":  {"patientsK": 200,  "wtpPct": 35, "priceK": 0.2},
        "row": {"patientsK": 3000, "wtpPct": 20, "priceK": 0.05},
    },
    "infectious_disease.vaccines.lyme": {
        "us":  {"patientsK": 20000, "wtpPct": 40, "priceK": 0.2},
        "eu":  {"patientsK": 15000, "wtpPct": 30, "priceK": 0.15},
        "row": {"patientsK": 50000, "wtpPct": 15, "priceK": 0.1},
    },
    "infectious_disease.vaccines.shigella_zika": {
        "us":  {"patientsK": 5000,   "wtpPct": 25, "priceK": 0.15},
        "eu":  {"patientsK": 2000,   "wtpPct": 20, "priceK": 0.1},
        "row": {"patientsK": 100000, "wtpPct": 35, "priceK": 0.02},
    },
    "infectious_disease.vaccines.travel": {
        "us":  {"patientsK": 30000,  "wtpPct": 55, "priceK": 0.25},
        "eu":  {"patientsK": 80000,  "wtpPct": 50, "priceK": 0.2},
        "row": {"patientsK": 200000, "wtpPct": 40, "priceK": 0.1},
    },

    # =====================================================================
    # OPHTHALMOLOGY - ANTERIOR & NEURO
    # =====================================================================
    "ophthalmology.anterior_neuro.deb_ocular": {
        "us":  {"patientsK": 3, "wtpPct": 55, "priceK": 350},
        "eu":  {"patientsK": 4, "wtpPct": 30, "priceK": 230},
        "row": {"patientsK": 1, "wtpPct": 10, "priceK": 100},
    },
    "ophthalmology.anterior_neuro.dry_eye": {
        "us":  {"patientsK": 16000,  "wtpPct": 40, "priceK": 7},
        "eu":  {"patientsK": 30000,  "wtpPct": 30, "priceK": 2},
        "row": {"patientsK": 15000,  "wtpPct": 20, "priceK": 0.5},
    },
    "ophthalmology.anterior_neuro.naion": {
        "us":  {"patientsK": 6,  "wtpPct": 50, "priceK": 40},
        "eu":  {"patientsK": 8,  "wtpPct": 30, "priceK": 25},
        "row": {"patientsK": 10, "wtpPct": 10, "priceK": 12},
    },
    "ophthalmology.anterior_neuro.neurotrophic_keratitis": {
        "us":  {"patientsK": 5, "wtpPct": 60, "priceK": 96},
        "eu":  {"patientsK": 7, "wtpPct": 45, "priceK": 60},
        "row": {"patientsK": 4, "wtpPct": 20, "priceK": 35},
    },
    "ophthalmology.anterior_neuro.optic_neuritis": {
        "us":  {"patientsK": 15, "wtpPct": 45, "priceK": 50},
        "eu":  {"patientsK": 20, "wtpPct": 30, "priceK": 30},
        "row": {"patientsK": 12, "wtpPct": 15, "priceK": 15},
    },
    "ophthalmology.anterior_neuro.ted": {
        "us":  {"patientsK": 50, "wtpPct": 65, "priceK": 450},
        "eu":  {"patientsK": 70, "wtpPct": 40, "priceK": 280},
        "row": {"patientsK": 30, "wtpPct": 15, "priceK": 150},
    },

    # =====================================================================
    # OPHTHALMOLOGY - RETINA
    # =====================================================================
    "ophthalmology.retina.dme": {
        "us":  {"patientsK": 750,  "wtpPct": 70, "priceK": 11},
        "eu":  {"patientsK": 1000, "wtpPct": 55, "priceK": 6},
        "row": {"patientsK": 500,  "wtpPct": 30, "priceK": 2},
    },
    "ophthalmology.retina.dr": {
        "us":  {"patientsK": 800,  "wtpPct": 65, "priceK": 11},
        "eu":  {"patientsK": 1100, "wtpPct": 50, "priceK": 6},
        "row": {"patientsK": 4000, "wtpPct": 25, "priceK": 2},
    },
    "ophthalmology.retina.ga": {
        "us":  {"patientsK": 1000, "wtpPct": 35, "priceK": 25},
        "eu":  {"patientsK": 1500, "wtpPct": 10, "priceK": 15},
        "row": {"patientsK": 200,  "wtpPct": 10, "priceK": 8},
    },
    "ophthalmology.retina.nvamd": {
        "us":  {"patientsK": 200,  "wtpPct": 80, "priceK": 11},
        "eu":  {"patientsK": 300,  "wtpPct": 65, "priceK": 6},
        "row": {"patientsK": 1000, "wtpPct": 35, "priceK": 2},
    },

    # =====================================================================
    # OPHTHALMOLOGY - OPTIC NERVE
    # =====================================================================
    "ophthalmology.optic_nerve.lhon": {
        "us":  {"patientsK": 4, "wtpPct": 45, "priceK": 800},
        "eu":  {"patientsK": 6, "wtpPct": 30, "priceK": 500},
        "row": {"patientsK": 3, "wtpPct": 10, "priceK": 200},
    },
    "ophthalmology.optic_nerve.nmosd": {
        "us":  {"patientsK": 15, "wtpPct": 75, "priceK": 500},
        "eu":  {"patientsK": 20, "wtpPct": 55, "priceK": 350},
        "row": {"patientsK": 20, "wtpPct": 30, "priceK": 150},
    },

    # =====================================================================
    # RESPIRATORY - INFLAMMATORY
    # =====================================================================
    "respiratory.inflammatory.asthma_severe": {
        "us":  {"patientsK": 2500,  "wtpPct": 70, "priceK": 40},
        "eu":  {"patientsK": 3000,  "wtpPct": 55, "priceK": 22},
        "row": {"patientsK": 25000, "wtpPct": 25, "priceK": 10},
    },
    "respiratory.inflammatory.copd": {
        "us":  {"patientsK": 3000,  "wtpPct": 60, "priceK": 40},
        "eu":  {"patientsK": 4000,  "wtpPct": 40, "priceK": 22},
        "row": {"patientsK": 30000, "wtpPct": 15, "priceK": 1},
    },
}

PEN_PCT = {
    "musculoskeletal.bone_cartilage.achondroplasia": 40,
    "musculoskeletal.bone_cartilage.osteoporosis": 25,
    "musculoskeletal.neuromuscular.cms": 20,
    "musculoskeletal.neuromuscular.dm1": 25,
    "musculoskeletal.neuromuscular.dmd.exon45": 35,
    "musculoskeletal.neuromuscular.dmd.exon51": 35,
    "musculoskeletal.neuromuscular.dmd.exon53": 35,
    "musculoskeletal.neuromuscular.dmd.gene_therapy": 12,
    "musculoskeletal.neuromuscular.fshd": 30,
    "musculoskeletal.neuromuscular.lgmd": 15,
    "infectious_disease.anti_infective.hiv_prevention": 35,
    "infectious_disease.anti_infective.hiv_treatment": 40,
    "infectious_disease.vaccines.chikungunya": 30,
    "infectious_disease.vaccines.lyme": 25,
    "infectious_disease.vaccines.shigella_zika": 20,
    "infectious_disease.vaccines.travel": 25,
    "ophthalmology.anterior_neuro.deb_ocular": 25,
    "ophthalmology.anterior_neuro.dry_eye": 15,
    "ophthalmology.anterior_neuro.naion": 15,
    "ophthalmology.anterior_neuro.neurotrophic_keratitis": 35,
    "ophthalmology.anterior_neuro.optic_neuritis": 20,
    "ophthalmology.anterior_neuro.ted": 30,
    "ophthalmology.retina.dme": 35,
    "ophthalmology.retina.dr": 30,
    "ophthalmology.retina.ga": 10,
    "ophthalmology.retina.nvamd": 50,
    "ophthalmology.optic_nerve.lhon": 20,
    "ophthalmology.optic_nerve.nmosd": 40,
    "respiratory.inflammatory.asthma_severe": 25,
    "respiratory.inflammatory.copd": 10,
}
