---
name: product-job-seeker
description: Weekly job scraper for cyy. Pulls the latest issue from 3 job newsletters every Monday, filters for relevant product/ops/PM roles based on cyy's profile, and delivers top 10-15 opportunities via Telegram with application links and LinkedIn search links.
---

# Product Job Seeker

## Purpose

Every Monday, scrape the latest issue from 3 curated job newsletters. Filter for roles that fit cyy's background: consulting + banking + AI product builder. Compile top 10-15 roles and send via Telegram.

---

## Cyy's Profile (use for filtering)

**Background:**
- ~2 years combined consulting + banking (not top-tier MBB, but finance/strategy experience)
- Has built and shipped an AI product (Dropspace)
- No formal engineering/coding background — not a software engineer

**Target roles:**
- Product Manager (PM, APM, Technical PM, AI PM)
- Product Operations
- Project Manager (tech-adjacent)
- Strategy & Operations / BizOps (at a product-focused company)
- Chief of Staff (early-stage or growth-stage tech)
- Program Manager (not government/enterprise only)
- Go-to-Market / Revenue Operations (if product-adjacent)
- Founding / early team product roles

**Hard filters — skip these:**
- Software Engineer, SWE, Backend, Frontend, Full-Stack
- VC / Investor / Principal (unless it's an operator role at a fund)
- Data Scientist, ML Engineer, AI Researcher
- Finance-only (CFO, Controller, FP&A without product exposure)
- Roles requiring 5+ years of PM/product experience
- Roles requiring MBA preferred/required (unless waivable by shipped product experience)

**Soft criteria — use judgment:**
- Prefer roles at AI/tech companies or AI-adjacent (healthtech, fintech, devtools, B2B SaaS)
- Prefer 0-4 years experience requirements (cyy can stretch to 5 if the JD is vague)
- Prefer remote or US-based (NY preferred but not required)
- Slight stretch is OK: if the JD says "2-3 years PM experience" and cyy has adjacent experience + shipped product, flag it with a note
- If it's a product-adjacent role (e.g., Strategy & Ops at an AI company), it's in scope

---

## Sources

### 1. Beyond Bay St. (beyondbayst.substack.com)
Strategy & Ops, Chief of Staff, BizOps across U.S. and Canada. Most structured newsletter — jobs come with direct links.

**How to get latest issue:**
1. Fetch: `https://beyondbayst.substack.com/archive`
2. Find the most recent post URL (first link in the list)
3. Fetch that post's full content

### 2. Next PM Role (nextpmrole.substack.com)
PM-specific newsletter, spun off from Beyond Bay St. Covers Product Manager roles across U.S. and Canada. High signal for cyy's target roles.

**How to get latest issue:**
1. Fetch: `https://nextpmrole.substack.com/archive`
2. Find the most recent post URL (first link in the list)
3. Fetch that post's full content

### 3. Job Hunting Sux (jobhuntingsux.com)
Curated tech, consumer, and entertainment jobs. Narrative style with embedded job links. Skews startup/tech.

**How to get latest issue:**
1. Fetch: `https://www.jobhuntingsux.com/archive`
2. Find the most recent post URL (first link in the list)
3. Fetch that post's full content

### 4. Ali Rohde Jobs (alirohdejobs.substack.com)
Chief of Staff, BizOps, VC roles in tech. May be paywalled — if content is empty or footer-only, skip and note it.

**How to get latest issue:**
1. Fetch: `https://alirohdejobs.substack.com/archive`
2. Find the most recent post URL (first link in the list)
3. Fetch that post's full content
4. If content is essentially empty (paywalled), skip this source and note it in the output

---

## How to Run

### Step 1 — Fetch latest issue from each source

For each source:
- Fetch the `/archive` page
- Extract the first (most recent) post URL
- Fetch that post's full content
- Extract all job listings (title, company, location, link)

### Step 2 — Fetch job descriptions

For each extracted job listing that looks remotely in-scope:
- Fetch the linked page (Greenhouse, Lever, Ashby, Tally, company site, etc.)
- Read the full job description
- Note: years of experience required, key qualifications, what the role actually does

Skip fetching if:
- The link is dead/returns error
- The role title alone clearly disqualifies it (e.g., "Staff Engineer", "VP Finance")

### Step 3 — Filter and score

Apply cyy's profile. For each role that passes the hard filters:

**Score it:**
- **3 pts**: Core target (PM, APM, Technical PM, Product Ops, Chief of Staff at AI/tech company)
- **2 pts**: Adjacent target (BizOps, Strategy & Ops, Program Manager at tech company)
- **1 pt**: Stretch (ops-adjacent at non-tech company, or title is vague but JD looks product-y)
- **0 pts**: Skip (engineering, finance, investor, 5+ years strict)

Pick top 10-15 by score. If fewer than 10 pass, include all that scored 1+.

### Step 4 — Find LinkedIn links

For each selected role:
- If the job was directly posted on LinkedIn, use that URL
- Otherwise, construct a LinkedIn job search URL:
  `https://www.linkedin.com/jobs/search/?keywords=[ROLE TITLE]&f_C=[COMPANY]`
  Encode spaces as `+` or `%20`
  Example: `https://www.linkedin.com/jobs/search/?keywords=Product+Manager&f_C=Metronome`
- Note: LinkedIn search links find the company page, not always the exact listing — tell cyy to verify

### Step 5 — Generate Excel file and send via Telegram

Generate an Excel file with all selected roles, then send it as a file attachment via Telegram.

**Excel columns:**
- Rank
- Role
- Company
- Location
- Why It Fits (1 sentence)
- Exp Required
- Apply Link (direct URL to job listing)
- LinkedIn Search (constructed URL)
- Source (newsletter name)

**How to generate the Excel file:**

Use the exec tool to run this Node.js script (xlsx module is at `/home/cyy/.npm-global/lib/node_modules/xlsx`):

```js
const XLSX = require('/home/cyy/.npm-global/lib/node_modules/xlsx');

const jobs = [ /* array of job objects with the 9 columns */ ];

const wb = XLSX.utils.book_new();
const ws = XLSX.utils.json_to_sheet(jobs);
ws['!cols'] = [
  { wch: 6 },  // Rank
  { wch: 38 }, // Role
  { wch: 32 }, // Company
  { wch: 28 }, // Location
  { wch: 65 }, // Why It Fits
  { wch: 22 }, // Exp Required
  { wch: 58 }, // Apply Link
  { wch: 58 }, // LinkedIn Search
  { wch: 18 }, // Source
];
XLSX.utils.book_append_sheet(wb, ws, 'Jobs');

const filename = `/home/cyy/.openclaw/workspace/job-brief-${DATE}.xlsx`;
XLSX.writeFile(wb, filename);
```

Replace `DATE` with the current date (YYYY-MM-DD format).

**Then send via Telegram using the message tool:**
```
action: send
channel: telegram
target: 8560730620
filePath: /home/cyy/.openclaw/workspace/job-brief-[DATE].xlsx
caption: "Job brief — [Date]. [N] roles from [sources]. Fresh from this week's issues."
```

No plain-text job list needed — the Excel file is the deliverable.

---

## Edge Cases

**If a newsletter hasn't published in the past 10 days:**
- Skip it and note "no recent issue" in output

**If a job link is a Tally form (tally.so/r/...):**
- Fetch the Tally form page to get the role description
- These are often from small AI startups — worth reading carefully

**If a role title is vague (e.g., "Associate", "Manager"):**
- Always fetch the JD before deciding — the title alone is not enough
- "Associate" at an AI company often means PM/ops, not banking analyst

**If a job is clearly for a senior person (VP, Director, Head of):**
- Skip unless the JD specifically says "early career welcome" or the company is tiny (<20 people) where titles are inflated

---

## Schedule

Every Monday. Send by 10 AM ET.

---

## Tracking

Log each run in: `product-job-log.md` in workspace

Format per entry:
```
## [Date]
Sources: [which newsletters had fresh issues]
Jobs found: [total extracted]
Jobs sent: [how many passed filter]
```
