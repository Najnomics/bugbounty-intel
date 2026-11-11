# GHSA-5m8f-chrv-7rw5: Denial of Service in Go-Ethereum

| Field | Value |
| --- | --- |
| Source | GitHub global Advisory DB (affects go-ethereum) |
| GHSA | GHSA-5m8f-chrv-7rw5 |
| CVE | CVE-2021-43668 |
| Severity | medium |
| Published | 2021-11-23T18:04:47Z |
| Advisory URL | https://github.com/advisories/GHSA-5m8f-chrv-7rw5 |

## Description (verbatim)

Go-Ethereum 1.10.9 nodes crash (denial of service) after receiving a serial of messages and cannot be recovered. They will crash with "runtime error: invalid memory address or nil pointer dereference" and arise a SEGV signal.

## References

- https://nvd.nist.gov/vuln/detail/CVE-2021-43668
- https://github.com/ethereum/go-ethereum/issues/23866
- https://github.com/syndtr/goleveldb/issues/373
- https://github.com/advisories/GHSA-5m8f-chrv-7rw5
