---
name: job-finder
description: Automated startup job discovery. Scans HN Who is Hiring + HN Algolia job posts, filters for PM/FDE/ops roles, pushes to Notion. Run monthly after new HN thread drops.
---

# Job Finder

## Notion Setup

- **Token:** `${NOTION_TOKEN}`
- **DB ID:** `3207cca3-92fe-80ae-be95-ec2120c9ef64`
- **Columns:** Company (title), Role (rich_text), Link (url), Source (select), Notes (rich_text), Date Found (date), Status (select)
- **No Score, Stage, or Location columns** — keep it clean

## Profile

- **Want:** Product Manager, Forward Deployed Engineer, FDE, Chief of Staff, Solutions Engineer, Solutions Architect, Technical Program Manager, Deployment Strategist, AI Strategist, Business Operations, Head of Product, Founding PM, Implementation Engineer, Customer Success Engineer, Product Operations, Strategy & Operations
- **Skip:** Any SWE, backend/frontend/fullstack/platform/systems engineer, ML engineer, data engineer, DevOps, SRE, designer, BDR/SDR, account exec, sales rep, copywriter, recruiter, engineering manager, staff engineer, principal engineer, research scientist, data scientist, iOS/Android engineer
- **No big corps:** Bloomberg, Microsoft, Google, Meta, Amazon, Apple, Netflix, Salesforce, Oracle, IBM, Cisco, Intel, Nvidia, Adobe, Twilio, Stripe, Shopify, Uber, Lyft, Airbnb, DoorDash, Coinbase, Robinhood, Plaid, Datadog, Snowflake, Databricks, Cloudflare, MongoDB, Elastic, GitLab, Atlassian, Figma, Canva, Discord, Zoom, HubSpot, Zendesk, Intercom, Postman, Samsung, Sony, Siemens, McKinsey, Bain, BCG, Deloitte, Accenture, JPMorgan, Goldman, Morgan Stanley, Reddit, Mozilla, PostHog, Zed, DeepL, SafetyWing, Ashby, Wave, Wikipedia, Palantir, Scale AI, Anduril, OpenAI, Anthropic, Mistral, Cohere, Perplexity
- **Location:** Remote = always OK. Onsite = only NYC or SF/Bay Area. No explicit location = include.

## Link + Notes Rules

- **Link column:** Only real URLs. Leave blank if none.
- **Notes column:** Catch-all. If no link → full job description. Always include location context (e.g., "NYC onsite", "Remote"). Put anything else relevant (stage, funding, team size) here too.

## Rate Limits

- Notion API: 0.35s between writes (3 req/s limit)
- HN Firebase API: 0.1s between comment fetches, batch with 10 concurrent threads max
- HN Algolia API: 0.4s between search queries
- If any 429 response: sleep 2s and retry once

---

## Source 1: HN "Who is Hiring?" Thread (Monthly)

Run once per month after the new thread is posted (first weekday of month).

### Find current thread ID

```python
import requests, time, datetime

cutoff = int((datetime.datetime.now() - datetime.timedelta(days=35)).timestamp())
r = requests.get(
    f'https://hn.algolia.com/api/v1/search?query="Ask HN: Who is hiring"&tags=ask_hn'
    f'&numericFilters=created_at_i>{cutoff}&hitsPerPage=5',
    timeout=10
)
hits = r.json().get('hits', [])
# Pick the most recent one titled "Ask HN: Who is hiring? (..."
thread = next((h for h in hits if 'who is hiring' in h['title'].lower()), None)
THREAD_ID = thread['objectID']  # e.g. "43324661"
```

### Fetch all comments

```python
import requests, json, time
from concurrent.futures import ThreadPoolExecutor

def fetch_item(item_id):
    r = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json', timeout=8)
    return r.json() if r.status_code == 200 else None

# Get thread
thread = fetch_item(THREAD_ID)
comment_ids = thread.get('kids', [])

# Fetch all top-level comments (these are the job postings)
comments = []
with ThreadPoolExecutor(max_workers=10) as ex:
    results = list(ex.map(fetch_item, comment_ids))
comments = [c for c in results if c and not c.get('deleted') and not c.get('dead')]
# Save locally: json.dump(comments, open('/tmp/hn_comments.json', 'w'))
```

### Filter and push

```python
import re, html, requests, json, time

NOTION_KEY = '${NOTION_TOKEN}'
DB_ID = '3207cca3-92fe-80ae-be95-ec2120c9ef64'
H = {"Authorization": f"Bearer {NOTION_KEY}", "Notion-Version": "2022-06-28", "Content-Type": "application/json"}

def cl(t):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html.unescape(t))).strip()

WANT = [
    'product manager', 'head of product', 'vp of product', 'director of product',
    'founding pm', 'founding product manager', 'product lead',
    'forward deployed', 'fde',
    'deployment strategist', 'ai strategist',
    'chief of staff', 'head of operations', 'biz ops', 'head of biz ops',
    'solutions engineer', 'solution engineer', 'solutions architect',
    'customer success engineer', 'implementation engineer',
    'technical program manager', 'tpm',
    'product operations', 'strategic operations', 'business operations',
    'strategy and operations', 'ai product',
]

KILL = [
    'software engineer', 'backend engineer', 'frontend engineer',
    'full stack engineer', 'fullstack engineer', 'platform engineer',
    'systems engineer', 'data engineer', 'ml engineer', 'devops', 'sre',
    'security engineer', 'qa engineer', 'embedded', 'compiler',
    'infrastructure engineer', 'founding engineer',
    'designer', 'ux designer', 'ui designer', 'product designer',
    'bdr', 'sdr', 'account executive', 'sales rep',
    'copywriter', 'content writer', 'recruiter',
    'engineering manager', 'staff engineer', 'principal engineer',
    'research scientist', 'data scientist', 'ml researcher', 'ml manager',
    'ios engineer', 'android engineer', 'mobile engineer',
    'java engineer', 'ruby engineer', 'go engineer', 'rust engineer',
]

BIG = [
    'bloomberg', 'microsoft', 'google', 'meta', 'amazon', 'apple', 'netflix',
    'salesforce', 'oracle', 'ibm', 'cisco', 'intel', 'nvidia', 'adobe', 'twilio',
    'stripe', 'shopify', 'uber', 'lyft', 'airbnb', 'doordash', 'coinbase',
    'robinhood', 'plaid', 'datadog', 'snowflake', 'databricks', 'cloudflare',
    'mongodb', 'elastic', 'gitlab', 'atlassian', 'figma', 'canva', 'discord',
    'zoom', 'hubspot', 'zendesk', 'intercom', 'postman', 'samsung', 'sony',
    'siemens', 'mckinsey', 'bain', 'bcg', 'deloitte', 'accenture', 'jpmorgan',
    'goldman', 'morgan stanley', 'reddit', 'mozilla', 'posthog', 'zed industries',
    'deepl', 'safetywing', 'ashby', 'wave', 'wikipedia', 'palantir', 'scale ai',
    'anduril', 'openai', 'anthropic', 'mistral', 'cohere', 'perplexity',
]

ONSITE = ['onsite', 'on-site', 'in-office', 'in office', 'hybrid']
NYC = ['nyc', 'new york']
SF = ['sf ', 'san francisco', 'bay area']
REMOTE = ['remote', 'worldwide', 'work from anywhere', 'distributed']

def location_ok(t):
    if any(r in t for r in REMOTE): return True
    if any(o in t for o in ONSITE):
        return any(n in t for n in NYC + SF)
    return True  # unspecified = include

def extract_link(raw):
    urls = re.findall(r'https?://[^\s<"\')\]]+', raw)
    for u in urls:
        ul = u.lower()
        if any(x in ul for x in ['jobs.ashbyhq', 'greenhouse.io', 'lever.co', '/jobs',
                                   '/careers', 'workable', 'boards.greenhouse', 'wellfound']):
            return u.rstrip('.,;)')
    for u in urls:
        ul = u.lower()
        if not any(x in ul for x in ['ycombinator', 'news.yc', 'twitter', 'linkedin', 'github', 't.co']):
            return u.rstrip('.,;)')
    return None

def push_row(company, role, link, notes, source='hn'):
    if not role or len(role) < 3: return False
    if re.match(r'^(remote|http|san francisco|new york|nyc|sf)', role.lower()): return False
    props = {
        'Company': {'title': [{'text': {'content': company[:100]}}]},
        'Role': {'rich_text': [{'text': {'content': role[:200]}}]},
        'Source': {'select': {'name': source}},
        'Date Found': {'date': {'start': datetime.date.today().isoformat()}},
        'Status': {'select': {'name': 'New'}},
    }
    if link and link.startswith('http'):
        props['Link'] = {'url': link}
    if notes:
        props['Notes'] = {'rich_text': [{'text': {'content': notes[:2000]}}]}
    r = requests.post("https://api.notion.com/v1/pages",
        json={"parent": {"database_id": DB_ID}, "properties": props}, headers=H)
    if r.status_code == 429:
        time.sleep(2)
        r = requests.post("https://api.notion.com/v1/pages",
            json={"parent": {"database_id": DB_ID}, "properties": props}, headers=H)
    time.sleep(0.35)
    return r.status_code == 200

# Load cached comments (if already fetched this session)
comments = json.load(open('/tmp/hn_comments.json'))

pushed = 0
for c in comments:
    raw = c.get('text', '')
    if not raw: continue
    t = cl(raw).lower()
    first = raw.split('<p>')[0]
    fc = cl(first)
    parts = re.split(r'\s*[\|]\s*', fc)
    company = parts[0].strip()

    if any(bc in company.lower() for bc in BIG): continue
    if not any(w in t for w in WANT): continue
    if any(k in t for k in KILL): continue
    if not location_ok(t): continue

    # Parse role — must be 2nd pipe segment and look like a title, not a location
    if len(parts) >= 2:
        candidate = parts[1].strip()
        if re.match(r'^(remote|http|san francisco|new york|nyc|sf |worldwide)', candidate.lower()):
            candidate = fc
    else:
        candidate = fc
    role = candidate[:200]
    if any(k in role.lower() for k in KILL): continue

    link = extract_link(raw)
    loc_raw = ' | '.join(p.strip() for p in parts[2:] if p.strip()) if len(parts) > 2 else ''
    desc = cl(raw)[:800]
    notes = (f"[{loc_raw}] " if loc_raw else "") + (desc if not link else "")

    ok = push_row(company, role, link, notes.strip(), 'hn')
    if ok:
        pushed += 1
        print(f"✅ [{'✓' if link else 'desc'}] {company[:35]:35s} | {role[:55]}")

print(f"HN: {pushed} pushed")
```

---

## Source 2: HN Algolia Job Posts (YC companies that post on HN)

Run alongside HN thread scan.

```python
import requests, re, datetime, time

NOTION_KEY = '${NOTION_TOKEN}'
DB_ID = '3207cca3-92fe-80ae-be95-ec2120c9ef64'
H = {"Authorization": f"Bearer {NOTION_KEY}", "Notion-Version": "2022-06-28", "Content-Type": "application/json"}

cutoff = int((datetime.datetime.now() - datetime.timedelta(days=60)).timestamp())

queries = [
    'forward deployed engineer',
    'deployment lead',
    'product manager hiring',
    'solutions engineer hiring',
    'chief of staff hiring',
    'technical program manager hiring',
    'head of product hiring',
    'biz ops hiring',
    'implementation engineer hiring',
    'ai product manager',
    'founding pm hiring',
    'product operations',
    'strategy operations startup',
    'customer engineer startup',
]

results = []
seen = set()
for q in queries:
    url = (f"https://hn.algolia.com/api/v1/search?query={requests.utils.quote(q)}"
           f"&tags=job&numericFilters=created_at_i>{cutoff}&hitsPerPage=20")
    r = requests.get(url, timeout=10)
    for h in r.json().get('hits', []):
        if h['objectID'] not in seen:
            seen.add(h['objectID'])
            results.append(h)
    time.sleep(0.4)

# Reuse KILL and BIG lists from above

pushed = 0
for h in results:
    title = h.get('title', '')
    url = h.get('url', '')
    t = title.lower()
    if any(k in t for k in KILL): continue
    if any(bc in t for bc in BIG): continue

    # Parse "Company (YC XX) Is Hiring [Role]" pattern
    m = re.match(r'^(.+?)\s+(?:\(YC [A-Z]\d+\)\s+)?[Ii]s [Hh]iring\s+(?:a\s+|an\s+)?(.+)$', title)
    if m:
        company = re.sub(r'\s*\(YC [A-Z]\d+\)', '', m.group(1)).strip()
        role = m.group(2).strip()
    else:
        parts = title.split(' Is Hiring ')
        company = re.sub(r'\s*\(YC [A-Z]\d+\)', '', parts[0]).strip() if len(parts) == 2 else title[:50]
        role = parts[1].strip() if len(parts) == 2 else title

    link = url if url and url.startswith('http') else ''
    notes = f"HN job post: {title}"

    ok = push_row(company, role, link, notes, source='yc')
    if ok:
        pushed += 1
        print(f"✅ [{'✓' if link else '✗'}] {company[:35]:35s} | {role[:55]}")

print(f"YC/HN Algolia: {pushed} pushed")
```

---

## Wipe DB Before a Fresh Run

```python
import requests, time

NOTION_KEY = '${NOTION_TOKEN}'
DB_ID = '3207cca3-92fe-80ae-be95-ec2120c9ef64'
H = {"Authorization": f"Bearer {NOTION_KEY}", "Notion-Version": "2022-06-28", "Content-Type": "application/json"}

cursor = None
wiped = 0
while True:
    body = {"page_size": 100}
    if cursor: body["start_cursor"] = cursor
    r = requests.post(f"https://api.notion.com/v1/databases/{DB_ID}/query", json=body, headers=H)
    data = r.json()
    rows = data.get("results", [])
    if not rows: break
    for row in rows:
        requests.patch(f"https://api.notion.com/v1/pages/{row['id']}",
            json={"archived": True}, headers=H)
        wiped += 1
        time.sleep(0.15)
    if not data.get("has_more"): break
    cursor = data.get("next_cursor")
    time.sleep(0.3)
print(f"Wiped {wiped} rows")
```

---

## Execution Instructions

**Full monthly run (run this when a new HN thread drops):**

1. Find current HN thread ID via Algolia
2. Fetch all thread comments (batch with 10 threads)
3. Save to `/tmp/hn_comments.json`
4. (Optional) Wipe DB if doing a fresh pass
5. Run HN filter + push
6. Run HN Algolia job posts search + push

**Invoke:** "Run job-finder" or "Scan HN jobs and push to Notion"

**Notes:**
- HN thread = ~300-500 comments, takes ~1-2 min to fetch at 10 concurrent
- Notion push at 0.35s/row = ~3.5s per 10 rows
- Algolia search = ~6s for 14 queries
- Total run time: ~3-5 minutes
- Do NOT re-fetch HN thread if `/tmp/hn_comments.json` already exists from same session

## Known Limitations

- HN "Who is Hiring" posts often have no job board link — only company site or none at all. Description goes in Notes.
- HN Algolia job tag is thin — only YC/startup companies that post HN job listings directly (not the monthly thread)
- No browser = can't reach Wellfound, ycombinator.com/jobs (JS-rendered). If browser is available, add Wellfound as Source 3.
- Notion API occasionally returns 400 on malformed URLs — strip trailing punctuation from links
