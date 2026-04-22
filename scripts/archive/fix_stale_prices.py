# -*- coding: utf-8 -*-
"""Fix source notes where the stated price doesn't match the actual slider value."""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIGS = ROOT / "configs"

def fmt(k):
    return "$" + str(round(k/1000, 1)) + "M" if k >= 1000 else "$" + str(round(k)) + "K"

def run():
    manifest = json.loads((CONFIGS / "manifest.json").read_text())
    fixed = 0
    for t in manifest:
        path = CONFIGS / (t + ".json")
        d = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for a in d["assets"]:
            for ind in a["indications"]:
                m = ind.get("market", {})
                regions = m.get("regions", {})
                sources = m.get("sources", {})
                for rk, rLabel in [("us", "US"), ("eu", "EU"), ("row", "ROW")]:
                    r = regions.get(rk, {})
                    actual = r.get("priceK", 0)
                    pk = rk + ".priceK"
                    note = sources.get(pk, {}).get("note", "")
                    if not note or actual == 0:
                        continue
                    # Find dollar amounts in note
                    for m2 in re.finditer(r'\$(\d+(?:\.\d+)?)\s*([KkMm])', note):
                        val = float(m2.group(1))
                        if m2.group(2).upper() == "M":
                            val *= 1000
                        # If noted value differs >30% from actual
                        if abs(val - actual) / max(actual, 1) > 0.3:
                            new_note = rLabel + " market blended avg " + fmt(actual) + "/yr across treatment modalities."
                            sources[pk] = {"note": new_note}
                            changed = True
                            fixed += 1
                            print(f"{t:5s} {ind.get('name','')[:30]:30s} {rk}: note said ${val:.0f}K, actual ${actual}K -> fixed")
                            break
        if changed:
            path.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"---\n{fixed} stale price notes fixed")

if __name__ == "__main__":
    run()
