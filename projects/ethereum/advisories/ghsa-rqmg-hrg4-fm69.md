# GHSA-rqmg-hrg4-fm69: Go Ethereum allows attackers to use manipulation of time-difference values to achieve replacement of main-chain blocks

| Field | Value |
| --- | --- |
| Source | GitHub global Advisory DB (affects go-ethereum) |
| GHSA | GHSA-rqmg-hrg4-fm69 |
| CVE | CVE-2022-37450 |
| Severity | medium |
| Published | 2022-08-06T00:00:36Z |
| Advisory URL | https://github.com/advisories/GHSA-rqmg-hrg4-fm69 |

## Description (verbatim)

Go Ethereum (aka geth) through 1.10.21 allows attackers to increase rewards by mining blocks in certain situations, and using a manipulation of time-difference values to achieve replacement of main-chain blocks, aka Riskless Uncle Making (RUM), as exploited in the wild in 2020 through 2022.

## References

- https://nvd.nist.gov/vuln/detail/CVE-2022-37450
- https://github.com/ethereum/go-ethereum/blob/671094279e8d27f4b4c3c94bf8b636c26b473976/core/forkchoice.go#L91-L94
- https://medium.com/@aviv.yaish/uncle-maker-time-stamping-out-the-competition-in-ethereum-d27c1cb62fef
- https://news.ycombinator.com/item?id=32354896
- http://dx.doi.org/10.13140/RG.2.2.27813.99043
- https://github.com/advisories/GHSA-rqmg-hrg4-fm69
