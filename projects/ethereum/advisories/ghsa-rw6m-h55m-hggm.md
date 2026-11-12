# GHSA-rw6m-h55m-hggm: Besu's transaction pool has no per-transaction encoded-size cap, causing peer clients to penalize or disconnect nodes that relay oversized transactions

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-rw6m-h55m-hggm |
| CVE | none assigned |
| Severity | medium |
| CWE | n/a |
| Published | 2026-10-02T02:37:04Z |
| Updated | 2026-10-02T02:37:04Z |
| Affected | org.hyperledger.besu:besu <= 26.8.0 (patched: 26.8.1) |
| Credits | lgprbs |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-rw6m-h55m-hggm |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

Besu's transaction-pool admission path enforces no maximum RLP-encoded size for a pooled
transaction, while geth, reth, erigon, and nethermind all reject transactions above a
128 KiB encoded-size cap at admission. A transaction can be crafted with a large
`calldata` payload that stays under Besu's gas-limit, EIP-7623, and EIP-7825 checks but
exceeds 128 KiB once RLP-encoded. Besu's `MainnetTransactionValidator` accepts such a
transaction into its pool and gossips it to peers.

Reth and erigon both treat receipt of an oversized transaction as a protocol violation by
the relaying peer. Reth records a bad-import strike per delivery and bans the relaying
peer for 12 hours once its reputation threshold is crossed; erigon disconnects the
relaying peer on first delivery and re-kicks it on reconnection while the oversized
transaction keeps circulating through the network. A remote, unauthenticated party can
inject a handful of oversized-but-otherwise-valid transactions into any Besu node's RPC
or p2p interface and cause that node to lose connectivity to all of its reth and erigon
peers, degrading its view of the network and its ability to promptly receive blocks and
transactions from those clients.

## Patches and references

Fixed in Besu 26.8.1.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/21f794ca848b7cfa1a8efab709a29e07e96ce264
- Pull request: https://github.com/besu-eth/besu/pull/11214
