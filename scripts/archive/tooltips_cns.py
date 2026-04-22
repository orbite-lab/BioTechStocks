# -*- coding: utf-8 -*-
"""
Source-cited tooltips for CNS disease areas.
All notes ASCII only, no em-dashes, no unicode, <180 chars each.
Sources: Alzheimer's Association, NAMI, MDA, Epilepsy Foundation, NINDS,
NIH registries, AHA, CDC BRFSS, WHO, ALS Association, NIDA, SAMHSA.
"""

TOOLTIPS = {
    # =========================================================================
    # EPILEPSY
    # =========================================================================
    "cns.epilepsy.dee": {
        "us.patientsK":  {"note": "Epilepsy Foundation/NINDS: ~30K US developmental and epileptic encephalopathies (LGS, Dravet, SCN2A, CDKL5)."},
        "eu.patientsK":  {"note": "Orphanet/ILAE EU: ~35K prevalent DEE across EU27+UK; LGS ~40% of treated, Dravet ~20%."},
        "row.patientsK": {"note": "WHO 2023: ~150K global DEE ex-US/EU; Japan PMDA covers Epidiolex and Fintepla for Dravet/LGS."},
        "us.wtpPct":     {"note": "~75% - Medicaid and commercial cover Epidiolex/Fintepla/Ztalmy for LGS/Dravet/CDKL5 with PA; pediatric neuro centers drive uptake."},
        "eu.wtpPct":     {"note": "~55% - EMA approved Epidiolex and Fintepla; NICE/G-BA reimburse with genetic confirmation requirements."},
        "row.wtpPct":    {"note": "~20% - Japan PMDA covered; emerging markets limited to valproate/clobazam generics."},
        "us.priceK":     {"note": "Blended $45K: Epidiolex $32K, Fintepla $96K, Ztalmy $100K, ASO pipeline $300K+; older AEDs (clobazam/valproate) $3K."},
        "eu.priceK":     {"note": "~$25K blended; EU net ~55% of US list; generic AED backbone with branded add-on."},
        "row.priceK":    {"note": "~$8K blended; Japan near EU, rest generics only."},
        "penPct":        {"note": "~40% peak - genetic diagnosis rate rising with NGS panels; ASO/gene therapy pipeline expanding addressable."}
    },
    "cns.epilepsy.focal": {
        "us.patientsK":  {"note": "NIH/CDC: ~1.2M US treated focal (partial-onset) epilepsy; ~60% of ~3.4M total epilepsy prevalence."},
        "eu.patientsK":  {"note": "ILAE EU: ~2.5M treated focal epilepsy EU27+UK; ~6M total epilepsy prevalence."},
        "row.patientsK": {"note": "WHO 2023: ~30M global epilepsy; ~18M focal; 80% treatment gap in LMICs."},
        "us.wtpPct":     {"note": "~85% - Medicare Part D and commercial cover Vimpat/Briviact/Xcopri; 30% refractory drive branded AED use."},
        "eu.wtpPct":     {"note": "~70% - EMA approved all modern AEDs; generics dominate first-line, branded for refractory."},
        "row.wtpPct":    {"note": "~35% - Japan broad coverage; emerging markets heavy generic (levetiracetam/carbamazepine)."},
        "us.priceK":     {"note": "Blended $4K: levetiracetam generic $0.5K (70% of pts), Xcopri $12K, Briviact $14K, Vimpat generic $2K."},
        "eu.priceK":     {"note": "~$2K blended; EU net ~50% of US, generic levetiracetam backbone."},
        "row.priceK":    {"note": "~$0.8K blended; mostly generics globally."},
        "penPct":        {"note": "~70% peak - large treated pool but branded share limited by generic levetiracetam first-line."}
    },
    "cns.epilepsy.generalized": {
        "us.patientsK":  {"note": "NIH/CDC: ~400K US treated generalized epilepsy (JME, absence, tonic-clonic); ~15% of total epilepsy."},
        "eu.patientsK":  {"note": "ILAE EU: ~900K treated generalized epilepsy EU27+UK."},
        "row.patientsK": {"note": "WHO 2023: ~9M global generalized epilepsy; valproate restrictions (women of childbearing age) drive switching."},
        "us.wtpPct":     {"note": "~85% - Medicare Part D and commercial broad AED coverage; valproate/lamotrigine/levetiracetam generics first-line."},
        "eu.wtpPct":     {"note": "~70% - EMA valproate restrictions 2018 shifted generalized epilepsy to lamotrigine/levetiracetam."},
        "row.wtpPct":    {"note": "~35% - Japan broad; emerging markets valproate-heavy despite teratogenicity concerns."},
        "us.priceK":     {"note": "Blended $3K: valproate/lamotrigine/levetiracetam generics $0.5K (80% of pts), Briviact $14K, newer AEDs $10K+."},
        "eu.priceK":     {"note": "~$1.5K blended; EU generic-heavy."},
        "row.priceK":    {"note": "~$0.5K blended; mostly generics."},
        "penPct":        {"note": "~65% peak - generics dominate; branded penetration limited to refractory/teratogenicity-driven switches."}
    },

    # =========================================================================
    # MOVEMENT DISORDERS
    # =========================================================================
    "cns.movement.essential_tremor": {
        "us.patientsK":  {"note": "International Essential Tremor Foundation/NINDS: ~500K US on treatment (propranolol/primidone base); ~7M US total prevalence."},
        "eu.patientsK":  {"note": "EU ET societies: ~1M treated ET EU27+UK; ~14M total prevalence."},
        "row.patientsK": {"note": "Global prevalence ~1% age 40+; ~60M worldwide, <10% treated in LMICs."},
        "us.wtpPct":     {"note": "~60% - Medicare Part D covers propranolol/primidone generics; DBS reserved for severe refractory; Jazz Suvecaltamide pipeline."},
        "eu.wtpPct":     {"note": "~45% - EU generic beta-blockers first-line; DBS via NICE/G-BA for refractory."},
        "row.wtpPct":    {"note": "~15% - Japan covered; emerging markets limited to propranolol generics."},
        "us.priceK":     {"note": "Blended $1.5K: propranolol/primidone generics $0.3K (85% of pts), DBS $75K one-time amortized, pipeline CaV3.x inhibitors $20K+."},
        "eu.priceK":     {"note": "~$0.8K blended; EU generic-dominated."},
        "row.priceK":    {"note": "~$0.3K blended; generics only."},
        "penPct":        {"note": "~25% peak - Suvecaltamide (Jazz) and other T-type Ca channel blockers expanding branded share if approved."}
    },
    "cns.movement.tardive_dyskinesia": {
        "us.patientsK":  {"note": "NAMI/APA: ~600K US TD eligible for VMAT2 inhibitors (Ingrezza, Austedo); ~20% of chronic antipsychotic users."},
        "eu.patientsK":  {"note": "EU TD prevalence: ~400K eligible; EMA approved Austedo, Ingrezza in select markets."},
        "row.patientsK": {"note": "Global: ~2M TD with growing antipsychotic use; Japan PMDA approved Ingrezza 2022."},
        "us.wtpPct":     {"note": "~65% - Medicare Part D and commercial cover Ingrezza/Austedo with PA; Medicaid variability in psych carve-outs."},
        "eu.wtpPct":     {"note": "~35% - EMA/NICE slow uptake; Austedo reimbursed Germany/France, restricted elsewhere."},
        "row.wtpPct":    {"note": "~15% - Japan covered; LMICs rely on dose adjustment of antipsychotics."},
        "us.priceK":     {"note": "Blended $70K: Ingrezza $85K, Austedo $80K, older benzodiazepines/clonazepam $0.5K (30% off-label)."},
        "eu.priceK":     {"note": "~$40K blended; EU net ~55% of US list."},
        "row.priceK":    {"note": "~$15K blended; Japan near EU, rest generics."},
        "penPct":        {"note": "~30% peak - VMAT2 branded uptake constrained by neuro/psych prescriber comfort and step edits."}
    },

    # =========================================================================
    # NEURODEGENERATION
    # =========================================================================
    "cns.neurodegeneration.alexander": {
        "us.patientsK":  {"note": "NORD/Orphanet: ~500 US ultra-rare Alexander disease (GFAP mutations); infantile/juvenile/adult forms."},
        "eu.patientsK":  {"note": "Orphanet EU: ~600 Alexander disease EU27+UK; ultra-rare designation."},
        "row.patientsK": {"note": "Global: ~3K Alexander disease; Ionis zilganersen (GFAP ASO) in Phase 3."},
        "us.wtpPct":     {"note": "~85% - ultra-rare orphan; Medicaid/commercial cover supportive care; future ASO pricing under orphan designation."},
        "eu.wtpPct":     {"note": "~70% - EMA orphan designation; national funds cover rare pediatric neuro."},
        "row.wtpPct":    {"note": "~30% - Japan covers via PMDA rare disease program; LMICs minimal access."},
        "us.priceK":     {"note": "Pipeline ASO $400K+ (Ionis zilganersen benchmark Spinraza $750K Y1); current supportive care <$10K."},
        "eu.priceK":     {"note": "~$250K expected ASO; EU net ~60% of US orphan list."},
        "row.priceK":    {"note": "~$80K; Japan near EU rare disease pricing."},
        "penPct":        {"note": "~60% peak - ultra-rare with concentrated KOL prescribing; diagnosis rate limits beyond genetic testing."}
    },
    "cns.neurodegeneration.als": {
        "us.patientsK":  {"note": "ALS Association/MDA: ~30K US prevalent ALS, ~5K new/year; median survival 3-5 years from dx."},
        "eu.patientsK":  {"note": "EU ALS registries: ~40K prevalent ALS EU27+UK; ~7K incident/year."},
        "row.patientsK": {"note": "WHO/ALS global: ~220K prevalent ALS worldwide; Japan PMDA approved Radicava and Qalsody."},
        "us.wtpPct":     {"note": "~70% - Medicare Part B Radicava IV/oral, Qalsody (tofersen) for SOD1 ~2% of ALS; riluzole generic first-line."},
        "eu.wtpPct":     {"note": "~45% - EMA approved Qalsody 2024; Radicava withdrawn EMA; riluzole generic dominant."},
        "row.wtpPct":    {"note": "~20% - Japan broad coverage; emerging markets riluzole only."},
        "us.priceK":     {"note": "Blended $40K: riluzole generic $2K (90% of pts), Radicava $170K, Qalsody $182K (SOD1 only ~2%)."},
        "eu.priceK":     {"note": "~$20K blended; Qalsody EU ~60% of US list, riluzole generic."},
        "row.priceK":    {"note": "~$5K blended; Japan near EU, rest generics."},
        "penPct":        {"note": "~25% peak - branded neuroprotection capped by modest efficacy; SOD1 ASO and C9orf72 pipeline expanding genetic subsets."}
    },
    "cns.neurodegeneration.alzheimer": {
        "us.patientsK":  {"note": "Alzheimer's Association 2024: ~6.9M Americans age 65+ with AD; ~2M early-stage eligible for anti-amyloid."},
        "eu.patientsK":  {"note": "Alzheimer Europe: ~7.8M prevalent AD EU27+UK; ~1.5M mild-to-moderate amyloid-positive per PET criteria."},
        "row.patientsK": {"note": "WHO 2023: ~39M global AD; ex-US/EU ~25M, Japan PMDA approved lecanemab (~1M Japan AD)."},
        "us.wtpPct":     {"note": "~50% - Medicare Part B covers Leqembi/Kisunla post-CMS 2024 decision with CED monitoring; PET/MRI infrastructure limits access."},
        "eu.wtpPct":     {"note": "~35% - EMA approved Leqembi July 2024 (excl APOE4 homozygotes); NICE rejected, G-BA under review."},
        "row.wtpPct":    {"note": "~8% - Japan PMDA covered; China/emerging markets minimal anti-amyloid access, donepezil generics dominate."},
        "us.priceK":     {"note": "Blended $28K: Leqembi $26.5K + Kisunla $32K + donepezil/memantine generics ($2K avg, 70% of treated pts)."},
        "eu.priceK":     {"note": "~$15K blended; EU anti-amyloid net ~55% of US list, generics widely used."},
        "row.priceK":    {"note": "~$5K blended; Japan near EU pricing, rest generics."},
        "penPct":        {"note": "~12% peak through 2030 - infusion capacity, PET access, and ARIA monitoring cap near-term reach of amyloid-targeting."}
    },
    "cns.neurodegeneration.caa": {
        "us.patientsK":  {"note": "AHA/NINDS: ~500K US CAA-related ICH risk; cerebral amyloid angiopathy underdiagnosed, MRI SWI detection growing."},
        "eu.patientsK":  {"note": "EU stroke registries: ~600K CAA at ICH risk EU27+UK; Boston criteria v2.0 improving detection."},
        "row.patientsK": {"note": "Global: ~3M at-risk CAA; overlaps AD pathology; no approved disease-modifying therapy."},
        "us.wtpPct":     {"note": "~25% - no approved CAA-specific Rx; BP control and antiplatelet management; pipeline anti-amyloid trials ongoing."},
        "eu.wtpPct":     {"note": "~15% - supportive care only; EMA no CAA-specific approvals."},
        "row.wtpPct":    {"note": "~5% - minimal access globally; awareness/MRI availability limiting factor."},
        "us.priceK":     {"note": "Current <$1K (antihypertensives generic); pipeline anti-amyloid benchmarks Leqembi $26.5K if approved for CAA."},
        "eu.priceK":     {"note": "<$0.5K current; generics only."},
        "row.priceK":    {"note": "<$0.3K; generics."},
        "penPct":        {"note": "~8% peak - no approved disease-modifying; pipeline hinges on anti-amyloid trials in CAA (Biogen, Eisai readouts)."}
    },
    "cns.neurodegeneration.dlb": {
        "us.patientsK":  {"note": "Lewy Body Dementia Association/NINDS: ~1.4M US dementia with Lewy bodies; 2nd most common neurodegenerative dementia."},
        "eu.patientsK":  {"note": "EU DLB registries: ~1.6M DLB EU27+UK; underdiagnosed vs AD."},
        "row.patientsK": {"note": "Global: ~7M DLB; no DLB-specific approved therapy; cholinesterase inhibitors used off-label."},
        "us.wtpPct":     {"note": "~55% - Medicare Part D covers donepezil/rivastigmine generics off-label; antipsychotic sensitivity limits options."},
        "eu.wtpPct":     {"note": "~40% - EU rivastigmine approved for PDD, used DLB off-label."},
        "row.wtpPct":    {"note": "~12% - Japan covered; LMICs minimal DLB-specific management."},
        "us.priceK":     {"note": "Blended $2.5K: donepezil/rivastigmine generics $1K (80% of pts), pimavanserin $30K for DLB psychosis (~10%)."},
        "eu.priceK":     {"note": "~$1K blended; EU generics dominate."},
        "row.priceK":    {"note": "~$0.5K blended; generics."},
        "penPct":        {"note": "~20% peak - off-label AD therapeutics; alpha-synuclein pipeline (Lundbeck, Roche) expanding addressable."}
    },
    "cns.neurodegeneration.parkinson_disease": {
        "us.patientsK":  {"note": "Parkinson's Foundation/NINDS: ~1M US PD (~60K new/yr); levodopa 50+ years cornerstone."},
        "eu.patientsK":  {"note": "EU PD registries: ~1.2M PD EU27+UK; ~100K incident/year."},
        "row.patientsK": {"note": "WHO 2023: ~10M global PD; Japan ~250K PD with DUOPA/Vyalev access."},
        "us.wtpPct":     {"note": "~80% - Medicare Part D broad PD coverage; Vyalev (foslevodopa), DUOPA, MAO-B inhibitors, Nourianz."},
        "eu.wtpPct":     {"note": "~65% - EU broad PD formulary; device-aided (DUOPA, DBS) per NICE/G-BA."},
        "row.wtpPct":    {"note": "~30% - Japan broad; emerging markets levodopa/carbidopa generic only."},
        "us.priceK":     {"note": "Blended $8K: levodopa/carbidopa generics $1K (70% of pts), Vyalev $95K, Nourianz $20K, DBS $75K amortized."},
        "eu.priceK":     {"note": "~$4K blended; EU device-aided per access criteria."},
        "row.priceK":    {"note": "~$1.5K blended; generics dominant."},
        "penPct":        {"note": "~50% peak - levodopa generic saturates; branded share in advanced PD (Vyalev, DUOPA) and GBA1/LRRK2 pipeline."}
    },
    "cns.neurodegeneration.ppa": {
        "us.patientsK":  {"note": "NINDS/AFTD: ~30K US primary progressive aphasia; variant of frontotemporal dementia spectrum."},
        "eu.patientsK":  {"note": "EU FTD registries: ~40K PPA EU27+UK; logopenic/nonfluent/semantic variants."},
        "row.patientsK": {"note": "Global: ~200K PPA; overlaps FTLD and AD pathology; no approved PPA-specific therapy."},
        "us.wtpPct":     {"note": "~30% - no approved PPA Rx; speech therapy and off-label AD drugs; anti-amyloid if logopenic AD-variant."},
        "eu.wtpPct":     {"note": "~20% - supportive care; EMA no PPA-specific approvals."},
        "row.wtpPct":    {"note": "~8% - minimal access; diagnosis rate low globally."},
        "us.priceK":     {"note": "Current <$3K (off-label AD generics + speech therapy); pipeline progranulin (GRN) therapies $200K+ if approved."},
        "eu.priceK":     {"note": "~$1.5K current; generics."},
        "row.priceK":    {"note": "~$0.5K; generics."},
        "penPct":        {"note": "~15% peak - genetic FTD subsets (GRN, C9orf72) drive pipeline; small addressable, high KOL concentration."}
    },
    "cns.neurodegeneration.stroke": {
        "us.patientsK":  {"note": "AHA 2024 Stats: ~800K US stroke/yr (~610K first-ever); ischemic ~87%, hemorrhagic ~13%."},
        "eu.patientsK":  {"note": "EU stroke registries: ~1.1M stroke/yr EU27+UK; thrombectomy centers expanding."},
        "row.patientsK": {"note": "WHO 2023: ~12M stroke/yr globally; leading cause of disability."},
        "us.wtpPct":     {"note": "~90% - Medicare Part A/B covers tPA, tenecteplase, thrombectomy; secondary prevention antiplatelets generic."},
        "eu.wtpPct":     {"note": "~80% - EU broad stroke care; tenecteplase increasingly replacing alteplase per ESO guidelines."},
        "row.wtpPct":    {"note": "~35% - Japan broad coverage; LMICs limited thrombectomy access."},
        "us.priceK":     {"note": "Blended $12K acute: tPA/tenecteplase $6K, thrombectomy device $25K (20% of ischemic); 2ndary prevention generics $0.5K."},
        "eu.priceK":     {"note": "~$7K blended; EU device/drug net ~60% of US."},
        "row.priceK":    {"note": "~$2K blended; Japan near EU, rest generics."},
        "penPct":        {"note": "~40% peak acute treatment - thrombectomy-eligible window (24hr) and LVO selection cap device penetration."}
    },

    # =========================================================================
    # PAIN
    # =========================================================================
    "cns.pain.migraine": {
        "us.patientsK":  {"note": "American Migraine Foundation/CDC: ~4M US on preventive therapy; ~12M total migraine sufferers (~40M ever diagnosed)."},
        "eu.patientsK":  {"note": "EU migraine registries: ~6M on preventive EU27+UK; ~70M prevalent migraine."},
        "row.patientsK": {"note": "WHO 2023: ~1B global migraine prevalence; ~50M on preventive therapy worldwide."},
        "us.wtpPct":     {"note": "~65% - Medicare Part D and commercial cover CGRP mAbs (Aimovig, Emgality, Ajovy) and gepants (Nurtec, Qulipta, Ubrelvy) with PA."},
        "eu.wtpPct":     {"note": "~45% - EMA approved all CGRPs; NICE/G-BA reimburse after 2-3 preventive failures."},
        "row.wtpPct":    {"note": "~15% - Japan covers CGRPs; emerging markets triptan/beta-blocker generics."},
        "us.priceK":     {"note": "Blended $6K preventive: CGRP mAbs $7K (50%), Qulipta/Nurtec oral $9K (20%), propranolol/topiramate generics $0.5K (30%)."},
        "eu.priceK":     {"note": "~$3K blended; EU CGRPs net ~50% of US list."},
        "row.priceK":    {"note": "~$1K blended; Japan near EU, rest generics."},
        "penPct":        {"note": "~35% peak - CGRP uptake strong but step edits and PA hurdles; acute gepant market expanding into preventive."}
    },

    # =========================================================================
    # PSYCHIATRY
    # =========================================================================
    "cns.psychiatry.adhd": {
        "us.patientsK":  {"note": "CDC BRFSS/NAMI 2023: ~6M US on ADHD treatment; ~11M prevalent (pediatric + adult)."},
        "eu.patientsK":  {"note": "EU ADHD registries: ~4M on treatment EU27+UK; lower diagnosis rates than US."},
        "row.patientsK": {"note": "Global: ~35M on ADHD treatment; Japan Vyvanse approved adults 2019."},
        "us.wtpPct":     {"note": "~75% - Medicaid/commercial broad coverage; stimulant shortages 2022-2024 impacted access; Axsome's solriamfetol (AXS-05) pipeline non-stim."},
        "eu.wtpPct":     {"note": "~55% - EMA approved stimulants, atomoxetine; stricter controls, lower pediatric diagnosis."},
        "row.wtpPct":    {"note": "~25% - Japan adult Vyvanse; LMICs limited methylphenidate access."},
        "us.priceK":     {"note": "Blended $2.5K: methylphenidate/amphetamine generics $0.8K (70%), Vyvanse generic 2023 $1.5K, Qelbree $5K, Adzenys $7K."},
        "eu.priceK":     {"note": "~$1.2K blended; EU generic-heavy."},
        "row.priceK":    {"note": "~$0.4K blended; generics."},
        "penPct":        {"note": "~55% peak - Vyvanse generic erosion 2023 compressed branded share; non-stim (Qelbree, solriamfetol) growth."}
    },
    "cns.psychiatry.anxiety": {
        "us.patientsK":  {"note": "NAMI/NIMH 2024: ~6M US GAD treated; ~19M any anxiety disorder; SSRIs/SNRIs first-line."},
        "eu.patientsK":  {"note": "EU mental health: ~8M GAD treated EU27+UK; SSRI/SNRI dominant."},
        "row.patientsK": {"note": "WHO 2023: ~300M global anxiety disorders; treatment gap >70% in LMICs."},
        "us.wtpPct":     {"note": "~75% - Medicare Part D and commercial broad SSRI/SNRI coverage; benzo tapering trends; psych carve-outs variable."},
        "eu.wtpPct":     {"note": "~65% - EU broad SSRI coverage; pregabalin approved GAD in EU (not US)."},
        "row.wtpPct":    {"note": "~25% - Japan SSRI broad; LMICs minimal access."},
        "us.priceK":     {"note": "Blended $0.8K: sertraline/escitalopram/venlafaxine generics $0.3K (90%), buspirone generic, pipeline NR-IR $5K+."},
        "eu.priceK":     {"note": "~$0.4K blended; EU generic SSRIs dominate."},
        "row.priceK":    {"note": "~$0.2K blended; generics."},
        "penPct":        {"note": "~70% peak - generics saturate; branded limited to novel MoA (orexin, psilocybin, rapid-onset) pipeline."}
    },
    "cns.psychiatry.asd": {
        "us.patientsK":  {"note": "CDC ADDM 2023: ~2M US ASD across age groups; 1 in 36 children; behavioral interventions primary."},
        "eu.patientsK":  {"note": "EU ASD registries: ~2.5M ASD EU27+UK; diagnosis rates rising."},
        "row.patientsK": {"note": "WHO 2023: ~75M global ASD prevalence; limited pharmacotherapy, ABA/behavioral primary."},
        "us.wtpPct":     {"note": "~40% - Medicaid covers risperidone/aripiprazole for ASD irritability (only FDA-approved); behavioral services coverage variable."},
        "eu.wtpPct":     {"note": "~30% - EMA limited ASD approvals; off-label atypical antipsychotics common."},
        "row.wtpPct":    {"note": "~10% - minimal ASD-specific Rx globally."},
        "us.priceK":     {"note": "Blended $3K: risperidone/aripiprazole generics $0.5K (80% of pharma-treated), ABA behavioral services $15K+ annual."},
        "eu.priceK":     {"note": "~$1.5K blended; EU generics + behavioral."},
        "row.priceK":    {"note": "~$0.5K; generics."},
        "penPct":        {"note": "~10% peak pharma - no ASD-core-symptom approved Rx; pipeline (balovaptan, bumetanide) largely failed; IRAK-M/microbiome early."}
    },
    "cns.psychiatry.depression": {
        "us.patientsK":  {"note": "NAMI/NIMH 2024: ~8M US MDD on treatment; ~21M any depressive episode; SSRIs/SNRIs first-line."},
        "eu.patientsK":  {"note": "EU depression registries: ~12M MDD on treatment EU27+UK."},
        "row.patientsK": {"note": "WHO 2023: ~280M global depression; treatment gap >60% in LMICs."},
        "us.wtpPct":     {"note": "~80% - Medicare Part D broad SSRI/SNRI; Spravato (esketamine) with REMS; Auvelity/Exxua newer branded with PA."},
        "eu.wtpPct":     {"note": "~65% - EU broad SSRI/SNRI; Spravato approved, NICE/G-BA conditional."},
        "row.wtpPct":    {"note": "~25% - Japan broad; LMICs minimal branded access."},
        "us.priceK":     {"note": "Blended $1.5K: sertraline/fluoxetine/venlafaxine generics $0.3K (85%), Auvelity $8K, Spravato $32K, Exxua $7K."},
        "eu.priceK":     {"note": "~$0.7K blended; EU generic-heavy, Spravato ~60% of US."},
        "row.priceK":    {"note": "~$0.3K; generics dominant."},
        "penPct":        {"note": "~60% peak - generics saturate; branded growth in TRD (Spravato, Auvelity) and rapid-onset pipeline (psilocybin, zuranolone)."}
    },
    "cns.psychiatry.opioid_dependence": {
        "us.patientsK":  {"note": "SAMHSA/NIDA 2024: ~2M US OUD; ~500K on MAT (buprenorphine, methadone, naltrexone)."},
        "eu.patientsK":  {"note": "EMCDDA 2024: ~1.3M EU27+UK OUD; ~700K on OAT."},
        "row.patientsK": {"note": "WHO: ~40M global OUD; treatment access highly variable."},
        "us.wtpPct":     {"note": "~70% - Medicare/Medicaid cover buprenorphine (Suboxone), Sublocade, Vivitrol; X-waiver eliminated 2023 expanding access."},
        "eu.wtpPct":     {"note": "~60% - EU methadone/buprenorphine OAT programs; Sublocade LAI expanding."},
        "row.wtpPct":    {"note": "~15% - LMICs minimal MAT access; stigma and regulation barriers."},
        "us.priceK":     {"note": "Blended $5K: buprenorphine generic (Suboxone) $2K (70%), Sublocade LAI $22K, Vivitrol $15K, methadone clinic $5K."},
        "eu.priceK":     {"note": "~$2.5K blended; EU methadone cheap, buprenorphine generic."},
        "row.priceK":    {"note": "~$0.8K; generics where available."},
        "penPct":        {"note": "~25% peak branded - generic buprenorphine dominates; LAI (Sublocade, Brixadi) growth in treatment retention."}
    },
    "cns.psychiatry.pain_fibromyalgia": {
        "us.patientsK":  {"note": "CDC/NIH: ~4M US fibromyalgia; 2-4% US adults; Lyrica/Cymbalta/Savella FDA-approved."},
        "eu.patientsK":  {"note": "EU rheum societies: ~5M fibromyalgia EU27+UK; Lyrica approved in some, not all EU markets."},
        "row.patientsK": {"note": "Global: ~80M fibromyalgia; diagnosis controversial, treatment gap large."},
        "us.wtpPct":     {"note": "~60% - Medicare Part D covers pregabalin/duloxetine generics; milnacipran branded; Journavx (suzetrigine) Jan 2025 expanding."},
        "eu.wtpPct":     {"note": "~40% - EMA did not approve Lyrica for fibro (US-only indication); duloxetine off-label."},
        "row.wtpPct":    {"note": "~15% - Japan Lyrica approved; LMICs limited access."},
        "us.priceK":     {"note": "Blended $1.5K: pregabalin/duloxetine generics $0.4K (85%), milnacipran $4K, Journavx $15K acute use."},
        "eu.priceK":     {"note": "~$0.6K blended; EU duloxetine off-label, generics dominant."},
        "row.priceK":    {"note": "~$0.3K; generics."},
        "penPct":        {"note": "~30% peak - generics dominant; Nav1.8 (Journavx) and novel analgesics limited uptake given dx controversy."}
    },
    "cns.psychiatry.schizophrenia": {
        "us.patientsK":  {"note": "NAMI/NIMH 2024: ~1.5M US treated schizophrenia; ~2.8M prevalent (~1% adults)."},
        "eu.patientsK":  {"note": "EU schizophrenia registries: ~2.5M treated EU27+UK."},
        "row.patientsK": {"note": "WHO 2023: ~24M global schizophrenia; large treatment gap in LMICs."},
        "us.wtpPct":     {"note": "~75% - Medicaid (65% of schizophrenia pts) broad atypical coverage; Cobenfy (KarXT) Sept 2024 under PA; LAIs growing."},
        "eu.wtpPct":     {"note": "~60% - EU broad atypical generic coverage; LAIs per NICE/G-BA; KarXT EMA pending."},
        "row.wtpPct":    {"note": "~25% - Japan broad; LMICs haloperidol/chlorpromazine generics."},
        "us.priceK":     {"note": "Blended $10K: atypicals generic $5K (50%), LAIs (Invega Sustenna/Trinza) $25K (25%), KarXT/emraclidine $25K (10%), Vraylar $28K (15%)."},
        "eu.priceK":     {"note": "~$5K blended; EU generics dominate, LAI ~55% of US."},
        "row.priceK":    {"note": "~$1.5K; generics."},
        "penPct":        {"note": "~60% peak - LAI penetration (~25%) growing; muscarinic agonists (Cobenfy, emraclidine) expand non-D2 addressable."}
    },

    # =========================================================================
    # SLEEP
    # =========================================================================
    "cns.sleep.narcolepsy": {
        "us.patientsK":  {"note": "Narcolepsy Network/NINDS: ~200K US narcolepsy (type 1 + type 2); Xywav/Xyrem/Wakix/Sunosi approved."},
        "eu.patientsK":  {"note": "EU narcolepsy registries: ~250K narcolepsy EU27+UK."},
        "row.patientsK": {"note": "Global: ~3M narcolepsy; orexin agonist pipeline (TAK-861, ALKS 2680) expanding."},
        "us.wtpPct":     {"note": "~80% - Medicare Part D covers Xywav/Xyrem with REMS; Wakix, Sunosi under PA; orexin agonist pipeline potentially curative for NT1."},
        "eu.wtpPct":     {"note": "~60% - EMA approved oxybates, Wakix; EU pricing lower than US."},
        "row.wtpPct":    {"note": "~20% - Japan covered; LMICs modafinil generic only."},
        "us.priceK":     {"note": "Blended $45K: Xywav $190K (30%), Xyrem generic $40K (20%), Wakix $60K (15%), Sunosi $15K (15%), modafinil generic $2K (20%)."},
        "eu.priceK":     {"note": "~$25K blended; EU oxybates ~55% of US list."},
        "row.priceK":    {"note": "~$6K; Japan near EU, rest modafinil generic."},
        "penPct":        {"note": "~45% peak - oxybate access strong; orexin agonist pipeline (TAK-861) potentially transformative for NT1 (~30% of narcolepsy)."}
    },
}
