# GHSA-rvxr-393q-q925: Memory exhaustion when serving data column requests

| Field | Value |
| --- | --- |
| Repo | sigp/lighthouse |
| GHSA | GHSA-rvxr-393q-q925 |
| CVE | none assigned |
| Severity | high |
| CWE | n/a |
| Published | 2026-10-26T03:13:56Z |
| Updated | 2026-10-26T03:13:56Z |
| Affected |  <8.3.0 (patched: >=8.3.0) |
| Advisory URL | https://github.com/sigp/lighthouse/security/advisories/GHSA-rvxr-393q-q925 |

## Description (verbatim)

### Summary

When Lighthouse serves `DataColumnsByRange` or `DataColumnsByRoot` requests, it rate-limits how fast it sends the responses back. Lighthouse first reads the requested data column sidecars from the database and produces a full response, and only then rate-limits the sending. Lighthouse generates the response much faster than it is allowed to send. Therefore, any response that exceeds the sending limit is held in an unbounded queue that is only cleared when the peer disconnects. A few peers sending maximum-size requests could make the node accumulate gigabytes of data column sidecars and run out of memory.

### Impact

Any remote peer can send these requests to the victim node. By sending 2 `DataColumnsByRange` and 2 `DataColumnsByRoot` requests, a single peer causes the victim node to accumulate 2.85GiB of data at 21 blobs (current maximum blobs per block on mainnet). This scales linearly with the number of peers connected. Therefore, multiple attacking peers can cost the victim node tens of GiB of memory and crash it with an out-of-memory error. In a simulated devnet, 4 attacking peers crashed a node with a 2 GiB memory limit in about 85 seconds. Supernodes are the easy target as they store all data column sidecars. The node recovers when the peer disconnects, or on a restart.

### Patches

Lighthouse reworked its RPC rate limiting to limit requests at request time rather than response time. Now, when a request arrives, it is checked against the rate limiter before any response is produced, so over-limit response data is no longer queued without bound. You may refer to this commit for the details: https://github.com/sigp/lighthouse/commit/b7a6e64066d3a04ac5974c2236d30f5a33b61d30.


### Credits

This issue was reported by the Ethereum Foundation Protocol Security Research Team. 
