---
name: reddit-customer-comment
description: Reddit comment engine targeting potential Dropspace customers — not builders, but business owners, marketers, creators, and shop owners who need to post consistently across platforms. Uses dropspaceapp account. Max 2 promotional comments per day, 10:1 organic-to-promo ratio required. Goal: click to dropspace.dev + registration.
---

# Reddit Customer Comment — Conversion Engine

## What This Skill Does

Finds threads in non-builder communities where someone is experiencing the exact pain Dropspace solves, and drops a natural peer recommendation that makes them click.

This is not a warm-up skill. Every comment has a purpose: get someone to visit dropspace.dev and register.

---


## The Conversion Model

Reddit converts when the comment reads like a peer recommendation, not an ad.

**What converts:**
A comment that: (1) names OP's exact pain in their own language, (2) mentions that you had this problem too, (3) says what fixed it, (4) drops the link as an afterthought, not a CTA.

**What doesn't convert:**
- "Check out Dropspace!" — sounds like an ad
- "I built a tool for this" — sounds like a pitch
- "You might want to try..." — sounds uncertain and soft
- Long explanations of features — nobody reads them
- UTM links — spam filter trigger AND looks promotional

**The conversion sequence:**
1. Start with their exact problem (one sentence, their language)
2. One sentence about how you had this too / how long you dealt with it
3. One sentence about what changed when you used Dropspace
4. Drop the link: `dropspace.dev` — plain domain, no UTM, no tracking parameters, no full URL with slashes

---

## Thread Types That Convert (in order)

### Type 1 — Explicit tool-seeking (highest conversion rate)
OP is actively looking for a solution.

Thread signals:
- "What tool do you use to [cross-post / schedule / manage multiple platforms]?"
- "Is there anything that automates [social media / posting / launch content]?"
- "Buffer alternative?" / "Hootsuite alternative for small business?"
- "How do you handle posting to multiple platforms without going crazy?"

Comment template:
> "We use Dropspace (dropspace.dev) — write it once, it reformats and schedules for each platform automatically. Replaced about 2 hours of manual work per launch for us."

Why this converts: OP asked for exactly this. The comment answers the question directly. No fluff.

---

### Type 2 — Active frustration (second highest)
OP is not looking for a product but is clearly in pain about the exact problem Dropspace solves.

Thread signals:
- "I keep falling off with posting consistently"
- "I hate that I have to manually reformat everything for each platform"
- "There's no way [big accounts] do all this manually"
- "I'm so tired of the social media content treadmill"
- "How do successful [founders / shop owners / podcasters] post so much"
- "Managing TikTok + Twitter + Reddit is killing me"
- "I know I need to post but I never have time"

Comment template:
> "Dealt with this for a year before we automated it. The reformatting for each platform was the part that actually killed consistency for us — not the content creation. We've been using Dropspace (dropspace.dev) since [timeframe] and it solved that specific problem. Not perfect but the manual part is gone."

Why this converts: the comment names the sub-problem they described (reformatting, not "social media") and sounds like a real experience, not a pitch. "Not perfect" is what makes it credible.

---

### Type 3 — Process questions (lower conversion, safer)
OP is asking about workflow, not looking for a tool.

Thread signals:
- "What's your content workflow?"
- "How do you handle social media as a solo founder/owner?"
- "What does your launch process look like?"

Comment template:
> "We batch content on Sundays, then [Dropspace](dropspace.dev) handles the actual scheduling and platform formatting. Used to spend 3-4 hours on this, now it's maybe 30 minutes. The rest of the week I don't think about it."

Why this converts: sounds like a natural workflow answer. The product mention is embedded in the process, not spotlighted.

---

## The Link Rule

**Always:** `dropspace.dev` — plain domain, lowercase, no trailing slash, no UTM parameters.

**Never:** 
- `dropspace.dev?utm_source=reddit` — spam filter trigger
- `https://www.dropspace.dev/` — looks promotional
- "Click here" / "check it out" / "sign up" — ad language

The link should feel like you're sharing a bookmark, not making a sale.

---

## Account Safety Rules (non-negotiable)

**Volume:**
- Max 2 promotional comments per day from `dropspaceapp`
- At least 3 hours between any two promotional comments
- For every promotional comment, leave 5+ pure helpful comments (no Dropspace, no link) across different threads

**Ratio enforcement:**
The account should have at minimum a 10:1 ratio of organic:promotional comments in any rolling 7-day window. If you've done 2 promotional comments today, do at least 10 organic comments before running this skill again.

**Repetition:**
- Never post the same link twice from the same account within 24 hours
- Never comment on the same thread twice
- Never drop Dropspace in two different threads in the same subreddit on the same day
- If you commented in r/socialmediamarketing today, wait 48h before another Dropspace comment there

**Link placement:**
- Drop the link IN the comment that mentions Dropspace (not a separate reply)
- Do not reply to your own comment to add the link
- Do not edit a comment to add the link after posting

**Karma threshold:**
- dropspaceapp at 19 karma: can comment in most subs, cannot post
- If karma drops: stop and investigate (downvote campaigns can happen)

**Shadowban check:**
Before each run: open incognito, go to your account profile URL. If recent comments don't appear, stop all activity.

---

## Subreddit Pool (customer subs only)

These are NOT builder subs. The persona here is a business owner or marketer, not a developer.

**Tier 1 — Start here (open posting, highest pain density):**
- r/socialmediamarketing — marketers and SMBs managing their own social, 700K subs
- r/smallbusiness — owner-operators who do their own marketing, 530K subs
- r/agency — digital agency owners managing multiple clients, 81K subs

**Tier 2 — Strong fit (comment first, check rules before posting):**
- r/ecommerce — DTC and Shopify merchants, 614K subs
- r/shopify — Shopify store owners, 339K subs
- r/content_marketing — content strategists, 176K subs

**Tier 3 — Different language, same pain:**
- r/podcasting — podcasters needing clip distribution, 174K subs
- r/NewTubers — small YouTube creators cross-promoting, 646K subs
- r/blogging — bloggers expanding to social, ~200K subs

**Tier 4 — Niche, high intent:**
- r/DigitalMarketing — tool comparison threads are common, 490K subs
- r/Etsy — sellers needing TikTok/Pinterest/Instagram, 300K subs
- r/freelance — freelancers building personal brand, 300K subs

**Do NOT use builder subs** (r/indiehackers, r/SideProject, r/startups, etc.) for promotional comments. Those subs know what Dropspace is and promotional comments there get flagged. Customer subs don't.

---

## Keyword Search Strategy

Before fetching /new for each sub, look for threads containing these phrases:

**Explicit demand (highest intent):**
- "cross-post" / "cross posting"
- "multiple platforms" + "tired" / "exhausting" / "help" / "workflow"
- "scheduling tool" + "looking for" / "recommend"
- "Buffer" OR "Hootsuite" + "alternative" / "too expensive" / "cancel"
- "social media" + "automate" / "automated"
- "post everywhere" / "everywhere at once"

**Frustration signals (second tier):**
- "manually" + "posting" / "reformatting"
- "I hate" + "social media" / "content"
- "no time" + "post" / "social"
- "staying consistent"
- "content treadmill" / "content hamster wheel"
- "copy paste" + "platforms" / "announcement"

**Process questions (third tier):**
- "what tool do you use"
- "how do you handle" + "social" / "content"
- "workflow" + "launch" / "posting"

---

## Comment Voice (different from warm-up)

In builder subs, the persona is an indie dev with sharp takes. In customer subs, the persona is a business operator who solved a logistics problem. The voice shifts.

**Customer sub voice:**
- First person "we" when natural (implies a real business, not a solo dev)
- Practical and outcome-focused ("replaced 2 hours of manual work")
- Not technical ("reformats for each platform automatically" not "API cross-posting")
- Slightly tired, like someone who dealt with this problem for too long before fixing it
- Honest about limitations ("not perfect but the manual part is gone")

**What not to say:**
- "I built this" — makes it sound like a product pitch, not a recommendation
- Feature lists — nobody cares, they want outcomes
- "It's amazing" — nobody trusts superlatives
- "Game-changing" / "seamless" / "powerful" — instant spam read
- Any CTA: "check it out", "sign up", "try it free"

---

## Organic Comment Ratio (run before promotional comments)

Before leaving a promotional comment in a subreddit, leave at least one purely helpful comment in a different thread in that sub or an adjacent sub. This does two things:
1. Account looks like a real participant, not someone who only appears to promote
2. Gives the account more sub-specific comment history before the promotional one

Organic comment example (r/socialmediamarketing, genuinely helpful, no product):
> "The 'post at these exact times' advice is mostly cargo-culted data from 2019. Your audience's active window depends entirely on your specific follower demographics — the only reliable signal is checking your own analytics for when your existing followers are online."

That's a real comment. The promotional comment can follow in a different thread in the same session.

---

## Output Format

Per run, produce:
- 2 promotional comment slots (with sub, thread URL, comment text)
- 3 organic comment slots (same format, no product, build ratio)

```
--- CUSTOMER COMMENT RUN — [DATE] ---

PROMOTIONAL (max 2)

SLOT P1
Sub: r/[subreddit]
Thread: [title]
URL: [direct link to thread]
Thread type: [Explicit ask / Active frustration / Process question]
[paste-ready comment — includes dropspace.dev inline, no UTM, plain domain]

---

SLOT P2
[same format]

---

ORGANIC (complete ratio — pick 3+ from fresh threads)

SLOT O1
Sub: r/[subreddit]
Thread: [title]
URL: [direct link]
[paste-ready organic comment — no product, no link]

---

SLOT O2
[same format]

SLOT O3
[same format]
```

---

## Tracking

After posting, log outcomes in `reddit-customer-comment-log.md`:

```
Date:
Sub:
Thread URL:
Thread type: [explicit ask / frustration / process]
Comment posted: [yes / no]
Upvotes at 24h:
Link in comment: [yes — dropspace.dev]
Clicks (if trackable): unknown
Notes:
```

Weekly review: which thread types get the most upvotes? Which subs are most receptive? Double down on what works.

---

## Failure Log

| What happened | Why | Rule |
|---|---|---|
| UTM link used | Spam filter triggered | Plain domain only, ever |
| Commented twice in same sub same day | Pattern flagged | One promo per sub per 48h |
| No organic ratio maintained | Account looked like a shill | 5+ organic before promotional |
| "Check out Dropspace!" opener | Immediate ad read | Never open with product name |
| Link in separate reply | Looks self-promotional | Link in same comment as mention |
| Posted to builder sub | Wrong audience, gets flagged | Customer subs only for this skill |
