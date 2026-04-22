#!/usr/bin/env python3
"""
Fetch options-implied moves + directionality for catalyst events.
Writes to options_cache.json.

Usage:
  pip install yfinance --break-system-packages
  python scripts/fetch_options.py          # all companies
  python scripts/fetch_options.py BHVN     # single company
  python scripts/fetch_options.py --dry    # preview without writing

Adds per catalyst:
  impliedMove: ATM straddle implied move (%)
  skew25d:     25-delta put IV - 25-delta call IV (positive = bearish)
  pcOI:        put/call open interest ratio at expiry (>1 = bearish)
  pcVol:       put/call volume ratio at expiry (>1 = bearish flow)
  callIV/putIV: ATM implied volatility
  direction:   "bullish" / "bearish" / "neutral" (composite signal)
"""
import json, sys
from pathlib import Path
from datetime import datetime, date, timedelta

try:
    import yfinance as yf
except ImportError:
    print("[ERROR] Install yfinance: pip install yfinance --break-system-packages")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS = ROOT / "configs"
CACHE = ROOT / "options_cache.json"


def get_options_data(ticker_yahoo, catalyst_date_str, stock_price):
    """Fetch ATM straddle + directional signals for expiry closest to catalyst."""
    try:
        tk = yf.Ticker(ticker_yahoo)
        expiries = tk.options
        if not expiries:
            return None, "No options chain"

        try:
            cat_date = datetime.strptime(catalyst_date_str, "%Y-%m-%d").date()
        except ValueError:
            return None, f"Bad date: {catalyst_date_str}"

        # Find closest expiry on or after catalyst date (allow 7 days before)
        best_expiry = None
        best_delta = timedelta(days=9999)
        for exp_str in expiries:
            exp_date = datetime.strptime(exp_str, "%Y-%m-%d").date()
            delta = exp_date - cat_date
            if delta.days >= -7 and abs(delta) < abs(best_delta):
                best_delta = delta
                best_expiry = exp_str

        if not best_expiry:
            deltas = [(abs((datetime.strptime(e, "%Y-%m-%d").date() - cat_date).days), e)
                       for e in expiries]
            deltas.sort()
            best_expiry = deltas[0][1]

        chain = tk.option_chain(best_expiry)
        calls = chain.calls
        puts = chain.puts
        if calls.empty or puts.empty:
            return None, f"Empty chain for {best_expiry}"

        # --- ATM straddle ---
        strikes = calls['strike'].values
        atm_idx = abs(strikes - stock_price).argmin()
        atm_strike = strikes[atm_idx]

        atm_call = calls[calls['strike'] == atm_strike].iloc[0]
        atm_put = puts[puts['strike'] == atm_strike].iloc[0]

        call_mid = (atm_call['bid'] + atm_call['ask']) / 2 if atm_call['bid'] > 0 else atm_call['lastPrice']
        put_mid = (atm_put['bid'] + atm_put['ask']) / 2 if atm_put['bid'] > 0 else atm_put['lastPrice']
        straddle = call_mid + put_mid
        implied_move = round(straddle / stock_price * 100)

        call_iv_atm = round(atm_call.get('impliedVolatility', 0) * 100)
        put_iv_atm = round(atm_put.get('impliedVolatility', 0) * 100)

        # --- 25-delta skew (OTM put IV vs OTM call IV) ---
        # Approximate 25-delta: ~20% OTM on each side
        otm_put_strike = stock_price * 0.80
        otm_call_strike = stock_price * 1.20

        otm_put_iv = 0
        otm_call_iv = 0
        try:
            put_otm_idx = abs(puts['strike'].values - otm_put_strike).argmin()
            otm_put_row = puts.iloc[put_otm_idx]
            otm_put_iv = round(otm_put_row.get('impliedVolatility', 0) * 100)
        except:
            pass
        try:
            call_otm_idx = abs(calls['strike'].values - otm_call_strike).argmin()
            otm_call_row = calls.iloc[call_otm_idx]
            otm_call_iv = round(otm_call_row.get('impliedVolatility', 0) * 100)
        except:
            pass

        skew_25d = otm_put_iv - otm_call_iv  # positive = bearish

        # --- Put/Call OI ratio ---
        total_call_oi = calls['openInterest'].sum() if 'openInterest' in calls.columns else 0
        total_put_oi = puts['openInterest'].sum() if 'openInterest' in puts.columns else 0
        pc_oi = round(total_put_oi / total_call_oi, 2) if total_call_oi > 0 else 0

        # --- Put/Call Volume ratio ---
        total_call_vol = calls['volume'].sum() if 'volume' in calls.columns else 0
        total_put_vol = puts['volume'].sum() if 'volume' in puts.columns else 0
        pc_vol = round(total_put_vol / total_call_vol, 2) if total_call_vol > 0 else 0

        # --- Composite direction signal ---
        signals = 0  # positive = bullish, negative = bearish
        if skew_25d > 10: signals -= 1     # puts expensive → bearish
        elif skew_25d < -10: signals += 1  # calls expensive → bullish
        if pc_oi < 0.7: signals += 1       # more call OI → bullish
        elif pc_oi > 1.3: signals -= 1     # more put OI → bearish
        if pc_vol < 0.7: signals += 1      # more call volume → bullish
        elif pc_vol > 1.3: signals -= 1    # more put volume → bearish

        direction = "bullish" if signals >= 2 else ("bearish" if signals <= -2 else "neutral")

        exp_date = datetime.strptime(best_expiry, "%Y-%m-%d").date()

        return {
            "impliedMove": implied_move,
            "callIV": call_iv_atm,
            "putIV": put_iv_atm,
            "skew25d": skew_25d,
            "pcOI": pc_oi,
            "pcVol": pc_vol,
            "direction": direction,
            "straddleCost": round(straddle, 2),
            "atmStrike": float(atm_strike),
            "expiryUsed": best_expiry,
            "daysToExpiry": (exp_date - date.today()).days,
            "totalCallOI": int(total_call_oi),
            "totalPutOI": int(total_put_oi)
        }, None

    except Exception as e:
        return None, str(e)


def main():
    args = sys.argv[1:]
    dry_run = "--dry" in args
    args = [a for a in args if a != "--dry"]
    filter_ticker = args[0].upper() if args else None

    manifest = json.loads((CONFIGS / "manifest.json").read_text())
    if filter_ticker and filter_ticker not in manifest:
        print(f"[ERROR] {filter_ticker} not in manifest")
        sys.exit(1)

    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    cache.pop("_meta", None)

    tickers = [filter_ticker] if filter_ticker else manifest
    total = 0; errors = 0

    for tk in tickers:
        cfg_path = CONFIGS / f"{tk}.json"
        d = json.loads(cfg_path.read_text())
        co = d.get("company", {})
        catalysts = d.get("catalysts", [])
        if not catalysts:
            continue

        yahoo_tk = co.get("yahooTicker", tk)
        price = co.get("currentPrice", 0)

        try:
            live = yf.Ticker(yahoo_tk)
            hist = live.history(period="1d")
            if not hist.empty:
                price = round(float(hist['Close'].iloc[-1]), 2)
        except:
            pass

        if not price:
            print(f"  {tk:6} SKIP -- no price")
            continue

        if tk not in cache:
            cache[tk] = {}

        for cat in catalysts:
            cat_date = cat.get("dateSort", "")
            if not cat_date:
                continue

            key = f"{cat['asset']}.{cat['indication']}"
            print(f"  {tk:6} {cat['title'][:40]:40} ...", end=" ", flush=True)

            data, err = get_options_data(yahoo_tk, cat_date, price)
            if err:
                print(f"SKIP ({err})")
                errors += 1
                continue

            arrow = {"bullish": "^", "bearish": "v", "neutral": "-"}[data['direction']]
            print(f"+/-{data['impliedMove']}% {arrow} skew={data['skew25d']:+d}pp P/C_OI={data['pcOI']} P/C_Vol={data['pcVol']} -> {data['direction'].upper()}")
            cache[tk][key] = data
            total += 1

    out = {"_meta": {"fetchDate": str(date.today()), "count": total}}
    out.update(dict(sorted(cache.items())))

    if not dry_run:
        CACHE.write_text(json.dumps(out, indent=2))
        print(f"\n[OK] Wrote {CACHE} ({total} new, {errors} errors)")
    else:
        print(f"\n[DRY RUN] Would write {total} quotes, {errors} errors")


if __name__ == "__main__":
    main()
