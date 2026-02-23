---
name: reply
description: Monitor Reddit and X/Twitter for buying intent signals. Use when you want to find people actively looking for your product category, complaining about competitors, or asking for recommendations — and reply with your product naturally. Handles keyword monitoring, intent scoring, reply drafting, human-paced posting, and outcome tracking.
---

# Intent Sniping

## What This Skill Does

Finds people mid-decision — right when they're frustrated with a competitor, asking for recommendations, or admitting a problem your product solves — and gets your product in front of them before they've made up their mind.

This is not a broadcast strategy. It's a sniper approach: low volume, high precision, high conversion.

---

## Section 1: Keyword Setup

### High-Intent Keywords (reply immediately)
These signal active buying intent. Prioritize these above everything else.

```
"alternative to [competitor]"
"switching from [competitor]"
"[competitor] is too expensive"
"[competitor] keeps [breaking/crashing/failing]"
"cancel [competitor]"
"best tool for [your use case]"
"recommend a [product category]"
"looking for something like [competitor] but"
"anyone use [competitor]? worth it?"
"need help with [pain point your product solves]"
```

### Medium-Intent Keywords (reply if context looks right)
These signal awareness of the problem but not active search yet. Only engage if the post has clear buying signals in the body.

```
"struggle with [pain point]"
"anyone else dealing with [problem]"
"how do you handle [problem]"
"what's your workflow for [use case]"
"[competitor] pricing"
"[competitor] review"
```

### Low-Intent / Skip These
Don't waste replies here. Low signal, high noise.

```
"[competitor] meme"
"[competitor] founders"
"history of [competitor]"
General industry news with no personal pain
Rants with no question or action intent
```

### How to Search Per Platform

**Reddit:**
```
site:reddit.com "[keyword]"
reddit.com/search/?q=[keyword]&sort=new&t=week
```
Scan /new not /hot — hot posts are old, new posts are where you can actually change someone's mind.

**X/Twitter:**
```
"[keyword]" min_faves:5 -is:retweet lang:en
"[competitor]" (alternative OR switching OR cancel) since:[3 days ago]
```
Use Twitter's advanced search. Filter out retweets to get original posts only.

---

## Section 2: Intent Scoring — Engage or Skip

Before replying, score the post. If it doesn't hit the threshold, skip it.

### Green Light — Reply
- Post is less than 24 hours old
- OP is clearly asking a question or expressing frustration
- No accepted answer yet, or existing answers are weak
- Thread tone is neutral or frustrated (not hostile)
- Post has at least some engagement (2+ upvotes, 1+ comment) — signals it's real
- Keywords match high-intent list above

### Yellow Light — Reply Only If You Have Something Genuinely Useful
- Post is 24-72 hours old
- OP got some answers but none mention your product category
- Medium-intent keywords
- You can add a clearly different angle from existing replies

### Red Light — Skip
- Post is 72+ hours old (too late, decision likely made)
- OP is clearly venting with no intent to change tools
- Thread is already full of competitor replies (you'll look desperate)
- OP has replied "solved!" or "thanks, going with X"
- Subreddit/community has strict no-promo rules
- Post has 0 engagement (may be shadowbanned or dead)
- OP seems emotionally distressed — not the moment to pitch

---

## Section 3: Reply Templates by Intent Type

The formula that works: answer the problem first → compare honestly → mention your product last, casually.

Never lead with your product. Always lead with value.

### Type 1: "Looking for an alternative to [Competitor]"

**BAD (sounds like a bot):**
> "Have you tried [Your Product]? It's a great alternative to [Competitor] with features X, Y, Z. Here's a link: [url]"

**GOOD:**
> "depends what's frustrating you about [Competitor] tbh. if it's the pricing, [Competitor B] has a cheaper tier but the UX is rough. if it's the [specific feature], i've been using [Your Product] for that — handles it better in my experience. what's the main thing that's not working for you?"

Why it works: Asks a follow-up, sounds like a real user, doesn't over-pitch. OP will reply, you get a second touchpoint.

---

### Type 2: "Struggling with [Pain Point]"

**BAD:**
> "[Your Product] solves exactly this! Check it out at [url]"

**GOOD:**
> "this used to kill me too. what worked for me was [genuine tip that doesn't require your product]. if you're doing that at scale though, [Your Product] handles it automatically — saved me probably 3hrs/week. happy to share more if that's the direction you're heading"

Why it works: Gives free value first. Product mention feels earned, not forced.

---

### Type 3: "Best tool for [Use Case]?" (Recommendation Request)

**BAD:**
> "[Your Product] is the best for this hands down"

**GOOD:**
> "three that actually get used in this space: [Competitor A] if you need [feature], [Competitor B] if [different use case], and [Your Product] if [your specific strength]. depends on your workflow — what does your current setup look like?"

Why it works: Listing competitors makes you look unbiased. Converts better than a solo pitch. This format gets upvoted because it's genuinely useful.

---

### Type 5: X Reply

Short. Direct. No paragraphs.

**BAD:**
> "Great point! Have you considered [Your Product]? It handles [feature] really well and integrates with [tool]. Here's the link:"

**GOOD:**
> "this is exactly why we built [Your Product] — [one sentence on how you solve it]. happy to show you if you're curious"

Or just answer the question and let them follow you back organically.

---

## Section 4: Tone Per Platform

| Platform | Tone | Length | Product Mention |
|----------|------|--------|-----------------|
| Reddit | Casual, lowercase ok, slightly self-deprecating | 3-6 sentences | Late, subtle, optional |
| X | Punchy, direct, can be slightly bold | 1-3 sentences | Can be more direct |
 Mid-answer, one mention |

**Universal rules across all platforms:**
- Never use marketing language: "game-changing," "revolutionary," "best-in-class," "seamless"
- Never end with "Feel free to reach out!" or "Happy to answer any questions!"
- Never use bullet points listing your features — dead giveaway
- Vary your sentence length — short and punchy mixed with longer ones
- Lowercase "i" is fine on Reddit. Slightly imperfect grammar is fine. It signals human.

---

## Section 5: Human-Speed Pacing

This is what keeps accounts alive. Bots are fast and predictable. Humans are slow and erratic.

**Between replies:**
- Wait 4-8 minutes between replies (randomize — never the same gap twice)
- After every 3 replies, take a longer break (10-15 minutes)
- During waits, actually browse the platform — scroll the sub, read other posts, upvote something unrelated

**Daily limits:**
- Reddit: max 15-20 replies/day per account
- X: max 30-50 replies/day (X bans accounts at 200+ automated replies)

**Navigation patterns:**
- Don't go directly to the reply box every time. Sometimes read the full thread first. Sometimes upvote the OP before replying.
- Vary your sequence: sometimes search → read → reply. Sometimes browse sub → find post → reply. Never identical flow every session.

**If you hit a rate limit, CAPTCHA, or "you're doing that too much" warning: stop immediately. Do not retry. Tell the user.**

---

## Section 6: Account Health Rules

### Before You Run This Skill
- Account must be at least 2 weeks old
- Reddit accounts need 50+ karma before any promotion — build it first in unrelated threads
- Profile should look complete: bio, post history, non-promotional activity
- Never run on a brand new account

### Shadowban Detection
Reddit and X can shadowban silently — your posts appear to go through but nobody sees them.

After posting, check:
- Open an incognito window and navigate to the thread — can you see your reply?
- Check your profile from incognito — does the post appear?
- If it doesn't show: shadowbanned or spam-filtered. Stop the run and tell the user.

### When to Rotate Approach
- If 3+ replies in a row get downvoted or removed — pause and review tone
- If you get a mod warning in any community — stop posting there entirely
- If engagement drops sharply over a week — templates are stale, rewrite them

---

## Section 7: Tracking & Compounding

Log every reply. This is how the skill improves over time.

**Log format per reply:**
```
Date:
Platform:
Post URL:
Keyword that triggered it:
Reply text used:
Template type (1-5):
Outcome: [upvoted / ignored / downvoted / removed / got reply / converted to click]
Notes:
```

**Weekly review questions:**
- Which keywords are generating the most green-light opportunities?
- Which template types are converting vs getting ignored?
- Which subreddits/communities are worth watching vs cutting?
- Add winning variations to this file. Document failures with a "never do this" note.

**The compounding effect:**
Reddit answers get Google-indexed. A good answer today may drive traffic for 18 months. Track which old answers are still getting views — those topics are worth doubling down on.

---

## Section 8: Failure Log — What Gets You Banned or Ignored

Add to this table every time something fails. This is how the skill gets smarter.

| What Happened | Why It Failed | Rule Added |
|---------------|---------------|------------|
| Reply led with product link | Looked like spam, got removed | Never open with a link |
| Posted same template across 5 subs in 10 min | Reddit spam filter triggered | 4-8 min gaps minimum |
| Replied to 72hr old post | OP had moved on, zero engagement | Skip posts older than 48hrs |
| Used "game-changing" in reply | Downvoted immediately | No marketing language ever |
| Replied to hostile thread | Got into argument, damaged brand | Skip threads with negative tone |
| Replied to post with 0 upvotes | Post was shadowbanned, nobody saw reply | Skip posts with 0 engagement |

---

## Error Handling

- If browser automation fails mid-reply: save the draft text, report to user, do not retry blindly
- If a community blocks you: report it and skip — don't attempt workarounds
- If login is required: ask user to authenticate before running
- If reply was partially submitted: check profile in incognito before retrying — don't double-post
- If account gets suspended mid-run: stop all activity across all platforms immediately and tell the user
