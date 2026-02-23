---
name: reddit-launch
description: Launch Dropspace across 29 targeted subreddits at 2-3 posts/day. Claw researches each subreddit and drafts the post. Human posts manually to bypass Reddit's 2026 API restrictions and community-specific filters.
---

# Reddit Launch — Dropspace

## Product

**Dropspace** — https://www.dropspace.dev/
Write your launch once. It reformats and posts to 9+ platforms automatically.
Solves the problem of founders spending days copy-pasting the same announcement into different formats for LinkedIn, Reddit, Twitter, Product Hunt, etc.

---

## Why Manual Posting

Reddit's 2026 API restrictions and community-specific requirements (mandatory flairs, karma thresholds, participation checks) have effectively blocked AI-driven automation for individual users. Automated posting gets flagged or silently removed.

**The hybrid workflow:**
- Claw handles research, drafting, and tracking
- Human handles the final submit on Reddit
- This bypasses "human-first" filters safely while keeping the content quality high

---

## The 29 Subreddits

r/AlphaandBetaUsers, r/AppIdeas, r/buildinpublic, r/business, r/Business_Ideas, r/Entrepreneur, r/EntrepreneurRideAlong, r/Entrepreneurs, r/GrowthHacking, r/growmybusiness, r/indiebiz, r/indiehackers, r/InternetIsBeautiful, r/juststart, r/MicroSaas, r/micro_saas, r/passive_income, r/productivity, r/SaaS, r/scaleinpublic, r/SideProject, r/smallbusiness, r/Solopreneur, r/startup, r/startup_resources, r/Startup_Ideas, r/startups, r/thesidehustle, r/vibecoding

---

## Pace

- 2-3 posts per day, spread across the day — never back to back
- At least 2 hours between posts
- Post during active hours (morning or evening), not late night
- Full campaign runs ~12 days

---

## Workflow Per Post

### Step 1 — Claw researches the subreddit
- Fetches Hot posts from the last week via Reddit JSON API
- Reads titles, post length, tone, link placement, comment patterns
- Checks subreddit rules (karma requirements, flair, self-promo policy)

### Step 2 — Claw drafts the post
- Writes title + body tailored to that subreddit's observed style
- Sends draft to user via Telegram with direct link to submit page

### Step 3 — Human posts manually
- Open the subreddit submit link provided
- Copy-paste title and body from Claw's draft
- Select flair if required
- Submit

### Step 4 — Claw logs the result
- User confirms post is live (or flags if removed)
- Claw updates the tracking log

---

## Tone Rules (non-negotiable)

These came from studying what actually gets upvotes vs ignored vs downvoted.

### What works
- **Brutally specific personal story** — not "I was frustrated by X" but "I got charged €15 for a JPEG that took 30 seconds"
- **Casual to the point of rough** — write how you'd text a friend, not how you'd write a press release
- **Product is secondary** — the story comes first, the link is buried and feels incidental
- **Vulnerability gets replies** — "Four hours feels embarrassing to admit" invites engagement
- **End with a hook** — not a CTA, not "check it out", but something that makes people want to roast you, disagree, or share their own experience

### What kills posts
- Any pitch structure (problem → solution → CTA)
- Marketing adjectives: "game-changing," "powerful," "seamless," "excited to share"
- Phrases that sound like ad copy: "generates content tailored to each platform"
- Generic endings: "Would love feedback!" or "Let me know what you think!"
- Saying the product name like it's a brand announcement

### The hook rule
Every post must end with a line that does one of these:
- Makes people want to roast/correct you ("Am I missing something obvious?")
- Invites debate or a hot take ("Or is this just a solved problem nobody talks about?")
- Surfaces a shared frustration and asks if they've felt it too
- Is slightly self-deprecating in a way that's relatable

**Examples of bad endings:**
- "Would love your feedback on dropspace.dev"
- "Happy to answer questions!"
- "Let me know what you think"

**Examples of good endings:**
- "Four hours feels embarrassing to admit but I couldn't find a faster way. Am I missing something obvious?"
- "Probably reinvented something that already exists. What are people actually using for this?"
- "Still not sure if the problem is big enough to matter or if I just have terrible launch habits."

---

## If Something Goes Wrong

- Post removed silently: check in incognito, log it, skip the sub or adjust angle
- Karma gate blocks posting: note it, skip, come back later
- Sub has strict self-promo rules: flag to user, decide together whether to skip

---

## Track As You Go

Log file: `reddit-launch-log.md` in workspace

For each post: subreddit, title, date, outcome (live/removed/karma-gated), upvotes at 24h, notes.

After day 6: review what's landing. Double down on angles with traction. Cut subs that keep removing.
