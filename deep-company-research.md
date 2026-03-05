---
name: deep-company-research
description: Deep-dive research on a target startup. Produces a brief dense enough that the user can walk into a room with the CEO and hold a real conversation — not "tell me about your company" but "I already know your thesis, your traction signals, your competitive moat, and where you're vulnerable."
---

# Deep Company Research

## Purpose

Research a company thoroughly enough that:
1. You understand the business better than 95% of applicants
2. You can reference specific products, benchmarks, papers, metrics, and people by name
3. You can ask questions that signal insider-level knowledge
4. You have a mental model of their thesis, not just their product

This is NOT a surface-level company overview. This is "I read your arXiv papers, I know your investor signals, I understand why your team composition matters, and I have opinions about your competitive position."

---

## Research Layers (in order)

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
- Named customers with quotes — these are gold. Real names + titles + specific outcomes = real traction.
- Pricing model if visible (self-serve tiers, enterprise only, usage-based)
- Security/compliance badges (SOC2, HIPAA, ISO 27001 — tells you who they're selling to)

### Layer 2 — Funding and Investors

Try in order:
1. Company blog for funding announcements (most reliable — they write their own narrative)
2. Ashby API: `https://api.ashbyhq.com/posting-api/job-board/[slug]` — JDs often name investors
3. Crunchbase: `https://www.crunchbase.com/organization/[name]`
4. TechCrunch search
5. Investor portfolio pages (e.g., sequoia.com/companies, greylock.com/portfolio)

What to extract AND what it means:
- **Total raised + round history** — tells you burn rate and runway
- **Investor names** — tier matters. Sequoia/a16z/Founders Fund = gold standard signal
- **Strategic investors** — e.g., J.P. Morgan investing in a fintech = almost certainly a customer. This is the strongest traction signal in enterprise.
- **Angel investors** — notable angels (Chris Manning, Guillermo Rauch, etc.) signal what kind of company it is
- **Funding velocity** — seed to Series B in 14 months = exceptional. Normal is 18-24 months per round.
- **Cash-flow positive claims** — rare and important. Means no fundraising pressure.
- **"Zero salespeople" claims** — founder-led sales to meaningful ARR = genuine product-market fit

### Layer 3 — Research and Publications

This is the layer most people skip. It's where you find the actual intellectual substance.

Check:
- Company blog (every post, not just the first page)
- arXiv papers authored by the team (`arxiv.org/search/?query=[company name]`)
- Named benchmarks or leaderboards (check if they host their own)
- Conference talks, podcast appearances
- GitHub repos (open-source projects, benchmark code)
- Manifesto or thesis posts (often the most revealing content on the site)

What to look for:
- **Published research** — if a startup publishes arXiv papers, they're serious about the technical moat. Read the abstracts and key findings.
- **Benchmarks they've built** — companies that build evaluation benchmarks are positioning themselves as the standard-setter in a space. This is a category-creation move.
- **Data they've released** — open-source datasets on HuggingFace or GitHub = credibility signal
- **Shipping velocity** — how often does the blog show new features? Weekly = intense. Monthly = normal. Quarterly = slow.
- **Who's writing** — founders writing posts themselves = hands-on culture. Marketing team only = different signal.

### Layer 4 — Team and Founders

Sources (in priority order):
1. Company website /team page
2. JD text (founders often name themselves, especially in "notes from the founder" sections)
3. LinkedIn company page → People tab
4. arXiv paper author lists (first/last author = usually founders)
5. Crunchbase people tab
6. YC directory
7. Press releases

What to capture:
- **Founder names + backgrounds** — where they worked before matters enormously. Ex-Jane Street means quant rigor. Ex-Palantir means FDE model. Ex-McKinsey means process-heavy.
- **Team pedigree mentions in JDs** — "Waterloo, MIT, Berkeley, IMO Gold Medalist" = talent density signal
- **Specific backgrounds that surprise** — e.g., an HRT (quant trading) person at a home services company means they're thinking about signal extraction, not just standard ML
- **Advisory function** — if they've built a team of domain experts (ex-bankers, ex-lawyers) as a first-class function, that tells you the trust gap is the main sales blocker
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

Read EVERY open JD, not just the target role. Why:
- JDs reveal internal state: "we've never had a [role] before" = building from zero
- Comp ranges reveal stage and funding health
- Investor names are often in JDs but not on the website
- Culture language in JDs is often more honest than the careers page
- Open roles tell you where the company is investing (lots of eng = product phase, lots of sales = GTM phase)
- Travel requirements, hours expectations, onsite policy = real culture signals

### Layer 7 — CEO/Founder Talk Track

After all research is done, synthesize into:

**What to lead with** — the one observation that signals you've done real research. Not "I love AI." Something like "The fact that J.P. Morgan invested in your Series B is almost certainly a customer signal, not just a financial one."

**2-3 questions to ask** — questions that can't be answered by reading the website. Questions that show you're thinking about their business:
- "How does [specific feature] adoption look across your customer base — is it 10% or 80% using it?"
- "Who do you lose deals to most often, and why?"
- "What does [specific metric on their site] actually measure — is it your ARR or customer revenue?"

**What NOT to say** — don't parrot their marketing copy back to them. Don't say "I'm excited about AI." Don't ask questions answered on the first page of their website.

---

## Output Format

Save to: `research/[company-slug].md`

The brief should be structured so you can skim it in 5 minutes before a call and sound like you've been following the company for months.

### Required Sections:
1. **TL;DR** — 2-3 sentences. What they do, why it matters, key traction signal.
2. **Product** — what it does, who it's for, core differentiator, pricing, stage
3. **The Thesis** — what is this company actually betting on? Not the product — the worldview. (e.g., "expert tacit knowledge is the moat, not compute")
4. **Research & Benchmarks** — any published papers, benchmarks, open-source work. Include key findings.
5. **Funding** — full round history, investor names + what they signal, funding velocity
6. **Team** — founders + backgrounds, team pedigree, headcount, notable hires
7. **Traction** — named customers, live metrics, product shipping velocity, sales motion signals
8. **Competitive Landscape** — direct competitors, incumbent threat, defensible moat
9. **Culture** — work model, intensity signals, founder visibility, values language
10. **The Roles** — decoded from JD language, who they're actually looking for
11. **CEO Talk Track** — what to lead with, questions to ask, things to know walking in
12. **Red Flags** — anything concerning
13. **1hr Project Ideas** — two concrete mini-projects you could build to demonstrate fit
14. **Sources** — every URL fetched

---

## Key Principles

1. **Go deeper than the homepage.** The homepage is marketing. The blog, the papers, the JDs, and the investor signals are truth.

2. **Follow the research trail.** If they published a paper, read the abstract. If they built a benchmark, check the leaderboard. If they host a conference, look at who attended. These are the things competitors and most applicants never look at.

3. **Decode investor signals.** A strategic investor (J.P. Morgan investing in a fintech, Dylan Field investing in a product company) is worth more than a financial investor. It usually means they're also a customer or design partner.

4. **Read every JD.** Not just the target role. The AE JD tells you about deal sizes. The eng JD tells you about tech stack. The CoS JD tells you about internal chaos. Every JD is a window into the company's real state.

5. **Understand the thesis, not just the product.** Products change. The thesis is what the founders actually believe about the world. Find their manifesto, their founding blog post, their first arXiv paper. That's the real company.

6. **Named customers with outcomes > logo walls.** "Trusted by 1000+ companies" means nothing. "Chris Hoffmann, CEO of Hoffmann Brothers: 'After a $12,337 close, the skeptical technician told us the customer loved the AI'" — that's real traction.

7. **Shipping velocity = culture signal.** A company that ships weekly features and tracks GPT-5 on day 0 has a fundamentally different culture than one that ships quarterly. Check the blog dates.

8. **Build the CEO talk track last.** Only after you've done all 7 layers can you write questions that actually impress a founder. The talk track is the synthesis, not the starting point.
