# -*- coding: utf-8 -*-
"""Add company_slice to all remaining 23 companies' indications.

Companies: 4568, 6990, ALLO, ARQT, BCYC, BHVN, BOLD, CAMX, CELC, CRSP,
           CRVO, CRVS, GLMD, JANX, KYMR, NAMS, NKTR, NTLA, OCS, ONC,
           PRAX, RVMD, VLA
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TICKERS = [
    "4568", "6990", "ALLO", "ARQT", "BCYC", "BHVN", "BOLD", "CAMX",
    "CELC", "CRSP", "CRVO", "CRVS", "GLMD", "JANX", "KYMR", "NAMS",
    "NKTR", "NTLA", "OCS", "ONC", "PRAX", "RVMD", "VLA",
]

# ===================================================================
# SLICES keyed by (ticker, asset_id, indication_id)
# Each value: {"us": {reachPct, wtpPct, priceK}, "eu": {...}, "row": {...}}
# ===================================================================
SLICES = {
    # ---------------------------------------------------------------
    # ONC (BeOne Medicines) -- btk already has CS, add rest
    # ---------------------------------------------------------------
    # Tevimbra: commercial PD-1 $737M, 50+ markets, crowded PD-1 but growing
    ("ONC", "tevimbra", "pd1"): {
        "us": {"reachPct": 12, "wtpPct": 60, "priceK": 180},
        "eu": {"reachPct": 8, "wtpPct": 45, "priceK": 100},
        "row": {"reachPct": 8, "wtpPct": 15, "priceK": 40},
    },
    # Sonrotoclax: Ph3 BCL2, potentially best-in-class combo w/ Brukinsa
    ("ONC", "sonro", "bcl2"): {
        "us": {"reachPct": 12, "wtpPct": 45, "priceK": 180},
        "eu": {"reachPct": 8, "wtpPct": 35, "priceK": 110},
        "row": {"reachPct": 3, "wtpPct": 10, "priceK": 45},
    },
    # BTK CDAC: Ph2/3 degrader for BTK-resistant, niche
    ("ONC", "btk_cdac", "btk_deg"): {
        "us": {"reachPct": 15, "wtpPct": 40, "priceK": 200},
        "eu": {"reachPct": 10, "wtpPct": 32, "priceK": 120},
        "row": {"reachPct": 4, "wtpPct": 10, "priceK": 50},
    },
    # Pipeline: mixed Ph1-3 HCC/gastric, early
    ("ONC", "pipeline", "onc_pipe"): {
        "us": {"reachPct": 5, "wtpPct": 35, "priceK": 180},
        "eu": {"reachPct": 3, "wtpPct": 28, "priceK": 100},
        "row": {"reachPct": 2, "wtpPct": 8, "priceK": 35},
    },

    # ---------------------------------------------------------------
    # BHVN (Biohaven) -- all pre-pivotal
    # ---------------------------------------------------------------
    # Opakalim: Ph2/3 Kv7 epilepsy, novel mechanism, oral, large TAM
    ("BHVN", "bhv7000", "epilepsy"): {
        "us": {"reachPct": 5, "wtpPct": 40, "priceK": 15},
        "eu": {"reachPct": 3, "wtpPct": 30, "priceK": 8},
        "row": {"reachPct": 1, "wtpPct": 8, "priceK": 3},
    },
    # BHV-1300: Ph1b Graves' disease, first-in-class MoDE degrader
    ("BHVN", "bhv1300", "graves"): {
        "us": {"reachPct": 4, "wtpPct": 30, "priceK": 30},
        "eu": {"reachPct": 2, "wtpPct": 22, "priceK": 15},
        "row": {"reachPct": 0.5, "wtpPct": 8, "priceK": 5},
    },
    # BHV-1400: Ph1 expansion IgAN, TRAP degrader, pivotal planned
    ("BHVN", "bhv1400", "igan"): {
        "us": {"reachPct": 5, "wtpPct": 30, "priceK": 60},
        "eu": {"reachPct": 3, "wtpPct": 22, "priceK": 30},
        "row": {"reachPct": 1, "wtpPct": 8, "priceK": 12},
    },
    # Taldefgrobep: Ph2 obesity, differentiated muscle-sparing but vs GLP-1 juggernaut
    ("BHVN", "taldef", "obesity"): {
        "us": {"reachPct": 0.3, "wtpPct": 25, "priceK": 12},
        "eu": {"reachPct": 0.15, "wtpPct": 18, "priceK": 6},
        "row": {"reachPct": 0.05, "wtpPct": 5, "priceK": 2},
    },
    # BHV-1510: Ph1 Trop2 ADC, very early, crowded space
    ("BHVN", "bhv1510", "onc"): {
        "us": {"reachPct": 2, "wtpPct": 20, "priceK": 180},
        "eu": {"reachPct": 1, "wtpPct": 15, "priceK": 100},
        "row": {"reachPct": 0.5, "wtpPct": 5, "priceK": 40},
    },

    # ---------------------------------------------------------------
    # CRSP (CRISPR Therapeutics)
    # ---------------------------------------------------------------
    # Casgevy: commercial gene therapy $116M, $2.2M one-time, manufacturing constrained
    ("CRSP", "casgevy", "scd_tdt"): {
        "us": {"reachPct": 3, "wtpPct": 60, "priceK": 440},
        "eu": {"reachPct": 1.5, "wtpPct": 45, "priceK": 220},
        "row": {"reachPct": 0.3, "wtpPct": 8, "priceK": 70},
    },
    # CTX310: Ph1 in vivo ANGPTL3 gene edit for CV, one-shot cure potential, huge TAM
    ("CRSP", "ctx310", "cv_edit"): {
        "us": {"reachPct": 0.5, "wtpPct": 20, "priceK": 250},
        "eu": {"reachPct": 0.3, "wtpPct": 15, "priceK": 130},
        "row": {"reachPct": 0.1, "wtpPct": 5, "priceK": 50},
    },
    # CTX460: preclinical AATD gene edit, ultra-rare
    ("CRSP", "ctx460", "aatd"): {
        "us": {"reachPct": 8, "wtpPct": 15, "priceK": 350},
        "eu": {"reachPct": 5, "wtpPct": 10, "priceK": 180},
        "row": {"reachPct": 1, "wtpPct": 5, "priceK": 60},
    },
    # Zugocel (CTX611): Ph1/2 allogeneic CAR-T autoimmune SLE
    ("CRSP", "zugocel", "cart_ai"): {
        "us": {"reachPct": 2, "wtpPct": 25, "priceK": 350},
        "eu": {"reachPct": 1, "wtpPct": 18, "priceK": 180},
        "row": {"reachPct": 0.3, "wtpPct": 5, "priceK": 60},
    },
    # Discovery: preclinical diabetes islet + other
    ("CRSP", "discovery", "other"): {
        "us": {"reachPct": 0.3, "wtpPct": 12, "priceK": 200},
        "eu": {"reachPct": 0.2, "wtpPct": 8, "priceK": 100},
        "row": {"reachPct": 0.05, "wtpPct": 3, "priceK": 30},
    },

    # ---------------------------------------------------------------
    # PRAX (Praxis Precision Medicines) -- 2 NDAs filed + Ph3 + preclinical
    # ---------------------------------------------------------------
    # Ulixacaltamide: NDA filed ET, BTD, first new ET drug in decades
    ("PRAX", "ulixa", "et"): {
        "us": {"reachPct": 12, "wtpPct": 55, "priceK": 15},
        "eu": {"reachPct": 7, "wtpPct": 38, "priceK": 8},
        "row": {"reachPct": 2, "wtpPct": 10, "priceK": 3},
    },
    # Relutrigine: NDA filed DEEs, BTD + orphan, ultra-rare pediatric
    ("PRAX", "relut", "dee"): {
        "us": {"reachPct": 20, "wtpPct": 65, "priceK": 250},
        "eu": {"reachPct": 12, "wtpPct": 48, "priceK": 130},
        "row": {"reachPct": 3, "wtpPct": 12, "priceK": 50},
    },
    # Vormatrigine: Ph3 focal epilepsy, best-in-disease profile, crowded but differentiated
    ("PRAX", "vormat", "fos"): {
        "us": {"reachPct": 6, "wtpPct": 42, "priceK": 15},
        "eu": {"reachPct": 4, "wtpPct": 32, "priceK": 8},
        "row": {"reachPct": 1, "wtpPct": 8, "priceK": 3},
    },
    # Elsunersen: Ph3 SCN2A-DEE, orphan ASO
    ("PRAX", "elsun", "scn2a"): {
        "us": {"reachPct": 18, "wtpPct": 60, "priceK": 250},
        "eu": {"reachPct": 10, "wtpPct": 45, "priceK": 130},
        "row": {"reachPct": 2, "wtpPct": 10, "priceK": 50},
    },
    # Preclinical rare epilepsy programs
    ("PRAX", "preclin", "rare_epi"): {
        "us": {"reachPct": 1, "wtpPct": 15, "priceK": 80},
        "eu": {"reachPct": 0.5, "wtpPct": 10, "priceK": 40},
        "row": {"reachPct": 0.2, "wtpPct": 5, "priceK": 15},
    },

    # ---------------------------------------------------------------
    # CAMX (Camurus) -- SEK-denominated, SOTP
    # ---------------------------------------------------------------
    # Buvidal/Brixadi: commercial OUD, no regions in config (SOTP commercial)
    ("CAMX", "commercial", "oud"): {
        "us": {"reachPct": 25, "wtpPct": 60, "priceK": 15},
        "eu": {"reachPct": 15, "wtpPct": 50, "priceK": 8},
        "row": {"reachPct": 5, "wtpPct": 12, "priceK": 3},
    },
    # Oczyesa: commercial EU + US PDUFA Jun 2026 acromegaly, rare
    ("CAMX", "oczyesa", "acro"): {
        "us": {"reachPct": 25, "wtpPct": 65, "priceK": 100},
        "eu": {"reachPct": 15, "wtpPct": 50, "priceK": 55},
        "row": {"reachPct": 5, "wtpPct": 12, "priceK": 22},
    },
    # SORENTO: Ph3 GEP-NET vs Sandostatin LAR, rare
    ("CAMX", "sorento", "gepnet"): {
        "us": {"reachPct": 18, "wtpPct": 50, "priceK": 200},
        "eu": {"reachPct": 12, "wtpPct": 40, "priceK": 100},
        "row": {"reachPct": 3, "wtpPct": 12, "priceK": 35},
    },
    # PLD: Ph2b positive, orphan, no approved therapy
    ("CAMX", "pld", "pld"): {
        "us": {"reachPct": 5, "wtpPct": 35, "priceK": 60},
        "eu": {"reachPct": 3, "wtpPct": 25, "priceK": 30},
        "row": {"reachPct": 1, "wtpPct": 8, "priceK": 12},
    },
    # Lilly incretin: Ph1 monthly semaglutide, royalty/milestone model
    ("CAMX", "lilly", "incretin"): {
        "us": {"reachPct": 0.2, "wtpPct": 18, "priceK": 12},
        "eu": {"reachPct": 0.1, "wtpPct": 12, "priceK": 6},
        "row": {"reachPct": 0.03, "wtpPct": 5, "priceK": 2},
    },

    # ---------------------------------------------------------------
    # KYMR (Kymera) -- Ph2 degrader platform
    # ---------------------------------------------------------------
    # KT-621: Ph2b STAT6 degrader AD/asthma, oral dupilumab replacement thesis
    ("KYMR", "kt621", "stat6"): {
        "us": {"reachPct": 4, "wtpPct": 32, "priceK": 40},
        "eu": {"reachPct": 2, "wtpPct": 22, "priceK": 20},
        "row": {"reachPct": 0.5, "wtpPct": 8, "priceK": 8},
    },
    # KT-579: Ph1 IRF5 degrader autoimmune, first-in-class
    ("KYMR", "kt579", "irf5"): {
        "us": {"reachPct": 3, "wtpPct": 22, "priceK": 50},
        "eu": {"reachPct": 1.5, "wtpPct": 15, "priceK": 25},
        "row": {"reachPct": 0.5, "wtpPct": 5, "priceK": 10},
    },
    # IRAK4: Ph1 (Sanofi partnered), 50/50 US profit split
    ("KYMR", "irak4", "irak4"): {
        "us": {"reachPct": 3, "wtpPct": 22, "priceK": 45},
        "eu": {"reachPct": 1.5, "wtpPct": 15, "priceK": 22},
        "row": {"reachPct": 0.5, "wtpPct": 5, "priceK": 8},
    },
    # CDK2: preclinical (Gilead option), royalties only
    ("KYMR", "cdk2", "onc"): {
        "us": {"reachPct": 1, "wtpPct": 12, "priceK": 150},
        "eu": {"reachPct": 0.5, "wtpPct": 8, "priceK": 80},
        "row": {"reachPct": 0.2, "wtpPct": 3, "priceK": 30},
    },

    # ---------------------------------------------------------------
    # NKTR (Nektar) -- Treg IL-2 platform
    # ---------------------------------------------------------------
    # Rezpeg AD: Ph2b complete, Ph3 starting Q2 2026, SC biologic
    ("NKTR", "rezpeg_ad", "ad"): {
        "us": {"reachPct": 5, "wtpPct": 38, "priceK": 40},
        "eu": {"reachPct": 3, "wtpPct": 28, "priceK": 20},
        "row": {"reachPct": 0.8, "wtpPct": 8, "priceK": 8},
    },
    # Rezpeg AA: Ph2b, stat sig with exclusions, safety edge vs JAKi
    ("NKTR", "rezpeg_aa", "aa"): {
        "us": {"reachPct": 5, "wtpPct": 30, "priceK": 40},
        "eu": {"reachPct": 3, "wtpPct": 22, "priceK": 20},
        "row": {"reachPct": 0.5, "wtpPct": 6, "priceK": 8},
    },
    # Rezpeg T1D: Ph2, early, speculative
    ("NKTR", "rezpeg_t1d", "t1d"): {
        "us": {"reachPct": 1, "wtpPct": 20, "priceK": 30},
        "eu": {"reachPct": 0.5, "wtpPct": 15, "priceK": 15},
        "row": {"reachPct": 0.2, "wtpPct": 5, "priceK": 5},
    },
    # NKTR-255: Ph1/2 IL-15 combo with CAR-T, niche
    ("NKTR", "nktr255", "onc"): {
        "us": {"reachPct": 8, "wtpPct": 25, "priceK": 100},
        "eu": {"reachPct": 4, "wtpPct": 18, "priceK": 60},
        "row": {"reachPct": 1, "wtpPct": 5, "priceK": 25},
    },

    # ---------------------------------------------------------------
    # 4568 (Daiichi Sankyo) -- SOTP commercial + pipeline
    # ---------------------------------------------------------------
    # Enhertu: commercial $4.6B, #1 ADC, partnered AZ
    ("4568", "commercial", "her2"): {
        "us": {"reachPct": 30, "wtpPct": 70, "priceK": 200},
        "eu": {"reachPct": 22, "wtpPct": 55, "priceK": 110},
        "row": {"reachPct": 8, "wtpPct": 15, "priceK": 50},
    },
    # Datroway: newly launched TROP2, exceeding forecasts, $350M
    ("4568", "datroway", "trop2"): {
        "us": {"reachPct": 18, "wtpPct": 55, "priceK": 180},
        "eu": {"reachPct": 10, "wtpPct": 40, "priceK": 100},
        "row": {"reachPct": 3, "wtpPct": 10, "priceK": 40},
    },
    # HER3-DXd: Ph3 with Merck, first-in-class
    ("4568", "her3_dxd", "her3"): {
        "us": {"reachPct": 12, "wtpPct": 42, "priceK": 200},
        "eu": {"reachPct": 7, "wtpPct": 32, "priceK": 110},
        "row": {"reachPct": 2, "wtpPct": 8, "priceK": 45},
    },
    # I-DXd + R-DXd: Ph1-3 Merck ADCs
    ("4568", "idxd", "merck_adc"): {
        "us": {"reachPct": 3, "wtpPct": 35, "priceK": 200},
        "eu": {"reachPct": 2, "wtpPct": 25, "priceK": 110},
        "row": {"reachPct": 0.5, "wtpPct": 8, "priceK": 45},
    },
    # Japan legacy: declining, mature portfolio but still ~JPY 500B/yr
    ("4568", "japan_legacy", "japan"): {
        "us": {"reachPct": 5, "wtpPct": 52, "priceK": 8},
        "eu": {"reachPct": 3, "wtpPct": 42, "priceK": 4},
        "row": {"reachPct": 12, "wtpPct": 40, "priceK": 3},
    },

    # ---------------------------------------------------------------
    # 6990 (Kelun-Biotech)
    # ---------------------------------------------------------------
    # Sac-TMT: commercial China TROP2, $200M, Merck global partner
    ("6990", "commercial", "trop2"): {
        "us": {"reachPct": 12, "wtpPct": 50, "priceK": 180},
        "eu": {"reachPct": 7, "wtpPct": 38, "priceK": 100},
        "row": {"reachPct": 10, "wtpPct": 15, "priceK": 45},
    },
    # A166: commercial China HER2 ADC, $150M
    ("6990", "a166", "her2_adc"): {
        "us": {"reachPct": 3, "wtpPct": 35, "priceK": 180},
        "eu": {"reachPct": 2, "wtpPct": 25, "priceK": 100},
        "row": {"reachPct": 5, "wtpPct": 15, "priceK": 45},
    },
    # SKB315: Ph2/3 CLDN18.2 ADC gastric
    ("6990", "skb315", "cldn"): {
        "us": {"reachPct": 8, "wtpPct": 38, "priceK": 180},
        "eu": {"reachPct": 5, "wtpPct": 28, "priceK": 100},
        "row": {"reachPct": 5, "wtpPct": 10, "priceK": 40},
    },
    # Merck-partnered Nectin-4 + bsADC pipeline
    ("6990", "merck_pipe", "merck_adc"): {
        "us": {"reachPct": 2, "wtpPct": 25, "priceK": 200},
        "eu": {"reachPct": 1, "wtpPct": 18, "priceK": 110},
        "row": {"reachPct": 0.5, "wtpPct": 5, "priceK": 40},
    },
    # OptiDC platform: preclinical/Ph1
    ("6990", "platform", "next_gen"): {
        "us": {"reachPct": 0.5, "wtpPct": 12, "priceK": 200},
        "eu": {"reachPct": 0.3, "wtpPct": 8, "priceK": 110},
        "row": {"reachPct": 0.2, "wtpPct": 3, "priceK": 40},
    },

    # ---------------------------------------------------------------
    # RVMD (Revolution Medicines)
    # ---------------------------------------------------------------
    # Daraxonrasib PDAC: Ph3, BTD, unprecedented OS data
    ("RVMD", "darax_pdac", "pdac"): {
        "us": {"reachPct": 20, "wtpPct": 50, "priceK": 180},
        "eu": {"reachPct": 12, "wtpPct": 38, "priceK": 100},
        "row": {"reachPct": 3, "wtpPct": 8, "priceK": 40},
    },
    # Daraxonrasib NSCLC: Ph3 2L+ vs docetaxel
    ("RVMD", "darax_nsclc", "nsclc"): {
        "us": {"reachPct": 18, "wtpPct": 48, "priceK": 180},
        "eu": {"reachPct": 10, "wtpPct": 35, "priceK": 100},
        "row": {"reachPct": 3, "wtpPct": 8, "priceK": 40},
    },
    # Zoldonrasib: Ph3 G12D-selective, BTD, first-in-class
    ("RVMD", "zoldon", "g12d"): {
        "us": {"reachPct": 8, "wtpPct": 42, "priceK": 180},
        "eu": {"reachPct": 5, "wtpPct": 32, "priceK": 100},
        "row": {"reachPct": 1.5, "wtpPct": 8, "priceK": 40},
    },
    # Elironrasib: Ph1/2 G12C next-gen
    ("RVMD", "eliron", "g12c"): {
        "us": {"reachPct": 8, "wtpPct": 30, "priceK": 180},
        "eu": {"reachPct": 5, "wtpPct": 22, "priceK": 100},
        "row": {"reachPct": 1, "wtpPct": 6, "priceK": 40},
    },
    # Pipeline: G12V, Q61H, G13C, early
    ("RVMD", "pipeline", "other_ras"): {
        "us": {"reachPct": 3, "wtpPct": 20, "priceK": 180},
        "eu": {"reachPct": 2, "wtpPct": 15, "priceK": 100},
        "row": {"reachPct": 0.5, "wtpPct": 5, "priceK": 40},
    },

    # ---------------------------------------------------------------
    # NAMS (NewAmsterdam Pharma) -- mass market oral LDL
    # ---------------------------------------------------------------
    # Obicetrapib mono: EMA H2 2026, mass market oral
    ("NAMS", "obi_mono", "ldl_mono"): {
        "us": {"reachPct": 1.5, "wtpPct": 35, "priceK": 6},
        "eu": {"reachPct": 1.0, "wtpPct": 30, "priceK": 3},
        "row": {"reachPct": 0.3, "wtpPct": 8, "priceK": 1.5},
    },
    # Obicetrapib FDC: EMA H2 2026
    ("NAMS", "obi_fdc", "ldl_fdc"): {
        "us": {"reachPct": 1.2, "wtpPct": 38, "priceK": 7},
        "eu": {"reachPct": 0.8, "wtpPct": 32, "priceK": 3.5},
        "row": {"reachPct": 0.2, "wtpPct": 8, "priceK": 1.5},
    },
    # PREVAIL CVOT: Ph3, the binary event for US access
    ("NAMS", "prevail", "cvot"): {
        "us": {"reachPct": 1.0, "wtpPct": 30, "priceK": 8},
        "eu": {"reachPct": 0.6, "wtpPct": 25, "priceK": 4},
        "row": {"reachPct": 0.2, "wtpPct": 6, "priceK": 2},
    },
    # Alzheimer: Ph2, speculative biomarker data
    ("NAMS", "alzheimer", "alz"): {
        "us": {"reachPct": 0.3, "wtpPct": 15, "priceK": 8},
        "eu": {"reachPct": 0.15, "wtpPct": 10, "priceK": 4},
        "row": {"reachPct": 0.05, "wtpPct": 3, "priceK": 2},
    },
    # RUBENS T2D: Ph3 enrolling
    ("NAMS", "rubens", "t2d"): {
        "us": {"reachPct": 0.5, "wtpPct": 28, "priceK": 6},
        "eu": {"reachPct": 0.3, "wtpPct": 22, "priceK": 3},
        "row": {"reachPct": 0.1, "wtpPct": 5, "priceK": 1.5},
    },

    # ---------------------------------------------------------------
    # GLMD (Galmed) -- micro-cap, speculative pivots
    # ---------------------------------------------------------------
    # Aramchol oncology CRC: Ph1b, no human data yet
    ("GLMD", "aramchol_onco", "crc"): {
        "us": {"reachPct": 1, "wtpPct": 12, "priceK": 30},
        "eu": {"reachPct": 0.5, "wtpPct": 8, "priceK": 15},
        "row": {"reachPct": 0.2, "wtpPct": 3, "priceK": 6},
    },
    # HCC: Ph1b basket
    ("GLMD", "aramchol_hcc", "hcc"): {
        "us": {"reachPct": 1.5, "wtpPct": 12, "priceK": 30},
        "eu": {"reachPct": 0.8, "wtpPct": 8, "priceK": 15},
        "row": {"reachPct": 0.3, "wtpPct": 3, "priceK": 6},
    },
    # Cholangiocarcinoma: Ph1b basket, rare
    ("GLMD", "aramchol_chol", "chol"): {
        "us": {"reachPct": 2, "wtpPct": 15, "priceK": 30},
        "eu": {"reachPct": 1, "wtpPct": 10, "priceK": 15},
        "row": {"reachPct": 0.5, "wtpPct": 5, "priceK": 6},
    },
    # Parkinson: preclinical brain-penetrant LNP, speculative
    ("GLMD", "aramchol_pd", "pd"): {
        "us": {"reachPct": 0.5, "wtpPct": 8, "priceK": 25},
        "eu": {"reachPct": 0.3, "wtpPct": 5, "priceK": 12},
        "row": {"reachPct": 0.1, "wtpPct": 2, "priceK": 5},
    },
    # NASH/MASH legacy: dormant, combo only
    ("GLMD", "aramchol_nash_legacy", "mash"): {
        "us": {"reachPct": 0.3, "wtpPct": 8, "priceK": 20},
        "eu": {"reachPct": 0.15, "wtpPct": 5, "priceK": 10},
        "row": {"reachPct": 0.05, "wtpPct": 2, "priceK": 4},
    },

    # ---------------------------------------------------------------
    # NTLA (Intellia) -- in vivo CRISPR gene editing
    # ---------------------------------------------------------------
    # Lonvo-z HAE: Ph3 HAELO, BLA H2 2026, one-time gene edit
    ("NTLA", "lonvoz", "hae"): {
        "us": {"reachPct": 30, "wtpPct": 65, "priceK": 500},
        "eu": {"reachPct": 18, "wtpPct": 50, "priceK": 250},
        "row": {"reachPct": 5, "wtpPct": 12, "priceK": 80},
    },
    # Nexiguran ATTR-CM: Ph3, one-time gene edit for large population
    ("NTLA", "nexz_cm", "attr_cm"): {
        "us": {"reachPct": 5, "wtpPct": 42, "priceK": 500},
        "eu": {"reachPct": 3, "wtpPct": 30, "priceK": 250},
        "row": {"reachPct": 1, "wtpPct": 8, "priceK": 80},
    },
    # Nexiguran ATTR-PN: Ph3 data, polyneuropathy
    ("NTLA", "nexz_pn", "attr_pn"): {
        "us": {"reachPct": 15, "wtpPct": 50, "priceK": 500},
        "eu": {"reachPct": 8, "wtpPct": 38, "priceK": 250},
        "row": {"reachPct": 2, "wtpPct": 10, "priceK": 80},
    },

    # ---------------------------------------------------------------
    # CELC (Celcuity) -- gedatolisib PI3K/mTOR breast cancer
    # ---------------------------------------------------------------
    # Geda WT: NDA Priority Review, PDUFA Jul 17, best PFS ever in 2L+ HR+/HER2-
    ("CELC", "geda_wt", "bc_wt"): {
        "us": {"reachPct": 15, "wtpPct": 55, "priceK": 150},
        "eu": {"reachPct": 8, "wtpPct": 40, "priceK": 80},
        "row": {"reachPct": 2, "wtpPct": 10, "priceK": 30},
    },
    # Geda MT: PIK3CA-mutant expansion
    ("CELC", "geda_mt", "bc_mt"): {
        "us": {"reachPct": 10, "wtpPct": 48, "priceK": 150},
        "eu": {"reachPct": 5, "wtpPct": 35, "priceK": 80},
        "row": {"reachPct": 1.5, "wtpPct": 8, "priceK": 30},
    },
    # Geda 1L: earlier line potential
    ("CELC", "geda_1l", "bc_1l"): {
        "us": {"reachPct": 5, "wtpPct": 35, "priceK": 150},
        "eu": {"reachPct": 3, "wtpPct": 25, "priceK": 80},
        "row": {"reachPct": 1, "wtpPct": 6, "priceK": 30},
    },
    # Geda prostate: early exploration
    ("CELC", "geda_prost", "prost"): {
        "us": {"reachPct": 2, "wtpPct": 22, "priceK": 150},
        "eu": {"reachPct": 1, "wtpPct": 15, "priceK": 80},
        "row": {"reachPct": 0.5, "wtpPct": 5, "priceK": 30},
    },

    # ---------------------------------------------------------------
    # CRVO (CervoMed) -- micro-cap, financing-dependent
    # ---------------------------------------------------------------
    # Neflamapimod DLB: Ph3 ready, no approved DMTs
    ("CRVO", "nef_dlb", "dlb"): {
        "us": {"reachPct": 3, "wtpPct": 35, "priceK": 25},
        "eu": {"reachPct": 2, "wtpPct": 25, "priceK": 12},
        "row": {"reachPct": 0.5, "wtpPct": 6, "priceK": 5},
    },
    # Nef stroke: early
    ("CRVO", "nef_stroke", "stroke"): {
        "us": {"reachPct": 0.5, "wtpPct": 18, "priceK": 20},
        "eu": {"reachPct": 0.3, "wtpPct": 12, "priceK": 10},
        "row": {"reachPct": 0.1, "wtpPct": 3, "priceK": 4},
    },
    # Nef ALS: rare, no good treatments
    ("CRVO", "nef_als", "als"): {
        "us": {"reachPct": 5, "wtpPct": 25, "priceK": 100},
        "eu": {"reachPct": 3, "wtpPct": 18, "priceK": 50},
        "row": {"reachPct": 1, "wtpPct": 5, "priceK": 20},
    },
    # Nef PPA: ultra-rare, Ph2
    ("CRVO", "nef_ppa", "ppa"): {
        "us": {"reachPct": 5, "wtpPct": 22, "priceK": 30},
        "eu": {"reachPct": 3, "wtpPct": 15, "priceK": 15},
        "row": {"reachPct": 1, "wtpPct": 5, "priceK": 6},
    },

    # ---------------------------------------------------------------
    # CRVS (Corvus) -- ITK inhibitor soquelitinib
    # ---------------------------------------------------------------
    # PTCL: Ph3 registrational, orphan, first-in-class
    ("CRVS", "soq_ptcl", "ptcl"): {
        "us": {"reachPct": 25, "wtpPct": 55, "priceK": 200},
        "eu": {"reachPct": 15, "wtpPct": 42, "priceK": 100},
        "row": {"reachPct": 4, "wtpPct": 10, "priceK": 35},
    },
    # AD: Ph2 starting H1 2026, large TAM, oral
    ("CRVS", "soq_ad", "ad"): {
        "us": {"reachPct": 3, "wtpPct": 25, "priceK": 40},
        "eu": {"reachPct": 2, "wtpPct": 18, "priceK": 20},
        "row": {"reachPct": 0.5, "wtpPct": 5, "priceK": 8},
    },
    # Severe asthma: early
    ("CRVS", "soq_asthma", "severe_asthma"): {
        "us": {"reachPct": 1, "wtpPct": 18, "priceK": 40},
        "eu": {"reachPct": 0.5, "wtpPct": 12, "priceK": 20},
        "row": {"reachPct": 0.2, "wtpPct": 4, "priceK": 8},
    },
    # HS: Ph2
    ("CRVS", "soq_hs", "hs"): {
        "us": {"reachPct": 5, "wtpPct": 28, "priceK": 45},
        "eu": {"reachPct": 3, "wtpPct": 20, "priceK": 22},
        "row": {"reachPct": 1, "wtpPct": 5, "priceK": 8},
    },

    # ---------------------------------------------------------------
    # JANX (Janux) -- TRACTr platform
    # ---------------------------------------------------------------
    # JANX007: Ph1a/b PSMA mCRPC, 109 pts treated
    ("JANX", "janx007", "mcrpc"): {
        "us": {"reachPct": 3, "wtpPct": 25, "priceK": 200},
        "eu": {"reachPct": 1.5, "wtpPct": 18, "priceK": 110},
        "row": {"reachPct": 0.5, "wtpPct": 5, "priceK": 40},
    },
    # JANX008: Ph1 EGFR solid tumors
    ("JANX", "janx008", "egfr_solid"): {
        "us": {"reachPct": 3, "wtpPct": 20, "priceK": 180},
        "eu": {"reachPct": 1.5, "wtpPct": 15, "priceK": 100},
        "row": {"reachPct": 0.5, "wtpPct": 4, "priceK": 40},
    },
    # JANX011: Ph1 CD19 autoimmune
    ("JANX", "janx011", "autoimmune"): {
        "us": {"reachPct": 2, "wtpPct": 18, "priceK": 300},
        "eu": {"reachPct": 1, "wtpPct": 12, "priceK": 150},
        "row": {"reachPct": 0.3, "wtpPct": 4, "priceK": 50},
    },
    # PSMA-TRACIr: preclinical radioconjugate
    ("JANX", "psma_tracir", "tracir"): {
        "us": {"reachPct": 1, "wtpPct": 12, "priceK": 200},
        "eu": {"reachPct": 0.5, "wtpPct": 8, "priceK": 110},
        "row": {"reachPct": 0.2, "wtpPct": 3, "priceK": 40},
    },
    # Merck + BMS partnerships: early
    ("JANX", "merck_bms", "partnerships"): {
        "us": {"reachPct": 0.5, "wtpPct": 10, "priceK": 200},
        "eu": {"reachPct": 0.3, "wtpPct": 7, "priceK": 110},
        "row": {"reachPct": 0.1, "wtpPct": 3, "priceK": 40},
    },

    # ---------------------------------------------------------------
    # ALLO (Allogene) -- allogeneic CAR-T
    # ---------------------------------------------------------------
    # Cema-cel: Ph2 pivotal 1L LBCL MRD+ consolidation
    ("ALLO", "cema_cel", "lbcl_1l"): {
        "us": {"reachPct": 5, "wtpPct": 35, "priceK": 400},
        "eu": {"reachPct": 3, "wtpPct": 25, "priceK": 200},
        "row": {"reachPct": 1, "wtpPct": 5, "priceK": 80},
    },
    # ALLO-329: Ph1 allogeneic CAR-T SLE autoimmune
    ("ALLO", "allo329", "sle_basket"): {
        "us": {"reachPct": 2, "wtpPct": 20, "priceK": 300},
        "eu": {"reachPct": 1, "wtpPct": 14, "priceK": 150},
        "row": {"reachPct": 0.3, "wtpPct": 4, "priceK": 50},
    },
    # ALLO-316: anti-CD70 RCC
    ("ALLO", "allo316", "ccrcc"): {
        "us": {"reachPct": 2, "wtpPct": 18, "priceK": 400},
        "eu": {"reachPct": 1, "wtpPct": 12, "priceK": 200},
        "row": {"reachPct": 0.3, "wtpPct": 4, "priceK": 80},
    },

    # ---------------------------------------------------------------
    # BCYC (Bicycle Therapeutics) -- bicycle peptide platform
    # ---------------------------------------------------------------
    # Zelenectide: Ph2/3 mUC, approval path rejected, pivoting
    ("BCYC", "zelenectide", "muc"): {
        "us": {"reachPct": 3, "wtpPct": 25, "priceK": 180},
        "eu": {"reachPct": 2, "wtpPct": 18, "priceK": 100},
        "row": {"reachPct": 0.5, "wtpPct": 5, "priceK": 35},
    },
    # Nuzefatide: EphA2 targeted, Ph1/2 dose escalation
    ("BCYC", "nuzefatide", "epha2"): {
        "us": {"reachPct": 4, "wtpPct": 22, "priceK": 180},
        "eu": {"reachPct": 2, "wtpPct": 15, "priceK": 100},
        "row": {"reachPct": 0.5, "wtpPct": 5, "priceK": 35},
    },
    # BRC: bicycle radio conjugate, preclinical
    ("BCYC", "brc", "radio"): {
        "us": {"reachPct": 1, "wtpPct": 12, "priceK": 200},
        "eu": {"reachPct": 0.5, "wtpPct": 8, "priceK": 110},
        "row": {"reachPct": 0.2, "wtpPct": 3, "priceK": 40},
    },
    # BT7480: Ph1 TICA immune agonist
    ("BCYC", "bt7480", "tica"): {
        "us": {"reachPct": 1.5, "wtpPct": 15, "priceK": 180},
        "eu": {"reachPct": 0.8, "wtpPct": 10, "priceK": 100},
        "row": {"reachPct": 0.3, "wtpPct": 3, "priceK": 35},
    },
    # Platform/discovery
    ("BCYC", "platform", "disc"): {
        "us": {"reachPct": 0.5, "wtpPct": 8, "priceK": 180},
        "eu": {"reachPct": 0.3, "wtpPct": 5, "priceK": 100},
        "row": {"reachPct": 0.1, "wtpPct": 2, "priceK": 35},
    },

    # ---------------------------------------------------------------
    # OCS (Oculis) -- ophthalmology
    # ---------------------------------------------------------------
    # Privosegtor ON: registrational, BTD, orphan, no approved therapies
    ("OCS", "privo_on", "on"): {
        "us": {"reachPct": 25, "wtpPct": 60, "priceK": 200},
        "eu": {"reachPct": 15, "wtpPct": 45, "priceK": 100},
        "row": {"reachPct": 4, "wtpPct": 12, "priceK": 35},
    },
    # Privosegtor NAION: registrational
    ("OCS", "privo_naion", "naion"): {
        "us": {"reachPct": 20, "wtpPct": 55, "priceK": 200},
        "eu": {"reachPct": 12, "wtpPct": 40, "priceK": 100},
        "row": {"reachPct": 3, "wtpPct": 10, "priceK": 35},
    },
    # OCS-01 DME: Ph3 topical, large TAM
    ("OCS", "ocs01", "dme"): {
        "us": {"reachPct": 3, "wtpPct": 35, "priceK": 15},
        "eu": {"reachPct": 2, "wtpPct": 25, "priceK": 8},
        "row": {"reachPct": 0.5, "wtpPct": 8, "priceK": 3},
    },
    # Licaminlimab DED: Ph2
    ("OCS", "licam", "ded"): {
        "us": {"reachPct": 2, "wtpPct": 25, "priceK": 12},
        "eu": {"reachPct": 1, "wtpPct": 18, "priceK": 6},
        "row": {"reachPct": 0.3, "wtpPct": 5, "priceK": 3},
    },

    # ---------------------------------------------------------------
    # VLA (Valneva) -- vaccines, SOTP
    # ---------------------------------------------------------------
    # VLA15 Lyme: royalty stream from Pfizer
    ("VLA", "vla15", "lyme"): {
        "us": {"reachPct": 5, "wtpPct": 50, "priceK": 0.2},
        "eu": {"reachPct": 3, "wtpPct": 40, "priceK": 0.15},
        "row": {"reachPct": 0.5, "wtpPct": 10, "priceK": 0.05},
    },
    # IXCHIQ chikungunya: commercial $30M, only approved chik vaccine globally, travel + endemic + military
    ("VLA", "ixchiq", "chik"): {
        "us": {"reachPct": 55, "wtpPct": 72, "priceK": 0.28},
        "eu": {"reachPct": 35, "wtpPct": 58, "priceK": 0.18},
        "row": {"reachPct": 22, "wtpPct": 35, "priceK": 0.1},
    },
    # S4V2 Shigella: Ph2
    ("VLA", "s4v2", "shig"): {
        "us": {"reachPct": 2, "wtpPct": 25, "priceK": 0.2},
        "eu": {"reachPct": 1, "wtpPct": 18, "priceK": 0.12},
        "row": {"reachPct": 1, "wtpPct": 8, "priceK": 0.05},
    },
    # Zika: Ph1
    ("VLA", "zika", "zika"): {
        "us": {"reachPct": 1, "wtpPct": 15, "priceK": 0.15},
        "eu": {"reachPct": 0.5, "wtpPct": 10, "priceK": 0.1},
        "row": {"reachPct": 1, "wtpPct": 8, "priceK": 0.05},
    },
    # Commercial travel vaccines (IXIARO + DUKORAL)
    ("VLA", "commercial", "travel"): {
        "us": {"reachPct": 10, "wtpPct": 60, "priceK": 0.2},
        "eu": {"reachPct": 8, "wtpPct": 50, "priceK": 0.15},
        "row": {"reachPct": 3, "wtpPct": 15, "priceK": 0.08},
    },

    # ---------------------------------------------------------------
    # BOLD (Boundless Bio) -- below cash micro-cap
    # ---------------------------------------------------------------
    # BBI-940 ER+/HER2- breast: Ph1 starting H1 2026
    ("BOLD", "bbi940_er", "er_her2_neg_amp"): {
        "us": {"reachPct": 1, "wtpPct": 12, "priceK": 150},
        "eu": {"reachPct": 0.5, "wtpPct": 8, "priceK": 80},
        "row": {"reachPct": 0.2, "wtpPct": 3, "priceK": 30},
    },
    # BBI-940 TNBC LAR: Ph1
    ("BOLD", "bbi940_tnbc", "tnbc_lar_amp"): {
        "us": {"reachPct": 3, "wtpPct": 15, "priceK": 150},
        "eu": {"reachPct": 1.5, "wtpPct": 10, "priceK": 80},
        "row": {"reachPct": 0.5, "wtpPct": 4, "priceK": 30},
    },

    # ---------------------------------------------------------------
    # ARQT (Arcutis) -- ZORYVE topical derm franchise, SOTP commercial
    # ---------------------------------------------------------------
    # ZORYVE commercial: $250M (annualized), growing 30%+, profitable
    ("ARQT", "commercial", "derm"): {
        "us": {"reachPct": 8, "wtpPct": 65, "priceK": 18},
        "eu": {"reachPct": 3, "wtpPct": 40, "priceK": 9},
        "row": {"reachPct": 1, "wtpPct": 10, "priceK": 4},
    },
    # ZORYVE expansions: infant AD + new formulations
    ("ARQT", "zoryve_exp", "derm_exp"): {
        "us": {"reachPct": 3, "wtpPct": 50, "priceK": 8},
        "eu": {"reachPct": 2, "wtpPct": 35, "priceK": 4},
        "row": {"reachPct": 0.5, "wtpPct": 8, "priceK": 2},
    },
    # ARQ-234: AD biologic, Ph2
    ("ARQT", "arq234", "ad_bio"): {
        "us": {"reachPct": 3, "wtpPct": 28, "priceK": 45},
        "eu": {"reachPct": 2, "wtpPct": 20, "priceK": 22},
        "row": {"reachPct": 0.5, "wtpPct": 5, "priceK": 8},
    },
    # ARQ-255: topical alopecia, early
    ("ARQT", "arq255", "aa_top"): {
        "us": {"reachPct": 4, "wtpPct": 30, "priceK": 15},
        "eu": {"reachPct": 2, "wtpPct": 22, "priceK": 8},
        "row": {"reachPct": 0.5, "wtpPct": 6, "priceK": 3},
    },
    # ARQ-252: hand eczema + vitiligo
    ("ARQT", "arq252", "hand_vit"): {
        "us": {"reachPct": 2, "wtpPct": 25, "priceK": 12},
        "eu": {"reachPct": 1, "wtpPct": 18, "priceK": 6},
        "row": {"reachPct": 0.3, "wtpPct": 5, "priceK": 3},
    },
}

# ===================================================================
# SOURCES for company_slice (us.reachPct and us.priceK rationale)
# ===================================================================
SOURCES = {
    ("ONC", "tevimbra", "pd1"): {
        "us.reachPct": {"note": "Tevimbra late entrant in crowded PD-1 class (Keytruda/Opdivo dominant); ~8% reach in niche solid tumor indications where tislelizumab has data"},
        "us.priceK": {"note": "PD-1 class pricing ~$180K/yr US WAC; Tevimbra priced competitively with existing IO agents"},
    },
    ("ONC", "sonro", "bcl2"): {
        "us.reachPct": {"note": "Ph3 BCL2 -- strong combo data with Brukinsa positions for 12% reach in CLL/NHL BCL2-eligible patients"},
        "us.priceK": {"note": "BCL2 class pricing anchored by venetoclax ~$180K/yr; sonrotoclax priced at parity"},
    },
    ("ONC", "btk_cdac", "btk_deg"): {
        "us.reachPct": {"note": "BTK-resistant niche is small (15K US pts) but high unmet need; 15% reach = patients who failed prior BTKi"},
        "us.priceK": {"note": "Next-gen BTK degrader priced at premium to BTKi class (~$200K/yr) for resistance setting"},
    },
    ("ONC", "pipeline", "onc_pipe"): {
        "us.reachPct": {"note": "Mixed early pipeline (HCC orphan, gastric, other) -- 5% reach reflects Ph1-3 mix across multiple tumors"},
        "us.priceK": {"note": "Oncology specialty pricing ~$180K/yr across IO/targeted combos"},
    },
    ("BHVN", "bhv7000", "epilepsy"): {
        "us.reachPct": {"note": "Ph2/3 novel Kv7 mechanism in 1.2M US epilepsy patients; 5% reach reflects 3rd+ line ASM positioning and Ph2/3 stage"},
        "us.priceK": {"note": "Specialty oral epilepsy ASM class ~$15K/yr (cenobamate, brivaracetam benchmarks)"},
    },
    ("BHVN", "bhv1300", "graves"): {
        "us.reachPct": {"note": "Ph1b first-in-class MoDE IgG degrader; 4% reach in 500K Graves' reflects early stage + need to displace antithyroid drugs"},
        "us.priceK": {"note": "Specialty biologic for autoimmune endocrine ~$30K/yr; premium to generic antithyroid drugs but below mAb pricing"},
    },
    ("BHVN", "bhv1400", "igan"): {
        "us.reachPct": {"note": "Ph1 expansion TRAP degrader; 5% reach in 130K IgAN patients reflects early but promising biomarker data"},
        "us.priceK": {"note": "IgAN specialty pricing anchored by Filspari (~$60K/yr); novel mechanism commands parity"},
    },
    ("BHVN", "taldef", "obesity"): {
        "us.reachPct": {"note": "Ph2 in massive 40M-patient US obesity market; 0.3% reach reflects differentiated but unproven muscle-sparing vs dominant GLP-1s"},
        "us.priceK": {"note": "Obesity class pricing ~$12K/yr (GLP-1 net benchmark); taldefgrobep positioned similarly"},
    },
    ("BHVN", "bhv1510", "onc"): {
        "us.reachPct": {"note": "Ph1 Trop2 ADC in crowded space (Trodelvy, Dato-DXd); 2% reach reflects very early single-agent data"},
        "us.priceK": {"note": "ADC oncology class pricing ~$180K/yr US (Trodelvy/Enhertu benchmarks)"},
    },
    ("CRSP", "casgevy", "scd_tdt"): {
        "us.reachPct": {"note": "Commercial gene therapy but manufacturing-constrained; 64 infusions in Year 1; 3% of 100K US SCD/TDT patients reflects manufacturing bottleneck"},
        "us.priceK": {"note": "One-time gene therapy priced $2.2M; amortized to ~$440K/yr over 5yr for SOM calculation"},
    },
    ("CRSP", "ctx310", "cv_edit"): {
        "us.reachPct": {"note": "Ph1 in vivo CRISPR gene edit for 5M US CV patients; 0.5% reach reflects early Ph1 + gene editing safety concerns in large population"},
        "us.priceK": {"note": "One-time CV gene edit priced ~$500K; amortized to ~$250K/yr; large-pop discount vs rare disease gene therapy"},
    },
    ("CRSP", "ctx460", "aatd"): {
        "us.reachPct": {"note": "Preclinical ultra-rare AATD (3K US pts); 8% reach reflects small diagnosed population + orphan positioning"},
        "us.priceK": {"note": "Ultra-rare gene edit priced at $350K/yr (chronic equivalent); A1AT augmentation therapy benchmark ~$100K, gene edit premium"},
    },
    ("CRSP", "zugocel", "cart_ai"): {
        "us.reachPct": {"note": "Ph1/2 allogeneic CAR-T for SLE; 2% of 300K US patients reflects early off-the-shelf CAR-T for autoimmune"},
        "us.priceK": {"note": "Allogeneic CAR-T for autoimmune ~$350K one-time; less than autologous CAR-T ($400-500K) due to off-the-shelf manufacturing"},
    },
    ("CRSP", "discovery", "other"): {
        "us.reachPct": {"note": "Preclinical discovery (diabetes islets + other); 0.3% reach in 1.6M T1D reflects very early stage"},
        "us.priceK": {"note": "Gene-edited islet cells for T1D -- one-time therapy priced ~$200K amortized; novel but preclinical"},
    },
    ("PRAX", "ulixa", "et"): {
        "us.reachPct": {"note": "NDA filed with BTD for ET -- first new pharmacological treatment in decades for 500K diagnosed US patients; 12% reach post-approval"},
        "us.priceK": {"note": "Specialty oral CNS pricing ~$15K/yr; novel mechanism but ET market has no pricing precedent for new Rx"},
    },
    ("PRAX", "relut", "dee"): {
        "us.reachPct": {"note": "NDA filed BTD+orphan for ultra-rare pediatric DEEs; 20% reach in small 30K US pop reflects high unmet need + precision targeting"},
        "us.priceK": {"note": "Orphan rare epilepsy pricing ~$250K/yr; SCN2A/SCN8A precision therapy commands orphan premium (Epidiolex $40K, Ztalmy $70K -- but this is more targeted)"},
    },
    ("PRAX", "vormat", "fos"): {
        "us.reachPct": {"note": "Ph3 best-in-disease NaV modulator; 6% reach in 1.2M epilepsy patients reflects crowded ASM market (lacosamide, cenobamate)"},
        "us.priceK": {"note": "Specialty oral ASM ~$15K/yr (cenobamate/brivaracetam benchmark)"},
    },
    ("PRAX", "elsun", "scn2a"): {
        "us.reachPct": {"note": "Ph3 ASO for rare SCN2A-DEE; 18% reach in 30K US patients reflects strong Ph2 data (77% seizure reduction)"},
        "us.priceK": {"note": "Orphan ASO for rare epilepsy ~$250K/yr (nusinersen/Spinraza class pricing for rare CNS ASO)"},
    },
    ("PRAX", "preclin", "rare_epi"): {
        "us.reachPct": {"note": "Preclinical rare genetic epilepsy programs (KCNT1, PCDH19, SYNGAP1); 1% reach in 400K reflects very early stage"},
        "us.priceK": {"note": "Rare genetic epilepsy pricing ~$80K/yr; mix of small molecule and ASO programs"},
    },
    ("CAMX", "commercial", "oud"): {
        "us.reachPct": {"note": "Brixadi ~30% US LAI buprenorphine share (royalties) + Buvidal EU own sales; 25% combined reach of addressable OUD patients"},
        "us.priceK": {"note": "LAI buprenorphine ~$15K/yr US (Sublocade/Brixadi benchmark); specialty addiction medicine pricing"},
    },
    ("CAMX", "oczyesa", "acro"): {
        "us.reachPct": {"note": "Commercial EU + US PDUFA Jun 2026; 25% reach in 15K US acromegaly patients reflects superior SC depot vs Sandostatin LAR IM"},
        "us.priceK": {"note": "Acromegaly SRL pricing ~$100K/yr US (Sandostatin LAR ~$120K, Oczyesa may price ~$100K)"},
    },
    ("CAMX", "sorento", "gepnet"): {
        "us.reachPct": {"note": "Ph3 GEP-NET vs Sandostatin LAR; 18% reach in 11.3K US NET patients reflects rare disease high-need setting"},
        "us.priceK": {"note": "Rare neuroendocrine tumor pricing ~$200K/yr US (lutathera $200K+, SRL $120K); premium for novel SC depot"},
    },
    ("CAMX", "pld", "pld"): {
        "us.reachPct": {"note": "Ph2b positive PLD/ADPKD; 5% reach in 140K reflects no approved therapy but orphan positioning needed"},
        "us.priceK": {"note": "Rare liver/kidney disease ~$60K/yr; octreotide-based pricing but chronic use premium"},
    },
    ("CAMX", "lilly", "incretin"): {
        "us.reachPct": {"note": "Ph1 monthly semaglutide; 0.2% reach in 40M obesity reflects very early stage + Camurus is royalty recipient not developer"},
        "us.priceK": {"note": "GLP-1 obesity class ~$12K/yr net US (Wegovy/Zepbound benchmark)"},
    },
    ("KYMR", "kt621", "stat6"): {
        "us.reachPct": {"note": "Ph2b oral STAT6 degrader for AD/asthma; 4% reach in 1.5M US moderate-severe AD patients (oral dupilumab replacement thesis)"},
        "us.priceK": {"note": "Oral specialty immunology ~$40K/yr; discount to dupilumab ($42K) for oral convenience trade-off"},
    },
    ("KYMR", "kt579", "irf5"): {
        "us.reachPct": {"note": "Ph1 first-in-class IRF5 degrader; 3% reach in 300K US SLE/RA patients reflects very early clinical stage"},
        "us.priceK": {"note": "Specialty autoimmune oral ~$50K/yr (belimumab/anifrolumab class pricing)"},
    },
    ("KYMR", "irak4", "irak4"): {
        "us.reachPct": {"note": "Ph1 IRAK4 degrader (Sanofi partner); 3% reach in 200K US HS/AD patients; Sanofi controls timeline"},
        "us.priceK": {"note": "Specialty oral immunology ~$45K/yr (HS/AD specialist pricing, JAKi class benchmark)"},
    },
    ("KYMR", "cdk2", "onc"): {
        "us.reachPct": {"note": "Preclinical CDK2 molecular glue (Gilead option); 1% reach in 444K US breast cancer reflects very early + Gilead option may not be exercised"},
        "us.priceK": {"note": "Oncology specialty oral ~$150K/yr (CDK4/6 inhibitor class $150-175K benchmark)"},
    },
    ("NKTR", "rezpeg_ad", "ad"): {
        "us.reachPct": {"note": "Ph2b complete, Ph3 starting; 5% reach in 1.5M US AD reflects SC injection Q4-12W dosing; competing with dupilumab but with safety differentiation"},
        "us.priceK": {"note": "SC biologic for AD ~$40K/yr; discount to dupilumab ($42K) reflecting newer entrant positioning"},
    },
    ("NKTR", "rezpeg_aa", "aa"): {
        "us.reachPct": {"note": "Ph2b PoC with signal; 5% reach in 300K US severe AA reflects safety edge vs JAKi but uncertain efficacy magnitude"},
        "us.priceK": {"note": "SC biologic for AA ~$40K/yr; JAKi AA pricing $50K (Olumiant/Litfulo) -- biologic priced similarly"},
    },
    ("NKTR", "rezpeg_t1d", "t1d"): {
        "us.reachPct": {"note": "Ph2 early; 1% reach in 1.6M US T1D reflects speculative disease-modification approach"},
        "us.priceK": {"note": "T1D disease-modifying therapy ~$30K/yr (Tzield $200K one-time = ~$30K amortized; chronic Treg therapy benchmark)"},
    },
    ("NKTR", "nktr255", "onc"): {
        "us.reachPct": {"note": "Ph1/2 IL-15 combo with CAR-T; 8% reach in small 5K US r/r LBCL patients reflects niche combo positioning"},
        "us.priceK": {"note": "Oncology supportive therapy ~$100K/yr; IL-15 agonist priced as add-on to CAR-T regime"},
    },
    ("4568", "commercial", "her2"): {
        "us.reachPct": {"note": "Enhertu #1 ADC globally; 30% reach in 300K US HER2+ patients across breast/gastric/NSCLC/CRC expanding indications"},
        "us.priceK": {"note": "ADC oncology premium pricing ~$200K/yr US (Enhertu WAC ~$13K/28-day cycle = ~$170K/yr)"},
    },
    ("4568", "datroway", "trop2"): {
        "us.reachPct": {"note": "Newly launched TROP2 ADC exceeding forecasts; 18% reach in 40K US NSCLC/TNBC reflects strong early launch signals"},
        "us.priceK": {"note": "TROP2 ADC class pricing ~$180K/yr US (Trodelvy benchmark ~$180K)"},
    },
    ("4568", "her3_dxd", "her3"): {
        "us.reachPct": {"note": "Ph3 first-in-class HER3 ADC with Merck; 12% reach in 15K eligible NSCLC patients reflects novel target + Ph3 stage"},
        "us.priceK": {"note": "Next-gen ADC pricing ~$200K/yr US; premium for first-in-class HER3 target"},
    },
    ("4568", "idxd", "merck_adc"): {
        "us.reachPct": {"note": "Ph1-3 B7-H3 + CDH6 ADCs (Merck); 3% reach reflects mixed early/late pipeline across large tumor populations"},
        "us.priceK": {"note": "ADC oncology premium ~$200K/yr US; Merck $22B deal validates pricing potential"},
    },
    ("4568", "japan_legacy", "japan"): {
        "us.reachPct": {"note": "Mature Japan domestic portfolio declining; 3% US reach reflects minimal ex-Japan presence for legacy drugs"},
        "us.priceK": {"note": "Japan generic/mature pricing ~$5K/yr US equivalent; Lixiana/Tarlige declining"},
    },
    ("6990", "commercial", "trop2"): {
        "us.reachPct": {"note": "Sac-TMT commercial China (4 indications) + Merck global; 12% US reach assumes Merck-led global registration succeeds"},
        "us.priceK": {"note": "TROP2 ADC class ~$180K/yr US; Merck partnership enables US pricing at class standard"},
    },
    ("6990", "a166", "her2_adc"): {
        "us.reachPct": {"note": "A166 commercial China HER2 ADC; 3% US reach reflects Enhertu dominance limiting ex-China opportunity"},
        "us.priceK": {"note": "HER2 ADC pricing ~$180K/yr US; competing with Enhertu's established position"},
    },
    ("6990", "skb315", "cldn"): {
        "us.reachPct": {"note": "Ph2/3 CLDN18.2 ADC; 8% reach in 45K US gastric/pancreatic reflects hot target but competition from Zolbetuximab"},
        "us.priceK": {"note": "Gastric/pancreatic ADC ~$180K/yr US; CLDN18.2 class pricing (Zolbetuximab ~$180K benchmark)"},
    },
    ("6990", "merck_pipe", "merck_adc"): {
        "us.reachPct": {"note": "Ph1-3 Nectin-4 + bsADC (Merck); 2% reach reflects early pipeline across large tumor populations"},
        "us.priceK": {"note": "ADC oncology ~$200K/yr US; Nectin-4 (Padcev $200K benchmark)"},
    },
    ("6990", "platform", "next_gen"): {
        "us.reachPct": {"note": "Preclinical/Ph1 next-gen ADC platform (RDC, iADC, DAC); 0.5% reach reflects discovery stage"},
        "us.priceK": {"note": "Next-gen ADC modalities ~$200K/yr US; novel payloads may command premium"},
    },
    ("RVMD", "darax_pdac", "pdac"): {
        "us.reachPct": {"note": "Ph3 pan-RAS PDAC with unprecedented OS data (HR 0.40); 20% reach in 60K US PDAC reflects ~90% KRAS-driven + strong efficacy"},
        "us.priceK": {"note": "Oncology targeted oral ~$180K/yr US (sotorasib/adagrasib $180-200K benchmark)"},
    },
    ("RVMD", "darax_nsclc", "nsclc"): {
        "us.reachPct": {"note": "Ph3 2L+ NSCLC vs docetaxel; 18% reach in 20K US RAS-mutant NSCLC patients; covers ALL RAS mutations (broader than G12C-only drugs)"},
        "us.priceK": {"note": "RAS inhibitor oral ~$180K/yr US; multi-selective advantage may support premium pricing"},
    },
    ("RVMD", "zoldon", "g12d"): {
        "us.reachPct": {"note": "Ph3 G12D-selective with BTD; 8% reach in 150K US G12D patients (most common KRAS in PDAC); first-in-class G12D"},
        "us.priceK": {"note": "First-in-class targeted oral oncology ~$180K/yr US"},
    },
    ("RVMD", "eliron", "g12c"): {
        "us.reachPct": {"note": "Ph1/2 next-gen G12C; 8% reach in 20K US G12C patients reflects RAS(ON) differentiation from covalent inhibitors"},
        "us.priceK": {"note": "G12C inhibitor class ~$180K/yr US (sotorasib/adagrasib benchmark)"},
    },
    ("RVMD", "pipeline", "other_ras"): {
        "us.reachPct": {"note": "Ph1/preclinical G12V + Q61H + G13C; 3% reach reflects very early stage"},
        "us.priceK": {"note": "Targeted oral oncology ~$180K/yr US"},
    },
    ("NAMS", "obi_mono", "ldl_mono"): {
        "us.reachPct": {"note": "EMA H2 2026 but no US until PREVAIL CVOT; 1.5% reach in 20M US statin-treated patients reflects oral PCSK9-alternative positioning"},
        "us.priceK": {"note": "Mass market oral LDL-lowering ~$6K/yr US; below PCSK9 ($14K) but above statin generic; oral convenience premium"},
    },
    ("NAMS", "obi_fdc", "ldl_fdc"): {
        "us.reachPct": {"note": "FDC (obicetrapib+ezetimibe); 1.2% reach -- single pill vs PCSK9 injection advantage; slightly higher WTP due to convenience"},
        "us.priceK": {"note": "FDC oral LDL ~$7K/yr US; modest premium over monotherapy for combination convenience"},
    },
    ("NAMS", "prevail", "cvot"): {
        "us.reachPct": {"note": "PREVAIL CVOT Ph3 ongoing; 1.0% reach in 15M high-risk CV patients -- US access entirely depends on this trial"},
        "us.priceK": {"note": "CV outcomes-proven oral ~$8K/yr US; premium over LDL-only label if CVOT positive"},
    },
    ("NAMS", "alzheimer", "alz"): {
        "us.reachPct": {"note": "Ph2 Alzheimer biomarker data; 0.3% reach in 6M US AD patients reflects speculative phase"},
        "us.priceK": {"note": "Oral Alzheimer prevention ~$8K/yr; mass market pricing if validated"},
    },
    ("NAMS", "rubens", "t2d"): {
        "us.reachPct": {"note": "Ph3 RUBENS T2D enrolling; 0.5% reach in 25M US T2D reflects add-on to existing therapy positioning"},
        "us.priceK": {"note": "Oral T2D add-on therapy ~$6K/yr (SGLT2/DPP4 class pricing)"},
    },
    ("GLMD", "aramchol_onco", "crc"): {
        "us.reachPct": {"note": "Ph1b combo with regorafenib; 1% reach in 150K US mCRC reflects no human data, unvalidated mechanism"},
        "us.priceK": {"note": "If validated, Aramchol combo would be oral add-on to Stivarga ~$30K/yr; combo pricing caps at low specialty range"},
    },
    ("GLMD", "aramchol_hcc", "hcc"): {
        "us.reachPct": {"note": "Ph1b basket HCC arm; 1.5% reach in 35K US HCC reflects liver biology thesis but unproven"},
        "us.priceK": {"note": "HCC oral add-on therapy ~$30K/yr; Stivarga backbone limits pricing upside"},
    },
    ("GLMD", "aramchol_chol", "chol"): {
        "us.reachPct": {"note": "Ph1b basket cholangiocarcinoma; 2% reach in 12K US CCA reflects rare biliary + orphan potential"},
        "us.priceK": {"note": "Rare biliary oral add-on ~$30K/yr"},
    },
    ("GLMD", "aramchol_pd", "pd"): {
        "us.reachPct": {"note": "Preclinical brain-penetrant LNP for PD; 0.5% reach in 1M US PD reflects no human data + LNP BBB crossing unproven"},
        "us.priceK": {"note": "Disease-modifying PD therapy ~$25K/yr; mass CNS pricing if validated"},
    },
    ("GLMD", "aramchol_nash_legacy", "mash"): {
        "us.reachPct": {"note": "ARMOR NASH essentially dormant; 0.3% reach reflects combo-only strategy vs approved Rezdiffra"},
        "us.priceK": {"note": "NASH oral add-on ~$20K/yr; Rezdiffra ~$48K but Aramchol would be combo partner at lower price"},
    },
    ("NTLA", "lonvoz", "hae"): {
        "us.reachPct": {"note": "Ph3 HAELO BLA H2 2026; 30% reach in 7K US treated HAE patients (96% attack reduction, attack-free at 50mg)"},
        "us.priceK": {"note": "One-time CRISPR cure priced ~$2-3M; amortized ~$500K/yr; replaces chronic $400-600K/yr prophylaxis"},
    },
    ("NTLA", "nexz_cm", "attr_cm"): {
        "us.reachPct": {"note": "Ph3 in vivo gene edit ATTR-CM; 5% reach in 120K US ATTR-CM patients (one-time vs chronic tafamidis)"},
        "us.priceK": {"note": "One-time gene edit for ATTR ~$500K amortized; vs tafamidis $200K/yr chronic cost"},
    },
    ("NTLA", "nexz_pn", "attr_pn"): {
        "us.reachPct": {"note": "Ph3 ATTR-PN; 15% reach in 10K US ATTR-PN patients (smaller population, higher penetration)"},
        "us.priceK": {"note": "One-time gene edit ~$500K amortized; ATTR-PN more homogeneous patient population"},
    },
    ("CELC", "geda_wt", "bc_wt"): {
        "us.reachPct": {"note": "NDA Priority Review PDUFA Jul 2026; 15% reach in PIK3CA-WT 2L+ HR+/HER2- BC; best PFS ever (HR=0.24)"},
        "us.priceK": {"note": "IV oncology specialty ~$150K/yr; PI3K/mTOR class pricing (alpelisib ~$150K benchmark)"},
    },
    ("CELC", "geda_mt", "bc_mt"): {
        "us.reachPct": {"note": "PIK3CA-mutant expansion; 10% reach -- competes with inavolisib (Roche) in mutant subgroup"},
        "us.priceK": {"note": "IV oncology specialty ~$150K/yr; same class pricing as WT indication"},
    },
    ("CELC", "geda_1l", "bc_1l"): {
        "us.reachPct": {"note": "1L expansion potential; 5% reach reflects competitive CDK4/6i-dominated front-line landscape"},
        "us.priceK": {"note": "1L breast cancer oncology ~$150K/yr"},
    },
    ("CELC", "geda_prost", "prost"): {
        "us.reachPct": {"note": "Early prostate cancer exploration; 2% reach reflects preclinical/early stage"},
        "us.priceK": {"note": "Oncology specialty ~$150K/yr"},
    },
    ("CRVO", "nef_dlb", "dlb"): {
        "us.reachPct": {"note": "Ph3 ready p38a inhibitor for DLB; 3% reach in 1.4M US DLB reflects oral drug with Ph2b signal but missed primary + financing-dependent"},
        "us.priceK": {"note": "CNS specialty oral ~$25K/yr (neurodegeneration pricing; lecanemab $26K benchmark)"},
    },
    ("CRVO", "nef_stroke", "stroke"): {
        "us.reachPct": {"note": "Early stroke indication; 0.5% reach in 800K US stroke patients reflects preclinical rationale only"},
        "us.priceK": {"note": "CNS neuroprotection ~$20K/yr"},
    },
    ("CRVO", "nef_als", "als"): {
        "us.reachPct": {"note": "ALS exploration; 5% reach in 30K US ALS patients reflects high unmet need + p38a rationale"},
        "us.priceK": {"note": "Rare neurodegenerative ~$100K/yr (Relyvrio $158K, Radicava $150K benchmark)"},
    },
    ("CRVO", "nef_ppa", "ppa"): {
        "us.reachPct": {"note": "Ultra-rare PPA; 5% reach in 30K US patients reflects niche positioning"},
        "us.priceK": {"note": "CNS specialty oral ~$30K/yr"},
    },
    ("CRVS", "soq_ptcl", "ptcl"): {
        "us.reachPct": {"note": "Ph3 registrational PTCL; 25% reach in tiny 3K US R/R PTCL reflects orphan + no approved agents + first-in-class ITK"},
        "us.priceK": {"note": "Rare heme-onc oral ~$200K/yr (romidepsin/belinostat class; orphan premium)"},
    },
    ("CRVS", "soq_ad", "ad"): {
        "us.reachPct": {"note": "Ph2 AD starting; 3% reach in 1.5M US AD reflects early stage oral ITK; novel mechanism"},
        "us.priceK": {"note": "Oral specialty immunology ~$40K/yr (JAKi/oral biologic alternative class)"},
    },
    ("CRVS", "soq_asthma", "severe_asthma"): {
        "us.reachPct": {"note": "Early asthma; 1% reach reflects speculative extension of ITK mechanism"},
        "us.priceK": {"note": "Oral severe asthma ~$40K/yr (dupilumab asthma ~$37K benchmark)"},
    },
    ("CRVS", "soq_hs", "hs"): {
        "us.reachPct": {"note": "Ph2 HS; 5% reach in 200K US HS patients reflects high unmet need + ITK rationale"},
        "us.priceK": {"note": "HS specialty oral ~$45K/yr (Humira HS ~$70K, oral at discount)"},
    },
    ("JANX", "janx007", "mcrpc"): {
        "us.reachPct": {"note": "Ph1a/b PSMA TRACTr; 3% reach in large 1.3M prostate reflects early stage but 109 pts treated + strong PSA responses"},
        "us.priceK": {"note": "Bispecific T-cell engager oncology ~$200K/yr (teclistamab/Lunsumio class pricing)"},
    },
    ("JANX", "janx008", "egfr_solid"): {
        "us.reachPct": {"note": "Ph1 EGFR TRACTr; 3% reach in 150K US EGFR+ solid tumors reflects very early but novel mechanism"},
        "us.priceK": {"note": "Bispecific oncology ~$180K/yr US"},
    },
    ("JANX", "janx011", "autoimmune"): {
        "us.reachPct": {"note": "Ph1 CD19 TRACTr for autoimmune; 2% reach in 300K US SLE/autoimmune; off-the-shelf alternative to CAR-T"},
        "us.priceK": {"note": "Off-the-shelf T-cell engager for autoimmune ~$300K (less than CAR-T $400K, more than mAb $40K)"},
    },
    ("JANX", "psma_tracir", "tracir"): {
        "us.reachPct": {"note": "Preclinical PSMA-TRACIr radioconjugate; 1% reach reflects very early discovery stage"},
        "us.priceK": {"note": "Radioconjugate oncology ~$200K/yr (Pluvicto $200K benchmark)"},
    },
    ("JANX", "merck_bms", "partnerships"): {
        "us.reachPct": {"note": "Merck + BMS partnered programs; 0.5% reach reflects undisclosed targets, royalty/milestone model"},
        "us.priceK": {"note": "Partnered oncology bispecifics ~$200K/yr US"},
    },
    ("ALLO", "cema_cel", "lbcl_1l"): {
        "us.reachPct": {"note": "Ph2 pivotal cema-cel 1L LBCL MRD+ consolidation; 5% reach in 277K patients (MRD+ subset = ~14K addressable)"},
        "us.priceK": {"note": "Allogeneic CAR-T one-time ~$400K (autologous Yescarta/Breyanzi $400K; allo may be at parity for off-the-shelf advantage)"},
    },
    ("ALLO", "allo329", "sle_basket"): {
        "us.reachPct": {"note": "Ph1 allogeneic CAR-T for SLE; 2% reach in 300K US SLE reflects very early off-the-shelf autoimmune CAR-T"},
        "us.priceK": {"note": "Allogeneic CAR-T autoimmune ~$300K one-time (discount to oncology CAR-T for broader autoimmune use)"},
    },
    ("ALLO", "allo316", "ccrcc"): {
        "us.reachPct": {"note": "Anti-CD70 allogeneic CAR-T for RCC; 2% reach reflects deprioritized program + competitive landscape"},
        "us.priceK": {"note": "Allogeneic CAR-T oncology ~$400K one-time (solid tumor CAR-T if validated)"},
    },
    ("BCYC", "zelenectide", "muc"): {
        "us.reachPct": {"note": "Ph2/3 mUC but approval path rejected by FDA; 3% reach reflects pivot to breast/NSCLC with NECTIN4-amp biomarker"},
        "us.priceK": {"note": "BDC (bicycle drug conjugate) oncology ~$180K/yr US; novel modality but ADC-competitive pricing"},
    },
    ("BCYC", "nuzefatide", "epha2"): {
        "us.reachPct": {"note": "Ph1/2 EphA2-targeted BDC; 4% reach in 60K EphA2+ patients reflects dose-finding stage"},
        "us.priceK": {"note": "BDC oncology ~$180K/yr US"},
    },
    ("BCYC", "brc", "radio"): {
        "us.reachPct": {"note": "Preclinical bicycle radio conjugate; 1% reach reflects discovery stage"},
        "us.priceK": {"note": "Radioconjugate oncology ~$200K/yr (Pluvicto benchmark)"},
    },
    ("BCYC", "bt7480", "tica"): {
        "us.reachPct": {"note": "Ph1 TICA immune agonist; 1.5% reach reflects first-in-human dose escalation"},
        "us.priceK": {"note": "Immuno-oncology agonist ~$180K/yr US"},
    },
    ("BCYC", "platform", "disc"): {
        "us.reachPct": {"note": "Discovery/platform programs; 0.5% reach reflects preclinical optionality"},
        "us.priceK": {"note": "Oncology specialty ~$180K/yr US"},
    },
    ("OCS", "privo_on", "on"): {
        "us.reachPct": {"note": "Registrational privosegtor for ON; BTD+orphan; 25% reach in 11.3K US ON patients (no approved therapies)"},
        "us.priceK": {"note": "Rare ophthalmology neuroprotection ~$200K/yr (orphan pricing for first-in-class)"},
    },
    ("OCS", "privo_naion", "naion"): {
        "us.reachPct": {"note": "Registrational NAION; 20% reach in 15.1K US NAION patients (no approved therapies)"},
        "us.priceK": {"note": "Rare ophthalmology ~$200K/yr (orphan neuroprotection pricing)"},
    },
    ("OCS", "ocs01", "dme"): {
        "us.reachPct": {"note": "Ph3 topical DME; 3% reach in 750K US DME patients (topical eye drop vs anti-VEGF injections -- convenience advantage)"},
        "us.priceK": {"note": "Topical ophthalmology ~$15K/yr (eye drop pricing; significant discount to anti-VEGF injections $20-40K)"},
    },
    ("OCS", "licam", "ded"): {
        "us.reachPct": {"note": "Ph2 anti-TNF for dry eye; 2% reach in 666K US DED patients reflects early clinical stage"},
        "us.priceK": {"note": "Dry eye specialty ~$12K/yr (Restasis/Xiidra class pricing)"},
    },
    ("VLA", "vla15", "lyme"): {
        "us.reachPct": {"note": "Pfizer Lyme vaccine royalty; 5% reach in 20M US at-risk (initial launch year)"},
        "us.priceK": {"note": "Lyme vaccine ~$0.20K per dose (3-dose primary series ~$150-200 per patient; at-risk population pricing)"},
    },
    ("VLA", "ixchiq", "chik"): {
        "us.reachPct": {"note": "IXCHIQ commercial chikungunya; 8% reach in 200K US travelers to endemic areas"},
        "us.priceK": {"note": "Travel vaccine ~$0.28K/dose US ($275 per dose; single-dose live-attenuated)"},
    },
    ("VLA", "s4v2", "shig"): {
        "us.reachPct": {"note": "Ph2 Shigella vaccine; 2% reach in 1M US travelers/military reflects early development stage"},
        "us.priceK": {"note": "Travel vaccine ~$0.20K/dose"},
    },
    ("VLA", "zika", "zika"): {
        "us.reachPct": {"note": "Ph1 Zika vaccine; 1% reach reflects early stage + uncertain Zika outbreak dynamics"},
        "us.priceK": {"note": "Travel/pandemic vaccine ~$0.15K/dose"},
    },
    ("VLA", "commercial", "travel"): {
        "us.reachPct": {"note": "IXIARO+DUKORAL established travel vaccines; 10% reach in travel medicine market segment"},
        "us.priceK": {"note": "Travel vaccine pricing ~$0.20K/dose average (IXIARO Japanese encephalitis + DUKORAL cholera)"},
    },
    ("BOLD", "bbi940_er", "er_her2_neg_amp"): {
        "us.reachPct": {"note": "Ph1 kinesin degrader for ER+/HER2- with oncogene amplification (20-30% of mBC); 1% reach in 555K reflects IND-stage"},
        "us.priceK": {"note": "Oral oncology specialty ~$150K/yr (CDK4/6i resistance setting pricing)"},
    },
    ("BOLD", "bbi940_tnbc", "tnbc_lar_amp"): {
        "us.reachPct": {"note": "Ph1 TNBC LAR subtype with oncogene amp; 3% reach in 50K reflects higher need in TNBC but still Ph1"},
        "us.priceK": {"note": "TNBC oral specialty ~$150K/yr"},
    },
    ("ARQT", "commercial", "derm"): {
        "us.reachPct": {"note": "ZORYVE $376M 2025 commercial; topical PDE4 franchise across pso+AD+sebderm; 8% reach reflects established growing commercial franchise"},
        "us.priceK": {"note": "Topical dermatology ~$18K/yr US (ZORYVE net pricing ~$18K/yr per treated patient)"},
    },
    ("ARQT", "zoryve_exp", "derm_exp"): {
        "us.reachPct": {"note": "Infant AD + new formulation expansions; 3% reach in 8M broader population reflects label-broadening potential"},
        "us.priceK": {"note": "Topical derm ~$8K/yr (pediatric/infant lower dosing and pricing)"},
    },
    ("ARQT", "arq234", "ad_bio"): {
        "us.reachPct": {"note": "Ph2 AD biologic; 3% reach in 1.5M US moderate-severe AD reflects dupilumab-crowded market + Ph2 stage"},
        "us.priceK": {"note": "SC biologic for AD ~$45K/yr (dupilumab $42K benchmark)"},
    },
    ("ARQT", "arq255", "aa_top"): {
        "us.reachPct": {"note": "Topical alopecia early; 4% reach in 300K US severe AA reflects unmet need for topical option vs oral JAKi"},
        "us.priceK": {"note": "Topical alopecia ~$15K/yr (premium topical pricing)"},
    },
    ("ARQT", "arq252", "hand_vit"): {
        "us.reachPct": {"note": "Hand eczema + vitiligo topical; 2% reach in 1.5M US patients (Opzelura $35K competitor but Arcutis in non-steroidal niche)"},
        "us.priceK": {"note": "Topical derm ~$12K/yr (non-steroidal topical specialty pricing)"},
    },
}


# ===================================================================
# Main logic
# ===================================================================
def main():
    total_added = 0
    total_issues = 0

    for ticker in TICKERS:
        path = ROOT / "configs" / f"{ticker}.json"
        d = json.loads(path.read_text(encoding="utf-8"))

        added = 0
        for a in d["assets"]:
            for ind in a["indications"]:
                key = (ticker, a["id"], ind["id"])
                if key in SLICES and "company_slice" not in ind["market"]:
                    ind["market"]["company_slice"] = SLICES[key]
                    added += 1
                if key in SOURCES and "company_slice_sources" not in ind["market"]:
                    ind["market"]["company_slice_sources"] = SOURCES[key]

        # Validate SOM >= salesM
        issues = []
        for a in d["assets"]:
            for ind in a["indications"]:
                m = ind["market"]
                cs = m.get("company_slice", {})
                r = m.get("regions", {})
                salesM = m.get("salesM", 0)
                if not cs or not r:
                    continue
                som = sum(
                    r.get(rk, {}).get("patientsK", 0)
                    * (cs.get(rk, {}).get("reachPct", 0) / 100)
                    * (cs.get(rk, {}).get("wtpPct", 0) / 100)
                    * cs.get(rk, {}).get("priceK", 0)
                    for rk in ["us", "eu", "row"]
                )
                flag = "OK" if som >= salesM or salesM == 0 else "SALES > SOM"
                print(
                    f"{ticker:6s} {a['id']:20s} {ind['id']:20s} "
                    f"sales=${salesM:>8.0f}M  SOM=${som:>10.0f}M  [{flag}]"
                )
                if salesM > 0 and som < salesM:
                    issues.append((ticker, a["id"], ind["id"], salesM, som))

        path.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
        total_added += added
        total_issues += len(issues)

        if issues:
            for t, aid, iid, s, som in issues:
                print(f"  !! {t}.{aid}.{iid}: sales=${s}M > SOM=${som:.0f}M")

    print(f"\n{'='*60}")
    print(f"Total: {total_added} company_slice entries added across {len(TICKERS)} companies")
    if total_issues:
        print(f"{total_issues} SALES > SOM issues to review")
    else:
        print("All SOM >= sales -- clean!")


if __name__ == "__main__":
    main()
