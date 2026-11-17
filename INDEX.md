# Index

Generated 11 Nov 2026 (WAT), Telegram sources added 12 Nov 2026 (Africa/Lagos). Every link points to a file inside this repo that holds **full verbatim text** — no X or Telegram access needed.

## Daily update — 17 November 2026 (Africa/Lagos)

- **X:** Full-archive search of all watched handles since the 16 Nov run. **213** new posts ingested into `store.json` / `data/x_posts.jsonl`; new security-relevant verbatim files + analysis (mdp_sec ×7: $1,500 Bugcrowd composite-key IDOR in an AI support bot, DeepSeek V4.1 Flash 13-provider benchmark + speed/solve thread, exposed llama.cpp-with-tools = RCE, Optimizely supply-chain malware/SRI note, MCP "call three", HuntDeck open-source; plus Rhynorater OAuth android-app:// ATO (quoting @rgjny_), 0xriptide Safe/Zodiac Roles $6.4M drain, pcaversaccio EIP-8037/8038 gas invariants, S1r1u5_ FBI ARTEX flash + Anthropic/OpenAI payouts, Assass1nmarcos $2,789 PII + $3,000 SSRF, Swartz068 Mercedes-Benz, NahamSec, DevDacian, immunefi $11.8M Solana). Backfill pass 6 continued: cursors n6a (DONE), n6b (DONE), n6c (OPEN), n6e (OPEN), **+905** new archive posts (ARCHIVE → 17,798).
- **Telegram:** @defendor_eng +4 (ids 2350–2353: CHAIN Polygon staking reward-checkpoint mint ~37.98M, Lighter suspected $10.4M exploit, Gnosis Safe Zodiac Roles $6.45M drain, MORE DeFi Flow EVM e-mode self-liquidation ~$308k); @dailybountywriteup +1 (id 14986). Writeups fetched today: defendor +48 backlog (0 pending); dailybounty +86 (8 new-msg, 35 retry, 43 via Medium RSS mirror) → 10,842 still pending.
- **HackerOne:** +1 disclosed — [#4199917](hackerone/reports/2026/4199917.md) curl SFTP/SCP connection reuse ignores the per-transfer host-key pin (`ssh_config_matches()` compares only key filenames; CVE-2023-27538 class). H1 inventory 12,759. `harness/findings.jsonl` +600 H1 + 9 manual entries.
- **CVE:** cvelistV5 delta since the 16 Nov cut — **396 new / 1,798 updated** (top vendors Microsoft, WordPress, Apache, Fortinet, Intel, GitLab, Samsung); total 426,270. NVD lastMod delta → 426,319. KEV unchanged. GHSA 37,810 → 37,854 (+44). OSV unchanged (23,843). ZDI stable at 17,417 (fixed stale `cve_state` count 17,361 → 17,417). Google Project Zero blog_posts corrected to 258 (excludes `0day.md`; last_post_file `2026_11_disclosure-policy.md`). Exploit-DB / kernel CNA refreshed.
- **Projects:** No new Zcash/Ethereum/Solana advisories beyond the CVE/GHSA/OSV streams. @mdp_sec site unchanged (591/150/267), still no public disclosures; H1 hacktivity 18 entries, 0 disclosed. Crypto/DeFi incidents captured via Telegram writeups (Safe/Zodiac Roles, CHAIN mint, Lighter, MORE DeFi).
- **New researchers:** +1 — [`researchers/pcaversaccio.md`](researchers/pcaversaccio.md) (Vyper core / EVM smart-contract security; gas-invariant research).
- **Harness:** new [`harness/bug-classes/2026-11-17-ai-tool-idor-oauth-scheme-roles-module.md`](harness/bug-classes/2026-11-17-ai-tool-idor-oauth-scheme-roles-module.md) (6 check-specs) with pointers from idor-bola, oauth, smart-contract, mev, crypto-primitives.
- **Failures:** thedefiant.io 403 (Safe drain writeup partial — no Wayback snapshot, jina blocked 401); OpenAI blog direct 403 (retrieved via WebFetch); some Telegram backlog fetches failed (219 cumulative defendor / 1,100 dailybounty). No invented content.

## Daily update — 16 November 2026 (Africa/Lagos)

- New X posts (with analysis): [mdp_sec MCP bearer-presence auth bypass $5k](posts/mdp_sec/2026-11-15-2121878367997714848.md), [mdp_sec unauthenticated file API](posts/mdp_sec/2026-11-15-2122089761938518398.md), [mdp_sec open data server (dupe)](posts/mdp_sec/2026-11-15-2122059562161487988.md), [mdp_sec perk mint logic](posts/mdp_sec/2026-11-15-2121968965266088068.md), [mdp_sec DeepSeek 0 refusals](posts/mdp_sec/2026-11-15-2121908568110628935.md), [zkSecurity Collision Atlas](posts/zksecurityXYZ/2026-11-16-2122127588986438139.md) + [writeup](writeups/zksecurityXYZ/collision-atlas-2026-11-16.md), [naresh_1337 Immunefi High](posts/naresh_1337/2026-11-16-2122192059536699603.md), [Neodyme](posts/Neodyme/2026-11-15-2121941626822004761.md). 112 new watched-account posts; backfill +605.
- Telegram: @defendor_eng +4 ([archive](telegram/defendor_eng/ARCHIVE-2026-02071-02349.md); Proxima SigNoz key leak [writeup](writeups/telegram-defendor_eng/proxima-post-mortem-signoz-leaked-private-keys.md)); @dailybountywriteup +1. Writeups: defendor +74 (246 total, 77 pending); dailybounty +168 (933 total, 10,842 pending; 76 via Medium RSS).
- HackerOne +3: [Arc RPC JS-tracer DoS #3966160](hackerone/reports/2026/3966160.md), [Weblate XFF rate-limit bypass #4059744](hackerone/reports/2026/4059744.md), [Weblate suggestion IP exposure #4117330](hackerone/reports/2026/4117330.md).
- CVE cvelistV5 +106 / 15 upd; NVD +110 / 11; OSV +42; ZDI +56; P0 +1; KEV/GHSA unchanged.
- Harness: [2026-11-16 bug-class checks](harness/bug-classes/2026-11-16-mcp-open-data-rpc-tracer-logs.md); [techniques.md 2026-11-16 additions](techniques.md).

## Daily update — 15 November 2026 (Africa/Lagos)

- New X posts (security-relevant, with analysis): [mdp_sec guest-upload RCE](posts/mdp_sec/2026-11-14-2121727373498257576.md), [mdp_sec widget-config stored XSS](posts/mdp_sec/2026-11-14-2121606577698308308.md), [mdp_sec sequential-IDOR SSN (Critical dupe)](posts/mdp_sec/2026-11-14-2121546179360276882.md), [mdp_sec mobile hardcoded key → prod private key](posts/mdp_sec/2026-11-14-2121515980211785729.md), [mdp_sec AI harness zero-steering](posts/mdp_sec/2026-11-15-2121817970381094966.md), [kobigurk harness skeuomorphism](posts/kobigurk/2026-11-15-2121784321799598543.md), [zkSecurity newsletter](posts/zksecurityXYZ/2026-11-14-2121564859724648754.md) + [writeup](writeups/zksecurityXYZ/newsletter-2026-11-14.md). 93 new watched-account posts captured into `data/x_posts.jsonl` / ARCHIVEs.
- Telegram: @defendor_eng +4 (Pool Party $215K, Centrifuge V3.3, …); @dailybountywriteup +1. Writeups fetched this run: defendor +62 (total 172), dailybounty +167 (total 765); pending 263 / 11,239.
- HackerOne +1: [Weblate #4081135 critical backup-import priv-esc](hackerone/reports/2026/4081135.md).
- CVE cvelistV5 +75 new / 24 updated; KEV unchanged; GHSA reviewed +0.

## Daily update — 14 November 2026 (Africa/Lagos)

- New X posts (security-relevant, with analysis): [mdp_sec $2k cross-tenant IDOR credential leak](posts/mdp_sec/2026-11-13-2121244189593940355.md), [mdp_sec harness model benchmarks](posts/mdp_sec/2026-11-13-2121358210577883544.md) + [Grok 4.7 vs 4.6](posts/mdp_sec/2026-11-13-2121274388435922971.md), [mdp_sec triage telemetry](posts/mdp_sec/2026-11-13-2121213990546088318.md), [S1r1u5_ Cursor/Fireworks AI-infra breach](posts/S1r1u5_/2026-11-14-2121447753410904131.md), [S1r1u5_ Project Zero Full-X disclosure](posts/S1r1u5_/2026-11-14-2121423646539604228.md), [saxenism email .zip PoC blocked](posts/saxenism/2026-11-13-2121239127467434217.md), [saxenism L1 secure release](posts/saxenism/2026-11-13-2121167157329584138.md), [garethheyes PHP XOR-string filter bypass](posts/garethheyes/2026-11-13-2121236435273675134.md), [albinowax/zseano RCE proof-of-impact trend](posts/albinowax/2026-11-13-2121234124476183016.md), [NahamSec "Weird Ways to Hack Gemini"](posts/NahamSec/2026-11-13-2121246957616390355.md). 121 new watched-account posts captured verbatim into `posts/*/ARCHIVE*` and `data/x_posts.jsonl`.
- New writeups: [Cursor security incident update](writeups/S1r1u5_/cursor-security-incident-update-2026-11.md), [Fireworks Oct-2026 incident](writeups/S1r1u5_/fireworks-october-2026-security-incident.md) + [update](writeups/S1r1u5_/fireworks-october-2026-security-incident-update.md), [Project Zero Full-X policy](writeups/S1r1u5_/project-zero-disclosure-policy-update-2026-11.md), [asymmetric conference opsec](writeups/asymmetric_re/conference-week-opsec-a-guide.md); Telegram: [CertiK Arcus integer-overflow](writeups/telegram-defendor_eng/certik-arcus-incident-analysis.md), [Certora Sui audit guide](writeups/telegram-defendor_eng/certora-auditing-smart-contracts-sui.md), [SecurityCipher GitHub Actions wfx stealer](writeups/telegram-dailybountywriteup/securitycipher-github-actions-secret-stealer-wfx.md), +190 more (150 HackerOne reports + 40 DeFi writeups).
- HackerOne (+2): [Basecamp cross-account stored XSS → admin takeover](hackerone/reports/2026/4175245.md), [PortSwigger Burp OpenAPI $id local-file read](hackerone/reports/2026/4000535.md).
- CVEs: 736 new + 1,855 updated (cvelistV5 delta); GHSA reviewed 37,810; CISA KEV 2026.11.13 (1,781); ZDI full-text backfill complete (17,361). Projects: Ethereum +1 (erigon), crypto +2 (russh). HackerOne 12,754 total.

## Daily update — 13 November 2026 (Africa/Lagos)

- New X posts (security-relevant, with analysis): [saxenism Zcash finding #8](posts/saxenism/2026-11-12-2120829077829582959.md), [zkSecurity Monero Lean proof](posts/zksecurityXYZ/2026-11-12-2120960376791847035.md), [Trail of Bits Patch the Planet](posts/trailofbits/2026-11-12-2120943246587392210.md) + [agent patch plugins](posts/trailofbits/2026-11-12-2121009628855357931.md), [S1r1u5_ n-day/0day](posts/S1r1u5_/2026-11-12-2120761362075079124.md), [0xvivekd private bounty](posts/0xvivekd/2026-11-12-2120893385519313126.md). 64 new watched-account posts captured verbatim into `posts/*/ARCHIVE*` and `data/x_posts.jsonl`.
- New writeups: [writeups/zksecurityXYZ/monero-generalized-bulletproofs-lean-proof-2026-11.md](writeups/zksecurityXYZ/monero-generalized-bulletproofs-lean-proof-2026-11.md), [writeups/trailofbits/patch-the-planet-dashboard-2026-11.md](writeups/trailofbits/patch-the-planet-dashboard-2026-11.md), [writeups/S1r1u5_/glasswing-nday-0day-exploited-in-wild-2026-11.md](writeups/S1r1u5_/glasswing-nday-0day-exploited-in-wild-2026-11.md), [Mercado Bitcoin rekt](writeups/telegram-defendor_eng/mercado-rekt-c0939a8c.md), [wallet pentest checklist](writeups/telegram-defendor_eng/guardianaudits-crypto-wallet-pentest-2120924685890413008.md), +170 HackerOne reports under `writeups/telegram-dailybountywriteup/`.
- CVEs: 423 new + 1,970 updated (cvelistV5 delta); GHSA reviewed 37,767. HackerOne 12,752 (+2).

## Daily update — 12 November 2026 (Africa/Lagos)

New / refreshed technical material today (verbatim under `posts/` and `writeups/`):

| Topic | Local files |
| --- | --- |
| CSP form-action credential theft (no JS) | [posts/garethheyes/2026-11-11-2120523482220167240.md](posts/garethheyes/2026-11-11-2120523482220167240.md), [writeups/garethheyes/blind-trust-stealing-credentials-through-csp.md](writeups/garethheyes/blind-trust-stealing-credentials-through-csp.md) |
| SSRF signed cloud creds (no metadata IP) | [posts/mdp_sec/2026-11-11-2120519414491566209.md](posts/mdp_sec/2026-11-11-2120519414491566209.md) |
| TEE GPU fake-verified + 4-check checklist | [posts/bluethroat_labs/2026-11-11-2120528783673299290.md](posts/bluethroat_labs/2026-11-11-2120528783673299290.md), [writeups/bluethroat_labs/phala-cloud-gpu-attestation-fake-verified-no-cryptography.md](writeups/bluethroat_labs/phala-cloud-gpu-attestation-fake-verified-no-cryptography.md) |
| TEE intent binding / SGLang incident | [posts/saxenism/2026-11-11-2120538169259209027.md](posts/saxenism/2026-11-11-2120538169259209027.md), [writeups/saxenism/near-ai-sglang-security-incident-report.md](writeups/saxenism/near-ai-sglang-security-incident-report.md) |
| Codex → npm supply chain (Depi) | [writeups/Rhynorater/depi-backdooring-codex.md](writeups/Rhynorater/depi-backdooring-codex.md) |
| Solana Privacy Rings / gnark fake-GLV | [writeups/zksecurityXYZ/solana-privacy-rings-zolana-audit-2026-08.md](writeups/zksecurityXYZ/solana-privacy-rings-zolana-audit-2026-08.md) |
| Besu + Vyper GHSAs; TDX / gnark crypto | [projects/ethereum/advisories-index.md](projects/ethereum/advisories-index.md), [projects/crypto/advisories-index.md](projects/crypto/advisories-index.md) |
| Telegram intel sources (verbatim) | [telegram/defendor_eng/](telegram/defendor_eng/) (2,096 msgs, complete), [telegram/dailybountywriteup/](telegram/dailybountywriteup/) (14,969 msgs, complete) |

## CVE, advisory, exploit and HackerOne layers (added 12 Nov 2026, Africa/Lagos)

| Source | Local files | Captured / available |
| --- | --- | --- |
| CVE List V5 (all CVEs 1999–2026) | [data/cve/all/](data/cve/all/), per vendor [cves/vendors/](cves/vendors/) | 424,534 / 424,534 |
| NVD enrichment | [data/nvd/](data/nvd/) | 424,750 / 424,750 |
| CISA KEV | [cves/kev/](cves/kev/) | 1,779 / 1,779 |
| GitHub Advisory Database (reviewed) | [data/ghsa/](data/ghsa/), [cves/ghsa/](cves/ghsa/) | 37,715 / 37,715 |
| OSV.dev (non-GHSA: Android, Go, PYSEC, RustSec, OSS-Fuzz, FriendsOfPHP, Hex) | [data/osv/](data/osv/), [cves/osv/](cves/osv/) | 23,801 |
| Exploit-DB (with exploit code) | [data/exploitdb/](data/exploitdb/) | 47,182 / 47,182 |
| Linux kernel CNA (vulns.git) | [data/cve/linux-kernel-cna/](data/cve/linux-kernel-cna/), [cves/vendors/linux-kernel/](cves/vendors/linux-kernel/) | 18,563 / 18,563 |
| PHP (CVE layer + php-src advisories) | [cves/vendors/php/](cves/vendors/php/), [cves/repo-advisories/php__php-src.md](cves/repo-advisories/php__php-src.md) | 1,390 CVEs + 66 GHSA |
| Google (Chrome, Android, Google, Project Zero) | [cves/vendors/google-chrome/](cves/vendors/google-chrome/), [cves/vendors/android/](cves/vendors/android/), [cves/vendors/google/](cves/vendors/google/), [cves/google-project-zero/](cves/google-project-zero/) | P0: 258 posts, ITW sheet, RCAs |
| Zero Day Initiative | [data/zdi/](data/zdi/), [cves/zdi/](cves/zdi/) | 17,361 indexed; full text pending (see `data/cve_state.json`) |
| HackerOne Hacktivity (all disclosed) | [hackerone/](hackerone/) ([by weakness](hackerone/BY_WEAKNESS.md), [by program](hackerone/BY_PROGRAM.md), [top bounties](hackerone/TOP_BOUNTIES.md)), [data/h1/](data/h1/) | 12,750 / 12,750 |
| Bug class → best examples | [harness/cve-index.md](harness/cve-index.md) | |

How to search and the daily incremental procedure: [cves/README.md](cves/README.md), [hackerone/README.md](hackerone/README.md). State: [data/cve_state.json](data/cve_state.json), [data/h1_state.json](data/h1_state.json).

## Telegram sources

Public channels archived from `https://t.me/s/<channel>`. Full message text, links, media type and forwarded-from are stored locally. State for incremental daily updates: [`data/telegram_state.json`](data/telegram_state.json).

| Channel | Archive | Messages | IDs | Dates (WAT) | Writeups |
| --- | --- | ---: | --- | --- | --- |
| [@defendor_eng](https://t.me/defendor_eng) | [telegram/defendor_eng/](telegram/defendor_eng/) | 2,096 | 1–2334 (complete) | 2025-04-22 → 2026-11-12 | [links.md](telegram/defendor_eng/links.md); fetched copies under [writeups/telegram-defendor_eng/](writeups/telegram-defendor_eng/) |
| [@dailybountywriteup](https://t.me/dailybountywriteup) | [telegram/dailybountywriteup/](telegram/dailybountywriteup/) | 14,969 | 1–14981 (complete) | 2022-08-22 → 2026-11-12 | [links.md](telegram/dailybountywriteup/links.md) (12,879 URLs); fetched copies under [writeups/telegram-dailybountywriteup/](writeups/telegram-dailybountywriteup/) |

## By researcher

| Researcher | Profile | Posts (files) | Writeups | Specialty | Platforms |
| --- | --- | --- | --- | --- | --- |
| 0xacb | [researchers/0xacb.md](researchers/0xacb.md) | [6](posts/0xacb/) | [1](writeups/0xacb/) | Web | HackerOne; co-founder Ethiack |
| 0xiczc | [researchers/0xiczc.md](researchers/0xiczc.md) | [9](posts/0xiczc/) | [3](writeups/0xiczc/) | Web3 / ZK / Cosmos | Immunefi |
| 0xPARC | — | [1](posts/0xPARC/) | 0 | see profile (original set) | see profile |
| 0xriptide | [researchers/0xriptide.md](researchers/0xriptide.md) | [6](posts/0xriptide/) | [2](writeups/0xriptide/) | Web3 (also web via AI tooling) | Immunefi (bio: top-ranked whitehat); host of Bountyhunt3rz podcast |
| 0xteddav | — | [1](posts/0xteddav/) | 0 | see profile (original set) | see profile |
| 0xvivekd | [researchers/0xvivekd.md](researchers/0xvivekd.md) | [10](posts/0xvivekd/) | 0 | see profile (original set) | see profile |
| _bagipro | [researchers/_bagipro.md](researchers/_bagipro.md) | [15](posts/_bagipro/) | [1](writeups/_bagipro/) | Mobile (Android/iOS) | Google Play Security Rewards #1 (bio); Oversecured |
| _blockian | [researchers/_blockian.md](researchers/_blockian.md) | [6](posts/_blockian/) | 0 | Web3 | Immunefi (Elite All Star); HackenProof rank 8 |
| ajxchapman | [researchers/ajxchapman.md](researchers/ajxchapman.md) | [6](posts/ajxchapman/) | 0 | Web | HackerOne / full-time bug bounty |
| al_f4lc0n | [researchers/al_f4lc0n.md](researchers/al_f4lc0n.md) | [5](posts/al_f4lc0n/) | [1](writeups/al_f4lc0n/) | see profile (original set) | see profile |
| albinowax | [researchers/albinowax.md](researchers/albinowax.md) | [44](posts/albinowax/) | 0 | Web (HTTP desync) | PortSwigger research |
| anchabadze | [researchers/anchabadze.md](researchers/anchabadze.md) | [6](posts/anchabadze/) | 0 | Web3 audits | HackenProof |
| asanso | — | [1](posts/asanso/) | 0 | see profile (original set) | see profile |
| Assass1nmarcos | [researchers/Assass1nmarcos.md](researchers/Assass1nmarcos.md) | [10](posts/Assass1nmarcos/) | [4](writeups/Assass1nmarcos/) | see profile (original set) | see profile |
| asymmetric_re | [researchers/asymmetric_re.md](researchers/asymmetric_re.md) | [6](posts/asymmetric_re/) | 0 | Web3 (Solana) | Immunefi (#1 Barracuda3172 is associated per leaderboard search) |
| bbarwik | [researchers/bbarwik.md](researchers/bbarwik.md) | [6](posts/bbarwik/) | 0 | Web3 | HackenProof (rank 3 on leaderboard) |
| bluethroat_labs | [researchers/bluethroat_labs.md](researchers/bluethroat_labs.md) | [6](posts/bluethroat_labs/) | [3](writeups/bluethroat_labs/) | see profile (original set) | see profile |
| brandon_shi | [researchers/brandon_shi.md](researchers/brandon_shi.md) | [1](posts/brandon_shi/) | 0 | see profile (original set) | see profile |
| ChainLight_io | [researchers/ChainLight_io.md](researchers/ChainLight_io.md) | [4](posts/ChainLight_io/) | 0 | Web3 / ZK | Audit firm; DEF CON winners |
| cmichelio | [researchers/cmichelio.md](researchers/cmichelio.md) | [6](posts/cmichelio/) | 0 | Web3 audits | Spearbit / Cantina (bio); historically top Code4rena warden |
| csanuragjain | [researchers/csanuragjain.md](researchers/csanuragjain.md) | [1](posts/csanuragjain/) | 0 | see profile (original set) | see profile |
| deadrosesxyz | [researchers/deadrosesxyz.md](researchers/deadrosesxyz.md) | [4](posts/deadrosesxyz/) | 0 | Web3 audits | Contests |
| DevDacian | [researchers/DevDacian.md](researchers/DevDacian.md) | [5](posts/DevDacian/) | 0 | Web3 audits | Cyfrin |
| farazsth98 | [researchers/farazsth98.md](researchers/farazsth98.md) | [5](posts/farazsth98/) | 0 | Native (kernel, browser) | Zellic |
| fransrosen | [researchers/fransrosen.md](researchers/fransrosen.md) | [24](posts/fransrosen/) | [1](writeups/fransrosen/) | Web (XSS, OAuth, postMessage) | HackerOne (4x MVH per post) |
| galnagli | [researchers/galnagli.md](researchers/galnagli.md) | [16](posts/galnagli/) | [1](writeups/galnagli/) | Web / AI pentesting | HackerOne, Bugcrowd ($3M+ per bio); Wiz Research |
| garethheyes | [researchers/garethheyes.md](researchers/garethheyes.md) | [30](posts/garethheyes/) | [3](writeups/garethheyes/) | Web (XSS) | PortSwigger research |
| Guhu95 | [researchers/Guhu95.md](researchers/Guhu95.md) | [6](posts/Guhu95/) | 0 | Web3 | Immunefi ($60k bug per post), contests |
| GuplerSaxanoid | [researchers/GuplerSaxanoid.md](researchers/GuplerSaxanoid.md) | [1](posts/GuplerSaxanoid/) | 0 | see profile (original set) | see profile |
| iguardz | [researchers/iguardz.md](researchers/iguardz.md) | 0 | [1](writeups/iguardz/) | see profile (original set) | see profile |
| immunefi | — | [9](posts/immunefi/) | 0 | see profile (original set) | see profile |
| infinitelogins | [researchers/infinitelogins.md](researchers/infinitelogins.md) | [13](posts/infinitelogins/) | [1](writeups/infinitelogins/) | see profile (original set) | see profile |
| infosec_au | [researchers/infosec_au.md](researchers/infosec_au.md) | [26](posts/infosec_au/) | [3](writeups/infosec_au/) | Web / pre-auth RCE | Independent / Assetnote |
| irsdl | [researchers/irsdl.md](researchers/irsdl.md) | [20](posts/irsdl/) | 0 | Web | Independent |
| j00ru | [researchers/j00ru.md](researchers/j00ru.md) | [14](posts/j00ru/) | [4](writeups/j00ru/) | Native / Windows / Android | Google Project Zero |
| jovanbulck | [researchers/jovanbulck.md](researchers/jovanbulck.md) | [22](posts/jovanbulck/) | 0 | TEE (Intel SGX) | Academic research (KU Leuven) |
| kankodu | [researchers/kankodu.md](researchers/kankodu.md) | [4](posts/kankodu/) | 0 | Web3 | Independent |
| KeiZo_Zo | [researchers/KeiZo_Zo.md](researchers/KeiZo_Zo.md) | [2](posts/KeiZo_Zo/) | 0 | see profile (original set) | see profile |
| keterka | [researchers/keterka.md](researchers/keterka.md) | [6](posts/keterka/) | 0 | Web3 audits | HackenProof (Top-18 all-time per bio), Code4rena |
| kevin_mizu | [researchers/kevin_mizu.md](researchers/kevin_mizu.md) | [15](posts/kevin_mizu/) | [2](writeups/kevin_mizu/) | Web (XSS, DOMPurify, logic) | HackerOne (Best Hacker at an LHE, per post); Assetnote/SLCyberSec |
| Kiki_developer | [researchers/Kiki_developer.md](researchers/Kiki_developer.md) | [5](posts/Kiki_developer/) | [5](writeups/Kiki_developer/) | see profile (original set) | see profile |
| kobigurk | — | [1](posts/kobigurk/) | 0 | see profile (original set) | see profile |
| krishnsec | [researchers/krishnsec.md](researchers/krishnsec.md) | [13](posts/krishnsec/) | 0 | see profile (original set) | see profile |
| lavados | — | [1](posts/lavados/) | 0 | see profile (original set) | see profile |
| lonelysloth_sec | [researchers/lonelysloth_sec.md](researchers/lonelysloth_sec.md) | [28](posts/lonelysloth_sec/) | 0 | see profile (original set) | see profile |
| ma1fan | [researchers/ma1fan.md](researchers/ma1fan.md) | [6](posts/ma1fan/) | 0 | Web3 | Immunefi (All Star per bio) |
| mdp_sec **(Marius du Preez)** | [researchers/mdp_sec.md](researchers/mdp_sec.md) | [423](posts/mdp_sec/) | [6](writeups/mdp_sec/) | Web / API | HackerOne (mdpsec / marius_dp), Bugcrowd (marius_dp), HackenProof (MDPSEC) |
| NahamSec | [researchers/NahamSec.md](researchers/NahamSec.md) | [6](posts/NahamSec/) | 0 | Web / AI hackbots | HackerOne (ex-employee), Bugcrowd |
| naresh_1337 | [researchers/naresh_1337.md](researchers/naresh_1337.md) | [7](posts/naresh_1337/) | 0 | see profile (original set) | see profile |
| Neodyme | — | [1](posts/Neodyme/) | 0 | see profile (original set) | see profile |
| orange_8361 | [researchers/orange_8361.md](researchers/orange_8361.md) | [24](posts/orange_8361/) | [1](writeups/orange_8361/) | Web / Pwn2Own | Pwn2Own (DEVCORE); historic MSRC/Exchange findings |
| osec_io | — | [1](posts/osec_io/) | 0 | see profile (original set) | see profile |
| pcaversaccio | — | [1](posts/pcaversaccio/) | 0 | see profile (original set) | see profile |
| Piki_eth | [researchers/Piki_eth.md](researchers/Piki_eth.md) | [11](posts/Piki_eth/) | 0 | see profile (original set) | see profile |
| PwningEth | [researchers/PwningEth.md](researchers/PwningEth.md) | [5](posts/PwningEth/) | [1](writeups/PwningEth/) | Web3 / EVM / bridges | Immunefi (Hall of Fame; leaderboard lists ~$8M across 8 reports) |
| Rhynorater | [researchers/Rhynorater.md](researchers/Rhynorater.md) | [6](posts/Rhynorater/) | 0 | Web | HackerOne (4x LHE MVH, bio), Bugcrowd |
| RootxRavi | [researchers/RootxRavi.md](researchers/RootxRavi.md) | [11](posts/RootxRavi/) | 0 | see profile (original set) | see profile |
| ryotkak | [researchers/ryotkak.md](researchers/ryotkak.md) | [5](posts/ryotkak/) | 0 | Web / supply chain | GMO Flatt Security; Pwn2Own entrant |
| S1r1u5_ | [researchers/S1r1u5_.md](researchers/S1r1u5_.md) | [5](posts/S1r1u5_/) | 0 | Web / browser | HackerOne; co-founder HacktronAI |
| samczsun | [researchers/samczsun.md](researchers/samczsun.md) | [25](posts/samczsun/) | [4](writeups/samczsun/) | Web3 / smart contracts | Independent; founder of SEAL (Security Alliance) — industry incident response |
| samwcyo | [researchers/samwcyo.md](researchers/samwcyo.md) | [12](posts/samwcyo/) | [2](writeups/samwcyo/) | Web / API / automotive | HackerOne and private disclosures (Sam Curry) |
| saxenism | [researchers/saxenism.md](researchers/saxenism.md) | [471](posts/saxenism/) | [5](writeups/saxenism/) | TEE / ZK / protocol | Immunefi (via Bluethroat Labs); ETHSecurity |
| Shanon40439853 | [researchers/Shanon40439853.md](researchers/Shanon40439853.md) | [6](posts/Shanon40439853/) | 0 | Web3 | Immunefi ($1m Balancer critical; leaderboard GothicShanon ~$4.18M) |
| Suryesh_92 | [researchers/Suryesh_92.md](researchers/Suryesh_92.md) | [12](posts/Suryesh_92/) | [3](writeups/Suryesh_92/) | see profile (original set) | see profile |
| SuyashS91823422 | [researchers/SuyashS91823422.md](researchers/SuyashS91823422.md) | [8](posts/SuyashS91823422/) | 0 | see profile (original set) | see profile |
| Swartz068 | [researchers/Swartz068.md](researchers/Swartz068.md) | [13](posts/Swartz068/) | 0 | see profile (original set) | see profile |
| trailofbits | — | [1](posts/trailofbits/) | 0 | see profile (original set) | see profile |
| trust__90 | [researchers/trust__90.md](researchers/trust__90.md) | [6](posts/trust__90/) | 0 | Web3 audits | Code4rena / Immunefi / Sherlock VIP (bio); founder Trust Security |
| usmannk | [researchers/usmannk.md](researchers/usmannk.md) | [6](posts/usmannk/) | 0 | Web3 / chains | Independent disclosures; security at Plasma (bio) |
| WhiteHatMage | [researchers/WhiteHatMage.md](researchers/WhiteHatMage.md) | [6](posts/WhiteHatMage/) | 0 | Web3 | Immunefi |
| xssdoctor | [researchers/xssdoctor.md](researchers/xssdoctor.md) | [4](posts/xssdoctor/) | [1](writeups/xssdoctor/) | Web / OAuth | HackerOne |
| zellic_io | — | [1](posts/zellic_io/) | 0 | see profile (original set) | see profile |
| zksecurityXYZ | [researchers/zksecurityXYZ.md](researchers/zksecurityXYZ.md) | [15](posts/zksecurityXYZ/) | 0 | ZK / cryptography | Audit firm |
| zseano | [researchers/zseano.md](researchers/zseano.md) | [22](posts/zseano/) | [1](writeups/zseano/) | Web | HackerOne (ex full-time Amazon hacker per bio) |

## By bug class

Tags are automatic keyword matches on the post text (false positives possible); read the post file to confirm.

### AI-assisted hunting (248)

- [@0xacb — 2026-11-02 — This @bishopfox tool is next level! 🚀](posts/0xacb/2026-11-02-2117156243588497749.md)
- [@0xacb — 2026-11-03 — I was reading a blog on the "AI RCEssion" today, and it captures what happened during Octo](posts/0xacb/2026-11-03-2117647871285584365.md)
- [@0xriptide — 2026-10-08 — A note to those building on chain in 2026:](posts/0xriptide/2026-10-08-2107985669410947229.md)
- [@Assass1nmarcos — 2026-10-15 — Yay, I was awarded a $12,500 bounty on @Hacker0x01!](posts/Assass1nmarcos/2026-10-15-2110759502081675582.md)
- [@Assass1nmarcos — 2026-10-17 — The biggest comeback is](posts/Assass1nmarcos/2026-10-17-2111534424198451434.md)
- [@ChainLight_io — 2025-03-24 — Which rug pulls, exploits, and security breaches happened this week?](posts/ChainLight_io/2025-03-24-1904184855891771421.md)
- [@DevDacian — 2026-10-14 — All our clients are using AI &amp; various scanning services before coming to us for priva](posts/DevDacian/2026-10-14-2110334037856579752.md)
- [@DevDacian — 2026-10-19 — This week @cyfrin running 8 private audits in parallel engaging 20 top auditors!](posts/DevDacian/2026-10-19-2112147202089107746.md)
- [@Guhu95 — 2026-02-26 — Looking at a live Ethereum Mainnet bug is an unforgettable experience.](posts/Guhu95/2026-02-26-2026925805176238370.md)
- [@KeiZo_Zo — 2026-07-10 — I've been doing extensive research on AI "led" bug bounty hunting since the beginning of M](posts/KeiZo_Zo/2026-07-10-2075628283027234941.md)
- [@NahamSec — 2026-10-26 — My AI hackbot missed this $5,000 bounty. Here's how I fixed it. https://youtu.be/CRkFArW5j](posts/NahamSec/2026-10-26-2114703602505949692.md)
- [@NahamSec — 2026-11-02 — Someone found SSRF in MCP servers from Google and others. So I rebuilt the bug in a lab an](posts/NahamSec/2026-11-02-2117255416367517800.md)
- [@NahamSec — 2026-11-04 — Launched my hackbot at a new target on Bugcrowd at 11:09 and by 11:32 it had its first wor](posts/NahamSec/2026-11-04-2118067189576286345.md)
- [@Piki_eth — 2026-08-28 — My local Qwen ran for 5 hours auditing a crypto project and found a strong DoS vulnerabili](posts/Piki_eth/2026-08-28-2093217981732171978.md)
- [@Piki_eth — 2026-10-26 — Found an SSRF vulnerability using FREE DeepSeek 😂🔥](posts/Piki_eth/2026-10-26-2114761602025304105.md)
- [@Rhynorater — 2026-10-01 — Lupin and the squad are killing it in bug bounty using supply chain attacks.](posts/Rhynorater/2026-10-01-2105716901423001866.md)
- [@Rhynorater — 2026-10-08 — I just told my AI agent to write "colloquially" when it writes the report and holy crap. I](posts/Rhynorater/2026-10-08-2108216951160058341.md)
- [@RootxRavi — 2026-06-16 — Which MacBook configuration do you think is ideal for full-time bug bounty hunting in 2026](posts/RootxRavi/2026-06-16-2066959135414055188.md)
- [@S1r1u5_ — 2026-11-06 — Two crazy things happened in my life:](posts/S1r1u5_/2026-11-06-2118778782677127663.md)
- [@Swartz068 — 2026-10-15 — 11 reports triaged on the same target on @Bugcrowd.](posts/Swartz068/2026-10-15-2110728116180226209.md)
- [@Swartz068 — 2026-10-15 — @EliotGeo @Bugcrowd $0 , in Era of Ai &amp; automation I focusing on manual testing &amp;](posts/Swartz068/2026-10-15-2110784539757015170.md)
- [@Swartz068 — 2026-10-16 — @1111whiteGkep @Bugcrowd Target matter bro , I always choose wild card domain program](posts/Swartz068/2026-10-16-2110996965148266599.md)
- [@WhiteHatMage — 2026-10-13 — The AI kids doing reverse engineering and game mashups actually capture the hacker curiosi](posts/WhiteHatMage/2026-10-13-2110098233624064497.md)
- [@WhiteHatMage — 2026-10-13 — Quick thoughts on the events I missed over the past two months:](posts/WhiteHatMage/2026-10-13-2110119559600517319.md)
- [@_bagipro — 2026-04-22 — We launched Android DAST. And the first problem we hit is that login flows block everything.](posts/_bagipro/2026-04-22-2046911820452216842.md)
- [@_bagipro — 2026-07-21 — On July 28, I'll host a live webinar introducing Oversecured 2.0](posts/_bagipro/2026-07-21-2079551614327644307.md)
- [@_bagipro — 2026-09-16 — On September 24, I’m hosting a free webinar with a special guest from Vimeo where we will discu](posts/_bagipro/2026-09-16-2100241972661280995.md)
- [@_bagipro — 2026-11-03 — This Thursday, Nov 5, I'm doing a live security workshop. I'll hack a real production mobile ap](posts/_bagipro/2026-11-03-2117598779406795232.md)
- [@_blockian — 2025-12-30 — I think this might be the largest bounty so far for an AI-assisted finding.](posts/_blockian/2025-12-30-2005973018858721499.md)
- [@_blockian — 2026-07-13 — Confession time:](posts/_blockian/2026-07-13-2076742583468835023.md)
- [@al_f4lc0n — 2026-03-18 — the figures referenced in the post are entirely misleading. There was no impact realized f](posts/al_f4lc0n/2026-03-18-2034125406748741827.md)
- [@albinowax — 2026-04-28 — I just did an interview with @SecWeekly, with teasers for my upcoming #BHUSA presentation "Can](posts/albinowax/2026-04-28-2049137259559936504.md)
- [@albinowax — 2026-05-14 — AI-pentest companies get significant marketing value from publishing findings attributed to th](posts/albinowax/2026-05-14-2054980130762531104.md)
- [@albinowax — 2026-05-27 — While researching "Can AI do novel research? Meet the HTTP Terminator" I logged the discovery ](posts/albinowax/2026-05-27-2059654722097697125.md)
- [@albinowax — 2026-06-09 — Woo, I can confirm "Can AI Do Novel Security Research? Meet the HTTP Terminator" is coming to ](posts/albinowax/2026-06-09-2064357763510161664.md)
- [@albinowax — 2026-07-28 — Next week I'll present "Can AI Do Novel Security Research? Meet the HTTP Terminator" at #defco](posts/albinowax/2026-07-28-2082115108436574214.md)
- [@albinowax — 2026-07-30 — In "Can AI Do Novel Security Research?" I'll share:](posts/albinowax/2026-07-30-2082840835675025805.md)
- [@albinowax — 2026-08-05 — The whitepaper is live! Read "Can AI Do Novel Security Research? Meet the HTTP Terminator" her](posts/albinowax/2026-08-05-2085086940185960770.md)
- [@albinowax — 2026-08-07 — 90 minutes till "Can AI do novel security research? Meet the HTTP Terminator" kicks off at #DE](posts/albinowax/2026-08-07-2085780973090668604.md)
- [@albinowax — 2026-08-24 — Next month I'll present my latest research live at @SEC_T_org in Stockholm, Sweden! This will ](posts/albinowax/2026-08-24-2091831632592605359.md)
- [@albinowax — 2026-09-09 — Just about to land in Stockholm for @SEC_T_org! Can't wait to meet you all - you can catch the](posts/albinowax/2026-09-09-2097632959855522199.md)
- [@albinowax — 2026-09-15 — The HTTP Terminator will be back! I'll be presenting at @OffensiveAIcon with a streamlined AI-](posts/albinowax/2026-09-15-2099855663740412095.md)
- [@albinowax — 2026-09-22 — My latest presentation has landed on YouTube, courtesy of @SEC_T_org! Can AI do novel security](posts/albinowax/2026-09-22-2102414569163416047.md)
- [@albinowax — 2026-09-29 — It's a year since I started to build the HTTP Terminator and AI models have come a long way, b](posts/albinowax/2026-09-29-2104924480384483460.md)
- [@albinowax — 2026-10-04 — I recently spotted something sneaky &amp; unexpected about how AI approaches original hacking ](posts/albinowax/2026-10-04-2106852747157098898.md)
- [@anchabadze — 2026-10-27 — 🎯 Day 549 of my #RoadToWeb3SecurityJobChallenge](posts/anchabadze/2026-10-27-2115200664594776559.md)
- [@anchabadze — 2026-10-29 — 🎯 Day 551 of my #RoadToWeb3SecurityJobChallenge](posts/anchabadze/2026-10-29-2115946842257310068.md)
- [@anchabadze — 2026-11-03 — 🎯 Day 555 of my #RoadToWeb3SecurityJobChallenge](posts/anchabadze/2026-11-03-2117421009079067074.md)
- [@anchabadze — 2026-11-03 — 🎯 Day 556 of my #RoadToWeb3SecurityJobChallenge](posts/anchabadze/2026-11-03-2117737221226971358.md)
- [@asymmetric_re — 2026-09-22 — The @SolanaFndn just open-sourced Microscope, a free monitoring &amp; alerting tool for So](posts/asymmetric_re/2026-09-22-2102397819386745185.md)
- [@bluethroat_labs — 2026-10-01 — Bounty #9 on @immunefi is extremely special for us.](posts/bluethroat_labs/2026-10-01-2105581456550461936.md)
- [@bluethroat_labs — 2026-10-06 — Bounty #10 on @immunefi stems from the same root as #9.](posts/bluethroat_labs/2026-10-06-2107490499305124027.md)
- [@bluethroat_labs — 2026-11-07 — A major L1 offered Bluethroat Labs a $10,000 bounty for a finding where two layers disag](posts/bluethroat_labs/2026-11-07-2119050683840438658.md)
- [@cmichelio — 2026-11-04 — Today was my last day at Anthropic.](posts/cmichelio/2026-11-04-2117938732909388206.md)
- [@deadrosesxyz — 2026-07-31 — congrats to Zellic on the raise. impressive stuff.](posts/deadrosesxyz/2026-07-31-2083100523821936906.md)
- [@deadrosesxyz — 2026-08-12 — a few months ago i argued that security researchers would be some of the last people to ge](posts/deadrosesxyz/2026-08-12-2087462866207043943.md)
- [@farazsth98 — 2026-10-24 — It's crazy to think there was a time where analyzing a bugfix and writing a full exploit o](posts/farazsth98/2026-10-24-2114044534078533946.md)
- [@galnagli — 2026-09-24 — Today we're launching Scan for Good in partnership with @GoogleDeepMind.](posts/galnagli/2026-09-24-2103111505860497685.md)
- [@galnagli — 2026-10-20 — NASA had a flaw that could have allowed threat actors unauthorized access to their Mission AI H](posts/galnagli/2026-10-20-2112572671682617413.md)
- [@galnagli — 2026-10-22 — It took 17 minutes to turn the Gitlab RCE to a working HEAP exploit using Gemini 4 Argon a](posts/galnagli/2026-10-22-2113185093871095893.md)
- [@galnagli — 2026-10-22 — CVEs are nice, but organization are way more vulnerable to misconfigurations - chasing CVEs is ](posts/galnagli/2026-10-22-2113356015983030710.md)
- [@galnagli — 2026-10-31 — I'm really enjoying Gemini 4 Carbon, I always find myself asking it how it figures out its way ](posts/galnagli/2026-10-31-2116479102442234094.md)
- [@galnagli — 2026-11-10 — Gemini 4 Carbon is now publicly available - It's the world SOTA model on ExploitGym and pe](posts/galnagli/2026-11-10-2120191027525067042.md)
- [@garethheyes — 2026-10-29 — What if your agent could fuzz browsers using your templates?](posts/garethheyes/2026-10-29-2115891012648554659.md)
- [@immunefi — 2026-09-21 — Security researcher @0xvivekd has earned over $323k in the past 90 days across 16 paid rep](posts/immunefi/2026-09-21-2102010814442181024.md)
- [@infinitelogins — 2026-02-23 — Researchers at @HacktronAI found a bug in Google’s Antigravity IDE browser extension that](posts/infinitelogins/2026-02-23-2025934052759367834.md)
- [@infinitelogins — 2026-04-13 — Been a minute.](posts/infinitelogins/2026-04-13-2043552103076094169.md)
- [@infinitelogins — 2026-10-19 — PwnEscape escapes KVM in Vercel's $1M sandbox, @opencode's big week ends in a breach, @Ha](posts/infinitelogins/2026-10-19-2112170733228966180.md)
- [@infinitelogins — 2026-10-28 — I found a critical privilege escalation that took a brand new free trial account all the ](posts/infinitelogins/2026-10-28-2115429533738262954.md)
- [@infinitelogins — 2026-10-30 — If you're doing bug bounty, you should be storing your recon data in an actual database i](posts/infinitelogins/2026-10-30-2116236446147240443.md)
- [@infosec_au — 2026-06-12 —](posts/infosec_au/2026-06-12-2065233739710697756.md)
- [@infosec_au — 2026-09-26 — one of my engineers reached out to me about how they  struggled to find satisfaction in their](posts/infosec_au/2026-09-26-2103649540104745079.md)
- [@irsdl — 2026-10-14 — A friend is trying to report a valid security vulnerability to @Meta (which I've reviewed), but th](posts/irsdl/2026-10-14-2110372713529500029.md)
- [@irsdl — 2026-10-16 — Please don't give this to a robot, at least don't give it a weapon… or don't give it AI...](posts/irsdl/2026-10-16-2111029764383465570.md)
- [@irsdl — 2026-10-21 — Do you want your security finding or post to be overlooked? Then release it this week 😂](posts/irsdl/2026-10-21-2112859406182355007.md)
- [@irsdl — 2026-10-22 — Great video from @LiveOverflow 👏](posts/irsdl/2026-10-22-2113195840328094077.md)
- [@irsdl — 2026-10-22 — As promised, I've got your back! 💪 All the latest research is already in. 🚀](posts/irsdl/2026-10-22-2113236874449854969.md)
- [@irsdl — 2026-10-31 — AI did this when I was doing treat or tricking with my kid 😂 This is a nice surprise!](posts/irsdl/2026-10-31-2116668313518342257.md)
- [@irsdl — 2026-11-03 — 371 articles and counting in 2026! 🚀](posts/irsdl/2026-11-03-2117689463291977773.md)
- [@irsdl — 2026-11-04 — This feels like AI did all the research while the researcher was away, then published ever](posts/irsdl/2026-11-04-2118039406674076081.md)
- [@irsdl — 2026-11-10 — This is how my local llm model works!](posts/irsdl/2026-11-10-2120207393640398987.md)
- [@jovanbulck — 2023-08-10 — Registration still open for the 2nd Summer School on Security and Privacy in the Age of AI to](posts/jovanbulck/2023-08-10-1689436782314819584.md)
- [@keterka — 2026-04-27 — Security researchers: which AI tools impressed you the most lately? What should I test nex](posts/keterka/2026-04-27-2048580338759155952.md)
- [@keterka — 2026-05-27 — Results are in for @monetrix_xyz  on @code4rena.](posts/keterka/2026-05-27-2059434905482740185.md)
- [@kevin_mizu — 2026-04-08 — I'm happy to release the first version of my DOMLogger++ plugin for @CaidoIO! 🔎](posts/kevin_mizu/2026-04-08-2041896181744161159.md)
- [@krishnsec — 2026-08-15 — @Rishurana2867 the difference is that finding one bug isn’t the whole skill. someone with](posts/krishnsec/2026-08-15-2088675304198078711.md)
- [@krishnsec — 2026-11-01 — P1 - AI Application Security &gt; Model Extraction &gt; API Query-Based Model Reconstructi](posts/krishnsec/2026-11-01-2116965015777628269.md)
- [@lonelysloth_sec — 2026-03-08 — I was starting to get hopeful about using Claude in some capacity in my work.](posts/lonelysloth_sec/2026-03-08-2030545303607329178.md)
- [@lonelysloth_sec — 2026-06-05 — My take on the Zcash bug.](posts/lonelysloth_sec/2026-06-05-2062916729676648907.md)
- [@lonelysloth_sec — 2026-10-19 — Very similar experience.](posts/lonelysloth_sec/2026-10-19-2112289622843949366.md)
- [@lonelysloth_sec — 2026-10-23 — Says someone who never worked finding bugs.](posts/lonelysloth_sec/2026-10-23-2113674779043783132.md)
- [@lonelysloth_sec — 2026-10-23 — I have been saying for almost a year that capital intensive AI bug bounty hunting is a d](posts/lonelysloth_sec/2026-10-23-2113729242035085740.md)
- [@lonelysloth_sec — 2026-10-23 — So apparently what Altman means by “doing crazy hardware stuff beyond what we understand](posts/lonelysloth_sec/2026-10-23-2113736764158542073.md)
- [@lonelysloth_sec — 2026-10-27 — So AI refuted ETH. Boring.](posts/lonelysloth_sec/2026-10-27-2115166191669096689.md)
- [@lonelysloth_sec — 2026-11-04 — Im declaring that my dog is officially smarter than all of the world’s brightest human a](posts/lonelysloth_sec/2026-11-04-2118000301563404601.md)
- [@lonelysloth_sec — 2026-11-10 — For some reason my timeline is now full of speculation about a billionaire CEO’s love li](posts/lonelysloth_sec/2026-11-10-2119983204564427000.md)
- [@mdp_sec — 2026-07-22 — Just cancelled 2× Claude Max 20 accounts and rotated straight to 2 new SuperGrok Heavy instead](posts/mdp_sec/2026-07-22-2080070852088054104.md)
- [@mdp_sec — 2026-07-23 — Here is what your money actually buys in tokens.](posts/mdp_sec/2026-07-23-2080128823706689956.md)
- [@mdp_sec — 2026-08-06 — People keep asking me for the prompt behind my AI bug bounty system.](posts/mdp_sec/2026-08-06-2085187655101530370.md)
- [@mdp_sec — 2026-08-10 — Daybreak Red being available to individual researchers is huge.](posts/mdp_sec/2026-08-10-2086909842439197029.md)
- [@mdp_sec — 2026-08-10 — Hey @AnthropicAI @ClaudeDevs  @trq212 @bcherny can you guys check into CVP.](posts/mdp_sec/2026-08-10-2086950923956576534.md)
- [@mdp_sec — 2026-08-11 — Claude: hey](posts/mdp_sec/2026-08-11-2087284315461972068.md)
- [@mdp_sec — 2026-08-12 — Gotta say a big thanks to @cjav_dev for sorting out my Claude CVP got my 3 accounts ready to rol](posts/mdp_sec/2026-08-12-2087544742850736538.md)
- [@mdp_sec — 2026-08-17 — Well promo was fun while lasted.](posts/mdp_sec/2026-08-17-2089462010451005513.md)
- [@mdp_sec — 2026-08-19 — Everyone is discovering cloud agents because their laptop starts crying after 4 concurrent sessi](posts/mdp_sec/2026-08-19-2090205014036025371.md)
- [@mdp_sec — 2026-08-20 — Legit hope this becomes a permanent thing](posts/mdp_sec/2026-08-20-2090365412768956459.md)
- [@mdp_sec — 2026-08-20 — Waking up to a Claude or Codex ban email..](posts/mdp_sec/2026-08-20-2090551076017885297.md)
- [@mdp_sec — 2026-08-21 — So atm claude on promo levels giving about 4-4.5b tokens a week using opus.](posts/mdp_sec/2026-08-21-2090907252383478129.md)
- [@mdp_sec — 2026-08-22 — This is pretty banger tbh.](posts/mdp_sec/2026-08-22-2091064571931017666.md)
- [@mdp_sec — 2026-08-28 — Most AI cybersecurity benchmarks answer the wrong question for bug-bounty hunters.](posts/mdp_sec/2026-08-28-2093342858501820901.md)
- [@mdp_sec — 2026-09-01 — Sadly another model that cyber defenders cant use.](posts/mdp_sec/2026-09-01-2094870059416166591.md)
- [@mdp_sec — 2026-09-02 — I selected Opus.](posts/mdp_sec/2026-09-02-2094986075920097578.md)
- [@mdp_sec — 2026-09-08 — So this happened almost a month ago now.](posts/mdp_sec/2026-09-08-2097417271216054476.md)
- [@mdp_sec — 2026-09-09 — took about a month to get a reply.](posts/mdp_sec/2026-09-09-2097804851455676716.md)
- [@mdp_sec — 2026-09-12 — My AI agents run on a Linux server in another country.](posts/mdp_sec/2026-09-12-2098923749156458655.md)
- [@mdp_sec — 2026-09-19 — Built a small standalone piece of my bug bounty workflow: Should I Submit This.](posts/mdp_sec/2026-09-19-2101181485046993353.md)
- [@mdp_sec — 2026-09-21 — New project up for everyone](posts/mdp_sec/2026-09-21-2101978915871031611.md)
- [@mdp_sec — 2026-09-23 — Tried to bench opus 5.5 but refusals just downgrades it to 4.8 so wont be able to bench this](posts/mdp_sec/2026-09-23-2102556490402058707.md)
- [@mdp_sec — 2026-09-24 — bypassing any llm guardrails 1 word at a time](posts/mdp_sec/2026-09-24-2103251491402444842.md)
- [@mdp_sec — 2026-09-25 — Who remembers this guy.](posts/mdp_sec/2026-09-25-2103409495741509907.md)
- [@mdp_sec — 2026-09-27 — LLM: escapes sandbox.](posts/mdp_sec/2026-09-27-2104091127079190873.md)
- [@mdp_sec — 2026-09-30 — Was not trying to build a cyber dataset.](posts/mdp_sec/2026-09-30-2105131551386415322.md)
- [@mdp_sec — 2026-09-30 — Everyone wants agents that find real vulnerabilities.](posts/mdp_sec/2026-09-30-2105401938213036106.md)
- [@mdp_sec — 2026-10-01 — genuine question for the labs training security agents.](posts/mdp_sec/2026-10-01-2105769650172903555.md)
- [@mdp_sec — 2026-10-02 — Just shy of 1 trillion tokens of real agent traces from 7 months of bug bounty hunting.](posts/mdp_sec/2026-10-02-2106165547327271028.md)
- [@mdp_sec — 2026-10-04 — Something new launching this week](posts/mdp_sec/2026-10-04-2106845239864635891.md)
- [@mdp_sec — 2026-10-07 — thx cvp](posts/mdp_sec/2026-10-07-2107636851133886641.md)
- [@mdp_sec — 2026-10-10 — Added Gemini to bench](posts/mdp_sec/2026-10-10-2109004960906244258.md)
- [@mdp_sec — 2026-10-10 — Bug Hunter tip](posts/mdp_sec/2026-10-10-2109022016062083241.md)
- [@mdp_sec — 2026-10-11 — Back to hunting this week, fam 🫡](posts/mdp_sec/2026-10-11-2109428613615698052.md)
- [@mdp_sec — 2026-10-12 — Legit never been this impressed](posts/mdp_sec/2026-10-12-2109486039987573147.md)
- [@mdp_sec — 2026-10-13 — If my cyber gets approved ill bench this.](posts/mdp_sec/2026-10-13-2110100051263676751.md)
- [@mdp_sec — 2026-10-15 — As requested Gemini 4 Argon @GoogleDeepMind @GoogleAI](posts/mdp_sec/2026-10-15-2110571337542778974.md)
- [@mdp_sec — 2026-10-19 — Gotta give credit](posts/mdp_sec/2026-10-19-2112188966363402648.md)
- [@mdp_sec — 2026-10-19 — Sadly got a few of these within same min](posts/mdp_sec/2026-10-19-2112306543094120786.md)
- [@mdp_sec — 2026-10-22 — feels legit like this a endless cycle between openai and claude for cyber](posts/mdp_sec/2026-10-22-2113153033328906402.md)
- [@mdp_sec — 2026-10-22 — well this be new.](posts/mdp_sec/2026-10-22-2113392897802600547.md)
- [@mdp_sec — 2026-10-26 — someone's hackbot broke out of its sandbox and used his github to message the challenge owner as](posts/mdp_sec/2026-10-26-2114571298840158212.md)
- [@mdp_sec — 2026-10-26 — claude found its own way past a georgia paywall without being asked](posts/mdp_sec/2026-10-26-2114630468322939090.md)
- [@mdp_sec — 2026-10-26 — everyone's laughing at mythos going out of scope](posts/mdp_sec/2026-10-26-2114675909424730475.md)
- [@mdp_sec — 2026-10-26 — gpt-6.1 terra just dropped](posts/mdp_sec/2026-10-26-2114816838119157855.md)
- [@mdp_sec — 2026-10-27 — gpt-6.1 terra is pretty much useless for defenders](posts/mdp_sec/2026-10-27-2114946685562757385.md)
- [@mdp_sec — 2026-10-27 — gemini 4 argon rolling out to everyone in antigravity tonight](posts/mdp_sec/2026-10-27-2115023197817172279.md)
- [@mdp_sec — 2026-10-27 — anthropic filed to go public with an $80.7bn net loss for the first half of 2026](posts/mdp_sec/2026-10-27-2115053396759883788.md)
- [@mdp_sec — 2026-10-27 — pro tip dont launch ur coding agent from downloads](posts/mdp_sec/2026-10-27-2115113794863329748.md)
- [@mdp_sec — 2026-10-28 — anthropic gave claude code a hidden lean on 4 calls in a study with 50 expert analysts](posts/mdp_sec/2026-10-28-2115445983752638800.md)
- [@mdp_sec — 2026-10-28 — 57/100 black box labs, $0.24 a solve, refused 0](posts/mdp_sec/2026-10-28-2115536580509122706.md)
- [@mdp_sec — 2026-10-29 — gpt-6 astra refused 35 of my 100 black box hacking labs and solved 0](posts/mdp_sec/2026-10-29-2115657376372048162.md)
- [@mdp_sec — 2026-10-29 — 220b tokens of my own usage over the last 14 days, average output speed](posts/mdp_sec/2026-10-29-2115717774647644341.md)
- [@mdp_sec — 2026-10-29 — STEVE didnt make the cyber 60 again](posts/mdp_sec/2026-10-29-2115747973518762387.md)
- [@mdp_sec — 2026-10-29 — gemini 4 carbon is sota on cyber and google strengthened the safeguards](posts/mdp_sec/2026-10-29-2115778172356902954.md)
- [@mdp_sec — 2026-10-29 — openai just doubled pro limits and my codex sub says thanks](posts/mdp_sec/2026-10-29-2115887157881745719.md)
- [@mdp_sec — 2026-10-29 — 5 more labs for 10x the price](posts/mdp_sec/2026-10-29-2115898968534306846.md)
- [@mdp_sec — 2026-10-30 — everyone wants their app agent ready now](posts/mdp_sec/2026-10-30-2115989565395841400.md)
- [@mdp_sec — 2026-10-30 — anthropics unreleased claude got zero click root on linux in 53 minutes and im verified with bot](posts/mdp_sec/2026-10-30-2116140561044292021.md)
- [@mdp_sec — 2026-11-04 — Personal Claude account got into @AnthropicAI CVP.](posts/mdp_sec/2026-11-04-2118130528239149369.md)
- [@mdp_sec — 2026-11-09 — BB Arena v2 is live. 100 new private black-box labs, and it's a lot harder](posts/mdp_sec/2026-11-09-2119670856075166075.md)
- [@mdp_sec — 2026-11-09 — claude fable 5.1 refused all 100 of my black-box hacking labs](posts/mdp_sec/2026-11-09-2119885234887876972.md)
- [@mdp_sec — 2026-11-09 — So... who is gotta sleep with for red access..](posts/mdp_sec/2026-11-09-2119895827091206184.md)
- [@mdp_sec — 2026-11-12 — gemini 4 carbon dropped this morning and i can't bench it](posts/mdp_sec/2026-11-12-2120308020798488654.md)
- [@naresh_1337 — 2026-10-21 — Another finding, another milestone. The hunt continues......](posts/naresh_1337/2026-10-21-2112901217278214612.md)
- [@orange_8361 — 2026-05-14 — That's my chain — a full chain w/ logic bugs only! No memory corruption, no AI, and of cou](posts/orange_8361/2026-05-14-2054906050143240399.md)
- [@orange_8361 — 2026-05-15 — And this one is human insight w/ LLM-assisted research. Took about one week to finish ever](posts/orange_8361/2026-05-15-2055330289652539850.md)
- [@ryotkak — 2026-06-01 — Claude Codeに対してサプライチェーン攻撃を行うことが可能だった脆弱性についての記事を公開しました！ https://twitter.com/flatt_security/](posts/ryotkak/2026-06-01-2061434879309664575.md)
- [@samczsun — 2026-02-05 — on one hand the crypto dream feels dead but on the other hand weve finally figured out how to s](posts/samczsun/2026-02-05-2019551027457097765.md)
- [@samwcyo — 2026-03-19 — Asked Claude to root my Xiaomi 17 Pro Max. Did not go well. [pic.x.com/HSCrRo2sqK]](posts/samwcyo/2026-03-19-2034495676533612643.md)
- [@samwcyo — 2026-08-18 — For anyone using LLMs to do security research, bug bounty, red teaming, etc, we made a Dis](posts/samwcyo/2026-08-18-2089536974444982714.md)
- [@samwcyo — 2026-10-18 — I’d be willing to pay $100 per report for priority triage with automated dupe checking and](posts/samwcyo/2026-10-18-2111805910448529757.md)
- [@samwcyo — 2026-11-12 — I've got a feeling that a lot of security consultants who are being told not to use LLMs on pent](posts/samwcyo/2026-11-11-2120395487237075210.md)
- [@saxenism — 2024-11-29 — I bribed the AI](posts/saxenism/2024-11-29-1862497236980310323.md)
- [@saxenism — 2024-12-12 — Yap early, yap only, yap often.](posts/saxenism/2024-12-12-1867083327746023648.md)
- [@saxenism — 2024-12-21 — The currently existing AI models, at least the publicly available ones, have a serious limitati](posts/saxenism/2024-12-21-1870299724504326271.md)
- [@saxenism — 2024-12-30 — If you're a guy in your 20s:](posts/saxenism/2024-12-30-1873789962233229512.md)
- [@saxenism — 2025-02-14 — In this AI era, you better be pretty good at what you do... whether it is development or securi](posts/saxenism/2025-02-14-1890267472357667005.md)
- [@saxenism — 2025-03-18 — &gt; Structured context and context hints](posts/saxenism/2025-03-18-1901913524617855047.md)
- [@saxenism — 2025-07-09 — Been using the publicly accessible LLMs for a while and my strongest realisation is that:](posts/saxenism/2025-07-09-1942873393692340343.md)
- [@saxenism — 2025-08-13 — Perhaps the greatest benefit I've had from using LLMs is the rapid prototyping of my heuristics](posts/saxenism/2025-08-13-1955588400628801807.md)
- [@saxenism — 2025-08-17 — Let this be your final call.](posts/saxenism/2025-08-17-1957048373225115902.md)
- [@saxenism — 2025-08-22 — A rather elaborate hack/drain attempt on me](posts/saxenism/2025-08-22-1958796012115640471.md)
- [@saxenism — 2025-08-29 — Fucking Hell. I kinda understand now why judging and triaging sucks for everyone involved.](posts/saxenism/2025-08-29-1961348543173755177.md)
- [@saxenism — 2025-08-29 — a good thing would be to use an LLM that has not been trained for excessive politeness, yk, RLH](posts/saxenism/2025-08-29-1961349603996873197.md)
- [@saxenism — 2025-10-31 — So, Sam just launched Aardvark which is OpenAI’s agentic security researcher.](posts/saxenism/2025-10-31-1984144303195877454.md)
- [@saxenism — 2025-12-02 — Frens who’ve built or worked on static analysers, shower your wisdom on me](posts/saxenism/2025-12-02-1995894227000262968.md)
- [@saxenism — 2025-12-12 — This is 100% a specialised LLM at work.](posts/saxenism/2025-12-12-1999317684287340738.md)
- [@saxenism — 2025-12-13 — How exactly am I supposed to make "specialised LLM agents"?](posts/saxenism/2025-12-13-1999677754951049283.md)
- [@saxenism — 2025-12-18 — Yooooo, this is incredibly fun!!](posts/saxenism/2025-12-18-2001613448631980322.md)
- [@saxenism — 2025-12-31 — 10/10 advice for protocol development teams.](posts/saxenism/2025-12-31-2006278815706906732.md)
- [@saxenism — 2026-01-10 — How well you use LLMs in your workflow as a dev & auditor is directly proportional to your abil](posts/saxenism/2026-01-10-2009962510913536462.md)
- [@saxenism — 2026-01-15 — AN ARTIST.](posts/saxenism/2026-01-15-2011821124615798836.md)
- [@saxenism — 2026-01-18 — Claude Code + Claude Skills &gt;&gt; Security Agents.](posts/saxenism/2026-01-18-2012877350468518060.md)
- [@saxenism — 2026-01-18 — Sooo many writeups on how best to use Claude for development work... wen writeup for using Clau](posts/saxenism/2026-01-18-2012878209226822082.md)
- [@saxenism — 2026-01-20 — Top-down learning for me, ALWAYS.](posts/saxenism/2026-01-20-2013594786469712183.md)
- [@saxenism — 2026-02-09 — With new AI frontier models being launched literally every week, protocols have an increased ch](posts/saxenism/2026-02-09-2020806738887495887.md)
- [@saxenism — 2026-02-09 — Yes.](posts/saxenism/2026-02-09-2020828400051757297.md)
- [@saxenism — 2026-02-17 — With AI aggressively entering everyday lives, novel attack vectors come up every day.](posts/saxenism/2026-02-17-2023754001305760019.md)
- [@saxenism — 2026-03-05 — The last few months at Bluethroat have been intense.](posts/saxenism/2026-03-05-2029562576326311980.md)
- [@saxenism — 2026-03-06 — The much-talked-about "security-mindset" is different for every security researcher doing sophi](posts/saxenism/2026-03-06-2029884965199163718.md)
- [@saxenism — 2026-03-12 — If you're leveraging AI agressively enough in your technical workflows, you'll find yourself re](posts/saxenism/2026-03-12-2032116949845754067.md)
- [@saxenism — 2026-03-13 — Reviewed the biggest TEE protocols in Web3 earlier this year.](posts/saxenism/2026-03-13-2032358750846144694.md)
- [@saxenism — 2026-03-18 — I do not believe in generic AI security tooling.](posts/saxenism/2026-03-18-2034198942385336442.md)
- [@saxenism — 2026-03-19 — Can someone help me w/ the said coupons?](posts/saxenism/2026-03-19-2034595139700871314.md)
- [@saxenism — 2026-03-24 — Extremely bullish on AI in (web3) security.](posts/saxenism/2026-03-24-2036446969200255093.md)
- [@saxenism — 2026-04-03 — With LLMs aggressively getting integrated into our workflows, the written word holds more weigh](posts/saxenism/2026-04-03-2040014988585357755.md)
- [@saxenism — 2026-04-08 — Attackers are getting smarter, faster, and cheaper.](posts/saxenism/2026-04-08-2041890307814342940.md)
- [@saxenism — 2026-04-09 — The most satisfying use case of AI for me has been turning my cursed internal bug-hunting heuri](posts/saxenism/2026-04-09-2042384058366509423.md)
- [@saxenism — 2026-04-17 — Well, I have been using AI rigorously for the past few months. Almost daily.](posts/saxenism/2026-04-17-2045119506293588044.md)
- [@saxenism — 2026-04-27 — Funny, but I don't think this is what the future is gonna look like.](posts/saxenism/2026-04-27-2048735945961398731.md)
- [@saxenism — 2026-04-28 — In the era of AI, clear thinkers will absolutely melt faces.](posts/saxenism/2026-04-28-2049095534863098076.md)
- [@saxenism — 2026-04-29 — So, like... the NK threat actors are working w/ self hosted LLMs??](posts/saxenism/2026-04-29-2049356784218087657.md)
- [@saxenism — 2026-04-29 — The scary part is not “AI wrote bad Solidity” or that AI created old-school access control bugs](posts/saxenism/2026-04-29-2049401347414323288.md)
- [@saxenism — 2026-04-29 — 1) The sharper framing isn’t “Sui protocols are uniquely careless.”](posts/saxenism/2026-04-29-2049495518376866086.md)
- [@saxenism — 2026-05-02 — Hot take: Do not try to run 10 different agents in parallel. Stick with 1 to 2 agents and reall](posts/saxenism/2026-05-02-2050692729622118621.md)
- [@saxenism — 2026-05-13 — If this is not the peak bear signal, I don't know what is.](posts/saxenism/2026-05-13-2054508841136472069.md)
- [@saxenism — 2026-05-20 — The amount of malware-infested repos floating around Web3 right now is genuinely insane.](posts/saxenism/2026-05-20-2057106189587243181.md)
- [@saxenism — 2026-05-28 — This truly is one of THE most brutal times for teams building in Web3.](posts/saxenism/2026-05-28-2060042698032296244.md)
- [@saxenism — 2026-06-09 — A gentle re-framing for your "AI-assisted blackhats":](posts/saxenism/2026-06-09-2064264210486620404.md)
- [@saxenism — 2026-06-17 — Tested the `codebase-memory-mcp` today with two of my specialist security agents:](posts/saxenism/2026-06-17-2067126654452027521.md)
- [@saxenism — 2026-06-17 — Words are just that, words.](posts/saxenism/2026-06-17-2067177511138558422.md)
- [@saxenism — 2026-06-24 — Recently I've started to get deeper into AI.](posts/saxenism/2026-06-24-2069674104328990852.md)
- [@saxenism — 2026-06-30 — I used to HATE those "auditing mindset" videos circa '23.](posts/saxenism/2026-06-30-2071892345927450709.md)
- [@saxenism — 2026-07-11 — I have this really really strong inkling that if I simply went back to my old working style of ](posts/saxenism/2026-07-11-2075865356468691223.md)
- [@saxenism — 2026-07-13 — One massively underrated personal AI use case I’ve stumbled upon: connecting 2 seemingly unrela](posts/saxenism/2026-07-13-2076624680417444105.md)
- [@saxenism — 2026-07-22 — You asked for receipts, you got it.](posts/saxenism/2026-07-22-2079962866921480607.md)
- [@saxenism — 2026-07-27 — My For You is getting insufferable again.](posts/saxenism/2026-07-27-2081632296155976064.md)
- [@saxenism — 2026-07-30 — Here's the current reality of the web3 landscape:](posts/saxenism/2026-07-30-2082771949529567668.md)
- [@saxenism — 2026-08-23 — This is a world where blackhats are running wild with their built-for-the-kill SOTA LLMs and ha](posts/saxenism/2026-08-23-2091451966757187586.md)
- [@saxenism — 2026-08-23 — For fellow bug hunters who are leveraging the shit out of LLMs in the process, what is the best](posts/saxenism/2026-08-23-2091514485265838499.md)
- [@saxenism — 2026-08-25 — Ok so I am a security engineer and I got into it 6 months into my first proper job.](posts/saxenism/2026-08-25-2092152128982683682.md)
- [@saxenism — 2026-09-11 — 1/3 We think BlueSkills is difficult to fool. Prove us wrong.](posts/saxenism/2026-09-11-2098352916612407695.md)
- [@saxenism — 2026-09-21 — These LLMs have gotten so stupidly good that just leaking a generalised title of the finding is](posts/saxenism/2026-09-21-2102039983112757477.md)
- [@saxenism — 2026-10-02 — I will be participating in @paradigm Frontiers '26 in SF, Oct 12-14.](posts/saxenism/2026-10-02-2105995003055296775.md)
- [@saxenism — 2026-10-02 — Things you discover when you and your hunting agents are locked in.](posts/saxenism/2026-10-02-2106039567673651479.md)
- [@saxenism — 2026-10-09 — Looks like Eclipse is transitioning to training offensive LLMs on actual web3 findings/data XD](posts/saxenism/2026-10-09-2108370713082249563.md)
- [@saxenism — 2026-10-19 — deepseek-ai/DeepSeek-V4.1-Flash has been pretty average for me so far.](posts/saxenism/2026-10-19-2112313843376693538.md)
- [@saxenism — 2026-10-21 — Accepted finding #5 from the @Zcash campaign :)](posts/saxenism/2026-10-21-2112713764999250220.md)
- [@saxenism — 2026-10-23 — COPY-PASTE PROMPT BELOW: patch your systems and audit who can access them.](posts/saxenism/2026-10-23-2113509059903320412.md)
- [@saxenism — 2026-11-05 — About to give a detailed presentation on how companies can defend themselves in the AI era, in ](posts/saxenism/2026-11-05-2118203579697861082.md)
- [@trust__90 — 2026-04-20 — CT focusing on the low-hanging fruit takes -](posts/trust__90/2026-04-20-2046203827305484565.md)
- [@trust__90 — 2026-04-29 — The ironic thing is that this will sound to many like old people come across when irration](posts/trust__90/2026-04-29-2049528623489781939.md)
- [@trust__90 — 2026-05-13 — We all need to take a moment and give our appreciation to the pioneers of decentralized se](posts/trust__90/2026-05-13-2054502639207961066.md)
- [@trust__90 — 2026-10-14 — Anthropic continues to abstract away any notion of hands-on control over their codebase.](posts/trust__90/2026-10-14-2110335614998462608.md)
- [@zksecurityXYZ — 2026-10-14 — are other companies really interviewing candidates using AI avatars?](posts/zksecurityXYZ/2026-10-14-2110500746567520470.md)
- [@zksecurityXYZ — 2026-10-25 — New https://zk.golf challenge ⛳️ Google ID Token Claims Extraction.](posts/zksecurityXYZ/2026-10-25-2114284396450893976.md)
- [@zseano — 2026-01-31 — AI is moving fast I can’t keep up 😂 everyday something new is being released. We are living in wi](posts/zseano/2026-01-31-2017538347204259978.md)
- [@zseano — 2026-08-20 — Wondering if the GTA6 leaks are real or if they’re AI generated 😅 never know these days…](posts/zseano/2026-08-20-2090414817563607512.md)
- [@zseano — 2026-10-01 — AI hackbots go BRRRRR ? (maybe? who knows). But damn some programs are being overwhelmed haha rep](posts/zseano/2026-10-01-2105764085141037123.md)
- [@zseano — 2026-10-08 — Did a bit of hacking past few days and I still prefer manual hacking over relying on AI. E](posts/zseano/2026-10-08-2108274552480444661.md)
- [@zseano — 2026-10-18 — non hacking post, but did anyone here ever do Halo2 Superbouncing? then Halo3 came out and the bo](posts/zseano/2026-10-18-2111728419431936384.md)

### Account takeover (3)

- [@NahamSec — 2026-11-04 — Launched my hackbot at a new target on Bugcrowd at 11:09 and by 11:32 it had its first wor](posts/NahamSec/2026-11-04-2118067189576286345.md)
- [@infinitelogins — 2026-11-04 — I found a critical unauthenticated account takeover that let me log in as any customer on](posts/infinitelogins/2026-11-04-2117981403161764138.md)
- [@xssdoctor — 2026-10-01 — Found a cool bug today, thought i should share it.](posts/xssdoctor/2026-10-01-2105723370125881675.md)

### Auth bypass (5)

- [@NahamSec — 2026-10-15 — Filed 3 PII leaks and a really cool authentication bypass.. but can you guess what happene](posts/NahamSec/2026-10-15-2110822271770411297.md)
- [@infinitelogins — 2026-10-08 — I found a critical auth bypass that resulted in a $10K bounty due to mass PII exfiltratio](posts/infinitelogins/2026-10-08-2108181015885685018.md)
- [@infosec_au — 2026-05-10 — Reported another cPanel critical pre-authentication vuln. Our research dates back to early](posts/infosec_au/2026-05-10-2053414439635054961.md)
- [@mdp_sec — 2026-11-05 — $8,000 for an auth bypass](posts/mdp_sec/2026-11-05-2118435683329310786.md)
- [@mdp_sec — 2026-11-11 — one /./ in the path walked me straight past a login wall into an admin console](posts/mdp_sec/2026-11-11-2120338219841544604.md)

### Blockchain / L1-L2 / bridge (49)

- [@0xiczc — 2023-01-06 — I have a fun blockchain challenge ready for everyone to try out! #realworldctf](posts/0xiczc/2023-01-06-1611472273181151232.md)
- [@0xiczc — 2023-05-26 — 1/ Recently, I discovered a vulnerability in the  @0xPolygon zkEVM and earned my first L2](posts/0xiczc/2023-05-26-1662090451493740545.md)
- [@0xiczc — 2024-01-26 — Congrats to Blue Water! And a warm welcome to all to try out this blockchain challenge I prepared](posts/0xiczc/2024-01-26-1750915452141007134.md)
- [@0xiczc — 2025-10-04 — Thanks @CertiK for the great write-up on the vulnerability I found in Cosmos EVM-compatibl](posts/0xiczc/2025-10-04-1974521372597723619.md)
- [@0xriptide — 2026-10-08 — A note to those building on chain in 2026:](posts/0xriptide/2026-10-08-2107985669410947229.md)
- [@ChainLight_io — 2025-03-24 — Which rug pulls, exploits, and security breaches happened this week?](posts/ChainLight_io/2025-03-24-1904184855891771421.md)
- [@Piki_eth — 2026-10-29 — Another bug bounty report triaged by HackenProof. 🔥](posts/Piki_eth/2026-10-29-2115783655092277530.md)
- [@PwningEth — 2022-09-04 — Two brilliant whitehat hackers guarded the @auroraisnear bridge again! Hundreds of million](posts/PwningEth/2022-09-04-1566381803405209601.md)
- [@PwningEth — 2022-12-02 — Could wrapped tokens like WETH be forced Insolvent? This bug I reported in frontier EVM ca](posts/PwningEth/2022-12-02-1598592820268642304.md)
- [@WhiteHatMage — 2026-10-23 — How lucrative would it be to build a tool that proves EVM contracts are free of asset thef](posts/WhiteHatMage/2026-10-23-2113630146053972258.md)
- [@al_f4lc0n — 2026-03-15 — I Saved Injective's $500M. They Pay Me $50K.](posts/al_f4lc0n/2026-03-15-2033110168045568434.md)
- [@al_f4lc0n — 2026-03-18 — the figures referenced in the post are entirely misleading. There was no impact realized f](posts/al_f4lc0n/2026-03-18-2034125406748741827.md)
- [@al_f4lc0n — 2026-06-03 — 3 tips for Bug Bounty Hunters:](posts/al_f4lc0n/2026-06-03-2062082215962366225.md)
- [@asymmetric_re — 2026-09-22 — The @SolanaFndn just open-sourced Microscope, a free monitoring &amp; alerting tool for So](posts/asymmetric_re/2026-09-22-2102397819386745185.md)
- [@asymmetric_re — 2026-10-19 — For its first 6 weeks on mainnet, Solana's governance program had a bug: any validator cou](posts/asymmetric_re/2026-10-19-2112236410455597403.md)
- [@bluethroat_labs — 2026-10-01 — Bounty #9 on @immunefi is extremely special for us.](posts/bluethroat_labs/2026-10-01-2105581456550461936.md)
- [@bluethroat_labs — 2026-10-06 — Bounty #10 on @immunefi stems from the same root as #9.](posts/bluethroat_labs/2026-10-06-2107490499305124027.md)
- [@bluethroat_labs — 2026-11-07 — A major L1 offered Bluethroat Labs a $10,000 bounty for a finding where two layers disag](posts/bluethroat_labs/2026-11-07-2119050683840438658.md)
- [@immunefi — 2026-10-13 — Security researcher @GuplerSaxanoid just earned $30,000 for finding a critical vulnerabili](posts/immunefi/2026-10-13-2109982938578522400.md)
- [@immunefi — 2026-11-04 — This security researcher earned $33,000 for a high-severity bug in a blockchain’s core inf](posts/immunefi/2026-11-04-2117965345550172382.md)
- [@lonelysloth_sec — 2026-06-05 — My take on the Zcash bug.](posts/lonelysloth_sec/2026-06-05-2062916729676648907.md)
- [@samczsun — 2025-11-22 — i love etherscan but unless im misunderstanding something, they have essentially paywalled](posts/samczsun/2025-11-22-1992296916491915403.md)
- [@saxenism — 2024-12-13 — Same.](posts/saxenism/2024-12-13-1867571600234803463.md)
- [@saxenism — 2025-01-15 — While Linus's Law ("given enough eyeballs, all bugs are shallow") helped scale Linux, the block](posts/saxenism/2025-01-15-1879380630112464998.md)
- [@saxenism — 2025-01-23 — Finally Ethereum is onto what ZKsync had already been doing.](posts/saxenism/2025-01-23-1882267577730424973.md)
- [@saxenism — 2025-03-19 — Fantastic list and I hope it does come to fruition.](posts/saxenism/2025-03-19-1902330211007443320.md)
- [@saxenism — 2025-04-25 — Can someone point me towards a well put-together argument explaining this "value leakage from L](posts/saxenism/2025-04-25-1915650732671328613.md)
- [@saxenism — 2025-08-08 — What's the CoW swap equivalent fall in Solana?](posts/saxenism/2025-08-08-1953680322832289916.md)
- [@saxenism — 2025-09-30 — Gm Chat!](posts/saxenism/2025-09-30-1972961286729470288.md)
- [@saxenism — 2025-10-23 — TEEs are truly fascinating.](posts/saxenism/2025-10-23-1981230974999630198.md)
- [@saxenism — 2025-11-10 — I downright disagree with your statement that "TEEs are useless" &amp; I assume that this is ju](posts/saxenism/2025-11-10-1987931403582140482.md)
- [@saxenism — 2026-04-23 — Honoured to be selected as an ETHSecurity Badge holder.](posts/saxenism/2026-04-23-2047248003497693600.md)
- [@saxenism — 2026-04-28 — In the era of AI, clear thinkers will absolutely melt faces.](posts/saxenism/2026-04-28-2049095534863098076.md)
- [@saxenism — 2026-04-28 — This is the exact shift that every protocol needs to make to survive in web3.](posts/saxenism/2026-04-28-2049136710169272562.md)
- [@saxenism — 2026-04-29 — 1) The sharper framing isn’t “Sui protocols are uniquely careless.”](posts/saxenism/2026-04-29-2049495518376866086.md)
- [@saxenism — 2026-06-23 — "Just a .pem in a public repo" is the trigger for sure, just not the bug.](posts/saxenism/2026-06-23-2069405688397447285.md)
- [@saxenism — 2026-10-16 — I have been hearing @Zcash is THE thing in web3 now.](posts/saxenism/2026-10-16-2111134534549086330.md)
- [@saxenism — 2026-10-17 — Somewhere in the @Zcash ecosystem, something just got more secure.](posts/saxenism/2026-10-17-2111558018311880938.md)
- [@saxenism — 2026-10-18 — Accepted finding #3.](posts/saxenism/2026-10-18-2111915973330808856.md)
- [@saxenism — 2026-10-19 — Accepted finding #4 (High).](posts/saxenism/2026-10-19-2112209735986577759.md)
- [@saxenism — 2026-10-21 — Accepted finding #5 from the @Zcash campaign :)](posts/saxenism/2026-10-21-2112713764999250220.md)
- [@saxenism — 2026-10-21 — Several private security reports I filed across the Zcash ecosystem are awaiting review.](posts/saxenism/2026-10-21-2112982713963852188.md)
- [@saxenism — 2026-10-22 — One of our @Zcash advisories has just been published.](posts/saxenism/2026-10-22-2113303290654216476.md)
- [@saxenism — 2026-11-04 — Attended @drakefjustin session at @safe's event and someone brought up ZCash.](posts/saxenism/2026-11-04-2117974338385437111.md)
- [@saxenism — 2026-11-06 — Accepted finding #6 (High) from the @Zcash campaign.](posts/saxenism/2026-11-06-2118554252570427494.md)
- [@saxenism — 2026-11-09 — Accepted finding #7 (Moderate) from the @ZCash campaign.](posts/saxenism/2026-11-09-2119670604177834285.md)
- [@trust__90 — 2026-04-20 — CT focusing on the low-hanging fruit takes -](posts/trust__90/2026-04-20-2046203827305484565.md)
- [@zksecurityXYZ — 2026-10-05 — Who verifies the formal verification?](posts/zksecurityXYZ/2026-10-05-2107169364202189182.md)
- [@zksecurityXYZ — 2026-11-03 — evm.asm, our collaboration with EF on an e2e verified EVM implementation for zkVMs, now ha](posts/zksecurityXYZ/2026-11-03-2117550503060185134.md)

### CSP / CSPT (1)

- [@kevin_mizu — 2026-10-28 — With @hash_kitten, we've been looking into Cloudflare's /cdn-cgi/image endpoint and manage](posts/kevin_mizu/2026-10-28-2115448862869500312.md)

### Dependency confusion / supply chain (3)

- [@Rhynorater — 2026-10-01 — Lupin and the squad are killing it in bug bounty using supply chain attacks.](posts/Rhynorater/2026-10-01-2105716901423001866.md)
- [@mdp_sec — 2026-11-06 — $1,200 for a package name nobody had claimed. dependency confusion, my only paid supply chain bu](posts/mdp_sec/2026-11-06-2118803107119325691.md)
- [@trust__90 — 2026-04-20 — CT focusing on the low-hanging fruit takes -](posts/trust__90/2026-04-20-2046203827305484565.md)

### IDOR / BOLA (2)

- [@Assass1nmarcos — 2026-07-08 — Hello @Hacker0x01,](posts/Assass1nmarcos/2026-07-08-2074871162035986895.md)
- [@Swartz068 — 2026-08-24 — 2 x Duplicate on @Bugcrowd](posts/Swartz068/2026-08-24-2091854507970081180.md)

### Memory corruption / native (23)

- [@Guhu95 — 2025-07-17 — There are just two types of bugs:](posts/Guhu95/2025-07-17-1945640502025752709.md)
- [@S1r1u5_ — 2026-11-02 — apart from ip options potentially being dropped in transit, kernel text leaks taking time,](posts/S1r1u5_/2026-11-02-2117097902774640858.md)
- [@ajxchapman — 2024-11-04 — Program: We are downgrading your RCE to medium as the environment in it runs in can only a](posts/ajxchapman/2024-11-04-1853373604206887326.md)
- [@farazsth98 — 2026-01-10 — Just wanted to share a few things I learned that prevents this exploit from working out-of](posts/farazsth98/2026-01-10-2009932971692962216.md)
- [@farazsth98 — 2026-06-16 — Wow... After writing the Chronomaly exploit, I studied the task exit flow for a long time](posts/farazsth98/2026-06-16-2066983836328628615.md)
- [@farazsth98 — 2026-10-28 — Don't worry @orange_8361, there are still people reading blog posts and articles from star](posts/farazsth98/2026-10-28-2115464807042465864.md)
- [@galnagli — 2026-10-22 — It took 17 minutes to turn the Gitlab RCE to a working HEAP exploit using Gemini 4 Argon a](posts/galnagli/2026-10-22-2113185093871095893.md)
- [@infosec_au — 2026-05-10 — Reported another cPanel critical pre-authentication vuln. Our research dates back to early](posts/infosec_au/2026-05-10-2053414439635054961.md)
- [@irsdl — 2026-10-22 — Great video from @LiveOverflow 👏](posts/irsdl/2026-10-22-2113195840328094077.md)
- [@j00ru — 2020-07-28 — Trying hard to keep up the weekly cadence of the MMS series. Today we're finally moving to](posts/j00ru/2020-07-28-1288200298390081536.md)
- [@j00ru — 2020-08-04 — This week's episode: MMS Exploit Part 4: MMS Primer, Completing the ASLR Oracle](posts/j00ru/2020-08-04-1290678374487162881.md)
- [@j00ru — 2020-08-12 — The final part 5 of my Samsung MMS exploit blog series is out 🎉 It covers bypassing Androi](posts/j00ru/2020-08-12-1293600839320428545.md)
- [@j00ru — 2021-03-12 — Fixed this month: CVE-2021-26863, a race condition/use-after-free in win32k.sys demonstrat](posts/j00ru/2021-03-12-1370364905862352901.md)
- [@mdp_sec — 2026-08-08 — The human equivalent of what token cost would look like](posts/mdp_sec/2026-08-08-2085907122383118673.md)
- [@mdp_sec — 2026-08-22 — One of the smaller things that made automated account creation more reliable was adding more tha](posts/mdp_sec/2026-08-22-2091302807479652372.md)
- [@mdp_sec — 2026-08-28 — Most AI cybersecurity benchmarks answer the wrong question for bug-bounty hunters.](posts/mdp_sec/2026-08-28-2093342858501820901.md)
- [@mdp_sec — 2026-10-26 — Everyone's talking about the vulnpocalypse.](posts/mdp_sec/2026-10-26-2114586570686628009.md)
- [@mdp_sec — 2026-10-26 — lines up with BB Arena](posts/mdp_sec/2026-10-26-2114825143046521124.md)
- [@mdp_sec — 2026-11-04 — heaps of sunscreen, multiple days back to back 80km offshore and my soft IT skin still lost. hid](posts/mdp_sec/2026-11-04-2118073295358808429.md)
- [@mdp_sec — 2026-11-11 — HuntDeck is live in demo mode 🎯](posts/mdp_sec/2026-11-11-2120371004916805916.md)
- [@orange_8361 — 2024-08-30 — My first kernel exploit! Big thanks to @d3vc0r3 and @offsectraining ! 🎉](posts/orange_8361/2024-08-30-1829491975986589764.md)
- [@orange_8361 — 2026-09-19 — It’s gonna overflow!](posts/orange_8361/2026-09-19-2101101039885910124.md)
- [@ryotkak — 2026-05-08 — Does anyone have a direct contact at @thezdi? I've been trying to register my Pwn2Own entr](posts/ryotkak/2026-05-08-2052881664909660521.md)

### Mobile / Android / iOS (15)

- [@_bagipro — 2024-03-21 — Android bug hunters, your chance to get rewards from Google](posts/_bagipro/2024-03-21-1770899301171941595.md)
- [@_bagipro — 2024-07-30 — We have updated scan reports for all Google phone apps and additionally included reports for We](posts/_bagipro/2024-07-30-1818236331388252588.md)
- [@_bagipro — 2025-08-01 — New Android host validation bypass technique!](posts/_bagipro/2025-08-01-1951318010444005529.md)
- [@_bagipro — 2025-08-28 — We’re hiring a Mobile App Security Expert!](posts/_bagipro/2025-08-28-1961055207476867529.md)
- [@_bagipro — 2026-02-25 — An attack on Android content providers that researchers might overlook](posts/_bagipro/2026-02-25-2026798826871247233.md)
- [@_bagipro — 2026-04-22 — We launched Android DAST. And the first problem we hit is that login flows block everything.](posts/_bagipro/2026-04-22-2046911820452216842.md)
- [@_bagipro — 2026-05-27 — [1/3] It's common to get a ParcelFileDescriptor pointing to a directory through an Android Cont](posts/_bagipro/2026-05-27-2059779421876232588.md)
- [@farazsth98 — 2026-01-10 — Just wanted to share a few things I learned that prevents this exploit from working out-of](posts/farazsth98/2026-01-10-2009932971692962216.md)
- [@j00ru — 2020-07-13 — In July, there is a lot going on for the security of Android image decoding, so I recommend instal](posts/j00ru/2020-07-13-1282681407832125441.md)
- [@j00ru — 2020-07-28 — Trying hard to keep up the weekly cadence of the MMS series. Today we're finally moving to](posts/j00ru/2020-07-28-1288200298390081536.md)
- [@j00ru — 2020-08-12 — The final part 5 of my Samsung MMS exploit blog series is out 🎉 It covers bypassing Androi](posts/j00ru/2020-08-12-1293600839320428545.md)
- [@mdp_sec — 2026-09-12 — My AI agents run on a Linux server in another country.](posts/mdp_sec/2026-09-12-2098923749156458655.md)
- [@mdp_sec — 2026-09-23 — Ps on android using premium plus sub](posts/mdp_sec/2026-09-23-2102909109477777750.md)
- [@mdp_sec — 2026-10-31 — opencode got breached, 1.4% of console users with external provider keys hit, and command code r](posts/mdp_sec/2026-10-31-2116351953273827524.md)
- [@xssdoctor — 2026-10-01 — Found a cool bug today, thought i should share it.](posts/xssdoctor/2026-10-01-2105723370125881675.md)

### OAuth (2)

- [@mdp_sec — 2026-09-03 — I found a public OAuth client where any free account could read and write the production billing](posts/mdp_sec/2026-09-03-2095462761111388207.md)
- [@xssdoctor — 2026-10-01 — Found a cool bug today, thought i should share it.](posts/xssdoctor/2026-10-01-2105723370125881675.md)

### Path normalization (6)

- [@mdp_sec — 2026-08-28 — Most AI cybersecurity benchmarks answer the wrong question for bug-bounty hunters.](posts/mdp_sec/2026-08-28-2093342858501820901.md)
- [@mdp_sec — 2026-08-29 — Adding one dot segment turned an admin login redirect into HTTP 200.](posts/mdp_sec/2026-08-29-2093595999847731482.md)
- [@mdp_sec — 2026-10-14 — A few bypasses that keep working for me in hunts. There are huge lists out there, but these are ](posts/mdp_sec/2026-10-14-2110165381239521347.md)
- [@mdp_sec — 2026-10-19 — New on BB Arena: OrcaCyber Zero 1.5 (High)](posts/mdp_sec/2026-10-19-2112097740046111101.md)
- [@mdp_sec — 2026-11-11 — one /./ in the path walked me straight past a login wall into an admin console](posts/mdp_sec/2026-11-11-2120338219841544604.md)
- [@samwcyo — 2026-02-26 — Two years ago, I reported an improper path parsing vulnerability in Next.js. Today, they r](posts/samwcyo/2026-02-26-2026888257779224594.md)

### RCE (22)

- [@Suryesh_92 — 2026-06-22 — Just got my first Remote Code Execution report accepted. Found RCE directly in thick clien](posts/Suryesh_92/2026-06-22-2069043943640301896.md)
- [@Suryesh_92 — 2026-06-30 — Another Bounty 😉](posts/Suryesh_92/2026-06-30-2071781463767580756.md)
- [@Suryesh_92 — 2026-09-09 — Another RCE Bounty in a Thick Client Application! 🤑😊](posts/Suryesh_92/2026-09-09-2097690285799313440.md)
- [@Suryesh_92 — 2026-09-10 — @virajmathpati thick client pentest depends on source code anlysis capabilities](posts/Suryesh_92/2026-09-10-2097850230930862237.md)
- [@Suryesh_92 — 2026-11-03 — Another new Thick Client finding accepted and rewarded.](posts/Suryesh_92/2026-11-03-2117598354641482125.md)
- [@ajxchapman — 2024-11-04 — Program: We are downgrading your RCE to medium as the environment in it runs in can only a](posts/ajxchapman/2024-11-04-1853373604206887326.md)
- [@fransrosen — 2024-09-04 — Here's my x-correlation/json-injection research also in writing, thank you @ctbbpodcast!](posts/fransrosen/2024-09-04-1831348652930949616.md)
- [@galnagli — 2026-10-21 — As the embargo is now lifted, find all the information needed on https://php2shell.com/ -](posts/galnagli/2026-10-21-2112902206152167640.md)
- [@galnagli — 2026-10-22 — It took 17 minutes to turn the Gitlab RCE to a working HEAP exploit using Gemini 4 Argon a](posts/galnagli/2026-10-22-2113185093871095893.md)
- [@infinitelogins — 2026-02-23 — Researchers at @HacktronAI found a bug in Google’s Antigravity IDE browser extension that](posts/infinitelogins/2026-02-23-2025934052759367834.md)
- [@infinitelogins — 2026-10-19 — PwnEscape escapes KVM in Vercel's $1M sandbox, @opencode's big week ends in a breach, @Ha](posts/infinitelogins/2026-10-19-2112170733228966180.md)
- [@infosec_au — 2025-12-05 — Pushed a new update to https://github.com/assetnote/react2shell-scanner -- it now scans fo](posts/infosec_au/2025-12-05-1996737719356297595.md)
- [@infosec_au — 2026-06-25 — i always find that the more obscure the industry and niche is, the more vulnerable the softwa](posts/infosec_au/2026-06-25-2070108885529378882.md)
- [@infosec_au — 2026-07-14 — Our research team at @SLCyberSec discovered a pre-auth RCE in ServiceNow by bypassing their s](posts/infosec_au/2026-07-14-2076989533850362149.md)
- [@infosec_au — 2026-07-18 — Note on WordPress pre-auth RCE (CVE-2026-63030). There are SQLi poc's out there, but RCE PoC ](posts/infosec_au/2026-07-18-2078334919307374599.md)
- [@infosec_au — 2026-09-09 — A few months ago, @SLCyberSec's research team took a look at Goja. It's a JavaScript engine t](posts/infosec_au/2026-09-09-2097644154465788209.md)
- [@j00ru — 2020-05-06 — Today I'm happy to release new research I've been working on for a while: 0-click RCE via MMS in a](posts/j00ru/2020-05-06-1258066559765004295.md)
- [@j00ru — 2020-07-28 — Trying hard to keep up the weekly cadence of the MMS series. Today we're finally moving to](posts/j00ru/2020-07-28-1288200298390081536.md)
- [@j00ru — 2020-08-12 — The final part 5 of my Samsung MMS exploit blog series is out 🎉 It covers bypassing Androi](posts/j00ru/2020-08-12-1293600839320428545.md)
- [@kevin_mizu — 2026-10-07 — I'm happy that my first article as part of the @SLCyberSec research team is finally out! 😁](posts/kevin_mizu/2026-10-07-2107783292091007306.md)
- [@orange_8361 — 2026-05-15 — And this one is human insight w/ LLM-assisted research. Took about one week to finish ever](posts/orange_8361/2026-05-15-2055330289652539850.md)
- [@samwcyo — 2026-11-07 — Had some time off of work and was finally able to release a few blog posts: the first is about a](posts/samwcyo/2026-11-07-2119030320171266117.md)

### Race condition (4)

- [@0xacb — 2026-11-03 — I was reading a blog on the "AI RCEssion" today, and it captures what happened during Octo](posts/0xacb/2026-11-03-2117647871285584365.md)
- [@j00ru — 2021-03-12 — Fixed this month: CVE-2021-26863, a race condition/use-after-free in win32k.sys demonstrat](posts/j00ru/2021-03-12-1370364905862352901.md)
- [@kevin_mizu — 2026-10-07 — I'm happy that my first article as part of the @SLCyberSec research team is finally out! 😁](posts/kevin_mizu/2026-10-07-2107783292091007306.md)
- [@mdp_sec — 2026-09-14 — So pushing 6 months now waiting on @intigriti](posts/mdp_sec/2026-09-14-2099392439853387918.md)

### Request smuggling / desync (2)

- [@albinowax — 2026-10-01 — SMTP smuggling is back! Dot-stuffing is a great find, awesome work! https://twitter.com/ti](posts/albinowax/2026-10-01-2105615340088762638.md)
- [@albinowax — 2026-10-13 — I've started a new research project for Black Hat USA 2027 and I'm pleased to announce it](posts/albinowax/2026-10-13-2110004455244505511.md)

### SQL injection (6)

- [@infinitelogins — 2026-05-09 — after escalating for hours today.. finally found my first bug bounty SQLi!! super excited](posts/infinitelogins/2026-05-09-2053257780895920586.md)
- [@infinitelogins — 2026-10-14 — I found a critical unauthenticated SQL injection that earned a $4,000 bounty. The WAF blo](posts/infinitelogins/2026-10-14-2110355630133322159.md)
- [@infosec_au — 2026-05-21 — We recently analyzed Drupal's security advisory (SA-CORE-2026-004 &amp; CVE-2026-9082). This ](posts/infosec_au/2026-05-21-2057484346093887921.md)
- [@infosec_au — 2026-07-18 — Note on WordPress pre-auth RCE (CVE-2026-63030). There are SQLi poc's out there, but RCE PoC ](posts/infosec_au/2026-07-18-2078334919307374599.md)
- [@mdp_sec — 2026-11-10 — i found an unauthed sql injection that let me pull customer pii and resume tokens off a public q](posts/mdp_sec/2026-11-10-2120066429223317560.md)
- [@ryotkak — 2026-07-17 — 【注意】WordPress本体において、未認証で任意コード実行に繋がる脆弱性が修正されています。](posts/ryotkak/2026-07-17-2078257717983236594.md)

### SSRF (2)

- [@NahamSec — 2026-11-02 — Someone found SSRF in MCP servers from Google and others. So I rebuilt the bug in a lab an](posts/NahamSec/2026-11-02-2117255416367517800.md)
- [@Piki_eth — 2026-10-26 — Found an SSRF vulnerability using FREE DeepSeek 😂🔥](posts/Piki_eth/2026-10-26-2114761602025304105.md)

### Smart contract / DeFi (39)

- [@ChainLight_io — 2025-03-31 — Which rug pulls, exploits, and security breaches happened this week?](posts/ChainLight_io/2025-03-31-1906729496440709516.md)
- [@Guhu95 — 2025-06-23 — Stared at the code so hard that a 5 year old bug crawled out.](posts/Guhu95/2025-06-23-1937016161847402638.md)
- [@Guhu95 — 2025-07-17 — There are just two types of bugs:](posts/Guhu95/2025-07-17-1945640502025752709.md)
- [@PwningEth — 2022-10-11 — White hat hackers are being exploited by defi projects @O3_Labs 👿](posts/PwningEth/2022-10-11-1579771011041734656.md)
- [@WhiteHatMage — 2026-10-23 — How lucrative would it be to build a tool that proves EVM contracts are free of asset thef](posts/WhiteHatMage/2026-10-23-2113630146053972258.md)
- [@anchabadze — 2026-10-22 — 🎯 Day 544 of my #RoadToWeb3SecurityJobChallenge](posts/anchabadze/2026-10-22-2113389416760721559.md)
- [@anchabadze — 2026-10-27 — 🎯 Day 549 of my #RoadToWeb3SecurityJobChallenge](posts/anchabadze/2026-10-27-2115200664594776559.md)
- [@anchabadze — 2026-10-29 — 🎯 Day 551 of my #RoadToWeb3SecurityJobChallenge](posts/anchabadze/2026-10-29-2115946842257310068.md)
- [@anchabadze — 2026-11-03 — 🎯 Day 555 of my #RoadToWeb3SecurityJobChallenge](posts/anchabadze/2026-11-03-2117421009079067074.md)
- [@anchabadze — 2026-11-03 — 🎯 Day 556 of my #RoadToWeb3SecurityJobChallenge](posts/anchabadze/2026-11-03-2117737221226971358.md)
- [@immunefi — 2026-10-19 — Security researcher @iguardz just earned $20,000 for a Critical Smart Contract bug.](posts/immunefi/2026-10-19-2112203877881991543.md)
- [@immunefi — 2026-10-26 — Security researcher @naresh_1337 just earned $25,000 for finding a critical smart contract](posts/immunefi/2026-10-26-2114677302378565786.md)
- [@immunefi — 2026-11-04 — This security researcher earned $33,000 for a high-severity bug in a blockchain’s core inf](posts/immunefi/2026-11-04-2117965345550172382.md)
- [@keterka — 2026-04-27 — Security researchers: which AI tools impressed you the most lately? What should I test nex](posts/keterka/2026-04-27-2048580338759155952.md)
- [@keterka — 2026-05-27 — Results are in for @monetrix_xyz  on @code4rena.](posts/keterka/2026-05-27-2059434905482740185.md)
- [@lonelysloth_sec — 2026-03-08 — I was starting to get hopeful about using Claude in some capacity in my work.](posts/lonelysloth_sec/2026-03-08-2030545303607329178.md)
- [@ma1fan — 2026-10-19 — Lol. Reported a smart contract compiler bug I assessed as Critical. Waited a month. The te](posts/ma1fan/2026-10-19-2112203544350880105.md)
- [@naresh_1337 — 2026-10-26 — 8 criticals, 2 highs, and still just getting started. 🔥](posts/naresh_1337/2026-10-26-2114804871002194359.md)
- [@saxenism — 2025-03-18 — Can't wait to take apart your vibe-coded smart contracts.](posts/saxenism/2025-03-18-1901959250441863561.md)
- [@saxenism — 2025-08-15 — All the Solidity auditors I know live a pretty straightforward life. Find bugs, get paid, log o](posts/saxenism/2025-08-15-1956418610785923159.md)
- [@saxenism — 2025-09-08 — Yeah, being a security researcher who can report smart contract bugs is cool](posts/saxenism/2025-09-08-1964933563138396345.md)
- [@saxenism — 2025-09-09 — Centralisation Risks.](posts/saxenism/2025-09-09-1965373469589377343.md)
- [@saxenism — 2025-10-11 — I remember writing a handy guide to handle oracle integrations in DeFi protocols and after toda](posts/saxenism/2025-10-11-1977025691393855714.md)
- [@saxenism — 2025-10-13 — I have audited DeFi protocols.](posts/saxenism/2025-10-13-1977693643881279717.md)
- [@saxenism — 2025-10-24 — This is just sad, and it makes me angry.](posts/saxenism/2025-10-24-1981646862269513949.md)
- [@saxenism — 2025-11-04 — Given the recent devastating @Balancer hack, I wanted to re-share something I wrote some time b](posts/saxenism/2025-11-04-1985612718318240076.md)
- [@saxenism — 2025-11-06 — This is a very relevant podcast around what our industry needs right now.](posts/saxenism/2025-11-06-1986312719675556162.md)
- [@saxenism — 2025-11-25 — Just wrapped an insane @EFDevconnect week in BA. I met a LOT of sharp people, and this time, a ](posts/saxenism/2025-11-25-1993323171915665895.md)
- [@saxenism — 2025-12-02 — Yoooooo!!!](posts/saxenism/2025-12-02-1995810425640829399.md)
- [@saxenism — 2026-02-09 — Good one, Paul!](posts/saxenism/2026-02-09-2020838088868495536.md)
- [@saxenism — 2026-02-09 — This is a take I strongly align with, because it clearly identifies why security is such a big ](posts/saxenism/2026-02-09-2020858473161031764.md)
- [@saxenism — 2026-03-11 — I spent 2 years on the ZKSync internal security team.](posts/saxenism/2026-03-11-2031696386388054029.md)
- [@saxenism — 2026-04-08 — Bullish on projects led by security-first founders.](posts/saxenism/2026-04-08-2041884341589123091.md)
- [@saxenism — 2026-04-27 — Another day, another hack.](posts/saxenism/2026-04-27-2048725225995681964.md)
- [@saxenism — 2026-04-28 — This is the exact shift that every protocol needs to make to survive in web3.](posts/saxenism/2026-04-28-2049136710169272562.md)
- [@saxenism — 2026-04-29 — The scary part is not “AI wrote bad Solidity” or that AI created old-school access control bugs](posts/saxenism/2026-04-29-2049401347414323288.md)
- [@saxenism — 2026-04-29 — Never a dull day in web3 🍿🍿](posts/saxenism/2026-04-29-2049554286527524892.md)
- [@saxenism — 2026-05-29 — I disagree with this statement, yet I understand why someone would say that.](posts/saxenism/2026-05-29-2060237102403702990.md)
- [@trust__90 — 2026-04-20 — CT focusing on the low-hanging fruit takes -](posts/trust__90/2026-04-20-2046203827305484565.md)

### TEE / enclave (64)

- [@asymmetric_re — 2026-07-09 — Anchor's release pipeline just got a major security upgrade.](posts/asymmetric_re/2026-07-09-2075265472107556875.md)
- [@jovanbulck — 2020-11-18 — Don't miss @FritzAlder presenting our latest work "Faulty Point Unit: ABI Poisoning Attacks o](posts/jovanbulck/2020-11-18-1329018922520219648.md)
- [@jovanbulck — 2020-12-03 — Happy we'll be organizing the 2nd ed. of a dedicated Hardware-Aided Trusted Computing Devroom](posts/jovanbulck/2020-12-03-1334531084973985801.md)
- [@jovanbulck — 2021-02-05 — Join us tomorrow for the 2nd open-source trusted computing devroom at #FOSDEM2021! Impress](posts/jovanbulck/2021-02-05-1357704326475579393.md)
- [@jovanbulck — 2021-12-06 — A viable free and open-source ecosystem will be instrumental to the success of emerging TE](posts/jovanbulck/2021-12-06-1467855660616454145.md)
- [@jovanbulck — 2022-02-04 — Reminder: join us tomorrow Saturday Feb 5 from 10:00 am UTC+1 for a full day of talks on the ](posts/jovanbulck/2022-02-04-1489603659352653832.md)
- [@jovanbulck — 2022-03-21 — Our #SysTEX22 opinion article: ABI sanitization in #IntelSGX runtimes is non-trivial and erro](posts/jovanbulck/2022-03-21-1505934847960924163.md)
- [@jovanbulck — 2023-11-26 — The future of #ConfidentialComputing is open source or is not! 🚀 Embrace the movement and](posts/jovanbulck/2023-11-26-1728777246226145386.md)
- [@jovanbulck — 2024-03-12 — Working in the area of trusted execution? Consider submitting your work (in progress), res](posts/jovanbulck/2024-03-12-1767608194220581358.md)
- [@saxenism — 2024-11-22 — And the TEE-fication of the world has started.](posts/saxenism/2024-11-22-1859897748620976548.md)
- [@saxenism — 2025-10-19 — I'm out here living in the streets of TEE security 24x7 now and it's so fun to see that the sam](posts/saxenism/2025-10-19-1979889414982815969.md)
- [@saxenism — 2025-10-21 — Is it just the TEE folks that are obsessed with acronyms or is it true for all hardware guys?](posts/saxenism/2025-10-21-1980531198880543062.md)
- [@saxenism — 2025-10-21 — It is absolutely wild to think that the automotive industry (yes, cars, honk honk cars) literal](posts/saxenism/2025-10-21-1980607414383812697.md)
- [@saxenism — 2025-10-22 — I've been pretty deep in TEE security research lately, and I came across this really fascinatin](posts/saxenism/2025-10-22-1980940485322813441.md)
- [@saxenism — 2025-10-23 — TEEs are truly fascinating.](posts/saxenism/2025-10-23-1981230974999630198.md)
- [@saxenism — 2025-10-27 — I am working on a comprehensive document around TEE security, which is a crystallisation of:](posts/saxenism/2025-10-27-1982697048018481438.md)
- [@saxenism — 2025-10-27 — If you are pretty deep in the TEE weeds or know someone who's a TEE chad, please hit me up.](posts/saxenism/2025-10-27-1982712368028393806.md)
- [@saxenism — 2025-10-29 — The recent  exploit brings to light the extremely nuanced and in general, hard nature of hardwa](posts/saxenism/2025-10-29-1983450406333370828.md)
- [@saxenism — 2025-10-29 — The stakes are getting higher.](posts/saxenism/2025-10-29-1983475396239667350.md)
- [@saxenism — 2025-11-06 — For the next TEE exploit research project, let's get Ethan Hunt onboard to make things a little](posts/saxenism/2025-11-06-1986468282875203883.md)
- [@saxenism — 2025-11-07 — Just to be very clear, I am not associated with this token or whatever this is, in any way, sha](posts/saxenism/2025-11-07-1986757151935844613.md)
- [@saxenism — 2025-11-13 — Draft for the "TEE Security Doc" has been sent out to folks who expressed interest yesterday.](posts/saxenism/2025-11-13-1989031021493514557.md)
- [@saxenism — 2025-11-16 — The TEE security handbook is live now.](posts/saxenism/2025-11-16-1990004582781776169.md)
- [@saxenism — 2025-11-17 — Probably cause dStack was reviewed in detail in the TEE Security Handbook 👀](posts/saxenism/2025-11-17-1990286956698411485.md)
- [@saxenism — 2025-11-17 — We released the TEE Security Handbook yesterday, and we already have the next update XD.](posts/saxenism/2025-11-17-1990559763470426559.md)
- [@saxenism — 2025-11-25 — Just wrapped an insane @EFDevconnect week in BA. I met a LOT of sharp people, and this time, a ](posts/saxenism/2025-11-25-1993323171915665895.md)
- [@saxenism — 2025-11-27 — The next update to the TEE Security Handbook is live.](posts/saxenism/2025-11-27-1993877018530709908.md)
- [@saxenism — 2025-12-02 — Yoooooo!!!](posts/saxenism/2025-12-02-1995810425640829399.md)
- [@saxenism — 2025-12-02 — Excuse me wtf… the TEE Security Handbook is already popping up inside real audits?](posts/saxenism/2025-12-02-1995868306213859600.md)
- [@saxenism — 2025-12-03 — You can absolutely get started with building on TEEs with a few clicks (AWS Nitro enclaves or s](posts/saxenism/2025-12-03-1996201500289515687.md)
- [@saxenism — 2025-12-06 — JORAN HONIG just gave a shoutout to the TEE Security Handbook.](posts/saxenism/2025-12-06-1997199723502227719.md)
- [@saxenism — 2025-12-10 — It's so fascinating to see when I am introducing TEEs to my web3 frens.](posts/saxenism/2025-12-10-1998596334174220742.md)
- [@saxenism — 2025-12-11 — Building the TEE Security Handbook has been one of the most rewarding things I've done.](posts/saxenism/2025-12-11-1999148671393513589.md)
- [@saxenism — 2025-12-12 — A critical systemic risk that I see missing from TEE-heavy protocol architectures is: fallbacks](posts/saxenism/2025-12-12-1999355134451810809.md)
- [@saxenism — 2025-12-13 — I think this depends heavily on how TEEs are used.](posts/saxenism/2025-12-13-1999738517942067332.md)
- [@saxenism — 2025-12-13 — Again, designing around availability for TEE-based protocols is a MUST.](posts/saxenism/2025-12-13-1999872692170990022.md)
- [@saxenism — 2025-12-16 — The top players in the space are already leveraging the TEE Security Handbook and you still don](posts/saxenism/2025-12-16-2000784093542498351.md)
- [@saxenism — 2025-12-16 — So... I have made a decision.](posts/saxenism/2025-12-16-2000952055523934580.md)
- [@saxenism — 2025-12-20 — This is a pretty cool attempt by @MarlinProtocol  to address the availability concerns in any T](posts/saxenism/2025-12-20-2002311606752215253.md)
- [@saxenism — 2025-12-26 — Shoutout to @phoenixfrozen86 and @sha2nk_ for helping us improve the TEE Security Handbook.](posts/saxenism/2025-12-26-2004450666505556225.md)
- [@saxenism — 2025-12-31 — 10/10 advice for protocol development teams.](posts/saxenism/2025-12-31-2006278815706906732.md)
- [@saxenism — 2026-01-05 — At this point, I am basically codifying my approach to hunt down bugs in a TEE-powered protocol](posts/saxenism/2026-01-05-2008174074720391484.md)
- [@saxenism — 2026-01-09 — Please. If you're building TEE protocols, DO NOT discount microarchitectural side-channel explo](posts/saxenism/2026-01-09-2009518067144171826.md)
- [@saxenism — 2026-01-15 — might just fuck around and start bringing to you byte-sized educational TEE content that makes ](posts/saxenism/2026-01-15-2011816214235111766.md)
- [@saxenism — 2026-01-17 — Always wanted to get into TEEs but somehow never got to it?](posts/saxenism/2026-01-17-2012508901028069397.md)
- [@saxenism — 2026-01-19 — 1. If you're building with SGX, DO NOT let your "software mode" become a production footgun.](posts/saxenism/2026-01-19-2013146724269953380.md)
- [@saxenism — 2026-01-19 — Intel removed itself as the bottleneck in online verification paths when it started moving away](posts/saxenism/2026-01-19-2013186167974572348.md)
- [@saxenism — 2026-01-19 — With the sheer plethora of things that can (and do) go wrong when building TEE protocols, defen](posts/saxenism/2026-01-19-2013265943900647766.md)
- [@saxenism — 2026-01-20 — Let me get into the weeds here.](posts/saxenism/2026-01-20-2013567106416287821.md)
- [@saxenism — 2026-02-12 — Compromised and revoked TEE machines could pass dstack's attestation verification as perfectly ](posts/saxenism/2026-02-12-2021943382155899351.md)
- [@saxenism — 2026-03-13 — Reviewed the biggest TEE protocols in Web3 earlier this year.](posts/saxenism/2026-03-13-2032358750846144694.md)
- [@saxenism — 2026-03-18 — I do not believe in generic AI security tooling.](posts/saxenism/2026-03-18-2034198942385336442.md)
- [@saxenism — 2026-04-08 — Attackers are getting smarter, faster, and cheaper.](posts/saxenism/2026-04-08-2041890307814342940.md)
- [@saxenism — 2026-05-08 — Quick personal update:](posts/saxenism/2026-05-08-2052661168595243488.md)
- [@saxenism — 2026-06-17 — Tested the `codebase-memory-mcp` today with two of my specialist security agents:](posts/saxenism/2026-06-17-2067126654452027521.md)
- [@saxenism — 2026-06-23 — "Just a .pem in a public repo" is the trigger for sure, just not the bug.](posts/saxenism/2026-06-23-2069405688397447285.md)
- [@saxenism — 2026-06-23 — This question is pretty revealing, actually. It kinda validates the DEBUG/allowlist path.](posts/saxenism/2026-06-23-2069428511082004930.md)
- [@saxenism — 2026-08-05 — Brought to you by Bluethroat Labs!!](posts/saxenism/2026-08-05-2084983497228472669.md)
- [@saxenism — 2026-08-21 — Subliminal work.](posts/saxenism/2026-08-21-2090613761094946980.md)
- [@saxenism — 2026-10-06 — I am hiring a full-time, paid TEE security research intern at @bluethroat_labs.](posts/saxenism/2026-10-06-2107493319873798649.md)
- [@saxenism — 2026-10-12 — Gm everyone!!](posts/saxenism/2026-10-12-2109724464804164050.md)
- [@saxenism — 2026-10-14 — I started working on @bluethroat_labs with a special focus on TEEs bc of my personal TEE bull t](posts/saxenism/2026-10-14-2110449694971470215.md)
- [@saxenism — 2026-10-14 — I don’t know what exactly Venice and Turnkey offers in the inference side of things, but from m](posts/saxenism/2026-10-14-2110515192669102236.md)
- [@saxenism — 2026-10-23 — We are still accepting applications for the TEE Security internship at @bluethroat_labs.](posts/saxenism/2026-10-23-2113466402560692369.md)

### XSS (16)

- [@Suryesh_92 — 2026-01-24 — 2nd Bounty in 2026 🥳🥳🎉🎉🤑](posts/Suryesh_92/2026-01-24-2014855434696597734.md)
- [@fransrosen — 2023-12-08 — Here's an XSS-challenge taken from real life. Can you make it alert() on my origin? Send me y](posts/fransrosen/2023-12-08-1733004108448059677.md)
- [@fransrosen — 2023-12-15 — In the 🧵 below is the solution for the XSS-challenge I posted last Friday.](posts/fransrosen/2023-12-15-1735585892130005195.md)
- [@fransrosen — 2024-08-21 — I found a bug and made a XSS-challenge out of it:](posts/fransrosen/2024-08-21-1826303938888695892.md)
- [@fransrosen — 2024-08-27 — Here's the solution for the XSS-challenge from last week.](posts/fransrosen/2024-08-27-1828503460183941420.md)
- [@garethheyes — 2026-09-28 — Stuck inside a &lt;meta&gt; and angle brackets blocked?](posts/garethheyes/2026-09-28-2104571830950609102.md)
- [@garethheyes — 2026-09-30 — Chrome added a &lt;camera&gt; tag.](posts/garethheyes/2026-09-30-2105289062487855361.md)
- [@garethheyes — 2026-10-01 — Chrome's new &lt;microphone&gt; tag has something to say:](posts/garethheyes/2026-10-01-2105651444762481000.md)
- [@garethheyes — 2026-10-06 — Another XSS vector for our cheat sheet, this time using &lt;usermedia&gt;](posts/garethheyes/2026-10-06-2107463389039689908.md)
- [@garethheyes — 2026-10-13 — Safari wanted a decryption key. @AmirMSafari gave it alert(1).](posts/garethheyes/2026-10-13-2109999115841220737.md)
- [@garethheyes — 2026-10-19 — Six consuming tags. One Safari trick: &lt;select&gt;.](posts/garethheyes/2026-10-19-2112174430696722645.md)
- [@garethheyes — 2026-10-27 — XSS from a response header 🤯](posts/garethheyes/2026-10-27-2115088588874650054.md)
- [@infinitelogins — 2026-10-19 — PwnEscape escapes KVM in Vercel's $1M sandbox, @opencode's big week ends in a breach, @Ha](posts/infinitelogins/2026-10-19-2112170733228966180.md)
- [@infosec_au — 2026-05-22 — Adam (@hash_kitten) posted the solution for the XSS challenge he made earlier in the week on ](posts/infosec_au/2026-05-22-2057714139091579022.md)
- [@kevin_mizu — 2026-07-21 — Chrome keeps adding fun features!](posts/kevin_mizu/2026-07-21-2079553635470430622.md)
- [@kevin_mizu — 2026-10-28 — With @hash_kitten, we've been looking into Cloudflare's /cdn-cgi/image endpoint and manage](posts/kevin_mizu/2026-10-28-2115448862869500312.md)

### ZK (41)

- [@0xiczc — 2023-02-14 — I'm delighted to have participated in the Audit Contest on  @secure3io! And thanks for the](posts/0xiczc/2023-02-14-1625325970269048832.md)
- [@0xiczc — 2023-05-26 — 1/ Recently, I discovered a vulnerability in the  @0xPolygon zkEVM and earned my first L2](posts/0xiczc/2023-05-26-1662090451493740545.md)
- [@ChainLight_io — 2025-04-21 — Which rug pulls, exploits, and security breaches happened this week?](posts/ChainLight_io/2025-04-21-1914325760921489673.md)
- [@Suryesh_92 — 2026-01-19 — Yay, I rewarded 1500 CHF ===  $1877 🤑🤑🤩🤩🔥🥳🥳🥳](posts/Suryesh_92/2026-01-19-2013196581994946685.md)
- [@lonelysloth_sec — 2026-06-05 — My take on the Zcash bug.](posts/lonelysloth_sec/2026-06-05-2062916729676648907.md)
- [@saxenism — 2024-11-12 — Say it one more time!!](posts/saxenism/2024-11-12-1856381181723550120.md)
- [@saxenism — 2024-11-12 — Meeting a lot of people especially security researchers that want to get deeper into the trench](posts/saxenism/2024-11-12-1856406690796822859.md)
- [@saxenism — 2024-11-13 — Custom handmade merch from @cryptobuilder_ made the entire PlonkcafÉ worth it for me!!!](posts/saxenism/2024-11-13-1856663449256014033.md)
- [@saxenism — 2024-11-14 — From my understanding of the current crypto landscape, atleast two innovations from our industr](posts/saxenism/2024-11-14-1857009806059483357.md)
- [@saxenism — 2024-11-18 — This is an 8x -&gt; 56x improvement.](posts/saxenism/2024-11-18-1858465176124883427.md)
- [@saxenism — 2024-11-19 — Clocked a CRAZY REALISATION about ZkVMs.](posts/saxenism/2024-11-19-1858795693663764568.md)
- [@saxenism — 2024-11-21 — Just a friendly reminder to all my security frens that the 500k USD UNCONDITIONAL pot from @zks](posts/saxenism/2024-11-21-1859639846773588087.md)
- [@saxenism — 2024-11-22 — Yesterday I had someone ask, what excites me about ZKsync.](posts/saxenism/2024-11-22-1860029810908758444.md)
- [@saxenism — 2024-11-22 — Be a Chad like @giovannidisiena &amp; follow in his footsteps!](posts/saxenism/2024-11-22-1860059201655144505.md)
- [@saxenism — 2024-11-29 — Even a 5-year-old, but thoroughly written blog with no fluff and just the right amount of abstr](posts/saxenism/2024-11-29-1862427834394059203.md)
- [@saxenism — 2024-12-13 — Same.](posts/saxenism/2024-12-13-1867571600234803463.md)
- [@saxenism — 2024-12-16 — Not a top signal.](posts/saxenism/2024-12-16-1868664881546670214.md)
- [@saxenism — 2024-12-19 — Not a top signal.](posts/saxenism/2024-12-19-1869840092325654824.md)
- [@saxenism — 2025-01-23 — Finally Ethereum is onto what ZKsync had already been doing.](posts/saxenism/2025-01-23-1882267577730424973.md)
- [@saxenism — 2025-03-21 — So, why should you be bullish on @zksync](posts/saxenism/2025-03-21-1902986611564089800.md)
- [@saxenism — 2025-08-14 — ===Leaving Matter Labs / ZKSync===](posts/saxenism/2025-08-14-1955944994025390288.md)
- [@saxenism — 2025-08-21 — This is some seriously cool stuff.](posts/saxenism/2025-08-21-1958511052867404006.md)
- [@saxenism — 2025-08-22 — A rather elaborate hack/drain attempt on me](posts/saxenism/2025-08-22-1958796012115640471.md)
- [@saxenism — 2025-10-13 — I'm a firm believer in Zipf’s Law of Least Effort.](posts/saxenism/2025-10-13-1977737681778946484.md)
- [@saxenism — 2025-11-12 — This dinner is definitely going to be a banger.](posts/saxenism/2025-11-12-1988601398054015282.md)
- [@saxenism — 2026-01-20 — Let me get into the weeds here.](posts/saxenism/2026-01-20-2013567106416287821.md)
- [@saxenism — 2026-01-20 — Top-down learning for me, ALWAYS.](posts/saxenism/2026-01-20-2013594786469712183.md)
- [@saxenism — 2026-01-29 — This cat got some serious zk and growth chops!!](posts/saxenism/2026-01-29-2016801638334226795.md)
- [@saxenism — 2026-03-11 — I spent 2 years on the ZKSync internal security team.](posts/saxenism/2026-03-11-2031696386388054029.md)
- [@saxenism — 2026-04-27 — Another day, another hack.](posts/saxenism/2026-04-27-2048725225995681964.md)
- [@saxenism — 2026-04-28 — In the era of AI, clear thinkers will absolutely melt faces.](posts/saxenism/2026-04-28-2049095534863098076.md)
- [@saxenism — 2026-06-23 — "Just a .pem in a public repo" is the trigger for sure, just not the bug.](posts/saxenism/2026-06-23-2069405688397447285.md)
- [@saxenism — 2026-06-23 — This question is pretty revealing, actually. It kinda validates the DEBUG/allowlist path.](posts/saxenism/2026-06-23-2069428511082004930.md)
- [@saxenism — 2026-06-24 — Recently I've started to get deeper into AI.](posts/saxenism/2026-06-24-2069674104328990852.md)
- [@saxenism — 2026-09-10 — That's a fun way to teach people about under constrained soundness bugs in zk circuits.](posts/saxenism/2026-09-10-2098041491939848235.md)
- [@zksecurityXYZ — 2026-10-11 — zknews now has tags, including supply chain security :)](posts/zksecurityXYZ/2026-10-11-2109314817500827950.md)
- [@zksecurityXYZ — 2026-10-16 — We're proud to announce the release of zkao version 3, the most powerful zkao update we've](posts/zksecurityXYZ/2026-10-16-2110927385868571017.md)
- [@zksecurityXYZ — 2026-10-21 — we packed the last zk podcast with zksecurity folks! mathias, giorgio, nico, and kobi talk](posts/zksecurityXYZ/2026-10-21-2112911877403758680.md)
- [@zksecurityXYZ — 2026-10-25 — New https://zk.golf challenge ⛳️ Google ID Token Claims Extraction.](posts/zksecurityXYZ/2026-10-25-2114284396450893976.md)
- [@zksecurityXYZ — 2026-10-28 — latest zk report mentions our work on https://zk.golf and https://better.codes! https://tw](posts/zksecurityXYZ/2026-10-28-2115470138355138982.md)
- [@zksecurityXYZ — 2026-11-03 — evm.asm, our collaboration with EF on an e2e verified EVM implementation for zkVMs, now ha](posts/zksecurityXYZ/2026-11-03-2117550503060185134.md)

## By platform

### Researchers by platform (from profiles)

- **HackerOne:** [mdp_sec](researchers/mdp_sec.md), [samwcyo](researchers/samwcyo.md), [NahamSec](researchers/NahamSec.md), [fransrosen](researchers/fransrosen.md), [Rhynorater](researchers/Rhynorater.md), [zseano](researchers/zseano.md), [galnagli](researchers/galnagli.md), [xssdoctor](researchers/xssdoctor.md), [S1r1u5_](researchers/S1r1u5_.md), [kevin_mizu](researchers/kevin_mizu.md), [ajxchapman](researchers/ajxchapman.md), [0xacb](researchers/0xacb.md)
- **Bugcrowd:** [mdp_sec](researchers/mdp_sec.md), [NahamSec](researchers/NahamSec.md), [Rhynorater](researchers/Rhynorater.md), [galnagli](researchers/galnagli.md)
- **Immunefi:** [PwningEth](researchers/PwningEth.md), [0xriptide](researchers/0xriptide.md), [trust__90](researchers/trust__90.md), [asymmetric_re](researchers/asymmetric_re.md), [WhiteHatMage](researchers/WhiteHatMage.md), [_blockian](researchers/_blockian.md), [ma1fan](researchers/ma1fan.md), [Guhu95](researchers/Guhu95.md), [0xiczc](researchers/0xiczc.md), [Shanon40439853](researchers/Shanon40439853.md), [saxenism](researchers/saxenism.md)
- **HackenProof:** [mdp_sec](researchers/mdp_sec.md), [bbarwik](researchers/bbarwik.md), [keterka](researchers/keterka.md), [anchabadze](researchers/anchabadze.md), [_blockian](researchers/_blockian.md)
- **Code4rena:** [trust__90](researchers/trust__90.md), [cmichelio](researchers/cmichelio.md), [keterka](researchers/keterka.md)
- **Sherlock:** [trust__90](researchers/trust__90.md)
- **Cantina:** [cmichelio](researchers/cmichelio.md)
- **Pwn2Own:** [orange_8361](researchers/orange_8361.md), [ryotkak](researchers/ryotkak.md)
- **Google Play:** [_bagipro](researchers/_bagipro.md)

_Original 19 researchers: see the Platforms column in [researchers.md](researchers.md)._

### Posts mentioning a platform

#### Platform: Bugcrowd (79)

- [@Assass1nmarcos — 2026-10-02 — I earned $8,000 for my submission on @bugcrowd #ItTakesACrowd](posts/Assass1nmarcos/2026-10-02-2106068361662922971.md)
- [@NahamSec — 2026-11-04 — Launched my hackbot at a new target on Bugcrowd at 11:09 and by 11:32 it had its first wor](posts/NahamSec/2026-11-04-2118067189576286345.md)
- [@Rhynorater — 2026-08-28 — I have actually been seeing really fast triage from both HackerOne and Bugcrowd lately. Se](posts/Rhynorater/2026-08-28-2093394741391999198.md)
- [@RootxRavi — 2026-06-16 — Which MacBook configuration do you think is ideal for full-time bug bounty hunting in 2026](posts/RootxRavi/2026-06-16-2066959135414055188.md)
- [@RootxRavi — 2026-07-01 — Finished #2 on the @Bugcrowd India Leaderboard for June! 🎉](posts/RootxRavi/2026-07-01-2072261644709986608.md)
- [@RootxRavi — 2026-08-01 — Finished #4 on the @Bugcrowd India Leaderboard for July! 🎉 [pic.x.com/EvVAiwYI2X]](posts/RootxRavi/2026-08-01-2083510058093326602.md)
- [@RootxRavi — 2026-08-05 — Finally made it into the Top 100 on @Bugcrowd](posts/RootxRavi/2026-08-05-2084992157388345591.md)
- [@RootxRavi — 2026-10-25 — P1 in 30 Sec🙃](posts/RootxRavi/2026-10-25-2114368791408947313.md)
- [@Suryesh_92 — 2026-06-22 — Just got my first Remote Code Execution report accepted. Found RCE directly in thick clien](posts/Suryesh_92/2026-06-22-2069043943640301896.md)
- [@Suryesh_92 — 2026-06-30 — Another Bounty 😉](posts/Suryesh_92/2026-06-30-2071781463767580756.md)
- [@Suryesh_92 — 2026-11-03 — Another new Thick Client finding accepted and rewarded.](posts/Suryesh_92/2026-11-03-2117598354641482125.md)
- [@SuyashS91823422 — 2026-10-29 — After 30+ Triaged Reports on @Bugcrowd, making a long-awaited comeback to @Hacker0x01](posts/SuyashS91823422/2026-10-29-2115710027713360150.md)
- [@SuyashS91823422 — 2026-11-03 — I was awarded $4500 Today on @Bugcrowd [pic.x.com/kdB3HcKNys]](posts/SuyashS91823422/2026-11-03-2117667516780777854.md)
- [@SuyashS91823422 — 2026-11-04 — I earned $2300 for my 3 submissions on @bugcrowd https://bugcrowd.com/h/{id: "suyash_tec](posts/SuyashS91823422/2026-11-04-2118048829715148801.md)
- [@SuyashS91823422 — 2026-11-05 — Finally after much hard work and consistency](posts/SuyashS91823422/2026-11-05-2118419045682926068.md)
- [@SuyashS91823422 — 2026-11-09 — I earned $2225 for my submissions on @bugcrowd https://bugcrowd.com/h/{id: "suyash_techn](posts/SuyashS91823422/2026-11-09-2119839963034669357.md)
- [@SuyashS91823422 — 2026-11-10 — Fast Triaged Keep it up @Bugcrowd [pic.x.com/1vXQHSXidz]](posts/SuyashS91823422/2026-11-10-2120089891610476947.md)
- [@SuyashS91823422 — 2026-11-11 — @mdp_sec @Bugcrowd Got bounty within 8 hrs 🫡](posts/SuyashS91823422/2026-11-11-2120398564870549635.md)
- [@Swartz068 — 2026-08-24 — 2 x Duplicate on @Bugcrowd](posts/Swartz068/2026-08-24-2091854507970081180.md)
- [@Swartz068 — 2026-09-10 — One more Triaged on @Bugcrowd](posts/Swartz068/2026-09-10-2098076274497626251.md)
- [@Swartz068 — 2026-09-29 — 3 reports Triaged today. Currently my 10 reports Successfully Triaged by Bugcrowd ASE Team](posts/Swartz068/2026-09-29-2104893407655305597.md)
- [@Swartz068 — 2026-10-08 — 10 reports triaged on a single program on @Bugcrowd. Now targeting 25 valid reports on thi](posts/Swartz068/2026-10-08-2108307317322379620.md)
- [@Swartz068 — 2026-10-15 — 11 reports triaged on the same target on @Bugcrowd.](posts/Swartz068/2026-10-15-2110728116180226209.md)
- [@Swartz068 — 2026-10-15 — @EliotGeo @Bugcrowd $0 , in Era of Ai &amp; automation I focusing on manual testing &amp;](posts/Swartz068/2026-10-15-2110784539757015170.md)
- [@Swartz068 — 2026-10-16 — @1111whiteGkep @Bugcrowd Target matter bro , I always choose wild card domain program](posts/Swartz068/2026-10-16-2110996965148266599.md)
- [@Swartz068 — 2026-10-20 — Meta’s Bug Bounty Program has been one of the worst in my experience regarding response ti](posts/Swartz068/2026-10-20-2112591482884628659.md)
- [@Swartz068 — 2026-10-31 — P3 to P2 on @Bugcrowd .](posts/Swartz068/2026-10-31-2116525685305139421.md)
- [@Swartz068 — 2026-11-02 — Bug Bounty Tip: Easy P3/P2](posts/Swartz068/2026-11-02-2117202589918114241.md)
- [@Swartz068 — 2026-11-02 — I earned $100 for my submission on @bugcrowd #ItTakesACrowd](posts/Swartz068/2026-11-02-2117294264254435641.md)
- [@Swartz068 — 2026-11-04 — Bug Bounty Tip #2: Old JS Secrets 🔍](posts/Swartz068/2026-11-04-2117931096726016043.md)
- [@infosec_au — 2026-06-12 —](posts/infosec_au/2026-06-12-2065233739710697756.md)
- [@krishnsec — 2026-08-13 — Made it into the Top 15 All-Time on @Bugcrowd](posts/krishnsec/2026-08-13-2087905595471139144.md)
- [@krishnsec — 2026-08-18 — Crossed 18K reputation on @Bugcrowd ✅](posts/krishnsec/2026-08-18-2089703314653089816.md)
- [@krishnsec — 2026-09-16 — Top 3 P1 Warrior globally on @Bugcrowd ✅](posts/krishnsec/2026-09-16-2100141425983881443.md)
- [@krishnsec — 2026-09-17 — August on @Bugcrowd 🏆](posts/krishnsec/2026-09-17-2100479403478417659.md)
- [@krishnsec — 2026-09-21 — Crossed 19K reputation on @Bugcrowd ✅](posts/krishnsec/2026-09-21-2102006855241482637.md)
- [@krishnsec — 2026-10-05 — September wrapped up with another #1 on the @Bugcrowd leaderboard &gt;&gt; [pic.x.com/XiO1](posts/krishnsec/2026-10-05-2106984299560124675.md)
- [@krishnsec — 2026-10-07 — Finally hit 20,000 reputation on @Bugcrowd A long journey and definitely not an easy miles](posts/krishnsec/2026-10-07-2107784924162093528.md)
- [@mdp_sec — 2026-07-27 — nice batch of payment thx @Bugcrowd](posts/mdp_sec/2026-07-27-2081605952554647944.md)
- [@mdp_sec — 2026-07-28 — This one was fun.](posts/mdp_sec/2026-07-28-2081892628996804623.md)
- [@mdp_sec — 2026-07-28 — #9 last month on @Bugcrowd](posts/mdp_sec/2026-07-28-2081998048683778456.md)
- [@mdp_sec — 2026-07-28 — Gotta love when contesting a downgraded rating swings your way.](posts/mdp_sec/2026-07-28-2082218685180400076.md)
- [@mdp_sec — 2026-07-30 — Zero bugs submitted this month...](posts/mdp_sec/2026-07-30-2082952213505397088.md)
- [@mdp_sec — 2026-07-31 — Gotta keep score.](posts/mdp_sec/2026-07-31-2083112167575015881.md)
- [@mdp_sec — 2026-08-03 — Look at these legends on @Bugcrowd](posts/mdp_sec/2026-08-03-2084147462554746943.md)
- [@mdp_sec — 2026-08-05 — Good start to the week :)](posts/mdp_sec/2026-08-05-2084934544004948361.md)
- [@mdp_sec — 2026-08-07 — Waited 2 months for this one..](posts/mdp_sec/2026-08-07-2085651486231630022.md)
- [@mdp_sec — 2026-08-18 — PoC video contains:](posts/mdp_sec/2026-08-18-2089543192463167889.md)
- [@mdp_sec — 2026-08-18 — Giving AI a bug bounty target is easy.](posts/mdp_sec/2026-08-18-2089584180497969222.md)
- [@mdp_sec — 2026-08-18 — Got invited to a private program for something I’ve used daily for years.](posts/mdp_sec/2026-08-18-2089839409881579826.md)
- [@mdp_sec — 2026-08-21 — V2 had the fix.](posts/mdp_sec/2026-08-21-2090672289625026872.md)
- [@mdp_sec — 2026-08-22 — One of the smaller things that made automated account creation more reliable was adding more tha](posts/mdp_sec/2026-08-22-2091302807479652372.md)
- [@mdp_sec — 2026-08-23 — One report has at least seven clocks:](posts/mdp_sec/2026-08-23-2091415699260637377.md)
- [@mdp_sec — 2026-08-26 — An API key in an APK can be limited, monitored, or designed for a public client.](posts/mdp_sec/2026-08-26-2092483261448724523.md)
- [@mdp_sec — 2026-08-27 — Before assigning severity, write seven facts:](posts/mdp_sec/2026-08-27-2092809905900261713.md)
- [@mdp_sec — 2026-08-28 — Most AI cybersecurity benchmarks answer the wrong question for bug-bounty hunters.](posts/mdp_sec/2026-08-28-2093342858501820901.md)
- [@mdp_sec — 2026-08-29 — Adding one dot segment turned an admin login redirect into HTTP 200.](posts/mdp_sec/2026-08-29-2093595999847731482.md)
- [@mdp_sec — 2026-09-01 — I have spent most of my time hunting on @Bugcrowd](posts/mdp_sec/2026-09-01-2094614973146448108.md)
- [@mdp_sec — 2026-09-01 — I post plenty about where bug bounty triage breaks.](posts/mdp_sec/2026-09-01-2094739133868769645.md)
- [@mdp_sec — 2026-09-03 — Busy month.](posts/mdp_sec/2026-09-03-2095365982349074744.md)
- [@mdp_sec — 2026-09-03 — I found a public OAuth client where any free account could read and write the production billing](posts/mdp_sec/2026-09-03-2095462761111388207.md)
- [@mdp_sec — 2026-09-04 — Bug bounty is moving toward an abundance problem.](posts/mdp_sec/2026-09-04-2095827649046466845.md)
- [@mdp_sec — 2026-09-06 — We all love free tokens right... If someone else pays for it. Found this one recently.](posts/mdp_sec/2026-09-06-2096462049857634733.md)
- [@mdp_sec — 2026-09-07 — Grinding way up on h1](posts/mdp_sec/2026-09-07-2097085872000864484.md)
- [@mdp_sec — 2026-09-08 — legit one thing I would love....](posts/mdp_sec/2026-09-08-2097223659488456988.md)
- [@mdp_sec — 2026-09-14 — Banger way to wake up :)](posts/mdp_sec/2026-09-14-2099587928418828750.md)
- [@mdp_sec — 2026-09-17 — I found a self-service login token that was forgeable for any user.](posts/mdp_sec/2026-09-17-2100438961256796461.md)
- [@mdp_sec — 2026-09-26 — RAR legit doesn't work](posts/mdp_sec/2026-09-26-2103729280572387523.md)
- [@mdp_sec — 2026-10-04 — hey @Bugcrowd recon you could look at these fam?](posts/mdp_sec/2026-10-04-2106583593871122473.md)
- [@mdp_sec — 2026-10-05 — I swear @Bugcrowd has a roulette wheel](posts/mdp_sec/2026-10-05-2107019197066998014.md)
- [@mdp_sec — 2026-10-05 — gotta love when PII is NA right...](posts/mdp_sec/2026-10-05-2107220037388120120.md)
- [@mdp_sec — 2026-10-07 — idk whats happening at @Bugcrowd](posts/mdp_sec/2026-10-07-2107955393251131511.md)
- [@mdp_sec — 2026-10-12 — Getting a proper response like this after a report is rewarded legit means a lot for hunters](posts/mdp_sec/2026-10-12-2109511254213849599.md)
- [@mdp_sec — 2026-10-19 — this goes straight back into tokens :)](posts/mdp_sec/2026-10-19-2112130274310099094.md)
- [@mdp_sec — 2026-10-30 — 13 payout emails tagged broken access control paid me $12,206](posts/mdp_sec/2026-10-30-2116080162349465978.md)
- [@mdp_sec — 2026-11-06 — $1,200 for a package name nobody had claimed. dependency confusion, my only paid supply chain bu](posts/mdp_sec/2026-11-06-2118803107119325691.md)
- [@mdp_sec — 2026-11-10 — looking for a few early testers for HuntDeck](posts/mdp_sec/2026-11-10-2119948851318784342.md)
- [@mdp_sec — 2026-11-11 — HuntDeck is live in demo mode 🎯](posts/mdp_sec/2026-11-11-2120371004916805916.md)
- [@mdp_sec — 2026-11-11 — RT @mdp_sec: HuntDeck is live in demo mode 🎯](posts/mdp_sec/2026-11-11-2120416381330170346.md)

#### Platform: Code4rena / Sherlock / Cantina (7)

- [@Guhu95 — 2025-12-30 — Glamsterdam upgrade contest rules wish-list🤞:](posts/Guhu95/2025-12-30-2005901452196421928.md)
- [@Guhu95 — 2026-02-26 — Looking at a live Ethereum Mainnet bug is an unforgettable experience.](posts/Guhu95/2026-02-26-2026925805176238370.md)
- [@Shanon40439853 — 2024-03-22 — My goal of the year was to spend more time on bug bounty https://twitter.com/cantinasecur](posts/Shanon40439853/2024-03-22-1771189328166764762.md)
- [@al_f4lc0n — 2026-09-03 — Regarding the recent attack on @injective, I want to make one thing very clear: this incid](posts/al_f4lc0n/2026-09-03-2095543489920483753.md)
- [@kankodu — 2026-01-16 — Here's where you can do some weekend bug hunting:](posts/kankodu/2026-01-16-2012219532056645916.md)
- [@keterka — 2026-04-27 — Security researchers: which AI tools impressed you the most lately? What should I test nex](posts/keterka/2026-04-27-2048580338759155952.md)
- [@keterka — 2026-05-27 — Results are in for @monetrix_xyz  on @code4rena.](posts/keterka/2026-05-27-2059434905482740185.md)

#### Platform: HackenProof (17)

- [@Piki_eth — 2026-08-28 — My local Qwen ran for 5 hours auditing a crypto project and found a strong DoS vulnerabili](posts/Piki_eth/2026-08-28-2093217981732171978.md)
- [@Piki_eth — 2026-09-01 — The best notification: “has been paid.” 💰](posts/Piki_eth/2026-09-01-2094790419410567631.md)
- [@Piki_eth — 2026-10-26 — Found an SSRF vulnerability using FREE DeepSeek 😂🔥](posts/Piki_eth/2026-10-26-2114761602025304105.md)
- [@Piki_eth — 2026-10-29 — Another bug bounty report triaged by HackenProof. 🔥](posts/Piki_eth/2026-10-29-2115783655092277530.md)
- [@Piki_eth — 2026-11-07 — Another critical report TRIAGED by HackenProof! 🔥](posts/Piki_eth/2026-11-07-2119008635946930555.md)
- [@Piki_eth — 2026-11-08 — Submitted another bug bounty report to HackenProof and got it TRIAGED in just 30 minutes.](posts/Piki_eth/2026-11-08-2119348331537396059.md)
- [@bbarwik — 2025-02-23 — I got my first bug bounty from @HackenProof. I'm officially starting my bug hunter journey](posts/bbarwik/2025-02-23-1893762330741117269.md)
- [@bbarwik — 2025-04-10 — Got another bug bounty on @HackenProof! My bug bounty journey continues 😁 My goal for this](posts/bbarwik/2025-04-10-1910367210859589907.md)
- [@bbarwik — 2025-04-18 — I've found another issue on @HackenProof! I'm getting closer to be in top 3 hackers on Hac](posts/bbarwik/2025-04-18-1913222803546943674.md)
- [@bbarwik — 2025-06-30 — I did it. I found first "real critical issue" on @HackenProof . I am looking forward to pr](posts/bbarwik/2025-06-30-1939604794684981576.md)
- [@bbarwik — 2025-07-30 — At 15:00 CET / 13:00 UTC I'm hosting a webinar about "Top 10 Attack Paths Your Devs Are Bl](posts/bbarwik/2025-07-30-1950512717103591696.md)
- [@keterka — 2026-08-09 — Hey, frens! Happy to share my latest @HackenProof results 🫡](posts/keterka/2026-08-09-2086493338140610908.md)
- [@keterka — 2026-10-30 — Finally, a win 🥇](posts/keterka/2026-10-30-2115961607679254802.md)
- [@keterka — 2026-10-30 — Hacker of the Week again 🔥](posts/keterka/2026-10-30-2116207308753547406.md)
- [@mdp_sec — 2026-07-29 — It's been very interesting working on @HackenProof](posts/mdp_sec/2026-07-29-2082542340225536300.md)
- [@saxenism — 2026-03-19 — Can someone help me w/ the said coupons?](posts/saxenism/2026-03-19-2034595139700871314.md)
- [@saxenism — 2026-10-17 — yo! is @HackenProof down?](posts/saxenism/2026-10-17-2111553272570089975.md)

#### Platform: HackerOne (64)

- [@Assass1nmarcos — 2026-03-30 — Yay, I was awarded a $5,000 bounty on @Hacker0x01! https://hackerone.com/assassin_marcos](posts/Assass1nmarcos/2026-03-30-2038648576335884461.md)
- [@Assass1nmarcos — 2026-07-08 — Hello @Hacker0x01,](posts/Assass1nmarcos/2026-07-08-2074871162035986895.md)
- [@Assass1nmarcos — 2026-10-01 — Yay, I was awarded a $10,000 bounty on @Hacker0x01! https://hackerone.com/assassin_marcos](posts/Assass1nmarcos/2026-10-01-2105768256917389365.md)
- [@Assass1nmarcos — 2026-10-02 — I earned $8,000 for my submission on @bugcrowd #ItTakesACrowd](posts/Assass1nmarcos/2026-10-02-2106068361662922971.md)
- [@Assass1nmarcos — 2026-10-12 — Yay, I was awarded a $7,200 bounty on @Hacker0x01! https://hackerone.com/assassin_marcos ](posts/Assass1nmarcos/2026-10-12-2109726553705959685.md)
- [@Assass1nmarcos — 2026-10-12 — Yay, I was awarded a $6,000 bounty on @Hacker0x01! https://hackerone.com/assassin_marcos ](posts/Assass1nmarcos/2026-10-12-2109728544893120639.md)
- [@Assass1nmarcos — 2026-10-15 — Yay, I was awarded a $12,500 bounty on @Hacker0x01!](posts/Assass1nmarcos/2026-10-15-2110759502081675582.md)
- [@Assass1nmarcos — 2026-10-20 — Yay, I was awarded a $6,421 bounty on @Hacker0x01!](posts/Assass1nmarcos/2026-10-20-2112550747087024581.md)
- [@Rhynorater — 2026-08-28 — I have actually been seeing really fast triage from both HackerOne and Bugcrowd lately. Se](posts/Rhynorater/2026-08-28-2093394741391999198.md)
- [@RootxRavi — 2026-06-16 — Which MacBook configuration do you think is ideal for full-time bug bounty hunting in 2026](posts/RootxRavi/2026-06-16-2066959135414055188.md)
- [@RootxRavi — 2026-08-10 — Recently started hunting on HackerOne. 🚀](posts/RootxRavi/2026-08-10-2086836477095469280.md)
- [@RootxRavi — 2026-08-13 — Yay, I was awarded a $1,500 bounty on @Hacker0x01! https://hackerone.com/rootxravi #Togeth](posts/RootxRavi/2026-08-13-2087876415006085516.md)
- [@RootxRavi — 2026-08-14 — Yay, I was awarded a $4,500 bounty on @Hacker0x01 ! https://hackerone.com/rootxravi #Toget](posts/RootxRavi/2026-08-14-2088272412072902705.md)
- [@RootxRavi — 2026-10-06 — Yay, I was awarded a $1,500 bounty on](posts/RootxRavi/2026-10-06-2107491994331423053.md)
- [@RootxRavi — 2026-10-31 — Yay, I was awarded a $10,250 bounty on @Hacker0x01! https://hackerone.com/rootxravi](posts/RootxRavi/2026-10-31-2116477287554232616.md)
- [@Suryesh_92 — 2026-06-22 — Just got my first Remote Code Execution report accepted. Found RCE directly in thick clien](posts/Suryesh_92/2026-06-22-2069043943640301896.md)
- [@Suryesh_92 — 2026-06-30 — Another Bounty 😉](posts/Suryesh_92/2026-06-30-2071781463767580756.md)
- [@Suryesh_92 — 2026-11-03 — Another new Thick Client finding accepted and rewarded.](posts/Suryesh_92/2026-11-03-2117598354641482125.md)
- [@SuyashS91823422 — 2026-10-29 — After 30+ Triaged Reports on @Bugcrowd, making a long-awaited comeback to @Hacker0x01](posts/SuyashS91823422/2026-10-29-2115710027713360150.md)
- [@Swartz068 — 2026-08-24 — 2 x Duplicate on @Bugcrowd](posts/Swartz068/2026-08-24-2091854507970081180.md)
- [@Swartz068 — 2026-09-10 — One more Triaged on @Bugcrowd](posts/Swartz068/2026-09-10-2098076274497626251.md)
- [@Swartz068 — 2026-10-15 — 11 reports triaged on the same target on @Bugcrowd.](posts/Swartz068/2026-10-15-2110728116180226209.md)
- [@Swartz068 — 2026-10-15 — @EliotGeo @Bugcrowd $0 , in Era of Ai &amp; automation I focusing on manual testing &amp;](posts/Swartz068/2026-10-15-2110784539757015170.md)
- [@Swartz068 — 2026-10-16 — @1111whiteGkep @Bugcrowd Target matter bro , I always choose wild card domain program](posts/Swartz068/2026-10-16-2110996965148266599.md)
- [@Swartz068 — 2026-10-31 — P3 to P2 on @Bugcrowd .](posts/Swartz068/2026-10-31-2116525685305139421.md)
- [@Swartz068 — 2026-11-02 — Bug Bounty Tip: Easy P3/P2](posts/Swartz068/2026-11-02-2117202589918114241.md)
- [@al_f4lc0n — 2026-06-03 — 3 tips for Bug Bounty Hunters:](posts/al_f4lc0n/2026-06-03-2062082215962366225.md)
- [@fransrosen — 2024-05-03 — If you ever wanted a video about live hacking including @JonathanBouman smashing a sign sayin](posts/fransrosen/2024-05-03-1786270442795241566.md)
- [@fransrosen — 2024-09-24 — I just won my 4th MVH at @Hacker0x01 H1-0131 in Scotland! 🤯 So sad I could not attend in p](posts/fransrosen/2024-09-24-1838679292189848033.md)
- [@infinitelogins — 2026-04-13 — Been a minute.](posts/infinitelogins/2026-04-13-2043552103076094169.md)
- [@infinitelogins — 2026-07-03 — For the first time in my life, I finished in the top 5 in the US on H1 for a quarter. Bug](posts/infinitelogins/2026-07-03-2073099379712671799.md)
- [@infinitelogins — 2026-10-19 — PwnEscape escapes KVM in Vercel's $1M sandbox, @opencode's big week ends in a breach, @Ha](posts/infinitelogins/2026-10-19-2112170733228966180.md)
- [@infosec_au — 2026-06-12 —](posts/infosec_au/2026-06-12-2065233739710697756.md)
- [@kevin_mizu — 2026-07-09 — It was a really fun event! Thanks to @Hacker0x01 and Salesforce for the invitation!](posts/kevin_mizu/2026-07-09-2075234997246496822.md)
- [@kevin_mizu — 2026-09-07 — A logical bug that I've reported to MariaDB has just been disclosed! 🎉](posts/kevin_mizu/2026-09-07-2097055819447550388.md)
- [@mdp_sec — 2026-07-31 — Gotta keep score.](posts/mdp_sec/2026-07-31-2083112167575015881.md)
- [@mdp_sec — 2026-08-18 — PoC video contains:](posts/mdp_sec/2026-08-18-2089543192463167889.md)
- [@mdp_sec — 2026-08-18 — Giving AI a bug bounty target is easy.](posts/mdp_sec/2026-08-18-2089584180497969222.md)
- [@mdp_sec — 2026-08-18 — Got invited to a private program for something I’ve used daily for years.](posts/mdp_sec/2026-08-18-2089839409881579826.md)
- [@mdp_sec — 2026-08-21 — V2 had the fix.](posts/mdp_sec/2026-08-21-2090672289625026872.md)
- [@mdp_sec — 2026-08-22 — One of the smaller things that made automated account creation more reliable was adding more tha](posts/mdp_sec/2026-08-22-2091302807479652372.md)
- [@mdp_sec — 2026-08-23 — One report has at least seven clocks:](posts/mdp_sec/2026-08-23-2091415699260637377.md)
- [@mdp_sec — 2026-08-26 — An API key in an APK can be limited, monitored, or designed for a public client.](posts/mdp_sec/2026-08-26-2092483261448724523.md)
- [@mdp_sec — 2026-08-27 — Before assigning severity, write seven facts:](posts/mdp_sec/2026-08-27-2092809905900261713.md)
- [@mdp_sec — 2026-08-28 — Most AI cybersecurity benchmarks answer the wrong question for bug-bounty hunters.](posts/mdp_sec/2026-08-28-2093342858501820901.md)
- [@mdp_sec — 2026-08-29 — Adding one dot segment turned an admin login redirect into HTTP 200.](posts/mdp_sec/2026-08-29-2093595999847731482.md)
- [@mdp_sec — 2026-09-01 — I have spent most of my time hunting on @Bugcrowd](posts/mdp_sec/2026-09-01-2094614973146448108.md)
- [@mdp_sec — 2026-09-01 — I post plenty about where bug bounty triage breaks.](posts/mdp_sec/2026-09-01-2094739133868769645.md)
- [@mdp_sec — 2026-09-03 — Busy month.](posts/mdp_sec/2026-09-03-2095365982349074744.md)
- [@mdp_sec — 2026-09-03 — I found a public OAuth client where any free account could read and write the production billing](posts/mdp_sec/2026-09-03-2095462761111388207.md)
- [@mdp_sec — 2026-09-04 — Bug bounty is moving toward an abundance problem.](posts/mdp_sec/2026-09-04-2095827649046466845.md)
- [@mdp_sec — 2026-09-06 — We all love free tokens right... If someone else pays for it. Found this one recently.](posts/mdp_sec/2026-09-06-2096462049857634733.md)
- [@mdp_sec — 2026-09-07 — Grinding way up on h1](posts/mdp_sec/2026-09-07-2097085872000864484.md)
- [@mdp_sec — 2026-09-08 — legit one thing I would love....](posts/mdp_sec/2026-09-08-2097223659488456988.md)
- [@mdp_sec — 2026-09-17 — I found a self-service login token that was forgeable for any user.](posts/mdp_sec/2026-09-17-2100438961256796461.md)
- [@mdp_sec — 2026-09-26 — Gotta love all them @Hacker0x01 invites](posts/mdp_sec/2026-09-26-2103961764711027026.md)
- [@mdp_sec — 2026-10-12 — Getting a proper response like this after a report is rewarded legit means a lot for hunters](posts/mdp_sec/2026-10-12-2109511254213849599.md)
- [@mdp_sec — 2026-10-19 — this goes straight back into tokens :)](posts/mdp_sec/2026-10-19-2112130274310099094.md)
- [@mdp_sec — 2026-10-30 — 13 payout emails tagged broken access control paid me $12,206](posts/mdp_sec/2026-10-30-2116080162349465978.md)
- [@mdp_sec — 2026-11-05 — $8,000 for an auth bypass](posts/mdp_sec/2026-11-05-2118435683329310786.md)
- [@zseano — 2026-06-02 — can we get more context on this @Hacker0x01 @senorarroz ? :D](posts/zseano/2026-06-02-2061898249439515121.md)
- [@zseano — 2026-10-01 — some data if you're curious on active *PUBLIC* programs on hackerone :) some insight into](posts/zseano/2026-10-01-2105766060398162315.md)
- [@zseano — 2026-10-04 — Damn how does h1 have bugs like this 🫠](posts/zseano/2026-10-04-2106711601223180342.md)
- [@zseano — 2026-10-28 — Expedia Group Program has gone from $21k bounties paid to $250k in just 2 months. Seems pe](posts/zseano/2026-10-28-2115577340273066390.md)

#### Platform: Immunefi (49)

- [@0xiczc — 2023-05-26 — 1/ Recently, I discovered a vulnerability in the  @0xPolygon zkEVM and earned my first L2](posts/0xiczc/2023-05-26-1662090451493740545.md)
- [@0xvivekd — 2026-03-17 — I just found a confirmed bug on @immunefi #immunefitribe https://immunefi.com/s/ss/?severi](posts/0xvivekd/2026-03-17-2033863076022522192.md)
- [@0xvivekd — 2026-04-20 — I just found a confirmed bug on @immunefi #immunefitribe https://immunefi.com/s/ss/?severi](posts/0xvivekd/2026-04-20-2046273710471180392.md)
- [@0xvivekd — 2026-07-20 — I just found a confirmed bug on @immunefi #immunefitribe https://immunefi.com/s/ss/?severi](posts/0xvivekd/2026-07-20-2079252344894832652.md)
- [@0xvivekd — 2026-07-27 — I just found a bug and got paid on @immunefi #immunefitribe https://immunefi.com/s/ss/?sev](posts/0xvivekd/2026-07-27-2081734637991440850.md)
- [@0xvivekd — 2026-08-20 — I just found a bug and got paid on @immunefi #immunefitribe https://immunefi.com/s/ss/?sev](posts/0xvivekd/2026-08-20-2090389092735603101.md)
- [@0xvivekd — 2026-09-03 — I just found a bug and got paid on @immunefi #immunefitribe https://immunefi.com/s/ss/?sev](posts/0xvivekd/2026-09-03-2095544239220470026.md)
- [@0xvivekd — 2026-09-09 — I just found a bug and got paid on @immunefi #immunefitribe https://immunefi.com/s/ss/?sev](posts/0xvivekd/2026-09-09-2097698749468578021.md)
- [@0xvivekd — 2026-10-05 — I just found a confirmed bug on @immunefi #immunefitribe https://immunefi.com/s/ss/?severi](posts/0xvivekd/2026-10-05-2107115801455276191.md)
- [@0xvivekd — 2026-10-12 — I just found a bug and got paid on @immunefi #immunefitribe https://immunefi.com/s/ss/?sev](posts/0xvivekd/2026-10-12-2109689569298051337.md)
- [@Guhu95 — 2025-06-23 — Stared at the code so hard that a 5 year old bug crawled out.](posts/Guhu95/2025-06-23-1937016161847402638.md)
- [@KeiZo_Zo — 2026-07-10 — I've been doing extensive research on AI "led" bug bounty hunting since the beginning of M](posts/KeiZo_Zo/2026-07-10-2075628283027234941.md)
- [@Kiki_developer — 2026-01-29 — I just found a bug and got paid on @immunefi #immunefitribe https://immunefi.com/s/ss/?se](posts/Kiki_developer/2026-01-29-2016898778209669412.md)
- [@PwningEth — 2022-10-11 — White hat hackers are being exploited by defi projects @O3_Labs 👿](posts/PwningEth/2022-10-11-1579771011041734656.md)
- [@Shanon40439853 — 2023-10-14 — Really lucky to spot this issue. Thanks @Balancer and @immunefi  for treating wh like thi](posts/Shanon40439853/2023-10-14-1713056980510851327.md)
- [@Shanon40439853 — 2023-12-13 — When doing bug bounties on Immunefi, I find it easier to find issues on a codebase that w](posts/Shanon40439853/2023-12-13-1734801151495926098.md)
- [@Shanon40439853 — 2024-01-03 — All my reports were paid in 2023.](posts/Shanon40439853/2024-01-03-1742433339666219379.md)
- [@WhiteHatMage — 2026-10-13 — Quick thoughts on the events I missed over the past two months:](posts/WhiteHatMage/2026-10-13-2110119559600517319.md)
- [@_blockian — 2025-03-19 — Don’t forget to use falmal velification in your audits, this is the only way to find those](posts/_blockian/2025-03-19-1902372726997741905.md)
- [@_blockian — 2025-04-07 — Unlocking our skills section on our Immunefi profile! #ImmunefiUnlocked @immunefi https://](posts/_blockian/2025-04-07-1909341705058333155.md)
- [@_blockian — 2025-04-17 — Just reached rank 30 on @immunefi all-time!](posts/_blockian/2025-04-17-1912804911219147045.md)
- [@al_f4lc0n — 2026-03-15 — I Saved Injective's $500M. They Pay Me $50K.](posts/al_f4lc0n/2026-03-15-2033110168045568434.md)
- [@al_f4lc0n — 2026-03-18 — the figures referenced in the post are entirely misleading. There was no impact realized f](posts/al_f4lc0n/2026-03-18-2034125406748741827.md)
- [@al_f4lc0n — 2026-09-03 — Regarding the recent attack on @injective, I want to make one thing very clear: this incid](posts/al_f4lc0n/2026-09-03-2095543489920483753.md)
- [@bluethroat_labs — 2026-10-01 — Bounty #9 on @immunefi is extremely special for us.](posts/bluethroat_labs/2026-10-01-2105581456550461936.md)
- [@bluethroat_labs — 2026-10-06 — Bounty #10 on @immunefi stems from the same root as #9.](posts/bluethroat_labs/2026-10-06-2107490499305124027.md)
- [@bluethroat_labs — 2026-10-09 — Bounty #11 on @immunefi was downgraded from a Critical to a High due to a contrived trig](posts/bluethroat_labs/2026-10-09-2108575109535433161.md)
- [@bluethroat_labs — 2026-11-07 — We are happy and proud to announce that we have moved to the 4th place on the @immunefi ](posts/bluethroat_labs/2026-11-07-2119030716373832154.md)
- [@immunefi — 2026-06-16 — This Security Researcher has earned $1,073,742 on Immunefi in 2026.](posts/immunefi/2026-06-16-2066898721523028465.md)
- [@immunefi — 2026-09-24 — Security researcher @brandon_shi just found a critical vulnerability, netting him a $50k b](posts/immunefi/2026-09-24-2103156012798869539.md)
- [@immunefi — 2026-10-13 — Security researcher @GuplerSaxanoid just earned $30,000 for finding a critical vulnerabili](posts/immunefi/2026-10-13-2109982938578522400.md)
- [@immunefi — 2026-10-19 — Security researcher @iguardz just earned $20,000 for a Critical Smart Contract bug.](posts/immunefi/2026-10-19-2112203877881991543.md)
- [@immunefi — 2026-10-26 — Security researcher @naresh_1337 just earned $25,000 for finding a critical smart contract](posts/immunefi/2026-10-26-2114677302378565786.md)
- [@immunefi — 2026-10-28 — Security team @bluethroat_labs just earned a whopping $50,000 bounty for finding a critica](posts/immunefi/2026-10-28-2115411377557062016.md)
- [@immunefi — 2026-11-04 — This security researcher earned $33,000 for a high-severity bug in a blockchain’s core inf](posts/immunefi/2026-11-04-2117965345550172382.md)
- [@lonelysloth_sec — 2025-12-07 — Bug bounty income variance is sometimes hard to grasp.](posts/lonelysloth_sec/2025-12-07-1997709908834439182.md)
- [@lonelysloth_sec — 2026-06-05 — My take on the Zcash bug.](posts/lonelysloth_sec/2026-06-05-2062916729676648907.md)
- [@naresh_1337 — 2026-08-24 — I just found a confirmed bug on @immunefi #immunefitribe https://immunefi.com/s/ss/?severi](posts/naresh_1337/2026-08-24-2091908429119983811.md)
- [@naresh_1337 — 2026-09-23 — Huge thanks to @immunefi and @QuantusNetwork for the recognition. 🫡](posts/naresh_1337/2026-09-23-2102840461430005790.md)
- [@naresh_1337 — 2026-09-24 — @defijangle @Destinyxeiiios1 @immunefi @QuantusNetwork Appreciate it 🫡 Glad I could help h](posts/naresh_1337/2026-09-24-2103196335851614609.md)
- [@naresh_1337 — 2026-10-21 — Another finding, another milestone. The hunt continues......](posts/naresh_1337/2026-10-21-2112901217278214612.md)
- [@naresh_1337 — 2026-10-26 — 8 criticals, 2 highs, and still just getting started. 🔥](posts/naresh_1337/2026-10-26-2114804871002194359.md)
- [@samwcyo — 2026-10-18 — I’d be willing to pay $100 per report for priority triage with automated dupe checking and](posts/samwcyo/2026-10-18-2111805910448529757.md)
- [@saxenism — 2026-07-17 — Now Immunefi tells you exactly how long ago the original report was filed in case your report i](posts/saxenism/2026-07-17-2077976177676112161.md)
- [@saxenism — 2026-08-13 — People whose primary definition of a bug bounty platform is @immunefi seriously have no idea ho](posts/saxenism/2026-08-13-2087756149605150865.md)
- [@saxenism — 2026-10-14 — Thank you @immunefi for sponsoring my SF visit :)](posts/saxenism/2026-10-14-2110421403757679016.md)
- [@saxenism — 2026-10-15 — Thanks for upgrading my stay in SF @immunefi](posts/saxenism/2026-10-15-2110856315858014334.md)
- [@saxenism — 2026-11-07 — A bunch of bounties just got processed and now @bluethroat_labs is #4 on the 90 days Immunefi l](posts/saxenism/2026-11-07-2118914993630630057.md)
- [@saxenism — 2026-11-08 — Oh and btw this is BESIDES the fuckton of bugs that we have found, validated, reported and help](posts/saxenism/2026-11-08-2119310072182653174.md)

## Harness layer (for the no-X hunting agent)

Machine-readable + check-spec material lives under [`harness/`](harness/):

- [`harness/findings.jsonl`](harness/findings.jsonl) — **1,047** documented findings (web BB, smart-contract, ZK, TEE, Zcash/Ethereum/Solana advisories, RustSec crypto, Solidity compiler bugs, plus 641 verbatim Telegram-sourced records).
- [`harness/bug-classes/`](harness/bug-classes/) — 36 class check-specs.
- [`harness/payloads/`](harness/payloads/) — verbatim payloads per class (16 files).
- [`harness/tools.md`](harness/tools.md) — tools researchers actually mention and how they used them.
- [`harness/recon-methodology.md`](harness/recon-methodology.md) — phased recon (Marius prompt pack backbone).

