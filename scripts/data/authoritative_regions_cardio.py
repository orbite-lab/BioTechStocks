# -*- coding: utf-8 -*-
# Authoritative slider values extracted from tooltips_cardio.py
# patientsK: primary treated/eligible number (M -> K, 1M = 1000K)
# wtpPct: first market-level WTP percentage
# priceK: blended dollar figure (M -> K, 1M = 1000K)

REGIONS = {
    # ==================== ATTR ====================
    # source: ATTR-CM diagnosed prevalence ~80K US, ~60K EU5, ~40K ROW per
    # Pfizer/BMS IR + ATTR registry data. Branded class: Vyndaqel/Vyndamax
    # ~$5B 2025 (Pfizer) + Amvuttra-CM (Alnylam, expanded label 2025) +
    # Acoramidis (BBIO, launched 2025). Class peak ~$10-15B by 2030 with
    # Acoramidis + ATTR-CRISPR (NTLA NEXZ) entrants. Prior $30B at $250K
    # uniform priceK assumed every diagnosed pt on tafamidis/Amvuttra at
    # WAC; ~2.5x off given ~50% of diagnosed pts are still on supportive
    # care or pending diagnosis.
    "cardio_metabolic.attr.attr_cm": {
        "us":  {"patientsK": 80,    "wtpPct": 55, "priceK": 180},
        "eu":  {"patientsK": 60,    "wtpPct": 40, "priceK": 120},
        "row": {"patientsK": 40,    "wtpPct": 20, "priceK": 70},
    },
    # source: ATTR-PN ~10K US (smaller than ATTR-CM); orphan-priced franchise.
    # Onpattro (Alnylam, declining post-Amvuttra) + Wainua (IONS/AZ) + Amvuttra
    # ~$3B today, peak $4-5B. Prior $6B at $460K WAC slightly overstated.
    "cardio_metabolic.attr.attr_pn": {
        "us":  {"patientsK": 10,    "wtpPct": 65, "priceK": 350},
        "eu":  {"patientsK": 10,    "wtpPct": 50, "priceK": 220},
        "row": {"patientsK": 8,     "wtpPct": 25, "priceK": 120},
    },

    # ==================== DIABETES ====================
    "cardio_metabolic.diabetes.t1d": {
        "us":  {"patientsK": 1900,  "wtpPct": 85, "priceK": 5},
        "eu":  {"patientsK": 1500,  "wtpPct": 80, "priceK": 2.5},
        "row": {"patientsK": 8000,  "wtpPct": 40, "priceK": 1},
    },
    # source: US T2D ~38M (CDC) but branded-priced patients ~17M (~70% on Rx,
    # but ~80% of those receive generic metformin/sulfonylureas at <$300/yr
    # before stepping up). Branded class breakdown: GLP-1 diabetes labels
    # (Ozempic/Trulicity/Mounjaro/Rybelsus) ~$30B + insulin franchise $15-20B
    # + SGLT2 (Jardiance/Farxiga/Invokana) ~$10B + DPP4 declining ~$3B = ~$60B
    # current global, projected $80-90B peak with GLP-1 class expansion.
    # Prior values (90% WTP at $4K US uniform) treated entire diagnosed
    # population as on premium GLP-1; ~2x off net economics.
    "cardio_metabolic.diabetes.t2d": {
        "us":  {"patientsK": 25000, "wtpPct": 70, "priceK": 2.5},
        "eu":  {"patientsK": 22000, "wtpPct": 60, "priceK": 1.5},
        "row": {"patientsK": 150000,"wtpPct": 25, "priceK": 0.4},
    },

    # ==================== CARDIOPULMONARY (PH-HFpEF) ====================
    # source: US HFpEF ~3M diagnosed (NHANES); ~30-50% have PH overlap
    # (echocardiographic estPASP > 35) per ESC/AHA guidance = ~1M PH-HFpEF
    # diagnosed; severe symptomatic NYHA III-IV addressable for novel oral
    # therapies ~500K. EU5 ~700K. ROW ~2M. NO approved therapy specifically
    # for PH-HFpEF (Group 2 PH per WSPH classification); off-label PDE5i
    # contraindicated by RELAX/PILUMA-PH-HFpEF. First-mover oral pricing
    # $25-35K/yr specialty cardiology. Class peak TAM ~$5-8B if first agent
    # gets approved; conservative TAM $7B given uncertain payor envelope.
    "cardio_metabolic.cardiopulmonary.ph_hfpef": {
        "us":  {"patientsK": 500,  "wtpPct": 35, "priceK": 25},
        "eu":  {"patientsK": 700,  "wtpPct": 20, "priceK": 15},
        "row": {"patientsK": 2000, "wtpPct": 5,  "priceK": 5},
    },

    # ==================== HYPERTENSION ====================
    # source: AGT knockdown is a brand-new RNAi class addressing resistant
    # hypertension specifically (~5M US per ACC criteria). NOT the entire HTN
    # market (which is generic-dominated, ACEi/ARB/CCB/diuretic at <$50/yr
    # branded TAM <$3B). Zilebesiran (Alnylam/Roche partnership) is the only
    # asset and analyst peak forecasts $2-4B globally. Prior values (10M US
    # at $8K) inflated 10x by treating all HTN at biologic pricing.
    "cardio_metabolic.hypertension.agt_knockdown": {
        "us":  {"patientsK": 1000, "wtpPct": 30, "priceK": 8},
        "eu":  {"patientsK": 1500, "wtpPct": 20, "priceK": 4},
        "row": {"patientsK": 5000, "wtpPct": 5,  "priceK": 1},
    },

    # ==================== LIPIDS ====================
    # source: US ~80M with elevated LDL but statin generics dominate first-
    # line at <$50/yr. Branded class is the high-risk subset addressable by
    # PCSK9 (Repatha + Praluent ~$2B) + Inclisiran/Leqvio ~$1B + Nexletol
    # ~$0.4B + emerging CETP (obicetrapib Ph3) and Lp(a)-specific agents.
    # Total branded class ~$5B today, peak $20-25B with new entrants. Prior
    # TAM $117B treated all elevated-LDL patients as PCSK9-priced -- ~6x off.
    "cardio_metabolic.lipids.ldl_cv_risk": {
        "us":  {"patientsK": 30000, "wtpPct": 25, "priceK": 1.5},
        "eu":  {"patientsK": 35000, "wtpPct": 20, "priceK": 1},
        "row": {"patientsK": 200000,"wtpPct": 8,  "priceK": 0.2},
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
    # source: US MASH ~5M with significant fibrosis F2-F3 (the trial-eligible
    # cohort per AASLD); EU5 ~4M; ROW ~20M but specialty access very limited.
    # Class is launching: Rezdiffra (MDGL) approved Mar 2024, Wegovy MASH on
    # the way, FGF21 + GLP-1 combos in Ph3. Analyst peak forecast for the
    # whole class ~$25B by 2030. Prior $175B TAM at $47K uniform priceK
    # treated all MASH like high-end orphan biologic -- ~7x off.
    "cardio_metabolic.liver.mash": {
        "us":  {"patientsK": 3000,  "wtpPct": 35, "priceK": 12},
        "eu":  {"patientsK": 4000,  "wtpPct": 25, "priceK": 8},
        "row": {"patientsK": 20000, "wtpPct": 8,  "priceK": 2},
    },
    "cardio_metabolic.liver.pld_adpkd": {
        "us":  {"patientsK": 20,    "wtpPct": 65, "priceK": 13},
        "eu":  {"patientsK": 25,    "wtpPct": 55, "priceK": 7},
        "row": {"patientsK": 30,    "wtpPct": 25, "priceK": 4},
    },

    # ==================== OBESITY ====================
    # source: US obesity ~108M (NHANES) but branded-Rx-eligible (BMI >=30 or
    # >=27 w/ comorbidity, with insurance access) ~40M. Net realized price
    # ~$9K/yr after PBM rebates (WAC $13-15K, ~30-40% rebates). Wegovy + Zepbound
    # + Saxenda + diabetes-label GLP-1 spillover = ~$30-40B today, projected
    # peak $150-200B by 2030 per Goldman/MS estimates. Prior TAM $396B at $15K
    # WAC across full 40M US assumed every eligible patient buys at full WAC
    # -- 2x net economics. New TAM $144B sits in the middle of the analyst
    # peak band, with growth headroom.
    "cardio_metabolic.obesity.general": {
        "us":  {"patientsK": 40000, "wtpPct": 30, "priceK": 9},
        "eu":  {"patientsK": 30000, "wtpPct": 20, "priceK": 5},
        "row": {"patientsK": 50000, "wtpPct": 6,  "priceK": 2},
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
    # source: US AFib + VTE patients on anticoagulation ~6M (CDC + AHA
    # registries). Branded DOAC class (Eliquis $13B + Xarelto $7B + Pradaxa
    # ~$2B + Savaysa) ~$22B today globally. Eliquis/Xarelto generic erosion
    # 2026-28 partly offset by emerging Factor XI/XIa class (BHV-1310/abelacimab
    # / asundexian etc.) -- class peak $35-40B. Warfarin generic carries the
    # rest. LMWHs (enoxaparin) generic. Prior $60B at $5K uniform priceK
    # treated entire patient pool as on premium DOAC; ~2x off net economics.
    "cardio_metabolic.thrombosis.anticoagulation": {
        "us":  {"patientsK": 6000,  "wtpPct": 60, "priceK": 3.5},
        "eu":  {"patientsK": 7000,  "wtpPct": 50, "priceK": 1.5},
        "row": {"patientsK": 30000, "wtpPct": 15, "priceK": 0.4},
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
    # source: US Graves' disease prevalence ~150K (NIDDK); EU5 ~200K; ROW ~1M.
    # Standard care is methimazole + RAI + thyroidectomy (all generic); branded
    # franchise emerging via FcRn (batoclimab Ph3 failed Apr 2026) and IgG
    # degraders (BHV-1300 Ph1b -> pivotal H2 2026). Analyst peak forecast for
    # the branded class ~$3-5B globally. NOTE: TED (thyroid-eye disease) is
    # tagged separately under ophthalmology.anterior_neuro.ted with its own
    # Tepezza-anchored TAM. Prior $35B treated all Graves' patients as
    # branded-biologic eligible at $350K -- ~7x off.
    "endocrine.thyroid.graves": {
        "us":  {"patientsK": 150,   "wtpPct": 35, "priceK": 30},
        "eu":  {"patientsK": 200,   "wtpPct": 22, "priceK": 18},
        "row": {"patientsK": 1000,  "wtpPct": 5,  "priceK": 5},
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
    "cardio_metabolic.cardiopulmonary.ph_hfpef": 20,
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
