# @asymmetric_re

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/asymmetric_re/`](../posts/asymmetric_re/).

| Field | Value |
| --- | --- |
| X | [@asymmetric_re](https://x.com/asymmetric_re) (user id 1696517900159631360, joined 2023-08-29) |
| Name (profile) | asymmetric research |
| Followers (11 Nov 2026) | 5401 |
| Bio (verbatim) | Security that starts below the surface. Join us: https://t.co/rD1LdScnpd |
| Specialty | Web3 (Solana) |
| Platforms | Immunefi (#1 Barracuda3172 is associated per leaderboard search) |
| Evidence of valid finds | Solana governance vote-erasure bug. |

## Key findings and analysis

### Solana governance: any validator could silently erase its delegators' dissenting votes

- Post: https://x.com/asymmetric_re/status/2112236410455597403 — verbatim: [`posts/asymmetric_re/2026-10-19-2112236410455597403.md`](../posts/asymmetric_re/2026-10-19-2112236410455597403.md)
- **Bug class:** Governance program logic
- **Root cause:** For its first 6 weeks on mainnet the governance program let a validator erase delegators' dissenting votes; without the fix SGP-0002 would have failed by 0.02 percentage points (per post).
- **How it was found:** Found with their tool Crucible (per post).
- **Takeaways:** Governance vote-accounting is security-critical; check who can overwrite or reset another party's vote record.

## All captured posts (verbatim files)

- 2026-10-19 — For its first 6 weeks on mainnet, Solana's governance program had a bug: any validator could silently erase it — [`posts/asymmetric_re/2026-10-19-2112236410455597403.md`](../posts/asymmetric_re/2026-10-19-2112236410455597403.md) · https://x.com/asymmetric_re/status/2112236410455597403
- 2026-06-23 — The Open Protocol Security Coalition (OPSeC) is a new initiative by @fund_defi, in partnership with @_SEAL_Org — [`posts/asymmetric_re/2026-06-23-2069405607782965335.md`](../posts/asymmetric_re/2026-06-23-2069405607782965335.md) · https://x.com/asymmetric_re/status/2069405607782965335
- 2026-09-22 — The @SolanaFndn just open-sourced Microscope, a free monitoring &amp; alerting tool for Solana programs. — [`posts/asymmetric_re/2026-09-22-2102397819386745185.md`](../posts/asymmetric_re/2026-09-22-2102397819386745185.md) · https://x.com/asymmetric_re/status/2102397819386745185
- 2026-07-09 — Anchor's release pipeline just got a major security upgrade. — [`posts/asymmetric_re/2026-07-09-2075265472107556875.md`](../posts/asymmetric_re/2026-07-09-2075265472107556875.md) · https://x.com/asymmetric_re/status/2075265472107556875
- 2026-10-29 — Different implementations, same underlying vulnerabilities. — [`posts/asymmetric_re/2026-10-29-2115842298563187037.md`](../posts/asymmetric_re/2026-10-29-2115842298563187037.md) · https://x.com/asymmetric_re/status/2115842298563187037

## Writeups saved (full text)

- None fetched in this pass.

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 1 finding(s). Full verbatim posts under `posts/asymmetric_re/`._

- **Solana governance: any validator could silently erase its delegators' dissenting votes** (`Governance program logic`)
  - post: https://x.com/asymmetric_re/status/2112236410455597403
  - local: `posts/asymmetric_re/2026-10-19-2112236410455597403.md`
