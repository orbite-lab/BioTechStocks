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
    # source: US osteoporosis ~10M diagnosed (NOF), of which ~3-5M are at high
    # fracture risk (the branded-biologic addressable subset). Bisphosphonate
    # generics dominate first-line at <$200/yr. Branded class (Prolia $4B +
    # Evenity $1.5B + Forteo $0.7B + Tymlos $0.4B + Tymlos generic emerging)
    # totals ~$7B today; analyst peak $15-20B as Prolia loses exclusivity but
    # Evenity + new Romosozumab follow-ons grow. Prior US TAM 10M x 35% x $25K
    # = $87B treated all OP patients as biologic-priced -- ~6x off.
    "musculoskeletal.bone_cartilage.osteoporosis": {
        "us":  {"patientsK": 5000,  "wtpPct": 35, "priceK": 5},
        "eu":  {"patientsK": 8000,  "wtpPct": 25, "priceK": 3},
        "row": {"patientsK": 80000, "wtpPct": 10, "priceK": 0.5},
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
    # source: US PLHIV ~1.2M with ~80% on ART (CDC HIV Surveillance); EU5
    # ~900K PLHIV; ROW ~37M (UNAIDS) with treatment access ~75% via PEPFAR
    # /Global Fund at near-generic pricing. Branded ART franchise (Biktarvy
    # $13B + Descovy $2B + Cabenuva LAA $1B + Tivicay/Triumeq + Genvoya etc.)
    # ~$30-35B today globally. Long-acting + Lenacapavir-based regimens push
    # peak to $40-50B by 2030. Prior $66B at $45K WAC across full US PLHIV
    # treated everyone as on Biktarvy-priced ART; ~2x off vs net realized
    # (Medicaid 340B discounts, ADAP, and a chunk on generic Atripla/Truvada).
    "infectious_disease.anti_infective.hiv_treatment": {
        "us":  {"patientsK": 1000,  "wtpPct": 70, "priceK": 25},
        "eu":  {"patientsK": 800,   "wtpPct": 60, "priceK": 12},
        "row": {"patientsK": 28000, "wtpPct": 30, "priceK": 0.4},
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
    # HPV vaccine (Gardasil 9, MRK): adolescent + young adult routine vaccination.
    # US ~25M eligible 9-26 (CDC ACIP catch-up to 26); ~75% 1+ dose coverage;
    # 3-dose series ~$700/yr equivalent. EU ~30M. ROW ~150M (China Gardasil
    # massive — was $5B+ pre-2024 inventory crisis). 2025 Gardasil $5.2B (-39%)
    # post-China inventory pause. Class peak $8-10B at recovery. Cervarix (GSK)
    # near-zero share. source: CDC ACIP; Merck 10-K; WHO EPI coverage.
    "infectious_disease.vaccines.hpv": {
        "us":  {"patientsK": 25000,  "wtpPct": 75, "priceK": 0.7},
        "eu":  {"patientsK": 30000,  "wtpPct": 60, "priceK": 0.45},
        "row": {"patientsK": 150000, "wtpPct": 25, "priceK": 0.18},
    },
    # Pneumococcal vaccines (PCV/PPSV): Prevnar 20 (Pfizer ~$6.5B 2024), Capvaxive
    # 21-valent (Merck launch 2024, $759M 2025), Vaxneuvance 15-valent (Merck),
    # Pneumovax 23 (Merck PPSV legacy). Adult >=50 ACIP-recommended;
    # US ~110M adult eligible (~70% lifetime coverage); EU 200M; ROW broader.
    # Class peak $12-15B globally with universal adult recommendation.
    # source: CDC ACIP 2024; Pfizer + Merck 10-Ks.
    "infectious_disease.vaccines.pneumococcal": {
        "us":  {"patientsK": 110000, "wtpPct": 60, "priceK": 0.22},
        "eu":  {"patientsK": 200000, "wtpPct": 45, "priceK": 0.15},
        "row": {"patientsK": 800000, "wtpPct": 15, "priceK": 0.05},
    },
    # Influenza vaccines: Sanofi #1 globally (Fluzone HD, Flublok recombinant,
    # Vaxigrip, Quadrivalent), GSK Fluarix, CSL Seqirus Afluria/Flucelvax,
    # Moderna mRNA-1010 in Ph3. US ~150M doses/yr (~50% adult coverage),
    # EU ~250M, ROW ~600M. Class peak ~$8-10B globally; pricing pressure
    # 2024-25 (German tender, US Medicare/commercial mix). Sanofi flu franchise
    # ~$3.5B 2025. source: CDC FluVaxView; WHO; Sanofi/GSK 10-Ks.
    "infectious_disease.vaccines.influenza": {
        "us":  {"patientsK": 150000,  "wtpPct": 35, "priceK": 0.05},
        "eu":  {"patientsK": 250000,  "wtpPct": 25, "priceK": 0.03},
        "row": {"patientsK": 600000,  "wtpPct": 12, "priceK": 0.012},
    },
    # Pertussis (whooping cough) booster + DTaP/Tdap: Adacel (Sanofi),
    # Boostrix (GSK), Daptacel/Pediarix (peds). US ~3.7M birth cohort routine
    # + ~10M adult Tdap booster annually; EU 4M peds + 12M adult; ROW 100M
    # peds. Class ~$1B globally. WHO EPI growing.
    "infectious_disease.vaccines.pertussis": {
        # Class bumped to ~$2B globally (Sanofi DTP + GSK Boostrix + peds combos).
        "us":  {"patientsK": 14000,   "wtpPct": 60, "priceK": 0.10},
        "eu":  {"patientsK": 18000,   "wtpPct": 45, "priceK": 0.07},
        "row": {"patientsK": 110000,  "wtpPct": 18, "priceK": 0.025},
    },
    # Meningococcal vaccines: Menactra/Menquadfi (Sanofi MenACWY ~$700M),
    # Bexsero/Trumenba (GSK/Pfizer MenB), Penbraya (Pfizer pentavalent).
    # ACIP recommends adolescent (11-12 + booster 16) + at-risk adult. US ~10M
    # adolescent annual + ~5M adult; EU ~15M; ROW ~50M. Class peak ~$2.5B.
    "infectious_disease.vaccines.meningococcal": {
        # Class peak bumped to $3-3.5B globally to fit actual GSK Bexsero/
        # Menveo/Penmenvy + Pfizer Trumenba + Sanofi MenQuadfi market.
        "us":  {"patientsK": 15000,  "wtpPct": 65, "priceK": 0.20},
        "eu":  {"patientsK": 15000,  "wtpPct": 50, "priceK": 0.13},
        "row": {"patientsK": 50000,  "wtpPct": 18, "priceK": 0.05},
    },
    # IPV (inactivated polio) + Hib (Haemophilus influenzae b) peds vaccines:
    # Sanofi IPV + Hib portfolio (Pentacel, IPOL, ActHIB), GSK Pediarix.
    # US 3.7M birth cohort routine; EU 4M; ROW 120M (WHO EPI). Class ~$2B
    # globally, mature.
    "infectious_disease.vaccines.polio_hib": {
        "us":  {"patientsK": 3700,    "wtpPct": 75, "priceK": 0.18},
        "eu":  {"patientsK": 4000,    "wtpPct": 60, "priceK": 0.12},
        "row": {"patientsK": 120000,  "wtpPct": 18, "priceK": 0.03},
    },
    # COVID mRNA vaccine: Comirnaty (Pfizer/BNT) + Spikevax (Moderna). Routine
    # 2024+ became seasonal annual booster (FDA + CDC ACIP recommendation,
    # adult >=65 + at-risk). Demand normalized post-pandemic: 2024-25 season
    # ~25M doses US, ~80M EU+UK, ~150M ROW. Class peak ~$10-12B globally
    # post-normalization (vs $50B+ at pandemic peak). Pricing $115-130/dose
    # commercial.
    "infectious_disease.vaccines.covid": {
        "us":  {"patientsK": 100000,  "wtpPct": 25, "priceK": 0.13},
        "eu":  {"patientsK": 200000,  "wtpPct": 22, "priceK": 0.09},
        "row": {"patientsK": 1500000, "wtpPct": 8,  "priceK": 0.04},
    },
    # COVID antiviral treatment: Paxlovid (Pfizer nirmatrelvir/ritonavir),
    # Lagevrio (Merck molnupiravir, declining). High-risk symptomatic COVID
    # outpatient. US ~5M Rx eligible/yr, ~80% age>=65 + comorbid. EU 10M, ROW
    # 50M. Class peak ~$2B post-normalization (vs $19B Paxlovid 2022 peak).
    "infectious_disease.anti_infective.covid_treatment": {
        "us":  {"patientsK": 5000,   "wtpPct": 35, "priceK": 1.4},
        "eu":  {"patientsK": 10000,  "wtpPct": 25, "priceK": 0.9},
        "row": {"patientsK": 50000,  "wtpPct": 8,  "priceK": 0.4},
    },
    # RSV adult/maternal vaccine: Abrysvo (Pfizer ~$700M 2025), Arexvy
    # (GSK adjuvanted ~$1.5B 2025), mResvia (Moderna). Adult >=60 ACIP-
    # recommended single-dose; maternal 32-36w gestation Abrysvo. US ~80M
    # adult>=60 + ~3.7M pregnancies; EU ~120M; ROW ~600M. Class peak ~$5-6B
    # globally with universal adult recommendation.
    # source: CDC ACIP RSV adult guidelines; GSK + Pfizer + Moderna 10-Ks.
    "infectious_disease.vaccines.rsv_adult": {
        "us":  {"patientsK": 80000,  "wtpPct": 25, "priceK": 0.27},
        "eu":  {"patientsK": 120000, "wtpPct": 18, "priceK": 0.18},
        "row": {"patientsK": 600000, "wtpPct": 5,  "priceK": 0.06},
    },
    # Rotavirus vaccine (peds): RotaTeq (Merck pentavalent, ~$700M 2025),
    # Rotarix (GSK monovalent, ~$1B 2025). Routine US/EU/many ROW infant
    # immunization (2-3 doses 2-6mo). US 3.7M birth cohort, EU 4M, ROW ~120M.
    # Class peak ~$2-3B globally. WHO EPI growing in LMICs.
    "infectious_disease.vaccines.rotavirus": {
        "us":  {"patientsK": 3700,    "wtpPct": 75, "priceK": 0.2},
        "eu":  {"patientsK": 4000,    "wtpPct": 60, "priceK": 0.13},
        "row": {"patientsK": 100000,  "wtpPct": 22, "priceK": 0.06},
    },
    # MMR + Varicella peds vaccines (combo MMRV ProQuad + monovalent M-M-R II
    # + Varivax + Zostavax shingles legacy). Routine US/EU/many ROW infant +
    # adult shingles. Class peak ~$3-4B (M-M-R II, Varivax, ProQuad, Zostavax
    # combined, mostly Merck) -- declining as Shingrix (GSK adjuvanted) replaces
    # Zostavax for shingles. US 3.7M birth cohort + 80M shingles-eligible adults.
    "infectious_disease.vaccines.mmr_varicella": {
        "us":  {"patientsK": 8000,    "wtpPct": 70, "priceK": 0.15},
        "eu":  {"patientsK": 10000,   "wtpPct": 55, "priceK": 0.1},
        "row": {"patientsK": 250000,  "wtpPct": 18, "priceK": 0.04},
    },
    # Hospital-acquired bacterial infections + general hospital antibiotics:
    # MDR/XDR Gram-negative specialty (US/EU): ceftolozane-tazobactam (Zerbaxa,
    # Merck ~$200M), imipenem-relebactam (Recarbrio, Merck ~$50M), meropenem-
    # vaborbactam, ceftazidime-avibactam. Plus broader hospital antibiotics
    # in China + EM (cefoperazone-sulbactam Sulperazon Pfizer ~$2B China,
    # piperacillin-tazobactam, meropenem branded). ROW patient volumes
    # dominated by China NRDL hospital formularies. Class peak ~$5B globally
    # (US/EU specialty + China branded volume).
    "infectious_disease.anti_infective.bacterial_hospital": {
        "us":  {"patientsK": 750,    "wtpPct": 60, "priceK": 1.5},
        "eu":  {"patientsK": 900,    "wtpPct": 45, "priceK": 0.9},
        "row": {"patientsK": 20000,  "wtpPct": 35, "priceK": 0.5},
    },
    # CMV prophylaxis post-HCT (Prevymis letermovir, Merck ~$500M 2025): post-
    # allogeneic stem cell transplant CMV reactivation prevention. Approved 2017
    # adult HCT, 2023 kidney transplant. ~25K US allogeneic HCT + ~10K kidney/yr
    # at-risk; EU 25K; ROW 50K. Class peak ~$700M-1B. Future: HIV + congenital
    # CMV expansion (Phase 3 SC HCMV vaccine pipeline).
    "infectious_disease.anti_infective.cmv": {
        "us":  {"patientsK": 35,     "wtpPct": 80, "priceK": 25},
        "eu":  {"patientsK": 25,     "wtpPct": 65, "priceK": 15},
        "row": {"patientsK": 50,     "wtpPct": 18, "priceK": 6},
    },
    # NMB Reversal (perioperative anesthesia adjunct): Bridion (Merck sugammadex
    # ~$1.84B), neostigmine generic (dominant ex-US), edrophonium. Reverses
    # rocuronium/vecuronium NMB at end-of-surgery. ~12M US general anesthesia
    # surgeries/yr; ~30% use NMB reversal = ~4M doses. Bridion US LOE 2026
    # (post-AAM litigation). Class branded peak ~$2.5B; biosimilar/generic
    # erosion 2026-28.
    "perioperative.anesthesia.nmb_reversal": {
        "us":  {"patientsK": 4000,   "wtpPct": 55, "priceK": 0.5},
        "eu":  {"patientsK": 5000,   "wtpPct": 45, "priceK": 0.3},
        "row": {"patientsK": 25000,  "wtpPct": 18, "priceK": 0.1},
    },
    # Menopause hormone replacement therapy (HRT): conjugated estrogens
    # (Premarin, Pfizer ~$300M legacy), estradiol+progestin (Prempro), oral
    # contraceptives crossover (Yaz/Yasmin Bayer), intravaginal estrogen.
    # ~50M US menopausal women, ~5M actively on HRT (declined post-WHI 2002
    # safety concerns; modest recovery). Branded tail ~$1B globally;
    # generic dominant.
    "women_health.menopause.hrt": {
        "us":  {"patientsK": 5000,   "wtpPct": 25, "priceK": 0.4},
        "eu":  {"patientsK": 7000,   "wtpPct": 18, "priceK": 0.25},
        "row": {"patientsK": 30000,  "wtpPct": 5,  "priceK": 0.08},
    },
    # Endometriosis: chronic gynecologic pain disorder, ~10-15% of repro-age
    # women. SoC mostly NSAIDs + OCP (generic). Branded specialty class:
    # Orilissa/Oriahnn (AbbVie elagolix GnRH antagonist), Myfembree (Pfizer
    # relugolix combo), Decapeptyl/Trelstar (Ipsen triptorelin GnRH agonist
    # depot), Lupron generics. Most patients DON'T receive branded therapy
    # (low penetration); branded utilization ~5% of diagnosed at ~$1.5K/yr
    # blended. source: ACOG endometriosis prevalence ~6.5M US (11% repro-age),
    # EU5 ~9M; ROW ~50M (under-diagnosed in LMIC).
    "women_health.gyn_disorders.endometriosis": {
        "us":  {"patientsK": 6500,   "wtpPct": 22, "priceK": 1.5},
        "eu":  {"patientsK": 9000,   "wtpPct": 15, "priceK": 0.8},
        "row": {"patientsK": 50000,  "wtpPct": 4,  "priceK": 0.25},
    },
    # Uterine fibroids (leiomyomas): benign smooth-muscle tumors of uterus.
    # Branded specialty class: Myfembree (Pfizer relugolix combo), Oriahnn
    # (AbbVie elagolix combo), Esmya (CDXC ulipristal -- restricted),
    # Decapeptyl (Ipsen triptorelin pre-op shrinkage). Most patients managed
    # via OCP + surgery (myomectomy/hysterectomy); branded ~5% of symptomatic
    # at ~$8K/yr blended. source: ACOG fibroid prevalence US ~5M symptomatic,
    # EU5 ~7M; ROW ~40M.
    "women_health.gyn_disorders.uterine_fibroids": {
        "us":  {"patientsK": 5000,   "wtpPct": 18, "priceK": 8},
        "eu":  {"patientsK": 7000,   "wtpPct": 12, "priceK": 4.5},
        "row": {"patientsK": 40000,  "wtpPct": 3,  "priceK": 1.2},
    },
    # Long-acting reversible contraception (LARC) implant: Nexplanon (Merck
    # etonogestrel ~$1.4B 2025) dominates implant subclass. Broader LARC also
    # includes IUDs (Mirena/Liletta/Skyla) -- this entry is the implant subclass
    # specifically. US ~3M Nexplanon users / ~70M reproductive-age women =
    # ~4% reach. Class peak ~$2B implant subclass globally.
    "women_health.contraception.larc_implant": {
        "us":  {"patientsK": 70000,  "wtpPct": 35, "priceK": 0.4},
        "eu":  {"patientsK": 80000,  "wtpPct": 28, "priceK": 0.25},
        "row": {"patientsK": 600000, "wtpPct": 8,  "priceK": 0.08},
    },
    # Differentiated thyroid cancer (DTC) / advanced refractory: Lenvima
    # (lenvatinib, Eisai+Merck ~$1B combined; thyroid ~25%), Cabometyx
    # (cabozantinib, Exelixis), sorafenib (Bayer Nexavar generic). US 50K
    # advanced thyroid cancer prevalent, ~10K need systemic Rx; EU 60K/12K;
    # ROW 150K/25K. Class peak ~$1.5B globally.
    "oncology.endocrine.thyroid_cancer": {
        "us":  {"patientsK": 10,    "wtpPct": 70, "priceK": 175},
        "eu":  {"patientsK": 12,    "wtpPct": 50, "priceK": 100},
        "row": {"patientsK": 25,    "wtpPct": 14, "priceK": 35},
    },
    # RSV mAb (peds long-acting): nirsevimab (Beyfortus, AZ/Sanofi ~$2B 2024),
    # clesrovimab (Enflonsia, Merck approved Jun 2025), motavizumab legacy.
    # Single-dose RSV season prophylaxis for <8mo + high-risk 8-19mo. US ~3.7M
    # birth cohort + ~1M high-risk older, EU ~4M, ROW ~120M (concentrated peds).
    # Class peak ~$5-7B at full coverage. Adult RSV vaccines (Arexvy GSK, Abrysvo
    # Pfizer, mResvia Moderna) are in vaccines.rsv_adult separately.
    # source: CDC ACIP RSV peds guidelines; AZ/Sanofi + Merck 10-Ks.
    "infectious_disease.vaccines.rsv": {
        "us":  {"patientsK": 4500,   "wtpPct": 70, "priceK": 0.5},
        "eu":  {"patientsK": 4500,   "wtpPct": 55, "priceK": 0.32},
        "row": {"patientsK": 120000, "wtpPct": 12, "priceK": 0.1},
    },

    # =====================================================================
    # OPHTHALMOLOGY - ANTERIOR & NEURO
    # =====================================================================
    "ophthalmology.anterior_neuro.deb_ocular": {
        "us":  {"patientsK": 3, "wtpPct": 55, "priceK": 350},
        "eu":  {"patientsK": 4, "wtpPct": 30, "priceK": 230},
        "row": {"patientsK": 1, "wtpPct": 10, "priceK": 100},
    },
    # source: US DED prevalence ~16M (AAO + NEI estimates) but the branded
    # specialty market (Restasis $0.4B declining + Xiidra $0.5B + Tyrvaya $0.3B
    # + Eysuvis + Miebo) addresses only the moderate-severe ~3M who fail OTC
    # tears. Total branded class ~$3B today, peak $5-6B with new entrants
    # (licaminlimab Ph3, varenicline-N reformulations). Prior US TAM 16M x 40%
    # x $7K = $45B treated entire DED population as buying branded scripts at
    # WAC -- ~12x off. Generic OTC artificial tears + cyclosporine generic
    # carry the bulk of patients at $20-100/yr OOP.
    "ophthalmology.anterior_neuro.dry_eye": {
        "us":  {"patientsK": 3000,  "wtpPct": 30, "priceK": 4},
        "eu":  {"patientsK": 4000,  "wtpPct": 18, "priceK": 2},
        "row": {"patientsK": 20000, "wtpPct": 5,  "priceK": 0.5},
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
    # source: US active moderate-severe TED ~50K (Tepezza-addressable per
    # Horizon/Amgen IR); EU5 ~70K; ROW ~150K. IGF-1R class is genuinely premium
    # priced (Tepezza WAC ~$460K per 8-infusion course; veligrotug similar).
    # Tepezza ~$2B today, peak forecast $3-4B; veligrotug + elegrobart-SC
    # entering 2026-27 -> total class peak $5-8B globally. Prior US TAM 50K
    # x 65% x $450K assumed nearly all active TED on Tepezza at full WAC --
    # ~3x off given net realization (PBM rebates + course-not-chronic).
    "ophthalmology.anterior_neuro.ted": {
        "us":  {"patientsK": 50,  "wtpPct": 50, "priceK": 250},
        "eu":  {"patientsK": 70,  "wtpPct": 30, "priceK": 150},
        "row": {"patientsK": 100, "wtpPct": 10, "priceK": 50},
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
    # source: ADOA prevalence ~1:25K general (NIH GARD, OMIM 165500); higher in
    # Denmark ~1:10K due to OPA1 founder mutation (Yu-Wai-Man et al., Brain
    # 2010). 65-90% of ADOA caused by OPA1 haploinsufficiency. US diagnosed
    # ~13K, EU5+UK ~25K (Danish/Northern European founder boost), ROW ~30K
    # (most undiagnosed in LMICs). No approved disease-modifying therapy.
    # Pricing pegs to ASO orphan pediatric/genetic precedent (Spinraza $750K
    # yr1 / $375K maint; Qalsody $190K). Stoke STK-002 first-in-class P1 OSPREY.
    "ophthalmology.optic_nerve.adoa": {
        "us":  {"patientsK": 13, "wtpPct": 55, "priceK": 400},
        "eu":  {"patientsK": 25, "wtpPct": 40, "priceK": 250},
        "row": {"patientsK": 30, "wtpPct": 15, "priceK": 100},
    },
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
    # source: GINA 2024 ~5-10% of asthmatics are severe; US biologic-eligible
    # pool ~500K (CDC/GBD), EU5 ~600K, ROW ~3M via specialty channels. Blended
    # biologic net price ~$20-25K post-rebate (WAC $35-40K). Global addressable
    # TAM ~$17B aligns with current branded biologic spend (Xolair + Fasenra +
    # Nucala + Tezspire + Dupixent-asthma = ~$12-15B). Prior values (2.5M US,
    # 25M ROW) conflated all asthmatics with severe biologic-eligible -- 10x off.
    "respiratory.inflammatory.asthma_severe": {
        "us":  {"patientsK": 500,   "wtpPct": 55, "priceK": 35},
        "eu":  {"patientsK": 600,   "wtpPct": 40, "priceK": 20},
        "row": {"patientsK": 3000,  "wtpPct": 12, "priceK": 8},
    },
    # source: GOLD 2024 ~16M diagnosed US COPD, ~22M EU, ~350M global. Branded
    # market dominated by triple inhalers (Trelegy/Breztri/Anoro ~$6B US) with
    # emerging biologic segment (Dupixent-COPD, ensifentrine). Blended inhaler
    # +biologic pricing ~$10-12K US. Global addressable TAM ~$25B matches
    # combined inhaled+biologic spend. Prior values ($40K priceK, full 3M US)
    # assumed uniform biologic pricing for all COPD which is not the franchise
    # structure -- ~4x off on US, ~6x off on EU.
    "respiratory.inflammatory.copd": {
        "us":  {"patientsK": 2500,  "wtpPct": 45, "priceK": 12},
        "eu":  {"patientsK": 3500,  "wtpPct": 30, "priceK": 7},
        "row": {"patientsK": 25000, "wtpPct": 10, "priceK": 1.5},
    },
    # source: NEI prevalence ~250K US RVO; ~280K EU; ROW per WHO Vision 2020
    "ophthalmology.retina.rvo": {
        "us":  {"patientsK": 250,  "wtpPct": 60, "priceK": 12},
        "eu":  {"patientsK": 280,  "wtpPct": 45, "priceK": 7},
        "row": {"patientsK": 600,  "wtpPct": 8,  "priceK": 2},
    },
    # source: Sanofi/REGN CRSwNP biologic-eligible severe pop estimates ~750K US;
    # Dupixent CRSwNP WAC ~$35K/yr
    "respiratory.inflammatory.crswnp": {
        "us":  {"patientsK": 750,  "wtpPct": 50, "priceK": 35},
        "eu":  {"patientsK": 900,  "wtpPct": 35, "priceK": 20},
        "row": {"patientsK": 3000, "wtpPct": 8,  "priceK": 5},
    },

    # ------------------------------------------------------------
    # NEPHROLOGY - SUPPORTIVE / DIALYSIS-ADJACENT
    # ------------------------------------------------------------
    # General CKD (chronic kidney disease, stages 3-5 non-dialysis): ~37M US
    # CKD prevalence; ~15M Stage 3-4 (treatable with disease-modifying agents).
    # Branded class: SGLT2i for CKD (Farxiga DAPA-CKD 2020, Jardiance
    # EMPA-KIDNEY 2022), MRA finerenone (Bayer Kerendia FIDELIO/FIGARO),
    # roxadustat (FibroGen/AZ HIF-PHI), Tezspire CKD pipeline, ziltivekimab
    # ZEUS pipeline. Class peak ~$15-20B with SGLT2 + MRA + new entrants.
    # Distinct from dialysis-specific phosphate_binder + cardiorenal_inflammation.
    "nephrology.ckd.disease_modifying": {
        "us":  {"patientsK": 15000, "wtpPct": 30, "priceK": 5},
        "eu":  {"patientsK": 18000, "wtpPct": 22, "priceK": 3},
        "row": {"patientsK": 80000, "wtpPct": 7,  "priceK": 1.2},
    },
    # Phosphate binders for ESRD/CKD-MBD: ~600K US dialysis pts; class:
    # Renagel/Renvela (sevelamer Sanofi ~$200M legacy), Velphoro
    # (sucroferric oxyhydroxide Vifor), Auryxia (ferric citrate Akebia),
    # Phoslyra (calcium acetate). Class peak ~$1B globally; mature, generic
    # pressure on sevelamer.
    "nephrology.ckd.phosphate_binder": {
        "us":  {"patientsK": 600,  "wtpPct": 60, "priceK": 4},
        "eu":  {"patientsK": 700,  "wtpPct": 45, "priceK": 2.5},
        "row": {"patientsK": 3000, "wtpPct": 12, "priceK": 0.8},
    },

    # ------------------------------------------------------------
    # NEPHROLOGY - CHRONIC KIDNEY DISEASE
    # ------------------------------------------------------------
    # Cardiorenal inflammation in CKD: high-CRP CKD patients with
    # atherosclerotic CV disease (ASCVD). Phase 3 ZEUS (Novo ziltivekimab,
    # anti-IL-6) primary endpoint = MACE. Patient population is CKD-defined
    # (Stage 3-4 + elevated hsCRP + prior CV event), specialty crosses
    # nephrology + cardiology. Class-defining if positive (canakinumab CANTOS
    # validated POC but never approved). ~5M US CKD with elevated hsCRP;
    # addressable subset (Stage 3-4 + hsCRP >2 mg/L + ASCVD) ~800K US.
    # Branded class peer pricing ~$10K/yr (PCSK9 analog given specialty +
    # chronic). source: Pradhan ASBMR 2024 hsCRP-CKD prevalence; CDC + USRDS
    # CKD registry; KDIGO 2024 cardiorenal guidelines.
    "nephrology.ckd.cardiorenal_inflammation": {
        "us":  {"patientsK": 800,  "wtpPct": 30, "priceK": 10},
        "eu":  {"patientsK": 1000, "wtpPct": 22, "priceK": 5},
        "row": {"patientsK": 3000, "wtpPct": 7,  "priceK": 1},
    },
    # source: SMA prevalence ~10K US, ~14K EU5, ~50K ROW (NIH 2024).
    # Branded class: Spinraza (Biogen ASO) ~$1.7B, Evrysdi (Roche oral) ~$1.5B,
    # Zolgensma (Novartis AAV9 GT) ~$1.2B. Net price ~$300K/yr blended
    # (Spinraza $750K Y1, Evrysdi $340K, Zolgensma one-shot $2.25M amortized).
    "musculoskeletal.neuromuscular.sma": {
        "us":  {"patientsK": 10,   "wtpPct": 75, "priceK": 350},
        "eu":  {"patientsK": 14,   "wtpPct": 60, "priceK": 220},
        "row": {"patientsK": 50,   "wtpPct": 18, "priceK": 80},
    },
    # source: non-infectious uveitis ~350K US (NEI 2024), ~500K EU5, ~3M ROW.
    # Branded class small (~$0.5-1B): Humira off-label, Yutiq implant, plus
    # emerging IL-6 inhibitors (vamikibart Roche Ph3). Most patients on
    # corticosteroids. Vision-threatening; blended branded $25K/yr.
    "ophthalmology.anterior_neuro.uveitis": {
        "us":  {"patientsK": 350,  "wtpPct": 35, "priceK": 25},
        "eu":  {"patientsK": 500,  "wtpPct": 22, "priceK": 14},
        "row": {"patientsK": 3000, "wtpPct": 6,  "priceK": 4},
    },
    # source: Acute ischemic stroke + STEMI thrombolysis. US AIS ~700K/yr,
    # tPA-treated ~10% (~70K/yr); EU similar. Branded Activase/TNKase (Roche),
    # generic alteplase. Net branded ~$5K/dose. Class small ~$1.5B globally.
    "cardio_metabolic.thrombosis.thrombolytic": {
        "us":  {"patientsK": 200,  "wtpPct": 90, "priceK": 18},
        "eu":  {"patientsK": 220,  "wtpPct": 70, "priceK": 11},
        "row": {"patientsK": 800,  "wtpPct": 22, "priceK": 5},
    },
    # source: Cystic fibrosis ~40K US (CFF Patient Registry 2024), ~50K EU5,
    # ~80K ROW. Branded class dominated by Vertex CFTR modulators (Trikafta
    # ~$10B) for ~90% of patients with eligible mutations. Adjuncts include
    # Pulmozyme (Roche dornase alfa), Tobi (inhaled tobramycin). Net branded
    # ~$320K/yr Trikafta; mucolytic adjuncts ~$13K/yr.
    "respiratory.genetic.cystic_fibrosis": {
        "us":  {"patientsK": 40,  "wtpPct": 80, "priceK": 280},
        "eu":  {"patientsK": 50,  "wtpPct": 60, "priceK": 170},
        "row": {"patientsK": 80,  "wtpPct": 18, "priceK": 60},
    },
    # Refractory chronic gout (uncontrolled hyperuricemia despite ULT):
    # ~50K US treated/yr, ~70K EU5, ~200K ROW. Class: Krystexxa (Amgen
    # pegloticase IV uricase ~$1.3B), febuxostat (generic). Branded
    # ~$30K/yr blended (Krystexxa premium-priced).
    "musculoskeletal.crystal_arthropathy.gout": {
        "us":  {"patientsK": 50,  "wtpPct": 65, "priceK": 30},
        "eu":  {"patientsK": 70,  "wtpPct": 45, "priceK": 18},
        "row": {"patientsK": 200, "wtpPct": 12, "priceK": 6},
    },
    # ANCA-associated vasculitis (GPA + MPA): ~50K US prevalent on tx,
    # ~70K EU5, ~200K ROW. Class: Tavneos (Amgen avacopan C5aR
    # antagonist ~$0.5B), rituximab (Roche/biosim). Net branded
    # ~$200K/yr orphan-priced.
    "nephrology.glomerular.aav_anca": {
        "us":  {"patientsK": 50,  "wtpPct": 60, "priceK": 200},
        "eu":  {"patientsK": 70,  "wtpPct": 42, "priceK": 120},
        "row": {"patientsK": 200, "wtpPct": 12, "priceK": 45},
    },
    # NMO spectrum disorder (NMOSD AQP4-IgG+): ~10K US prevalent, ~14K
    # EU5, ~80K ROW. Class: Uplizna (Amgen/Horizon inebilizumab anti-CD19
    # ~$650M), Soliris/Ultomiris (AZN anti-C5), Enspryng (Roche
    # anti-IL-6R). Net branded ~$300K/yr orphan-priced.
    "immunology.demyelinating.nmosd": {
        "us":  {"patientsK": 10,  "wtpPct": 75, "priceK": 300},
        "eu":  {"patientsK": 14,  "wtpPct": 55, "priceK": 180},
        "row": {"patientsK": 80,  "wtpPct": 18, "priceK": 70},
    },
    # Bone metastases SRE prevention in solid tumors with bone mets:
    # US ~600K prevalent population, ~800K EU5, ~3M ROW. Class: Xgeva
    # (Amgen denosumab ~$2B; same molecule as Prolia), zoledronic acid
    # generic. Net branded ~$25K/yr.
    "oncology.supportive_care.bone_metastases": {
        "us":  {"patientsK": 600,  "wtpPct": 60, "priceK": 25},
        "eu":  {"patientsK": 800,  "wtpPct": 45, "priceK": 14},
        "row": {"patientsK": 3000, "wtpPct": 12, "priceK": 5},
    },
    # B-cell acute lymphoblastic leukemia (B-ALL): pediatric + adult.
    # US ~6K new cases/yr, ~10K prevalent on treatment. EU ~12K, ROW ~80K.
    # Class: Blincyto (Amgen CD19xCD3 BiTE ~$1.6B), Kymriah (Novartis CD19
    # CAR-T pediatric/AYA), Besponsa (Pfizer CD22 ADC), Tecartus (Gilead
    # CD19 CAR-T adult). Net branded ~$200K/yr.
    "oncology.hematology.b_all": {
        "us":  {"patientsK": 10,  "wtpPct": 75, "priceK": 200},
        "eu":  {"patientsK": 12,  "wtpPct": 55, "priceK": 120},
        "row": {"patientsK": 80,  "wtpPct": 14, "priceK": 35},
    },
    # Chemo-induced neutropenia / febrile neutropenia prophylaxis: US
    # ~1.2M chemo-treated patients/yr, ~50% receive G-CSF support.
    # Class: Neulasta (Amgen pegfilgrastim long-acting), Neupogen
    # (filgrastim short-acting), biosim Pelgraz/Udenyca/Fulphila/
    # Ziextenzo. Net branded ~$8K/cycle.
    "oncology.supportive_care.neutropenia": {
        "us":  {"patientsK": 600,  "wtpPct": 70, "priceK": 8},
        "eu":  {"patientsK": 800,  "wtpPct": 50, "priceK": 5},
        "row": {"patientsK": 3000, "wtpPct": 12, "priceK": 1.5},
    },
    # Acute moderate-to-severe pain (post-surgical, dental, traumatic):
    # ~80M US procedures/yr generating moderate-to-severe acute pain
    # episodes; ~70M EU; ~300M ROW. Standard care: opioids (oxycodone,
    # hydrocodone -- addiction crisis driving non-opioid alternatives) +
    # NSAIDs (Toradol, ibuprofen) + acetaminophen. Branded class: Journavx
    # (Vertex suzetrigine NaV1.8, FDA Jan 2025 first non-opioid in 25 yrs)
    # ~$60M ramp 2025; emerging NaV1.8 class (Latigo LTG-001, SiteOne SOS).
    # Net branded ~$1.5K/episode (4-week course).
    "cns.pain.acute": {
        "us":  {"patientsK": 80000,  "wtpPct": 60, "priceK": 1.5},
        "eu":  {"patientsK": 70000,  "wtpPct": 45, "priceK": 0.9},
        "row": {"patientsK": 300000, "wtpPct": 12, "priceK": 0.3},
    },
    # ADPKD (autosomal dominant polycystic kidney disease): ~140K US, 200K
    # EU5, ~1M ROW prevalent on tx. Branded class: Jynarque (Otsuka
    # tolvaptan V2 antagonist ~$1.5B, hepatotoxicity REMS), VX-407 (Vertex
    # PC1 modulator Ph2). Net branded ~$50K/yr.
    "nephrology.glomerular.adpkd": {
        "us":  {"patientsK": 140,   "wtpPct": 50, "priceK": 50},
        "eu":  {"patientsK": 200,   "wtpPct": 35, "priceK": 30},
        "row": {"patientsK": 1000,  "wtpPct": 10, "priceK": 10},
    },
    # APOL1-mediated kidney disease (AMKD): proteinuric CKD in APOL1 G1/G2
    # high-risk genotype carriers (~13% of Black Americans, ~1.5M US).
    # Includes FSGS + collapsing glomerulopathy + HIV-associated nephropathy
    # phenotypes. Branded class emerging: inaxaplin (Vertex VX-147 first-
    # in-class APOL1 inhibitor, AMPLITUDE Ph2/3). Net branded peak ~$60K/yr.
    "nephrology.glomerular.amkd": {
        "us":  {"patientsK": 100,   "wtpPct": 55, "priceK": 60},
        "eu":  {"patientsK": 50,    "wtpPct": 38, "priceK": 35},
        "row": {"patientsK": 800,   "wtpPct": 12, "priceK": 12},
    },
    # Friedreich's ataxia (FA): rare autosomal recessive frataxin (FXN)
    # deficiency; progressive ataxia + cardiomyopathy. ~5K US, ~7K EU5,
    # ~25K ROW prevalent. Class: Skyclarys (Vertex/Reata omaveloxolone
    # Nrf2 activator ~$165M, FDA approval Feb 2023; only approved drug),
    # gene therapy + RNA pipeline (Lexeo LX2006, ELONA). Net branded
    # ~$370K/yr orphan-priced.
    "cns.neurodegeneration.friedreich": {
        "us":  {"patientsK": 5,    "wtpPct": 80, "priceK": 370},
        "eu":  {"patientsK": 7,    "wtpPct": 60, "priceK": 230},
        "row": {"patientsK": 25,   "wtpPct": 18, "priceK": 80},
    },
    # Herpes zoster (shingles) vaccine: adult >=50 ACIP-recommended.
    # US ~120M eligible (lifetime coverage ~50-60%), EU 200M, ROW 800M.
    # Class: Shingrix (GSK adjuvanted recombinant gE ~$4.5B globally),
    # Zostavax (Merck live attenuated, discontinued 2020). Net branded
    # ~$0.4/dose blended (2-dose series). Class peak $5-6B at full coverage.
    "infectious_disease.vaccines.zoster": {
        "us":  {"patientsK": 120000, "wtpPct": 60, "priceK": 0.40},
        "eu":  {"patientsK": 200000, "wtpPct": 45, "priceK": 0.30},
        "row": {"patientsK": 800000, "wtpPct": 12, "priceK": 0.10},
    },
    # Refractory chronic cough (RCC): unexplained or cough refractory to
    # treatment, >8 weeks duration. ~10M US affected, ~14M EU, ~50M ROW.
    # No approved therapies (FDA rejected gefapixant/Lyfnua Merck 2024).
    # Branded class emerging: Camlipixant (GSK P2X3 antagonist Ph3 CALM-1/2).
    # Net branded peak ~$3K/yr.
    "respiratory.inflammatory.cough_chronic": {
        "us":  {"patientsK": 10000, "wtpPct": 35, "priceK": 3},
        "eu":  {"patientsK": 14000, "wtpPct": 25, "priceK": 1.8},
        "row": {"patientsK": 50000, "wtpPct": 8,  "priceK": 0.5},
    },
    # Lupus nephritis (LN): kidney manifestation of SLE. ~100K US
    # prevalent (40-60% of SLE patients develop LN), ~120K EU5, ~600K
    # ROW. Branded class: Benlysta (GSK belimumab BLISS-LN ~$300M LN
    # share), Lupkynis (Aurinia voclosporin calcineurin inhibitor
    # ~$200M), Saphnelo (AZN anifrolumab Ph3 ongoing LN), MMF/cyclo
    # (off-label generics standard). Net branded ~$45K/yr.
    "nephrology.glomerular.lupus_nephritis": {
        "us":  {"patientsK": 100,  "wtpPct": 60, "priceK": 45},
        "eu":  {"patientsK": 120,  "wtpPct": 42, "priceK": 27},
        "row": {"patientsK": 600,  "wtpPct": 12, "priceK": 9},
    },
    # Dengue vaccine: dengue is the most rapidly spreading mosquito-borne
    # viral disease. Endemic countries (LATAM, SE Asia, Africa) ~3.9B
    # at-risk population; ~400M infections/yr; ~100M symptomatic. Class:
    # Qdenga (Takeda TAK-003 tetravalent live-attenuated ~$330M, EU + 30
    # endemic countries approval; FDA filing pending), Dengvaxia (Sanofi
    # CYD-TDV seroprevalence-restricted ~$50M residual). Net branded
    # ~$50/dose blended.
    "infectious_disease.vaccines.dengue": {
        "us":  {"patientsK": 200,    "wtpPct": 35, "priceK": 0.20},
        "eu":  {"patientsK": 500,    "wtpPct": 30, "priceK": 0.15},
        "row": {"patientsK": 100000, "wtpPct": 25, "priceK": 0.05},
    },
    # Oral contraceptive pills (OCPs): combined estrogen-progestin or
    # progestin-only daily pills. US ~15M users, EU ~30M, ROW ~150M.
    # Class: Yaz/Yasmin franchise (Bayer drospirenone + estradiol),
    # Lo Loestrin (Allergan), Slynd (progestin-only), Mylan/Teva generics.
    # Class globally ~$5B with branded share ~$1B.
    "women_health.contraception.ocp": {
        "us":  {"patientsK": 15000,  "wtpPct": 35, "priceK": 0.4},
        "eu":  {"patientsK": 30000,  "wtpPct": 30, "priceK": 0.25},
        "row": {"patientsK": 150000, "wtpPct": 18, "priceK": 0.08},
    },
    # Antiplatelet therapy (CV prophylaxis post-MI/stroke + DAPT):
    # blocks platelet aggregation. US ~30M users (low-dose ASA + DAPT),
    # EU ~50M, ROW ~200M. Class: low-dose Aspirin (Bayer Cardio brand
    # ROW + generics), Plavix (Sanofi clopidogrel generic), Brilinta
    # (AZN ticagrelor branded ~$1.5B), Effient (Lilly prasugrel generic).
    # Net branded blended ~$0.3K/yr.
    "cardio_metabolic.thrombosis.antiplatelet": {
        "us":  {"patientsK": 30000,  "wtpPct": 25, "priceK": 0.4},
        "eu":  {"patientsK": 50000,  "wtpPct": 20, "priceK": 0.25},
        "row": {"patientsK": 200000, "wtpPct": 12, "priceK": 0.08},
    },
    # IVF / Assisted Reproductive Technology (ART): gonadotropin-stimulated
    # ovulation + IVF cycles. US ~400K cycles/yr, EU ~1M cycles, ROW ~3M.
    # Class: Merck KGaA Gonal-f (rFSH ~$1.1B) + Pergoveris + Cetrotide +
    # Ovitrelle; Ferring Bemfola/Rekovelle/Menopur; Theramex generics.
    # Class globally ~$3-4B branded. Net branded ~$4-5K/cycle.
    "women_health.fertility.ivf": {
        # Bumped patientsK (gonadotropin-treated cycles, not just women)
        # and price to reflect actual class size (~$5-6B globally branded).
        "us":  {"patientsK": 400,   "wtpPct": 70, "priceK": 6},
        "eu":  {"patientsK": 1000,  "wtpPct": 55, "priceK": 4},
        "row": {"patientsK": 3000,  "wtpPct": 18, "priceK": 1.5},
    },
    # CKD-associated pruritus (CKD-aP, uremic itch): chronic itch in
    # dialysis patients. ~400K US dialysis patients, ~30-50% with
    # moderate-severe pruritus = ~150K eligible. EU ~200K, ROW ~1M.
    # Class: Korsuva (CSL Vifor difelikefalin kappa-opioid agonist
    # ~$50M, KALM-1/-2 Ph3). Net branded ~$12K/yr.
    "nephrology.ckd.pruritus": {
        "us":  {"patientsK": 150,   "wtpPct": 55, "priceK": 12},
        "eu":  {"patientsK": 200,   "wtpPct": 38, "priceK": 7},
        "row": {"patientsK": 1000,  "wtpPct": 10, "priceK": 2.5},
    },
    # CKD anemia (EPO-stimulating agents + iron + HIF-PHI): chronic anemia
    # in dialysis + non-dialysis CKD. US ~600K dialysis + ~3M non-dialysis
    # CKD with anemia, EU ~800K, ROW ~3M. Class: Aranesp (Amgen darbepoetin
    # ~$1.4B), Mircera (CSL Vifor CERA EPO ~$200M), Procrit/Eprex (legacy),
    # Pelmeg/Udenyca biosims, HIF-PHI (Vafseo/vadadustat AKBA, Jesduvroq
    # GSK daprodustat, Roxadustat AZN/Astellas). Net branded ~$18K/yr.
    "nephrology.ckd.anemia": {
        "us":  {"patientsK": 600,   "wtpPct": 65, "priceK": 18},
        "eu":  {"patientsK": 800,   "wtpPct": 50, "priceK": 11},
        "row": {"patientsK": 3000,  "wtpPct": 12, "priceK": 4},
    },
    # Anticoagulant reversal (warfarin/DOAC bleeding emergencies):
    # ~150K US emergency reversal events/yr, ~200K EU, ~600K ROW. Class:
    # Kcentra/Beriplex (CSL 4F-PCC ~$700M), Andexxa (Astellas/Portola
    # andexanet alfa Factor Xa-specific reversal ~$200M), Praxbind
    # (BI idarucizumab anti-dabigatran ~$50M). Net branded ~$5-15K/event.
    "cardio_metabolic.thrombosis.reversal": {
        "us":  {"patientsK": 150,   "wtpPct": 80, "priceK": 5},
        "eu":  {"patientsK": 200,   "wtpPct": 60, "priceK": 3},
        "row": {"patientsK": 600,   "wtpPct": 18, "priceK": 1.5},
    },
    # Overactive bladder (OAB): chronic urinary urgency/frequency.
    # ~33M US adults (mostly women), ~50M EU, ~200M ROW. Branded class:
    # Myrbetriq/Betmiga (Astellas mirabegron beta-3 ~$2B), Vesicare
    # (Astellas solifenacin generic), Detrol (generic), Toviaz (Pfizer
    # fesoterodine), vibegron (Sumitomo Gemtesa), oxybutynin (generic).
    # Class branded ~$3-4B; generic dominant. Net branded ~$1K/yr.
    "urology.lower_tract.oab": {
        "us":  {"patientsK": 33000,  "wtpPct": 25, "priceK": 1.0},
        "eu":  {"patientsK": 50000,  "wtpPct": 18, "priceK": 0.6},
        "row": {"patientsK": 200000, "wtpPct": 8,  "priceK": 0.2},
    },
    # Cardiac stress imaging pharmacological agents: used during myocardial
    # perfusion imaging (MPI) for patients unable to exercise. US ~5M MPI
    # studies/yr, ~30% pharmacological stress. EU ~7M, ROW ~25M. Class:
    # Lexiscan (Astellas regadenoson A2A agonist ~$300M), Adenoscan
    # (adenosine generic), dobutamine (generic). Net branded ~$0.5K/study.
    "cardio_metabolic.imaging.cardiac_stress": {
        "us":  {"patientsK": 1500,   "wtpPct": 70, "priceK": 0.5},
        "eu":  {"patientsK": 2000,   "wtpPct": 50, "priceK": 0.3},
        "row": {"patientsK": 8000,   "wtpPct": 12, "priceK": 0.1},
    },
    # Invasive fungal disease (IFD): hospital antifungal therapy for
    # aspergillosis, candidiasis, mucormycosis, cryptococcosis. US ~150K
    # IFD episodes/yr, EU ~200K, ROW ~800K. Class: Cresemba (Astellas/
    # Pfizer/Merck KGaA isavuconazole triazole), Mycamine (Astellas
    # micafungin echinocandin), Cancidas (caspofungin Merck generic),
    # Eraxis (anidulafungin Pfizer), voriconazole/posaconazole (generics).
    # Net branded ~$15K/episode (1-3 wk IV course).
    "infectious_disease.anti_infective.invasive_fungal": {
        "us":  {"patientsK": 150,   "wtpPct": 70, "priceK": 15},
        "eu":  {"patientsK": 200,   "wtpPct": 50, "priceK": 9},
        "row": {"patientsK": 800,   "wtpPct": 14, "priceK": 3},
    },
    # Blastic plasmacytoid dendritic cell neoplasm (BPDCN): ultra-rare
    # CD123-driven myeloid-adjacent neoplasm; ~1K US, ~1.5K EU, ~5K ROW.
    # Class: Elzonris (Stemline tagraxofusp first-in-class CD123
    # diphtheria toxin fusion), Pivekimab sunirine (Astellas/AbbVie/
    # ImmunoGen CD123 ADC Ph2/3). Net branded ~$280K/yr orphan-priced.
    "oncology.hematology.bpdcn": {
        "us":  {"patientsK": 1,    "wtpPct": 70, "priceK": 280},
        "eu":  {"patientsK": 1.5,  "wtpPct": 50, "priceK": 170},
        "row": {"patientsK": 5,    "wtpPct": 14, "priceK": 60},
    },
    # IgA nephropathy: most common primary glomerulonephritis. ~150K US
    # diagnosed proteinuric, ~150K EU5, ~1.5M ROW (Asia high). Class:
    # Tarpeyo (Calliditas budesonide ~00M), atrasentan (Novartis ETA),
    # Filspari (Travere sparsentan ETA+ARB), Fabhalta (Novartis Factor B),
    # Povetacicept (Vertex BAFF+APRIL Ph3), Felzartamab (Biogen anti-CD38).
    "nephrology.glomerular.iga_nephropathy": {
        "us":  {"patientsK": 130,  "wtpPct": 50, "priceK": 65},
        "eu":  {"patientsK": 150,  "wtpPct": 35, "priceK": 32},
        "row": {"patientsK": 1500, "wtpPct": 10, "priceK": 6},
    },
    # Focal segmental glomerulosclerosis (FSGS): ~40K US, ~45K EU,
    # ~200K ROW. Class: Filspari (Travere sparsentan dual ETA+ARB),
    # Mircera/EPO supportive, off-label tac/rituximab. Net branded ~0K/yr.
    "nephrology.glomerular.fsgs": {
        "us":  {"patientsK": 40,   "wtpPct": 45, "priceK": 90},
        "eu":  {"patientsK": 45,   "wtpPct": 30, "priceK": 45},
        "row": {"patientsK": 200,  "wtpPct": 8,  "priceK": 8},
    },
    # Primary membranous nephropathy (pMN): ~30K US, ~50K EU, ~150K ROW.
    # Anti-PLA2R-driven autoimmune kidney. Class: rituximab off-label
    # standard, emerging anti-CD20/CD19/APRIL inhibitors (povetacicept,
    # budoprutug, felzartamab). Net branded ~0K/yr.
    "nephrology.glomerular.pmn": {
        "us":  {"patientsK": 30,  "wtpPct": 60, "priceK": 90},
        "eu":  {"patientsK": 50,  "wtpPct": 40, "priceK": 50},
        "row": {"patientsK": 150, "wtpPct": 8,  "priceK": 15},
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
    "infectious_disease.vaccines.hpv": 65,
    "infectious_disease.vaccines.pneumococcal": 55,
    "infectious_disease.vaccines.rsv": 35,
    "infectious_disease.vaccines.rotavirus": 65,
    "infectious_disease.vaccines.mmr_varicella": 70,
    "infectious_disease.anti_infective.bacterial_hospital": 25,
    "infectious_disease.anti_infective.cmv": 50,
    "perioperative.anesthesia.nmb_reversal": 30,
    "women_health.contraception.larc_implant": 18,
    "women_health.menopause.hrt": 10,
    "women_health.gyn_disorders.endometriosis": 8,
    "women_health.gyn_disorders.uterine_fibroids": 8,
    "oncology.endocrine.thyroid_cancer": 35,
    "infectious_disease.vaccines.covid": 8,
    "infectious_disease.anti_infective.covid_treatment": 12,
    "infectious_disease.vaccines.rsv_adult": 25,
    "infectious_disease.vaccines.influenza": 38,
    "infectious_disease.vaccines.pertussis": 45,
    "infectious_disease.vaccines.polio_hib": 75,
    "infectious_disease.vaccines.meningococcal": 55,
    "nephrology.ckd.phosphate_binder": 25,
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
    "ophthalmology.optic_nerve.adoa": 25,
    "ophthalmology.optic_nerve.lhon": 20,
    "ophthalmology.optic_nerve.nmosd": 40,
    "respiratory.inflammatory.asthma_severe": 25,
    "respiratory.inflammatory.copd": 10,
    "ophthalmology.retina.rvo": 35,
    "respiratory.inflammatory.crswnp": 25,
    "nephrology.ckd.cardiorenal_inflammation": 12,
    "nephrology.ckd.disease_modifying": 10,
    "musculoskeletal.neuromuscular.sma": 55,
    "ophthalmology.anterior_neuro.uveitis": 18,
    "cardio_metabolic.thrombosis.thrombolytic": 70,
    "respiratory.genetic.cystic_fibrosis": 80,
    "musculoskeletal.crystal_arthropathy.gout": 35,
    "nephrology.glomerular.aav_anca": 45,
    "immunology.demyelinating.nmosd": 50,
    "oncology.supportive_care.bone_metastases": 35,
    "oncology.hematology.b_all": 70,
    "oncology.supportive_care.neutropenia": 50,
    "cns.pain.acute": 30,
    "nephrology.glomerular.adpkd": 28,
    "nephrology.glomerular.amkd": 25,
    "cns.neurodegeneration.friedreich": 50,
    "infectious_disease.vaccines.zoster": 35,
    "respiratory.inflammatory.cough_chronic": 25,
    "nephrology.glomerular.lupus_nephritis": 40,
    "infectious_disease.vaccines.dengue": 22,
    "women_health.contraception.ocp": 25,
    "cardio_metabolic.thrombosis.antiplatelet": 20,
    "women_health.fertility.ivf": 35,
    "nephrology.ckd.pruritus": 25,
    "nephrology.ckd.anemia": 60,
    "cardio_metabolic.thrombosis.reversal": 70,
    "urology.lower_tract.oab": 35,
    "cardio_metabolic.imaging.cardiac_stress": 30,
    "infectious_disease.anti_infective.invasive_fungal": 50,
    "oncology.hematology.bpdcn": 65,
    "nephrology.glomerular.iga_nephropathy": 50,
    "nephrology.glomerular.fsgs": 25,
    "nephrology.glomerular.pmn": 35,
}
