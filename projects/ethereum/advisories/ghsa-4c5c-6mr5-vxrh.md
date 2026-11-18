# GHSA-4c5c-6mr5-vxrh: Uncaught NullPointerException in Clique header validation via crafted proposer seal

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-4c5c-6mr5-vxrh |
| CVE | none assigned |
| Severity | low |
| CWE | CWE-476 |
| Published | 2026-11-18T05:22:05Z |
| Updated | 2026-11-18T05:22:05Z |
| Affected | org.hyperledger.besu:besu <= 26.10.2 (patched: 26.11.0) |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-4c5c-6mr5-vxrh |

## Description (verbatim)

### Summary
Clique header validation recovers the block proposer's address from the proposer seal in the header's extra data. Recovery returns `null` when the seal's signature does not recover to a public key, and a crafted seal can produce this without any key. The null proposer was then checked against the validator set with `contains`, and the validator set is a natural-ordering `TreeSet`, which throws `NullPointerException` on `contains(null)`.

### Impact
The exception is thrown while validating a block header received from a peer, either through block propagation or header download during sync. Both paths run validation in an asynchronous task, so the exception fails that task rather than crashing the node.

During sync, because the failure is an exception rather than an invalid-block result, the peer that served the header is not disconnected for a protocol breach. The node logs an error and restarts the download after a short pause, so while a malicious peer remains the node's sync target, the node can be held back from syncing.

There is no persistent damage, no chain fork and no fund impact.

No validator key is required.

### Affected configurations
Clique networks.

### Patches
Recovering the proposer from a seal that does not recover to an address now fails with `IllegalArgumentException`, as it already did for a missing seal. Header validation catches this and rejects the block.

### Workarounds
None. Restricting which peers may connect (for example with node permissioning) reduces exposure.

## Patches and references

Fixed in Besu 26.11.0.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/5d207f8127251fed58065320b81f9e1ce5d110d7
- Release: https://github.com/besu-eth/besu/releases/tag/26.11.0

