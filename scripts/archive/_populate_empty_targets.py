# -*- coding: utf-8 -*-
"""One-shot: populate targets[] for the 57 platform / multi-specific
assets that seed_targets.py left empty. Covers:
  - siRNA / ASO / CRISPR / gene therapy: each asset has a specific per-program
    target even though the modality L3 is a platform string
  - Molecular glues + degraders: each degrader has its own substrate
  - Vaccines: pathogen antigen
  - Bispecifics: each arm's target
  - Formulation modifiers: target of the encapsulated drug
  - Fillers / discovery platforms: remain empty (genuinely targetless)

Curated by hand from config stage/name/indication context.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS = ROOT / "configs"

# (ticker, asset_id) -> list of targets. [] means leave empty (true platform).
MAP = {
    # ─── ADC / radio platforms ───
    ("6990", "platform"):       [],                 # OptiDC discovery platform
    ("BCYC", "platform"):       [],                 # Bicycle discovery
    ("BCYC", "brc"):            ["MMP14"],          # BT1702 MT1-MMP radioconjugate

    # ─── Aesthetics (no molecular target) ───
    ("ABBV", "juvederm"):       [],                 # Hyaluronic acid filler

    # ─── ALNY siRNA ───
    ("ALNY", "commercial"):     ["TTR"],            # Amvuttra + Onpattro
    ("ALNY", "nucresiran"):     ["TTR"],            # Next-gen TTR
    ("ALNY", "zilebesiran"):    ["AGT"],            # Angiotensinogen
    ("ALNY", "mivelsiran"):     ["APP"],            # Amyloid precursor (CAA/AD)
    ("ALNY", "givlaari"):       ["ALAS1"],          # Porphyria
    ("ALNY", "oxlumo"):         ["HAO1"],           # Hyperoxaluria (glycolate ox)

    # ─── ARWR TRiM ───
    ("ARWR", "commercial"):     ["APOC3"],          # Plozasiran FCS
    ("ARWR", "zodasiran"):      ["ANGPTL3"],
    ("ARWR", "obesity"):        ["INHBE", "ACVR1C"],  # INHBE + ALK7
    ("ARWR", "aro_mapt"):       ["MAPT"],

    # ─── BHVN MoDE degraders ───
    ("BHVN", "bhv1300"):        ["IGG"],            # IgG lysosomal degrader
    ("BHVN", "bhv1400"):        ["IGA1_GAL_DEF"],   # Gd-IgA1
    ("BHVN", "taldef"):         ["MSTN", "ACVR2B"], # Myostatin-activin
    ("BHVN", "bhv1510"):        ["TACSTD2"],        # TROP2 ADC

    # ─── CAMX depot formulations ───
    ("CAMX", "commercial"):     ["OPRM1"],          # Buprenorphine
    ("CAMX", "oczyesa"):        ["SSTR2"],          # Octreotide (acromegaly)
    ("CAMX", "sorento"):        ["SSTR2"],          # Octreotide (GEP-NET)
    ("CAMX", "pld"):            ["SSTR2"],          # Octreotide (PLD)

    # ─── CRSP CRISPR ───
    ("CRSP", "casgevy"):        ["BCL11A"],         # Exa-cel fetal-Hb derepression
    ("CRSP", "ctx310"):         ["ANGPTL3"],
    ("CRSP", "ctx460"):         ["SERPINA1"],       # A1AT
    ("CRSP", "discovery"):      ["F11"],            # CTX340 Factor XI

    # ─── IONS ASO ───
    ("IONS", "commercial"):     ["APOC3"],          # Tryngolza
    ("IONS", "dawnzera"):       ["KLKB1"],          # Prekallikrein (HAE)
    ("IONS", "zilgan"):         ["GFAP"],           # Alexander disease
    ("IONS", "eplont"):         ["TTR"],            # Wainua ATTR
    ("IONS", "bepiro"):         ["HBV"],            # Hepatitis B surface
    ("IONS", "pelac"):          ["LPA"],            # Pelacarsen Lp(a)

    # ─── JANX TCEs ───
    ("JANX", "janx007"):        ["FOLH1", "CD3E"],  # PSMA + CD3
    ("JANX", "janx008"):        ["EGFR", "CD3E"],   # EGFR + CD3
    ("JANX", "psma_tracir"):    ["FOLH1", "CD28"],
    ("JANX", "merck_bms"):      [],                 # collab platform, target varies

    # ─── KRYS HSV1 gene therapy ───
    ("KRYS", "commercial"):     ["COL7A1"],         # VYJUVEK DEB
    ("KRYS", "kb803"):          ["COL7A1"],         # ocular DEB
    ("KRYS", "kb801"):          ["NGF"],            # neurotrophic keratitis
    ("KRYS", "kb407"):          ["CFTR"],           # cystic fibrosis
    ("KRYS", "kb707"):          ["IL2", "IL12A"],   # NSCLC immunotherapy
    ("KRYS", "kb111"):          ["ATP2C1"],         # Hailey-Hailey

    # ─── KYMR molecular glues ───
    ("KYMR", "kt621"):          ["STAT6"],
    ("KYMR", "kt579"):          ["IRF5"],
    ("KYMR", "irak4"):          ["IRAK4"],
    ("KYMR", "cdk2"):           ["CDK2"],

    # ─── LEGN in vivo CAR-T ───
    ("LEGN", "invivo"):         ["TNFRSF17"],       # BCMA

    # ─── MDGL Rezdiffra combos ───
    ("MDGL", "combos"):         ["THRB", "DGAT2"],  # Rezdiffra + DGAT2 partners

    # ─── NTLA in vivo CRISPR ───
    ("NTLA", "lonvoz"):         ["KLKB1"],          # Prekallikrein (HAE)
    ("NTLA", "nexz_cm"):        ["TTR"],
    ("NTLA", "nexz_pn"):        ["TTR"],

    # ─── PRAX ASO ───
    ("PRAX", "elsun"):          ["SCN2A"],          # SCN2A-DEE

    # ─── VLA vaccines (pathogen antigens) ───
    ("VLA", "vla15"):           ["BORRELIA_OSPA"],  # Lyme OspA
    ("VLA", "ixchiq"):          ["CHIK_VIRUS"],     # Chikungunya
    ("VLA", "s4v2"):            ["SHIGELLA"],       # Shigella O-antigens
    ("VLA", "zika"):            ["ZIKA_VIRUS"],
    ("VLA", "commercial"):      ["JEV", "VIBRIO_CHOLERAE"],  # IXIARO JE + DUKORAL
}


def main():
    manifest = json.loads((CONFIGS / "manifest.json").read_text(encoding="utf-8"))
    touched = 0
    for tk in manifest:
        path = CONFIGS / f"{tk}.json"
        cfg = json.loads(path.read_text(encoding="utf-8"))
        dirty = False
        for a in cfg.get("assets", []):
            key = (tk, a["id"])
            if key not in MAP:
                continue
            new_targets = MAP[key]
            current = a.get("targets", [])
            if current == new_targets:
                continue
            a["targets"] = new_targets
            dirty = True
            touched += 1
            print(f"  {tk:6} {a['id']:18} -> {new_targets}")
        if dirty:
            path.write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n",
                            encoding="utf-8")
    print(f"\n[WROTE] {touched} assets updated.")


if __name__ == "__main__":
    main()
