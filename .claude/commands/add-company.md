---
description: Research and scaffold a new company config with full taxonomy + market coverage
argument-hint: TICKER [optional_name]
---

# Add Company — $ARGUMENTS

You are adding a new company to the biotech valuation model. Follow this
workflow **strictly and in order**. Do **not** skip research steps; do **not**
invent data. The config must pass schema validation, audit (0 CRIT), and
snapshot tests before the command is complete.

## Prerequisites

Read `CLAUDE.md` at the repo root first to refresh context on:
- Two-tier market model (TAM via `market.regions`, SOM via `market.company_slice`)
- SOTP vs non-SOTP scenario structure
- Directory layout (`configs/`, `scripts/{recurring,ops,data,lib,archive}/`, `data/`)
- Invariants enforced by CI: schema, SOM ≤ TAM, SOM ≥ salesM, scenario monotonicity

## Step 1 — Parse the ticker argument

Argument format: `TICKER` or `TICKER "Company Name"`.

```
TICKER = first token of $ARGUMENTS, uppercase, letters/digits/underscore only
NAME   = remainder (if provided); otherwise research will find it
```

Reject and ask the user if TICKER is missing, is ambiguous, or already has
a config at `configs/TICKER.json`.

## Step 2 — Research the company

Use **WebSearch** and **WebFetch** to gather (cite sources in a scratchpad):

1. **Company overview**: full legal name, HQ country, listing currency (USD/EUR/JPY/etc.),
   current stock price, shares outstanding (millions), cash position (USD $M).
   Prefer the latest 10-K / 20-F / annual report.
2. **Yahoo ticker**: may differ from the NYSE/LSE/TSE ticker (e.g., "4568.T",
   "LLY", "UCB.BR"). Needed for `company.yahooTicker` so `fetch_prices.py` works.
3. **Pipeline**: every asset the company owns with its name, modality
   (small molecule / antibody / ADC / gene therapy / RNAi / cell therapy /
   peptide / etc.), current stage (`commercial`, `nda_filed`, `phase3`,
   `phase2`, `phase1`), and every indication being pursued.
4. **Reported sales per indication** for commercial products (from 10-K).
   Required for any commercial asset.
5. **Catalysts** in the next 18 months: Ph2/Ph3 readouts, PDUFA dates,
   EMA decisions, label expansions, investor days. Need: date, type,
   asset, indication, binary outcome moves.

Do NOT proceed until you have concrete answers for items 1-3. Items 4-5 are
best-effort; missing data is acceptable with a note to the user.

## Step 3 — Map indications to taxonomy areas

For each indication, determine its L1.L2.L3(.L4) taxonomy path. **Disease
taxonomy is pure clinical classification** — never tag technology / modality
as a disease sub-segment. Examples of correct patterns from `data/taxonomy.json`:

- `oncology.{breast, lung, gi, hematology, genitourinary, gynecologic, neuroendocrine, multi_tumor*, skin}.{subtype}`
  - `oncology.hematology.{aml, cll, nhl.{dlbcl,fl,mcl,wm,mzl,tcell}, myeloma.{1l,2l_3l,4l_plus}}`
  - L4 = line-of-therapy when relevant (myeloma 1L vs 2L_3L vs 4L+)
- `cardio_metabolic.{obesity, diabetes, lipids.{ldl_cv_risk,lpa,triglycerides,hofh}, liver.{mash, hbv_functional_cure, ...}}`
- `cns.{neurodegeneration.{alzheimer,parkinson,als}, psychiatry.{depression,schizophrenia,...}, pain.{migraine,...}}`
- `immunology.{autoimmune, inflammatory_gi.{crohns,uc,eoe}, inflammatory_systemic, transplant.cgvhd}`
- `dermatology.{inflammatory_derm.{psoriasis_systemic,atopic_dermatitis_systemic,prurigo_nodularis}, aesthetics, rare_skin}`
- `ophthalmology.{retina.{nvamd,dme,dr,rvo,ga}, anterior_neuro.{dry_eye,ted,...}}`
- `respiratory.inflammatory.{severe_asthma, copd, crswnp}`
- `musculoskeletal.{neuromuscular.{dmd.*,fshd,dm1,...}, bone_cartilage.*}`
- `rare_disease`, `infectious_disease`, `endocrine`, etc.

**Check each area against `data/taxonomy.json`**. If an L3 area doesn't
exist, do **not** invent it without coordination:
1. Propose the new L3 in a summary to the user.
2. Ask: "This indication (X) doesn't map to an existing L3. Proposed:
   `L1.L2.NEW_L3`. Add it?" Wait for confirmation before creating.
3. If approved, add to the relevant authoritative module AND document in
   the taxonomy.

### Step 3.5 — Append the new area to relevant disease synonym groups

If the new L3 belongs to an established cross-cutting disease family that
already has a `disease_synonym_groups` entry in `data/taxonomy.json`,
**append the new area path to the group's `areas` array**. This is what
makes cross-L1 disease views (Market Explorer search, find_disease_family)
auto-include the new area.

Current groups (25 as of latest update) -- check whether the new area fits any:
- `sle_spectrum`, `ibd_spectrum`, `prostate_cancer`, `breast_cancer_all`,
  `multiple_myeloma_all`, `nsclc_all`, `hemoglobinopathy_all`,
  `hereditary_angioedema_all`, `amyloid_alzheimers_disease`,
  `kidney_disease_specialty`, `hemophilia_all`, `polycystic_disease`,
  `attr_amyloidosis`, `amyloidosis_all`, `complement_mediated`,
  `heart_failure_spectrum`, `pulmonary_hypertension`, `anemia_spectrum`,
  `lysosomal_storage_disease`, `muscular_dystrophy`, `obesity_all`,
  `thrombosis_spectrum`, `epilepsy_spectrum`, `sarcoma_all`,
  `autoimmune_glomerulopathy`, `autoimmune_spectrum`

Common triggers:
- New amyloidosis area (AL, AA, hereditary apoA-I, etc.) → append to
  `amyloidosis_all`; if TTR-specific also `attr_amyloidosis`
- New autoimmune disease (any L1) → append to `autoimmune_spectrum`; if
  glomerular also `autoimmune_glomerulopathy`
- New complement-driven disease → append to `complement_mediated`
- New muscular dystrophy / SMA-adjacent → append to `muscular_dystrophy`
- New NSCLC driver / breast subtype / myeloma line → append to the
  matching cancer-spectrum group
- New rare anemia / hemoglobinopathy → `anemia_spectrum`
- New cardiomyopathy / HF subtype → `heart_failure_spectrum`
- New PH subtype → `pulmonary_hypertension`
- New LSD → `lysosomal_storage_disease`
- New rare epilepsy / DEE → `epilepsy_spectrum`

If the new area belongs to a *new* cross-cutting family (no existing group
fits), propose a new `disease_synonym_groups` entry to the user. Don't
create one without confirmation -- single-area "spectrums" add noise, not
signal.

**Pseudo-areas (`_*` prefix)** for assets that genuinely have no specific
disease (pure platform / discovery — typically pre-clinical R&D):
- `_platform.adc_discovery`, `_platform.bicycle_discovery` (current examples)
- Hidden from Market Explorer; visible in Technology Explorer
- Don't populate market.regions / market.salesM
- Use only when there's truly no lead indication; once one is picked, retag

**Multi-indication assets** (Imbruvica, Brukinsa, Dupixent, Darzalex, etc.):
split `salesM` across the actual approved indications as separate `indications[]`
entries. Don't lump a $13B Dupixent franchise into one indication.

## Step 4 — Check authoritative regions coverage

For each mapped L3 area, read the matching module in
`scripts/data/authoritative_regions_{oncology|cardio|cns|immuno_derm|rare_other}.py`.

**If the L3 is already covered**: nothing to do — `reconcile_sliders.py` will
auto-populate `market.regions` when the config is created.

**If the L3 is NOT covered**: research epidemiology:
- US/EU/ROW diagnosed-patient counts (thousands per year) — sources: NORD,
  Orphanet, NIH SEER, CDC, WHO, ECDC, company 10-K, Datamonitor/GlobalData
  abstracts, published systematic reviews.
- Willingness-to-pay / reimbursed access percentage (commercial insurance
  + Medicare coverage in US; EU5 + UK access; ROW low).
- Blended annual treatment cost in $K (market-average across modalities).

Add the entry to the correct authoritative module using the existing
format (see `scripts/data/authoritative_regions_oncology.py` for examples).

**Cite every number in a `# source: ...` comment**. No hand-waved epi.

## Step 5 — Check modality coverage

If any asset uses a modality not present in `data/taxonomy.json` under the
`modalities` key, propose adding it. Valid top-level modalities include:
`small_molecule`, `antibody`, `adc`, `gene_therapy`, `rna`, `cell_therapy`,
`peptide`, `vaccine`, `oligonucleotide`, `sirna`, `protein`, `bispecific`.

## Step 6 — Scaffold the config

Create `configs/TICKER.json` following this structure (mirror an existing
similar config — e.g., use `configs/VRDN.json` for a pure-pipeline biotech,
`configs/LEGN.json` for a single-franchise commercial, or `configs/ABBV.json`
for a big-pharma SOTP):

```json
{
  "company": {
    "ticker": "TICKER",
    "name": "<legal name>",
    "currentPrice": <local ccy>,
    "sharesOut": <millions>,
    "cash": <$M>,
    "currency": "<USD|EUR|...>",
    "phase": "<commercial|phase3|...>",
    "subtitle": "<1-line tagline>",
    "yahooTicker": "<yahoo symbol>"
  },
  "assets": [ ... ],
  "scenarios": {
    "mega_bear":        {"wt": 5,  "val": { ... }, "assumptions": { ... }},
    "bear":             {"wt": 15, "val": { ... }, "assumptions": { ... }},
    "base":             {"wt": 50, "val": { ... }, "assumptions": { ... }},
    "bull":             {"wt": 25, "val": { ... }, "assumptions": { ... }},
    "psychedelic_bull": {"wt": 5,  "val": { ... }, "assumptions": { ... }}
  },
  "catalysts": [ ... ]
}
```

### Scenario defaults (non-SOTP, pure pipeline)
```json
"val": {
  "mega_bear":        {"mult": 3, "dr": 15, "cannib": 10},
  "bear":             {"mult": 4, "dr": 12, "cannib": 5},
  "base":             {"mult": 6, "dr": 10, "cannib": 2},
  "bull":             {"mult": 9, "dr": 9,  "cannib": 0},
  "psychedelic_bull": {"mult": 13, "dr": 8, "cannib": 0}
}
```

### Scenario defaults (mature pharma — use these only if truly a mega/large cap)
See `scripts/ops/recalibrate_mega_cap.py` — mult 5.5/6.5/8/12/16, dr=3,
cannib=25/15/5/2/0.

### Assumptions (per asset.indication) — MUST be monotonically non-decreasing
```
mega_bear  pos=<low>, apr=<low>
bear       pos=<low-mid>
base       pos=<realistic>
bull       pos=<optimistic>
psy_bull   pos=<max>
```

Commercial drugs: `pos=100, apr=100` across all scenarios (they're already approved).
Phase 3: scale from ~30% to ~85% across scenarios.
Phase 2: scale from ~15% to ~65%.
Phase 1: scale from ~5% to ~40%.

### Market block per indication
```json
"market": {
  "regions": { },              // LEAVE EMPTY -- reconcile_sliders fills it
  "company_slice": {
    "us":  {"reachPct": <n>, "wtpPct": <n>, "priceK": <n>},
    "eu":  {"reachPct": <n>, "wtpPct": <n>, "priceK": <n>},
    "row": {"reachPct": <n>, "wtpPct": <n>, "priceK": <n>}
  },
  "company_slice_sources": {
    "us.reachPct": "<citation>",
    "us.priceK":   "<citation>",
    ...
  },
  "penPct":   0,               // ignored when company_slice present
  "cagrPct":  <market growth>,
  "peakYear": <2030-2035>,
  "salesM":   <if commercial>,
  "salesYear": <year>
}
```

**SOM validation before commit**: `SOM ≤ TAM` and (for commercial drugs)
`SOM ≥ salesM × 1.0`. The audit enforces both.

### Catalysts
```json
{
  "date": "Q2 2026",
  "dateSort": "2026-06-30",
  "asset": "<asset.id>",
  "indication": "<indication.id>",
  "title": "<catalyst title>",
  "type": "<phase3_data|pdufa|...>",
  "binary": true,
  "fail_pos": 10, "fail_apr": 30,
  "success_pos": 85, "success_apr": 90,
  "_source": "<URL>",
  "_confidence": "<high|medium|low>"
}
```

## Step 7 — Add to manifest

Append the ticker to `configs/manifest.json` (alphabetical order).

## Step 8 — Populate regions from authoritative data

Run:
```bash
py scripts/ops/reconcile_sliders.py
```

This will populate `market.regions` for every indication whose `area` has
an authoritative entry. Verify the new config was updated (check a few
indications).

## Step 9 — Run the full validation gauntlet

All three must pass before commit:

```bash
py scripts/ops/validate_schema.py TICKER    # structural schema
py scripts/ops/audit_configs.py             # SOM/TAM invariants, scenario shape
py scripts/ops/snapshot_scenarios.py        # will show NEW ticker, no regressions
py scripts/ops/snapshot_scenarios.py --update  # accept new ticker into baseline
```

**If audit reports CRIT for the new company, fix before committing**:
- `SOM > TAM` → reduce reachPct or priceK in company_slice
- `SOM < salesM` (commercial) → bump reachPct
- `non-monotonic scenarios` → fix assumptions to be monotonically non-decreasing
- `mega_bear > current price` → multiples or PoS assumptions are too generous

**If a FLAG appears, decide**:
- Aspirational SOM (>5× sales) on an early commercial — acceptable for growth stories, document rationale in config notes
- Extreme weighted TP — usually means scenarios are miscalibrated; rebalance

## Step 10 — Summarize and commit

Before committing, print a summary to the user:

```
NEW COMPANY: TICKER — <Name>
  Price: <ccy><price>  MCap: $<X>B
  Assets: <N> (commercial: <m>, pipeline: <n>)
  Markets covered: <list of L3 areas>
  New authoritative regions added: <list or "none">
  New taxonomy areas proposed: <list or "none">
  Synonym groups updated: <list or "none">
  Catalysts next 18m: <count>
  Scenario returns at base: <-x% to +y%>
  All CI checks: PASS
```

Then stage and commit. **Important: include all reconciliation drift in
the same commit** -- when reconcile_sliders runs it may touch other configs
beyond TICKER (calibrating SOMs against updated authoritative regions).
Commit those alongside the feature, never leave them as uncommitted drift
that would force a stash dance on the next push.

```bash
# Stage everything modified -- TICKER plus any drift on other configs from
# reconcile, plus targets/taxonomy auto-rebuilds.
git add configs/ \
        scripts/data/authoritative_regions_*.py \
        data/taxonomy.json data/targets.json \
        snapshots/scenarios.json
# (Verify with `git status` that no sensitive/unintended files snuck in.)
git commit -m "feat(configs): add TICKER (<Name>)

<one-paragraph company description>

- <N> assets: <comma-separated asset names with stages>
- Markets: <L3 areas>
- New epi: <list or 'none; all areas already covered'>
- Synonym groups: <list of groups updated, or 'none'>
- Current price <ccy><X>, weighted TP <ccy><Y> (<upside>%)
- (If reconcile drifted other configs: 'Auto-reconcile drift on N other
  configs from updated authoritative regions: TK1, TK2, ...')

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>"
```

Do **not** push unless the user asks.

## Guardrails

1. **Never invent epi data**. If a market's patient counts or pricing can't
   be sourced, stop and ask the user.
2. **Never bypass the audit**. CRIT = 0 is non-negotiable.
3. **Never commit the `configs/TICKER.json` without running reconcile_sliders
   first** — otherwise TAM regions will be blank and the model won't compute.
4. **Never bump the SOM cap to > 1.5× salesM** for mature commercial drugs.
   Growth stories get up to ~3×; anything higher needs a documented rationale.
5. **Never skip the scenario snapshot update** — leave the baseline
   clean so future PRs can detect regressions.

If any step fails or surfaces a judgement call (missing taxonomy, missing epi,
unusual pricing structure), pause and ask the user. Don't paper over data
gaps to get to "done".
