# GHSA-9h4h-8w5p-f28w: Go Ethereum Denial of Service

| Field | Value |
| --- | --- |
| Source | GitHub global Advisory DB (affects go-ethereum) |
| GHSA | GHSA-9h4h-8w5p-f28w |
| CVE | CVE-2018-19184 |
| Severity | high |
| Published | 2021-06-29T21:23:15Z |
| Advisory URL | https://github.com/advisories/GHSA-9h4h-8w5p-f28w |

## Description (verbatim)

`cmd/evm/runner.go` in Go Ethereum (aka geth) allows attackers to cause a denial of service (SEGV) via crafted bytecode.
### Specific Go Packages Affected
github.com/ethereum/go-ethereum/cmd/evm

## References

- https://nvd.nist.gov/vuln/detail/CVE-2018-19184
- https://github.com/ethereum/go-ethereum/issues/18069
- https://github.com/ethereum/go-ethereum/commit/83e2761c3a13524bd5d6597ac08994488cf872ef
- https://github.com/ethereum/go-ethereum/commit/fb9f7261ec51e38eedb454594fc19f00de1a6834
- https://github.com/advisories/GHSA-9h4h-8w5p-f28w
