# @infosec_au

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/infosec_au/`](../posts/infosec_au/); full writeups under [`writeups/infosec_au/`](../writeups/infosec_au/).

| Field | Value |
| --- | --- |
| X | [@infosec_au](https://x.com/infosec_au) (user id 1674598830, joined 2013-08-16) |
| Name (profile) | shubs |
| Followers (11 Nov 2026) | 60244 |
| Bio (verbatim) | Co-founder, security researcher. Building an attack surface management platform, @assetnote |
| Specialty | Web / pre-auth RCE |
| Platforms | Independent / Assetnote |
| Evidence of valid finds | cPanel pre-auth criticals; car-unlock research with samwcyo; react2shell scanner. |
| Links | https://www.assetnote.io |

## Key findings and analysis

### Remote unlock of cars in AU and US

- Post: https://x.com/infosec_au/status/2119025620969828598 — verbatim: [`posts/infosec_au/2026-11-07-2119025620969828598.md`](../posts/infosec_au/2026-11-07-2119025620969828598.md)
- **Bug class:** Auth/API flaws in automotive backend
- **Root cause:** See writeups/infosec_au/unlocking-any-car.md.
- **How it was found:** Backend/API research on the automaker.
- **Takeaways:** Connected-vehicle APIs often trust weak identity binding.

### cPanel pre-auth critical

- Post: https://x.com/infosec_au/status/2053414439635054961 — verbatim: [`posts/infosec_au/2026-05-10-2053414439635054961.md`](../posts/infosec_au/2026-05-10-2053414439635054961.md)
- **Bug class:** Pre-auth RCE chain
- **Root cause:** See post.
- **How it was found:** —
- **Takeaways:** —

## All captured posts (verbatim files)

- 2025-12-05 — Vercel is questioning whether or not a WAF bypass is possible... Pushed an update that uses a payload from @SL — [`posts/infosec_au/2025-12-05-1997063075422429657.md`](../posts/infosec_au/2025-12-05-1997063075422429657.md) · https://x.com/infosec_au/status/1997063075422429657
- 2025-12-05 — Pushed a new update to  -- it now scans for the RCE payload via reflection. Use the --waf-bypass flag to bypas — [`posts/infosec_au/2025-12-05-1996737719356297595.md`](../posts/infosec_au/2025-12-05-1996737719356297595.md) · https://x.com/infosec_au/status/1996737719356297595
- 2026-11-07 — Earlier this year, I hacked a major automotive company with @samwcyo. We were able to remotely unlock cars in  — [`posts/infosec_au/2026-11-07-2119025620969828598.md`](../posts/infosec_au/2026-11-07-2119025620969828598.md) · https://x.com/infosec_au/status/2119025620969828598
- 2026-05-10 — Reported another cPanel critical pre-authentication vuln. Our research dates back to early April, but this exp — [`posts/infosec_au/2026-05-10-2053414439635054961.md`](../posts/infosec_au/2026-05-10-2053414439635054961.md) · https://x.com/infosec_au/status/2053414439635054961
- 2026-08-01 — Things are getting weird (or interesting?) in the vulnerability research space. I published some of my persona — [`posts/infosec_au/2026-08-01-2083521903667671316.md`](../posts/infosec_au/2026-08-01-2083521903667671316.md) · https://x.com/infosec_au/status/2083521903667671316

## Writeups saved (full text)

- [`writeups/infosec_au/frontier-class-vulnerabilities.md`](../writeups/infosec_au/frontier-class-vulnerabilities.md)
- [`writeups/infosec_au/react2shell-scanner-readme.md`](../writeups/infosec_au/react2shell-scanner-readme.md)
- [`writeups/infosec_au/unlocking-any-car.md`](../writeups/infosec_au/unlocking-any-car.md)
