# GHSA-4f6v-mj46-gxg3: Coinbase scriptSig rewrite drops a gossiped block on the inbound path without penalizing the supplying peer

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-4f6v-mj46-gxg3 |
| CVE | none assigned |
| Severity | low (CVSS 3.7) |
| CWE | CWE-354, CWE-807 |
| Published | 2026-09-28T07:57:48Z |
| Updated | 2026-09-28T07:57:48Z |
| Affected | zebrad >=6.3.0 (patched: 6.4.2) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-4f6v-mj46-gxg3 |

## Description (verbatim)

# Coinbase scriptSig rewrite drops a gossiped block on the inbound path without penalizing the supplying peer

| Field | Content |
|---|---|
| Severity | Low |
| CVSS 3.1 | `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L` |
| CWE | CWE-354 (Improper Validation of Integrity Check Value); secondary CWE-807 (Reliance on Untrusted Inputs in a Security Decision) |
| Affected versions | All versions through v6.3.0 (latest release) |
| Patched versions | 6.4.2 |
| Reporter credit | craftsoldier |
| GHSA | GHSA-4f6v-mj46-gxg3 |

## Am I affected

You are affected if all of the following hold:

- You run `zebrad` v6.3.0 or earlier (the latest release at time of reporting).
- Your node accepts inbound P2P connections and processes block gossip (the default for a participating node).
- No non-default configuration is required. The default configuration is affected.

The impact is materially higher if your node supplies chain state or block templates to a miner or pool.

## Summary

A malicious peer can delay your node's discovery of the newest canonical block by answering a gossip-initiated block-download request with a forged body that still matches the requested block hash. The peer copies a real block, rewrites only the coinbase transaction scriptSig to encode height 1, and keeps the original header. Because the coinbase scriptSig is excluded from the V5 transaction ID (ZIP-244), the merkle root and block hash are unchanged, so the response passes the hash check. The inbound downloader reads the forged height from the unvalidated body, treats the block as too far behind the tip, and drops it before consensus validation runs. The supplying peer is not scored or banned because the error is returned with `None` as the advertiser address, and the inbound error handler skips errors that lack an advertiser address. The peer can repeat indefinitely.

This is the inbound gossip path sibling of GHSA-g95h-hw6g-pvgv, which describes the same attack on the sync download path. The sync path was fixed in v6.3.0 (adding a parent-header lookup and carrying the advertiser address on the behind-tip error, with scoring gated on height inconsistency so honest peers serving genuinely old blocks are not penalized). The inbound path was not patched. A separate inbound scoring bypass, GHSA-8hh2-hrf2-cqf4 (wrong error downcast type), was also fixed in v6.3.0, but that fix addressed a different mechanism (the verifier-error downcast at `inbound.rs:351-357`), not the pre-verifier height check at `inbound/downloads.rs:390-391` described here.

## Details

For V5+ transactions the transaction ID follows ZIP-244 and excludes authorizing data, including the transparent input scriptSig. The block's transaction merkle tree is built from these transaction IDs.

An attacker copies a canonical block with hash H, changes only the coinbase scriptSig to encode height 1 instead of the real height, and retains the original header. The resulting body keeps the canonical merkle root and, because the header is unchanged, the canonical block hash H and proof of work.

In the inbound gossip download path (`zebrad/src/components/inbound/downloads.rs`, v6.3.0):

1. The attacker sends an `inv` message advertising hash H. The victim's inbound service receives the `AdvertiseBlock` request and queues the hash for download.
2. The download task checks `KnownBlock(H)` (the block is not in the victim's state) and sends `BlocksByHash(H)` through the peer set, which routes to a peer that advertised the hash (`inbound/downloads.rs:297-317`).
3. The attacker serves the forged body. The block hash matches H, so the response is accepted.
4. The coinbase height is read from the unverified body at `inbound/downloads.rs:354-355`.
5. Because the forged height (1) is more than `MAX_BLOCK_REORG_HEIGHT` (1000) behind the tip, the path drops the block at `inbound/downloads.rs:379-391` and discards the advertiser address:
   ```rust
   } else if block_height < min_accepted_height {
       debug!(... "gossiped block height behind the finalized tip: dropped downloaded block");
       Err("gossiped block height behind the finalized tip")
           .map_err(|e| (e.into(), None))?;
   }
   ```
   The `None` discards the advertiser address.
6. This return happens before the verifier is called (`inbound/downloads.rs:394-398`), so consensus never validates the body.

In the inbound error handler (`zebrad/src/components/inbound.rs:334`, v6.3.0), the cleanup requires `Some(advertiser_addr)` to score:

```rust
let Err((err, Some(advertiser_addr))) = result else {
    continue;
};
```

Because the error carries `None`, the `else` branch fires and the error is silently skipped. The peer is never scored, never banned, and remains a preferred download candidate (the failed hash is not marked as missing inventory, so the attacker stays in the advertising-peers set).

A second, independent gap compounds this. Even if the behind-tip error carried `Some(advertiser)`, the value is an untyped string error that downcasts to neither `RouterError` nor `VerifyBlockError` at `inbound.rs:351-357`, so it would still fall through to the unscored branch. Any correct fix therefore needs a typed, scoreable behind-tip error on the inbound path, not only the advertiser address (see Patches).

The sibling sync download path handles this correctly after the v6.3.0 fix (`zebra/src/components/sync/downloads.rs:539-590`): it uses a typed `BehindTipHeightLimit` error that carries the advertiser address, performs a parent-header lookup to distinguish genuinely-old blocks from forged-height rewrites, sets the advertiser (for scoring) only when the parent proves the height inconsistent (`(parent_height + 1) != block_height`), and otherwise drops the block anonymously so honest peers serving legitimately old blocks are not penalized. The inbound path has none of these safeguards.

Full consensus validation would reject the forged body, both because the V5 coinbase auth digest (which includes the scriptSig) changes the `hashAuthDataRoot` committed in the header, and because the coinbase height would not match the block's real height. Neither check is reached, because the height read and the drop occur first.

## Impact

Discovery of the newest canonical block is delayed for as long as the peer set keeps selecting the attacker to serve that hash. The supplying peer is not penalized, so the attacker remains a preferred candidate. For a node that feeds a mining backend, a delayed tip can leave the backend issuing work on an obsolete parent, so hash power spent on that work is at risk of being wasted. The attacker reuses an existing header and performs a cheap body rewrite, with no new proof of work, creating a cost asymmetry against the targeted operator.

## Severity

The finding is unauthenticated and default-config, reliably drops the targeted freshest block when the attacker is selected, and repeats at no cost, but the effect is a transient, self-healing delay rather than a total loss of availability, and there is no state corruption or consensus divergence. This matches the assessment of the sync-path sibling GHSA-g95h-hw6g-pvgv.

## PoC

A runtime PoC was confirmed against Zebra v6.3.0 built with `--features release_max_level_debug` on regtest. The PoC obtains a block the victim has not seen, forges the coinbase scriptSig from the real height to height 1 (OP_1 = 0x51) while leaving the block hash unchanged (ZIP-244), connects to the victim as a P2P peer, advertises the block hash via `inv`, and serves the forged body when the victim requests it. The victim's inbound download path reads coinbase height 1, finds it below `min_accepted_height`, and drops the block with `(error, None)`.

Debug logs from the victim confirm the vulnerable path fired:

```
inbound:download_and_verify{advertiser=Some(v4redacted:61156) hash=63bc1d45...}:
  zebrad::components::inbound::downloads: gossiped block height behind the finalized tip:
  dropped downloaded block
  block_height=Height(1) tip_height=Some(Height(1101)) min_accepted_height=Height(101)
  behind_tip_limit=1000
```

The peer's `misbehavior_score` remained 0 throughout. Ping/pong succeeded after the drop and the connection remained usable, confirming the peer was not banned and could repeat the attack.

## Workarounds

Limited. Peering preferentially with trusted peers reduces exposure to the gossip download race. Mining operators can monitor the age of the parent of issued templates and alert when the tip stops advancing. Neither is a substitute for the fix.

## Credit

Reported by craftsoldier, with a runtime PoC and debug-log confirmation against v6.3.0.

## References

- ZIP-244 (transaction identifiers): https://zips.z.cash/zip-0244
- ZIP-225 (V5 transaction format): https://zips.z.cash/zip-0225
- CWE-354: https://cwe.mitre.org/data/definitions/354.html
- CWE-807: https://cwe.mitre.org/data/definitions/807.html
- Related advisory (sync path sibling, same attack, patched in v6.3.0): GHSA-g95h-hw6g-pvgv
- Related advisory (inbound path, different mechanism, wrong downcast type, patched in v6.3.0): GHSA-8hh2-hrf2-cqf4
- Related advisory (same ZIP-244 property, SentHashes lockout, patched in v6.2.1): GHSA-x93j-mj2f-q338
- Fix PR for the sync path sibling: #11235 (confirmed; a combined PR that fixed GHSA-qhr3, GHSA-g95h on the sync path, and GHSA-8hh2 on the inbound verifier-error path, but did not touch `inbound/downloads.rs`)
- Source (pinned v6.3.0):
  - `zebrad/src/components/inbound/downloads.rs:354-355` (coinbase height read), `:379-391` (behind-tip drop with `None`)
  - `zebrad/src/components/inbound.rs:334` (handler skips `None`), `:351-357` (untyped error not scoreable)
  - `zebrad/src/components/sync/downloads.rs:539-590` (fixed sync path for comparison)
  - `zebra-chain/src/parameters/constants.rs:30` (`MAX_BLOCK_REORG_HEIGHT = 1000`)
  - `zebra-chain/src/transparent/serialize.rs` (coinbase height parsing)
  - `zebra-chain/src/block/hash.rs` (block hash includes equihash solution)

