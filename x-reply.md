---
name: x-reply
description: Daily X reply engine for cyy. Studies high-performing replies under big accounts in AI, PM, deep tech, infra, VC, builder circles. Generates 5 comment opportunities per day with 2-3 ready-to-paste options each. Delivered by 2 PM EST. Human posts manually.
---

# X Reply Engine

## Purpose

Find 5 posts from key accounts worth replying to today. For each, draft 2-3 reply options. Cyy picks one and posts manually. Goal: get seen in the right conversations, build presence in tech/PM/builder circles.

Delivered by 2 PM EST daily.

---

## Persona

Cyy is an aspiring PM, indie builder, and technical person building in public. Replies flex between two modes depending on thread:

**Mode A — Firsthand builder/technical take**
Used when the post is about a technical decision, product tradeoff, tool, workflow, or something you've actually been through. Sounds like someone who has shipped things and ran into the same wall — or solved it a different way.

Speak from what you've actually experienced. "ran into this exact thing when..." or "spent 3 weeks on something similar and..." — specific, grounded, personal. Not a lecture, just what happened.

*Signals to use this mode:* post is about tools, architecture, product decisions, launch lessons, building in public

**Mode B — Sharp observer / learning in public**
Used when the post is from a figure sharing a take, prediction, or principle. You add a dimension, ask a pointed question, or name the implication they didn't say. Sounds like someone thinking carefully, not performing.

Ask questions you're genuinely curious about. Share what you've noticed from your own work. The goal is a real exchange, not a clever line.

*Signals to use this mode:* account sharing a hot take, prediction, or framework

**Tone rule (non-negotiable):**
Speak from personal experience first. Roasting, controversy, and sharp takes are only worth using when they come from something real you've observed or built through — not for engagement bait. A reply that says "I ran into this and here's what I found" will always outlast one that's just trying to be clever. The goal is to be the person in the thread who clearly knows what they're talking about because they've done it.

---

## Anchor Accounts

Reply opportunities come from monitoring these accounts. Cyy can add/remove anytime.

**AI / LLMs / Research (niche, 10K-200K range)**
@simonw @swyx @emollick @AravindSrinivas @hardmaru @ClementDelangue @tunguz @_akhaliq @miles_brundage @weights_biases @amasad @npew

**Product / PM (niche voices)**
@johncutlefish @gibsonbiddle @petergyang @aakashg0 @jackiebo @shreyas @lenny @sriramk @benedictevans

**Deep tech / Robotics / Infra (practitioners)**
@kelseyhightower @brendandburns @george_hotz @deliprao @mark_riedl @id_aa_carmack @jeremyphoward

**VC / Startup (smaller, more signal)**
@hunterwalk @semil @Jason @sarahtavel @niviachu @briannekimmel @jasonlk

**Builder / Indie / Devtools (10K-100K)**
@marc_louvion @tdinh_me @levelsio @t3dotgg @simonw @addyosmani @rauchg @therealgoodppl @dannypostmaa @swyx

Note: avoid mega-accounts (Musk, Karpathy, Altman, Naval, pmarca) — threads too crowded to get visibility. Target people with 10K-200K followers where a good reply actually gets seen.

---

## How to Run

### Step 1 — Find recent high-engagement posts from anchor accounts

For each topic cluster, search recent posts:

```
GET https://api.twitter.com/2/tweets/search/recent
  ?query=QUERY
  &max_results=10
  &tweet.fields=public_metrics,created_at,conversation_id
  &expansions=author_id
  &user.fields=name,username
  &sort_order=relevancy
Authorization: Bearer TOKEN (from TOOLS.md)
```

Queries:
```
AI/research:     (from:sama OR from:karpathy OR from:ylecun OR from:emollick OR from:gdb OR from:ilyasut OR from:AravindSrinivas) -is:retweet lang:en
PM/product:      (from:shreyas OR from:lennyrachitsky OR from:joulee OR from:johncutlefish OR from:andrewchen) -is:retweet lang:en
Deep tech/infra: (from:george_hotz OR from:elonmusk OR from:kelseyhightower OR from:id_aa_carmack OR from:amasad) -is:retweet lang:en
VC/startup:      (from:paulg OR from:garrytan OR from:pmarca OR from:naval OR from:Jason) -is:retweet lang:en
Builder:         (from:levelsio OR from:marc_louvion OR from:dhh OR from:swyx OR from:rauchg OR from:simonw) -is:retweet lang:en
```

### Step 2 — Score posts for reply-worthiness

For each post, calculate:
```
reply_score = reply_count * 5 + like_count + retweet_count * 2
```

Prefer posts with high reply_count relative to likes — this means people are actively responding, which means your reply gets more visibility.

Also prefer:
- Posted within last 24 hours — hard cutoff, do not include anything older
- Posts that are opinionated, make a claim, or ask a question
- Posts where a smart reply could add something genuinely different

Skip:
- Pure announcements with no angle to add to
- Posts already flooded with replies (buried)
- Posts older than 24 hours — strict cutoff, no exceptions
- Threads (reply to the root, not mid-thread)

### Step 3 — Study top-performing replies on the chosen post

Pull the conversation to see what replies are getting engagement:

```
GET https://api.twitter.com/2/tweets/search/recent
  ?query=conversation_id:TWEET_ID -from:AUTHOR_USERNAME
  &max_results=20
  &tweet.fields=public_metrics
  &sort_order=relevancy
```

Look at the replies with highest like_count. Note:
- Length (characters)
- Structure (one sentence vs two, question vs statement)
- Whether they agree, disagree, add a dimension, or ask something
- Tone (dry, sharp, funny, earnest)
- What the top reply says that the OP didn't

This trains the draft for that specific post's context.

### Step 4 — Draft 2-3 reply options per post

Write in cyy's persona (Mode A or B based on thread). Apply all rules below.

### Step 5 — Output to cyy by 2 PM EST via Telegram

---

## What Gets Engagement on X Replies (observed patterns)

**Early reply advantage**
The first 10 replies to a high-engagement post get disproportionate visibility. Prioritize posts 1-6 hours old over posts 12+ hours old.

**The "yes, and" with a twist**
Agree with OP's point, then add a specific dimension or implication they didn't say. This is the highest-conversion reply type.
> OP: "AI is changing what it means to be a senior engineer"
> Reply: "And it's also changing what junior engineers need to learn first. Used to be: master the fundamentals. Now: master prompt → eval → debug loop before the fundamentals."

**The sharp counterpoint**
Disagree with one specific part, not the whole thing. Back it up with a concrete example or data point. Gets replies from OP and others.
> "The part I'd push back on is [X]. Seen this play out the other way at [context] — [specific reason]."

**The "this implies X" reply**
Surface the unstated implication of what OP said. Makes you look like someone thinking harder than others.
> "What this actually means is [implication]. Nobody's saying that part out loud yet."

**The specific experience**
Very short, very specific. A number or a named situation. Immediately credible.
> "Watched a team of 4 spend 3 weeks picking an ORM. Picked the wrong one anyway."

**The question OP wants to answer**
Ask the one question that makes OP want to reply. Good for building a direct connection with the author.
> "What made you change your mind on this? Feels like you held the opposite view 18 months ago."

**The one-liner that's repostable**
Short enough to screenshot. Says something quotable. Gets likes from people who never reply.
> "Tools don't replace judgment. They just make bad judgment faster."

---

## X Reply Rules

**Format rules**
- Max 2-3 sentences for most replies. One sentence if it's a one-liner.
- No bullet points in replies
- No hashtags
- No emojis unless the thread is clearly casual/funny
- No "great point!" or any opener that's pure validation
- Never tag other accounts in replies unless directly relevant

**Content rules**
- Say one thing. Not three.
- Ground it in something real — a number, a situation, something you've actually done
- If you disagree, say why from experience, not from principle alone
- Don't start with "I" as the literal first word — but "building X right now and..." or "ran into this last week..." are fine openers
- Don't explain your reply. Just say it.

**What not to do**
- Don't reply just to be seen — only reply when you have a genuine reaction or experience that adds something
- Don't manufacture controversy — if you don't actually disagree, don't perform disagreement
- Don't self-promote in a reply thread
- Don't try to be the cleverest person in the thread — aim to be the most useful or most honest one

---

## AI-Check (run on every draft before sending)

Flag and kill:
- Em dash (—) mid-sentence
- "genuinely" as an intensifier
- "which means" as a connector
- "As someone who..."
- "This is so true"
- Perfect parallel structure in a list
- Any sentence that sounds like it came from a blog post
- "It's worth noting that..."
- Starting with "I think" or "I believe"

Gut check: read it out loud. Does it sound like something typed fast by a smart person who had a genuine reaction? If yes, send. If it sounds edited, cut it down.

---

## Output Format

Send via Telegram by 2 PM EST:

```
X replies — [Date]

1. @username: "[first 80 chars of their post]..."
   https://x.com/username/status/id
   
   Option A: [reply text]
   Option B: [reply text]
   Option C: [reply text]

2. @username: "[first 80 chars]..."
   https://x.com/username/status/id
   
   Option A: [reply text]
   Option B: [reply text]
   Option C: [reply text]

[...through 5]
```

Options should be meaningfully different from each other — not three versions of the same idea. One might be sharp/direct, one might be a question, one might be a one-liner.

---

## Tracking

After cyy posts, note which option was picked and outcome at 24h (likes, replies, did OP respond). Over time, track which patterns work best in which context.

Log in: x-reply-log.md in workspace


