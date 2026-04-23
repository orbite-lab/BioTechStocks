# -*- coding: utf-8 -*-
"""
Seed asset.targets[] from existing modality tags.

One-shot script that parses each asset's modality L3 string and writes a
best-guess targets[] list into the config. Intended to run once to
populate the new dimension; after this, targets are hand-edited in
configs like modality/area.

Target naming convention
------------------------
Prefer HGNC gene / protein symbols (TNF, NLRP3, GLP1R, KRAS, BTK, ERBB2).
For mutation-specific drugs: GENE_MUTATION (KRAS_G12C, KRAS_G12D, EGFR_L858R).
For pathway-level mechanisms without a single gene: PATHWAY_NAME in caps
(AMYLOID_BETA, HIV_INTEGRASE, HIV_RT, HIV_CAPSID, CALCIUM_MODULATOR).
For drugs targeting platforms / multi-target (TCEs, ADC platforms, etc.),
leave empty; editor adds per-asset.

Usage
-----
    py scripts/ops/seed_targets.py           # dry-run, print proposals
    py scripts/ops/seed_targets.py --write   # write targets[] into configs
"""
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS = ROOT / "configs"

# Modality-L3 -> list of target symbols
# Covers every L3 currently in data/taxonomy.json. Extend as new modalities
# are added to configs.
MAP: dict[str, list[str]] = {
    # ─── ADC ───
    "b7h3_adc":            ["CD276"],
    "cldn18_adc":          ["CLDN18"],
    "cmet_adc":            ["MET"],
    "folr1_adc":           ["FOLR1"],
    "her2_adc":            ["ERBB2"],
    "her3_adc":            ["ERBB3"],
    "nectin4_adc":         ["NECTIN4"],
    "trop2_adc":           ["TACSTD2"],
    "rdc_iadc_dac":        [],  # multi-payload platform
    "bdc_epha2":           ["EPHA2"],
    "bdc_nectin4":         ["NECTIN4"],
    "bicycle_platform":    [],  # platform, context-specific

    # ─── Aesthetic ───
    "dermal_filler":       [],

    # ─── Antibody ───
    "bcma_cd3":                  ["TNFRSF17", "CD3"],
    "cd19_arm_modulator":        ["CD19"],
    "cd20_cd3":                  ["MS4A1", "CD3"],
    "nav1_7_blocker":            ["SCN9A"],
    "nectin4_cd137":             ["NECTIN4", "TNFRSF9"],
    "tumor_activated_tce":       [],  # platform
    "fcrn_blocker":              ["FCGRT"],
    "anti_tnf_topical":          ["TNF"],
    "vegf_trap":                 ["VEGFA"],
    "anti_amyloid":              ["AMYLOID_BETA"],
    "anti_angptl3":              ["ANGPTL3"],
    "anti_c2_complement":        ["C2"],
    "anti_c5":                   ["C5"],
    "anti_cd40l":                ["CD40LG"],
    "anti_il13":                 ["IL13"],
    "anti_il17a":                ["IL17A"],
    "anti_il17a_f":              ["IL17A", "IL17F"],
    "anti_il23":                 ["IL23A"],
    "anti_il4ra":                ["IL4R"],
    "anti_lag3":                 ["LAG3"],
    "anti_pcsk9":                ["PCSK9"],
    "anti_pd1":                  ["PDCD1"],
    "anti_sclerostin":           ["SOST"],
    "anti_tnf":                  ["TNF"],
    "anti_ttr":                  ["TTR"],
    "musk_agonist":              ["MUSK"],

    # ─── Cell therapy ───
    "cd19_allo_car_t":              ["CD19"],
    "cd70_allo_car_t":              ["CD70"],
    "dual_cd19_cd70_allo_car_t":    ["CD19", "CD70"],
    "bcma_car_t":                   ["TNFRSF17"],
    "cd19_autoimmune":              ["CD19"],
    "cd19_car_t":                   ["CD19"],
    "lnp_car_t":                    [],  # platform

    # ─── Formulation modifier ───
    "fluidcrystal_incretin":   ["GLP1R"],
    "fluidcrystal_sc":         [],  # depot, target varies
    "dex_cyclodextrin":        ["NR3C1"],  # glucocorticoid receptor (dexamethasone)

    # ─── Gene editing / therapy ───
    "exvivo":                  [],  # context varies
    "invivo":                  [],
    "beta_sarcoglycan":        ["SGCB"],
    "micro_dystrophin":        ["DMD"],
    "hsv1_vector":             [],  # platform

    # ─── Nucleic acid ───
    "galnac_aso":              [],  # platform
    "dmpk":                    ["DMPK"],
    "dux4":                    ["DUX4"],
    "galnac_platform":         [],
    "galnac_platform_nextgen": [],
    "edon_pmo":                ["DMD"],
    "exon_skipping_pmo":       ["DMD"],
    "arrow_trirna":            [],
    "pcsk9_apoc3_dual":        ["PCSK9", "APOC3"],

    # ─── Peptide ───
    "glp1_gip":            ["GLP1R", "GIPR"],
    "glp1_gip_glucagon":   ["GLP1R", "GIPR", "GCGR"],
    "calcium_modulator":   ["CALCIUM_MODULATOR"],

    # ─── Radiopharm ───
    "lead212_target":      [],  # platform, target varies

    # ─── Recombinant protein ───
    "il15":                    ["IL15"],
    "il2":                     ["IL2"],
    "cbs":                     ["CBS"],
    "botulinum_cosmetic":      ["SNAP25"],
    "botulinum_type_a":        ["SNAP25"],

    # ─── Small molecule ───
    "triple_metabolic":            [],  # combination, multi-target
    "nlrp3_inhibitor":             ["NLRP3"],
    "cetp":                        ["CETP"],
    "cyp11b1":                     ["CYP11B1"],
    "factor_xa":                   ["F10"],
    "integrase":                   ["HIV_INTEGRASE"],
    "nrti":                        ["HIV_RT"],
    "pde4":                        ["PDE4B", "PDE4D"],
    "scd1":                        ["SCD"],
    "5ht2a_agonist":               ["HTR2A"],
    "apelin_agonist":              ["APLNR"],
    "casr_antagonist":             ["CASR"],
    "cgrp_antagonist":             ["CALCRL"],
    "d2_d3_partial_agonist":       ["DRD2", "DRD3"],
    "eta_at1_antagonist":          ["EDNRA", "AGTR1"],
    "glp1_oral_agonist":           ["GLP1R"],
    "m4_muscarinic_agonist":       ["CHRM4"],
    "mc4r_agonist":                ["MC4R"],
    "muscarinic_agonist":          ["CHRM1", "CHRM4"],
    "muscarinic_m1_m4_agonist":    ["CHRM1", "CHRM4"],
    "s1p_modulator":               ["S1PR1"],
    "ampa_modulator":              ["GRIA1"],
    "gaba_modulator":              ["GABRA1"],
    "k_atp_opener":                ["KCNJ11"],
    "kv7_opener":                  ["KCNQ2", "KCNQ3"],
    "nav_blocker":                 ["SCN1A"],
    "nmda_modulator":              ["GRIN2B"],
    "nmda_sigma1_modulator":       ["GRIN2B", "SIGMAR1"],
    "sv2a_modulator":              ["SV2A"],
    "alk":                         ["ALK"],
    "btk_bcl2_next_gen":           ["BTK", "BCL2"],
    "btk_covalent":                ["BTK"],
    "btk_reversible":              ["BTK"],
    "cdk4_6":                      ["CDK4", "CDK6"],
    "fgfr3":                       ["FGFR3"],
    "her2":                        ["ERBB2"],
    "itk":                         ["ITK"],
    "jak1_selective":              ["JAK1"],
    "jak1_topical":                ["JAK1"],
    "p38_mapk":                    ["MAPK14"],
    "pi3k":                        ["PIK3CA"],
    "ras_on_inhibitor":            ["KRAS", "NRAS", "HRAS"],
    "ros1":                        ["ROS1"],
    "thr_beta_agonist":            ["THRB"],
    "btk_cdac":                    ["BTK"],
    "kinesin_degrader":            ["KIF11"],
    "mode_platform":               [],
    "molecular_glue":              [],
    "bcl2":                        ["BCL2"],
    "dat_net_inhibitor":           ["SLC6A3", "SLC6A2"],
    "dri":                         ["SLC6A3"],
    "ttr":                         ["TTR"],
    "ribitol":                     ["FKRP"],
    "sglt2":                       ["SLC5A2"],
    "vmat2":                       ["SLC18A2"],
    "capsid_inhibitor":            ["HIV_CAPSID"],
    "vlp_conjugate":               [],  # antigen varies
}


def infer_targets(modality: str) -> list[str]:
    """Return best-guess target symbols from a modality string (L1.L2.L3).

    Matches on the L3 segment only. Unknown L3 -> empty list (editor must
    provide targets manually).
    """
    if not modality:
        return []
    parts = modality.split(".")
    l3 = parts[-1]
    return list(MAP.get(l3, []))


def main():
    write = "--write" in sys.argv
    manifest = json.loads((CONFIGS / "manifest.json").read_text(encoding="utf-8"))
    touched, empty, preserved = 0, 0, 0
    empty_rows = []
    for t in manifest:
        path = CONFIGS / f"{t}.json"
        if not path.exists():
            continue
        cfg = json.loads(path.read_text(encoding="utf-8"))
        dirty = False
        for a in cfg.get("assets", []):
            current = a.get("targets")
            inferred = infer_targets(a.get("modality", ""))
            if current is None:
                # Never set -- seed it
                a["targets"] = inferred
                dirty = True
                if inferred:
                    touched += 1
                else:
                    empty += 1
                    empty_rows.append((t, a["id"], a.get("modality", "")))
            else:
                preserved += 1
        if dirty and write:
            path.write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n",
                            encoding="utf-8")
    print(f"Seeded targets on {touched} assets.")
    print(f"{empty} assets have empty targets[] (platform / mechanism-only / needs manual).")
    print(f"{preserved} assets already had targets[] (preserved).")
    if empty_rows:
        print("\nManual review needed (targets left empty):")
        for t, aid, mod in empty_rows:
            print(f"  {t:6} {aid:18} modality={mod}")
    if not write:
        print("\nDry run. Re-run with --write to apply.")


if __name__ == "__main__":
    main()
