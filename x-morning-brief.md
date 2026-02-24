---
name: x-morning-brief
description: Twice-weekly X research brief for cyy. Finds 5 noteworthy posts from AI/LLMs, PM, deep tech, VC/startup, and devtools using anchor account searches + topic filters. Runs Mon + Wed at 8 AM. Pure reading, no engagement. Send via Telegram.
---

# X Morning Brief

## Purpose

Find 5 X posts worth reading from the past few days. Actual links, no summaries. Covers what's stirring in cyy's niche circles whether or not they follow the account.

Runs Monday and Wednesday at 8 AM. Covers posts from the past 2-4 days.

---

## Credentials

Bearer Token: stored in TOOLS.md under "X (Twitter) API"

---

## How to Run

### Step 1 — Search each topic using anchor accounts + topic filter

Use the X API recent search endpoint:

```
GET https://api.twitter.com/2/tweets/search/recent
  ?query=QUERY
  &max_results=5
  &tweet.fields=public_metrics,created_at
  &expansions=author_id
  &user.fields=name,username
  &sort_order=relevancy
Authorization: Bearer TOKEN
```

**Queries (account-anchored + topic-filtered):**

```
AI/LLMs:
(from:sama OR from:karpathy OR from:ylecun OR from:AnthropicAI OR from:OpenAI OR from:emollick OR from:fchollet) (AI OR model OR LLM OR agent OR reasoning OR benchmark) -is:retweet lang:en

PM/Product:
(from:shreyas OR from:lennyrachitsky OR from:joulee OR from:sriramk OR from:joshelman OR from:cagan OR from:johncutlefish OR from:benedictevans) (product OR PM OR shipped OR strategy OR growth OR decision OR launch) -is:retweet lang:en

Deep tech:
(from:SpaceX OR from:EricTopol OR from:NvidiaAI OR from:darioamodei OR from:waitbutwhy OR from:elonmusk) (launch OR biotech OR chip OR robot OR space OR breakthrough OR hardware) -is:retweet lang:en

VC/Startup:
(from:paulg OR from:garrytan OR from:pmarca OR from:benedictevans OR from:naval OR from:hunterwalk OR from:semil) (startup OR funding OR founder OR market OR build OR company OR raise) -is:retweet lang:en

Devtools:
(from:dhh OR from:swyx OR from:rauchg OR from:kelseyhightower OR from:t3dotgg OR from:addyosmani OR from:simonw) (code OR developer OR tool OR framework OR open source OR shipped OR engineering OR CLI) -is:retweet lang:en
```

### Step 2 — Pick best post per topic

From each topic's results, pick the post with highest combined score:

```
score = like_count + (reply_count * 3)
```

Reply count is weighted higher because replies = debate = people actually engaging with the idea.

### Step 3 — If a topic returns no results

Skip it. Do not fire a fallback query. Include only the topics that returned results. A 4-post brief is fine.

### Step 4 — Build the post list

Construct link: `https://x.com/[username]/status/[tweet_id]`

### Step 5 — Send to cyy via Telegram

Format:
```
Morning brief — [Mon/Wed], [Date]

1. [Why it's worth 2 min — not what it is, why it matters now]
   https://x.com/username/status/id

2. ...
3. ...
4. ...
5. ...

6. [Viral/Moment — why everyone in tech is talking about this today]
   https://x.com/username/status/id
```

One line per post. Say why it's worth reading today, not just what it's about.

Bad: "OpenAI released a new benchmark"
Good: "OpenAI's EVMbench: AI agents now autonomously detecting + patching smart contract vulnerabilities — first serious AI security eval"

---

## What "worth noting" means

- Changes how people think, not just confirms what they believe
- Announces something that will matter in 6 months
- A contrarian take generating real debate (high reply/like ratio)
- Firsthand observation from someone who built or shipped something
- Signals a shift in the field

Skip: engagement bait, hustle content, generic ChatGPT amazement, pure fundraising PR with no substance

---


## Viral / Funny Tech Moment

Every brief includes one slot for something going viral in the tech/AI/builder circles — not because it's deep, but because everyone is talking about it and you should know the reference.

This can be:
- Something ironic or funny (e.g. a VP of Security at Meta having an AI agent delete her inbox)
- A hot debate blowing up in builder circles
- A meme, screenshot, or moment that's circulating widely
- Anything that would come up if you were at a tech dinner that evening

**How to find it:**
Search anchor accounts for high reply-to-like ratio (replies > 10% of likes = debate/reaction). Also search broader viral tech queries:



Pick the post with the highest reply_count / like_count ratio from any tech account — that signals a reaction moment, not passive consumption.

Include as post 6 in the brief, labeled [Viral/Moment].

---
## Anchor Accounts Reference

These are updated over time. Add accounts that consistently post signal.

| Topic | Key accounts |
|---|---|
| AI/LLMs | @sama @karpathy @ylecun @AnthropicAI @OpenAI @emollick @fchollet |
| PM/Product | @shreyas @lennyrachitsky @joulee @sriramk @johncutlefish @cagan |
| Deep tech | @SpaceX @EricTopol @NvidiaAI @darioamodei @waitbutwhy |
| VC/Startup | @paulg @garrytan @pmarca @naval @benedictevans @hunterwalk |
| Devtools | @dhh @swyx @rauchg @kelseyhightower @t3dotgg @addyosmani @simonw |

---

## Schedule

Monday and Wednesday at 8 AM cyy's timezone (see MEMORY.md once timezone confirmed).

