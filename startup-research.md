---
name: startup-research
description: Deep-dive research on target startups + direct outreach execution. Produces a brief dense enough that the user can walk into a room with the CEO and hold a real conversation, plus a tailored one-pager and DM script for reaching the founding team directly.
---

# Startup Research + Direct Outreach

## Purpose

Two-phase skill:
1. **Research** — know the company deeply enough to talk to the CEO without asking "so what do you guys do?"
2. **Outreach** — one-pager + DM to founding team, not a resume into an ATS

The goal is a 15-minute call booked by a founding team member. Not an application confirmation email.

---

## Phase 1 — Research (7 Layers)

Go deeper than the homepage. The homepage is marketing. The blog, the papers, the JDs, and the investor signals are truth.

### Layer 1 — Homepage + Product Pages

Fetch:
- Homepage
- /about, /team, /careers, /pricing, /customers, /security
- Any product-specific pages (/platform, /solutions, etc.)

Extract:
- What the product does in one sentence (no marketing fluff)
- Who buys it (ICP — job titles, company size, industry)
- Core differentiator claim — what do THEY think makes them special?
- Live metrics on the site (revenue numbers, customer counts, usage stats, booking rates)
- Named customers with quotes — real names + titles + specific outcomes = real traction. Logo walls mean nothing.
- Pricing model if visible (self-serve tiers, enterprise only, usage-based)
- Security/compliance badges (SOC2, HIPAA, ISO 27001 — tells you who they're selling to)

### Layer 2 — Funding and Investor Signal Decoding

Try in order:
1. Company blog for funding announcements (most reliable — they write their own narrative)
2. Ashby API: `https://api.ashbyhq.com/posting-api/job-board/[slug]` — JDs often name investors
3. Crunchbase: `https://www.crunchbase.com/organization/[name]`
4. TechCrunch search
5. Investor portfolio pages (e.g., sequoia.com/companies, greylock.com/portfolio)

What to extract AND what it means:
- **Total raised + round history** — tells you burn rate and runway
- **Investor names** — tier matters. Sequoia/a16z/Founders Fund = gold standard signal
- **Strategic investors** — e.g., J.P. Morgan investing in a fintech = almost certainly a customer too. This is the strongest traction signal in enterprise.
- **Angel investors** — notable angels (Chris Manning, Guillermo Rauch, etc.) signal what kind of company it is
- **Funding velocity** — seed to Series B in 14 months = exceptional. Normal is 18-24 months per round.
- **Cash-flow positive claims** — rare and important. Means no fundraising pressure.
- **"Zero salespeople" claims** — founder-led sales to meaningful ARR = genuine product-market fit

### Layer 3 — Research, Papers, and Benchmarks

**This is the layer most people skip. It's where you find the actual intellectual substance.**

Check:
- Company blog (every post, not just the first page)
- arXiv papers authored by the team: `arxiv.org/search/?query=[company name]`
- Named benchmarks or leaderboards they host
- Conference talks, podcast appearances
- GitHub repos (open-source projects, benchmark code)
- HuggingFace datasets they've released
- Manifesto or thesis posts (often the most revealing content on the site)

What to look for:
- **Published research** — if a startup publishes arXiv papers, they're serious about the technical moat. Read the abstracts and key findings.
- **Benchmarks they've built** — companies that build evaluation benchmarks are positioning themselves as the standard-setter. This is a category-creation move.
- **Data they've released** — open-source datasets on HuggingFace = credibility signal
- **The thesis** — what is this company actually betting on? Not the product — the worldview. (e.g., "expert tacit knowledge is the moat, not compute"). Find their manifesto, their founding blog post, their first arXiv paper. That's the real company.

### Layer 4 — Team and Founders

Sources (in priority order):
1. Company website /team or /about page
2. JD text (founders often name themselves in "notes from the founder" sections)
3. LinkedIn company page → People tab
4. arXiv paper author lists (first/last author = usually founders)
5. YC directory if YC-backed: `https://www.ycombinator.com/companies?query=[name]`
6. Crunchbase, Tracxn, PitchBook
7. Press releases from Business Wire, PR Newswire
8. Portfolio pages of known investors (e.g., greylock.com/portfolio/[name])

What to capture:
- **Founder names + backgrounds** — where they worked before matters enormously. Ex-Jane Street = quant rigor. Ex-Palantir = FDE model. Ex-McKinsey = process-heavy.
- **Team pedigree mentions in JDs** — "Waterloo, MIT, Berkeley, IMO Gold Medalist" = talent density signal
- **Specific backgrounds that surprise** — e.g., an HRT (quant trading) person at a home services company means they're thinking about signal extraction, not standard ML
- **Advisory function** — if they've built a team of domain experts (ex-bankers, ex-lawyers) as a first-class function, the trust gap is the main sales blocker
- **Headcount estimate** — count open roles + team page + LinkedIn employee count. <20 = very early. 30-80 = scaling. 100+ = growth stage.

### Layer 5 — Competitive Landscape

Don't just list competitors. Understand the positioning.

For each competitor:
- What do they do differently?
- Are they broader or narrower?
- Are they the incumbent or the insurgent?
- What's their funding/stage relative to the target company?

Key questions:
- Who's the 800-lb gorilla? (e.g., ServiceTitan in home services, Semrush in SEO)
- Is the target company replacing the incumbent, sitting alongside it, or targeting a gap the incumbent ignores?
- What's the defensible moat? (data, network effects, category creation, expert network, regulatory capture)
- Could the incumbent just copy the feature? What makes that hard?

### Layer 6 — Job Listings (Deep Read)

Ashby API: `https://api.ashbyhq.com/posting-api/job-board/[slug]?includeCompensation=true`
Also try Greenhouse: `https://job-boards.greenhouse.io/[company]/jobs`

**Read EVERY open JD, not just the target role.** Why:
- JDs reveal internal state: "we've never had a [role] before" = building from zero
- Comp ranges reveal stage and funding health
- Investor names are often in JDs but not on the website
- Culture language in JDs is often more honest than the careers page
- Open roles tell you where the company is investing (lots of eng = product phase, lots of sales = GTM phase)
- Travel requirements, hours expectations, onsite policy = real culture signals
- The AE JD tells you about deal sizes. The eng JD tells you about tech stack. The CoS JD tells you about internal chaos.

Look specifically for:
- Explicit hour expectations (6 days/week, 9-9-5, weekend sprints)
- Values language (is it founder-written or HR-template?)
- What "fast track" looks like (equity, title, responsibility)
- Remote/hybrid/onsite policy

### Layer 7 — CEO Talk Track (Synthesis)

Only do this AFTER layers 1-6 are complete. The talk track is the synthesis, not the starting point.

**What to lead with** — the one observation that signals you've done real research. Not "I love AI." Something like:
- "The fact that J.P. Morgan invested in your Series B is almost certainly a customer signal, not just a financial one."
- "The FinanceQA paper showing models fail 60% of realistic finance tasks — that's the gap your training data is designed to close."

**2-3 questions to ask** — questions that can't be answered by reading the website:
- "How does [specific feature] adoption look across your customer base — 10% or 80% using it?"
- "Who do you lose deals to most often, and why?"
- "What does [specific metric on their site] actually measure — your ARR or customer revenue?"

**What NOT to say:**
- Don't parrot their marketing copy back to them
- Don't say "I'm excited about AI"
- Don't ask questions answered on the first page of their website

---

## Key Research Principles

1. **Follow the research trail.** If they published a paper, read the abstract. If they built a benchmark, check the leaderboard. If they host a conference, look at who attended.

2. **Decode investor signals.** A strategic investor (J.P. Morgan in fintech, Dylan Field in product) usually means they're also a customer or design partner.

3. **Read every JD.** Not just the target role. Every JD is a window into the company's real state.

4. **Understand the thesis, not just the product.** Products change. The thesis is what the founders believe about the world.

5. **Named customers with outcomes > logo walls.** "Chris Hoffmann, CEO: 'After a $12,337 close, the skeptical technician loved the AI'" = real traction. "Trusted by 1000+ companies" = nothing.

6. **Shipping velocity = culture signal.** Weekly features + tracks GPT-5 on day 0 = fundamentally different culture than quarterly releases.

7. **Build the talk track last.** Only after all 7 layers can you write questions that impress a founder.

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

### Required Sections:

```markdown
# [Company Name] — Research Brief

**Date:** [YYYY-MM-DD]
**URL:** [url]
**Role targeting:** [role + comp if known]

## TL;DR
[2-3 sentences. What they do, why it matters, key traction signal. No marketing speak.]

## Product
- What it does (plain English)
- Who it's for (ICP)
- Core differentiator claim
- Pricing model
- Stage of product

## The Thesis
[What is this company actually betting on? Not the product — the worldview.]

## Research & Benchmarks
- Published papers (arXiv links + key findings)
- Benchmarks built + leaderboard results
- Open-source data/code released
- Conference/events hosted

## Funding
| Field | Detail |
|---|---|
| Stage | [stage] |
| Total | [$XM] |
| Last round | [date, amount, lead] |
| Investors | [list + what each signals] |

## Team
- Founders: [names, backgrounds, where to find them]
- Key leadership
- Team pedigree signals from JDs
- Headcount estimate
- Hiring velocity (what roles are open = where they're investing)

## Traction
- Named customers + specific outcomes
- Live metrics on site
- Product shipping velocity (blog post cadence)
- Sales motion signals (founder-led? first AE? enterprise?)

## Competitive Landscape
- Direct competitors + positioning
- The 800-lb gorilla (incumbent)
- Defensible moat
- Can the incumbent copy this? Why/why not?

## Culture and Vibe
- Work model (onsite/hybrid/remote)
- Intensity signals from JDs (hours, travel, weekend expectations)
- Founder visibility (writing their own blog posts? booking their own demos?)
- Values language (founder-written or HR-template?)

## The Roles
- What each role actually is (decoded from JD language)
- Who they're imagining (background, trajectory)
- Red flags or strong fits

## CEO Talk Track
- What to lead with (the one observation that signals deep research)
- 2-3 questions to ask (can't be answered by reading the website)
- What NOT to say

## 1hr Project Ideas
- Two concrete mini-projects to demonstrate fit
- Each should be completable in 1 hour
- Each should touch a real problem the company faces

## Who to Message
- Name, title, platform preference
- Active on X: [yes/no + handle]
- LinkedIn: [profile URL if found]
- Email pattern: [if discoverable]

## One-Pager Angles
- Why this company (specific insight to lead with)
- Why this role (3 proof point hooks)
- One thing I noticed

## Red Flags
[Anything concerning — hours, stage risk, competitive threat, role ambiguity]

## Sources
[Every URL fetched during research]
```
