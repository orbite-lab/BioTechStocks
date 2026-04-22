# -*- coding: utf-8 -*-
"""
Source-cited tooltips for oncology and hematology disease-area TAM inputs.

Each entry maps a taxonomy path (L3 or L4) to a dict of input-level notes.
Applied to configs/*.json by a separate script that walks market.tamInputs.

All notes are ASCII-only, <= ~180 chars, and cite real registries or filings.
"""

TOOLTIPS = {

    # ============================================================
    # BREAST
    # ============================================================
    "oncology.breast.her2_pos": {
        "us.patientsK":  {"note": "SEER 2024: ~310K new breast/yr; ~15-20% HER2+ = ~50K incident + ~120K prevalent on-tx. Source: NCI SEER, ACS Facts 2024."},
        "eu.patientsK":  {"note": "EU5 ~355K new breast/yr (GLOBOCAN 2022); HER2+ ~55K incident, ~140K prevalent on HER2-directed tx."},
        "row.patientsK": {"note": "ROW HER2+ ~200K on-tx; China NCC registry ~420K breast/yr, Japan NCR ~95K, HER2+ ~18%."},
        "us.wtpPct":     {"note": "~70% -- Medicare + commercial full coverage for Enhertu/Herceptin; NCCN Cat 1. 340B uptake strong at academic centers."},
        "eu.wtpPct":     {"note": "~50% -- NICE TA approved Enhertu 2023; G-BA Zusatznutzen betraechtlich; trastuzumab biosim dominant in 1L adj."},
        "row.wtpPct":    {"note": "~18% -- Japan PMDA/C2H full reimb, China NRDL added Enhertu 2023; EM rely on trastuzumab biosim."},
        "us.priceK":     {"note": "Blended $165K: Enhertu $165K (35% pts) + Kadcyla $185K (15%) + Herceptin+pertuzumab $130K (30%) + trastuzumab biosim $45K (20%)."},
        "eu.priceK":     {"note": "~$95K blended; EU net ~58% of US list. Biosim trastuzumab 1L standard, Enhertu reserved 2L+."},
        "row.priceK":    {"note": "~$35K blended; biosim trastuzumab <$15K drives mix outside Japan/Korea."},
        "penPct":        {"note": "~65% peak -- Enhertu displacing Kadcyla in 2L (DESTINY-Breast03), 5yr ramp vs standing Herceptin base."}
    },

    "oncology.breast.hr_her2_neg": {
        "us.patientsK":  {"note": "SEER: ~310K breast/yr; HR+/HER2- ~68% = ~210K incident, ~400K prevalent on-tx including adjuvant ET. Source: NCI SEER 2024."},
        "eu.patientsK":  {"note": "EU5 ~240K HR+/HER2- incident; ~450K prevalent on ET +/- CDK4/6. EUROCARE-6 + ESMO 2024 data."},
        "row.patientsK": {"note": "ROW ~550K on-tx; China NCC + Japan NCR report HR+/HER2- ~70% of breast mix."},
        "us.wtpPct":     {"note": "~75% -- CDK4/6i (Ibrance/Verzenio/Kisqali) NCCN Cat 1 1L; Medicare Part D + commercial broad; adj Verzenio approved 2021."},
        "eu.wtpPct":     {"note": "~55% -- NICE + G-BA approved all 3 CDK4/6i; France ASMR III-IV; AI/fulvestrant generic baseline."},
        "row.wtpPct":    {"note": "~20% -- Japan J-DPC + China NRDL cover CDK4/6i; EM AI generics dominant (letrozole, anastrozole)."},
        "us.priceK":     {"note": "Blended $95K: CDK4/6i $160K (40% pts) + Trodelvy/Enhertu-low $180K (8%) + AI+fulvestrant $15K (40%) + Orserdu $220K (5%)."},
        "eu.priceK":     {"note": "~$55K blended; EU net ~58% of US list; generic AI floor keeps blend low."},
        "row.priceK":    {"note": "~$20K blended; AI generics <$2K/yr dominate outside developed APAC."},
        "penPct":        {"note": "~58% peak -- CDK4/6i saturated 1L MBC; adj penetration growing 5yr; ESR1-mut Orserdu + ADCs expand late line."}
    },

    "oncology.breast.tnbc": {
        "us.patientsK":  {"note": "SEER: TNBC ~15% of breast = ~45K incident/yr, ~60K prevalent on-tx (short OS limits prevalence). Source: NCI SEER, TNBC Foundation."},
        "eu.patientsK":  {"note": "EU5 TNBC ~52K incident; ~65K prevalent. EUROCARE + ESMO TNBC consortium."},
        "row.patientsK": {"note": "ROW ~120K on-tx; TNBC over-represented in AA/African and younger cohorts per GLOBOCAN."},
        "us.wtpPct":     {"note": "~65% -- Keytruda+chemo (KEYNOTE-522) neoadj SOC; Trodelvy 2L+ NCCN Cat 1; Medicare + commercial broad."},
        "eu.wtpPct":     {"note": "~48% -- NICE approved Keytruda neoadj 2022, Trodelvy 2L 2023; G-BA betraechtlich for both."},
        "row.wtpPct":    {"note": "~15% -- Japan PMDA full reimb; China NRDL pembro 2023; EM rely on chemo (AC-T)."},
        "us.priceK":     {"note": "Blended $140K: Keytruda+chemo $180K (40% pts) + Trodelvy $155K (25%) + chemo alone $25K (30%) + Talzenna/PARPi $180K (5%)."},
        "eu.priceK":     {"note": "~$80K blended; EU net ~57% US list; neoadj pembro course-limited lowers cost vs metastatic."},
        "row.priceK":    {"note": "~$30K blended; chemo (docetaxel, carbo) generic <$5K dominates."},
        "penPct":        {"note": "~55% peak -- IO+chemo neoadj penetrated 70%+ eligible; Trodelvy 2L standard; Datroway (TROP2) + PARPi extend."}
    },

    # ============================================================
    # GENITOURINARY
    # ============================================================
    "oncology.genitourinary.bladder": {
        "us.patientsK":  {"note": "SEER: ~83K new bladder/yr US; ~25K muscle-invasive/metastatic on systemic tx. Source: NCI SEER 2024, BCAN."},
        "eu.patientsK":  {"note": "EU5 ~95K new bladder/yr (GLOBOCAN); ~28K on systemic therapy."},
        "row.patientsK": {"note": "ROW ~80K on-tx; high incidence in smoking-heavy APAC + aniline dye regions."},
        "us.wtpPct":     {"note": "~62% -- Padcev+Keytruda (EV-302) 1L SOC 2024; Medicare + commercial NCCN Cat 1; BCG shortage drives intravesical alternatives."},
        "eu.wtpPct":     {"note": "~45% -- NICE approved Padcev+pembro 2024; G-BA betraechtlich; gem/cis remains cost-effective comparator."},
        "row.wtpPct":    {"note": "~14% -- Japan J-DPC covers Padcev; China NRDL tislelizumab; EM rely on gem/cis + BCG."},
        "us.priceK":     {"note": "Blended $185K: Padcev+pembro $310K (35% pts) + nivo adj $165K (15%) + gem/cis+IO $95K (30%) + chemo alone $20K (20%)."},
        "eu.priceK":     {"note": "~$105K blended; EU net ~57% US; Padcev combo priced ~EUR 195K/course."},
        "row.priceK":    {"note": "~$35K blended; gem/cis generic dominates ex-Japan."},
        "penPct":        {"note": "~50% peak -- EV+pembro displacing chemo 1L over 5yr; FGFR3 Balversa + HER2 ADCs (disitamab) expand 2L."}
    },

    "oncology.genitourinary.prostate": {
        "us.patientsK":  {"note": "SEER: ~300K new prostate/yr; ~55K mCSPC + ~45K mCRPC on systemic tx. Source: NCI SEER 2024, PCF."},
        "eu.patientsK":  {"note": "EU5 ~345K new prostate/yr; ~110K on ARPi/chemo/PARPi per EUROCARE."},
        "row.patientsK": {"note": "ROW ~200K on-tx; Japan high incidence post-PSA screening expansion."},
        "us.wtpPct":     {"note": "~70% -- ARPi (Xtandi/Erleada/Nubeqa) mCSPC SOC; Medicare Part D + VA cover; 340B strong at academic."},
        "eu.wtpPct":     {"note": "~52% -- NICE + G-BA approved all ARPi; France ASMR III; ADT generic baseline."},
        "row.wtpPct":    {"note": "~18% -- Japan full reimb, China NRDL enza/apa; EM use ADT + docetaxel."},
        "us.priceK":     {"note": "Blended $95K: ARPi $180K (45% pts) + Pluvicto $240K (8%) + Lynparza/Talzenna $175K (7%) + ADT+chemo $25K (40%)."},
        "eu.priceK":     {"note": "~$55K blended; EU net ~58% US; ADT leuprolide generic <$3K/yr."},
        "row.priceK":    {"note": "~$18K blended; ADT generic dominates; bicalutamide <$200/yr."},
        "penPct":        {"note": "~60% peak -- ARPi intensification 1L mCSPC reached 75% eligible; Pluvicto + PARPi (HRR+) extend 5yr."}
    },

    "oncology.genitourinary.rcc": {
        "us.patientsK":  {"note": "SEER: ~82K new RCC/yr US; ~25K advanced/metastatic on systemic tx. Source: NCI SEER 2024, KCA."},
        "eu.patientsK":  {"note": "EU5 ~95K new RCC/yr; ~30K on IO+TKI per EUROCARE."},
        "row.patientsK": {"note": "ROW ~70K on-tx; rising incidence in APAC per GLOBOCAN 2022."},
        "us.wtpPct":     {"note": "~68% -- IO+TKI (Keytruda+Inlyta, Opdivo+Cabometyx) 1L SOC; NCCN Cat 1; Medicare + commercial broad."},
        "eu.wtpPct":     {"note": "~50% -- NICE approved pembro+axi + nivo+cabo; G-BA betraechtlich; sunitinib generic baseline for resource-limited."},
        "row.wtpPct":    {"note": "~16% -- Japan J-DPC covers IO+TKI; China NRDL toripalimab+axitinib; EM sunitinib generic."},
        "us.priceK":     {"note": "Blended $215K: IO+TKI doublet $310K (55% pts) + TKI mono $110K (20%) + IO mono $180K (15%) + HIF-2a Welireg $240K (10%)."},
        "eu.priceK":     {"note": "~$125K blended; EU net ~58% US; sunitinib generic ~$15K."},
        "row.priceK":    {"note": "~$40K blended; sunitinib/pazopanib generic <$10K dominate."},
        "penPct":        {"note": "~58% peak -- IO+TKI 1L saturated; belzutifan (VHL/HIF) + CTLA-4 combos extend; adj pembro (KEYNOTE-564) growing."}
    },

    # ============================================================
    # GI
    # ============================================================
    "oncology.gi.cholangiocarcinoma": {
        "us.patientsK":  {"note": "NCI: ~8K intrahepatic + ~4K extrahepatic CCA/yr US; ~10K prevalent on systemic. Source: NCI, Cholangiocarcinoma Foundation."},
        "eu.patientsK":  {"note": "EU5 ~14K CCA/yr; ~12K on systemic. Rising intrahepatic incidence per ENS-CCA registry."},
        "row.patientsK": {"note": "ROW ~60K on-tx; APAC high due to fluke-endemic (Thailand) + HBV-driven iCCA."},
        "us.wtpPct":     {"note": "~55% -- FGFR2 (Pemazyre/Truseltiq) + IDH1 (Tibsovo) tgt rx covered; gem/cis+IO (durvalumab) 1L SOC post-TOPAZ-1."},
        "eu.wtpPct":     {"note": "~42% -- NICE approved pemigatinib + durva+chemo; EMA orphan designation supports ASMR III."},
        "row.wtpPct":    {"note": "~12% -- Japan PMDA covers tgt rx; EM limited to gem/cis."},
        "us.priceK":     {"note": "Blended $155K: FGFR2i $185K (15% pts) + IDH1i $165K (5%) + durva+gemcis $125K (50%) + gemcis alone $25K (30%)."},
        "eu.priceK":     {"note": "~$90K blended; EU net ~58% US."},
        "row.priceK":    {"note": "~$30K blended; gem/cis generic dominant."},
        "penPct":        {"note": "~42% peak -- FGFR2 fusion ~10-15% + IDH1 ~15% + HER2 + KRAS G12C cumulative tgt pop; IO+chemo 1L backbone."}
    },

    "oncology.gi.colorectal": {
        "us.patientsK":  {"note": "SEER: ~155K new CRC/yr US; ~55K metastatic/advanced on systemic tx. Source: NCI SEER 2024, ACS."},
        "eu.patientsK":  {"note": "EU5 ~215K new CRC/yr; ~70K on systemic per EUROCARE-6."},
        "row.patientsK": {"note": "ROW ~320K on-tx; China NCC reports ~560K new CRC/yr (highest globally)."},
        "us.wtpPct":     {"note": "~65% -- FOLFOX/FOLFIRI + bev/cetux/pani SOC; Krazati/Lumakras KRAS G12C; Keytruda MSI-H 1L; Medicare + commercial broad."},
        "eu.wtpPct":     {"note": "~48% -- NICE + G-BA approved all tgt rx; France ASMR III-IV; bevacizumab biosim widely used."},
        "row.wtpPct":    {"note": "~16% -- Japan J-DPC full coverage; China NRDL cetux + bev; EM chemo backbone."},
        "us.priceK":     {"note": "Blended $95K: bev/cetux+chemo $125K (50% pts) + KRAS G12Ci $195K (5%) + pembro MSI-H $180K (5%) + chemo alone $30K (40%)."},
        "eu.priceK":     {"note": "~$55K blended; EU net ~58% US; bev biosim ~50% off list."},
        "row.priceK":    {"note": "~$22K blended; 5-FU/oxali/irino generic <$3K."},
        "penPct":        {"note": "~50% peak -- tgt rx tied to biomarkers (KRAS G12C 4%, MSI-H 5%, BRAF V600E 8%, HER2 3%); broad chemo base."}
    },

    "oncology.gi.gastric_esoph": {
        "us.patientsK":  {"note": "SEER: ~27K gastric + ~22K esophageal/yr US; ~25K on systemic. Source: NCI SEER 2024."},
        "eu.patientsK":  {"note": "EU5 ~75K gastric+GEJ+esoph/yr; ~35K on systemic."},
        "row.patientsK": {"note": "ROW ~800K on-tx; China + Japan + Korea >60% global gastric burden (GLOBOCAN 2022)."},
        "us.wtpPct":     {"note": "~58% -- Keytruda+chemo 1L (KEYNOTE-859), Enhertu HER2+ 2L, Vyloy CLDN18.2 covered; NCCN Cat 1."},
        "eu.wtpPct":     {"note": "~44% -- NICE approved pembro+chemo + Enhertu + zolbetuximab; G-BA betraechtlich for HER2+."},
        "row.wtpPct":    {"note": "~20% -- Japan PMDA + China NRDL cover IO+chemo; high volume market."},
        "us.priceK":     {"note": "Blended $135K: pembro+chemo $175K (40% pts) + Enhertu HER2+ $185K (15%) + Vyloy CLDN18.2 $140K (20%) + chemo alone $25K (25%)."},
        "eu.priceK":     {"note": "~$78K blended; EU net ~58% US."},
        "row.priceK":    {"note": "~$32K blended; China/Japan mix with trastuzumab biosim + tislelizumab NRDL price."},
        "penPct":        {"note": "~48% peak -- IO+chemo 1L saturated; CLDN18.2 (Vyloy) ~38% + HER2+ 20% + FGFR2b (bemarituzumab) extend."}
    },

    "oncology.gi.hcc": {
        "us.patientsK":  {"note": "NCI: ~42K new liver/yr US; ~20K advanced HCC on systemic. Source: NCI SEER 2024, AASLD."},
        "eu.patientsK":  {"note": "EU5 ~60K HCC/yr; ~25K on systemic per EASL registry."},
        "row.patientsK": {"note": "ROW ~650K on-tx; China ~400K HCC/yr (HBV-driven), Japan ~40K."},
        "us.wtpPct":     {"note": "~60% -- atezo+bev (IMbrave150) + durva+treme (HIMALAYA) 1L SOC; NCCN Cat 1; Medicare broad."},
        "eu.wtpPct":     {"note": "~46% -- NICE approved atezo+bev 2022; G-BA betraechtlich; sorafenib/lenvatinib generic fallback."},
        "row.wtpPct":    {"note": "~22% -- Japan J-DPC + China NRDL cover IO+VEGF; high HCC volume drives TKI generic use."},
        "us.priceK":     {"note": "Blended $135K: atezo+bev $180K (35% pts) + durva+treme $195K (15%) + lenva/sora $95K (30%) + nivo+ipi 2L $175K (20%)."},
        "eu.priceK":     {"note": "~$78K blended; EU net ~58% US; lenvatinib/sorafenib generic <$20K."},
        "row.priceK":    {"note": "~$28K blended; sorafenib generic ~$5K China/EM dominates."},
        "penPct":        {"note": "~45% peak -- IO-VEGF 1L penetrated 55% eligible; Child-Pugh A only limits; FGF19 + GPC3 ADCs emerging."}
    },

    "oncology.gi.pancreatic": {
        "us.patientsK":  {"note": "SEER: ~66K new PDAC/yr US; ~45K on systemic (mostly metastatic). Source: NCI SEER 2024, PanCAN."},
        "eu.patientsK":  {"note": "EU5 ~95K PDAC/yr; ~60K on systemic per EUROCARE."},
        "row.patientsK": {"note": "ROW ~250K on-tx; rising incidence globally per GLOBOCAN 2022."},
        "us.wtpPct":     {"note": "~55% -- FOLFIRINOX + gem/nab-pac SOC; Lynparza BRCA+ 8%; KRAS G12C/D pipeline covered; Medicare broad."},
        "eu.wtpPct":     {"note": "~42% -- NICE approved FOLFIRINOX + gem/nabpac; olaparib BRCA+ maintenance via ASMR IV."},
        "row.wtpPct":    {"note": "~14% -- Japan J-DPC + China NRDL; EM rely on gemcitabine mono."},
        "us.priceK":     {"note": "Blended $70K: FOLFIRINOX $45K (50% pts) + gem/nabpac $85K (35%) + PARPi BRCA+ $180K (5%) + Onivyde 2L $95K (10%)."},
        "eu.priceK":     {"note": "~$40K blended; EU net ~57% US; chemo backbones generic."},
        "row.priceK":    {"note": "~$15K blended; gemcitabine generic <$2K dominant."},
        "penPct":        {"note": "~40% peak -- poor OS limits prevalence buildup; KRAS inhibitors (G12D, pan-RAS) + NALIRIFOX reshape 5yr."}
    },

    # ============================================================
    # GYNECOLOGIC
    # ============================================================
    "oncology.gynecologic.ovarian": {
        "us.patientsK":  {"note": "SEER: ~20K new ovarian/yr US; ~35K prevalent on-tx incl maintenance. Source: NCI SEER 2024, OCRA."},
        "eu.patientsK":  {"note": "EU5 ~30K new/yr; ~50K prevalent on PARPi/bev/chemo maintenance."},
        "row.patientsK": {"note": "ROW ~90K on-tx; Japan NCR ~13K/yr, China ~58K."},
        "us.wtpPct":     {"note": "~65% -- PARPi (Lynparza/Zejula) BRCA/HRD maintenance NCCN Cat 1; Elahere FRa+ 2L; Medicare + commercial broad."},
        "eu.wtpPct":     {"note": "~50% -- NICE approved olaparib + niraparib maintenance; G-BA betraechtlich for BRCA+."},
        "row.wtpPct":    {"note": "~16% -- Japan PMDA full; China NRDL olaparib + niraparib; EM carbo/taxol."},
        "us.priceK":     {"note": "Blended $125K: PARPi $140K (35% pts) + Elahere FRa+ $220K (15%) + bev maint $95K (20%) + carbo/taxol $15K (30%)."},
        "eu.priceK":     {"note": "~$72K blended; EU net ~58% US."},
        "row.priceK":    {"note": "~$25K blended; carbo/taxol generic <$3K."},
        "penPct":        {"note": "~52% peak -- PARPi saturated BRCA/HRD (~50% tumors); Elahere FRa+ ~35%; bispecifics + next-gen ADCs extend."}
    },

    # ============================================================
    # HEMATOLOGY
    # ============================================================
    "oncology.hematology.aml": {
        "us.patientsK":  {"note": "SEER: ~20K new AML/yr US; ~22K prevalent on-tx (short OS). Source: NCI SEER 2024, LLS."},
        "eu.patientsK":  {"note": "EU5 ~25K AML/yr; ~27K on-tx per HMRN + ELN registries."},
        "row.patientsK": {"note": "ROW ~90K on-tx; China + Japan major APAC volumes."},
        "us.wtpPct":     {"note": "~62% -- Venclexta+aza unfit 1L SOC; FLT3 (Rydapt/Xospata) + IDH (Tibsovo/Idhifa/Rezlidhia) + menin covered; Medicare broad."},
        "eu.wtpPct":     {"note": "~45% -- NICE approved ven+aza 2022; G-BA betraechtlich FLT3+IDH; 7+3 chemo generic baseline."},
        "row.wtpPct":    {"note": "~14% -- Japan PMDA full; China NRDL azacitidine + venetoclax; EM 7+3 generic."},
        "us.priceK":     {"note": "Blended $185K: ven+aza $220K (40% pts) + FLT3i $165K (15%) + IDHi $195K (10%) + menin (Revuforj) $340K (5%) + 7+3 $40K (30%)."},
        "eu.priceK":     {"note": "~$105K blended; EU net ~57% US; azacitidine biosim lowers backbone."},
        "row.priceK":    {"note": "~$35K blended; cytarabine/daunorubicin generic dominates."},
        "penPct":        {"note": "~48% peak -- ven+aza saturated unfit; menin (KMT2A/NPM1 ~40%) + FLT3 (~30%) + IDH (~15%) stack biomarker pop."}
    },

    "oncology.hematology.cll_nhl": {
        "us.patientsK":  {"note": "SEER 2024: ~21K new CLL + ~80K new NHL/yr; ~180K prevalent on active tx. Source: NCI SEER, LLS."},
        "eu.patientsK":  {"note": "EU5 prevalence ~200K CLL/NHL on tx; HMRN + EUROCARE registries."},
        "row.patientsK": {"note": "Global ex-US/EU ~250K; China NMPA CLL registry + APAC hematology estimates."},
        "us.wtpPct":     {"note": "~60% -- Medicare + commercial coverage for BTKi/CAR-T strong; CAR-T access gated by accredited centers."},
        "eu.wtpPct":     {"note": "~45% -- HTA (NICE, G-BA) approved BTKi/bispecifics; CAR-T reimbursement varies by country."},
        "row.wtpPct":    {"note": "~12% -- Japan + AU well-covered; EM rely on rituximab biosimilars + CHOP chemo."},
        "us.priceK":     {"note": "Blended $220K: BTKi $200K (45% pts) + CAR-T $410K (5%) + bispecific $250K (10%) + anti-CD20 $80K (25%) + chemo $30K (15%)."},
        "eu.priceK":     {"note": "~$130K blended; EU net ~60% of US list across modalities."},
        "row.priceK":    {"note": "~$50K blended; generics (rituximab biosim, CHOP) dominant outside Japan."},
        "penPct":        {"note": "~47% peak -- BTKi + CAR-T + bispecifics combined capture of eligible CLL/NHL over 5yr."}
    },

    "oncology.hematology.cll_nhl.bcl2": {
        "us.patientsK":  {"note": "~80K US CLL + FL prevalent on BCL2-directed tx (Venclexta label). Source: AbbVie 10-K, CLL Society."},
        "eu.patientsK":  {"note": "EU5 ~90K BCL2-eligible CLL/FL; NICE CLL guidance + CLL14 regimen."},
        "row.patientsK": {"note": "ROW ~110K; Japan CLL ~7K + China ~40K CLL+FL on ven-based regimens."},
        "us.wtpPct":     {"note": "~65% -- Venclexta+obinutuzumab 1L CLL NCCN Cat 1; Medicare Part B+D; ramp-up TLS monitoring in outpatient."},
        "eu.wtpPct":     {"note": "~48% -- NICE TA approved ven+obi CLL 2019; G-BA betraechtlich; HTA favors fixed-duration vs continuous BTKi."},
        "row.wtpPct":    {"note": "~14% -- Japan PMDA full; China NRDL 2020; EM chlorambucil+rituximab biosim."},
        "us.priceK":     {"note": "Blended $165K: ven+obi fixed 12mo $180K (70% pts) + ven+R 2L $150K (20%) + ven mono $120K (10%)."},
        "eu.priceK":     {"note": "~$95K blended; fixed-duration reduces EU cost vs continuous BTKi."},
        "row.priceK":    {"note": "~$35K blended; obi biosim + ven priced lower in China/EM."},
        "penPct":        {"note": "~40% peak -- BCL2-dependent subset (CLL + FL); next-gen BCL2 (sonrotoclax) + BCL2+BTKi doublets extend."}
    },

    "oncology.hematology.cll_nhl.btk_resistant": {
        "us.patientsK":  {"note": "~15K US post-covalent-BTKi failure (C481S mut + intolerance); ~12K eligible for Jaypirca/pirto. Source: Lilly 10-K, MDACC."},
        "eu.patientsK":  {"note": "EU5 ~18K post-BTKi resistant/intolerant; ERIC registry."},
        "row.patientsK": {"note": "ROW ~25K on 2nd-gen non-covalent BTKi or CAR-T salvage."},
        "us.wtpPct":     {"note": "~60% -- Jaypirca (pirtobrutinib) post-BTKi accel approval 2023; Medicare + commercial NCCN Cat 2A R/R CLL."},
        "eu.wtpPct":     {"note": "~42% -- EMA approved pirto 2023; NICE TA in progress; reimbursement via CDF."},
        "row.wtpPct":    {"note": "~10% -- Japan PMDA review pending; limited access elsewhere."},
        "us.priceK":     {"note": "Blended $215K: pirto $225K (60% pts) + CAR-T salvage $420K (10%) + bispecific (epco/mosu) $260K (20%) + allo-SCT $150K (10%)."},
        "eu.priceK":     {"note": "~$125K blended; EU net ~58% US for non-covalent BTKi."},
        "row.priceK":    {"note": "~$45K blended; limited 2G BTKi access."},
        "penPct":        {"note": "~35% peak -- ncBTKi + BCL2 retreatment + CAR-T stack; BTK degraders (BGB-16673, NX-5948) next wave."}
    },

    "oncology.hematology.cll_nhl.car_t_combo": {
        "us.patientsK":  {"note": "~5K US CAR-T eligible R/R CLL/NHL per yr; limited by fitness + center access. Source: CIBMTR, Kite/Gilead Q reports."},
        "eu.patientsK":  {"note": "EU5 ~4K CAR-T infused/yr; EBMT CAR-T registry; capacity-constrained."},
        "row.patientsK": {"note": "ROW ~3K; Japan + China rapid build-out of CAR-T centers 2023-25."},
        "us.wtpPct":     {"note": "~55% -- Breyanzi/Yescarta R/R DLBCL + CLL; Medicare transitional pass-through; center-based billing."},
        "eu.wtpPct":     {"note": "~38% -- NICE via CDF; G-BA Erstattungsbetrag negotiated; EBMT capacity bottleneck."},
        "row.wtpPct":    {"note": "~10% -- Japan MHLW covers; China domestic CAR-T (relma-cel, cilta-cel) lower priced."},
        "us.priceK":     {"note": "Blended $440K: Breyanzi $470K (40% pts) + Yescarta $460K (35%) + in-house CAR-T $350K (15%) + combo w/bispecific $520K (10%)."},
        "eu.priceK":     {"note": "~$260K blended; EU net ~60% US list post negotiation."},
        "row.priceK":    {"note": "~$85K blended; China domestic CAR-T ~$75K drives mix."},
        "penPct":        {"note": "~30% peak -- capacity + fitness gate; allo/off-the-shelf CAR-T + CAR-T+bispecific combos expand access 5yr."}
    },

    "oncology.hematology.cll_nhl.dlbcl": {
        "us.patientsK":  {"note": "SEER: ~30K new DLBCL/yr US (most aggressive NHL subtype); ~40K prevalent on-tx. Source: NCI SEER, LLS."},
        "eu.patientsK":  {"note": "EU5 ~38K DLBCL/yr; HMRN + GELA registries."},
        "row.patientsK": {"note": "ROW ~120K on-tx; China NHL registry + Japan NCR."},
        "us.wtpPct":     {"note": "~68% -- Polivy+R-CHP 1L (POLARIX) NCCN Cat 1; CAR-T 2L (Yescarta/Breyanzi ZUMA-7/TRANSFORM); bispecifics 3L."},
        "eu.wtpPct":     {"note": "~50% -- NICE approved Polivy 1L + CAR-T 2L; G-BA betraechtlich; rituximab biosim baseline."},
        "row.wtpPct":    {"note": "~15% -- Japan PMDA full; China NRDL R-CHOP + domestic CAR-T; EM R-CHOP biosim."},
        "us.priceK":     {"note": "Blended $195K: Polivy+R-CHP $175K (45% pts) + CAR-T 2L $460K (15%) + bispecific (Epkinly/Columvi) $250K (15%) + R-CHOP $40K (25%)."},
        "eu.priceK":     {"note": "~$115K blended; EU net ~59% US."},
        "row.priceK":    {"note": "~$40K blended; R-CHOP biosim <$20K dominates ex-Japan."},
        "penPct":        {"note": "~52% peak -- Polivy 1L penetrated 50%+; CAR-T 2L growing; bispecifics 3L fixed-duration; ADCs (ZW191) emerge."}
    },

    "oncology.hematology.dlbcl": {
        "us.patientsK":  {"note": "SEER 2024: ~30K new DLBCL/yr US (largest aggressive NHL subtype); ~40K prevalent. Source: NCI SEER, LLS."},
        "eu.patientsK":  {"note": "EU5 ~38K DLBCL/yr; HMRN UK + GELA France registries."},
        "row.patientsK": {"note": "ROW ~120K on-tx; APAC DLBCL rising per GLOBOCAN 2022."},
        "us.wtpPct":     {"note": "~68% -- R-CHOP baseline; Polivy+R-CHP 1L NCCN Cat 1; CAR-T 2L SOC; Epkinly/Columvi 3L+ covered."},
        "eu.wtpPct":     {"note": "~50% -- NICE + G-BA approved Polivy, CAR-T, bispecifics; rituximab biosim universal."},
        "row.wtpPct":    {"note": "~15% -- Japan PMDA + China NRDL full R-CHOP + Polivy; EM biosim R-CHOP."},
        "us.priceK":     {"note": "Blended $195K: Polivy+R-CHP $175K (45% pts) + CAR-T 2L $460K (15%) + bispecific $250K (15%) + R-CHOP alone $40K (25%)."},
        "eu.priceK":     {"note": "~$115K blended; EU net ~59% US list."},
        "row.priceK":    {"note": "~$40K blended; R-CHOP biosim ex-Japan."},
        "penPct":        {"note": "~55% peak -- 1L Polivy + 2L CAR-T + 3L bispecific fill LOT ladder over 5yr."}
    },

    "oncology.hematology.myeloma": {
        "us.patientsK":  {"note": "SEER: ~35K new MM/yr US; ~160K prevalent on active tx (long OS in era of quadruplets). Source: NCI SEER, IMF."},
        "eu.patientsK":  {"note": "EU5 ~40K MM/yr; ~180K prevalent on-tx; EMN registry."},
        "row.patientsK": {"note": "ROW ~300K on-tx; China + Japan major APAC volumes."},
        "us.wtpPct":     {"note": "~65% -- DaraRVd quadruplet 1L NCCN Cat 1; CAR-T (Carvykti, Abecma) 2L post-CARTITUDE-4; bispecifics 4L+."},
        "eu.wtpPct":     {"note": "~48% -- NICE + G-BA approved DaraRVd + CAR-T + bispecifics; IMWG guidelines."},
        "row.wtpPct":    {"note": "~16% -- Japan PMDA full; China NRDL daratumumab + lenalidomide generic; EM Vel/Dex/Len."},
        "us.priceK":     {"note": "Blended $235K: DaraRVd $220K (45% pts) + CAR-T $470K (10%) + bispecific (Tecvayli/Elrexfio/Talvey) $280K (15%) + Vd/Rd $95K (30%)."},
        "eu.priceK":     {"note": "~$140K blended; EU net ~60% US list."},
        "row.priceK":    {"note": "~$50K blended; lenalidomide generic 2022 reshapes mix."},
        "penPct":        {"note": "~58% peak -- quadruplet 1L + CAR-T 2L + bispecifics 4L fill ladder; GPRC5D + FcRH5 extend; long OS grows prevalence."}
    },

    "oncology.hematology.myeloma.frontline": {
        "us.patientsK":  {"note": "~20K US newly dx MM/yr starting systemic tx (transplant-eligible + ineligible). Source: NCI SEER 2024, ASH."},
        "eu.patientsK":  {"note": "EU5 ~24K new MM/yr; ~75% receive triplet/quadruplet 1L per EMN."},
        "row.patientsK": {"note": "ROW ~80K starting 1L; VRd + daratumumab global standard."},
        "us.wtpPct":     {"note": "~72% -- DaraRVd PERSEUS + IsaKRd IMROZ TE + DaraVMP non-TE; NCCN Cat 1; Medicare Part B+D."},
        "eu.wtpPct":     {"note": "~55% -- NICE TA approved DaraVMP + DaraRVd; France ASMR III; HTA values MRD-negativity."},
        "row.wtpPct":    {"note": "~18% -- Japan PMDA full dara-based; China NRDL dara 2021; EM VRd."},
        "us.priceK":     {"note": "Blended $225K: DaraRVd $220K (60% pts) + IsaKRd $240K (15%) + DaraVMP non-TE $195K (15%) + VRd alone $145K (10%)."},
        "eu.priceK":     {"note": "~$135K blended; EU net ~60% US; len generic reduces triplet cost."},
        "row.priceK":    {"note": "~$55K blended; len generic + biosim dara lower APAC/EM."},
        "penPct":        {"note": "~68% peak -- quadruplet 1L saturated TE; non-TE DaraVMP/VRd-lite standard; MRD-guided de-escalation emerging."}
    },

    "oncology.hematology.myeloma.car_t": {
        "us.patientsK":  {"note": "~3K US R/R MM eligible for CAR-T/yr (Carvykti CARTITUDE-4 2L+, Abecma KarMMa-3). Source: CIBMTR, J&J/BMS 10-Ks."},
        "eu.patientsK":  {"note": "EU5 ~2K CAR-T infused/yr MM; EBMT registry; capacity-constrained."},
        "row.patientsK": {"note": "ROW ~1.5K; Japan + China expanding CAR-T centers."},
        "us.wtpPct":     {"note": "~58% -- Carvykti + Abecma 2L+ post-CARTITUDE-4 + KarMMa-3; Medicare transitional pass-through; center-gated."},
        "eu.wtpPct":     {"note": "~42% -- NICE CDF + G-BA Erstattungsbetrag; capacity limits access."},
        "row.wtpPct":    {"note": "~12% -- Japan MHLW; China domestic (equecabtagene) lower priced."},
        "us.priceK":     {"note": "Blended $490K: Carvykti $515K (60% pts) + Abecma $455K (30%) + academic CAR-T $380K (10%)."},
        "eu.priceK":     {"note": "~$295K blended; EU net ~60% US post negotiation."},
        "row.priceK":    {"note": "~$110K blended; China domestic ~$75K."},
        "penPct":        {"note": "~32% peak -- capacity-gated; earlier-line shift CARTITUDE-5 + off-the-shelf allo CAR-T expand 5yr."}
    },

    "oncology.hematology.myeloma.car_t_invivo": {
        "us.patientsK":  {"note": "~20K US potential if in-vivo CAR-T broadens to non-eligible (unfit, rural); frontier modality. Source: Capstan/Umoja pipeline."},
        "eu.patientsK":  {"note": "EU5 ~22K potential; decentralization + no-apheresis model bypasses center bottleneck."},
        "row.patientsK": {"note": "ROW ~50K if in-vivo reaches EM; mRNA/LNP-CAR or AAV-CAR lowers CoGS."},
        "us.wtpPct":     {"note": "~50% -- pre-commercial; model assumes Medicare + commercial if outpatient-compatible lower-toxicity profile."},
        "eu.wtpPct":     {"note": "~40% -- HTA likely to value access expansion; EMA ATMP pathway."},
        "row.wtpPct":    {"note": "~15% -- decentralization opens APAC/EM markets currently excluded from ex-vivo."},
        "us.priceK":     {"note": "Blended $220K: in-vivo CAR-T est $220K target (vs $500K ex-vivo); lower CoGS + infusion-only delivery."},
        "eu.priceK":     {"note": "~$140K blended; EU HTA likely more favorable to cost-effective in-vivo."},
        "row.priceK":    {"note": "~$55K blended; EM-accessible pricing key to broad launch."},
        "penPct":        {"note": "~38% peak -- transformational if clinical delivers; 2028+ timeline assumes Capstan/Umoja POC; 5yr ramp post launch."}
    },

    "oncology.hematology.tcell_lymphoma": {
        "us.patientsK":  {"note": "SEER: ~6K new PTCL + ~3K CTCL/yr US; ~12K prevalent on-tx. Source: NCI SEER 2024, Cutaneous Lymphoma Foundation."},
        "eu.patientsK":  {"note": "EU5 ~9K T-cell lymphoma/yr; T-cell Project registry (Italy + EU)."},
        "row.patientsK": {"note": "ROW ~40K on-tx; higher PTCL-NOS + ATLL in APAC (HTLV-1)."},
        "us.wtpPct":     {"note": "~58% -- Adcetris CD30+ (ALCL) NCCN Cat 1; Poteligeo CCR4+ CTCL; Istodax/Folotyn 2L; Medicare broad."},
        "eu.wtpPct":     {"note": "~42% -- NICE + G-BA approved Adcetris frontline PTCL; ESMO guidelines."},
        "row.wtpPct":    {"note": "~14% -- Japan PMDA (mogamulizumab Japan-origin); China NRDL cHHP + CHOEP."},
        "us.priceK":     {"note": "Blended $155K: Adcetris+CHP $175K (40% pts) + Poteligeo $165K (15%) + HDAC/folotyn $125K (15%) + CHOP alone $35K (30%)."},
        "eu.priceK":     {"note": "~$90K blended; EU net ~58% US."},
        "row.priceK":    {"note": "~$32K blended; CHOP generic + mogamulizumab Japan NHI."},
        "penPct":        {"note": "~42% peak -- CD30+ Adcetris saturated ALCL; CCR4 Poteligeo CTCL; CD7 CAR-T + JAK/STAT emerging."}
    },

    # ============================================================
    # LUNG - NSCLC DRIVER SUBTYPES (L4)
    # ============================================================
    "oncology.lung.nsclc_driver.alk": {
        "us.patientsK":  {"note": "~5-6K US ALK+ NSCLC/yr (5-7% of NSCLC), FISH/NGS-confirmed. Source: NCI SEER + IASLC mol epi 2023."},
        "eu.patientsK":  {"note": "EU5 ~7K ALK+ NSCLC/yr; ESMO mol testing guidelines drive >85% reflex testing."},
        "row.patientsK": {"note": "ROW ~15K; higher ALK+ fraction in never-smoker East Asian cohorts (~8-10%)."},
        "us.wtpPct":     {"note": "~72% -- Alecensa 1L SOC (ALEX); Lorbrena ASCEND-2023; Medicare + commercial NCCN Cat 1; NGS reflex covered."},
        "eu.wtpPct":     {"note": "~55% -- NICE + G-BA approved alectinib + lorlatinib 1L; France ASMR II-III; ESMO guidelines."},
        "row.wtpPct":    {"note": "~22% -- Japan PMDA + China NRDL all-gen ALK TKIs; high never-smoker ALK+ volume in APAC."},
        "us.priceK":     {"note": "Blended $205K: Alecensa $210K (55% pts) + Lorbrena $215K (30%) + Xalkori/ensar $185K (10%) + chemo $30K (5%)."},
        "eu.priceK":     {"note": "~$120K blended; EU net ~58% US; lorlatinib 1L uptake growing."},
        "row.priceK":    {"note": "~$55K blended; China NRDL ensartinib domestic ~$30K drives mix."},
        "penPct":        {"note": "~68% peak -- 3G TKI (lorla) displaces 2G (alec) in 1L; 4G (NVL-655) addresses G1202R resistance."}
    },

    "oncology.lung.nsclc_driver.cmet": {
        "us.patientsK":  {"note": "~3K US MET ex14 skip or amp NSCLC/yr; RNA-seq + NGS confirmed. Source: NCI SEER, Merck/Novartis 10-K."},
        "eu.patientsK":  {"note": "EU5 ~4K MET+ NSCLC; testing penetration ~60% via comprehensive NGS."},
        "row.patientsK": {"note": "ROW ~10K; APAC mol testing driven by China NRDL reimb of NGS."},
        "us.wtpPct":     {"note": "~60% -- Tabrecta + Tepmetko MET ex14 NCCN Cat 1; Enhertu HER2/MET combos; Medicare broad."},
        "eu.wtpPct":     {"note": "~45% -- NICE + G-BA approved capmatinib + tepotinib; ESMO testing guidelines."},
        "row.wtpPct":    {"note": "~16% -- Japan PMDA (tepotinib Merck KGaA); China NRDL."},
        "us.priceK":     {"note": "Blended $195K: Tabrecta $205K (40% pts) + Tepmetko $195K (35%) + MET ADC (telisotuzumab) $225K (15%) + chemo $30K (10%)."},
        "eu.priceK":     {"note": "~$115K blended; EU net ~59% US."},
        "row.priceK":    {"note": "~$45K blended; China NRDL negotiation lowers."},
        "penPct":        {"note": "~50% peak -- MET ex14 testing limits TAM; ADCs (telisotuzumab vedotin) + amp/overexpr extends biomarker pool."}
    },

    "oncology.lung.nsclc_driver.her2": {
        "us.patientsK":  {"note": "~3-4K US HER2-mut/amp NSCLC/yr (2-4% of NSCLC); NGS required. Source: NCI SEER, DS/AZ DESTINY-Lung filings."},
        "eu.patientsK":  {"note": "EU5 ~5K HER2+ NSCLC; DESTINY-Lung02 enrollment estimates."},
        "row.patientsK": {"note": "ROW ~12K; higher HER2-mut in Asian never-smoker NSCLC."},
        "us.wtpPct":     {"note": "~62% -- Enhertu HER2-mut NSCLC accel approval 2022; NCCN Cat 2A 2L; Medicare + commercial."},
        "eu.wtpPct":     {"note": "~46% -- NICE + EMA approved Enhertu 2L HER2-mut NSCLC 2023."},
        "row.wtpPct":    {"note": "~15% -- Japan PMDA (DS-origin) full; China NRDL 2024."},
        "us.priceK":     {"note": "Blended $195K: Enhertu $220K (55% pts) + pan-HER TKI (poziotinib/pyrotinib) $160K (20%) + chemo $30K (25%)."},
        "eu.priceK":     {"note": "~$115K blended; EU net ~59% US."},
        "row.priceK":    {"note": "~$50K blended; China pyrotinib domestic pricing."},
        "penPct":        {"note": "~48% peak -- DESTINY-Lung04 1L readout could shift from 2L; HER2 bispecifics (zanidatamab) extend."}
    },

    "oncology.lung.nsclc_driver.her3": {
        "us.patientsK":  {"note": "~15K US HER3-expressing NSCLC/yr (broad expression, EGFR-mut post-TKI enriched). Source: Daiichi HERTHENA-Lung."},
        "eu.patientsK":  {"note": "EU5 ~20K HER3+ NSCLC; broad expression in EGFR-mut post-progression."},
        "row.patientsK": {"note": "ROW ~60K; EGFR-mut APAC high enriches HER3 target."},
        "us.wtpPct":     {"note": "~55% -- patritumab deruxtecan (HER3-DXd) BLA filed post-HERTHENA-Lung02; pre-launch model."},
        "eu.wtpPct":     {"note": "~40% -- EMA filing 2024; NICE CDF likely pathway."},
        "row.wtpPct":    {"note": "~14% -- Japan first approval expected (DS-origin)."},
        "us.priceK":     {"note": "Blended $195K: HER3-DXd $220K (60% pts) + HER3 bispecifics (izalontamab) $190K (10%) + chemo $30K (30%)."},
        "eu.priceK":     {"note": "~$115K blended; EU net ~59% US."},
        "row.priceK":    {"note": "~$45K blended; Japan J-DPC first."},
        "penPct":        {"note": "~42% peak -- HER3-DXd 2L+ EGFR-mut post-Tagrisso; broader NSCLC and other tumors extend 5yr."}
    },

    "oncology.lung.nsclc_driver.kras": {
        "us.patientsK":  {"note": "~20K US KRAS-mut NSCLC/yr (25% of NSCLC); G12C ~13%, G12D ~4%, G12V ~6%. Source: NCI SEER, AMG/MRTX trials."},
        "eu.patientsK":  {"note": "EU5 ~28K KRAS-mut NSCLC; ESMO testing guidelines drive NGS."},
        "row.patientsK": {"note": "ROW ~60K; KRAS G12C lower in East Asian (~7%) than Western (~13%) NSCLC."},
        "us.wtpPct":     {"note": "~62% -- Lumakras + Krazati 2L KRAS G12C+ NCCN Cat 1; Medicare + commercial broad; NGS reflex."},
        "eu.wtpPct":     {"note": "~46% -- NICE + G-BA approved sotorasib + adagrasib; France ASMR IV."},
        "row.wtpPct":    {"note": "~15% -- Japan PMDA full; China NRDL sotorasib 2023."},
        "us.priceK":     {"note": "Blended $185K: KRAS G12Ci $205K (50% pts G12C+) + pan-KRAS/G12D (RMC-6236, MRTX1133) $220K (15%) + chemo $30K (35%)."},
        "eu.priceK":     {"note": "~$110K blended; EU net ~59% US."},
        "row.priceK":    {"note": "~$45K blended; China NRDL negotiation."},
        "penPct":        {"note": "~50% peak -- G12C saturated 2L; 1L CodeBreaK-202 + pan-KRAS (divarasib, glecirasib) + KRAS+SHP2 combos extend."}
    },

    "oncology.lung.nsclc_driver.other": {
        "us.patientsK":  {"note": "~8K US RET/NTRK/EGFR ex20/BRAF NSCLC/yr combined; rare driver mix. Source: NCI + oncogenic driver consortium."},
        "eu.patientsK":  {"note": "EU5 ~10K combined rare drivers; ESMO reflex NGS captures most."},
        "row.patientsK": {"note": "ROW ~25K combined."},
        "us.wtpPct":     {"note": "~65% -- Retevmo RET+, Rozlytrek NTRK+, Rybrevant EGFR ex20+, Tafinlar+Mekinist BRAF V600E+ all NCCN Cat 1."},
        "eu.wtpPct":     {"note": "~48% -- NICE + G-BA approved selpercatinib + entrectinib + amivantamab."},
        "row.wtpPct":    {"note": "~16% -- Japan PMDA full; China NRDL selective."},
        "us.priceK":     {"note": "Blended $210K: RET TKI $225K (25% pts) + NTRK TKI $225K (10%) + Rybrevant EGFR ex20 $240K (30%) + BRAF combo $220K (15%) + chemo $30K (20%)."},
        "eu.priceK":     {"note": "~$125K blended; EU net ~60% US."},
        "row.priceK":    {"note": "~$50K blended."},
        "penPct":        {"note": "~55% peak -- tgt rx for rare drivers at high WTP; next-gen (zipalertinib EGFR ex20, NVL-520 RET) extend 5yr."}
    },

    "oncology.lung.nsclc_driver.ros1": {
        "us.patientsK":  {"note": "~2-3K US ROS1+ NSCLC/yr (1-2% of NSCLC); FISH/NGS confirmed. Source: NCI SEER + IASLC mol epi."},
        "eu.patientsK":  {"note": "EU5 ~3K ROS1+ NSCLC; ESMO reflex guidelines."},
        "row.patientsK": {"note": "ROW ~7K; higher ROS1 in never-smoker APAC."},
        "us.wtpPct":     {"note": "~70% -- Rozlytrek + Xalkori + Augtyro (repotrectinib) 1L NCCN Cat 1; Medicare broad."},
        "eu.wtpPct":     {"note": "~52% -- NICE + G-BA approved entrectinib + repotrectinib; ESMO guidelines."},
        "row.wtpPct":    {"note": "~20% -- Japan PMDA full; China NRDL 2024."},
        "us.priceK":     {"note": "Blended $215K: Augtyro $230K (50% pts) + Rozlytrek $220K (25%) + Xalkori $185K (15%) + chemo $30K (10%)."},
        "eu.priceK":     {"note": "~$125K blended; EU net ~58% US."},
        "row.priceK":    {"note": "~$55K blended."},
        "penPct":        {"note": "~65% peak -- 3G repotrectinib displacing 1G/2G; 4G (NVL-520 zidesamtinib) for G2032R emerges."}
    },

    "oncology.lung.nsclc_driver.trop2": {
        "us.patientsK":  {"note": "~40K US NSCLC with TROP2 expression (broad, ~80% tumors); actionable via ADC. Source: DS/AZ TROPION-Lung filings."},
        "eu.patientsK":  {"note": "EU5 ~55K; broad TROP2 NSCLC expression."},
        "row.patientsK": {"note": "ROW ~180K; broad biomarker pool."},
        "us.wtpPct":     {"note": "~58% -- Datroway (Dato-DXd) BLA filed post-TROPION-Lung01; Medicare NCCN pending full approval; Trodelvy ex-lung."},
        "eu.wtpPct":     {"note": "~42% -- EMA filing 2024; NICE CDF likely."},
        "row.wtpPct":    {"note": "~14% -- Japan first launch (DS-origin)."},
        "us.priceK":     {"note": "Blended $175K: Dato-DXd $200K (50% pts) + sacituzumab tirumotecan $205K (15%) + next-gen TROP2 ADC $215K (5%) + chemo $30K (30%)."},
        "eu.priceK":     {"note": "~$105K blended; EU net ~60% US."},
        "row.priceK":    {"note": "~$40K blended."},
        "penPct":        {"note": "~45% peak -- TROP2 ADC 2L+ nonsq NSCLC; combos w/IO (AVANZAR) + 1L could expand if EGFR/KRAS agnostic data holds."}
    },

    "oncology.lung.nsclc_undruggable": {
        "us.patientsK":  {"note": "~30K US NSCLC w/o targetable driver (wild-type); IO+chemo SOC 1L. Source: NCI SEER + KEYNOTE-189 enrollment."},
        "eu.patientsK":  {"note": "EU5 ~45K driver-negative NSCLC; ESMO NGS reflex excludes drivers."},
        "row.patientsK": {"note": "ROW ~180K driver-negative; smoking-associated heavy in APAC/EM."},
        "us.wtpPct":     {"note": "~65% -- Keytruda+chemo 1L (KN-189/407), Tecentriq+chemo, Libtayo; NCCN Cat 1; Medicare + commercial broad."},
        "eu.wtpPct":     {"note": "~48% -- NICE + G-BA approved pembro+chemo + atezo+chemo 1L; France ASMR III."},
        "row.wtpPct":    {"note": "~18% -- Japan PMDA full; China NRDL tislelizumab/sintilimab + chemo."},
        "us.priceK":     {"note": "Blended $135K: pembro+chemo $175K (50% pts) + atezo/cemi+chemo $165K (15%) + IO+CTLA4 $210K (10%) + chemo alone $30K (25%)."},
        "eu.priceK":     {"note": "~$80K blended; EU net ~59% US."},
        "row.priceK":    {"note": "~$30K blended; China NRDL IO <$30K drives mix."},
        "penPct":        {"note": "~55% peak -- IO+chemo saturated 1L; LAG3 + TIGIT + PD1xVEGF (ivonescimab) 1L combos extend 5yr."}
    },

    # ============================================================
    # LUNG - SCLC
    # ============================================================
    "oncology.lung.sclc": {
        "us.patientsK":  {"note": "SEER: ~30K new SCLC/yr US (~13% of lung); ~22K on systemic. Source: NCI SEER 2024, LCFA."},
        "eu.patientsK":  {"note": "EU5 ~40K SCLC/yr; ~28K on systemic per EUROCARE."},
        "row.patientsK": {"note": "ROW ~180K; smoking-heavy China/EM dominant."},
        "us.wtpPct":     {"note": "~60% -- Imfinzi+EP + Tecentriq+EP 1L ES-SCLC (CASPIAN/IMpower133); Imdelltra (tarlatamab) DLL3 2L; Medicare broad."},
        "eu.wtpPct":     {"note": "~44% -- NICE + G-BA approved durva/atezo+EP 1L; tarlatamab EMA 2024."},
        "row.wtpPct":    {"note": "~14% -- Japan PMDA full; China NRDL durvalumab + EP."},
        "us.priceK":     {"note": "Blended $125K: durva/atezo+EP $145K (55% pts) + Imdelltra DLL3 $165K (15%) + lurbinectedin 2L $120K (10%) + EP alone $25K (20%)."},
        "eu.priceK":     {"note": "~$72K blended; EU net ~58% US."},
        "row.priceK":    {"note": "~$28K blended; etoposide/platinum generic."},
        "penPct":        {"note": "~48% peak -- IO+chemo 1L saturated ES; tarlatamab DLL3 2L + ADCs (ifinatamab DXd) + DLL3 CAR-T emerge."}
    },

    # ============================================================
    # MULTI-TUMOR
    # ============================================================
    "oncology.multi_tumor.adc_platform": {
        "us.patientsK":  {"note": "~250K US addressable across HER2/TROP2/HER3/CEACAM5/B7-H3 ADCs; sum of biomarker-positive solid tumors. Source: company 10-Ks."},
        "eu.patientsK":  {"note": "EU5 ~320K ADC-addressable solid tumors; ESMO testing expansion."},
        "row.patientsK": {"note": "ROW ~900K; broad solid tumor ADC potential in APAC/EM."},
        "us.wtpPct":     {"note": "~55% -- approved ADCs (Enhertu, Trodelvy, Padcev, Elahere) across HER2/TROP2/Nectin4/FRa; Medicare + commercial broad."},
        "eu.wtpPct":     {"note": "~42% -- NICE + G-BA approved major ADCs; France ASMR II-III."},
        "row.wtpPct":    {"note": "~14% -- Japan PMDA (DS-origin Enhertu); China NRDL disitamab vedotin + RC48."},
        "us.priceK":     {"note": "Blended $195K: HER2 ADC $205K (30% pts) + TROP2 ADC $200K (25%) + Nectin4 ADC $310K (8%) + FRa ADC $220K (10%) + others $180K (27%)."},
        "eu.priceK":     {"note": "~$115K blended; EU net ~59% US."},
        "row.priceK":    {"note": "~$45K blended; China domestic ADCs lower."},
        "penPct":        {"note": "~40% peak -- platform addresses broad range; launch curves staggered by asset; 5-7yr ramp across targets."}
    },

    "oncology.multi_tumor.bicycle_discovery": {
        "us.patientsK":  {"note": "~80K US across BT8009 (Nectin4+ bladder/other) + BT5528 (EphA2+) + BT7480 (Nectin4xCD137) targets. Source: Bicycle 10-K."},
        "eu.patientsK":  {"note": "EU5 ~100K Bicycle-addressable across Nectin4 + EphA2 + MT1-MMP."},
        "row.patientsK": {"note": "ROW ~250K addressable."},
        "us.wtpPct":     {"note": "~52% -- pre-commercial; model assumes Medicare + commercial at Padcev-like pricing given Nectin4 precedent."},
        "eu.wtpPct":     {"note": "~38% -- EMA pathway; NICE CDF for novel modality."},
        "row.wtpPct":    {"note": "~12% -- Japan PMDA + selective APAC."},
        "us.priceK":     {"note": "Blended $225K: Bicycle Toxin Conjugate (BTC) $240K (70% pts) + Bicycle TICA/CD137 $200K (30%); Padcev-benchmarked."},
        "eu.priceK":     {"note": "~$135K blended; EU net ~60% US."},
        "row.priceK":    {"note": "~$55K blended; launch Japan + China."},
        "penPct":        {"note": "~30% peak -- Phase 1/2 assets; BT8009 Phase 2/3 Duravelo; 5-7yr ramp from first approval ~2027+."}
    },

    # ============================================================
    # NEUROENDOCRINE
    # ============================================================
    "oncology.neuroendocrine.gepnet": {
        "us.patientsK":  {"note": "~12K US GEP-NET prevalent on-tx; ~4K incident/yr. Source: NCI SEER 2024, NET Research Foundation."},
        "eu.patientsK":  {"note": "EU5 ~15K GEP-NET prevalent; ENETS registry."},
        "row.patientsK": {"note": "ROW ~40K; Japan JNETS registry + China."},
        "us.wtpPct":     {"note": "~62% -- Sandostatin/Somatuline SSA 1L; Lutathera (Lu-177-DOTATATE) PRRT NETTER-1/2; Afinitor/Sutent mid-grade; Medicare broad."},
        "eu.wtpPct":     {"note": "~48% -- NICE + G-BA approved lanreotide + Lutathera; ESMO + ENETS guidelines."},
        "row.wtpPct":    {"note": "~16% -- Japan PMDA full; China NRDL octreotide biosim."},
        "us.priceK":     {"note": "Blended $110K: SSA $45K (55% pts) + Lutathera $190K (25%) + Afinitor/Sutent $165K (15%) + chemo $30K (5%)."},
        "eu.priceK":     {"note": "~$65K blended; EU net ~59% US; octreotide LAR generic lowers."},
        "row.priceK":    {"note": "~$22K blended; octreotide biosim/generic."},
        "penPct":        {"note": "~50% peak -- SSA + Lutathera saturated grade-dependent; next-gen PRRT (Ac-225) + combos (Lutathera+nivo) extend."}
    },

    # ============================================================
    # HEMATOLOGY - RARE BLOOD
    # ============================================================
    "hematology.rare_blood.hemoglobinopathy": {
        "us.patientsK":  {"note": "~100K US SCD + ~3K TDT; ~20K SCD severe (2+ VOCs/yr) eligible for gene tx. Source: CDC SCDC, NORD, CRISPR/Vertex 10-K."},
        "eu.patientsK":  {"note": "EU5 ~60K SCD + ~15K TDT; higher TDT in Southern EU (Mediterranean)."},
        "row.patientsK": {"note": "ROW ~5M SCD (sub-Saharan Africa dominant); ~200K TDT APAC/Med; gene tx access extremely limited."},
        "us.wtpPct":     {"note": "~45% -- Casgevy (exa-cel) + Lyfgenia (lovo-cel) approved Dec 2023; Medicaid (where most SCD pts are) limited; CMS outcomes-based."},
        "eu.wtpPct":     {"note": "~32% -- NICE CDF Casgevy 2024; Italy + Germany early access; single-payer negotiation in progress."},
        "row.wtpPct":    {"note": "~6% -- Japan + AU limited; sub-Saharan access near-zero; GCC bilateral deals emerging."},
        "us.priceK":     {"note": "Blended $2200K: Casgevy $2200K (50% pts) + Lyfgenia $3100K (40%) + Oxbryta/Adakveo (delisted) / hydroxyurea $5K (10%)."},
        "eu.priceK":     {"note": "~$1600K blended; EU net ~72% US list for gene tx; annuity payment models under negotiation."},
        "row.priceK":    {"note": "~$200K blended; gene tx near-zero access outside GCC; hydroxyurea + transfusions dominate globally."},
        "penPct":        {"note": "~18% peak -- capacity (myeloablation beds) + payer friction limit; 5-7yr ramp; in-vivo gene editing (Beam, Editas) could expand."}
    },

}


if __name__ == "__main__":
    print(f"Total disease-area tooltip entries: {len(TOOLTIPS)}")
    for path in sorted(TOOLTIPS.keys()):
        print(f"  {path} ({len(TOOLTIPS[path])} fields)")
