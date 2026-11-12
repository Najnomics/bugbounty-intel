# Xss

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **13** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- Look for differential parsing of the same URL; regex char-class mistakes are common. (from fransrosen). Source: [`posts/fransrosen/2024-08-27-1828503460183941420.md`](../../posts/fransrosen/2024-08-27-1828503460183941420.md), [`writeups/fransrosen/hackernotes-ep86-xcorrelation.md`](../../writeups/fransrosen/hackernotes-ep86-xcorrelation.md).
- Hunt cross-privilege stored sinks: unauth write surfaces that privileged UIs later render. (from mdp_sec). Source: [`posts/mdp_sec/2026-09-13-2099031404252434591.md`](../../posts/mdp_sec/2026-09-13-2099031404252434591.md).
- Patched CVEs often leave bypasses — re-test the same sink with new encodings/contexts. (from 0xacb). Source: [`posts/0xacb/ARCHIVE.md`](../../posts/0xacb/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Test sanitizer bypasses under non-default option combinations apps actually ship. (from kevin_mizu). Source: [`posts/kevin_mizu/ARCHIVE.md`](../../posts/kevin_mizu/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- — (from garethheyes). Source: [`posts/garethheyes/2026-10-27-2115088588874650054.md`](../../posts/garethheyes/2026-10-27-2115088588874650054.md), [`writeups/garethheyes/frag-readme.md`](../../writeups/garethheyes/frag-readme.md), [`writeups/garethheyes/ikaes-strings-without-parentheses.md`](../../writeups/garethheyes/ikaes-strings-without-parentheses.md).
- — (from kevin_mizu). Source: [`posts/kevin_mizu/2026-10-28-2115448862869500312.md`](../../posts/kevin_mizu/2026-10-28-2115448862869500312.md), [`writeups/kevin_mizu/dompurify-bypass-smil-animatetransform-safari.md`](../../writeups/kevin_mizu/dompurify-bypass-smil-animatetransform-safari.md), [`writeups/kevin_mizu/hackerone-report-3876430.md`](../../writeups/kevin_mizu/hackerone-report-3876430.md).

## Method / findings in sources

- **XSS-challenge solution thread (10 parts)** — The page parsed the query twice with different logic; a regex char class `[?|&]` (pipe treated literally) let a crafted parameter be picked up by one parser but not the other. Source: [`posts/fransrosen/2024-08-27-1828503460183941420.md`](../../posts/fransrosen/2024-08-27-1828503460183941420.md), [`writeups/fransrosen/hackernotes-ep86-xcorrelation.md`](../../writeups/fransrosen/hackernotes-ep86-xcorrelation.md).
- **Stored XSS: unauth API writes into LESS config later sunk in back-office designer** — Unauthenticated API wrote attacker-controlled value into LESS configuration; later a back-office designer loaded that value and inserted it into a string (cross-world source→sink). Source: [`posts/mdp_sec/2026-09-13-2099031404252434591.md`](../../posts/mdp_sec/2026-09-13-2099031404252434591.md).
- **Grafana CVE-2025-6023 bypass → XSS and account takeover (Hack.lu 0day challenge)** — New bypass for a previous Grafana CVE resulting in XSS and account takeover. Solved as 0day challenge at Hack.lu 2025; technical deep dive published. Source: [`posts/0xacb/ARCHIVE.md`](../../posts/0xacb/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **DOMPurify bypass under CUSTOM_ELEMENT_HANDLING + FORBID_CONTENT (non-default)** — DOMPurify bypass when CUSTOM_ELEMENT_HANDLING and FORBID_CONTENT options are used together. Not a default-config bypass; documented for completeness. Source: [`posts/kevin_mizu/ARCHIVE.md`](../../posts/kevin_mizu/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **XSS from a response header (Firefox XSLT via Link header)** — Firefox loads XSLT from a data: URL in a Link header. Source: [`posts/garethheyes/2026-10-27-2115088588874650054.md`](../../posts/garethheyes/2026-10-27-2115088588874650054.md), [`writeups/garethheyes/frag-readme.md`](../../writeups/garethheyes/frag-readme.md), [`writeups/garethheyes/ikaes-strings-without-parentheses.md`](../../writeups/garethheyes/ikaes-strings-without-parentheses.md).
- **Cloudflare /cdn-cgi/image XSS** — See post. Source: [`posts/kevin_mizu/2026-10-28-2115448862869500312.md`](../../posts/kevin_mizu/2026-10-28-2115448862869500312.md), [`writeups/kevin_mizu/dompurify-bypass-smil-animatetransform-safari.md`](../../writeups/kevin_mizu/dompurify-bypass-smil-animatetransform-safari.md), [`writeups/kevin_mizu/hackerone-report-3876430.md`](../../writeups/kevin_mizu/hackerone-report-3876430.md).
- **faav-17-trillion-microsoft-records** — **An estimated 17.3 trillion stored rows across a wide range of Microsoft datasets were reachable through a single internal analytics service, all because it never checked the signature on a login token. That flaw let me claim an administrator’s identity and submit unauthorized SQL queries without any real credentials. I used only table description Source: [`writeups/xssdoctor/faav-17-trillion-microsoft-records.md`](../../writeups/xssdoctor/faav-17-trillion-microsoft-records.md).
- **vulnerability-spoiler-alert-action** — [![GitHub Action](https://img.shields.io/badge/GitHub-Action-2088FF?logo=github-actions&logoColor=white)](https://github.com/marketplace) [![TypeScript](https://img.shields.io/badge/TypeScript-5.3-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) Source: [`writeups/infinitelogins/vulnerability-spoiler-alert-action.md`](../../writeups/infinitelogins/vulnerability-spoiler-alert-action.md).
- **wiz-php2shell-php-rce** — Wiz Research uncovered multiple critical vulnerabilities in core PHP, a popular general-purpose scripting language that powers 70% of all websites in the world. Successful exploitation could allow attackers to take control of affected servers, steal sensitive data, and deface the websites running on them. Source: [`writeups/galnagli/wiz-php2shell-php-rce.md`](../../writeups/galnagli/wiz-php2shell-php-rce.md).
- **portswigger-scalable-vector-grief** — **I tested eight popular SVG sanitizers and bypassed six of them. In this post, I'll show you how a response header can run JavaScript in Firefox even when the response body is completely harmless XML. I'll also show you how to get Safari to import a GIF as SVG and execute JavaScript from it.** Source: [`writeups/garethheyes/portswigger-scalable-vector-grief.md`](../../writeups/garethheyes/portswigger-scalable-vector-grief.md).
- **Rxss + CSTI In Search Field Via Polygot Payload** — Hii Everyone I’m Suryesh a Bug Bounty Hunter. In this write-up/blog i’ll explained about Reflected Xss. So, everything i’ll keep it very simple. Please forgot to any grammatical error. So, Let’s get Start Source: [`writeups/Suryesh_92/rxss-csti-in-search-field-via-polygot-payload.md`](../../writeups/Suryesh_92/rxss-csti-in-search-field-via-polygot-payload.md).
- **ikaes-strings-without-parentheses** — everyone knows [js fuck](https://github.com/aemkei/jsfuck) - the javascript trick to generate arbitrary strings and code without using any alphanumeric characters. Source: [`writeups/garethheyes/ikaes-strings-without-parentheses.md`](../../writeups/garethheyes/ikaes-strings-without-parentheses.md).
- **dompurify-bypass-smil-animatetransform-safari** — title: DOMPurify ≤3.2.6 bypass via SMIL animateTransform on Safari Source: [`writeups/kevin_mizu/dompurify-bypass-smil-animatetransform-safari.md`](../../writeups/kevin_mizu/dompurify-bypass-smil-animatetransform-safari.md).

## Payloads / requests seen in sources

- `Send two query params: ?|targetUrl=<validated> and &targetUrl=javascript:... — one extraction validates, the other reaches location.href (regex [?|&] treats | literally)` — XSS-challenge solution thread (10 parts). Source: [`posts/fransrosen/2024-08-27-1828503460183941420.md`](../../posts/fransrosen/2024-08-27-1828503460183941420.md), [`writeups/fransrosen/hackernotes-ep86-xcorrelation.md`](../../writeups/fransrosen/hackernotes-ep86-xcorrelation.md).

See also [`../payloads/xss.md`](../payloads/xss.md) when present.

## Automation (check spec)

```
# Checks derived from 13 documented finding(s) in findings.jsonl for class=xss
# try: Send two query params: ?|targetUrl=<validated> and &targetUrl=javascript:... — one extraction validates, the other reaches location.href (regex [?|&] treats | l
# note: Hunt cross-privilege stored sinks: unauth write surfaces that privileged UIs later render.
# note: Patched CVEs often leave bypasses — re-test the same sink with new encodings/contexts.
# note: Test sanitizer bypasses under non-default option combinations apps actually ship.
# note: —
# note: —
```

## Prior harness notes (retained)

_Retained from earlier curated harness file; still cites local sources._

## Detection signals
- The same URL/param is parsed twice with different logic (one path validates, another sinks to `location.href`/innerHTML).
- Sanitizer in use (DOMPurify) with browser-specific parsing quirks.
- A response header can introduce script (XSLT via Link header).

## Payloads / requests seen in sources
- Differential query-param extraction + regex char-class bug: send `?|targetUrl=<validates>` and `&targetUrl=javascript:...`; the regex `[?|&]` treats `|` literally so one extraction passes validation while the other reaches the sink. Source: [`posts/fransrosen/2024-08-27-1828503460183941420.md`](../../posts/fransrosen/2024-08-27-1828503460183941420.md).
- DOMPurify ≤3.2.6 Safari SMIL/animateTransform bypass. Source: [`writeups/kevin_mizu/dompurify-bypass-smil-animatetransform-safari.md`](../../writeups/kevin_mizu/dompurify-bypass-smil-animatetransform-safari.md).
- Firefox XSLT from a `data:` URL in a `Link` response header → XSS. Source: [`posts/garethheyes/2026-10-27-2115088588874650054.md`](../../posts/garethheyes/2026-10-27-2115088588874650054.md).
- Cloudflare `/cdn-cgi/image` XSS via caching/CSP. Source: [`posts/kevin_mizu/`](../../posts/kevin_mizu/).

## Tools
- DOM Invader / DOMLogger++ (kevin_mizu's tool), Hackvertor (garethheyes).

## Automation (check spec)
```
for param in params:
  if parsed_more_than_once(param) and extraction_differs(): FLAG differential-xss
for sink in dom_sinks: test postMessage + markup payloads
check response Link/CSP headers for script-introducing values
```

## Added 2026-11-12 — CSP form-action credential theft (garethheyes)

Even with `default-src 'none'`, if `form-action` is missing or `'self'` and there is a reflected HTML sink, a two-stage self-posting form steals credentials via Referer (`meta referrer=unsafe-url` + meta refresh to Collaborator). No JS required. Always evaluate form-action independently of default-src.
Source: writeups/garethheyes/blind-trust-stealing-credentials-through-csp.md
