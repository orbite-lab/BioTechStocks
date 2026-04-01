# Biotech Catalyst Monitor

Autonomous pipeline that monitors biotech catalysts, updates scenario models, and notifies via Telegram.

## Architecture

```
GitHub Actions (cron every 12h)
  → scripts/monitor.py
    → Claude API + web_search (per ticker)
    → Material? → Update configs/*.json
    → Log to changelog/*.json + changelog.html
    → Git commit + push → GitHub Pages auto-deploys
    → Telegram alert with diff
```

## Setup (10 minutes)

### 1. Create the GitHub repo

```bash
# Clone or create a new repo
git init biotech-model
cd biotech-model

# Copy all these files into the repo
# (index.html, configs/, scripts/, .github/workflows/)

git add -A
git commit -m "Initial setup"
git push -u origin main
```

### 2. Enable GitHub Pages

- Repo → Settings → Pages → Source: "Deploy from a branch" → Branch: `main` → Folder: `/ (root)` → Save
- Your site will be at `https://yourusername.github.io/biotech-model/`

### 3. Set up Telegram bot

1. Message @BotFather on Telegram → `/newbot` → follow prompts
2. Copy the bot token (looks like `123456:ABC-DEF...`)
3. Message your new bot (send anything to activate it)
4. Get your chat ID:
   ```
   curl https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates
   ```
   Look for `"chat":{"id":123456789}` — that number is your chat ID

### 4. Add secrets to GitHub

Repo → Settings → Secrets and variables → Actions → New repository secret:

| Secret name | Value |
|---|---|
| `ANTHROPIC_API_KEY` | Your Anthropic API key (sk-ant-...) |
| `TELEGRAM_BOT_TOKEN` | From BotFather (123456:ABC-DEF...) |
| `TELEGRAM_CHAT_ID` | Your chat ID number |

### 5. Test it

- Go to repo → Actions → "Biotech catalyst monitor" → "Run workflow" → click the green button
- Watch the run log
- Check Telegram for notifications (if any material news exists)

## File structure

```
├── index.html              ← Interactive model (GitHub Pages serves this)
├── changelog.html          ← Auto-generated change log page
├── configs/
│   ├── manifest.json       ← ["PEPG", "VRDN", "DFTX"]
│   ├── PEPG.json           ← Company configs (updated by bot)
│   ├── VRDN.json
│   └── DFTX.json
├── changelog/
│   ├── 2026-03-31.json     ← Daily change logs (auto-generated)
│   └── latest_summary.txt  ← Used for git commit message
├── scripts/
│   └── monitor.py          ← The monitoring script
└── .github/workflows/
    └── monitor.yml         ← GitHub Actions cron config
```

## Adding a new company

1. Create `configs/NEWCO.json` (use any existing config as template)
2. Add `"NEWCO"` to `configs/manifest.json`
3. Commit + push
4. The monitor will start checking NEWCO on the next run

Or: ask Claude to generate the config — "add LEGN to the model" → paste the output.

## How the monitor decides what's "material"

Material events that trigger config updates:
- **Trial data readouts** (Phase 1/2/3 results) → changes PoS, approval probability
- **FDA actions** (CRL, approval, hold lifted/imposed, advisory committee) → changes PoS, DR, approval
- **Financing** (offerings, ATM, shelf registration) → changes dilution, cash
- **Partnerships/licenses** (deals, royalty agreements) → changes platform value, ex-US
- **Competitor events** (approvals, data, withdrawals) → cross-company market changes
- **Regulatory precedents** (new guidance, REMS changes) → changes DR, approval across companies

NOT material (skipped):
- Routine press releases rehashing known info
- Analyst rating changes / price target updates
- Conference presentations with no new data
- Management hires (unless CEO/CMO level)
- Routine SEC filings

## Cross-company effects

The monitor is aware of ALL companies in the portfolio. When a news event for company A affects company B's market, it updates both configs. Examples:

- "FDA approves new TED drug" → VRDN market sizing changes
- "New DM1 natural history study shows higher prevalence" → PEPG patient population changes
- "Psychiatric drug class labeling change" → DFTX regulatory risk changes

## Cost

- Claude API: ~$0.05-0.10 per company per run (Sonnet + web search)
- 3 companies × 2 runs/day = ~$0.30-0.60/day ≈ **$10-18/month**
- GitHub Actions: free for public repos, 2000 min/month for private repos
- Telegram: free

## Telegram message format

```
🔬 PEPG — PepGen

📰 FDA lifts partial clinical hold on FREEDOM2 trial

Config changes:
  • [base] pos: 40 → 52
  • [base] dr: 28 → 25
  • [bull] pos: 75 → 82

🔗 https://example.com/article
```
