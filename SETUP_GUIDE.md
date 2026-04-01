# Biotech Catalyst Monitor — Complete Setup Guide

Everything you need to deploy an autonomous biotech scenario model with live catalyst monitoring.

---

## What you get

- **Interactive model** at `yourusername.github.io/biotech-model/` — bear/base/bull scenarios with tweakable sliders for PEPG, VRDN, DFTX (and any company you add)
- **Autonomous monitoring** every 12h — Claude + web search checks for material news, updates your assumptions, commits the diff
- **Changelog** at `yourusername.github.io/biotech-model/changelog.html` — full history of every assumption change with timestamps and reasons
- **Telegram alerts** — instant notification when something material happens

**Cost:** ~$10-18/month (Claude API). Everything else is free.

---

## Repo structure

```
biotech-model/
├── index.html                         ← Interactive model (GitHub Pages)
├── changelog.html                     ← Auto-generated change log (created by bot)
├── .gitignore
├── configs/
│   ├── manifest.json                  ← ["PEPG", "VRDN", "DFTX"]
│   ├── PEPG.json                      ← One JSON per company
│   ├── VRDN.json
│   └── DFTX.json
├── changelog/
│   ├── .gitkeep
│   ├── 2026-03-31.json                ← Daily logs (created by bot)
│   └── latest_summary.txt            ← Git commit message (temp)
├── scripts/
│   └── monitor.py                     ← The monitoring script
└── .github/
    └── workflows/
        └── monitor.yml                ← GitHub Actions cron config
```

---

## Step-by-step setup

### Step 1 — Create the GitHub repo (2 min)

1. Go to github.com → click **+** → **New repository**
2. Name: `biotech-model`
3. Visibility: **Public**
4. Check "Add a README file" (we'll replace it)
5. Click **Create repository**

### Step 2 — Upload all files (3 min)

**Option A — GitHub web UI (easiest):**
1. In your repo, click **Add file** → **Upload files**
2. Drag and drop all the files from the `github-pipeline/` folder I gave you
3. For nested folders (configs/, scripts/, .github/workflows/), you'll need to create them:
   - Click **Add file** → **Create new file**
   - Type the full path: `configs/manifest.json` → paste content → commit
   - Repeat for each file

**Option B — Command line:**
```bash
git clone https://github.com/YOUR_USERNAME/biotech-model.git
cd biotech-model
# Copy all files from github-pipeline/ into this folder
git add -A
git commit -m "init"
git push
```

### Step 3 — Enable GitHub Pages (30 sec)

1. Repo → **Settings** → **Pages** (left sidebar)
2. Source: **Deploy from a branch**
3. Branch: **main** / Folder: **/ (root)**
4. Click **Save**
5. Wait ~1 minute → your site is live at `YOUR_USERNAME.github.io/biotech-model/`

### Step 4 — Create Telegram bot (2 min)

1. Open Telegram → search for **@BotFather** → start a chat
2. Send `/newbot`
3. Follow prompts — give it a name like "Catalyst Monitor"
4. **Copy the bot token** (looks like `7123456789:AAF1x2y3z4...`)
5. Open a new chat with YOUR bot (search for its username) → send any message (this activates it)
6. Get your chat ID — open this URL in your browser (replace YOUR_TOKEN):
   ```
   https://api.telegram.org/botYOUR_TOKEN/getUpdates
   ```
7. In the JSON response, find `"chat":{"id":123456789}` — that number is your **chat ID**

### Step 5 — Add secrets to GitHub (1 min)

1. Repo → **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret** for each:

| Secret name | Value | Where to get it |
|---|---|---|
| `ANTHROPIC_API_KEY` | `sk-ant-api03-...` | console.anthropic.com → API Keys |
| `TELEGRAM_BOT_TOKEN` | `7123456789:AAF1x2y3z4...` | From BotFather (step 4) |
| `TELEGRAM_CHAT_ID` | `123456789` | From getUpdates URL (step 4) |

### Step 6 — Test it (1 min)

1. Repo → **Actions** tab
2. Click **"Biotech catalyst monitor"** in the left sidebar
3. Click **"Run workflow"** dropdown → click the green **"Run workflow"** button
4. Watch the run — click into it to see logs
5. If material news exists → check Telegram for a notification
6. Check your repo's git history — if anything changed, you'll see a new commit

---

## How it works

**Every 12 hours (7am + 7pm CET), GitHub Actions runs this pipeline:**

```
For each ticker in manifest.json:
  │
  ├─ Claude API + web_search: "any material news for PEPG?"
  │
  ├─ Claude reads current PEPG.json + the news
  │
  ├─ Material? ──No──→ Log "no change", skip
  │      │
  │     Yes
  │      │
  ├─ Claude outputs updated JSON assumptions
  │   Example: base.pos 40→52, base.dr 28→25
  │   Reason: "FDA lifted partial clinical hold"
  │
  ├─ Also checks cross-company effects
  │   Example: "New TED competitor" → updates VRDN too
  │
  ├─ Writes updated JSON + appends to changelog
  │
  ├─ Git commit + push → GitHub Pages auto-deploys
  │
  └─ Telegram alert:
     🔬 PEPG — PepGen
     📰 FDA lifts partial clinical hold
     • [base] pos: 40 → 52
     • [base] dr: 28 → 25
```

**What counts as "material":**
- Trial data readouts (Phase 1/2/3 results)
- FDA actions (CRL, approval, hold changes, AdCom)
- Financing (offerings, ATM, shelf registration)
- Partnerships / licenses
- Competitor approvals or failures
- Regulatory precedents

**What gets skipped:**
- Routine press releases rehashing known data
- Analyst rating changes
- Conference presentations with no new data
- Routine SEC filings

---

## Adding a new company

1. Create `configs/NEWCO.json` following this template:

```json
{
  "company": {
    "ticker": "NEWCO",
    "name": "Company Name",
    "subtitle": "One-liner context",
    "sharesOut": 100,
    "cash": 500,
    "currentPrice": 10.0,
    "cashRunway": "Into 2028"
  },
  "assets": [
    {
      "id": "drug1",
      "name": "Drug Name",
      "stage": "Phase 2",
      "designations": ["Orphan"],
      "indications": [
        {
          "id": "disease1",
          "name": "Disease Name",
          "market": {
            "patientsK": 25,
            "pricingK": 275,
            "penPct": 14,
            "peakYear": 2033
          }
        }
      ]
    }
  ],
  "scenarios": {
    "bear": {
      "wt": 30,
      "narrative": "What goes wrong",
      "events": ["✗ Bad thing 1", "✗ Bad thing 2", "→ Outcome"],
      "assumptions": {
        "drug1": { "disease1": { "pos": 0, "apr": 0, "pen": 0.4 } }
      },
      "val": { "dr": 35, "dil": 20, "mult": 5, "plat": 0, "exus": 0 }
    },
    "base": {
      "wt": 45,
      "narrative": "Mixed results",
      "events": ["✓ Good thing", "~ Mixed thing", "→ Outcome"],
      "assumptions": {
        "drug1": { "disease1": { "pos": 40, "apr": 65, "pen": 1.0 } }
      },
      "val": { "dr": 25, "dil": 15, "mult": 5, "plat": 100, "exus": 50 }
    },
    "bull": {
      "wt": 25,
      "narrative": "Everything works",
      "events": ["✓ Win 1", "✓ Win 2", "→ Blockbuster"],
      "assumptions": {
        "drug1": { "disease1": { "pos": 75, "apr": 85, "pen": 1.5 } }
      },
      "val": { "dr": 15, "dil": 5, "mult": 5.5, "plat": 500, "exus": 200 }
    }
  },
  "context": {
    "lastData": {
      "date": "Mar 2026",
      "title": "Last data readout",
      "points": ["Key point 1", "Key point 2"]
    },
    "nextCatalyst": {
      "date": "Q3 2026",
      "title": "Next catalyst",
      "thresholds": ["What good looks like"]
    },
    "risks": ["Risk 1", "Risk 2"]
  }
}
```

2. Edit `configs/manifest.json`:
```json
["PEPG", "VRDN", "DFTX", "NEWCO"]
```

3. Commit + push. Done — the button appears on the site, the bot starts monitoring.

**Or just ask me** — "add LEGN to the model" and I'll generate the config with calibrated assumptions.

---

## Market sizing

Two options per indication:

**Bottom-up** (rare disease — you know patient count + pricing):
```json
"market": {
  "patientsK": 25,
  "pricingK": 275,
  "penPct": 14,
  "peakYear": 2033
}
```
Formula: 25K × $275K × 14% = $962M peak revenue

**Top-down** (large market — you know TAM):
```json
"market": {
  "tamB": 9.0,
  "penPct": 10,
  "peakYear": 2032,
  "cagrPct": 12,
  "expansionPct": 20
}
```
Formula: $9B × (1.12)^6 × 1.20 × 10% = peak revenue

---

## Event icons

Use these at the start of event strings in scenarios:
- `✓` → renders green (positive)
- `✗` → renders red (negative)
- `~` → renders amber (mixed)
- `→` → renders grey (outcome/consequence)

---

## Optional: Change your URL

**Rename the repo:**
Settings → General → Repository name → `alpha`
→ URL becomes `yourusername.github.io/alpha/`

**Custom domain** ($10/year):
1. Buy a domain (Namecheap, Cloudflare)
2. Settings → Pages → Custom domain → `models.yourdomain.com`
3. Add CNAME record: `models → yourusername.github.io`
4. Free HTTPS included

---

## Cost breakdown

| Item | Cost |
|---|---|
| GitHub repo + Pages + Actions | Free |
| Telegram bot | Free |
| Claude API (Sonnet + web search) | ~$0.05-0.10 per company per run |
| 3 companies × 2 runs/day | ~$0.30-0.60/day |
| **Monthly total** | **~$10-18** |
| Each additional company | +$3-6/month |

---

## Troubleshooting

**GitHub Pages not loading:** Wait 2-3 minutes after enabling. Check Settings → Pages for the URL.

**Actions workflow not running:** Make sure the `.github/workflows/monitor.yml` file is in the right path. The `.github` folder must be at the repo root.

**Telegram not receiving:** Send any message to your bot first (activates the chat). Verify the chat ID with the getUpdates URL.

**Bot says "no material news" every time:** This is correct if nothing happened in the last 24h. Run manually after a known catalyst (earnings, data readout) to verify it picks it up.

**Config parse errors:** Validate your JSON at jsonlint.com before committing. A missing comma or bracket breaks the whole file.

---

NFA/DYOR. Models are illustrative. Not financial advice.
