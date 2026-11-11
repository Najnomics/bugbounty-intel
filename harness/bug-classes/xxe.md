# XXE (XML External Entity)

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **1** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- Pre-auth XXE on ecommerce platforms remains high-impact; keep XXE probes in Magento scope. (from infosec_au). Source: [`posts/infosec_au/ARCHIVE.md`](../../posts/infosec_au/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Method / findings in sources

- **Magento pre-auth XXE (CVE-2024-34102) reproduced** — Pre-authentication XXE in Magento originally found by Sergey Temnikov; Assetnote (infosec_au / hash_kitten) reproduced and published research. Source: [`posts/infosec_au/ARCHIVE.md`](../../posts/infosec_au/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).

## Automation (check spec)

```
# Checks derived from 1 documented finding(s) in findings.jsonl for class=xxe
# note: Pre-auth XXE on ecommerce platforms remains high-impact; keep XXE probes in Magento scope.
```
