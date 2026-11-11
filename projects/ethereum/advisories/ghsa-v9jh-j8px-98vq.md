# GHSA-v9jh-j8px-98vq: go-ethereum vulnerable to denial of service via crafted GraphQL query

| Field | Value |
| --- | --- |
| Source | GitHub global Advisory DB (affects go-ethereum) |
| GHSA | GHSA-v9jh-j8px-98vq |
| CVE | CVE-2023-42319 |
| Severity | high |
| Published | 2023-10-18T06:30:30Z |
| Advisory URL | https://github.com/advisories/GHSA-v9jh-j8px-98vq |

## Description (verbatim)

Geth (aka go-ethereum) through 1.13.4, when `--http --graphql` is used, allows remote attackers to cause a denial of service (memory consumption and daemon hang) via a crafted GraphQL query.

NOTE: the vendor's position is that the "graphql endpoint [is not] designed to withstand attacks by hostile clients, nor handle huge amounts of clients/traffic.

## References

- https://nvd.nist.gov/vuln/detail/CVE-2023-42319
- https://geth.ethereum.org/docs/fundamentals/security
- https://blog.mevsec.com/posts/geth-dos-with-graphql
- https://github.com/advisories/GHSA-v9jh-j8px-98vq
