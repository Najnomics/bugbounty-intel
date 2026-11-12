# GHSA-8g2r-qvch-4c9j: GraphQL blocks(from, to) range query has no cap on range span or clamp to the chain head, letting a single client exhaust request-handling capacity

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-8g2r-qvch-4c9j |
| CVE | none assigned |
| Severity | medium |
| CWE | n/a |
| Published | 2026-10-02T02:29:16Z |
| Updated | 2026-10-02T02:29:16Z |
| Affected | org.hyperledger.besu:besu <= 26.7.1 (patched: 26.8.0) |
| Credits | n/a |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-8g2r-qvch-4c9j |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

A GraphQL blocks(from, to) query on Besu iterates every block number in the caller-supplied [from, to] interval and fetches each block, with no clamp to the chain head and no cap on the range span. GraphQLDataFetchers.getRangeBlockDataFetcher() uses the supplied to raw; the only validation is a from > to check. The to parameter accepts any long up to Long.MAX_VALUE via the GraphQL Long scalar, so a single query such as blocks(from:1000000000000, to:9223372036854775806) drives an effectively unbounded loop that pins a request-handling thread. The fetcher passes no IsAliveHandler (unlike getLogsDataFetcher), so the loop cannot be cancelled: a client disconnect or HTTP timeout does not stop the server-side work. A small number of concurrent such queries exhausts request-handling capacity for both the GraphQL service and the main JSON-RPC service. Requires --graphql-http-enabled (off by default). This is CertiK finding HYB-07 (Medium). Not yet fixed as of Besu 26.7.1.

## Patches and references

Fixed in Besu 26.8.0.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/46c2331986da
- Pull request: https://github.com/besu-eth/besu/pull/11095
