#!/usr/bin/env python3
"""
Fetch current + previous-close prices for every ticker in manifest.json.

- Resolves company.yahooTicker overrides (VLA.PA, 4568.T, 6990.HK, CAMX.ST, etc.)
- Writes prices.json at repo root, keyed by config ticker (not Yahoo ticker)
- Preserves existing entries on partial failures so one Yahoo hiccup doesn't
  blank the whole file. A new run only overwrites tickers it successfully fetched.

Usage:
  pip install yfinance --break-system-packages
  python scripts/fetch_prices.py           # all tickers
  python scripts/fetch_prices.py PEPG VRDN # subset
  python scripts/fetch_prices.py --dry     # print, do not write
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yfinance as yf
except ImportError:
    print("[ERROR] yfinance not installed. Run: pip install yfinance --break-system-packages")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS = ROOT / "configs"
MANIFEST = CONFIGS / "manifest.json"
PRICES = ROOT / "data" / "prices.json"


def load_existing():
    """Load existing prices.json so partial failures don't blank the file."""
    if not PRICES.exists():
        return {}
    try:
        data = json.loads(PRICES.read_text())
        # Strip _meta — we rebuild it every run
        return {k: v for k, v in data.items() if not k.startswith("_")}
    except (json.JSONDecodeError, Exception) as e:
        print(f"[WARN] Could not read existing prices.json ({e}); starting fresh")
        return {}


def fetch_one(config_ticker, yahoo_ticker):
    """Fetch price + prev close + 1W/1M/YTD historicals. Returns dict or None on failure."""
    try:
        tk = yf.Ticker(yahoo_ticker)
        # Fetch from start of last calendar year to "now" -- gives us YTD anchor
        # plus enough trailing history for 1W/1M lookback. Using "ytd" alone misses
        # the prior-year anchor; "1y" + manual filter handles year-boundary safely.
        hist = tk.history(period="1y", auto_adjust=False)
        if hist.empty or len(hist) == 0:
            return None, "empty history"

        # Most recent close (today if live, otherwise last trading day)
        last_close = float(hist["Close"].iloc[-1])
        prev_close = float(hist["Close"].iloc[-2]) if len(hist) >= 2 else last_close

        # Prefer fast_info for intraday current price if available
        price = last_close
        try:
            fi = tk.fast_info
            lp = fi.get("last_price") if hasattr(fi, "get") else getattr(fi, "last_price", None)
            if lp and lp > 0:
                price = float(lp)
                if len(hist) >= 2:
                    prev_close = float(hist["Close"].iloc[-1])
        except Exception:
            pass

        if price <= 0:
            return None, "price <= 0"

        # London Stock Exchange (.L) tickers report in pence (GBp) on Yahoo;
        # convert to pounds (GBP) so the unit matches config.currentPrice.
        # E.g. HIK.L returns 1408 (pence) -> store 14.08 (pounds).
        if yahoo_ticker.endswith(".L"):
            price /= 100.0
            prev_close /= 100.0

        # Helper: lookup close N trading days back (positive N)
        def close_n_back(n):
            try:
                if len(hist) > n:
                    return float(hist["Close"].iloc[-(n + 1)])
            except Exception:
                pass
            return None

        # 1W ~ 5 trading days, 1M ~ 21 trading days
        price_1w = close_n_back(5)
        price_1m = close_n_back(21)

        # Apply same pence->pounds conversion to historical lookbacks
        if yahoo_ticker.endswith(".L"):
            if price_1w is not None: price_1w /= 100.0
            if price_1m is not None: price_1m /= 100.0

        # YTD: first close of current calendar year (last close of prior year as fallback)
        price_ytd = None
        try:
            from datetime import datetime as _dt
            year = _dt.now().year
            year_start = hist[hist.index.year == year]
            if len(year_start) > 0:
                price_ytd = float(year_start["Close"].iloc[0])
            else:
                # If no current-year prints yet (early Jan), use prior-year last close
                price_ytd = float(hist["Close"].iloc[0])
            if yahoo_ticker.endswith(".L") and price_ytd is not None:
                price_ytd /= 100.0
        except Exception:
            pass

        out = {
            "price": round(price, 4),
            "prevClose": round(prev_close, 4),
            "yahooTicker": yahoo_ticker,
        }
        if price_1w is not None: out["price1W"] = round(price_1w, 4)
        if price_1m is not None: out["price1M"] = round(price_1m, 4)
        if price_ytd is not None: out["priceYTD"] = round(price_ytd, 4)
        return out, None
    except Exception as e:
        return None, str(e)[:80]


def main():
    args = sys.argv[1:]
    dry_run = "--dry" in args
    args = [a for a in args if a != "--dry"]

    if not MANIFEST.exists():
        print(f"[ERROR] {MANIFEST} not found")
        sys.exit(1)

    all_tickers = json.loads(MANIFEST.read_text())
    tickers = [t for t in all_tickers if t in args] if args else all_tickers

    if not tickers:
        print(f"[ERROR] No matching tickers. Available: {', '.join(all_tickers)}")
        sys.exit(1)

    print(f"Fetching {len(tickers)} tickers...")

    # Preserve existing entries so partial failures don't wipe the file
    prices = load_existing()
    fetched = 0
    failed = 0

    for ct in tickers:
        cfg_path = CONFIGS / f"{ct}.json"
        if not cfg_path.exists():
            print(f"  {ct:8} SKIP  — config not found")
            failed += 1
            continue
        try:
            cfg = json.loads(cfg_path.read_text())
        except json.JSONDecodeError as e:
            print(f"  {ct:8} SKIP  — bad JSON ({e})")
            failed += 1
            continue

        co = cfg.get("company", {})
        # Skip private (non-tradeable reference) configs -- no price feed
        if co.get("private"):
            print(f"  {ct:8} PRIV  — private reference, skipping price fetch")
            continue
        yt = co.get("yahooTicker") or ct
        result, err = fetch_one(ct, yt)

        if result is None:
            existing = prices.get(ct)
            status = "STALE" if existing else "FAIL "
            print(f"  {ct:8} {status} — {yt} ({err})")
            failed += 1
            continue

        chg_pct = ((result["price"] - result["prevClose"]) / result["prevClose"] * 100) if result["prevClose"] else 0
        arrow = "▲" if chg_pct >= 0 else "▼"
        print(f"  {ct:8} OK    — {yt:10} {result['price']:>10.2f} {arrow}{abs(chg_pct):>5.2f}%")
        prices[ct] = result
        fetched += 1

    out = {
        "_meta": {
            "fetchedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "count": len(prices),
            "fetchedThisRun": fetched,
            "failedThisRun": failed,
        },
    }
    out.update(dict(sorted(prices.items())))

    if dry_run:
        print(f"\n[DRY RUN] Would write {len(prices)} tickers ({fetched} new, {failed} failed)")
        return

    PRICES.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\n[OK] Wrote {PRICES} — {len(prices)} tickers ({fetched} fetched, {failed} failed/stale)")


if __name__ == "__main__":
    main()
