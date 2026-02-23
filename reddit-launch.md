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

### Step 3 — Claw runs the AI-check (mandatory, see below)
- Every draft gets reviewed against the AI-check list before being sent

### Step 4 — Send draft to user
- Title, body, and direct submit link sent via Telegram

### Step 5 — Human posts manually
- Copy-paste title and body, select flair if required, submit

### Step 6 — Claw logs the result
- User confirms live or flags removed
- Claw updates reddit-launch-log.md

---

## Tone Rules (non-negotiable)

### What works
- Brutally specific personal story — not "I was frustrated by X" but "I got charged 15 euros for a JPEG that took 30 seconds"
- Casual to the point of rough — write how you'd text a friend, not a press release
- Product is secondary — story first, link buried and incidental
- Vulnerability gets replies — "four hours feels embarrassing to admit" invites engagement
- End with a hook — something that makes people want to roast you, disagree, or share their own story

### What kills posts
- Any pitch structure (problem, solution, CTA)
- Marketing words: game-changing, powerful, seamless, excited to share, streamline, leverage, curated, tailored
- Generic endings: "Would love feedback!" / "Let me know what you think!" / "Happy to answer questions!"
- Announcing the product name like a brand launch

### The hook rule
End with one line that does one of:
- Makes people want to correct or roast you ("am I missing something obvious?")
- Invites a hot take or debate
- Surfaces a shared frustration and asks if they felt it too
- Is slightly self-deprecating in a relatable way

Good: "Probably reinvented something that already exists. What are people actually using for this?"
Good: "Still not sure if the problem is real or I just have bad launch habits."
Bad: "Would love your feedback on dropspace.dev"
Bad: "Happy to answer any questions!"

---

## Persona Rule

Every post needs one line early on that grounds who is speaking. Not a bio. Just enough to make the frustration feel earned.

Weave it into the first paragraph, one sentence max, match it to the subreddit audience.

Examples by sub type:
- Solo/indie subs: "Been building side projects solo for a couple years, no co-founder, just shipping stuff and seeing what sticks."
- Entrepreneur subs: "I run a small bootstrapped thing, so I'm the builder and the marketer and the person up at midnight copy-pasting into LinkedIn."
- Side hustle subs: "I build things evenings and weekends, so any launch time I can cut actually matters."
- SaaS/growth subs: "Launched a few products over the past couple years and the distribution side always takes longer than the build."

Never open with "I'm an indie developer and I built..." — that's a bio, not a persona. Vary the line across posts, never reuse the same one.

---

## AI-Check (run this on every draft before sending)

This is the last step before the post goes out. Read the draft and flag anything on this list. If you find it, rewrite that sentence.

### Instant AI tells — kill on sight
- Em dash used mid-sentence (—) — real people use commas or just end the sentence
- "no team, just me" or any "not X, just Y" contrast pattern
- "figuring out X as I go"
- "hacked something together" / "cleaned it up"
- "which means" as a connector
- "the part I [emotion] most" (e.g. "the part I dreaded most")
- Starting a paragraph with "So" for dramatic effect
- "genuinely" as an intensifier anywhere
- Three-part parallel lists that feel too neat
- Any sentence that explains itself ("X, which means Y")
- "I realized I needed to..."
- "as I go" / "as it turns out" / "it turns out"

### Structural AI tells
- Every paragraph does exactly one clean job — real writing is messier
- Sentences are too uniformly medium-length — mix short and long unevenly
- The post has a beginning, middle, end that are too distinct
- Nothing is left unresolved or rough

### The gut check
Read the full draft out loud. If any sentence sounds like something a product landing page would say, cut it. If it sounds like a LinkedIn thought leader, cut it. If it sounds like a person typing quickly and not editing much, keep it.

---

## If Something Goes Wrong

- Post removed silently: check in incognito, log it, adjust angle or skip the sub
- Karma gate blocks posting: note it, move on
- Sub has strict self-promo rules: flag to user, decide together

---

## Track As You Go

Log file: reddit-launch-log.md in workspace

Per post: subreddit, title, date, outcome (live/removed/karma-gated), upvotes at 24h, notes.

After day 6: review what lands. Double down on traction angles. Cut subs that keep removing.
