# GHSA-pvx3-gm3c-gmpr: Denial of Service in Go-Ethereum

| Field | Value |
| --- | --- |
| Source | GitHub global Advisory DB (affects go-ethereum) |
| GHSA | GHSA-pvx3-gm3c-gmpr |
| CVE | CVE-2022-23327 |
| Severity | high |
| Published | 2022-03-05T00:00:46Z |
| Advisory URL | https://github.com/advisories/GHSA-pvx3-gm3c-gmpr |

## Description (verbatim)

A design flaw in Go-Ethereum 1.10.12 and older versions allows an attacker node to send 5120 future transactions with a high gas price in one message, which can purge all of pending transactions in a victim node's memory pool, causing a denial of service (DoS).

## References

- https://nvd.nist.gov/vuln/detail/CVE-2022-23327
- https://dl.acm.org/doi/pdf/10.1145/3460120.3485369
- https://tristartom.github.io/docs/ccs21.pdf
- https://nrdax.com/techniques/NRDAX-T0156-mempool-pending-eviction-flood
- https://github.com/advisories/GHSA-pvx3-gm3c-gmpr
