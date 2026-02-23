---
name: reddit-reply
description: Daily Reddit content engine. Two-phase: Phase 1 (0-20 karma) pure warm-up comments. Phase 2 (20+ karma) generate a daily batch of 10 Reddit opportunities — a mix of Dropspace intent threads and adjacent tech/building topics where the persona can comment something helpful, fun, or sassy. Human does the final manual step. Output is a ready-to-use daily list.
---

# Reddit Reply — Daily 10 Opportunities

## What This Skill Outputs

Every time you run this skill, it produces a list of 10 Reddit threads to engage with today — including:
- The subreddit
- Direct link to the thread
- A short, ready-to-paste comment or post reply
- Whether this is a Dropspace-relevant reply or a persona-building comment

Human manually posts each one. Claw does the research and drafting.

---

## The Persona

Every comment comes from this person.

**Who you are:** Solo developer and indie entrepreneur. You build your own stuff in tech, ship it, and share what you learn. You have opinions. You find certain things funny. You've been burned by bad tools and made dumb mistakes building products. You're helpful when you know something, sassy when something is obviously wrong, and honest about what you don't know.

**Tone:**
- Short. Most comments are 2-4 sentences max.
- Lowercase is fine. Slightly rough grammar is fine.
- Helpful, direct, occasionally dry or sarcastic
- No filler: "Great question!", "Happy to help!", "As someone who works in this space..." — all banned
- Opinions are welcome. Wishy-washy non-answers are not.

---

## What Gets Upvoted — Research-Backed Criteria

Before writing any comment, check it against these patterns. These come from studying r/TheoryOfReddit, comment quality research across millions of Reddit comments, and viral post analysis in tech/builder subs.

### The 6 comment types that consistently get upvoted

**1. "You said what I was thinking"**
Articulates the shared feeling that nobody else put into words. Gets upvoted because people feel seen/validated. Works when a thread has a lot of vague frustration and you name it precisely.

Example: Someone posts about a complicated dev setup. Your comment: "the real problem isn't the tool, it's that every new tool promises to be the last tool."

**2. The one-sentence killer**
Short, sharp, lands perfectly. Dry wit, the perfect analogy, or just the exact right observation. These punch above their weight because they're easy to upvote and re-read.

Example: "most 'best practices' are just 'what the last senior dev was comfortable with' written down."

**3. The "wait, actually" insight**
Gently reframes or corrects the premise with a fact or angle the thread missed. People upvote because they learned something or had their mind slightly changed. Must be specific — a vague counterpoint gets ignored.

Example: Someone asks if jQuery is dead. Your comment: "jQuery still ships on more sites than React, Vue, and Angular combined. 'dead' means 'the blogs stopped writing about it.'"

**4. The specific experience**
"I did this exact thing and here's what actually happened: [specific detail]." More specific = more credible = more upvotes. Generic experiences get ignored. Exact numbers, exact tools, exact outcomes get read.

Example: "spent 3 weeks on our own auth system. two months later we replaced it with Auth0. the 3 weeks were not worth it."

**5. The pattern recognition**
"This keeps happening because X" — when X explains something the reader noticed but couldn't name. These are the most shareable comments.

Example: "every startup I've seen die at series A had the same thing: the founders stopped talking to users after product-market fit."

**6. The honest/self-deprecating take**
"I've been that person and it was embarrassing." Relatable vulnerability in a room full of people performing competence. Gets upvotes because it gives others permission to relate.

Example: "genuinely thought I was the only one who spent 4 hours reformatting the same launch post. apparently not."

---

### What kills comments (data-backed)

- **Generic agreement** — "this is so true!" adds nothing, gets ignored
- **Long explanations without a sharp point** — nobody reads a wall of text in a comment section
- **Internet slang** — lol, tbh, ngl used to signal credibility; now they signal low quality
- **Hedged takes** — "well it depends..." without actually saying what it depends on and why
- **The obvious answer** — if 5 other comments already said it, you're wasting a post
- **Leading with "I"** — comments that start with "I think..." or "I believe..." get read as opinion, not insight
- **Asserting without evidence** — "that's wrong" with no follow-up gets downvoted; "that's wrong because X" gets upvoted

---

### Comment quality self-check

Before finalizing any comment, ask:
- Does the first sentence make someone want to read the second?
- Is there one specific thing in this comment that couldn't have been said by anyone?
- If I saw this comment from a stranger, would I upvote it?
- Does it add something the thread doesn't already have?

If the answer to any of these is no, rewrite or skip the thread.

---

## Phase 1 — Warm-Up (0 to 20 karma)

No Dropspace mentions. No product links.

Goal: make the account look like a real person with a history before any product activity.

**Where to look:**
- r/learnprogramming — answer technical questions
- r/webdev — share opinions on tools and workflows
- r/SideProject — comment on other people's launches
- r/indiehackers — join discussion threads
- r/startups — answer process questions
- r/programming — chime in on technical debates

**What counts as a good warm-up comment:**
- Specific and short — "ran into this exact thing, [X] worked for me because [specific reason]"
- Opinionated — "honestly [popular tool] is overrated for this, [alternative] does the same thing with less setup"
- Curious — "has anyone tried [approach] for this? wondering if the complexity is worth it"
- Dry/funny when the post warrants it

**What doesn't count:**
- Generic agreement
- Long explanations
- Any mention of Dropspace or links

---

## Phase 2 — Daily 10 (20+ karma)

### Types of content in the daily batch

Each daily batch of 10 mixes two types:

**Type A — Dropspace intent (3-4 per day)**
Threads where someone is experiencing the pain Dropspace solves. Reply with the persona, product mention comes last and softly.

**Type B — Adjacent persona content (6-7 per day)**
Threads about tech, building, indie hacking, tools, shipping, distribution — where the persona can say something genuinely useful, funny, or opinionated without mentioning Dropspace at all. These build karma, credibility, and voice.

The ratio matters. An account that only comments when it can mention its product looks like a bot. One that has real opinions across many threads looks like a person.

---

### Where to find Type A (Dropspace intent)

Scan r/new, not r/hot.

**High-intent keywords:**
```
"reformatting" + launch / announcement
"copy-pasting" + announcement / platforms
"how do you post to multiple platforms"
"alternative to Buffer" OR "alternative to Hootsuite"
"launch workflow" + pain / annoying / takes too long
"cross-posting" + hate / annoying / problem
"best tool for" + launch / social / multi-platform
"distribution" + "side project" OR "indie" OR "solo"
"spending too long on" + launch / announcements
```

**Skip:** posts over 48hrs old, 0 engagement, OP already picked a solution, hostile threads.

---

### Where to find Type B (adjacent persona content)

Good hunting grounds for interesting tech/building discussions:

- r/SideProject — anything in Hot/New about building, launching, struggling
- r/indiehackers — process discussions, failure stories, workflow questions
- r/webdev — tool debates, workflow arguments, "is X still worth learning" threads
- r/programming — takes on languages, tools, paradigms — especially controversial ones
- r/startups — founder struggles, product decisions, growth problems
- r/Entrepreneur — solo builder problems, time management, distribution woes
- r/buildinpublic — milestone posts, struggle posts
- r/SaaS — pricing debates, churn problems, distribution questions
- r/ExperiencedDevs — more nuanced technical takes

**What makes a good Type B thread:**
- Has a genuine question or controversy where a short, opinionated answer adds something
- The post is under 24 hours old
- Has at least a few comments already (real thread, not dead)
- A short punchy reply would stand out from the usual walls of text

---

### Comment/reply length guide

| Thread type | Target length |
|---|---|
| Answering a specific technical question | 2-3 sentences |
| Opinionated take on a tool debate | 1-3 sentences |
| Dropspace intent reply | 3-5 sentences, question at the end |
| Funny/sassy response to something obvious | 1-2 sentences |
| Genuinely complex question | max 4-5 sentences — if it needs more, don't reply |

Short wins on Reddit. Long comments get skimmed. Short comments that say the thing get upvoted.

---

## Freshness Rule (mandatory — run before building every daily batch)

Every post in the daily 10 must be one you haven't engaged with before. Recycling old threads wastes the comment (OP has moved on) and makes the account look like a bot pattern.

### How to enforce freshness

**Step 1 — Pull from /new, not /hot or /top**
Hot and Top posts are days or weeks old. /new is where fresh conversations are. Always fetch from `/new.json` when scanning for threads.

**Step 2 — Age filter: under 24 hours only**
Check the `created_utc` field on each post. Convert to hours since posting. Reject anything over 24 hours old. Exceptions allowed up to 48 hours only if the thread is still actively getting new comments.

**Step 3 — Check against the used-posts log**
Before adding a thread to the daily batch, check `reddit-used-posts.md` in the workspace. If the post URL is already there, skip it. No exceptions.

**Step 4 — Log every post URL after the batch is sent**
After generating the daily 10, append all 10 post URLs to `reddit-used-posts.md` with today's date. This is how future runs know what's been used.

### reddit-used-posts.md format
```
## 2026-02-23
- https://www.reddit.com/r/webdev/comments/1rcmvph/
- https://www.reddit.com/r/webdev/comments/1rcq0pl/
...

## 2026-02-24
- ...
```

### Why this matters
- Commenting on a 3-day-old post gets ignored — OP and the thread have moved on
- Reusing a post you already commented on looks spammy and can get flagged
- Fresh threads mean your comment appears near the top when people are still reading
- New posts on /new have fewer comments, so yours stands out more

---

## Daily Output Format

When running this skill, produce exactly this format — 10 entries, ready to hand to the user.

```
--- REDDIT DAILY 10 — [DATE] ---

1. [TYPE A / TYPE B]
   Sub: r/[subreddit]
   Thread: [title] — [direct URL]
   Comment:
   [paste-ready comment text]

2. [TYPE A / TYPE B]
   Sub: r/[subreddit]
   Thread: [title] — [direct URL]
   Comment:
   [paste-ready comment text]

...
```

Notes on the format:
- Thread URL should be the direct link to the post
- Comment should be paste-ready — no brackets, no placeholders
- Mark clearly whether it's Type A (Dropspace-relevant) or Type B (persona)
- If a thread requires a flair on the sub, note it

---

## Karma Thresholds

- 0-20 karma: Phase 1 only, no product, no links
- 20-50 karma: Phase 2 but stick to smaller subs
- 50-100 karma: most subs unlocked
- 100+ karma: full access including r/Entrepreneur, r/startups, r/SaaS

---

## Shadowban Check

Every few days: open incognito, go to your profile, check if recent comments appear. If they don't, account may be shadowbanned. Stop all activity and flag immediately.

---

## Tracking

After posting, log outcomes:

```
Date:
Thread URL:
Type (A or B):
Upvotes at 24h:
Got reply: yes / no
Notes (what worked, what felt off):
```

Weekly: which Type B topics generate the most engagement? Which Type A keywords are finding the best intent threads? Double down on what works, cut what doesn't.

---

## Failure Log

| What Happened | Why It Failed | Rule Added |
|---|---|---|
| Led with product link | Spam filter | Never open with a link |
| Same reply tone across 10 comments | Looked automated | Vary sentence structure, vary length |
| Replied to 72hr old post | No engagement | Skip posts older than 48hrs |
| Used marketing language | Downvoted | No marketing language |
| Replied to hostile thread | Got into argument | Skip negative-tone threads |
| Generic reply with no opinion | Got ignored | Every comment needs a take |


