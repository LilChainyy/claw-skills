---
name: reddit-customer-comment
description: Reddit comment engine targeting potential Dropspace customers across a wide sub pool. 3 comments per run. Before writing each comment, reads top comments in the thread to understand what voice gets upvoted and whether tool recommendations are landing. Dropspace included only where it genuinely fits.
---

# Reddit Customer Comment — Conversion Engine

## What This Skill Does

Finds 3 threads per run where someone is experiencing a pain point Dropspace solves. Before writing, reads top comments in each thread to understand (a) what voice gets upvoted, and (b) whether people are actually recommending tools. Writes comments that look native — not like a recommendation from a tool maker, but from a person in the same situation.

Goal: top-of-thread comment that drives clicks to dropspace.dev and registrations.

---

## The Product

**Dropspace** — write your launch or announcement once, it reformats and posts to 9+ platforms automatically.

Core pain it solves: spending hours reformatting the same content for LinkedIn, Twitter, Reddit, TikTok, etc. The manual copy-paste workflow that kills consistency.

Customer language (use these phrases, not product marketing language):
- "I keep falling off with posting"
- "no way big accounts do this manually"
- "I hate reformatting for every platform"
- "I just want to write it once"
- NOT: "cross-posting", "content distribution", "multi-platform publishing"

---

## Subreddit Pool

### Business owners / operators
- r/smallbusiness (530K) — owner-operators doing their own marketing
- r/Entrepreneur (3M) — solo founders and small teams
- r/EntrepreneurRideAlong (366K) — people building in public
- r/growmybusiness (150K) — actively trying to grow
- r/startups (1.3M) — early-stage founders
- r/Solopreneur (80K) — one-person businesses
- r/Freelancers (100K)
- r/freelance (300K) — freelancers building personal brand
- r/consulting (100K)

### Social media / marketing
- r/socialmediamarketing (700K) — marketers and SMBs managing their own social
- r/marketing (1.2M) — broader marketing, tool discussions common
- r/DigitalMarketing (490K) — tool comparison threads are frequent
- r/content_marketing (176K) — content strategists
- r/agency (81K) — digital agency owners managing multiple clients
- r/copywriting (370K) — writers who need to distribute their work
- r/SEO (250K) — SEO people expanding to social

### Ecommerce / retail
- r/ecommerce (614K) — DTC and online store owners
- r/shopify (339K) — Shopify merchant community
- r/Etsy (300K) — sellers needing presence on multiple platforms
- r/AmazonSeller (75K) — expanding beyond Amazon
- r/dropshipping (300K) — often building brand presence
- r/WooCommerce (90K)
- r/realtors (80K) — posting listings and content across platforms

### Creators
- r/podcasting (174K) — clips and episode distribution
- r/NewTubers (646K) — small YouTube creators cross-promoting
- r/youtubers (760K)
- r/blogging (230K) — bloggers expanding to social
- r/TikTok (700K) — creators posting to multiple platforms
- r/Instagram (1.4M) — cross-platform presence
- r/contentcreation (175K)
- r/personalbranding (80K)
- r/photography (3M) — photographers selling prints, building brand

### Niche but high intent
- r/nocode (100K) — builders who automate workflows
- r/automation (300K) — explicitly looking for automation solutions
- r/productivity (2.5M) — people optimizing time, tools discussions common
- r/zapier (60K) — workflow automation community, tool-switchers
- r/sidehustle (100K)
- r/RestaurantOwners (30K) — high pain around consistent social posting
- r/Coaches (40K) — coaches building online presence
- r/RealEstate (600K) — listing promotion across platforms

**Rotation rule:** Don't comment in the same subreddit twice within 48 hours. Track in `reddit-customer-comment-log.md`.

---

## Step 1 — Find the Thread

Search for *people*, not keywords. Four archetypes:

### Archetype A — Overwhelmed operator ⭐ highest conversion
Managing social on top of running a real business. Exhausted, not curious. Tone is tired.
Example titles: "How do you actually keep up with posting consistently?", "I know I need to do social media but I hate it"

### Archetype B — Active tool-seeker ⭐ highest intent
Explicit question about a tool or workflow. May name a tool that's failing them.
Example titles: "Best social media scheduling tool for small business?", "Is Buffer worth it?"

### Archetype C — Inconsistency sufferer
Thinks the problem is motivation. Real problem is friction/reformatting overhead.
Example titles: "How do you stay consistent on social media?", "I always start strong then stop posting"

### Archetype D — Frustrated tool-switcher
Named a specific tool that failed them. Already committed to solving it.
Example titles: "Buffer is too expensive, alternatives?", "Later doesn't support Reddit"

**Skip:**
- Posts over 72 hours old
- OP already thanked someone for a specific tool
- Thread dominated by one tool with 50+ upvotes
- Emotional/grief/burnout thread (leave organic comment instead)
- 0-comment threads

---

## Step 2 — Read the Thread Before Writing (mandatory)

Fetch top 5 comments sorted by upvotes. Ask:

**What are people actually doing in the comments?**
- Are they recommending tools? → tool mention lands naturally, use it
- Are they giving emotional support or general advice? → tool mention feels jarring, skip or reframe
- Are they asking follow-up questions? → match that curiosity tone
- Are they writing lists or flowing sentences? → match the format

**Are tool recommendations present?**
This is the decision gate. If nobody in the top 5 comments has recommended a tool, a tool recommendation from you will stand out negatively. Either wait for a better thread, or write an organic comment without the mention.

If tool recommendations ARE in the comments, your Dropspace mention is expected and competes directly. Go ahead.

**Length and tone calibration:** match what the top comments are doing exactly. If they're 2 sentences, write 2 sentences. If they're lowercase and loose, match that.

---

## Step 3 — Write the Comment

### Voice calibration (learned from real edits)

**First-person beats third-party when you have a real experience to share.**
"I tried hiring but still had to proofread everything. ended up getting a small tool built just for this (dropspace.dev)" outperforms "my friend uses dropspace.dev, still testing it."

Why: first-person sounds like you solved your own problem. Third-party framing sounds like you heard about something. The first has credibility; the second has uncertainty.

**"small tool built just for this"** is the exact frame to use. It positions Dropspace as purpose-built for the specific pain, not a general tool you found.

**No hedge needed when using first-person.** If you're claiming you use it yourself, hedging ("still testing it") undercuts the credibility. Drop the hedge. State it as the solution you found.

**Two sentences is the ceiling.** Most of my drafts are too long. Cut 60-70%. State the pain reframe + the solution. Done.

**Parenthetical `(dropspace.dev)` at sentence end works.** Not always mid-sentence. Put it at the end: "ended up getting a small tool for this (dropspace.dev)"

**Still use third-party when you haven't claimed personal experience.** If the comment is a tools list (Structure 1), third-party framing for Dropspace is correct — you're one of several options, not the thing you use yourself.

---

### Structure 1 — Tools List
Use when: top comments are listing tools, thread is explicitly asking for recommendations.

List 3-4 tools. Dropspace is one. Third-party framing for Dropspace entry here since you're being balanced.

Example:
> "tools worth testing: buffer for basics, dropspace.dev if you're reformatting the same content for every platform manually, later if you're visual-first. two weeks with real content tells you more than any review."

---

### Structure 2 — First-Person Fix
Use when: top comments are experiential, thread is frustration or "what worked for you."

State the pain in OP's terms. Then drop what fixed it for you. First-person, no hedge, two sentences.

Example:
> "The reformatting isn't creative work, I tried hiring but still had to proofread everything. Ended up getting a small tool built just for this (dropspace.dev)"

What makes it work: validates OP's specific pain first, frames solution as personally earned not discovered, no sales language, no features listed.

---

### Structure 3 — Reframe + Fix
Use when: top comments are about habits/motivation, OP doesn't realize the problem is workflow friction.

Reframe the problem first. Then the solution.

Example:
> "consistency on social isn't a motivation problem, it's a friction problem — the more steps between writing and posted everywhere, the more it falls off. fixed it by cutting the reformatting step (dropspace.dev)."

---

## The Dropspace Mention Rules

**Always:**
- Validate OP's specific pain before the mention — never lead with the product
- End with a statement, not a question
- Match the thread's length and tone

**First-person rules (Structure 2 + 3):**
- State it as what you actually use
- No hedge — you found it, it works
- Parenthetical at end: `(dropspace.dev)` or plain in sentence: `dropspace.dev`
- "small tool built just for this" framing

**Third-party rules (Structure 1 — tools list only):**
- "someone pointed me to dropspace.dev" or drop it neutral alongside other tools
- Add a brief hedge since you're not claiming personal use

**Never:**
- UTM parameters
- "Check out", "sign up", "try it"
- Feature lists — one outcome max
- Superlatives: "amazing", "game-changer", "best"
- Full URL with https:// — plain domain only
- Tool mention when top comments contain no tool recommendations

**When to skip the mention:**
- Thread top comments are all emotional support → organic comment only
- Thread top comments are all general advice with no tools → organic comment only
- You're not confident the mention will land naturally → organic comment, build account credibility

---

## Account Safety Rules

- Max 2 promotional comments (with dropspace.dev link) per day per account
- At least 3 hours between promotional comments
- Max 1 promotional comment per subreddit per 48 hours per account
- 5 organic comments for every 1 promotional in any 7-day rolling window
- dropspaceapp: comments only, no posts

---

## Improvement Loop

Log each run in `reddit-customer-comment-log.md`:

```
Date:
Account:
Sub:
Thread URL:
Archetype: [A/B/C/D]
Structure: [tools-list / first-person / reframe]
Top comments were recommending tools: yes/no
Dropspace mentioned: yes/no
Comment text:
Upvotes at 24h:
OP replied: yes/no
Notes:
```

Weekly: check which archetype + structure + sub type performs best. Update skill.
