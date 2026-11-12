# GHSA-6r9q-wjp4-34gh: Pre-STATUS RLPx connections are excluded from --max-peers accounting, letting a peer hold unbounded connections via distinct node identities

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-6r9q-wjp4-34gh |
| CVE | none assigned |
| Severity | medium |
| CWE | n/a |
| Published | 2026-10-02T02:23:09Z |
| Updated | 2026-10-02T02:23:09Z |
| Affected | org.hyperledger.besu:besu <= 26.7.1 (patched: 26.8.0) |
| Credits | Oblivionis214 |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-6r9q-wjp4-34gh |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

Besu enforces --max-peers using EthPeers.peerCount(), which counts only peers that have completed the eth STATUS handshake. Connections that have completed the devp2p HELLO but not yet sent eth STATUS live in a separate incompleteConnections cache with a 20-second expiry and are not counted by peerCount(), the remote-connection-fraction limits, or the net_peerCount gauge. A peer that completes HELLO but never replies with STATUS stays pinned in incompleteConnections, holding an open socket/file-descriptor while remaining invisible to --max-peers; on cache eviction the removal listener does not close a lone pre-STATUS connection, so the socket can be leaked outright. A single peer using distinct node identities per connection can therefore hold far more connections than --max-peers permits, consuming file descriptors and heap unbounded. This is CertiK finding HYB-06 (Medium). Not yet fixed as of Besu 26.7.1.


Independently reported a second time via the Ethereum Foundation bug bounty program; that duplicate report is credited here rather than tracked as a separate advisory.

## Patches and references

Fixed in Besu 26.8.0.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/e540ae239495
- Pull request: https://github.com/besu-eth/besu/pull/11096
