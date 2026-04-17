# -*- coding: utf-8 -*-
"""
Finish adding company_slice to the remaining indications that batches 1-3 missed.
These are primarily commercial assets with id='commercial' and a few pipeline items.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIGS = ROOT / "configs"

# (ticker, asset_id, ind_id): {"us": {r, w, p}, "eu": {...}, "row": {...}, "notes": {us_reach, us_price}}
SLICES = {
    # ABVX - Obefazimod Phase 3 UC, Phase 2b Crohn's
    ("ABVX", "obef_uc", "uc"): {
        "us":  {"reachPct": 10, "wtpPct": 45, "priceK": 45},
        "eu":  {"reachPct": 7,  "wtpPct": 32, "priceK": 25},
        "row": {"reachPct": 2,  "wtpPct": 10, "priceK": 10},
        "us_reach_note": "Phase 3 positive; oral miR-124 enhancer, differentiated MoA vs JAKi/biologics in mod-severe UC",
        "us_price_note": "Oral specialty pricing ~$45K/yr, below biologics"
    },
    ("ABVX", "obef_cd", "cd"): {
        "us":  {"reachPct": 5, "wtpPct": 30, "priceK": 45},
        "eu":  {"reachPct": 3, "wtpPct": 22, "priceK": 25},
        "row": {"reachPct": 1, "wtpPct": 8,  "priceK": 10},
        "us_reach_note": "Phase 2b ENHANCE-CD; Crohn's is second indication for obefazimod",
        "us_price_note": "Oral specialty pricing ~$45K/yr"
    },
    # ALNY
    ("ALNY", "commercial", "ttr"): {
        "us":  {"reachPct": 30, "wtpPct": 70, "priceK": 475},
        "eu":  {"reachPct": 22, "wtpPct": 55, "priceK": 300},
        "row": {"reachPct": 8,  "wtpPct": 18, "priceK": 120},
        "us_reach_note": "Amvuttra+Onpattro: ATTR-CM market expanding with Amvuttra CM label (2025); diagnosed population growing ~20%/yr",
        "us_price_note": "Amvuttra ~$475K/yr (~$460K WAC); Onpattro ~$450K/yr"
    },
    ("ALNY", "nucresiran", "ttr_next"): {
        "us":  {"reachPct": 15, "wtpPct": 50, "priceK": 450},
        "eu":  {"reachPct": 10, "wtpPct": 38, "priceK": 280},
        "row": {"reachPct": 3,  "wtpPct": 12, "priceK": 110},
        "us_reach_note": "Phase 3 next-gen quarterly dosing; if approved, expected to take share from Amvuttra/Attruby",
        "us_price_note": "Premium rare pricing ~$450K/yr"
    },
    ("ALNY", "zilebesiran", "htn"): {
        "us":  {"reachPct": 1.2, "wtpPct": 30, "priceK": 8},
        "eu":  {"reachPct": 0.8, "wtpPct": 22, "priceK": 4},
        "row": {"reachPct": 0.3, "wtpPct": 8,  "priceK": 2},
        "us_reach_note": "Phase 3 CVOT; twice-yearly injectable for resistant HTN; niche within mass HTN market",
        "us_price_note": "RNAi in mass market; estimated $8K/yr premium vs generics"
    },
    ("ALNY", "mivelsiran", "alz_rna"): {
        "us":  {"reachPct": 3, "wtpPct": 20, "priceK": 60},
        "eu":  {"reachPct": 2, "wtpPct": 15, "priceK": 35},
        "row": {"reachPct": 0.5, "wtpPct": 6, "priceK": 15},
        "us_reach_note": "Phase 1/2 cerebral amyloid angiopathy; ultra-early, small eligible population",
        "us_price_note": "Rare CNS RNAi estimated ~$60K/yr"
    },
    ("ALNY", "givlaari", "ahp"): {
        "us":  {"reachPct": 25, "wtpPct": 72, "priceK": 500},
        "eu":  {"reachPct": 18, "wtpPct": 55, "priceK": 320},
        "row": {"reachPct": 5,  "wtpPct": 15, "priceK": 120},
        "us_reach_note": "Acute hepatic porphyria ultra-rare; diagnosed pts mostly on treatment",
        "us_price_note": "Givlaari ~$490K/yr WAC"
    },
    ("ALNY", "oxlumo", "ph1"): {
        "us":  {"reachPct": 40, "wtpPct": 75, "priceK": 550},
        "eu":  {"reachPct": 28, "wtpPct": 58, "priceK": 350},
        "row": {"reachPct": 8,  "wtpPct": 15, "priceK": 130},
        "us_reach_note": "Primary hyperoxaluria type 1 ultra-rare; saturating diagnosed population",
        "us_price_note": "Oxlumo ~$525K/yr"
    },
    # ARGX - Vyvgart FcRn franchise
    ("ARGX", "commercial", "fcrn_comm"): {
        "us":  {"reachPct": 35, "wtpPct": 70, "priceK": 380},
        "eu":  {"reachPct": 25, "wtpPct": 55, "priceK": 250},
        "row": {"reachPct": 8,  "wtpPct": 15, "priceK": 100},
        "us_reach_note": "Vyvgart gMG + CIDP: rapid launch, best-in-class FcRn, expanding into ITP/MMN",
        "us_price_note": "Vyvgart ~$375K/yr"
    },
    ("ARGX", "itp_expand", "itp"): {
        "us":  {"reachPct": 12, "wtpPct": 40, "priceK": 350},
        "eu":  {"reachPct": 8,  "wtpPct": 30, "priceK": 220},
        "row": {"reachPct": 2,  "wtpPct": 10, "priceK": 90},
        "us_reach_note": "Phase 3 ITP expansion H2 2026; second-line eligible subset",
        "us_price_note": "FcRn class pricing ~$350K/yr"
    },
    ("ARGX", "empas", "complement"): {
        "us":  {"reachPct": 18, "wtpPct": 45, "priceK": 300},
        "eu":  {"reachPct": 12, "wtpPct": 35, "priceK": 190},
        "row": {"reachPct": 3,  "wtpPct": 10, "priceK": 80},
        "us_reach_note": "Phase 3 MMN + CIDP; anti-C2 complement",
        "us_price_note": "Biologic rare disease ~$300K/yr"
    },
    ("ARGX", "argx119", "musk"): {
        "us":  {"reachPct": 45, "wtpPct": 55, "priceK": 400},
        "eu":  {"reachPct": 30, "wtpPct": 42, "priceK": 260},
        "row": {"reachPct": 8,  "wtpPct": 12, "priceK": 100},
        "us_reach_note": "CMS ultra-rare; first-in-class MuSK agonist Phase 3 entering Q3 2026",
        "us_price_note": "Ultra-rare chronic ~$400K/yr"
    },
    ("ARGX", "pipeline", "ai_pipe"): {
        "us":  {"reachPct": 3, "wtpPct": 20, "priceK": 300},
        "eu":  {"reachPct": 2, "wtpPct": 15, "priceK": 190},
        "row": {"reachPct": 0.5, "wtpPct": 6, "priceK": 80},
        "us_reach_note": "Broader autoimmune pipeline Phase 1-3; 15 indications, cross-portfolio",
        "us_price_note": "Specialty biologic ~$300K/yr blended"
    },
    # ARWR
    ("ARWR", "commercial", "fcs"): {
        "us":  {"reachPct": 25, "wtpPct": 55, "priceK": 400},
        "eu":  {"reachPct": 15, "wtpPct": 40, "priceK": 250},
        "row": {"reachPct": 4,  "wtpPct": 12, "priceK": 100},
        "us_reach_note": "REDEMPLO plozasiran FCS; ultra-rare diagnosed ~3K US, capture expanding",
        "us_price_note": "Plozasiran FCS ~$400K/yr (orphan pricing)"
    },
    ("ARWR", "zodasiran", "lipid"): {
        "us":  {"reachPct": 2, "wtpPct": 30, "priceK": 10},
        "eu":  {"reachPct": 1.2, "wtpPct": 22, "priceK": 6},
        "row": {"reachPct": 0.3, "wtpPct": 8, "priceK": 3},
        "us_reach_note": "Phase 3 mixed hyperlipidemia ANGPTL3; competes with pelacarsen/olpasiran class",
        "us_price_note": "RNAi lipids ~$10K/yr premium vs statins"
    },
    ("ARWR", "aro_dimer", "ascvd"): {
        "us":  {"reachPct": 1.5, "wtpPct": 25, "priceK": 12},
        "eu":  {"reachPct": 1,   "wtpPct": 18, "priceK": 7},
        "row": {"reachPct": 0.3, "wtpPct": 6,  "priceK": 3},
        "us_reach_note": "Phase 1/2 PCSK9+APOC3 dual-target RNAi; broad ASCVD but unproven",
        "us_price_note": "RNAi lipid class ~$12K/yr"
    },
    ("ARWR", "obesity", "obesity"): {
        "us":  {"reachPct": 1, "wtpPct": 20, "priceK": 15},
        "eu":  {"reachPct": 0.6, "wtpPct": 15, "priceK": 9},
        "row": {"reachPct": 0.2, "wtpPct": 5, "priceK": 4},
        "us_reach_note": "Phase 1/2a INHBE+ALK7 RNAi; early vs dominant GLP-1 class",
        "us_price_note": "RNAi chronic dosing ~$15K/yr"
    },
    ("ARWR", "aro_mapt", "cns"): {
        "us":  {"reachPct": 2, "wtpPct": 18, "priceK": 35},
        "eu":  {"reachPct": 1.3, "wtpPct": 13, "priceK": 20},
        "row": {"reachPct": 0.3, "wtpPct": 5, "priceK": 8},
        "us_reach_note": "Phase 1 TRiM platform tauopathies; ultra-early, large AD population",
        "us_price_note": "CNS RNAi estimated ~$35K/yr"
    },
    # AXSM
    ("AXSM", "auvelity", "mdd"): {
        "us":  {"reachPct": 2.5, "wtpPct": 55, "priceK": 15},
        "eu":  {"reachPct": 1.5, "wtpPct": 38, "priceK": 8},
        "row": {"reachPct": 0.3, "wtpPct": 10, "priceK": 4},
        "us_reach_note": "Auvelity MDD growing; rapid-onset oral, differentiated vs SSRIs",
        "us_price_note": "Auvelity ~$15K/yr"
    },
    ("AXSM", "sunosi", "eds"): {
        "us":  {"reachPct": 12, "wtpPct": 55, "priceK": 90},
        "eu":  {"reachPct": 8,  "wtpPct": 38, "priceK": 55},
        "row": {"reachPct": 2,  "wtpPct": 10, "priceK": 20},
        "us_reach_note": "Sunosi EDS in narcolepsy+OSA; specialty niche",
        "us_price_note": "Sunosi ~$90K/yr"
    },
    ("AXSM", "symbravo", "gad"): {
        "us":  {"reachPct": 1, "wtpPct": 30, "priceK": 12},
        "eu":  {"reachPct": 0.6, "wtpPct": 22, "priceK": 6},
        "row": {"reachPct": 0.1, "wtpPct": 6, "priceK": 3},
        "us_reach_note": "Symbravo GAD launched 2025; early ramp vs generic SSRI/SNRI",
        "us_price_note": "Symbravo ~$12K/yr"
    },
    ("AXSM", "axs05_ad", "ad_agit"): {
        "us":  {"reachPct": 10, "wtpPct": 45, "priceK": 32},
        "eu":  {"reachPct": 6,  "wtpPct": 32, "priceK": 18},
        "row": {"reachPct": 1,  "wtpPct": 8,  "priceK": 8},
        "us_reach_note": "sNDA PDUFA Apr 30 2026; AD agitation first therapy if approved",
        "us_price_note": "Specialty CNS ~$32K/yr for AD indication"
    },
    ("AXSM", "axs14", "fibro"): {
        "us":  {"reachPct": 2, "wtpPct": 38, "priceK": 12},
        "eu":  {"reachPct": 1.2, "wtpPct": 28, "priceK": 7},
        "row": {"reachPct": 0.3, "wtpPct": 8,  "priceK": 3},
        "us_reach_note": "AXS-14 fibromyalgia NDA submitted; niche vs generic pregabalin",
        "us_price_note": "Specialty oral ~$12K/yr"
    },
    ("AXSM", "solri_adhd", "sol_expan"): {
        "us":  {"reachPct": 2, "wtpPct": 35, "priceK": 14},
        "eu":  {"reachPct": 1.2, "wtpPct": 25, "priceK": 8},
        "row": {"reachPct": 0.2, "wtpPct": 6, "priceK": 4},
        "us_reach_note": "Solriamfetol ADHD+MDD-EDS+BED Phase 3 expansions",
        "us_price_note": "Oral specialty ~$14K/yr"
    },
    ("AXSM", "axs12", "narco"): {
        "us":  {"reachPct": 15, "wtpPct": 50, "priceK": 85},
        "eu":  {"reachPct": 10, "wtpPct": 38, "priceK": 50},
        "row": {"reachPct": 2,  "wtpPct": 10, "priceK": 20},
        "us_reach_note": "AXS-12 narcolepsy NDA track post-ENCORE; specialty orphan-like",
        "us_price_note": "Narcolepsy specialty ~$85K/yr"
    },
    # BBIO
    ("BBIO", "commercial", "attr_cm"): {
        "us":  {"reachPct": 15, "wtpPct": 55, "priceK": 260},
        "eu":  {"reachPct": 10, "wtpPct": 40, "priceK": 160},
        "row": {"reachPct": 3,  "wtpPct": 12, "priceK": 65},
        "us_reach_note": "Attruby acoramidis launched Nov 2024; competing with tafamidis for ATTR-CM",
        "us_price_note": "Attruby ~$258K/yr list"
    },
    ("BBIO", "bbp418", "lgmd"): {
        "us":  {"reachPct": 50, "wtpPct": 55, "priceK": 400},
        "eu":  {"reachPct": 35, "wtpPct": 42, "priceK": 250},
        "row": {"reachPct": 8,  "wtpPct": 12, "priceK": 100},
        "us_reach_note": "BBP-418 LGMD2I/R9 NDA planned H1 2026 post-FORTIFY; ultra-rare, first therapy",
        "us_price_note": "Ultra-rare NMD ~$400K/yr"
    },
    ("BBIO", "infig", "achon"): {
        "us":  {"reachPct": 30, "wtpPct": 50, "priceK": 320},
        "eu":  {"reachPct": 20, "wtpPct": 38, "priceK": 200},
        "row": {"reachPct": 5,  "wtpPct": 10, "priceK": 80},
        "us_reach_note": "Infigratinib achondroplasia Phase 3 positive (low-dose); competes with vosoritide",
        "us_price_note": "Pediatric rare ~$320K/yr"
    },
    ("BBIO", "encal", "adh1"): {
        "us":  {"reachPct": 55, "wtpPct": 60, "priceK": 350},
        "eu":  {"reachPct": 40, "wtpPct": 45, "priceK": 220},
        "row": {"reachPct": 10, "wtpPct": 15, "priceK": 90},
        "us_reach_note": "Encaleret ADH1 Phase 3 positive; first therapy for ultra-rare ADH1",
        "us_price_note": "Ultra-rare first-in-class ~$350K/yr"
    },
    ("BBIO", "depleter", "attr_next"): {
        "us":  {"reachPct": 5, "wtpPct": 20, "priceK": 250},
        "eu":  {"reachPct": 3, "wtpPct": 15, "priceK": 160},
        "row": {"reachPct": 0.5, "wtpPct": 5, "priceK": 60},
        "us_reach_note": "TTR amyloid depleter antibody preclinical; clinic 2027-2028",
        "us_price_note": "ATTR pricing analog ~$250K/yr"
    },
    # DFTX
    ("DFTX", "dt120", "gad"): {
        "us":  {"reachPct": 3, "wtpPct": 35, "priceK": 15},
        "eu":  {"reachPct": 2, "wtpPct": 25, "priceK": 8},
        "row": {"reachPct": 0.3, "wtpPct": 6, "priceK": 3},
        "us_reach_note": "DT120 lysergide GAD Phase 3; single-dose psychedelic, REMS complexity caps reach",
        "us_price_note": "Single-dose psychedelic ~$15K per treatment"
    },
    ("DFTX", "dt120", "mdd"): {
        "us":  {"reachPct": 2, "wtpPct": 30, "priceK": 18},
        "eu":  {"reachPct": 1.2, "wtpPct": 22, "priceK": 10},
        "row": {"reachPct": 0.2, "wtpPct": 5, "priceK": 4},
        "us_reach_note": "DT120 MDD Phase 3 EMERGE; competes with SSRIs + esketamine",
        "us_price_note": "Single-dose psychedelic ~$18K per treatment"
    },
    ("DFTX", "dt402", "asd"): {
        "us":  {"reachPct": 1, "wtpPct": 20, "priceK": 20},
        "eu":  {"reachPct": 0.6, "wtpPct": 15, "priceK": 12},
        "row": {"reachPct": 0.1, "wtpPct": 5, "priceK": 5},
        "us_reach_note": "DT402 R-MDMA ASD Phase 2a; early-stage, limited REMS pathway",
        "us_price_note": "Psychedelic-assisted ~$20K per treatment"
    },
    # GILD
    ("GILD", "len_prev", "hiv_prev"): {
        "us":  {"reachPct": 8, "wtpPct": 55, "priceK": 28},
        "eu":  {"reachPct": 4, "wtpPct": 30, "priceK": 18},
        "row": {"reachPct": 1, "wtpPct": 8,  "priceK": 6},
        "us_reach_note": "Yeztugo lenacapavir PrEP twice-yearly; game-changer but early ramp",
        "us_price_note": "Lenacapavir PrEP ~$28K/yr"
    },
    ("GILD", "trodelvy", "onc_bc"): {
        "us":  {"reachPct": 22, "wtpPct": 55, "priceK": 220},
        "eu":  {"reachPct": 14, "wtpPct": 40, "priceK": 130},
        "row": {"reachPct": 3,  "wtpPct": 10, "priceK": 55},
        "us_reach_note": "Trodelvy 1L mTNBC sNDA (ASCENT-04 positive); PDUFA H2 2026",
        "us_price_note": "Trodelvy ~$220K/yr"
    },
    ("GILD", "anito_cel", "mm_cart"): {
        "us":  {"reachPct": 8, "wtpPct": 45, "priceK": 465},
        "eu":  {"reachPct": 5, "wtpPct": 28, "priceK": 350},
        "row": {"reachPct": 1, "wtpPct": 8,  "priceK": 180},
        "us_reach_note": "Anito-cel BCMA CAR-T BLA review (Kite/Gilead); competing with Carvykti/Abecma",
        "us_price_note": "CAR-T MM one-time ~$465K"
    },
    ("GILD", "liver", "liver_port"): {
        "us":  {"reachPct": 12, "wtpPct": 60, "priceK": 75},
        "eu":  {"reachPct": 8,  "wtpPct": 42, "priceK": 45},
        "row": {"reachPct": 2,  "wtpPct": 15, "priceK": 18},
        "us_reach_note": "Livdelzi PBC + HCV portfolio + Veklury COVID remdesivir",
        "us_price_note": "Mixed liver portfolio blended ~$75K/yr"
    },
    ("GILD", "biktarvy", "hiv_tx"): {
        "us":  {"reachPct": 45, "wtpPct": 75, "priceK": 42},
        "eu":  {"reachPct": 25, "wtpPct": 48, "priceK": 25},
        "row": {"reachPct": 8,  "wtpPct": 18, "priceK": 10},
        "us_reach_note": "Biktarvy dominant STR in HIV-1 treatment; ~45% US market share",
        "us_price_note": "Biktarvy ~$42K/yr WAC"
    },
    ("GILD", "descovy", "hiv_prep"): {
        "us":  {"reachPct": 25, "wtpPct": 60, "priceK": 25},
        "eu":  {"reachPct": 8,  "wtpPct": 22, "priceK": 15},
        "row": {"reachPct": 1,  "wtpPct": 5,  "priceK": 6},
        "us_reach_note": "Descovy PrEP dominant in US PrEP; Truvada generic pressure",
        "us_price_note": "Descovy PrEP ~$25K/yr"
    },
    # IONS
    ("IONS", "commercial", "tg"): {
        "us":  {"reachPct": 5, "wtpPct": 50, "priceK": 300},
        "eu":  {"reachPct": 3, "wtpPct": 35, "priceK": 180},
        "row": {"reachPct": 0.5, "wtpPct": 10, "priceK": 70},
        "us_reach_note": "TRYNGOLZA olezarsen FCS approved; sHTG sNDA PDUFA Apr 3 2026 expands addressable",
        "us_price_note": "Olezarsen FCS ~$300K/yr"
    },
    ("IONS", "dawnzera", "hae"): {
        "us":  {"reachPct": 12, "wtpPct": 40, "priceK": 400},
        "eu":  {"reachPct": 8,  "wtpPct": 28, "priceK": 250},
        "row": {"reachPct": 2,  "wtpPct": 8,  "priceK": 100},
        "us_reach_note": "DAWNZERA donidalorsen HAE launched Q3 2025; competes with Takhzyro",
        "us_price_note": "DAWNZERA ~$400K/yr"
    },
    ("IONS", "zilgan", "axd"): {
        "us":  {"reachPct": 55, "wtpPct": 65, "priceK": 550},
        "eu":  {"reachPct": 40, "wtpPct": 45, "priceK": 350},
        "row": {"reachPct": 10, "wtpPct": 12, "priceK": 130},
        "us_reach_note": "Zilganersen Alexander disease NDA Q1 2026; ultra-rare, first therapy",
        "us_price_note": "Ultra-rare ASO ~$550K/yr"
    },
    ("IONS", "eplont", "attr"): {
        "us":  {"reachPct": 18, "wtpPct": 50, "priceK": 350},
        "eu":  {"reachPct": 12, "wtpPct": 38, "priceK": 220},
        "row": {"reachPct": 3,  "wtpPct": 10, "priceK": 90},
        "us_reach_note": "WAINUA eplontersen ATTRv-PN + Phase 3 CARDIO-TTRansform ATTR-CM; AZ partnered",
        "us_price_note": "Eplontersen ~$350K/yr"
    },
    ("IONS", "bepiro", "hbv"): {
        "us":  {"reachPct": 15, "wtpPct": 45, "priceK": 65},
        "eu":  {"reachPct": 10, "wtpPct": 32, "priceK": 40},
        "row": {"reachPct": 8,  "wtpPct": 15, "priceK": 18},
        "us_reach_note": "Bepirovirsen HBV B-Well Phase 3 positive; first functional cure candidate",
        "us_price_note": "HBV functional cure estimated ~$65K/yr"
    },
    ("IONS", "pelac", "lpa"): {
        "us":  {"reachPct": 2, "wtpPct": 30, "priceK": 12},
        "eu":  {"reachPct": 1.2, "wtpPct": 22, "priceK": 7},
        "row": {"reachPct": 0.3, "wtpPct": 6, "priceK": 3},
        "us_reach_note": "Pelacarsen Lp(a) Phase 3 HORIZON CVOT readout mid-2026 (Novartis partnered)",
        "us_price_note": "Lp(a) lowering ~$12K/yr premium vs statins"
    },
    # KRYS
    ("KRYS", "commercial", "deb"): {
        "us":  {"reachPct": 60, "wtpPct": 75, "priceText": "500K", "priceK": 500},
        "eu":  {"reachPct": 40, "wtpPct": 50, "priceK": 320},
        "row": {"reachPct": 10, "wtpPct": 15, "priceK": 120},
        "us_reach_note": "VYJUVEK redosable gene therapy DEB; US 2023, EU 2025, Japan 2025 launches; ultra-rare",
        "us_price_note": "VYJUVEK ~$500K/yr redosable gene therapy"
    },
    ("KRYS", "kb803", "ocular_deb"): {
        "us":  {"reachPct": 45, "wtpPct": 55, "priceK": 350},
        "eu":  {"reachPct": 30, "wtpPct": 42, "priceK": 220},
        "row": {"reachPct": 6,  "wtpPct": 12, "priceK": 90},
        "us_reach_note": "KB803 ocular DEB Phase 3 registrational topline 2026; expansion of VYJUVEK",
        "us_price_note": "Ocular rare ~$350K/yr"
    },
    ("KRYS", "kb801", "nk"): {
        "us":  {"reachPct": 25, "wtpPct": 50, "priceK": 350},
        "eu":  {"reachPct": 15, "wtpPct": 38, "priceK": 220},
        "row": {"reachPct": 3,  "wtpPct": 10, "priceK": 85},
        "us_reach_note": "KB801 neurotrophic keratitis Phase 3 registrational; competes with Oxervate",
        "us_price_note": "Ophthalmic biologic ~$350K/yr"
    },
    ("KRYS", "kb407", "cf"): {
        "us":  {"reachPct": 6, "wtpPct": 30, "priceK": 300},
        "eu":  {"reachPct": 4, "wtpPct": 20, "priceK": 180},
        "row": {"reachPct": 1, "wtpPct": 6, "priceK": 70},
        "us_reach_note": "KB407 inhaled gene therapy CF Phase 1 CORAL-1 Cohort 3 positive",
        "us_price_note": "Inhaled gene therapy CF ~$300K/yr"
    },
    ("KRYS", "kb707", "nsclc"): {
        "us":  {"reachPct": 3, "wtpPct": 25, "priceK": 200},
        "eu":  {"reachPct": 2, "wtpPct": 18, "priceK": 120},
        "row": {"reachPct": 0.4, "wtpPct": 5, "priceK": 50},
        "us_reach_note": "KB707 redosable immunotherapy NSCLC Phase 1/2; early vs established IO",
        "us_price_note": "Oncology IO ~$200K/yr"
    },
    ("KRYS", "kb111", "hhd"): {
        "us":  {"reachPct": 50, "wtpPct": 60, "priceK": 250},
        "eu":  {"reachPct": 35, "wtpPct": 45, "priceK": 160},
        "row": {"reachPct": 8,  "wtpPct": 12, "priceK": 60},
        "us_reach_note": "KB111 Hailey-Hailey Phase 1/2; ultra-rare first-in-class",
        "us_price_note": "Ultra-rare topical gene therapy ~$250K/yr"
    },
    # LLY
    ("LLY", "commercial", "incretin"): {
        "us":  {"reachPct": 5, "wtpPct": 65, "priceK": 14},
        "eu":  {"reachPct": 1.5, "wtpPct": 25, "priceK": 8},
        "row": {"reachPct": 0.5, "wtpPct": 8, "priceK": 4},
        "us_reach_note": "Mounjaro+Zepbound dominating GLP-1/GIP market; supply-constrained ~5% of eligible obesity+T2D",
        "us_price_note": "Mounjaro/Zepbound ~$14K/yr gross"
    },
    ("LLY", "orforglipron", "oral_glp1"): {
        "us":  {"reachPct": 8, "wtpPct": 60, "priceK": 12},
        "eu":  {"reachPct": 3, "wtpPct": 30, "priceK": 7},
        "row": {"reachPct": 1, "wtpPct": 10, "priceK": 4},
        "us_reach_note": "Orforglipron FDA approved Apr 2026; first oral GLP-1 pill, manufacturing advantage",
        "us_price_note": "Oral GLP-1 ~$12K/yr"
    },
    ("LLY", "retatrutide", "triple"): {
        "us":  {"reachPct": 6, "wtpPct": 55, "priceK": 16},
        "eu":  {"reachPct": 2, "wtpPct": 25, "priceK": 9},
        "row": {"reachPct": 0.5, "wtpPct": 8, "priceK": 5},
        "us_reach_note": "Retatrutide triple agonist Phase 3; highest-efficacy weight loss",
        "us_price_note": "Premium next-gen obesity ~$16K/yr"
    },
    ("LLY", "verzenio", "bc"): {
        "us":  {"reachPct": 20, "wtpPct": 60, "priceK": 180},
        "eu":  {"reachPct": 14, "wtpPct": 42, "priceK": 110},
        "row": {"reachPct": 3,  "wtpPct": 10, "priceK": 45},
        "us_reach_note": "Verzenio HR+ BC adjuvant + mBC; CDK4/6 class leader",
        "us_price_note": "Verzenio ~$180K/yr"
    },
    ("LLY", "taltz", "pso_psa"): {
        "us":  {"reachPct": 8, "wtpPct": 55, "priceK": 65},
        "eu":  {"reachPct": 5, "wtpPct": 38, "priceK": 35},
        "row": {"reachPct": 1, "wtpPct": 10, "priceK": 14},
        "us_reach_note": "Taltz IL-17A pso+PsA+axSpA; ~8% systemic psoriasis share",
        "us_price_note": "Taltz ~$65K/yr"
    },
    ("LLY", "kisunla", "alz"): {
        "us":  {"reachPct": 1, "wtpPct": 30, "priceK": 32},
        "eu":  {"reachPct": 0.4, "wtpPct": 15, "priceK": 18},
        "row": {"reachPct": 0.1, "wtpPct": 5, "priceK": 8},
        "us_reach_note": "Kisunla donanemab amyloid-confirmed early AD; infusion centers limit reach",
        "us_price_note": "Kisunla ~$32K/yr"
    },
    ("LLY", "jardiance", "t2d_hf"): {
        "us":  {"reachPct": 4, "wtpPct": 60, "priceK": 7},
        "eu":  {"reachPct": 2, "wtpPct": 35, "priceK": 4},
        "row": {"reachPct": 0.5, "wtpPct": 12, "priceK": 2},
        "us_reach_note": "Jardiance SGLT2 T2D+HF; BI partnership, Lilly share ~40% of global",
        "us_price_note": "Jardiance ~$7K/yr Lilly US net"
    },
    # MDGL
    ("MDGL", "commercial", "mash"): {
        "us":  {"reachPct": 2,   "wtpPct": 45, "priceK": 50},
        "eu":  {"reachPct": 1.2, "wtpPct": 32, "priceK": 30},
        "row": {"reachPct": 0.3, "wtpPct": 8,  "priceK": 12},
        "us_reach_note": "Rezdiffra MASH F2-F3 first-to-market; rapid ramp but huge TAM caps reach %",
        "us_price_note": "Rezdiffra ~$50K/yr"
    },
    ("MDGL", "f4c", "mash_f4"): {
        "us":  {"reachPct": 3,   "wtpPct": 40, "priceK": 50},
        "eu":  {"reachPct": 2,   "wtpPct": 28, "priceK": 30},
        "row": {"reachPct": 0.4, "wtpPct": 8,  "priceK": 12},
        "us_reach_note": "Rezdiffra MASH F4c compensated cirrhosis outcomes study; first-mover if approved",
        "us_price_note": "Rezdiffra F4 ~$50K/yr"
    },
    ("MDGL", "combos", "mash_combo"): {
        "us":  {"reachPct": 0.8, "wtpPct": 25, "priceK": 60},
        "eu":  {"reachPct": 0.5, "wtpPct": 18, "priceK": 35},
        "row": {"reachPct": 0.1, "wtpPct": 5,  "priceK": 14},
        "us_reach_note": "Rezdiffra combination pipeline Phase 1/2 + preclinical",
        "us_price_note": "Combo pricing premium ~$60K/yr"
    },
    # NBIX
    ("NBIX", "commercial", "td"): {
        "us":  {"reachPct": 10, "wtpPct": 70, "priceK": 100},
        "eu":  {"reachPct": 3,  "wtpPct": 35, "priceK": 55},
        "row": {"reachPct": 0.5, "wtpPct": 10, "priceK": 20},
        "us_reach_note": "Ingrezza TD + Huntington's chorea; specialty neuro franchise",
        "us_price_note": "Ingrezza ~$100K/yr"
    },
    ("NBIX", "crenessity", "cah"): {
        "us":  {"reachPct": 45, "wtpPct": 65, "priceK": 120},
        "eu":  {"reachPct": 30, "wtpPct": 45, "priceK": 75},
        "row": {"reachPct": 8,  "wtpPct": 12, "priceK": 30},
        "us_reach_note": "Crenessity CAH launched Dec 2024; first CRF1 antagonist for CAH",
        "us_price_note": "Crenessity ~$120K/yr"
    },
    ("NBIX", "osav", "mdd"): {
        "us":  {"reachPct": 2,   "wtpPct": 35, "priceK": 14},
        "eu":  {"reachPct": 1.2, "wtpPct": 25, "priceK": 8},
        "row": {"reachPct": 0.3, "wtpPct": 6,  "priceK": 3},
        "us_reach_note": "Osavampator AMPA MDD Phase 3; differentiated MoA vs SSRIs",
        "us_price_note": "Novel MDD ~$14K/yr"
    },
    ("NBIX", "direc", "schizo"): {
        "us":  {"reachPct": 8,  "wtpPct": 40, "priceK": 28},
        "eu":  {"reachPct": 5,  "wtpPct": 30, "priceK": 15},
        "row": {"reachPct": 1,  "wtpPct": 8,  "priceK": 6},
        "us_reach_note": "Direclidine NBI-568 muscarinic schizophrenia Phase 3; competes with BMS KarXT",
        "us_price_note": "Muscarinic schizophrenia ~$28K/yr"
    },
    ("NBIX", "pipeline", "neuro_pipe"): {
        "us":  {"reachPct": 2, "wtpPct": 25, "priceK": 28},
        "eu":  {"reachPct": 1.2, "wtpPct": 18, "priceK": 15},
        "row": {"reachPct": 0.2, "wtpPct": 5, "priceK": 6},
        "us_reach_note": "Broader muscarinic + neuro pipeline Phase 1/2",
        "us_price_note": "Specialty CNS blended ~$28K/yr"
    },
    ("NBIX", "vykat", "pws"): {
        "us":  {"reachPct": 15, "wtpPct": 55, "priceK": 90},
        "eu":  {"reachPct": 10, "wtpPct": 38, "priceK": 55},
        "row": {"reachPct": 2,  "wtpPct": 10, "priceK": 22},
        "us_reach_note": "VYKAT XR diazoxide choline Prader-Willi acquired Apr 2025; $190M 2025",
        "us_price_note": "VYKAT XR ~$90K/yr"
    },
    # NUVL
    ("NUVL", "zides", "ros1"): {
        "us":  {"reachPct": 40, "wtpPct": 55, "priceK": 220},
        "eu":  {"reachPct": 28, "wtpPct": 40, "priceK": 130},
        "row": {"reachPct": 5,  "wtpPct": 10, "priceK": 50},
        "us_reach_note": "Zidesamtinib ROS1 NDA filed PDUFA Sep 18 2026; best-in-class ROS1 TKI",
        "us_price_note": "ROS1 TKI ~$220K/yr"
    },
    ("NUVL", "nelad", "alk"): {
        "us":  {"reachPct": 20, "wtpPct": 45, "priceK": 220},
        "eu":  {"reachPct": 14, "wtpPct": 32, "priceK": 130},
        "row": {"reachPct": 3,  "wtpPct": 10, "priceK": 50},
        "us_reach_note": "Neladalkib ALK NDA H1 2026 TKI pre-treated; competes with lorlatinib",
        "us_price_note": "ALK TKI ~$220K/yr"
    },
    ("NUVL", "nvl330", "her2"): {
        "us":  {"reachPct": 8,  "wtpPct": 35, "priceK": 220},
        "eu":  {"reachPct": 5,  "wtpPct": 25, "priceK": 130},
        "row": {"reachPct": 1,  "wtpPct": 8,  "priceK": 50},
        "us_reach_note": "NVL-330 HER2 NSCLC Phase 1a/1b HEROEX-1; early vs Enhertu ADC",
        "us_price_note": "HER2 TKI ~$220K/yr"
    },
    # ONC - commercial Brukinsa
    ("ONC", "commercial", "btk"): {
        "us":  {"reachPct": 22, "wtpPct": 65, "priceK": 210},
        "eu":  {"reachPct": 15, "wtpPct": 48, "priceK": 125},
        "row": {"reachPct": 4,  "wtpPct": 12, "priceK": 50},
        "us_reach_note": "Brukinsa BTKi CLL+MCL+WM; ~22% CLL/NHL share, growing vs Imbruvica decline",
        "us_price_note": "Brukinsa ~$210K/yr"
    },
    # RYTM
    ("RYTM", "commercial", "rare_ob"): {
        "us":  {"reachPct": 12, "wtpPct": 65, "priceK": 420},
        "eu":  {"reachPct": 8,  "wtpPct": 45, "priceK": 260},
        "row": {"reachPct": 2,  "wtpPct": 10, "priceK": 110},
        "us_reach_note": "Imcivree setmelanotide BBS+POMC/LEPR+ACQ HO; growing +50% YoY",
        "us_price_note": "Imcivree ~$420K/yr ultra-rare"
    },
    ("RYTM", "acq_ho", "ho"): {
        "us":  {"reachPct": 18, "wtpPct": 55, "priceK": 400},
        "eu":  {"reachPct": 12, "wtpPct": 40, "priceK": 250},
        "row": {"reachPct": 2,  "wtpPct": 10, "priceK": 100},
        "us_reach_note": "Setmelanotide acquired HO sNDA PDUFA Mar 20 2026; label expansion",
        "us_price_note": "Setmelanotide acquired HO ~$400K/yr"
    },
    ("RYTM", "emanate", "mc4r_rare"): {
        "us":  {"reachPct": 25, "wtpPct": 55, "priceK": 420},
        "eu":  {"reachPct": 18, "wtpPct": 42, "priceK": 260},
        "row": {"reachPct": 3,  "wtpPct": 10, "priceK": 110},
        "us_reach_note": "EMANATE Phase 3 topline Mar 2026; 4 additional rare MC4R indications",
        "us_price_note": "Ultra-rare MC4R ~$420K/yr"
    },
    ("RYTM", "bivam", "oral_mc4r"): {
        "us":  {"reachPct": 10, "wtpPct": 45, "priceK": 180},
        "eu":  {"reachPct": 6,  "wtpPct": 32, "priceK": 110},
        "row": {"reachPct": 1,  "wtpPct": 8,  "priceK": 45},
        "us_reach_note": "Bivamelagon oral MC4R Phase 3 planned YE 2026; oral convenience advantage",
        "us_price_note": "Oral MC4R ~$180K/yr (below injectable)"
    },
    ("RYTM", "pws", "pws"): {
        "us":  {"reachPct": 15, "wtpPct": 40, "priceK": 400},
        "eu":  {"reachPct": 10, "wtpPct": 30, "priceK": 250},
        "row": {"reachPct": 2,  "wtpPct": 8,  "priceK": 100},
        "us_reach_note": "Setmelanotide + RM-718 Prader-Willi Phase 2 exploratory + Phase 1/2",
        "us_price_note": "PWS hyperphagia ~$400K/yr"
    },
    # TVTX
    ("TVTX", "filspari_igan", "igan"): {
        "us":  {"reachPct": 8,  "wtpPct": 45, "priceK": 130},
        "eu":  {"reachPct": 5,  "wtpPct": 32, "priceK": 80},
        "row": {"reachPct": 0.8, "wtpPct": 10, "priceK": 30},
        "us_reach_note": "FILSPARI sparsentan IgAN full approval; growing rapidly",
        "us_price_note": "FILSPARI IgAN ~$130K/yr"
    },
    ("TVTX", "filspari_fsgs", "fsgs"): {
        "us":  {"reachPct": 6,  "wtpPct": 38, "priceK": 130},
        "eu":  {"reachPct": 4,  "wtpPct": 28, "priceK": 80},
        "row": {"reachPct": 0.6, "wtpPct": 8, "priceK": 30},
        "us_reach_note": "FILSPARI FSGS full approval Apr 2026; first-ever FSGS therapy",
        "us_price_note": "FILSPARI FSGS ~$130K/yr"
    },
    ("TVTX", "pegtibatinase", "hcu"): {
        "us":  {"reachPct": 65, "wtpPct": 60, "priceK": 400},
        "eu":  {"reachPct": 45, "wtpPct": 45, "priceK": 250},
        "row": {"reachPct": 10, "wtpPct": 12, "priceK": 100},
        "us_reach_note": "Pegtibatinase classical homocystinuria Phase 3 HARMONY; ultra-rare ~1K US",
        "us_price_note": "Ultra-rare enzyme replacement ~$400K/yr"
    },
    # UCB
    ("UCB", "commercial", "bimzelx"): {
        "us":  {"reachPct": 5, "wtpPct": 45, "priceK": 70},
        "eu":  {"reachPct": 4, "wtpPct": 35, "priceK": 40},
        "row": {"reachPct": 0.8, "wtpPct": 10, "priceK": 16},
        "us_reach_note": "Bimzelx IL-17A/F pso+HS+PsA+axSpA; late US launch catching up to Cosentyx/Taltz",
        "us_price_note": "Bimzelx ~$70K/yr"
    },
    ("UCB", "neuro_rare", "neuro_port"): {
        "us":  {"reachPct": 30, "wtpPct": 55, "priceK": 180},
        "eu":  {"reachPct": 20, "wtpPct": 40, "priceK": 110},
        "row": {"reachPct": 3,  "wtpPct": 10, "priceK": 40},
        "us_reach_note": "Fintepla Dravet/LGS + Rystiggo gMG + Zilbrysq gMG portfolio",
        "us_price_note": "Rare neuro portfolio blended ~$180K/yr"
    },
    ("UCB", "evenity", "osteo"): {
        "us":  {"reachPct": 3, "wtpPct": 45, "priceK": 22},
        "eu":  {"reachPct": 2, "wtpPct": 32, "priceK": 13},
        "row": {"reachPct": 0.3, "wtpPct": 8, "priceK": 5},
        "us_reach_note": "Evenity romosozumab osteoporosis (Amgen partnered); specialist-initiated",
        "us_price_note": "Evenity ~$22K/yr"
    },
    ("UCB", "cimzia", "ra_cd"): {
        "us":  {"reachPct": 2, "wtpPct": 30, "priceK": 50},
        "eu":  {"reachPct": 1.2, "wtpPct": 22, "priceK": 28},
        "row": {"reachPct": 0.2, "wtpPct": 6, "priceK": 10},
        "us_reach_note": "Cimzia anti-TNF RA+Crohn's+PsA; declining vs biosimilars",
        "us_price_note": "Cimzia ~$50K/yr"
    },
    ("UCB", "vimpat", "epilepsy_leg"): {
        "us":  {"reachPct": 12, "wtpPct": 50, "priceK": 18},
        "eu":  {"reachPct": 8,  "wtpPct": 35, "priceK": 10},
        "row": {"reachPct": 1,  "wtpPct": 8,  "priceK": 4},
        "us_reach_note": "Vimpat+Briviact focal epilepsy; Vimpat LOE declining, Briviact growing",
        "us_price_note": "Vimpat/Briviact blended ~$18K/yr"
    },
    ("UCB", "donzakimig", "epilepsy_new"): {
        "us":  {"reachPct": 4,  "wtpPct": 32, "priceK": 20},
        "eu":  {"reachPct": 3,  "wtpPct": 22, "priceK": 12},
        "row": {"reachPct": 0.5, "wtpPct": 6, "priceK": 4},
        "us_reach_note": "Donzakimig Phase 2/3 epilepsy; adjunctive novel mechanism",
        "us_price_note": "Specialty epilepsy ~$20K/yr"
    },
    ("UCB", "dapirolizumab", "sle"): {
        "us":  {"reachPct": 12, "wtpPct": 42, "priceK": 60},
        "eu":  {"reachPct": 8,  "wtpPct": 30, "priceK": 35},
        "row": {"reachPct": 1,  "wtpPct": 8,  "priceK": 14},
        "us_reach_note": "Dapirolizumab anti-CD40L Phase 3 SLE",
        "us_price_note": "SLE biologic ~$60K/yr"
    },
    # VRDN
    ("VRDN", "veli", "ted_iv"): {
        "us":  {"reachPct": 18, "wtpPct": 55, "priceK": 320},
        "eu":  {"reachPct": 12, "wtpPct": 40, "priceK": 200},
        "row": {"reachPct": 2,  "wtpPct": 10, "priceK": 80},
        "us_reach_note": "Veligrotug IV BLA filed; best-in-class TED vs Tepezza",
        "us_price_note": "Veligrotug ~$320K/yr (below Tepezza)"
    },
    ("VRDN", "ele", "ted_sc"): {
        "us":  {"reachPct": 14, "wtpPct": 45, "priceK": 200},
        "eu":  {"reachPct": 10, "wtpPct": 32, "priceK": 120},
        "row": {"reachPct": 1.5, "wtpPct": 8, "priceK": 50},
        "us_reach_note": "Elegrobart SC Phase 3 REVEAL; expands TED to SC population",
        "us_price_note": "Elegrobart SC ~$200K/yr"
    },
}

manifest = json.loads((CONFIGS / "manifest.json").read_text())
added = 0
issues = []

for t in manifest:
    path = CONFIGS / (t + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    for a in d["assets"]:
        for ind in a["indications"]:
            key = (t, a["id"], ind["id"])
            if key not in SLICES:
                continue
            if ind["market"].get("company_slice"):
                continue  # already has one
            s = SLICES[key]
            cs = {
                "us":  {"reachPct": s["us"]["reachPct"],  "wtpPct": s["us"]["wtpPct"],  "priceK": s["us"]["priceK"]},
                "eu":  {"reachPct": s["eu"]["reachPct"],  "wtpPct": s["eu"]["wtpPct"],  "priceK": s["eu"]["priceK"]},
                "row": {"reachPct": s["row"]["reachPct"], "wtpPct": s["row"]["wtpPct"], "priceK": s["row"]["priceK"]},
            }
            ind["market"]["company_slice"] = cs
            ind["market"]["company_slice_sources"] = {
                "us.reachPct": {"note": s["us_reach_note"]},
                "us.priceK":   {"note": s["us_price_note"]},
            }
            changed = True
            added += 1
            # Validate
            r = ind["market"].get("regions", {})
            som = sum(
                (r.get(rk, {}).get("patientsK", 0))
                * (cs[rk]["reachPct"] / 100)
                * (cs[rk]["wtpPct"] / 100)
                * cs[rk]["priceK"]
                for rk in ["us", "eu", "row"]
            )
            salesM = ind["market"].get("salesM", 0)
            status = "OK" if som >= salesM or salesM == 0 else "SALES>SOM"
            print(f"{t:5s} {a['id']:18s} {ind['id']:15s} sales=${salesM:>6.0f}M  SOM=${som:>7.0f}M  [{status}]")
            if salesM > 0 and som < salesM:
                issues.append((t, a["id"], ind["id"], salesM, som))
    if changed:
        path.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")

print(f"\n{added} company_slice entries added")
if issues:
    print(f"{len(issues)} SALES > SOM issues:")
    for i in issues:
        print(f"  {i}")
else:
    print("All OK")
