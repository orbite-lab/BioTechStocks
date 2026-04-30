# -*- coding: utf-8 -*-
"""
Authoritative slider values for immunology and dermatology disease areas.
Parsed from scripts/tooltips_immuno_derm.py.

patientsK: treated/eligible count in thousands (M converted to K).
           For aesthetics, procedures/yr used as patientsK.
wtpPct:    first "~XX%" market-level willingness-to-pay figure.
priceK:    blended annualized price per patient, in USD thousands
           (for aesthetics, per-syringe/session price in $K).
"""

REGIONS = {
    # ============================================================
    # IMMUNOLOGY - AUTOIMMUNE
    # ============================================================
    "immunology.autoimmune.fsgs": {
        "us":  {"patientsK": 40,   "wtpPct": 45, "priceK": 90},
        "eu":  {"patientsK": 45,   "wtpPct": 30, "priceK": 45},
        "row": {"patientsK": 200,  "wtpPct": 8,  "priceK": 8},
    },
    "immunology.autoimmune.hereditary_angioedema": {
        "us":  {"patientsK": 7,    "wtpPct": 75, "priceK": 450},
        "eu":  {"patientsK": 10,   "wtpPct": 55, "priceK": 280},
        "row": {"patientsK": 20,   "wtpPct": 15, "priceK": 100},
    },
    "immunology.autoimmune.iga_nephropathy": {
        "us":  {"patientsK": 130,  "wtpPct": 50, "priceK": 65},
        "eu":  {"patientsK": 150,  "wtpPct": 35, "priceK": 32},
        "row": {"patientsK": 1500, "wtpPct": 10, "priceK": 6},
    },
    "immunology.autoimmune.sjogrens": {
        "us":  {"patientsK": 1000,  "wtpPct": 25, "priceK": 8},
        "eu":  {"patientsK": 2000,  "wtpPct": 18, "priceK": 4},
        "row": {"patientsK": 15000, "wtpPct": 5,  "priceK": 1},
    },
    "immunology.autoimmune.sle": {
        "us":  {"patientsK": 300,  "wtpPct": 55, "priceK": 45},
        "eu":  {"patientsK": 350,  "wtpPct": 38, "priceK": 22},
        "row": {"patientsK": 4000, "wtpPct": 10, "priceK": 5},
    },
    # source: pMN (primary membranous nephropathy) ~30K US diagnosed; ~50K EU5;
    # ~150K ROW. Anti-PLA2R-driven autoimmune kidney disease. Standard care
    # rituximab off-label + cyclophosphamide. Emerging branded class (anti-CD19
    # / anti-CD20 / APRIL inhibitors); peak class TAM ~$2-3B globally with
    # first-line label. Orphan-priced specialty nephrology channel.
    "immunology.autoimmune.pmn": {
        "us":  {"patientsK": 30,  "wtpPct": 60, "priceK": 90},
        "eu":  {"patientsK": 50,  "wtpPct": 40, "priceK": 50},
        "row": {"patientsK": 150, "wtpPct": 8,  "priceK": 15},
    },

    # ============================================================
    # IMMUNOLOGY - INFLAMMATORY GI
    # ============================================================
    # source: US Crohn's ~800K diagnosed (CCFA) but biologic-treated ~50%.
    # Branded class: Stelara ~$4B Crohn's + Skyrizi-Crohn's ~$4B + Entyvio
    # (both UC+Crohn's) ~$5B + Humira-Crohn's ~$2B + Rinvoq + Tremfya =
    # ~$18-20B current global, peak $25B post-Humira-biosimilar. Net price
    # ~$25K/yr after PBM rebates (WAC $50-65K). Prior TAM $53B at $62K WAC
    # uniform = ~3x off net economics.
    "immunology.inflammatory_gi.crohns": {
        "us":  {"patientsK": 800,  "wtpPct": 55, "priceK": 25},
        "eu":  {"patientsK": 1500, "wtpPct": 35, "priceK": 15},
        "row": {"patientsK": 5000, "wtpPct": 10, "priceK": 4},
    },
    # source: US UC ~1M diagnosed (CCFA), biologic-treated ~40%. Same branded
    # franchises as Crohn's (Entyvio + Stelara + Skyrizi-UC + Humira + Rinvoq
    # + Tremfya + Zeposia + Velsipity), totalling ~$15-18B current global,
    # peak ~$20B. Same $25K net pricing pattern. Prior $46B inflated 3x.
    "immunology.inflammatory_gi.ulcerative_colitis": {
        "us":  {"patientsK": 1000, "wtpPct": 50, "priceK": 20},
        "eu":  {"patientsK": 1500, "wtpPct": 30, "priceK": 12},
        "row": {"patientsK": 5000, "wtpPct": 8,  "priceK": 3},
    },
    # Eosinophilic esophagitis (EoE): chronic Th2-driven esophageal
    # inflammation. US ~150K diagnosed (CDC 2024), ~250K EU5, ~1M ROW.
    # Class: Dupixent (SNY/REGN IL-4/13, approved EoE 2022 ~$1.5B EoE
    # share globally), cendakimab (BMS anti-IL-13 Ph3 filed 2025),
    # tezepelumab (AZN/Amgen anti-TSLP Ph2 EoE), corticosteroids
    # standard. Net branded ~$35K/yr.
    "immunology.inflammatory_gi.eoe": {
        "us":  {"patientsK": 150,  "wtpPct": 50, "priceK": 35},
        "eu":  {"patientsK": 250,  "wtpPct": 35, "priceK": 22},
        "row": {"patientsK": 1000, "wtpPct": 8,  "priceK": 8},
    },

    # ============================================================
    # IMMUNOLOGY - INFLAMMATORY SYSTEMIC
    # ============================================================
    # source: US RA ~1.5M diagnosed (ACR), biologic-treated ~50%. Branded
    # class post-Humira-biosimilar: Humira-RA ~$5B (declining) + Rinvoq-RA
    # ~$3B + Cimzia + Actemra + Orencia + Olumiant + Xeljanz = ~$25-30B today
    # global. Class peak ~$30-35B as Humira completes its biosimilar slide
    # offset by Rinvoq + new oral entries. Net ~$20K/yr post-rebate. Prior
    # $98B at $55K WAC across full population was ~3x off net economics.
    # Psoriatic arthritis (PsA): inflammatory arthritis associated with psoriasis.
    # ~1.5M US prevalent (~30% of psoriasis pts develop PsA), ~2M EU, ~10M ROW.
    # Class: Stelara/Tremfya (J&J IL-12/23/IL-23), Cosentyx/Bimzelx (Novartis/UCB
    # IL-17), Skyrizi (AbbVie IL-23), Rinvoq/Olumiant (JAK), TNFi legacy. Class
    # peak ~$10-12B globally. source: NPF; J&J + AbbVie + Novartis 10-Ks.
    "immunology.inflammatory_systemic.psoriatic_arthritis": {
        "us":  {"patientsK": 1500,  "wtpPct": 50, "priceK": 50},
        "eu":  {"patientsK": 2000,  "wtpPct": 35, "priceK": 30},
        "row": {"patientsK": 10000, "wtpPct": 8,  "priceK": 10},
    },
    # Giant cell arteritis (GCA) + Polymyalgia rheumatica (PMR):
    # GCA US ~228K prevalent, PMR ~711K (NIH). Mostly elderly women.
    # Class: Actemra (tocilizumab approved 2017 GCA), corticosteroids
    # standard, Cosentyx Ph3 PMR positive 2025 (submission H1 2026).
    # Net branded blended ~$30K/yr.
    "immunology.inflammatory_systemic.gca_pmr": {
        "us":  {"patientsK": 940,  "wtpPct": 25, "priceK": 30},
        "eu":  {"patientsK": 1300, "wtpPct": 18, "priceK": 18},
        "row": {"patientsK": 4000, "wtpPct": 6,  "priceK": 7},
    },
    # Periodic fever syndromes (CAPS, TRAPS, HIDS/MKD, FMF) + Still's
    # disease (sJIA + AOSD) + Behcet. US ~30K biologics-eligible, EU 40K,
    # ROW 200K (FMF higher in Mediterranean). Class: Ilaris (canakinumab
    # anti-IL-1b Novartis ~$1.9B), Kineret (anakinra Sobi), Arcalyst
    # (rilonacept Kiniksa). Net branded ~$220K/yr orphan-priced.
    "immunology.autoinflammatory.periodic_fever": {
        "us":  {"patientsK": 30,   "wtpPct": 70, "priceK": 220},
        "eu":  {"patientsK": 40,   "wtpPct": 55, "priceK": 130},
        "row": {"patientsK": 200,  "wtpPct": 12, "priceK": 50},
    },
    # Eosinophilic granulomatosis with polyangiitis (EGPA, formerly
    # Churg-Strauss): rare ANCA-associated vasculitis with eosinophilic
    # infiltration. ~5K US prevalent, ~7K EU5, ~30K ROW. Branded class:
    # Nucala (GSK mepolizumab anti-IL-5 first-in-class EGPA approval 2017
    # ~$300M EGPA share), Tezspire (AZN/Amgen anti-TSLP Ph3 EGPA
    # ongoing). Net branded ~$45K/yr.
    "immunology.autoimmune.egpa": {
        # Bumped for actual class size: Nucala EGPA share alone ~$300-400M
        # supports class TAM ~$1B with broader treated population.
        "us":  {"patientsK": 12,  "wtpPct": 75, "priceK": 60},
        "eu":  {"patientsK": 15,  "wtpPct": 55, "priceK": 35},
        "row": {"patientsK": 60,  "wtpPct": 14, "priceK": 12},
    },
    # Primary immunodeficiency (PI/PIDD): X-linked agammaglobulinemia,
    # CVID, hyper-IgM, severe combined immunodeficiency, etc. ~250K US
    # diagnosed (Jeffrey Modell Foundation), ~350K EU5, ~2M ROW. Class:
    # Hyqvia/Gammagard/Cuvitru (Takeda IGSC ~$2.2B), CSL Privigen/Hizentra
    # (~$3B), Grifols Flebogamma (~$1.5B). IgG replacement therapy SC/IV.
    # Net branded ~$110K/yr (lifelong replacement).
    "immunology.autoimmune.primary_immunodeficiency": {
        "us":  {"patientsK": 250,  "wtpPct": 80, "priceK": 110},
        "eu":  {"patientsK": 350,  "wtpPct": 60, "priceK": 70},
        "row": {"patientsK": 2000, "wtpPct": 18, "priceK": 22},
    },
    # Solid organ transplant rejection prophylaxis (kidney + liver +
    # heart + lung): chronic immunosuppression. US ~250K transplant
    # recipients on tx, EU ~350K, ROW ~600K. Class: tacrolimus
    # (Astellas Astagraf XL + Prograf ~$400M brand + generics dominant),
    # cyclosporine (Sandimmune NVS legacy generic), mycophenolate
    # (CellCept generic), Envarsus XR (Veloxis tac MR), everolimus
    # (Zortress Novartis), belatacept (Nulojix BMS). Net branded
    # ~$18K/yr (mostly generics).
    "immunology.transplant.solid_organ": {
        "us":  {"patientsK": 250,  "wtpPct": 70, "priceK": 18},
        "eu":  {"patientsK": 350,  "wtpPct": 50, "priceK": 11},
        "row": {"patientsK": 600,  "wtpPct": 14, "priceK": 4},
    },
    # Ankylosing spondylitis (AS) + axial spondyloarthritis (axSpA): chronic
    # inflammatory spinal arthritis. ~1M US AS + ~2M nr-axSpA, ~1.5M EU AS,
    # ~10M ROW. Class: Cosentyx/Bimzelx (IL-17), TNFi legacy (Humira/Enbrel/
    # Simponi), JAKi (Rinvoq/Xeljanz). Class peak ~$5-7B globally.
    "immunology.inflammatory_systemic.ankylosing_spondylitis": {
        "us":  {"patientsK": 1000,  "wtpPct": 45, "priceK": 50},
        "eu":  {"patientsK": 1500,  "wtpPct": 32, "priceK": 30},
        "row": {"patientsK": 10000, "wtpPct": 7,  "priceK": 10},
    },
    "immunology.inflammatory_systemic.rheumatoid_arthritis": {
        "us":  {"patientsK": 1500,  "wtpPct": 50, "priceK": 20},
        "eu":  {"patientsK": 2500,  "wtpPct": 35, "priceK": 12},
        "row": {"patientsK": 12000, "wtpPct": 12, "priceK": 4},
    },

    # ============================================================
    # IMMUNOLOGY - NEUROMUSCULAR AUTOIMMUNE
    # ============================================================
    "immunology.neuromuscular_autoimmune.itp": {
        "us":  {"patientsK": 60,  "wtpPct": 60, "priceK": 80},
        "eu":  {"patientsK": 80,  "wtpPct": 45, "priceK": 45},
        "row": {"patientsK": 500, "wtpPct": 12, "priceK": 12},
    },
    "immunology.neuromuscular_autoimmune.mmn": {
        "us":  {"patientsK": 5,  "wtpPct": 70, "priceK": 150},
        "eu":  {"patientsK": 7,  "wtpPct": 55, "priceK": 80},
        "row": {"patientsK": 20, "wtpPct": 20, "priceK": 30},
    },
    "immunology.neuromuscular_autoimmune.myasthenia_gravis": {
        "us":  {"patientsK": 60,  "wtpPct": 65, "priceK": 280},
        "eu":  {"patientsK": 130, "wtpPct": 48, "priceK": 150},
        "row": {"patientsK": 800, "wtpPct": 12, "priceK": 25},
    },
    # Idiopathic inflammatory myopathies (myositis): dermatomyositis (DM),
    # polymyositis (PM), inclusion body myositis (IBM), immune-mediated
    # necrotizing myopathy (IMNM). ~50K US, ~70K EU, ~200K ROW. Class:
    # IVIg (Octapharma) standard, corticosteroids legacy, MMF/aza off-label.
    # Argenx Vyvgart Ph3 ALKIVIA (DM, polymyositis, IMNM) -- if positive
    # opens novel branded class. Class peak ~$2-3B globally.
    # source: Myositis Association; Argenx + Octapharma 10-Ks.
    "immunology.neuromuscular_autoimmune.myositis": {
        "us":  {"patientsK": 50,  "wtpPct": 50, "priceK": 200},
        "eu":  {"patientsK": 70,  "wtpPct": 38, "priceK": 130},
        "row": {"patientsK": 200, "wtpPct": 10, "priceK": 35},
    },
    # CIDP (chronic inflammatory demyelinating polyneuropathy): rare autoimmune
    # peripheral neuropathy. ~30K US diagnosed, ~50K EU, ~150K ROW. Class:
    # Vyvgart Hytrulo (Argenx efgartigimod, FDA approved 2024 ~$700M ramping),
    # IVIg/SCIg standard-of-care historic, Riliprubart (Sanofi anti-C1s Ph3
    # MOBILIZE+VITALIZE), CSL Behring Hizentra. Class peak ~$3-4B globally
    # with Vyvgart class adoption. source: GBS/CIDP Foundation; Argenx 10-K.
    "immunology.neuromuscular_autoimmune.cidp": {
        "us":  {"patientsK": 30,  "wtpPct": 70, "priceK": 200},
        "eu":  {"patientsK": 50,  "wtpPct": 50, "priceK": 130},
        "row": {"patientsK": 150, "wtpPct": 12, "priceK": 35},
    },
    # source: SPS prevalence ~1 per 1M (NORD, Stiff Person Syndrome Foundation)
    # = ~330 US diagnosed; broader "treatable" pool (off-label IVIG/benzo
    # responders) ~1-2K. EU5 ~1.5K. No approved therapy specifically for SPS;
    # IVIG + benzodiazepines used off-label. KYV-101 (Kyverna CAR-T) BLA H1
    # 2026 would be first-in-class. Premium orphan-CAR-T pricing ~$600K
    # one-time (Yescarta $480K precedent).
    "immunology.neuromuscular_autoimmune.sps": {
        "us":  {"patientsK": 1.5, "wtpPct": 65, "priceK": 600},
        "eu":  {"patientsK": 1.5, "wtpPct": 45, "priceK": 400},
        "row": {"patientsK": 3,   "wtpPct": 8,  "priceK": 200},
    },

    # ============================================================
    # IMMUNOLOGY - DEMYELINATING (multiple sclerosis class)
    # ============================================================
    # source: US MS ~900K diagnosed (NMSS); EU5 ~1.5M; ROW ~1.5M global. Branded
    # DMT class (Ocrevus $7B + Kesimpta $3B + Tysabri $2B + Mavenclad + Tecfidera
    # post-generic + Aubagio post-generic + Lemtrada + Briumvi + Ponvory) = ~$25B
    # current global, peak $30B with new entries. Net ~$25K/yr post-rebates.
    "immunology.demyelinating.multiple_sclerosis": {
        "us":  {"patientsK": 900,   "wtpPct": 60, "priceK": 25},
        "eu":  {"patientsK": 1500,  "wtpPct": 40, "priceK": 15},
        "row": {"patientsK": 1500,  "wtpPct": 12, "priceK": 5},
    },

    # ============================================================
    # DERMATOLOGY - AESTHETICS (procedures/yr as patientsK)
    # ============================================================
    "dermatology.aesthetics.filler": {
        "us":  {"patientsK": 3000,  "wtpPct": 90, "priceK": 0.8},
        "eu":  {"patientsK": 4000,  "wtpPct": 85, "priceK": 0.5},
        "row": {"patientsK": 15000, "wtpPct": 80, "priceK": 0.3},
    },
    "dermatology.aesthetics.neurotoxin": {
        "us":  {"patientsK": 5000,  "wtpPct": 92, "priceK": 0.55},
        "eu":  {"patientsK": 6000,  "wtpPct": 88, "priceK": 0.35},
        "row": {"patientsK": 25000, "wtpPct": 80, "priceK": 0.2},
    },

    # ============================================================
    # DERMATOLOGY - INFLAMMATORY
    # ============================================================
    # source: US moderate-to-severe AD on systemic Rx ~500K (NHANES + derm
    # billing claims); EU5 ~700K; ROW ~4M through dermatology channels.
    # Blended net price ~$25K/yr (Dupixent WAC $38K with PBM rebates ~35%;
    # Rinvoq/Cibinqo similar). Global addressable TAM ~$14B matches current
    # branded biologic+JAK spend (Dupixent-AD $9B + Rinvoq-AD $1.5B + others
    # $3B = $13-14B). Prior values (1.5M US, 20M ROW, $38K uniform WAC)
    # conflated all AD with biologic-eligible severe -- 6x inflation vs reality.
    "dermatology.inflammatory_derm.atopic_dermatitis_systemic": {
        "us":  {"patientsK": 500,   "wtpPct": 55, "priceK": 25},
        "eu":  {"patientsK": 700,   "wtpPct": 40, "priceK": 16},
        "row": {"patientsK": 4000,  "wtpPct": 12, "priceK": 5},
    },
    # source: US AD prevalence ~30M but branded topical-addressable (novel
    # nonsteroidal creams -- Opzelura, Zoryve-AD, Eucrisa) ~5M per INCY / ARQT
    # commercial franchises. Generic steroids + Elidel/Protopic tacrolimus
    # dominate the remainder at $20-100 per tube. Addressable branded TAM
    # ~$4-5B globally -- matches Opzelura ~$600M + Zoryve-AD launch curve +
    # Eucrisa + Aldara combined. Prior TAM ($17B at 8M US / 55% / $2K) assumed
    # every topical-using AD patient buys at branded pricing; ~4x too big.
    "dermatology.inflammatory_derm.atopic_dermatitis_topical": {
        "us":  {"patientsK": 5000,   "wtpPct": 30, "priceK": 2},
        "eu":  {"patientsK": 5000,   "wtpPct": 20, "priceK": 1},
        "row": {"patientsK": 20000,  "wtpPct": 8,  "priceK": 0.2},
    },
    "dermatology.inflammatory_derm.hidradenitis_suppurativa": {
        "us":  {"patientsK": 200,  "wtpPct": 55, "priceK": 45},
        "eu":  {"patientsK": 300,  "wtpPct": 40, "priceK": 22},
        "row": {"patientsK": 2000, "wtpPct": 10, "priceK": 5},
    },
    # source: US biologic-treated moderate-severe psoriasis ~1.5M (NPF registry
    # + dermatology claims); EU5 ~2M; ROW ~10M via specialty derm channels.
    # Blended net price ~$20K/yr -- Stelara/Skyrizi/Cosentyx/Taltz/Tremfya
    # WAC $50-60K but PBM rebates + biosimilar competition on Stelara drive
    # net down. Global addressable TAM ~$42B matches projected 2027-28 peak
    # branded spend (Skyrizi ~$15B + Stelara ~$5B post-biosimilar + Cosentyx
    # ~$7B + Tremfya ~$5B + Taltz ~$3.5B + Bimzelx ~$3B + Sotyktu/Otezla ~$4B).
    # Prior TAM $105B at $52K uniform WAC overstated net economics by ~2.5x.
    "dermatology.inflammatory_derm.psoriasis_systemic": {
        "us":  {"patientsK": 1500,  "wtpPct": 55, "priceK": 20},
        "eu":  {"patientsK": 2000,  "wtpPct": 40, "priceK": 12},
        "row": {"patientsK": 10000, "wtpPct": 12, "priceK": 4},
    },
    # source: US psoriasis ~7M but topical-branded-addressable (novel
    # nonsteroidal creams -- Zoryve, Vtama, Enstilar) ~3M. Taclonex generics
    # + topical corticosteroid generics + vitamin-D analogs dominate at
    # $30-100 per tube. Addressable branded TAM ~$3B globally -- matches
    # Zoryve ~$250M + Vtama ~$350M today with $1-2B peak each projected.
    # Prior TAM ($8B at 6M US / 50% / $1.5K) assumed every topical-using
    # psoriasis patient pays branded -- ~3x too big.
    "dermatology.inflammatory_derm.psoriasis_topical": {
        "us":  {"patientsK": 3000,   "wtpPct": 30, "priceK": 2},
        "eu":  {"patientsK": 4000,   "wtpPct": 20, "priceK": 1},
        "row": {"patientsK": 20000,  "wtpPct": 8,  "priceK": 0.2},
    },

    # ============================================================
    # DERMATOLOGY - RARE SKIN
    # ============================================================
    "dermatology.rare_skin.alopecia_areata": {
        "us":  {"patientsK": 300,  "wtpPct": 45, "priceK": 42},
        "eu":  {"patientsK": 450,  "wtpPct": 32, "priceK": 22},
        "row": {"patientsK": 4000, "wtpPct": 10, "priceK": 4},
    },
    "dermatology.rare_skin.deb": {
        "us":  {"patientsK": 3,   "wtpPct": 80, "priceK": 800},
        "eu":  {"patientsK": 4,   "wtpPct": 65, "priceK": 300},
        "row": {"patientsK": 20,  "wtpPct": 15, "priceK": 25},
    },
    "dermatology.rare_skin.hailey_hailey": {
        "us":  {"patientsK": 2,   "wtpPct": 30, "priceK": 3},
        "eu":  {"patientsK": 3,   "wtpPct": 25, "priceK": 1.5},
        "row": {"patientsK": 15,  "wtpPct": 8,  "priceK": 0.3},
    },
    "dermatology.rare_skin.vitiligo": {
        "us":  {"patientsK": 1500,  "wtpPct": 50, "priceK": 8},
        "eu":  {"patientsK": 2000,  "wtpPct": 35, "priceK": 3},
        "row": {"patientsK": 60000, "wtpPct": 12, "priceK": 0.5},
    },
    # source: Dellon 2022 EoE diagnosed prevalence ~150K US (rising); Dupixent EoE WAC ~$35K
    "immunology.inflammatory_gi.eoe": {
        "us":  {"patientsK": 150,  "wtpPct": 55, "priceK": 35},
        "eu":  {"patientsK": 120,  "wtpPct": 35, "priceK": 20},
        "row": {"patientsK": 250,  "wtpPct": 6,  "priceK": 5},
    },
    # source: Boozalis 2018 PN US prevalence ~150K severe; Dupixent PN approval 2022, WAC ~$35K
    "dermatology.inflammatory_derm.prurigo_nodularis": {
        "us":  {"patientsK": 150,  "wtpPct": 55, "priceK": 35},
        "eu":  {"patientsK": 180,  "wtpPct": 35, "priceK": 20},
        "row": {"patientsK": 800,  "wtpPct": 5,  "priceK": 4},
    },
    # CSU (chronic spontaneous urticaria): chronic itchy hives >=6 weeks despite
    # H1-antihistamine. ~1.5M US, ~2M EU, ~10M ROW. Class: Xolair (omalizumab,
    # Roche $4B all indications), Dupixent (FDA approved CSU 2025 expansion),
    # ligelizumab (Novartis, dropped 2024), KalVista bradykinin pipeline.
    # Class peak ~$3-4B with Dupixent + Xolair share.
    "dermatology.inflammatory_derm.csu": {
        "us":  {"patientsK": 1500, "wtpPct": 28, "priceK": 35},
        "eu":  {"patientsK": 2000, "wtpPct": 18, "priceK": 20},
        "row": {"patientsK": 10000, "wtpPct": 5, "priceK": 4},
    },
    # source: Lee 2022 cGVHD prevalence ~14K incident/yr post-allo-SCT US;
    # actively-treated active disease ~30K prevalent. Imbruvica + Jakafi + ECP.
    "immunology.transplant.cgvhd": {
        "us":  {"patientsK": 30,  "wtpPct": 70, "priceK": 150},
        "eu":  {"patientsK": 28,  "wtpPct": 50, "priceK": 90},
        "row": {"patientsK": 60,  "wtpPct": 10, "priceK": 30},
    },
}

# Peak penetration (%) per disease area, from the penPct tooltip note.
PEN_PCT = {
    "immunology.autoimmune.fsgs": 25,
    "immunology.autoimmune.hereditary_angioedema": 70,
    "immunology.autoimmune.iga_nephropathy": 30,
    "immunology.autoimmune.pmn": 30,
    "immunology.autoimmune.sjogrens": 15,
    "immunology.autoimmune.sle": 25,
    "immunology.inflammatory_gi.crohns": 38,
    "immunology.inflammatory_gi.ulcerative_colitis": 35,
    "immunology.inflammatory_gi.eoe": 35,
    "immunology.inflammatory_systemic.rheumatoid_arthritis": 28,
    "immunology.inflammatory_systemic.psoriatic_arthritis": 30,
    "immunology.inflammatory_systemic.gca_pmr": 18,
    "immunology.autoinflammatory.periodic_fever": 65,
    "immunology.autoimmune.egpa": 60,
    "immunology.autoimmune.primary_immunodeficiency": 35,
    "immunology.transplant.solid_organ": 60,
    "immunology.inflammatory_systemic.ankylosing_spondylitis": 25,
    "immunology.neuromuscular_autoimmune.itp": 35,
    "immunology.neuromuscular_autoimmune.mmn": 65,
    "immunology.neuromuscular_autoimmune.myasthenia_gravis": 40,
    "immunology.neuromuscular_autoimmune.cidp": 35,
    "immunology.neuromuscular_autoimmune.myositis": 25,
    "immunology.neuromuscular_autoimmune.sps": 30,
    "immunology.demyelinating.multiple_sclerosis": 25,
    "dermatology.aesthetics.filler": 5,
    "dermatology.aesthetics.neurotoxin": 12,
    "dermatology.inflammatory_derm.atopic_dermatitis_systemic": 35,
    "dermatology.inflammatory_derm.atopic_dermatitis_topical": 12,
    "dermatology.inflammatory_derm.hidradenitis_suppurativa": 25,
    "dermatology.inflammatory_derm.psoriasis_systemic": 40,
    "dermatology.inflammatory_derm.psoriasis_topical": 10,
    "dermatology.rare_skin.alopecia_areata": 20,
    "dermatology.rare_skin.deb": 60,
    "dermatology.rare_skin.hailey_hailey": 10,
    "dermatology.rare_skin.vitiligo": 15,
    "immunology.inflammatory_gi.eoe": 30,
    "dermatology.inflammatory_derm.prurigo_nodularis": 30,
    "dermatology.inflammatory_derm.csu": 18,
    "immunology.transplant.cgvhd": 35,
}
