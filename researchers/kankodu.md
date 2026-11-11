# @kankodu

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/kankodu/`](../posts/kankodu/).

| Field | Value |
| --- | --- |
| X | [@kankodu](https://x.com/kankodu) (user id 1549732767692627970, joined 2022-07-20) |
| Name (profile) | kankodu |
| Followers (11 Nov 2026) | 3675 |
| Bio (verbatim) | Security Researcher |
| Specialty | Web3 |
| Platforms | Independent |
| Evidence of valid finds | EtherFi hack analysis. |

## Key findings and analysis

### EtherFi helper contract hack — three holes lined up

- Post: https://x.com/kankodu/status/2098377603396915590 — verbatim: [`posts/kankodu/2026-09-11-2098377603396915590.md`](../posts/kankodu/2026-09-11-2098377603396915590.md)
- **Bug class:** Smart contract: unsafe callback + stale approval + EIP-7702
- **Root cause:** AtomicQueue called a callback on a user-provided address and treated a successful call as intent (no required return data); the victim had a year-old hanging approval; EIP-7702 delegation made the victim EOA execute code, so the callback no longer simply failed.
- **How it was found:** Post-incident analysis.
- **Takeaways:** Require specific callback return data; revoke stale approvals; re-audit EOA-assumptions after EIP-7702.

## All captured posts (verbatim files)

- 2026-09-11 — Today's hack of EtherFi helper contract is a good example of how multiple holes in a system can line up to cre — [`posts/kankodu/2026-09-11-2098377603396915590.md`](../posts/kankodu/2026-09-11-2098377603396915590.md) · https://x.com/kankodu/status/2098377603396915590
- 2026-11-08 — Uniswap V4 Position Manager is being used as an example of highly used contract that will be broken after Glam — [`posts/kankodu/2026-11-08-2119414649204699528.md`](../posts/kankodu/2026-11-08-2119414649204699528.md) · https://x.com/kankodu/status/2119414649204699528
- 2026-01-16 — Here's where you can do some weekend bug hunting: — [`posts/kankodu/2026-01-16-2012219532056645916.md`](../posts/kankodu/2026-01-16-2012219532056645916.md) · https://x.com/kankodu/status/2012219532056645916

## Writeups saved (full text)

- None fetched in this pass.
