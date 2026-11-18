# GHSA-pvgm-f647-f7vc: Uncaught NullPointerException in IBFT 2.0/QBFT commit seal validation via crafted commit seal

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-pvgm-f647-f7vc |
| CVE | none assigned |
| Severity | low |
| CWE | CWE-476 |
| Published | 2026-11-18T05:21:38Z |
| Updated | 2026-11-18T05:21:38Z |
| Affected | org.hyperledger.besu:besu <= 26.10.2 (patched: 26.11.0) |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-pvgm-f647-f7vc |

## Description (verbatim)

### Summary
IBFT 2.0 and QBFT header validation recovers an address from each commit seal in the block header and checks the committers against the validator set. Recovery returns `null` when a seal's signature does not recover to a public key, and a crafted seal can produce this without any key. The committers list was not checked for `null`, and with block-header validator selection the validator set is a natural-ordering `TreeSet`, which throws `NullPointerException` on `contains(null)`.

### Impact
The exception is thrown while validating a block header downloaded from a peer during sync. The sync pipeline catches it, so the node does not crash.

Because the failure is an exception rather than an invalid-block result, the peer that served the header is not disconnected for a protocol breach. The node logs an error and restarts the download after a short pause. A header with crafted commit seals keeps the block hash of the genuine header, since the hash does not cover the commit seals, so a malicious peer can keep serving it. While that peer remains the node's sync target, the node can be held back from syncing.

Consensus at the chain head is not affected: a proposed block carries no commit seals, and each commit seal a validator collects is checked against the author of its Commit message. There is no persistent damage, no chain fork and no fund impact.

No validator key is required.

### Affected configurations
- IBFT 2.0 networks.
- QBFT networks using block-header validator selection.

### Patches
Header validation now rejects a block when any commit seal does not recover to an address, before the committers are checked against the validator set.

### Workarounds
None. Restricting which peers may connect to validators (for example with node permissioning) reduces exposure.

## Patches and references

Fixed in Besu 26.11.0.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/7af5074735b3290992f5f7fa0ed8bba66b93058e
- Release: https://github.com/besu-eth/besu/releases/tag/26.11.0

