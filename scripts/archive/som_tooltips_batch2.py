# -*- coding: utf-8 -*-
"""
Hand-researched drug-specific SOM tooltips for batch 2 (12 companies).
Each note explains WHY the reach/WTP/price assumption applies to that specific asset.
"""

SOM_TOOLTIPS = {
    # ============================================================
    # SRPT -- Sarepta Therapeutics
    # ============================================================
    ("SRPT", "elevidys", "dmd_gt"): {
        "us.reachPct": {"note": "Ambulatory + non-amb per Jun-2024 expanded label; ~40% of eligible treated at peak given AAV capacity + 1x dose; 2025 sales ~$820M after label pause."},
        "us.wtpPct":   {"note": "50% -- commercial/Medicaid cover with PA; 3 fatal liver injury events + boxed warning + FDA hold on non-amb dosing temper adoption."},
        "us.priceK":   {"note": "$3.2M WAC one-time; ~$2.5M net after Medicaid + outcomes-based rebates; amortized ~$500K/yr over effective 5yr durability."},
        "eu.reachPct": {"note": "Roche ex-US; EU reach 25% -- UK/Germany launched; CHMP neg opinion Jun-2024 retained as negative, Roche appeals; Spain/Italy early access only."},
        "eu.wtpPct":   {"note": "30% -- EMA refused marketing auth 2024; country-by-country named patient access; G-BA/NICE awaiting Phase 3 EMBARK confirmatory readout."},
        "eu.priceK":   {"note": "~$1.8M net EU via Roche; ~56% of US WAC per HTA benchmark and named-patient pricing."},
        "row.reachPct":{"note": "8% -- Japan PMDA reviewing; Brazil private; Saudi RSPRC cohort; limited AAV dosing centers constrain APAC rollout."},
        "row.wtpPct":  {"note": "10% -- Japan NHI expected 2026; Korea/AU cash pay; emerging markets access only via Roche global program."},
        "row.priceK":  {"note": "~$800K blended; Japan ~$1.5M, Gulf ~$1.2M, Brazil ~$400K tiered."}
    },
    ("SRPT", "exondys", "dmd_ex51"): {
        "us.reachPct": {"note": "First-gen exon skipper, ~13% of DMD population w/ exon 51 amenable; ~60% of eligible pts on therapy; 2024 sales ~$320M declining as Elevidys cannibalizes."},
        "us.wtpPct":   {"note": "55% -- entrenched commercial/Medicaid coverage since 2016 accel approval; modest dystrophin benefit, parents reluctant to switch off."},
        "us.priceK":   {"note": "~$750K/yr WAC weight-based; ~$620K net after GPO/Medicaid rebates."},
        "eu.reachPct": {"note": "5% -- EMA never approved (2018 withdrawal); compassionate use only in select EU5 markets."},
        "eu.wtpPct":   {"note": "8% -- named-patient / expanded access only; no HTA reimbursement path."},
        "eu.priceK":   {"note": "~$500K blended via private/compassionate channels."},
        "row.reachPct":{"note": "4% -- Japan NHI covered since 2020; MENA via tender; limited APAC presence."},
        "row.wtpPct":  {"note": "6% -- Japan reimbursed at reduced price; Korea/AU off-label import; no EM access."},
        "row.priceK":  {"note": "~$400K blended; Japan ~$600K post NHI negotiation."}
    },
    ("SRPT", "amondys", "dmd_ex45"): {
        "us.reachPct": {"note": "Exon 45 amenable ~8% of DMD; ~55% of eligible pts on therapy; 2024 sales ~$180M, slow uptake competing w/ Elevidys."},
        "us.wtpPct":   {"note": "50% -- PPMD/KOL support; accelerated approval 2021 w/ dystrophin surrogate; payors cover w/ genetic confirmation."},
        "us.priceK":   {"note": "~$750K/yr WAC weight-based; ~$620K net parallel to Exondys pricing tier."},
        "eu.reachPct": {"note": "3% -- no EMA approval; private import/compassionate use only."},
        "eu.wtpPct":   {"note": "5% -- no HTA pathway; patient advocacy-driven named patient access."},
        "eu.priceK":   {"note": "~$500K via private channels."},
        "row.reachPct":{"note": "3% -- Japan PMDA filing pending; MENA small cohort."},
        "row.wtpPct":  {"note": "5% -- limited reimbursement; Japan launch expected 2026."},
        "row.priceK":  {"note": "~$400K blended."}
    },
    ("SRPT", "vyondys", "dmd_ex53"): {
        "us.reachPct": {"note": "Exon 53 ~8% of DMD; ~55% penetration; 2024 sales ~$170M; same PMO competitive dynamic as Amondys."},
        "us.wtpPct":   {"note": "50% -- accel approval 2019; commercial + Medicaid covered w/ PA; modest clinical benefit."},
        "us.priceK":   {"note": "~$750K/yr WAC; ~$620K net."},
        "eu.reachPct": {"note": "3% -- no EU approval; private compassionate use."},
        "eu.wtpPct":   {"note": "5% -- no HTA; minimal access."},
        "eu.priceK":   {"note": "~$500K private."},
        "row.reachPct":{"note": "3% -- Japan approved 2020 via JCR partnership; small cohort."},
        "row.wtpPct":  {"note": "6% -- Japan NHI reimbursed."},
        "row.priceK":  {"note": "~$450K blended."}
    },
    ("SRPT", "srp9003", "lgmd2e"): {
        "us.reachPct": {"note": "LGMD2E/R4 ultra-rare (~2K US pts); ~30% peak penetration post-approval (2026E) limited by AAV mfg + newborn screening ramp."},
        "us.wtpPct":   {"note": "45% -- BLA filing 2025 w/ AAVrh74 gene tx; payors will require confirmatory data given Elevidys safety experience."},
        "us.priceK":   {"note": "~$3M one-time pricing in line w/ Elevidys; gene therapy precedent."},
        "eu.reachPct": {"note": "15% -- EU Roche partnership likely; EMA review 2027+."},
        "eu.wtpPct":   {"note": "20% -- HTA bodies cautious on one-time AAV given LGMD natural history data gaps."},
        "eu.priceK":   {"note": "~$1.7M HTA-negotiated."},
        "row.reachPct":{"note": "5% -- Japan/Brazil limited rollout given mfg constraints."},
        "row.wtpPct":  {"note": "8% -- narrow reimbursement outside Japan NHI."},
        "row.priceK":  {"note": "~$700K blended."}
    },
    ("SRPT", "srp1001", "fshd"): {
        "us.reachPct": {"note": "FSHD ~16K US pts; siRNA preclinical/Ph1; 25% peak reach post-approval (2029E); first disease-modifying therapy for FSHD."},
        "us.wtpPct":   {"note": "35% -- patient advocacy strong (FSHD Society); adult-onset + slow progression means payors will demand functional endpoints."},
        "us.priceK":   {"note": "~$350K/yr chronic siRNA; priced vs ultra-rare neuromuscular precedents."},
        "eu.reachPct": {"note": "10% -- EU pipeline launch 2030+; requires EMA + HTA."},
        "eu.wtpPct":   {"note": "15% -- HTA bodies want OLE data on muscle MRI endpoints."},
        "eu.priceK":   {"note": "~$180K blended EU."},
        "row.reachPct":{"note": "3% -- Japan/APAC early commercial."},
        "row.wtpPct":  {"note": "5% -- limited reimbursement."},
        "row.priceK":  {"note": "~$100K blended."}
    },
    ("SRPT", "srp1003", "dm1"): {
        "us.reachPct": {"note": "DM1 ~40K US pts; early pipeline; 20% peak reach (2030+) competing w/ Avidity AOC-1001 + Dyne DYNE-101."},
        "us.wtpPct":   {"note": "30% -- crowded field; payors will step-edit given multiple AOC/siRNA options reading out."},
        "us.priceK":   {"note": "~$350K/yr chronic therapy; orphan neuromuscular pricing band."},
        "eu.reachPct": {"note": "8% -- pipeline launch 2031+; EMA + HTA required."},
        "eu.wtpPct":   {"note": "12% -- competitive landscape limits pricing power."},
        "eu.priceK":   {"note": "~$180K EU."},
        "row.reachPct":{"note": "2% -- minimal ROW presence pre-2032."},
        "row.wtpPct":  {"note": "3% -- limited reimbursement."},
        "row.priceK":  {"note": "~$100K blended."}
    },

    # ============================================================
    # LEGN -- Legend Biotech (Carvykti)
    # ============================================================
    ("LEGN", "commercial", "mm_2l"): {
        "us.reachPct": {"note": "Carvykti 2L+ post CARTITUDE-4 label expansion Apr-2024; ~30% of eligible 2L+ pts treated given apheresis capacity; 2024 global sales $963M."},
        "us.wtpPct":   {"note": "60% -- J&J/Legend 50:50 profit share; NCCN pref 2L+; commercial + Medicare cover w/ PA; vein-to-vein ~6wk improved from ~10wk."},
        "us.priceK":   {"note": "$530K WAC one-time; ~$450K net after J&J access programs + 340B."},
        "eu.reachPct": {"note": "20% -- EMA approved 2L+ Jun-2024; UK NICE reimb Dec-2024; Germany G-BA 'considerable' benefit; Italy/Spain PA."},
        "eu.wtpPct":   {"note": "35% -- HTA bodies accept CARTITUDE-4 PFS HR 0.26; budget impact + CAR-T capacity constrain uptake."},
        "eu.priceK":   {"note": "~$420K net EU; ~80% of US WAC per NICE/G-BA confidential discounts."},
        "row.reachPct":{"note": "10% -- Japan PMDA 2L+ expansion approved 2024; China via Legend partnership; Korea/AU private."},
        "row.wtpPct":  {"note": "15% -- Japan NHI reimbursed ~$350K; China NRDL pending; limited EM capacity."},
        "row.priceK":  {"note": "~$300K blended; Japan $400K, China ~$200K tendered."}
    },
    ("LEGN", "carv_1l", "mm_1l"): {
        "us.reachPct": {"note": "Potential 1L transplant-eligible expansion 2027+ if CARTITUDE-5/6 positive; 15% peak reach limited by mfg capacity + SCT standard."},
        "us.wtpPct":   {"note": "45% -- payors will compare vs SCT ~$150K; 1L CAR-T requires robust OS benefit + durability."},
        "us.priceK":   {"note": "$530K WAC assumption consistent w/ 2L+; J&J unlikely to discount 1L given value story."},
        "eu.reachPct": {"note": "8% -- 1L launch 2028+; HTA bodies will benchmark vs SCT + bispecifics."},
        "eu.wtpPct":   {"note": "20% -- EU HTA strict on 1L in MM given established pathways."},
        "eu.priceK":   {"note": "~$420K EU net."},
        "row.reachPct":{"note": "4% -- mfg + capacity constraints globally."},
        "row.wtpPct":  {"note": "8% -- 1L reimbursement lagged."},
        "row.priceK":  {"note": "~$300K blended."}
    },
    ("LEGN", "lucar", "nhl"): {
        "us.reachPct": {"note": "LUCAR-G39D autologous CD20 CAR-T for B-NHL; Ph1; 10% peak reach (2029+) given crowded NHL CAR-T field (Yescarta, Breyanzi, Kymriah)."},
        "us.wtpPct":   {"note": "25% -- differentiation vs CD19 CAR-Ts uncertain; payors will step-edit."},
        "us.priceK":   {"note": "~$450K WAC in line with NHL CAR-T class pricing."},
        "eu.reachPct": {"note": "4% -- pipeline launch 2030+."},
        "eu.wtpPct":   {"note": "10% -- competitive HTA environment."},
        "eu.priceK":   {"note": "~$350K EU."},
        "row.reachPct":{"note": "2% -- APAC minimal pre-2031."},
        "row.wtpPct":  {"note": "4% -- limited access."},
        "row.priceK":  {"note": "~$200K blended."}
    },
    ("LEGN", "invivo", "invivo_onc"): {
        "us.reachPct": {"note": "In vivo CAR-T preclinical; 2032+ launch if successful; 15% peak reach for solid/heme tumors -- transformative but unproven."},
        "us.wtpPct":   {"note": "30% -- could disrupt autologous CAR-T if durable; pricing/reimb TBD."},
        "us.priceK":   {"note": "~$400K placeholder; cheaper than ex vivo autologous CAR-T mfg."},
        "eu.reachPct": {"note": "5% -- speculative EU launch 2033+."},
        "eu.wtpPct":   {"note": "12% -- HTA highly scrutinized."},
        "eu.priceK":   {"note": "~$300K EU."},
        "row.reachPct":{"note": "2% -- pipeline, ROW minimal."},
        "row.wtpPct":  {"note": "5% -- limited access."},
        "row.priceK":  {"note": "~$180K blended."}
    },

    # ============================================================
    # NUVL -- Nuvalent
    # ============================================================
    ("NUVL", "zides", "ros1"): {
        "us.reachPct": {"note": "Zidesamtinib ROS1 NSCLC; ARROS-1 registrational cohort; 50% peak reach in 2L+ ROS1 (post-crizotinib/entrectinib/repotrectinib) given best-in-class CNS + G2032R activity."},
        "us.wtpPct":   {"note": "65% -- NCCN will prefer in 2L+ if ORR >70% + mDoR >15mo; 1L competitive vs repotrectinib Augtyro."},
        "us.priceK":   {"note": "~$260K/yr WAC assumption in line with repotrectinib $250K + Rozlytrek $230K precedent."},
        "eu.reachPct": {"note": "25% -- EMA filing 2026 expected; launch 2027; NICE/G-BA will require cross-trial vs repotrectinib."},
        "eu.wtpPct":   {"note": "40% -- HTA accepts ROS1 orphan positioning; budget impact modest."},
        "eu.priceK":   {"note": "~$140K EU net; ~55% of US."},
        "row.reachPct":{"note": "10% -- Japan PMDA priority review likely; China partnership TBD; APAC rollout 2028."},
        "row.wtpPct":  {"note": "15% -- Japan NHI reimbursed; China NRDL typical 60-70% discount."},
        "row.priceK":  {"note": "~$90K blended; Japan $150K, China $50K tendered."}
    },
    ("NUVL", "nelad", "alk"): {
        "us.reachPct": {"note": "Neladalkib ALK NSCLC post-lorlatinib; ALKOVE-1 Ph2; 35% peak reach in 2L+ ALK given compound mutation coverage + CNS penetration."},
        "us.wtpPct":   {"note": "55% -- NCCN adoption likely if beats alectinib/lorlatinib retreat; ALK 1L locked by alectinib + lorlatinib."},
        "us.priceK":   {"note": "~$220K/yr WAC vs lorlatinib ~$215K; premium if G1202R/compound activity confirmed."},
        "eu.reachPct": {"note": "18% -- EMA 2027+; 2L ALK small market; HTA will benchmark vs lorlatinib."},
        "eu.wtpPct":   {"note": "32% -- ALK orphan but HTA price-sensitive."},
        "eu.priceK":   {"note": "~$120K EU."},
        "row.reachPct":{"note": "7% -- Japan/China partnership; ROW 2028+."},
        "row.wtpPct":  {"note": "12% -- limited reimbursement initially."},
        "row.priceK":  {"note": "~$70K blended."}
    },
    ("NUVL", "nvl330", "her2"): {
        "us.reachPct": {"note": "NVL-330 HER2 NSCLC exon 20; Ph1 2025; 25% peak (2029+) competing w/ Enhertu + zongertinib + BAY 2927088."},
        "us.wtpPct":   {"note": "40% -- crowded HER2 mut NSCLC; positioning depends on exon 20 specificity + brain penetration."},
        "us.priceK":   {"note": "~$220K/yr WAC parallel to selective TKI pricing."},
        "eu.reachPct": {"note": "10% -- pipeline 2030+; competitive HTA vs Enhertu."},
        "eu.wtpPct":   {"note": "18% -- HTA selectivity premium limited."},
        "eu.priceK":   {"note": "~$110K EU."},
        "row.reachPct":{"note": "3% -- ROW pipeline minimal pre-2031."},
        "row.wtpPct":  {"note": "6% -- limited access."},
        "row.priceK":  {"note": "~$60K blended."}
    },

    # ============================================================
    # NBIX -- Neurocrine Biosciences
    # ============================================================
    ("NBIX", "commercial", "td"): {
        "us.reachPct": {"note": "Ingrezza TD ~600K US prev; ~30% of treated TD pts on VMAT2; 2024 sales $2.36B, ~$2.5B 2025E; PRIME competition from Teva Austedo."},
        "us.wtpPct":   {"note": "75% -- entrenched Medicare Part D + Medicaid; PBMs prefer via rebates; HD chorea indication added 2023 expansion."},
        "us.priceK":   {"note": "~$90K/yr WAC; ~$55K net after PBM rebates (40%+ GTN); sprinkle cap launched 2024."},
        "eu.reachPct": {"note": "5% -- no EU approval; no filing; EU TD treated w/ generic tetrabenazine."},
        "eu.wtpPct":   {"note": "5% -- no HTA pathway."},
        "eu.priceK":   {"note": "N/A -- negligible EU presence."},
        "row.reachPct":{"note": "8% -- Mitsubishi Tanabe Japan rights; Takeda-backed commercial coverage; limited APAC."},
        "row.wtpPct":  {"note": "12% -- Japan NHI covered; other APAC limited."},
        "row.priceK":  {"note": "~$50K blended; Japan $70K."}
    },
    ("NBIX", "crenessity", "cah"): {
        "us.reachPct": {"note": "Crenessity (crinecerfont) CAH approved Dec-2024; ~25K US CAH pts; 40% peak reach as first steroid-sparing therapy; 2025 launch ramp."},
        "us.wtpPct":   {"note": "60% -- clear unmet need in CAH; endocrinology KOL support; CTNNB1 pathway first-in-class; payors cover w/ genetic confirmation."},
        "us.priceK":   {"note": "~$150K/yr WAC; ~$110K net; premium pricing for rare endocrine."},
        "eu.reachPct": {"note": "15% -- EMA approved 2025; NICE/G-BA review 2025-26; CAH well-recognized orphan."},
        "eu.wtpPct":   {"note": "30% -- HTA bodies accept steroid-sparing value; budget modest given prevalence."},
        "eu.priceK":   {"note": "~$85K EU net; ~55% of US."},
        "row.reachPct":{"note": "6% -- Japan PMDA 2026+; APAC rollout gradual."},
        "row.wtpPct":  {"note": "10% -- Japan NHI expected; other ROW limited access."},
        "row.priceK":  {"note": "~$55K blended."}
    },
    ("NBIX", "osav", "mdd"): {
        "us.reachPct": {"note": "Osavampator (NBI-1065845) AMPA PAM MDD adjunct; Ph3 2025; 20% peak reach (2028+) in TRD given crowded space (Spravato, Auvelity)."},
        "us.wtpPct":   {"note": "40% -- PBMs step-edit adjunct MDD; payors will compare vs Spravato + Auvelity."},
        "us.priceK":   {"note": "~$12K/yr WAC assumption in line with branded MDD adjunct pricing."},
        "eu.reachPct": {"note": "8% -- EU launch 2029+; depression mostly generic SSRIs."},
        "eu.wtpPct":   {"note": "15% -- HTA tough on MDD given genericization."},
        "eu.priceK":   {"note": "~$6K EU blended."},
        "row.reachPct":{"note": "3% -- ROW minimal MDD branded access."},
        "row.wtpPct":  {"note": "6% -- limited reimbursement."},
        "row.priceK":  {"note": "~$3K blended."}
    },
    ("NBIX", "direc", "schizo"): {
        "us.reachPct": {"note": "Direclidine (NBI-'568) M4 agonist schizophrenia; Ph2 2025; 15% peak reach competing vs Bristol Cobenfy (KarXT)."},
        "us.wtpPct":   {"note": "35% -- 2nd-in-class muscarinic; payors will prefer Cobenfy launched 2024 unless tolerability edge."},
        "us.priceK":   {"note": "~$20K/yr WAC vs Cobenfy $1,850/mo ($22K/yr)."},
        "eu.reachPct": {"note": "5% -- EU schizo pricing pressured by generics."},
        "eu.wtpPct":   {"note": "12% -- HTA discount for schizophrenia."},
        "eu.priceK":   {"note": "~$9K EU."},
        "row.reachPct":{"note": "2% -- ROW limited branded schizo access."},
        "row.wtpPct":  {"note": "4% -- minimal."},
        "row.priceK":  {"note": "~$5K blended."}
    },
    ("NBIX", "pipeline", "neuro_pipe"): {
        "us.reachPct": {"note": "Broad neuroscience pipeline (NBI-'770, '921, others); 10% aggregate reach across indications 2030+."},
        "us.wtpPct":   {"note": "25% -- early stage; payor access unproven."},
        "us.priceK":   {"note": "~$15K/yr blended across programs."},
        "eu.reachPct": {"note": "3% -- pipeline EU launch 2031+."},
        "eu.wtpPct":   {"note": "8% -- HTA scrutiny."},
        "eu.priceK":   {"note": "~$7K EU."},
        "row.reachPct":{"note": "1% -- negligible ROW."},
        "row.wtpPct":  {"note": "3% -- minimal."},
        "row.priceK":  {"note": "~$3K blended."}
    },
    ("NBIX", "vykat", "pws"): {
        "us.reachPct": {"note": "VYKAT XR (diazoxide choline) Prader-Willi hyperphagia approved Mar-2025; ~10K US PWS pts; 40% peak reach as first approved hyperphagia therapy."},
        "us.wtpPct":   {"note": "55% -- clear unmet need in PWS; caregiver/KOL advocacy strong; payors cover via PA."},
        "us.priceK":   {"note": "~$470K/yr WAC list; ~$350K net; ultra-rare pediatric premium pricing."},
        "eu.reachPct": {"note": "12% -- EMA filing 2026; HTA bodies will require hyperphagia PROs."},
        "eu.wtpPct":   {"note": "22% -- rare pediatric reimbursed but budget-capped."},
        "eu.priceK":   {"note": "~$260K EU net."},
        "row.reachPct":{"note": "5% -- Japan PMDA 2027+; APAC small PWS population."},
        "row.wtpPct":  {"note": "8% -- Japan NHI expected; limited EM access."},
        "row.priceK":  {"note": "~$170K blended."}
    },

    # ============================================================
    # AXSM -- Axsome Therapeutics
    # ============================================================
    ("AXSM", "auvelity", "mdd"): {
        "us.reachPct": {"note": "Auvelity MDD approved Aug-2022; ~21M US MDD pts, ~7M TRD; 8% peak reach in branded MDD given PBM step-edit vs generics; 2024 sales $291M."},
        "us.wtpPct":   {"note": "45% -- Express Scripts + CVS formulary tier 3; step through 2 generics; KOL traction for rapid onset (1wk vs 6wk SSRI)."},
        "us.priceK":   {"note": "~$7.5K/yr WAC; ~$4.5K net after PBM rebates (~40% GTN)."},
        "eu.reachPct": {"note": "5% -- no EMA filing; AXSM focused on US commercial."},
        "eu.wtpPct":   {"note": "5% -- no HTA pathway planned."},
        "eu.priceK":   {"note": "~$3K blended minimal EU presence."},
        "row.reachPct":{"note": "3% -- no meaningful ROW launch."},
        "row.wtpPct":  {"note": "5% -- minimal."},
        "row.priceK":  {"note": "~$2K blended."}
    },
    ("AXSM", "sunosi", "eds"): {
        "us.reachPct": {"note": "Sunosi EDS narcolepsy/OSA acquired from Jazz 2022; ~400K US EDS; 12% reach; 2024 sales ~$95M, modest growth."},
        "us.wtpPct":   {"note": "40% -- Schedule IV DEA; PBMs step-edit vs modafinil generics; niche vs Xywav/Wakix."},
        "us.priceK":   {"note": "~$12K/yr WAC; ~$7K net after PBM rebates."},
        "eu.reachPct": {"note": "8% -- Jazz/Axsome EU rights; launched 2020 by Jazz; NICE/G-BA reimbursed."},
        "eu.wtpPct":   {"note": "18% -- HTA covered for narcolepsy but budget-capped."},
        "eu.priceK":   {"note": "~$6K EU net."},
        "row.reachPct":{"note": "3% -- Japan/APAC minimal."},
        "row.wtpPct":  {"note": "5% -- limited reimbursement."},
        "row.priceK":  {"note": "~$3K blended."}
    },
    ("AXSM", "symbravo", "gad"): {
        "us.reachPct": {"note": "Symbravo (AXS-07) migraine acute approved Jan-2025 (not GAD -- config label); ~40M US migraineurs; 10% peak reach given CGRP gepant competition."},
        "us.wtpPct":   {"note": "40% -- PBMs step-edit vs rizatriptan generics + Nurtec; formulary access moderate."},
        "us.priceK":   {"note": "~$1K/pack WAC per-use; ~$600/pack net after rebates; episodic pricing."},
        "eu.reachPct": {"note": "4% -- no EU filing; AXSM US-focused."},
        "eu.wtpPct":   {"note": "5% -- no HTA."},
        "eu.priceK":   {"note": "Minimal EU."},
        "row.reachPct":{"note": "2% -- negligible ROW."},
        "row.wtpPct":  {"note": "3% -- minimal."},
        "row.priceK":  {"note": "Minimal."}
    },
    ("AXSM", "axs05_ad", "ad_agit"): {
        "us.reachPct": {"note": "AXS-05 Alzheimer's agitation Ph3 ADVANCE-2 readout; 30% peak reach (2026+) given ~50% of AD pts develop agitation + only Rexulti approved."},
        "us.wtpPct":   {"note": "50% -- payors will cover if labeled; competes vs Rexulti (~$10K/yr); supplemental NDA path."},
        "us.priceK":   {"note": "~$7.5K/yr parallel to Auvelity pricing."},
        "eu.reachPct": {"note": "8% -- EU launch 2028+; HTA scrutiny on AD agitation pricing."},
        "eu.wtpPct":   {"note": "18% -- HTA bodies will benchmark vs antipsychotics generic."},
        "eu.priceK":   {"note": "~$3.5K EU."},
        "row.reachPct":{"note": "3% -- ROW minimal."},
        "row.wtpPct":  {"note": "5% -- limited."},
        "row.priceK":  {"note": "~$2K blended."}
    },
    ("AXSM", "axs14", "fibro"): {
        "us.reachPct": {"note": "AXS-14 (esreboxetine) fibromyalgia Ph3 planned; ~6M US FM; 15% peak reach vs Lyrica/Savella/Cymbalta generics."},
        "us.wtpPct":   {"note": "35% -- PBMs step-edit heavily in FM given generics; differentiation required."},
        "us.priceK":   {"note": "~$5K/yr WAC placeholder; branded FM ceiling."},
        "eu.reachPct": {"note": "4% -- EU FM market small; no clear filing strategy."},
        "eu.wtpPct":   {"note": "8% -- HTA tough on FM."},
        "eu.priceK":   {"note": "~$2K EU."},
        "row.reachPct":{"note": "2% -- ROW minimal."},
        "row.wtpPct":  {"note": "3% -- minimal."},
        "row.priceK":  {"note": "~$1K blended."}
    },
    ("AXSM", "solri_adhd", "sol_expan"): {
        "us.reachPct": {"note": "Solriamfetol ADHD expansion; Ph3 FOCUS; 10% peak reach given Adderall/Vyvanse generics + Qelbree branded."},
        "us.wtpPct":   {"note": "30% -- crowded ADHD; payors step-edit aggressively."},
        "us.priceK":   {"note": "~$12K/yr WAC consistent w/ Sunosi pricing."},
        "eu.reachPct": {"note": "4% -- EU ADHD mostly methylphenidate generic; Jazz Sunosi EU not ADHD."},
        "eu.wtpPct":   {"note": "8% -- HTA tough on ADHD."},
        "eu.priceK":   {"note": "~$5K EU."},
        "row.reachPct":{"note": "2% -- ROW limited."},
        "row.wtpPct":  {"note": "3% -- minimal."},
        "row.priceK":  {"note": "~$2K blended."}
    },
    ("AXSM", "axs12", "narco"): {
        "us.reachPct": {"note": "AXS-12 (reboxetine) narcolepsy cataplexy Ph3 SYMPHONY; ~170K US narcolepsy; 15% peak reach vs Xywav/Wakix."},
        "us.wtpPct":   {"note": "35% -- niche cataplexy; payors step-edit vs SSRIs off-label + Wakix."},
        "us.priceK":   {"note": "~$25K/yr WAC premium orphan pricing if approved."},
        "eu.reachPct": {"note": "6% -- EU narcolepsy HTA covered; AXSM partnership TBD."},
        "eu.wtpPct":   {"note": "15% -- HTA accepts rare sleep disorder premium."},
        "eu.priceK":   {"note": "~$12K EU."},
        "row.reachPct":{"note": "2% -- Japan partnership possible."},
        "row.wtpPct":  {"note": "4% -- limited."},
        "row.priceK":  {"note": "~$6K blended."}
    },

    # ============================================================
    # 4568 -- Daiichi Sankyo
    # ============================================================
    ("4568", "commercial", "her2"): {
        "us.reachPct": {"note": "Enhertu HER2 BC + gastric + NSCLC (HER2-low added DESTINY-Breast06 2024); ~45% of HER2+ BC 2L+ treated; 2024 global sales $3.75B, AZ co-promoted."},
        "us.wtpPct":   {"note": "70% -- NCCN cat 1 in HER2+ MBC 2L + HER2-low; ILD boxed warning monitored; commercial + Medicare cover widely."},
        "us.priceK":   {"note": "~$180K/yr WAC per median 14mo duration; ~$140K net after 340B + rebates."},
        "eu.reachPct": {"note": "35% -- EMA HER2-low approved 2023; NICE/G-BA reimbursed; capacity + ILD monitoring constrain."},
        "eu.wtpPct":   {"note": "55% -- HTA accepts DESTINY-Breast04/06 OS benefit; budget impact managed by AZ/Daiichi rebates."},
        "eu.priceK":   {"note": "~$110K EU net; ~60% of US."},
        "row.reachPct":{"note": "18% -- Japan PMDA leads globally; China NRDL 2024; Brazil/APAC rollout."},
        "row.wtpPct":  {"note": "28% -- Japan NHI covered; China NRDL ~70% discount; APAC variable."},
        "row.priceK":  {"note": "~$70K blended; Japan $130K, China $45K tendered."}
    },
    ("4568", "datroway", "trop2"): {
        "us.reachPct": {"note": "Datroway (datopotamab) TROP2 ADC approved Jan-2025 HR+/HER2- MBC 2L+; ~20% reach vs Trodelvy (Gilead), competitive TROP2 class."},
        "us.wtpPct":   {"note": "45% -- NCCN cat 2A; payors will compare vs Trodelvy $170K + cross-trial PFS; AZ/Daiichi promotion."},
        "us.priceK":   {"note": "~$170K/yr WAC parallel to Trodelvy; ~$130K net."},
        "eu.reachPct": {"note": "12% -- EMA approved 2025; HTA accepts TROPION-Breast01 but modest OS delta."},
        "eu.wtpPct":   {"note": "25% -- HTA budget-cap given Trodelvy dominance in HR+/HER2-."},
        "eu.priceK":   {"note": "~$100K EU net."},
        "row.reachPct":{"note": "6% -- Japan PMDA priority; China partnership; ROW ramp 2026+."},
        "row.wtpPct":  {"note": "12% -- limited tender pricing."},
        "row.priceK":  {"note": "~$60K blended."}
    },
    ("4568", "her3_dxd", "her3"): {
        "us.reachPct": {"note": "Patritumab deruxtecan HER3-DXd; CRL Jun-2024 for EGFR-mut NSCLC; Ph3 HERTHENA-Lung02 readout 2026; 15% peak reach if relaunched."},
        "us.wtpPct":   {"note": "35% -- NCCN positioning unclear post-CRL; will benchmark vs Rybrevant + Leclaza."},
        "us.priceK":   {"note": "~$180K/yr parallel to Enhertu class pricing."},
        "eu.reachPct": {"note": "6% -- EMA filing delayed; launch 2027+."},
        "eu.wtpPct":   {"note": "15% -- HTA skeptical post-CRL."},
        "eu.priceK":   {"note": "~$110K EU."},
        "row.reachPct":{"note": "4% -- Japan PMDA possible earlier approval; ROW small."},
        "row.wtpPct":  {"note": "8% -- Japan NHI expected."},
        "row.priceK":  {"note": "~$60K blended."}
    },
    ("4568", "idxd", "merck_adc"): {
        "us.reachPct": {"note": "Merck-partnered ADC (ifinatamab deruxtecan, raludotatug + patritumab); Ph2/3 across tumors; 15% peak reach aggregate."},
        "us.wtpPct":   {"note": "35% -- $4B upfront deal w/ Merck 2023; commercial push strong; indication-dependent payor access."},
        "us.priceK":   {"note": "~$180K/yr WAC parallel to DXd class."},
        "eu.reachPct": {"note": "6% -- Merck co-commercialization EU; EMA 2027+."},
        "eu.wtpPct":   {"note": "15% -- HTA indication-specific."},
        "eu.priceK":   {"note": "~$110K EU."},
        "row.reachPct":{"note": "4% -- Japan/China leadership."},
        "row.wtpPct":  {"note": "8% -- reimbursement gradual."},
        "row.priceK":  {"note": "~$55K blended."}
    },
    ("4568", "japan_legacy", "japan"): {
        "us.reachPct": {"note": "Japan legacy portfolio (Edoxaban, Nilemdo, Benicar); minimal US; 5% placeholder reach."},
        "us.wtpPct":   {"note": "8% -- US commercial limited; Daiichi divested many US assets."},
        "us.priceK":   {"note": "~$2K blended retail US legacy."},
        "eu.reachPct": {"note": "10% -- EU edoxaban (Lixiana) mature."},
        "eu.wtpPct":   {"note": "15% -- HTA covered; generics encroach."},
        "eu.priceK":   {"note": "~$1K EU blended."},
        "row.reachPct":{"note": "35% -- Japan home market dominance; Asian rollout mature."},
        "row.wtpPct":  {"note": "55% -- Japan NHI entrenched."},
        "row.priceK":  {"note": "~$1.5K blended; Japan retail."}
    },

    # ============================================================
    # CRSP -- CRISPR Therapeutics
    # ============================================================
    ("CRSP", "casgevy", "scd_tdt"): {
        "us.reachPct": {"note": "Casgevy SCD + TDT approved Dec-2023; ~16K eligible US SCD/TDT; ~4% reach by 2026 given ATC capacity bottleneck (~40 centers), conditioning toxicity; 2024 CRSP share ~$10M (early ramp)."},
        "us.wtpPct":   {"note": "40% -- CMS gene therapy access model + Medicaid outcomes-based agreements (e.g. MI, TN); vein-to-vein 8-10mo; busulfan conditioning limits appeal."},
        "us.priceK":   {"note": "$2.2M WAC one-time; CRSP books 40% of Vertex ~$1.8M net US; amortized ~$440K/yr over 5yr."},
        "eu.reachPct": {"note": "3% -- EMA approved 2024; NICE/G-BA + Saudi RSPRC reimbursed 2024; France Italy in negotiation."},
        "eu.wtpPct":   {"note": "25% -- HTA cautious on one-time gene tx budget; outcomes-based deals required."},
        "eu.priceK":   {"note": "~$1.6M EU net (Vertex); CRSP gets 40% share."},
        "row.reachPct":{"note": "2% -- Saudi + Gulf leading; Brazil cohort; APAC limited; Africa SCD high-burden but no access."},
        "row.wtpPct":  {"note": "10% -- Saudi/UAE reimbursed; Brazil private; rest via sponsored programs."},
        "row.priceK":  {"note": "~$1.2M blended; Gulf $1.5M, Brazil $800K."}
    },
    ("CRSP", "ctx310", "cv_edit"): {
        "us.reachPct": {"note": "CTX310 ANGPTL3 in vivo LNP edit; Ph1 2025; 20% peak reach in HoFH/refractory lipid pts (2030+) vs Leqvio siRNA + evinacumab."},
        "us.wtpPct":   {"note": "35% -- one-time in vivo edit attractive; payors will require LDL/TG lowering durability >2yr + safety."},
        "us.priceK":   {"note": "~$750K one-time pricing vs Evkeeza $450K/yr annualized x5yr = $2.25M."},
        "eu.reachPct": {"note": "8% -- EMA 2031+; HTA skeptical of one-time gene edit durability."},
        "eu.wtpPct":   {"note": "18% -- EU HTA budget-cap on gene editing."},
        "eu.priceK":   {"note": "~$450K EU one-time."},
        "row.reachPct":{"note": "3% -- Japan early; ROW minimal."},
        "row.wtpPct":  {"note": "7% -- limited reimbursement."},
        "row.priceK":  {"note": "~$250K blended."}
    },
    ("CRSP", "ctx460", "aatd"): {
        "us.reachPct": {"note": "CTX460 AATD in vivo edit; preclinical; 15% peak reach (2031+) vs weekly IV AAT augmentation ~$125K/yr (Prolastin/Aralast/Zemaira)."},
        "us.wtpPct":   {"note": "30% -- one-time edit compelling vs lifelong IV but safety bar high."},
        "us.priceK":   {"note": "~$800K one-time premium vs IV AAT lifetime cost ~$2.5M."},
        "eu.reachPct": {"note": "6% -- EU augmentation limited; HTA cautious."},
        "eu.wtpPct":   {"note": "15% -- EU HTA scrutinized."},
        "eu.priceK":   {"note": "~$480K EU."},
        "row.reachPct":{"note": "2% -- ROW minimal."},
        "row.wtpPct":  {"note": "5% -- limited."},
        "row.priceK":  {"note": "~$250K blended."}
    },
    ("CRSP", "zugocel", "cart_ai"): {
        "us.reachPct": {"note": "CTX112 (zugocel) allo CD19 CAR-T for SLE/lupus + B-cell; Ph1 2025; 15% peak reach in refractory autoimmune pts (2030+)."},
        "us.wtpPct":   {"note": "30% -- allo CAR-T cost advantage vs auto; payors interested but durability TBD vs Cabaletta + Kyverna."},
        "us.priceK":   {"note": "~$350K one-time allo pricing vs auto CAR-T ~$500K."},
        "eu.reachPct": {"note": "6% -- EU SLE HTA rigorous."},
        "eu.wtpPct":   {"note": "15% -- HTA budget-capped."},
        "eu.priceK":   {"note": "~$220K EU."},
        "row.reachPct":{"note": "2% -- ROW minimal."},
        "row.wtpPct":  {"note": "5% -- limited."},
        "row.priceK":  {"note": "~$130K blended."}
    },
    ("CRSP", "discovery", "other"): {
        "us.reachPct": {"note": "Discovery-stage CRISPR programs; 5% aggregate reach (2033+); includes T1D beta cell + next-gen edits."},
        "us.wtpPct":   {"note": "15% -- earliest stage; payor uncertainty high."},
        "us.priceK":   {"note": "~$500K placeholder blended one-time."},
        "eu.reachPct": {"note": "2% -- speculative."},
        "eu.wtpPct":   {"note": "6% -- minimal."},
        "eu.priceK":   {"note": "~$300K EU."},
        "row.reachPct":{"note": "1% -- negligible."},
        "row.wtpPct":  {"note": "3% -- minimal."},
        "row.priceK":  {"note": "~$180K blended."}
    },

    # ============================================================
    # MDGL -- Madrigal Pharmaceuticals
    # ============================================================
    ("MDGL", "commercial", "mash"): {
        "us.reachPct": {"note": "Rezdiffra MASH F2/F3 approved Mar-2024 (first MASH therapy); ~600K US F2/F3 pts diagnosed; ~12% reach by 2026 as dx infra ramps; 2024 sales $180M launch, 2025E ~$800M."},
        "us.wtpPct":   {"note": "50% -- commercial + Medicare Part D covered w/ PA requiring fibrosis evidence (FibroScan/MRE); MASH dx still nascent in primary care."},
        "us.priceK":   {"note": "~$47K/yr WAC; ~$32K net after commercial rebates (~30% GTN) + 340B."},
        "eu.reachPct": {"note": "5% -- EMA filing 2025; launch 2026; HTA bodies awaiting MAESTRO outcomes OLE."},
        "eu.wtpPct":   {"note": "20% -- NICE/G-BA cautious on MASH prevalence + budget impact; expect managed entry."},
        "eu.priceK":   {"note": "~$20K EU net; ~40% of US post-HTA."},
        "row.reachPct":{"note": "2% -- Japan NASH interest; Korea/APAC partnerships TBD."},
        "row.wtpPct":  {"note": "6% -- Japan NHI 2027+; limited EM access."},
        "row.priceK":  {"note": "~$12K blended."}
    },
    ("MDGL", "f4c", "mash_f4"): {
        "us.reachPct": {"note": "Rezdiffra F4c compensated cirrhosis label expansion pending MAESTRO-NASH OLE + outcomes; 15% peak reach in F4 pts 2027+."},
        "us.wtpPct":   {"note": "45% -- PA hurdles higher for F4; payors require transplant-free survival data."},
        "us.priceK":   {"note": "~$47K/yr WAC parallel to F2/F3 pricing."},
        "eu.reachPct": {"note": "6% -- EU F4c 2028+; HTA tight budget."},
        "eu.wtpPct":   {"note": "20% -- HTA budget-cap."},
        "eu.priceK":   {"note": "~$20K EU."},
        "row.reachPct":{"note": "2% -- minimal ROW."},
        "row.wtpPct":  {"note": "5% -- limited."},
        "row.priceK":  {"note": "~$12K blended."}
    },
    ("MDGL", "combos", "mash_combo"): {
        "us.reachPct": {"note": "Rezdiffra + GLP-1 combo (semaglutide/tirzepatide) or FGF21 combos; 2028+; 20% peak reach as payors accept stacked MASH therapy."},
        "us.wtpPct":   {"note": "40% -- combinatorial pricing risk; payors will step-edit + require head-to-head fibrosis endpoint data."},
        "us.priceK":   {"note": "~$47K/yr Rezdiffra share (partner drug priced separately)."},
        "eu.reachPct": {"note": "5% -- EU combo uptake lagged."},
        "eu.wtpPct":   {"note": "15% -- HTA cautious on combos."},
        "eu.priceK":   {"note": "~$20K EU."},
        "row.reachPct":{"note": "2% -- ROW minimal."},
        "row.wtpPct":  {"note": "5% -- limited."},
        "row.priceK":  {"note": "~$12K blended."}
    },

    # ============================================================
    # TVTX -- Travere Therapeutics
    # ============================================================
    ("TVTX", "filspari_igan", "igan"): {
        "us.reachPct": {"note": "Filspari (sparsentan) IgAN full approval Sep-2024 via PROTECT OS; ~30-50K US IgAN dx; 25% peak reach vs Kerendia + Tarpeyo steroid + ACEi; 2024 sales $195M."},
        "us.wtpPct":   {"note": "55% -- NKF + nephrology KOL support; commercial + Medicare Part D cover w/ PA; hepatotoxicity REMS manageable."},
        "us.priceK":   {"note": "~$114K/yr WAC; ~$75K net after Medicare + commercial rebates; premium vs generics."},
        "eu.reachPct": {"note": "12% -- CSL Vifor EU partner; EMA approved 2024; NICE/G-BA reimbursed 2025 w/ conditions."},
        "eu.wtpPct":   {"note": "30% -- HTA accepts IgAN orphan + PROTECT data; budget modest; CSL commercial push."},
        "eu.priceK":   {"note": "~$60K EU net; CSL revenue share."},
        "row.reachPct":{"note": "5% -- Japan partnership via Kyowa Kirin; APAC rollout 2026+."},
        "row.wtpPct":  {"note": "12% -- Japan NHI expected; other APAC limited."},
        "row.priceK":  {"note": "~$35K blended; Japan $60K."}
    },
    ("TVTX", "filspari_fsgs", "fsgs"): {
        "us.reachPct": {"note": "Filspari FSGS sNDA pending DUPLEX Phase 3 OLE; ~40K US FSGS; 20% peak reach if approved 2026 given no FSGS-specific therapy."},
        "us.wtpPct":   {"note": "45% -- unmet need high; payors will cover w/ PA requiring biopsy-proven FSGS."},
        "us.priceK":   {"note": "~$114K/yr WAC parallel to IgAN pricing."},
        "eu.reachPct": {"note": "8% -- CSL Vifor EU; EMA 2026+ pending."},
        "eu.wtpPct":   {"note": "22% -- HTA FSGS orphan recognition."},
        "eu.priceK":   {"note": "~$60K EU net."},
        "row.reachPct":{"note": "3% -- Japan/APAC ramp 2027+."},
        "row.wtpPct":  {"note": "8% -- limited."},
        "row.priceK":  {"note": "~$35K blended."}
    },
    ("TVTX", "pegtibatinase", "hcu"): {
        "us.reachPct": {"note": "Pegtibatinase HCU (homocystinuria) Ph3 HARMONY; ultra-rare ~2K US pts; 30% peak reach as first enzyme replacement vs diet/betaine."},
        "us.wtpPct":   {"note": "50% -- HCU unmet need clear; payors will cover enzyme replacement rare disease precedent."},
        "us.priceK":   {"note": "~$450K/yr WAC ultra-rare ERT pricing in line with MPS/Pompe ERTs."},
        "eu.reachPct": {"note": "12% -- EMA 2027+; HTA accepts ultra-rare budget."},
        "eu.wtpPct":   {"note": "25% -- HTA reimbursement typical rare ERT pathway."},
        "eu.priceK":   {"note": "~$260K EU net."},
        "row.reachPct":{"note": "5% -- Japan/ROW ultra-rare rollout."},
        "row.wtpPct":  {"note": "10% -- Japan NHI expected."},
        "row.priceK":  {"note": "~$160K blended."}
    },

    # ============================================================
    # KRYS -- Krystal Biotech
    # ============================================================
    ("KRYS", "commercial", "deb"): {
        "us.reachPct": {"note": "VYJUVEK DEB topical HSV gene tx approved May-2023; ~3K US DEB pts; 55% peak reach given weekly/biweekly application, broad severity; 2024 sales $291M, 2025E ~$500M."},
        "us.wtpPct":   {"note": "75% -- debra + dermatology KOL strong advocacy; commercial + Medicaid cover w/ PA; first DEB therapy approved."},
        "us.priceK":   {"note": "~$630K/yr WAC weight-based; ~$490K net after Medicaid rebates; ~$24K/vial with chronic dosing."},
        "eu.reachPct": {"note": "20% -- EMA approved Apr-2025; launch Germany/UK 2025; pricing negotiations Italy/France/Spain."},
        "eu.wtpPct":   {"note": "40% -- HTA accepts DEB ultra-rare severe unmet need; G-BA 'considerable' expected."},
        "eu.priceK":   {"note": "~$380K EU net; ~60% of US."},
        "row.reachPct":{"note": "12% -- Japan PMDA pending; KRYS building global commercial; Brazil/MENA access."},
        "row.wtpPct":  {"note": "22% -- Japan NHI expected 2026; MENA Gulf tier reimbursement."},
        "row.priceK":  {"note": "~$250K blended; Japan $400K."}
    },
    ("KRYS", "kb803", "ocular_deb"): {
        "us.reachPct": {"note": "KB803 ophthalmic DEB eye mfg Ph3 IOLITE; ~30% of DEB pts have corneal scarring; 40% peak reach as line-extension for existing VYJUVEK pts."},
        "us.wtpPct":   {"note": "60% -- VYJUVEK pull-through; PAs straightforward given same molecule + infrastructure."},
        "us.priceK":   {"note": "~$150K/yr incremental WAC pricing; topical ocular gene tx premium."},
        "eu.reachPct": {"note": "15% -- EU launch 2027+; HTA benchmark vs VYJUVEK."},
        "eu.wtpPct":   {"note": "30% -- HTA covers orphan eye indication."},
        "eu.priceK":   {"note": "~$90K EU net."},
        "row.reachPct":{"note": "8% -- ROW follow-on launch."},
        "row.wtpPct":  {"note": "15% -- limited but growing."},
        "row.priceK":  {"note": "~$60K blended."}
    },
    ("KRYS", "kb801", "nk"): {
        "us.reachPct": {"note": "KB801 neurotrophic keratitis Ph1/2; ~65K US NK pts; 25% peak reach (2028+) vs Oxervate (cenegermin)."},
        "us.wtpPct":   {"note": "45% -- ophthalmology KOL open to gene tx vs weekly cenegermin drops; payors will compare cost-effectiveness."},
        "us.priceK":   {"note": "~$60K/yr WAC vs Oxervate ~$60K 8wk course."},
        "eu.reachPct": {"note": "10% -- EU launch 2029+; EMA rare ophth path."},
        "eu.wtpPct":   {"note": "20% -- HTA accepts NK orphan eye."},
        "eu.priceK":   {"note": "~$35K EU."},
        "row.reachPct":{"note": "4% -- ROW minimal."},
        "row.wtpPct":  {"note": "8% -- limited."},
        "row.priceK":  {"note": "~$20K blended."}
    },
    ("KRYS", "kb407", "cf"): {
        "us.reachPct": {"note": "KB407 CF inhaled HSV gene tx Ph1; ~10% CF pts non-modulator eligible; 15% peak reach in that subset (2030+) vs Trikafta ineligible."},
        "us.wtpPct":   {"note": "35% -- niche CF subpop; payors cautious on inhaled gene tx durability vs Trikafta $300K/yr."},
        "us.priceK":   {"note": "~$300K/yr WAC inhaled gene tx premium."},
        "eu.reachPct": {"note": "5% -- EU CF modulator-era restrictive HTA."},
        "eu.wtpPct":   {"note": "12% -- HTA tough on CF non-modulator."},
        "eu.priceK":   {"note": "~$180K EU."},
        "row.reachPct":{"note": "2% -- ROW CF population small ex-EU."},
        "row.wtpPct":  {"note": "5% -- limited."},
        "row.priceK":  {"note": "~$120K blended."}
    },
    ("KRYS", "kb707", "nsclc"): {
        "us.reachPct": {"note": "KB707 IL-2/IL-12 HSV oncolytic intratumoral NSCLC Ph1; 10% peak reach in checkpoint-refractory solid tumors (2030+)."},
        "us.wtpPct":   {"note": "30% -- crowded oncolytic space (T-VEC precedent limited); payors will demand OS benefit."},
        "us.priceK":   {"note": "~$180K/yr WAC oncolytic premium."},
        "eu.reachPct": {"note": "4% -- EU oncolytic uptake slow."},
        "eu.wtpPct":   {"note": "10% -- HTA skeptical."},
        "eu.priceK":   {"note": "~$110K EU."},
        "row.reachPct":{"note": "2% -- ROW minimal."},
        "row.wtpPct":  {"note": "5% -- limited."},
        "row.priceK":  {"note": "~$60K blended."}
    },
    ("KRYS", "kb111", "hhd"): {
        "us.reachPct": {"note": "KB111 Hailey-Hailey disease topical HSV gene tx; ~40K US HHD; 35% peak reach (2029+) as first HHD therapy."},
        "us.wtpPct":   {"note": "50% -- derm KOL enthusiasm; payors cover as orphan genodermatosis."},
        "us.priceK":   {"note": "~$300K/yr WAC HHD ultra-rare pricing parallel to DEB."},
        "eu.reachPct": {"note": "12% -- EU HHD dx registry strong; HTA accepts orphan."},
        "eu.wtpPct":   {"note": "25% -- HTA reimbursement expected."},
        "eu.priceK":   {"note": "~$180K EU."},
        "row.reachPct":{"note": "5% -- ROW limited."},
        "row.wtpPct":  {"note": "10% -- Japan possible."},
        "row.priceK":  {"note": "~$110K blended."}
    },

    # ============================================================
    # 6990 -- Kelun-Biotech / Kelun Pharmaceuticals (TROP2 + ADC franchise)
    # ============================================================
    ("6990", "commercial", "trop2"): {
        "us.reachPct": {"note": "Sac-TMT (SKB264/MK-2870) TROP2 ADC; partnered w/ Merck $1.4B; Ph3 NSCLC + TNBC + HR+ BC; 20% peak reach vs Trodelvy + Datroway."},
        "us.wtpPct":   {"note": "40% -- Merck commercial leverage in US; payors will compare cross-trial ORR/PFS vs Trodelvy."},
        "us.priceK":   {"note": "~$170K/yr WAC parallel to TROP2 ADC class."},
        "eu.reachPct": {"note": "10% -- Merck EU commercialization; EMA 2027+."},
        "eu.wtpPct":   {"note": "22% -- HTA budget-cap in TROP2 space."},
        "eu.priceK":   {"note": "~$100K EU net."},
        "row.reachPct":{"note": "30% -- China home market Sac-TMT approved Nov-2024 TNBC, NRDL 2025; broad hospital access; Kelun dominates domestic."},
        "row.wtpPct":  {"note": "40% -- China NRDL covered ~$25K/yr post-negotiation; Japan/Korea partnership."},
        "row.priceK":  {"note": "~$35K blended; China $25K tendered, Japan $80K."}
    },
    ("6990", "a166", "her2_adc"): {
        "us.reachPct": {"note": "A166 HER2 ADC Ph3; HER2+ BC/gastric; 8% peak reach (2029+) vs Enhertu dominance + other HER2 ADCs."},
        "us.wtpPct":   {"note": "20% -- tough to displace Enhertu in US; Merck leverage limited in HER2 class."},
        "us.priceK":   {"note": "~$180K/yr WAC parallel to HER2 ADC class."},
        "eu.reachPct": {"note": "4% -- EMA 2029+; HTA challenging vs Enhertu."},
        "eu.wtpPct":   {"note": "12% -- budget-cap."},
        "eu.priceK":   {"note": "~$110K EU."},
        "row.reachPct":{"note": "18% -- China domestic A166 NRDL target; Kelun strong."},
        "row.wtpPct":  {"note": "28% -- China NRDL ~$20K post-neg."},
        "row.priceK":  {"note": "~$25K blended; China $20K."}
    },
    ("6990", "skb315", "cldn"): {
        "us.reachPct": {"note": "SKB315 Claudin 18.2 ADC Ph1/2; gastric/pancreatic; 10% peak reach (2030+) vs Astellas zolbetuximab."},
        "us.wtpPct":   {"note": "25% -- crowded CLDN18.2 space (zolbetuximab mAb + multiple ADCs)."},
        "us.priceK":   {"note": "~$180K/yr WAC ADC class."},
        "eu.reachPct": {"note": "4% -- EU 2031+."},
        "eu.wtpPct":   {"note": "10% -- HTA budget-cap."},
        "eu.priceK":   {"note": "~$110K EU."},
        "row.reachPct":{"note": "15% -- China gastric prevalence high, NRDL target."},
        "row.wtpPct":  {"note": "22% -- China NRDL reimbursement."},
        "row.priceK":  {"note": "~$22K blended."}
    },
    ("6990", "merck_pipe", "merck_adc"): {
        "us.reachPct": {"note": "Merck-partnered Kelun ADC pipeline (~7 assets $9.3B total deal 2022-23); 12% aggregate peak reach across tumors."},
        "us.wtpPct":   {"note": "30% -- Merck commercial push; payor access indication-dependent."},
        "us.priceK":   {"note": "~$170K/yr WAC blended ADC class."},
        "eu.reachPct": {"note": "6% -- Merck EU rollout."},
        "eu.wtpPct":   {"note": "15% -- HTA selective."},
        "eu.priceK":   {"note": "~$100K EU."},
        "row.reachPct":{"note": "20% -- China co-commercialization retained."},
        "row.wtpPct":  {"note": "30% -- China NRDL gradual."},
        "row.priceK":  {"note": "~$25K blended."}
    },
    ("6990", "platform", "next_gen"): {
        "us.reachPct": {"note": "Next-gen ADC platform (topo + novel payloads); 6% aggregate peak reach (2033+)."},
        "us.wtpPct":   {"note": "18% -- early stage; payor uncertainty."},
        "us.priceK":   {"note": "~$170K/yr placeholder."},
        "eu.reachPct": {"note": "3% -- speculative."},
        "eu.wtpPct":   {"note": "8% -- minimal."},
        "eu.priceK":   {"note": "~$100K EU."},
        "row.reachPct":{"note": "10% -- China pipeline."},
        "row.wtpPct":  {"note": "18% -- China NRDL."},
        "row.priceK":  {"note": "~$20K blended."}
    },

    # ============================================================
    # RVMD -- Revolution Medicines
    # ============================================================
    ("RVMD", "darax_pdac", "pdac"): {
        "us.reachPct": {"note": "Daraxonrasib (RMC-6236) pan-RAS(ON) 2L+ PDAC; Ph3 RASolute 302 readout 2026; 35% peak reach in 2L+ PDAC given no approved post-gemcitabine/FOLFIRINOX options; ~90% of PDAC is RAS-mutated."},
        "us.wtpPct":   {"note": "60% -- unmet need dire (2L PDAC mOS ~3mo); NCCN will rapidly adopt if Ph3 OS HR <0.7; commercial + Medicare broad coverage."},
        "us.priceK":   {"note": "~$240K/yr WAC RAS TKI premium (vs Krazati $230K, Lumakras $200K); launch 2027E."},
        "eu.reachPct": {"note": "15% -- EMA 2028+; HTA accepts PDAC unmet need; NICE/G-BA budget-cap."},
        "eu.wtpPct":   {"note": "35% -- HTA OS premium for PDAC but budget impact large."},
        "eu.priceK":   {"note": "~$140K EU net."},
        "row.reachPct":{"note": "6% -- Japan PMDA priority; China partnership; APAC gradual."},
        "row.wtpPct":  {"note": "12% -- Japan NHI expected; China NRDL -60% typical."},
        "row.priceK":  {"note": "~$75K blended; Japan $140K, China $50K."}
    },
    ("RVMD", "darax_nsclc", "nsclc"): {
        "us.reachPct": {"note": "Daraxonrasib NSCLC G12 + other KRAS mutant; Ph3 RASolute-Lung 2026; 25% peak reach vs Krazati/Lumakras in G12C + expansion to G12D/V."},
        "us.wtpPct":   {"note": "50% -- NCCN adoption broad if pan-RAS efficacy; payors cover NSCLC KRAS TKIs established."},
        "us.priceK":   {"note": "~$240K/yr WAC pan-RAS premium."},
        "eu.reachPct": {"note": "12% -- EMA 2029+; HTA accepts NSCLC KRAS."},
        "eu.wtpPct":   {"note": "28% -- EU budget-cap but accepted."},
        "eu.priceK":   {"note": "~$140K EU."},
        "row.reachPct":{"note": "5% -- Japan/China rollout."},
        "row.wtpPct":  {"note": "10% -- gradual APAC."},
        "row.priceK":  {"note": "~$75K blended."}
    },
    ("RVMD", "zoldon", "g12d"): {
        "us.reachPct": {"note": "Zoldonrasib (RMC-9805) KRAS G12D(ON) selective; Ph1/1b; G12D most common KRAS (PDAC 40%, CRC 13%, NSCLC 4%); 25% peak reach 2029+."},
        "us.wtpPct":   {"note": "45% -- first selective G12D; payors will cover if ORR >30% + DoR >6mo."},
        "us.priceK":   {"note": "~$230K/yr WAC in line with Krazati."},
        "eu.reachPct": {"note": "10% -- EMA 2030+; HTA G12D positioning."},
        "eu.wtpPct":   {"note": "22% -- HTA budget-cap."},
        "eu.priceK":   {"note": "~$130K EU."},
        "row.reachPct":{"note": "4% -- ROW gradual."},
        "row.wtpPct":  {"note": "9% -- limited."},
        "row.priceK":  {"note": "~$65K blended."}
    },
    ("RVMD", "eliron", "g12c"): {
        "us.reachPct": {"note": "Elironrasib (RMC-6291) KRAS G12C(ON) + combos w/ daraxonrasib; Ph1/2; 20% peak reach in G12C post Krazati/Lumakras relapse."},
        "us.wtpPct":   {"note": "40% -- ON vs OFF state selectivity differentiates; payors step-edit after 1st-gen G12Ci."},
        "us.priceK":   {"note": "~$220K/yr WAC post-1st-gen G12Ci parity."},
        "eu.reachPct": {"note": "8% -- EU 2029+; HTA budget-cap vs Krazati."},
        "eu.wtpPct":   {"note": "18% -- HTA tough competition."},
        "eu.priceK":   {"note": "~$130K EU."},
        "row.reachPct":{"note": "3% -- ROW minimal."},
        "row.wtpPct":  {"note": "7% -- limited."},
        "row.priceK":  {"note": "~$60K blended."}
    },
    ("RVMD", "pipeline", "other_ras"): {
        "us.reachPct": {"note": "RAS(ON) pipeline (RMC-5552 mTORC1, RMC-0708 Q61, SHP2 combos); 10% aggregate peak reach (2030+)."},
        "us.wtpPct":   {"note": "25% -- early stage; payor uncertainty."},
        "us.priceK":   {"note": "~$220K/yr placeholder RAS class."},
        "eu.reachPct": {"note": "5% -- EU pipeline."},
        "eu.wtpPct":   {"note": "12% -- HTA budget."},
        "eu.priceK":   {"note": "~$130K EU."},
        "row.reachPct":{"note": "2% -- ROW minimal."},
        "row.wtpPct":  {"note": "5% -- limited."},
        "row.priceK":  {"note": "~$60K blended."}
    },
}
