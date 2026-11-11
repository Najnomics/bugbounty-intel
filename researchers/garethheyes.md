# @garethheyes

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/garethheyes/`](../posts/garethheyes/); full writeups under [`writeups/garethheyes/`](../writeups/garethheyes/).

| Field | Value |
| --- | --- |
| X | [@garethheyes](https://x.com/garethheyes) (user id 16879627, joined 2008-10-21) |
| Name (profile) | Gareth Heyes \u2028 |
| Followers (11 Nov 2026) | 39816 |
| Bio (verbatim) | Web security researcher at PortSwigger. Author of JS for Hackers and Hackvertor.  https://t.co/akVN6ZR4C8 |
| Specialty | Web (XSS) |
| Platforms | PortSwigger research |
| Evidence of valid finds | XSS research; Frag CSS exfil tool. |
| Links | https://portswigger.net/research |

## Key findings and analysis

### XSS from a response header (Firefox XSLT via Link header)

- Post: https://x.com/garethheyes/status/2115088588874650054 — verbatim: [`posts/garethheyes/2026-10-27-2115088588874650054.md`](../posts/garethheyes/2026-10-27-2115088588874650054.md)
- **Bug class:** XSS
- **Root cause:** Firefox loads XSLT from a data: URL in a Link header.
- **How it was found:** —
- **Takeaways:** —

### Frag: CSS-only token exfiltration

- Post: https://x.com/garethheyes/status/2118691773333782693 — verbatim: [`posts/garethheyes/2026-11-06-2118691773333782693.md`](../posts/garethheyes/2026-11-06-2118691773333782693.md)
- **Bug class:** CSS injection
- **Root cause:** See writeups/garethheyes/frag-readme.md.
- **How it was found:** —
- **Takeaways:** —

## All captured posts (verbatim files)

- 2026-10-27 — XSS from a response header 🤯 — [`posts/garethheyes/2026-10-27-2115088588874650054.md`](../posts/garethheyes/2026-10-27-2115088588874650054.md) · https://x.com/garethheyes/status/2115088588874650054
- 2026-11-06 — I built a new tool called Frag. A CSS-only token exfiltration tool. No JavaScript needed. Inject a stylesheet, — [`posts/garethheyes/2026-11-06-2118691773333782693.md`](../posts/garethheyes/2026-11-06-2118691773333782693.md) · https://x.com/garethheyes/status/2118691773333782693
- 2026-10-28 — Hackvertor now supports encoding and decoding reverse JS fuck — [`posts/garethheyes/2026-10-28-2115416967050141971.md`](../posts/garethheyes/2026-10-28-2115416967050141971.md) · https://x.com/garethheyes/status/2115416967050141971
- 2026-10-28 — Oh Hackvertor now decodes JS Fuck now because you know that's like a 2 min job now. — [`posts/garethheyes/2026-10-28-2115425425367199834.md`](../posts/garethheyes/2026-10-28-2115425425367199834.md) · https://x.com/garethheyes/status/2115425425367199834

## Writeups saved (full text)

- [`writeups/garethheyes/frag-readme.md`](../writeups/garethheyes/frag-readme.md)
- [`writeups/garethheyes/ikaes-strings-without-parentheses.md`](../writeups/garethheyes/ikaes-strings-without-parentheses.md)
- [`writeups/garethheyes/portswigger-scalable-vector-grief.md`](../writeups/garethheyes/portswigger-scalable-vector-grief.md)

## Key findings (mined into harness)

_Auto-maintained from `harness/findings.jsonl`. 6 finding(s). Full verbatim posts under `posts/garethheyes/`._

- **XSS from a response header (Firefox XSLT via Link header)** (`XSS`)
  - post: https://x.com/garethheyes/status/2115088588874650054
  - local: `posts/garethheyes/2026-10-27-2115088588874650054.md`, `writeups/garethheyes/frag-readme.md`, `writeups/garethheyes/ikaes-strings-without-parentheses.md`
- **Frag: CSS-only token exfiltration** (`CSS injection`)
  - post: https://x.com/garethheyes/status/2118691773333782693
  - local: `posts/garethheyes/2026-11-06-2118691773333782693.md`, `writeups/garethheyes/frag-readme.md`, `writeups/garethheyes/ikaes-strings-without-parentheses.md`
- **CSRF token leaked via search form URL + sandboxed-iframe baseURI theft** (`csrf`)
  - post: https://x.com/garethheyes/status/1834985571422245055
  - local: `posts/garethheyes/ARCHIVE.md`, `data/x_posts.jsonl`
- **frag-readme** (`web`)
  - post: https://raw.githubusercontent.com/hackvertor/frag/main/README.md
  - local: `writeups/garethheyes/frag-readme.md`
- **ikaes-strings-without-parentheses** (`xss`)
  - post: https://blog.ikaes.de/generating-strings-without-parentheses-in-javascript/
  - local: `writeups/garethheyes/ikaes-strings-without-parentheses.md`
- **portswigger-scalable-vector-grief** (`xss`)
  - post: https://portswigger.net/research/scalable-vector-grief
  - local: `writeups/garethheyes/portswigger-scalable-vector-grief.md`
