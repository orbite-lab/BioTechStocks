#!/usr/bin/env python3
"""
Fetch options chain data from Yahoo Finance to sanity-check catalyst swing estimates.

Usage:
  pip install yfinance --break-system-packages
  cd ~/Downloads/biotech-model
  python scripts/fetch_options.py

Adds to each catalyst:
  "options": {
    "expiryDate": "2026-09-19",
    "atmStrike": 9.0,
    "callPrice": 2.10,
    "putPrice": 1.85,
    "straddle": 3.95,
    "impliedMovePct": 44,
    "callIV": 0.85,
    "putIV": 0.92,
    "skew": -0.07,
    "fetchDate": "2026-04-10"
  }
"""
import json, sys, time
from datetime import datetime
from pathlib import Path

try:
    import yfinance as yf
except ImportError:
    print("Install yfinance first: pip install yfinance --break-system-packages")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
CONFIGS = ROOT / "configs"
TODAY = datetime.now().strftime("%Y-%m-%d")


def find_closest_expiry(ticker_obj, target_date):
    """Find options expiry closest to but after the catalyst date."""
    try:
        expiries = ticker_obj.options
    except Exception:
        return None
    if not expiries:
        return None

    target = datetime.strptime(target_date, "%Y-%m-%d")
    candidates = []
    for exp_str in expiries:
        exp = datetime.strptime(exp_str, "%Y-%m-%d")
        diff = (exp - target).days
        # Accept expiry from 7 days before to 45 days after catalyst
        if -7 <= diff <= 45:
            candidates.append((abs(diff), exp_str))

    if candidates:
        candidates.sort()
        return candidates[0][1]

    # Fallback: first expiry after catalyst
    for exp_str in sorted(expiries):
        exp = datetime.strptime(exp_str, "%Y-%m-%d")
        if (exp - target).days >= -7:
            return exp_str
    return None


def compute_atm_straddle(ticker_obj, expiry, current_price):
    """Compute ATM straddle price, implied move, and IV skew."""
    try:
        chain = ticker_obj.option_chain(expiry)
    except Exception as e:
        return None, str(e)

    calls = chain.calls
    puts = chain.puts
    if calls.empty or puts.empty:
        return None, "empty chain"

    # Find ATM strike
    strikes = calls["strike"].values
    atm_idx = abs(strikes - current_price).argmin()
    atm_strike = strikes[atm_idx]

    atm_call = calls[calls["strike"] == atm_strike]
    atm_put = puts[puts["strike"] == atm_strike]
    if atm_call.empty or atm_put.empty:
        return None, "no ATM option"

    # Mid prices (fallback to last price if bid/ask is zero)
    def mid(row):
        b = row["bid"].values[0]
        a = row["ask"].values[0]
        if b > 0 and a > 0:
            return (b + a) / 2
        return row["lastPrice"].values[0]

    call_mid = mid(atm_call)
    put_mid = mid(atm_put)
    straddle = call_mid + put_mid
    implied_move = round(straddle / current_price * 100) if current_price > 0 else 0

    call_iv = atm_call["impliedVolatility"].values[0]
    put_iv = atm_put["impliedVolatility"].values[0]
    skew = round(call_iv - put_iv, 3)  # positive = calls more expensive = bullish skew

    # OTM 25-delta approximation for upside/downside implied moves
    # Straddle gives symmetric +-X%, but skew tells direction
    # Rough: upside implied = impliedMove * (1 + skew), downside = impliedMove * (1 - skew)

    return {
        "expiryDate": expiry,
        "atmStrike": round(float(atm_strike), 2),
        "callPrice": round(float(call_mid), 2),
        "putPrice": round(float(put_mid), 2),
        "straddle": round(float(straddle), 2),
        "impliedMovePct": int(implied_move),
        "callIV": round(float(call_iv), 3),
        "putIV": round(float(put_iv), 3),
        "skew": skew,
        "fetchDate": TODAY,
    }, None


def main():
    manifest = json.loads((CONFIGS / "manifest.json").read_text())
    updated = 0
    skipped = 0
    errors = 0

    for tk in sorted(manifest):
        cfg_path = CONFIGS / f"{tk}.json"
        d = json.loads(cfg_path.read_text())
        cats = d.get("catalysts", [])
        if not cats:
            continue

        # Yahoo ticker mapping
        yahoo_tk = d["company"].get("yahooTicker", tk)
        ccy = d["company"].get("currency", "USD")
        if ccy == "JPY" and "." not in yahoo_tk:
            yahoo_tk += ".T"
        elif ccy == "HKD" and "." not in yahoo_tk:
            yahoo_tk += ".HK"
        elif ccy == "SEK" and "." not in yahoo_tk:
            yahoo_tk += ".ST"

        print(f"\n{tk} ({yahoo_tk}):")

        try:
            ticker = yf.Ticker(yahoo_tk)
            # Get current price
            hist = ticker.history(period="1d")
            if hist.empty:
                current_price = d["company"]["currentPrice"]
                print(f"  Using config price ${current_price}")
            else:
                current_price = float(hist["Close"].iloc[-1])
        except Exception as e:
            print(f"  [ERROR] Can't fetch ticker: {e}")
            errors += 1
            continue

        changed = False
        for cat in cats:
            target = cat.get("dateSort", "")
            if not target:
                print(f"  [{cat['title'][:35]}] no dateSort, skip")
                skipped += 1
                continue

            expiry = find_closest_expiry(ticker, target)
            if not expiry:
                print(f"  [{cat['title'][:35]}] no options expiry found near {target}")
                skipped += 1
                continue

            result, err = compute_atm_straddle(ticker, expiry, current_price)
            if err:
                print(f"  [{cat['title'][:35]}] expiry={expiry} error: {err}")
                skipped += 1
                continue

            cat["options"] = result
            changed = True
            imp = result["impliedMovePct"]
            skw = result["skew"]
            print(
                f"  [{cat['title'][:35]}] "
                f"exp={expiry} straddle=${result['straddle']:.2f} "
                f"implied=+-{imp}% skew={skw:+.3f} "
                f"(callIV={result['callIV']:.0%} putIV={result['putIV']:.0%})"
            )
            updated += 1

            time.sleep(0.3)  # rate limit

        if changed:
            cfg_path.write_text(json.dumps(d, indent=2))

    print(f"\n{'='*60}")
    print(f"  Updated: {updated} catalysts with options data")
    print(f"  Skipped: {skipped} (no expiry / illiquid / error)")
    print(f"  Errors:  {errors} (ticker not found)")
    print(f"{'='*60}")
    print(f"\n  Run the screener to see 'Mkt Implied Move' vs your model swing.")
    print(f"  Re-run this script periodically to refresh as options prices change.")


if __name__ == "__main__":
    main()
