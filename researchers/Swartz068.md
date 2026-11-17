# @Swartz068 — Swartz (Rajcyber068)

- X: [https://x.com/Swartz068](https://x.com/Swartz068) (id `1787485777259040768`, created 6 May 2024)
- Bio (Nov 2026): Security researcher; Top 4K @Bugcrowd; Hall of Fame: NASA, EPA, Linktree, Zola & Kohl’s + more; Security intern @HubC3i, IIT Kanpur
- Platforms: Bugcrowd (primary), mentions HackerOne; also talks about VDP / government HoF
- Focus: Web recon, historical JS / JWT leftovers, wildcard-domain programs, manual testing

He posts fewer payout screenshots than some seed hunters, but he posts **reusable tips** and is a clear example of staying on one target.

## Methodology (not a single named CVE)

### Tip: historical JavaScript in the Wayback Machine

- **Claim:** Config/env/app JS snapshots from different years can still contain secrets even when the live file does not.
- **Method (as stated):** Collect historical URLs from the Wayback Machine; look for files such as `config.js`, `env.js`, `app.js`; compare snapshots across years (he listed 2021, 2022, 2024, 2025).
- **Takeaways:** Secret rotation is uneven. Archived frontend bundles are part of recon, not only the live tree.
- **Source:** 4 Nov 2026 11:44 WAT — [post](https://x.com/Swartz068/status/2117931096726016043)

### Tip: JWTs sitting in archived URLs (described as an "easy P3/P2")

- **Claim:** Wayback URL lists sometimes include JWTs that decode to email, name, user id, roles, or other PII.
- **Method (as stated):** Fetch Wayback URLs, search the corpus for JWT-shaped strings (he mentioned filtering for the common `eyJ` prefix), decode at jwt.io, look for PII or role claims.
- **Takeaways:** Treat historical URL dumps as a credential and PII mine, not only as a path wordlist. Confirm the token is still meaningful before reporting; a dead token may be informative only.
- **Source:** 2 Nov 2026 11:30 WAT — [post](https://x.com/Swartz068/status/2117202589918114241)

## Consistency evidence

- **15 Oct 2026 14:42 WAT:** "11 reports triaged on the same target on @Bugcrowd." Advice: "be loyal to your target… invest your time in the right targets." [post](https://x.com/Swartz068/status/2110728116180226209)
- **8 Oct 2026 22:23 WAT:** 10 reports triaged on a single Bugcrowd program; goal of 25 valid on that program. [post](https://x.com/Swartz068/status/2108307317322379620)
- **29 Sep 2026 12:17 WAT:** 3 triaged that day; 10 successful triages total, 9 of them on a single program. [post](https://x.com/Swartz068/status/2104893407655305597)
- **10 Sep 2026:** One more Bugcrowd triage. [post](https://x.com/Swartz068/status/2098076274497626251)
- **24 Aug 2026:** 2× duplicate on Bugcrowd (hashtag `#idor` — not enough to document an IDOR finding). [post](https://x.com/Swartz068/status/2091854507970081180)
- **31 Oct 2026:** A Bugcrowd report upgraded P3 to P2. Details undisclosed. [post](https://x.com/Swartz068/status/2116525685305139421)
- **2 Nov 2026:** $100 Bugcrowd submission. Details undisclosed. [post](https://x.com/Swartz068/status/2117294264254435641)

## Other workflow comments

- **16 Oct 2026:** "I always choose wild card domain program." [post](https://x.com/Swartz068/status/2110996965148266599)
- **15 Oct 2026:** In the "era of AI & automation" he said he is focusing on manual testing and studying new attacks, and that this particular work paid $0 so far. [post](https://x.com/Swartz068/status/2110784539757015170)
- **20 Oct 2026:** Complained that a Meta Bug Bounty report had been pending 6+ months with only pre-triage. That is a process note, not a finding. [post](https://x.com/Swartz068/status/2112591482884628659)

## Daily update 2026-11-16

### Wayback URL grep for IDOR candidates (2026-11-15)

- Post: https://x.com/Swartz068/status/2121944192893264156 — verbatim: [`posts/Swartz068/2026-11-15-2121944192893264156.md`](../posts/Swartz068/2026-11-15-2121944192893264156.md)
- **Bug class:** IDOR recon
- **Root cause:** N/A (tip)
- **How it was found:** Wayback URLs → urls.txt → `grep -E '/user|/order|/id'`.
- **Takeaways / harness:** waybackurls/gau → regex for object-ID paths → replay with second account (Autorize-style).

## Daily update 2026-11-17

### Mercedes-Benz valid Bugcrowd submission (2026-11-16) (2026-11-16)

- Post: https://x.com/Swartz068/status/2122306655132270666 — verbatim: [`posts/Swartz068/2026-11-16-2122306655132270666.md`](../posts/Swartz068/2026-11-16-2122306655132270666.md)
- **Bug class:** Undisclosed (asset path under `/Account/`)
- **Root cause:** Undisclosed.
- **How it was found:** Undisclosed.
- **Takeaways / harness:** Bounty-only evidence: "accepted as a valid issue" on a mercedes-benz.com account path.

