# Target Company Briefs & 1hr Project Ideas

**Updated:** 2026-03-03

---

## 1. AfterQuery — Strategic Projects Lead

### What They Do
Applied research lab building high-quality training data to accelerate foundation model development. Their thesis: model performance is bounded by data quality, and the winning data is **expert tacit knowledge** — the stuff that lives in practitioners' heads, not on the internet. They curate datasets by partnering with domain experts (finance, law, medicine) to capture professional reasoning that can't be scraped or synthetically generated.

### Why It Matters
Foundation models are commoditizing (GPT, Claude, Gemini converging). The moat shifts to data. AfterQuery is building the data supply chain for the next generation of domain-specific AI. Think of them as the "expert knowledge refinery" — they turn the unwritten intuition of top professionals into structured training data.

### Key Details
- **Customers:** "Every frontier AI research lab" (homepage claim). Selling to OpenAI, Anthropic, Google DeepMind, Meta AI, etc.
- **Founding team:** Citadel Securities, Jane Street, Meta, Google, Goldman Sachs, Morgan Stanley (quant finance + big tech). Research side: Berkeley AI Research, Allen Institute for AI, Stanford AI Lab.
- **Funding:** Not publicly disclosed. The team pedigree suggests strong backing.
- **Location:** Not stated on site. Likely NYC or SF given team backgrounds.
- **Stage:** Early — "founding" roles, manifesto framing, small team energy.

### Their Core Thesis (from manifesto)
- AI can pass the bar exam but can't practice law. The gap = tacit expert knowledge never captured in training data.
- Reinforcement learning worked for code because code is verifiable (compiles or not). Professional work exists in "gradients of correctness" only experts can perceive.
- The breakthrough: **granular evaluation rubrics** that capture expert reasoning processes, not just outcomes. Train models on *how* experts think, not just *what* they conclude.
- "The companies that win the next decade will be the companies that help models extract, structure, and encode professional expertise."

### Role: Strategic Projects Lead
Likely an ops/strategy role owning cross-functional initiatives — data pipeline scaling, expert partnerships, research-to-product translation. "Strategic Projects" at a data company this early = you're the person making sure the expert knowledge capture process actually works at scale.

### CEO Talk Track
- Their manifesto is intellectually ambitious — the "intelligence paradox" framing (AI solves hard problems but fails at easy professional tasks) is sharp. Reference it.
- The quant finance backgrounds (Citadel, Jane Street) suggest they think about data quality the way quant firms think about alpha — it's a measurable edge, not vibes.
- Ask: "How do you source and retain domain experts? That's the supply constraint — finding a partner-level lawyer willing to spend hours annotating reasoning for a training dataset."
- Ask: "Which professional domains are you deepest in right now, and which are next? The manifesto mentions finance, law, and medicine — are you vertical or horizontal?"

### 1hr Project Ideas

**A: Expert Knowledge Capture Workflow Audit.** Pick one domain (e.g., financial analysis). Map the current state of how an expert's reasoning could be captured: what tools they use, where tacit decisions happen, what a "grading rubric" for a DCF model would look like across 5 quality dimensions. Deliver a 1-page process doc showing you understand the capture bottleneck. This is the core operational challenge of their business.

**B: Data Moat Competitive Analysis.** Map 5 companies selling training data to AI labs (Scale AI, Appen, Surge AI, Labelbox, Snorkel). For each, identify what kind of data they sell, pricing model, and quality methodology. Then show where AfterQuery's "expert tacit knowledge" thesis creates a gap none of them fill. Deliver as a 1-page positioning memo their sales team could use.

---

## 2. Probook — Founding FDE + Deployment Strategist

### What They Do
AI dispatching software for the $700B home services market (plumbers, HVAC techs, electricians). The core insight: which technician you send to a job determines whether the customer gets a $300 band-aid fix or a $20,000 system replacement. Currently dispatchers make this decision manually based on gut feel. Probook automates it with AI — matching technician skills, close rates, and job history to maximize both customer outcome and revenue per call.

### Key Details
- **CEO:** George Eliadis (books demos personally via Calendly)
- **Investors:** Sequoia + a16z — gold standard combination
- **ARR:** "$XXM" in 18 months with zero salespeople (all founder-led). Cash-flow positive.
- **Team:** 30+ people. Manhattan, NYC. All onsite.
- **Backgrounds:** Waterloo, MIT, Berkeley, ICPC World Finalist, IMO Gold Medalist, ex-Meta/Palantir/McKinsey
- **Culture:** Intense. 6 days/week (CoS), "9-9-5" (recruiter JD), weekend sprints (eng). Honest about it.
- **First AE hired:** December 2025. Previously 100% inbound/founder-led.
- **Key competitor:** ServiceTitan ($9B, went public). Probook is the AI-native wedge into dispatch.

### The $300 vs $20,000 Problem
This is Probook's entire pitch. In home services, a senior tech with consultative selling skills turns a "my AC isn't working" call into a full system assessment and potential replacement sale. A junior tech patches it for $300. The revenue difference per call is 10-60x depending on the job. Multiply by hundreds of daily calls across a service business, and the dispatch decision is worth millions annually. Currently made by a dispatcher staring at a whiteboard.

### CEO Talk Track
- George is direct and unfiltered. The JDs read like personal memos, not HR copy. Match that energy — no corporate speak.
- Lead with: "The fact that you hit significant ARR with zero salespeople is the most important signal. Home services operators are coming to you. What does that inbound motion actually look like?"
- Ask: "ServiceTitan owns the CRM layer. Are you replacing them, sitting alongside them, or targeting shops that haven't bought in?"
- Ask: "Cash-flow positive this early is unusual. Is that deliberate — controlling your own destiny — or is there a larger round coming?"
- Know: The home services market is relationship-driven and referral-heavy. If Probook works, owners tell other owners. The sales motion is network effects within trade associations and vendor groups.

### Roles

**Founding FDE (Forward Deployed Engineer):** Sits between engineering and customers. Deploys the product into customer environments, debugs integration issues with FSM tools (ServiceTitan, Housecall Pro), translates customer workflows into product requirements. Technical + customer-facing.

**Deployment Strategist ($120K-$150K):** Customer success meets consulting. Go on-site with home services businesses (2-4 days/week travel), deploy the product, own onboarding through expansion, track ROI, lead QBRs. Needs to understand home services P&L.

### 1hr Project Ideas

**A: Onboarding Diagnostic Checklist.** Create a structured deployment readiness assessment: what data a new customer needs to provide (tech profiles with close rates, job history, service area maps), common integration blockers with ServiceTitan/Housecall Pro, and a 30/60/90 day deployment timeline. Shows you can systematize their FDE motion at the point where it matters most — first impressions with a new customer.

**B: Dispatch ROI Calculator.** Build a spreadsheet model: input average ticket size, number of daily jobs, current random-assignment close rate → output revenue lift from optimized dispatch. Use real benchmarks (HVAC avg ticket ~$350, system replacement ~$8K-20K, avg close rate ~30%). This is a sales tool they can use in demos. Shows you think about their go-to-market, not just operations.

---

## 3. Profound — AI Strategist

### What They Do
AEO (Answer Engine Optimization) platform. As AI search (ChatGPT, Perplexity, Claude, Gemini) replaces Google, Profound helps brands understand and control how AI systems mention and recommend them. If ChatGPT doesn't mention your brand when someone asks "best running shoes," you're invisible to 700M weekly users.

### Key Details
- **Founders:** James Cadwallader (CEO) + Dylan Babbs (CTO). Met at South Park Commons NYC.
- **Funding:** $58.5M in <14 months. Seed $3.5M (Khosla/Keith Rabois, Aug 2024) → Series A $20M (Kleiner Perkins, Jun 2025) → Series B $35M (Aug 2025). Series A to B in 8 weeks.
- **Investors:** Khosla Ventures, Kleiner Perkins, Max Altman (Sam's brother), South Park Commons
- **Offices:** NYC Union Square (HQ), SF, London, Buenos Aires
- **Data:** 400M+ real AI conversations. 27M citations analyzed. This is their moat.
- **Customers:** Fortune 500 brands. G2 "Definitive Leader" in AEO (Winter 2026) — they created and won the category.
- **Conference:** Zero Click NYC — 300+ attendees from Walmart, Amazon, Google. Category-defining event.
- **Competitors:** Semrush, BrightEdge, Conductor, Ahrefs — all adding AEO features from an SEO base. Profound is AEO-native.

### Role: AI Strategist ($110K-$150K, NYC Union Square)
Hands-on, analytical. Work directly with large-scale AI prompt data. Analyze brand visibility across ChatGPT, Perplexity, Claude. Write SQL. Build dashboards (Retool/Tableau/Looker). Produce data-backed recommendations for Fortune 500 clients. 1-3 years experience as biz ops analyst, data analyst, or technical consultant.

### CEO Talk Track
- James writes publicly and confidently. "Goodbye blue links." "The front door of the internet is changing for the first time in 25 years." He's a category evangelist.
- Lead with the data moat: "400M real conversations is fundamentally different from running simulated prompts. The Black Friday Index is research only Profound can do. That's a durable edge."
- The G2 category creation is a Hubspot-style move — defining the vocabulary is a moat. Reference it.
- Ask: "Seed to Series B in 14 months is exceptional. What specifically triggered the B so quickly — was it planned or did inbound investor interest force the timeline?"
- Ask: "How many active enterprise accounts today, and what does a successful 90-day engagement look like for an AI Strategist?"

### 1hr Project Ideas

**A: Brand Visibility Audit.** Pick a real mid-size DTC brand. Run 20 purchase-intent prompts across ChatGPT, Perplexity, and Claude in that brand's category. Score each: mentioned? ranked? cited? positive/negative sentiment? Deliver a 1-page audit with specific recommendations (content gaps, citation opportunities). This is literally what the job is — doing it unprompted proves you can.

**B: Prompt Taxonomy for a Vertical.** Choose one vertical (e.g., travel, fintech, fitness). Classify 30 real prompts by intent type (comparison, recommendation, troubleshooting, purchase). Map which prompt types surface which brands and why. Deliver as a framework their strategists could reuse across clients. Shows analytical thinking at the level they sell to Fortune 500s.

---

## 4. Rogo — Product Manager, AI & Financial Intelligence

### What They Do
"Wall Street's first true AI analyst." Purpose-built AI agents for investment bankers, PE investors, and hedge fund analysts. Custom financial reasoning model trained by actual practitioners. Outputs work products in PowerPoint, Excel, and Word — the formats bankers actually use. Not a copilot or search tool; a full workflow agent that produces the deliverable.

### Key Details
- **Funding:** Series B, $50M (April 2025). Thrive Capital, J.P. Morgan, Tiger Global.
- **J.P. Morgan as investor** = almost certainly a customer. Strongest possible credibility signal in finance.
- **Product:** Custom financial reasoning model (not a GPT wrapper). Integrates internal firm data + external sources. Single-tenant deployments. SOC2, ISO 27001, GDPR.
- **Advisory function:** Built a whole team of ex-bankers/investors as a first-class function alongside sales and engineering. You only do this if you have enterprise customers complex enough to need domain consulting.
- **Contracts:** "Multi-year enterprise license agreements," "$1M+ quotas" per AE. Large ACV.
- **Location:** NYC onsite.
- **Competitors:** AlphaSense (research/search, more passive), Kensho (S&P Global, analytics), Harvey AI (legal, adjacent model). Generic enterprise AI (Copilot, ChatGPT Enterprise) doesn't understand banking workflows.

### Role: Product Manager, AI & Financial Intelligence
Likely owns the product roadmap for specific financial workflows — defining what the AI agent should do for IB analysts vs PE deal teams, prioritizing features based on customer feedback from the advisory team, and working with ML engineers on model capabilities.

### CEO Talk Track
- The J.P. Morgan investment is the elephant in the room. It signals institutional buy-in at the highest level. Ask directly: "Are they a production customer, and what are they running?"
- The advisory function (ex-bankers on staff) is a strategic choice. It says: "The trust gap in finance is so high that software alone doesn't close deals — you need a former banker in the room." Reference this.
- Ask: "What does the feedback loop look like between the advisory team and product? Are they pre-sale only, or do they stay with accounts post-deployment?"
- Ask: "The financial reasoning model claim is the core differentiator. What does 'trained by sophisticated bankers' mean in practice — RLHF, fine-tuning, RAG, or a combination?"
- Know: IB analysts spend 80+ hours/week on repetitive tasks (comps tables, CIM creation, market sizing). The value prop is giving those hours back. The adoption blocker is trust — bankers won't use output they can't verify.

### 1hr Project Ideas

**A: IB Analyst Workflow Gap Analysis.** Map a typical IB analyst's deal workflow step by step: CIM creation, comps table, market sizing memo, management presentation. For each step, assess: what Rogo likely automates well today, where analysts still fall back to manual work, and why (data access? formatting? trust?). Propose 2-3 product features to close the gaps, with prioritization rationale. Shows PM thinking in their domain.

**B: Financial Accuracy Eval Framework.** Design a lightweight test suite: 10 finance questions with known correct answers across difficulty levels (public company metrics, deal terms, market stats). Define scoring criteria: accuracy, source citation quality, recency, reasoning transparency. This is what Rogo needs to prove to every new bank — that the AI is trustworthy. Shows you understand the core adoption barrier.

---

## 5. Judgment Labs — Forward Deployed AI Engineer

### What They Do
Agent Behavior Monitoring (ABM) infrastructure. "Sentry-style monitoring for reliable agents." While traditional observability logs exceptions and latency, Judgment surfaces **behavioral anomalies** — instruction drift, context retrieval loss, hallucination patterns — in production AI agents at scale.

### Key Details
- **Funding:** $30M+ across two rounds in 5 months. Lightspeed, SV Angel, Valor Equity Partners, Nova Global. Angels: Chris Manning (Stanford NLP legend), Michael Ovitz, Michael Abbott, Kevin Hartz.
- **Team:** <20 people. "Olympiad medalists, debate champions, competitive athletes." SF onsite.
- **Customers:** "Hundreds of teams building autonomous agents." Named case study: legal AI immigration platform (saved 100+ hrs lawyer time/month, 3x faster agent updates).
- **Product:** Three capabilities:
  1. **Agent Behavior Monitoring** — trace and monitor agents in production, capturing behavioral signals
  2. **Custom Scoring** — curate golden datasets from production data, define scorers based on real outcomes (not brittle LLM judges)
  3. **Optimization** — use scores and failure patterns to update prompts, context rules, agent configs
- **Approach:** Post-train custom LLM judges on a customer's own data (e.g., pairs of AI drafts vs lawyer-edited drafts). The judge learns what "good" looks like for that specific customer.
- **Research:** Published "Climbing the Hills That Matter" — about evaluation methods grounded in production data.
- **Competitors:** Langsmith/LangChain (logging, lighter), Arize AI (ML observability), Braintrust (evals), Datadog (general observability adding AI). Judgment differentiates on behavioral anomaly detection and custom-trained judges.
- **Culture:** "Ship like 50+ on the daily." Everyone is "an ex-founder or a founder-to-be." Equinox, private chef, Smash/Mario Kart tournaments. In-person SF.

### Role: Forward Deployed AI Engineer
Embed directly into customer codebases. Integrate Judgment's monitoring into real agent workflows. Diagnose failures in live environments. Own customer engagements end-to-end. This is the most technical role on this list — they want someone who can read customer code, understand agent architecture, and deploy monitoring that catches behavioral drift.

### CEO Talk Track
- The Sentry analogy is sharp — every developer knows Sentry. "But for AI agents, the failure mode isn't a stack trace. It's the agent gradually drifting off-instruction over thousands of conversations. How do you define 'anomaly' when the agent's behavior is probabilistic by nature?"
- The case study is gold. A legal AI platform: immigration workflows, AI drafts → lawyer review. Judgment trained a custom judge on pairs of AI drafts vs lawyer-edited drafts. The judge learned what "good" looks like. Ask: "How generalizable is that approach across domains? Does each customer need their own judge model?"
- The team is tiny (<20) shipping for "hundreds of teams." Ask: "How much of the product is self-serve vs. how much requires your FDE team to deploy? What's the ratio?"
- Chris Manning as an angel investor is a legitimacy signal in NLP/AI research circles.

### 1hr Project Ideas

**A: Agent Failure Taxonomy.** Document a classification system for production agent failures: instruction drift, hallucination, context window loss, tool misuse, loop behavior, refusal creep, tone drift, escalation failure. For each, describe: what the monitoring signal looks like in logs, how you'd detect it programmatically, and severity level. Deliver as a 1-page reference card. Shows deep understanding of their core problem space.

**B: Customer Integration Playbook — First 48 Hours.** Write a deployment guide: what hooks/instrumentation a customer needs to add to their agent codebase, what data Judgment needs to start clustering behavioral patterns, what the first diagnostic report should look like, and when to schedule the first review. Shows FDE thinking — you're not just technical, you can own the customer relationship from integration to insight.

---

## 6. Context — Deployment Strategist

### What They Do
Enterprise AI workspace — AI agents that complete real tasks (create presentations, documents, spreadsheets, websites) powered by AI that understands organizational context. 50+ integrations (Slack, Google Drive, Notion, etc.). Deploy on customer terms: managed cloud, private instance, VPC, or fully on-premises.

### Key Details
- **Founded:** 2024, San Francisco
- **Product:** AI workspace where teams create real work artifacts (not just chat). Combines frontier AI models with deep organizational knowledge.
- **Deployment flexibility:** SaaS, dedicated private instance, VPC, fully on-prem. This is enterprise-ready.
- **Go-to-market:** "From discovery to deployment in under one month." Direct enterprise sales + consulting firm channel.
- **Hiring:** Engineering, design, go-to-market.
- **Stage:** Early. Website is clean but light on specifics. "Getting things ready" on getcontext.ai suggests recent rebrand or new domain.

### Your Note: Selling to End Customers vs. Consulting Firms
This is the core strategic question for Context. Two channels, two different pain points:
- **Direct enterprise:** Care about ROI, security, integration with their specific tools, and speed to value. Decision-maker is a VP of Operations or CTO.
- **Consulting firms:** Care about scalability across their client base, margin preservation, and differentiation vs other firms. Decision-maker is a practice lead or partner. They want to white-label or embed Context into their own offerings.
- **The tension:** Consulting firms are a multiplier (one deal = many deployments) but add a layer between you and the end user. Feedback loops slow down. Product roadmap gets pulled by the consulting firm's priorities, not the end user's pain.

### Role: Deployment Strategist
Customer-facing role. Own the deployment lifecycle: assess fit, design deployment architecture, scale across the organization. Technical enough to understand infrastructure requirements, strategic enough to navigate enterprise stakeholders.

### CEO Talk Track
- Context is early and positioning broadly ("AI workspace for every team"). Push on specificity: "Which use case are you seeing the fastest adoption for — presentations, documents, spreadsheets? Where does the AI actually outperform a human doing it manually?"
- The deployment flexibility (SaaS → on-prem) is a selling point for regulated industries. Ask: "What percentage of your customers are on-prem vs cloud? That tells you a lot about who's buying."
- The consulting firm channel: "How are you structuring partnerships with consulting firms? Is it a reseller model, a white-label, or do they bring you in as a subcontractor on engagements?"
- Ask: "What's the biggest reason a deployment stalls or fails after the first month?"

### 1hr Project Ideas

**A: Channel Strategy Memo — Direct vs. Consulting Firms.** Map the buyer journey for each channel: who's the champion, who's the economic buyer, what objections they raise, what the deployment timeline looks like. Propose differentiated packaging for each (direct = outcome-based pricing, consulting = per-seat with volume tiers). Address the feedback loop tension. Deliver as a 1-page strategy doc.

**B: Enterprise AI Deployment Friction Map.** List the top 10 reasons enterprise AI deployments stall (IT security review, data access permissions, champion leaves, unclear success metrics, integration complexity, change management, legal review, etc.). For each, propose a specific mitigation Context could build into their deployment process. Shows you understand that the product isn't the hard part — the last mile is.

---

## 7. Hightouch — AI Strategy Consultant

### What They Do
Customer Data Platform (CDP) + AI marketing platform. Started as "Reverse ETL" (syncing data from warehouses like Snowflake/Databricks to marketing tools). Evolved into a full AI marketing platform with agentic capabilities. AI agents that help marketers create content, plan campaigns, and execute strategies.

### Key Details
- **Customers:** Domino's, Chime, Spotify, Ramp, Whoop, Grammarly, and 1000+ others. These are real logos.
- **Gartner Magic Quadrant:** Named in Gartner's CDP Magic Quadrant (Jan 2026). This is enterprise validation.
- **Product suite (massive):**
  - **Composable CDP** — build your CDP on your existing data warehouse
  - **Customer Studio** — audience segmentation + journey orchestration
  - **Reverse ETL** — sync data from warehouse to 250+ destinations
  - **Identity Resolution** — stitch user profiles
  - **AI Decisioning** — reinforcement learning for 1:1 marketing experiences
  - **Content Assembly** (new) — remix existing creative into new on-brand content
  - **Agentic Marketing Platform** — AI agents that execute marketing workflows
  - **Real-time Personalization** — dynamic digital experiences
  - **Match Booster** — increase ad match rates
- **Integrations:** 250+ (Salesforce, HubSpot, Google Ads, Facebook, Snowflake, Databricks, etc.)
- **Stage:** Growth stage. Likely Series C+. Gartner recognition + 1000+ customers = established.
- **Location:** SF-based. The role may be flexible — JD says "ability to travel 10-25%."

### Role: AI Strategy Consultant ($170K-$200K, 80/20 variable split)
Drive marketing strategy and transformation in enterprise organizations. Help customers move from "planned weeks in advance, 3-5 people per email" to "AI agents delivering 1:1 experiences." Run design sessions, own use case delivery, project management, build relationships with customer executives. Martech experience important.

### CEO Talk Track
- Hightouch has a legitimacy advantage none of the other companies on this list have: Gartner Magic Quadrant + 1000+ customers + household-name logos. The question isn't "is this real" — it's "where's the growth edge?"
- The AI Decisioning product (reinforcement learning for 1:1 marketing) is the frontier bet. Ask: "How many customers are live on AI Decisioning vs. the core CDP product? What does adoption look like — are enterprise marketers ready for RL-driven campaigns, or is there an education gap?"
- Content Assembly is brand new. Ask: "How does Content Assembly interact with AI Decisioning — is the vision that the AI creates the content AND decides who sees it AND when?"
- The comp structure (80/20 variable) suggests this is partially a revenue role. Ask: "What does the variable component tie to — customer health, expansion revenue, use case delivery milestones?"

### 1hr Project Ideas

**A: Use Case Prioritization Matrix.** For a hypothetical retail brand: list 10 AI marketing use cases (abandoned cart recovery, churn prediction, dynamic pricing, personalized email cadence, browse abandonment, loyalty tier optimization, win-back campaigns, cross-sell recommendations, seasonal promotion timing, ad audience suppression). Score each on implementation complexity vs. revenue impact. Recommend the "first 3 deployments" with sequencing rationale. This mirrors the actual job.

**B: Campaign Migration Playbook.** Take a typical enterprise marketing calendar (plan-weeks-ahead, committee-approved). Pick one campaign type (e.g., weekly promotional email). Show how to migrate it to AI-driven 1:1 personalization using Hightouch's stack: data requirements (what needs to be in the warehouse), AI Decisioning setup, success metrics, and what "week 1 vs week 4" looks like. Shows you can translate the Hightouch vision into a concrete customer deliverable.

---

## 8. Netic — Agent Product Manager

### What They Do
AI revenue engine for home services and essential service enterprises. Three engines: (1) AI booking agents handling inbound across all channels (91% booking rate), (2) Cultivate engine for autonomous outbound (weather-triggered campaigns, maintenance reminders, upsells), (3) analytics dashboards. The full customer lifecycle — from generating demand to booking the job.

### Key Details
- **Funding:** $43M Series B. Dylan Field (Figma CEO, led personally), Founders Fund, Greylock.
- **Live metrics on homepage:** $36.31M revenue generated YTD, 11,214 jobs booked autonomously, 91% booking rate, $720K from after-hours jobs.
- **Named customers:** 14+ named testimonials with job titles and specific outcomes. Hoffmann Brothers has a full case study.
- **Team backgrounds:** Scale AI, Databricks, HRT (Hudson River Trading — quant trading firm), Meta, MIT, Stanford, Harvard.
- **Location:** SF onsite, Jackson Square.
- **Competitors:** Probook (dispatch only, narrower), ServiceTitan (incumbent CRM), Hatch (AI outbound, narrower), Podium (messaging, broader but not AI-native).
- **Culture:** "Live to build. Run through walls and win. Lose sleep over the almost perfect." Craft-focused intensity. More polished than Probook.
- **Key differentiator:** Weather-triggered outbound campaigns. Heatwave → AC maintenance outreach to customers with >12-month service gaps. No generic AI platform does this.

### Role: Agent Product Manager
Own the product roadmap for Netic's AI agents. Define what the booking agent should handle, how the Cultivate engine targets opportunities, and how the analytics surface insights. Likely working closely with ML engineers on agent capabilities and with the deployment team on what customers need.

### CEO Talk Track
- Dylan Field personally leading the Series B is the signal. Ask: "What specifically drew Dylan to Netic — the AI product quality, the market size, or something about the team?"
- The $36M YTD revenue figure on the homepage needs clarification: "Is that total customer revenue generated through Netic-booked jobs, or Netic's own ARR? Big difference."
- The Cultivate engine with weather signals is the most differentiated feature. Ask: "How many customers are actively using signal-triggered campaigns vs. basic outbound? What's the adoption curve?"
- The HRT background on the team suggests quantitative rigor in their AI. Ask: "The HRT background is unusual for a home services company. How does that influence how you think about signal extraction and optimization?"
- Julian Scadden's quote mentions "members" — likely a franchise association. Ask: "How are you thinking about scaling through channel partners like trade associations vs. direct enterprise sales?"

### 1hr Project Ideas

**A: Weather-Triggered Campaign Spec.** Design the full product spec: data sources (NWS API, Weather.gov), trigger rules (3-day forecast >90°F → AC maintenance campaign to customers with >12-month service gap + equipment age >8 years), message templates by channel (SMS, email, call), A/B test structure, and success metrics (booking rate, revenue per campaign, false positive rate). This is one of their key differentiators — speccing it shows you think like their PM.

**B: Booking Agent Failure Analysis Framework.** The AI books 91% of jobs. Design how to measure and improve the other 9%. Categorize failure modes: complex multi-service requests, scheduling conflicts, angry/emotional callers, language barriers, out-of-service-area, pricing objections, competitors mentioned. For the top 3 failure modes, propose product improvements. Shows PM thinking that directly impacts their headline metric.

---

## 9. Applied Labs — AI Agent Product Manager

### What They Do
On-brand AI agents for customer experience (CX) — handling complex customer conversations across chat, email, and voice. Go live in 30 days. Enterprise-grade security (SOC 2 Type II, HIPAA, GDPR).

### Key Details
- **CEO:** Michael Woo (co-founder)
- **Investors:** Abstract Ventures, Point72 Ventures, Outlander Ventures. Angels: Guillermo Rauch (CEO/Founder Vercel), Akshat Bubna (CTO Modal), Ali Rowghani (MD at Y Combinator).
- **Location:** NYC ("Heart of NYC")
- **Values:** Extreme Ownership, Customer Obsession, Craftsmanship. "From words to systems, we sweat the details. Quality is never optional — it is the product."
- **Stage:** Early to growth. Small team energy + YC/Vercel angel network.
- **Differentiator:** "On-brand" — the AI matches the company's voice, tone, and guidelines. Not generic chatbot responses. Strict guardrails enforced in every interaction.
- **Competitors:** Intercom (adding AI), Zendesk (adding AI), Ada, Forethought, Sierra AI (Bret Taylor's company), Decagon. Crowded space — differentiation is on brand quality and speed to deploy.
- **Key claim:** Go live in 30 days. This is aggressive and a strong GTM differentiator if true.

### Role: AI Agent Product Manager
Own the product roadmap for their AI agents. Define capabilities across chat, email, and voice. Work on agent quality (brand adherence, resolution accuracy), deployment speed (the 30-day promise), and integration depth.

### CEO Talk Track
- The "on-brand" positioning is the strategic choice. In a crowded CX AI market, everyone claims accuracy. Applied Labs claims taste. Ask: "How do you measure 'on-brand'? Is it a rubric, customer feedback, or automated scoring?"
- Guillermo Rauch (Vercel founder) as an angel is interesting — he cares about developer experience and design quality. His bet says Applied Labs builds well.
- Point72 Ventures (Steve Cohen's firm) investing in a CX AI company is notable — suggests they see the market as large enough for venture returns.
- Ask: "The 30-day go-live claim is bold. What's the longest a deployment has actually taken, and why?"
- Ask: "Voice is the hardest channel for AI. Where are you in voice maturity vs. chat and email?"
- The CX AI space is crowded (Sierra, Ada, Intercom, Zendesk). Ask: "Who do you lose deals to most often, and why?"

### 1hr Project Ideas

**A: Voice Agent Quality Scorecard.** Design an eval framework for voice AI agents: brand tone adherence (formal/casual/empathetic), resolution accuracy (did the customer's issue get solved?), escalation appropriateness (did the AI know when to hand off?), handle time, and post-call sentiment. Include how you'd score calls (sample size, human review cadence, automated metrics). Voice is their newest and hardest channel — showing you've thought about it deeply signals product instinct.

**B: 30-Day Deployment Timeline Teardown.** Reverse-engineer the "go live in 30 days" promise: Week 1 (data ingestion, brand guidelines, knowledge base import), Week 2 (agent training, integration with CRM/helpdesk), Week 3 (testing, edge case identification, guardrail tuning), Week 4 (soft launch on one channel, monitoring, customer review). Identify the riskiest week and propose a de-risk measure. Shows you can think about their core delivery promise as a product.

---

*Each brief is designed so you can walk into a room with the CEO and hold a real conversation — not "tell me about your company" but "here's what I already know, here's what I think matters, here are the questions I'd ask."*
