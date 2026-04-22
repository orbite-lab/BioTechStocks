# -*- coding: utf-8 -*-
"""
Apply real source-cited tooltips from tooltips_*.py to all config files.
Replaces generic template notes in market.sources with proper citations.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIGS = ROOT / "configs"
SCRIPTS = ROOT / "scripts"

# Import all tooltip modules
import sys
sys.path.insert(0, str(SCRIPTS))

# Detect which modules are available (agents write these)
TOOLTIPS = {}
for mod_name in [
    "tooltips_oncology",
    "tooltips_cardio",
    "tooltips_cns",
    "tooltips_immuno_derm",
    "tooltips_rare_other",
]:
    try:
        mod = __import__(mod_name)
        if hasattr(mod, "TOOLTIPS"):
            TOOLTIPS.update(mod.TOOLTIPS)
            print(f"  Loaded {len(mod.TOOLTIPS)} areas from {mod_name}")
    except Exception as e:
        print(f"  Skipped {mod_name}: {e}")

print(f"\nTotal areas with tooltips: {len(TOOLTIPS)}")

# Apply to configs
manifest = json.loads((CONFIGS / "manifest.json").read_text())
updated_indications = 0
updated_fields = 0
configs_changed = set()

for t in manifest:
    path = CONFIGS / (t + ".json")
    d = json.loads(path.read_text(encoding="utf-8"))
    changed = False
    for a in d["assets"]:
        for ind in a["indications"]:
            area = ind.get("area", "")
            if area not in TOOLTIPS:
                continue
            area_tips = TOOLTIPS[area]
            m = ind.get("market", {})
            sources = m.setdefault("sources", {})
            ind_updated = False
            for field_key, note_obj in area_tips.items():
                # Replace existing note with the real citation
                sources[field_key] = note_obj
                updated_fields += 1
                ind_updated = True
            if ind_updated:
                updated_indications += 1
                changed = True
    if changed:
        path.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
        configs_changed.add(t)

print(f"\nApplied to {updated_indications} indications ({updated_fields} fields) across {len(configs_changed)} configs.")
