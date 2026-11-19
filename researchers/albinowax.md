# @albinowax

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/albinowax/`](../posts/albinowax/).

| Field | Value |
| --- | --- |
| X | [@albinowax](https://x.com/albinowax) (user id 109850328, joined 2010-01-30) |
| Name (profile) | James Kettle |
| Followers (11 Nov 2026) | 85837 |
| Bio (verbatim) | Director of Research at @PortSwigger. Startup advisor. Find my research, tools & contact details at https://t.co/vP6UbGmvl3 |
| Specialty | Web (HTTP desync) |
| Platforms | PortSwigger research |
| Evidence of valid finds | HTTP request smuggling research. |
| Links | https://portswigger.net/research |

## Key findings and analysis

### $300k for a trusted internal header

- Post: https://x.com/albinowax/status/2117935178278371560 — verbatim: [`posts/albinowax/2026-11-04-2117935178278371560.md`](../posts/albinowax/2026-11-04-2117935178278371560.md)
- **Bug class:** Header trust / auth bypass
- **Root cause:** Internal header trusted from outside.
- **How it was found:** —
- **Takeaways:** Try Param Miner for hidden headers.

## All captured posts (verbatim files)

- 2026-10-01 — SMTP smuggling is back! Dot-stuffing is a great find, awesome work! — [`posts/albinowax/2026-10-01-2105615340088762638.md`](../posts/albinowax/2026-10-01-2105615340088762638.md) · https://x.com/albinowax/status/2105615340088762638
- 2026-11-04 — $300k for a trusted internal header! I wonder if Param Miner found it... congrats to the discoverer either way — [`posts/albinowax/2026-11-04-2117935178278371560.md`](../posts/albinowax/2026-11-04-2117935178278371560.md) · https://x.com/albinowax/status/2117935178278371560
- 2026-10-13 — I've started a new research project for Black Hat USA 2027 and I'm pleased to announce it has nothing to do wi — [`posts/albinowax/2026-10-13-2110004455244505511.md`](../posts/albinowax/2026-10-13-2110004455244505511.md) · https://x.com/albinowax/status/2110004455244505511
- 2026-11-02 — I've been nominated for the SANS Difference Makers Awards, in the Red Teamer category! I'd love your vote: — [`posts/albinowax/2026-11-02-2117261005268869507.md`](../posts/albinowax/2026-11-02-2117261005268869507.md) · https://x.com/albinowax/status/2117261005268869507
- 2026-10-23 — daybreak-blue cares so much about authorisation, I asked it to patch a bug in "scope add" and it removed the f — [`posts/albinowax/2026-10-23-2113624732952338477.md`](../posts/albinowax/2026-10-23-2113624732952338477.md) · https://x.com/albinowax/status/2113624732952338477

## Writeups saved (full text)

- None fetched in this pass.

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 1 finding(s). Full verbatim posts under `posts/albinowax/`._

- **$300k for a trusted internal header** (`Header trust / auth bypass`)
  - post: https://x.com/albinowax/status/2117935178278371560
  - local: `posts/albinowax/2026-11-04-2117935178278371560.md`


### Update 2026-11-19

- **NGINX HTTP/2 RCE disclosure → request-smuggling window** — https://x.com/albinowax/status/2123100309065199643 — [`posts/albinowax/2026-11-18-2123100309065199643.md`](../posts/albinowax/2026-11-18-2123100309065199643.md); quoted Wiz thread (nirohfeld) on CVE-2026-123633/123007, full Wiz writeup [`writeups/albinowax/wiz-nginx-http2-rce-cve-2026-123633-123007.md`](../writeups/albinowax/wiz-nginx-http2-rce-cve-2026-123633-123007.md).
  - Methodology: the mitigation (disable HTTP/2) pushes front-ends back to HTTP/1.1 → re-scan for CL.TE/TE.CL/H2-downgrade desync on hosts whose ALPN dropped `h2`. Takeaway: diff ALPN per host between recon snapshots and queue smuggling scans on changes.
