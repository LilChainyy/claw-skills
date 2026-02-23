---
name: x-morning-brief
description: Twice-weekly morning research brief. Uses X API to find 5 noteworthy posts from cyy's niche areas — AI/LLMs, PM, deep tech, VC/startup, devtools. Delivered Monday and Wednesday at 8 AM. Pure research, no engagement required.
---

# X Morning Brief

## Purpose

Find 5 X posts worth reading from the past few days. Not a summary — actual links. Covers what's stirring in cyy's niche circles whether or not they follow the person.

Runs Monday and Wednesday at 8 AM. Covers posts from the past 2-3 days.

---

## Credentials

Bearer Token is stored in TOOLS.md. Load it from there before making any API calls.

---

## Topic Areas

1. **AI/LLMs** — model releases, research getting traction, infra shifts, agent/eval/reasoning debates
2. **Product management** — frameworks, career takes, big product decisions, PM hot takes
3. **Deep tech** — biotech, space, chips (TSMC/Nvidia/AMD), robotics
4. **VC/startup** — notable rounds, fund news, investor market takes
5. **Developer tools / devex** — new tool launches, paradigm shifts, workflow debates

---

## How to Run

### Step 1 — Search each topic area via X API

Use the recent search endpoint with engagement-based filtering:

```
GET https://api.twitter.com/2/tweets/search/recent
  ?query=QUERY
  &max_results=20
  &tweet.fields=public_metrics,author_id,created_at,entities
  &expansions=author_id
  &user.fields=name,username,public_metrics
  &sort_order=relevancy
Authorization: Bearer TOKEN
```

Run one query per topic area. Use these queries:

| Topic | Query |
|---|---|
| AI/LLMs | `(AI OR LLM OR "language model" OR "model release" OR "reasoning model") -is:retweet -is:reply lang:en min_faves:50` |
| PM | `("product management" OR "product manager" OR "product decision" OR "PM take") -is:retweet -is:reply lang:en min_faves:30` |
| Deep tech | `(biotech OR "space launch" OR semiconductor OR robotics OR "chip shortage" OR TSMC OR Nvidia) -is:retweet -is:reply lang:en min_faves:30` |
| VC/startup | `(funding OR "Series A" OR "Series B" OR "seed round" OR "venture capital" OR VC) -is:retweet -is:reply lang:en min_faves:30` |
| Devtools | `("developer tool" OR devex OR SDK OR "new framework" OR "dev workflow" OR "open source") -is:retweet -is:reply lang:en min_faves:30` |

### Step 2 — Score and filter results

From each topic's results, pick the single best post using this scoring:

**Must pass:**
- Posted in the last 3 days
- At least 30 likes (50+ for AI topic)
- Not a retweet, not a reply thread opener with no context

**Prefer:**
- High reply count relative to likes (signals debate, not just passive approval)
- From accounts with 1K+ followers (but don't exclude smaller accounts if the content is strong)
- Says something new, not just reacts to something older
- Short and sharp over long and thorough

**Skip:**
- Engagement bait ("change my mind", "hot take:", "thread:")
- Generic AI hype ("ChatGPT changed everything")
- Fundraising announcements with no substance or context
- Hustle/motivational content
- Anything that just describes a feature release without analysis

### Step 3 — Build the 5-post list

Pick the single best post from each topic area. If one area had nothing noteworthy, replace it with a second pick from the strongest area that week.

Construct a direct x.com link:
```
https://x.com/[username]/status/[tweet_id]
```

### Step 4 — Send to cyy via Telegram

Format:
```
Morning brief — [Mon/Wed], [Date]

1. [Why it's worth 2 min — not what it's about, why it matters now]
   https://x.com/username/status/id

2. ...

3. ...

4. ...

5. ...
```

The one-line description must say why it's worth reading today, not just describe the topic. Bad: "interesting AI post." Good: "Anthropic researcher on why reasoning models are hitting a wall on multi-step planning — specific and not the usual hype."

---

## What "worth noting" means

One of:
- Changes how people think about something, not just confirms what they already believe
- Announces something that will matter in 6 months
- A take so sharp or contrarian that it's generating real debate (check reply count)
- From someone who has built/shipped something sharing firsthand observations
- Signals a shift — something that would have been unsayable 6 months ago

---

## Schedule

Monday and Wednesday at 8 AM cyy's local time. Timezone in MEMORY.md once confirmed.
