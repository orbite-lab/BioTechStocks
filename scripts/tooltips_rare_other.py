# -*- coding: utf-8 -*-
"""
Source-cited tooltips for rare/other therapeutic areas:
- Musculoskeletal (bone/cartilage + neuromuscular)
- Infectious disease (anti-infective + vaccines)
- Ophthalmology (anterior/neuro + retina + optic nerve)
- Respiratory (inflammatory)

Citations: MDA, PPMD, TREAT-NMD, NORD, Orphanet, MDF, FSHD Society, LPA, MAGIC,
NIH/NIAMS, CDC, WHO, ECDC, AAO, NEI, BrightFocus, Prevent Blindness, GINA, GOLD,
AAAAI, ATS, Cure DEB/DEBRA.
"""

TOOLTIPS = {
    # =====================================================================
    # MUSCULOSKELETAL - BONE & CARTILAGE
    # =====================================================================
    "musculoskeletal.bone_cartilage.achondroplasia": {
        "us.patientsK":  {"note": "LPA + MAGIC Foundation: ~10K US achondroplasia (~1:25K births); pediatric growing pool ~3-4K eligible for CNP analogs."},
        "eu.patientsK":  {"note": "Orphanet EU-5: ~12K achondroplasia; pediatric eligible (<18yr, open growth plates) ~4K for Voxzogo."},
        "row.patientsK": {"note": "Global ~250K achondroplasia; ex-US/EU ~8K diagnosed & accessible (Japan PMDA approved, BMS ex-US partner)."},
        "us.wtpPct":     {"note": "~70% -- BioMarin Voxzogo strong pediatric uptake; payors cover for open growth plates; parental advocacy high (LPA)."},
        "eu.wtpPct":     {"note": "~55% -- EMA approved 2021; NICE/G-BA reimbursed with age restrictions; annual HTA reviews for pricing."},
        "row.wtpPct":    {"note": "~25% -- Japan reimbursed; LatAm/APAC slower access; out-of-pocket barriers in non-OECD markets."},
        "us.priceK":     {"note": "Voxzogo ~$320K/yr WAC (weight-based daily SC); duration ~5-8yr until growth plate closure."},
        "eu.priceK":     {"note": "EU ~$210K/yr post-HTA (~30-35% discount vs US); duration similar 5-8yr pediatric dosing."},
        "row.priceK":    {"note": "$150K/yr blended; Japan ~$260K, emerging markets tiered pricing $50-100K."},
        "penPct":        {"note": "~40% peak -- pediatric-only eligibility + 5-8yr duration limits ceiling; adult indication in trials could expand."}
    },
    "musculoskeletal.bone_cartilage.osteoporosis": {
        "us.patientsK": {"note": "NIH/NIAMS: ~10M US osteoporosis (women >50 dominant); ~2M treated with Rx (Prolia, Evenity, bisphosphonates)."},
        "eu.patientsK": {"note": "IOF EU-5: ~22M osteoporosis; ~4M on Rx therapy; Evenity/Prolia reimbursed post-fracture or high FRAX score."},
        "row.patientsK":{"note": "Global >200M osteoporosis (WHO); ~15M ex-US/EU on Rx -- Japan/China large aging pools, LatAm underdiagnosed."},
        "us.wtpPct":    {"note": "~35% -- crowded class (Prolia, Evenity, Forteo, generics); Medicare Part D + Part B biologics coverage strong."},
        "eu.wtpPct":    {"note": "~28% -- HTA strict on incremental benefit vs generic bisphosphonates; Evenity restricted to high-risk post-menopausal."},
        "row.wtpPct":   {"note": "~15% -- Japan high use of denosumab/teriparatide; China/India rely on oral bisphosphonates; vertebral fracture triggers."},
        "us.priceK":    {"note": "Evenity ~$25K/yr (12 mo course); Prolia ~$3K/yr; Forteo ~$40K/yr (2yr max); oral generics <$0.5K/yr."},
        "eu.priceK":    {"note": "Evenity ~$16K course; Prolia ~$2K/yr post-HTA; generic alendronate dominates >70% Rx volume."},
        "row.priceK":   {"note": "Blended ~$1.5K/yr -- Japan/Korea $5-10K biologic, emerging markets <$0.3K oral bisphosphonates."},
        "penPct":       {"note": "~25% peak for branded anabolic/biologic within treated pool; generics cap premium share."}
    },

    # =====================================================================
    # MUSCULOSKELETAL - NEUROMUSCULAR
    # =====================================================================
    "musculoskeletal.neuromuscular.cms": {
        "us.patientsK": {"note": "NORD/MDA: ~3K US congenital myasthenic syndrome (~1:100K); genetic dx (CHRNE, DOK7, RAPSN most common)."},
        "eu.patientsK": {"note": "Orphanet: ~4K EU-5 CMS; TREAT-NMD registry growing; salbutamol/pyridostigmine symptom mgmt standard."},
        "row.patientsK":{"note": "Global ~50K CMS; ex-US/EU ~3K diagnosed -- underdx in most markets absent genetic testing."},
        "us.wtpPct":    {"note": "~55% -- ultra-rare; pyridostigmine/albuterol off-label free; novel therapy WTP high given unmet need."},
        "eu.wtpPct":    {"note": "~40% -- orphan pathway, HTA challenging for ultra-rare; named-patient access common."},
        "row.wtpPct":   {"note": "~15% -- diagnosis gap limits access; Japan/select APAC via orphan import programs."},
        "us.priceK":    {"note": "Novel CMS therapy (e.g., DYN-101) modeled ~$400K/yr -- ultra-rare orphan premium pricing."},
        "eu.priceK":    {"note": "~$280K/yr post-HTA (~30% discount); managed access agreements likely for ultra-rare."},
        "row.priceK":   {"note": "~$150K/yr blended; Japan orphan drug premium, LatAm/APAC limited."},
        "penPct":       {"note": "~20% peak -- genetic subtype specificity (subtype-matched Rx) narrows addressable slice."}
    },
    "musculoskeletal.neuromuscular.dm1": {
        "us.patientsK": {"note": "Myotonic Dystrophy Foundation: ~15K US DM1 diagnosed (~1:8K prevalence, many undiagnosed); adult-onset dominant."},
        "eu.patientsK": {"note": "Orphanet EU-5: ~20K DM1 diagnosed; TREAT-NMD registry; no approved disease-modifying Rx, symptom mgmt only."},
        "row.patientsK":{"note": "Global ~600K DM1 (~1:8K); ex-US/EU ~15K on clinical/specialty care; Japan Kii peninsula cluster."},
        "us.wtpPct":    {"note": "~60% -- zero approved DMT; MDF patient community trial-ready; Dyne/Avidity/PepGen late-stage."},
        "eu.wtpPct":    {"note": "~40% -- EMA orphan designation; HTA will scrutinize functional endpoints (vHOT, MIRS)."},
        "row.wtpPct":   {"note": "~15% -- Japan high DM1 awareness via registries; rest of ROW limited specialty access."},
        "us.priceK":    {"note": "DM1 DMT modeled ~$450K/yr (antisense/siRNA); orphan premium + chronic dosing."},
        "eu.priceK":    {"note": "~$300K/yr post-HTA; outcomes-based agreements likely given functional endpoint uncertainty."},
        "row.priceK":   {"note": "~$150K/yr blended; Japan ~$350K, emerging markets tiered."},
        "penPct":       {"note": "~25% peak -- multisystem disease complicates eligibility; cardiac/pulmonary exclusions likely in label."}
    },
    "musculoskeletal.neuromuscular.dmd.exon45": {
        "us.patientsK": {"note": "PPMD/MDA: ~12K US DMD; exon 45-skip amenable ~9% = ~1.4K addressable (UCL Leiden open mutation db)."},
        "eu.patientsK": {"note": "TREAT-NMD: ~15K EU-5 DMD; ~9% exon 45-amenable = ~1.4K; Vyondys/Viltepso EU filings pending."},
        "row.patientsK":{"note": "Global ~300K DMD; ex-US/EU exon 45 amenable ~3K accessible; Japan PMDA approved Viltolarsen."},
        "us.wtpPct":    {"note": "~50% -- Sarepta Casimersen (Amondys 45) approved 2021; PA + dystrophin confirmation required."},
        "eu.wtpPct":    {"note": "~25% -- EMA declined exon-skippers (low dystrophin uplift); named-patient/compassionate only."},
        "row.wtpPct":   {"note": "~15% -- Japan approved, rest of ROW limited access; IV weekly infusion logistics."},
        "us.priceK":    {"note": "Amondys 45 ~$750K/yr WAC (weight-based IV weekly); chronic dosing, duration 5-10yr pre-gene-tx."},
        "eu.priceK":    {"note": "Limited reimbursement; named-patient ~$500K/yr where available."},
        "row.priceK":   {"note": "~$400K/yr blended; Japan Viltepso ~$600K, emerging markets rare access."},
        "penPct":       {"note": "~35% peak -- displaced by gene therapy (Elevidys) in amenable/eligible patients over time."}
    },
    "musculoskeletal.neuromuscular.dmd.exon51": {
        "us.patientsK": {"note": "PPMD/MDA: ~12K US DMD; exon 51-skip amenable ~13% = ~2K addressable (most common DMD mutation cluster)."},
        "eu.patientsK": {"note": "TREAT-NMD: ~15K EU-5 DMD; ~13% exon 51 = ~2K; EMA declined Exondys 51 (efficacy concerns)."},
        "row.patientsK":{"note": "Global DMD ~300K; ex-US/EU exon 51 ~4K; Japan approved Exondys analogs, limited ROW."},
        "us.wtpPct":    {"note": "~50% -- Sarepta Eteplirsen (Exondys 51) accelerated approval 2016; confirmatory EMBARK ongoing."},
        "eu.wtpPct":    {"note": "~20% -- EMA rejected Exondys 51; named-patient only, no broad reimbursement."},
        "row.wtpPct":   {"note": "~15% -- Japan PMDA approved, emerging markets limited IV infusion infra."},
        "us.priceK":    {"note": "Exondys 51 ~$750K/yr weight-based IV weekly; chronic dosing pre-gene-therapy era."},
        "eu.priceK":    {"note": "~$500K/yr named-patient where available; no HTA-backed reimbursement."},
        "row.priceK":   {"note": "~$400K blended; Japan premium, rest ROW sparse."},
        "penPct":       {"note": "~35% peak -- cannibalization by Elevidys gene therapy accelerating in amenable patients."}
    },
    "musculoskeletal.neuromuscular.dmd.exon53": {
        "us.patientsK": {"note": "PPMD/MDA: ~12K US DMD; exon 53-skip amenable ~8% = ~1.2K addressable (Leiden mutation db)."},
        "eu.patientsK": {"note": "TREAT-NMD: ~15K EU-5 DMD; ~8% exon 53 = ~1.2K amenable; EMA no approval."},
        "row.patientsK":{"note": "Global DMD exon 53 ~2K ex-US/EU accessible; Japan NS Pharma Viltepso approved 2020."},
        "us.wtpPct":    {"note": "~50% -- Sarepta Vyondys 53 (golodirsen) + NS Pharma Viltepso (viltolarsen) both approved."},
        "eu.wtpPct":    {"note": "~20% -- EMA negative opinion on exon-skippers; named-patient access."},
        "row.wtpPct":   {"note": "~20% -- Japan co-developed Viltepso, strong PMDA/MHLW support; rest ROW sparse."},
        "us.priceK":    {"note": "Vyondys 53 ~$750K/yr; Viltepso similar; weight-based IV weekly chronic dosing."},
        "eu.priceK":    {"note": "~$500K/yr where named-patient available."},
        "row.priceK":   {"note": "Japan Viltepso ~$600K; emerging markets minimal."},
        "penPct":       {"note": "~35% peak -- gene therapy cannibalization similar to exon 51/45 dynamics."}
    },
    "musculoskeletal.neuromuscular.dmd.gene_therapy": {
        "us.patientsK":  {"note": "MDA + PPMD: ~12K US DMD total; ~7K ambulatory + eligible (excl exon 8/9 del, immune-incompatible AAVrh74)."},
        "eu.patientsK":  {"note": "TREAT-NMD EU registry: ~15K DMD; ~9K ambulatory eligible for Elevidys (Roche ex-US partner)."},
        "row.patientsK": {"note": "Global DMD ~300K; ex-US/EU ~12K diagnosed & potentially accessible (Japan approved, LatAm/APAC limited)."},
        "us.wtpPct":     {"note": "~55% -- post-safety events (3 deaths) commercial payor scrutiny + PA requirements; families still willing but logistics complex."},
        "eu.wtpPct":     {"note": "~35% -- EMA conditional approval; NICE/G-BA pricing negotiations ongoing; Roche leads ex-US launches."},
        "row.wtpPct":    {"note": "~10% -- Japan PMDA approved 2025; Brazil/select APAC limited; most ROW lacks AAV infusion capacity."},
        "us.priceK":     {"note": "Elevidys $3.2M list / ~$2.6M net one-time; amortize $500K/yr over 5yr effective lifetime dosing."},
        "eu.priceK":     {"note": "EU Elevidys ~$1.8M one-time (amortize $360K/yr); Roche HTA pricing discount ~30-45% vs US."},
        "row.priceK":    {"note": "$800K blended one-time (~$160K/yr amortized); Japan ~$1.5M via J-DPS, emerging markets tiered."},
        "penPct":        {"note": "~12% peak reflects one-time treatment nature -- saturates ambulatory pool within 3-5yr post-launch."}
    },
    "musculoskeletal.neuromuscular.fshd": {
        "us.patientsK": {"note": "FSHD Society: ~17K US FSHD (~1:20K prevalence); type 1 (D4Z4 contraction) ~95%, type 2 SMCHD1 ~5%."},
        "eu.patientsK": {"note": "Orphanet EU-5: ~22K FSHD; TREAT-NMD/UK FSHD registry; no approved DMT, symptom mgmt only."},
        "row.patientsK":{"note": "Global ~870K FSHD; ex-US/EU ~15K on specialty care; awareness rising via Fulcrum/Dyne trials."},
        "us.wtpPct":    {"note": "~55% -- zero approved DMT; Fulcrum losmapimod P3 REACH ongoing; patient advocacy strong."},
        "eu.wtpPct":    {"note": "~35% -- EMA orphan designation; HTA will require functional benefit (Reachable Workspace, FSHD-COM)."},
        "row.wtpPct":   {"note": "~15% -- limited diagnostic infra; Japan/EU-adjacent markets primary ROW access."},
        "us.priceK":    {"note": "FSHD DMT modeled ~$400K/yr oral small molecule; orphan premium chronic dosing."},
        "eu.priceK":    {"note": "~$260K/yr post-HTA (~35% discount); outcomes-based agreements likely."},
        "row.priceK":   {"note": "~$130K/yr blended; Japan ~$300K, emerging markets limited."},
        "penPct":       {"note": "~30% peak -- ambulatory + mild/moderate patients primary eligibility per trial criteria."}
    },
    "musculoskeletal.neuromuscular.lgmd": {
        "us.patientsK": {"note": "MDA/NORD: ~5K US LGMD total across subtypes; LGMD2E (SGCB) ~500; LGMD2I/2A/2B larger subsets."},
        "eu.patientsK": {"note": "Orphanet EU-5: ~7K LGMD; TREAT-NMD registry; Sarepta SRP-9003 (LGMD2E) gene tx in trials."},
        "row.patientsK":{"note": "Global LGMD ~140K; ex-US/EU ~4K diagnosed; genetic subtyping gap in emerging markets."},
        "us.wtpPct":    {"note": "~50% -- ultra-rare subtypes; gene therapy one-time potential high WTP for confirmed genotype."},
        "eu.wtpPct":    {"note": "~30% -- EMA orphan; HTA will scrutinize one-time gene tx durability data."},
        "row.wtpPct":   {"note": "~10% -- AAV infusion infra limited; Japan/select EU-adjacent primary ROW."},
        "us.priceK":    {"note": "LGMD gene tx modeled ~$2.5M one-time (amortize $500K/yr over 5yr); Sarepta SRP-9003 pipeline."},
        "eu.priceK":    {"note": "~$1.6M one-time post-HTA (amortize $320K/yr); outcomes-based common for gene tx."},
        "row.priceK":   {"note": "~$700K one-time blended (amortize $140K/yr); Japan ~$1.2M, emerging markets minimal."},
        "penPct":       {"note": "~15% peak -- subtype-specific gene tx (one per SGCB/SGCA/etc.); each addresses <15% of LGMD pool."}
    },

    # =====================================================================
    # INFECTIOUS DISEASE - ANTI-INFECTIVE
    # =====================================================================
    "infectious_disease.anti_infective.hiv_prevention": {
        "us.patientsK": {"note": "CDC: ~1.2M US PrEP-eligible (MSM, high-risk hetero, PWID); ~400K currently on PrEP (Truvada/Descovy/Apretude)."},
        "eu.patientsK": {"note": "ECDC: ~600K EU-5 PrEP-eligible; uptake highest France/UK/Germany; oral generic TDF/FTC dominates."},
        "row.patientsK":{"note": "WHO global PrEP-eligible ~15M; ex-US/EU ~8M accessible (SSA focus via PEPFAR/Global Fund)."},
        "us.wtpPct":    {"note": "~65% -- ACA preventive services $0 copay mandate; long-acting cabotegravir (Apretude) Q2M adherence advantage."},
        "eu.wtpPct":    {"note": "~45% -- national HIV programs cover; generic TDF/FTC dominant; LA injectable slower uptake."},
        "row.wtpPct":   {"note": "~25% -- PEPFAR/Global Fund drive access; lenacapavir 6-monthly Q2025+ game-changer in SSA."},
        "us.priceK":    {"note": "Apretude ~$22K/yr (Q2M IM); Descovy ~$24K/yr oral daily; generic TDF/FTC <$0.5K/yr."},
        "eu.priceK":    {"note": "Apretude ~$15K/yr post-HTA; oral generic TDF/FTC ~$0.3K/yr dominates EU prescriptions."},
        "row.priceK":   {"note": "Generic oral <$0.1K/yr via PEPFAR; LA cabotegravir Gilead tiered $0-5K; lenacapavir access pricing pending."},
        "penPct":       {"note": "~35% peak PrEP uptake within eligible pool; long-acting formulations driving growth from ~33% current."}
    },
    "infectious_disease.anti_infective.hiv_treatment": {
        "us.patientsK": {"note": "CDC: ~1.2M US PLHIV (~1.1M diagnosed); ~75% on ART achieving viral suppression; Ryan White program."},
        "eu.patientsK": {"note": "ECDC: ~900K EU-5 PLHIV on ART; integrase inhibitor regimens (Biktarvy dominant); LA Cabenuva Q2M rising."},
        "row.patientsK":{"note": "UNAIDS global ~39M PLHIV; ~30M on ART; ex-US/EU ~25M via WHO/PEPFAR/Global Fund tiered access."},
        "us.wtpPct":    {"note": "~85% -- universal test-and-treat guideline; Medicaid/Ryan White cover; Biktarvy gold standard."},
        "eu.wtpPct":    {"note": "~80% -- universal access via national HIV programs; generic dolutegravir-based regimens widely used."},
        "row.wtpPct":   {"note": "~65% -- PEPFAR/Global Fund dolutegravir-based TLD (tenofovir/lamivudine/DTG) generic access."},
        "us.priceK":    {"note": "Biktarvy ~$45K/yr WAC; Cabenuva LA Q2M ~$48K/yr; chronic lifetime dosing."},
        "eu.priceK":    {"note": "Biktarvy ~$25K/yr post-HTA; generic DTG-based ~$2K/yr; 60% discount typical vs US."},
        "row.priceK":   {"note": "Generic TLD <$0.1K/yr via PEPFAR/tiered pricing; branded LA cabotegravir niche use."},
        "penPct":       {"note": "~40% peak for branded LA/novel agents within treated pool; generics dominate base."}
    },

    # =====================================================================
    # INFECTIOUS DISEASE - VACCINES
    # =====================================================================
    "infectious_disease.vaccines.chikungunya": {
        "us.patientsK": {"note": "CDC: ~500K potential doses/yr US travel + endemic Puerto Rico/USVI; Ixchiq (Valneva) approved 2023 age 18+."},
        "eu.patientsK": {"note": "EMA approved Ixchiq 2024; ~200K EU-5 doses/yr travelers to Americas/SSA/South Asia endemic zones."},
        "row.patientsK":{"note": "WHO: global chikungunya outbreak-prone; ~3M doses/yr endemic (Brazil, India, SE Asia) + travel."},
        "us.wtpPct":    {"note": "~45% -- ACIP recommends for travelers to outbreak areas + lab workers; not routine immunization."},
        "eu.wtpPct":    {"note": "~35% -- EMA approved; national travel clinics + outbreak response; not in routine schedule."},
        "row.wtpPct":   {"note": "~20% -- Brazil ANVISA approved 2024; outbreak stockpile procurement (WHO/Gavi emerging)."},
        "us.priceK":    {"note": "Ixchiq ~$0.3K per dose list (single-dose live attenuated); travel clinic pricing."},
        "eu.priceK":    {"note": "~$0.2K per dose post-HTA; national immunization tenders lower."},
        "row.priceK":   {"note": "~$0.05K per dose tiered via PAHO/Gavi for endemic Brazil/LatAm; single-dose."},
        "penPct":       {"note": "~30% peak of addressable travel + outbreak response; competition from Bavarian Nordic VLA1553-bivalent."}
    },
    "infectious_disease.vaccines.lyme": {
        "us.patientsK": {"note": "CDC: ~20M US in Lyme-endemic areas (Northeast/Midwest); ~476K new cases/yr; Pfizer/Valneva VLA15 P3 ongoing."},
        "eu.patientsK": {"note": "ECDC: ~15M EU-5 endemic exposure (Germany/Austria/Scandinavia); ~85K cases/yr reported."},
        "row.patientsK":{"note": "Global Lyme-endemic exposure ~50M; ROW mostly Canada/Russia/China endemic focus areas."},
        "us.wtpPct":    {"note": "~40% -- ACIP likely to recommend post-approval for endemic residents + outdoor workers; school-age focus."},
        "eu.wtpPct":    {"note": "~30% -- STIKO/JCVI likely endemic-region recommendation; similar TBE vaccine adoption pattern."},
        "row.wtpPct":   {"note": "~15% -- Canada NACI + Russia endemic; most ROW low priority for immunization programs."},
        "us.priceK":    {"note": "VLA15 modeled ~$0.2K per dose (3-dose primary + boosters); Pfizer adult/pediatric pricing."},
        "eu.priceK":    {"note": "~$0.15K per dose post-HTA; national tender pricing likely lower."},
        "row.priceK":   {"note": "~$0.1K per dose blended; Canada/Russia primary markets."},
        "penPct":       {"note": "~25% peak of endemic eligible pool within 5yr; competition from Moderna mRNA Lyme (mRNA-1975)."}
    },
    "infectious_disease.vaccines.shigella_zika": {
        "us.patientsK": {"note": "CDC: ~5M global potential doses/yr travel + endemic (shigella pediatric LMIC, Zika outbreak response)."},
        "eu.patientsK": {"note": "EMA/ECDC: travel clinic + outbreak response; shigella pediatric focus for LMIC via Gavi; Zika stockpile."},
        "row.patientsK":{"note": "WHO shigella LMIC pediatric ~100M birth cohort Gavi-eligible; Zika endemic Americas/APAC."},
        "us.wtpPct":    {"note": "~25% -- shigella primarily LMIC pediatric; US travel niche; Zika outbreak-response procurement."},
        "eu.wtpPct":    {"note": "~20% -- travel clinic + outbreak stockpile; EMA approval pathways open for both."},
        "row.wtpPct":   {"note": "~35% -- Gavi procurement for LMIC pediatric shigella; Zika PAHO stockpile LatAm."},
        "us.priceK":    {"note": "Shigella/Zika vaccines modeled ~$0.15K per dose US travel; outbreak response procurement."},
        "eu.priceK":    {"note": "~$0.1K per dose travel clinic; lower via tender."},
        "row.priceK":   {"note": "~$0.02K per dose Gavi tiered (shigella LMIC); Zika outbreak stockpile similar."},
        "penPct":       {"note": "~20% peak -- early-stage assets; shigella strong LMIC volume + Gavi procurement potential."}
    },
    "infectious_disease.vaccines.travel": {
        "us.patientsK": {"note": "CDC: ~30M US international travelers/yr needing travel vaccines (YF, JE, typhoid, rabies, cholera)."},
        "eu.patientsK": {"note": "ECDC: ~80M EU-5 international travelers/yr; Sanofi/GSK/Valneva/Bavarian Nordic dominant portfolio."},
        "row.patientsK":{"note": "WHO: ~200M global travel vaccine doses/yr; pilgrimage (Hajj) + business travel + expatriate."},
        "us.wtpPct":    {"note": "~55% -- out-of-pocket at travel clinics; employer-paid for business; not in ACIP routine schedule."},
        "eu.wtpPct":    {"note": "~50% -- national travel clinics (UK/France/Germany) + private; military/expatriate coverage."},
        "row.wtpPct":   {"note": "~40% -- pilgrimage mandatory (Saudi YF/meningitis); business travel private; expat employer."},
        "us.priceK":    {"note": "YF Stamaril ~$0.25K, JE Ixiaro ~$0.3K x2, typhoid Typhim Vi ~$0.1K, rabies ~$0.3K x3 per dose."},
        "eu.priceK":    {"note": "~20-30% lower than US; national tenders for military/govt travel further discounted."},
        "row.priceK":   {"note": "Pilgrimage volume driven; tiered pricing via WHO prequalification + PAHO."},
        "penPct":       {"note": "~25% peak of travelers actually vaccinated; steady mature market, innovation via new indications."}
    },

    # =====================================================================
    # OPHTHALMOLOGY - ANTERIOR & NEURO
    # =====================================================================
    "ophthalmology.anterior_neuro.deb_ocular": {
        "us.patientsK": {"note": "DEBRA/Cure DEB: ~3K US DEB; ocular complications (corneal erosions, symblepharon) in ~500 severe RDEB."},
        "eu.patientsK": {"note": "EB-CLINET/DEBRA EU: ~4K EU-5 DEB; ~700 with ocular manifestations; topical Vyjuvek (Krystal) approved."},
        "row.patientsK":{"note": "Global DEB ~50K; ex-US/EU ~1K with severe ocular involvement accessible in specialty centers."},
        "us.wtpPct":    {"note": "~55% -- Vyjuvek topical gene tx approved 2023 for skin; ocular formulation Krystal B-VEC-101 P1/2."},
        "eu.wtpPct":    {"note": "~30% -- EMA Vyjuvek 2024; ocular indication pending; named-patient ultra-rare access."},
        "row.wtpPct":   {"note": "~10% -- ultra-rare ocular subset; Japan/EU-adjacent only primary ROW."},
        "us.priceK":    {"note": "Vyjuvek ocular modeled ~$350K/yr topical redosing; Krystal pipeline indication extension."},
        "eu.priceK":    {"note": "~$230K/yr post-HTA ocular extension; named-patient where available."},
        "row.priceK":   {"note": "~$100K/yr blended; minimal access outside US/EU-5/Japan."},
        "penPct":       {"note": "~25% peak -- severe ocular DEB subset only; Vyjuvek topical delivery feasibility dependent."}
    },
    "ophthalmology.anterior_neuro.dry_eye": {
        "us.patientsK": {"note": "AAO/NEI: ~16M US dry eye disease diagnosed; ~4M moderate-severe Rx-treated; Restasis/Xiidra/Miebo/Tyrvaya."},
        "eu.patientsK": {"note": "EU dry eye ~30M; ~5M Rx-treated; Ikervis (ciclosporin) + generics dominate; newer agents EMA pending."},
        "row.patientsK":{"note": "Global dry eye ~300M; ~15M ex-US/EU Rx-treated; Japan rebamipide (Mucosta) widely used."},
        "us.wtpPct":    {"note": "~40% -- crowded class Restasis generic, Xiidra (Bausch), Miebo (Bausch 2023), Tyrvaya (Viatris nasal spray)."},
        "eu.wtpPct":    {"note": "~30% -- Ikervis reimbursed; HTA strict on incremental benefit; generic ciclosporin pressure."},
        "row.wtpPct":   {"note": "~20% -- Japan rebamipide standard; emerging markets mostly artificial tears OTC."},
        "us.priceK":    {"note": "Xiidra ~$7K/yr WAC; Miebo ~$6K/yr; Tyrvaya ~$7K/yr; Restasis generic <$1K/yr."},
        "eu.priceK":    {"note": "Ikervis ~$2K/yr post-HTA; generic ciclosporin ~$0.3K/yr."},
        "row.priceK":   {"note": "Blended ~$0.5K/yr; Japan rebamipide ~$0.3K, emerging markets OTC tears dominate."},
        "penPct":       {"note": "~15% peak for branded Rx within diagnosed pool; high OTC artificial tear use caps Rx share."}
    },
    "ophthalmology.anterior_neuro.naion": {
        "us.patientsK": {"note": "AAO/NANOS: ~6K US non-arteritic AION/yr incidence; acute onset optic nerve ischemia, typically >50yr."},
        "eu.patientsK": {"note": "ESAO: ~8K EU-5 NAION/yr incidence; no approved Rx, supportive care only (aspirin, BP control)."},
        "row.patientsK":{"note": "Global NAION ~60K/yr; ex-US/EU ~10K accessible in specialty ophthalmology centers."},
        "us.wtpPct":    {"note": "~50% -- zero approved Rx; Quark QPI-1007 P3 failed; Stoke STK-002 P1 early; high unmet need."},
        "eu.wtpPct":    {"note": "~30% -- EMA orphan pathway; HTA will require visual acuity endpoint (ETDRS letters gain)."},
        "row.wtpPct":   {"note": "~10% -- acute care specialty access limited outside US/EU-5/Japan."},
        "us.priceK":    {"note": "NAION Rx modeled ~$40K acute course (single/short course IVT); premium for approved agent."},
        "eu.priceK":    {"note": "~$25K acute course post-HTA."},
        "row.priceK":   {"note": "~$12K acute course blended."},
        "penPct":       {"note": "~15% peak -- narrow 14-day acute window limits addressable; late presentation common."}
    },
    "ophthalmology.anterior_neuro.neurotrophic_keratitis": {
        "us.patientsK": {"note": "AAO: ~5K US neurotrophic keratitis stage 2/3 (corneal ulcer); Oxervate (cenegermin) approved 2018."},
        "eu.patientsK": {"note": "Orphanet EU-5: ~7K NK stage 2/3; Oxervate EMA approved 2017; Dompe (now Chiesi) commercial."},
        "row.patientsK":{"note": "Global NK ~80K moderate-severe; ex-US/EU ~4K on specialty corneal care."},
        "us.wtpPct":    {"note": "~60% -- Oxervate first-in-class; strong ophthalmology KOL adoption; specialty pharmacy dispense."},
        "eu.wtpPct":    {"note": "~45% -- EMA approved with reimbursement; Chiesi commercial across EU-5."},
        "row.wtpPct":   {"note": "~20% -- Japan PMDA approved 2024; emerging markets limited specialty access."},
        "us.priceK":    {"note": "Oxervate ~$96K per 8-week course (6x daily drops); typically 1-2 courses."},
        "eu.priceK":    {"note": "~$60K per course post-HTA."},
        "row.priceK":   {"note": "~$35K per course blended."},
        "penPct":       {"note": "~35% peak of stage 2/3 NK; 8-week course nature limits chronic exposure."}
    },
    "ophthalmology.anterior_neuro.optic_neuritis": {
        "us.patientsK": {"note": "AAO/NANOS: ~15K US optic neuritis/yr (MS-associated dominant); acute demyelinating episode."},
        "eu.patientsK": {"note": "ECTRIMS: ~20K EU-5 ON/yr; IV methylprednisolone standard acute; remyelination agents in trials."},
        "row.patientsK":{"note": "Global ON ~150K/yr; MS prevalence-driven; ex-US/EU ~12K accessible in MS specialty centers."},
        "us.wtpPct":    {"note": "~45% -- acute IV steroid standard; novel remyelinating agents (e.g., Clene CNM-Au8) late-stage trials."},
        "eu.wtpPct":    {"note": "~30% -- EMA orphan/fast-track pathways; HTA will require OCT RNFL + visual acuity endpoints."},
        "row.wtpPct":   {"note": "~15% -- MS specialty care limited outside OECD; acute steroid universal."},
        "us.priceK":    {"note": "Remyelinating agent modeled ~$50K acute course; one-time/short-course pricing."},
        "eu.priceK":    {"note": "~$30K post-HTA."},
        "row.priceK":   {"note": "~$15K blended."},
        "penPct":       {"note": "~20% peak -- acute window + MS workflow integration; background steroid still SOC."}
    },
    "ophthalmology.anterior_neuro.ted": {
        "us.patientsK": {"note": "AAO/Graves' Foundation: ~50K US Thyroid Eye Disease (Tepezza-addressable moderate-severe active)."},
        "eu.patientsK": {"note": "EUGOGO: ~70K EU-5 TED moderate-severe; Tepezza EMA approved 2025; historically IV steroids + orbital radiation."},
        "row.patientsK":{"note": "Global TED ~500K; ex-US/EU ~30K accessible in specialty endocrine/ophthalmology centers."},
        "us.wtpPct":    {"note": "~65% -- Tepezza (Amgen/Horizon) first-in-class; strong proptosis reduction data; PA + pricing scrutiny."},
        "eu.wtpPct":    {"note": "~40% -- EMA approved 2025; HTA ongoing; competitive IV steroid standard still cheap."},
        "row.wtpPct":   {"note": "~15% -- Japan Amgen partnership; rest ROW limited access."},
        "us.priceK":    {"note": "Tepezza ~$450K per 8-infusion course (Q3W x 8); typically 1 course, retreatment rare."},
        "eu.priceK":    {"note": "~$280K per course post-HTA."},
        "row.priceK":   {"note": "~$150K per course blended; Japan ~$350K."},
        "penPct":       {"note": "~30% peak of moderate-severe active TED; competition from Viridian VRDN-003 SC late-stage."}
    },

    # =====================================================================
    # OPHTHALMOLOGY - RETINA
    # =====================================================================
    "ophthalmology.retina.dme": {
        "us.patientsK": {"note": "CDC DiRECT + NEI: ~750K US diabetic macular edema; anti-VEGF (Eylea/Vabysmo/Lucentis) standard IVT Rx."},
        "eu.patientsK": {"note": "EU DME ~1M; anti-VEGF + dexamethasone implant (Ozurdex); biosimilar ranibizumab eroding originator."},
        "row.patientsK":{"note": "Global DME ~21M (IDF diabetes-driven); ex-US/EU ~500K on IVT therapy in specialty retina centers."},
        "us.wtpPct":    {"note": "~70% -- Medicare Part B coverage; anti-VEGF workhorse; Vabysmo Q16W durability advantage vs Eylea Q8W."},
        "eu.wtpPct":    {"note": "~55% -- national health coverage; biosimilar ranibizumab cost pressure; Vabysmo HTA ongoing."},
        "row.wtpPct":   {"note": "~30% -- Japan/Korea strong anti-VEGF use; emerging markets bevacizumab off-label compounded."},
        "us.priceK":    {"note": "Eylea HD ~$11K/yr (Q8-16W IVT); Vabysmo ~$12K/yr; Lucentis ~$14K/yr; biosimilars ~$5K/yr."},
        "eu.priceK":    {"note": "Eylea ~$6K/yr post-HTA; biosimilar ranibizumab ~$2K/yr dominant in several markets."},
        "row.priceK":   {"note": "~$2K/yr blended; compounded bevacizumab <$0.2K/dose common in emerging markets."},
        "penPct":       {"note": "~35% peak of diagnosed DME on IVT therapy; suboptimal adherence + undertreatment limits ceiling."}
    },
    "ophthalmology.retina.dr": {
        "us.patientsK": {"note": "NEI/CDC: ~800K US treated diabetic retinopathy (PDR + severe NPDR); anti-VEGF + PRP laser standard."},
        "eu.patientsK": {"note": "EU treated DR ~1.1M; similar anti-VEGF + PRP paradigm; screening programs variable by country."},
        "row.patientsK":{"note": "Global DR ~100M (103M IAPB); ~4M treated ex-US/EU; massive undertreatment in LMIC."},
        "us.wtpPct":    {"note": "~65% -- Medicare Part B coverage; anti-VEGF first-line per DRCR.net; PRP still used for PDR."},
        "eu.wtpPct":    {"note": "~50% -- national screening/treatment programs; biosimilar pressure on anti-VEGF pricing."},
        "row.wtpPct":   {"note": "~25% -- Japan/Korea specialty retina strong; emerging markets laser + bevacizumab off-label."},
        "us.priceK":    {"note": "Eylea ~$11K/yr; Vabysmo ~$12K/yr IVT; similar to DME pricing (same agents)."},
        "eu.priceK":    {"note": "~$6K/yr post-HTA; biosimilar ~$2K/yr."},
        "row.priceK":   {"note": "~$2K/yr blended; bevacizumab compounded <$0.2K/dose."},
        "penPct":       {"note": "~30% peak -- PRP-only treated portion cannibalized by anti-VEGF in PDR expansion."}
    },
    "ophthalmology.retina.ga": {
        "us.patientsK": {"note": "AAO/BrightFocus: ~1M US geographic atrophy (AMD advanced dry form); Syfovre/Izervay anti-C3/C5 IVT approved."},
        "eu.patientsK": {"note": "EU GA ~1.5M; EMA declined Syfovre (risk/benefit); Izervay (Astellas) EU pending; high unmet need."},
        "row.patientsK":{"note": "Global GA ~5M; ex-US/EU ~200K on Rx (Japan pending); massive untreated pool."},
        "us.wtpPct":    {"note": "~35% -- Syfovre (Apellis) + Izervay (Astellas) approved but modest VA benefit + IOI risk limits uptake."},
        "eu.wtpPct":    {"note": "~10% -- EMA declined Syfovre 2024; Izervay review pending; HTA tough on modest benefit."},
        "row.wtpPct":   {"note": "~10% -- Japan PMDA reviewing; rest ROW limited access until label + pricing clarity."},
        "us.priceK":    {"note": "Syfovre ~$25K/yr (Q4-8W IVT); Izervay ~$25K/yr (Q4W IVT); Medicare Part B coverage."},
        "eu.priceK":    {"note": "Izervay modeled ~$15K/yr post-HTA if approved; Syfovre declined."},
        "row.priceK":   {"note": "~$8K/yr blended; Japan ~$18K if approved."},
        "penPct":       {"note": "~10% peak -- modest VA benefit + monthly/Q2M IVT burden + IOI adverse events limit uptake."}
    },
    "ophthalmology.retina.nvamd": {
        "us.patientsK": {"note": "AAO/BrightFocus: ~200K US nvAMD on active anti-VEGF treatment (~1.5M nvAMD total, undertreated)."},
        "eu.patientsK": {"note": "EU nvAMD ~300K on treatment; anti-VEGF standard; Eylea HD Q16W + Vabysmo durability advantage."},
        "row.patientsK":{"note": "Global nvAMD ~20M; ~1M on ex-US/EU treatment; Japan aggressive anti-VEGF use."},
        "us.wtpPct":    {"note": "~80% -- Medicare Part B workhorse; anti-VEGF dominant IVT class; biosimilar entry expanding."},
        "eu.wtpPct":    {"note": "~65% -- national health coverage; biosimilar ranibizumab + aflibercept driving cost down."},
        "row.wtpPct":   {"note": "~35% -- Japan/Korea strong; emerging markets compounded bevacizumab common."},
        "us.priceK":    {"note": "Eylea HD ~$11K/yr; Vabysmo ~$12K/yr; Lucentis ~$14K/yr; biosimilars ~$5K/yr."},
        "eu.priceK":    {"note": "Eylea ~$6K/yr post-HTA; biosimilar ~$2K/yr dominant."},
        "row.priceK":   {"note": "~$2K/yr blended; compounded bevacizumab <$0.2K/dose."},
        "penPct":       {"note": "~50% peak for Eylea HD/Vabysmo share within treated pool; biosimilar cannibalization ongoing."}
    },
    "ophthalmology.optic_nerve.lhon": {
        "us.patientsK": {"note": "NORD/UMDF: ~4K US Leber hereditary optic neuropathy (mtDNA mutations ND4/ND1/ND6); ~300 new/yr."},
        "eu.patientsK": {"note": "Orphanet EU-5: ~6K LHON; GS010 (lenadogene, GenSight) EMA conditional approval pending re-submission."},
        "row.patientsK":{"note": "Global LHON ~100K; ex-US/EU ~3K accessible; Japan/UK LHON registries."},
        "us.wtpPct":    {"note": "~45% -- Tnaogen idebenone off-label; GenSight lenadogene IVT gene tx filing pending post-RESCUE/REVERSE."},
        "eu.wtpPct":    {"note": "~30% -- EMA previously negative on lenadogene; resubmission with REFLECT data pending."},
        "row.wtpPct":   {"note": "~10% -- ultra-rare; Japan/select EU-adjacent only."},
        "us.priceK":    {"note": "LHON gene tx modeled ~$800K one-time IVT (amortize $160K/yr over 5yr); orphan ultra-rare premium."},
        "eu.priceK":    {"note": "~$500K one-time post-HTA (amortize $100K/yr)."},
        "row.priceK":   {"note": "~$200K one-time blended (amortize $40K/yr)."},
        "penPct":       {"note": "~20% peak -- early-stage vision loss (<1yr) only; late presentation common, limits eligibility."}
    },
    "ophthalmology.optic_nerve.nmosd": {
        "us.patientsK": {"note": "Guthy-Jackson/NMSS: ~15K US NMOSD (neuromyelitis optica spectrum); ~2-3K new/yr; AQP4-IgG+ majority."},
        "eu.patientsK": {"note": "EU NMOSD ~20K; Soliris/Uplizna/Enspryng approved EMA; steroid-sparing biologic era."},
        "row.patientsK":{"note": "Global NMOSD ~150K; ex-US/EU ~20K on biologic/specialty care; Japan/Asia higher prevalence."},
        "us.wtpPct":    {"note": "~75% -- Soliris (eculizumab), Uplizna (inebilizumab), Enspryng (satralizumab) all approved; strong uptake."},
        "eu.wtpPct":    {"note": "~55% -- EMA approved all three; HTA pricing negotiations ongoing; Soliris generic eculizumab (Bkemv) 2025."},
        "row.wtpPct":   {"note": "~30% -- Japan strong satralizumab (Chugai origin); rest ROW limited biologic access."},
        "us.priceK":    {"note": "Soliris ~$500K/yr; Uplizna ~$400K/yr; Enspryng ~$200K/yr SC; chronic dosing lifetime."},
        "eu.priceK":    {"note": "Soliris ~$350K/yr; Uplizna ~$280K/yr; Enspryng ~$140K/yr post-HTA."},
        "row.priceK":   {"note": "Blended ~$150K/yr; Japan satralizumab ~$180K."},
        "penPct":       {"note": "~40% peak for branded biologics within AQP4+ pool; eculizumab biosimilar (Bkemv) pricing pressure."}
    },

    # =====================================================================
    # RESPIRATORY - INFLAMMATORY
    # =====================================================================
    "respiratory.inflammatory.asthma_severe": {
        "us.patientsK": {"note": "CDC/AAAAI: ~26M US asthma; ~10% severe = ~2.5M; biologics (Dupixent/Tezspire/Nucala/Fasenra/Xolair) for Type 2."},
        "eu.patientsK": {"note": "GINA: ~30M EU-5 asthma; ~3M severe; biologic penetration ~15% of severe pool, rising."},
        "row.patientsK":{"note": "Global asthma ~262M (GINA); ~25M severe ex-US/EU; Japan/China large pools, biologic uptake rising."},
        "us.wtpPct":    {"note": "~70% -- biologics strong commercial/Medicare coverage; PA + specialist Rx; Tezspire (TSLP) broad Type 2-low coverage."},
        "eu.wtpPct":    {"note": "~55% -- national coverage via HTA; NICE/G-BA restrict to specific biomarker thresholds."},
        "row.wtpPct":   {"note": "~25% -- Japan/Korea strong biologic uptake; emerging markets rely on ICS/LABA + oral steroids."},
        "us.priceK":    {"note": "Dupixent ~$40K/yr; Tezspire ~$45K/yr; Nucala/Fasenra/Xolair ~$30-35K/yr SC; chronic."},
        "eu.priceK":    {"note": "Dupixent ~$22K/yr post-HTA; similar ~40-50% discount across class."},
        "row.priceK":   {"note": "~$10K/yr blended; Japan ~$25K, emerging markets minimal biologic use."},
        "penPct":       {"note": "~25% peak of severe asthma on biologics; Type 2-high/Type 2-low segmentation drives agent selection."}
    },
    "respiratory.inflammatory.copd": {
        "us.patientsK": {"note": "GOLD/CDC: ~15M US COPD diagnosed (~30M total incl undiagnosed); ~3M severe GOLD 3-4; Dupixent approved 2024."},
        "eu.patientsK": {"note": "GOLD EU-5: ~20M COPD; ~4M severe; LAMA/LABA/ICS triple (Trelegy) standard; biologics emerging."},
        "row.patientsK":{"note": "WHO: global COPD ~390M; ~30M ex-US/EU severe; China/India massive smoking/pollution-driven pools."},
        "us.wtpPct":    {"note": "~60% -- Dupixent (dupilumab) first biologic in COPD (eosinophilic phenotype); Medicare coverage strong."},
        "eu.wtpPct":    {"note": "~40% -- Dupixent EMA approved 2024 COPD indication; HTA will restrict to eosinophilic GOLD 3-4."},
        "row.wtpPct":   {"note": "~15% -- Japan/Korea early biologic adoption; emerging markets inhaled triple therapy generic-dominated."},
        "us.priceK":    {"note": "Dupixent ~$40K/yr SC Q2W chronic; Trelegy triple ICS/LAMA/LABA ~$5K/yr inhaler."},
        "eu.priceK":    {"note": "Dupixent ~$22K/yr post-HTA; Trelegy ~$2.5K/yr."},
        "row.priceK":   {"note": "Blended ~$1K/yr -- generic inhaled therapies dominate; biologic niche in OECD."},
        "penPct":       {"note": "~10% peak for biologics in severe eosinophilic COPD subset; inhaled triple therapy remains base SOC."}
    },
}
