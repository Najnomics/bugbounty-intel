# GHSA-g5j7-4r2x-rx9j: A permissionless non-validator peer can halt QBFT finality through pre-authorization proposal decoding

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-g5j7-4r2x-rx9j |
| CVE | none assigned |
| Severity | high |
| CWE | CWE-400, CWE-770, CWE-799 |
| Published | 2026-10-08T04:08:37Z |
| Updated | 2026-10-08T04:08:37Z |
| Affected | org.hyperledger.besu:besu <= 26.8.1 (patched: 26.9.0) |
| Credits | CertiK4Audit |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-g5j7-4r2x-rx9j |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

## 1. Summary

**Issue:** Besu fully decodes attacker-sized QBFT Proposals on the single consensus event processor before applying cheap sender and height admissibility checks. A non-validator peer can use this work amplification against enough validators to prevent the network from assembling a finality quorum.

**Reachability:** any party with network access to enough QBFT validator P2P listeners to cross the liveness threshold. The tested actor authenticated only a newly generated RLPx identity and held no validator key, Ethereum account, funds, RPC credential, filesystem access or operator privilege. In a four-validator QBFT network, reaching two validators is sufficient to prevent the three-signature quorum.

**Severity:** Critical when enough validator P2P listeners accept ordinary inbound RLPx peers — one self-generated non-validator identity halted four-validator QBFT finality by directly attacking exactly two validators. Strict peer permissioning changes the actor class and lowers the availability rating.

One ordinary non-validator peer can make two validators serially decode attacker-sized QBFT Proposal certificates. Honest consensus messages and timers share that single FIFO processor, so the work blocks finality without crashing either target.

`BftProtocolManager` converts every inbound consensus message into a `BftEvent` and adds it to `BftEventQueue`. The queue limits event count, not expanded bytes, nested certificate elements, decode work or sender share. `QbftController` later decodes the complete Proposal—including both certificate lists—before applying message admissibility checks. Current-height messages reach `isMsgFromKnownValidator` only after decoding. The tested far-future messages are also completely decoded before `FutureMessageBuffer` rejects them for exceeding the configured future-height distance. In both cases, rejection occurs too late to protect the consensus processor from the decode work.

The strongest deterministic run used one self-generated identity and exactly two target validators. It sent one distinct 8,388,564-byte expanded future-height Proposal per target per second for five minutes. Each Proposal contained 78,391 prepared-certificate entries. All 600 sends completed. The four validators advanced from a common height 66 to 68 during the initial seconds and then stayed at height 68 and one canonical hash across 310.662 seconds of action-window observations. After the peer disconnected, finality still did not recover during the complete 600-second recovery window.

This is not rated from RSS or queue growth. Every validator process remained running, healthy, RPC-responsive and `syncing=false`, with no OOM; each reported three active ETH peers. The proven consequence is the network-wide finality halt.

**Public-prior-art check, 26 August 2026.** Besu's [public advisory page](https://github.com/besu-eth/besu/security/advisories) contains no advisory for this QBFT mechanism. The nearest public symptom is [issue #6896](https://github.com/besu-eth/besu/issues/6896), an unreproduced Besu 22.10.0 OOM report during Blockscout synchronization that included `BftEventQueue` warnings. That issue does not identify a permissionless non-validator Proposal stream, pre-authorization nested-certificate decoding, a two-validator threshold attack, or a process-healthy consensus halt.

## 2. Affected code locations

Paths at commit [`49026aaf059f832a93f964d8d27191de2f0580e9`](https://github.com/besu-eth/besu/commit/49026aaf059f832a93f964d8d27191de2f0580e9), released as Besu 26.7.1:

- [`BftProtocolManager.java` L94–103](https://github.com/besu-eth/besu/blob/49026aaf059f832a93f964d8d27191de2f0580e9/consensus/common/src/main/java/org/hyperledger/besu/consensus/common/bft/protocol/BftProtocolManager.java#L94-L103) — every inbound BFT message becomes an event and is enqueued without an author, byte or work gate.
- [`BftEventQueue.java` L29–74](https://github.com/besu-eth/besu/blob/49026aaf059f832a93f964d8d27191de2f0580e9/consensus/common/src/main/java/org/hyperledger/besu/consensus/common/bft/BftEventQueue.java#L29-L74) — an unbounded `LinkedBlockingQueue` guarded only by a non-atomic `queue.size() > messageQueueLimit` count check.
- [`BftProcessor.java` L66–79](https://github.com/besu-eth/besu/blob/49026aaf059f832a93f964d8d27191de2f0580e9/consensus/common/src/main/java/org/hyperledger/besu/consensus/common/bft/BftProcessor.java#L66-L79) — one processor drains the shared FIFO and dispatches every BFT event.
- [`QbftController.java` L96–108](https://github.com/besu-eth/besu/blob/49026aaf059f832a93f964d8d27191de2f0580e9/consensus/qbft-core/src/main/java/org/hyperledger/besu/consensus/qbft/core/statemachine/QbftController.java#L96-L108) — the complete message is decoded before it is consumed.
- [`QbftController.java` L306–320](https://github.com/besu-eth/besu/blob/49026aaf059f832a93f964d8d27191de2f0580e9/consensus/qbft-core/src/main/java/org/hyperledger/besu/consensus/qbft/core/statemachine/QbftController.java#L306-L320) — `isMsgFromKnownValidator` runs only after decode for current-height messages; future messages have already incurred decode work before buffering logic.
- [`FutureMessageBuffer.java` L199–225](https://github.com/besu-eth/besu/blob/49026aaf059f832a93f964d8d27191de2f0580e9/consensus/common/src/main/java/org/hyperledger/besu/consensus/common/bft/statemachine/FutureMessageBuffer.java#L199-L225) — the tested height offset is rejected here only after the complete Proposal has been decoded.
- [`Proposal.java` L114–128](https://github.com/besu-eth/besu/blob/49026aaf059f832a93f964d8d27191de2f0580e9/consensus/qbft-core/src/main/java/org/hyperledger/besu/consensus/qbft/core/messagewrappers/Proposal.java#L114-L128) — `Proposal.decode` materializes the round-change and prepare certificate lists.
- [`RlpxConfiguration.java` L27–35](https://github.com/besu-eth/besu/blob/49026aaf059f832a93f964d8d27191de2f0580e9/ethereum/p2p/src/main/java/org/hyperledger/besu/ethereum/p2p/config/RlpxConfiguration.java#L27-L35) — the generic expanded-message ceiling is 10 MiB, but no QBFT aggregate byte, structural-cardinality or per-peer work budget exists before the serial decode.

## 3. Root cause

The admission limit measures the wrong unit and the authorization gate runs after the expensive unit has already been consumed.

- **Count is not work.** A Proposal near the generic 10 MiB ceiling and containing tens of thousands of nested certificate elements costs one queue entry, the same as a small honest message.
- **No sender partition exists.** One freely generated peer can consume the consensus processor's work budget; there is no per-peer event, expanded-byte, certificate-cardinality or decode-time reservation.
- **Timers and honest traffic have no protected lane.** Block timers, chain-head events and honest consensus messages wait behind attacker-controlled Proposal decode work in the same FIFO.
- **Admissibility checks are post-decode.** The current-height author check and the tested far-future height rejection cannot undo work already admitted and serialized ahead of consensus-critical events.
- **The transport ceiling is only per message.** The 10 MiB RLPx limit bounds one expanded payload, not aggregate admitted work or the multiplication produced by a sustained stream.

The `queue.size() > messageQueueLimit` comparison also permits an entry when the queue is already exactly at the configured limit and does not reserve capacity atomically, but the demonstrated halt did not rely on that off-by-one: only 300 messages per target were sent, below the default 1,000-event limit.

## 4. Impact

- **Network-wide finality halted at the real threshold.** One external peer directly targeted validators 1 and 2; validators 3 and 4 received no measured attack traffic and remained independent observers. Four-validator QBFT requires three signatures, so impairing two validators prevents quorum.
- **The halt was sustained.** The common canonical head remained unchanged across 310.662 seconds of action-window observations and the following 600-second recovery window.
- **The attack was positively delivered to both targets.** Each target received 300 messages and Besu's Proposal-byte metric increased by approximately 2.516 GB on each.
- **The measured sender cost was bounded.** The attacker's interface transmitted 245,257,512 bytes over 309.77 seconds—approximately 0.792 MB/s aggregate—while the two validators accounted approximately 5.033 GB of expanded Proposal data in total.
- **No crash or OOM was needed.** Target peak memory increased by approximately 162 MB and 165 MB; every process stayed healthy. The impact is consensus starvation, not resource telemetry.
- **The targets fell behind in QBFT rounds.** During the halt, the untouched observers reached round 7 while the targeted validators remained around round 2. With only two timely validators, the network could not assemble the required three signatures.
- **Stopping the sender did not restore service inside the observation window.** Finality did not recover during the 600-second observation window after disconnect; the experiment did not establish the full cause or eventual recovery time. Coordinated restart was not tested.
- **Strict peer permissioning mitigates reachability.** If every validator endpoint admits only allowlisted peers, the same code path requires a permissioned identity. Ordinary RLPx authentication alone only proves ownership of the attacker's freely generated key.

**Severity:** Critical for a QBFT deployment whose validator P2P listeners accept ordinary inbound peers. The same permissionless mechanism was delivered concurrently to the minimum two-of-four liveness threshold and stopped network-wide finality for the complete observation window.

## 5. Steps to reproduce (deterministic PoC)

**Method.** Create a dedicated private four-validator QBFT network from fresh genesis. Run every validator from an unmodified Besu 26.7.1 build at commit `49026aaf059f832a93f964d8d27191de2f0580e9`. Run one external non-validator peer separately with a hard limit of two vCPUs and two GiB RAM, and connect it only to validators 1 and 2. Validators 3 and 4 remain untouched observers. No Hyperledger or third-party infrastructure is contacted.

**Goal.** Determine whether one external non-validator peer can halt a four-validator QBFT network by sending bounded traffic only to the minimum two-validator liveness threshold, without crashing or stopping any validator.

**Control.** All four validators first finalized one common chain. A separate capture control temporarily used the test-network validator-4 key only to obtain a known-valid canonical Proposal shape while validators 1–3 retained quorum. Validator 4 was then restored and all four validators proved common progress before the measured attack. The attack identity was freshly generated and unrelated to every validator. Capturing the control is not an attacker prerequisite; canonical block material is obtainable through ordinary ETH synchronization from the same reachable network, without a validator secret.

**Fault.** The client negotiated `istanbul/100`, signed a future-height outer Proposal with its non-validator key, and filled the prepared certificate with 78,391 structurally decodable entries. It generated 300 byte-distinct Proposals and sent each one to both targets at one-second intervals:

```java
final NodeKey nodeKey = ephemeralNodeKey();
final List<Endpoint> attackEndpoints = endpoints.subList(0, 2);
final QbftBlock block = captured.getBlock();
final long futureSequence =
    captured.getRoundIdentifier().getSequenceNumber() + 1_024;
final ConsensusRoundIdentifier future =
    new ConsensusRoundIdentifier(futureSequence, 0);

try (PeerSession session =
    PeerSession.open(nodeKey, new NoOpManager(), attackEndpoints, count -> {})) {
  final SignedData<PreparePayload> filler =
      sign(nodeKey, new PreparePayload(future, block.getHash()));
  final SignedData<ProposalPayload> outer =
      sign(nodeKey, new ProposalPayload(future, block, BLOCK_CODEC));

  for (int index = 0; index < 300; index++) {
    final SignedData<PreparePayload> distinct =
        sign(
            nodeKey,
            new PreparePayload(
                new ConsensusRoundIdentifier(futureSequence, 1_000_000 + index),
                Hash.hash(Bytes.ofUnsignedLong(index + 1L))));

    // encode exposes one distinct entry followed by 78,390 filler entries.
    final Bytes encoded = encode(outer, distinct, filler, 78_391);
    for (final PeerConnection connection : session.connections()) {
      connection.send(
          connection.capability(Istanbul100SubProtocol.NAME),
          new RawMessage(QbftV1.PROPOSAL, encoded));
    }
    Thread.sleep(1_000L);
  }
}
```

Compile the external client against the unmodified Besu 26.7.1 distribution libraries, negotiate only `istanbul/100`, and open outbound RLPx sessions to validators 1 and 2 using the self-generated node key. The `encode` helper constructs `new Proposal(outer, List.of(), certificate).encode()`, where `certificate` exposes the one distinct entry followed by 78,390 references to `filler`. Each resulting Proposal is 8,388,564 expanded bytes.

**Observed.** The non-validator completed every bounded send. All four validators retained the same canonical head, but finality stopped while every validator process remained live:

```text
attacker identity:       non-validator, self-generated
direct targets:          validator-1, validator-2
sent per target:         300 / 300, zero send failures
expanded Proposal size:  8,388,564 bytes
certificate entries:     78,391
sender interface bytes:  245,257,512 total (~791,741 bytes/s)
common head:              66 -> 68, then unchanged
active trailing stall:   310.662 seconds
post-disconnect recovery: no progress for 600 seconds
target processes:         running, healthy, OOM=false
```

**Result: Vulnerability reproduced** — a permissionless non-validator peer delivered bounded traffic to exactly two honest validators and halted common QBFT finality without killing either node.

## 6. Suggested remediation

- **Apply a QBFT-specific expanded-size and structural-cardinality ceiling before complete Proposal or RoundChange decoding.** Bound nested certificate counts independently of the generic RLPx message ceiling.
- **Perform a cheap outer-envelope parse and author gate before nested materialization.** Recover and reject a non-validator signer without decoding the embedded block and certificate lists. If that split cannot be made safe, enforce a conservative pre-authorization size/work ceiling first.
- **Reserve aggregate and per-peer work atomically.** Charge in-flight expanded bytes, nested elements and decode tasks before enqueue; release the reservation on every terminal path.
- **Protect consensus-critical events.** Give timers, chain-head events and current-height authorized-validator messages a reserved capacity or separate priority lane that untrusted traffic cannot occupy.
- **Penalize repeated unauthorized consensus traffic.** Disconnect or quarantine peers that send signed QBFT messages whose author is not a current validator.
- **Fix the queue bound itself.** Replace the `size()` precheck with a capacity-enforcing offer and observable rejection counters. This is defense in depth; an entry-count fix alone does not address variable decode work.
- **Retain threshold regression coverage.** Test one self-generated identity against exactly two of four validators, verify positive delivery to both, and require untouched-observer finality to continue under the bounded hostile stream.

P2P allowlisting is a useful deployment mitigation, but it changes reachability rather than fixing the shared pre-authorization work path.

## 7. Reporter and secure contact

- **Reporter:** CertiK
- **Email:** Security@certik.com
- **Secure contact mechanism:** Security@certik.com
- **Acknowledgement preference:** CertiK, CertiK4Audit

## Patches and references

Fixed in Besu 26.9.0.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/e4d39ad64cc4
- Pull request: https://github.com/besu-eth/besu/pull/11378
