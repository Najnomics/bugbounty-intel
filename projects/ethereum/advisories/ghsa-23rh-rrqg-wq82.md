# GHSA-23rh-rrqg-wq82: `QbftRoundChangeManager.roundChangeCache` is keyed by `ConsensusRoundIdentifier` (sequence + round number) and `RoundChangePayloadValidator` only requires `targetRound > 0` — there is no upper bound. A single misbehaving validator can flood `RoundC

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-23rh-rrqg-wq82 |
| CVE | none assigned |
| Severity | medium |
| CWE | CWE-400 |
| Published | 2026-10-02T02:18:13Z |
| Updated | 2026-10-02T02:18:13Z |
| Affected | org.hyperledger.besu:besu <= 26.7.1 (patched: 26.8.0) |
| Credits | macfarla |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-23rh-rrqg-wq82 |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

**Summary**: `QbftRoundChangeManager.roundChangeCache` is keyed by `ConsensusRoundIdentifier` (sequence + round number) and `RoundChangePayloadValidator` only requires `targetRound > 0` — there is no upper bound. A single misbehaving validator can flood `RoundChange` messages with monotonically increasing round numbers up to `Integer.MAX_VALUE` (~2.1 billion); each unique round produces a fresh `RoundChangeStatus` map entry that is never evicted. On a QBFT-secured chain this exhausts the heap of every honest node in the network.

**Severity**: High

**Affected file/line**:
- `consensus/qbft-core/src/main/java/org/hyperledger/besu/consensus/qbft/core/statemachine/RoundChangeManager.java:102` (unbounded `roundChangeCache`)
- `consensus/qbft-core/src/main/java/org/hyperledger/besu/consensus/qbft/core/statemachine/RoundChangeManager.java:233-242` (`storeRoundChangeMessage`, `computeIfAbsent` with no cap)
- `consensus/qbft-core/src/main/java/org/hyperledger/besu/consensus/qbft/core/validation/RoundChangePayloadValidator.java:71-75` (only requires `targetRound > 0`, no upper bound)
- `consensus/qbft-core/src/main/java/org/hyperledger/besu/consensus/qbft/core/payload/QbftPayload.java:45-47` (`readIntScalar()` admits any 4-byte signed int up to `2^31-1`)

## Vulnerability

`RoundChangeManager` keeps one `RoundChangeStatus` per (height, round):

```java
// RoundChangeManager.java:102
@VisibleForTesting
final Map<ConsensusRoundIdentifier, RoundChangeStatus> roundChangeCache = Maps.newHashMap();
```

Every accepted `RoundChange` message creates a new entry if one does not already exist:

```java
// RoundChangeManager.java:213-242
public Optional<Collection<RoundChange>> appendRoundChangeMessage(final RoundChange msg) {
  if (!isMessageValid(msg)) {
    LOG.info("RoundChange message was invalid.");
    return Optional.empty();
  }
  final RoundChangeStatus roundChangeStatus = storeRoundChangeMessage(msg);
  ...
}

private RoundChangeStatus storeRoundChangeMessage(final RoundChange msg) {
  final ConsensusRoundIdentifier msgTargetRound = msg.getRoundIdentifier();
  final RoundChangeStatus roundChangeStatus =
      roundChangeCache.computeIfAbsent(msgTargetRound, ignored -> new RoundChangeStatus(quorum));
  roundChangeStatus.addMessage(msg);
  return roundChangeStatus;
}
```

`isMessageValid` delegates to `RoundChangeMessageValidator`, which in turn delegates to `RoundChangePayloadValidator.validate`:

```java
// RoundChangePayloadValidator.java:57-89
public boolean validate(final SignedData<RoundChangePayload> signedPayload) {
  if (!validators.contains(signedPayload.getAuthor())) { ... return false; }
  final RoundChangePayload payload = signedPayload.getPayload();
  if (payload.getRoundIdentifier().getSequenceNumber() != chainHeight) { ... return false; }

  final int targetRound = payload.getRoundIdentifier().getRoundNumber();
  if (targetRound <= 0) {
    LOG.info("{}: must contain a positive target round number", ERROR_PREFIX);
    return false;
  }

  if (payload.getPreparedRoundMetadata().isPresent()) {
    final PreparedRoundMetadata metadata = payload.getPreparedRoundMetadata().get();
    if (metadata.getPreparedRound() >= targetRound) { ... return false; }
    if (metadata.getPreparedRound() < 0)            { ... return false; }
  }
  return true;
}
```

The only round-related guards are `targetRound > 0` and (when present) `preparedRound < targetRound`. There is no upper bound at all, so any value up to `Integer.MAX_VALUE` is accepted.

`RoundChangePayload.readFrom` reads the round number via `readIntScalar()` (`QbftPayload.java:46`) which accepts up to 4 bytes signed:

```java
// QbftPayload.java:45-47
protected static ConsensusRoundIdentifier readConsensusRound(final RLPInput in) {
  return new ConsensusRoundIdentifier(in.readLongScalar(), in.readIntScalar());
}
```

so the wire encoding can carry any round in `[1, 2^31-1]`.

`RoundChange` messages without an attached `proposedBlock` and without `preparedRoundMetadata` need no block validation:

```java
// RoundChangeMessageValidator.java:79-91
public boolean validate(final RoundChange msg) {
  if (!roundChangePayloadValidator.validate(msg.getSignedPayload())) { return false; }
  if (msg.getProposedBlock().isPresent()) {
    return validateWithBlock(msg);   // skipped if absent
  }
  return msg.getPreparedRoundMetadata().isEmpty();
}
```

so a malicious validator can craft tiny RLP payloads of the form `[ConsensusRound{height, round=k}, []]` for any `k` in `[1, 2^31-1]` and burn ~64–128 bytes of heap per message on every honest node.

The existing `discardRoundsPriorTo` only purges rounds **earlier** than the just-completed one (`RoundChangeManager.java:249-251`) — it never purges future rounds, so once height `h` is finalised the cache for that height is dropped, but during height `h` the cache grows monotonically.

### Compounding factors

1. `roundChangeCache` is a `HashMap`, not a bounded `Caffeine` cache or a TreeMap with a window. There is no max size, no LRU, no eviction.
2. Each `RoundChangeStatus` allocates its own `LinkedHashMap` (`receivedMessages`) with default capacity 16, so the per-entry footprint is ~250–300 bytes (key + value object + child map) on a 64-bit JVM.
3. `Integer.MAX_VALUE` rounds × ~300 bytes ≈ 600 GB worst case. Even a fraction of that — say 10⁸ rounds — is enough to OOM a default 4-8 GB Besu heap.
4. The flood does **not** trigger `peer.disconnect`: the validator is in the validator set, so the messages are signed correctly and pass author check; the only failure mode is to silently drop one malformed message and accept the next.
5. `storeAndLogRoundChangeSummary` (the IBFT/QBFT diagnostic helper at `RoundChangeManager.java:151-171`) maintains a *second* unbounded map, `roundSummary`, keyed by validator address — that one is at least bounded by validator-set size, but the *value* (round identifier) is replaced on each new message so it does not grow. The primary leak is the round-keyed cache.

## Impact

- **Network-wide DoS of a QBFT chain by a single byzantine validator.** All honest nodes accept the messages, allocate the cache entries, and OOM at roughly the same rate. Permissioned QBFT deployments (Hyperledger Besu's primary deployment target for QBFT, e.g. consortium chains, financial test-nets) are particularly exposed because they are explicitly configured for low-tolerance byzantine behaviour — a single rogue validator should not be able to halt the chain.
- **Cheap to mount.** A validator only needs to keep a UDP/TCP connection open and sign ~32 bytes of payload per message. Sustaining 10k messages/sec is trivial.
- **Indistinguishable from a honest validator that genuinely sees a long round-change cascade**, so naive logging-based monitoring will not detect it until heap pressure shows up.
- **Recovery requires restart**, since `discardRoundsPriorTo` is only called when *this* node (or another honest node) successfully proposes a round; if the chain is already halted because of memory pressure, the cache cannot be cleaned up.
- **Persists across the height** even if the malicious round changes never reach quorum: the cache for height `h` is only cleared when height `h` is committed, so the attacker can ride a single height for as long as the network can stand.

## PoC

Sketch (intentionally not a full reproducer because it requires a malicious validator key):

```java
// Run as a malicious validator on a QBFT testnet.
final BftProtocolMessageFactory factory = new BftProtocolMessageFactory(myValidatorKey);
for (int round = 1; round < Integer.MAX_VALUE; round++) {
    RoundChange msg = factory.createRoundChange(
        new ConsensusRoundIdentifier(currentHeight, round),
        Optional.empty()  /* no proposed block */
    );
    network.broadcast(msg);
}
```

After ~30s of broadcast at 10k msg/sec, every honest node in the network has ~300k cache entries (~90 MB of allocated `Maps.newLinkedHashMap()` skeletons plus `RoundChangeStatus` objects). At 100k msg/sec sustained for ten minutes, every node exhausts a 4 GB heap. The chain halts.

A non-validator-key version of the attack is also possible: collect a peer's RoundChange messages (or steal a validator key from a single compromised node), then re-broadcast at high rate. Honest nodes do not de-duplicate by signature in `roundChangeCache` — they de-duplicate per (round, author) inside `RoundChangeStatus.addMessage`, so flooding *different* rounds is the high-amplification path.

## Recommendation

1. **Bound the round number on the wire**. `RoundChangePayloadValidator.validate` should reject `targetRound > MAX_ALLOWED_ROUND` — a sane network should never need more than a few hundred rounds at one height. Hard-coding `MAX_ALLOWED_ROUND = 1024` (or making it configurable) is a one-liner with no downside.
   ```java
   if (targetRound <= 0 || targetRound > MAX_ALLOWED_ROUND) {
     LOG.info("{}: target round number out of range", ERROR_PREFIX);
     return false;
   }
   ```

2. **Bound the cache size**. Replace the plain `HashMap` with a Caffeine cache or with an `if (roundChangeCache.size() >= MAX_CACHED_ROUNDS) { return Optional.empty(); }` guard at the top of `storeRoundChangeMessage`.

3. **Bound the relative gap**. A round more than (say) 64 ahead of the current round is almost certainly malicious. `RoundChangeMessageValidator` already knows the current height — passing the current round in too would let it reject `targetRound > currentRound + 64`.

4. **Penalize / disconnect** validators that send out-of-band rounds. The discovery / RLPx layer already supports peer reputation (`AbstractPeerBlockValidator`, `PeerReputation`); plumb a "byzantine round change rate" signal through to it so a misbehaving validator gets disconnected after N malformed messages.

5. **Consider the same hardening for IBFT** (`consensus/ibft/.../RoundChangeManager.java`) and IBFT2 — the same shape of cache and validator pair exists in those packages and has the same property.

**Payment / Contact**
If this finding qualifies for a reward, payment can be sent to:
`0x83e033dd8ddb93052cc880227b06a8ee38f25eb2`
(EVM address — any chain)

Filing through GitHub PVR because the platform that hosts the official bounty has KYC requirements I have not been able to clear from my jurisdiction.

## Patches and references

Fixed in Besu 26.8.0.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/118f8b1920f9
- Pull request: https://github.com/besu-eth/besu/pull/11102
