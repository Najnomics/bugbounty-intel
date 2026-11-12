# GHSA-hhgq-3gvc-4jhp: QBFT RoundChange executes the piggybacked block before the free hash check, letting a non-validator replay one captured signature with substituted blocks

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-hhgq-3gvc-4jhp |
| CVE | none assigned |
| Severity | medium |
| CWE | n/a |
| Published | 2026-11-10T04:40:09Z |
| Updated | 2026-11-10T04:40:09Z |
| Affected | org.hyperledger.besu:besu <= 26.10.1 (patched: 26.10.2) |
| Credits | fab-10, jflo |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-hhgq-3gvc-4jhp |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

### Impact

QBFT `RoundChange` handling validates the piggybacked block - a full state transition over every transaction in it - before performing the prepared-block-hash comparison that would have rejected the message, and does so twice per accepted message.

The proposed block rides **outside** the payload signature: `RoundChange` encodes it as a separate wire item alongside the signed payload. `MessageTracker` de-duplicates on raw message bytes, so every substituted block is a fresh message. Consequently an attacker who captures a single genuine validator-signed `RoundChange` carrying a prepared block can replay it with arbitrary blocks substituted, buying a full block execution on the single BFT consensus thread per replay. **No validator key is required**, and delivery needs only a devp2p peer speaking `istanbul/100`.

Two further ordering defects compound it: the message was validated once for a diagnostic before the early return that discards messages for already-passed rounds, and again when appended, with no memoisation between them.

This is an availability issue affecting QBFT networks. There is no consensus-split or safety claim. IBFT does not share the second ordering defect.

### Patches

The prepared-metadata and prepared-block-hash checks now run before block validation; the message-age check runs before the diagnostic; and the message is validated once rather than twice.

### Workarounds

None. Restricting peering to trusted nodes reduces exposure.

## Patches and references

Fixed in Besu 26.10.2.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/0758badf6673e5bc649303c95783141f83d46dc9
- Release: https://github.com/besu-eth/besu/releases/tag/26.10.2

