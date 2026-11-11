# XSS (reflected, stored, DOM, mutation)

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/` and `writeups/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


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

