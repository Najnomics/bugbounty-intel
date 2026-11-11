# GHSA-vrcc-g6vj-mh5w: Denial of service in go-ethereum

| Field | Value |
| --- | --- |
| Source | GitHub global Advisory DB (affects go-ethereum) |
| GHSA | GHSA-vrcc-g6vj-mh5w |
| CVE | CVE-2021-42219 |
| Severity | high |
| Published | 2022-03-18T00:01:13Z |
| Advisory URL | https://github.com/advisories/GHSA-vrcc-g6vj-mh5w |

## Description (verbatim)

Go-Ethereum v1.10.9 was discovered to contain an issue which allows attackers to cause a denial of service (DoS) via sending an excessive amount of messages to a node. This is caused by missing memory in the component /ethash/algorithm.go.

## References

- https://nvd.nist.gov/vuln/detail/CVE-2021-42219
- https://docs.google.com/document/d/1dYFSpNZPC0OV-n1mMqdc269u9yYU1XQy/edit?usp=sharing&ouid=112110745137218798745&rtpof=true&sd=true
- https://github.com/advisories/GHSA-vrcc-g6vj-mh5w
