# -*- coding: utf-8 -*-
"""
Hand-researched, drug-specific SOM tooltips for batch 1:
LLY, ABBV, GILD, UCB, ONC, ALNY, ARGX, BBIO

Each entry maps (ticker, asset_id, ind_id) to a dict of 9 tooltips:
  us.reachPct / us.wtpPct / us.priceK
  eu.reachPct / eu.wtpPct / eu.priceK
  row.reachPct / row.wtpPct / row.priceK

Notes explain why the specific slider value in config is what it is --
actual sales, reach, payor coverage, HTA decisions, WAC/net pricing.
ASCII only, no em-dash, <200 chars per note.
"""

SOM_TOOLTIPS = {

    # ============================== LLY ==============================
    ("LLY", "commercial", "incretin"): {
        "us.reachPct": {"note": "Mounjaro+Zepbound ~2.8M US pts on tx of ~40M AOM-eligible = ~7%; slider 12% reflects 2028 supply-unlocked peak (capacity +60% H1-26)."},
        "us.wtpPct":   {"note": "80% -- SELECT/SURMOUNT CV+MACE benefit + T2D label drives broad commercial + Medicare Part D coverage for Mounjaro; Part D weight-loss statute caps Zepbound."},
        "us.priceK":   {"note": "Mounjaro $13K + Zepbound $12K WAC; LillyDirect self-pay $349/mo (~$4K) for single-dose vials; net ~$14K blended after 30-40% PBM rebates."},
        "eu.reachPct": {"note": "~4% of 30M AOM-eligible EU; UK NHS covers Mounjaro T2D + Wegovy obesity BMI>=35+comorbid; Germany G-BA added benefit T2D only, obesity self-pay."},
        "eu.wtpPct":   {"note": "35% -- NICE TA875 Mounjaro T2D reimbursed; obesity restricted to specialist tier-3 weight services; France ASMR IV (minor) limits uptake."},
        "eu.priceK":   {"note": "EU net ~$8K -- UK Mounjaro GBP 120-220/mo NHS, Germany AMNOG ~EUR 400/mo, ~55% of US list post-HTA negotiation."},
        "row.reachPct":{"note": "~1% of 50M eligible ROW -- Japan PMDA Mounjaro T2D only (not obesity); China NMPA approved 2024, NRDL pending; emerging markets compounded semag."},
        "row.wtpPct":  {"note": "12% -- Japan NHI tirzepatide T2D covered 30% copay; Korea HIRA covered T2D; AU PBS T2D-only; obesity self-pay ex-Japan."},
        "row.priceK":  {"note": "$4K blended -- Japan NHI tirzepatide ~$8K/yr reimbursed, China Gaoxin private ~$3K, emerging markets cash-pay $1-2K via Lilly tiered access."}
    },
    ("LLY", "orforglipron", "oral_glp1"): {
        "us.reachPct": {"note": "Orforglipron Apr 2026 FDA approval; 8% reflects rapid PCP uptake -- first oral non-peptide GLP-1 eliminates injection barrier + unlimited oral manufacturing."},
        "us.wtpPct":   {"note": "60% -- obesity launch WTP lower than Zepbound as payors demand step-therapy post-injectable; T2D label drives Medicare Part D coverage."},
        "us.priceK":   {"note": "Launch WAC ~$12K/yr; priced ~10-15% below Zepbound to drive formulary preference; LillyDirect cash program expected <$300/mo for oral pill."},
        "eu.reachPct": {"note": "3% -- EMA filing H2-2026, reimbursement 12-18mo behind US; no injection cold-chain advantage drives primary-care access once HTA clears."},
        "eu.wtpPct":   {"note": "30% -- early-launch WTP; NICE/G-BA will require ACHIEVE-1 head-to-head vs injectable before expanded coverage; obesity self-pay dominant."},
        "eu.priceK":   {"note": "$7K/yr post-HTA, ~55% of US list; EU pricing anchored to Wegovy/Mounjaro oral semaglutide (~EUR 300-400/mo)."},
        "row.reachPct":{"note": "1% of 50M ROW -- Japan PMDA + China NMPA filings 2026; emerging markets primary care will benefit most from oral formulation once approved."},
        "row.wtpPct":  {"note": "10% -- Japan NHI expected broad coverage for T2D; China NRDL pending; obesity access minimal ex-Japan at launch."},
        "row.priceK":  {"note": "$4K blended -- oral manufacturing enables sharper tiered pricing than injectable GLP-1s; emerging markets $1-3K cash-pay."}
    },
    ("LLY", "retatrutide", "triple"): {
        "us.reachPct": {"note": "Phase 3; 6% peak reflects premium positioning for highest-BMI patients -- 24% weight loss Phase 2 best-in-class but 2028+ launch behind tirzepatide base."},
        "us.wtpPct":   {"note": "55% -- pre-label estimate; glucagon agonist raises LFT/HR concerns needing Phase 3 safety; premium pricing limits payor adoption to severe obesity."},
        "us.priceK":   {"note": "Projected $16K WAC -- premium vs Zepbound $12K reflecting best-in-class efficacy + multi-indication (MASH/OA/sleep apnea) label strategy."},
        "eu.reachPct": {"note": "2% -- EMA approval 2028+; HTA will gate to BMI>=40 + failed prior GLP-1; most severe-obesity patients will flow to retatrutide."},
        "eu.wtpPct":   {"note": "25% -- lower than tirzepatide reflecting later launch, higher bar for HTA added benefit vs now-established injectable GLP-1 class."},
        "eu.priceK":   {"note": "$9K/yr -- ~55% of US; premium over Mounjaro net on superior efficacy but HTA negotiation cuts list sharply."},
        "row.reachPct":{"note": "0.5% -- Japan PMDA + AU TGA likely first ex-US; glucagon mechanism metabolic benefits attractive to APAC payors if safety clean."},
        "row.wtpPct":  {"note": "8% -- narrow ROW access at launch to Japan, AU, select APAC; emerging markets too cost-sensitive for triple agonist premium."},
        "row.priceK":  {"note": "$5K blended -- Japan NHI ~$10K, emerging markets tiered or not launched; Lilly prioritizing US/EU rollout 2028-30."}
    },
    ("LLY", "verzenio", "bc"): {
        "us.reachPct": {"note": "Verzenio 20% of ~400K HR+/HER2- US pts on tx -- only adjuvant CDK4/6i approved (monarchE), ~$2.5B US 2025; growing in adj while Ibrance leads 1L MBC."},
        "us.wtpPct":   {"note": "60% -- NCCN Cat 1 adj node-positive HR+ EBC + 1L/2L MBC; Medicare Part D oral oncology parity + commercial broad; copay card $0 commercial."},
        "us.priceK":   {"note": "Verzenio WAC $17K/mo = $204K/yr, blended ~$180K net after Part D rebates + 340B/GPO discounts; Lilly Cares PAP for uninsured."},
        "eu.reachPct": {"note": "14% of 450K HR+ EU -- NICE TA810/G-BA reimbursed adj; 4yr adj duration drives prevalent penetration vs competing CDK4/6i."},
        "eu.wtpPct":   {"note": "42% -- NICE ACD Jul 2023 recommended adj, ASMR IV France, G-BA added benefit not proven; shares 1L with Ibrance/Kisqali."},
        "eu.priceK":   {"note": "$110K/yr EU net -- UK NHS discount ~GBP 2.5K/mo, Germany AMNOG ~EUR 3K/mo post-negotiation; ~60% of US list typical."},
        "row.reachPct":{"note": "3% of 550K ROW -- Japan NHI reimbursed, China NRDL added 2024; emerging markets AI generics (letrozole) dominate."},
        "row.wtpPct":  {"note": "10% -- Japan NHI full 30% copay, China NRDL price ~$25K post-negotiation, rest patchy; ROW share lags Ibrance (launched 2yr earlier)."},
        "row.priceK":  {"note": "$45K blended -- Japan ~$80K NHI, China NRDL ~$30K, emerging markets Lilly access program or AI generics <$2K."}
    },
    ("LLY", "taltz", "pso_psa"): {
        "us.reachPct": {"note": "Taltz ~8% of 1.5M systemic pso -- IL-17A class with Cosentyx; growing vs Humira biosimilars; Skyrizi IL-23 taking share in severe pso."},
        "us.wtpPct":   {"note": "55% -- commercial + Medicare Part B/D ladder; typically 2L after Humira biosimilar step-therapy; PsA/axSpA labels expand usable pop."},
        "us.priceK":   {"note": "Taltz WAC ~$87K/yr (4 doses/quarter maint); net $65K after ~25% PBM rebates + Taltz Together copay $5/mo commercial."},
        "eu.reachPct": {"note": "5% of 2.5M EU mod-severe pso -- biosimilar adalim first-line ~60% share; IL-17 class 2L+; Bimzelx (UCB) taking dual IL-17A/F share."},
        "eu.wtpPct":   {"note": "38% -- NICE TA442 + G-BA reimbursed pso/PsA/axSpA; post-biosimilar step therapy limits first-line use; ASMR IV minor add-on."},
        "eu.priceK":   {"note": "EU net ~$35K -- UK NHS ~GBP 1.1K/mo, Germany AMNOG ~EUR 1.7K/mo post-negotiation; ~55% of US list."},
        "row.reachPct":{"note": "1% of 15M ROW mod-severe pso -- Japan J-DPC reimbursed broadly, China NRDL 2021; EM biosimilar adalim dominant."},
        "row.wtpPct":  {"note": "10% -- Japan NHI 30% copay, China NRDL listed ~$13K; emerging markets MTX/phototherapy standard."},
        "row.priceK":  {"note": "$14K blended -- Japan NHI ~$25K, China NRDL ~$13K, EM via Lilly access program or biosimilar anti-TNF substitution."}
    },
    ("LLY", "kisunla", "alz"): {
        "us.reachPct": {"note": "Kisunla ~30-50K US pts treated of 2M amyloid+ early AD = ~2-3%; PET/MRI infusion infrastructure + ARIA monitoring caps scaling."},
        "us.wtpPct":   {"note": "55% -- CMS NCD 2023 covers anti-amyloid with registry; Medicare Part B J-code Oct 2024; commercial variable; APOE4 testing required."},
        "us.priceK":   {"note": "Kisunla $32K/yr WAC = $695 per vial, 12-18mo finite duration cuts cumulative cost; shorter course vs Leqembi $26.5K chronic IV."},
        "eu.reachPct": {"note": "0.8% of 1.5M EU eligible -- EMA CHMP negative opinion Jul 2024 reversed Mar 2025 narrow label; UK NICE TA recommended only in research context."},
        "eu.wtpPct":   {"note": "25% -- narrow EMA label (APOE4 non-homozygotes), G-BA added benefit not proven; limited specialty center infusion capacity gates."},
        "eu.priceK":   {"note": "$18K/yr -- post-HTA UK/Germany access pricing ~55% of US list; EU ACB voluntary discount to enable reimbursement."},
        "row.reachPct":{"note": "0.2% of 25M ROW -- Japan PMDA approved Sep 2024, infusion centers ramping; China/EM minimal anti-amyloid access, donepezil generic dominant."},
        "row.wtpPct":  {"note": "8% -- Japan NHI 30% copay + specialty center gating; AU TGA under review; emerging markets no reimbursement."},
        "row.priceK":  {"note": "$8K blended -- Japan NHI ~$22K reimbursed, AU self-pay, EM negligible revenue; Lilly focused on US/EU first."}
    },
    ("LLY", "jardiance", "t2d_hf"): {
        "us.reachPct": {"note": "Jardiance ~4% of 25M T2D pts -- SGLT2 class ~15% penetration shared w/ Farxiga; Lilly ~40% global share via BI co-promote."},
        "us.wtpPct":   {"note": "60% -- Medicare Part D + commercial broad coverage on EMPA-REG CV outcomes + HFrEF/HFpEF/CKD label expansions; T1 formulary."},
        "us.priceK":   {"note": "Jardiance WAC $7K/yr ($570/mo) gross, net ~$3K post 50%+ PBM rebates; Lilly Cares PAP + $10/mo commercial copay card."},
        "eu.reachPct": {"note": "2% of 22M EU T2D on pharmacotx -- SGLT2 class second-line post-metformin; NICE/G-BA reimbursed broadly on outcomes data."},
        "eu.wtpPct":   {"note": "35% -- NICE TA390/G-BA added benefit T2D + HF; broad step-therapy post-metformin; ASMR IV France."},
        "eu.priceK":   {"note": "$4K EU net -- UK NHS ~GBP 500/yr, Germany AMNOG ~EUR 700/yr; metformin generic baseline keeps SGLT2 pricing disciplined."},
        "row.reachPct":{"note": "0.5% of 150M ROW T2D on pharmacotx -- Japan NHI full coverage, China NRDL added 2020, EM metformin/SU dominant."},
        "row.wtpPct":  {"note": "12% -- Japan NHI 30% copay, China NRDL ~70% discount to launch, AU PBS listed; emerging markets generic oral antidiabetics."},
        "row.priceK":  {"note": "$2K blended -- Japan NHI ~$4K, China NRDL ~$400/yr post-negotiation, EM cash-pay $1-2K or generic substitution."}
    },

    # ============================== ABBV ==============================
    ("ABBV", "skyrizi", "pso"): {
        "us.reachPct": {"note": "Skyrizi ~15% of 1.5M US mod-severe pso -- IL-23 class leader, overtook Humira as #1 pso Rx 2024; $6B 2025 pso sales globally."},
        "us.wtpPct":   {"note": "65% -- NCCN-like AAD pathway first-line IL-23/IL-17 post-Humira biosimilar step; Medicare Part D + commercial T2; Skyrizi Complete copay $5."},
        "us.priceK":   {"note": "Skyrizi WAC $100K/yr (4 doses q12wk maintenance); net ~$70K after PBM rebates; SC self-injection OnBody device launched 2023."},
        "eu.reachPct": {"note": "10% of 2.5M EU mod-severe pso -- NICE TA596 + G-BA reimbursed; biosimilar adalim first-line limits reach; Bimzelx taking dual IL-17A/F share."},
        "eu.wtpPct":   {"note": "50% -- NICE full recommended, G-BA added benefit proven PASI 90/100 superiority vs Humira; ASMR IV France moderate."},
        "eu.priceK":   {"note": "$35K EU net -- UK NHS ~GBP 10K/yr, Germany AMNOG ~EUR 16K/yr post-Rabattvertrag; ~50% of US list."},
        "row.reachPct":{"note": "3% of 15M ROW -- Japan J-DPC + China NRDL 2023; emerging markets biosimilar adalim or MTX standard."},
        "row.wtpPct":  {"note": "12% -- Japan NHI 30% copay broadly reimbursed; China NRDL listed ~60% discount; AU PBS; emerging markets minimal."},
        "row.priceK":  {"note": "$15K blended -- Japan NHI ~$22K, China NRDL ~$14K, EM AbbVie patient access or biosimilar anti-TNF."}
    },
    ("ABBV", "skyrizi", "ibd"): {
        "us.reachPct": {"note": "Skyrizi IBD launched 2022 CD + 2024 UC; 10% of ~800K US mod-severe IBD pts on advanced tx; fastest-growing IBD biologic 2025."},
        "us.wtpPct":   {"note": "60% -- AGA clinical care pathway added Skyrizi CD/UC; commercial + Medicare Part B IV induction + Part D SC maint; copay card $5."},
        "us.priceK":   {"note": "Skyrizi IBD WAC $130K/yr (higher dose than pso) net ~$70K; FORTIFY + INSPIRE/COMMAND superior vs Stelara drove formulary wins."},
        "eu.reachPct": {"note": "7% of 1.2M EU mod-severe IBD on advanced tx -- EMA CD 2022 + UC 2024; NICE TA888 CD reimbursed; post-TNF biosim step."},
        "eu.wtpPct":   {"note": "45% -- NICE + G-BA added benefit proven vs Stelara in SEQUENCE head-to-head CD; HTA step-therapy limits 1L."},
        "eu.priceK":   {"note": "$35K EU net -- UK/Germany ~50% of US list post-negotiation; higher IBD dose costs vs pso partially offset by discounts."},
        "row.reachPct":{"note": "2% of 8M ROW IBD -- Japan NHI + China NRDL 2024 CD; emerging markets TNF biosim dominant."},
        "row.wtpPct":  {"note": "10% -- Japan NHI 30% copay; China NRDL listed post-2024; rest patchy specialist only."},
        "row.priceK":  {"note": "$15K blended -- Japan NHI higher IBD dose ~$25K, China NRDL ~$14K."}
    },
    ("ABBV", "rinvoq", "ra"): {
        "us.reachPct": {"note": "Rinvoq RA ~8% of 1.5M US biologic/advanced RA -- oral JAKi class w/ Xeljanz; FDA black box limits 1L vs TNF; $2.2B RA 2025."},
        "us.wtpPct":   {"note": "65% -- ACR guideline 2L after TNF biosim; commercial + Medicare Part D; PA with TNF step; copay card $5 commercial."},
        "us.priceK":   {"note": "Rinvoq RA WAC $70K/yr; net ~$65K after ~25% PBM rebates; oral convenience vs SC biologic drives premium vs TNF biosim $8-18K."},
        "eu.reachPct": {"note": "6% of 2M EU mod-severe RA -- NICE TA665 + G-BA reimbursed post-TNF; EMA 2023 cardiovascular warning restricted elderly."},
        "eu.wtpPct":   {"note": "50% -- post-TNF biosim step-therapy; EMA PRAC risk minimization gated elderly/smokers; ASMR IV."},
        "eu.priceK":   {"note": "$35K EU net -- UK NHS ~GBP 900/mo, Germany AMNOG ~EUR 1.5K/mo; ~50% of US list."},
        "row.reachPct":{"note": "2% of 10M ROW RA -- Japan NHI covered, China NRDL 2021; TNF biosim dominant EM."},
        "row.wtpPct":  {"note": "12% -- Japan NHI 30% copay, China NRDL listed, AU PBS; EM biosimilar anti-TNF."},
        "row.priceK":  {"note": "$15K blended -- Japan NHI ~$25K, China NRDL ~$12K, EM AbbVie access."}
    },
    ("ABBV", "rinvoq", "ad"): {
        "us.reachPct": {"note": "Rinvoq AD ~12% of ~800K mod-severe AD -- fastest-growing AD indication; oral convenience vs Dupixent SC q2wk, 1.5B 2025."},
        "us.wtpPct":   {"note": "60% -- step-therapy after Dupixent typical; commercial + Medicare Part D; FDA black box limits expansion; copay $5."},
        "us.priceK":   {"note": "Rinvoq AD WAC $75K (higher 30mg dose); net ~$55K after rebates; priced at Dupixent parity."},
        "eu.reachPct": {"note": "8% of ~1M EU mod-severe AD -- NICE TA814 + G-BA recommended post-Dupixent; EMA CV warning gates elderly."},
        "eu.wtpPct":   {"note": "45% -- HTA step-therapy Dupixent first; G-BA added benefit not proven; France ASMR IV."},
        "eu.priceK":   {"note": "$30K EU net -- UK NHS ~GBP 750/mo, Germany ~EUR 1.3K/mo post-negotiation."},
        "row.reachPct":{"note": "3% of 15M ROW AD -- Japan PMDA + NHI, China NRDL; EM minimal advanced tx."},
        "row.wtpPct":  {"note": "10% -- Japan NHI 30% copay, China NRDL listed 2023."},
        "row.priceK":  {"note": "$12K blended -- Japan NHI ~$20K, China NRDL ~$10K, EM access program."}
    },
    ("ABBV", "rinvoq", "uc_rinvoq"): {
        "us.reachPct": {"note": "Rinvoq UC ~10% of 400K US mod-severe UC on advanced tx -- approved 2022; growing post-TNF; $1B UC 2025."},
        "us.wtpPct":   {"note": "55% -- AGA pathway 2L post-TNF; commercial + Medicare Part D; PA required; FDA black box limits first-line."},
        "us.priceK":   {"note": "Rinvoq UC WAC $90K/yr (45mg induction + 15-30mg maint); net ~$65K; priced similar to Skyrizi UC."},
        "eu.reachPct": {"note": "7% of 600K EU mod-severe UC advanced tx -- EMA 2022; NICE TA856 reimbursed post-TNF; G-BA added benefit moderate."},
        "eu.wtpPct":   {"note": "42% -- step-therapy post-TNF biosim; HTA strict UC gating; ASMR IV France."},
        "eu.priceK":   {"note": "$35K EU net -- UK/Germany ~55% US list post-induction/maintenance pricing."},
        "row.reachPct":{"note": "2% of 3M ROW UC -- Japan NHI 2023 UC label, China NRDL pending."},
        "row.wtpPct":  {"note": "10% -- Japan NHI covered 30% copay; rest patchy."},
        "row.priceK":  {"note": "$12K blended -- Japan higher dose NHI ~$22K."}
    },
    ("ABBV", "rinvoq", "crohns_rinvoq"): {
        "us.reachPct": {"note": "Rinvoq CD approved May 2023; 8% of 400K US mod-severe CD advanced tx -- rapid uptake, $900M 2025."},
        "us.wtpPct":   {"note": "55% -- AGA pathway 2L post-TNF; commercial + Medicare Part D; oral advantage vs Skyrizi IV induction."},
        "us.priceK":   {"note": "Rinvoq CD WAC $90K/yr; net ~$65K after rebates; same dose schedule as UC (45/15-30mg)."},
        "eu.reachPct": {"note": "5% of 500K EU mod-severe CD -- EMA 2024 CD; NICE/G-BA reviewing; slower launch than UC."},
        "eu.wtpPct":   {"note": "42% -- post-TNF + Stelara step; HTA CD pathway strict."},
        "eu.priceK":   {"note": "$35K EU net -- aligned w/ Rinvoq UC pricing post-HTA."},
        "row.reachPct":{"note": "2% of 2M ROW CD -- Japan NHI 2024, China NRDL pending."},
        "row.wtpPct":  {"note": "10% -- Japan 30% copay, rest limited access."},
        "row.priceK":  {"note": "$12K blended -- Japan NHI ~$22K, EM access program."}
    },
    ("ABBV", "humira", "ra_humira"): {
        "us.reachPct": {"note": "Humira RA 5% residual -- Amjevita/Cyltezo/Hyrimoz biosim 60% share 2025; loyal AbbVie Patient Access Card pts remain; $3B total 2025."},
        "us.wtpPct":   {"note": "40% -- PBM exclusion policies 2024-25 migrated most to biosim; remaining access tier 3 formulary or patient preference."},
        "us.priceK":   {"note": "Humira WAC $88K/yr unchanged but net ~$55K after 35-40% PBM rebates + Humira Complete copay card $5."},
        "eu.reachPct": {"note": "3% of EU RA -- adalimumab biosim since 2018 dominates ~80%; Humira brand residual NHS/SHI trust."},
        "eu.wtpPct":   {"note": "30% -- biosim tender policies in Denmark/Germany/UK force switches; Humira brand carved out for switch-refusers only."},
        "eu.priceK":   {"note": "$25K EU net -- biosim tender ~GBP 1-3K/yr; Humira brand premium ~EUR 8-15K for retained pts."},
        "row.reachPct":{"note": "2% of 10M ROW RA -- AbbVie brand retained Japan + select APAC; China NRDL adalim biosim ~90% share."},
        "row.wtpPct":  {"note": "10% -- Japan NHI brand retained, EM biosim domestically produced."},
        "row.priceK":  {"note": "$10K blended -- Japan NHI brand ~$18K, rest biosim or EM access."}
    },
    ("ABBV", "humira", "ibd_humira"): {
        "us.reachPct": {"note": "Humira IBD 5% residual -- biosim adalim ~55% share 2025 post PBM exclusions; loyal IBD pts on Patient Access remain."},
        "us.wtpPct":   {"note": "35% -- IBD PBM exclusion slower than RA due to clinical switching concerns; some remaining commercial coverage."},
        "us.priceK":   {"note": "Humira IBD higher-dose WAC $110K/yr; net ~$55K after rebates."},
        "eu.reachPct": {"note": "3% of EU IBD -- biosim adalim >80% share since 2018 ESPEN guidance; Humira brand very small residual."},
        "eu.wtpPct":   {"note": "28% -- tender policies force biosim; UK/Germany IBD slightly more switch-resistant than RA."},
        "eu.priceK":   {"note": "$25K EU net -- brand retained price for switch-refusers ~EUR 10-18K IBD dose."},
        "row.reachPct":{"note": "1% of 8M ROW IBD -- Japan retains brand, EM biosim."},
        "row.wtpPct":  {"note": "8% -- Japan NHI brand only, EM biosim."},
        "row.priceK":  {"note": "$10K blended -- Japan IBD dose ~$20K, rest biosim."}
    },
    ("ABBV", "humira", "pso_humira"): {
        "us.reachPct": {"note": "Humira pso 3% residual -- biosim + IL-23/IL-17 dominate; Skyrizi cannibalized most AbbVie loyal pts; minimal new starts."},
        "us.wtpPct":   {"note": "30% -- formulary excluded for new starts on most PBMs; remaining access for continued therapy."},
        "us.priceK":   {"note": "Humira pso WAC $88K unchanged; net ~$55K after PBM rebate; Patient Access Card $5 commercial."},
        "eu.reachPct": {"note": "2% of EU pso -- biosim adalim 80%+ share; IL-23/IL-17 for advanced; brand Humira negligible."},
        "eu.wtpPct":   {"note": "25% -- biosim tender dominant; brand only for switch-refusers."},
        "eu.priceK":   {"note": "$25K EU net -- brand residual ~EUR 10-15K for retained pts."},
        "row.reachPct":{"note": "1% of 15M ROW pso -- Japan brand retained, EM biosim."},
        "row.wtpPct":  {"note": "8% -- Japan NHI brand, EM biosim adalim domestic."},
        "row.priceK":  {"note": "$10K blended -- Japan ~$18K, rest biosim/EM access."}
    },
    ("ABBV", "vraylar", "schizo_vraylar"): {
        "us.reachPct": {"note": "Vraylar schizophrenia ~15% of ~1.3M schizo on branded antipsychotics; D3-preferring partial agonist differentiates vs generics."},
        "us.wtpPct":   {"note": "60% -- Medicare Part D + Medicaid broad; commercial PA after 1-2 generic failures; long-acting branded niche."},
        "us.priceK":   {"note": "Vraylar WAC $18K/yr; net ~$28K includes bipolar/MDD blended; Medicaid ~50%+ of Rx, aggressive rebates."},
        "eu.reachPct": {"note": "10% EU schizo branded -- Recordati co-promote partner; slower uptake vs US; generic risperidone/olanzapine dominant."},
        "eu.wtpPct":   {"note": "45% -- NICE/G-BA reimbursed but tier 2 vs generics; ASMR V France."},
        "eu.priceK":   {"note": "$14K EU net -- ~50% of US list, generic competition caps."},
        "row.reachPct":{"note": "3% of 20M ROW schizo -- Japan PMDA + NHI 2022; China NRDL pending; EM risperidone generic dominant."},
        "row.wtpPct":  {"note": "10% -- Japan NHI covered 30% copay, rest generic antipsychotic."},
        "row.priceK":  {"note": "$6K blended -- Japan NHI ~$12K, rest generic."}
    },
    ("ABBV", "vraylar", "bipolar_vraylar"): {
        "us.reachPct": {"note": "Vraylar bipolar ~10% of 1.5M bipolar on branded; approved both manic + depressive episodes + maintenance; $1.2B 2025."},
        "us.wtpPct":   {"note": "55% -- Medicare/Medicaid + commercial post 1-2 generic failures; only AP approved for all 3 bipolar phases."},
        "us.priceK":   {"note": "Same WAC $18K/yr across indications; net ~$28K blended; bipolar 40% of Vraylar script volume."},
        "eu.reachPct": {"note": "7% EU bipolar branded -- Recordati partnered; generic lithium/quetiapine baseline."},
        "eu.wtpPct":   {"note": "40% -- NICE/G-BA recommended bipolar I manic/depressive; step-therapy post-generic."},
        "eu.priceK":   {"note": "$14K EU net -- consistent Vraylar EU pricing."},
        "row.reachPct":{"note": "2% of 10M ROW bipolar -- Japan PMDA, EM generic."},
        "row.wtpPct":  {"note": "8% -- Japan NHI, rest generic quetiapine/lithium."},
        "row.priceK":  {"note": "$6K blended -- Japan ~$12K NHI."}
    },
    ("ABBV", "vraylar", "mdd_adj_vraylar"): {
        "us.reachPct": {"note": "Vraylar MDD adjunctive approved Dec 2022; 3% of 20M US MDD inadequate responders -- massive TAM but niche AP add-on."},
        "us.wtpPct":   {"note": "50% -- Medicare/Medicaid coverage with adjunctive label; commercial PA strict; competing Rexulti/aripiprazole generic."},
        "us.priceK":   {"note": "Same Vraylar WAC $18K/yr; net ~$28K; MDD adj highest copay sensitivity -- cash-pay hurdle."},
        "eu.reachPct": {"note": "2% EU MDD -- no EU adjunctive MDD filing; off-label minimal."},
        "eu.wtpPct":   {"note": "35% -- EMA adjunctive MDD not approved; off-label restricted."},
        "eu.priceK":   {"note": "$14K EU net -- pricing assumed parallel to schizo/bipolar."},
        "row.reachPct":{"note": "0.5% ROW -- limited MDD adj approvals outside US."},
        "row.wtpPct":  {"note": "8% -- minimal ex-US MDD adj use."},
        "row.priceK":  {"note": "$6K blended -- niche off-label use."}
    },
    ("ABBV", "botox_neuro", "migraine"): {
        "us.reachPct": {"note": "Botox chronic migraine ~12% of ~4M CM pts on preventive -- $3.5B Botox therapeutic 2025 (migraine ~70%); q12wk injection."},
        "us.wtpPct":   {"note": "55% -- PREEMPT trials + FDA approval 2010; Medicare Part B + commercial after 2+ oral failures; CGRP competition (Qulipta/Ajovy)."},
        "us.priceK":   {"note": "Botox 155-195U dose @ $700/100U WAC = ~$18K/yr per pt (4 cycles); net after hospital/physician rebates."},
        "eu.reachPct": {"note": "8% of 5M EU CM -- NICE TA260 recommended chronic migraine post 3 oral failures; NHS neurology gatekeeping."},
        "eu.wtpPct":   {"note": "40% -- NICE/G-BA CM recommended but strict step therapy; ASMR IV; CGRP mAbs eating share."},
        "eu.priceK":   {"note": "$10K EU net -- UK NHS ~GBP 350/cycle, Germany ~EUR 500/cycle; ~55% of US list."},
        "row.reachPct":{"note": "3% of 30M ROW CM -- Japan NHI covered 2018, China NRDL pending for neurology label."},
        "row.wtpPct":  {"note": "10% -- Japan NHI 30% copay, EM access limited."},
        "row.priceK":  {"note": "$4K blended -- Japan ~$10K NHI, EM via Allergan access."}
    },
    ("ABBV", "qulipta", "mig_prev"): {
        "us.reachPct": {"note": "Qulipta ~8% of ~10M US migraine preventive -- oral CGRP, $1.2B 2025; vs Nurtec/Ubrelvy oral + Ajovy/Aimovig SC."},
        "us.wtpPct":   {"note": "50% -- first oral CGRP preventive; commercial + Medicare Part D post 1-2 older orals; copay $0 card."},
        "us.priceK":   {"note": "Qulipta WAC $13K/yr oral; net ~$12K after rebates; oral convenience vs SC CGRP $7K list."},
        "eu.reachPct": {"note": "4% of 15M EU migraine prev -- EMA 2023; NICE TA859 EU rollout behind US."},
        "eu.wtpPct":   {"note": "35% -- NICE + G-BA recommended post-2 oral failures; CGRP mAb SC competition."},
        "eu.priceK":   {"note": "$6K EU net -- ~50% of US list; oral CGRP tier similar to SC CGRP."},
        "row.reachPct":{"note": "1% of 50M ROW migraine prev -- Japan PMDA 2024, EM minimal."},
        "row.wtpPct":  {"note": "8% -- Japan NHI covered, rest limited."},
        "row.priceK":  {"note": "$3K blended -- Japan ~$5K NHI."}
    },
    ("ABBV", "imbruvica", "cll"): {
        "us.reachPct": {"note": "Imbruvica 12% of ~200K US CLL/MCL/WM -- declining fast vs Brukinsa (BeOne) + Calquence (AZ) on superior selectivity/AF profile."},
        "us.wtpPct":   {"note": "55% -- Medicare Part D + commercial; NCCN Cat 1 CLL but Brukinsa head-to-head ALPINE superiority shifting preference."},
        "us.priceK":   {"note": "Imbruvica WAC $220K/yr; net ~$200K; Medicare Part D oral onc + J&J co-promote share."},
        "eu.reachPct": {"note": "8% EU CLL/MCL -- NICE TA429 + G-BA reimbursed but Brukinsa/Calquence taking 1L share on tolerability."},
        "eu.wtpPct":   {"note": "45% -- HTA reimbursed but newer BTKi preferred; step-therapy changes 2024-25."},
        "eu.priceK":   {"note": "$120K EU net -- UK NHS ~GBP 4K/mo, Germany AMNOG ~EUR 5.5K/mo; ~55% of US list."},
        "row.reachPct":{"note": "3% of 400K ROW CLL -- Japan NHI + China NRDL; competition from Brukinsa heavy in China."},
        "row.wtpPct":  {"note": "10% -- Japan NHI 30% copay, China NRDL discount."},
        "row.priceK":  {"note": "$45K blended -- Japan ~$80K NHI, China NRDL ~$30K."}
    },
    ("ABBV", "venclexta", "cll_ven"): {
        "us.reachPct": {"note": "Venclexta CLL 25% US -- fixed-duration Ven+Obinutuzumab 1L + Ven+R 2L; BCL2i class leader, MURANO + CLL14 data."},
        "us.wtpPct":   {"note": "60% -- NCCN Cat 1 CLL 1L/2L; Medicare Part D + commercial broad; Roche co-promote (Genentech share)."},
        "us.priceK":   {"note": "Venclexta WAC $18K/mo x 12mo fixed = ~$220K cycle; blended $180K w/ tumor lysis syndrome ramp + retreatment."},
        "eu.reachPct": {"note": "18% EU CLL -- NICE TA487 1L CLL14 combo; G-BA added benefit proven; fixed duration attractive to HTAs."},
        "eu.wtpPct":   {"note": "48% -- NICE/G-BA recommended; fixed 12-24mo duration cost-effective vs chronic BTKi."},
        "eu.priceK":   {"note": "$110K EU net -- UK/Germany ~60% of US; fixed-duration total cost favorable for HTA."},
        "row.reachPct":{"note": "5% of 400K ROW CLL -- Japan NHI + China NRDL 2021; AU PBS."},
        "row.wtpPct":  {"note": "12% -- Japan NHI 30% copay, China NRDL post-negotiation."},
        "row.priceK":  {"note": "$50K blended -- Japan ~$90K, China NRDL ~$40K."}
    },
    ("ABBV", "venclexta", "aml_ven"): {
        "us.reachPct": {"note": "Venclexta AML 45% of ~20K US unfit AML pts -- Ven+aza 1L unfit AML standard of care; VIALE-A trial; $1B AML 2025."},
        "us.wtpPct":   {"note": "65% -- NCCN Cat 1 unfit AML; Medicare Part D + Part B (aza IV component); elderly AML standard."},
        "us.priceK":   {"note": "Venclexta AML WAC ~$20K/mo induction; blended $150K/yr w/ azacitidine $10K; total regimen ~$200K/yr."},
        "eu.reachPct": {"note": "35% EU unfit AML -- NICE TA765 + G-BA proven added benefit vs aza alone; first targeted AML option."},
        "eu.wtpPct":   {"note": "52% -- HTA reimbursed; hematology unfit-AML standard of care; ASMR III France."},
        "eu.priceK":   {"note": "$90K EU net -- UK/Germany ~55% of US; shorter AML duration (~6mo median) limits total cost."},
        "row.reachPct":{"note": "8% of 40K ROW unfit AML -- Japan NHI + China NRDL 2022."},
        "row.wtpPct":  {"note": "15% -- Japan NHI 30% copay, China NRDL listed."},
        "row.priceK":  {"note": "$35K blended -- Japan ~$60K, China NRDL ~$25K."}
    },
    ("ABBV", "elahere", "ovarian"): {
        "us.reachPct": {"note": "Elahere 22% of FRa+ platinum-resistant ovarian (~4K US pts/yr) -- ImmunoGen acq; MIRASOL confirmatory 2023; niche ADC."},
        "us.wtpPct":   {"note": "55% -- FDA accelerated 2022, full 2024; NCCN Cat 1 FRa+ PROC; Medicare Part B IV q3wk; FRa IHC required."},
        "us.priceK":   {"note": "Elahere WAC $20K/cycle q3wk = ~$220K/yr; net ~$200K; companion diagnostic Ventana FOLR1 RxDx."},
        "eu.reachPct": {"note": "14% EU FRa+ PROC -- EMA 2024 approval; NICE TA reviewing; G-BA added benefit pending MIRASOL."},
        "eu.wtpPct":   {"note": "40% -- HTA recommended PROC FRa+ specialty; companion Dx infrastructure ramping."},
        "eu.priceK":   {"note": "$120K EU net -- UK/Germany ~55% of US post-HTA; ADC pricing anchored to Enhertu."},
        "row.reachPct":{"note": "3% of 50K ROW PROC -- Japan NHI 2024, China NMPA pending; FRa IHC centers limited."},
        "row.wtpPct":  {"note": "10% -- Japan NHI covered, rest narrow specialty access."},
        "row.priceK":  {"note": "$45K blended -- Japan NHI ~$90K, EM access program."}
    },
    ("ABBV", "botox_cosm", "wrinkles"): {
        "us.reachPct": {"note": "Botox Cosmetic 55% of ~6M US aesthetic neurotox pts -- market leader ~70% share vs Dysport/Xeomin/Daxxify; Allure brand."},
        "us.wtpPct":   {"note": "90% -- pure cash-pay aesthetic; Allergan Alle loyalty program drives repeat 3-4x/yr; commercial insurance excluded."},
        "us.priceK":   {"note": "Botox Cosmetic ~$400-600/session at 3-4 sessions/yr = $1.2-2K/yr; provider-priced, no WAC list for aesthetic."},
        "eu.reachPct": {"note": "40% EU aesthetic neurotox ~3M pts -- slower adoption than US, Dysport (Ipsen) stronger share."},
        "eu.wtpPct":   {"note": "80% -- cash-pay aesthetic Europe; UK/France strongest markets; tax advantages for med-spa sector."},
        "eu.priceK":   {"note": "$700/yr EU blended -- UK GBP 150-300/session, France EUR 300-500; less frequent sessions."},
        "row.reachPct":{"note": "25% of ~50M ROW aesthetic -- Korea/Japan/China huge markets; domestic neurotox competition (Hugel, Daewoong) in Korea."},
        "row.wtpPct":  {"note": "60% -- cash-pay APAC middle class; China gray market risk; Korea domestic brands low-cost."},
        "row.priceK":  {"note": "$300/yr blended -- Korea/China lower per-session $150-250; emerging markets discount pricing."}
    },
    ("ABBV", "juvederm", "fillers"): {
        "us.reachPct": {"note": "Juvederm 45% of ~3M US dermal filler pts -- HA filler market leader ~60% share vs Restylane/RHA; Allergan portfolio."},
        "us.wtpPct":   {"note": "85% -- pure cash-pay; Alle loyalty program drives repeat; commercial insurance excluded; longer lasting (2yr) value prop."},
        "us.priceK":   {"note": "Juvederm ~$600-800/syringe provider-priced; avg 2 syringes/pt/yr = ~$1.2K."},
        "eu.reachPct": {"note": "35% EU HA filler -- Galderma Restylane strong competitor; Teoxane RHA growing; less injection volume than US."},
        "eu.wtpPct":   {"note": "75% -- cash-pay aesthetic; UK/France/Italy strongest markets; stricter med-spa regulation."},
        "eu.priceK":   {"note": "$800/yr EU blended -- EUR 300-500/syringe typical, 1-2 syringes/yr."},
        "row.reachPct":{"note": "18% of ~30M ROW filler pts -- Korea/China HA filler leaders; domestic competition (Medytox, LG Chem)."},
        "row.wtpPct":  {"note": "55% -- APAC cash-pay growing; China gray market, Korea low-cost domestic HA fillers."},
        "row.priceK":  {"note": "$400/yr blended -- Korea/China ~$200/syringe domestic competition."}
    },
    ("ABBV", "emraclidine", "schizo_new"): {
        "us.reachPct": {"note": "Emraclidine (Cerevel acq $8.7B) Phase 3 schizo; 8% -- muscarinic M4 class novel MOA vs D2 APs; EMPOWER Ph3 failed Nov 2024, pipeline risk."},
        "us.wtpPct":   {"note": "40% -- pre-approval estimate; if Ph3 succeeds, Medicare Part D + commercial step post-generic AP; Cobenfy (BMS) competition."},
        "us.priceK":   {"note": "Projected WAC ~$28K/yr -- muscarinic class premium anchored to Cobenfy $22K list."},
        "eu.reachPct": {"note": "5% EU schizo -- EMA filing post-Ph3 success; generic AP dominant baseline."},
        "eu.wtpPct":   {"note": "30% -- HTA novel MOA uncertain; step-therapy post-generic strict."},
        "eu.priceK":   {"note": "$13K EU net -- ~50% of US list projected."},
        "row.reachPct":{"note": "2% of 20M ROW schizo -- Japan PMDA pathway pending Ph3."},
        "row.wtpPct":  {"note": "8% -- Japan NHI if approved, rest generic AP."},
        "row.priceK":  {"note": "$5K blended -- Japan projected, EM generic."}
    },
    ("ABBV", "abbv400", "nsclc"): {
        "us.reachPct": {"note": "ABBV-400 c-Met ADC Phase 2/3 NSCLC; 20% of c-Met overexpressing NSCLC (~15% of NSCLC); targets post-osimertinib EGFR + c-Met high."},
        "us.wtpPct":   {"note": "45% -- pre-approval; competing vs Tepotinib/Capmatinib c-Met TKIs + Enhertu HER2+; payor tier specialty."},
        "us.priceK":   {"note": "Projected WAC ~$220K/yr -- ADC pricing anchored to Enhertu/Trodelvy NSCLC class."},
        "eu.reachPct": {"note": "12% EU c-Met NSCLC -- EMA post-Ph3; companion Dx IHC gating."},
        "eu.wtpPct":   {"note": "35% -- HTA reimburse targeted ADCs but strict c-Met+ gating; ASMR uncertain."},
        "eu.priceK":   {"note": "$110K EU net -- ~50% of US list projected ADC pricing."},
        "row.reachPct":{"note": "3% of 500K ROW c-Met NSCLC -- Japan NHI pathway + China NMPA."},
        "row.wtpPct":  {"note": "8% -- Japan NHI, limited rest."},
        "row.priceK":  {"note": "$45K blended -- Japan ~$80K projected, EM access."}
    },

    # ============================== GILD ==============================
    ("GILD", "len_prev", "hiv_prev"): {
        "us.reachPct": {"note": "Lenacapavir PrEP (Yeztugo approved Jun 2025) ~8% of 350K US PrEP pts; twice-yearly SC injection differentiator vs Descovy oral daily."},
        "us.wtpPct":   {"note": "55% -- CDC PrEP guidelines updated 2025; Medicaid + commercial coverage ramping; Ready, Set, PrEP free program; HHS CED monitoring."},
        "us.priceK":   {"note": "Yeztugo PrEP WAC $28K/yr (2 doses) per GILD launch; net ~$28K; Gilead Advancing Access PAP for uninsured."},
        "eu.reachPct": {"note": "4% of ~200K EU PrEP -- EMA Nov 2024 approval; NICE TA pending; slow rollout vs generic TDF/FTC PrEP."},
        "eu.wtpPct":   {"note": "30% -- HTA value vs generic TDF/FTC ~EUR 60/mo challenging; UK NHS PrEP program generic baseline."},
        "eu.priceK":   {"note": "$18K EU net -- ~65% of US list, HTA demands price cut vs generic oral PrEP baseline."},
        "row.reachPct":{"note": "1% of global PrEP -- GILD voluntary license to generics 6 LMIC mfrs Oct 2024; branded access concentrated Japan/AU."},
        "row.wtpPct":  {"note": "8% -- Japan PMDA pending, AU PBS; LMIC served via generics ~$40/yr post-ViiV/GILD license."},
        "row.priceK":  {"note": "$6K blended -- branded Japan/AU ~$15K, LMIC generic $40-100; Global Fund access."}
    },
    ("GILD", "trodelvy", "onc_bc"): {
        "us.reachPct": {"note": "Trodelvy 22% of ~30K US 2L+ mTNBC + HR+ post-CDK4/6 -- ASCENT + TROPiCS-02; ADC pricing competitive vs Enhertu."},
        "us.wtpPct":   {"note": "55% -- NCCN Cat 1 2L mTNBC + 3L+ HR+; Medicare Part B IV + commercial; no biomarker req."},
        "us.priceK":   {"note": "Trodelvy WAC $18K/cycle q3wk + D8 = ~$220K/yr; net ~$200K after 340B + GPO discounts."},
        "eu.reachPct": {"note": "14% EU mTNBC -- NICE TA819 + G-BA added benefit proven; slower HR+ rollout pending TROPiCS-02 HTA."},
        "eu.wtpPct":   {"note": "40% -- NICE/G-BA reimbursed TNBC; HR+ label pending HTA; ASMR III."},
        "eu.priceK":   {"note": "$130K EU net -- UK/Germany ~60% of US ADC list post-HTA."},
        "row.reachPct":{"note": "3% of 100K ROW mTNBC -- Japan NHI 2022, China NMPA 2022 + NRDL 2023."},
        "row.wtpPct":  {"note": "10% -- Japan NHI 30% copay, China NRDL ~70% discount."},
        "row.priceK":  {"note": "$55K blended -- Japan NHI ~$110K, China NRDL ~$40K."}
    },
    ("GILD", "anito_cel", "mm_cart"): {
        "us.reachPct": {"note": "Anito-cel (BCMA CAR-T, Arcellx collab) Phase 2 iMMagine-1; 8% of ~10K US 3L+ MM CAR-T eligible; vs Abecma/Carvykti."},
        "us.wtpPct":   {"note": "45% -- pre-approval; NCCN 4L+ MM post-BCMA/CELMoD/anti-CD38; commercial + Medicare Part B hospital-administered."},
        "us.priceK":   {"note": "Projected WAC ~$475K single-dose infusion + hospitalization + bridging chemo = ~$700K total cost of care."},
        "eu.reachPct": {"note": "5% EU 3L+ MM -- EMA post-Ph3 2027+; NICE/G-BA gating specialty CAR-T centers."},
        "eu.wtpPct":   {"note": "28% -- HTA gating CAR-T strict; managed-entry/outcomes agreements typical."},
        "eu.priceK":   {"note": "$350K EU net -- ~70% of US for CAR-T (narrower discount than biologics)."},
        "row.reachPct":{"note": "1% of 50K ROW 3L+ MM -- Japan NHI + AU PBS likely, CAR-T capacity limited."},
        "row.wtpPct":  {"note": "8% -- Japan NHI CAR-T reimbursed, EM negligible capacity."},
        "row.priceK":  {"note": "$180K blended -- Japan ~$350K NHI, rest limited."}
    },
    ("GILD", "liver", "liver_port"): {
        "us.reachPct": {"note": "Liver franchise 12% -- Livdelzi PBC (+Chemomab 2025), HCV legacy (Harvoni/Epclusa ~$1B), HBV (Vemlidy), Veklury COVID IV."},
        "us.wtpPct":   {"note": "60% -- PBC + HCV + HBV broad Medicare/commercial; Veklury hospital PHE; Seladelpar (Livdelzi) specialty access."},
        "us.priceK":   {"note": "Blended $75K -- Livdelzi WAC $76K PBC, HCV $80K 12wk cycle, Veklury ~$3.1K per 5-day course."},
        "eu.reachPct": {"note": "8% EU -- EMA HCV fully reimbursed (now niche), PBC Livdelzi pending HTA."},
        "eu.wtpPct":   {"note": "42% -- HCV mature + PBC Livdelzi NICE pending; HBV Vemlidy reimbursed broadly."},
        "eu.priceK":   {"note": "$45K EU net -- ~60% of US list HCV/PBC blended."},
        "row.reachPct":{"note": "2% ROW -- HCV generic widely available, Livdelzi rolling; China NRDL HCV."},
        "row.wtpPct":  {"note": "15% -- Japan NHI broad, China HCV NRDL, EM generic HCV."},
        "row.priceK":  {"note": "$18K blended -- Japan NHI higher, EM generic HCV ~$500."}
    },
    ("GILD", "biktarvy", "hiv_tx"): {
        "us.reachPct": {"note": "Biktarvy 45% of ~900K US HIV on ART -- market leader, $14.1B 2025; replacing older GILD regimens + Dovato (GSK) 2L."},
        "us.wtpPct":   {"note": "75% -- Medicare Part D + Medicaid + Ryan White + ADAP broad; DHHS guidelines first-line; commercial formulary tier 2."},
        "us.priceK":   {"note": "Biktarvy WAC $46K/yr; net ~$42K after 340B + Medicaid rebates + commercial rebates ~20%."},
        "eu.reachPct": {"note": "25% EU ~700K HIV on ART -- EMA 2018; NICE TA539 + G-BA broad reimbursement; Dovato/ViiV competition."},
        "eu.wtpPct":   {"note": "48% -- NICE + G-BA recommended first-line; ASMR IV; HTA negotiated discounts ~30-40% off list."},
        "eu.priceK":   {"note": "$25K EU net -- UK NHS ~GBP 9K/yr, Germany AMNOG ~EUR 11K/yr; ~55% of US list."},
        "row.reachPct":{"note": "8% of 20M ROW HIV -- generic TLD PEPFAR/Global Fund dominates LMIC; Japan/AU Biktarvy branded."},
        "row.wtpPct":  {"note": "18% -- Japan NHI covered, AU PBS; LMIC generic TLD ~$60/yr via MPP/ViiV licenses."},
        "row.priceK":  {"note": "$10K blended -- Japan NHI ~$25K, AU ~$15K, LMIC generic substitute."}
    },
    ("GILD", "descovy", "hiv_prep"): {
        "us.reachPct": {"note": "Descovy PrEP 25% of 350K US PrEP -- DISCOVER trial; taking share from generic Truvada TDF/FTC ($0 copay generic pressure)."},
        "us.wtpPct":   {"note": "60% -- CDC guidelines recommended; Medicaid + commercial broad; Ready, Set, PrEP free uninsured; USPSTF A-grade."},
        "us.priceK":   {"note": "Descovy WAC $25K/yr; net ~$25K after commercial rebates; vs generic Truvada $360/yr (90%+ discount)."},
        "eu.reachPct": {"note": "8% EU PrEP -- NICE TA reviewing; generic TDF/FTC dominates UK NHS PrEP (~10 EUR/mo)."},
        "eu.wtpPct":   {"note": "22% -- HTA prefers generic Truvada; Descovy restricted to specific indications (renal/bone concerns)."},
        "eu.priceK":   {"note": "$15K EU net -- ~60% of US list; limited branded PrEP given generic floor."},
        "row.reachPct":{"note": "1% ROW PrEP -- generic TDF/FTC dominates; Gilead brand Descovy limited to developed APAC."},
        "row.wtpPct":  {"note": "5% -- Japan NHI, rest generic TDF/FTC via GILD license."},
        "row.priceK":  {"note": "$6K blended -- Japan branded, rest generic ~$60/yr."}
    },

    # ============================== UCB ==============================
    ("UCB", "commercial", "bimzelx"): {
        "us.reachPct": {"note": "Bimzelx ~5% of 1.5M US mod-severe pso -- launched Oct 2023 post-3yr FDA delay; dual IL-17A/F mechanism; $1.5B 2025 global."},
        "us.wtpPct":   {"note": "45% -- commercial formulary ramping 2024-25; Medicare Part D; post-biologic step therapy; PASI 100 data drives adoption."},
        "us.priceK":   {"note": "Bimzelx WAC $76K/yr; net ~$70K; priced parity to Cosentyx/Taltz but superior PASI 100 head-to-head BE RADIANT/HEAD."},
        "eu.reachPct": {"note": "4% of 2.5M EU mod-severe pso -- EMA 2021 ahead of US; NICE TA723 + G-BA added benefit proven; HS + PsA + axSpA expand."},
        "eu.wtpPct":   {"note": "35% -- NICE/G-BA recommended; HS label differentiator; post-biologic step therapy; ASMR III-IV."},
        "eu.priceK":   {"note": "$40K EU net -- UK NHS ~GBP 1.2K/mo, Germany ~EUR 1.8K/mo post-AMNOG; ~55% of US list."},
        "row.reachPct":{"note": "0.8% of 15M ROW mod-severe pso -- Japan NHI 2022, China NMPA pending."},
        "row.wtpPct":  {"note": "10% -- Japan NHI 30% copay, rest limited launch."},
        "row.priceK":  {"note": "$16K blended -- Japan NHI ~$28K, EM UCB access."}
    },
    ("UCB", "neuro_rare", "neuro_port"): {
        "us.reachPct": {"note": "Neuro rare portfolio 30% -- Fintepla Dravet/LGS (Zogenix acq), Rystiggo gMG (2023), Zilbrysq gMG (2023); orphan disease concentration."},
        "us.wtpPct":   {"note": "55% -- Medicare + commercial broad for ultra-rare; Dravet/LGS specialty pharmacy; gMG IVIG alternative."},
        "us.priceK":   {"note": "Blended $180K -- Fintepla WAC $96K, Rystiggo $325K, Zilbrysq $540K; ultra-rare pricing across."},
        "eu.reachPct": {"note": "20% EU -- EMA Fintepla 2020, Rystiggo 2024, Zilbrysq 2024; NICE/G-BA orphan drug reimbursement."},
        "eu.wtpPct":   {"note": "40% -- NICE/G-BA orphan recommended; specialist center access; ASMR III rare disease."},
        "eu.priceK":   {"note": "$110K EU net -- ~60% of US ultra-rare pricing post-HTA."},
        "row.reachPct":{"note": "3% ROW -- Japan PMDA + select markets; China NMPA pipeline."},
        "row.wtpPct":  {"note": "10% -- Japan NHI rare disease reimbursed, rest minimal."},
        "row.priceK":  {"note": "$40K blended -- Japan NHI ~$80K rare, rest UCB access."}
    },
    ("UCB", "evenity", "osteo"): {
        "us.reachPct": {"note": "Evenity ~3% of 10M US severe osteoporosis -- Amgen co-promote; 12-month max duration limits reach; 2nd-line after Prolia/teriparatide."},
        "us.wtpPct":   {"note": "45% -- Medicare Part B + commercial for severe fracture-risk; CV black box warning restricts; UCB/Amgen share US."},
        "us.priceK":   {"note": "Evenity WAC $22K for 12mo total course (2 SC doses/mo); net ~$22K; finite course vs chronic osteo meds."},
        "eu.reachPct": {"note": "2% of 30M EU osteo -- NICE TA791 + G-BA recommended severe fracture risk; Amgen EU partnership."},
        "eu.wtpPct":   {"note": "32% -- NICE/G-BA severe OP post-fracture; CV risk gating; generic bisphosphonate baseline."},
        "eu.priceK":   {"note": "$13K EU net -- UK/Germany ~55% of US for 12mo course."},
        "row.reachPct":{"note": "0.3% of 100M ROW OP -- Japan Amgen Astellas partnership; China NMPA 2023."},
        "row.wtpPct":  {"note": "8% -- Japan NHI covered, EM generic bisphosphonate dominant."},
        "row.priceK":  {"note": "$5K blended -- Japan NHI ~$18K, EM generic substitution."}
    },
    ("UCB", "cimzia", "ra_cd"): {
        "us.reachPct": {"note": "Cimzia 2% of US RA/CD/PsA biologic pts -- declining anti-TNF class; pegylated (no Fc) pregnancy-safe niche; $400M 2025."},
        "us.wtpPct":   {"note": "30% -- PBM biosimilar exclusions favor adalim biosim; Cimzia retained niche for pregnancy/breastfeeding + preference."},
        "us.priceK":   {"note": "Cimzia WAC $62K/yr; net ~$50K after rebates; price competitive w/ adalim biosim but brand loyalty limited."},
        "eu.reachPct": {"note": "1.2% EU RA/IBD/PsA -- NICE/G-BA reimbursed but biosim adalim dominant tender winner."},
        "eu.wtpPct":   {"note": "22% -- biosim tender displacement; Cimzia retained pregnancy-specific + switch-refuser access."},
        "eu.priceK":   {"note": "$28K EU net -- UK/Germany discounted to compete w/ biosim tenders."},
        "row.reachPct":{"note": "0.2% ROW -- Japan NHI + AU PBS, minimal EM launch."},
        "row.wtpPct":  {"note": "6% -- Japan NHI 30% copay, rest limited."},
        "row.priceK":  {"note": "$10K blended -- Japan NHI ~$20K, minimal rest."}
    },
    ("UCB", "vimpat", "epilepsy_leg"): {
        "us.reachPct": {"note": "Vimpat + Briviact 12% of ~2M US focal epilepsy; Vimpat generic lacosamide Mar 2022 erosion; Briviact branded retained."},
        "us.wtpPct":   {"note": "50% -- Medicare Part D + commercial; generic lacosamide cheap; Briviact branded for specific response/tolerability."},
        "us.priceK":   {"note": "Blended $18K -- Briviact WAC $12K/yr branded, Vimpat brand $13K residual, generic lacosamide ~$1K."},
        "eu.reachPct": {"note": "8% EU focal epilepsy -- generic lacosamide dominant post-2022; Briviact retained NICE/G-BA niche."},
        "eu.wtpPct":   {"note": "35% -- HTA generic preference; Briviact brand ~EUR 2K/yr post-AMNOG."},
        "eu.priceK":   {"note": "$10K EU net -- blended brand + generic; generic floor ~EUR 500."},
        "row.reachPct":{"note": "1% of 30M ROW epilepsy -- Japan NHI Vimpat/Briviact, EM generic lacosamide."},
        "row.wtpPct":  {"note": "8% -- Japan NHI covered, rest generic."},
        "row.priceK":  {"note": "$4K blended -- Japan NHI ~$8K, EM generic."}
    },
    ("UCB", "donzakimig", "epilepsy_new"): {
        "us.reachPct": {"note": "Donzakimig (Zilucoplan Phase?) UCB neuro pipeline; 4% projected in drug-resistant epilepsy; pre-approval."},
        "us.wtpPct":   {"note": "32% -- pre-approval; complement C5 MOA; payor tier uncertain."},
        "us.priceK":   {"note": "Projected WAC ~$25K/yr -- branded novel MOA premium."},
        "eu.reachPct": {"note": "3% EU drug-resistant epilepsy -- EMA post-Ph3."},
        "eu.wtpPct":   {"note": "22% -- HTA uncertain novel MOA."},
        "eu.priceK":   {"note": "$12K EU net projected."},
        "row.reachPct":{"note": "0.5% ROW -- Japan PMDA pathway pending."},
        "row.wtpPct":  {"note": "6% -- Japan NHI if approved."},
        "row.priceK":  {"note": "$4K blended projected."}
    },
    ("UCB", "dapirolizumab", "sle"): {
        "us.reachPct": {"note": "Dapirolizumab (anti-CD40L, Biogen partnership) Phase 3 SLE; 12% of ~160K US moderate-severe SLE -- positive Ph3 2024 PHOENYCS-GO."},
        "us.wtpPct":   {"note": "42% -- pre-approval; Benlysta + Saphnelo competition; lupus payor tier specialty post-antimalarial/steroid."},
        "us.priceK":   {"note": "Projected WAC ~$65K/yr -- SLE biologic class Saphnelo anchor $70K, Benlysta $40K."},
        "eu.reachPct": {"note": "8% EU SLE -- EMA post-Ph3; NICE/G-BA strict SLE reimbursement."},
        "eu.wtpPct":   {"note": "30% -- HTA SLE biologics post-standard-care step; ASMR uncertain."},
        "eu.priceK":   {"note": "$35K EU net projected -- ~55% of US."},
        "row.reachPct":{"note": "1% ROW SLE -- Japan NHI pathway, limited rest."},
        "row.wtpPct":  {"note": "8% -- Japan NHI projected."},
        "row.priceK":  {"note": "$14K blended projected."}
    },

    # ============================== ONC (BeOne) ==============================
    ("ONC", "commercial", "btk"): {
        "us.reachPct": {"note": "Brukinsa 22% of US CLL/MCL/WM BTKi market -- ALPINE head-to-head superiority vs Imbruvica drove 2024-25 share gains; $3.9B 2025 global."},
        "us.wtpPct":   {"note": "65% -- NCCN Cat 1 CLL/MCL/WM/MZL; Medicare Part D + commercial broad; superior AF/safety vs Imbruvica drives formulary wins."},
        "us.priceK":   {"note": "Brukinsa WAC $235K/yr; net ~$210K after Part D rebates + 340B; BeOne direct patient assistance."},
        "eu.reachPct": {"note": "15% of EU CLL/MCL BTKi -- EMA 2021; NICE TA814 + G-BA added benefit proven ALPINE; taking Imbruvica share."},
        "eu.wtpPct":   {"note": "48% -- NICE/G-BA recommended all indications; ASMR III CLL 1L; ALPINE superiority drives HTA."},
        "eu.priceK":   {"note": "$125K EU net -- UK NHS ~GBP 4K/mo, Germany AMNOG ~EUR 5.5K/mo; ~55% of US list."},
        "row.reachPct":{"note": "4% of 400K ROW CLL/MCL -- China NMPA + NRDL 2020 (BeiGene home market), Japan NHI 2022."},
        "row.wtpPct":  {"note": "12% -- China NRDL ~70% discount, Japan NHI 30% copay, AU PBS."},
        "row.priceK":  {"note": "$50K blended -- China NRDL ~$40K, Japan NHI ~$85K."}
    },
    ("ONC", "tevimbra", "pd1"): {
        "us.reachPct": {"note": "Tevimbra 12% -- FDA 2024 2L ESCC + 2025 1L gastric/ESCC; late entrant vs Keytruda dominance; niche biomarker positioning."},
        "us.wtpPct":   {"note": "60% -- NCCN listed GI tumors; Medicare Part B + commercial; tier 2 parity w/ Keytruda but PA step to Keytruda first."},
        "us.priceK":   {"note": "Tevimbra WAC $13K/cycle = ~$180K/yr; priced ~15% below Keytruda to drive formulary position."},
        "eu.reachPct": {"note": "8% EU -- EMA 2023 ESCC + 2024 NSCLC; NICE/G-BA added benefit limited vs Keytruda; ASMR V."},
        "eu.wtpPct":   {"note": "45% -- HTA reimburses but prefers Keytruda on head-to-head; Tevimbra secondary indication access."},
        "eu.priceK":   {"note": "$100K EU net -- UK/Germany ~55% of US list; discounted vs Keytruda for formulary access."},
        "row.reachPct":{"note": "8% of 2M ROW solid tumors -- China NMPA + NRDL 2019 flagship (BeOne home market), Novartis ex-China partnership."},
        "row.wtpPct":  {"note": "15% -- China NRDL major share, Japan NHI pending, EM PD-1 class limited."},
        "row.priceK":  {"note": "$40K blended -- China NRDL ~$15K/yr, Japan projected higher."}
    },
    ("ONC", "sonro", "bcl2"): {
        "us.reachPct": {"note": "Sonrotoclax Phase 3 CLL/NHL; 12% projected -- BCL2i class, differentiated selectivity/TLS profile vs Venclexta; filing 2026-27."},
        "us.wtpPct":   {"note": "45% -- pre-approval; if Ph3 superior to Ven, NCCN + Medicare Part D; fixed duration CLL anchor."},
        "us.priceK":   {"note": "Projected WAC ~$200K/yr -- parity to Venclexta $220K; fixed-duration total similar."},
        "eu.reachPct": {"note": "8% EU CLL -- EMA post-Ph3 2028+; NICE/G-BA fixed-duration BCL2i preferred vs chronic BTKi."},
        "eu.wtpPct":   {"note": "35% -- HTA reimbursement dependent on head-to-head vs Venclexta; ASMR TBD."},
        "eu.priceK":   {"note": "$110K EU net projected -- parity to Venclexta EU pricing."},
        "row.reachPct":{"note": "3% ROW -- China NMPA (BeOne home) + Japan NHI pathway post-Ph3."},
        "row.wtpPct":  {"note": "10% -- China NRDL projected, Japan NHI."},
        "row.priceK":  {"note": "$45K blended -- China NRDL ~$30K, Japan ~$75K projected."}
    },
    ("ONC", "btk_cdac", "btk_deg"): {
        "us.reachPct": {"note": "BGB-16673 BTK CDAC (degrader) Phase 1/2; 15% of BTKi-resistant post-covalent/non-covalent (~20K US pts); novel MOA niche."},
        "us.wtpPct":   {"note": "40% -- pre-approval; post-BTKi resistance major unmet need; specialty payor tier."},
        "us.priceK":   {"note": "Projected WAC ~$220K/yr -- BTKi-resistant premium pricing anchored to pirtobrutinib $230K."},
        "eu.reachPct": {"note": "10% EU BTKi-resistant -- EMA post-Ph3; NICE/G-BA niche subsegment."},
        "eu.wtpPct":   {"note": "32% -- HTA specialty CLL resistance; ASMR TBD."},
        "eu.priceK":   {"note": "$120K EU net projected."},
        "row.reachPct":{"note": "4% ROW -- China NMPA (BeOne flagship) + Japan pathway."},
        "row.wtpPct":  {"note": "10% -- China NRDL + Japan NHI projected."},
        "row.priceK":  {"note": "$50K blended -- China NRDL discount + Japan."}
    },
    ("ONC", "pipeline", "onc_pipe"): {
        "us.reachPct": {"note": "Broader pipeline 5% -- HCC (ociperlimab anti-TIGIT), gastric, solid tumors; early-stage, commercial uptake uncertain."},
        "us.wtpPct":   {"note": "35% -- pre-approval pipeline; checkpoint class combinations under payor scrutiny."},
        "us.priceK":   {"note": "Projected $180K/yr -- IO combination pricing anchored to checkpoint class."},
        "eu.reachPct": {"note": "3% EU -- EMA pathway 2028+; narrow indication rollout."},
        "eu.wtpPct":   {"note": "28% -- HTA combinations strict review."},
        "eu.priceK":   {"note": "$100K EU net projected."},
        "row.reachPct":{"note": "2% ROW -- China NMPA home market flagship for anti-TIGIT."},
        "row.wtpPct":  {"note": "8% -- China NRDL pathway."},
        "row.priceK":  {"note": "$35K blended -- China NRDL discount."}
    },

    # ============================== ALNY ==============================
    ("ALNY", "commercial", "ttr"): {
        "us.reachPct": {"note": "Amvuttra+Onpattro 30% -- post-HELIOS-B CM label Mar 2025 expanded to ATTR-CM ~150K US eligible; transitioning many from Onpattro IV to Amvuttra SC q3mo."},
        "us.wtpPct":   {"note": "70% -- Medicare Part B (Amvuttra SC in-office) + commercial; HELIOS-B all-cause mortality drove payor broadening 2025."},
        "us.priceK":   {"note": "Amvuttra WAC $476K/yr; Onpattro $450K; net ~$475K w/ outcomes-based contracts + Alnylam Patient Access."},
        "eu.reachPct": {"note": "22% EU ~100K ATTR-CM -- EMA Amvuttra CM label 2024; NICE TA868 + G-BA added benefit proven HELIOS-B."},
        "eu.wtpPct":   {"note": "55% -- NICE/G-BA recommended; ATTR hematology/cardiology centers; ASMR III."},
        "eu.priceK":   {"note": "$300K EU net -- UK NHS ~GBP 7.5K/mo, Germany ~EUR 10K/mo post-AMNOG; ~60% of US."},
        "row.reachPct":{"note": "8% of 400K ROW ATTR -- Japan NHI Amvuttra 2023, AU PBS, Brazil/LatAm via Alnylam access."},
        "row.wtpPct":  {"note": "18% -- Japan NHI 30% copay major share, AU PBS, EM access program."},
        "row.priceK":  {"note": "$120K blended -- Japan NHI ~$220K, AU ~$150K, EM tiered."}
    },
    ("ALNY", "nucresiran", "ttr_next"): {
        "us.reachPct": {"note": "Nucresiran (ALN-TTRsc04) Phase 3 TRITON-CM; 15% projected -- quarterly SC TTR silencing; filing 2027+; competing w/ Amvuttra itself."},
        "us.wtpPct":   {"note": "50% -- pre-approval; cannibalizes Amvuttra; Alnylam lifecycle management; payor tier specialty."},
        "us.priceK":   {"note": "Projected WAC ~$450K/yr -- parity to Amvuttra; less frequent dosing value prop."},
        "eu.reachPct": {"note": "10% EU ATTR -- EMA post-Ph3 2028+; transitions from Amvuttra."},
        "eu.wtpPct":   {"note": "38% -- HTA will require non-inferiority vs Amvuttra + convenience premium justification."},
        "eu.priceK":   {"note": "$280K EU net projected -- parity to Amvuttra EU."},
        "row.reachPct":{"note": "3% ROW -- Japan NHI + AU PBS pathway, EM via Alnylam."},
        "row.wtpPct":  {"note": "12% -- Japan NHI transition projected."},
        "row.priceK":  {"note": "$110K blended projected."}
    },
    ("ALNY", "zilebesiran", "htn"): {
        "us.reachPct": {"note": "Zilebesiran (Roche partnership) Ph2 KARDIA; 1.2% of massive hypertension TAM -- Ph2 positive but novel chronic HTN RNAi approach; launch 2028+."},
        "us.wtpPct":   {"note": "30% -- pre-approval; generic oral antihypertensives ubiquitous; HTA gating to resistant HTN likely."},
        "us.priceK":   {"note": "Projected WAC ~$8K/yr -- twice-yearly SC dosing; premium vs generic HTN meds but resistant subpopulation."},
        "eu.reachPct": {"note": "0.8% EU HTN -- EMA post-Ph3 2028+; HTA strict vs generics."},
        "eu.wtpPct":   {"note": "22% -- resistant HTN niche; generic oral baseline."},
        "eu.priceK":   {"note": "$4K EU net projected."},
        "row.reachPct":{"note": "0.3% of huge ROW HTN TAM -- Roche global rollout pending Ph3."},
        "row.wtpPct":  {"note": "8% -- Japan NHI pathway if approved, EM generic dominant."},
        "row.priceK":  {"note": "$2K blended projected."}
    },
    ("ALNY", "mivelsiran", "alz_rna"): {
        "us.reachPct": {"note": "Mivelsiran (ALN-APP) Phase 2 CAA/AD; 3% of ~2M early AD + CAA -- first RNAi for AD, APP silencing; early data 2025."},
        "us.wtpPct":   {"note": "20% -- pre-approval; anti-amyloid mAb class challenging; HTA CAA stroke niche more straightforward."},
        "us.priceK":   {"note": "Projected WAC ~$60K/yr -- priced at anti-amyloid class Leqembi $26.5K + RNAi premium."},
        "eu.reachPct": {"note": "2% EU -- EMA post-Ph3 2029+."},
        "eu.wtpPct":   {"note": "15% -- HTA pathway strict anti-amyloid post-Kisunla/Leqembi experience."},
        "eu.priceK":   {"note": "$35K EU net projected."},
        "row.reachPct":{"note": "0.5% ROW AD/CAA -- Japan NHI pathway projected."},
        "row.wtpPct":  {"note": "6% -- Japan NHI if approved, rest minimal."},
        "row.priceK":  {"note": "$15K blended projected."}
    },
    ("ALNY", "givlaari", "ahp"): {
        "us.reachPct": {"note": "Givlaari 51.5% of ~1K US AHP symptomatic pts -- ultra-rare, near ceiling penetration; monthly SC dosing limits some pts."},
        "us.wtpPct":   {"note": "72% -- Medicare Part B + commercial rare disease coverage; specialty distribution Alnylam; CED outcomes tracking."},
        "us.priceK":   {"note": "Givlaari WAC $575K/yr (monthly SC); net ~$500K after outcomes-based contracts + rebates."},
        "eu.reachPct": {"note": "37% of ~800 EU AHP -- NICE TA639 + G-BA orphan approved; ATU France; specialty porphyria centers."},
        "eu.wtpPct":   {"note": "55% -- NICE/G-BA orphan recommended; managed entry agreements typical."},
        "eu.priceK":   {"note": "$320K EU net -- UK/Germany ~55% of US ultra-rare pricing."},
        "row.reachPct":{"note": "10.3% of ~3K ROW AHP -- Japan NHI 2021, EM minimal access."},
        "row.wtpPct":  {"note": "15% -- Japan NHI rare disease, AU PBS, rest EM access."},
        "row.priceK":  {"note": "$120K blended -- Japan NHI ~$250K, EM access program."}
    },
    ("ALNY", "oxlumo", "ph1"): {
        "us.reachPct": {"note": "Oxlumo 95% of ~300 US PH1 pts -- ultra-rare ceiling penetration achieved; only approved PH1 therapy; q3mo SC maint."},
        "us.wtpPct":   {"note": "75% -- Medicare + commercial ultra-rare; specialty distribution; CED reporting; near-universal access for diagnosed."},
        "us.priceK":   {"note": "Oxlumo WAC $495K/yr weight-based; pediatric dosing lower; outcomes-based with LT/KT avoidance value."},
        "eu.reachPct": {"note": "79% of ~400 EU PH1 -- NICE HST17 + G-BA orphan; pediatric metabolism centers gatekeep."},
        "eu.wtpPct":   {"note": "58% -- NICE HST + G-BA recommended ultra-rare; managed entry, weight-based dose."},
        "eu.priceK":   {"note": "$350K EU net -- ~60% of US ultra-rare."},
        "row.reachPct":{"note": "22.5% of ~1K ROW PH1 -- Japan NHI 2022, EM access via Alnylam."},
        "row.wtpPct":  {"note": "15% -- Japan NHI, EM limited ultra-rare."},
        "row.priceK":  {"note": "$130K blended -- Japan NHI ~$280K, EM access."}
    },

    # ============================== ARGX ==============================
    ("ARGX", "commercial", "fcrn_comm"): {
        "us.reachPct": {"note": "Vyvgart 35% of ~20K US gMG biologic-eligible + CIDP expansion Jun 2024; $4.2B 2025 global; cyclical IV/SC dosing differentiates."},
        "us.wtpPct":   {"note": "70% -- Medicare Part B (IV) + Part D (Hytrulo SC); CIDP expansion broadened TAM 2x; step post-IVIG/plasma."},
        "us.priceK":   {"note": "Vyvgart WAC ~$11K per cycle, 6-12 cycles/yr = $380K/yr blended gMG+CIDP; SC Hytrulo priced parity."},
        "eu.reachPct": {"note": "25% of ~16K EU gMG + CIDP -- EMA 2022 gMG + 2024 CIDP; NICE TA934 + G-BA added benefit proven."},
        "eu.wtpPct":   {"note": "55% -- NICE/G-BA recommended; ATU France; HTA cyclical treatment advantage."},
        "eu.priceK":   {"note": "$250K EU net -- UK/Germany ~65% of US; managed entry outcomes-based."},
        "row.reachPct":{"note": "8% of ~70K ROW gMG/CIDP -- Japan NHI 2022, China NMPA 2023, AU PBS."},
        "row.wtpPct":  {"note": "15% -- Japan NHI major share, China NRDL pending, AU PBS."},
        "row.priceK":  {"note": "$100K blended -- Japan NHI ~$180K, China projected NRDL discount."}
    },
    ("ARGX", "itp_expand", "itp"): {
        "us.reachPct": {"note": "Vyvgart ITP (Phase 3 ADVANCE-ITP positive); 12% of ~60K US chronic ITP -- pre-approval, filing 2026; vs TPO-RA (Nplate/Promacta)."},
        "us.wtpPct":   {"note": "40% -- post-TPO-RA step; specialty payor tier; advantages in rapid response vs TPO-RA ramp."},
        "us.priceK":   {"note": "Vyvgart ITP cyclical dosing ~$350K/yr projected -- parity to gMG pricing."},
        "eu.reachPct": {"note": "8% of EU chronic ITP -- EMA post-approval; NICE/G-BA pathway; TPO-RA generic eltrombopag."},
        "eu.wtpPct":   {"note": "30% -- HTA vs generic eltrombopag tough; specialist hematology."},
        "eu.priceK":   {"note": "$220K EU net projected."},
        "row.reachPct":{"note": "2% ROW ITP -- Japan NHI pathway + Zai Lab China partnership."},
        "row.wtpPct":  {"note": "10% -- Japan NHI, China Zai Lab co-develop."},
        "row.priceK":  {"note": "$90K blended projected."}
    },
    ("ARGX", "empas", "complement"): {
        "us.reachPct": {"note": "Empasiprubart (anti-C2) Ph3 MMN + CIDP; 18% projected of rare MMN/CIDP -- novel complement C2 MOA post-Vyvgart experience."},
        "us.wtpPct":   {"note": "45% -- pre-approval; post-IVIG step; rare neuro specialty payor tier."},
        "us.priceK":   {"note": "Projected WAC ~$300K/yr -- rare neuro premium anchored to Vyvgart."},
        "eu.reachPct": {"note": "12% EU MMN/CIDP -- EMA post-Ph3; NICE/G-BA orphan pathway."},
        "eu.wtpPct":   {"note": "35% -- HTA complement MOA novel; ASMR TBD."},
        "eu.priceK":   {"note": "$190K EU net projected."},
        "row.reachPct":{"note": "3% ROW MMN/CIDP -- Japan NHI pathway."},
        "row.wtpPct":  {"note": "10% -- Japan NHI if approved."},
        "row.priceK":  {"note": "$80K blended projected."}
    },
    ("ARGX", "argx119", "musk"): {
        "us.reachPct": {"note": "Adimanebart (ARGX-119 anti-MuSK agonist) Phase 2 CMS; 45% projected of ~1K US CMS -- ultra-orphan, near-ceiling penetration."},
        "us.wtpPct":   {"note": "55% -- pre-approval; ultra-rare CMS Medicare + commercial broad; specialty neuromuscular centers."},
        "us.priceK":   {"note": "Projected WAC ~$400K/yr -- ultra-rare pediatric neuro pricing."},
        "eu.reachPct": {"note": "30% EU CMS ultra-rare -- EMA orphan pathway; NICE HST + G-BA orphan."},
        "eu.wtpPct":   {"note": "42% -- HTA orphan drug managed entry; weight-based pediatric."},
        "eu.priceK":   {"note": "$260K EU net projected -- ~65% of US ultra-rare."},
        "row.reachPct":{"note": "8% ROW CMS -- Japan NHI rare disease, limited EM."},
        "row.wtpPct":  {"note": "12% -- Japan NHI projected."},
        "row.priceK":  {"note": "$100K blended projected."}
    },
    ("ARGX", "pipeline", "ai_pipe"): {
        "us.reachPct": {"note": "Broader AI pipeline 3% -- ARGX immunology development engine across 15 autoimmune indications; cumulative reach pre-approval."},
        "us.wtpPct":   {"note": "20% -- pre-approval pipeline aggregate; autoimmune specialty tier."},
        "us.priceK":   {"note": "Projected $300K/yr blended -- rare autoimmune FcRn/complement pricing."},
        "eu.reachPct": {"note": "2% EU aggregated AI pipeline -- EMA pathway varies by indication."},
        "eu.wtpPct":   {"note": "15% -- HTA pipeline uncertainty."},
        "eu.priceK":   {"note": "$190K EU net projected."},
        "row.reachPct":{"note": "0.5% ROW -- Japan NHI partnership for select assets."},
        "row.wtpPct":  {"note": "6% -- Japan NHI pipeline."},
        "row.priceK":  {"note": "$80K blended projected."}
    },

    # ============================== BBIO ==============================
    ("BBIO", "commercial", "attr_cm"): {
        "us.reachPct": {"note": "Attruby (acoramidis) 15% of ~150K US ATTR-CM -- launched Feb 2025; competing vs Vyndamax (Pfizer) $4B + Amvuttra CM; ATTRibute-CM 81% survival."},
        "us.wtpPct":   {"note": "55% -- ACC/AHA HF guidelines + Medicare Part D + commercial; formulary ramping; step sometimes after Vyndamax."},
        "us.priceK":   {"note": "Attruby WAC $244K/yr; net ~$260K oral convenience; Vyndamax parity strategy; BridgeBio co-pay program."},
        "eu.reachPct": {"note": "10% of ~80K EU ATTR-CM -- EMA Feb 2025; NICE/G-BA ramping; vs Vyndaqel + Amvuttra established."},
        "eu.wtpPct":   {"note": "40% -- NICE + G-BA recommended; ASMR pending; HTA ATTR-CM anchored to Vyndaqel."},
        "eu.priceK":   {"note": "$160K EU net -- UK/Germany ~60% of US; parity to Vyndaqel EU pricing."},
        "row.reachPct":{"note": "3% of 300K ROW ATTR-CM -- Japan ex-US partnership Bayer; China NMPA pending."},
        "row.wtpPct":  {"note": "12% -- Japan NHI pathway via Bayer, rest limited access."},
        "row.priceK":  {"note": "$65K blended -- Japan NHI ~$140K projected, EM access."}
    },
    ("BBIO", "bbp418", "lgmd"): {
        "us.reachPct": {"note": "BBP-418 (ribitol) Phase 3 FORTIFY LGMD2I/R9; 50% of ~1-2K US LGMD2I -- ultra-orphan, near-ceiling pending 2026 approval."},
        "us.wtpPct":   {"note": "55% -- pre-approval; ultra-rare Medicare/commercial specialty tier; first approved LGMD2I therapy potential."},
        "us.priceK":   {"note": "Projected WAC ~$400K/yr -- ultra-rare neuromuscular pricing anchored to SMA/DMD therapies."},
        "eu.reachPct": {"note": "35% of ~3K EU LGMD2I/R9 -- EMA orphan pathway post-Ph3; NICE HST + G-BA ultra-rare."},
        "eu.wtpPct":   {"note": "42% -- orphan HTA managed entry; specialty neuromuscular centers."},
        "eu.priceK":   {"note": "$250K EU net projected -- ~60% US ultra-rare."},
        "row.reachPct":{"note": "8% of ~10K ROW LGMD2I -- Japan NHI pathway, limited rest."},
        "row.wtpPct":  {"note": "12% -- Japan NHI rare disease projected."},
        "row.priceK":  {"note": "$100K blended projected -- Japan NHI ~$220K."}
    },
    ("BBIO", "infig", "achon"): {
        "us.reachPct": {"note": "Infigratinib (FGFR1-3 inhibitor) Ph3 PROPEL3 achondroplasia; 30% of ~10K US achon pediatric; vs BioMarin Voxzogo (vosoritide) SOC."},
        "us.wtpPct":   {"note": "50% -- pre-approval; oral vs daily SC Voxzogo convenience; Medicare pediatric specialty + commercial."},
        "us.priceK":   {"note": "Projected WAC ~$320K/yr -- anchored to Voxzogo $320K oral convenience parity."},
        "eu.reachPct": {"note": "20% of ~12K EU achon -- EMA post-Ph3; NICE/G-BA pediatric rare."},
        "eu.wtpPct":   {"note": "38% -- HTA achon rare pediatric; oral convenience vs Voxzogo injection."},
        "eu.priceK":   {"note": "$200K EU net projected -- parity to Voxzogo EU."},
        "row.reachPct":{"note": "5% of ~60K ROW achon -- Japan NHI + AU PBS pathway."},
        "row.wtpPct":  {"note": "10% -- Japan NHI rare pediatric."},
        "row.priceK":  {"note": "$80K blended projected."}
    },
    ("BBIO", "encal", "adh1"): {
        "us.reachPct": {"note": "Encaleret (CaSR antagonist) Ph3 CALIBRATE ADH1; 55% of ~12K US ADH1 symptomatic -- ultra-orphan near-ceiling post-approval."},
        "us.wtpPct":   {"note": "60% -- pre-approval; first approved ADH1 therapy potential; specialty endocrine Medicare + commercial."},
        "us.priceK":   {"note": "Projected WAC ~$350K/yr -- ultra-rare endocrine pricing."},
        "eu.reachPct": {"note": "40% of EU ADH1 -- EMA orphan post-Ph3."},
        "eu.wtpPct":   {"note": "45% -- HTA ultra-rare managed entry."},
        "eu.priceK":   {"note": "$220K EU net projected."},
        "row.reachPct":{"note": "10% ROW ADH1 -- Japan NHI pathway, EM access limited."},
        "row.wtpPct":  {"note": "15% -- Japan NHI rare endocrine."},
        "row.priceK":  {"note": "$90K blended projected."}
    },
    ("BBIO", "depleter", "attr_next"): {
        "us.reachPct": {"note": "TTR amyloid depleter (anti-TTR mAb, preclinical-Ph1) 5% -- next-gen disease reversal beyond stabilization/silencing; early-stage risky."},
        "us.wtpPct":   {"note": "20% -- pre-clinical; if reversal shown, premium over Attruby/Amvuttra; payor tier speculative."},
        "us.priceK":   {"note": "Projected WAC ~$250K/yr -- anchored to ATTR class; premium TBD on clinical data."},
        "eu.reachPct": {"note": "3% EU ATTR-CM -- EMA post-Ph3 late 2020s; behind Attruby launch."},
        "eu.wtpPct":   {"note": "15% -- HTA pathway TBD; novel depleter MOA evidence bar high."},
        "eu.priceK":   {"note": "$160K EU net projected."},
        "row.reachPct":{"note": "0.5% ROW -- Japan NHI pathway pending Ph3."},
        "row.wtpPct":  {"note": "5% -- early-stage ROW uncertain."},
        "row.priceK":  {"note": "$60K blended projected."}
    },
}


if __name__ == "__main__":
    n_entries = len(SOM_TOOLTIPS)
    n_tooltips = sum(len(v) for v in SOM_TOOLTIPS.values())
    by_ticker = {}
    for (t, a, i) in SOM_TOOLTIPS:
        by_ticker[t] = by_ticker.get(t, 0) + 1
    print(f"SOM_TOOLTIPS: {n_entries} (ticker, asset, indication) entries")
    print(f"Total tooltip notes: {n_tooltips}")
    print("By ticker:")
    for t in sorted(by_ticker):
        print(f"  {t}: {by_ticker[t]} indications")
