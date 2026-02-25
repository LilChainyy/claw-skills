---
name: startup-research
description: Research a target startup company in depth for job applications and interviews. Given a company URL, produces a structured brief covering product, funding, team, traction, culture, competitive landscape, and interview prep angles.
---

# Startup Research

## Purpose

Produce a research brief on a target company before applying or interviewing. The goal is to know the company well enough to:
- Answer "why this company" credibly
- Demonstrate product understanding in a screening call
- Ask smart questions that signal strategic thinking
- Spot red flags before wasting time in a long process

---

## Input

- Company URL (required)
- Role(s) targeting (optional — helps focus the brief)

---

## Research Process

### Step 1 — Homepage and About/Team pages

Fetch the company's homepage, /about, and /team pages.

Extract:
- What the product actually does in plain English (strip marketing copy)
- Who it's for (ICP)
- What the core differentiator claim is
- Founder names and any bios visible on site

### Step 2 — Funding and stage

Fetch Crunchbase:
`https://www.crunchbase.com/organization/[company-slug]`

If Crunchbase is blocked, try:
- `https://techcrunch.com/search/?q=[company+name]`
- `https://www.linkedin.com/company/[company-slug]/about/`

Extract:
- Funding stage (Seed / Series A / B / C / etc.)
- Total raised
- Last round: date, amount, lead investor
- All investor names (signals prestige and network)
- Founded year

### Step 3 — Team and headcount

Fetch LinkedIn company page if possible:
`https://www.linkedin.com/company/[company-slug]/`

Extract:
- Current headcount
- Headcount 6 months ago if shown (growth rate signal)
- Any notable recent hires (VP/Director level = growth signal)

Also check the founders on LinkedIn individually:
- Prior companies, prior roles (relevant domain expertise?)
- Any prior exits?

### Step 4 — Recent news and announcements

Search:
`https://news.google.com/search?q=[company+name]`
or fetch the company blog at `/blog` or `/news`.

Extract:
- Any press coverage in the last 3 months
- Product launches, new features, partnerships
- Any layoffs, pivots, leadership departures (red flags)

### Step 5 — Traction signals

Check the company website for:
- Named customers or logos on site
- Case studies (B2B) or testimonials
- "Trusted by X companies" counts

Check job postings (company careers page or LinkedIn jobs):
- How many open roles?
- What functions are they hiring? (Engineering = building; Sales = GTM push; Finance = pre-exit prep)
- Are JDs well-written? (Signal of organizational maturity)

### Step 6 — Competitive landscape

Search: `[company name] vs [competitor]` or `[company name] alternatives`

Identify:
- 2-3 direct competitors
- How the company differentiates (their claim vs. what you can verify)
- Where the market is heading (is this company ahead, behind, or carving a niche?)

### Step 7 — Culture and vibe

Check:
- Glassdoor: `https://www.glassdoor.com/Search/results.htm?keyword=[company+name]`
- LinkedIn posts by founders (how do they talk publicly?)
- Tone and language in job postings (startup grindy vs. process-heavy)
- Remote/hybrid/in-office policy (check careers page)

Red flags on Glassdoor: management changes, comp complaints, "fast-paced" used as warning not selling point.

---

## Output Format

Save the brief to: `research/[company-slug].md` in the workspace.

---

# [Company Name] — Research Brief

**Date:** [YYYY-MM-DD]
**URL:** [url]
**Role(s) targeting:** [role or TBD]

---

## TL;DR

[2 sentences. What they do and why it's interesting. No marketing speak.]

---

## Product

- **What it does:** [plain English]
- **Who it's for:** [ICP — company size, role, industry]
- **Core claim:** [their differentiator in one line]
- **Pricing model:** [usage / seat / enterprise contract / unknown]
- **Stage of product:** [early beta / growth / scaling / mature]

---

## Funding

| Field | Detail |
|---|---|
| Stage | [Seed / Series A / B / C] |
| Total raised | [$X] |
| Last round | [Date — $X — Lead investor] |
| Investors | [list] |
| Founded | [year] |

**Runway read:** [e.g. "Series B in 2024, likely 18-24 months runway, currently hiring aggressively"]

---

## Team

- **Founders:** [names, backgrounds, prior exits if any]
- **Key leadership:** [CEO, CPO, VP Eng, etc. — relevant context]
- **Headcount:** [~X on LinkedIn as of date]
- **Hiring velocity:** [growing fast / stable / slowing / unclear]

---

## Traction Signals

- Named customers: [list or "none visible"]
- Press mentions (last 3 months): [list or "none found"]
- Recent launches: [product updates, partnerships, etc.]
- Job posting volume: [X open roles — signal of growth]

---

## Competitive Landscape

- **Direct competitors:** [list]
- **Differentiation:** [how they claim to be different]
- **Market read:** [is the space crowded? is this company differentiated or a me-too?]

---

## Culture and Vibe

- **Work model:** [remote / hybrid / in-office / unknown]
- **Glassdoor:** [rating if available, key themes from reviews]
- **Founder public presence:** [active on LinkedIn/X? What's their tone?]
- **Job posting tone:** [signal of culture — scrappy, process-heavy, values-forward, etc.]

---

## Red Flags

[Anything concerning: long funding gap, layoffs, pivot history, founder departures, negative press]

If nothing found: "None identified. Continue monitoring."

---

## Role Fit

- **Open roles relevant to me:** [list]
- **What the JDs imply:** [what function the company is investing in; who you'd work with]
- **Likely interview process:** [based on company stage and any Glassdoor data]

---

## Interview Prep

### Talking points (show homework)

1. [Specific recent development — e.g. "I saw you just launched X last month — how is early adoption looking?"]
2. [Product angle that shows you understand the space — e.g. "The per-account agent model is interesting vs. the batch-scoring approach most tools use"]
3. [Market/competitor angle — optional]

### Questions to ask

1. [Strategic question about product direction]
2. [Question about team/role scope that signals you think in terms of impact]
3. [Honest question about stage/growth that shows you've thought about risk]

**Example questions (adapt to company):**
- "What's the biggest thing that needs to be true for this company to work at the next stage of scale?"
- "How does the team measure whether [core product function] is actually working?"
- "What does the first 90 days look like for this role — what would a strong start look like vs. a slow one?"

---

## Open Questions

[Things you couldn't find or verify — worth asking in interview or researching further]

---

## Sources

[List of URLs fetched during research]

---

## Worked Example — actively.ai

**TL;DR:** Actively AI deploys per-account AI agents for enterprise GTM teams — each agent retains context, learns from outcomes, and drives next-best-action for SDRs, AEs, and AMs. Targets large enterprise sales orgs that want AI to work continuously across their full TAM, not just assist reps ad hoc.

**Product:** Custom model trained on a company's specific GTM data + per-account agents that research, understand, reason, and improve over time. Competes with generic AI sales tools (Clay, Outreach AI, Salesforce Einstein) by claiming custom model training as the differentiator.

**What to look up:**
- Crunchbase: funding stage, investors (likely Series A/B given "enterprise" positioning + SOC2)
- LinkedIn: headcount growth (AI GTM is hot in 2025-2026)
- Recent blog: "Building Context Graphs for GTM" — read it before any interview, it's their technical differentiation argument

**Smart question for this company:** "The custom model angle is the core differentiator claim — how long does model training take for a new enterprise customer, and what does the onboarding funnel look like today?"
