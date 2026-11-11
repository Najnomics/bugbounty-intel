# Web cache poisoning and cache deception

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/` and `writeups/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


## Detection signals
- Unkeyed inputs (headers, params) influence a cached response; or sensitive pages get cached under attacker-reachable keys.

## Method seen in sources
- Cache deception and cache poisoning are a Stage-B sweep across all modes. Source: Marius du Preez's sweep class matrix: [`writeups/mdp_sec/prompts/phases/phase-02-sweep.md`](../../writeups/mdp_sec/prompts/phases/phase-02-sweep.md) (class `cache`).
- Cloudflare `/cdn-cgi/image` XSS used a Cache-Control/CSP interaction. Source: [`posts/kevin_mizu/`](../../posts/kevin_mizu/).

## Tools
- Burp Param Miner (unkeyed input detection).

## Automation (check spec)
```
for page in cacheable_pages:
  for inj in [header_variants, param_variants]:
    if response_reflects(inj) and gets_cached(): FLAG cache-poisoning
  if sensitive(page) and cacheable_by_attacker_key(page): FLAG cache-deception
```

