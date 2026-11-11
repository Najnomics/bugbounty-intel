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
