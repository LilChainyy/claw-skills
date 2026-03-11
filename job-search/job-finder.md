---
name: job-finder
description: Automated startup job discovery. Scans multiple sources for relevant roles, filters by profile fit, and pushes matches to a Notion database. Self-improving — tracks what you click on to refine future results.
---

# Job Finder

## Purpose

Continuously discover early-stage startup roles that match your profile. Push company name + role link to Notion. Learn over time what you're interested in.

## Your Profile (filter criteria)

- **Roles:** Product Manager, Strategic Projects, Forward Deployed Engineer, Deployment Strategist, Business Operations, AI Strategist, GTM roles at AI companies
- **Stage:** Seed to Series B. <200 people. Founding-team energy.
- **Domain:** AI/ML infrastructure, fintech, devtools, enterprise AI, data platforms
- **Location:** NYC preferred, SF ok, remote ok
- **Comp floor:** $120K+ base
- **Background match:** Values consulting/FDD experience, technical building (LLM pipelines, RAG), customer-facing roles, ambiguity tolerance
- **Red flags to skip:** Pure engineering (>80% coding), pure sales/BDR, companies with no funding info, roles requiring 5+ years specific domain experience

## Sources (checked in order)

### 1. HN "Who is Hiring?" (Monthly)
- **URL pattern:** `https://news.ycombinator.com/item?id={THREAD_ID}`
- **API:** `https://hacker-news.firebaseio.com/v0/item/{id}.json`
- **How:** Fetch thread → get all top-level comment IDs → fetch each comment → parse company name, role, location, remote status, description
- **Finding the thread:** Search `https://hn.algolia.com/api/v1/search?query="Who is hiring"&tags=ask_hn&numericFilters=created_at_i>{UNIX_30_DAYS_AGO}` for the latest thread ID
- **Frequency:** 1st of every month (new thread posted automatically)

### 2. Wellfound (AngelList) — Startup Jobs
- **URL:** `https://wellfound.com/role/l/product-manager/united-states`
- **How:** Fetch listing pages, filter by stage/funding/role
- **Frequency:** Weekly

### 3. YC Work at a Startup
- **URL:** `https://www.workatastartup.com/jobs`
- **API:** `https://www.workatastartup.com/companies/autocomplete?query=&page=1&batch=&demo_day=true`
- **How:** Filter by role type, company size, funding
- **Frequency:** Weekly

### 4. Ashby Job Boards (direct)
- **How:** For companies on your radar, check `https://api.ashbyhq.com/posting-api/job-board/{slug}?includeCompensation=true`
- **Frequency:** When researching specific companies

### 5. Recently Funded Companies
- **Sources:**
  - Crunchbase recent rounds: search for Seed/A/B in AI, fintech, devtools
  - TechCrunch funding tag: `https://techcrunch.com/category/fundraise/`
  - The Information, Axios Pro Rata (if accessible)
- **How:** Find companies that raised in last 30 days → check their careers page → filter for matching roles
- **Frequency:** Weekly

### 6. Twitter/X Signals
- **How:** Search X for "we're hiring" + "AI" / "founding" / "product" from accounts with <50K followers (startup signal)
- **Frequency:** When X research cron runs

### 7. Hacker News "Who wants to be hired" Adjacent
- **URL:** Companies that post on HN Show/Launch often have open roles
- **How:** Check `https://news.ycombinator.com/show` for AI/dev companies, then check their careers

## Filtering Algorithm

### Pass 1: Keyword Match (fast, rules-based)
Score each role 0-100 based on:

```
+20  title contains: product manager, PM, strategic projects, deployment, 
     FDE, forward deployed, business ops, AI strategist, GTM
+15  company description mentions: AI, LLM, agents, infrastructure, fintech, devtools
+10  stage: seed, series A, series B, <100 employees
+10  location: NYC, SF, remote
+10  comp: $120K+ mentioned or likely based on stage
-30  title contains: senior engineer, staff engineer, SRE, BDR, SDR
-20  requires: 5+ years, PhD required, specific language fluency
-10  company: >500 employees, government contractor, non-tech
```

Threshold: score >= 40 passes to output.

### Pass 2: LLM Judgment (slower, for borderline cases)
For roles scoring 30-50, ask the LLM:
"Given this role description and this candidate profile, is this a realistic fit? Reply YES/NO with one reason."

### Self-Improvement Loop
Track in `job-search-state.json`:
```json
{
  "lastRun": "2026-03-11T00:00:00Z",
  "sources": {
    "hn": { "lastThreadId": 47219668, "lastChecked": "..." },
    "wellfound": { "lastPage": 3, "lastChecked": "..." },
    "yc": { "lastChecked": "..." },
    "funding": { "lastChecked": "..." }
  },
  "stats": {
    "totalFound": 0,
    "totalPushed": 0,
    "clickedBack": [],
    "ignoredCompanies": [],
    "preferredCompanies": []
  },
  "learned": {
    "preferredKeywords": [],
    "avoidKeywords": [],
    "preferredInvestors": ["sequoia", "a16z", "founders fund", "greylock", "kleiner perkins"],
    "notes": ""
  }
}
```

Over time:
- If you consistently ignore roles from certain company types → add to avoid list
- If you click on roles with certain keywords → boost those keywords
- If you message companies with certain investors → boost those investors
- Weekly: review what was pushed vs what you acted on, update scoring weights

## Notion Output

### Database: `31f7cca3-92fe-8015-988c-000b8326f168`

Required: Notion API token (set as `NOTION_API_KEY` in env)

Each row:
| Property | Type | Value |
|---|---|---|
| Company | Title | Company name |
| Role | Rich Text | Role title |
| Link | URL | Job posting URL |
| Source | Select | hn / wellfound / yc / funding / ashby / twitter |
| Score | Number | 0-100 filter score |
| Location | Rich Text | NYC / SF / Remote / etc |
| Stage | Select | Seed / Series A / Series B / Growth |
| Date Found | Date | When discovered |
| Status | Select | New / Reviewed / Applied / Skipped |

### Notion API Push
```bash
curl -X POST "https://api.notion.com/v1/pages" \
  -H "Authorization: Bearer $NOTION_API_KEY" \
  -H "Notion-Version: 2022-06-28" \
  -H "Content-Type: application/json" \
  -d '{
    "parent": {"database_id": "31f7cca392fe8015988c000b8326f168"},
    "properties": {
      "Company": {"title": [{"text": {"content": "AfterQuery"}}]},
      "Role": {"rich_text": [{"text": {"content": "Strategic Projects Lead"}}]},
      "Link": {"url": "https://jobs.ashbyhq.com/..."},
      "Source": {"select": {"name": "hn"}},
      "Score": {"number": 85},
      "Location": {"rich_text": [{"text": {"content": "SF"}}]},
      "Date Found": {"date": {"start": "2026-03-11"}}
    }
  }'
```

## Execution

### Manual Run
```
"Run job-finder: scan HN March 2026 thread and push matches to Notion"
```

### Cron (recommended)
- **Weekly (Monday 8 AM ET):** Scan all sources, push new matches
- **Monthly (1st, after HN thread posts):** Full HN thread scan

### First Run Setup
1. Get Notion API token → set `NOTION_API_KEY`
2. Share the database with the integration
3. Create the database properties (Company, Role, Link, Source, Score, Location, Stage, Date Found, Status)
4. Run initial scan of current HN thread
5. Set up weekly cron
