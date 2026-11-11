# @krishnsec — Kanhaiya Sharma

- X: [https://x.com/krishnsec](https://x.com/krishnsec) (id `1367090101981913090`, created 3 Mar 2021)
- Bio (Nov 2026): Ethical hacker; globally Top 3 P1 warriors on Bugcrowd; HackerOne verified Clear hacker
- Profiles: [bugcrowd.com/krishnsec](http://bugcrowd.com/krishnsec), [hackerone.com/krishnsec_](http://hackerone.com/krishnsec_)
- Platforms: Bugcrowd (primary public identity), HackerOne
- Focus: High-severity web / API bugs; at least one public 2026 note on AI application security (model extraction)

One of the most consistent Bugcrowd hunters in the seed set. Most payout posts still omit bug details. The few class names he does drop are worth filing.

## Findings

### 1. Shared Bugcrowd P1 with RootxRavi — $10,000

See [RootxRavi](RootxRavi.md). Technical details undisclosed. He replied to the announcement ("Hakuna matata") on 25 Oct 2026. [RootxRavi's post](https://x.com/RootxRavi/status/2114368791408947313)

### 2. P1 — AI model extraction via API query-based reconstruction

- **Title:** As stated in the post: "P1 - AI Application Security > Model Extraction > API Query-Based Model Reconstruction"
- **Platform / program:** Undisclosed (posted without a platform tag)
- **Severity:** P1 (author)
- **Bounty:** Undisclosed
- **Bug class:** Model extraction / AI application security
- **Root cause / method:** Not explained. The post is only a taxonomy line, but it tells you he is actively looking at whether a model's weights or behavior can be reconstructed through the query API rather than through classic web bugs.
- **Takeaways:** On AI-featured programs, do not stop at prompt injection. Ask whether the inference or training API lets you extract the model (or a close copy) by querying it.
- **Source:** 1 Nov 2026 19:46 WAT — [post](https://x.com/krishnsec/status/2116965015777628269)

## Consistency evidence (no new technical detail)

- **7 Oct 2026:** 20,000 reputation on Bugcrowd. [post](https://x.com/krishnsec/status/2107784924162093528)
- **5 Oct 2026:** #1 on the Bugcrowd leaderboard for September. [post](https://x.com/krishnsec/status/2106984299560124675)
- **21 Sep 2026:** Crossed 19k Bugcrowd reputation. [post](https://x.com/krishnsec/status/2102006855241482637)
- **17 Sep 2026:** #1 on Bugcrowd for August; "some old pending bugs finally got resolved." [post](https://x.com/krishnsec/status/2100479403478417659)
- **16 Sep 2026:** Top 3 P1 warrior globally on Bugcrowd; "consistency beats noise." [post](https://x.com/krishnsec/status/2100141425983881443)
- **18 Aug 2026:** 18k Bugcrowd reputation. [post](https://x.com/krishnsec/status/2089703314653089816)
- **13 Aug 2026:** Top 15 all-time on Bugcrowd. [post](https://x.com/krishnsec/status/2087905595471139144)

## Workflow comments worth keeping

- **13 Oct 2026:** "My accuracy over the last 90 days is 69%, so even though I can report as many bugs as I want, I'm still choosing to report only a few." Signal/accuracy over volume. [post](https://x.com/krishnsec/status/2109886780657029303)
- **25 Oct 2026:** "4.6 can still find P1 criticals — it's all about the harness." Implied: model quality matters less than how you wrap the model for hunting. [post](https://x.com/krishnsec/status/2114270259687661611)
- **15 Aug 2026:** Finding one bug is not the whole skill; real bounty knowledge is understanding why it exists, validating impact, chaining, spotting edge cases, and knowing when AI is hallucinating. [post](https://x.com/krishnsec/status/2088675304198078711)
- **21 Aug 2026:** Mentioned some programs paying 4x bonus for P1/P2. [post](https://x.com/krishnsec/status/2090784263096680870)
