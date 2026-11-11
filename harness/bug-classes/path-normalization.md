# Path normalization / traversal for authz

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/` and `writeups/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


## Detection signals
- Auth/gate matches the raw path; the router normalises afterwards.

## Payloads seen in sources
- `/./`, `//`, trailing dots, `%2e` on any 403/login-gated path. `/admin/./` → bypass. Source: [`posts/mdp_sec/2026-11-11-2120338219841544604.md`](../../posts/mdp_sec/2026-11-11-2120338219841544604.md). Also `path-bypass` Stage-B class in Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md).
- Path traversal / LFI is its own Stage-B class (not demoted). Source: Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md) (`lfi`).

## Automation (check spec)
```
for p in gated_paths:
  for variant in dot_segment_and_encoding_variants(p):
    if status(variant)==200 and status(p) in (401,403,302): FLAG path-authz-bypass
```

