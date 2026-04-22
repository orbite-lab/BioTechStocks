# -*- coding: utf-8 -*-
"""Bulk-add display labels for all remaining modality L2/L3 keys
(antibody, nucleic_acid, gene_therapy, cell_therapy, adc, peptide,
recombinant_protein, gene_editing, radiopharmaceutical, vaccine,
formulation_modifier, aesthetic_or_other).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
TAX = ROOT / "data" / "taxonomy.json"

NEW_LABELS = {
    # ============= L2 buckets =============
    "monoclonal":              "Monoclonal antibody (mAb)",
    "bispecific":              "Bispecific antibody (TCE / agonist)",
    "fc_fragment":             "Antibody fragment (Fc / scFv)",
    "fusion":                  "Antibody fusion protein",
    "dxd_linker":              "DXd-linker ADC",
    "multi_payload":           "Multi-payload ADC / iADC / DAC",
    "peptide_drug_conjugate":  "Peptide-drug conjugate (PDC)",
    "car_t_autologous":        "Autologous CAR-T",
    "car_t_allogeneic":        "Allogeneic CAR-T (off-the-shelf)",
    "car_t_in_vivo":           "In vivo CAR-T (LNP-delivered)",
    "aav":                     "AAV gene therapy",
    "gene_replacement":        "Gene replacement (non-AAV vector)",
    "crispr_cas9":             "CRISPR-Cas9 editing",
    "antisense":               "Antisense oligonucleotide (ASO)",
    "sirna":                   "Small interfering RNA (siRNA)",
    "trirna":                  "Tri-targeted RNAi (multi-target)",
    "splice_modulator":        "Splice-modulating PMO",
    "incretin":                "Incretin (GLP-1 family)",
    "cytokine":                "Recombinant cytokine",
    "enzyme":                  "Recombinant enzyme",
    "toxin":                   "Bacterial toxin",
    "radio_conjugate":         "Radio-conjugate",
    "radio_ligand":            "Radio-ligand therapy (RLT)",
    "radio_immunotherapy":     "Radio-immunotherapy (RIT)",
    "alpha_emitter":           "Alpha-particle emitter",
    "beta_emitter":            "Beta-particle emitter",
    "protein_subunit":         "Protein subunit vaccine",
    "vlp_conjugate":           "VLP conjugate vaccine",
    "mrna_vaccine":            "mRNA vaccine",
    "viral_vector":            "Viral-vector vaccine",
    "long_acting":             "Long-acting depot",
    "half_life_extender":      "Half-life extender",
    "oral_reformulation":      "Oral reformulation",
    "subq_to_iv":              "SubQ co-formulation (IV-to-SubQ)",
    "subq_to_oral":            "Oral peptide carrier (SubQ-to-oral)",
    "ocular_sustained":        "Sustained ocular delivery",
    "cns_delivery":            "CNS delivery (BBB shuttle / intrathecal)",
    "hyaluronic_acid":         "Hyaluronic acid filler",
    "hormone":                 "Peptide hormone",
    "cyclic_peptide":          "Cyclic peptide",
    "bicycle_peptide":         "Bicycle peptide (constrained)",
    "nk_cell":                 "NK cell therapy",
    "tcr_engineered":          "TCR-engineered T cell",
    "lentivirus":              "Lentiviral gene therapy",
    "non_viral":               "Non-viral gene delivery",
    "base_editing":            "Base editing (BE3 / ABE / CBE)",
    "prime_editing":           "Prime editing",
    "zinc_finger":             "Zinc-finger nuclease",
    "mrna_therapeutic":        "mRNA therapeutic",
    "saRNA":                   "Small activating RNA (saRNA)",

    # ============= L3 (target-based) =============
    # Antibody targets
    "anti_amyloid":      "Anti-amyloid (AD)",
    "anti_angptl3":      "Anti-ANGPTL3",
    "anti_c2_complement":"Anti-C2 complement",
    "anti_c5":           "Anti-C5 complement",
    "anti_cd40l":        "Anti-CD40L",
    "anti_il13":         "Anti-IL-13",
    "anti_il17a":        "Anti-IL-17A",
    "anti_il17a_f":      "Anti-IL-17A/F",
    "anti_il23":         "Anti-IL-23",
    "anti_il4ra":        "Anti-IL-4Ra (Dupixent class)",
    "anti_lag3":         "Anti-LAG-3",
    "anti_pcsk9":        "Anti-PCSK9",
    "anti_pd1":          "Anti-PD-1",
    "anti_sclerostin":   "Anti-sclerostin",
    "anti_tnf":          "Anti-TNF-alpha",
    "anti_ttr":          "Anti-TTR",
    "anti_vegf":         "Anti-VEGF",
    "musk_agonist":      "Anti-MuSK agonist",
    "vegf_trap":         "VEGF-Trap (Eylea)",
    "fcrn_blocker":      "FcRn blocker",

    # Bispecifics
    "bcma_cd3":            "BCMA x CD3 bispecific",
    "cd19_arm_modulator":  "CD19-arm modulator",
    "cd20_cd3":            "CD20 x CD3 bispecific",
    "nav1_7_blocker":      "Nav1.7 ion-channel bispecific",
    "nectin4_cd137":       "Nectin-4 x CD137 (4-1BB) bispecific agonist",
    "tumor_activated_tce": "Tumor-activated T-cell engager",

    # ADCs (target_adc -> "Target ADC")
    "b7h3_adc":         "B7-H3 ADC",
    "cldn18_adc":       "CLDN18.2 ADC",
    "cmet_adc":         "c-MET ADC",
    "folr1_adc":        "FRalpha ADC",
    "her2_adc":         "HER2 ADC",
    "her3_adc":         "HER3 ADC",
    "nectin4_adc":      "Nectin-4 ADC",
    "trop2_adc":        "TROP2 ADC",
    "rdc_iadc_dac":     "Multi-payload ADC platform",
    "bdc_epha2":        "EphA2 PDC (Bicycle)",
    "bdc_nectin4":      "Nectin-4 PDC (Bicycle)",
    "bicycle_platform": "Bicycle Therapeutics platform",

    # Cell therapy CAR-T targets
    "cd19_car_t":               "CD19 CAR-T",
    "cd19_autoimmune":          "CD19 CAR-T (autoimmune indication)",
    "bcma_car_t":               "BCMA CAR-T",
    "cd19_allo_car_t":          "CD19 allogeneic CAR-T",
    "cd70_allo_car_t":          "CD70 allogeneic CAR-T",
    "dual_cd19_cd70_allo_car_t":"CD19/CD70 dual allogeneic CAR-T",
    "lnp_car_t":                "LNP-delivered in vivo CAR-T",

    # Gene therapy / editing transgenes
    "beta_sarcoglycan":   "beta-sarcoglycan AAV (LGMD2E)",
    "micro_dystrophin":   "Micro-dystrophin AAV (DMD)",
    "hsv1_vector":        "HSV-1 vector gene therapy",
    "exvivo":             "Ex vivo CRISPR (cell-engineered)",
    "invivo":             "In vivo CRISPR (LNP-delivered)",

    # Nucleic acid
    "galnac_aso":            "GalNAc-conjugated ASO",
    "galnac_platform":       "GalNAc siRNA platform (1st gen)",
    "galnac_platform_nextgen":"GalNAc siRNA platform (next-gen)",
    "dmpk":                  "DMPK siRNA (DM1)",
    "dux4":                  "DUX4 siRNA (FSHD)",
    "edon_pmo":              "Exon-skipping PMO (PEPG platform)",
    "exon_skipping_pmo":     "Exon-skipping PMO (Sarepta)",
    "arrow_trirna":          "Arrowhead Tri-RNA platform",
    "pcsk9_apoc3_dual":      "PCSK9 + APOC3 dual siRNA",

    # Peptides (incretin family)
    "glp1_gip":              "Dual GLP-1 / GIP agonist (tirzepatide)",
    "glp1_gip_glucagon":     "Triple GLP-1 / GIP / glucagon agonist (retatrutide)",

    # Recombinant proteins
    "il2":                  "IL-2 (rezpegaldesleukin class)",
    "il15":                 "IL-15 (NKTR-255 class)",
    "cbs":                  "Cystathionine beta-synthase (homocystinuria)",
    "botulinum_type_a":     "Botulinum toxin type A (therapeutic)",
    "botulinum_cosmetic":   "Botulinum toxin (cosmetic)",

    # Radiopharmaceutical
    "lead212_target":       "Lead-212 alpha radio-conjugate",

    # Vaccine
    # vlp_conjugate already in L2 above; specific assets share that label

    # Formulation
    "fluidcrystal_sc":         "FluidCrystal subcutaneous depot",
    "fluidcrystal_incretin":   "FluidCrystal monthly incretin",

    # Aesthetic
    "dermal_filler":           "Dermal filler",
}

def main():
    tax = json.loads(TAX.read_text(encoding="utf-8"))
    existing = tax.get("display_names", {})
    new_count = 0
    overwrite_count = 0
    for k, v in NEW_LABELS.items():
        if k in existing and existing[k] != v:
            overwrite_count += 1
        elif k not in existing:
            new_count += 1
        existing[k] = v
    tax["display_names"] = existing
    TAX.write_text(json.dumps(tax, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"display_names total: {len(existing)} ({new_count} new, {overwrite_count} overwritten)")

if __name__ == "__main__":
    main()
