# -*- coding: utf-8 -*-
"""
Source-cited tooltips for cardio_metabolic + endocrine disease areas.
All citations from CDC, NIH, Orphanet, WHO, SEER, FDA labels, and company 10-Ks.
ASCII only. No em-dashes (use -- instead). No unicode. <180 chars per note.
"""

TOOLTIPS = {

    # ==================== ATTR ====================
    "cardio_metabolic.attr.attr_cm": {
        "us.patientsK":  {"note": "Pfizer/BridgeBio 10-K 2024: ~120K US ATTR-CM (wild-type + hereditary), growing ~20%/yr post-tafamidis label expansion and cardiac scintigraphy awareness."},
        "eu.patientsK":  {"note": "ESC 2023 ATTR registry + Pfizer EU: ~90K diagnosed/diagnosable ATTR-CM across EU5+UK; under-diagnosed vs prevalence estimates of 300K+."},
        "row.patientsK": {"note": "Alnylam/Pfizer ROW: ~60K treatable ATTR-CM (Japan high V30M hATTR endemic pockets + AU/CA commercial markets)."},
        "us.wtpPct":     {"note": "~70% -- Medicare Part B/D covers Vyndaqel, Attruby, Amvuttra post-ATTR-ACT/HELIOS-B; commercial payors require scintigraphy confirmation."},
        "eu.wtpPct":     {"note": "~55% -- NICE/HAS reimburse tafamidis for NYHA I-II only; G-BA negotiated price cuts limiting access to severe genotypes."},
        "row.wtpPct":    {"note": "~40% -- Japan NHI covers tafamidis (V30M endemic); emerging Asia ex-Japan limited access."},
        "us.priceK":     {"note": "$250K blended: Vyndaqel $225K WAC, Attruby $244K, Amvuttra $476K (BridgeBio/Pfizer/Alnylam 10-Ks 2024)."},
        "eu.priceK":     {"note": "EU net ~$140K post HTA negotiation; UK NICE list $130K, Germany AMNOG ~$150K."},
        "row.priceK":    {"note": "$90K blended: Japan NHI tafamidis ~$120K, emerging markets tiered ~$40-60K."},
        "penPct":        {"note": "~45% peak -- diagnosis rate expansion + HELIOS-B Amvuttra label unlock drives sustained uptake through 2030."}
    },

    "cardio_metabolic.attr.attr_pn": {
        "us.patientsK":  {"note": "Alnylam 10-K 2024: ~10K US hATTR-PN (TTR mutation carriers with polyneuropathy), driven by Onpattro/Amvuttra uptake post-APOLLO."},
        "eu.patientsK":  {"note": "Orphanet/Alnylam EU: ~10K hATTR-PN across EU5 (Portugal V30M cluster, Sweden, Cyprus endemic regions)."},
        "row.patientsK": {"note": "Japan V30M endemic ~1K; Brazil/AR Portuguese-descent clusters; global ROW ~8K hATTR-PN."},
        "us.wtpPct":     {"note": "~75% -- Medicare Part B (Onpattro infusion) and Part D (Amvuttra SC) both covered post-APOLLO/HELIOS-A outcomes data."},
        "eu.wtpPct":     {"note": "~65% -- NICE/HAS reimburse patisiran/vutrisiran for Stage 1-2 hATTR-PN with polyneuropathy FAP confirmation."},
        "row.wtpPct":    {"note": "~50% -- Japan NHI covers patisiran since 2019; Brazil SUS limited access via judicial orders."},
        "us.priceK":     {"note": "Amvuttra $476K/yr WAC (Alnylam), Onpattro $450K; blended $460K reflects SC shift."},
        "eu.priceK":     {"note": "EU net ~$280K post HTA; UK NICE $250K, Germany AMNOG ~$300K."},
        "row.priceK":    {"note": "$180K blended: Japan NHI ~$250K, Brazil judicial ~$150K, tiered emerging ~$80K."},
        "penPct":        {"note": "~55% peak -- mature ASO/siRNA competition (Wainua, Amvuttra) saturates diagnosed pool."}
    },

    # ==================== DIABETES ====================
    "cardio_metabolic.diabetes.t1d": {
        "us.patientsK":  {"note": "CDC 2023 + JDRF: ~1.9M US T1D (adults + pediatric); ~200K newly diagnosed annually, auto-antibody positive."},
        "eu.patientsK":  {"note": "IDF Atlas 2023: ~1.5M EU5+UK T1D; Nordic/Finland highest incidence globally (60/100K)."},
        "row.patientsK": {"note": "IDF global: ~8M T1D ex-US/EU (India, China rising; historically under-diagnosed)."},
        "us.wtpPct":     {"note": "~85% -- Medicare, Medicaid, commercial cover insulin + CGM; Inflation Reduction Act $35/mo insulin cap."},
        "eu.wtpPct":     {"note": "~80% -- Universal coverage for insulin analogs, CGM reimbursed in UK/Germany/France for T1D."},
        "row.wtpPct":    {"note": "~40% -- Japan/AU covered; emerging markets basal-bolus access limited, CGM mostly self-pay."},
        "us.priceK":     {"note": "$5K/yr blended: insulin ($1-3K post-IRA cap), CGM Dexcom/Libre ($2-3K), pump $4-6K amortized; Lantidra cell therapy $500K one-time."},
        "eu.priceK":     {"note": "EU net ~$2.5K: insulin generics ~$500, CGM ~$1.5K reimbursed tier."},
        "row.priceK":    {"note": "$1K blended: biosimilar insulin dominant, CGM penetration growing in China/Japan."},
        "penPct":        {"note": "~12% peak -- Tzield (teplizumab) delays onset in Stage 2; Vertex VX-880 islet cell pipeline limited near-term."}
    },

    "cardio_metabolic.diabetes.t2d": {
        "us.patientsK":  {"note": "CDC National Diabetes Statistics Report 2024: ~38M US T2D diagnosed; ~25M on pharmacotherapy (metformin + GLP-1 + SGLT2 + insulin)."},
        "eu.patientsK":  {"note": "IDF Atlas 2023: ~35M EU5+UK T2D; ~22M treated with oral/injectable antihyperglycemics."},
        "row.patientsK": {"note": "IDF global: ~460M T2D ex-US/EU (China 140M, India 100M); ~150M on pharmacotherapy."},
        "us.wtpPct":     {"note": "~90% -- Medicare Part D, Medicaid, commercial cover GLP-1s (Ozempic, Mounjaro) for T2D indication; contrast with obesity exclusion."},
        "eu.wtpPct":     {"note": "~85% -- NICE/G-BA reimburse GLP-1/SGLT2 second-line post-metformin; CV outcomes (LEADER, SUSTAIN-6) drove access."},
        "row.wtpPct":    {"note": "~45% -- Japan NHI broad coverage; emerging markets metformin-dominant, GLP-1 access growing."},
        "us.priceK":     {"note": "$4K blended: metformin ($50), DPP-4 ($3K), SGLT2 Jardiance/Farxiga ($6K), GLP-1 Ozempic/Mounjaro ($10K), insulin ($2K post-cap)."},
        "eu.priceK":     {"note": "EU net ~$2K: GLP-1/SGLT2 ~$4K post-AMNOG/NICE, oral generics dominant."},
        "row.priceK":    {"note": "$600 blended: generic metformin/SU dominant, branded GLP-1 ~$3K in Japan/AU."},
        "penPct":        {"note": "~10% peak reflects incremental novel MOA (glucagon/GIP triagonists, oral GLP-1) on top of saturated standard-of-care."}
    },

    # ==================== HYPERTENSION ====================
    "cardio_metabolic.hypertension.agt_knockdown": {
        "us.patientsK":  {"note": "CDC 2024: ~120M US adults with HTN; ~10M resistant/uncontrolled on 3+ agents (Alnylam zilebesiran KARDIA target population)."},
        "eu.patientsK":  {"note": "ESC 2023: ~100M EU HTN; ~8M resistant HTN eligible for AGT siRNA or novel MOA add-on."},
        "row.patientsK": {"note": "WHO Global HTN 2023: ~1.3B HTN globally; ~60M resistant HTN ex-US/EU treated pool."},
        "us.wtpPct":     {"note": "~25% -- Medicare/commercial cover generic antihypertensives; novel siRNA (zilebesiran) will face step-edits to 3+ generics first."},
        "eu.wtpPct":     {"note": "~15% -- NICE/G-BA stringent on novel HTN pricing given abundant generics; resistant HTN niche."},
        "row.wtpPct":    {"note": "~5% -- Japan NHI conservative on novel HTN; emerging markets generic-dominant."},
        "us.priceK":     {"note": "$8K/yr anchored to Alnylam zilebesiran estimated launch (biannual SC siRNA, premium vs generics $100)."},
        "eu.priceK":     {"note": "EU net ~$4K post HTA negotiation for resistant HTN niche."},
        "row.priceK":    {"note": "$2K blended -- limited novel RNAi access ex-Japan."},
        "penPct":        {"note": "~8% peak -- resistant HTN subset realistic capture; KARDIA-3 Ph3 readout 2025 gates uptake."}
    },

    # ==================== LIPIDS ====================
    "cardio_metabolic.lipids.ldl_cv_risk": {
        "us.patientsK":  {"note": "AHA 2024 + IQVIA: ~20M US on lipid-lowering therapy (statins ~17M, PCSK9i/ezetimibe ~3M); FH ~1.3M, ASCVD high-risk ~8M."},
        "eu.patientsK":  {"note": "ESC/EAS 2023: ~25M EU on LLT; ~2M on PCSK9i (Repatha/Praluent) + inclisiran (Leqvio)."},
        "row.patientsK": {"note": "Global ROW: ~40M on LLT; Japan 8M, China rising statin + PCSK9i access."},
        "us.wtpPct":     {"note": "~70% -- Medicare Part D covers Leqvio (Part B buy-and-bill), Repatha, Praluent post-FOURIER/ODYSSEY CV outcomes."},
        "eu.wtpPct":     {"note": "~60% -- NICE/G-BA reimburse PCSK9i/inclisiran for FH and secondary prevention per LDL thresholds."},
        "row.wtpPct":    {"note": "~30% -- Japan NHI covers PCSK9i; emerging markets statin-dominant."},
        "us.priceK":     {"note": "$5K blended: statins generic ($100), ezetimibe generic ($200), Repatha/Praluent $6K, Leqvio $6.5K biannual, Nexletol $4K."},
        "eu.priceK":     {"note": "EU net ~$2.5K: PCSK9i post-AMNOG ~$3K, Leqvio ~$3.5K, statins near-zero."},
        "row.priceK":    {"note": "$800 blended: statin generics dominant, branded PCSK9i niche."},
        "penPct":        {"note": "~6% peak -- novel CETPi (obicetrapib) + ANGPTL3 (Evkeeza) layer on top of saturated statin/PCSK9i pool."}
    },

    "cardio_metabolic.lipids.lpa": {
        "us.patientsK":  {"note": "AHA Lp(a) Consensus 2024: ~64M US Lp(a) >=50 mg/dL; treated pool narrower ~100K eventual (olpasiran, pelacarsen, lepodisiran Ph3)."},
        "eu.patientsK":  {"note": "EAS 2022: ~50M EU with elevated Lp(a); ~60K treatment-eligible at launch given HTA gates."},
        "row.patientsK": {"note": "Global ~700M elevated Lp(a); Japan/AU early adopters, treatable pool ~80K."},
        "us.wtpPct":     {"note": "~40% -- Medicare/commercial will require prior ASCVD + LDL optimized; Lp(a) screening still limited to ~10% of population."},
        "eu.wtpPct":     {"note": "~25% -- NICE/G-BA will tightly gate Lp(a) siRNA/ASO to secondary prevention + Lp(a) >=70 mg/dL."},
        "row.wtpPct":    {"note": "~10% -- Japan early adoption; emerging markets limited Lp(a) testing infrastructure."},
        "us.priceK":     {"note": "$8K/yr anchored to Novartis pelacarsen / Amgen olpasiran / Lilly lepodisiran Ph3 pricing analog (similar to PCSK9i premium)."},
        "eu.priceK":     {"note": "EU net ~$4K post HTA negotiation for Lp(a)-specific therapy launch 2026-2027."},
        "row.priceK":    {"note": "$2K blended -- Japan NHI likely leads ex-US/EU adoption."},
        "penPct":        {"note": "~3% peak reflects diagnosis bottleneck + HTA gates; HORIZON / OCEAN(a) Ph3 CV outcomes 2025-2026 gate growth."}
    },

    "cardio_metabolic.lipids.triglycerides": {
        "us.patientsK":  {"note": "NIH/FCS registry: ~4K US FCS (familial chylomicronemia, LPL deficiency); ~4M sHTG (severe TG >500 mg/dL) per NHANES."},
        "eu.patientsK":  {"note": "Orphanet FCS: ~5K EU5+UK; sHTG ~3M per ESC 2023 European epi."},
        "row.patientsK": {"note": "Global FCS ~15K (Ionis/Arrowhead 10-Ks); sHTG ~20M ex-US/EU."},
        "us.wtpPct":     {"note": "~60% -- Medicare/commercial cover Waylivra (volanesorsen) + emerging plozasiran/olezarsen for FCS; sHTG access tighter."},
        "eu.wtpPct":     {"note": "~50% -- EMA approved Waylivra 2019 for FCS; NICE/G-BA gated on pancreatitis history."},
        "row.wtpPct":    {"note": "~20% -- Japan NHI FCS coverage emerging; sHTG largely statin/fibrate generics."},
        "us.priceK":     {"note": "$300K/yr anchored to Waylivra/olezarsen (Ionis) FCS pricing; sHTG launch 2025-2026 at lower price ~$15K for broader pool."},
        "eu.priceK":     {"note": "EU net ~$180K FCS post HTA; sHTG net ~$8K."},
        "row.priceK":    {"note": "$100K blended for FCS, ~$4K sHTG."},
        "penPct":        {"note": "~25% peak for FCS (small captive market); sHTG penetration capped ~2% given massive pool."}
    },

    # ==================== LIVER ====================
    "cardio_metabolic.liver.a1at": {
        "us.patientsK":  {"note": "Alpha-1 Foundation + Takeda 10-K 2024: ~100K US A1AT deficiency (PiZZ homozygotes); ~30K diagnosed, ~10K on augmentation therapy."},
        "eu.patientsK":  {"note": "Orphanet A1AT: ~125K EU PiZZ (Scandinavia highest); ~20K on Prolastin/Zemaira/Glassia augmentation."},
        "row.patientsK": {"note": "Global PiZZ ~1M prevalence; treated pool ex-US/EU ~8K (augmentation access limited)."},
        "us.wtpPct":     {"note": "~70% -- Medicare Part B covers IV augmentation; commercial reimburses per FDA label for moderate-severe emphysema."},
        "eu.wtpPct":     {"note": "~55% -- Augmentation reimbursed in Germany/France; NICE rejected on cost-effectiveness."},
        "row.wtpPct":    {"note": "~30% -- Japan/AU limited; emerging markets minimal augmentation access."},
        "us.priceK":     {"note": "$150K/yr blended: Prolastin-C, Zemaira, Glassia IV augmentation WAC; novel siRNA (fazirsiran, Arrowhead/Takeda) Ph3 pricing TBD."},
        "eu.priceK":     {"note": "EU net ~$90K: augmentation post tender pricing Germany ~$100K."},
        "row.priceK":    {"note": "$50K blended -- limited augmentation access outside Japan."},
        "penPct":        {"note": "~15% peak -- fazirsiran liver-directed siRNA (Ph3 readout 2025) expands addressable beyond lung augmentation."}
    },

    "cardio_metabolic.liver.hbv_functional_cure": {
        "us.patientsK":  {"note": "CDC 2023 + WHO: ~2.4M US chronic HBV (HBsAg+); ~800K on tenofovir/entecavir NUCs, functional cure candidates ~500K."},
        "eu.patientsK":  {"note": "ECDC 2023: ~4.7M EU chronic HBV; ~1.5M on NUCs eligible for siRNA/pegIFN combination functional cure regimens."},
        "row.patientsK": {"note": "WHO global: ~296M chronic HBV (Asia-Pac dominant); China 75M, Africa 80M; treatable pool ~50M."},
        "us.wtpPct":     {"note": "~60% -- Medicare/commercial cover NUCs; functional cure regimens (GSK bepirovirsen, VIR-2218) will require strict HBsAg/DNA gates."},
        "eu.wtpPct":     {"note": "~50% -- EASL guidelines + G-BA/NICE reimburse NUCs; cure combos gated on Ph3 outcomes 2026+."},
        "row.wtpPct":    {"note": "~15% -- China NRDL generic NUCs dominant; novel functional cure access limited near-term."},
        "us.priceK":     {"note": "$15K/yr blended anchored to NUC generics ($200) + emerging cure regimens Ph3 (GSK bepirovirsen ASO, Arbutus siRNA pricing TBD $40-60K)."},
        "eu.priceK":     {"note": "EU net ~$8K: NUC generics dominant, functional cure launch 2027+ at ~$30K."},
        "row.priceK":    {"note": "$300 blended -- generic NUC-dominant globally."},
        "penPct":        {"note": "~4% peak -- functional cure Ph3 gated 2026-2027; NUCs mature + generic."}
    },

    "cardio_metabolic.liver.mash": {
        "us.patientsK":  {"note": "Madrigal 10-K 2024 + AASLD: ~14M US MASH (F2-F3 fibrosis); ~6M biopsy-confirmed/FibroScan-qualified treatment-eligible."},
        "eu.patientsK":  {"note": "EASL 2023: ~10M EU MASH F2-F3; ~4M eligible post Rezdiffra/Wegovy MASH label expansion."},
        "row.patientsK": {"note": "Global MASH ~115M F2-F3; treated pool ex-US/EU ~15M (Japan NHI early mover, China growing)."},
        "us.wtpPct":     {"note": "~45% -- Medicare/commercial cover Rezdiffra (resmetirom, Madrigal) post-MAESTRO-NASH; prior-auth requires F2-F3 confirmation."},
        "eu.wtpPct":     {"note": "~30% -- EMA approved resmetirom 2024; HTA negotiation ongoing G-BA/NICE through 2025."},
        "row.wtpPct":    {"note": "~10% -- Japan PMDA approved 2024; emerging MASH access minimal near-term."},
        "us.priceK":     {"note": "$47K/yr anchored to Madrigal Rezdiffra WAC 2024; GLP-1 adjacent (Wegovy MASH-expanded) ~$16K."},
        "eu.priceK":     {"note": "EU net ~$25K Rezdiffra post AMNOG/NICE; GLP-1 ~$8K."},
        "row.priceK":    {"note": "$12K blended -- Japan NHI Rezdiffra ~$20K, emerging tiered."},
        "penPct":        {"note": "~8% peak -- capacity + diagnosis bottleneck (FibroScan access) limits uptake despite large pool."}
    },

    "cardio_metabolic.liver.pld_adpkd": {
        "us.patientsK":  {"note": "Otsuka Jynarque 10-K + NIH: ~140K US ADPKD; ~20K PLD (polycystic liver disease) with significant hepatomegaly treatment-eligible."},
        "eu.patientsK":  {"note": "Orphanet ADPKD: ~160K EU; PLD treatable ~25K per ERA-EDTA registry."},
        "row.patientsK": {"note": "Global ADPKD ~12M prevalence; treatable pool ROW ~30K PLD."},
        "us.wtpPct":     {"note": "~65% -- Medicare/commercial cover Jynarque (tolvaptan) for ADPKD progression; PLD novel agents (somatostatin analogs) step-edited."},
        "eu.wtpPct":     {"note": "~55% -- NICE/G-BA reimburse tolvaptan for rapid progression ADPKD Mayo Class 1C-1E."},
        "row.wtpPct":    {"note": "~25% -- Japan NHI covers tolvaptan; emerging markets octreotide/lanreotide off-label."},
        "us.priceK":     {"note": "$13K/yr anchored to Otsuka Jynarque WAC + octreotide/lanreotide (~$20K) for PLD off-label."},
        "eu.priceK":     {"note": "EU net ~$7K post HTA negotiation; Jynarque ~$8K, somatostatin ~$12K."},
        "row.priceK":    {"note": "$4K blended -- Japan tolvaptan reimbursed, emerging generic/biosimilar."},
        "penPct":        {"note": "~15% peak -- PLD-specific pipeline limited; tolvaptan mature for ADPKD."}
    },

    # ==================== OBESITY ====================
    "cardio_metabolic.obesity.general": {
        "us.patientsK":  {"note": "CDC NHANES 2023: 42% US adults BMI>=30 = ~110M; ~40M eligible for anti-obesity medications (AOMs) post-insurance criteria."},
        "eu.patientsK":  {"note": "WHO Europe 2023: ~150M obese in EU+UK; ~30M eligible for AOMs given stricter HTA BMI/comorbidity gates."},
        "row.patientsK": {"note": "Global ex-US/EU ~450M obese; ~50M eligible (China, Japan, AU have growing GLP-1 reimbursement)."},
        "us.wtpPct":     {"note": "~50% -- Medicare excludes weight-loss indication (Part D statute); commercial coverage expanding post-SELECT CV outcomes."},
        "eu.wtpPct":     {"note": "~35% -- NICE/G-BA limited to BMI>=35 + comorbidities; most purchase out-of-pocket."},
        "row.wtpPct":    {"note": "~8% -- Japan PMDA approved, Medicare-equivalent coverage; emerging markets mostly self-pay."},
        "us.priceK":     {"note": "$15K/yr avg across Mounjaro ($13K), Zepbound ($12K), Wegovy ($16K), Saxenda ($15K); oral GLP-1 pending."},
        "eu.priceK":     {"note": "EU net ~$8K; post-G-BA negotiation Zepbound/Wegovy in UK, Germany ~50% of US list."},
        "row.priceK":    {"note": "$3K blended; Japan PMDA pricing ~$9K, emerging markets ~$1-2K via rebates/tiered pricing."},
        "penPct":        {"note": "~5% peak reflects capacity-constrained launch curve; supply expansion through 2028 unlocks more."}
    },

    "cardio_metabolic.obesity.rare_genetic.hypothalamic_obesity": {
        "us.patientsK":  {"note": "Rhythm Pharma 10-K 2024: ~10K US acquired hypothalamic obesity (craniopharyngioma resection, hypothalamic tumor, TBI); TRANSCEND Ph3 target."},
        "eu.patientsK":  {"note": "Orphanet acquired HO: ~8K EU post-craniopharyngioma/tumor/surgery; pediatric-dominant."},
        "row.patientsK": {"note": "Global HO ~20K; ex-US/EU treatable ~15K (Japan, AU registry-tracked)."},
        "us.wtpPct":     {"note": "~70% -- orphan indication + clear biomarker (hypothalamic damage); Medicare/commercial support Imcivree label expansion."},
        "eu.wtpPct":     {"note": "~55% -- EMA HO review pending; NICE/G-BA orphan pathway likely."},
        "row.wtpPct":    {"note": "~30% -- Japan PMDA emerging orphan obesity pathway."},
        "us.priceK":     {"note": "$325K/yr anchored to Rhythm Imcivree (setmelanotide) WAC 2024 orphan pricing; TRANSCEND Ph3 readout 2024+ supports label."},
        "eu.priceK":     {"note": "EU net ~$200K post HTA orphan rare obesity pricing."},
        "row.priceK":    {"note": "$120K blended -- Japan NHI orphan pathway."},
        "penPct":        {"note": "~30% peak -- orphan captive market, pediatric dosing growth potential."}
    },

    "cardio_metabolic.obesity.rare_genetic.monogenic_mc4r": {
        "us.patientsK":  {"note": "Rhythm Pharma 10-K: ~4.3K US Imcivree-addressable (BBS ~2K + POMC/LEPR/PCSK1 ~500 + SRC1/SH2B1/Alstrom ~1.8K) per MC4R pathway genetic confirmation."},
        "eu.patientsK":  {"note": "Orphanet MC4R pathway: ~4K EU (BBS Ciliopathies European registry + POMC/LEPR carriers)."},
        "row.patientsK": {"note": "Global MC4R pathway ~8K diagnosable ex-US/EU; under-diagnosed without genetic testing infrastructure."},
        "us.wtpPct":     {"note": "~80% -- orphan rare genetic obesity; Medicare/commercial cover Imcivree post-genetic confirmation (Invitae panel)."},
        "eu.wtpPct":     {"note": "~65% -- EMA approved 2021 for BBS, POMC, LEPR, PCSK1; HAS/G-BA orphan reimbursed."},
        "row.wtpPct":    {"note": "~35% -- Japan orphan drug pathway; emerging markets genetic testing bottleneck."},
        "us.priceK":     {"note": "$325K/yr anchored to Rhythm Imcivree setmelanotide WAC; MC4R agonist orphan pricing tier."},
        "eu.priceK":     {"note": "EU net ~$200K post HTA orphan pathway."},
        "row.priceK":    {"note": "$120K blended -- Japan NHI orphan reimbursed."},
        "penPct":        {"note": "~35% peak -- small captive market, genetic testing expansion drives diagnosis rate."}
    },

    "cardio_metabolic.obesity.rare_genetic.prader_willi": {
        "us.patientsK":  {"note": "FPWR + PWSA 2024: ~15K US genetically confirmed Prader-Willi Syndrome (SNRPN/SNORD116 deletion or maternal UPD 15q11-q13)."},
        "eu.patientsK":  {"note": "Orphanet PWS: ~15K EU confirmed; registry-tracked via EPWGC."},
        "row.patientsK": {"note": "Global PWS ~30K confirmed; Japan/AU registries + emerging markets under-diagnosed."},
        "us.wtpPct":     {"note": "~75% -- orphan; Soleno DCCR (diazoxide) approved Mar 2025; Medicare/commercial reimburse + somatropin legacy coverage."},
        "eu.wtpPct":     {"note": "~60% -- EMA pathway for DCCR pending; somatropin reimbursed in EU5."},
        "row.wtpPct":    {"note": "~30% -- Japan PMDA somatropin reimbursed; DCCR global rollout 2025+."},
        "us.priceK":     {"note": "$300K/yr blended: Soleno DCCR (diazoxide choline) WAC 2025 + somatropin legacy ($30K) for short stature in PWS."},
        "eu.priceK":     {"note": "EU net ~$180K: DCCR HTA pending, somatropin ~$20K."},
        "row.priceK":    {"note": "$80K blended -- Japan NHI somatropin, DCCR emerging."},
        "penPct":        {"note": "~40% peak -- DCCR hyperphagia-specific targets core symptom, captive orphan pool."}
    },

    # ==================== RARE METABOLIC ====================
    "cardio_metabolic.rare_metabolic.homocystinuria": {
        "us.patientsK":  {"note": "Travere/Orphanet CBS deficiency homocystinuria: ~1.5K US classical homocystinuria (CBS-deficient); ~500 B6-non-responsive pegtibatinase candidates."},
        "eu.patientsK":  {"note": "Orphanet EU: ~2K classical homocystinuria (Ireland/Qatar highest incidence via newborn screen)."},
        "row.patientsK": {"note": "Global homocystinuria ~50K prevalence; ROW treatable ~3K diagnosed."},
        "us.wtpPct":     {"note": "~70% -- orphan ultra-rare; Medicare/Medicaid cover betaine (Cystadane) + emerging pegtibatinase (Travere Ph3)."},
        "eu.wtpPct":     {"note": "~55% -- EMA orphan Cystadane; pegtibatinase HTA 2026+."},
        "row.wtpPct":    {"note": "~25% -- Japan NHI orphan pathway."},
        "us.priceK":     {"note": "$400K/yr anchored to Travere pegtibatinase Ph3 pricing analog (ultra-orphan enzyme therapy); Cystadane ($50K) legacy."},
        "eu.priceK":     {"note": "EU net ~$250K post ultra-orphan HTA negotiation."},
        "row.priceK":    {"note": "$120K blended -- Japan orphan pathway."},
        "penPct":        {"note": "~30% peak -- captive ultra-orphan pool, B6-non-responsive subset."}
    },

    "cardio_metabolic.rare_metabolic.hyperoxaluria": {
        "us.patientsK":  {"note": "Alnylam Oxlumo 10-K + OHF: ~0.4K US PH1 (primary hyperoxaluria type 1, AGXT mutation); ~5K enteric hyperoxaluria secondary."},
        "eu.patientsK":  {"note": "Orphanet PH1: ~0.5K EU AGXT-confirmed; ERKNet registry-tracked."},
        "row.patientsK": {"note": "Global PH1 ~5K prevalence; treatable ex-US/EU ~1K."},
        "us.wtpPct":     {"note": "~80% -- ultra-orphan kidney stone disease; Medicare/commercial cover Oxlumo (lumasiran) post ILLUMINATE-A Ph3."},
        "eu.wtpPct":     {"note": "~65% -- EMA approved Oxlumo 2020; G-BA/HAS orphan reimbursed."},
        "row.wtpPct":    {"note": "~35% -- Japan PMDA orphan pathway."},
        "us.priceK":     {"note": "$495K/yr anchored to Alnylam Oxlumo (lumasiran) WAC 2024; nedosiran (Novo/Dicerna) similar tier."},
        "eu.priceK":     {"note": "EU net ~$300K post HTA negotiation."},
        "row.priceK":    {"note": "$180K blended -- Japan NHI orphan pathway."},
        "penPct":        {"note": "~50% peak -- ultra-orphan captive pool + prophylaxis prevents ESRD progression."}
    },

    "cardio_metabolic.rare_metabolic.porphyria": {
        "us.patientsK":  {"note": "Alnylam Givlaari + APF 2024: ~3K US acute hepatic porphyria (AHP: AIP, VP, HCP, ADP); ~1K symptomatic with recurrent attacks."},
        "eu.patientsK":  {"note": "Orphanet AHP: ~4K EU (Sweden/Finland AIP clusters, South Africa VP)."},
        "row.patientsK": {"note": "Global AHP ~20K prevalence; treatable ROW ~2K symptomatic."},
        "us.wtpPct":     {"note": "~75% -- ultra-orphan; Medicare/commercial cover Givlaari (givosiran) post ENVISION Ph3."},
        "eu.wtpPct":     {"note": "~60% -- EMA approved Givlaari 2020; G-BA/HAS orphan reimbursed."},
        "row.wtpPct":    {"note": "~30% -- Japan PMDA orphan pathway."},
        "us.priceK":     {"note": "$575K/yr anchored to Alnylam Givlaari (givosiran) WAC 2024 ultra-orphan RNAi pricing."},
        "eu.priceK":     {"note": "EU net ~$350K post HTA negotiation."},
        "row.priceK":    {"note": "$200K blended -- Japan NHI orphan pathway."},
        "penPct":        {"note": "~40% peak -- captive recurrent-attack subset within AHP diagnosed pool."}
    },

    # ==================== THROMBOSIS ====================
    "cardio_metabolic.thrombosis.anticoagulation": {
        "us.patientsK":  {"note": "CDC 2023 + DOAC analytics: ~8M US on anticoagulation (AFib ~6M, VTE ~1.5M, mechanical valves ~0.5M); dominated by Eliquis/Xarelto DOACs."},
        "eu.patientsK":  {"note": "ESC 2023: ~7M EU on anticoagulation; DOAC penetration ~70% post-ARISTOTLE/ROCKET-AF."},
        "row.patientsK": {"note": "Global anticoagulation pool ~40M; Japan NHI DOAC-dominant, China warfarin-transitioning."},
        "us.wtpPct":     {"note": "~85% -- Medicare/commercial cover Eliquis/Xarelto/Pradaxa; IRA negotiation Eliquis 2026 pricing."},
        "eu.wtpPct":     {"note": "~75% -- NICE/G-BA reimburse DOACs first-line for AFib/VTE; warfarin legacy."},
        "row.wtpPct":    {"note": "~40% -- Japan NHI DOAC covered; emerging markets warfarin-dominant."},
        "us.priceK":     {"note": "$5K/yr blended: Eliquis ($6K WAC pre-IRA), Xarelto ($6K), Pradaxa ($5K), warfarin generic ($100); factor XI (abelacimab Ph3) pending."},
        "eu.priceK":     {"note": "EU net ~$2.5K post AMNOG DOAC; warfarin near-zero."},
        "row.priceK":    {"note": "$800 blended: warfarin generics dominant, Japan DOAC branded."},
        "penPct":        {"note": "~4% peak -- factor XI inhibitors (abelacimab, asundexian) incremental to saturated DOAC pool."}
    },

    # ==================== ENDOCRINE: ADRENAL ====================
    "endocrine.adrenal.cah": {
        "us.patientsK":  {"note": "Neurocrine Crenessity 10-K 2025 + CARES Foundation: ~20K US classical CAH (21-hydroxylase deficiency); ~15K treatment-eligible adults/peds."},
        "eu.patientsK":  {"note": "Orphanet CAH: ~25K EU classical CAH; newborn screen confirmed 1:15K births."},
        "row.patientsK": {"note": "Global CAH ~75K prevalence; treatable ROW ~40K (Japan, AU NBS programs)."},
        "us.wtpPct":     {"note": "~75% -- Neurocrine Crenessity (crinecerfont) FDA approved Dec 2024; Medicare/commercial cover + legacy glucocorticoids."},
        "eu.wtpPct":     {"note": "~60% -- EMA crinecerfont approved 2025; HTA negotiation ongoing; Spruce CAH pipeline."},
        "row.wtpPct":    {"note": "~30% -- Japan PMDA review; generic hydrocortisone globally dominant."},
        "us.priceK":     {"note": "$160K/yr anchored to Neurocrine Crenessity (crinecerfont) WAC 2025 + legacy hydrocortisone ($2K)."},
        "eu.priceK":     {"note": "EU net ~$90K post HTA negotiation."},
        "row.priceK":    {"note": "$40K blended -- Japan NHI orphan pathway."},
        "penPct":        {"note": "~35% peak -- crinecerfont steroid-sparing, captive orphan pool."}
    },

    # ==================== ENDOCRINE: CALCIUM ====================
    "endocrine.calcium.adh1": {
        "us.patientsK":  {"note": "Calcilytix/BridgeBio + NIH: ~10K US ADH1 (autosomal dominant hypocalcemia type 1, CaSR gain-of-function); encaleret Ph3 target."},
        "eu.patientsK":  {"note": "Orphanet ADH1: ~12K EU; under-diagnosed vs hypoparathyroidism broader pool."},
        "row.patientsK": {"note": "Global ADH1 ~50K prevalence; treatable ROW ~15K diagnosed."},
        "us.wtpPct":     {"note": "~70% -- orphan; Medicare/commercial will cover encaleret (BridgeBio Ph3) post-readout; Natpara legacy for hypoPT."},
        "eu.wtpPct":     {"note": "~55% -- EMA orphan pathway; Yorvipath (palopegteriparatide) Ascendis approved 2024."},
        "row.wtpPct":    {"note": "~25% -- Japan PMDA orphan pathway."},
        "us.priceK":     {"note": "$250K/yr anchored to Ascendis Yorvipath (palopegteriparatide) WAC 2024 + BridgeBio encaleret Ph3 analog."},
        "eu.priceK":     {"note": "EU net ~$150K post HTA orphan negotiation."},
        "row.priceK":    {"note": "$80K blended -- Japan NHI orphan pathway."},
        "penPct":        {"note": "~25% peak -- orphan captive ADH1 subset within broader hypoPT pool."}
    },

    # ==================== ENDOCRINE: PITUITARY ====================
    "endocrine.pituitary.acromegaly": {
        "us.patientsK":  {"note": "Ipsen/Crinetics 10-Ks + Acromegaly Community: ~25K US acromegaly prevalence; ~8K on somatostatin analogs (Sandostatin, Somatuline, Mycapssa)."},
        "eu.patientsK":  {"note": "Orphanet acromegaly: ~30K EU; ESE registry; ~10K treated with SSA/pegvisomant."},
        "row.patientsK": {"note": "Global acromegaly ~90K prevalence; treatable ex-US/EU ~15K (Japan/AU registries)."},
        "us.wtpPct":     {"note": "~75% -- Medicare/commercial cover Sandostatin LAR, Somatuline Depot, Mycapssa oral, pegvisomant (Somavert); Crinetics paltusotine Ph3."},
        "eu.wtpPct":     {"note": "~65% -- NICE/G-BA reimburse SSAs + pegvisomant second-line; oral Mycapssa growing."},
        "row.wtpPct":    {"note": "~35% -- Japan NHI SSA/pegvisomant covered."},
        "us.priceK":     {"note": "$80K/yr blended: Sandostatin LAR ($45K), Somatuline Depot ($55K), Mycapssa oral ($70K), Somavert ($120K); paltusotine (Crinetics) Ph3 pricing TBD."},
        "eu.priceK":     {"note": "EU net ~$45K post AMNOG/NICE SSA pricing."},
        "row.priceK":    {"note": "$20K blended -- Japan NHI branded, emerging octreotide generic."},
        "penPct":        {"note": "~20% peak -- oral paltusotine (Crinetics Ph3) + Mycapssa shift drives SSA switch pool expansion."}
    },

    # ==================== ENDOCRINE: THYROID ====================
    "endocrine.thyroid.graves": {
        "us.patientsK":  {"note": "ATA 2024 + Amgen Tepezza context: ~1.2M US Graves disease; ~100K Thyroid Eye Disease (TED) moderate-severe subset (Tepezza-addressable)."},
        "eu.patientsK":  {"note": "Orphanet/EUGOGO: ~1M EU Graves; ~80K TED moderate-severe eligible for teprotumumab."},
        "row.patientsK": {"note": "Global Graves ~50M prevalence; treatable pool ROW ~150K TED."},
        "us.wtpPct":     {"note": "~70% -- Medicare/commercial cover Tepezza (teprotumumab) for TED post OPTIC Ph3; methimazole/PTU generic for Graves hyperthyroidism."},
        "eu.wtpPct":     {"note": "~50% -- EMA approved Tepezza 2025; HTA negotiation G-BA/NICE ongoing."},
        "row.wtpPct":    {"note": "~20% -- Japan PMDA Tepezza review; emerging methimazole generic-dominant."},
        "us.priceK":     {"note": "$350K/course anchored to Amgen/Horizon Tepezza (teprotumumab) 8-infusion course WAC 2024; methimazole generic ($200)."},
        "eu.priceK":     {"note": "EU net ~$200K/course Tepezza post HTA; methimazole near-zero."},
        "row.priceK":    {"note": "$100K/course blended -- Japan PMDA pricing emerging."},
        "penPct":        {"note": "~15% peak -- TED moderate-severe captive subset; Viridian VRDN-001/003 Ph3 competition 2025+."}
    },

}
