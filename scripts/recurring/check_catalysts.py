#!/usr/bin/env python3
"""
Catalyst Auto-Sync
==================
Find missing catalysts in the next N months via web search and AUTO-APPLY them
to configs/<TICKER>.json. Pre-computes success_pos / success_apr / fail_pos /
fail_apr using heuristics seeded by the company's current base-case assumptions.

Replaces the earlier "review proposals manually" workflow — proposals now land
directly in the source-of-truth configs. Audit trail goes to changelog/.

Pipeline
--------
1. Load each config, extract unresolved catalysts in the check window
2. Batch 5 tickers per Sonnet+web_search call
3. Sonnet returns proposals WITH success/fail floors and ceilings already filled
4. Schema validation: asset/indication must exist, dateSort must parse,
   success/fail must be integers in [0,100]
5. Deduplication against existing catalysts by (asset, indication, type, ±30d date)
6. Append new catalysts to config, sort by dateSort, write
7. Log additions to changelog/YYYY-MM-DD.json under action: "catalyst_added"
8. Optional Telegram alert summarizing additions

Usage
-----
    pip install anthropic --break-system-packages
    export ANTHROPIC_API_KEY=sk-ant-...
    python scripts/check_catalysts.py                  # all tickers, auto-apply
    python scripts/check_catalysts.py RVMD VRDN PEPG   # subset
    python scripts/check_catalysts.py --window 90      # 3-month horizon
    python scripts/check_catalysts.py --dry-run        # preview, no writes
"""
import anthropic
import json
import os
import sys
import requests
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CONFIGS_DIR = ROOT / "configs"
MANIFEST = CONFIGS_DIR / "manifest.json"
CHANGELOG_DIR = ROOT / "changelog"
CHANGELOG_DIR.mkdir(exist_ok=True)

DEFAULT_WINDOW_DAYS = 180
BATCH_SIZE = 5
DEDUP_DATE_TOLERANCE_DAYS = 30

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

client = anthropic.Anthropic()


# ─── Loading ──────────────────────────────────────────────────

def load_configs(tickers_filter=None):
    if not MANIFEST.exists():
        print(f"[ERROR] {MANIFEST} not found")
        sys.exit(1)
    all_tickers = json.loads(MANIFEST.read_text())
    target = [t for t in all_tickers if t in tickers_filter] if tickers_filter else all_tickers
    if not target:
        print(f"[ERROR] No matching tickers. Available: {', '.join(all_tickers)}")
        sys.exit(1)
    configs = {}
    for t in target:
        cfg_path = CONFIGS_DIR / f"{t}.json"
        if not cfg_path.exists():
            print(f"  [SKIP] {t}: config not found")
            continue
        try:
            configs[t] = json.loads(cfg_path.read_text())
        except json.JSONDecodeError as e:
            print(f"  [SKIP] {t}: bad JSON ({e})")
    return configs


def get_base_pos_apr(config, asset_id, indication_id):
    base_assumptions = (
        config.get("scenarios", {}).get("base", {}).get("assumptions", {})
    )
    asset_block = base_assumptions.get(asset_id, {})
    ind_block = asset_block.get(indication_id, {})
    return {
        "pos": ind_block.get("pos", 50),
        "apr": ind_block.get("apr", 50),
    }


def summarize_existing_catalysts(config, window_end):
    out = []
    for cat in config.get("catalysts", []):
        if cat.get("resolved"):
            continue
        ds = cat.get("dateSort", "")
        try:
            cat_date = datetime.fromisoformat(ds.replace("Z", "+00:00")) if ds else None
        except (ValueError, AttributeError):
            cat_date = None
        if cat_date and cat_date.replace(tzinfo=None) > window_end:
            continue
        out.append({
            "title": cat.get("title", ""),
            "asset": cat.get("asset", ""),
            "indication": cat.get("indication", ""),
            "type": cat.get("type", ""),
            "dateSort": ds,
        })
    return out


def summarize_recent_past_catalysts(config, today, lookback_days=90):
    """Past catalysts in the last `lookback_days`. Used by the LLM to judge
    whether the subtitle thesis line is stale (e.g. last quarter's readout
    still framing today's narrative even though the event has landed)."""
    cutoff = today - timedelta(days=lookback_days)
    out = []
    for cat in config.get("catalysts", []):
        ds = cat.get("dateSort", "")
        try:
            cat_date = datetime.fromisoformat(ds.replace("Z", "+00:00")) if ds else None
        except (ValueError, AttributeError):
            cat_date = None
        if not cat_date:
            continue
        cat_date_n = cat_date.replace(tzinfo=None)
        if cat_date_n < cutoff or cat_date_n > today.replace(tzinfo=None):
            continue
        out.append({
            "title": cat.get("title", ""),
            "dateSort": ds,
            "type": cat.get("type", ""),
            "asset": cat.get("asset", ""),
            "indication": cat.get("indication", ""),
        })
    return out


# ─── Sonnet call ──────────────────────────────────────────────

SYSTEM_PROMPT = """You are a biotech equity analyst auto-syncing catalyst tracking. Today is {today}.

For each company, find any MATERIAL catalysts in the next {window_days} days (between {today} and {window_end}) that are NOT already in their existing_catalysts_in_window list. Return them in JSON with success_pos, success_apr, fail_pos, fail_apr ALREADY COMPUTED using the heuristics below.

WHAT COUNTS AS MATERIAL
- Phase 1/2/3 trial readouts (primary completion dates from ClinicalTrials.gov)
- PDUFA dates (FDA action dates)
- AdCom meetings
- EMA / MHRA / PMDA opinions or approvals
- Label expansion decisions (sNDA outcomes)
- Major data presentations at named conferences (ASCO, AACR, ASH, ACC, JPM, ESMO, etc.) WITH a confirmed date
- Pivotal trial initiations announced as 2026 milestones
- Partnership / licensing milestones with disclosed dates

NOT MATERIAL — do not propose
- Vague guidance like "data expected H2"
- Phase 1 dose-escalation routine cohort updates
- Earnings calls (the events themselves)
- Investor day generic presentations
- Patent filings, hires, board changes
- Events that have ALREADY occurred (see VERIFICATION below)

VERIFICATION — events already occurred
This is critical: company press releases and earnings filings are often DATED BEFORE an event but say "expected H1 2026" or "anticipated mid-year." If you read this language verbatim WITHOUT checking for follow-up news, you will propose catalysts for events that have already happened.

For EVERY catalyst you are about to propose, run an additional web_search of the form:
  "<COMPANY> <TRIAL OR EVENT NAME> results"
  "<COMPANY> <DRUG NAME> readout 2026"
  "<COMPANY> <PDUFA DRUG> approved OR CRL"

Look specifically for news dated AFTER the source you originally found. If the search returns:
- A press release announcing the readout (positive, negative, or mixed) — the event HAPPENED, do NOT propose
- An FDA approval / CRL / AdCom vote announcement — the event HAPPENED, do NOT propose
- A stock price reaction post-event (e.g. "shares fell 38%", "stock surged on data") — the event HAPPENED, do NOT propose
- Coverage describing the trial as "completed" or "read out" — the event HAPPENED, do NOT propose

A company saying "expected H1 2026" in a January earnings release is NOT proof the event is still pending in April 2026. The release is stale guidance, not current state. Always cross-check.

If you find conflicting signals (some sources call the event "upcoming," others describe results), TRUST THE MORE RECENT SOURCE. Recent dated news always overrides older guidance.

When in doubt — if you cannot find clear post-event news AND you cannot confirm the event is still future-dated — skip the proposal. False negatives (missing a catalyst) are recoverable on the next bi-monthly run. False positives (proposing already-occurred catalysts) corrupt the source-of-truth config and require manual cleanup.

ASSET MATCHING
Match each catalyst to one of the company's existing asset.id and indication.id from their assets list. NEVER invent new asset ids. If you cannot match cleanly, skip the proposal — do not return it with empty asset.

SUCCESS / FAIL HEURISTICS
For each proposed catalyst, set:
  fail_pos:    pos floor IF the catalyst fails (program impaired or dies)
  fail_apr:    apr floor IF the catalyst fails
  success_pos: pos ceiling IF the catalyst hits (de-risked)
  success_apr: apr ceiling IF the catalyst hits

Use the company's current_base_assumptions for that asset/indication as a seed. The input includes `current_base_pos` and `current_base_apr` for each matched asset+indication. Apply these rules:

- phase3_data (binary pivotal readout):
    fail_pos: 0   |  fail_apr: 0
    success_pos: 80 (clinically de-risked)  |  success_apr: 85
    EXCEPTION: if the asset has multiple indications and only one is being read out,
    fail_pos floor is max(5, current_base_pos - 30) instead of 0.

- phase2_data:
    fail_pos: max(5, current_base_pos - 25)
    fail_apr: max(10, current_base_apr - 25)
    success_pos: min(70, current_base_pos + 20)
    success_apr: min(80, current_base_apr + 20)

- phase1_data:
    fail_pos: max(5, current_base_pos - 15)
    fail_apr: max(10, current_base_apr - 10)
    success_pos: min(50, current_base_pos + 15)
    success_apr: min(60, current_base_apr + 10)

- pdufa (FDA action):
    fail_pos: current_base_pos (clinical already done)
    fail_apr: 5 (CRL, retry possible)
    success_pos: current_base_pos
    success_apr: 100

- adcom:
    fail_pos: current_base_pos
    fail_apr: max(15, current_base_apr - 35)
    success_pos: current_base_pos
    success_apr: min(95, current_base_apr + 15)

- ema_approval:
    fail_pos: current_base_pos
    fail_apr: max(20, current_base_apr - 25)
    success_pos: current_base_pos
    success_apr: 95

- label_expansion:
    fail_pos: current_base_pos
    fail_apr: max(20, current_base_apr - 15)
    success_pos: current_base_pos
    success_apr: min(95, current_base_apr + 10)

- phase3_start / phase2_start / phase1_start:
    fail_pos: max(5, current_base_pos - 5)  (delay = mild bear)
    fail_apr: current_base_apr
    success_pos: min(100, current_base_pos + 5)
    success_apr: current_base_apr

- conference_data (non-pivotal data presentation):
    fail_pos: max(5, current_base_pos - 8)
    fail_apr: max(5, current_base_apr - 5)
    success_pos: min(100, current_base_pos + 8)
    success_apr: min(100, current_base_apr + 5)

- partnership / other:
    fail_pos: current_base_pos
    fail_apr: current_base_apr
    success_pos: min(100, current_base_pos + 10)
    success_apr: min(100, current_base_apr + 5)

All four fields MUST be integers in [0, 100]. success_pos must be >= fail_pos. success_apr must be >= fail_apr.

SUBTITLE THESIS LINE
Each company has a `current_subtitle` — a short free-form thesis line that reads like
"<Company Name> · <current framing>" (e.g. "Viridian Therapeutics · Post-REVEAL-1 · Batoclimab TED failure (Apr 2 2026) clears competitive path").

Propose an updated subtitle when BOTH are true:
  1) A material catalyst listed in `recent_resolved_catalysts` (last 90 days) makes the
     current framing stale — e.g. subtitle references "pre-data" but the data is now out,
     a competitor event has resolved, or a pivotal readout has landed.
  2) You have concrete post-event evidence from web_search confirming the outcome and
     can restate the thesis in one punchy clause.

Rules for subtitle output:
  - ALWAYS lead with the company name verbatim, then " · ", then the new thesis clause.
  - Keep it under 140 characters total.
  - NO em-dashes (use " - " or " · ").
  - NO hallucinated asset names or dates. If you can't confirm, skip the proposal.
  - Preserve editorial voice ("clears competitive path", "de-risks BLA", etc. are good;
    generic "strong pipeline" is bad).
  - Skip entirely if the current subtitle still reads as accurate — do not rewrite for style.

OUTPUT
Output ONLY valid JSON, no preamble:
{{
  "TICKER1": [
    {{
      "title": "RASolute 305 1L PDAC Phase 3 first patient dosed",
      "date": "H2 2026",
      "dateSort": "2026-09-01",
      "asset": "zoldon",
      "indication": "g12d",
      "type": "phase3_start",
      "binary": false,
      "fail_pos": 25,
      "fail_apr": 30,
      "success_pos": 35,
      "success_apr": 30,
      "source": "https://...",
      "confidence": "high",
      "rationale": "one sentence"
    }}
  ],
  "TICKER2": [],
  "_subtitles": {{
    "TICKER1": {{
      "text": "Revolution Medicines · Daraxonrasib PDAC Ph3 positive · consensus peak revises higher",
      "rationale": "RASolute 303 primary endpoint hit April 15 2026; subtitle previously said 'awaiting pivotal data'",
      "confidence": "high",
      "source": "https://..."
    }}
  }}
}}

ALWAYS include every requested ticker as a key in the top level (value is the catalyst array). Include "_subtitles" as a top-level object (may be empty {{}}) — only include tickers that need an update. Set "binary": true only for pivotal phase 2/3 readouts and PDUFA. confidence in {{high, medium, low}}."""


def check_batch(batch_configs, window_days):
    today = datetime.now(timezone.utc)
    today_str = today.strftime("%Y-%m-%d")
    window_end = today + timedelta(days=window_days)
    window_end_str = window_end.strftime("%Y-%m-%d")

    briefs = []
    for ticker, cfg in batch_configs.items():
        co = cfg.get("company", {})
        existing = summarize_existing_catalysts(cfg, window_end.replace(tzinfo=None))
        recent_past = summarize_recent_past_catalysts(cfg, today)
        base_lookup = {}
        for a in cfg.get("assets", []):
            for i in a.get("indications", []):
                key = f"{a.get('id', '')}.{i.get('id', '')}"
                base_lookup[key] = get_base_pos_apr(cfg, a.get("id", ""), i.get("id", ""))
        briefs.append({
            "ticker": ticker,
            "name": co.get("name", ticker),
            "current_subtitle": co.get("subtitle", ""),
            "phase": co.get("phase", ""),
            "assets": [
                {
                    "id": a.get("id", ""),
                    "name": a.get("name", ""),
                    "stage": a.get("stage", ""),
                    "indications": [
                        {"id": i.get("id", ""), "name": i.get("name", "")}
                        for i in a.get("indications", [])
                    ],
                }
                for a in cfg.get("assets", [])
            ],
            "current_base_assumptions": base_lookup,
            "existing_catalysts_in_window": existing,
            "recent_resolved_catalysts": recent_past,
        })

    system = SYSTEM_PROMPT.format(
        today=today_str, window_end=window_end_str, window_days=window_days
    )
    user_content = (
        f"Find missing catalysts for these {len(briefs)} companies in the next {window_days} days. "
        f"Today is {today_str}. "
        f"For EVERY candidate catalyst, run a follow-up web_search with the trial/drug name + 'results' or 'readout' to confirm the event has NOT already occurred. "
        f"If you find post-event news (positive, negative, or mixed outcome), DO NOT propose that catalyst. "
        f"Trust recent dated news over older company guidance. Use the heuristic formulas to fill success/fail values:\n\n"
        + json.dumps(briefs, indent=2)
    )

    print(f"  Calling Sonnet+web_search for {len(briefs)} tickers: {', '.join(batch_configs.keys())}...")
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8000,
            tools=[{"type": "web_search_20250305", "name": "web_search"}],
            system=system,
            messages=[{"role": "user", "content": user_content}],
        )
    except Exception as e:
        print(f"  [ERROR] API call failed: {e}")
        return {t: [] for t in batch_configs.keys()}

    text_parts = [b.text for b in response.content if hasattr(b, "text")]
    full_text = "\n".join(text_parts)
    try:
        first = full_text.index("{")
        last = full_text.rindex("}")
        result = json.loads(full_text[first:last + 1])
    except (ValueError, json.JSONDecodeError) as e:
        print(f"  [WARN] Could not parse model response: {e}")
        print(f"  Raw (first 500 chars): {full_text[:500]}")
        return {t: [] for t in batch_configs.keys()}, {}

    subtitle_proposals = result.pop("_subtitles", {}) or {}
    if not isinstance(subtitle_proposals, dict):
        subtitle_proposals = {}
    for t in batch_configs.keys():
        if t not in result or not isinstance(result.get(t), list):
            result[t] = []
    return result, subtitle_proposals


# ─── Validation + dedup ──────────────────────────────────────

def _clamp_int(v, lo, hi):
    try:
        return max(lo, min(hi, int(round(float(v)))))
    except (ValueError, TypeError):
        return None


def validate_proposal(prop, valid_asset_ids, valid_indication_pairs):
    """Return (cleaned_dict, ok, reason). cleaned_dict has clamped ints."""
    for k in ("title", "dateSort", "type", "asset", "indication"):
        if not prop.get(k):
            return None, False, f"missing {k}"
    try:
        datetime.fromisoformat(prop["dateSort"])
    except (ValueError, TypeError):
        return None, False, f"invalid dateSort {prop.get('dateSort')}"
    if prop["asset"] not in valid_asset_ids:
        return None, False, f"unknown asset {prop['asset']}"
    if (prop["asset"], prop["indication"]) not in valid_indication_pairs:
        return None, False, f"asset {prop['asset']} has no indication {prop['indication']}"

    fp = _clamp_int(prop.get("fail_pos"), 0, 100)
    fa = _clamp_int(prop.get("fail_apr"), 0, 100)
    sp = _clamp_int(prop.get("success_pos"), 0, 100)
    sa = _clamp_int(prop.get("success_apr"), 0, 100)
    if None in (fp, fa, sp, sa):
        return None, False, "non-integer success/fail value"
    if sp < fp or sa < fa:
        return None, False, f"success < fail (pos {sp}<{fp}, apr {sa}<{fa})"

    cleaned = {
        "date": prop.get("date", ""),
        "dateSort": prop["dateSort"],
        "asset": prop["asset"],
        "indication": prop["indication"],
        "title": prop["title"],
        "type": prop["type"],
        "binary": bool(prop.get("binary", False)),
        "fail_pos": fp,
        "fail_apr": fa,
        "success_pos": sp,
        "success_apr": sa,
        "_source": "auto",
        "_sourceUrl": prop.get("source", ""),
        "_addedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "_confidence": prop.get("confidence", "medium"),
        "_rationale": prop.get("rationale", ""),
    }
    return cleaned, True, ""


def validate_subtitle_proposal(prop, company_name, current_subtitle):
    """Return (cleaned_text, ok, reason). Enforces name prefix, length cap,
    and rejects if proposal is identical to current or trivially cosmetic."""
    if not isinstance(prop, dict):
        return None, False, "not a dict"
    text = (prop.get("text") or "").strip()
    conf = (prop.get("confidence") or "medium").lower()
    if not text:
        return None, False, "empty text"
    if len(text) > 180:
        return None, False, f"too long ({len(text)} chars)"
    if company_name and not text.lower().startswith(company_name.lower()[:6]):
        return None, False, f"must start with company name '{company_name}'"
    # Replace em-dashes defensively
    text = text.replace("\u2014", " - ").replace("\u2013", " - ")
    if text.strip() == (current_subtitle or "").strip():
        return None, False, "identical to current"
    if conf not in ("high", "medium", "low"):
        conf = "medium"
    # Only high-confidence proposals auto-apply; medium/low require manual review
    # (we still accept them into the changelog for visibility)
    return {
        "text": text,
        "confidence": conf,
        "rationale": prop.get("rationale", ""),
        "source": prop.get("source", ""),
    }, True, ""


def is_duplicate(prop, existing_catalysts):
    try:
        prop_date = datetime.fromisoformat(prop["dateSort"])
    except (ValueError, TypeError):
        return False
    for cat in existing_catalysts:
        if cat.get("asset") != prop["asset"]:
            continue
        if cat.get("indication") != prop["indication"]:
            continue
        if cat.get("type") != prop["type"]:
            continue
        try:
            cat_date = datetime.fromisoformat(cat.get("dateSort", ""))
        except (ValueError, TypeError):
            continue
        if abs((cat_date - prop_date).days) <= DEDUP_DATE_TOLERANCE_DAYS:
            return True
    return False


# ─── Changelog ───────────────────────────────────────────────

def log_additions(ticker, additions, timestamp):
    if not additions:
        return
    daily_file = CHANGELOG_DIR / f"{timestamp[:10]}.json"
    daily = json.loads(daily_file.read_text()) if daily_file.exists() else []
    if not isinstance(daily, list):
        daily = []
    for add in additions:
        daily.append({
            "timestamp": timestamp,
            "ticker": ticker,
            "action": "catalyst_added",
            "catalyst": add,
            "source": add.get("_sourceUrl", ""),
        })
    daily_file.write_text(json.dumps(daily, indent=2))


def log_subtitle_update(ticker, old_text, new_prop, timestamp, applied):
    daily_file = CHANGELOG_DIR / f"{timestamp[:10]}.json"
    daily = json.loads(daily_file.read_text()) if daily_file.exists() else []
    if not isinstance(daily, list):
        daily = []
    daily.append({
        "timestamp": timestamp,
        "ticker": ticker,
        "action": "subtitle_updated" if applied else "subtitle_proposed",
        "old": old_text,
        "new": new_prop["text"],
        "confidence": new_prop["confidence"],
        "rationale": new_prop.get("rationale", ""),
        "source": new_prop.get("source", ""),
    })
    daily_file.write_text(json.dumps(daily, indent=2))


# ─── Telegram ────────────────────────────────────────────────

def send_telegram(text):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        return
    try:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage",
            json={"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "HTML"},
            timeout=10,
        )
    except Exception as e:
        print(f"  [WARN] Telegram send failed: {e}")


# ─── Main ────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]

    window_days = DEFAULT_WINDOW_DAYS
    if "--window" in args:
        idx = args.index("--window")
        if idx + 1 < len(args):
            try:
                window_days = int(args[idx + 1])
                args = args[:idx] + args[idx + 2:]
            except ValueError:
                print("[ERROR] --window expects an integer")
                sys.exit(1)

    tickers_filter = args if args else None

    print("═══ Catalyst Auto-Sync ═══")
    print(f"Window: next {window_days} days")
    print(f"Today:  {datetime.now(timezone.utc).strftime('%Y-%m-%d')}")
    print(f"Mode:   {'DRY RUN' if dry_run else 'AUTO-APPLY'}\n")

    configs = load_configs(tickers_filter)
    print(f"Loaded {len(configs)} configs\n")
    if not configs:
        print("[ERROR] No configs loaded")
        sys.exit(1)

    tickers = sorted(configs.keys())
    all_proposals = {}
    all_subtitle_proposals = {}
    batches = [tickers[i:i + BATCH_SIZE] for i in range(0, len(tickers), BATCH_SIZE)]
    print(f"Processing {len(batches)} batch(es) of up to {BATCH_SIZE} tickers...\n")

    for i, batch in enumerate(batches, 1):
        print(f"── Batch {i}/{len(batches)} ──")
        batch_cfgs = {t: configs[t] for t in batch}
        result, subtitle_props = check_batch(batch_cfgs, window_days)
        all_proposals.update(result)
        all_subtitle_proposals.update(subtitle_props)
        for t in batch:
            n = len(result.get(t, []))
            sub_mark = " (+sub)" if t in subtitle_props else ""
            print(f"  {t:8} {'✓ none' if n == 0 else f'+{n} candidate(s)'}{sub_mark}")
        print()

    print("── Validating + applying ──")
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    total_added = 0
    total_rejected = 0
    total_duplicate = 0
    total_subtitles_applied = 0
    total_subtitles_proposed = 0
    summary_lines = []
    subtitle_summary_lines = []

    for ticker, props in all_proposals.items():
        if ticker not in configs:
            continue
        cfg = configs[ticker]
        valid_asset_ids = {a.get("id", "") for a in cfg.get("assets", [])}
        valid_indication_pairs = set()
        for a in cfg.get("assets", []):
            for i in a.get("indications", []):
                valid_indication_pairs.add((a.get("id", ""), i.get("id", "")))

        existing_cats = cfg.get("catalysts", [])
        kept = []
        for p in props:
            cleaned, ok, reason = validate_proposal(p, valid_asset_ids, valid_indication_pairs)
            if not ok:
                print(f"  [REJECT] {ticker}: {p.get('title', '?')[:60]} — {reason}")
                total_rejected += 1
                continue
            if is_duplicate(cleaned, existing_cats):
                print(f"  [DUP]    {ticker}: {cleaned['title'][:60]} — already tracked")
                total_duplicate += 1
                continue
            kept.append(cleaned)

        if not kept:
            continue

        new_cats = list(existing_cats) + kept
        new_cats.sort(key=lambda c: c.get("dateSort", "9999"))
        cfg["catalysts"] = new_cats

        if not dry_run:
            cfg_path = CONFIGS_DIR / f"{ticker}.json"
            cfg_path.write_text(json.dumps(cfg, indent=2))
            log_additions(ticker, kept, timestamp)

        total_added += len(kept)
        for k in kept:
            print(f"  [ADD]    {ticker}: {k['date']:8} {k['type']:18} {k['title'][:55]}")
            print(f"           pos {k['fail_pos']}->{k['success_pos']} apr {k['fail_apr']}->{k['success_apr']} ({k['_confidence']})")
            summary_lines.append(f"{ticker}: {k['title'][:55]} ({k['date']})")

    # ── Subtitle updates ─────────────────────────────────────────────
    # Only HIGH-confidence proposals auto-apply; medium/low are logged for review.
    print("── Subtitle proposals ──")
    for ticker, prop in all_subtitle_proposals.items():
        if ticker not in configs:
            continue
        cfg = configs[ticker]
        co = cfg.get("company", {})
        current = co.get("subtitle", "")
        name = co.get("name", ticker)
        cleaned, ok, reason = validate_subtitle_proposal(prop, name, current)
        if not ok:
            print(f"  [REJECT] {ticker}: subtitle - {reason}")
            continue
        total_subtitles_proposed += 1
        apply_now = cleaned["confidence"] == "high"
        if apply_now:
            co["subtitle"] = cleaned["text"]
            if not dry_run:
                cfg_path = CONFIGS_DIR / f"{ticker}.json"
                cfg_path.write_text(json.dumps(cfg, indent=2))
                log_subtitle_update(ticker, current, cleaned, timestamp, applied=True)
            total_subtitles_applied += 1
            print(f"  [APPLY]  {ticker}: {cleaned['text'][:80]}")
            subtitle_summary_lines.append(f"{ticker}: {cleaned['text'][:70]}")
        else:
            if not dry_run:
                log_subtitle_update(ticker, current, cleaned, timestamp, applied=False)
            print(f"  [PROPOSE {cleaned['confidence']:6}] {ticker}: {cleaned['text'][:70]}")
    if not all_subtitle_proposals:
        print("  (none)")

    print()
    print("═══ Summary ═══")
    print(f"  Catalysts added:      {total_added}")
    print(f"  Catalyst duplicates:  {total_duplicate}")
    print(f"  Catalysts rejected:   {total_rejected}")
    print(f"  Subtitles applied:    {total_subtitles_applied}")
    print(f"  Subtitles proposed:   {total_subtitles_proposed - total_subtitles_applied} (not auto-applied)")

    if dry_run:
        print(f"\n[dry-run] No files written")
    elif total_added > 0 or total_subtitles_applied > 0:
        touched = {l.split(':')[0] for l in summary_lines} | {l.split(':')[0] for l in subtitle_summary_lines}
        print(f"\n✓ Updated {len(touched)} configs")
        print(f"✓ Logged to changelog/{timestamp[:10]}.json")
        tg_parts = []
        if total_added > 0:
            tg_parts.append(f"<b>📅 {total_added} new catalyst(s) auto-added</b>\n" + "\n".join(f"• {s}" for s in summary_lines[:15]))
            if len(summary_lines) > 15:
                tg_parts.append(f"… and {len(summary_lines) - 15} more")
        if total_subtitles_applied > 0:
            tg_parts.append(f"<b>📝 {total_subtitles_applied} subtitle(s) updated</b>\n" + "\n".join(f"• {s}" for s in subtitle_summary_lines[:10]))
        if tg_parts:
            send_telegram("\n\n".join(tg_parts))
    else:
        print(f"\n✓ All configs are up to date")


if __name__ == "__main__":
    main()
