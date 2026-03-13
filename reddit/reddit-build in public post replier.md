---
name: reddit-post-replies
description: Manages replies to comments on your own Reddit posts. Given a post URL, fetches unanswered comments, classifies them, and drafts paste-ready replies that sound like the original poster — casual, honest, builder voice. Keeps threads alive without sounding corporate.
---

# Reddit Post Replies

## Job

When you post on Reddit and people comment, you need to reply. This skill does that.

It fetches the post's comments, finds the ones without a reply from you, classifies each one, and drafts a paste-ready response.

---

## Step 1 — Fetch the post + comments

Fetch: `https://www.reddit.com/r/[sub]/comments/[id].json?limit=50&sort=top`

From the response extract:
- The post body and title (so you understand what was said)
- All top-level comments + their replies
- Author of each comment
- Whether the OP (the post author) has already replied to it

**Unanswered = top-level comment with no reply from the post author.**

Flag any unanswered comment older than 6 hours — those should be prioritised.

---

## Step 2 — Classify each unanswered comment

**Type Q — Genuine question.** They asked something specific about the product, process, or numbers.
> Reply: Answer directly. Add one thing they didn't ask but would want to know. Keep it under 3 sentences.

**Type E — Enthusiasm / short positive.** "This is cool", "following for week 2", "love this".
> Reply: Short, warm, one specific detail that rewards their interest. Not just "thanks!". Don't mirror their enthusiasm back at them.

**Type C — Competitor mention.** They mention a similar tool.
> Reply: Acknowledge it genuinely. Don't trash the competitor. One sentence on how they differ. Move on.

**Type S — Skepticism or pushback.** "Does this actually work", "isn't this just copy-paste automation".
> Reply: Agree with the valid part of the skepticism. Correct the wrong assumption with a specific example. End with something honest about the limitation.

**Type X — Promo / irrelevant.** Bot or someone self-promoting in your thread.
> Skip. Don't reply.

---

## Step 3 — Draft the reply

**Voice rules (match the original post's tone):**
- Lowercase is fine
- Casual and direct — like texting someone who asked a real question
- No "great question!", no "thanks so much for the interest!", no corporate warmth
- Be honest about what's not working — it builds more trust than a polished answer
- Specific > vague: give a number, a platform name, a time, a concrete result
- 1-3 sentences. Shorter is almost always better.
- Never end with a question — end with a statement or a specific detail

**For competitor mentions specifically:**
- Don't be defensive or dismissive
- One genuine observation about the difference
- "Different approach" framing, not "mine is better"
- If their tool does something yours doesn't, acknowledge it

---

## Output format

```
POST: [URL]
Unanswered comments: [count]

---

REPLY 1
From: [username]
Their comment: [full text]
Type: [Q/E/C/S/X]

[paste-ready reply]

---

REPLY 2
[same format]
```

Skip Type X comments entirely.

---

## Tracking

Log replied threads in `reddit-post-log.md`:
```
Post: [URL]
Date replied: [date]
Comments replied to: [count]
Notes: [anything notable — competitor mentions, recurring questions to add to Week 2 post, etc.]
```
