# -*- coding: utf-8 -*-
"""Merge financials_batch_{a,b,c}.py into a single financials.json at repo root."""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

merged = {}
for mod_name in ["financials_batch_a", "financials_batch_b", "financials_batch_c"]:
    mod = __import__(mod_name)
    if hasattr(mod, "FINANCIALS"):
        merged.update(mod.FINANCIALS)
        print(f"  {mod_name}: {len(mod.FINANCIALS)} companies")

print(f"Total: {len(merged)} companies")
(ROOT / "financials.json").write_text(json.dumps(merged, indent=2), encoding="utf-8")
print("Wrote financials.json")
