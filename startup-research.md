---
name: startup-research
description: Research target startup companies and execute a direct outreach application strategy. Produces a research brief plus a tailored one-pager and DM script for reaching the founding team directly — no resume, no ATS black hole.
---

# Startup Research + Direct Outreach

## Purpose

Two-phase skill:
1. **Research** — know the company well enough to write something the founder actually reads
2. **Outreach** — one-pager + DM to founding team, not a resume into an ATS

The goal is a 15-minute call booked by a founding team member. Not an application confirmation email.

---

## Phase 1 — Research

### Step 1 — Homepage and About/Team pages

Fetch the company's homepage, /about, and /team pages.

Extract:
- What the product actually does in plain English (strip marketing copy)
- Who it's for (ICP)
- What the core differentiator claim is
- Founder names and any bios visible on site
- Any live metrics (ARR, customers, usage stats)

### Step 2 — Funding and stage

Fetch Crunchbase or try:
- `https://techcrunch.com/search/?q=[company+name]`
- `https://api.ashbyhq.com/posting-api/job-board/[company-slug]` (Ashby API — returns full JD text including investor mentions, team background, comp)

Extract:
- Funding stage and total raised
- Investors (tier-1 signals, strategic signals, angels)
- Founded year

### Step 3 — Job listings via Ashby API

Always try: `https://api.ashbyhq.com/posting-api/job-board/[company-slug]?includeCompensation=true`

This is often the richest source — JDs contain investor names, team backgrounds, culture framing, and comp ranges that aren't on the website.

### Step 4 — Team and founders

For direct outreach, finding named founders is mandatory. Try in order:
1. Company website /team or /about page
2. JD text (often mentions founders or CEO by name)
3. LinkedIn company page → People tab (requires login but headers are visible)
4. YC directory if YC-backed: `https://www.ycombinator.com/companies?query=[name]`
5. Tracxn, Crunchbase, PitchBook
6. Press releases from Business Wire, PR Newswire
7. Portfolio pages of known investors (e.g., greylock.com/portfolio/[name])

### Step 5 — Recent news and product velocity

Fetch the company blog. Check for:
- How fast are they shipping? (weekly = high velocity, monthly = moderate)
- What are they writing about? (signals priorities and thesis)
- Are founders writing posts themselves? (signals hands-on culture)
- Any recent funding announcements, case studies, product launches

### Step 6 — Competitive landscape

Search `[company name] vs [competitor]` or `[company name] alternatives`. Understand:
- 2-3 direct competitors
- How the company differentiates
- Whether the market is large and defensible

### Step 7 — Culture and intensity signals

Read every JD carefully for:
- Explicit hour expectations (6 days/week, 9-9-5, weekend sprints)
- Values language (is it founder-written or HR-template?)
- What "fast track" looks like (equity, title, responsibility)
- Remote/hybrid/onsite policy

---

## Phase 2 — Direct Outreach Application

### The Approach

Do not apply through the ATS form as your primary move. At companies with <100 people, the founding team reads their own DMs on LinkedIn and X/Twitter. A one-pager sent directly to a co-founder converts at a dramatically higher rate than a resume submitted through Ashby or Greenhouse.

Sequence:
1. Research (Phase 1)
2. Write the one-pager (company-specific, role-specific)
3. Find who to message (founder, CEO, or direct hiring manager)
4. Send the DM — ultra short, one-pager attached or linked
5. Follow up once after 3-4 days if no response
6. Submit the ATS form as a backup, not the primary move

### One-Pager Structure

One page. PDF or Notion link. Never a Word doc. Never a resume.

---

**[Company Name] × [Your Name]**
**[Role Title]**

**Why this company (2-3 sentences)**
Not "I'm excited about AI." Something specific that shows you read the product.
Example: "Your Cultivate engine using weather data to trigger outbound before a customer even calls is the most differentiated feature in home services AI. No generic AI platform does this — it requires domain knowledge Netic clearly has."

**Why this role (2-3 bullets)**
Mapped directly to what the JD actually says, not generic PM/ops talking points.
- [Specific responsibility from JD] → [Your specific proof point]
- [Specific responsibility from JD] → [Your specific proof point]
- [Specific responsibility from JD] → [Your specific proof point]

**What I bring (3-4 bullets)**
Concrete proof points only. No soft skills language.
- [Quantified outcome or named company/role]
- [Specific domain knowledge relevant to their ICP or product]
- [Specific tool/skill they'd care about]
- [Evidence of ownership/ambiguity tolerance if relevant]

**One thing I noticed**
1-2 sentences. An observation about their product, market, or customer problem that shows you're already thinking like someone on the team. This is the part most candidates skip. It's what separates a read from a pass.
Example: "The $12,337 single-close quote from the skeptical technician is the most interesting traction signal on your site — it means even resistant users convert once they see the outcome."

**What I'm asking for**
"15 minutes." Not "please review my application."

[LinkedIn URL] [Email or X handle if relevant]

---

### DM Script

**Version A (with attached one-pager):**
> Hey [Name] — I put together a one-pager on why I want the [Role] seat at [Company]. [One specific thing you noticed about the product or market]. Happy to send my background separately if you'd prefer that first — either way, love 15 minutes.

**Version B (opening hook, ask to send):**
> Hey [Name] — I've been following [specific thing] at [Company] closely. Put together a one-pager on why I want the [Role] seat. Can I send it over?

Keep it under 75 words. The DM is a door knock, not a pitch. The one-pager does the work.

### Where to Find Founders

**LinkedIn:**
- Search company name → People tab → filter by Co-Founder, CEO, CTO
- Also search "[Name] [Company] founder" directly

**X/Twitter:**
- Search "[Company] founder" or "[CEO name]"
- Check if founders are active (recent posts = they're reading DMs)
- Active founders on X respond to DMs faster than LinkedIn

**Priority for outreach:**
1. Co-founder/CEO (most direct, highest conversion at <50 person companies)
2. Hiring manager (VP Product, Head of Ops, etc. — if role is specialized)
3. CTO or Head of Engineering (good for FDE/deployment roles)
4. Skip: recruiters, HR, generic careers email

### Platform Choice

**Use X DM if:**
- Founder posts regularly (>1x per week) — they're checking DMs
- Founder has <50K followers — more accessible
- The company is tech-native (AI, devtools, infra)

**Use LinkedIn DM if:**
- Founder isn't active on X
- Company is more enterprise or ops-focused
- You have mutual connections (mention them)

**Email if:**
- You can find it (pattern: firstname@company.com, try Hunter.io)
- Founders aren't responsive on social
- Subject line: "[Company] × [Your Name] — [Role]"

### Follow-Up Rule

One follow-up after 3-4 business days. Keep it one sentence:
> "Following up on my note — happy to send anything else that'd be useful."

If no response after that: submit ATS application and move on. Don't triple-tap.

### Cadence

One company per day. No more. Each outreach takes real preparation time, and mass-applying one-pagers is worse than one great one.

Suggested workflow:
- Morning: research the company, read the JD, find the founder
- Afternoon: write the one-pager (45-60 min max — if it takes longer you're overthinking it)
- Evening: send the DM

---

## Research Brief Output Format

Save to: `research/[company-slug].md`

---

# [Company Name] — Research Brief

**Date:** [YYYY-MM-DD]
**URL:** [url]
**Role targeting:** [role + comp if known]

## TL;DR
[2 sentences. What they do and why it's interesting. No marketing speak.]

## Product
- What it does (plain English)
- Who it's for (ICP)
- Core differentiator claim
- Pricing model
- Stage of product

## Funding
| Stage | [stage] |
| Total | [$XM] |
| Last round | [date, amount, lead] |
| Investors | [list] |

## Team
- Founders: [names, backgrounds]
- Key leadership
- Headcount estimate
- Hiring velocity

## Traction
- Named customers + outcomes
- Metrics on site
- Product shipping velocity

## Competitive Landscape
- Direct competitors
- Their differentiation
- Market read

## Culture and Vibe
- Work model (onsite/hybrid/remote)
- Intensity signals from JDs
- Founder visibility

## The Role
- What it actually is (decoded from JD language)
- Who they're imagining (background, trajectory)
- Red flags or strong fits

## Who to Message
- Name, title, platform preference
- Active on X: [yes/no + handle]
- LinkedIn: [profile URL if found]

## One-Pager Angles
- Why this company (specific insight to lead with)
- Why this role (3 proof point hooks)
- One thing I noticed (the observation that shows you're already thinking like a team member)

## Red Flags
[Anything concerning]

## Sources
[URLs fetched]
