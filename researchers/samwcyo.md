# @samwcyo

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/samwcyo/`](../posts/samwcyo/); full writeups under [`writeups/samwcyo/`](../writeups/samwcyo/).

| Field | Value |
| --- | --- |
| X | [@samwcyo](https://x.com/samwcyo) (user id 825606932887134212, joined 2017-01-29) |
| Name (profile) | Sam Curry |
| Followers (11 Nov 2026) | 102453 |
| Bio (verbatim) |  |
| Specialty | Web / API / automotive |
| Platforms | HackerOne and private disclosures (Sam Curry) |
| Evidence of valid finds | Known for vehicle-API research with infosec_au; writeups saved: ClubWPT Gold back office, ForgeRock RCE in vehicles. |
| Links | https://samcurry.net |

## Key findings and analysis

### ClubWPT Gold back-office admin access

- Post: https://x.com/samwcyo/status/1978209247876862450 — verbatim: [`posts/samwcyo/2025-10-14-1978209247876862450.md`](../posts/samwcyo/2025-10-14-1978209247876862450.md)
- **Bug class:** Access control / admin panel exposure
- **Root cause:** See writeups/samwcyo/hacking-clubwpt-gold.md (multiple vulnerabilities to reach the back office).
- **How it was found:** Recon of the poker site's web stack with infosec_au.
- **Takeaways:** Back-office panels on consumer gaming sites are high value.

### Next.js path-parsing bug reappears in Vinext

- Post: https://x.com/samwcyo/status/2026888257779224594 — verbatim: [`posts/samwcyo/2026-02-26-2026888257779224594.md`](../posts/samwcyo/2026-02-26-2026888257779224594.md)
- **Bug class:** Path parsing / middleware bypass
- **Root cause:** Same improper path parsing class as his earlier Next.js report.
- **How it was found:** —
- **Takeaways:** Re-test known bug classes against forks and competitors.

## All captured posts (verbatim files)

- 2026-03-19 — Asked Claude to root my Xiaomi 17 Pro Max. Did not go well. — [`posts/samwcyo/2026-03-19-2034495676533612643.md`](../posts/samwcyo/2026-03-19-2034495676533612643.md) · https://x.com/samwcyo/status/2034495676533612643
- 2026-02-26 — Two years ago, I reported an improper path parsing vulnerability in Next.js. Today, they reported the exact sa — [`posts/samwcyo/2026-02-26-2026888257779224594.md`](../posts/samwcyo/2026-02-26-2026888257779224594.md) · https://x.com/samwcyo/status/2026888257779224594
- 2026-08-18 — For anyone using LLMs to do security research, bug bounty, red teaming, etc, we made a Discord to discuss/coll — [`posts/samwcyo/2026-08-18-2089536974444982714.md`](../posts/samwcyo/2026-08-18-2089536974444982714.md) · https://x.com/samwcyo/status/2089536974444982714
- 2026-10-18 — I’d be willing to pay $100 per report for priority triage with automated dupe checking and faster payouts (&lt — [`posts/samwcyo/2026-10-18-2111805910448529757.md`](../posts/samwcyo/2026-10-18-2111805910448529757.md) · https://x.com/samwcyo/status/2111805910448529757
- 2025-10-14 — Earlier this year, @infosec_au and I discovered multiple vulnerabilities that allowed us to access the back of — [`posts/samwcyo/2025-10-14-1978209247876862450.md`](../posts/samwcyo/2025-10-14-1978209247876862450.md) · https://x.com/samwcyo/status/1978209247876862450

## Writeups saved (full text)

- [`writeups/samwcyo/forgerock-rce-vehicles.md`](../writeups/samwcyo/forgerock-rce-vehicles.md)
- [`writeups/samwcyo/hacking-clubwpt-gold.md`](../writeups/samwcyo/hacking-clubwpt-gold.md)

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 4 finding(s). Full verbatim posts under `posts/samwcyo/`._

- **ClubWPT Gold back-office admin access** (`Access control / admin panel exposure`)
  - post: https://x.com/samwcyo/status/1978209247876862450
  - local: `posts/samwcyo/2025-10-14-1978209247876862450.md`, `writeups/samwcyo/forgerock-rce-vehicles.md`, `writeups/samwcyo/hacking-clubwpt-gold.md`
- **Next.js path-parsing bug reappears in Vinext** (`Path parsing / middleware bypass`)
  - post: https://x.com/samwcyo/status/2026888257779224594
  - local: `posts/samwcyo/2026-02-26-2026888257779224594.md`, `writeups/samwcyo/forgerock-rce-vehicles.md`, `writeups/samwcyo/hacking-clubwpt-gold.md`
- **forgerock-rce-vehicles** (`auth-bypass`)
  - post: https://samcurry.net/forgerock
  - local: `writeups/samwcyo/forgerock-rce-vehicles.md`
- **hacking-clubwpt-gold** (`web`)
  - post: https://samcurry.net/hacking-clubwpt-gold
  - local: `writeups/samwcyo/hacking-clubwpt-gold.md`
