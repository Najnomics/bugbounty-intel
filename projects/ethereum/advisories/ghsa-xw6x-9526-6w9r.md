# GHSA-xw6x-9526-6w9r: Besu's DiscV4 UDP discovery remote DoS

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-xw6x-9526-6w9r |
| CVE | none assigned |
| Severity | high |
| CWE | n/a |
| Published | 2026-10-02T02:17:19Z |
| Updated | 2026-10-02T02:17:19Z |
| Affected | org.hyperledger.besu:besu <= 26.7.1 (patched: 26.8.0) |
| Credits | sturnid |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-xw6x-9526-6w9r |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

## Summary

Besu's DiscV4 UDP ingress decodes every datagram on one thread. The queue
feeding that thread is unbounded. There is no rate limit or admission control.
One remote host can send datagrams faster than the thread decodes. The queue
grows until the JVM heap is exhausted. The whole Besu process dies.

## Vulnerability description

Ingress path:

1. `NettyTransport.V4InboundHandler.channelRead0` copies every datagram into a
   new byte array on the Netty event loop, at line rate. The only filter is a
   per-packet size cap of 1600 bytes (`MAX_PACKET_SIZE_BYTES`).
2. `PeerDiscoveryAgentV4.handleRawIncoming` repeats the size check, then hands
   the decode to an executor with a non-blocking `execute`.
3. The executor is `Executors.newSingleThreadExecutor("discv4-decode")` in
   `NettyPeerDiscoveryAgent`. One consumer thread on an unbounded
   `LinkedBlockingQueue`. There is no bounded queue, semaphore, or rate limiter
   anywhere on this path.
4. Each decode runs `PacketFactory.create`. Its keccak hash check is not
   authentication: the attacker computes the hash over their own payload.
   Secp256k1 public-key recovery then runs unconditionally, even for a garbage
   signature.

One crafted packet can therefore be replayed verbatim at line rate. Every copy
still forces a full secp256k1 recovery on the single decode thread. Ingress
outruns decoding by an order of magnitude.

Discovery is on by default and binds 0.0.0.0:30303 (`DiscoveryConfiguration`).
Any host with UDP reachability to the node can attack.

Measured against Besu 26.7.1 in a 16 GB container: one replayed PING at 30,000
packets/s versus a decode throughput of roughly 1,000-2,000/s. The heap fills in
about 10 minutes. The JVM then GC-thrashes and dies with
`java.lang.OutOfMemoryError`. Total time to kill: about 16 minutes.

Packets can also be padded up to the 1600-byte cap. EIP-8 tolerates extra RLP
list elements, and Besu's PING reader ends with `leaveListLenient()`. This keeps
the packet valid and grows the queue about 12x faster per packet.

## Impact

- Remote, unauthenticated, process-wide DoS. No valid signature or RLPx session
  needed.
- Besu is a single JVM process: discovery, sync, block import, txpool, and RPC
  all die together.
- Default-configured mainnet nodes are exposed.

## Timeline and disclosure

- Proposed timeline: public disclosure 90 days after this report, or with the
  security bulletin, whichever comes first.
- I ask for a patch, a public advisory, and reporter credit.
- If you do not assign a CVE, I could request one from MITRE myself. Please tell
  me your preference so we do not end up with duplicates.

## Patches and references

Fixed in Besu 26.8.0.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/6d731706cb6d
- Pull request: https://github.com/besu-eth/besu/pull/11105
