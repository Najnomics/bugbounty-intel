# Dependency confusion / supply chain

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/` and `writeups/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


## Detection signals
- Internal package names referenced in JS bundles, lockfiles, manifests, or build errors that are unclaimed on the public registry.

## Method seen in sources
- Harvest internal package names, check the public registry, claim a benign package of the same name, confirm with a callback-only PoC ($1,200). Source: [`posts/mdp_sec/2026-11-06-2118803107119325691.md`](../../posts/mdp_sec/2026-11-06-2118803107119325691.md).
- Supply-chain also appears via CI (ryotkak Claude Code GitHub Actions). Source: [`posts/ryotkak/`](../../posts/ryotkak/).

## Tools
- Bundle/source-map extractors, registry lookup scripts.

## Automation (check spec)
```
names = extract_pkg_names(js_bundles+manifests+error_bodies)
for n in names:
  if not public_registry_has(n): FLAG dependency-confusion(n)  # claim benign, callback-only PoC per rules
```

