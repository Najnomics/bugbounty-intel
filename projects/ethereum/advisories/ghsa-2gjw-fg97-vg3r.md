# GHSA-2gjw-fg97-vg3r: DoS via malicious p2p message

| Field | Value |
| --- | --- |
| Repo | ethereum/go-ethereum |
| GHSA | GHSA-2gjw-fg97-vg3r |
| CVE | CVE-2026-26314 |
| Severity | high |
| CWE | n/a |
| Published | 2026-02-17T16:23:48Z |
| Updated | 2026-02-17T16:23:48Z |
| Affected | github.com/ethereum/go-ethereum <= 1.16.8 (patched: >= 1.16.9) |
| Advisory URL | https://github.com/ethereum/go-ethereum/security/advisories/GHSA-2gjw-fg97-vg3r |

## Description (verbatim)

### Impact

A vulnerable node can be forced to shutdown/crash using a specially crafted message.
More details to be released later.

### Patches

The problem is resolved in the v1.16.9 and v1.17.0 releases of Geth.

### Credit

This issue was reported to the Ethereum Foundation Bug Bounty Program by Waleed Ahmed from vulsight.com

