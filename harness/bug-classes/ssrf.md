# SSRF and server-side execution

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/` and `writeups/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


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

