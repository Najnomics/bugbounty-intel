# GHSA-8rp4-6f4x-5j4p: Memory leak when peer disconnects after sending RPC requests

| Field | Value |
| --- | --- |
| Repo | sigp/lighthouse |
| GHSA | GHSA-8rp4-6f4x-5j4p |
| CVE | none assigned |
| Severity | medium |
| CWE | n/a |
| Published | 2026-10-26T03:13:02Z |
| Updated | 2026-10-26T03:13:02Z |
| Affected |  <8.3.0 (patched: >=8.3.0) |
| Advisory URL | https://github.com/sigp/lighthouse/security/advisories/GHSA-8rp4-6f4x-5j4p |

## Description (verbatim)

### Summary

When a peer sends an RPC request, Lighthouse keeps a record of it in memory and only removes that record after it has responded to the peer. If the peer disconnects before Lighthouse responds, the record is not removed but stays in memory. By repeatedly connecting, sending a large request, then disconnecting, an attacker can exhaust the victim node's memory and crash the node.


### Impact

Any remote peer can send these requests to the victim node. Each cycle of connecting, sending a `BlobsByRoot` request with the maximum blob count, and disconnecting leaks about 30-46 KiB in the victim node's memory that is never cleared. Lighthouse limits how many requests a single peer can have at one time, but if the peer disconnects, the sent request is no longer counted as active, so it does not use up the limit. Consequently, a single peer can launch the attack. Repeated over time, the accumulated requests exhaust the victim node's memory and can crash it with an out-of-memory error. The node recovers on a restart.

### Patches

Before the fix, a request record was only removed once Lighthouse had sent a response. After the fix, a request is removed when a peer disconnects, even if no response is sent. A disconnecting peer therefore no longer leaks memory. You may refer to this commit for the details: https://github.com/sigp/lighthouse/commit/b7a6e64066d3a04ac5974c2236d30f5a33b61d30.

### Credits

This issue was reported by [Octane Security](https://github.com/Octane-Security) to the Ethereum Foundation Protocol Security Research Team
