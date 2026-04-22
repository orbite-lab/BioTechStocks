# -*- coding: utf-8 -*-
"""
Generate consolidated TAM/SOM report across all 45 configs.
Outputs:
  - tam_report.csv: per-indication flat table
  - tam_report.md: markdown summary grouped by L1/L2
"""
import json, csv
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS = ROOT / "configs"

def fmt_m(v):
    return f"${v:,.0f}M" if v < 1000 else f"${v/1000:.2f}B"

def collect():
    manifest = json.loads((CONFIGS / "manifest.json").read_text())
    rows = []
    for tk in manifest:
        d = json.loads((CONFIGS / f"{tk}.json").read_text(encoding="utf-8"))
        co = d["company"]
        for a in d["assets"]:
            for ind in a["indications"]:
                m = ind.get("market", {})
                r = m.get("regions", {})
                cs = m.get("company_slice", {})

                # TAM
                tam_us  = (r.get("us",{}).get("patientsK",0))*(r.get("us",{}).get("wtpPct",0)/100)*r.get("us",{}).get("priceK",0)
                tam_eu  = (r.get("eu",{}).get("patientsK",0))*(r.get("eu",{}).get("wtpPct",0)/100)*r.get("eu",{}).get("priceK",0)
                tam_row = (r.get("row",{}).get("patientsK",0))*(r.get("row",{}).get("wtpPct",0)/100)*r.get("row",{}).get("priceK",0)
                tam_total = tam_us + tam_eu + tam_row

                # SOM
                som_us = som_eu = som_row = 0
                if cs:
                    som_us  = (r.get("us",{}).get("patientsK",0))*(cs.get("us",{}).get("reachPct",0)/100)*(cs.get("us",{}).get("wtpPct",0)/100)*cs.get("us",{}).get("priceK",0)
                    som_eu  = (r.get("eu",{}).get("patientsK",0))*(cs.get("eu",{}).get("reachPct",0)/100)*(cs.get("eu",{}).get("wtpPct",0)/100)*cs.get("eu",{}).get("priceK",0)
                    som_row = (r.get("row",{}).get("patientsK",0))*(cs.get("row",{}).get("reachPct",0)/100)*(cs.get("row",{}).get("wtpPct",0)/100)*cs.get("row",{}).get("priceK",0)
                som_total = som_us + som_eu + som_row

                rows.append({
                    "ticker": tk,
                    "company": co.get("name", ""),
                    "asset_id": a["id"],
                    "asset_name": a["name"],
                    "stage": a.get("stage", ""),
                    "ind_id": ind["id"],
                    "ind_name": ind["name"],
                    "area": ind.get("area", ""),
                    "rare": ind.get("rare", False),
                    "salesM": m.get("salesM", 0),
                    "salesYear": m.get("salesYear", ""),
                    # TAM inputs
                    "us_pts_K": r.get("us",{}).get("patientsK", 0),
                    "us_wtp_pct": r.get("us",{}).get("wtpPct", 0),
                    "us_price_K": r.get("us",{}).get("priceK", 0),
                    "eu_pts_K": r.get("eu",{}).get("patientsK", 0),
                    "eu_wtp_pct": r.get("eu",{}).get("wtpPct", 0),
                    "eu_price_K": r.get("eu",{}).get("priceK", 0),
                    "row_pts_K": r.get("row",{}).get("patientsK", 0),
                    "row_wtp_pct": r.get("row",{}).get("wtpPct", 0),
                    "row_price_K": r.get("row",{}).get("priceK", 0),
                    # TAM outputs
                    "tam_us_M": round(tam_us),
                    "tam_eu_M": round(tam_eu),
                    "tam_row_M": round(tam_row),
                    "tam_total_M": round(tam_total),
                    # SOM inputs
                    "us_reach_pct": cs.get("us",{}).get("reachPct", 0),
                    "us_cs_wtp_pct": cs.get("us",{}).get("wtpPct", 0),
                    "us_cs_price_K": cs.get("us",{}).get("priceK", 0),
                    "eu_reach_pct": cs.get("eu",{}).get("reachPct", 0),
                    "eu_cs_wtp_pct": cs.get("eu",{}).get("wtpPct", 0),
                    "eu_cs_price_K": cs.get("eu",{}).get("priceK", 0),
                    "row_reach_pct": cs.get("row",{}).get("reachPct", 0),
                    "row_cs_wtp_pct": cs.get("row",{}).get("wtpPct", 0),
                    "row_cs_price_K": cs.get("row",{}).get("priceK", 0),
                    # SOM outputs
                    "som_us_M": round(som_us),
                    "som_eu_M": round(som_eu),
                    "som_row_M": round(som_row),
                    "som_total_M": round(som_total),
                    "implied_pen_pct": round((som_total / tam_total * 100) if tam_total > 0 else 0, 1),
                })
    return rows

def write_csv(rows, path):
    if not rows: return
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

def write_md(rows, path):
    # Group by L1 > L2 > L3
    by_area = defaultdict(list)
    for r in rows:
        area = r["area"] or "unclassified"
        parts = area.split(".")
        l1 = parts[0] if parts else "unclassified"
        l2 = ".".join(parts[:2]) if len(parts) > 1 else l1
        by_area[(l1, l2, area)].append(r)

    # Dedupe TAM by area (each disease market counted once, not per-drug)
    unique_tam_by_area = {}
    for r in rows:
        area = r["area"] or "unclassified"
        if area not in unique_tam_by_area:
            unique_tam_by_area[area] = r["tam_total_M"]
    total_tam_unique = sum(unique_tam_by_area.values())
    total_tam_raw = sum(r["tam_total_M"] for r in rows)

    lines = ["# Consolidated TAM & SOM Report", "",
             "All 45 companies, 222 indications. Generated from configs/ via scripts/tam_report.py.", "",
             f"**Total TAM (unique markets)**: ${total_tam_unique/1000:.1f}B across {len(unique_tam_by_area)} distinct disease areas",
             f"**Total TAM (sum per-drug, with double-counting)**: ${total_tam_raw/1000:.1f}B",
             f"**Total SOM**: ${sum(r['som_total_M'] for r in rows)/1000:.1f}B (summed per-drug; company slices don't overlap)",
             f"**Total 2025 reported sales**: ${sum(r['salesM'] for r in rows)/1000:.1f}B", "",
             "_Note: Multiple companies target the same disease area (e.g. 4 companies in obesity/GLP-1 each_",
             "_see the same $396B TAM). The 'unique markets' total avoids double-counting._", "", "---", ""]

    # Summary by L1 - dedupe TAM per area
    l1_totals = defaultdict(lambda: {"tam": 0, "som": 0, "sales": 0, "count": 0, "areas": set()})
    for r in rows:
        l1 = (r["area"] or "unclassified").split(".")[0]
        area = r["area"] or "unclassified"
        if area not in l1_totals[l1]["areas"]:
            l1_totals[l1]["tam"] += r["tam_total_M"]
            l1_totals[l1]["areas"].add(area)
        l1_totals[l1]["som"] += r["som_total_M"]
        l1_totals[l1]["sales"] += r["salesM"]
        l1_totals[l1]["count"] += 1

    lines.append("## Summary by Therapeutic Area (L1)")
    lines.append("")
    lines.append("| L1 Area | Indications | TAM | SOM | 2025 Sales |")
    lines.append("|---|---:|---:|---:|---:|")
    for l1 in sorted(l1_totals, key=lambda k: -l1_totals[k]["tam"]):
        t = l1_totals[l1]
        lines.append(f"| {l1.replace('_',' ')} | {t['count']} | {fmt_m(t['tam'])} | {fmt_m(t['som'])} | {fmt_m(t['sales'])} |")
    lines.append("")

    # Detail grouped by L1/L2
    lines.append("## Detail by Indication")
    lines.append("")
    cur_l1 = cur_l2 = None
    for (l1, l2, area), area_rows in sorted(by_area.items()):
        if l1 != cur_l1:
            lines.append(f"\n### {l1.replace('_',' ').title()}\n")
            cur_l1 = l1
            cur_l2 = None
        if l2 != cur_l2:
            lines.append(f"\n#### {l2.replace('_',' ')}\n")
            cur_l2 = l2
            lines.append("| Ticker | Asset | Indication | Stage | US pts | TAM | SOM | Sales | Rare |")
            lines.append("|---|---|---|---|---:|---:|---:|---:|---|")
        for r in area_rows:
            stage_short = r["stage"][:30]
            rare = "★" if r["rare"] else ""
            lines.append(f"| {r['ticker']} | {r['asset_name'][:25]} | {r['ind_name'][:30]} | {stage_short} | {r['us_pts_K']}K | {fmt_m(r['tam_total_M'])} | {fmt_m(r['som_total_M'])} | {fmt_m(r['salesM'])} | {rare} |")

    Path(path).write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    rows = collect()
    csv_path = ROOT / "reports" / "tam_report.csv"
    md_path = ROOT / "reports" / "tam_report.md"
    write_csv(rows, csv_path)
    write_md(rows, md_path)
    print(f"Wrote {len(rows)} rows to:")
    print(f"  {csv_path}")
    print(f"  {md_path}")
    print(f"\nTotal TAM: ${sum(r['tam_total_M'] for r in rows)/1000:.1f}B")
    print(f"Total SOM: ${sum(r['som_total_M'] for r in rows)/1000:.1f}B")
    print(f"Total sales: ${sum(r['salesM'] for r in rows)/1000:.1f}B")
