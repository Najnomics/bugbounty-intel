# Sources log

Everything consulted while building this knowledge base. **Consulted** dates are 11 November 2026 (Africa/Lagos) unless noted. **Published** dates are converted to WAT when the source was an X post with a UTC timestamp.

X data came from the public-read `x` MCP tools (`get_users_by_usernames`, `get_posts_by_ids`, `get_users_posts`, `search_posts_all`). Web pages were fetched or summarized via WebSearch / WebFetch. No posts were liked, reposted, or replied to.

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

- **X:** Full-archive search of all watched handles since the 15 Nov run. **112** new posts ingested into `store.json` / `data/x_posts.jsonl`; 16 new security-relevant verbatim files + 2 regenerated (mdp_sec ×9: MCP presence-only bearer auth bypass $5k, unauthenticated file API, open data server (dupe), perk-mint logic, DeepSeek 0-refusals harness note, HuntDeck, Lovable; plus Swartz068, naresh_1337 (Immunefi High confirmed), saxenism, zksecurityXYZ Collision Atlas, Neodyme, usmannk, KeiZo_Zo). 32 posts refetched by id to recover entities/conversation ids. Backfill pass 6: cursors n6a–n6e, **+605** new archive posts (ARCHIVE 15,856 → 16,679); n6d closed DONE (low yield).
- **Telegram:** @defendor_eng +4 (ids 2346–2349: $1.2B DOJ seizure, FBI FaceStealer warning, WillPapper five years of formal verification, Proxima 5,324 SOL loss via SigNoz-exposed private keys); @dailybountywriteup +1 (id 14985). Writeups: defendor +74 (1 new-msg + 73 backlog incl. 3 via Medium RSS mirror, 3 x.com posts via X API) → 246 fetched / 190 failed / 77 pending; dailybounty +168 (9 new-msg, 91 backlog, 68 retry; 76 via Medium RSS mirror) → 933 fetched / 1,133 failed / 10,842 pending.
- **HackerOne:** +3 disclosed — [#3966160](hackerone/reports/2026/3966160.md) Arc RPC node termination via custom JS tracer (Boa) DoS; [#4059744](hackerone/reports/2026/4059744.md) Weblate anonymous API rate-limit bypass via X-Forwarded-For; [#4117330](hackerone/reports/2026/4117330.md) Weblate anonymous suggestion IP exposure via Change API. `harness/findings.jsonl` +600 H1 + 6 manual entries.
- **CVE:** cvelistV5 delta since 2026-11-15T03:15:17Z — **106 new / 15 updated**; NVD lastMod delta 110 new / 11 updated; KEV unchanged; GHSA unchanged (37,810); OSV +42 (23,843); ZDI +56 advisories (17,417 total); Google Project Zero +1 ([disclosure-policy post](cves/google-project-zero/blog/2026_11_disclosure-policy.md)); Exploit-DB / kernel CNA no change.
- **Projects:** No new Zcash/Ethereum/Solana advisories beyond the CVE/GHSA/OSV streams. [zkSecurity Collision Atlas](writeups/zksecurityXYZ/collision-atlas-2026-11-16.md) saved (123 hash pairs, 15 full breaks). mdpsec.com refreshed — still no public disclosures; H1 hacktivity count 15 → 17.
- **New researchers:** none added (candidate search found no account with multiple verified finds). `researchers/Neodyme.md` index created for an already-watched handle.
- **Harness:** new [`harness/bug-classes/2026-11-16-mcp-open-data-rpc-tracer-logs.md`](harness/bug-classes/2026-11-16-mcp-open-data-rpc-tracer-logs.md) (7 check-specs) with pointers from auth-bypass, blockchain-client, business-logic, crypto-primitives, idor-bola, tee-attestation.

## Daily update — 15 November 2026 (Africa/Lagos)

- **X:** Full-archive search of 89 watched handles since 2026-11-14T05:46:20Z. ~93 new posts ingested into `store.json` / `data/x_posts.jsonl`; 27 security-relevant verbatim files written under `posts/` (heavy @mdp_sec day: guest-upload RCE, widget-config XSS, sequential-IDOR SSN, mobile hardcoded key; plus AI-harness methodology). ARCHIVEs regenerated. Backfill: pass-5 cursors remain DONE; `iguardz` has 0 tweets; `GuidoVranken` full-archive search returned 0 (account has tweets but none indexed to search).
- **Telegram:** @defendor_eng +4 (ids 2342–2345; Pool Party $215K position-edit drain, Centrifuge V3.3 cross-pool manager, Cantina attack-cost note); @dailybountywriteup +1 (id 14984). Writeup backlog: +60 defendor fetches this run; substantial dailybounty H1 `.json` batch (reconcile after hung fetch killed).
- **HackerOne:** +1 disclosed — [#4081135](hackerone/reports/2026/4081135.md) Weblate critical privilege escalation via unfiltered role restoration in project backup import (reporter zukosdead).
- **CVE:** cvelistV5 delta 2026-11-14 0600Z→2026-11-15 0500Z — **75 new / 24 updated** (records 425768; max_dateUpdated 2026-11-15T03:15:17Z). KEV catalogVersion unchanged 2026.11.13. GHSA reviewed: 0 modified since 2026-11-14T00:37:03Z. NVD enrichment shards updated for touched years.
- **Projects:** No new Zcash/Ethereum/Solana advisories beyond CVE/GHSA stream. zkSecurity newsletter saved under `writeups/zksecurityXYZ/newsletter-2026-11-14.md`. mdpsec.com still has no public report listing.

## X user lookups

| Handle | User id | Account created (UTC as returned) | Notes |
| --- | --- | --- | --- |
| Assass1nmarcos | 1021768127896477696 | 2018-07-24 | |
| RootxRavi | 1578337507355131904 | 2022-10-07 | |
| krishnsec | 1367090101981913090 | 2021-03-03 | |
| Suryesh_92 | 1761704057029226497 | 2024-02-25 | |
| SuyashS91823422 | 1406634200157999107 | 2021-06-20 | |
| Swartz068 | 1787485777259040768 | 2024-05-06 | |
| iguardz | 202705552 | 2010-10-14 | 0 tweets; default profile |
| bluethroat_labs | 1975856622380453888 | 2025-10-08 | |
| Kiki_developer | 1545461069568622593 | 2022-07-08 | |
| Piki_eth | 1565300610504613888 | 2022-09-01 | |
| infinitelogins | 1197730077078720512 | 2019-11-22 | |
| naresh_1337 | 2027589186451345412 | 2026-02-28 | |
| 0xvivekd | 1583325920768585728 | 2022-10-21 | |
| brandon_shi | 2656191451 | 2014-07-18 | |
| KeiZo_Zo | 1572286047249104898 | 2022-09-20 | |
| csanuragjain | 185382495 | 2010-08-31 | |
| lonelysloth_sec | 1735770300766183424 | 2023-12-15 | |
| GuplerSaxanoid | 1657888651 | 2013-08-09 | |
| al_f4lc0n | 1864143484514652164 | 2024-12-04 | |
| saxenism | 1199306572083519488 | 2019-11-26 | Bluethroat founder; profile only |
| ipwning | 1101876971758247944 | 2019-03-02 | Profile only; first-paid $150k shoutout, not given a full file |

## Seed posts fetched by id

| URL | Published (WAT) | Author | Why consulted |
| --- | --- | --- | --- |
| https://x.com/Assass1nmarcos/status/2110759502081675582 | 2026-10-15 16:47 | Assass1nmarcos | $12,500 H1 claim |
| https://x.com/RootxRavi/status/2114368791408947313 | 2026-10-25 15:49 | RootxRavi | $10k Bugcrowd P1 with krishnsec |
| https://x.com/Suryesh_92/status/2117598354641482125 | 2026-11-03 13:42 | Suryesh_92 | Thick-client finding accepted |
| https://x.com/SuyashS91823422/status/2115710027713360150 | 2026-10-29 08:39 | SuyashS91823422 | 30+ Bugcrowd triages, H1 comeback |
| https://x.com/Swartz068/status/2110728116180226209 | 2026-10-15 14:42 | Swartz068 | 11 triages on one target |
| https://x.com/immunefi/status/2112203877881991543 | 2026-10-19 16:27 | immunefi | iguardz $20k critical |
| https://x.com/immunefi/status/2115411377557062016 | 2026-10-28 12:52 | immunefi | bluethroat_labs $50k critical |
| https://x.com/Piki_eth/status/2115783655092277530 | 2026-10-29 13:31 | Piki_eth | Bridged-funds HackenProof triage |
| https://x.com/infinitelogins/status/2112170733228966180 | 2026-10-19 14:15 | infinitelogins | Disclosed weekly issue |

## X searches (past-year keyword searches unless noted)

- `from:Assass1nmarcos (bounty OR triaged OR writeup OR disclosed OR vulnerability OR HackerOne OR rewarded OR finding OR report) -is:retweet` since 2025-11-11 — 13 posts, more pages exist
- `from:RootxRavi (bounty OR triaged OR writeup OR P1 OR Bugcrowd OR rewarded OR finding OR report OR disclosed) -is:retweet` — 25 posts, more pages exist
- `from:krishnsec (…)` — 24 posts, more pages exist
- `from:Suryesh_92 (… thick OR client OR RCE …)` — 18 posts, more pages exist
- `from:SuyashS91823422 (…)` — 18 posts, more pages exist
- `from:Swartz068 (…)` — 19 posts, more pages exist
- `from:bluethroat_labs (…)` — 22 posts, more pages exist
- `from:Kiki_developer (…)` — 8 posts, more pages exist
- `from:Piki_eth (…)` — 23 posts, more pages exist
- `from:infinitelogins (Disclosed OR writeup OR bounty OR disclosed) -is:retweet` — 23 posts, more pages exist
- `from:immunefi (earned OR bounty OR congratulat OR "security researcher" OR "security team" OR leaderboard) -is:retweet` — 25 posts (relevancy)
- `("I found" OR writeup OR "how I found" OR "root cause") (bounty OR "$" OR disclosed) (hackerone OR bugcrowd OR immunefi OR hackenproof) -is:retweet lang:en` — 25 posts
- `iguardz (immunefi OR bounty OR critical OR vulnerability)` since 2025-04-01 — mostly RTs of the official post
- `get_users_posts` on Kiki_developer since 2024-11-11 — 25 posts (timeline, not keyword-filtered)
- `from:0xvivekd (bounty OR immunefi OR writeup OR critical OR methodology OR finding OR report) -is:retweet`
- `(from:csanuragjain OR from:naresh_1337 OR from:GuplerSaxanoid OR from:lonelysloth_sec OR from:al_f4lc0n OR from:brandon_shi OR from:KeiZo_Zo) (bounty OR writeup OR critical OR immunefi OR hackerone OR vulnerability OR finding) -is:retweet` since 2025-01-01

Posts cited in researcher files were drawn from those result sets (and from `get_posts_by_ids` for Harley's long writeups). Not every matching reply ("thanks bro") is listed again below; the researcher files cite the ones that carried facts.

## Additional X posts cited in the files

### Assass1nmarcos
- https://x.com/Assass1nmarcos/status/2112550747087024581 — 2026-10-20 15:25 WAT — self-described fake $6,421 screenshot
- https://x.com/Assass1nmarcos/status/2111534424198451434 — 2026-10-17 "comeback" comment
- https://x.com/Assass1nmarcos/status/2109728544893120639 — $6,000 H1
- https://x.com/Assass1nmarcos/status/2109726553705959685 — $7,200 H1
- https://x.com/Assass1nmarcos/status/2106068361662922971 — $8,000 BC + $4,950 H1
- https://x.com/Assass1nmarcos/status/2105768256917389365 — $10,000 H1
- https://x.com/Assass1nmarcos/status/2038648576335884461 — $5,000 H1
- https://x.com/Assass1nmarcos/status/2074871162035986895 — disputed P1 BOLA triage

### RootxRavi / krishnsec
- https://x.com/RootxRavi/status/2116477287554232616 — $10,250 H1
- https://x.com/RootxRavi/status/2107491994331423053 — $1,500 H1
- https://x.com/RootxRavi/status/2088272412072902705 — $4,500 H1
- https://x.com/RootxRavi/status/2087876415006085516 — $1,500 H1
- https://x.com/RootxRavi/status/2086836477095469280 — $2,500 H1
- https://x.com/RootxRavi/status/2084992157388345591 — Bugcrowd Top 100
- https://x.com/RootxRavi/status/2083510058093326602 — India #4 July
- https://x.com/RootxRavi/status/2072261644709986608 — India #2 June
- https://x.com/RootxRavi/status/2066959135414055188 — tooling / laptop
- https://x.com/krishnsec/status/2116965015777628269 — P1 model extraction class
- https://x.com/krishnsec/status/2114270259687661611 — "harness" comment
- https://x.com/krishnsec/status/2109886780657029303 — 69% accuracy
- https://x.com/krishnsec/status/2107784924162093528 — 20k BC reputation
- https://x.com/krishnsec/status/2106984299560124675 — Sep #1
- https://x.com/krishnsec/status/2102006855241482637 — 19k reputation
- https://x.com/krishnsec/status/2100479403478417659 — Aug #1
- https://x.com/krishnsec/status/2100141425983881443 — Top 3 P1 warrior
- https://x.com/krishnsec/status/2089703314653089816 — 18k reputation
- https://x.com/krishnsec/status/2087905595471139144 — Top 15 all-time
- https://x.com/krishnsec/status/2088675304198078711 — skill vs one-bug
- https://x.com/krishnsec/status/2090784263096680870 — 4x P1/P2 bonus

### Suryesh_92
- https://x.com/Suryesh_92/status/2097690285799313440 — thick-client RCE tally
- https://x.com/Suryesh_92/status/2097850230930862237 — source-code analysis comment
- https://x.com/Suryesh_92/status/2080593128982188513 — program paused
- https://x.com/Suryesh_92/status/2071781463767580756 — another bounty
- https://x.com/Suryesh_92/status/2069043943640301896 — first thick-client RCE
- https://x.com/Suryesh_92/status/2018672994436948257 — 2FA bypass
- https://x.com/Suryesh_92/status/2016865602749813209 — BAC
- https://x.com/Suryesh_92/status/2014855434696597734 — upload stored XSS / double MIME
- https://x.com/Suryesh_92/status/2013636881272184929 — bounty increase 3500 CHF
- https://x.com/Suryesh_92/status/2013196581994946685 — 1500 CHF

### SuyashS91823422
- https://x.com/SuyashS91823422/status/2117667516780777854 — $4,500
- https://x.com/SuyashS91823422/status/2118048829715148801 — $2,300 / 3 submissions
- https://x.com/SuyashS91823422/status/2118419045682926068 — top 1000
- https://x.com/SuyashS91823422/status/2119839963034669357 — $2,225
- https://x.com/SuyashS91823422/status/2120089891610476947 — fast triage
- https://x.com/SuyashS91823422/status/2120398564870549635 — bounty in 8 hours

### Swartz068
- https://x.com/Swartz068/status/2117931096726016043 — Wayback JS secrets tip
- https://x.com/Swartz068/status/2117202589918114241 — Wayback JWT tip
- https://x.com/Swartz068/status/2117294264254435641 — $100
- https://x.com/Swartz068/status/2116525685305139421 — P3 to P2
- https://x.com/Swartz068/status/2108307317322379620 — 10 triages one program
- https://x.com/Swartz068/status/2104893407655305597 — 9 of 10 on one program
- https://x.com/Swartz068/status/2098076274497626251 — another triage
- https://x.com/Swartz068/status/2091854507970081180 — 2× duplicate
- https://x.com/Swartz068/status/2110996965148266599 — wildcard programs
- https://x.com/Swartz068/status/2110784539757015170 — manual testing / $0 so far
- https://x.com/Swartz068/status/2112591482884628659 — Meta program complaint

### bluethroat_labs
- https://x.com/bluethroat_labs/status/2119050683840438658 — $10k quorum disagreement
- https://x.com/bluethroat_labs/status/2119030716373832154 — 4th on Immunefi leaderboard
- https://x.com/bluethroat_labs/status/2108575109535433161 — bounty #11 crit→high
- https://x.com/bluethroat_labs/status/2107490499305124027 — bounty #10 determinism
- https://x.com/bluethroat_labs/status/2105581456550461936 — bounty #9 high
- plus earlier 2026 confirmed-finding posts linked in the researcher file

### Kiki_developer
- https://x.com/Kiki_developer/status/2016898778209669412 — Immunefi medium paid
- https://x.com/Kiki_developer/status/2017310553140826310 — "best bounty experience"
- https://x.com/Kiki_developer/status/2016925457271361718 — leftover privileged contract
- https://x.com/Kiki_developer/status/2017472477165945231 — "just a medium"

### Piki_eth
- https://x.com/Piki_eth/status/2119348331537396059 — triage in 30 minutes
- https://x.com/Piki_eth/status/2119008635946930555 — another critical triaged
- https://x.com/Piki_eth/status/2114761602025304105 — SSRF + DeepSeek
- https://x.com/Piki_eth/status/2104614940502094068 — $1,500
- https://x.com/Piki_eth/status/2102267347876909515 — $1,000
- https://x.com/Piki_eth/status/2094848073256333483 — private invite after critical
- https://x.com/Piki_eth/status/2094790419410567631 — paid
- https://x.com/Piki_eth/status/2093217981732171978 — local Qwen DoS, reputation gate
- https://x.com/Piki_eth/status/2103571947573686427 — DEX ghosting allegation

### infinitelogins (full text pulled)
- https://x.com/infinitelogins/status/2117981403161764138 — $5k ATO writeup
- https://x.com/infinitelogins/status/2116236446147240443 — recon database tip
- https://x.com/infinitelogins/status/2115429533738262954 — $5k priv-esc writeup
- https://x.com/infinitelogins/status/2110355630133322159 — $4k SQLi writeup
- https://x.com/infinitelogins/status/2108181015885685018 — $10k auth-bypass writeup
- https://x.com/infinitelogins/status/2073099379712671799 — top 5 US quarter
- https://x.com/infinitelogins/status/2043552103076094169 — top 60 / top 5 US 90 days
- https://x.com/infinitelogins/status/2053257780895920586 — first BB SQLi
- https://x.com/infinitelogins/status/2054931668570685494 — max crit paid
- https://x.com/infinitelogins/status/2025934052759367834 — HacktronAI / Antigravity (other people's bug)
- https://x.com/infinitelogins/status/2024484231062114553 — spaceraccoon patchdiff

### Immunefi shoutouts used for new researchers
- https://x.com/immunefi/status/2103156012798869539 — brandon_shi $50k
- https://x.com/immunefi/status/2114677302378565786 — naresh_1337 $25k
- https://x.com/immunefi/status/2102010814442181024 — 0xvivekd $323k / 16 reports
- https://x.com/immunefi/status/2066898721523028465 — 0xvivekd $1.07M in 2026
- https://x.com/immunefi/status/2117965345550172382 — KeiZo_Zo $33k
- https://x.com/immunefi/status/2075603795606675920 — csanuragjain $18k
- https://x.com/immunefi/status/2109982938578522400 — GuplerSaxanoid $30k (truncated text)
- Other Immunefi posts in the relevancy search (ipwning, ily2, broon, etc.) were read for discovery only

### 0xvivekd, naresh_1337, lonelysloth_sec, al_f4lc0n, KeiZo_Zo
- Listed and dated in their researcher files (paid/confirmed share cards, Quantus MVF, ZK methodology, Injective thread, 30 Immunefi reports)

## Web pages and writeups

| URL | What it contributed |
| --- | --- |
| https://hackerone.com/assassin_marcos?type=user | 148 vulns, rank, streak |
| https://adityasec.in/ and https://adityasec.in/about | Identity, HoF list, role |
| https://assassin-marcos.medium.com/ | Index of writeups |
| https://assassin-marcos.medium.com/5k-misconfigured-reset-password-that-leads-to-account-takeover-no-user-interaction-ato-e6a36b8ef183 | $5k ATO writeup |
| https://assassin-marcos.medium.com/dont-underestimates-the-errors-they-can-provide-good-bounty-d437ecca6596 | $200 path-disclosure writeup |
| https://www.bugbountydirectory.com/blogs/breaking-the-barrier-admin-panel-takeover-worth-3500 | $3,500 admin-takeover writeup (republish of Medium) |
| https://hackwithsuryesh.netlify.app/ | Blog home (linked from bio) |
| https://hackwithsuryesh.medium.com/ | Writeup index |
| https://hackwithsuryesh.medium.com/algolia-api-key-exploitation-leads-to-1000-bounty-p2-on-private-program-2e147f052ff0 | Algolia key writeup |
| https://hackwithsuryesh.medium.com/how-i-chained-rce-via-dependencies-to-lfi-348315aa17e8 | Dependency-confusion writeup |
| https://hackwithsuryesh.medium.com/rxss-csti-in-search-field-via-polygot-payload-65ca1a8be8ba | XSS + CSTI writeup |
| LinkedIn posts by Dhananjay Kumar Suryesh (Jun/Sep/Nov 2026 thick-client announcements) | Confirmed name; no extra technical detail |
| https://immunefi.com/profile/IGUARDZ/ | $63,280, 7 reports, member since 29 Apr 2026 |
| https://immunefi.com/pledge/IGUARDZ/ | Pledge page rank snapshot |
| Immunefi LinkedIn cross-posts for iguardz and bluethroat $50k | Corroboration; iguardz report-count wording differed (5 vs 6) |
| https://bluethroatlabs.com/ | Firm focus, scoreboard teaser |
| https://phala.com/posts/dstack-security-update-attestation-pipeline-hardening | dstack findings 1–7, timeline, credits |
| https://www.linkedin.com/posts/bluethroat-labs_56-trusted-execution-over-an-unsafe-transport-activity-7447638926099685376-GKd6 | Stale-collateral / TLS explainer |
| https://github.com/devNamedKiki/Audits and raw README | Audit/bounty tables |
| https://raw.githubusercontent.com/devNamedKiki/Audits/main/Bounties/013.md | Liquidation-threshold writeup |
| https://raw.githubusercontent.com/devNamedKiki/Audits/main/Bounties/016.md | Critical title only, writeup pending |
| https://raw.githubusercontent.com/devNamedKiki/Audits/main/Bounties/017.md | High title only, writeup pending |
| https://medium.com/@kiki.auditor/8-common-smart-contract-vulnerabilities-found-throughout-audit-contest-d8f19c494f7e | Common SC classes |
| https://audits.sherlock.xyz/watson/CodingNameKiki | Contest stats (search snippet) |
| https://github.com/0xvivekd/0xvivekd | Linked from bio; not fully inventoried |
| https://immunefi.com/profile/Naresh_Kandula/ | $35,538, rank 148 |
| https://yeswehack.com/hunters/nottiboy-1337 | Linked from a Naresh post |
| https://immunefi.com/profile/LonelySloth | Profile linked from bio |
| https://immunefi.com/profile/keizo/ and https://hackerone.com/keizo | Linked from bio |
| https://hackerone.com/csanuragjain?type=user and hacktivity / reports #279935, #434689 | Search snippets only; reports not fully read |
| https://y4y.space | brandon_shi site (not fully inventoried) |
| https://immunefi.com/profile/GuplerSaxanoid/ | Linked from bio |
| https://github.com/injective-wall-of-shame/bug-any-account-ordering | Linked by al_f4lc0n; fetch returned almost no body |
| https://bugcrowd.com/RootxRavi , http://bugcrowd.com/krishnsec , http://hackerone.com/krishnsec_ | Linked from bios; not fully scraped |
| https://getdisclosed.com | Disclosed home |
| https://github.com/BluethroatLabs/BluePaper | Linked from a Bluethroat post; tool, not a bounty writeup |

## Search queries used on the web

- Aditya Sharma assassin_marcos writeup / Medium slugs
- Suryesh HackWithSuryesh thick-client RCE / Algolia / dependency confusion
- iguardz Immunefi 2026
- Kiki developer GitHub Audits / Sherlock
- bluethroat labs Immunefi / dstack / deterministic execution
- csanuragjain HackerOne writeups
- naresh_1337 Immunefi

## Intentionally not copied into the knowledge base

Full HTTP requests, wildcard payloads, WAF-bypass SQL, XSS polyglots, Algolia curl command sequences, and npm `preinstall` proof-of-concept scripts that appeared in public writeups. Those remain in the source URLs above.


## Nov 2026 expansion — verbatim capture pass

- X reads: `get_posts_by_ids` (full note_tweet text), `get_users_posts` (timelines, time-windowed for old threads), `search_posts_all` (conversation threads, ~30-day index), `get_users_by_usernames`. All read-only; nothing posted, liked, followed or DM'd.
- 326 post files (583 posts incl. thread replies) under `posts/`; 51 writeups under `writeups/`.
- Medium article pages returned 403; full text was taken from the author's Medium RSS feed (`content:encoded`). HackerOne disclosed reports were read from `https://hackerone.com/reports/<id>.json`.

### Writeups saved

| File | Source line from header |
| --- | --- |
| `writeups/0xacb/tedivm-ai-rcession.md` | Source URL:** https://blog.tedivm.com/rants/2026/10/the-ai-rcession-has-begun/ |
| `writeups/0xiczc/certik-evm-cosmos-convergence-part-2.md` | Source URL:** https://certik.com/resources/blog/evm-cosmos-convergence-research-from-security-base-part-2 |
| `writeups/0xiczc/evmos-advisory-GHSA-3fp5-2xwh-fxm6.md` | Source URL:** https://github.com/evmos/evmos/security/advisories/GHSA-3fp5-2xwh-fxm6 |
| `writeups/0xiczc/polygon-zkevm-node-pr-2048.md` | Source URL:** https://github.com/0xPolygonHermez/zkevm-node/pull/2048 |
| `writeups/0xriptide/balancers-bountiful-merkle-orchard-mirror.md` | Source URL:** https://mirror.xyz/0x2719F6Dfb85086F87319079cC2f7EeFD0e40994D/NWDf5uW1Ve7-TrcPKwmM86xp8ploMSCRGC58A-NSoFY |
| `writeups/0xriptide/hackers-in-arbitrums-inbox.md` | Source URL:** https://medium.com/@0xriptide/hackers-in-arbitrums-inbox-ca23272641a2 |
| `writeups/Assass1nmarcos/5k-misconfigured-reset-password-that-leads-to-account-takeover-no-user-interacti.md` | Source URL:** https://assassin-marcos.medium.com/5k-misconfigured-reset-password-that-leads-to-account-takeover-no-user-interaction-ato-e6a36b8ef183 |
| `writeups/Assass1nmarcos/breaking-the-barrier-admin-panel-takeover-worth-3500.md` | Source URL:** https://assassin-marcos.medium.com/breaking-the-barrier-admin-panel-takeover-worth-3500-78da79089ca3 |
| `writeups/Assass1nmarcos/bugbountydirectory-republish-admin-panel-takeover-3500.md` | Source URL:** https://www.bugbountydirectory.com/blogs/breaking-the-barrier-admin-panel-takeover-worth-3500 |
| `writeups/Assass1nmarcos/dont-underestimates-the-errors-they-can-provide-good-bounty.md` | Source URL:** https://assassin-marcos.medium.com/dont-underestimates-the-errors-they-can-provide-good-bounty-d437ecca6596 |
| `writeups/Kiki_developer/8-common-smart-contract-vulnerabilities-found-throughout-audit-contest.md` | Source URL:** https://medium.com/@kiki.auditor/8-common-smart-contract-vulnerabilities-found-throughout-audit-contest-d8f19c494f7e |
| `writeups/Kiki_developer/bounty-013.md` | Source URL:** https://raw.githubusercontent.com/devNamedKiki/Audits/main/Bounties/013.md |
| `writeups/Kiki_developer/bounty-016.md` | Source URL:** https://raw.githubusercontent.com/devNamedKiki/Audits/main/Bounties/016.md |
| `writeups/Kiki_developer/bounty-017.md` | Source URL:** https://raw.githubusercontent.com/devNamedKiki/Audits/main/Bounties/017.md |
| `writeups/Kiki_developer/bounty-018.md` | Source URL:** https://raw.githubusercontent.com/devNamedKiki/Audits/main/Bounties/018.md |
| `writeups/PwningEth/frontier-evm-wrapped-token-insolvency.md` | Source URL:** https://pwning.mirror.xyz/RFNTSouIIlHVNmTNDThUVb1obIeN5c1LAiQuN9Ve-ok |
| `writeups/Suryesh_92/algolia-api-key-exploitation-leads-to-1000-bounty-p2-on-private-program.md` | Source URL:** https://hackwithsuryesh.medium.com/algolia-api-key-exploitation-leads-to-1000-bounty-p2-on-private-program-2e147f052ff0 |
| `writeups/Suryesh_92/how-i-chained-rce-via-dependencies-to-lfi.md` | Source URL:** https://hackwithsuryesh.medium.com/how-i-chained-rce-via-dependencies-to-lfi-348315aa17e8 |
| `writeups/Suryesh_92/rxss-csti-in-search-field-via-polygot-payload.md` | Source URL:** https://hackwithsuryesh.medium.com/rxss-csti-in-search-field-via-polygot-payload-65ca1a8be8ba |
| `writeups/_bagipro/oversecured-samsung-vulnerabilities-readme.md` | Source URL:** https://raw.githubusercontent.com/oversecured/Samsung_Vulnerabilities/main/README.md |
| `writeups/al_f4lc0n/injective-any-account-ordering-report.md` | Source URL:** https://raw.githubusercontent.com/injective-wall-of-shame/bug-any-account-ordering/main/report.md |
| `writeups/bluethroat_labs/bluepaper-readme.md` | Source URL:** https://raw.githubusercontent.com/BluethroatLabs/BluePaper/main/README.md |
| `writeups/bluethroat_labs/linkedin-trusted-execution-unsafe-transport.md` | Source URL:** https://www.linkedin.com/posts/bluethroat-labs_56-trusted-execution-over-an-unsafe-transport-activity-7447638926099685376-GKd6 |
| `writeups/bluethroat_labs/phala-dstack-attestation-hardening.md` | Source URL:** https://phala.com/posts/dstack-security-update-attestation-pipeline-hardening |
| `writeups/fransrosen/hackernotes-ep86-xcorrelation.md` | Source URL:** https://blog.criticalthinkingpodcast.io/p/hackernotes-ep86-xcorrelation-frans-rce-research-drop |
| `writeups/galnagli/wiz-php2shell-php-rce.md` | Source URL:** https://www.wiz.io/blog/php2shell-php-rce |
| `writeups/garethheyes/frag-readme.md` | Source URL:** https://raw.githubusercontent.com/hackvertor/frag/main/README.md |
| `writeups/garethheyes/ikaes-strings-without-parentheses.md` | Source URL:** https://blog.ikaes.de/generating-strings-without-parentheses-in-javascript/ |
| `writeups/garethheyes/portswigger-scalable-vector-grief.md` | Source URL:** https://portswigger.net/research/scalable-vector-grief |
| `writeups/iguardz/linkedin-immunefi-iguardz-20000.md` | Source URL:** https://www.linkedin.com/posts/immunefi_security-researcher-iguardz-just-earned-20000-activity-7517969578736631808-yrpm |
| `writeups/infinitelogins/vulnerability-spoiler-alert-action.md` | Source URL:** https://raw.githubusercontent.com/spaceraccoon/vulnerability-spoiler-alert-action/main/README.md |
| `writeups/infosec_au/frontier-class-vulnerabilities.md` | Source URL:** https://shubs.io/frontier-class-vulnerabilities-it-gets-worse-before-it-maybe-gets-better/ |
| `writeups/infosec_au/react2shell-scanner-readme.md` | Source URL:** https://raw.githubusercontent.com/assetnote/react2shell-scanner/master/README.md |
| `writeups/infosec_au/unlocking-any-car.md` | Source URL:** https://shubs.io/unlocking-any-car-from-x-brand-in-most-of-the-world/ |
| `writeups/j00ru/gpz-mms-exploit-part-3.md` | Source URL:** https://googleprojectzero.blogspot.com/2020/07/mms-exploit-part-3-constructing-primitives.html |
| `writeups/j00ru/gpz-mms-exploit-part-4.md` | Source URL:** https://googleprojectzero.blogspot.com/2020/08/mms-exploit-part-4-completing-aslr-oracle.html |
| `writeups/j00ru/gpz-mms-exploit-part-5.md` | Source URL:** https://googleprojectzero.blogspot.com/2020/08/mms-exploit-part-5-defeating-aslr-getting-rce.html |
| `writeups/j00ru/gpz-windows-exploitation-tricks-trapping.md` | Source URL:** https://googleprojectzero.blogspot.com/2021/01/windows-exploitation-tricks-trapping.html |
| `writeups/kevin_mizu/dompurify-bypass-smil-animatetransform-safari.md` | Source URL:** https://mizu.re/post/dompurify-bypass-smil-animatetransform-safari |
| `writeups/kevin_mizu/hackerone-report-3876430.md` | Source URL:** https://hackerone.com/reports/3876430 |
| `writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md` | Source URL:** https://raw.githubusercontent.com/mdpsec/bug-bounty-hunting-prompts/main/README.md |
| `writeups/mdp_sec/mdpsec-home.md` | Source URL:** https://mdpsec.com/ |
| `writeups/orange_8361/2026-10-browser-full-chain.md` | Source URL:** https://blog.orange.tw/posts/2026-10-the-last-proof-of-human-craft-browser-full-chain/ |
| `writeups/samczsun/higher-bug-bounties-wont-stop-hacks.md` | Source URL:** https://samczsun.com/higher-bug-bounties-wont-stop-hacks/ |
| `writeups/samczsun/so-you-want-to-use-a-price-oracle.md` | Source URL:** https://samczsun.com/so-you-want-to-use-a-price-oracle/ |
| `writeups/samczsun/taking-undercollateralized-loans-for-fun-and-for-profit.md` | Source URL:** https://samczsun.com/taking-undercollateralized-loans-for-fun-and-for-profit/ |
| `writeups/samczsun/two-rights-might-make-a-wrong.md` | Source URL:** https://samczsun.com/two-rights-might-make-a-wrong/ |
| `writeups/samwcyo/forgerock-rce-vehicles.md` | Source URL:** https://samcurry.net/forgerock |
| `writeups/samwcyo/hacking-clubwpt-gold.md` | Source URL:** https://samcurry.net/hacking-clubwpt-gold |
| `writeups/xssdoctor/faav-17-trillion-microsoft-records.md` | Source URL:** https://blog.faav.net/how-i-couldve-accessed-17-trillion-microsoft-records |
| `writeups/zseano/hackerone-report-3862641.md` | Source URL:** https://hackerone.com/reports/3862641 |

### Could not fetch

- Phrack 72 "The Art of PHP" (Orange Tsai) — page is JS-rendered; no text extracted.
- hacktron.ai Antigravity blog post — 404.
- Some old X threads are partial because the search index only covers ~30 days: `_bagipro` Android content-provider thread (3 of 4 parts), ChainLight weekly summaries (partial), zkSecurity challenge thread (as available). Timelines with time windows recovered the full Frans Rosén 10-part thread and the first `_bagipro` Uri thread.
- Dropped candidates (no technical posts returned): renniepak, bytes032, 0xleastwood, 0xalpharush, steventseeley, lavados, 0xPARC (event/announcement posts only).

## Nov 2026 — Marius du Preez deep crawl + harness layer

- **mdpsec.com**: crawled sitemap (`/`, `/privacy/`, `/security-test/` only), robots.txt, and probed for a reports page/API. The site is a static Astro marketing site with no per-report listing and no data API (only `/api/apply` lead form). Saved: `writeups/mdp_sec/mdpsec-home.md`, `mdpsec-privacy.md`, `mdpsec-security-test.md`.
- **HackerOne** (`mdpsec`): public GraphQL — `user(username:"mdpsec")` for stats and `search(index:CompleteHacktivityReportIndex, query_string:"reporter:mdpsec")` for hacktivity. 24 resolved, 0 disclosed, 15 hacktivity entries (metadata only). Read-only.
- **HackenProof** (`MDPSEC`): public profile HTML. 15 paid reports (3C/3H/6M/3L), 0 disclosed, rank 104.
- **Bugcrowd** (`marius_dp`): profile gated behind the authenticated hacker portal; no public per-report data retrievable.
- **GitHub** `mdpsec`: repos `bug-bounty-hunting-prompts` (full 11-phase prompt pack saved under `writeups/mdp_sec/prompts/`) and `should-i-submit` (README saved).
- **X** `@mdp_sec`: full retrievable original-post timeline via `get_users_posts` (exclude replies/retweets), 22 pages, 422 posts, 2026-07-22 → 2026-11-11. Timeline API returns nothing older than 2026-07-22. Read-only; nothing posted/liked/followed.
- **Medium**: no `@mdpsec`/`@mdp_sec`/`@mariusdupreez` feed exists (404).
- **Harness layer** built from the above plus existing repo sources: `harness/README.md`, `harness/recon-methodology.md`, `harness/bug-classes/*.md` (14 classes), `harness/findings.jsonl` (39 records).

### Could not fetch / not available
- Any Marius du Preez report with full disclosed detail (0 disclosed on HackerOne and HackenProof; Bugcrowd gated). His per-report detail exists only in his own X posts.
- His X posts from 2026-03-24 to 2026-07-21 (before the timeline API's reach limit).
- Bugcrowd per-researcher disclosures (authenticated hacker portal).

## Nov 2026 — saxenism + protocol advisories + backfill

- **@saxenism**: 27 timeline pages via `get_users_posts` (exclude replies/retweets); 470 original-post files, 2024-10-01 → 2026-11-10. Timeline API floor (next_token null). Linked writeups: dumb-ways-to-get-rekt-with-tees, TEE handbook, Argument.xyz RISC-V, Bluethroat docs, Turnkey whitepaper. Reveries SPA yielded no article bodies.
- **Zcash GHSA**: zcash/zcash (9), ZcashFoundation/zebra (52+1), zcash/lightwalletd (13), ZcashFoundation/frost (1) → 76 advisories under `projects/zcash/`. SECURITY.md from zcashd and zebra.
- **Ethereum GHSA**: ethereum/go-ethereum (17+9 global), sigp/lighthouse (8) → 34 under `projects/ethereum/`. Canonical Solidity `bugs.json` (67). SECURITY.md from geth and solidity.
- **Solana**: Anza/solana-labs GHSA returned 0 published; OSV crates.io + RustSec → 9 advisories (solana_rbpf, anchor-lang, spl-token-swap). Agave SECURITY.md saved.
- **Crypto**: 76 RustSec crypto-crate advisories (openssl mirrors omitted) + 0xPARC zk-bug-tracker README under `projects/crypto/`.
- **Backfill (partial)**: first/second timeline pages for fransrosen, albinowax, garethheyes, kevin_mizu, infosec_au, samwcyo, orange_8361, samczsun, jovanbulck, lonelysloth_sec, 0xiczc, zksecurityXYZ, _bagipro, j00ru, zseano, irsdl, galnagli — new posts merged into existing `posts/<handle>/` folders. Many accounts still thin (see report).

## 2026-11-11 — Backfill pass (full-archive X search)

- Full-archive keyword searches (security terms; unfiltered for small accounts) across all watched researchers plus 13 crypto/protocol accounts. Results regenerated into `posts/<handle>/ARCHIVE.md` (verbatim, threads grouped, quoted posts inlined) and `data/x_posts.jsonl`.
- Per-account before/after counts and which search cursors remain open: [data/backfill_status.md](data/backfill_status.md).
- Archive total after this pass: 5,407 verbatim posts.

## 2026-11-12 — Daily update (Africa/Lagos)

### X (public reads only; nothing posted/liked/followed)
- Recent-window full-archive search since 2026-11-11T08:00:00Z across all watched handles (3 OR-batches + mdp_sec original-post filter + pagination).
- Ingested ~40 new posts; security-relevant ones written under `posts/<handle>/` with Analysis.
- Backfill: `mdp5` DONE (timeline floor 2026-07-22); `sax5`→`sax5k` security-keyword backfill DONE to 2020-03-15 (373 keyword hits + 50 unfiltered bridge pages). Archive total 5581→15661.
- X quota at end of run: ~968/1000 remaining today.

### Writeups fetched (full readable markdown)
| File | Source |
| --- | --- |
| `writeups/garethheyes/blind-trust-stealing-credentials-through-csp.md` | https://portswigger.net/research/blind-trust-stealing-credentials-through-csp |
| `writeups/bluethroat_labs/phala-cloud-gpu-attestation-fake-verified-no-cryptography.md` | https://bluethroatlabs.com/reveries/phala-cloud-gpu-attestation-fake-verified-no-cryptography |
| `writeups/bluethroat_labs/tee-fail.md` | https://tee.fail |
| `writeups/saxenism/near-ai-sglang-security-incident-report.md` | https://near.ai/blog/security-incident-report-sglang-vulnerability |
| `writeups/Rhynorater/depi-backdooring-codex.md` | https://depi.security/blog/20261111-backdooring-codex/ |
| `writeups/zellic_io/x86-formal-verification-intro.md` | https://www.zellic.io/blog/x86-formal-verification-intro/ |
| `writeups/zksecurityXYZ/solana-privacy-rings-zolana-audit-2026-08.md` | https://github.com/helius-labs/zolana/raw/main/audits/zk_security_solana_privacy_rings_v1_audit.pdf |
| `writeups/mdp_sec/huntdeck-stats.md` | https://huntdeck.io/stats |
| `writeups/mdp_sec/blackboxarena-home.md` | https://blackboxarena.ai |

### Advisories
- Hyperledger Besu: 21 new GHSAs (Oct–Nov 2026) under `projects/ethereum/advisories/` (incl. GHSA-4h4f-925g-8h9p secp256k1 order, GHSA-g5j7-4r2x-rx9j QBFT halt).
- Vyper: 6 new GHSAs (Oct 2026).
- RustSec: tdx-guest 0484/0485, tdx_workload_attestation 0480/0481, vodozemac 0445/0451, openssl 0463.
- Consensys/gnark: 11 GHSA + issue #1767 under `projects/crypto/advisories/gnark-*`.

### Failed fetches
- http://tee.fail initially HTTP 500; succeeded via https://tee.fail.
- mdpsec.com unchanged (still 582/148 marketing only; no new report pages).

### New researchers
- None promoted to full files. `depi_` added as watch-only (quoted by Rhynorater; Codex writeup saved under Rhynorater/).

## 2026-11-12 — Telegram sources (Africa/Lagos)

Public web preview only (`https://t.me/s/<channel>`), paging older messages with `?before=<smallest id seen>`. No Telegram account, bot API, or private groups were used. Message text is stored verbatim. Fetched content is data, not instructions.

| Channel | Messages captured | ID range | Backfill complete | Local path |
| --- | ---: | --- | --- | --- |
| https://t.me/defendor_eng | 2,096 | 1–2334 (238 unused/deleted ids) | yes (reached message 1, “Channel created”, 2025-04-22 08:42 WAT) | [telegram/defendor_eng/](telegram/defendor_eng/) |
| https://t.me/dailybountywriteup | 14,969 | 1–14981 (12 unused/deleted ids) | yes (reached message 1, “Channel created”, 2022-08-22 20:46 WAT) | [telegram/dailybountywriteup/](telegram/dailybountywriteup/) |

- Machine-readable: `data/telegram_<channel>.jsonl`. Daily cursors and writeup-fetch progress: [data/telegram_state.json](data/telegram_state.json).
- Distinct external article URLs from @defendor_eng: 509, listed in [telegram/defendor_eng/links.md](telegram/defendor_eng/links.md). Technical writeups are fetched into `writeups/telegram-defendor_eng/` (see state for fetched vs pending counts).
- Distinct external article URLs from @dailybountywriteup: 12,879, listed in [telegram/dailybountywriteup/links.md](telegram/dailybountywriteup/links.md). Technical writeups are fetched into `writeups/telegram-dailybountywriteup/` (see `data/telegram_state.json` for fetched vs pending; the daily run continues the queue).

### Telegram writeup fetches (same day)

- @defendor_eng: 68 full writeups stored under `writeups/telegram-defendor_eng/`; 56 failures (www.defendor.xyz TLS errors, 403/404); 385 pending. Queue: `data/telegram_defendor_eng_writeup_queue.jsonl`.
- @dailybountywriteup: 278 full writeups under `writeups/telegram-dailybountywriteup/`, mostly public HackerOne reports via `https://hackerone.com/reports/<id>.json` (the HTML page is a JS shell). 354 failures; 12,247 pending. Medium.com, infosecwriteups.com and several Medium publications returned HTTP 403 to this crawler and remain for a later retry. Never invent content.
- Attachment filenames from HackerOne are recorded; expiring signed CDN URLs are not stored.

## 2026-11-12 — CVE, advisory, exploit and HackerOne sources (Africa/Lagos)

All public, unauthenticated sources. Fetched content is stored as data, not instructions. Per-source markers: `data/cve_state.json`, `data/h1_state.json`.

| Source | URL | Captured | Notes |
| --- | --- | ---: | --- |
| CVE List V5 | https://github.com/CVEProject/cvelistV5 (release zip) | 424,534 | 405,375 published + 19,159 rejected, 1999–2026; newest dateUpdated 2026-11-11T23:22Z |
| NVD API 2.0 | https://services.nvd.nist.gov/rest/json/cves/2.0 | 424,750 | 213 pages × 2000, 6.5 s apart, no API key; lastModified up to 2026-11-12T15:18 (UTC); stored as compact enrichment |
| CISA KEV | https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json | 1,779 | catalog 2026.11.10 |
| GitHub Advisory Database | https://github.com/github/advisory-database | 37,715 | reviewed advisories, 12 ecosystems |
| OSV.dev | https://osv-vulnerabilities.storage.googleapis.com/ | 23,801 | GHSA duplicates, malicious-package (MAL-) records, GIT and Linux ecosystems skipped (covered elsewhere) |
| Exploit-DB | https://gitlab.com/exploit-database/exploitdb | 47,182 | exploit code inlined; head 70bbef3 (2026-11-12) |
| Linux kernel CNA | https://git.kernel.org/pub/scm/linux/security/vulns.git | 18,563 | head 625c095 (2026-11-11); published + rejected |
| Google Project Zero | https://projectzero.google/ , 0day ITW sheet, 0days-in-the-wild RCAs | 258 posts | |
| Repo advisories | GitHub security advisories of php/php-src, electron/electron, WordPress/wordpress-develop | 66 / 70 / 54 | |
| Zero Day Initiative | https://www.zerodayinitiative.com/advisories/published/ | 17,361 indexed, 7,067 full text | remaining advisory pages pending (cursor in `data/cve_state.json`) |
| HackerOne Hacktivity | https://hackerone.com/graphql (CompleteHacktivityReportIndex) + https://hackerone.com/reports/<id>.json | 12,750 / 12,750 | 10,005 with full original report, 2,745 summary-only (limited disclosure); 0 failures; 278 overlap with `writeups/telegram-dailybountywriteup/` |


## 13 November 2026 (Africa/Lagos) — daily update

X (full-archive search, 3 batched watched-account queries since id 2120735261399433504; 64 new posts, retweets excluded):
- https://x.com/saxenism/status/2120829077829582959 (Zcash finding #8, High — remediation bypass) + thread
- https://x.com/zksecurityXYZ/status/2120960376791847035 (Monero Generalized Bulletproofs Lean proof)
- https://x.com/trailofbits/status/2120943246587392210 and /2121009628855357931 (Patch the Planet; agent patch plugins)
- https://x.com/S1r1u5_/status/2120761362075079124 and /2120772117788860528 (Glasswing n-day/0day)
- https://x.com/0xvivekd/status/2120893385519313126 (private bounty, undisclosed)

Writeups fetched:
- https://magicgrants.org/2026/11/12/Generalized-Bulletproofs-zkSecurity
- https://www.vulncheck.com/blog/anthropic-glasswing-november-update
- https://trailofbits.com/patch-the-planet/dashboard/
- https://rekt.news/mercado-rekt (Telegram @defendor_eng msg 2335)
- https://x.com/GuardianAudits/status/2120924685890413008 (Telegram @defendor_eng msg 2336; video thread)
- 170 HackerOne public reports from the @dailybountywriteup backlog (via /reports/<id>.json)

Telegram previews: https://t.me/s/defendor_eng (2 new: 2335-2336), https://t.me/s/dailybountywriteup (no new).

CVE/advisory: CVEProject/cvelistV5 deltas 2026-11-12_end_of_day + 2026-11-13_0500Z (423 new, 1,970 updated); github/advisory-database git pull (GHSA reviewed 37,767); CISA KEV unchanged (2026.11.10); Exploit-DB & Linux-kernel vulns.git unchanged. Per-repo security advisories re-checked for zcash/ethereum/solana (no new).
HackerOne: GraphQL CompleteHacktivityReportIndex disclosed_at:[2026-11-12 TO 2026-11-14] → +2 reports (4110110, 4062639).


## 14 November 2026 (Africa/Lagos) — daily update

X (full-archive search, 2 batched watched-account queries since id 2121117686692479126 + mdp_sec own-thread + reply pulls; 121 new posts, retweets excluded). Security-relevant captures:
- https://x.com/mdp_sec/status/2121244189593940355 ($2,000 Bugcrowd cross-tenant IDOR → live auth header)
- https://x.com/mdp_sec/status/2121358210577883544 and /2121274388435922971 (100-lab hacking-harness model benchmarks: Grok 4.6 vs 4.7 vs Opus 5; provider-routing/quantization effect)
- https://x.com/mdp_sec/status/2121213990546088318 (582 reports / 148 crits triage telemetry)
- https://x.com/S1r1u5_/status/2121447753410904131 (Cursor/Fireworks AI-infra supply-chain breach) and /2121423646539604228 (Project Zero "Full X" disclosure policy)
- https://x.com/saxenism/status/2121239127467434217 (email .zip PoC blocked by Workspace) and /2121167157329584138 (L1 secure-release / patch-gap)
- https://x.com/garethheyes/status/2121236435273675134 (PHP XOR-string WAF/filter bypass; quoting @pad1ryoshi)
- https://x.com/albinowax/status/2121234124476183016 (RCE proof-of-impact / pivot trend; with @zseano) · https://x.com/NahamSec/status/2121246957616390355 (NahamCon "Weird Ways to Hack Gemini")

Writeups fetched:
- https://cursor.com/blog/security-incident-update ; https://fireworks.ai/security/bulletins/october-2026-security-incident (+ -update) ; https://projectzero.google/2026/11/disclosure-policy.html ; https://asymmetric.com/blog/conference-week-opsec-a-guide/
- Telegram @defendor_eng new msgs: https://www.certik.com/blog/arcus-incident-analysis ; https://www.certora.com/blog/auditing-smart-contracts-sui (+SlowMist Pennysia and b612security are x.com, link-only) ; +40 from the DeFi backlog (rekt.news, QuillAudits, Cantina, ToB, OpenZeppelin, etc.)
- Telegram @dailybountywriteup: https://securitycipher.com/2026/11/12/github-actions-secret-stealer-wfx/ ; +150 HackerOne public reports from the backlog (via /reports/<id>.json). Medium/infosecwriteups/osintteam remain HTTP 403 and stay pending.

Telegram previews: https://t.me/s/defendor_eng (+4: 2337-2340), https://t.me/s/dailybountywriteup (+2: 14982-14983).

CVE/advisory: CVEProject/cvelistV5 deltas 2026-11-13_end_of_day + 2026-11-14_0500Z (736 new, 1,855 updated; Microsoft ~1,095, Android 116, WordPress 109, Google 103, Fortinet 32, Intel 27, PHP 16). github/advisory-database git pull (GHSA reviewed 37,810). CISA KEV refetched → catalog 2026.11.13, 1,781 (joined CVE-2026-114713 UnrealIRCd, CVE-2026-123039 Check Point). Linux-kernel vulns.git pulled (head 84a53c8, 2026-11-13). Exploit-DB unchanged. ZDI full-text backfill completed (all 17,361 advisories now have text). Repo advisories: erigon GHSA-4c6q-hpx8-75wm (Ethereum); russh GHSA-9264-jvgf-6w2f, GHSA-736f-c93q-9fwx (crypto/RustSec).
HackerOne: GraphQL CompleteHacktivityReportIndex disclosed_at:[2026-11-12 TO 2026-11-15] → +2 reports (4175245 Basecamp stored XSS→admin takeover, 4000535 PortSwigger Burp OpenAPI $id local-file read).
10.0.0.1 - campaign feed: apex-hunter/okta-bugcrowd-2026-11 (okta S1, 3 technique records)
session-feed: apex-hunter/thegraph 2026-11-16 — 3 technique rows appended
- 2026-11-16 apex-hunter/aera-2026-11-16 campaign feed: +4 records (vault pricing class, dead-code invariants, unaudited-rewrite gap, merkle value leaf)

## 2026-11-18 daily run (Africa/Lagos)
- X (Grok Bot connector `x`, search_posts_all, 8 grouped handle queries since 2026-11-17T05:30Z + pagination, backfill n6c/n6e): ~30 reads used of 1000; 971 remaining at last check.
- Writeups fetched: calif.io/java4shell, openjdk/jdk PR 32781, datadog securitylabs, vulncheck, access.redhat.com RHSB-2026-018, sysdig, tenable FAQ, security.berkeley.edu, bleepingcomputer (all Java4Shell); jira.atlassian.com/browse/JSDSERVER-16892 (+rapid7 fallback), wiz.io scan-for-good; github.com/mdpsec/huntdeck README; blackboxarena.ai board (2026-11-18 snapshot). Failed/skipped: github.com/PortSwigger/frag (404; README already in repo), x.com article by saxenism (not retrievable by curl), thedefiant (n/a today), Medium mirrors (scribe.rip 404, freedium unreachable, r.jina.ai 401).
- Telegram previews: https://t.me/s/defendor_eng (+5: 2354-2358), https://t.me/s/dailybountywriteup (+2: 14987-14988); x.com links of new defendor messages fetched through the X API (Lighter article, SlowMist alert, Blockaid, ZachXBT partial).
- GitHub Security Advisories: ZcashFoundation/zebra (+10), zcash/lightwalletd (+14), hyperledger/besu (+4); `solana-program/solana-program-library` returns 404 for advisories.
- CVE: cvelistV5 28 delta zips since 2026-11-17T03:00Z; NVD API lastModStartDate=2026-11-17..; CISA KEV 2026.11.17; OSV/GHSA re-pull; HackerOne GraphQL hacktivity [2026-11-16..2026-11-18]; ZDI index unchanged.

## 2026-11-19 daily run (Africa/Lagos)
- X (Grok Bot connector `x`): `search_posts_all` ×4 grouped handle queries since 2026-11-18T05:00Z (+ pagination), backfill n6c/n6e ×28 pages, `get_posts_by_ids` ×10 batches (942 ids) to restore long-form text, entities and conversation ids; t.co links resolved with curl. ~56 reads used; 944 of 1000 remaining at last check.
- Writeups fetched: wiz.io/blog (NGINX CVE-2026-123633/123007), xint.io blog (nginx2root), portswigger.net/research/achieving-the-impossible-xss-in-innerhtml-without-equals, github.com (kankodu lending CTF README), eprint.iacr.org/2026/1470, blackboxarena.ai (Gemini 4 Neon Max page; DeepSeek V4.1 Flash providers page), NahamCon Prompt2Pwn page. Failed: my.f5.com K000163928 (JS-rendered, no content), my.f5.com K000163926 (read timeout); nginx2root.com is a landing page only (Xint blog used instead).
- Telegram previews: https://t.me/s/defendor_eng (+5: 2359–2363), https://t.me/s/dailybountywriteup (+3: 14989–14991). x.com links of new defendor messages fetched through the X API (SEAL, CDSecurity, Blockaid ×2, ExVul). dailybounty backlog: 304 Medium-family URLs fetched from Wayback Machine snapshots (`archive.org/wayback/available` → `web.archive.org/web/<ts>id_/<url>`), 197 recorded as failed (no snapshot / unusable); 25 defendor failed-URL retries still failing.
- GitHub Security Advisories: zcash/librustzcash (+1 GHSA-4q7w-cx94-55pc), axiom-crypto/snark-verifier (+1 GHSA-265x-v3qf-ff6p); `solana-program/solana-program-library` advisories return 404.
- CVE: cvelistV5 27 delta zips since 2026-11-18T04:57:55Z; NVD API lastModStartDate=2026-11-18..; CISA KEV 2026.11.18 (+4); github/advisory-database pull (5a263e90); OSV all.zip re-pull; kernel vulns.git (f418c111); ZDI published/2026 (+28); Exploit-DB unchanged (70bbef3f); Project Zero unchanged (258); HackerOne GraphQL hacktivity [2026-11-18..2026-11-19] (+2).
- mdpsec.com checked (unchanged).
- 2026-11-17 apex-hunter/0x-immunefi S2+S3 campaigns: +4 findings rows (deployment-skew gates, ERC-7739 marker trap, AH probe-bound, strict-entry-decoder shield).
- 2026-11-19 apex-hunter/hibachi-immunefi S1+S2 campaigns: +3 findings rows (unsigned trigger fields, withdraw replay, two-plane identity fixture).
2026-11-19: apex-hunter/base-everest-s1 campaign feed — 5 technique records (comp re-run protocol, clone-gating, arithmetic elimination, parity mirror fuzz, live-config probes)

## 2026-11-20 daily run (Africa/Lagos)
- X (Grok Bot connector `x`, `search_posts_all`): 4 grouped handle queries since 2026-11-19T05:00Z (+ pagination to the window boundary), backfill n6c/n6e ×4 pages each, `get_posts_by_ids` ×1 batch (32 ids) to restore note_post/entities/conversation ids; t.co links resolved with curl. ~24 reads used of 1000. **177 new posts** archived into store.json; 15 verbatim post files + analysis written. Security-relevant captures:
  - https://x.com/S1r1u5_/status/2123497267340710122 ("2shell" CVEs exploited vs live targets but non-portable) + /2123294703210946988 + /2123504275980750858 (breach apocalypse)
  - https://x.com/galnagli/status/2123296653692301598 (Gemini 4 Neon SOTA web-pentest, denies black-box web testing)
  - https://x.com/Rhynorater/status/2123457669428076895 (prompt-injection in reports vs AI false-dupes)
  - https://x.com/mdp_sec/status/2123629909692039302 (unauth PII CSV 15k emails, medium→High) · /2123327919783059471 ($3,500 Bugcrowd LFI) · /2123358119392911553 (huntdeck open-sourced) · /2123388317786128746 (AI precision gate) · /2123509113745498345 (BB Arena board)
  - https://x.com/zellic_io/status/2123492765581676620 (x86 formal verification of glibc memrchr)
- Writeups fetched: https://www.zellic.io/blog/x86-formal-verification-memrchr ; https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/ ; https://securitycipher.com/2026/11/18/java2shell-cve-2026-114938-lab/ ; 3 x.com posts linked from @defendor_eng (CertiK PolinRider, CD Security newsletter, 4hm8d Templar dispute). dailybounty backlog +12 via job.
- Telegram previews: https://t.me/s/defendor_eng (+3: 2364-2366), https://t.me/s/dailybountywriteup (+2: 14992-14993).
- HackerOne: GraphQL CompleteHacktivityReportIndex disclosed_at:[2026-11-18 TO 2026-11-20] → +1 report (2256569 notification-reactions IDOR). Inventory 12,764.
- CVE/advisory: cvelistV5 28 delta zips since 2026-11-19T04:59Z (1,039 new / 5,683 updated; Microsoft ~4,908, linux-kernel 265, oracle-java 213, cisco 146, google-chrome 113, android 60, wordpress 22, apache 19, php 19). NVD lastModStartDate=2026-11-19T05:18.. (1,039 new / 966 updated → 429,286). CISA KEV refetched → unchanged (2026.11.18, 1,786). github/advisory-database git pull (72f482cd). OSV all.zip re-pull. Linux-kernel vulns.git pulled (73eb6a58, 2026-11-20) → kernel CNA 19,070. Exploit-DB unchanged (70bbef3f). ZDI index unchanged (17,445). Crypto/ZK advisories: snark-verifier GHSA-x26x-7f4v-cqx7 (Halo2 point-at-infinity, CVE-2026-62337), falcon-rust GHSA-25rm-9wvm-m38v (Gaussian sampler 2^-33). No new repo advisories on tracked Zcash/Ethereum/Solana repos (SPL endpoint 404).
- Backfill: n6c (trailofbits) +67 → 2017-11-09; n6e (samczsun/pcaversaccio) +61 → 2023-08-11; both OPEN.
- mdpsec.com checked (unchanged: 591 reports / 150 critical).
