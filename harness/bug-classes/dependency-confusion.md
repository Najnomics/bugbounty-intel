# Dependency Confusion

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **3** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- Claim-check every internal package name you find; report with a benign callback-only PoC per program rules. (from mdp_sec). Source: [`posts/mdp_sec/2026-11-06-2118803107119325691.md`](../../posts/mdp_sec/2026-11-06-2118803107119325691.md), [`writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`](../../writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md), [`writeups/mdp_sec/mdpsec-home.md`](../../writeups/mdp_sec/mdpsec-home.md).
- Dynamic 'always fetch latest' loaders turn a package compromise into instant mass client compromise. (from Neodyme). Source: [`posts/Neodyme/ARCHIVE.md`](../../posts/Neodyme/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- — (from ryotkak). Source: [`posts/ryotkak/2026-06-01-2061434879309664575.md`](../../posts/ryotkak/2026-06-01-2061434879309664575.md).

## Method / findings in sources

- **$1,200 Bugcrowd dependency confusion** — An internal package name used by the target was unclaimed on the public registry, so a public package with that name could be pulled by builds. Source: [`posts/mdp_sec/2026-11-06-2118803107119325691.md`](../../posts/mdp_sec/2026-11-06-2118803107119325691.md), [`writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`](../../writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md), [`writeups/mdp_sec/mdpsec-home.md`](../../writeups/mdp_sec/mdpsec-home.md).
- **Ledger Connect Kit npm supply-chain attack — wallet-drainer in 1.1.6/1.1.7** — Malicious JS inserted into connect-kit npm 1.1.6/1.1.7. connect-kit-loader dynamically fetched latest from NPM, so dApps that load it executed the drainer. Drained EVM tokens across wallets; Solana unaffected. Config fetched encrypted from Infura; researcher pubkeys excluded. Source: [`posts/Neodyme/ARCHIVE.md`](../../posts/Neodyme/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **Claude Code supply-chain attack** — See linked article. Source: [`posts/ryotkak/2026-06-01-2061434879309664575.md`](../../posts/ryotkak/2026-06-01-2061434879309664575.md).

## Payloads / requests seen in sources

- `Harvest internal package names from JS bundles/manifests; publish/claim a benign package of the same name on the public registry; confirm resolution with a callback-only PoC` — $1,200 Bugcrowd dependency confusion. Source: [`posts/mdp_sec/2026-11-06-2118803107119325691.md`](../../posts/mdp_sec/2026-11-06-2118803107119325691.md), [`writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md`](../../writeups/mdp_sec/bug-bounty-hunting-prompts-readme.md), [`writeups/mdp_sec/mdpsec-home.md`](../../writeups/mdp_sec/mdpsec-home.md).

See also [`../payloads/dependency-confusion.md`](../payloads/dependency-confusion.md) when present.

## Automation (check spec)

```
# Checks derived from 3 documented finding(s) in findings.jsonl for class=dependency-confusion
# try: Harvest internal package names from JS bundles/manifests; publish/claim a benign package of the same name on the public registry; confirm resolution with a call
# note: Dynamic 'always fetch latest' loaders turn a package compromise into instant mass client compromise.
# note: —
```

## Prior harness notes (retained)

_Retained from earlier curated harness file; still cites local sources._

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
