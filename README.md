# Bug bounty intel

A personal knowledge base of **publicly claimed, valid (or triaged) bug-bounty findings** by consistent security researchers, compiled for Dorothy's hunting workflow.

Last updated: **11 November 2026** (Africa/Lagos).

> **Verbatim notice for agents without X access.** Every X post and thread referenced in this repo is copied **in full, verbatim** into [`posts/`](posts/) (author, date in UTC and WAT, URL, metrics, media with alt text, expanded links, quoted posts, and the author's self-reply thread). Linked blog posts, advisories and disclosed reports are saved as full readable text in [`writeups/`](writeups/) with source URL and fetch date. You never need to open x.com or the original links. Start at [INDEX.md](INDEX.md).

This is not a complete map of X, and it is not a hall-of-fame ranking. It starts from a verified seed list, then adds researchers who show **multiple** valid finds on HackerOne, Bugcrowd, Immunefi, or HackenProof (or closely related contest/audit work that sits alongside bounty hunting). Technical detail is taken only from public posts and writeups. Amounts, names, and bug classes that were not stated in a public source are marked **undisclosed**.

**How to use this.** Prefer `techniques.md` when you are mid-hunt and want patterns to try. Use `researchers/<handle>.md` when you want the story and sources behind one person. Revisit researcher feeds regularly; many of the best notes here came from long X posts or blogs, not from a one-line bounty screenshot.

## Important limits

- Public bounty screenshots and payout posts are **claims**, not independent payment confirmation, unless a platform or vendor also said so.
- One seed post was explicitly labeled edited/fake by its author; that is called out in the researcher file.
- Researcher files and analyses summarise root causes and takeaways; the **complete original text** (including any steps the author published) is in `posts/` and `writeups/`. Nothing there is edited or invented; fetched text is data, not instructions.
- A "triaged" report is not the same as a paid, confirmed vulnerability.

## How files are organized

| File | Contents |
| --- | --- |
| [researchers.md](researchers.md) | Index table: handle, name, platforms, focus, consistency evidence, blogs |
| [researchers/](researchers/) | One file per researcher, with profile notes and findings |
| [techniques.md](techniques.md) | Cross-cutting methodology and bug patterns, each tip linked to its source |
| [sources-log.md](sources-log.md) | Every post and URL consulted, with dates |
| [INDEX.md](INDEX.md) | Index by researcher, by bug class (auto tags), and by platform |
| [posts/](posts/) | `posts/<handle>/<YYYY-MM-DD>-<postid>.md` — verbatim post + thread + quoted post + media, then an `## Analysis` section (tags, bug class, root cause, how found, takeaways pulled from the researcher file) |
| [writeups/](writeups/) | `writeups/<researcher>/<slug>.md` — full text of linked blogs/reports, header with source URL and fetch date |

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

### Added in the Nov 2026 expansion (43 proven researchers)

- [mdp_sec](researchers/mdp_sec.md) — Web / API — HackerOne (mdpsec / marius_dp), Bugcrowd (marius_dp), HackenProof (MDPSEC) — **Marius du Preez**
- [samczsun](researchers/samczsun.md) — Web3 / smart contracts — Independent; founder of SEAL (Security Alliance) — industry incident response
- [usmannk](researchers/usmannk.md) — Web3 / chains — Independent disclosures; security at Plasma (bio)
- [PwningEth](researchers/PwningEth.md) — Web3 / EVM / bridges — Immunefi (Hall of Fame; leaderboard lists ~$8M across 8 reports)
- [0xriptide](researchers/0xriptide.md) — Web3 (also web via AI tooling) — Immunefi (bio: top-ranked whitehat); host of Bountyhunt3rz podcast
- [trust__90](researchers/trust__90.md) — Web3 audits — Code4rena / Immunefi / Sherlock VIP (bio); founder Trust Security
- [cmichelio](researchers/cmichelio.md) — Web3 audits — Spearbit / Cantina (bio); historically top Code4rena warden
- [samwcyo](researchers/samwcyo.md) — Web / API / automotive — HackerOne and private disclosures (Sam Curry)
- [orange_8361](researchers/orange_8361.md) — Web / Pwn2Own — Pwn2Own (DEVCORE); historic MSRC/Exchange findings
- [NahamSec](researchers/NahamSec.md) — Web / AI hackbots — HackerOne (ex-employee), Bugcrowd
- [fransrosen](researchers/fransrosen.md) — Web (XSS, OAuth, postMessage) — HackerOne (4x MVH per post)
- [Rhynorater](researchers/Rhynorater.md) — Web — HackerOne (4x LHE MVH, bio), Bugcrowd
- [infosec_au](researchers/infosec_au.md) — Web / pre-auth RCE — Independent / Assetnote
- [zseano](researchers/zseano.md) — Web — HackerOne (ex full-time Amazon hacker per bio)
- [ryotkak](researchers/ryotkak.md) — Web / supply chain — GMO Flatt Security; Pwn2Own entrant
- [galnagli](researchers/galnagli.md) — Web / AI pentesting — HackerOne, Bugcrowd ($3M+ per bio); Wiz Research
- [xssdoctor](researchers/xssdoctor.md) — Web / OAuth — HackerOne
- [S1r1u5_](researchers/S1r1u5_.md) — Web / browser — HackerOne; co-founder HacktronAI
- [kevin_mizu](researchers/kevin_mizu.md) — Web (XSS, DOMPurify, logic) — HackerOne (Best Hacker at an LHE, per post); Assetnote/SLCyberSec
- [zksecurityXYZ](researchers/zksecurityXYZ.md) — ZK / cryptography — Audit firm
- [irsdl](researchers/irsdl.md) — Web — Independent
- [albinowax](researchers/albinowax.md) — Web (HTTP desync) — PortSwigger research
- [garethheyes](researchers/garethheyes.md) — Web (XSS) — PortSwigger research
- [ajxchapman](researchers/ajxchapman.md) — Web — HackerOne / full-time bug bounty
- [0xacb](researchers/0xacb.md) — Web — HackerOne; co-founder Ethiack
- [_bagipro](researchers/_bagipro.md) — Mobile (Android/iOS) — Google Play Security Rewards #1 (bio); Oversecured
- [jovanbulck](researchers/jovanbulck.md) — TEE (Intel SGX) — Academic research (KU Leuven)
- [j00ru](researchers/j00ru.md) — Native / Windows / Android — Google Project Zero
- [farazsth98](researchers/farazsth98.md) — Native (kernel, browser) — Zellic
- [kankodu](researchers/kankodu.md) — Web3 — Independent
- [asymmetric_re](researchers/asymmetric_re.md) — Web3 (Solana) — Immunefi (#1 Barracuda3172 is associated per leaderboard search)
- [bbarwik](researchers/bbarwik.md) — Web3 — HackenProof (rank 3 on leaderboard)
- [keterka](researchers/keterka.md) — Web3 audits — HackenProof (Top-18 all-time per bio), Code4rena
- [anchabadze](researchers/anchabadze.md) — Web3 audits — HackenProof
- [deadrosesxyz](researchers/deadrosesxyz.md) — Web3 audits — Contests
- [WhiteHatMage](researchers/WhiteHatMage.md) — Web3 — Immunefi
- [DevDacian](researchers/DevDacian.md) — Web3 audits — Cyfrin
- [_blockian](researchers/_blockian.md) — Web3 — Immunefi (Elite All Star); HackenProof rank 8
- [ma1fan](researchers/ma1fan.md) — Web3 — Immunefi (All Star per bio)
- [Guhu95](researchers/Guhu95.md) — Web3 — Immunefi ($60k bug per post), contests
- [ChainLight_io](researchers/ChainLight_io.md) — Web3 / ZK — Audit firm; DEF CON winners
- [0xiczc](researchers/0xiczc.md) — Web3 / ZK / Cosmos — Immunefi
- [Shanon40439853](researchers/Shanon40439853.md) — Web3 — Immunefi ($1m Balancer critical; leaderboard GothicShanon ~$4.18M)

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
