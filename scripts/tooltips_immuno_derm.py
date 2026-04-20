# -*- coding: utf-8 -*-
"""
Source-cited tooltips for immunology and dermatology disease areas.
Counts in thousands (K). Prices in USD thousands per patient-year (annualized).
All notes < 180 chars, ASCII only, no em-dashes.
"""

TOOLTIPS = {
    # ============================================================
    # IMMUNOLOGY - AUTOIMMUNE
    # ============================================================
    "immunology.autoimmune.fsgs": {
        "us.patientsK":  {"note": "NKF/NephCure: ~40K US FSGS prevalent; ~5-7K new cases/yr; ~50% progress to ESRD within 5-10yr without remission."},
        "eu.patientsK":  {"note": "ERA-EDTA registry: ~45K EU27+UK FSGS; underdiagnosis common; ~7% of primary glomerular disease biopsies."},
        "row.patientsK": {"note": "Global ex-US/EU ~200K (higher APOL1-associated incidence in African ancestry); China/Japan KDIGO-guided."},
        "us.wtpPct":     {"note": "~45% -- Medicare ESRD benefit + commercial cover Filspari (sparsentan); ACTH + CNI supportive still common."},
        "eu.wtpPct":     {"note": "~30% -- EMA approved Filspari 2024; NICE HST pathway; RAASi + steroids standard first-line."},
        "row.wtpPct":    {"note": "~8% -- limited novel access; steroids + CNI (tacrolimus/cyclosporine generics) dominate."},
        "us.priceK":     {"note": "Blended $90K: Filspari $120K (30% pts) + tacrolimus/CNI generic $3K + ACTH Acthar $200K niche; rituximab off-label $30K."},
        "eu.priceK":     {"note": "~$45K blended -- Filspari ~$70K net + generic CNI dominant backbone."},
        "row.priceK":    {"note": "~$8K -- generic immunosuppressants; novel agents minimal penetration."},
        "penPct":        {"note": "~25% peak -- Filspari + pipeline (atrasentan, obinutuzumab); steroid-resistant segment drives novel uptake."}
    },
    "immunology.autoimmune.hereditary_angioedema": {
        "us.patientsK":  {"note": "US HAE Association: ~7K US HAE diagnosed (~1:50K prevalence); ~20% still undiagnosed per HAEA registry."},
        "eu.patientsK":  {"note": "HAE International: ~10K EU27+UK; Germany/France strongest diagnosis rates; C1-INH deficiency type I dominant."},
        "row.patientsK": {"note": "Global ex-US/EU ~20K diagnosed; Japan HAE registry ~500 pts; China significantly underdiagnosed."},
        "us.wtpPct":     {"note": "~75% -- commercial + Medicare cover Takhzyro/Orladeyo prophylaxis; on-demand Firazyr/Berinert reimbursed."},
        "eu.wtpPct":     {"note": "~55% -- NICE approved Takhzyro/Orladeyo; G-BA added benefit; C1-INH (Cinryze/Berinert) first-line prophylaxis."},
        "row.wtpPct":    {"note": "~15% -- Japan PMDA approved lanadelumab; China access limited to on-demand C1-INH."},
        "us.priceK":     {"note": "Blended $450K: Takhzyro $600K + Orladeyo $500K + Haegarda $500K + on-demand Firazyr/Berinert $200K per attack."},
        "eu.priceK":     {"note": "~$280K blended -- Takhzyro net ~$350K post-discount; C1-INH prophylaxis $200K."},
        "row.priceK":    {"note": "~$100K -- Japan Takhzyro ~$250K; emerging markets C1-INH on-demand only."},
        "penPct":        {"note": "~70% peak -- prophylaxis shift from on-demand; Donidalorsen/garadacimab pipeline expanding coverage."}
    },
    "immunology.autoimmune.iga_nephropathy": {
        "us.patientsK":  {"note": "NKF: ~130K US IgAN prevalent; ~40% progress to ESRD within 20yr; most common primary GN globally."},
        "eu.patientsK":  {"note": "ERA registry: ~150K EU27+UK IgAN; Italy/France highest biopsy rates; MEST-C scoring standard."},
        "row.patientsK": {"note": "Global ex-US/EU ~1.5M (Asia Pacific 40-50% of primary GN biopsies); Japan screening program drives detection."},
        "us.wtpPct":     {"note": "~50% -- Tarpeyo (budesonide) + Filspari covered post-2023 FDA approvals; Medicare + commercial strong."},
        "eu.wtpPct":     {"note": "~35% -- EMA approved Kinpeygo/Filspari; NICE positive; RAASi + SGLT2i baseline therapy."},
        "row.wtpPct":    {"note": "~10% -- Japan JSN guidelines tonsillectomy + steroids; China TCM + supportive care common."},
        "us.priceK":     {"note": "Blended $65K: Tarpeyo $15K/9mo course (30%) + Filspari $120K (20%) + RAASi/SGLT2i generic $2K baseline."},
        "eu.priceK":     {"note": "~$32K blended -- Kinpeygo ~$25K course + Filspari ~$70K net + generic backbone."},
        "row.priceK":    {"note": "~$6K -- generics dominate; novel agents <5% penetration."},
        "penPct":        {"note": "~30% peak -- novel agents stacking (Tarpeyo + Filspari + SGLT2i); sibeprenlimab/atrasentan pipeline."}
    },
    "immunology.autoimmune.sjogrens": {
        "us.patientsK":  {"note": "Sjogren's Foundation: ~1M US diagnosed; ~4M including undiagnosed; 90% female; ASSAY/CLASSIC criteria."},
        "eu.patientsK":  {"note": "EULAR Sjogren's registry: ~2M EU27+UK; ESSDAI scoring for systemic disease; ~25% have systemic involvement."},
        "row.patientsK": {"note": "Global ex-US/EU ~15M prevalence extrapolated; Asia significantly underdiagnosed; no novel approved therapies."},
        "us.wtpPct":     {"note": "~25% -- no FDA-approved systemic therapy; off-label HCQ/rituximab + symptomatic (Restasis/Xiidra for sicca)."},
        "eu.wtpPct":     {"note": "~18% -- no EMA systemic approval; HCQ first-line per EULAR; pilocarpine/cevimeline for symptoms."},
        "row.wtpPct":    {"note": "~5% -- symptomatic care only; HCQ generic widely available."},
        "us.priceK":     {"note": "Blended $8K: HCQ generic $1K + rituximab biosim $20K (10% pts) + symptomatic eye/mouth $3K; ianalumab/dazodalibep pipeline."},
        "eu.priceK":     {"note": "~$4K blended -- HCQ + biosim rituximab dominant; Ruconest/symptomatic."},
        "row.priceK":    {"note": "~$1K -- HCQ generic + basic symptomatic care."},
        "penPct":        {"note": "~15% peak -- awaiting novel approvals (ianalumab, dazodalibep, remibrutinib); current pen reflects off-label biologics."}
    },
    "immunology.autoimmune.sle": {
        "us.patientsK":  {"note": "Lupus Foundation of America: ~300K US SLE; 90% female; African American 3x risk; CDC 2018 registry data."},
        "eu.patientsK":  {"note": "EULAR SLE registry: ~350K EU27+UK; SLEDAI/BILAG severity scoring; ~30% lupus nephritis subset."},
        "row.patientsK": {"note": "Global ex-US/EU ~4M; Asia Pacific highest age-standardized prevalence; lupus nephritis more aggressive."},
        "us.wtpPct":     {"note": "~55% -- Benlysta (IV + SC) Medicare Part B/D; Saphnelo (anifrolumab) commercial; Lupkynis LN covered."},
        "eu.wtpPct":     {"note": "~38% -- EMA approved Benlysta/Saphnelo/Lupkynis; NICE restrictive; HCQ + MMF backbone standard."},
        "row.wtpPct":    {"note": "~10% -- HCQ + steroids + MMF/AZA generics dominate; Japan Benlysta reimbursed."},
        "us.priceK":     {"note": "Blended $45K: Benlysta $40K + Saphnelo $65K + Lupkynis $90K (LN) + HCQ/MMF generic $3K backbone; rituximab off-label."},
        "eu.priceK":     {"note": "~$22K blended -- Benlysta net ~$25K + generic backbone; anifrolumab ~$40K net."},
        "row.priceK":    {"note": "~$5K -- HCQ + generic immunosuppressants; biologics <10% penetration."},
        "penPct":        {"note": "~25% peak -- biologic cycle-through (Benlysta -> Saphnelo -> CAR-T pipeline); steroid-sparing driver."}
    },

    # ============================================================
    # IMMUNOLOGY - INFLAMMATORY GI
    # ============================================================
    "immunology.inflammatory_gi.crohns": {
        "us.patientsK":  {"note": "Crohn's & Colitis Foundation: ~800K US CD; CDC NHIS ~3M IBD total; peak onset 15-35yr."},
        "eu.patientsK":  {"note": "ECCO registry: ~1.3M EU27+UK CD; Scandinavia highest incidence; Northern Europe gradient."},
        "row.patientsK": {"note": "Global ex-US/EU ~2M CD; rising incidence in newly industrialized (China, India, Brazil)."},
        "us.wtpPct":     {"note": "~65% -- Medicare Part B infusions (Remicade/Entyvio) + Part D Humira/Stelara/Rinvoq SC/oral; biosimilars expanding."},
        "eu.wtpPct":     {"note": "~48% -- NICE/G-BA cover anti-TNF + IL-23 + S1P; ~80% adalimumab biosimilar share; infliximab biosim dominant."},
        "row.wtpPct":    {"note": "~12% -- Japan J-DPS covers biologics; China NRDL added adalimumab biosim; LatAm biosimilar-led."},
        "us.priceK":     {"note": "Blended $62K: Humira biosim $18K + Stelara $75K + Entyvio $65K + Skyrizi $80K + Rinvoq $65K; 5-ASA/steroids generics."},
        "eu.priceK":     {"note": "~$30K blended -- adalimumab biosim ~$8K net + Stelara ~$35K + Entyvio ~$30K."},
        "row.priceK":    {"note": "~$10K -- biosimilars + 5-ASA generics; Japan closer to EU pricing."},
        "penPct":        {"note": "~38% peak -- sequential biologic/JAKi cycling; moderate-severe shift to advanced therapy earlier."}
    },
    "immunology.inflammatory_gi.ulcerative_colitis": {
        "us.patientsK":  {"note": "Crohn's & Colitis Foundation: ~700K US UC; slightly more common than CD; Mayo score severity index."},
        "eu.patientsK":  {"note": "ECCO: ~1.5M EU27+UK UC; higher prevalence than CD in most registries; Nordic countries peak incidence."},
        "row.patientsK": {"note": "Global ex-US/EU ~3M UC; Japan highest Asian prevalence; China/India rising rapidly."},
        "us.wtpPct":     {"note": "~62% -- Medicare/commercial cover full biologic ladder + JAKi (Rinvoq/Xeljanz) + S1P (Zeposia/Velsipity); 5-ASA first-line."},
        "eu.wtpPct":     {"note": "~45% -- NICE/G-BA stepwise; infliximab biosim preferred; Entyvio/Stelara/Rinvoq 2L+."},
        "row.wtpPct":    {"note": "~12% -- 5-ASA/steroids dominant; Japan adds biologics; biosimilars accelerating access."},
        "us.priceK":     {"note": "Blended $55K: Humira biosim $18K + Entyvio $65K + Stelara $75K + Rinvoq $65K + Zeposia $85K; mesalamine generic $3K."},
        "eu.priceK":     {"note": "~$28K blended -- biosim-heavy (~80% adalim/inflix) + Entyvio ~$30K + 5-ASA backbone."},
        "row.priceK":    {"note": "~$8K -- mesalamine + biosim anti-TNF in upper-middle income markets."},
        "penPct":        {"note": "~35% peak -- advanced therapy shift; S1P oral convenience + JAKi speed of onset."}
    },

    # ============================================================
    # IMMUNOLOGY - INFLAMMATORY SYSTEMIC
    # ============================================================
    "immunology.inflammatory_systemic.rheumatoid_arthritis": {
        "us.patientsK":  {"note": "CDC BRFSS 2023: ~1.3M US RA diagnosed; ~1.5M treated including undiagnosed (Rheumatology Research Fnd)."},
        "eu.patientsK":  {"note": "EULAR registry: ~2.9M EU27+UK RA; ~1.2M on bDMARD/tsDMARD; most on MTX first-line."},
        "row.patientsK": {"note": "Global ex-US/EU ~18M (high Asia prevalence); ~2M on biologics (biosimilars + originator)."},
        "us.wtpPct":     {"note": "~55% -- Medicare + commercial robust bDMARD coverage; biosimilar uptake accelerating post-2023 (Humira LOE)."},
        "eu.wtpPct":     {"note": "~42% -- NICE/G-BA approved bDMARDs; ~85% biosimilar share on adalimumab/etanercept."},
        "row.wtpPct":    {"note": "~10% -- China/LatAm: biosimilar-first; Japan J-DPS covers JAKi + anti-TNF widely."},
        "us.priceK":     {"note": "Blended $55K: anti-TNF biosim $15K (40%) + originator $60K + JAKi $65K (20%) + IL-6/CTLA4 $55K; MTX $2K first-line."},
        "eu.priceK":     {"note": "~$28K blended -- biosimilar-dominated (~85% adalim/etanercept), net prices 40-50% of US."},
        "row.priceK":    {"note": "~$10K blended -- biosimilars + local generics, Japan closer to EU."},
        "penPct":        {"note": "~28% peak reflects bDMARD/tsDMARD cycle-through; first-line MTX+steroids still dominant."}
    },

    # ============================================================
    # IMMUNOLOGY - NEUROMUSCULAR AUTOIMMUNE
    # ============================================================
    "immunology.neuromuscular_autoimmune.itp": {
        "us.patientsK":  {"note": "PDSA/ASH: ~60K US chronic ITP adults; ~125K total including pediatric acute; platelet <100K dx threshold."},
        "eu.patientsK":  {"note": "EHA registry: ~80K EU27+UK chronic ITP; TPO-RA + rituximab + splenectomy tiered algorithm."},
        "row.patientsK": {"note": "Global ex-US/EU ~500K chronic ITP; Japan J-Registry detailed; China TPO-RA access expanding."},
        "us.wtpPct":     {"note": "~60% -- Promacta/Doptelet/Nplate (TPO-RA) Medicare Part B/D; Tavneos emerging; rituximab biosim 2L+."},
        "eu.wtpPct":     {"note": "~45% -- NICE approved TPO-RA post-splenectomy; eltrombopag/romiplostim standard; rituximab biosim."},
        "row.wtpPct":    {"note": "~12% -- steroids + IVIG first-line; TPO-RA access growing; Japan reimburses full ladder."},
        "us.priceK":     {"note": "Blended $80K: Promacta $90K + Nplate $110K + Doptelet $95K + rituximab biosim $25K (20%); steroids/IVIG baseline."},
        "eu.priceK":     {"note": "~$45K blended -- TPO-RA net ~$55K + biosim rituximab ~$10K."},
        "row.priceK":    {"note": "~$12K -- steroids/IVIG + eltrombopag generic entry in some markets."},
        "penPct":        {"note": "~35% peak -- rilzabrutinib (BTKi) + efgartigimod (FcRn) pipeline expanding beyond TPO-RA."}
    },
    "immunology.neuromuscular_autoimmune.mmn": {
        "us.patientsK":  {"note": "GBS/CIDP Foundation: ~5K US MMN (multifocal motor neuropathy); ~1-2:100K prevalence; anti-GM1 antibodies common."},
        "eu.patientsK":  {"note": "EAN: ~7K EU27+UK MMN; IVIG mainstay; PNS diagnostic criteria; often misdiagnosed as ALS early."},
        "row.patientsK": {"note": "Global ex-US/EU ~20K MMN; underdiagnosed; Japan MHLW intractable disease registry."},
        "us.wtpPct":     {"note": "~70% -- Medicare Part B IVIG (Gamunex/Privigen) covered; SCIG (Hizentra) home admin; rituximab off-label."},
        "eu.wtpPct":     {"note": "~55% -- IVIG/SCIG covered; limited novel therapy; efgartigimod/nipocalimab trials ongoing."},
        "row.wtpPct":    {"note": "~20% -- IVIG access limited by cost; steroids ineffective in MMN unlike CIDP."},
        "us.priceK":     {"note": "Blended $150K: IVIG ~$150K/yr (maintenance dosing) + SCIG $140K; no approved targeted therapy; rituximab $25K off-label."},
        "eu.priceK":     {"note": "~$80K blended -- IVIG/SCIG net ~$80K; tender-based pricing."},
        "row.priceK":    {"note": "~$30K -- IVIG access-constrained; plasma-derived supply limits."},
        "penPct":        {"note": "~65% peak -- IVIG is standard of care; FcRn antagonists (efgartigimod) potential alternative in trials."}
    },
    "immunology.neuromuscular_autoimmune.myasthenia_gravis": {
        "us.patientsK":  {"note": "MGFA: ~60-80K US prevalent gMG; ~100K treated including ocular + undiagnosed; AChR+ 85%, MuSK+ 6%."},
        "eu.patientsK":  {"note": "EAN/EFNS: ~130K EU27+UK gMG; acetylcholinesterase inhibitors + steroids + MMF/AZA standard."},
        "row.patientsK": {"note": "Global ex-US/EU ~800K gMG; Japan MHLW registry detailed; China rising diagnosis rates."},
        "us.wtpPct":     {"note": "~65% -- Soliris/Ultomiris (C5) + Vyvgart/Rystiggo (FcRn) Medicare Part B covered; pyridostigmine generic backbone."},
        "eu.wtpPct":     {"note": "~48% -- NICE/G-BA approved Vyvgart/Ultomiris/Rystiggo; AChEi + steroids + MMF first-line."},
        "row.wtpPct":    {"note": "~12% -- pyridostigmine + steroids + AZA/MMF generic; Japan covers FcRn + C5; China limited."},
        "us.priceK":     {"note": "Blended $280K: Vyvgart $400K + Ultomiris $450K + Soliris $500K + rituximab off-label $25K; pyridostigmine $1K."},
        "eu.priceK":     {"note": "~$150K blended -- Vyvgart net ~$180K + Ultomiris ~$220K + generic backbone."},
        "row.priceK":    {"note": "~$25K -- pyridostigmine + steroids + generic immunosuppressants dominate."},
        "penPct":        {"note": "~40% peak -- FcRn (efgartigimod, rozanolixizumab) + C5 + pipeline CAR-T/nipocalimab driving advanced therapy shift."}
    },

    # ============================================================
    # DERMATOLOGY - AESTHETICS
    # ============================================================
    "dermatology.aesthetics.filler": {
        "us.patientsK":  {"note": "ASDS 2023 survey: ~3M US HA filler procedures/yr; ~1.5M unique patients; lips/cheeks/NLF top sites."},
        "eu.patientsK":  {"note": "IMCAS/ESAAD: ~4M EU27+UK filler procedures/yr; Germany/Italy/UK top markets; HA dermal fillers dominate."},
        "row.patientsK": {"note": "Global ex-US/EU ~15M procedures; Brazil/Korea/China top markets; Korea K-beauty export hub."},
        "us.wtpPct":     {"note": "~90% -- fully cash-pay cosmetic; no insurance coverage; loyalty program financing (CareCredit)."},
        "eu.wtpPct":     {"note": "~85% -- cash-pay aesthetic; VAT varies; medical tourism to Turkey/Poland for lower pricing."},
        "row.wtpPct":    {"note": "~80% -- cash-pay; Brazil/Korea highly price-competitive local manufacturers."},
        "us.priceK":     {"note": "Blended $0.8K per syringe: Juvederm/Restylane $600-900; avg 2 syringes/treatment; retreat every 12-18mo."},
        "eu.priceK":     {"note": "~$0.5K per syringe -- Juvederm/Restylane/Teoxane ~$350-500; price compression from private clinic competition."},
        "row.priceK":    {"note": "~$0.3K -- Korean manufacturers (Medytox, Hugel) + local HA brands compete on price."},
        "penPct":        {"note": "~5% peak of eligible adults; driven by social media, GLP-1 'Ozempic face' volume loss, male cohort growth."}
    },
    "dermatology.aesthetics.neurotoxin": {
        "us.patientsK":  {"note": "ASDS/ASPS 2023: ~5M US Botox cosmetic procedures/yr; ~7M unique patients across cosmetic + therapeutic uses."},
        "eu.patientsK":  {"note": "IMCAS: ~6M EU27+UK neurotoxin procedures/yr; Azzalure/Vistabel dominant; Bocouture #2."},
        "row.patientsK": {"note": "Global ex-US/EU ~25M procedures; Korea/China massive volume; Korean toxins (Nabota, Innotox) export globally."},
        "us.wtpPct":     {"note": "~92% -- cash-pay cosmetic; Brilliant Distinctions/Allē loyalty; therapeutic (migraine/hyperhidrosis) insurance-covered."},
        "eu.wtpPct":     {"note": "~88% -- cash-pay cosmetic; therapeutic indications (blepharospasm, cervical dystonia) reimbursed."},
        "row.wtpPct":    {"note": "~80% -- cash-pay; Korean domestic toxins undercut Allergan ~50%."},
        "us.priceK":     {"note": "Blended $0.55K per session: Botox Cosmetic ~$12/unit x 40-60 units; Daxxify (longer duration) premium ~$700."},
        "eu.priceK":     {"note": "~$0.35K per session -- Azzalure/Vistabel net ~$6-8/unit; Bocouture price-competitive."},
        "row.priceK":    {"note": "~$0.2K per session -- Nabota/Meditoxin/Innotox ~$3-5/unit; massive volume price compression."},
        "penPct":        {"note": "~12% peak of eligible adults; preventative 'baby Botox' in 20s-30s expanding TAM; male cohort rising."}
    },

    # ============================================================
    # DERMATOLOGY - INFLAMMATORY
    # ============================================================
    "dermatology.inflammatory_derm.atopic_dermatitis_systemic": {
        "us.patientsK":  {"note": "NEA: ~1.5M US moderate-severe AD on systemic therapy; ~16.5M US adults have AD symptoms total."},
        "eu.patientsK":  {"note": "ETFAD: ~2.5M EU27+UK moderate-severe AD systemic-eligible; EASI/IGA severity scoring."},
        "row.patientsK": {"note": "Global ex-US/EU ~20M mod-severe; Japan high prevalence + strong Dupixent uptake; China rapid growth."},
        "us.wtpPct":     {"note": "~65% -- Dupixent commercial/Medicare Part D; Rinvoq/Cibinqo JAKi; Adbry (tralokinumab); Ebglyss (lebrikizumab) new."},
        "eu.wtpPct":     {"note": "~48% -- NICE/G-BA cover Dupixent + JAKi restricted use (BBW); Adbry/Ebglyss rolling out."},
        "row.wtpPct":    {"note": "~15% -- Japan J-DPS + China NRDL added Dupixent; cyclosporine generic + steroids baseline elsewhere."},
        "us.priceK":     {"note": "Blended $38K: Dupixent $40K + Rinvoq $65K + Cibinqo $60K + Adbry $40K + Ebglyss $40K; cyclosporine generic $3K."},
        "eu.priceK":     {"note": "~$22K blended -- Dupixent net ~$25K + JAKi ~$30K; cyclosporine/MTX generic backbone."},
        "row.priceK":    {"note": "~$8K -- cyclosporine generic + phototherapy; biologics <15% penetration ex-Japan."},
        "penPct":        {"note": "~35% peak -- rapid biologic/JAKi expansion; OX40 (rocatinlimab, amlitelimab) pipeline adding options."}
    },
    "dermatology.inflammatory_derm.atopic_dermatitis_topical": {
        "us.patientsK":  {"note": "NEA: ~8M US AD on topicals; ~16% US adults had AD symptoms per NEA 2024; pediatric cohort large."},
        "eu.patientsK":  {"note": "ETFAD: ~12M EU27+UK AD topical-managed; emollients + TCS + TCI stepwise."},
        "row.patientsK": {"note": "Global ex-US/EU ~100M topical AD; emollients + TCS standard; Japan tacrolimus ointment widely used."},
        "us.wtpPct":     {"note": "~55% -- commercial/Medicaid cover Opzelura (ruxolitinib) + Eucrisa (crisaborole) + TCS generics; Zoryve emerging."},
        "eu.wtpPct":     {"note": "~45% -- NICE restrictive on Opzelura; generic TCS + TCI (Protopic/Elidel) mainstay."},
        "row.wtpPct":    {"note": "~20% -- TCS generics widely accessible; novel topicals minimal ex-Japan."},
        "us.priceK":     {"note": "Blended $2K: Opzelura $2.5K/tube (~$15K/yr if chronic use) + Eucrisa $600/tube + TCS/TCI generics $50-200."},
        "eu.priceK":     {"note": "~$0.8K blended -- generic TCS/TCI dominant + selective Opzelura/Eucrisa net ~$8K."},
        "row.priceK":    {"note": "~$0.2K -- TCS/emollient generics; novel topicals negligible."},
        "penPct":        {"note": "~12% peak -- novel non-steroidal topicals (Opzelura, Zoryve-AD, roflumilast) expanding long-term use."}
    },
    "dermatology.inflammatory_derm.hidradenitis_suppurativa": {
        "us.patientsK":  {"note": "HS Foundation: ~200K US moderate-severe HS; ~1% US prevalence estimated; underdiagnosed by 7-10yr delay."},
        "eu.patientsK":  {"note": "EADV HS registry: ~300K EU27+UK mod-severe HS; Hurley staging + IHS4 severity."},
        "row.patientsK": {"note": "Global ex-US/EU ~2M mod-severe HS; massively underdiagnosed globally; emerging awareness programs."},
        "us.wtpPct":     {"note": "~55% -- Humira (adalimumab) + Cosentyx (secukinumab, 2023 FDA) + Bimzelx (bimekizumab, 2024) Medicare/commercial."},
        "eu.wtpPct":     {"note": "~40% -- adalimumab biosim first-line (EMA HS approval) + Cosentyx + Bimzelx; clindamycin/rifampin combos baseline."},
        "row.wtpPct":    {"note": "~10% -- antibiotics + surgery; biologics minimal ex-Japan; Humira biosim entry expanding access."},
        "us.priceK":     {"note": "Blended $45K: Humira biosim $18K + Cosentyx $60K + Bimzelx $75K + clindamycin/rifampin $2K baseline."},
        "eu.priceK":     {"note": "~$22K blended -- adalimumab biosim ~$8K net + Cosentyx ~$30K + Bimzelx ~$35K."},
        "row.priceK":    {"note": "~$5K -- antibiotics + surgical excision; biologics <5% penetration."},
        "penPct":        {"note": "~25% peak -- IL-17 (Cosentyx/Bimzelx) expanded ladder; povorcitinib/sonelokimab pipeline accelerating."}
    },
    "dermatology.inflammatory_derm.psoriasis_systemic": {
        "us.patientsK":  {"note": "NPF: ~8M US psoriasis total; ~1.5M moderate-severe on systemic/biologic; CDC 3% adult prevalence."},
        "eu.patientsK":  {"note": "EADV registry: ~2.5M EU27+UK mod-severe on systemic; PASI 75/90/100 targets standard."},
        "row.patientsK": {"note": "Global ex-US/EU ~15M mod-severe; Japan high biologic uptake; China NRDL expanding biologic access."},
        "us.wtpPct":     {"note": "~68% -- Medicare + commercial full biologic ladder; IL-23 (Skyrizi/Tremfya) + IL-17 (Cosentyx/Taltz/Bimzelx); Sotyktu TYK2."},
        "eu.wtpPct":     {"note": "~52% -- NICE/G-BA cover full class; adalimumab biosim first-line ~80% share; IL-23/IL-17 2L."},
        "row.wtpPct":    {"note": "~15% -- MTX + phototherapy + adalimumab biosim; Japan J-DPS covers IL-23/IL-17 broadly."},
        "us.priceK":     {"note": "Blended $52K: Humira biosim $18K + Skyrizi $85K + Tremfya $75K + Cosentyx $60K + Taltz $60K + Sotyktu $75K; MTX $2K."},
        "eu.priceK":     {"note": "~$26K blended -- adalim biosim ~$8K net + IL-23 ~$35K + IL-17 ~$28K."},
        "row.priceK":    {"note": "~$8K -- MTX/biosim anti-TNF dominant ex-Japan."},
        "penPct":        {"note": "~40% peak -- IL-23/IL-17 shift continues; TYK2 (Sotyktu) oral convenience; biosimilars extend access."}
    },
    "dermatology.inflammatory_derm.psoriasis_topical": {
        "us.patientsK":  {"note": "NPF: ~6M US psoriasis on topical-only therapy; mild-moderate 70% of PsO population."},
        "eu.patientsK":  {"note": "EADV: ~10M EU27+UK topical-managed psoriasis; Dovobet/Enstilar vit-D + steroid combos standard."},
        "row.patientsK": {"note": "Global ex-US/EU ~80M topical PsO; calcipotriol + betamethasone generics widespread."},
        "us.wtpPct":     {"note": "~50% -- commercial/Medicare cover Vtama (tapinarof) + Zoryve (roflumilast) + generic calcipotriol/steroids."},
        "eu.wtpPct":     {"note": "~40% -- NICE approved Vtama/Zoryve; generic vit-D analog + steroid combos dominant."},
        "row.wtpPct":    {"note": "~18% -- TCS generics + coal tar; novel topicals minimal; Japan maxacalcitol standard."},
        "us.priceK":     {"note": "Blended $1.5K: Vtama ~$1.5K/tube + Zoryve $1K + Dovobet/Enstilar $400 + generic calcipotriol/steroid $50."},
        "eu.priceK":     {"note": "~$0.5K blended -- generic calcipotriol + steroid combos dominate; Vtama/Zoryve net ~$800."},
        "row.priceK":    {"note": "~$0.1K -- calcipotriol/betamethasone generics; coal tar preparations."},
        "penPct":        {"note": "~10% peak -- non-steroidal novel topicals (Vtama, Zoryve) shift from chronic TCS use concerns."}
    },

    # ============================================================
    # DERMATOLOGY - RARE SKIN
    # ============================================================
    "dermatology.rare_skin.alopecia_areata": {
        "us.patientsK":  {"note": "National Alopecia Areata Foundation: ~300K US AA active; ~700K lifetime risk; ~20% severe (AT/AU)."},
        "eu.patientsK":  {"note": "EADV: ~450K EU27+UK AA active; SALT severity scale; autoimmune comorbidity common."},
        "row.patientsK": {"note": "Global ex-US/EU ~4M AA; Japan JAK inhibitor early adopter; China limited novel access."},
        "us.wtpPct":     {"note": "~45% -- Olumiant (baricitinib, 2022) + Litfulo (ritlecitinib, 2023) Medicare/commercial; intralesional steroids off-label."},
        "eu.wtpPct":     {"note": "~32% -- NICE/G-BA approved Olumiant/Litfulo severe AA; topical/intralesional steroids standard baseline."},
        "row.wtpPct":    {"note": "~10% -- Japan approved baricitinib/ritlecitinib; topical minoxidil + steroids elsewhere."},
        "us.priceK":     {"note": "Blended $42K: Olumiant $30K + Litfulo $50K (severe AA SALT>=50); topical minoxidil + steroids $500 baseline."},
        "eu.priceK":     {"note": "~$22K blended -- Olumiant net ~$18K + Litfulo ~$30K; restricted to severe."},
        "row.priceK":    {"note": "~$4K -- minoxidil + steroids + limited JAKi access in Japan."},
        "penPct":        {"note": "~20% peak -- JAKi class expanding (Rinvoq, deuruxolitinib pipeline); severe AA first, moderate expansion next."}
    },
    "dermatology.rare_skin.deb": {
        "us.patientsK":  {"note": "debra of America: ~3K US DEB (dystrophic EB); ~200-500 severe RDEB; COL7A1 mutation; ultra-rare."},
        "eu.patientsK":  {"note": "EB-CLINET: ~4K EU27+UK DEB; ~600 severe RDEB; DEBRA International support network."},
        "row.patientsK": {"note": "Global ex-US/EU ~20K DEB; consanguinity areas higher incidence; Middle East/South Asia."},
        "us.wtpPct":     {"note": "~80% -- Vyjuvek (beremagene geperpavec, 2023) + Filsuvez (birch bark, 2024) + Zevaskyn (pz-cel, 2025) covered; wound care supplies."},
        "eu.wtpPct":     {"note": "~65% -- EMA approved Filsuvez; Vyjuvek/Zevaskyn rolling out; ERN-Skin specialist centers."},
        "row.wtpPct":    {"note": "~15% -- wound care + supportive; gene/cell therapy access minimal; Japan PMDA evaluating."},
        "us.priceK":     {"note": "Blended $800K: Vyjuvek $600K/yr + Zevaskyn ~$3M one-time (spread) + Filsuvez $100K + wound care $50K baseline."},
        "eu.priceK":     {"note": "~$300K blended -- Filsuvez ~$60K + wound care + selective gene therapy access."},
        "row.priceK":    {"note": "~$25K -- wound care supplies + pain management; novel therapy access rare."},
        "penPct":        {"note": "~60% peak -- Vyjuvek/Zevaskyn/Filsuvez expanding rapidly; first disease-modifying therapies in DEB history."}
    },
    "dermatology.rare_skin.hailey_hailey": {
        "us.patientsK":  {"note": "NORD: ~2K US Hailey-Hailey Disease; ~1:50K prevalence; ATP2C1 mutation; autosomal dominant."},
        "eu.patientsK":  {"note": "Orphanet: ~3K EU27+UK Hailey-Hailey; intertriginous erosions; heat/friction triggers."},
        "row.patientsK": {"note": "Global ex-US/EU ~15K Hailey-Hailey; underdiagnosed; often misdiagnosed as candidiasis or intertrigo."},
        "us.wtpPct":     {"note": "~30% -- no FDA-approved therapy; off-label topical steroids + antibiotics + botulinum toxin + laser."},
        "eu.wtpPct":     {"note": "~25% -- no EMA approval; off-label same as US; dermabrasion/laser specialist centers."},
        "row.wtpPct":    {"note": "~8% -- topical steroids + antibiotics; specialist access limited."},
        "us.priceK":     {"note": "Blended $3K: off-label TCS/TCI generic $200 + antibiotics $500 + botulinum toxin $2K/session + laser procedures $3-5K."},
        "eu.priceK":     {"note": "~$1.5K blended -- off-label generics + selective procedural interventions."},
        "row.priceK":    {"note": "~$0.3K -- topical steroids + antibiotics generic."},
        "penPct":        {"note": "~10% peak -- no approved therapy; Notch pathway + topical JAK pipeline early-stage; niche specialty."}
    },
    "dermatology.rare_skin.vitiligo": {
        "us.patientsK":  {"note": "American Vitiligo Research Foundation: ~1.5M US vitiligo; ~1% prevalence; non-segmental most common."},
        "eu.patientsK":  {"note": "EADV VETF: ~2M EU27+UK vitiligo; VES/VASI severity; facial/hand involvement drives treatment demand."},
        "row.patientsK": {"note": "Global ex-US/EU ~60M vitiligo; India highest prevalence + disease burden; stigma drives treatment demand."},
        "us.wtpPct":     {"note": "~50% -- Opzelura (ruxolitinib, 2022 first FDA vitiligo approval) commercial/Medicare; NB-UVB phototherapy covered."},
        "eu.wtpPct":     {"note": "~35% -- NICE approved Opzelura nonsegmental; phototherapy + topical steroids/TCI standard baseline."},
        "row.wtpPct":    {"note": "~12% -- topical steroids + NB-UVB; Opzelura access limited; India extensive phototherapy network."},
        "us.priceK":     {"note": "Blended $8K: Opzelura $2.5K/tube chronic use ~$15K/yr (30% pts) + NB-UVB $3K/yr + TCS/TCI generic $200."},
        "eu.priceK":     {"note": "~$3K blended -- Opzelura net ~$10K + generic TCS/TCI + phototherapy."},
        "row.priceK":    {"note": "~$0.5K -- TCS/TCI generics + phototherapy; novel topicals minimal."},
        "penPct":        {"note": "~15% peak -- Opzelura first-in-class; upadacitinib + povorcitinib oral JAKi pipeline expanding severe cohort."}
    },
}
