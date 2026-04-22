# -*- coding: utf-8 -*-
"""
Apply hand-researched drug-specific SOM tooltips from som_tooltips_*.py.
Overwrites existing (template-generated) SOM tooltips with the researched
per-drug versions. Preserves structure for any (ticker, asset, ind) not
covered by the research (falls back to what's already in config).
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIGS = ROOT / "configs"
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

SOM_TOOLTIPS = {}
for mod_name in [
    "som_tooltips_batch1",
    "som_tooltips_batch2",
    "som_tooltips_batch3",
    "som_tooltips_batch4",
]:
    try:
        mod = __import__(mod_name)
        if hasattr(mod, "SOM_TOOLTIPS"):
            SOM_TOOLTIPS.update(mod.SOM_TOOLTIPS)
            print(f"  {mod_name}: {len(mod.SOM_TOOLTIPS)} drugs")
    except Exception as e:
        print(f"  SKIP {mod_name}: {e}")

print(f"\nTotal drugs with researched SOM tooltips: {len(SOM_TOOLTIPS)}")

manifest = json.loads((CONFIGS / "manifest.json").read_text())
updated = 0
total_fields = 0
for t in manifest:
    path = CONFIGS / (t + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    for a in d["assets"]:
        for ind in a["indications"]:
            key = (t, a["id"], ind["id"])
            if key not in SOM_TOOLTIPS:
                continue
            notes = SOM_TOOLTIPS[key]
            m = ind.setdefault("market", {})
            css = m.setdefault("company_slice_sources", {})
            for field_key, note_obj in notes.items():
                css[field_key] = note_obj
                total_fields += 1
            updated += 1
            changed = True
    if changed:
        path.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")

print(f"Applied to {updated} drugs ({total_fields} fields) across configs.")

# Find any drug that still lacks researched tooltips
missing = []
for t in manifest:
    d = json.loads((CONFIGS / (t + ".json")).read_text(encoding="utf-8"))
    for a in d["assets"]:
        for ind in a["indications"]:
            if ind.get("market", {}).get("company_slice") and (t, a["id"], ind["id"]) not in SOM_TOOLTIPS:
                missing.append(f"{t}.{a['id']}.{ind['id']}")
if missing:
    print(f"\nWARN: {len(missing)} drugs lacking researched SOM tooltips (will retain template fills):")
    for m in missing[:20]:
        print(f"  {m}")
