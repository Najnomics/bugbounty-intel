# GHSA-689v-6xwf-5jf3: DoS via malicious p2p message

| Field | Value |
| --- | --- |
| Repo | ethereum/go-ethereum |
| GHSA | GHSA-689v-6xwf-5jf3 |
| CVE | CVE-2026-26313 |
| Severity | medium |
| CWE | n/a |
| Published | 2026-02-17T16:23:39Z |
| Updated | 2026-02-17T16:23:39Z |
| Affected | github.com/ethereum/go-ethereum < 1.17.0 (patched: >= 1.17.0) |
| Advisory URL | https://github.com/ethereum/go-ethereum/security/advisories/GHSA-689v-6xwf-5jf3 |

## Description (verbatim)

### Impact

An attacker can cause high memory usage by sending a specially-crafted p2p message.
More details to be released later.

### Patches

The issue is resolved in the v1.17.0 release. 

### Credit

This issue was reported to the Ethereum Foundation Bug Bounty Program by @revofusion
