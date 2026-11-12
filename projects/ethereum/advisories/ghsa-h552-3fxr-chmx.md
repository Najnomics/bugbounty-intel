# GHSA-h552-3fxr-chmx: Snap-sync storage-range count amplification: a tiny returned slot hash yields an unbounded child-range count, leading to OOM or sync-worker crash

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-h552-3fxr-chmx |
| CVE | none assigned |
| Severity | low |
| CWE | n/a |
| Published | 2026-10-02T03:50:57Z |
| Updated | 2026-10-02T03:50:57Z |
| Affected | org.hyperledger.besu:besu <= 26.8.0 (patched: 26.8.1) |
| Credits | n/a |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-h552-3fxr-chmx |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

During snap synchronization, when a peer returns a partial storage range, Besu decides how many child sub-ranges to request from the boundary of the returned data, and that count is neither clamped nor safely narrowed before it is used to eagerly allocate. RangeManager.getRangeCount computes MAX_RANGE / (lastReturnedKey - min) as a BigInteger with no upper clamp, then narrows it with BigInteger.intValue() (a low-32-bit, signed truncation). RangeManager.generateRanges then eagerly materializes that many range entries into a TreeMap. If the largest returned storage-slot hash is very small (many leading zero bits), the divisor is tiny and the count is astronomically large, with two failure modes: a huge positive int drives generateRanges to allocate ~count TreeMap entries, causing an OutOfMemoryError; or an intValue() negative/zero wrap produces an out-of-range BigInteger that RangeManager.format rejects, throwing an IllegalArgumentException that propagates out of the sync worker. Both outcomes are a denial of service against a node performing snap sync. Exploitation is conditional: the attacker must preposition a contract with genuinely tiny-hash storage slots in the chain the victim snap-syncs, then serve a valid, truncated storage-range response whose returned slot has a tiny hash. This is CertiK finding HYB-10 (Informational — CertiK notes the eager-materialization impact would be higher if fully unconditional, but rates the finding Informational given the proof-of-concept's conditional exploitation path). Not yet fixed as of Besu 26.7.1.

## Patches and references

Fixed in Besu 26.8.1.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/c3a15f960c94
- Pull request: https://github.com/besu-eth/besu/pull/11094
