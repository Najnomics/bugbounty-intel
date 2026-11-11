# Governance / voting / timelock

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **1** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- Governance vote-accounting is security-critical; check who can overwrite or reset another party's vote record. (from asymmetric_re). Source: [`posts/asymmetric_re/2026-10-19-2112236410455597403.md`](../../posts/asymmetric_re/2026-10-19-2112236410455597403.md).

## Method / findings in sources

- **Solana governance: any validator could silently erase its delegators' dissenting votes** — For its first 6 weeks on mainnet the governance program let a validator erase delegators' dissenting votes; without the fix SGP-0002 would have failed by 0.02 percentage points (per post). Source: [`posts/asymmetric_re/2026-10-19-2112236410455597403.md`](../../posts/asymmetric_re/2026-10-19-2112236410455597403.md).

## Automation (check spec)

```
# Checks derived from 1 documented finding(s) in findings.jsonl for class=governance
# note: Governance vote-accounting is security-critical; check who can overwrite or reset another party's vote record.
```
