# GHSA-5h3r-fpmj-483w: Lock-time mempool rejection bans honest peers that are one block ahead

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-5h3r-fpmj-483w |
| CVE | none assigned |
| Severity | medium (CVSS 5.3) |
| CWE | n/a |
| Published | 2026-10-22T14:46:41Z |
| Updated | 2026-10-22T14:46:41Z |
| Affected | zebrad >= 4.5.0, < 7.0.0 (patched: 7.0.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-5h3r-fpmj-483w |

## Description (verbatim)

# Lock-time mempool rejection bans honest peers that are one block ahead

| Field | Value |
|---|---|
| Severity | Medium |
| CVSS 3.1 | `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L` (5.3, Medium) |
| CWE | CWE-693: Protection Mechanism Failure |
| Affected versions | `zebrad` >= 4.5.0, <= 6.4.2; and 7.0.0-rc.0 |
| Patched versions | 7.0.0 |
| Reporter credit | @SphereDonout (this advisory); @sangsoo-osec (independent public report, #11623) |
| GHSA | [GHSA-5h3r-fpmj-483w](https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-5h3r-fpmj-483w) |
| Fix PR | [#11627](https://github.com/ZcashFoundation/zebra/pull/11627) |

## Am I affected?

You are affected if all of the following hold:

- You run `zebrad` 4.5.0 through 6.4.2, or 7.0.0-rc.0.
- P2P networking is enabled and the mempool is active (the default once the node is near the chain tip).
- Your node receives transaction relay from peers (the default).

No configuration change is required to trigger the issue. Mining, RPC, and wallet configuration do not affect it.

## Summary

A Zebra node that is one block behind a peer can ban that peer for relaying a valid transaction. When an ahead peer relays a transaction whose lock time is satisfied at the ahead peer's next block but not at the lagging node's next block, the lagging node rejects it with a lock-time error and scores the sender at the ban threshold. On 6.4.x the node bans the sender's IP group for 24 hours; on 4.5.0 through 6.3.x it bans the sender's IP until the node restarts. The same transaction becomes valid on the lagging node as soon as it receives the next block. The issue does not affect consensus, funds, or node liveness; it causes honest peers to be dropped.

## Details

Zebra verifies peer-relayed mempool transactions against the receiving node's next block height. The lock-height rule requires the candidate height to be strictly greater than the lock height ([`zebra-consensus/src/transaction/check.rs#L82-L85`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-consensus/src/transaction/check.rs#L82-L85)). A peer at tip `H` evaluates a transaction for candidate `H+1`; a node at tip `H-1` evaluates the same transaction for candidate `H`. A transaction locked until height `H` therefore passes on the ahead peer and fails on the lagging node, although neither node has done anything wrong.

The mempool scoring function assigns `LockedUntilAfterBlockHeight` and `LockedUntilAfterBlockTime` a score of 100 ([`zebra-consensus/src/error.rs#L430-L431`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-consensus/src/error.rs#L430-L431)), equal to the ban threshold ([`zebra-network/src/constants.rs#L401`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-network/src/constants.rs#L401)). When a peer-attributed verification fails, the mempool sends that score for the relaying peer ([`zebrad/src/components/mempool.rs#L725-L743`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebrad/src/components/mempool.rs#L725-L743)), and the address book bans the peer's group once the batched update is flushed ([`zebra-network/src/address_book.rs#L487-L526`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-network/src/address_book.rs#L487-L526)). Both pushed and advertised transactions carry the sending peer's address into this path ([`zebrad/src/components/inbound.rs#L560-L595`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebrad/src/components/inbound.rs#L560-L595)).

A second route reaches the same score. If the receiving node's own tip advances while a transaction is being verified, a successful result is retried against the new tip ([`mempool.rs#L692-L723`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebrad/src/components/mempool.rs#L692-L723)), but a failed result is scored without comparing tips ([`mempool.rs#L725-L743`](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebrad/src/components/mempool.rs#L725-L743)).

The reference behavior differs. `zcashd` rejects a non-final transaction from the mempool with a ban score of 0 and treats it as non-standard rather than invalid ([`zcash/src/main.cpp` `"non-final"`](https://github.com/zcash/zcash/blob/558f68659958/src/main.cpp#L1874-L1877)); it scores a non-final transaction inside a block separately ([`"bad-txns-nonfinal"`](https://github.com/zcash/zcash/blob/558f68659958/src/main.cpp#L5902-L5904)).

The lock-time errors were added to the ban-threshold scoring arm in 4.5.0; 4.4.1 scored them 0.

## Impact

A lagging node bans an honest peer that is ahead of it by one block whenever that peer relays a transaction at the lock-time boundary. Each occurrence removes one peer IP group (on 6.4.x, which can be an IPv6 `/64`) from the lagging node's peer set. On 6.4.x the ban lasts 24 hours. On 4.5.0 through 6.3.x the ban is held per IP with no time-based expiry, so it persists until the node restarts.

The lagging node keeps running and accepts the same transaction after it receives the next block. The issue does not cause a crash, a consensus divergence, state corruption, or loss of funds.

A third party can induce the condition deliberately: by broadcasting transactions locked until the current height immediately after each block, to peers that have already committed that block, it causes nodes that have not yet committed the block to ban the honest peers that relay those transactions. Each lagging node can ban one peer group per such transaction per block, and bans accumulate for their full duration, so the nodes most likely to be banned are the best-connected ones.

## Patches

Fixed in `zebrad` 7.0.0 ([#11627](https://github.com/ZcashFoundation/zebra/pull/11627)). The mempool no longer assigns a peer misbehavior score to lock-height and lock-time rejections (`adjusted_mempool_misbehavior_score`, `zebrad/src/components/mempool.rs`). The transaction is still rejected locally until it becomes valid, and blocks that contain non-final transactions are still scored as before. Upgrade to 7.0.0 or later.

## Workarounds

If you cannot upgrade to 7.0.0 yet:

- Keeping the node well connected and in sync reduces how often it is one block behind a relaying peer.

## Credit

Reported privately by @SphereDonout, with a complete two-node reproduction. Independently found and reported publicly by @sangsoo-osec ([#11623](https://github.com/ZcashFoundation/zebra/issues/11623)), with the fix shape adopted in #11627.

## References

- [GHSA-5h3r-fpmj-483w](https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-5h3r-fpmj-483w)
- [Issue #11623](https://github.com/ZcashFoundation/zebra/issues/11623) and [fix PR #11627](https://github.com/ZcashFoundation/zebra/pull/11627)
- [Zebra 7.0.0 release notes](https://github.com/ZcashFoundation/zebra/releases/tag/v7.0.0)
- [CWE-693: Protection Mechanism Failure](https://cwe.mitre.org/data/definitions/693.html)
- [`lock_time_has_passed`, v6.4.2](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-consensus/src/transaction/check.rs#L71-L100)
- [`mempool_misbehavior_score`, v6.4.2](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-consensus/src/error.rs#L386-L438)
- [`Mempool::poll_ready` result handling, v6.4.2](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebrad/src/components/mempool.rs#L680-L786)
- [Ban constants, v6.4.2](https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-network/src/constants.rs#L400-L433)
- [`zcashd` mempool non-final handling](https://github.com/zcash/zcash/blob/558f68659958/src/main.cpp#L1874-L1877)

