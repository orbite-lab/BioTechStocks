# -*- coding: utf-8 -*-
"""Restructure small_molecule taxonomy: consolidate duplicates, fix misclassified
items, rename L3s for clarity. Also add display_names map to taxonomy.json.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS = ROOT / "configs"

MIGRATIONS = {
    # === ion_channel + ion_channel_modulator merge ===
    "small_molecule.ion_channel_modulator.kv7_opener":          "small_molecule.ion_channel.kv7_opener",
    "small_molecule.ion_channel_modulator.nav_channel":         "small_molecule.ion_channel.nav_blocker",
    "small_molecule.ion_channel_modulator.nav_channel_blocker": "small_molecule.ion_channel.nav_blocker",

    # === Misclassified GPCR targets ===
    "small_molecule.enzyme_inhibitor.s1p_modulator":   "small_molecule.gpcr.s1p_modulator",
    "small_molecule.gpcr_agonist.oral_glp1":           "small_molecule.gpcr.glp1_oral_agonist",
    "small_molecule.gpcr_modulator.mc4r_agonist":      "small_molecule.gpcr.mc4r_agonist",
    "small_molecule.gpcr_modulator.muscarinic_agonist":"small_molecule.gpcr.muscarinic_agonist",
    "small_molecule.receptor_agonist.m4_muscarinic_agonist": "small_molecule.gpcr.m4_muscarinic_agonist",
    "small_molecule.receptor_agonist.muscarinic_m1_m4":      "small_molecule.gpcr.muscarinic_m1_m4_agonist",
    "small_molecule.receptor_antagonist.cgrp_antagonist":    "small_molecule.gpcr.cgrp_antagonist",
    "small_molecule.receptor_antagonist.casr_antagonist":    "small_molecule.gpcr.casr_antagonist",
    "small_molecule.receptor_antagonist.d2_d3_partial_agonist":"small_molecule.gpcr.d2_d3_partial_agonist",
    "small_molecule.receptor_antagonist.eta_at1_dual":       "small_molecule.gpcr.eta_at1_antagonist",
    "small_molecule.psychedelic_compound.mm120_lsd":         "small_molecule.gpcr.5ht2a_agonist",

    # === Misclassified ion-channel receptors ===
    "small_molecule.receptor_antagonist.ampa_modulator":  "small_molecule.ion_channel.ampa_modulator",
    "small_molecule.receptor_antagonist.nmda_modulator":  "small_molecule.ion_channel.nmda_modulator",
    "small_molecule.receptor_antagonist.nmda_sigma1":     "small_molecule.ion_channel.nmda_sigma1_modulator",

    # === JAK is a kinase ===
    "small_molecule.jak_inhibitor.jak1_selective": "small_molecule.kinase_inhibitor.jak1_selective",
    "small_molecule.jak_inhibitor.jak1_topical":   "small_molecule.kinase_inhibitor.jak1_topical",

    # === p38 MAPK is a kinase ===
    "small_molecule.enzyme_inhibitor.p38_mapk_inhibitor": "small_molecule.kinase_inhibitor.p38_mapk",

    # === Transporter targets get their own L2 ===
    "small_molecule.enzyme_inhibitor.sglt2_inhibitor":     "small_molecule.transporter_inhibitor.sglt2",
    "small_molecule.receptor_antagonist.vmat2_inhibitor":  "small_molecule.transporter_inhibitor.vmat2",

    # === Rename L3s for clarity ===
    "small_molecule.enzyme_inhibitor.bcl2_inhibitor":    "small_molecule.enzyme_inhibitor.bcl2",
    "small_molecule.enzyme_inhibitor.cetp_inhibitor":    "small_molecule.enzyme_inhibitor.cetp",
    "small_molecule.enzyme_inhibitor.cyp11b1_inhibitor": "small_molecule.enzyme_inhibitor.cyp11b1",
    "small_molecule.enzyme_inhibitor.factor_xa_inhibitor": "small_molecule.enzyme_inhibitor.factor_xa",
    "small_molecule.enzyme_inhibitor.integrase_inhibitor": "small_molecule.enzyme_inhibitor.integrase",
    "small_molecule.enzyme_inhibitor.pde4_inhibitor":    "small_molecule.enzyme_inhibitor.pde4",
    "small_molecule.enzyme_inhibitor.scd1_inhibitor":    "small_molecule.enzyme_inhibitor.scd1",
    "small_molecule.enzyme_inhibitor.diazoxide":         "small_molecule.ion_channel.k_atp_opener",  # diazoxide opens KATP
    "small_molecule.enzyme_inhibitor.ribitol_substrate": "small_molecule.substrate_replacement.ribitol",
    "small_molecule.enzyme_inhibitor.nrti":              "small_molecule.enzyme_inhibitor.nrti",  # keep -- common HIV abbrev

    "small_molecule.kinase_inhibitor.btk_inhibitor":  "small_molecule.kinase_inhibitor.btk_reversible",
    "small_molecule.kinase_inhibitor.bcl2_btk_next_gen": "small_molecule.kinase_inhibitor.btk_bcl2_next_gen",
    "small_molecule.kinase_inhibitor.her2_kinase":    "small_molecule.kinase_inhibitor.her2",
    "small_molecule.kinase_inhibitor.alk_inhibitor":  "small_molecule.kinase_inhibitor.alk",
    "small_molecule.kinase_inhibitor.cdk4_6_inhibitor": "small_molecule.kinase_inhibitor.cdk4_6",
    "small_molecule.kinase_inhibitor.fgfr3_inhibitor": "small_molecule.kinase_inhibitor.fgfr3",
    "small_molecule.kinase_inhibitor.itk_inhibitor":  "small_molecule.kinase_inhibitor.itk",
    "small_molecule.kinase_inhibitor.pi3k_inhibitor": "small_molecule.kinase_inhibitor.pi3k",
    "small_molecule.kinase_inhibitor.ros1_inhibitor": "small_molecule.kinase_inhibitor.ros1",

    "small_molecule.protein_degrader.mode_trap":      "small_molecule.protein_degrader.mode_platform",

    "small_molecule.reuptake_inhibitor.dat_net":      "small_molecule.reuptake_inhibitor.dat_net_inhibitor",
    "small_molecule.receptor_antagonist.dri_modulator": "small_molecule.reuptake_inhibitor.dri",

    # capsid_inhibitor stays in receptor_antagonist (HIV capsid is non-GPCR non-channel target)
    "small_molecule.receptor_antagonist.capsid_inhibitor": "small_molecule.viral_target.capsid_inhibitor",

    "small_molecule.nuclear_receptor.thr_beta_agonist": "small_molecule.nuclear_receptor.thr_beta_agonist",  # already clean
    "small_molecule.stabilizer.ttr_stabilizer":         "small_molecule.stabilizer.ttr",

    "small_molecule.combination.thr_beta_glp1_dgat2":  "small_molecule.combination.triple_metabolic",
}

# Display names: friendly UI labels for L1/L2/L3 modality keys.
# Used by index.html / model.html when rendering the Tech Explorer.
DISPLAY_NAMES = {
    # L1
    "small_molecule": "Small molecule",
    "peptide": "Peptide",
    "antibody": "Antibody",
    "adc": "Antibody-drug conjugate",
    "recombinant_protein": "Recombinant protein",
    "cell_therapy": "Cell therapy",
    "gene_therapy": "Gene therapy",
    "gene_editing": "Gene editing",
    "nucleic_acid": "Nucleic acid (RNA-modulating)",
    "radiopharmaceutical": "Radiopharmaceutical",
    "vaccine": "Vaccine",
    "formulation_modifier": "Formulation platform",
    "aesthetic_or_other": "Aesthetic / other",

    # small_molecule L2
    "enzyme_inhibitor": "Enzyme inhibitor",
    "kinase_inhibitor": "Kinase inhibitor",
    "protein_degrader": "Protein degrader",
    "gpcr": "GPCR (G-protein coupled receptor)",
    "ion_channel": "Ion channel",
    "transporter_inhibitor": "Transporter inhibitor",
    "reuptake_inhibitor": "Monoamine reuptake inhibitor",
    "receptor_antagonist": "Receptor antagonist (other)",
    "viral_target": "Viral target",
    "nuclear_receptor": "Nuclear receptor",
    "stabilizer": "Conformational stabilizer",
    "substrate_replacement": "Substrate replacement",
    "combination": "Fixed-dose combination",

    # small_molecule L3 (selected -- common abbreviations expanded)
    "bcl2": "BCL-2 inhibitor",
    "cetp": "CETP inhibitor",
    "cyp11b1": "CYP11B1 inhibitor",
    "factor_xa": "Factor Xa inhibitor",
    "integrase": "HIV integrase inhibitor",
    "nrti": "Nucleoside reverse transcriptase inhibitor (NRTI)",
    "pde4": "PDE4 inhibitor",
    "scd1": "SCD1 inhibitor",
    "btk_covalent": "BTK inhibitor (covalent)",
    "btk_reversible": "BTK inhibitor (reversible)",
    "btk_bcl2_next_gen": "Next-gen BTK / BCL-2",
    "btk_cdac": "BTK chimeric degrader (CDAC)",
    "her2": "HER2 kinase inhibitor",
    "alk": "ALK inhibitor",
    "cdk4_6": "CDK4/6 inhibitor",
    "fgfr3": "FGFR3 inhibitor",
    "itk": "ITK inhibitor",
    "pi3k": "PI3K inhibitor",
    "p38_mapk": "p38 MAPK inhibitor",
    "ras_on_inhibitor": "RAS(ON) inhibitor",
    "ros1": "ROS1 inhibitor",
    "jak1_selective": "JAK1-selective inhibitor",
    "jak1_topical": "JAK1 topical inhibitor",
    "molecular_glue": "Molecular glue degrader",
    "mode_platform": "MoDE-trap degrader (BHVN platform)",
    "kinesin_degrader": "Kinesin degrader",
    "glp1_oral_agonist": "Oral GLP-1 agonist",
    "mc4r_agonist": "MC4R agonist",
    "muscarinic_agonist": "Muscarinic agonist",
    "muscarinic_m1_m4_agonist": "M1/M4 muscarinic agonist",
    "m4_muscarinic_agonist": "M4-selective muscarinic agonist",
    "cgrp_antagonist": "CGRP receptor antagonist",
    "casr_antagonist": "Calcium-sensing receptor antagonist",
    "d2_d3_partial_agonist": "D2/D3 partial agonist",
    "eta_at1_antagonist": "Endothelin-A + AT1 dual antagonist",
    "s1p_modulator": "S1P receptor modulator",
    "5ht2a_agonist": "5-HT2A receptor agonist (psychedelic)",
    "gaba_modulator": "GABA-A modulator",
    "sv2a_modulator": "SV2A modulator",
    "kv7_opener": "Kv7 channel opener",
    "nav_blocker": "Nav channel blocker",
    "ampa_modulator": "AMPA receptor modulator",
    "nmda_modulator": "NMDA receptor modulator",
    "nmda_sigma1_modulator": "NMDA + sigma-1 modulator",
    "k_atp_opener": "K-ATP channel opener (diazoxide)",
    "sglt2": "SGLT2 inhibitor",
    "vmat2": "VMAT2 inhibitor",
    "dat_net_inhibitor": "DAT/NET reuptake inhibitor",
    "dri": "Dopamine reuptake inhibitor (DRI)",
    "capsid_inhibitor": "HIV capsid inhibitor",
    "thr_beta_agonist": "Thyroid hormone receptor-beta agonist",
    "ttr": "TTR stabilizer",
    "ribitol": "Ribitol substrate replacement (LGMD2I)",
    "triple_metabolic": "THR-β + GLP-1 + DGAT2 triple combo",
}


def main():
    write = "--write" in sys.argv[1:]
    manifest = json.loads((CONFIGS / "manifest.json").read_text(encoding="utf-8"))
    changes = []
    for tk in sorted(manifest):
        path = CONFIGS / f"{tk}.json"
        if not path.exists():
            continue
        c = json.loads(path.read_text(encoding="utf-8"))
        ticker_changes = []
        for a in c.get("assets", []):
            mod = a.get("modality")
            if mod and mod in MIGRATIONS:
                new = MIGRATIONS[mod]
                if new != mod:
                    ticker_changes.append(f"  {a['id']:18s}  {mod}  ->  {new}")
                    a["modality"] = new
        if ticker_changes:
            changes.append(f"=== {tk} ===")
            changes.extend(ticker_changes)
            if write:
                path.write_text(json.dumps(c, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for line in changes:
        print(line)
    n_assets = len(changes) - sum(1 for c in changes if c.startswith("==="))
    n_tickers = sum(1 for c in changes if c.startswith("==="))
    print(f"\n{n_tickers} tickers, {n_assets} asset retags")

    # Update taxonomy.json with display_names map
    if write:
        tax_path = ROOT / "data" / "taxonomy.json"
        tax = json.loads(tax_path.read_text(encoding="utf-8"))
        tax["display_names"] = DISPLAY_NAMES
        tax_path.write_text(json.dumps(tax, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"\n[WROTE] data/taxonomy.json display_names ({len(DISPLAY_NAMES)} entries)")
    else:
        print("\n[DRY-RUN] use --write to save")


if __name__ == "__main__":
    main()
