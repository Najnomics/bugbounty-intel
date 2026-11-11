# @naresh_1337 — Naresh Kandula

- X: [https://x.com/naresh_1337](https://x.com/naresh_1337) (id `2027589186451345412`, created 28 Feb 2026)
- Bio (Nov 2026): Building SPECTRE, "autonomous AI for offensive security"; hunting Web3, AI, APIs & web apps; "CVEs • Bug Bounties • Research"
- Immunefi: [Naresh_Kandula](https://immunefi.com/profile/Naresh_Kandula/) — member since 11 Sep 2025; all-time rank 148th; total earnings $35,538 (profile fetched 11 Nov 2026). The public report-count markup was messy; prefer the numbers he and Immunefi stated in posts, below.
- YesWeHack: [nottiboy-1337](https://yeswehack.com/hunters/nottiboy-1337)
- Platforms: Immunefi, YesWeHack (also mentioned HackerOne in a career-advice reply)
- Focus: Smart contracts; at least one web OS command-injection critical

## Findings with some technical detail

### 1. Quantus Audit Competition — critical account-bypass / guardian bypass (Most Valuable Finding)

- **Platform / program:** Quantus Audit Competition, recognized with Immunefi (@QuantusNetwork)
- **Severity:** Critical (author)
- **Bounty / prize:** Undisclosed; selected as **Most Valuable Finding** of the competition
- **Bug class:** Account bypass / authorization bypass on a "guardian" or advanced-account model
- **Root cause (as stated):** A "critical account-bypass path capable of draining almost the entire account balance in a single block." In a later reply he added that "the whole point of that guardian model is surviving key compromise, so finding a bypass there was especially interesting."
- **How found / PoC:** Not published.
- **Takeaways:** On account-abstraction, social recovery, or "guardian" designs, the interesting bug is often a path that still drains funds after the user has supposedly revoked or constrained a key. Also test whether the drain can complete in a single block (no practical reaction window).
- **Sources:** 23 Sep 2026 20:20 WAT [MVF post](https://x.com/naresh_1337/status/2102840461430005790); 24 Sep 2026 reply about the guardian model [post](https://x.com/naresh_1337/status/2103196335851614609)

### 2. OS command injection on YesWeHack — critical, paid

- **Platform:** YesWeHack
- **Severity:** Critical (author); CWE-78
- **Bounty:** Amount undisclosed ("just got a reward")
- **Bug class:** OS command injection
- **Root cause / method:** Not published.
- **Takeaways:** He is not only a Solidity hunter; classic injection still pays on Web2/Web3-adjacent programs.
- **Source:** 19 Aug 2026 19:16 WAT — [post](https://x.com/naresh_1337/status/2090140871182242262)

## Other Immunefi consistency

- **26 Oct 2026:** Immunefi announced $25,000 for a critical smart-contract bug; #26 on the 90-day leaderboard; "8 critical findings and 2 highs across 12 reports." [Immunefi post](https://x.com/immunefi/status/2114677302378565786). He echoed "8 criticals, 2 highs" the same day. [post](https://x.com/naresh_1337/status/2114804871002194359)
- **21 Oct 2026:** Another confirmed Immunefi **critical**. [post](https://x.com/naresh_1337/status/2112901217278214612)
- **24 Aug 2026:** A confirmed Immunefi finding (audit-competition card); "reported as critical but landed medium." [post](https://x.com/naresh_1337/status/2091908429119983811)

Profile earnings ($35,538 on 11 Nov 2026) and the "12 reports / 8 criticals" snapshot should be read as time-bounded public claims, not a fully reconciled ledger.
