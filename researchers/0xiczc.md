# @0xiczc

Compiled 11 Nov 2026 (WAT). Full verbatim post text lives under [`posts/0xiczc/`](../posts/0xiczc/); full writeups under [`writeups/0xiczc/`](../writeups/0xiczc/).

| Field | Value |
| --- | --- |
| X | [@0xiczc](https://x.com/0xiczc) (user id 800988245366435840, joined 2016-11-22) |
| Name (profile) | iczc |
| Followers (11 Nov 2026) | 784 |
| Bio (verbatim) |  |
| Specialty | Web3 / ZK / Cosmos |
| Platforms | Immunefi |
| Evidence of valid finds | Polygon zkEVM bug; Evmos mint bug. |

## Key findings and analysis

### Polygon zkEVM: reverted non-free claim txs mark deposit counts and block L1→L2 claims (Immunefi)

- Post: https://x.com/0xiczc/status/1662090451493740545 — verbatim: [`posts/0xiczc/2023-05-26-1662090451493740545.md`](../posts/0xiczc/2023-05-26-1662090451493740545.md)
- **Bug class:** L2 node / bridge logic (DoS, asset-migration blocking)
- **Root cause:** Claim txs were free (gas price 0) and pre-executed before entering the pool; only free+reverted claims were rejected. A claim with non-zero gas that reverted fell into the else-branch, was added to the pool and marked its deposit count as used — so attackers could DoS sequencer/prover cheaply and pre-burn any deposit count so the legitimate claim was rejected.
- **How it was found:** Reading the node's special-case handling of claim-tx pre-execution results and enumerating every branch (free/non-free × revert/non-revert).
- **Takeaways:** Special-case fee logic in rollup nodes is fertile ground; enumerate all branch combinations. Fixed by removing the special gas logic; Immunefi added a new impact category after the report.

## All captured posts (verbatim files)

- 2023-05-26 — 1/ Recently, I discovered a vulnerability in the  @0xPolygon zkEVM and earned my first L2 bug bounty from @Imm — [`posts/0xiczc/2023-05-26-1662090451493740545.md`](../posts/0xiczc/2023-05-26-1662090451493740545.md) · https://x.com/0xiczc/status/1662090451493740545
- 2025-10-04 — Thanks @CertiK for the great write-up on the vulnerability I found in Cosmos EVM-compatible chains👀 — [`posts/0xiczc/2025-10-04-1974521372597723619.md`](../posts/0xiczc/2025-10-04-1974521372597723619.md) · https://x.com/0xiczc/status/1974521372597723619
- 2023-02-14 — I'm delighted to have participated in the Audit Contest on  @secure3io! And thanks for the bounty :) — [`posts/0xiczc/2023-02-14-1625325970269048832.md`](../posts/0xiczc/2023-02-14-1625325970269048832.md) · https://x.com/0xiczc/status/1625325970269048832
- 2024-10-29 — Is it true? A few months ago, I discovered a vulnerability on Evmos that allowed arbitrary token minting, but  — [`posts/0xiczc/2024-10-29-1851281615592579445.md`](../posts/0xiczc/2024-10-29-1851281615592579445.md) · https://x.com/0xiczc/status/1851281615592579445
- 2024-01-28 — Added exploit scripts for this challenge — [`posts/0xiczc/2024-01-28-1751634293951222209.md`](../posts/0xiczc/2024-01-28-1751634293951222209.md) · https://x.com/0xiczc/status/1751634293951222209

## Writeups saved (full text)

- [`writeups/0xiczc/certik-evm-cosmos-convergence-part-2.md`](../writeups/0xiczc/certik-evm-cosmos-convergence-part-2.md)
- [`writeups/0xiczc/evmos-advisory-GHSA-3fp5-2xwh-fxm6.md`](../writeups/0xiczc/evmos-advisory-GHSA-3fp5-2xwh-fxm6.md)
- [`writeups/0xiczc/polygon-zkevm-node-pr-2048.md`](../writeups/0xiczc/polygon-zkevm-node-pr-2048.md)
