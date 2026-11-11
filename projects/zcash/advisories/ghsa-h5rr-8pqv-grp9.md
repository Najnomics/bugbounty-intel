# GHSA-h5rr-8pqv-grp9: Unauthenticated peer can crash zebrad by sending a version 6 transaction whose consensus branch predates NU6.3

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-h5rr-8pqv-grp9 |
| CVE | none assigned |
| Severity | high (CVSS 7.5) |
| CWE | n/a |
| Published | 2026-09-25T20:02:29Z |
| Updated | 2026-09-25T20:02:29Z |
| Affected | zebrad >= 6.4.0, < 6.4.2 (patched: 6.4.2) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-h5rr-8pqv-grp9 |

## Description (verbatim)

## Am I affected

You are affected if all of the following hold:

- You run zebrad v6.4.0 or v6.4.1. Earlier releases reject the triggering transaction at parse time and are not affected.
- Your node accepts inbound peer connections (the default on a listening node).
- No special configuration is required. The trigger is on the default P2P surface.

This does not require authentication, a completed handshake, or any non-default configuration. It affects mainnet nodes.

## Summary

An unauthenticated peer can abort a zebrad process by sending a single `tx` message whose body is a version 6 transaction carrying a consensus branch ID from before NU6.3 (for example NU6.1, `0x4DEC4DF0`). Zebra parses the transaction (the parser does not check that the transaction version is valid for the branch), then computes its serialized size while building the in-memory `UnminedTx`. The size computation re-serializes the transaction, the v6 writer refuses to emit a bundle whose version is not `orchard_v3` or `ironwood_v3`, and Zebra treats that re-serialization as infallible. The resulting error trips an `.expect`, and because the workspace builds with `panic = "abort"`, the whole node terminates. Any peer can repeat this immediately after restart.

## Details

Root cause: a read/write asymmetry in the pinned `zcash_primitives` transaction codec, which Zebra converts into a process abort by treating re-serialization of an already-parsed transaction as infallible.

The reproducing input decodes as: wire command `tx`; body is a v6 transaction (header `0x80000006`, version group ID `0xD884B698`) with consensus branch ID `0x4DEC4DF0` (NU6.1), no transparent inputs or outputs, no Sapling data, one Orchard-slot action with an empty proof, and no Ironwood actions.

The code path, pinned to v6.4.1:

1. Entry: `Codec::decode` dispatches a `tx` body to `read_tx` with no handshake gating (`zebra-network/src/protocol/external/codec.rs:475`, `:742`). The pre-handshake body cap is 1024 bytes (`MAX_HANDSHAKE_BODY_LEN`, `codec.rs:48`); the malicious body is 1016 bytes, so it is reachable before a handshake completes.

2. Parse: `read_tx` calls into `Transaction::zcash_deserialize` (`zebra-chain/src/transaction.rs:876`), which runs `deserialize_and_check` (`transaction.rs:886`) and then `zcash_primitives 0.30.0 Transaction::read` (`transaction/mod.rs:735`). `read` dispatches to `read_v6` (`mod.rs:878`). `read_v6` does not call `valid_in_branch`, so a v6 transaction under a pre-NU6.3 branch parses. Under NU6.1, `bundle_version_for_branch` selects `orchard_insecure_v1` for the Orchard pool, and because that revision does not enforce proof size, `read_bundle` accepts the bundle with its empty proof (`transaction/components/orchard.rs:92`, `:156`, `:216`). Zebra's `deserialize_and_check` adds coinbase and V4-balance checks but nothing that rejects this transaction.

3. Crash: `read_tx` builds `UnminedTx::from(Arc<Transaction>)` (`zebra-chain/src/transaction/unmined.rs:247`), which first calls `zcash_serialized_size()`. That method serializes into a counting writer and unwraps the result: `.expect("writer should never fail")` (`zebra-chain/src/serialization/zcash_serialize.rs:49`). The serialize path reaches `write_v6` (`zcash_primitives transaction/mod.rs:1034`) and `write_v6_bundle`, whose `check_v6_bundle_version` (`components/orchard.rs:196`, called at `:370`) returns an `Err` for any bundle version other than `orchard_v3` or `ironwood_v3`. The Orchard bundle read under NU6.1 has version `orchard_insecure_v1`, so the write fails, the `Err` trips the `.expect`, and the process aborts under `panic = "abort"` (`Cargo.toml:191`, `:312`).

The reported ASAN crash state (`UnminedTx` under two `Codec` frames) matches this path.

The underlying asymmetry is upstream: `zcash_primitives Transaction::read` accepts a v6 transaction under a branch whose bundle version its own `write_v6_bundle` will not emit. Zebra makes it fatal by assuming that re-serializing a parsed transaction cannot fail.

Regression history: v6.0.0 through v6.3.0 are not affected. Their v6 parse arm rejects any v6 transaction whose consensus branch ID predates NU6.3 at the wire layer (`zebra-chain/src/transaction/serialize.rs:1155-1159` at v6.3.0) and additionally round-trips the parsed transaction through librustzcash as a fail-closed guard. Both checks were removed by commit `8b91154` ("refactor(chain)!: replace the Transaction enum with a zcash_primitives newtype wrapper"), which delegates parsing to `zcash_primitives::Transaction::read` and first ships in v6.4.0. Neither `deserialize_and_check` nor the upstream `read_v6` re-applies the version/branch check, so the guard that previously blocked this input is absent on v6.4.0 and v6.4.1.

## Impact

Remote, unauthenticated, deterministic denial of service. One small `tx` frame from any peer terminates the node. Recovery requires a restart, and the node can be crashed again immediately, so a peer can hold a node down. No consensus divergence, funds impact, or information disclosure: availability only.

## Patches

TBD. Recommended fix shape (Zebra side, the immediate and scope-contained fix): restore the parse-time version/branch check in `deserialize_and_check`. A v6 transaction whose consensus branch ID is not one under which v6 is valid (`valid_in_branch` is false, that is, anything before NU6.3) can never be consensus-valid, so rejecting it during deserialization changes no valid transaction or block. The same check ran in production from v6.0.0 through v6.3.0 without incident. This closes the serialize-path abort and the sibling txid/auth-digest abort tracked in issue #11162 at the same site.

Recommended fix shape (upstream): `zcash_primitives read_v6` should reject bundle versions that `write_v6_bundle` refuses to emit, so read and write agree. File with librustzcash.

Hardening: audit every infallible re-serialization of a parsed, untrusted transaction. At minimum `zcash_serialized_size` (`.expect("writer should never fail")`) and `SerializedTransaction::from` (`.expect("Writing to a `Vec` should never fail")`, `zebra-chain/src/transaction/serialize.rs`).

## Workarounds

No configuration-only workaround removes the trigger, because it is on the default P2P surface before authentication. Restricting inbound peers to a trusted set reduces exposure but does not eliminate it.

## Credit

Originally reported by Google OSS-Fuzz via the `p2p_message_parse` fuzz target (issue 565699866, testcase 5494839396073472) on https://github.com/ZcashFoundation/zebra/commit/7c64a8419388dd72664a19a70aed66e84f3e2d5b  independently re-discovered by @v12security and @SphereDonout once it was included in zebra 6.4.0.

## References

- ZIP-230 / NU6.3 (Ironwood) transaction format: https://zips.z.cash/
- CWE-617: https://cwe.mitre.org/data/definitions/617.html
- CWE-248: https://cwe.mitre.org/data/definitions/248.html
- Related public engineering issue (txid/auth-digest sibling path): ZcashFoundation/zebra#11162
- Codec dispatch: https://github.com/ZcashFoundation/zebra/blob/v6.4.1/zebra-network/src/protocol/external/codec.rs
- UnminedTx construction: https://github.com/ZcashFoundation/zebra/blob/v6.4.1/zebra-chain/src/transaction/unmined.rs
- Serialized-size expect: https://github.com/ZcashFoundation/zebra/blob/v6.4.1/zebra-chain/src/serialization/zcash_serialize.rs

