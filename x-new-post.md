---
name: x-new-post
description: "Writes and optimizes X posts/threads for @YiyanChenX targeting 1k+ views and 100+ engagements. Finds 3 reference posts from relevant high-performing accounts, analyzes their structure, then rewrites the draft using proven patterns."
---

# X New Post

## Purpose

Take a draft post idea from cyy, find 3 high-performing reference posts on X in the same topic space, analyze what makes them work, and produce a final thread/post optimized for 1k+ views and 100+ combined engagements (likes + replies + retweets).

Persona: @YiyanChenX — aspiring PM / builder / technical, building in public, ships AI products.

---

## Step 1 — Find 3 reference posts

Use the X API to search for high-performing posts in the topic area.

**API endpoint:**
```
GET https://api.twitter.com/2/tweets/search/recent
  ?query=QUERY
  &max_results=10
  &tweet.fields=public_metrics,created_at
  &expansions=author_id
  &user.fields=name,username
Authorization: Bearer TOKEN (from TOOLS.md)
```

Note: `max_results` must be between 10 and 100.

**Scoring formula (post-fetch):**
`score = like_count + (reply_count * 3) + (retweet_count * 2)`

**Queries to run (pick based on post topic):**

For tech/building/indie posts:
- `"what i learned" (startup OR indie OR saas OR product) -is:retweet lang:en`
- `(reddit OR launch OR distribution) lessons building indie -is:retweet lang:en`
- `from:levelsio OR from:marc_louvion OR from:jdnoc OR from:swyx thread -is:retweet lang:en`

For PM/product posts:
- `"product manager" lessons learned (startup OR indie OR AI) -is:retweet lang:en`
- `product management tip (builders OR founders) -is:retweet lang:en`

For AI/devtools posts:
- `(AI OR LLM) shipped built learned -is:retweet lang:en`

Run 2-3 queries. Take top 3 by score across all results. Stop when you have 3.

**If API spend cap is hit (SpendCapReached error):**
Skip the live search. Use known patterns from the "Proven Thread Formats" section below instead. Note to cyy that the API cap is active and the live search will work when the cycle resets.

---

## Step 2 — Analyze the 3 reference posts

For each reference post, extract:
- **Hook structure**: how does the first tweet open? Question, statement, surprising fact, personal story?
- **Format**: single tweet, numbered thread, or free-flowing thread?
- **Specificity level**: does it use real numbers, tool names, timeframes?
- **Voice**: first person story, observation, hot take, advice?
- **CTA**: how does it end? Follow, reply, share?
- **What would make a lurker save it?**

---

## Step 3 — Rewrite the draft

Apply what you learned from the reference posts. Rules:

### Hook (first tweet) — most important thing
- Open with the most surprising or counterintuitive insight, not the topic intro
- If there's a specific failure or mistake in the draft, open with that — failure hooks outperform success hooks
- Under 280 chars, no hashtags, no "thread" label needed
- Must make someone stop scrolling in 1.5 seconds

### Thread body
- One insight per tweet. No multi-idea tweets.
- Each tweet should be self-contained — if someone only reads tweet 3, it should still make sense
- Lead with the conclusion, then explain. Not the other way around.
- Real specifics: numbers, tool names, timelines. "a while" → "3 days". "some subs" → "subs over 50k"
- Lowercase is fine. Rough grammar is fine. Polished grammar reads as corporate.
- 2-4 sentences per tweet max. Shorter wins.

### What kills reach
- Starting with "In today's thread..." or "I wanted to share..."
- Hashtags in the body (ok in final tweet only if at all)
- "If you found this useful, please RT" — desperate energy, kills engagement
- Numbered lists inside a single tweet (bullet points in tweets look like LinkedIn)
- Any sentence that could come from a blog post intro

### CTA (last tweet)
- Ask one specific question that invites a reply, not generic "thoughts?"
- OR: "If you want the [specific thing], DM me" — works for tools/skills
- OR: end on the most provocative insight with no CTA — lets the thread close on a bang

---

## Step 4 — Output

Produce:
1. **The final thread** — numbered tweets, each under 280 chars, paste-ready for @YiyanChenX
2. **Why it's structured this way** — 2-3 sentences on the key structural choices
3. **What to watch at 24h** — which metric matters most (reply rate, saves, retweets?)
4. **3 reference posts used** (or note if API was capped)

---

## Proven Thread Formats (use when API unavailable)

These formats consistently hit 1k+ views in tech/building circles. Choose the best fit for the draft.

### Format 1 — "I did X the wrong way. Here's what actually works."
Hook: Lead with the mistake. Be specific about what failed and why.
Body: Each tweet = one correction. Pairs "what I did" with "what to do instead."
Best for: personal lessons, tool failures, launch mistakes.

### Format 2 — "Nobody talks about [thing]. Here's the real picture."
Hook: Name the thing everyone does that secretly doesn't work.
Body: Each tweet exposes one assumption. Ends with what does work.
Best for: contrarian takes, hidden knowledge, industry criticism.

### Format 3 — "I built [thing] in [timeframe]. Here's exactly what happened."
Hook: Real number + real outcome. Good or bad doesn't matter — specific does.
Body: Chronological. Keep it honest. Include the part that went wrong.
Best for: build in public posts, launch recaps, product updates.

### Format 4 — "[Number] things [platform/tool] won't tell you"
Hook: The most shocking item from the list, stated plainly.
Body: Each tweet is one item. Short. Confident. No hedge.
Best for: platform-specific knowledge (Reddit, LinkedIn, App Store, etc.)

---

## Notes on X Reach

**Views:** driven by early engagement velocity. First 30 minutes matter most. Post when your audience is active (weekday mornings, 8-10am ET for tech crowd).

**Replies:** driven by the hook and the ending. A provocative question in tweet 1 + a strong closer = reply magnet.

**Retweets/saves:** driven by "I'm saving this" utility. How-to threads and lessons-learned threads get saved. Hot takes get retweeted. Hot takes + lessons = both.

**1k views target:** achievable with 3-5 good replies in the first hour. Replies signal to the algorithm that the thread is generating conversation.
