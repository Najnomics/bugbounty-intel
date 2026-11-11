# GHSA-qr2j-wrhx-4829: Go Ethereum Improper Input Validation

| Field | Value |
| --- | --- |
| Source | GitHub global Advisory DB (affects go-ethereum) |
| GHSA | GHSA-qr2j-wrhx-4829 |
| CVE | CVE-2018-16733 |
| Severity | high |
| Published | 2021-05-18T18:38:06Z |
| Advisory URL | https://github.com/advisories/GHSA-qr2j-wrhx-4829 |

## Description (verbatim)

In Go Ethereum (aka geth) before 1.8.14, TraceChain in eth/api_tracer.go does not verify that the end block is after the start block.

### Specific Go Packages Affected
github.com/ethereum/go-ethereum/eth

## References

- https://nvd.nist.gov/vuln/detail/CVE-2018-16733
- https://github.com/ethereum/go-ethereum/commit/106d196ec4a6451efedc60ab15957f231fa85639
- https://github.com/advisories/GHSA-qr2j-wrhx-4829
