# GHSA-mq3p-rrmp-79jg: DoS via malicious p2p message

| Field | Value |
| --- | --- |
| Repo | ethereum/go-ethereum |
| GHSA | GHSA-mq3p-rrmp-79jg |
| CVE | CVE-2026-22868 |
| Severity | medium |
| CWE | n/a |
| Published | 2026-01-13T19:24:59Z |
| Updated | 2026-01-13T20:04:07Z |
| Affected | github.com/ethereum/go-ethereum <= 1.16.7 (patched: >= 1.16.8) |
| Advisory URL | https://github.com/ethereum/go-ethereum/security/advisories/GHSA-mq3p-rrmp-79jg |

## Description (verbatim)

**Impact**

An attacker can cause high CPU usage by sending a specially crafted p2p message.
More details to be released later.

**Credit**

This issue was reported to the Ethereum Foundation Bug Bounty Program by @Yenya030
