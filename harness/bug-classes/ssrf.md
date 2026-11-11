# Ssrf

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **3** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- localtest.me and method-switching are still basic but effective filter/CSRF bypasses. (from zseano). Source: [`posts/zseano/ARCHIVE.md`](../../posts/zseano/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- HTML-to-PDF is a recurring SSRF/LFI/deser trust boundary; old embedded Chromium = RCE. (from Neodyme). Source: [`posts/Neodyme/ARCHIVE.md`](../../posts/Neodyme/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Framework-level SSRF in Next.js affects many deployments — check Server Actions / rewrite/proxy helpers. (from infosec_au). Source: [`posts/infosec_au/ARCHIVE.md`](../../posts/infosec_au/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Method / findings in sources

- **SSRF via localtest.me; open-redirect filter bypasses; CSRF token bypass by switching to GET** — SSRF filters blocked juicy reads but http://localtest.me worked. Open URL filters bypassed with /%255C → /\ and /%0d/. CSRF token enforced on POST but changing method to GET bypassed. Source: [`posts/zseano/ARCHIVE.md`](../../posts/zseano/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **HTML-to-PDF API file read + SSRF chained to RCE via Chromium 62 WebView** — HTML-to-PDF API allowed file reads and SSRF; chained into RCE via a Chromium 62 WebView exploit. Full writeup at neodyme.io. Source: [`posts/Neodyme/ARCHIVE.md`](../../posts/Neodyme/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **Next.js full-read SSRF (CVE-2024-34351)** — Full-read SSRF in Next.js discovered by infosec_au and hash_kitten (Assetnote); disclosed with Vercel. Source: [`posts/infosec_au/ARCHIVE.md`](../../posts/infosec_au/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Payloads / requests seen in sources

- `SSRF: http://localtest.me ; open URL: /%255C and /%0d/ ; CSRF: change POST→GET to drop token requirement` — SSRF via localtest.me; open-redirect filter bypasses; CSRF token bypass by switching to GET. Source: [`posts/zseano/ARCHIVE.md`](../../posts/zseano/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

See also [`../payloads/ssrf.md`](../payloads/ssrf.md) when present.

## Automation (check spec)

```
# Checks derived from 3 documented finding(s) in findings.jsonl for class=ssrf
# try: SSRF: http://localtest.me ; open URL: /%255C and /%0d/ ; CSRF: change POST→GET to drop token requirement
# note: HTML-to-PDF is a recurring SSRF/LFI/deser trust boundary; old embedded Chromium = RCE.
# note: Framework-level SSRF in Next.js affects many deployments — check Server Actions / rewrite/proxy helpers.
```

## Prior harness notes (retained)

_Retained from earlier curated harness file; still cites local sources._

## Detection signals
- Any URL / webhook / integration / image-fetch field that the server dereferences.
- Upload pipelines that process files server-side (thumbnailer, AV, ffmpeg, pandoc, ImageMagick).

## Recon steps
- Catalog every URL-accepting field and webhook/integration (Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md), class `ssrf`, Stage B, all modes).
- Flag upload surfaces for server-side processing (`upload`).

## Method / requests seen in sources
- Point URL fields at an OOB listener and cloud metadata (169.254.169.254) — bounded, non-destructive (Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md) testing policy + OOB listener).
- ImageMagick-driven arbitrary file read was a confirmed critical in his workflow (Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md) notes SSTI/ImageMagick are NOT demoted). Related: kevin_mizu ImageMagick→Discourse RCE, [`writeups/kevin_mizu/`](../../writeups/kevin_mizu/).

## Tools
- OOB/collaborator listener, polyglot upload files, `ffmpeg`/`ImageMagick` test payloads.

## Automation (check spec)
```
for field in url_fields+webhooks:
  if fetches(field, oob_url()): FLAG ssrf
  try(field, 'http://169.254.169.254/latest/meta-data/')
for up in upload_endpoints:
  submit(crafted_image_triggering_processor); watch oob + response
```
