# @GuplerSaxanoid — full verbatim X archive (security-relevant posts)

_Generated 2026-11-15 from the X API (full-archive search + timeline). Every post below is copied word-for-word; t.co links are expanded; quoted posts are inlined in full; media are listed with alt text when the author provided it. Posts are grouped by conversation (a thread = the author's root post followed by their own replies, oldest first). Groups are newest first. An agent without X access can rely on this file._

- Posts in this file: 8
- Conversations/threads: 6
- Oldest post captured: 2026-11-01
- Newest post captured: 2026-11-04


---

## 2026-11-04 · Post · Cross-model review still paid off for us on one thing: code that looks protected.


Tags (automatic): AI-assisted hunting


### Post — @GuplerSaxanoid — 2026-11-04 14:01 UTC (2026-11-04 15:01 WAT)

- URL: https://x.com/GuplerSaxanoid/status/2117980508307300748
- Metrics (at fetch): bookmark 0, impression 36, like 1, quote 0, reply 0, retweet 0

> Cross-model review still paid off for us on one thing: code that looks protected.
>
> Two Opus review agents found guards in our bug-hunting pipeline that failed open. One matched against a term table nobody had filled. Empty table, everything passes.
>
> That's where review still https://twitter.com/garrytan/status/2117661001332240434

**Links in post:** https://twitter.com/garrytan/status/2117661001332240434

**Quoted post** 2117661001332240434: not readable via the API (deleted, private, or withheld).


---

## 2026-11-04 · Thread · Two of our agent tools had high failure rates. Same metric, opposite meanings.


Tags (automatic): AI-assisted hunting


### Post — @GuplerSaxanoid — 2026-11-04 14:00 UTC (2026-11-04 15:00 WAT)

- URL: https://x.com/GuplerSaxanoid/status/2117980343739568375
- Metrics (at fetch): bookmark 0, impression 30, like 2, quote 0, reply 1, retweet 0

> Two of our agent tools had high failure rates. Same metric, opposite meanings.
>
> One was a guardrail doing its job. The other was a broken tool eating our exploit runs. 🧵


### Thread part 2 — @GuplerSaxanoid — 2026-11-04 14:00 UTC (2026-11-04 15:00 WAT)

- URL: https://x.com/GuplerSaxanoid/status/2117980346231017555
- Metrics (at fetch): bookmark 0, impression 6, like 0, quote 0, reply 1, retweet 0

> Our file-search tool failed on about 1 call in 7.
>
> Looked like a bug. It wasn't. Nearly every failure was a permission denial. The agents were hitting policy, which is what policy is for.


### Thread part 3 — @GuplerSaxanoid — 2026-11-04 14:00 UTC (2026-11-04 15:00 WAT)

- URL: https://x.com/GuplerSaxanoid/status/2117980348311363596
- Metrics (at fetch): bookmark 0, impression 5, like 0, quote 0, reply 1, retweet 0

> The test-network tool our exploit-writing agents use failed on more than 4 calls in 5.
>
> Almost none were denials. They were real errors. The tool, not the agents, was burning most of our PoC attempts.


---

## 2026-11-03 · Post · As models find more bugs, the hard part shifts to which findings you keep.


Tags (automatic): AI-assisted hunting


### Post — @GuplerSaxanoid — 2026-11-03 07:54 UTC (2026-11-03 08:54 WAT)

- URL: https://x.com/GuplerSaxanoid/status/2117525709430423997
- Metrics (at fetch): bookmark 0, impression 145, like 2, quote 0, reply 0, retweet 0

> As models find more bugs, the hard part shifts to which findings you keep.
>
> We tried 3 ways to make our detection agent report only bugs with a confirmed-live entry point. All 3 got reverted.
>
> The gate threw out real findings along with the noise. https://twitter.com/OpenAI/status/2117444048227123277

**Links in post:** https://twitter.com/OpenAI/status/2117444048227123277

**Quoted post** 2117444048227123277: not readable via the API (deleted, private, or withheld).


---

## 2026-11-02 · Post · LLMs are digging up bugs in decades-old Postgres code.


Tags (automatic): AI-assisted hunting


### Post — @GuplerSaxanoid — 2026-11-02 16:13 UTC (2026-11-02 17:13 WAT)

- URL: https://x.com/GuplerSaxanoid/status/2117289097970807109
- Metrics (at fetch): bookmark 0, impression 44, like 0, quote 0, reply 0, retweet 0

> LLMs are digging up bugs in decades-old Postgres code.
>
> The flip side in node security: across 100+ fresh disclosures, the median age of the vulnerable code was under two months. Most were mismatches between parts written separately.
>
> Old code hides bugs. New code makes them. https://twitter.com/lenny_enderle/status/2117177534039134253

**Links in post:** https://twitter.com/lenny_enderle/status/2117177534039134253

**Quoted post** 2117177534039134253: not readable via the API (deleted, private, or withheld).


---

## 2026-11-02 · Post · AI agents read a codebase in the order you list it. Put the critical file last and a bigger budget j


Tags (automatic): AI-assisted hunting


### Post — @GuplerSaxanoid — 2026-11-02 04:12 UTC (2026-11-02 05:12 WAT)

- URL: https://x.com/GuplerSaxanoid/status/2117107493667238239
- Metrics (at fetch): bookmark 0, impression 26, like 0, quote 0, reply 0, retweet 0

> AI agents read a codebase in the order you list it. Put the critical file last and a bigger budget just buys a longer read of the wrong files. Scope order is part of the prompt.


---

## 2026-11-01 · Post · Our best AI-audit prompt change wasn't a checklist. It was one sentence about who wrote the code: ev


Tags (automatic): AI-assisted hunting


### Post — @GuplerSaxanoid — 2026-11-01 16:56 UTC (2026-11-01 17:56 WAT)

- URL: https://x.com/GuplerSaxanoid/status/2116937486647853140
- Metrics (at fetch): bookmark 0, impression 36, like 1, quote 0, reply 0, retweet 0

> Our best AI-audit prompt change wasn't a checklist. It was one sentence about who wrote the code: everything the untrusted side exports is attacker-written, even the small helpers.
