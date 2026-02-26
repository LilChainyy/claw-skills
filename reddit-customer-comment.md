---
name: reddit-customer-comment
description: Reddit comment engine targeting potential Dropspace customers across a wide sub pool. 3 comments per run. Before writing each comment, reads top comments in the thread to understand what voice gets upvoted, then mimics it. Identifies user archetypes with real pain points, not just keywords. Dropspace included only where it genuinely fits.
---

# Reddit Customer Comment — Conversion Engine

## What This Skill Does

Finds 3 threads per run where someone is experiencing a pain point Dropspace solves. Before writing, reads top comments in each thread to understand what the sub rewards. Writes comments that look native to the sub — not like a recommendation from a tool maker, but from a person in the same situation.

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

This is the full pool to rotate across. Group by audience type so you pick threads where the pain is most natural.

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
- r/nocode (100K) — builders who automate workflows, already bought into tools
- r/automation (300K) — explicitly looking for automation solutions
- r/productivity (2.5M) — people optimizing time, tools discussions common
- r/zapier (60K) — workflow automation community, tool-switchers
- r/LifestyleBusiness (50K)
- r/personalfinance adjacent — r/sidehustle (100K)
- r/RestaurantOwners (30K) — high pain around consistent social posting
- r/gyms / r/personaltraining (60K) — fitness professionals posting content
- r/Coaches (40K) — coaches building online presence
- r/RealEstate (600K) — listing promotion across platforms

**Rotation rule:** Don't comment in the same subreddit twice within 48 hours. Track which subs were used in `reddit-customer-comment-log.md`.

---

## Step 1 — Find the Thread (user archetype first, keywords second)

Don't search for keywords. Search for *people*. These are the user archetypes with real pain:

### Archetype A — The overwhelmed operator ⭐ highest conversion
"I'm doing everything myself and social media is killing me"

What their post looks like:
- Mentions managing their own social media on top of running the actual business
- Expresses exhaustion or inconsistency ("I post for a week then fall off")
- Often asking how other people handle it, not asking for a tool specifically
- Tone is tired, not curious — they're already in pain, not research mode

Example thread titles: "How do you actually keep up with posting consistently?", "I know I need to do social media but I hate it", "Anyone else find content creation exhausting when you're running a business?"

---

### Archetype B — The active tool-seeker ⭐ highest intent
"I need something that does X, what do people use?"

What their post looks like:
- Explicit question about a tool
- Mentions a specific problem to solve (cross-posting, reformatting, scheduling)
- May mention current tool that's failing them (Buffer too expensive, Hootsuite overkill)
- Audience in the thread will also be sharing tools — your comment competes directly with others

Example thread titles: "Best social media scheduling tool for small business?", "Is Buffer worth it or is there something better?", "How do you manage posting across multiple platforms without spending hours?"

---

### Archetype C — The inconsistency sufferer
"I know I should post but I can never keep up"

What their post looks like:
- Identifies consistency as the problem
- Usually not asking for a tool, asking for motivation, systems, habits
- The real problem (buried in the post) is usually the time cost of formatting for each platform
- Mention of Dropspace works if you reframe the problem: consistency isn't a willpower problem, it's a workflow problem

Example thread titles: "How do you stay consistent on social media?", "I always start strong then stop posting after 2 weeks", "What's the secret to posting regularly?"

---

### Archetype D — The frustrated tool-switcher
"I tried [tool] and it didn't work for me"

What their post looks like:
- Names a specific tool (Buffer, Later, Hootsuite, Publer)
- Explains what it got wrong
- Still looking for a solution
- Very high conversion — they've already committed to solving the problem, just haven't found the right tool

Example thread titles: "Buffer is getting too expensive, what do people use instead?", "Later doesn't support Reddit, is there an alternative?", "Tried Hootsuite but it's overkill, looking for something simpler"

---

### How to scan for these threads

Fetch `/new.json` and `/hot.json` from 4-5 subs per run. Apply these filters:

**Age:** under 24 hours old for /new. Under 72 hours for /hot if comments are still active.

**Quick triage:** read the title + first paragraph. Ask: does this person have a real, current pain point? If yes, keep. If it's someone asking theoretically or doing research, lower priority.

**Skip these:**
- Posts over 72 hours old
- OP already marked a solution or thanked someone for a specific tool
- Thread is dominated by one tool recommendation with 50+ upvotes (you won't break through)
- Hostile or off-topic thread
- OP is a developer or technical person — they're in the warm-up pool, not the customer pool
- Posts with 0 comments (nobody is watching yet)

---

## Step 2 — Research the Thread Before Writing

**This is mandatory. Do not skip.**

Before writing any comment, fetch:
1. The top 5 comments in the thread sorted by upvotes
2. The post body in full

Analyze what you see:

**Tone:** Is the thread casual and conversational, or structured and informative? Do people use lowercase? Short sentences? Lists?

**Length:** Are top comments 1 sentence or 5 sentences? Match that range.

**Format:** Do people use headers, bullet points, or flowing text? Reddit comments with bullet points in casual threads get skimmed. Lists in informational threads get upvoted.

**What's being rewarded:** Are the top comments giving tool recommendations? Emotional validation? Practical steps? Sarcastic takes? Match what the thread is already rewarding.

**Dropspace fit check:** After reading the thread, ask: does a tool recommendation land naturally here? 
- If top comments are all tool recommendations → your comment can recommend Dropspace directly
- If top comments are all emotional support or general advice → tool recommendation feels jarring; wrap it differently or skip the mention
- If thread is a specific tool comparison → your comment competes directly; Dropspace mention is expected

---

## Step 3 — Write the Comment

Three comment structures that work. Choose based on what Step 2 told you the thread rewards.

---

### Structure 1 — The Tools List (use when thread is explicitly asking for tool recommendations)

List 3-4 tools. Dropspace is one of them. You're being helpful by giving options.

Use **third-party framing** for the Dropspace entry — "someone pointed me to dropspace.dev" or "a friend mentioned dropspace.dev." This removes the founder/user signal. Add a hedge: "still testing it" or "still playing with it."

Template:
> "what stuck: Claude, Cursor, Perplexity. someone pointed me to dropspace.dev for the content side recently — write once, formats for each platform. still testing it. everything else I tried added a new daily step, these ones removed steps."

Verify before using: do top comments list tools? If yes, use it. If the thread is "just recommend one thing," go to Structure 2.

---

### Structure 2 — The Peer Tip (use when thread is frustration or consistency focused)

Validate OP's exact pain in their own words. Then pass along a tip a friend gave you. You're not the product user — a friend is.

**Key rule: always use third-party framing.** "My friend sent me" / "someone in a similar situation told me about" — not "I use." This is the single most important thing that makes it not sound like marketing.

**Add a hedge.** "Still playing with it" / "haven't fully committed yet" — makes it a tip, not an endorsement.

**No parenthetical link format.** Drop the URL plain in the sentence: `dropspace.dev` not `Dropspace (dropspace.dev)`.

Template:
> "rewriting the same thing differently for instagram vs facebook vs tiktok eats up my time. my friend sent me dropspace.dev to cross platform post. im still playing with it"

What makes it convert: it names OP's specific pain (reformatting per platform), the framing is a friend sharing a find, the hedge ("still playing with it") makes it feel like honest curiosity rather than a pitch. OP clicks to see what the friend found.

---

### Structure 3 — The Reframe + Peer Tip (use when thread is about habits/consistency, not tools)

OP thinks their problem is willpower. Reframe it as friction. Then pass along what helped.

Template:
> "consistency on social isn't really a motivation problem, it's a friction problem. the more steps between 'I wrote this' and 'it's posted everywhere' the less likely it happens. someone showed me dropspace.dev — write it once and it handles the rest. still figuring it out but the friction part got better."

---

## The Dropspace Mention Rules

**Always:**
- Plain URL in the sentence: `dropspace.dev`
- Third-party framing: "my friend sent me", "someone pointed me to", "a friend mentioned"
- Hedge: "still playing with it", "still testing it", "still figuring it out"
- Validate OP's specific pain *before* the mention — never lead with the product

**Never:**
- Parenthetical format: `Dropspace (dropspace.dev)` — looks like a formatted ad
- UTM parameters: never
- "I use this tool" / "I built this" — first-person product ownership sounds like a founder pitch
- "Check out", "sign up", "try it" — CTA language
- Feature lists — outcomes only, one sentence max
- Superlatives: "amazing", "game-changer", "best"
- Full URL with https:// — plain domain only
- Mentioning Dropspace when no tool mention fits naturally (write an organic comment instead)

**When to skip the mention:**
If the thread is emotional (grief, burnout, existential) and the top comments are all support-focused, don't drop a tool link. Leave an organic comment that builds account credibility. That's more valuable long-term than a promotional comment that gets downvoted.

---

## Account Safety Rules

**Volume per account:**
- Max 2 promotional comments (with dropspace.dev link) per day per account
- At least 3 hours between promotional comments
- dropspaceapp: comments only, no posts (site-level flagged for submissions)

**Ratio:**
- 5 organic comments for every 1 promotional comment in any 7-day rolling window per account
- If the current session is promotional, the organic slots (O1-O3) in the output are mandatory — complete them before the promotional ones if possible

**Sub repetition:**
- Max 1 promotional comment per subreddit per 48 hours per account
- Track in log

**Link repetition:**
- Never post dropspace.dev more than twice from the same account in a 24-hour window total
- No self-replies to add the link after posting

---

## Improvement Loop — What to Track and Update

After each run, log in `reddit-customer-comment-log.md`:

```
Date:
Account:
Sub:
Thread URL:
Thread type: [tool-seeking / frustration / consistency / tool-switcher]
User archetype: [A / B / C / D]
Structure used: [tools-list / first-person / reframe]
Top comment style observed: [one line]
Comment posted: yes/no
Upvotes at 24h:
Replies from OP: yes/no
Notes (what felt right, what felt off):
```

**Weekly review:** after 2 weeks of runs, look at the log and ask:
- Which archetype converts best (upvotes + replies)?
- Which structure gets the most upvotes in which sub type?
- Is the tools-list structure getting upvoted or buried?
- Which subs are most receptive?

Then update this skill with what you learned. Specifically:
- Move high-performing subs up the pool list
- Update the structure templates with actual phrasing that worked
- Remove patterns that consistently underperform

The skill should get sharper every week. The first batch is a test. The tenth batch should be nearly guaranteed upvotes based on accumulated pattern data.

---

## Output Format

```
--- CUSTOMER COMMENT RUN — [DATE] ---

THREAD RESEARCH

Thread 1: [URL]
Top comment style observed: [one sentence — e.g., "casual lowercase, 2-3 sentences, tool recommendations without enthusiasm"]
User archetype: [A/B/C/D]
Dropspace fit: [yes/no and why]

Thread 2: [URL]
[same]

Thread 3: [URL]
[same]

---

COMMENTS

SLOT 1
Sub: r/[subreddit]
Thread: [title]
URL: [direct link]
Structure: [tools-list / first-person / reframe]
Promo: [yes / no]

[paste-ready comment]

---

SLOT 2
Sub: r/[subreddit]
Thread: [title]
URL: [direct link]
Structure: [tools-list / first-person / reframe]
Promo: [yes / no]

[paste-ready comment]

---

SLOT 3
Sub: r/[subreddit]
Thread: [title]
URL: [direct link]
Structure: [tools-list / first-person / reframe]
Promo: [yes / no]

[paste-ready comment]

---

ORGANIC RATIO SLOTS (complete if 2+ promo comments above)

SLOT O1
Sub: r/[subreddit]
Thread: [title]
URL: [direct link]

[paste-ready organic comment — no product, no link]

SLOT O2
[same]
```

---

## Failure Log

| What happened | Why it failed | Rule updated |
|---|---|---|
| UTM link used | Spam filter triggered | Plain domain only, ever |
| Same sub twice same day | Pattern flagged | One promo per sub per 48h |
| Comment on 0-comment thread | Nobody watching, no upvotes | Skip threads under 3 comments |
| Tool mention in emotional thread | Got downvoted, felt wrong | Skip promo when thread is support-focused |
| Features list in comment | Nobody read it | Outcomes only, no feature descriptions |
| Tools-list without checking if that style fits | Felt out of place | Always do Step 2 before writing |
| First-person product ownership ("I use Dropspace") | Sounds like founder/marketer | Use third-party framing: "my friend sent me" |
| Parenthetical link format `Dropspace (dropspace.dev)` | Looks like a formatted ad | Plain URL in sentence only |
| Full endorsement with no hedge | Reads as a pitch | Always add "still playing with it" or equivalent |
