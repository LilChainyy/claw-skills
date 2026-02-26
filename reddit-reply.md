---
name: reddit-reply
description: Daily Reddit warm-up engine. 5 paste-ready comments per run. Pure karma building — no Dropspace, no links, no product.
---

# Reddit Reply — Daily Warm-Up

## Job
Build account karma. Look like a real person with opinions. Nothing else.

---

## Step 0 — Read the thread before writing (mandatory)

Before writing any comment, fetch the top 5 comments in that specific thread sorted by upvotes.

Ask:
- What length are the top comments? Match it exactly.
- What tone? Dry/sarcastic, technical, casual, blunt?
- Do they use lowercase? Full sentences? No punctuation?
- What's the single thing that made the top comment win — a specific detail, a reframe, an ironic observation?

Then write in that exact style. Don't bring your own voice into a thread with an established tone — blend in first, then add the take.

---

## Rules

- 2-3 sentences max. 1 sentence is fine if it lands.
- Lowercase is fine. Rough grammar is fine.
- **Always end with a statement, never a question.** Questions sound like a chatbot. Statements get upvoted by lurkers.
- One specific detail (a number, a tool name, a named situation) — proves you've actually done this.
- No: "great question", "happy to help", "as someone who works in this space", "genuinely", em dashes, "So" openers.
- If it could be posted on LinkedIn without sounding weird, rewrite it.

---

## Patterns (pick one per comment)

**A — Reframe the premise.** OP is worried about X. Show the worry is aimed at the wrong thing.

**B — Quote + extend.** Pull the sharpest line OP wrote. Name why it's the real insight. Add one thing they missed.

**C — Correct + land.** Fix a wrong assumption in 1-2 sentences. End with something quotable.

**D — Stop, do this instead.** OP is doing the wrong thing. Direct, no softening. Confident statement at the end.

**E — Name the feeling.** One sentence that says what everyone in the thread is thinking but didn't say.

**F — Systemic diagnosis.** Don't answer OP's question. Name the structural pattern above it. Write for the lurkers, not OP.

---

## Thread selection

From `/new.json` only. Under 24h old. At least 2 comments already.

Prioritise:
1. Frustrated OP + jaded sub (r/ExperiencedDevs, r/startups) — highest upvote yield
2. Frustrated OP + any builder sub
3. Neutral question + experienced audience
4. Skip: beginner questions with obvious answers, hostile threads, 0-comment threads

Sub pool: r/webdev, r/SideProject, r/indiehackers, r/buildinpublic, r/startups, r/Entrepreneur, r/SaaS, r/programming, r/learnprogramming, r/ExperiencedDevs, r/Solopreneur, r/GrowthHacking, r/micro_saas, r/MicroSaas, r/scaleinpublic, r/vibecoding, r/AppIdeas, r/indiebiz, r/EntrepreneurRideAlong, r/juststart, r/passive_income, r/productivity, r/growmybusiness, r/Startup_Ideas, r/Business_Ideas, r/AlphaandBetaUsers

Span at least 2 different subreddits per batch.

---

## Output format

```
--- REDDIT DAILY 5 — [DATE] ---

SLOT 1
Sub: r/[sub]
Thread: [title]
URL: [link]
Pattern: [A/B/C/D/E/F] | Top comment style observed: [one line]

[comment]

---
```

Append all 5 URLs to `reddit-used-posts.md` after each run.
