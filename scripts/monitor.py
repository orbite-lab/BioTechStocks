"""
Biotech Catalyst Monitor — Funnel Architecture
================================================
Designed for 100-1000+ companies at ~$3-8/day total.

Pipeline:
  Tier 1a: ONE broad Sonnet+web_search for major headlines (~$0.15)
  Tier 1b: Batch Haiku+web_search per 20 tickers (~$0.03/batch)
  Tier 2:  Match news against our ticker universe (free, string matching)
  Tier 3:  Haiku triage — is each matched item material? (~$0.006/company)
  Tier 4:  Sonnet deep analysis — only for material events (~$0.10/event)

Cost model:
  4 companies:   1 broad + 1 batch + triage + analysis = ~$0.50-1.00/run
  100 companies:  1 broad + 5 batches + triage + analysis = ~$1-3/run
  1000 companies: 1 broad + 50 batches + triage + analysis = ~$3-8/run
"""

import anthropic
import json
import os
import requests
from datetime import datetime, timezone, timedelta
from pathlib import Path

CONFIGS_DIR = Path("configs")
CHANGELOG_DIR = Path("changelog")
CHANGELOG_DIR.mkdir(exist_ok=True)

client = anthropic.Anthropic()

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


# ─── Tier 1a: Broad news sweep ───────────────────────────────

def sweep_broad_news():
    """One Sonnet call: catch major headlines across all biotech/pharma."""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4000,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        system="""You are a biotech/pharma news scanner. Search for ALL material biotech and pharma news from the last 24 hours.

Focus on: trial data readouts, FDA actions (approvals, CRLs, holds, AdCom), financing events, partnerships, M&A, competitor approvals, regulatory precedents, significant management changes, new epidemiology data.

Use multiple searches:
- "biotech pharma FDA news today"
- "clinical trial results today"
- "FDA approval CRL today"
- "biotech IPO offering today"

Return a JSON array of news items. Each item:
{"headline": "...", "tickers_mentioned": ["TICKER1"], "companies_mentioned": ["Company Name"], "disease_areas": ["GAD", "Lyme"], "event_type": "trial_data|fda_action|financing|partnership|competitor|regulatory|epidemiology", "summary": "2-3 sentences", "source": "URL"}

If no material news, return: []
Return ONLY the JSON array, no other text.""",
        messages=[{"role": "user", "content": "Scan for all material biotech/pharma news from the last 24 hours. Search broadly."}],
    )

    text_parts = [b.text for b in response.content if hasattr(b, "text")]
    full_text = "\n".join(text_parts)

    try:
        json_start = full_text.index("[")
        json_end = full_text.rindex("]") + 1
        return json.loads(full_text[json_start:json_end])
    except (ValueError, json.JSONDecodeError):
        return []


# ─── Tier 1b: Batch ticker-specific searches ─────────────────

def sweep_ticker_batches(tickers_and_names, batch_size=8):
    """Search for news on specific tickers in batches. Catches small-cap events the broad sweep misses."""

    all_items = []
    batches = [tickers_and_names[i:i + batch_size] for i in range(0, len(tickers_and_names), batch_size)]

    for batch_num, batch in enumerate(batches):
        names_list = " OR ".join(f'"{n}"' for _, n in batch)
        tickers_list = ", ".join(t for t, _ in batch)

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=3000,
            tools=[{"type": "web_search_20250305", "name": "web_search"}],
            system="""Search for news about the specific companies listed. Look for ANY news from the last 24 hours about these companies — trial updates, FDA interactions, financing, partnerships, management changes, conference presentations with new data.

Return a JSON array. Each item:
{"headline": "...", "tickers_mentioned": ["TICKER"], "companies_mentioned": ["Name"], "disease_areas": ["disease"], "event_type": "trial_data|fda_action|financing|partnership|competitor|regulatory|epidemiology|other", "summary": "2-3 sentences", "source": "URL"}

If nothing found for this batch, return: []
Return ONLY the JSON array.""",
            messages=[{"role": "user", "content": f"Search for any news from the last 24 hours about these companies:\n{tickers_list}\n\nSearch for: {names_list}"}],
        )

        text_parts = [b.text for b in response.content if hasattr(b, "text")]
        full_text = "\n".join(text_parts)

        try:
            json_start = full_text.index("[")
            json_end = full_text.rindex("]") + 1
            batch_items = json.loads(full_text[json_start:json_end])
            all_items.extend(batch_items)
            print(f"    Batch {batch_num + 1}/{len(batches)}: {len(batch_items)} items ({tickers_list[:60]}...)")
        except (ValueError, json.JSONDecodeError):
            print(f"    Batch {batch_num + 1}/{len(batches)}: parse error, skipping")

    return all_items


# ─── Tier 1: Combined sweep ──────────────────────────────────

def sweep_news(tickers_and_names):
    """Broad sweep + batch ticker searches, deduplicated."""

    # 1a: Broad headlines
    print("  1a: Broad scan...")
    broad = sweep_broad_news()
    print(f"      {len(broad)} broad items")

    # 1b: Ticker-specific batches (Haiku + web_search, much cheaper)
    print("  1b: Ticker-specific batches...")
    specific = sweep_ticker_batches(tickers_and_names)
    print(f"      {len(specific)} specific items")

    # Deduplicate by headline similarity
    all_items = broad.copy()
    existing_headlines = {item.get("headline", "").lower()[:50] for item in broad}

    for item in specific:
        headline_key = item.get("headline", "").lower()[:50]
        if headline_key not in existing_headlines:
            all_items.append(item)
            existing_headlines.add(headline_key)

    return json.dumps(all_items)


# ─── Tier 2: Match news to universe (free) ───────────────────

def match_news_to_universe(news_json, configs):
    try:
        news_items = json.loads(news_json)
    except json.JSONDecodeError:
        return []

    if not news_items:
        return []

    ticker_set = {t.upper() for t in configs}
    name_to_ticker = {cfg["company"]["name"].lower(): t for t, cfg in configs.items()}
    disease_to_tickers = {}
    for ticker, cfg in configs.items():
        for asset in cfg.get("assets", []):
            for ind in asset.get("indications", []):
                disease = ind["name"].lower()
                if disease not in disease_to_tickers:
                    disease_to_tickers[disease] = set()
                disease_to_tickers[disease].add(ticker)

    matched = []
    for item in news_items:
        affected = set()
        for t in item.get("tickers_mentioned", []):
            if t.upper() in ticker_set:
                affected.add(t.upper())
        for name in item.get("companies_mentioned", []):
            t = name_to_ticker.get(name.lower())
            if t:
                affected.add(t)
        for disease in item.get("disease_areas", []):
            for d_key, d_tickers in disease_to_tickers.items():
                if disease.lower() in d_key or d_key in disease.lower():
                    affected.update(d_tickers)
        if affected:
            matched.append({**item, "affected_tickers": list(affected)})

    return matched


# ─── Tier 3: Haiku triage ────────────────────────────────────

def triage_news_item(item, ticker, config):
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=200,
        system="""You are a biotech analyst. Determine if this news is MATERIAL enough to change a company's scenario model assumptions (PoS, approval prob, DR, dilution, market size, penetration, weights).
NOT material: routine press releases, analyst opinions, conference rehash, minor hires.
Respond ONLY with: {"material": true/false, "reason": "one sentence"}""",
        messages=[{"role": "user", "content": f"News: {item['summary']}\nEvent: {item.get('event_type', 'unknown')}\nCompany: {ticker} ({config['company']['name']})\nAssets: {', '.join(a['name'] + ' (' + a['stage'] + ')' for a in config.get('assets', []))}\nMaterial?"}],
    )

    text = response.content[0].text if response.content else ""
    try:
        result = json.loads(text[text.index("{"):text.rindex("}") + 1])
        return result.get("material", False)
    except (ValueError, json.JSONDecodeError):
        return False


# ─── Tier 4: Sonnet deep analysis ────────────────────────────

def deep_analyze(item, ticker, config):
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1500,
        system="""You are a biotech equity analyst. Given material news and a company config, determine exact assumption changes.

Be conservative — typical changes: 5-15pts for PoS/approval, 1-3pts for DR, 0.1-0.3 for pen mult.

Respond ONLY with JSON:
{"news_summary": "one sentence", "source": "URL", "changes": [{"path": "scenarios.base.assumptions.asset_id.ind_id.pos", "old_value": 40, "new_value": 50, "reason": "why"}]}

Path rules:
- scenarios.{bear|base|bull}.assumptions.{asset_id}.{ind_id}.{pos|apr|pen}
- scenarios.{bear|base|bull}.val.{dr|pipelineDR|dil|mult|pipelineMult|commercialMult|commercialRevM|milestones|plat|exus}
- scenarios.{bear|base|bull}.wt
- assets.0.indications.0.market.tamB (numeric indices for arrays)
- company.currentPrice, company.cash""",
        messages=[{"role": "user", "content": f"Material news for {ticker} ({config['company']['name']}):\n{item['summary']}\nSource: {item.get('source', 'N/A')}\n\nConfig:\n{json.dumps(config, indent=2)}\n\nWhat changes?"}],
    )

    text_parts = [b.text for b in response.content if hasattr(b, "text")]
    full_text = "\n".join(text_parts)
    try:
        return json.loads(full_text[full_text.index("{"):full_text.rindex("}") + 1])
    except (ValueError, json.JSONDecodeError):
        return {"news_summary": item.get("summary", ""), "source": "", "changes": []}


# ─── Apply changes ────────────────────────────────────────────

def apply_changes(config, changes):
    updated = json.loads(json.dumps(config))
    applied = []
    for change in changes:
        path = change["path"]
        new_val = change["new_value"]
        keys = path.split(".")
        try:
            obj = updated
            for k in keys[:-1]:
                if isinstance(obj, list):
                    obj = obj[int(k)]
                elif k.isdigit():
                    obj = obj[int(k)]
                else:
                    obj = obj[k]
            last_key = keys[-1]
            if isinstance(obj, list):
                last_key = int(last_key)
            elif last_key.isdigit():
                last_key = int(last_key)
            old_actual = obj[last_key]
            obj[last_key] = new_val
            applied.append({**change, "old_actual": old_actual})
        except (KeyError, TypeError, IndexError, ValueError) as e:
            print(f"  ⚠ Could not apply change at {path}: {e}")
    return updated, applied


# ─── Logging ──────────────────────────────────────────────────

def log_changes(ticker, news_summary, source, applied_changes, timestamp):
    daily_file = CHANGELOG_DIR / f"{timestamp[:10]}.json"
    daily = json.loads(daily_file.read_text()) if daily_file.exists() else []
    daily.append({"timestamp": timestamp, "ticker": ticker, "news": news_summary, "source": source, "changes": applied_changes})
    daily_file.write_text(json.dumps(daily, indent=2))
    update_changelog_html()


def update_changelog_html():
    entries = []
    for f in sorted(CHANGELOG_DIR.glob("*.json"), reverse=True):
        try:
            entries.extend(json.loads(f.read_text()))
        except json.JSONDecodeError:
            continue

    rows = ""
    for e in entries:
        changes_html = "".join(f'<div class="change">{c["path"].split(".")[-1]}: {c.get("old_actual", c.get("old_value","?"))} &rarr; {c["new_value"]} <span class="reason">({c["reason"]})</span></div>' for c in e.get("changes", []))
        source_link = f'<a href="{e["source"]}" target="_blank">source</a>' if e.get("source") else ""
        rows += f'<div class="entry"><div class="meta"><span class="ticker">{e["ticker"]}</span><span class="time">{e["timestamp"][:16]}</span>{source_link}</div><div class="news">{e["news"]}</div>{changes_html}</div>'

    html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Catalyst Changelog</title><link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"><style>*{{box-sizing:border-box;margin:0;padding:0}}body{{background:#0f1117;color:#e2e4ea;font-family:'Inter',sans-serif;padding:32px 24px}}.container{{max-width:800px;margin:0 auto}}h1{{font-size:22px;font-weight:700;margin-bottom:24px;color:#f97316}}.entry{{background:#161920;border-radius:10px;padding:16px 20px;margin-bottom:12px;border:1px solid #ffffff06}}.meta{{display:flex;gap:12px;align-items:center;margin-bottom:8px;font-size:12px}}.ticker{{font-family:'JetBrains Mono';font-weight:700;color:#f97316;background:#f9731616;padding:2px 8px;border-radius:4px}}.time{{color:#6b7080;font-family:'JetBrains Mono'}}a{{color:#60a5fa;text-decoration:none;font-size:11px}}.news{{font-size:14px;color:#b0b4c0;margin-bottom:8px;line-height:1.5}}.change{{font-size:12px;font-family:'JetBrains Mono';color:#22c55e;margin-bottom:3px}}.reason{{color:#6b7080;font-weight:400}}.empty{{text-align:center;color:#6b7080;padding:60px 20px}}</style></head><body><div class="container"><h1>Catalyst changelog</h1><div style="font-size:12px;color:#6b7080;margin-bottom:20px">Auto-updated by Claude. Changes reflect material news impacting rNPV assumptions.</div>{rows if rows else '<div class="empty">No changes logged yet.</div>'}</div></body></html>"""
    Path("changelog.html").write_text(html)


# ─── Telegram ─────────────────────────────────────────────────

def send_telegram(message):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    try:
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            json={"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML", "disable_web_page_preview": True}, timeout=10)
    except Exception:
        pass


def format_telegram_alert(ticker, company_name, news, changes, source):
    lines = [f"\U0001f52c <b>{ticker}</b> \u2014 {company_name}", f"\n\U0001f4f0 {news}"]
    if changes:
        lines.append("\n<b>Changes:</b>")
        for c in changes:
            param = c["path"].split(".")[-1]
            scen = c["path"].split(".")[1] if len(c["path"].split(".")) > 1 else "?"
            old = c.get("old_actual", c.get("old_value", "?"))
            lines.append(f"  \u2022 [{scen}] {param}: {old} \u2192 {c['new_value']}")
    if source:
        lines.append(f"\n\U0001f517 {source}")
    return "\n".join(lines)


# ─── Dedup: track processed news across runs ─────────────────

PROCESSED_FILE = CHANGELOG_DIR / "processed_news.json"
DEDUP_DAYS = 7  # forget news older than 7 days

def load_processed():
    """Load set of already-processed news fingerprints."""
    if not PROCESSED_FILE.exists():
        return {}
    try:
        data = json.loads(PROCESSED_FILE.read_text())
        # Prune entries older than DEDUP_DAYS
        cutoff = (datetime.now(timezone.utc) - timedelta(days=DEDUP_DAYS)).isoformat()
        return {k: v for k, v in data.items() if v > cutoff}
    except (json.JSONDecodeError, Exception):
        return {}

def save_processed(processed):
    """Save processed news fingerprints."""
    PROCESSED_FILE.write_text(json.dumps(processed, indent=2))

def news_fingerprint(item, ticker):
    """Generate a unique fingerprint for a news+ticker pair."""
    headline = item.get("headline", item.get("summary", ""))[:80].lower().strip()
    return f"{ticker}:{hash(headline) & 0xFFFFFFFF:08x}"


# ─── Main ─────────────────────────────────────────────────────

def main():
    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"\u2550\u2550\u2550 Catalyst Monitor (Funnel) \u2014 {now.strftime('%Y-%m-%d %H:%M UTC')} \u2550\u2550\u2550\n")

    manifest_path = CONFIGS_DIR / "manifest.json"
    if not manifest_path.exists():
        print("\u274c No configs/manifest.json")
        return

    tickers = json.loads(manifest_path.read_text())
    configs = {}
    for t in tickers:
        cfg_path = CONFIGS_DIR / f"{t}.json"
        if cfg_path.exists():
            configs[t] = json.loads(cfg_path.read_text())

    print(f"Universe: {len(configs)} companies\n")

    # Tier 1
    print("\u2500\u2500 Tier 1: News sweep (broad + ticker batches) \u2500\u2500")
    tickers_and_names = [(t, configs[t]["company"]["name"]) for t in configs]
    news_json = sweep_news(tickers_and_names)
    try:
        news_items = json.loads(news_json)
    except json.JSONDecodeError:
        news_items = []
    print(f"  Found {len(news_items)} news items\n")

    if not news_items:
        print("\u2713 No news \u2014 done")
        return

    # Tier 2
    print("\u2500\u2500 Tier 2: Match to universe (free) \u2500\u2500")
    matched = match_news_to_universe(news_json, configs)
    print(f"  {len(matched)} items match our companies\n")

    if not matched:
        print("\u2713 No matches \u2014 done")
        return

    # Tier 3
    print("\u2500\u2500 Tier 3: Haiku triage \u2500\u2500")
    processed = load_processed()
    material_items = []
    skipped_dedup = 0
    for item in matched:
        for ticker in item["affected_tickers"]:
            if ticker not in configs:
                continue
            fp = news_fingerprint(item, ticker)
            if fp in processed:
                skipped_dedup += 1
                print(f"  {ticker}: \u00b7 already processed \u2014 {item.get('headline', item['summary'][:60])}")
                continue
            is_mat = triage_news_item(item, ticker, configs[ticker])
            print(f"  {ticker}: {'\u2713 MATERIAL' if is_mat else '\u00b7 skip'} \u2014 {item.get('headline', item['summary'][:60])}")
            if is_mat:
                material_items.append((item, ticker))
            # Mark as processed regardless of materiality — don't re-check next run
            processed[fp] = timestamp
    if skipped_dedup:
        print(f"  ({skipped_dedup} items skipped — already processed in prior runs)")
    print(f"\n  {len(material_items)} material events\n")

    # Save processed fingerprints (even if no material events)
    save_processed(processed)

    if not material_items:
        print("\u2713 No material events \u2014 done")
        return

    # Tier 4
    print("\u2500\u2500 Tier 4: Sonnet deep analysis \u2500\u2500")
    any_changes = False
    summaries = []

    for item, ticker in material_items:
        config = configs[ticker]
        print(f"\n  {ticker}: analyzing...")
        result = deep_analyze(item, ticker, config)
        changes = result.get("changes", [])

        if changes:
            updated_config, applied = apply_changes(config, changes)
            if applied:
                cfg_path = CONFIGS_DIR / f"{ticker}.json"
                cfg_path.write_text(json.dumps(updated_config, indent=2))
                configs[ticker] = updated_config
                news_summary = result.get("news_summary", item.get("summary", ""))
                source = result.get("source", item.get("source", ""))
                log_changes(ticker, news_summary, source, applied, timestamp)
                msg = format_telegram_alert(ticker, config["company"]["name"], news_summary, applied, source)
                send_telegram(msg)
                any_changes = True
                summaries.append(f"{ticker}: {news_summary}")
                print(f"  \u2713 Applied {len(applied)} changes:")
                for c in applied:
                    print(f"    {c['path']}: {c.get('old_actual','?')} \u2192 {c['new_value']}")

    print(f"\n{'─' * 40}")
    if summaries:
        Path("changelog/latest_summary.txt").write_text(" | ".join(summaries[:3]))
        print(f"\u2713 Done \u2014 {len(summaries)} updates")
    else:
        p = Path("changelog/latest_summary.txt")
        if p.exists():
            p.unlink()
        print("\u2713 Done \u2014 no config changes")


if __name__ == "__main__":
    main()
