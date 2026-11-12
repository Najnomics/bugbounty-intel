# Sources log

Everything consulted while building this knowledge base. **Consulted** dates are 11 November 2026 (Africa/Lagos) unless noted. **Published** dates are converted to WAT when the source was an X post with a UTC timestamp.

X data came from the public-read `x` MCP tools (`get_users_by_usernames`, `get_posts_by_ids`, `get_users_posts`, `search_posts_all`). Web pages were fetched or summarized via WebSearch / WebFetch. No posts were liked, reposted, or replied to.

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
