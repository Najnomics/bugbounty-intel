# File upload / zip-slip / polyglot / ImageMagick

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **2** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- Image processing pipelines are race-prone; polyglots can bridge parser boundaries. (from kevin_mizu). Source: [`posts/kevin_mizu/2026-10-07-2107783292091007306.md`](../../posts/kevin_mizu/2026-10-07-2107783292091007306.md).
- Ecommerce pre-auth upload→RCE chains are mass-scanned; prioritize Magento upload sinks. (from infosec_au). Source: [`posts/infosec_au/ARCHIVE.md`](../../posts/infosec_au/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Method / findings in sources

- **Discourse: ImageMagick JPEG race + polyglot → arbitrary file read/RCE (CVE-2026-55420); also cache-poisoning XSS (CVE-20** — ImageMagick race condition combined with a polyglot payload allowed file read/RCE on Discourse. Separately, pre-auth cache poisoning to sitewide XSS. Credited to kevin_mizu / SLCyberSec research team; HacktronAI also referenced. Source: [`posts/kevin_mizu/2026-10-07-2107783292091007306.md`](../../posts/kevin_mizu/2026-10-07-2107783292091007306.md).
- **Magento PolyShell pre-auth file upload → RCE (APSB25-94), exploited in the wild** — Pre-auth unauthenticated file upload to RCE in Magento (PolyShell). Reverse-engineered by SLCyberSec; actively exploited; flagged first by sansecio. Source: [`posts/infosec_au/ARCHIVE.md`](../../posts/infosec_au/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Payloads / requests seen in sources

- `Polyglot payload + ImageMagick race (details in linked research article)` — Discourse: ImageMagick JPEG race + polyglot → arbitrary file read/RCE (CVE-2026-55420); also cache-poisoning XSS (CVE-20. Source: [`posts/kevin_mizu/2026-10-07-2107783292091007306.md`](../../posts/kevin_mizu/2026-10-07-2107783292091007306.md).

See also [`../payloads/file-upload.md`](../payloads/file-upload.md) when present.

## Automation (check spec)

```
# Checks derived from 2 documented finding(s) in findings.jsonl for class=file-upload
# try: Polyglot payload + ImageMagick race (details in linked research article)
# note: Ecommerce pre-auth upload→RCE chains are mass-scanned; prioritize Magento upload sinks.
```
