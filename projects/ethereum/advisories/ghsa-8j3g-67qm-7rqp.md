# GHSA-8j3g-67qm-7rqp: snap-sync isValidRangeProof accepts a non-empty range as empty when the full subtrie is supplied as proof

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-8j3g-67qm-7rqp |
| CVE | none assigned |
| Severity | medium |
| CWE | CWE-345 |
| Published | 2026-10-07T23:14:43Z |
| Updated | 2026-10-07T23:14:43Z |
| Affected | org.hyperledger.besu:besu <= 26.8.1 (patched: 26.9.0) |
| Credits | fab-10 |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-8j3g-67qm-7rqp |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

## Summary

`WorldStateProofProvider.isValidRangeProof` has a soundness gap in its `keys.isEmpty()` branch. When a snap peer claims a requested range contains zero accounts, the check calls `trie.entriesFrom()` to detect missing trie nodes but **discards the returned entries** and returns `true` unconditionally — provided no node throws during loading. It does not verify that the range is actually empty.

A peer can therefore supply the complete, genuine proof set for a range that demonstrably contains accounts, return zero accounts, and be told the response is valid.

## Details

`ethereum/core/.../proof/WorldStateProofProvider.java` (the `keys.isEmpty()` branch):

```java
trie.entriesFrom(startKeyHash, Integer.MAX_VALUE);   // result discarded
return true;                                         // no emptiness check
```

The non-empty branch ends in a root-hash comparison. The empty branch has no equivalent.

**Precondition.** The attacker must be a snap peer the syncing node connects to, and must supply every in-range trie node as proof — cost scales with subtrie size, so wide ranges become impractical.

**Impact on the default snap/1 path.** `StorageRangeDataRequest` gates on `isValidRangeProof`. Accepting a false "empty range" means the node skips downloading those accounts. A final world-state root check against the beacon chain's trusted head would catch a resulting state mismatch, so the likely concrete effect is sync disruption/stall rather than persisted state corruption. The full consequence chain has not been independently verified.

**snap/2 path (non-default, `--Xsnap2-enabled`).** `SnapV2PersistDataStep` throws `IllegalStateException` on an empty account response, which is a separate but related symptom.

## Fix

Capture the result of `entriesFrom` and reject if non-empty:

```java
final var found = trie.entriesFrom(startKeyHash, Integer.MAX_VALUE);
if (!found.isEmpty()) { return false; }
```

The fix preserves the legitimate empty-range case (a range that genuinely contains no accounts must still be accepted).

## Patches and references

Fixed in Besu 26.9.0.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/e4d39ad64cc4
- Pull request: https://github.com/besu-eth/besu/pull/11378
