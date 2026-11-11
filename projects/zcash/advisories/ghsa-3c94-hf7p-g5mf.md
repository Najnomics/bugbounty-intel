# GHSA-3c94-hf7p-g5mf: Same-hash block body forces full proof verification with no peer penalty

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-3c94-hf7p-g5mf |
| CVE | none assigned |
| Severity | medium (CVSS 5.3) |
| CWE | n/a |
| Published | 2026-09-28T08:07:49Z |
| Updated | 2026-09-28T08:07:49Z |
| Affected | zebrad <=6.3.0 (patched: 6.4.2) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-3c94-hf7p-g5mf |

## Description (verbatim)

| Field | Content |
|---|---|
| Severity | Medium |
| CVSS 3.1 | Medium 5.3 `AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L` |
| CWE | CWE-400 (Uncontrolled Resource Consumption), root cause CWE-345 (Insufficient Verification of Data Authenticity) |
| Affected versions | <6.4.2 |
| Reporter credit | ouicate |
| GHSA | GHSA-3c94-hf7p-g5mf |

## Am I affected

You are affected if all of the following hold:

- You run a `zebrad` node reachable on the P2P network (the default listen configuration is sufficient; no RPC, mining, or authentication is required).
- Your node is on a network past NU5, and most acutely on NU6.3 (Ironwood), where each wasted verification also runs an Ironwood Halo2 batch.
- Your node accepts inbound block gossip or is syncing near or above the mandatory checkpoint (the effect is largest for a node catching up above the last checkpoint).

You are not affected in a way that changes chain state: there is no consensus split, no inflation, no monetary-base change, and no nullifier or pool corruption. The impact is availability only.

## Summary

An unauthenticated peer can make a `zebrad` node spend a full block verification, including the Sapling, Orchard, and (at NU6.3) Ironwood proof batches, on a block body that can never commit, and do so without the peer being scored or banned. After NU5 the block header hash and the Merkle root commit only to transaction txids; authorizing data (transparent `scriptSig`, coinbase extra-data, shielded authorizations) is committed separately in `hashBlockCommitments` and is checked only in later contextual validation. An attacker takes any honest block, flips one authorizing-only byte (for example a coinbase `scriptSig` byte), and produces a different body with the same header hash and the same Merkle root. Zebra accepts the downloaded body because its header hash matches an outstanding request, runs and awaits the entire transaction verifier, and only then rejects the body in contextual validation for an authorizing-data mismatch. On the block-sync path a single won download race additionally cancels the whole sync round and idles the syncer for 67 seconds. The effect is transient and clears when the attacker stops.

## Details

Root cause: after NU5 the block hash and Merkle root do not bind authorizing data, yet Zebra uses the header hash as both the download identity and the semantic-binding identity, and defers the authorizing-data commitment check to a stage that runs after the expensive work.

Verified code path (re-pinned to v6.3.0):

1. Authorizing data is excluded from the txid by construction. `txid_v5` computes the ZIP-244 txid via librustzcash (`zebra-chain/src/transaction/txid.rs:46-50`), and `txid_v6` delegates to it (`:54`). Flipping a coinbase `scriptSig` byte changes `auth_digest` (hence `auth_data_root` and `hashBlockCommitments`) but leaves the txid, the Merkle root, and the header hash unchanged.

2. The download layer accepts a body by header hash only. `pending_hashes.remove(&block.hash())` gates acceptance (`zebra-network/src/peer/connection.rs:308`), and `Block::hash()` is header-only (`zebra-chain/src/block.rs:282-284`, `zebra-chain/src/block/header.rs:139-140`).

3. A near-tip block routes to the full semantic verifier. Blocks at or below `max_checkpoint_height` take the hash-only checkpoint verifier; everything above (the tip region this targets) takes the full block verifier (`zebra-consensus/src/router.rs:210-215`).

4. The semantic verifier binds the header to the body over txids, so the forgery passes this gate. `check::merkle_root_validity` is computed over `transaction_hashes` (`zebra-consensus/src/block.rs:255-262`); a coinbase `scriptSig` mutation changes no txid.

5. The verifier runs and awaits every proof before touching the state. All transactions are dispatched and fully awaited (`zebra-consensus/src/block.rs:318`) before `CommitSemanticallyVerifiedBlock` (`:390`). For a V6 transaction this verifies the Sapling, Orchard v6, and Ironwood bundles (`zebra-consensus/src/transaction.rs:1138-1142`). The verifier holds no authorizing-data check by design; the doc comment states the authorizing data root is checked during contextual validation (`zebra-consensus/src/transaction.rs:208-209`).

6. The forgery is caught only in contextual validation, after all the expensive work. The `hashBlockCommitments` comparison lives in `zebra-state/src/service/check.rs:184-215` and returns `InvalidBlockCommitment(InvalidChainHistoryBlockTxAuthCommitment)` on mismatch; it is invoked from `validate_and_update_parallel` (`zebra-state/src/service/non_finalized_state.rs:624`), which runs only after the commit request.

Aggravating factor A: no cache absorbs the wasted work. The block transaction verifier holds no mempool handle and memoizes nothing across requests, so every transaction's proofs are re-verified from scratch even if the honest body's identical transactions were already verified.

Aggravating factor B: the serving peer is not scored. The rejection surfaces as `CommitBlockError`, whose `misbehavior_score()` returns a hard-coded `0` (`zebra-state/src/error.rs:129-131`, with a corroborating test at `:540-553`). The router forwards that score unchanged (`zebra-consensus/src/router.rs:150-151`; `zebra-consensus/src/block.rs:115`), and the sync path only reports a score when it is non-zero (`zebrad/src/components/sync.rs:1207-1215`), so this rejection falls through to the unscored arm (`:1244`). The peer that served the forged body is never scored or banned. This is a distinct rejection arm from the two adjacent paths the tree already handles: `BehindTipHeightLimit` scores 100 for a parent-proven coinbase-height rewrite (GHSA-g95h, `zebrad/src/components/sync.rs:1230-1234`), and `AboveLookaheadHeightLimit` deliberately stays unscored (GHSA-qhr3, `:1237-1244`).

Aggravating factor C: on the block-sync path a won race restarts the whole sync round. A same-hash forged body for a real requested hash fails as a non-duplicate `Invalid`, so `should_restart_sync` returns `true` for it (only `is_duplicate_request()` is excluded; everything else falls to the default arm, `zebrad/src/components/sync.rs:1350-1431`). `try_to_sync` then returns an error, the loop calls `cancel_all()`, and the node sleeps `SYNC_RESTART_DELAY = 67 s` before the next `obtain_tips` (`:224`, `:586-604`). Inbound gossip failures do not trigger this restart.

What bounds the blast radius: a per-IP one-in-flight download cap (`in_flight_ips`, `zebrad/src/components/inbound/downloads.rs:131`); same-hash de-duplication; the near-tip lookahead and reorg window (lookahead constant at `:32`); a `KnownBlock` short-circuit once the honest body commits; and a probabilistic download race, since a single-hash `getdata` is routed to a random less-loaded peer via power-of-two-choices (`zebra-network/src/peer_set/set.rs:908-925`), so the attacker wins roughly one race in N. Below the mandatory checkpoint the checkpoint verifier runs no Halo2 batches, so the proof cost and the factor-C restart both bite hardest in the post-checkpoint window.

## Impact

A well-positioned unauthenticated peer that wins download races forces the victim to spend full block-verification capacity (including Ironwood Halo2 at NU6.3) on bodies that can never commit, holding the node behind the tip for the duration of the attack, with no peer penalty. On the block-sync path each won race additionally idles the syncer for 67 seconds. The most damaging scenario is a node catching up above the mandatory checkpoint, where many hashes are forgeable and invalid bodies are deliberately not re-requested.

What is not affected: the forged body is never committed. There is no inflation, monetary-base change, nullifier or pool corruption, or consensus split. The effect is transient and clears when the attacker stops.

## Workarounds

No configuration change removes the vector on an exposed node. Operators concerned about a node catching up above the checkpoint can limit inbound exposure at the firewall and prefer trusted peers; these reduce, but do not eliminate, the surface.

## Credit

ouicate, for the finding, the control-flow analysis, and the same-hash construction. 

## References

- ZIP-244 (transaction identifier and authorizing data)
- CWE-400: https://cwe.mitre.org/data/definitions/400.html
- CWE-345: https://cwe.mitre.org/data/definitions/345.html
- Verified source (v6.3.0):
  - https://github.com/ZcashFoundation/zebra/blob/v6.3.0/zebra-network/src/peer/connection.rs#L308
  - https://github.com/ZcashFoundation/zebra/blob/v6.3.0/zebra-consensus/src/router.rs#L210-L215
  - https://github.com/ZcashFoundation/zebra/blob/v6.3.0/zebra-consensus/src/block.rs#L255-L262
  - https://github.com/ZcashFoundation/zebra/blob/v6.3.0/zebra-consensus/src/transaction.rs#L1138-L1142
  - https://github.com/ZcashFoundation/zebra/blob/v6.3.0/zebra-state/src/service/check.rs#L184-L215
  - https://github.com/ZcashFoundation/zebra/blob/v6.3.0/zebra-state/src/error.rs#L129-L131
  - https://github.com/ZcashFoundation/zebra/blob/v6.3.0/zebrad/src/components/sync.rs#L1207-L1244
  - https://github.com/ZcashFoundation/zebra/blob/v6.3.0/zebrad/src/components/sync.rs#L1350-L1431
