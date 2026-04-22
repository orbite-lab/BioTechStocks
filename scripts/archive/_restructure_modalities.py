# -*- coding: utf-8 -*-
"""One-shot: restructure modality taxonomy across all configs.

Migrations:
  Mechanism vs structure cleanup
    antibody.agonist_antibody.X     -> antibody.monoclonal.X
    antibody.bispecific_agonist.X   -> antibody.bispecific.X
    antibody.fc_fragment.vegf_trap  -> antibody.fusion.vegf_trap

  Duplicates / misplaced
    rna_interference.sirna.X        -> nucleic_acid.sirna.X
    gene_therapy.oligonucleotide_splice.X -> nucleic_acid.splice_modulator.X
    gene_therapy.gene_editing.X     -> gene_editing.crispr_cas9.exvivo|invivo
    adc.radioconjugate.X            -> radiopharmaceutical.radio_conjugate.X

  Pegylated -> recombinant_protein
    pegylated_protein.pegylated_cytokine.peg_X -> recombinant_protein.cytokine.X
    pegylated_protein.pegylated_enzyme.peg_X   -> recombinant_protein.enzyme.X

  Vague "biologic" -> proper homes
    biologic.neurotoxin.X      -> recombinant_protein.toxin.X
    biologic.hyaluronic_acid.X -> aesthetic_or_other.hyaluronic_acid.X

  Cell therapy: indication-tagged -> structural class
    cell_therapy.car_t_autoimmune.cd19_autoimmune -> cell_therapy.car_t_autologous.cd19_autoimmune

  Formulation: rename
    formulation_platform.long_acting_depot.X -> formulation_modifier.long_acting.X

  siRNA target consistency (galnac is delivery, not L3)
    nucleic_acid.sirna.galnac_sirna         -> nucleic_acid.sirna.galnac_platform
    nucleic_acid.sirna.galnac_sirna_nextgen -> nucleic_acid.sirna.galnac_platform_nextgen
    (these stay because they're ALNY platform-level pipeline tags; specific
    targets get their own L3 when assets are added)
"""
from __future__ import annotations
import json, sys
from pathlib import Path

CONFIGS = Path(__file__).resolve().parent.parent.parent / "configs"

MIGRATIONS = {
    # mechanism -> merge into parent structural class
    "antibody.agonist_antibody.musk_agonist":           "antibody.monoclonal.musk_agonist",
    "antibody.bispecific_agonist.nectin4_x_cd137":      "antibody.bispecific.nectin4_cd137",
    "antibody.fc_fragment.vegf_trap":                    "antibody.fusion.vegf_trap",

    # rna_interference duplicate of nucleic_acid.sirna
    "rna_interference.sirna.dmpk":                       "nucleic_acid.sirna.dmpk",
    "rna_interference.sirna.dux4":                       "nucleic_acid.sirna.dux4",

    # exon-skipping PMOs are RNA-modulating, not DNA delivery
    "gene_therapy.oligonucleotide_splice.edon_pmo":      "nucleic_acid.splice_modulator.edon_pmo",
    "gene_therapy.oligonucleotide_splice.exon_skipping_pmo": "nucleic_acid.splice_modulator.exon_skipping_pmo",

    # gene_editing promoted to L1
    "gene_therapy.gene_editing.crispr_cas9_exvivo":      "gene_editing.crispr_cas9.exvivo",
    "gene_therapy.gene_editing.crispr_cas9_invivo":      "gene_editing.crispr_cas9.invivo",

    # radioconjugates aren't ADCs
    "adc.radioconjugate.brc_lead212":                    "radiopharmaceutical.radio_conjugate.lead212_target",

    # pegylated_protein -> recombinant_protein
    "pegylated_protein.pegylated_cytokine.peg_il2":      "recombinant_protein.cytokine.il2",
    "pegylated_protein.pegylated_cytokine.peg_il15":     "recombinant_protein.cytokine.il15",
    "pegylated_protein.pegylated_enzyme.peg_cbs":        "recombinant_protein.enzyme.cbs",

    # biologic catch-all -> proper homes
    "biologic.neurotoxin.botulinum_cosmetic":            "recombinant_protein.toxin.botulinum_cosmetic",
    "biologic.neurotoxin.botulinum_type_a":              "recombinant_protein.toxin.botulinum_type_a",
    "biologic.hyaluronic_acid.dermal_filler":            "aesthetic_or_other.hyaluronic_acid.dermal_filler",

    # car_t_autoimmune is indication-tagged, not structural
    "cell_therapy.car_t_autoimmune.cd19_autoimmune":     "cell_therapy.car_t_autologous.cd19_autoimmune",

    # formulation platform rename + L2 simplification
    "formulation_platform.long_acting_depot.fluidcrystal_sc":         "formulation_modifier.long_acting.fluidcrystal_sc",
    "formulation_platform.long_acting_depot.fluidcrystal_incretin":   "formulation_modifier.long_acting.fluidcrystal_incretin",

    # siRNA: galnac is a delivery platform; rename L3 to make that explicit
    "nucleic_acid.sirna.galnac_sirna":                   "nucleic_acid.sirna.galnac_platform",
    "nucleic_acid.sirna.galnac_sirna_nextgen":           "nucleic_acid.sirna.galnac_platform_nextgen",
}

def main():
    write = "--write" in sys.argv[1:]
    manifest = json.loads((CONFIGS / "manifest.json").read_text(encoding="utf-8"))
    changes = []
    for tk in sorted(manifest):
        path = CONFIGS / f"{tk}.json"
        if not path.exists(): continue
        c = json.loads(path.read_text(encoding="utf-8"))
        ticker_changes = []
        for a in c.get("assets", []):
            mod = a.get("modality")
            if mod and mod in MIGRATIONS:
                new_mod = MIGRATIONS[mod]
                ticker_changes.append(f"  {a['id']:18s}  {mod}  ->  {new_mod}")
                a["modality"] = new_mod
        if ticker_changes:
            changes.append(f"=== {tk} ===")
            changes.extend(ticker_changes)
            if write:
                path.write_text(json.dumps(c, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for line in changes:
        print(line)
    print(f"\n{len([c for c in changes if c.startswith('===')])} configs, {len(changes) - sum(1 for c in changes if c.startswith('==='))} asset retags")
    if not write:
        print("[DRY-RUN] use --write to save")

if __name__ == "__main__":
    main()
