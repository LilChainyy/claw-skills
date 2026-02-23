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

## Writing Rules (always apply)

- No marketing language — "game-changing," "revolutionary," "excited to share" are instant downvotes
- Lead with the problem or a personal observation, not the product
- The link feels like an afterthought, not the point
- End with a real question when natural — it invites replies
- Every post must be meaningfully different — different angle, opening, structure

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
