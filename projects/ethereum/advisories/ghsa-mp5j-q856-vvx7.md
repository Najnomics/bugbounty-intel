# GHSA-mp5j-q856-vvx7: Malformed peer receipts poison Besu's synced receipt store and break historical transaction/event queries

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-mp5j-q856-vvx7 |
| CVE | none assigned |
| Severity | medium |
| CWE | n/a |
| Published | 2026-11-18T05:22:33Z |
| Updated | 2026-11-18T05:22:33Z |
| Affected | org.hyperledger.besu:besu <= 26.10.2 (patched: 26.11.0) |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-mp5j-q856-vvx7 |

## Description (verbatim)

### Summary
When Besu downloads receipts from a peer during sync, it checks them against the block header's receipts root. For a compacted receipt (eth/69, or a receipt sent without its bloom), the root is computed over a re-encoding of the fields Besu parses, but Besu stored the original bytes the peer sent. The eth/69 and compacted legacy decoders did not close the receipt list, and the compacted typed decoder did not check for bytes after it, so data appended to a receipt was not covered by the root check and still reached storage.

### Impact
A malicious peer serving receipts to a syncing Besu node can make that node's receipts for the affected blocks unreadable. Besu's storage decoder rejects the extra data, so `eth_getTransactionReceipt`, `eth_getBlockReceipts` and `eth_getLogs` fail for those blocks. The damage persists across restarts.

A single extra field on a compacted legacy receipt is read by the storage decoder as a revert reason, so the node serves a peer-chosen revert reason over RPC.

Block hashes, state and consensus are not affected. Only the node that downloaded the receipts from the malicious peer is affected.

### Affected configurations
Nodes that download historical receipts from peers, for example during snap or checkpoint sync.

### Patches
Besu now rejects a compacted receipt with trailing data as malformed, and stores a compacted receipt as an encoding of the same fields the receipts root is computed over, rather than the bytes the peer sent.

### Workarounds
None. A node whose receipts were affected can recover them by resyncing.

## Patches and references

Fixed in Besu 26.11.0.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/d266aa87139fe226b17fe9f579e2b19e2ca1ed59
- Release: https://github.com/besu-eth/besu/releases/tag/26.11.0

