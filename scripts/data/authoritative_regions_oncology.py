# -*- coding: utf-8 -*-
"""Authoritative region values extracted from tooltips_oncology.py.

For each taxonomy area, the {us, eu, row} x {patientsK, wtpPct, priceK}
values represent the single authoritative slider value reconciled from
the narrative tooltips (prevalent/treated/on-tx preferred; blended price
preferred; market-level WTP %).
"""

REGIONS = {
    # ------------------------------------------------------------
    # BREAST
    # ------------------------------------------------------------
    "oncology.breast.her2_pos": {
        "us":  {"patientsK": 120, "wtpPct": 70, "priceK": 165},
        "eu":  {"patientsK": 140, "wtpPct": 50, "priceK": 95},
        "row": {"patientsK": 200, "wtpPct": 18, "priceK": 35},
    },
    # source: US HR+/HER2- mBC + adjuvant high-risk ~250K Rx-eligible per ASCO/
    # NCCN treatment patterns. Branded class: Ibrance $5B + Verzenio $4B +
    # Kisqali $3B + Truqap $0.5B + Orserdu launching + emerging CDK7/oral SERDs
    # = ~$13-15B today globally, peak $25-30B by 2030 (post-CDK4/6 LOE
    # offsets from new oral SERDs + AKT/PI3K class). Prior $44B at $95K
    # uniform priceK assumed every diagnosed patient on premium oral therapy
    # for full duration; ~1.5x off net economics post PBM rebates and
    # treatment cycling.
    "oncology.breast.hr_her2_neg": {
        "us":  {"patientsK": 250, "wtpPct": 65, "priceK": 70},
        "eu":  {"patientsK": 350, "wtpPct": 45, "priceK": 40},
        "row": {"patientsK": 500, "wtpPct": 12, "priceK": 12},
    },
    "oncology.breast.tnbc": {
        "us":  {"patientsK": 60,  "wtpPct": 65, "priceK": 140},
        "eu":  {"patientsK": 65,  "wtpPct": 48, "priceK": 80},
        "row": {"patientsK": 120, "wtpPct": 15, "priceK": 30},
    },

    # ------------------------------------------------------------
    # GENITOURINARY
    # ------------------------------------------------------------
    "oncology.genitourinary.bladder": {
        "us":  {"patientsK": 25, "wtpPct": 62, "priceK": 185},
        "eu":  {"patientsK": 28, "wtpPct": 45, "priceK": 105},
        "row": {"patientsK": 80, "wtpPct": 14, "priceK": 35},
    },
    # Adjuvant / peri-operative urothelial carcinoma (post-cystectomy MIBC):
    # distinct competitive arena from advanced/metastatic. Standard of care:
    # adjuvant Opdivo nivolumab (CheckMate 274, FDA 2021), Keytruda adjuvant
    # under review. Emerging: ctDNA-MRD guided escalation, BNT122 autogene
    # cevumeran (IMCODE004 Ph2), BMS bnt327 PD-L1xVEGF in adjuvant setting.
    # source: NCI SEER bladder MIBC US ~20K cystectomies/yr -> ~15K eligible
    # for adjuvant tx; EU5 ~20K; ROW ~50K. Net branded ~$170K/yr (1-year adj IO).
    "oncology.genitourinary.bladder_adjuvant": {
        "us":  {"patientsK": 15, "wtpPct": 70, "priceK": 170},
        "eu":  {"patientsK": 20, "wtpPct": 50, "priceK": 100},
        "row": {"patientsK": 50, "wtpPct": 14, "priceK": 35},
    },
    "oncology.genitourinary.prostate": {
        "us":  {"patientsK": 100, "wtpPct": 70, "priceK": 95},
        "eu":  {"patientsK": 110, "wtpPct": 52, "priceK": 55},
        "row": {"patientsK": 200, "wtpPct": 18, "priceK": 18},
    },
    "oncology.genitourinary.rcc": {
        "us":  {"patientsK": 25, "wtpPct": 68, "priceK": 215},
        "eu":  {"patientsK": 30, "wtpPct": 50, "priceK": 125},
        "row": {"patientsK": 70, "wtpPct": 16, "priceK": 40},
    },

    # ------------------------------------------------------------
    # GI
    # ------------------------------------------------------------
    "oncology.gi.cholangiocarcinoma": {
        "us":  {"patientsK": 10, "wtpPct": 55, "priceK": 155},
        "eu":  {"patientsK": 12, "wtpPct": 42, "priceK": 90},
        "row": {"patientsK": 60, "wtpPct": 12, "priceK": 30},
    },
    "oncology.gi.colorectal": {
        "us":  {"patientsK": 55,  "wtpPct": 65, "priceK": 95},
        "eu":  {"patientsK": 70,  "wtpPct": 48, "priceK": 55},
        "row": {"patientsK": 320, "wtpPct": 16, "priceK": 22},
    },
    # Adjuvant CRC (resected stage II-III, ctDNA-MRD-positive subset):
    # distinct from advanced/metastatic. Currently SoC = adjuvant chemo
    # (FOLFOX, CAPOX) generic; Keytruda adj for dMMR/MSI-H subset. Emerging:
    # ctDNA-MRD-driven escalation (Natera/Guardant), individualized neoantigen
    # vaccines (BNT122 autogene cevumeran Ph2 with Genentech), MRD+ targeted
    # IO. source: NCI SEER CRC US ~150K/yr, ~50K stage II-III resected
    # -> ~15-20K ctDNA-MRD-positive eligible/yr; EU5 ~25K; ROW ~80K. Net
    # branded ~$170K/yr for 1-year adj IO/vaccine course.
    "oncology.gi.colorectal_adjuvant": {
        "us":  {"patientsK": 18, "wtpPct": 70, "priceK": 170},
        "eu":  {"patientsK": 25, "wtpPct": 50, "priceK": 100},
        "row": {"patientsK": 80, "wtpPct": 14, "priceK": 35},
    },
    "oncology.gi.gastric_esoph": {
        "us":  {"patientsK": 25,  "wtpPct": 58, "priceK": 135},
        "eu":  {"patientsK": 35,  "wtpPct": 44, "priceK": 78},
        "row": {"patientsK": 800, "wtpPct": 20, "priceK": 32},
    },
    "oncology.gi.hcc": {
        "us":  {"patientsK": 20,  "wtpPct": 60, "priceK": 135},
        "eu":  {"patientsK": 25,  "wtpPct": 46, "priceK": 78},
        "row": {"patientsK": 650, "wtpPct": 22, "priceK": 28},
    },
    "oncology.gi.pancreatic": {
        # bumped for next-gen RAS therapies (RVMD daraxonrasib): broader patient
        # eligibility + premium pricing. Was $3.3B WW (Folfirinox + gem-Abrax era);
        # now $6B WW reflecting 2027+ market with daraxonrasib at $150-200K WAC.
        "us":  {"patientsK": 60,  "wtpPct": 60, "priceK": 110},
        "eu":  {"patientsK": 80,  "wtpPct": 45, "priceK": 60},
        "row": {"patientsK": 350, "wtpPct": 15, "priceK": 22},
    },
    # Adjuvant resected PDAC: post-Whipple/distal-pancreatectomy. Currently
    # SoC = mFOLFIRINOX or gem+capecitabine (PRODIGE 24, ESPAC-4) -- all
    # generic chemo. No approved IO or targeted adjuvant. BNT122 IMCODE003
    # (autogene cevumeran + atezo + mFOLFIRINOX vs SOC) is first-in-class
    # mRNA cancer vaccine in this setting. Genentech 50/50 partnership.
    # source: NCI SEER PDAC US ~64K incidence/yr, ~20-25% surgically resectable
    # -> ~13-15K resected/yr eligible for adj therapy; EU5 ~12K; ROW ~50K.
    # Net branded aspirational ~$200K/yr (cancer vaccine premium).
    "oncology.gi.pancreatic_adjuvant": {
        "us":  {"patientsK": 13, "wtpPct": 65, "priceK": 200},
        "eu":  {"patientsK": 12, "wtpPct": 45, "priceK": 120},
        "row": {"patientsK": 50, "wtpPct": 12, "priceK": 40},
    },

    # ------------------------------------------------------------
    # GYNECOLOGIC
    # ------------------------------------------------------------
    "oncology.gynecologic.ovarian": {
        "us":  {"patientsK": 35, "wtpPct": 65, "priceK": 125},
        "eu":  {"patientsK": 50, "wtpPct": 50, "priceK": 72},
        "row": {"patientsK": 90, "wtpPct": 16, "priceK": 25},
    },
    # Endometrial cancer: ~67K US new cases/yr, ~50K prevalent on biologic
    # tx (advanced/recurrent dMMR + pMMR). EU 80K, ROW 250K. Class:
    # Jemperli (GSK dostarlimab anti-PD-1 dMMR + RUBY pMMR ~$700M),
    # Keytruda (Merck KEYNOTE-868 pMMR), Lenvima/Keytruda combo (Eisai/
    # Merck KEYNOTE-775 pMMR pre-PD-1). Net branded ~$170K/yr.
    "oncology.gynecologic.endometrial": {
        "us":  {"patientsK": 50,  "wtpPct": 70, "priceK": 170},
        "eu":  {"patientsK": 80,  "wtpPct": 50, "priceK": 100},
        "row": {"patientsK": 250, "wtpPct": 14, "priceK": 35},
    },

    # ------------------------------------------------------------
    # HEMATOLOGY
    # ------------------------------------------------------------
    "oncology.hematology.aml": {
        "us":  {"patientsK": 22, "wtpPct": 62, "priceK": 185},
        "eu":  {"patientsK": 27, "wtpPct": 45, "priceK": 105},
        "row": {"patientsK": 90, "wtpPct": 14, "priceK": 35},
    },
    # ------------------------------------------------------------
    # HEMATOLOGIC MALIGNANCIES -- CLL split from NHL (medically distinct);
    # NHL groups all B-cell + T-cell lymphomas with disease-specific L4s.
    # Patient counts are annual treated cohorts (not raw incidence) because
    # most drugs are continuous chronic therapy.
    # source: SEER, NORD, Lymphoma Research Foundation
    # ------------------------------------------------------------

    # CLL: chronic lymphocytic leukemia. ~21K US incident, ~80K actively-treated
    # prevalent (5-10yr median OS on BTK/BCL2). Supports the ~$10B WW BTK+BCL2 spend.
    "oncology.hematology.cll": {
        "us":  {"patientsK": 80,  "wtpPct": 70, "priceK": 100},
        "eu":  {"patientsK": 95,  "wtpPct": 50, "priceK": 60},
        "row": {"patientsK": 150, "wtpPct": 12, "priceK": 25},
    },

    # NHL parent (legacy aggregate). Sub-segments below.
    "oncology.hematology.nhl": {
        "us":  {"patientsK": 80, "wtpPct": 60, "priceK": 150},
        "eu":  {"patientsK": 90, "wtpPct": 45, "priceK": 90},
        "row": {"patientsK": 200, "wtpPct": 12, "priceK": 35},
    },
    # DLBCL: diffuse large B-cell lymphoma. Most common aggressive NHL.
    # Curative intent 1L (R-CHOP); 2L+ market for CAR-T + bispecifics + Polivy combos.
    "oncology.hematology.nhl.dlbcl": {
        "us":  {"patientsK": 40,  "wtpPct": 68, "priceK": 195},
        "eu":  {"patientsK": 38,  "wtpPct": 50, "priceK": 115},
        "row": {"patientsK": 120, "wtpPct": 15, "priceK": 40},
    },
    # FL + iNHL: indolent B-cell lymphoma; many on watch-and-wait initially.
    # Treatment mix: rituximab/lenalidomide/bispecifics/CAR-T.
    "oncology.hematology.nhl.fl": {
        "us":  {"patientsK": 14, "wtpPct": 65, "priceK": 80},
        "eu":  {"patientsK": 17, "wtpPct": 48, "priceK": 50},
        "row": {"patientsK": 30, "wtpPct": 12, "priceK": 20},
    },
    # MCL: mantle cell lymphoma; aggressive but treatable. ~5K US incident
    # + ~10K prevalent on therapy = ~15K addressable; ~18K EU; ~40K ROW.
    # BTK first-line (Calquence/Brukinsa/Imbruvica/pirtobrutinib), CAR-T
    # (Tecartus) post-BTKi. Class peak ~$3B globally.
    "oncology.hematology.nhl.mcl": {
        "us":  {"patientsK": 15, "wtpPct": 70, "priceK": 175},
        "eu":  {"patientsK": 18, "wtpPct": 52, "priceK": 100},
        "row": {"patientsK": 40, "wtpPct": 12, "priceK": 35},
    },
    # WM: Waldenstrom macroglobulinemia / lymphoplasmacytic lymphoma. Rare;
    # BTK inhibitors are 1L standard (Brukinsa, Imbruvica), rituximab combos.
    "oncology.hematology.nhl.wm": {
        "us":  {"patientsK": 5,  "wtpPct": 70, "priceK": 180},
        "eu":  {"patientsK": 6,  "wtpPct": 52, "priceK": 110},
        "row": {"patientsK": 12, "wtpPct": 10, "priceK": 35},
    },
    # MZL: marginal zone lymphoma (splenic, nodal, MALT).
    # BTK + lenalidomide-rituximab + CAR-T expanding.
    "oncology.hematology.nhl.mzl": {
        "us":  {"patientsK": 7,  "wtpPct": 65, "priceK": 100},
        "eu":  {"patientsK": 9,  "wtpPct": 48, "priceK": 60},
        "row": {"patientsK": 18, "wtpPct": 12, "priceK": 25},
    },
    # T-cell lymphomas (PTCL, CTCL, etc). Smaller market; Soquelitinib (CRVS)
    # + Adcetris + romidepsin + CAR-T pipeline.
    "oncology.hematology.nhl.tcell": {
        "us":  {"patientsK": 8,  "wtpPct": 60, "priceK": 130},
        "eu":  {"patientsK": 10, "wtpPct": 42, "priceK": 75},
        "row": {"patientsK": 20, "wtpPct": 10, "priceK": 28},
    },
    "oncology.hematology.myeloma": {
        "us":  {"patientsK": 160, "wtpPct": 65, "priceK": 235},
        "eu":  {"patientsK": 180, "wtpPct": 48, "priceK": 140},
        "row": {"patientsK": 300, "wtpPct": 16, "priceK": 50},
    },
    # MM line-of-therapy L4 sub-segments. Patient counts approximate the
    # cohort actively treated in that line annually (incidence x line-share x survival).
    # 1L = newly diagnosed, frontline regimens (RVd, dara-RVd combos)
    # 2l_3l = early relapse after 1-2 prior lines (Carvykti current label, daratumumab combos)
    # 4l_plus = heavily pre-treated R/R, where bispecifics + cell therapies live
    "oncology.hematology.myeloma.1l": {
        "us":  {"patientsK": 50, "wtpPct": 80, "priceK": 280},
        "eu":  {"patientsK": 55, "wtpPct": 62, "priceK": 165},
        "row": {"patientsK": 130, "wtpPct": 20, "priceK": 65},
    },
    "oncology.hematology.myeloma.2l_3l": {
        "us":  {"patientsK": 36, "wtpPct": 70, "priceK": 320},
        "eu":  {"patientsK": 42, "wtpPct": 55, "priceK": 195},
        "row": {"patientsK": 80, "wtpPct": 16, "priceK": 70},
    },
    "oncology.hematology.myeloma.4l_plus": {
        "us":  {"patientsK": 12, "wtpPct": 55, "priceK": 380},
        "eu":  {"patientsK": 14, "wtpPct": 42, "priceK": 220},
        "row": {"patientsK": 20, "wtpPct": 10, "priceK": 80},
    },
    # (oncology.hematology.tcell_lymphoma renamed to oncology.hematology.nhl.tcell above)

    # ------------------------------------------------------------
    # LUNG - NSCLC DRIVER SUBTYPES
    # ------------------------------------------------------------
    # ALK+ NSCLC: ~3-5% of NSCLC (US ~12K eligible/yr), EU ~15K, Asia
    # higher prevalence ~50K. Class: Alecensa (Roche $2B), Lorbrena (Pfizer
    # $0.8B), Xalkori (legacy gen), Brigatinib. Class globally ~$3.5-4B.
    "oncology.lung.nsclc_driver.alk": {
        "us":  {"patientsK": 12, "wtpPct": 72, "priceK": 205},
        "eu":  {"patientsK": 15, "wtpPct": 55, "priceK": 120},
        "row": {"patientsK": 50, "wtpPct": 22, "priceK": 55},
    },
    # EGFR-mutant NSCLC: largest driver subtype (~15% Caucasian, ~50% Asian
    # NSCLC). US ~50K eligible; EU 65K; ROW 250K (China dominant). Class:
    # Tagrisso (osimertinib AZ ~$7B near-monopoly), Iressa/Tarceva legacy,
    # Vizimpro (Pfizer dacomitinib), Lazcluze (Janssen lazertinib + Rybrevant).
    # Class peak ~$15B globally with Tagrisso 1L+adjuvant+LAURA expansions.
    # source: SEER + AACR EGFR-mutant prevalence; AZ + Janssen 10-Ks.
    "oncology.lung.nsclc_driver.egfr": {
        "us":  {"patientsK": 50,  "wtpPct": 78, "priceK": 230},
        "eu":  {"patientsK": 65,  "wtpPct": 60, "priceK": 135},
        "row": {"patientsK": 250, "wtpPct": 25, "priceK": 50},
    },
    "oncology.lung.nsclc_driver.cmet": {
        "us":  {"patientsK": 3,  "wtpPct": 60, "priceK": 195},
        "eu":  {"patientsK": 4,  "wtpPct": 45, "priceK": 115},
        "row": {"patientsK": 10, "wtpPct": 16, "priceK": 45},
    },
    "oncology.lung.nsclc_driver.her2": {
        "us":  {"patientsK": 4,  "wtpPct": 62, "priceK": 195},
        "eu":  {"patientsK": 5,  "wtpPct": 46, "priceK": 115},
        "row": {"patientsK": 12, "wtpPct": 15, "priceK": 50},
    },
    "oncology.lung.nsclc_driver.her3": {
        "us":  {"patientsK": 15, "wtpPct": 55, "priceK": 195},
        "eu":  {"patientsK": 20, "wtpPct": 40, "priceK": 115},
        "row": {"patientsK": 60, "wtpPct": 14, "priceK": 45},
    },
    "oncology.lung.nsclc_driver.kras": {
        "us":  {"patientsK": 20, "wtpPct": 62, "priceK": 185},
        "eu":  {"patientsK": 28, "wtpPct": 46, "priceK": 110},
        "row": {"patientsK": 60, "wtpPct": 15, "priceK": 45},
    },
    "oncology.lung.nsclc_driver.ros1": {
        "us":  {"patientsK": 3, "wtpPct": 70, "priceK": 215},
        "eu":  {"patientsK": 3, "wtpPct": 52, "priceK": 125},
        "row": {"patientsK": 7, "wtpPct": 20, "priceK": 55},
    },
    "oncology.lung.nsclc_driver.trop2": {
        "us":  {"patientsK": 40,  "wtpPct": 58, "priceK": 175},
        "eu":  {"patientsK": 55,  "wtpPct": 42, "priceK": 105},
        "row": {"patientsK": 180, "wtpPct": 14, "priceK": 40},
    },
    "oncology.lung.nsclc_undruggable": {
        "us":  {"patientsK": 30,  "wtpPct": 65, "priceK": 135},
        "eu":  {"patientsK": 45,  "wtpPct": 48, "priceK": 80},
        "row": {"patientsK": 180, "wtpPct": 18, "priceK": 30},
    },
    # IO-treatable advanced NSCLC: the broad PD-1/PD-L1-eligible 1L+ population
    # (PD-L1+ mono, chemo+IO combo, adjuvant, perioperative). Distinct from
    # nsclc_undruggable (KRAS-WT/non-driver only) and nsclc_io_resistant
    # (post-CPI failure). This is the bucket where Keytruda + Opdivo + Tecentriq
    # + Imfinzi compete head-to-head -- effectively all advanced NSCLC except
    # specific driver subtypes (EGFR/ALK first-line gets TKIs, IO at progression).
    # US ~80K eligible (advanced NSCLC + adjuvant); EU 100K; ROW 400K (China big).
    # Class total ~$20B globally (Keytruda ~$13B + Opdivo ~$4B + Tecentriq +
    # Imfinzi). Blended priceK ~$180 reflects Keytruda dominance.
    # source: SEER NSCLC registry; Merck/BMS/Roche 10-Ks; PD-L1 testing rates.
    "oncology.lung.nsclc_io_combo": {
        "us":  {"patientsK": 80,  "wtpPct": 75, "priceK": 180},
        "eu":  {"patientsK": 100, "wtpPct": 60, "priceK": 100},
        "row": {"patientsK": 400, "wtpPct": 16, "priceK": 35},
    },
    # Adjuvant / peri-operative NSCLC (resectable stage I-III): distinct
    # competitive setting from advanced disease. Standard of care is
    # Keytruda adjuvant (KEYNOTE-091, FDA 2023) +/- chemo neoadjuvant
    # (KEYNOTE-671). Tecentriq adjuvant (IMpower010), Imfinzi PACIFIC
    # (stage III chemoradiation). Emerging: cancer vaccines (Moderna INT
    # mRNA-4157 INTerpath-009, BioNTech BNT122 autogene cevumeran),
    # ctDNA MRD-guided escalation. Patient pool ~70K resected NSCLC/yr US
    # (SEER stage I-III ~50% receive surgery), EU5 ~90K, ROW ~250K.
    # Blended branded ~$170K/yr (1-year adjuvant Keytruda + perioperative chemo).
    # source: NCI SEER NSCLC stage at diagnosis; Merck/Roche/AZ adjuvant
    # NSCLC Ph3 trials + 10-Ks; ESMO/ASCO 2024-25 adjuvant updates.
    "oncology.lung.nsclc_adjuvant": {
        "us":  {"patientsK": 70,  "wtpPct": 75, "priceK": 170},
        "eu":  {"patientsK": 90,  "wtpPct": 60, "priceK": 95},
        "row": {"patientsK": 250, "wtpPct": 16, "priceK": 35},
    },
    # Driver-agnostic IO-resistant NSCLC: pts who progressed on checkpoint
    # inhibitors (~50% of advanced NSCLC progress within 1-2y on pembro/IO).
    # US: ~70K incident io-progressors/yr; large unmet need bucket distinct
    # from driver-mutation subtypes. Targets: oncolytic IO, novel checkpoints,
    # bispecific T-cell engagers, intratumoral cytokine delivery (e.g. KRYS KB707).
    "oncology.lung.nsclc_io_resistant": {
        "us":  {"patientsK": 70,  "wtpPct": 60, "priceK": 180},
        "eu":  {"patientsK": 95,  "wtpPct": 44, "priceK": 105},
        "row": {"patientsK": 320, "wtpPct": 15, "priceK": 40},
    },

    # ------------------------------------------------------------
    # LUNG - SCLC
    # ------------------------------------------------------------
    "oncology.lung.sclc": {
        "us":  {"patientsK": 22,  "wtpPct": 60, "priceK": 125},
        "eu":  {"patientsK": 28,  "wtpPct": 44, "priceK": 72},
        "row": {"patientsK": 180, "wtpPct": 14, "priceK": 28},
    },

    # ------------------------------------------------------------
    # (oncology.multi_tumor.* removed -- platform/discovery indications without
    # specific lead diseases now use the _platform.* pseudo-area, which the
    # Market Explorer filters out by convention. These are visible in the
    # Technology Explorer where platforms belong.)

    # ------------------------------------------------------------
    # NEUROENDOCRINE
    # ------------------------------------------------------------
    "oncology.neuroendocrine.gepnet": {
        "us":  {"patientsK": 12, "wtpPct": 62, "priceK": 110},
        "eu":  {"patientsK": 15, "wtpPct": 48, "priceK": 65},
        "row": {"patientsK": 40, "wtpPct": 16, "priceK": 22},
    },

    # ------------------------------------------------------------
    # HEMATOLOGY - RARE BLOOD
    # ------------------------------------------------------------
    # source: US SCD ~100K diagnosed (CDC); EU5 ~100K; ROW ~5M (high WHO Africa
    # incidence but very limited specialty access). TDT adds another ~5K US.
    # Branded franchise mixes one-time gene therapy (Casgevy + Lyfgenia, $2.2M
    # WAC each, ~5K transplant-eligible severe US, ~$1B class peak limited by
    # HCT capacity) with chronic management (voxelotor $140K/yr branded,
    # crizanlizumab $90K/yr, hydroxyurea generic). Class peak ~$8-10B globally.
    # Prior values (priceK $2200 x full population) treated all 5.2M ROW
    # patients as gene-therapy-eligible at $2.2M -- ~12x inflation.
    # Blended priceK below amortizes one-time GT over a 30-year horizon plus
    # chronic-management mix.
    # Sickle cell disease: ~100K US diagnosed (CDC SCDC), ~60K EU5,
    # ~5M sub-Saharan + India + Caribbean. Branded mix: Casgevy + Lyfgenia
    # one-time ($2.2-3.1M, ~5K severe transplant-eligible US) blended with
    # voxelotor/crizanlizumab/hydroxyurea chronic care.
    "hematology.rare_blood.hemoglobinopathy.scd": {
        "us":  {"patientsK": 100,  "wtpPct": 58, "priceK": 75},
        "eu":  {"patientsK": 60,   "wtpPct": 38, "priceK": 35},
        "row": {"patientsK": 5000, "wtpPct": 8,  "priceK": 4},
    },
    # Beta-thalassemia (transfusion-dependent, TDT): ~3K US, ~15K EU5
    # (Mediterranean burden), ~200K ROW (APAC + MENA). Casgevy + Zynteglo
    # both approved; faster initial uptake than SCD given existing transfusion
    # specialty centers + clearer transplant eligibility criteria.
    "hematology.rare_blood.hemoglobinopathy.beta_thalassemia": {
        "us":  {"patientsK": 3,   "wtpPct": 70, "priceK": 220},
        "eu":  {"patientsK": 15,  "wtpPct": 55, "priceK": 110},
        "row": {"patientsK": 200, "wtpPct": 18, "priceK": 30},
    },
    # Hemophilia A (Factor VIII deficiency): ~16K severe (FVIII <1%) + ~5K moderate
    # in US (~20K total branded-eligible); ~25K EU5+UK; ~280K ROW dominated by China
    # + India (high carrier rate, under-diagnosis). Branded class:
    #   Hemlibra (emicizumab subq, Roche, ~$5.5B 2024) -- ~50% US share
    #   Factor VIII concentrates (Eloctate, Adynovate, Esperoct, Jivi, Altuvoct,
    #     Refixia, Novoeight) -- ~$300K/yr blended, prophylactic
    #   Roctavian (BioMarin gene therapy, ~$2.9M one-time, slow uptake)
    #   Mim8/denecimig (Novo BLA pending H2 2026 PDUFA, monthly subq) -- next entrant
    # source: WFH 2024 registry, Roche FY24 10-K, NHF + EAHAD prevalence data.
    "hematology.rare_blood.hemophilia_a": {
        "us":  {"patientsK": 20,  "wtpPct": 85, "priceK": 300},
        "eu":  {"patientsK": 25,  "wtpPct": 80, "priceK": 200},
        "row": {"patientsK": 280, "wtpPct": 25, "priceK": 80},
    },
    # Hemophilia B (Factor IX deficiency): ~5K severe US, ~7K EU, ~80K ROW.
    # Class: Alprolix (rFIX-Fc Sanofi/Sobi ~$300M legacy), BeneFIX (Pfizer
    # nonacog alfa), Idelvion (CSL albutrepenonacog alfa long-acting),
    # Refixia/Rebinyn (Novo nonacog beta pegol). Hemgenix (CSL Behring,
    # AAV5 gene therapy ~$3.5M one-time, slow uptake). Class peak ~$1.5B
    # globally. source: WFH 2024; CSL/Sanofi/Pfizer 10-Ks.
    "hematology.rare_blood.hemophilia_b": {
        "us":  {"patientsK": 5,   "wtpPct": 80, "priceK": 280},
        "eu":  {"patientsK": 7,   "wtpPct": 70, "priceK": 180},
        "row": {"patientsK": 80,  "wtpPct": 22, "priceK": 70},
    },
    # Von Willebrand disease (vWD): autosomal bleeding disorder with vWF
    # deficiency/dysfunction. Type 3 severe ~2K US, type 1/2 moderate-
    # severe ~30K US treated. EU 40K, ROW 200K. Class: Vonvendi (Takeda
    # rVWF first & only recombinant ~$200M), Humate-P / Wilate (CSL
    # plasma-derived vWF/FVIII concentrates ~$0.5B). Net branded ~$380K/yr.
    "hematology.rare_blood.vwd": {
        "us":  {"patientsK": 30,   "wtpPct": 70, "priceK": 250},
        "eu":  {"patientsK": 40,   "wtpPct": 55, "priceK": 160},
        "row": {"patientsK": 200,  "wtpPct": 18, "priceK": 60},
    },
    # Congenital fibrinogen deficiency (afibrinogenemia + hypofibrinogenemia
    # + dysfibrinogenemia): rare bleeding disorder. ~1K US, ~1.5K EU5, ~10K
    # ROW. Class: Riastap (CSL plasma fibrinogen ~$200M), Fibryga (Octapharma),
    # cryoprecipitate (off-label). Net branded ~$200K/yr orphan-priced.
    "hematology.rare_blood.fibrinogen_deficiency": {
        "us":  {"patientsK": 1,    "wtpPct": 70, "priceK": 200},
        "eu":  {"patientsK": 1.5,  "wtpPct": 55, "priceK": 130},
        "row": {"patientsK": 10,   "wtpPct": 14, "priceK": 50},
    },
    # Plasma volume expansion / supportive care (cirrhosis ascites, burns,
    # cardiac surgery, hypovolemic shock, neonatal): broad supportive care
    # use of human serum albumin. US ~3M annual treated episodes, EU ~5M,
    # ROW ~30M (mostly hospital). Class: CSL Behring Albuminex/Plasbumin
    # (~$1.2B), Octapharma Albunorm + Grifols Albutein. Class globally
    # ~$3-4B branded. Net branded ~$5K/episode.
    "hematology.supportive_care.volume_expander": {
        "us":  {"patientsK": 3000,  "wtpPct": 60, "priceK": 5},
        "eu":  {"patientsK": 5000,  "wtpPct": 45, "priceK": 3},
        "row": {"patientsK": 30000, "wtpPct": 14, "priceK": 1},
    },
    # Myelofibrosis (MF): primary + post-PV/post-ET. ~17K US prevalent,
    # ~25K EU5, ~80K ROW. Branded class: Jakavi/Jakafi (ruxolitinib JAK1/2
    # Novartis/Incyte ~$5B globally), Inrebic (fedratinib BMS), Vonjo
    # (pacritinib SMPI/CTI), Ojjaara (momelotinib GSK 2023). Pelabresib
    # (Novartis BET inhibitor) Ph3 ongoing. Net branded ~$170K/yr.
    "hematology.myeloproliferative.mf": {
        "us":  {"patientsK": 17,  "wtpPct": 72, "priceK": 170},
        "eu":  {"patientsK": 25,  "wtpPct": 55, "priceK": 100},
        "row": {"patientsK": 80,  "wtpPct": 15, "priceK": 35},
    },
    # Polycythemia vera (PV): ~70K US, ~100K EU5, ~250K ROW. Branded class:
    # Jakavi/Jakafi 2L (HU intolerant ~$1B), Besremi (ropeginterferon
    # PharmaEssentia/AOP), hydroxyurea (generic). Net branded ~$120K/yr.
    "hematology.myeloproliferative.pv": {
        "us":  {"patientsK": 70,  "wtpPct": 35, "priceK": 120},
        "eu":  {"patientsK": 100, "wtpPct": 22, "priceK": 70},
        "row": {"patientsK": 250, "wtpPct": 8,  "priceK": 25},
    },
    # Myelodysplastic syndromes (MDS): bone-marrow failure with cytopenias.
    # Lower-risk MDS-associated anemia ~50K US prevalent on tx, ~70K EU5,
    # ~250K ROW. Class: Reblozyl (BMS luspatercept TGF-b trap, ~$2.4B 1L
    # lower-risk MDS-anemia + beta-thal), Vidaza/azacitidine (generic
    # hypomethylating), Onureg (BMS oral aza AML maintenance). Net branded
    # ~$140K/yr.
    "hematology.myeloproliferative.mds": {
        "us":  {"patientsK": 50,  "wtpPct": 70, "priceK": 140},
        "eu":  {"patientsK": 70,  "wtpPct": 50, "priceK": 85},
        "row": {"patientsK": 250, "wtpPct": 14, "priceK": 30},
    },
    # Hodgkin lymphoma (cHL + NLPHL): ~9K US new cases/yr, ~80% cure 1L
    # ABVD/BV+AVD; ~30% relapse on 1L = ~3K R/R prevalent on biologic tx.
    # EU 12K, ROW 50K. Class: Adcetris (Pfizer/Seagen brentuximab CD30
    # ADC ~$1.5B globally), Opdivo (BMS PD-1 ~$0.8B HL share), Keytruda
    # (Merck PD-1 KEYNOTE-204). Net branded ~$200K/yr.
    "oncology.hematology.hodgkin": {
        "us":  {"patientsK": 9,   "wtpPct": 75, "priceK": 200},
        "eu":  {"patientsK": 12,  "wtpPct": 55, "priceK": 120},
        "row": {"patientsK": 50,  "wtpPct": 14, "priceK": 35},
    },
    # Aplastic anemia (severe): ~3K US, ~4K EU5, ~30K ROW. Branded class:
    # Promacta/Revolade (eltrombopag TPO mimetic Novartis ~$300M AA share)
    # added to standard IST (cyclosporine + ATG). Net branded ~$110K/yr.
    "hematology.rare_blood.aplastic_anemia": {
        "us":  {"patientsK": 5,   "wtpPct": 80, "priceK": 140},
        "eu":  {"patientsK": 6,   "wtpPct": 60, "priceK": 85},
        "row": {"patientsK": 50,  "wtpPct": 18, "priceK": 30},
    },
    # Chronic myeloid leukemia (CML): ~9K US incident, ~70K prevalent on
    # chronic TKI therapy. Class: Glivec/Gleevec generic ($1B residual),
    # Tasigna (Novartis 2nd gen), Sprycel (BMS), Bosulif (Pfizer), Scemblix
    # (Novartis STAMP allosteric, ASC4FIRST 1L 2024). Class globally ~$5B
    # branded + generics. Net branded ~$160K/yr.
    "oncology.hematology.cml": {
        "us":  {"patientsK": 70,  "wtpPct": 60, "priceK": 160},
        "eu":  {"patientsK": 85,  "wtpPct": 45, "priceK": 95},
        "row": {"patientsK": 350, "wtpPct": 12, "priceK": 35},
    },
    # C3 glomerulopathy (C3G): ultra-rare complement-mediated kidney
    # disease, ~1K US prevalent, ~2K EU5, ~6K ROW. Branded class emerging:
    # Fabhalta (iptacopan factor B inhibitor Novartis Ph3 APPEAR-C3G 2025
    # positive), pegcetacoplan (Empaveli Apellis Ph3 VALIANT). Net branded
    # peak ~$280K/yr orphan-priced.
    "nephrology.glomerular.c3g": {
        "us":  {"patientsK": 1,   "wtpPct": 65, "priceK": 280},
        "eu":  {"patientsK": 2,   "wtpPct": 45, "priceK": 170},
        "row": {"patientsK": 6,   "wtpPct": 10, "priceK": 60},
    },
    # Acquired thrombotic thrombocytopenic purpura (aTTP): ultra-rare ADAMTS13
    # autoimmune deficiency. ~3K US incident/yr, ~4K EU, ~10K ROW. Class:
    # Cablivi (caplacizumab anti-vWF nanobody, Sanofi ~$300M), plasma exchange
    # standard-of-care. Class peak ~$500M globally.
    "hematology.rare_blood.attp": {
        "us":  {"patientsK": 3,  "wtpPct": 75, "priceK": 270},
        "eu":  {"patientsK": 4,  "wtpPct": 60, "priceK": 175},
        "row": {"patientsK": 10, "wtpPct": 15, "priceK": 60},
    },
    # Paroxysmal nocturnal hemoglobinuria (PNH): rare acquired stem-cell
    # disorder w/ uncontrolled complement-mediated hemolysis. ~12K US
    # diagnosed, ~7K on chronic Rx; EU 18K; ROW 50K. Class: Soliris
    # (eculizumab AZ/Alexion ~$2.5B PNH+aHUS+MG combined declining), Ultomiris
    # (ravulizumab AZ long-acting C5, ~$3B all indications growing), Voydeya
    # (danicopan add-on factor D), Empaveli/Fabhalta (pegcetacoplan/iptacopan
    # complement). Class peak ~$5B globally.
    # source: Alexion/AZ 10-Ks; NORD; PNH Foundation.
    "hematology.rare_blood.pnh": {
        "us":  {"patientsK": 12,  "wtpPct": 85, "priceK": 480},
        "eu":  {"patientsK": 18,  "wtpPct": 75, "priceK": 320},
        "row": {"patientsK": 50,  "wtpPct": 22, "priceK": 130},
    },
    # Atypical hemolytic uremic syndrome (aHUS): rare complement-mediated
    # thrombotic microangiopathy. ~5K US, ~7K EU, ~25K ROW prevalent. C5-
    # blockade is curative (Soliris/Ultomiris). Class peak ~$1.5B globally.
    # source: Alexion/AZ 10-Ks; NORD aHUS.
    "hematology.rare_blood.ahus": {
        "us":  {"patientsK": 5,   "wtpPct": 80, "priceK": 480},
        "eu":  {"patientsK": 7,   "wtpPct": 70, "priceK": 320},
        "row": {"patientsK": 25,  "wtpPct": 18, "priceK": 130},
    },

    # ------------------------------------------------------------
    # SKIN ONCOLOGY (cscc / bcc / melanoma) -- IO regimens dominate
    # ------------------------------------------------------------
    # source: SEER advanced/metastatic melanoma incidence ~30K US/yr;
    # IO regimen avg ~$180K (Opdivo+Yervoy / pembro)
    "oncology.skin.melanoma": {
        "us":  {"patientsK": 30,  "wtpPct": 75, "priceK": 180},
        "eu":  {"patientsK": 35,  "wtpPct": 60, "priceK": 100},
        "row": {"patientsK": 80,  "wtpPct": 12, "priceK": 40},
    },
    # Adjuvant resected melanoma (high-risk stage IIB-IV post-resection):
    # distinct competitive arena from advanced/metastatic melanoma.
    # SoC: Keytruda adj (KEYNOTE-054, KEYNOTE-716), Opdivo adj
    # (CheckMate 238). Adjuvant peri-operative emerging: pembro + INT
    # (MRNA-4157 INTerpath-001 fully enrolled, interim 2026), BNT316
    # gotistobart pH-CTLA-4 in some adjuvant trials.
    # source: SEER melanoma US ~100K incidence/yr, ~30% stage IIB+
    # high-risk resected -> ~30K eligible; EU5 ~25K; ROW ~80K. Net
    # branded ~$170K/yr (1-year adj IO) vs $180K advanced setting.
    "oncology.skin.melanoma_adjuvant": {
        "us":  {"patientsK": 30,  "wtpPct": 75, "priceK": 170},
        "eu":  {"patientsK": 25,  "wtpPct": 60, "priceK": 100},
        "row": {"patientsK": 80,  "wtpPct": 12, "priceK": 35},
    },
    # source: Karia 2013 advanced cSCC US ~20K; Libtayo WAC ~$200K
    "oncology.skin.cscc": {
        "us":  {"patientsK": 20,  "wtpPct": 70, "priceK": 200},
        "eu":  {"patientsK": 25,  "wtpPct": 55, "priceK": 110},
        "row": {"patientsK": 50,  "wtpPct": 10, "priceK": 40},
    },
    # source: NCI advanced/metastatic BCC US ~12K; Libtayo / sonidegib pricing ~$200K
    "oncology.skin.bcc": {
        "us":  {"patientsK": 12,  "wtpPct": 70, "priceK": 200},
        "eu":  {"patientsK": 15,  "wtpPct": 55, "priceK": 110},
        "row": {"patientsK": 30,  "wtpPct": 10, "priceK": 40},
    },
    # Merkel cell carcinoma (MCC): rare aggressive neuroendocrine skin
    # cancer (NOT keratinocyte-origin like cSCC). ~3K US new cases/yr,
    # ~70% MCPyV-associated. EU 4K, ROW 8K. Class: Bavencio (Merck KGaA/
    # Pfizer avelumab anti-PD-L1 first-in-class ~$150M MCC share),
    # Keytruda (Merck KEYNOTE-913 1L), Libtayo (REGN cemiplimab Ph2 MCC
    # cemiplimab in trials). Net branded ~$165K/yr.
    "oncology.skin.merkel_cell": {
        "us":  {"patientsK": 3,   "wtpPct": 75, "priceK": 165},
        "eu":  {"patientsK": 4,   "wtpPct": 55, "priceK": 95},
        "row": {"patientsK": 8,   "wtpPct": 14, "priceK": 35},
    },
    # Desmoid tumors (aggressive fibromatosis): rare soft-tissue tumor
    # from connective tissue; can occur anywhere (abdominal wall,
    # extremity, intra-abdominal). ~6K US prevalent on tx, ~8K EU,
    # ~25K ROW. Class: Ogsiveo (Merck KGaA/SpringWorks nirogacestat
    # gamma-secretase inhibitor first-in-class ~$200M, DEFI Ph3
    # positive 2023). Net branded ~$175K/yr orphan-priced.
    "oncology.musculoskeletal.desmoid": {
        "us":  {"patientsK": 6,   "wtpPct": 70, "priceK": 175},
        "eu":  {"patientsK": 8,   "wtpPct": 50, "priceK": 100},
        "row": {"patientsK": 25,  "wtpPct": 14, "priceK": 35},
    },
    # NF1 plexiform neurofibroma (NF1-PN): rare RASopathy with
    # peripheral nerve sheath tumors. ~80K US NF1 patients with PN,
    # ~120K EU, ~500K ROW. Class: Gomekli (Merck KGaA/SpringWorks
    # mirdametinib MEK1/2 inhibitor adult+pediatric, FDA approved
    # Feb 2025), Koselugo (AZN selumetinib MEK1/2 pediatric NF1-PN).
    # Net branded ~$250K/yr orphan-priced.
    "oncology.musculoskeletal.nf1_pn": {
        "us":  {"patientsK": 80,  "wtpPct": 65, "priceK": 250},
        "eu":  {"patientsK": 120, "wtpPct": 50, "priceK": 150},
        "row": {"patientsK": 500, "wtpPct": 12, "priceK": 50},
    },
    # Tenosynovial giant cell tumor (TGCT): locally aggressive joint/
    # tendon synovium proliferation. ~30K US prevalent on tx (most
    # surgical; ~10K systemic biologics-eligible), ~40K EU, ~150K ROW.
    # Class: Turalio (Daiichi pexidartinib CSF-1R first-in-class but
    # hepatotoxicity REMS), Pimicotinib (Merck KGaA/Abbisko/Innovent
    # CSF-1R Ph3 MANEUVER positive 2024). Net branded ~$175K/yr.
    "oncology.musculoskeletal.tgct": {
        "us":  {"patientsK": 10,  "wtpPct": 65, "priceK": 175},
        "eu":  {"patientsK": 15,  "wtpPct": 45, "priceK": 100},
        "row": {"patientsK": 50,  "wtpPct": 12, "priceK": 35},
    },
    # GIST (gastrointestinal stromal tumor): KIT/PDGFRA-driven mesenchymal
    # tumor of the GI tract. Molecularly distinct from classical STS;
    # treatment is sequential TKI (imatinib 1L -> sunitinib 2L -> regorafenib
    # 3L -> ripretinib/Qinlock 4L; bezuclastinib Ph3 ongoing for D842V).
    # source: NCCN/NIH SEER ~5-6K US new cases/yr (~14K prevalent on tx).
    # EU5 ~5K incidence (~12K prevalent). ROW ~10K incidence (~25K prevalent).
    # Net branded ~$120K/yr (post-Gleevec generic; Stivarga ~$15K/mo,
    # Qinlock ~$35K/mo).
    "oncology.musculoskeletal.gist": {
        "us":  {"patientsK": 14,  "wtpPct": 70, "priceK": 120},
        "eu":  {"patientsK": 12,  "wtpPct": 50, "priceK": 75},
        "row": {"patientsK": 25,  "wtpPct": 15, "priceK": 30},
    },
    # Soft tissue sarcoma (STS, non-GIST): heterogeneous histology-agnostic
    # umbrella -- liposarcoma (well-diff/dediff/myxoid/pleomorphic),
    # leiomyosarcoma, undifferentiated pleomorphic sarcoma, synovial
    # sarcoma, angiosarcoma, etc. Treatment is doxorubicin/ifosfamide
    # backbone -> Halaven (eribulin, liposarcoma) / Yondelis (trabectedin,
    # L-sarcomas) / Votrient (pazopanib, non-adipocytic) / TCR-T
    # (afami-cel synovial). source: NCI SEER ~13K US new cases/yr ex-GIST;
    # ~70K prevalent on tx. EU5 ~18K incidence (~95K prevalent). ROW ~70K
    # incidence (~330K prevalent). Net branded ~$170K/yr.
    "oncology.musculoskeletal.sts": {
        "us":  {"patientsK": 70,  "wtpPct": 65, "priceK": 170},
        "eu":  {"patientsK": 95,  "wtpPct": 48, "priceK": 100},
        "row": {"patientsK": 330, "wtpPct": 14, "priceK": 35},
    },

    # ------------------------------------------------------------
    # EYE ONCOLOGY (uveal melanoma) -- biologically distinct from cutaneous
    # GNAQ/GNA11 mutations, liver-met dominant, refractory to PD-1
    # ------------------------------------------------------------
    # source: AAO uveal melanoma US incidence ~2.5K/yr; ~50% develop mets;
    # tebentafusp (Kimmtrak, gp100xCD3 ImmTAC) approved Jan-2022 for HLA-A*02:01+
    # metastatic uveal mel; WAC ~$430K/yr (weekly IV, ~12 cycles); EU EMA approved
    # Apr-2022. EU5 incidence ~3K. ROW ~6K (Asia/LATAM). Branded class peak ~$700M.
    "oncology.eye.uveal_melanoma": {
        "us":  {"patientsK": 2.5, "wtpPct": 70, "priceK": 410},
        "eu":  {"patientsK": 3,   "wtpPct": 55, "priceK": 250},
        "row": {"patientsK": 6,   "wtpPct": 10, "priceK": 80},
    },

    # ------------------------------------------------------------
    # HEAD & NECK ONCOLOGY (HNSCC) -- IO + cetuximab dominate
    # ------------------------------------------------------------
    # source: NCI SEER head & neck SCC US incidence ~70K/yr (oral cavity + pharynx
    # + larynx, excluding thyroid); EU5 ~80K (ECIS); ROW ~600K driven by India/SEA
    # tobacco/betel-quid + China NPC. Branded mix: Keytruda+chemo 1L (~$190K/yr),
    # cetuximab+chemo (~$130K/yr), Opdivo 2L. Class peak ~$5B globally.
    # MAGEA4/8-positive subset ~20-30% (TCR-T addressable).
    "oncology.head_neck.hnscc": {
        "us":  {"patientsK": 70,  "wtpPct": 65, "priceK": 145},
        "eu":  {"patientsK": 80,  "wtpPct": 50, "priceK": 85},
        "row": {"patientsK": 600, "wtpPct": 12, "priceK": 25},
    },
}


PEN_PCT = {
    "oncology.breast.her2_pos": 65,
    "oncology.breast.hr_her2_neg": 58,
    "oncology.breast.tnbc": 55,
    "oncology.genitourinary.bladder": 50,
    "oncology.genitourinary.bladder_adjuvant": 50,
    "oncology.genitourinary.prostate": 60,
    "oncology.genitourinary.rcc": 58,
    "oncology.gi.cholangiocarcinoma": 42,
    "oncology.gi.colorectal": 50,
    "oncology.gi.colorectal_adjuvant": 50,
    "oncology.gi.gastric_esoph": 48,
    "oncology.gi.hcc": 45,
    "oncology.gi.pancreatic": 40,
    "oncology.gi.pancreatic_adjuvant": 50,
    "oncology.gynecologic.ovarian": 52,
    "oncology.gynecologic.endometrial": 60,
    "oncology.hematology.aml": 48,
    "oncology.hematology.cll": 65,
    "oncology.hematology.nhl": 35,
    "oncology.hematology.nhl.dlbcl": 55,
    "oncology.hematology.nhl.fl": 45,
    "oncology.hematology.nhl.mcl": 50,
    "oncology.hematology.nhl.wm": 55,
    "oncology.hematology.nhl.mzl": 40,
    "oncology.hematology.nhl.tcell": 40,
    "oncology.hematology.myeloma": 58,
    "oncology.hematology.myeloma.1l": 70,
    "oncology.hematology.myeloma.2l_3l": 55,
    "oncology.hematology.myeloma.4l_plus": 35,
    # tcell_lymphoma renamed -> nhl.tcell (above)
    "oncology.lung.nsclc_driver.alk": 68,
    "oncology.lung.nsclc_driver.egfr": 70,
    "oncology.lung.nsclc_driver.cmet": 50,
    "oncology.lung.nsclc_driver.her2": 48,
    "oncology.lung.nsclc_driver.her3": 42,
    "oncology.lung.nsclc_driver.kras": 50,
    "oncology.lung.nsclc_driver.ros1": 65,
    "oncology.lung.nsclc_driver.trop2": 45,
    "oncology.lung.nsclc_undruggable": 55,
    "oncology.lung.nsclc_io_combo": 60,
    "oncology.lung.nsclc_adjuvant": 50,
    "oncology.lung.nsclc_io_resistant": 35,
    "oncology.lung.sclc": 48,
    # (multi_tumor.* removed -- now _platform.*)
    "oncology.neuroendocrine.gepnet": 50,
    "hematology.rare_blood.hemoglobinopathy.scd": 15,
    "hematology.rare_blood.hemoglobinopathy.beta_thalassemia": 28,
    "hematology.rare_blood.hemophilia_a": 65,
    "hematology.rare_blood.pnh": 60,
    "hematology.rare_blood.ahus": 55,
    "hematology.rare_blood.attp": 70,
    "hematology.rare_blood.hemophilia_b": 60,
    "hematology.rare_blood.vwd": 50,
    "hematology.rare_blood.fibrinogen_deficiency": 55,
    "hematology.supportive_care.volume_expander": 40,
    "hematology.myeloproliferative.mf": 65,
    "hematology.myeloproliferative.pv": 25,
    "hematology.myeloproliferative.mds": 60,
    "oncology.hematology.hodgkin": 70,
    "hematology.rare_blood.aplastic_anemia": 60,
    "oncology.hematology.cml": 65,
    "nephrology.glomerular.c3g": 45,
    "oncology.skin.melanoma": 65,
    "oncology.skin.melanoma_adjuvant": 60,
    "oncology.skin.cscc": 50,
    "oncology.skin.bcc": 45,
    "oncology.skin.merkel_cell": 60,
    "oncology.musculoskeletal.desmoid": 50,
    "oncology.musculoskeletal.nf1_pn": 30,
    "oncology.musculoskeletal.tgct": 40,
    "oncology.musculoskeletal.gist": 50,
    "oncology.musculoskeletal.sts": 35,
    "oncology.eye.uveal_melanoma": 35,
    "oncology.head_neck.hnscc": 55,
}


if __name__ == "__main__":
    print(f"Total areas: {len(REGIONS)}")
    assert set(REGIONS.keys()) == set(PEN_PCT.keys()), "REGIONS and PEN_PCT keys must match"
    for key in sorted(REGIONS.keys()):
        print(f"  {key}: pen={PEN_PCT[key]}%")
