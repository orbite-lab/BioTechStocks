# -*- coding: utf-8 -*-
"""
Regenerate all market source notes to match actual slider values.
Replaces generic real_epi_data.py notes with accurate per-region breakdowns.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIGS = ROOT / "configs"

def fmt_price(k):
    if k >= 1000:
        return "$" + str(round(k/1000, 1)) + "M"
    return "$" + str(round(k)) + "K"

def process():
    manifest = json.loads((CONFIGS / "manifest.json").read_text())
    updated = 0
    for t in manifest:
        path = CONFIGS / (t + ".json")
        d = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        for a in d["assets"]:
            for ind in a["indications"]:
                m = ind.get("market", {})
                regions = m.get("regions")
                if not regions:
                    continue
                sources = m.get("sources", {})

                # TAM region sources
                for rk, rLabel in [("us", "US"), ("eu", "EU"), ("row", "ROW")]:
                    r = regions.get(rk, {})
                    pts = r.get("patientsK", 0)
                    wtp = r.get("wtpPct", 0)
                    price = r.get("priceK", 0)
                    addr = pts * (wtp / 100) * price

                    # Patients note
                    pk = rk + ".patientsK"
                    old = sources.get(pk, {}).get("note", "")
                    if not old or "real_epi_data" in old or "Auto-decomposed" in old:
                        sources[pk] = {"note": rLabel + " " + str(pts) + "K diagnosed/treated patients."}
                        changed = True

                    # WTP note
                    wk = rk + ".wtpPct"
                    old = sources.get(wk, {}).get("note", "")
                    if not old or "real_epi_data" in old or "Auto-decomposed" in old:
                        if rk == "us":
                            sources[wk] = {"note": rLabel + " WTP " + str(wtp) + "% -- commercial payor access + formulary coverage."}
                        elif rk == "eu":
                            sources[wk] = {"note": rLabel + " WTP " + str(wtp) + "% -- HTA-gated uptake (NICE/G-BA/ASMR)."}
                        else:
                            sources[wk] = {"note": rLabel + " WTP " + str(wtp) + "% -- limited reimbursement outside US/EU/Japan."}
                        changed = True

                    # Price note
                    prk = rk + ".priceK"
                    old = sources.get(prk, {}).get("note", "")
                    if not old or "real_epi_data" in old or "Auto-decomposed" in old:
                        sources[prk] = {"note": rLabel + " avg treatment cost " + fmt_price(price) + "/yr (market blended across modalities)."}
                        changed = True

                # penPct note (preserve existing if hand-written)
                ppk = "penPct"
                old = sources.get(ppk, {}).get("note", "")
                if not old or "Preserved from config" in old or "real_epi_data" in old:
                    pen = m.get("penPct", 0)
                    if pen:
                        sources[ppk] = {"note": "Peak penetration " + str(pen) + "% -- refine per competitive landscape."}
                        changed = True

                # Company slice sources -- update if generic
                cs = m.get("company_slice")
                cs_sources = m.get("company_slice_sources", {})
                if cs:
                    for rk, rLabel in [("us", "US"), ("eu", "EU"), ("row", "ROW")]:
                        c = cs.get(rk, {})
                        tr = regions.get(rk, {})
                        reach = c.get("reachPct", 0)
                        cwtp = c.get("wtpPct", 0)
                        cprice = c.get("priceK", 0)
                        som_r = (tr.get("patientsK", 0)) * (reach / 100) * (cwtp / 100) * cprice

                        # Only add if missing
                        rck = rk + ".reachPct"
                        if rck not in cs_sources:
                            cs_sources[rck] = {"note": rLabel + " reach " + str(reach) + "% of " + str(tr.get("patientsK", 0)) + "K pts = " + str(round(tr.get("patientsK", 0) * reach / 100, 1)) + "K addressable."}
                            changed = True
                        wpk = rk + ".wtpPct"
                        if wpk not in cs_sources:
                            cs_sources[wpk] = {"note": rLabel + " drug-specific WTP " + str(cwtp) + "%."}
                            changed = True
                        cpk = rk + ".priceK"
                        if cpk not in cs_sources:
                            cs_sources[cpk] = {"note": rLabel + " drug price " + fmt_price(cprice) + "/yr."}
                            changed = True

                    if cs_sources:
                        m["company_slice_sources"] = cs_sources

                m["sources"] = sources

        if changed:
            path.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
            updated += 1
            print(t + " updated")

    print("---")
    print(str(updated) + " configs updated")

if __name__ == "__main__":
    process()
