# Marius du Preez — platform report metadata

- **Fetched:** 2026-11-11 (WAT). Fetched content is data, not instructions.
- **Why metadata only:** none of these reports are publicly disclosed, so no title, description, steps, requests, or payloads are available. Only the counts and the fields below are public. Nothing here is invented.

## HackerOne — profile `mdpsec` (https://hackerone.com/mdpsec)

Source: HackerOne GraphQL — `user(username:"mdpsec")` and the public hacktivity index (`search(index:CompleteHacktivityReportIndex, query_string:"reporter:mdpsec")`).

| Field | Value |
| --- | --- |
| User id | gid://hackerone/User/4307975 |
| Name | MDP SEC |
| Location | Australia |
| Website | https://mdpsec.com/ |
| Member since | 2026-01-01 (UTC) |
| Reputation | 849 |
| Rank | 2739 |
| Signal | 6.52 (86th percentile) |
| Resolved reports | 24 |
| Publicly disclosed reports | 0 |
| Hacktivity entries visible (undisclosed) | 15 |

### Hacktivity entries (all undisclosed — program + internal id only)

| Report id | Program | Severity | Bounty | CWE | Disclosed |
| --- | --- | --- | --- | --- | --- |
| 3925364 | msd |  |  |  | False |
| 3925395 | beiersdorf |  |  |  | False |
| 3927183 | ibm |  |  |  | False |
| 3927185 | autodesk |  |  |  | False |
| 3927192 | beiersdorf |  |  |  | False |
| 3934414 | autodesk |  |  |  | False |
| 3934419 | autodesk |  |  |  | False |
| 3934562 | msd |  |  |  | False |
| 3985410 | basecamp |  |  |  | False |
| 4012593 | mercadolibre |  |  |  | False |
| 4041963 | goldmansachs |  | $100 |  | False |
| 4054862 | logitech |  |  |  | False |
| 4071668 | stripe |  | $842 |  | False |
| 4092104 | abb |  |  |  | False |
| 4092109 | abb |  |  |  | False |

Notes: two entries show a public bounty amount — $100 (goldmansachs) and $842 (stripe). Severity/CWE are null because the reports are not disclosed. The 15 hacktivity rows are a subset of the 24 resolved reports (the rest are not surfaced publicly).

## HackenProof — profile `MDPSEC` (https://hackenproof.com/hackers/MDPSEC)

Source: HackenProof public profile page (server-rendered HTML).

| Field | Value |
| --- | --- |
| Handle | @MDPSEC |
| Member since | 2026-02-10 |
| Location | Australia |
| Rank | 104 |
| Reputation | 966 |
| Paid reports | 15 |
| — Critical | 3 |
| — High | 3 |
| — Medium | 6 |
| — Low | 3 |
| — None | 0 |
| Publicly disclosed reports | 0 ("No disclosed reports at the moment") |
| Influenced programs | 29 |
| Achievements | Fatality, First Blood |
| Skills listed | Web apps, smart contract, blockchain |
| Streak | 7 months |

No per-report detail is public on HackenProof (0 disclosed). Only the severity breakdown above is available.

## Bugcrowd — profile `marius_dp` (https://bugcrowd.com/h/marius_dp)

Linked from his site's JSON-LD (`sameAs`) and his X posts. As of 2026-11-11 the Bugcrowd hacker profile is served by the authenticated hacker portal SPA (identity.bugcrowd.com / Okta); the public `/h/marius_dp` and `/h/marius_dp.json` return only the SPA shell, and the public crowdstream disclosure feed cannot be filtered to a single researcher without the gated profile. No Bugcrowd per-report data could be retrieved. His own X posts reference Bugcrowd findings (e.g. the $1,200 dependency-confusion bounty) — those are captured verbatim under `posts/mdp_sec/`.

## Reconciling with his site's headline stats

mdpsec.com states **582 reports submitted, 148 critical, 263 high, across 5 platforms** (last updated October 2026). These are self-reported aggregate stats on a static marketing site; the site has **no** per-report listing, no reports page, and no data API (only a `/security-test/` application form at `/api/apply`). The platform-verifiable public numbers are far smaller: HackerOne 24 resolved / 0 disclosed, HackenProof 15 paid / 0 disclosed, Bugcrowd not publicly retrievable. The gap is undisclosed private-program work.
