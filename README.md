# Bug bounty intel

A personal knowledge base of **publicly claimed, valid (or triaged) bug-bounty findings** by consistent security researchers, compiled for Dorothy's hunting workflow.

Last updated: **11 November 2026** (Africa/Lagos).

This is not a complete map of X, and it is not a hall-of-fame ranking. It starts from a verified seed list, then adds researchers who show **multiple** valid finds on HackerOne, Bugcrowd, Immunefi, or HackenProof (or closely related contest/audit work that sits alongside bounty hunting). Technical detail is taken only from public posts and writeups. Amounts, names, and bug classes that were not stated in a public source are marked **undisclosed**.

**How to use this.** Prefer `techniques.md` when you are mid-hunt and want patterns to try. Use `researchers/<handle>.md` when you want the story and sources behind one person. Revisit researcher feeds regularly; many of the best notes here came from long X posts or blogs, not from a one-line bounty screenshot.

## Important limits

- Public bounty screenshots and payout posts are **claims**, not independent payment confirmation, unless a platform or vendor also said so.
- One seed post was explicitly labeled edited/fake by its author; that is called out in the researcher file.
- This repo records **high-level root causes, methodology, and workflow takeaways**. It does not copy exploit requests, payloads, or reproduction procedures. When a writeup disclosed a PoC, the source link is the place to read it.
- A "triaged" report is not the same as a paid, confirmed vulnerability.

## How files are organized

| File | Contents |
| --- | --- |
| [researchers.md](researchers.md) | Index table: handle, name, platforms, focus, consistency evidence, blogs |
| [researchers/](researchers/) | One file per researcher, with profile notes and findings |
| [techniques.md](techniques.md) | Cross-cutting methodology and bug patterns, each tip linked to its source |
| [sources-log.md](sources-log.md) | Every post and URL consulted, with dates |

Post timestamps in these files are converted from UTC to **Africa/Lagos (WAT, UTC+1)**.

## Researchers

### Seed list

- [Assass1nmarcos](researchers/Assass1nmarcos.md) — Aditya Sharma
- [RootxRavi](researchers/RootxRavi.md) — Ravindra Lakhara
- [krishnsec](researchers/krishnsec.md) — Kanhaiya Sharma
- [Suryesh_92](researchers/Suryesh_92.md) — Dhananjay Kumar Suryesh
- [SuyashS91823422](researchers/SuyashS91823422.md) — Suyash Sharma
- [Swartz068](researchers/Swartz068.md) — Swartz (Rajcyber068)
- [iguardz](researchers/iguardz.md) — IGUARDZ (X account is silent; evidence is from Immunefi)
- [bluethroat_labs](researchers/bluethroat_labs.md) — Bluethroat Labs (Rahul Saxena / GuyPhy)
- [Kiki_developer](researchers/Kiki_developer.md) — Kiki
- [Piki_eth](researchers/Piki_eth.md) — Piki
- [infinitelogins](researchers/infinitelogins.md) — Harley Kimball

### Added after further X / web research

- [0xvivekd](researchers/0xvivekd.md) — Vivek
- [naresh_1337](researchers/naresh_1337.md) — Naresh Kandula
- [lonelysloth_sec](researchers/lonelysloth_sec.md) — LonelySloth
- [al_f4lc0n](researchers/al_f4lc0n.md) — f4lc0n
- [KeiZo_Zo](researchers/KeiZo_Zo.md) — Keizo
- [csanuragjain](researchers/csanuragjain.md) — Anurag Jain
- [brandon_shi](researchers/brandon_shi.md) — BRDNS
- [GuplerSaxanoid](researchers/GuplerSaxanoid.md) — GuplerSaxanoid

## Suggested watch list

For ongoing monitoring (newest posts first), these accounts currently produce the most useful public technical notes:

1. [@infinitelogins](https://x.com/infinitelogins) — own writeups plus the weekly [Disclosed](https://getdisclosed.com) roundup
2. [@bluethroat_labs](https://x.com/bluethroat_labs) and [@saxenism](https://x.com/saxenism) — TEE / consensus findings
3. [@Suryesh_92](https://x.com/Suryesh_92) and [hackwithsuryesh Medium](https://hackwithsuryesh.medium.com/) — thick-client and web writeups
4. [@Swartz068](https://x.com/Swartz068) — short, practical recon tips
5. [@krishnsec](https://x.com/krishnsec) / [@RootxRavi](https://x.com/RootxRavi) — Bugcrowd consistency, occasional bug-class hints
6. Immunefi official posts ([@immunefi](https://x.com/immunefi)) for paid-researcher shoutouts
7. [@Piki_eth](https://x.com/Piki_eth) — HackenProof triage notes, sometimes a bug class
8. [@Kiki_developer](https://x.com/Kiki_developer) and [github.com/devNamedKiki/Audits](https://github.com/devNamedKiki/Audits)

## Coverage notes

X search cannot cover "the whole of X" in one pass. Many elite hunters never post technical detail, only payout screenshots. Several of the most useful writeups live on Medium, personal sites, GitHub, or vendor advisories rather than on X.
