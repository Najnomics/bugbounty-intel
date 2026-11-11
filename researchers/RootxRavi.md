# @RootxRavi — Ravindra Lakhara

- X: [https://x.com/RootxRavi](https://x.com/RootxRavi) (id `1578337507355131904`, created 7 Oct 2022)
- Bio (Nov 2026): BSCP, CREST CPSA & CRT, OSCP, CRTA, CRTP, eJPT, eCPPTv2, eWPTX, eMAPT; Yogosha 20; Bugcrowd 100; open for freelance
- Bugcrowd: [bugcrowd.com/RootxRavi](https://bugcrowd.com/RootxRavi)
- Platforms: Bugcrowd (longer track record), HackerOne (started more visibly in Aug 2026)
- Focus: Web application hunting; frequently collaborates with [@krishnsec](krishnsec.md)
- Location listed: India

No public technical writeup for the 2026 payouts was found in this pass. His posts are still useful as **consistency evidence** and as a collaboration pattern (pair hunting with krishnsec).

## Findings / payout claims (details mostly undisclosed)

### Shared Bugcrowd P1, "in 30 seconds" — $10,000

- **Platform:** Bugcrowd
- **Severity:** P1 (author)
- **Bounty:** $10,000, shared with @krishnsec
- **Bug class / root cause / method:** Undisclosed. The "30 seconds" line is a hook; no recon or bug-class detail was in the post.
- **Takeaway:** High-severity bugs are sometimes obvious once you are already deep in a target, but this post cannot be used as a technique guide.
- **Source:** 25 Oct 2026 15:49 WAT — [post](https://x.com/RootxRavi/status/2114368791408947313)

### Other 2026 bounty posts (no technical detail)

- $10,250 HackerOne — 31 Oct 2026 11:28 WAT — [post](https://x.com/RootxRavi/status/2116477287554232616)
- $1,500 HackerOne, thanks @HarshDRanjan1 — 6 Oct 2026 16:23 WAT — [post](https://x.com/RootxRavi/status/2107491994331423053)
- $4,500 HackerOne — 14 Aug 2026 15:31 WAT — [post](https://x.com/RootxRavi/status/2088272412072902705)
- $1,500 HackerOne — 13 Aug 2026 16:18 WAT — [post](https://x.com/RootxRavi/status/2087876415006085516)
- $2,500 HackerOne, "recently started hunting on HackerOne" — 10 Aug 2026 16:26 WAT — [post](https://x.com/RootxRavi/status/2086836477095469280)

## Consistency / workflow notes

- **5 Aug 2026:** Posted that he made Bugcrowd Top 100 after "thousands of hours of manual testing," treating duplicates and informatives as part of the path. [post](https://x.com/RootxRavi/status/2084992157388345591)
- **1 Aug 2026:** #4 on Bugcrowd India leaderboard for July. [post](https://x.com/RootxRavi/status/2083510058093326602)
- **1 Jul 2026:** #2 on Bugcrowd India leaderboard for June, "while balancing a full-time job." [post](https://x.com/RootxRavi/status/2072261644709986608)
- **16 Jun 2026:** Mentioned a hunting laptop setup of Burp Suite, Claude Code, Docker, browsers, and recon tools (16GB M2 Pro struggling). Tool list only — not a finding. [post](https://x.com/RootxRavi/status/2066959135414055188)

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 1 finding(s). Full verbatim posts under `posts/RootxRavi/`._

- **IDOR on forgot-password → mass username/email enumeration (3-digit bounty)** (`idor-bola`)
  - post: https://x.com/RootxRavi/status/1592807918428037122
  - local: `posts/RootxRavi/ARCHIVE.md`, `data/x_posts.jsonl`
  - bounty: 3-digit
