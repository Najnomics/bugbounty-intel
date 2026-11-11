# Cross-chain bridges / message passing

_Harness check spec. Every signal, payload and automation note below is drawn from the cited local files (full verbatim text under `posts/`, `writeups/`, `projects/`). Nothing here is invented; where a source only states a pattern, no concrete payload is asserted._


_Findings in corpus for this class: **7** (see `harness/findings.jsonl`)._

## Detection signals / takeaways from sources

- Special-case fee logic in rollup nodes is fertile ground; enumerate all branch combinations. Fixed by removing the special gas logic; Immunefi added a new impact category after the report. (from 0xiczc). Source: [`posts/0xiczc/2023-05-26-1662090451493740545.md`](../../posts/0xiczc/2023-05-26-1662090451493740545.md), [`writeups/0xiczc/certik-evm-cosmos-convergence-part-2.md`](../../writeups/0xiczc/certik-evm-cosmos-convergence-part-2.md), [`writeups/0xiczc/evmos-advisory-GHSA-3fp5-2xwh-fxm6.md`](../../writeups/0xiczc/evmos-advisory-GHSA-3fp5-2xwh-fxm6.md).
- Cross-chain allowlists that can be self-populated via 'legit' side effects are authorization bypasses. (from ChainLight_io). Source: [`posts/ChainLight_io/ARCHIVE.md`](../../posts/ChainLight_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Bridge halt/DoS is often in-scope critical even without direct theft. (from farazsth98). Source: [`posts/farazsth98/ARCHIVE.md`](../../posts/farazsth98/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- L1→L2 deposit inboxes are direct theft surfaces — verify finalization and refund paths. (from 0xriptide). Source: [`posts/0xriptide/ARCHIVE.md`](../../posts/0xriptide/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- Audit operational config (verifier sets, thresholds), not only code. (from trust__90). Source: [`posts/trust__90/2026-04-20-2046203827305484565.md`](../../posts/trust__90/2026-04-20-2046203827305484565.md).
- — (from PwningEth). Source: [`posts/PwningEth/2022-09-04-1566381803405209601.md`](../../posts/PwningEth/2022-09-04-1566381803405209601.md), [`writeups/PwningEth/frontier-evm-wrapped-token-insolvency.md`](../../writeups/PwningEth/frontier-evm-wrapped-token-insolvency.md).

## Method / findings in sources

- **Polygon zkEVM: reverted non-free claim txs mark deposit counts and block L1→L2 claims (Immunefi)** — Claim txs were free (gas price 0) and pre-executed before entering the pool; only free+reverted claims were rejected. A claim with non-zero gas that reverted fell into the else-branch, was added to the pool and marked its deposit count as used — so attackers could DoS sequencer/prover cheaply and pre-burn any deposit count so the legitimate claim w Source: [`posts/0xiczc/2023-05-26-1662090451493740545.md`](../../posts/0xiczc/2023-05-26-1662090451493740545.md), [`writeups/0xiczc/certik-evm-cosmos-convergence-part-2.md`](../../writeups/0xiczc/certik-evm-cosmos-convergence-part-2.md), [`writeups/0xiczc/evmos-advisory-GHSA-3fp5-2xwh-fxm6.md`](../../writeups/0xiczc/evmos-advisory-GHSA-3fp5-2xwh-fxm6.md).
- **FEG $1M — Wormhole cross-chain message logic bug, allowlist self-registration** — Logic bug handling cross-chain messages via Wormhole. Exploiter could register himself in allowlist via a legit transaction that transfers ETH to admin address, then bypass address verification on the next tx. Source: [`posts/ChainLight_io/ARCHIVE.md`](../../posts/ChainLight_io/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **Cronos Gravity Bridge — two bugs that halt all or parts of the bridge** — Two bugs reported Jan 2023 to Cronos Gravity Bridge Immunefi project allowing an attacker to halt all or parts of the bridge. Belated writeup published. Source: [`posts/farazsth98/ARCHIVE.md`](../../posts/farazsth98/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **Arbitrum Nitro — steal all incoming ETH deposits on L1→L2 bridge (Critical)** — Critical vulnerability allowing an attacker to steal all incoming ETH deposits to the L1→L2 bridge. Medium writeup by 0xriptide. Source: [`posts/0xriptide/ARCHIVE.md`](../../posts/0xriptide/ARCHIVE.md), [`data/x_posts.jsonl`](../../data/x_posts.jsonl).
- **KelpDAO 1/1 DVN incident analysis** — Single-verifier (1/1 DVN) configuration let one compromised verifier approve messages. Source: [`posts/trust__90/2026-04-20-2046203827305484565.md`](../../posts/trust__90/2026-04-20-2046203827305484565.md).
- **Aurora bridge protected again** — See thread. Source: [`posts/PwningEth/2022-09-04-1566381803405209601.md`](../../posts/PwningEth/2022-09-04-1566381803405209601.md), [`writeups/PwningEth/frontier-evm-wrapped-token-insolvency.md`](../../writeups/PwningEth/frontier-evm-wrapped-token-insolvency.md).
- **Hackers in Arbitrum’s Inbox** — This is the story of wiped storage slots and well-intentioned gas optimizations that led to a multi-million dollar vulnerability affecting any would-be depositor attempting to bridge funds from Ethereum to Arbitrum Nitro. Read further anon to discover the mystery of the vulnerable inbox contract … Source: [`writeups/0xriptide/hackers-in-arbitrums-inbox.md`](../../writeups/0xriptide/hackers-in-arbitrums-inbox.md).

## Payloads / requests seen in sources

- `Submit a non-free (gas>0) claim tx that reverts: it falls into the else branch, is pooled and marks its deposit count used, blocking the legitimate L1->L2 claim and DoSing the sequencer` — Polygon zkEVM: reverted non-free claim txs mark deposit counts and block L1→L2 claims (Immunefi). Source: [`posts/0xiczc/2023-05-26-1662090451493740545.md`](../../posts/0xiczc/2023-05-26-1662090451493740545.md), [`writeups/0xiczc/certik-evm-cosmos-convergence-part-2.md`](../../writeups/0xiczc/certik-evm-cosmos-convergence-part-2.md), [`writeups/0xiczc/evmos-advisory-GHSA-3fp5-2xwh-fxm6.md`](../../writeups/0xiczc/evmos-advisory-GHSA-3fp5-2xwh-fxm6.md).

See also [`../payloads/cross-chain-bridge.md`](../payloads/cross-chain-bridge.md) when present.

## Automation (check spec)

```
# Checks derived from 7 documented finding(s) in findings.jsonl for class=cross-chain-bridge
# try: Submit a non-free (gas>0) claim tx that reverts: it falls into the else branch, is pooled and marks its deposit count used, blocking the legitimate L1->L2 claim
# note: Cross-chain allowlists that can be self-populated via 'legit' side effects are authorization bypasses.
# note: Bridge halt/DoS is often in-scope critical even without direct theft.
# note: L1→L2 deposit inboxes are direct theft surfaces — verify finalization and refund paths.
# note: Audit operational config (verifier sets, thresholds), not only code.
# note: —
```
