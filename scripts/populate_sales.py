# -*- coding: utf-8 -*-
"""
Parse asset.stage strings like "Commercial ($3.9B 2025)" or "Commercial ($480M 2025, +58%)"
and populate market.salesM + market.salesYear on each indication.

Only sets salesM/salesYear if:
  - The asset's stage contains a dollar/euro amount (e.g. $3.9B, $480M, EUR130M)
  - market.salesM is not already set

For multi-indication assets, the total is split evenly across indications
(crude but better than nothing -- user can refine manually).
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT / "configs"
MANIFEST = CONFIG_DIR / "manifest.json"

# Match patterns like: $3.9B, $480M, EUR130M, EUR1.2B, $6.4B
SALES_RE = re.compile(
    r'[\$\u20ac](\d+(?:\.\d+)?)\s*([BbMm])'
    r'|(?:EUR|USD)\s*(\d+(?:\.\d+)?)\s*([BbMm])',
    re.IGNORECASE
)
YEAR_RE = re.compile(r'\b(20[0-9]{2})\b')


def parse_sales_from_stage(stage: str):
    """Return (salesM, year) or (None, None)."""
    if not stage:
        return None, None
    m = SALES_RE.search(stage)
    if not m:
        return None, None
    if m.group(1):
        val, unit = float(m.group(1)), m.group(2).upper()
    else:
        val, unit = float(m.group(3)), m.group(4).upper()
    sales_m = val * 1000 if unit == 'B' else val
    ym = YEAR_RE.search(stage)
    year = int(ym.group(1)) if ym else None
    return sales_m, year


def process_config(path: Path) -> int:
    cfg = json.loads(path.read_text(encoding="utf-8"))
    touched = 0
    for asset in cfg.get("assets", []):
        stage = asset.get("stage", "")
        sales_m, year = parse_sales_from_stage(stage)
        if sales_m is None or sales_m <= 0:
            continue
        inds = asset.get("indications", [])
        n_inds = len(inds)
        if n_inds == 0:
            continue
        # Split sales across indications (equal split if >1)
        per_ind = round(sales_m / n_inds, 1)
        for ind in inds:
            mkt = ind.get("market")
            if not mkt or not isinstance(mkt, dict):
                continue
            if mkt.get("salesM") is not None:
                continue  # already set
            mkt["salesM"] = per_ind
            if year:
                mkt["salesYear"] = year
            touched += 1
    if touched:
        path.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8")
    return touched


def main():
    tickers = json.loads(MANIFEST.read_text(encoding="utf-8"))
    total = 0
    for t in tickers:
        p = CONFIG_DIR / f"{t}.json"
        if not p.exists():
            continue
        n = process_config(p)
        if n:
            print(f"{t:6s}  {n} indications got salesM")
            total += n
    print("-" * 40)
    print(f"TOTAL: {total} indications populated with salesM")


if __name__ == "__main__":
    main()
