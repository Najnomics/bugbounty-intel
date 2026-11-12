# GHSA-pcv4-pxhv-99m7: Besu nodes with the snap server enabled schedule an unbounded native thread per inbound snap/1 GET request, letting a single peer exhaust thread capacity

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-pcv4-pxhv-99m7 |
| CVE | none assigned |
| Severity | medium |
| CWE | n/a |
| Published | 2026-10-02T02:21:56Z |
| Updated | 2026-10-02T02:21:56Z |
| Affected | org.hyperledger.besu:besu <= 26.7.1 (patched: 26.8.0) |
| Credits | CertiK4Audit |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-pcv4-pxhv-99m7 |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

A Besu node with the snap server enabled (--snapsync-server-enabled=true) schedules an independent service task — and thus a native thread — for every inbound snap/1 GET request (GET_ACCOUNT_RANGE, GET_STORAGE_RANGE, GET_BYTECODES, GET_TRIE_NODES), with no per-peer, per-message, or global cap on the number of concurrently scheduled tasks. SnapProtocolManager.processMessage forwards every request to EthScheduler's services executor, an unbounded cached thread pool, so a new native thread is created whenever no idle thread can immediately accept the task. Per-task work caps inside SnapServer bound the cost of each individual task but do not bound how many run concurrently. The exhausted resource is off-heap native thread stacks, the same class of defect as the NEW_BLOCK_HASHES fan-out, reached over the snap sub-protocol rather than eth. This is CertiK finding HYB-05 (Medium). Not yet fixed as of Besu 26.7.1.

## Patches and references

Fixed in Besu 26.8.0.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/683880baa609
- Pull request: https://github.com/besu-eth/besu/pull/11101
