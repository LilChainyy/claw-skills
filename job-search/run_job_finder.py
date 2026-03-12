import os
#!/usr/bin/env python3
"""
Job Finder — run monthly after HN "Who is Hiring" thread drops.
Usage: python3 run_job_finder.py [--wipe] [--hn-only] [--yc-only]
"""
import re, html, json, time, datetime, sys
import requests
from concurrent.futures import ThreadPoolExecutor

NOTION_KEY = os.environ.get('NOTION_TOKEN', '')
DB_ID = '3207cca3-92fe-80ae-be95-ec2120c9ef64'
H = {"Authorization": f"Bearer {NOTION_KEY}", "Notion-Version": "2022-06-28", "Content-Type": "application/json"}
HN_CACHE = '/tmp/hn_comments.json'

# ── Filters ──────────────────────────────────────────────────────────────────

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

# ── Helpers ───────────────────────────────────────────────────────────────────

def cl(t):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html.unescape(t))).strip()

def location_ok(t):
    if any(r in t for r in REMOTE): return True
    if any(o in t for o in ONSITE):
        return any(n in t for n in NYC + SF)
    return True

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

# ── Wipe ──────────────────────────────────────────────────────────────────────

def wipe_db():
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
    print(f"Wiped {wiped} rows", flush=True)

# ── Source 1: HN "Who is Hiring" thread ──────────────────────────────────────

def find_hn_thread_id():
    cutoff = int((datetime.datetime.now() - datetime.timedelta(days=35)).timestamp())
    r = requests.get(
        f'https://hn.algolia.com/api/v1/search?query="Ask HN: Who is hiring"&tags=ask_hn'
        f'&numericFilters=created_at_i>{cutoff}&hitsPerPage=5', timeout=10)
    hits = r.json().get('hits', [])
    thread = next((h for h in hits if 'who is hiring' in h['title'].lower()), None)
    return thread['objectID'] if thread else None

def fetch_item(item_id):
    try:
        r = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json', timeout=8)
        return r.json() if r.status_code == 200 else None
    except: return None

def fetch_hn_comments(thread_id):
    print(f"Fetching HN thread {thread_id}...", flush=True)
    thread = fetch_item(thread_id)
    comment_ids = thread.get('kids', [])
    print(f"  {len(comment_ids)} top-level comments", flush=True)
    with ThreadPoolExecutor(max_workers=10) as ex:
        results = list(ex.map(fetch_item, comment_ids))
    comments = [c for c in results if c and not c.get('deleted') and not c.get('dead')]
    json.dump(comments, open(HN_CACHE, 'w'))
    print(f"  Fetched {len(comments)} comments → saved to {HN_CACHE}", flush=True)
    return comments

def run_hn():
    import os
    if os.path.exists(HN_CACHE):
        print(f"Loading cached HN comments from {HN_CACHE}", flush=True)
        comments = json.load(open(HN_CACHE))
    else:
        thread_id = find_hn_thread_id()
        if not thread_id:
            print("Could not find HN thread", flush=True)
            return
        comments = fetch_hn_comments(thread_id)

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
            print(f"  ✅ [{'✓' if link else 'desc'}] {company[:35]:35s} | {role[:55]}", flush=True)

    print(f"HN: {pushed} pushed", flush=True)

# ── Source 2: HN Algolia YC Job Posts ────────────────────────────────────────

def run_yc_algolia():
    cutoff = int((datetime.datetime.now() - datetime.timedelta(days=60)).timestamp())
    queries = [
        'forward deployed engineer', 'deployment lead', 'product manager hiring',
        'solutions engineer hiring', 'chief of staff hiring',
        'technical program manager hiring', 'head of product hiring',
        'biz ops hiring', 'implementation engineer hiring', 'ai product manager',
        'founding pm hiring', 'product operations', 'strategy operations startup',
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
    print(f"YC Algolia: {len(results)} unique posts found", flush=True)

    pushed = 0
    for h in results:
        title = h.get('title', '')
        url = h.get('url', '')
        t = title.lower()
        if any(k in t for k in KILL): continue
        if any(bc in t for bc in BIG): continue

        m = re.match(r'^(.+?)\s+(?:\(YC [A-Z]\d+\)\s+)?[Ii]s [Hh]iring\s+(?:a\s+|an\s+)?(.+)$', title)
        if m:
            company = re.sub(r'\s*\(YC [A-Z]\d+\)', '', m.group(1)).strip()
            role = m.group(2).strip()
        else:
            parts = title.split(' Is Hiring ')
            company = re.sub(r'\s*\(YC [A-Z]\d+\)', '', parts[0]).strip() if len(parts) == 2 else title[:50]
            role = parts[1].strip() if len(parts) == 2 else title

        if any(k in role.lower() for k in KILL): continue
        link = url if url and url.startswith('http') else ''
        notes = f"HN job post: {title}"

        ok = push_row(company, role, link, notes, source='yc')
        if ok:
            pushed += 1
            print(f"  ✅ [{'✓' if link else '✗'}] {company[:35]:35s} | {role[:55]}", flush=True)

    print(f"YC Algolia: {pushed} pushed", flush=True)

# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    args = sys.argv[1:]
    if '--wipe' in args:
        wipe_db()
    if '--yc-only' not in args:
        run_hn()
    if '--hn-only' not in args:
        run_yc_algolia()
    print("\nDone.", flush=True)
