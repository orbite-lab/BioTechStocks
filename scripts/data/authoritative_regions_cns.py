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
    # source: Dravet syndrome (SCN1A LoF) incidence ~1:15,700 live births
    # (Wu et al., Pediatrics 2015); US prevalent ~38K diagnosed (Dravet
    # Syndrome Foundation); EU5+UK ~50K (Orphanet); ROW ~60K (largely
    # undiagnosed in LMICs). Genetic-confirmed subset addressable by SCN1A
    # ASO (Stoke zorevunersen P3) — distinct drug niche from SCN2A/SCN8A
    # (PRAX relutrigine) and broader DEE pool. Pricing precedent: Fintepla
    # ($96K) + Epidiolex ($32K) + Diacomit (~$30K) + ASO premium (Spinraza
    # $375K maint) → blended class peak ~$80K.
    "cns.epilepsy.dee.dravet": {
        "us":  {"patientsK": 38,  "wtpPct": 80, "priceK": 80},
        "eu":  {"patientsK": 50,  "wtpPct": 60, "priceK": 50},
        "row": {"patientsK": 60,  "wtpPct": 25, "priceK": 12},
    },
    # source: SYNGAP1-related neurodevelopmental disorder, OMIM 612621.
    # Estimated prevalence ~1:10,000-30,000 (SynGAP Research Fund + recent
    # exome-sequencing studies); ~85% of pts have epilepsy (DEE phenotype).
    # US prevalent ~5K; EU5+UK ~7K; ROW ~15K. No approved DMT. Genetic
    # confirmation rate rising rapidly with NGS panel adoption. Pricing
    # pegs to ASO orphan pediatric (Spinraza/Qalsody precedent).
    "cns.epilepsy.dee.syngap1": {
        "us":  {"patientsK": 5,   "wtpPct": 70, "priceK": 60},
        "eu":  {"patientsK": 7,   "wtpPct": 50, "priceK": 35},
        "row": {"patientsK": 15,  "wtpPct": 18, "priceK": 10},
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
    # source: US TD diagnosed ~500K (per AAN guidance + Movement Disorder
    # Society reports). VMAT2 class is the only branded entry: Ingrezza
    # (NBIX) ~$2.5B 2025 sales -> ~$4B peak; Austedo (TEVA) ~$1.5B -> $2.5B
    # peak. Class peak ~$7-8B globally. Prior US TAM 600K x 65% x $70K = $27B
    # priced every TD patient as if on Ingrezza; net realized prices are
    # ~$25-30K/yr after PBM rebates. Right-sizing to ~$7B total.
    "cns.movement.tardive_dyskinesia": {
        "us":  {"patientsK": 500,   "wtpPct": 50, "priceK": 25},
        "eu":  {"patientsK": 500,   "wtpPct": 25, "priceK": 5},
        "row": {"patientsK": 2000,  "wtpPct": 3,  "priceK": 1.5},
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
    # source: US AD ~6M diagnosed (Alzheimer's Association); EU5 ~7M; ROW ~25M.
    # Branded class is the recently-launched anti-amyloid biologic franchise:
    # Leqembi (BIIB/Eisai) ~$300M 2025 + Kisunla (LLY) ~$200M 2025, both still
    # ramping. Class peak forecast $10-15B by 2030 (limited by MCI/early-AD
    # eligibility, ARIA monitoring requirement, infusion logistics). Donepezil
    # + memantine generic carry the rest. Prior US TAM at 50% WTP and $28K
    # priceK assumed all 2M moderate AD on biologics; ~5x off given eligibility
    # constraints. New TAM $11B fits Leqembi+Kisunla peak forecast.
    "cns.neurodegeneration.alzheimer": {
        "us":  {"patientsK": 6000,  "wtpPct": 25, "priceK": 5},
        "eu":  {"patientsK": 8000,  "wtpPct": 12, "priceK": 3},
        "row": {"patientsK": 40000, "wtpPct": 3,  "priceK": 0.5},
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
    # Post-stroke recovery / neuroprotection: chronic neuroinflammation + axonal
    # repair window AFTER acute ischemic stroke event (distinct from acute
    # thrombolytic setting in cardio_metabolic.thrombosis.thrombolytic and
    # AFib-driven stroke prevention in cardio_metabolic.thrombosis.anticoagulation).
    # No approved disease-modifying neuroprotectant globally (edaravone Japan
    # only, weak evidence; nerinetide/NA-1 Ph3 failed; 3K3A-APC Ph3 controversial).
    # source: AHA stroke incidence US ~800K/yr (~600K ischemic survivors eligible
    # for recovery window); EU5 ~900K; ROW ~10M. CRVO neflamapimod p38 MAPK
    # inhibitor Ph2a only material covered candidate.
    "cns.neurodegeneration.post_stroke_recovery": {
        "us":  {"patientsK": 800,   "wtpPct": 90, "priceK": 12},
        "eu":  {"patientsK": 1100,  "wtpPct": 80, "priceK": 7},
        "row": {"patientsK": 12000, "wtpPct": 35, "priceK": 2},
    },

    # PAIN
    # source: US migraine ~40M (AMF) but branded-Rx subset ~4M (the chronic +
    # episodic-frequent population eligible for CGRP class). Triptans now
    # generic. CGRP class (Aimovig + Ajovy + Emgality + Nurtec + Ubrelvy +
    # Qulipta) ~$5-7B today, peak $12-15B with more oral entries. Prior US
    # TAM 4M x 65% WTP x $6K assumed every CGRP-eligible patient on branded
    # at uniform pricing -- ~2.5x off vs realized net economics (PBM rebates
    # 30-40% on injectable/oral CGRPs, especially after Pfizer Rimegepant
    # competition).
    "cns.pain.migraine": {
        "us":  {"patientsK": 4000,  "wtpPct": 30, "priceK": 3},
        "eu":  {"patientsK": 6000,  "wtpPct": 18, "priceK": 1.5},
        "row": {"patientsK": 50000, "wtpPct": 5,  "priceK": 0.4},
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
    # Bipolar disorder (BPD I + II): manic/hypomanic + depressive episodes.
    # ~6M US prevalence (~2.8% adult lifetime), ~10M EU, ~50M ROW. Class:
    # atypical antipsychotics (Abilify Maintena, Vraylar, Latuda, Caplyta
    # bipolar depression label 2021), lithium legacy, anticonvulsants.
    # Class peak ~$8-10B globally. source: NIMH; J&J + AbbVie + Allergan/Lundbeck 10-Ks.
    "cns.psychiatry.bipolar": {
        "us":  {"patientsK": 6000,  "wtpPct": 40, "priceK": 12},
        "eu":  {"patientsK": 10000, "wtpPct": 28, "priceK": 7},
        "row": {"patientsK": 50000, "wtpPct": 8,  "priceK": 2},
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
    # ==================== SLEEP-WAKE DISORDERS ====================
    # Sleep medicine is a distinct neurologic specialty (not psychiatry per
    # AASM + AAN), with dedicated clinics, polysomnography infrastructure,
    # and ICSD-3 classification. Patients managed by sleep specialists.

    # Narcolepsy + Idiopathic Hypersomnia: chronic excessive daytime sleepiness
    # disorders. US prevalence: narcolepsy ~165K diagnosed (~80K NT1 with
    # cataplexy + ~80K NT2); idiopathic hypersomnia ~50K -- combined ~200K
    # treated US. EU ~250K, ROW ~800K (under-diagnosed). Class:
    #   Xyrem/Xywav (Jazz, sodium oxybate ~$1.7B 2024; Xyrem authorized
    #     generic via Hikma 2023)
    #   Wakix (Harmony Bio pitolisant, ~$700M 2025)
    #   Sunosi (Axsome solriamfetol, ~$80M)
    #   Generic stimulants (modafinil/methylphenidate)
    # Next-gen orexin agonists racing: Takeda TAK-861/oveporexton (Ph3),
    # LLY/Centessa cleminorexton/ORX750 (Ph2/3, $7.8B Mar-2026 deal),
    # Alkermes ALKS 2680 (Ph2). Class peak ~$5-7B with orexins expanding TAM
    # via better cataplexy + IH coverage. Pricing $30-50K/yr branded.
    # source: Sleep Foundation 2024; Jazz/Harmony/Takeda 10-Ks.
    "cns.sleep.narcolepsy_hypersomnia": {
        "us":  {"patientsK": 200,  "wtpPct": 50, "priceK": 35},
        "eu":  {"patientsK": 250,  "wtpPct": 35, "priceK": 20},
        "row": {"patientsK": 800,  "wtpPct": 12, "priceK": 7},
    },
    # Insomnia (chronic): ~25M US adults chronic, ~10M actively Rx'd; mostly
    # generic zolpidem/eszopiclone. Branded class: dual orexin antagonists
    # (DORAs) -- Belsomra (Merck suvorexant ~$300M), Quviviq (Idorsia
    # daridorexant), Dayvigo (Eisai lemborexant). Class peak ~$2-3B.
    # source: AASM 2024; Merck/Idorsia/Eisai 10-Ks.
    "cns.sleep.insomnia": {
        "us":  {"patientsK": 10000,  "wtpPct": 35, "priceK": 0.5},
        "eu":  {"patientsK": 12000,  "wtpPct": 22, "priceK": 0.3},
        "row": {"patientsK": 80000,  "wtpPct": 8,  "priceK": 0.12},
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
    "cns.epilepsy.dee.dravet": 50,
    "cns.epilepsy.dee.syngap1": 35,
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
    "cns.neurodegeneration.post_stroke_recovery": 40,
    "cns.pain.migraine": 35,
    "cns.psychiatry.adhd": 55,
    "cns.psychiatry.anxiety": 70,
    "cns.psychiatry.asd": 10,
    "cns.psychiatry.depression": 60,
    "cns.psychiatry.bipolar": 30,
    "cns.psychiatry.opioid_dependence": 25,
    "cns.psychiatry.pain_fibromyalgia": 30,
    "cns.psychiatry.schizophrenia": 60,
    "cns.sleep.insomnia": 12,
    "cns.sleep.narcolepsy_hypersomnia": 35,
    "cns.sleep.narcolepsy": 45,
}
