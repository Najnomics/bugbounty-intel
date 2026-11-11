# GHSA-3fm2-7wx2-vp46: Historical block requests can cause missed validator duties

| Field | Value |
| --- | --- |
| Repo | sigp/lighthouse |
| GHSA | GHSA-3fm2-7wx2-vp46 |
| CVE | none assigned |
| Severity | medium |
| CWE | n/a |
| Published | 2026-10-15T04:55:06Z |
| Updated | 2026-10-15T04:55:06Z |
| Affected |  <8.2.1 (patched: >=8.2.1) |
| Advisory URL | https://github.com/sigp/lighthouse/security/advisories/GHSA-3fm2-7wx2-vp46 |

## Description (verbatim)

### Summary
A peer connected to a Lighthouse beacon node can keep the beacon node busy by sending `BlocksByRoot` or `BlocksByRange` requests for historical blocks. It costs nothing for the attacker to send the requests, but it requires Lighthouse to obtain the execution payload via the execution client, which occupies the beacon processor workers. If timed correctly, it can lead to missed validator duties such as missed attestations and missed proposals.

### Impact
A targeted Lighthouse node can miss its validator duties while its beacon-processor workers are occupied serving historical block requests. When a requested block's payload is not stored in the database, Lighthouse rebuilds it by calling the execution client, which takes time and keeps the worker busy.

In a simulated attack on a beacon node with 4 workers:
- 1 attacking peer stalls the beacon node for a few seconds. If the validator is proposing or attesting at this time, it will miss the duty.
- 4 attacking peers: successful attestations dropped from 128/128 to 54/128.
- 8 attacking peers: successful attestations dropped from 128/128 to 10/128.
- 10 attacking peers: all workers were busy for a few minutes, which means that the beacon node cannot perform any validator duties in this duration.

The victim node will not crash and it does not cause out-of-memory issues. The node will recover after the attack stops. The attack does not cause large scale network safety and liveness issues. 

### Patches
The fix involves how Lighthouse rebuilds historical blocks. Lighthouse now asks the execution client for payloads by hash instead of by range. This reduces the number of payload lookups, limiting the cost of serving a request. You may refer to this commit for the details: https://github.com/sigp/lighthouse/commit/787614f6f646b28a4a9e4c0dc039edb1d9e59da5.

### Credits
This issue was reported by @ustas-eth to the Ethereum Foundation bug bounty program.

