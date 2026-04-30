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
    # source: US HFrEF ~3M (NHANES); ~30% have PH overlap (Group 2) = ~1M
    # diagnosed; severe addressable for novel oral/biologic Rx ~300K. EU5
    # ~400K. ROW ~1.5M. Existing therapies (sacubitril/valsartan, SGLT2i)
    # treat HF base but do not directly target PH overlap. Class peak ~$5B
    # for first-in-class PH-HFrEF agent. Distinct from HFpEF (preserved EF
    # has different cardiac remodeling biology).
    "cardio_metabolic.cardiopulmonary.ph_hfref": {
        "us":  {"patientsK": 300,  "wtpPct": 35, "priceK": 25},
        "eu":  {"patientsK": 400,  "wtpPct": 22, "priceK": 15},
        "row": {"patientsK": 1500, "wtpPct": 5,  "priceK": 5},
    },
    # source: ILD prevalence US ~200K (IPF ~150K + other interstitial lung
    # diseases); ~40% develop pulmonary hypertension overlap (Group 3 PH per
    # WSPH) = ~80K. Severe symptomatic addressable for oral/biologic ~30K.
    # EU5 ~50K. Tyvaso (United Therapeutics) approved 2021 for PH-ILD,
    # ~$300M franchise. Class peak ~$2-3B with new entrants. Orphan pricing.
    "cardio_metabolic.cardiopulmonary.ph_ild": {
        "us":  {"patientsK": 30,  "wtpPct": 50, "priceK": 80},
        "eu":  {"patientsK": 50,  "wtpPct": 30, "priceK": 50},
        "row": {"patientsK": 200, "wtpPct": 8,  "priceK": 15},
    },
    # PAH (Pulmonary Arterial Hypertension, WSPH Group 1): rare progressive
    # disease (~3-15 cases per 1M). US ~40K diagnosed (~30K functional class
    # II-IV active treatment), EU5 ~50K, ROW ~150K. Class peers: ERA (Tracleer/
    # Opsumit/Letairis), PDE5i (Adcirca/Revatio), prostacyclins (Tyvaso/Remodulin/
    # Uptravi/Yutrepia), riociguat (Adempas), sotatercept (Winrevair, Merck
    # post Acceleron $11.5B 2021). Winrevair launched 2024 as first activin
    # signaling pathway agent; ~$1.4B 2025 (+233% YoY); ZENITH outcomes 76%
    # MACE+death+transplant reduction. Class peak ~$10-12B globally.
    # source: PAH Registry / REVEAL; PHA US 2024; EU5 ESC PH guidelines.
    "cardio_metabolic.cardiopulmonary.pah": {
        "us":  {"patientsK": 40,  "wtpPct": 75, "priceK": 110},
        "eu":  {"patientsK": 50,  "wtpPct": 60, "priceK": 65},
        "row": {"patientsK": 150, "wtpPct": 18, "priceK": 25},
    },

    # ==================== HEART FAILURE (general, not PH-overlap) ====================
    # Distinct from cardiopulmonary.ph_hfref/hfpef (which capture PH-HF overlap).
    # General HF treated population is much larger.

    # Heart failure with reduced ejection fraction (HFrEF, NYHA II-IV):
    # ~3M US HFrEF, ~4M EU, ~15M ROW. Class: Entresto (Novartis sacubitril/
    # valsartan ~$8B 2024), SGLT2 (Farxiga + Jardiance label expansion),
    # ARNI/ACE/ARB legacy, MRA (spironolactone/eplerenone). Class peak
    # ~$15-20B globally with SGLT2 + Entresto adoption.
    # source: AHA 2024 HF stats; Novartis + AZN + LLY 10-Ks.
    "cardio_metabolic.heart_failure.hfref": {
        "us":  {"patientsK": 3000,  "wtpPct": 55, "priceK": 5},
        "eu":  {"patientsK": 4000,  "wtpPct": 42, "priceK": 3},
        "row": {"patientsK": 15000, "wtpPct": 12, "priceK": 1.2},
    },
    # Heart failure with preserved ejection fraction (HFpEF, NYHA II-IV):
    # ~3.5M US HFpEF, ~5M EU, ~16M ROW. Class: Farxiga (DELIVER 2022) +
    # Jardiance (EMPEROR-Preserved 2021) became 1L; Entresto (PARAGON-HF
    # marginal). Class peak ~$10-12B globally (overlapping but not equal
    # with HFrEF spend).
    "cardio_metabolic.heart_failure.hfpef": {
        "us":  {"patientsK": 3500,  "wtpPct": 50, "priceK": 5},
        "eu":  {"patientsK": 5000,  "wtpPct": 38, "priceK": 3},
        "row": {"patientsK": 16000, "wtpPct": 10, "priceK": 1.2},
    },
    # Hypertrophic cardiomyopathy (HCM): obstructive (oHCM) ~250K US
    # diagnosed, ~350K EU5, ~1M ROW. Branded class: Camzyos (BMS
    # mavacamten cardiac myosin inhibitor, ~$1.3B 2025; first-in-class,
    # approved oHCM 2022 + EXPLORER + VALOR), aficamten (Cytokinetics
    # cardiac myosin Ph3 SEQUOIA + ACACIA, NDA accepted PDUFA 2025).
    # Generic disopyramide + beta-blockers standard background. Net
    # branded ~$90K/yr.
    "cardio_metabolic.heart_failure.hcm": {
        "us":  {"patientsK": 250,  "wtpPct": 60, "priceK": 90},
        "eu":  {"patientsK": 350,  "wtpPct": 42, "priceK": 55},
        "row": {"patientsK": 1000, "wtpPct": 12, "priceK": 18},
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
    # Outpatient hypertension (generic ACEi/ARB/CCB/beta-blocker class):
    # ~120M US adults with HTN, ~80M on Rx. Class is ~95% generic (amlodipine
    # / lisinopril / losartan / metoprolol / atenolol / HCTZ all <$50/yr).
    # Branded tail: Norvasc remnants (Pfizer ~$300M global), Inderal LA
    # (propranolol ER), Cardura/Cardura XL (doxazosin), Vasotec/Vaseretic.
    # Total US branded HTN ~$1.5B, declining. Class peak ~$3B globally with
    # biosimilar/branded combo erosion. Distinct from agt_knockdown niche.
    # Chronic venous insufficiency / venous disease (CVD): chronic venous
    # reflux + valve incompetence in lower extremities; symptoms = leg
    # heaviness, edema, varicose veins, ulcers (advanced CEAP C5-C6).
    # ~25M US adults symptomatic, ~50M EU, ~300M ROW. Branded class:
    # Daflon (diosmin/hesperidin micronized purified flavonoid fraction;
    # Servier ~EUR 600M+ legacy in EU/Asia/LATAM); compression therapy +
    # surgical/endovenous interventions are non-pharma SoC. Net branded
    # ~EUR 50/mo (~$0.6K/yr).
    # source: ACOG/SVS CVD epi; Servier 10-K; AAFP review.
    "cardio_metabolic.vascular.chronic_venous_disease": {
        "us":  {"patientsK": 25000,  "wtpPct": 8,  "priceK": 0.6},
        "eu":  {"patientsK": 50000,  "wtpPct": 6,  "priceK": 0.4},
        "row": {"patientsK": 300000, "wtpPct": 2,  "priceK": 0.15},
    },
    "cardio_metabolic.hypertension.outpatient_generic": {
        # Bumped to reflect branded ARB / ARB-CCB FDC / aliskiren residuals:
        # Diovan/Exforge (Novartis ~$1.3B), Benicar/Edarbi/Atacand/Avapro
        # tail brands. Generic-eroded but ~$5B class globally.
        "us":  {"patientsK": 80000,  "wtpPct": 12, "priceK": 0.30},
        "eu":  {"patientsK": 100000, "wtpPct": 10, "priceK": 0.20},
        "row": {"patientsK": 500000, "wtpPct": 5,  "priceK": 0.05},
    },
    # Resistant hypertension (3+ antihypertensives w/ uncontrolled BP):
    # ~5M US per ACC criteria. Distinct from agt_knockdown niche (zilebesiran
    # RNAi specifically). Baxdrostat (AZ aldosterone synthase inhibitor) Ph3
    # BAX-CSO; PDUFA Q2 2026. Class peers: spironolactone generic (off-label),
    # finerenone Bayer (CKD label primarily), zilebesiran. Branded class
    # peak ~$3-5B globally for novel resistant HTN drugs.
    "cardio_metabolic.hypertension.resistant": {
        "us":  {"patientsK": 5000,  "wtpPct": 30, "priceK": 4},
        "eu":  {"patientsK": 7000,  "wtpPct": 22, "priceK": 2.5},
        "row": {"patientsK": 30000, "wtpPct": 6,  "priceK": 0.8},
    },
    # Lipids generic statin class: atorvastatin (Lipitor remnants ~$1B
    # globally), rosuvastatin (Crestor remnants), simvastatin/pravastatin/
    # lovastatin generic. ~30M US on statins; branded tail ~$2-3B globally
    # post-LOE wave 2011-2016 (Japan + China + EM where generic substitution
    # slower drives branded tail). Distinct from PCSK9 class (lipids.ldl_cv_risk).
    # priceK reflects average branded retail (not generic).
    "cardio_metabolic.lipids.statin_generic": {
        "us":  {"patientsK": 30000,  "wtpPct": 15, "priceK": 0.15},
        "eu":  {"patientsK": 40000,  "wtpPct": 12, "priceK": 0.08},
        "row": {"patientsK": 200000, "wtpPct": 8,  "priceK": 0.04},
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
    # Primary biliary cholangitis (PBC): chronic autoimmune cholestatic liver
    # disease, mostly women 40-60. Anti-AMA-positive in ~95%. Standard care
    # ursodeoxycholic acid (UDCA) generic 1L; 2L PPAR Iqirvo (Ipsen elafibranor
    # FDA Jun 2024) and OCA (Ocaliva, Intercept). source: AASLD PBC US ~60K
    # diagnosed; EU5 ~80K; ROW ~200K. Net branded 2L tx ~$50K/yr (Iqirvo $60K WAC).
    "cardio_metabolic.liver.pbc": {
        "us":  {"patientsK": 60,   "wtpPct": 60, "priceK": 50},
        "eu":  {"patientsK": 80,   "wtpPct": 45, "priceK": 30},
        "row": {"patientsK": 200,  "wtpPct": 12, "priceK": 12},
    },
    # Pediatric cholestatic liver disease: rare genetic/cholestatic conditions
    # affecting infants/children incl. PFIC (~2K US progressive familial intra-
    # hepatic cholestasis), Alagille syndrome (~3K, JAG1/NOTCH2), biliary atresia
    # (~0.5K/yr incidence). SoC liver transplant; Bylvay (Ipsen odevixibat IBAT
    # inhibitor, ex-Albireo $1.3B 2023) is first FDA-approved targeted therapy.
    # source: NORD/Orphanet rare cholestasis epi. Net branded ~$200K/yr orphan.
    "cardio_metabolic.liver.pediatric_cholestasis": {
        "us":  {"patientsK": 5,    "wtpPct": 75, "priceK": 200},
        "eu":  {"patientsK": 8,    "wtpPct": 55, "priceK": 120},
        "row": {"patientsK": 30,   "wtpPct": 14, "priceK": 40},
    },
    # Hepatic encephalopathy (HE): neuropsychiatric complication of decompensated
    # cirrhosis (~50% of cirrhosis pts develop HE). Branded class: Xifaxan
    # (Bausch rifaximin ~$700M HE share; reduces recurrence) + lactulose
    # generic 1L. SoC = chronic Xifaxan + lactulose. source: AASLD HE US
    # ~150K branded-treated, EU5 ~200K; ROW ~1.5M (large viral hepatitis
    # burden). Net branded ~$20K/yr (chronic rifaximin).
    "cardio_metabolic.liver.hepatic_encephalopathy": {
        "us":  {"patientsK": 150,   "wtpPct": 60, "priceK": 20},
        "eu":  {"patientsK": 200,   "wtpPct": 45, "priceK": 12},
        "row": {"patientsK": 1500,  "wtpPct": 12, "priceK": 4},
    },
    # Decompensated cirrhosis (advanced liver disease with ascites, hepatorenal
    # syndrome, hepatic encephalopathy): heterogeneous etiologies (alcohol,
    # MASH, viral hepatitis, autoimmune). SoC: albumin infusions (Grifols,
    # CSL, Baxter), terlipressin (Mallinckrodt Terlivaz for HRS-1 FDA 2022),
    # lactulose (HE), liver tx ultimate. Branded class ~$4-5B globally
    # (mostly albumin commodity ~$300/g x 100g/yr per pt = $30K). source:
    # AASLD decompensated cirrhosis prevalence ~250K US, ~350K EU5; ROW
    # ~3M (huge LMIC viral hep burden). Net branded ~$25K/yr blended.
    "cardio_metabolic.liver.cirrhosis_decompensated": {
        "us":  {"patientsK": 250,   "wtpPct": 60, "priceK": 25},
        "eu":  {"patientsK": 350,   "wtpPct": 45, "priceK": 14},
        "row": {"patientsK": 3000,  "wtpPct": 12, "priceK": 5},
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
    # Propionic acidemia (PA): autosomal recessive organic acidemia caused by
    # propionyl-CoA carboxylase deficiency (PCCA / PCCB). Severe metabolic
    # decompensations w/ hyperammonemia, neurologic injury, cardiomyopathy.
    # source: NORD / Orphanet PA prevalence US ~3K diagnosed (incidence 1:50K),
    # EU5 ~5K, ROW ~10K (under-diagnosed in low-income settings).
    # No approved disease-modifying therapy today (SoC = protein-restricted
    # diet, carnitine, biotin, liver tx). Moderna mRNA-3927 Ph2 registrational
    # in 2026, partnered Recordati Jan 2026. Aspirational pricing similar to
    # other ultra-rare mRNA therapeutics ~$450K/yr blended.
    "cardio_metabolic.rare_metabolic.propionic_acidemia": {
        "us":  {"patientsK": 3,     "wtpPct": 75, "priceK": 450},
        "eu":  {"patientsK": 5,     "wtpPct": 60, "priceK": 275},
        "row": {"patientsK": 10,    "wtpPct": 25, "priceK": 130},
    },
    # Methylmalonic acidemia (MMA): autosomal recessive organic acidemia
    # caused by methylmalonyl-CoA mutase deficiency (MUT, MMAA, MMAB).
    # Similar phenotype to PA -- metabolic crises, renal failure, NDD.
    # source: NORD / Orphanet MMA prevalence US ~5K diagnosed (incidence
    # 1:30K-50K, isolated MMA), EU5 ~8K, ROW ~15K. No approved disease-
    # modifying therapy (SoC = diet + B12 for cobalamin-responsive subset).
    # Moderna mRNA-3705 Ph2, FDA START program 2026 reg study.
    # Aspirational pricing ~$450K/yr blended.
    "cardio_metabolic.rare_metabolic.methylmalonic_acidemia": {
        "us":  {"patientsK": 5,     "wtpPct": 75, "priceK": 450},
        "eu":  {"patientsK": 8,     "wtpPct": 60, "priceK": 275},
        "row": {"patientsK": 15,    "wtpPct": 25, "priceK": 130},
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
    # Hypophosphatasia (HPP): rare inherited disorder of bone mineralization
    # (TNSALP/ALPL deficiency). ~3K US diagnosed (peds + adult); ~5K EU;
    # ~15K ROW. Strensiq (asfotase alfa, AZ/Alexion) is only approved enzyme
    # replacement; ~$1.5B 2025. Class peak ~$2B globally.
    # source: Alexion/AZ 10-K; NORD HPP.
    "endocrine.calcium.hypophosphatasia": {
        "us":  {"patientsK": 3,   "wtpPct": 90, "priceK": 700},
        "eu":  {"patientsK": 5,   "wtpPct": 80, "priceK": 480},
        "row": {"patientsK": 15,  "wtpPct": 22, "priceK": 200},
    },
    # X-linked hypophosphatemia (XLH; PHEX LoF) + tumor-induced osteomalacia
    # (TIO; benign mesenchymal tumor secreting FGF23): FGF23-driven phosphate-
    # wasting disorders causing rickets/osteomalacia. XLH prevalence ~1:20,000
    # -> ~25K US, ~30K EU diagnosed (Ultragenyx/KKD; XLH Network registry);
    # ROW ~80K (largely undiagnosed). TIO ultra-rare ~1K US prevalent.
    # Sole branded therapy: Crysvita (burosumab anti-FGF23 mAb, Kyowa Kirin +
    # Ultragenyx ex-Asia) FDA 2018; SoC pre-2018 = oral phosphate + calcitriol
    # (high adherence burden + nephrocalcinosis). Pricing: Crysvita WAC ~$200K
    # pediatric, ~$300K adult (weight-based).
    # source: NORD XLH; KKD 10-K (Crysvita ~$540M FY24); Ultragenyx 10-K.
    "endocrine.calcium.xlh": {
        "us":  {"patientsK": 25,  "wtpPct": 80, "priceK": 250},
        "eu":  {"patientsK": 30,  "wtpPct": 60, "priceK": 150},
        "row": {"patientsK": 80,  "wtpPct": 14, "priceK": 50},
    },
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
    # Cushing's disease (pituitary ACTH-secreting adenoma): ~3K US prevalent
    # surgically-refractory, ~4K EU5, ~10K ROW. Class: Signifor (pasireotide
    # Novartis SOM agonist ~$50M), Isturisa (osilodrostat Recordati 11-beta-
    # hydroxylase inhibitor ~$200M), Korlym (mifepristone Corcept ~$500M),
    # Mifepristone Recorlev (Xeris ~$50M). Class globally ~$0.8B branded.
    "endocrine.pituitary.cushings": {
        "us":  {"patientsK": 3,     "wtpPct": 70, "priceK": 110},
        "eu":  {"patientsK": 4,     "wtpPct": 55, "priceK": 65},
        "row": {"patientsK": 10,    "wtpPct": 18, "priceK": 25},
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
    # GH deficiency (pediatric idiopathic GHD + adult GHD): broader than
    # initially scoped. Global branded somatropin market ~$3.5-4B with multiple
    # players: Novo Norditropin/Sogroya ~$860M, Pfizer Genotropin ~$650M,
    # Novartis Omnitrope (biosim) ~$300M, Lilly Humatrope, Merck Saizen,
    # Ascendis Skytrofa (long-acting). US patientsK includes GHD peds (~12K),
    # GHD adult (~40K), ISS (~15K), Turner syndrome + Noonan + SHOX + Prader-
    # Willi (~13K) -- broader treatable pop ~80K. Daily injection $25K +
    # weekly long-acting (Sogroya, Skytrofa) $40K -> blended ~$32K/yr branded.
    # source: Pituitary Society 2024 prevalence; Novo + Pfizer + Ascendis 10-Ks.
    "endocrine.pituitary.gh_deficiency": {
        "us":  {"patientsK": 80,  "wtpPct": 60, "priceK": 32},
        "eu":  {"patientsK": 100, "wtpPct": 50, "priceK": 20},
        "row": {"patientsK": 400, "wtpPct": 15, "priceK": 10},
    },

    # ==================== LYSOSOMAL STORAGE DISEASES (LSDs) ====================
    # Genzyme legacy franchise; enzyme replacement therapy class. Sanofi dominant
    # post-Bioverativ; Takeda + BioMarin compete in some indications.

    # Gaucher disease (glucocerebrosidase deficiency, GBA): ~6K US (Type 1 most
    # common), ~12K EU, ~30K ROW (high in Ashkenazi Jewish ancestry). Class:
    # Cerezyme (imiglucerase ERT, Sanofi $700M), Cerdelga (eliglustat oral SRT,
    # Sanofi), VPRIV (velaglucerase, Takeda), Elelyso (taliglucerase, Pfizer
    # generic). Class peak ~$1.5B globally; biosimilar pressure on ERT.
    # source: NORD Gaucher; Sanofi Genzyme + Takeda 10-Ks.
    "endocrine.lysosomal_storage.gaucher": {
        "us":  {"patientsK": 6,   "wtpPct": 85, "priceK": 250},
        "eu":  {"patientsK": 12,  "wtpPct": 75, "priceK": 165},
        "row": {"patientsK": 30,  "wtpPct": 20, "priceK": 70},
    },
    # Fabry disease (alpha-galactosidase A deficiency, GLA): ~5K US,
    # ~8K EU, ~25K ROW. Class: Fabrazyme (agalsidase beta, Sanofi $600M),
    # Replagal (agalsidase alfa, Takeda; not US), Galafold (migalastat oral
    # chaperone, Amicus). Class peak ~$1.5B globally.
    "endocrine.lysosomal_storage.fabry": {
        "us":  {"patientsK": 5,   "wtpPct": 85, "priceK": 350},
        "eu":  {"patientsK": 8,   "wtpPct": 75, "priceK": 230},
        "row": {"patientsK": 25,  "wtpPct": 18, "priceK": 90},
    },
    # Pompe disease (acid alpha-glucosidase deficiency, GAA): ~3.5K US (IOPD +
    # LOPD), ~5K EU, ~15K ROW. Class: Myozyme/Lumizyme (alglucosidase alfa
    # legacy, Sanofi), Nexviazyme/Nexviadyme (avalglucosidase alfa next-gen,
    # Sanofi $600M growing), Pombiliti+Opfolda (Amicus next-gen). Class peak
    # ~$1.5B with Nexviazyme growth.
    "endocrine.lysosomal_storage.pompe": {
        "us":  {"patientsK": 3.5, "wtpPct": 90, "priceK": 600},
        "eu":  {"patientsK": 5,   "wtpPct": 80, "priceK": 400},
        "row": {"patientsK": 15,  "wtpPct": 22, "priceK": 150},
    },
    # MPS I (Hurler/Scheie syndrome, IDUA deficiency): ~1.5K US, ~2K EU,
    # ~8K ROW. Class: Aldurazyme (laronidase, Sanofi/BioMarin co-promote
    # ~$300M), HSCT for severe pediatric. Class peak ~$500M.
    "endocrine.lysosomal_storage.mps1": {
        "us":  {"patientsK": 1.5, "wtpPct": 85, "priceK": 400},
        "eu":  {"patientsK": 2,   "wtpPct": 75, "priceK": 270},
        "row": {"patientsK": 8,   "wtpPct": 18, "priceK": 100},
    },
    # ASMD (acid sphingomyelinase deficiency, formerly Niemann-Pick A/B):
    # ultra-rare. ~1K US, ~1.5K EU, ~5K ROW. Class: Xenpozyme (olipudase alfa,
    # Sanofi only approved ERT). Class peak ~$300M.
    # Alpha-mannosidosis (MAN2B1 LoF; lysosomal storage disorder): rare
    # autosomal recessive deficiency of lysosomal alpha-mannosidase causing
    # progressive intellectual disability + hearing loss + skeletal/immune
    # abnormalities. ~500 US prevalent, ~700 EU, ~3K ROW (NORD; Chiesi
    # GRD). Sole branded therapy: Lamzede (velmanase alfa ERT; Chiesi
    # FDA 2023 EU 2018). WAC ~$650K/yr. Distinct from MPS lysosomal
    # disorders (Hunter/Hurler/Sanfilippo/Morquio).
    # source: Borgwardt 2015 J Inherit Metab Dis; NORD; Chiesi 10-K.
    "endocrine.lysosomal_storage.alpha_mannosidosis": {
        "us":  {"patientsK": 0.5,  "wtpPct": 80, "priceK": 650},
        "eu":  {"patientsK": 0.7,  "wtpPct": 60, "priceK": 400},
        "row": {"patientsK": 3,    "wtpPct": 18, "priceK": 130},
    },
    # Generalized lipodystrophy (congenital + acquired; Berardinelli-Seip,
    # Lawrence syndrome, partial subtypes): rare metabolic disorder with
    # near-total loss of adipose tissue + leptin deficiency + severe
    # insulin resistance. ~500 US prevalent, ~700 EU, ~2K ROW. Sole
    # branded therapy: Myalepta (metreleptin recombinant leptin; Chiesi
    # via Amryt; FDA 2014). Pricing: Myalepta WAC ~$700K/yr.
    # source: NORD lipodystrophy; Lipodystrophy United registry.
    "cardio_metabolic.lipids.lipodystrophy": {
        "us":  {"patientsK": 0.5,  "wtpPct": 80, "priceK": 700},
        "eu":  {"patientsK": 0.7,  "wtpPct": 60, "priceK": 450},
        "row": {"patientsK": 2,    "wtpPct": 15, "priceK": 130},
    },
    "endocrine.lysosomal_storage.asmd": {
        "us":  {"patientsK": 1,   "wtpPct": 90, "priceK": 600},
        "eu":  {"patientsK": 1.5, "wtpPct": 80, "priceK": 400},
        "row": {"patientsK": 5,   "wtpPct": 18, "priceK": 150},
    },
}

PEN_PCT = {
    "cardio_metabolic.attr.attr_cm": 45,
    "cardio_metabolic.attr.attr_pn": 55,
    "cardio_metabolic.cardiopulmonary.ph_hfpef": 20,
    "cardio_metabolic.cardiopulmonary.ph_hfref": 20,
    "cardio_metabolic.cardiopulmonary.ph_ild": 30,
    "cardio_metabolic.cardiopulmonary.pah": 65,
    "cardio_metabolic.diabetes.t1d": 12,
    "cardio_metabolic.diabetes.t2d": 10,
    "cardio_metabolic.hypertension.agt_knockdown": 8,
    "cardio_metabolic.heart_failure.hfref": 25,
    "cardio_metabolic.heart_failure.hfpef": 18,
    "cardio_metabolic.heart_failure.hcm": 35,
    "cardio_metabolic.hypertension.outpatient_generic": 8,
    "cardio_metabolic.vascular.chronic_venous_disease": 12,
    "cardio_metabolic.hypertension.resistant": 18,
    "cardio_metabolic.lipids.statin_generic": 10,
    "endocrine.calcium.hypophosphatasia": 60,
    "endocrine.calcium.xlh": 65,
    "endocrine.lysosomal_storage.gaucher": 60,
    "endocrine.lysosomal_storage.fabry": 55,
    "endocrine.lysosomal_storage.pompe": 55,
    "endocrine.lysosomal_storage.mps1": 50,
    "endocrine.lysosomal_storage.asmd": 50,
    "endocrine.lysosomal_storage.alpha_mannosidosis": 55,
    "cardio_metabolic.lipids.lipodystrophy": 50,
    "cardio_metabolic.lipids.ldl_cv_risk": 6,
    "cardio_metabolic.lipids.lpa": 3,
    "cardio_metabolic.lipids.triglycerides": 25,
    "cardio_metabolic.liver.a1at": 15,
    "cardio_metabolic.liver.hbv_functional_cure": 4,
    "cardio_metabolic.liver.mash": 8,
    "cardio_metabolic.liver.pld_adpkd": 15,
    "cardio_metabolic.liver.cirrhosis_decompensated": 30,
    "cardio_metabolic.liver.hepatic_encephalopathy": 35,
    "cardio_metabolic.liver.pbc": 25,
    "cardio_metabolic.liver.pediatric_cholestasis": 50,
    "cardio_metabolic.obesity.general": 5,
    "cardio_metabolic.obesity.rare_genetic.hypothalamic_obesity": 30,
    "cardio_metabolic.obesity.rare_genetic.monogenic_mc4r": 35,
    "cardio_metabolic.obesity.rare_genetic.prader_willi": 40,
    "cardio_metabolic.rare_metabolic.homocystinuria": 30,
    "cardio_metabolic.rare_metabolic.hyperoxaluria": 50,
    "cardio_metabolic.rare_metabolic.porphyria": 40,
    "cardio_metabolic.rare_metabolic.propionic_acidemia": 35,
    "cardio_metabolic.rare_metabolic.methylmalonic_acidemia": 35,
    "cardio_metabolic.thrombosis.anticoagulation": 4,
    "endocrine.adrenal.cah": 35,
    "endocrine.calcium.adh1": 25,
    "endocrine.pituitary.acromegaly": 20,
    "endocrine.pituitary.cushings": 35,
    "endocrine.thyroid.graves": 15,
    "cardio_metabolic.lipids.hofh": 35,
    "endocrine.pituitary.gh_deficiency": 35,
}
