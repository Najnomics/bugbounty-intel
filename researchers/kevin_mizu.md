# @kevin_mizu

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/kevin_mizu/`](../posts/kevin_mizu/); full writeups under [`writeups/kevin_mizu/`](../writeups/kevin_mizu/).

| Field | Value |
| --- | --- |
| X | [@kevin_mizu](https://x.com/kevin_mizu) (user id 866258514196484096, joined 2017-05-21) |
| Name (profile) | Kévin GERVOT (Mizu) |
| Followers (11 Nov 2026) | 7034 |
| Bio (verbatim) | Vulnerabilty researcher at @assetnote 🐛 / DOMLogger++ developer 👨🏻‍💻 / CTF with @FlatNetworkOrg, @rhackgondins 🦦 / @ECSC_TeamFrance 2023 🇫🇷 |
| Specialty | Web (XSS, DOMPurify, logic) |
| Platforms | HackerOne (Best Hacker at an LHE, per post); Assetnote/SLCyberSec |
| Evidence of valid finds | MariaDB GRANT PROXY disclosure, Cloudflare /cdn-cgi/image XSS, DOMPurify Safari SMIL bypass. |

## Key findings and analysis

### MariaDB: any user can change root password

- Post: https://x.com/kevin_mizu/status/2097055819447550388 — verbatim: [`posts/kevin_mizu/2026-09-07-2097055819447550388.md`](../posts/kevin_mizu/2026-09-07-2097055819447550388.md)
- **Bug class:** Logic / privilege escalation
- **Root cause:** GRANT PROXY handling let any user act as root (see writeups/kevin_mizu/hackerone-report-3876430.md).
- **How it was found:** Reading permission logic.
- **Takeaways:** Logic bugs in DB auth.

### Cloudflare /cdn-cgi/image XSS

- Post: https://x.com/kevin_mizu/status/2115448862869500312 — verbatim: [`posts/kevin_mizu/2026-10-28-2115448862869500312.md`](../posts/kevin_mizu/2026-10-28-2115448862869500312.md)
- **Bug class:** XSS via CSP/caching
- **Root cause:** See post.
- **How it was found:** Research with hash_kitten.
- **Takeaways:** —

### DOMPurify ≤3.2.6 Safari SMIL bypass

- Post: https://x.com/kevin_mizu/status/2089366491179122821 — verbatim: [`posts/kevin_mizu/2026-08-17-2089366491179122821.md`](../posts/kevin_mizu/2026-08-17-2089366491179122821.md)
- **Bug class:** Sanitizer bypass (mXSS)
- **Root cause:** See writeups/kevin_mizu/dompurify-bypass-smil-animatetransform-safari.md.
- **How it was found:** —
- **Takeaways:** Browser-specific parsing differences break sanitizers.

## All captured posts (verbatim files)

- 2026-09-07 — A logical bug that I've reported to MariaDB has just been disclosed! 🎉 — [`posts/kevin_mizu/2026-09-07-2097055819447550388.md`](../posts/kevin_mizu/2026-09-07-2097055819447550388.md) · https://x.com/kevin_mizu/status/2097055819447550388
- 2026-10-28 — With @hash_kitten, we've been looking into Cloudflare's /cdn-cgi/image endpoint and managed to get an XSS :D — [`posts/kevin_mizu/2026-10-28-2115448862869500312.md`](../posts/kevin_mizu/2026-10-28-2115448862869500312.md) · https://x.com/kevin_mizu/status/2115448862869500312
- 2026-10-07 — I'm happy that my first article as part of the @SLCyberSec research team is finally out! 😁 — [`posts/kevin_mizu/2026-10-07-2107783292091007306.md`](../posts/kevin_mizu/2026-10-07-2107783292091007306.md) · https://x.com/kevin_mizu/status/2107783292091007306
- 2026-08-17 — Recently, I've been looking at DOMPurify again, trying to find ways to bypass 3.x.x after browsers started enc — [`posts/kevin_mizu/2026-08-17-2089366491179122821.md`](../posts/kevin_mizu/2026-08-17-2089366491179122821.md) · https://x.com/kevin_mizu/status/2089366491179122821
- 2026-07-09 — It was a really fun event! Thanks to @Hacker0x01 and Salesforce for the invitation! — [`posts/kevin_mizu/2026-07-09-2075234997246496822.md`](../posts/kevin_mizu/2026-07-09-2075234997246496822.md) · https://x.com/kevin_mizu/status/2075234997246496822

## Writeups saved (full text)

- [`writeups/kevin_mizu/dompurify-bypass-smil-animatetransform-safari.md`](../writeups/kevin_mizu/dompurify-bypass-smil-animatetransform-safari.md)
- [`writeups/kevin_mizu/hackerone-report-3876430.md`](../writeups/kevin_mizu/hackerone-report-3876430.md)

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 7 finding(s). Full verbatim posts under `posts/kevin_mizu/`._

- **MariaDB: any user can change root password** (`Logic / privilege escalation`)
  - post: https://x.com/kevin_mizu/status/2097055819447550388
  - local: `posts/kevin_mizu/2026-09-07-2097055819447550388.md`, `writeups/kevin_mizu/dompurify-bypass-smil-animatetransform-safari.md`, `writeups/kevin_mizu/hackerone-report-3876430.md`
- **Cloudflare /cdn-cgi/image XSS** (`XSS via CSP/caching`)
  - post: https://x.com/kevin_mizu/status/2115448862869500312
  - local: `posts/kevin_mizu/2026-10-28-2115448862869500312.md`, `writeups/kevin_mizu/dompurify-bypass-smil-animatetransform-safari.md`, `writeups/kevin_mizu/hackerone-report-3876430.md`
- **DOMPurify ≤3.2.6 Safari SMIL bypass** (`Sanitizer bypass (mXSS)`)
  - post: https://x.com/kevin_mizu/status/2089366491179122821
  - local: `posts/kevin_mizu/2026-08-17-2089366491179122821.md`, `writeups/kevin_mizu/dompurify-bypass-smil-animatetransform-safari.md`, `writeups/kevin_mizu/hackerone-report-3876430.md`
- **Discourse: ImageMagick JPEG race + polyglot → arbitrary file read/RCE (CVE-2026-55420); also cache-poisoning XSS (CVE-2026-55674)** (`file-upload`)
  - post: https://x.com/kevin_mizu/status/2107783292091007306
  - local: `posts/kevin_mizu/2026-10-07-2107783292091007306.md`
- **DOMPurify bypass under CUSTOM_ELEMENT_HANDLING + FORBID_CONTENT (non-default)** (`xss`)
  - post: https://x.com/kevin_mizu/status/1760341445872144520
  - local: `posts/kevin_mizu/ARCHIVE.md`, `data/x_posts.jsonl`
- **dompurify-bypass-smil-animatetransform-safari** (`xss`)
  - post: https://mizu.re/post/dompurify-bypass-smil-animatetransform-safari
  - local: `writeups/kevin_mizu/dompurify-bypass-smil-animatetransform-safari.md`
- **HackerOne report #3876430: MariaDB GRANT PROXY permits unauthorized authentication changes and administrator account takeover** (`auth-bypass`)
  - post: https://hackerone.com/reports/3876430
  - local: `writeups/kevin_mizu/hackerone-report-3876430.md`
