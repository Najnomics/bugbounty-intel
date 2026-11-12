# GHSA-cgvq-9xfq-c54j: Besu accepts RLP-wrapped typed transactions in ExecutionPayload block bodies, causing a client-line consensus split

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-cgvq-9xfq-c54j |
| CVE | none assigned |
| Severity | medium |
| CWE | CWE-20, CWE-436 |
| Published | 2026-10-14T00:14:20Z |
| Updated | 2026-10-14T00:14:20Z |
| Affected | org.hyperledger.besu:besu <= 26.7.1 (patched: 26.8.0) |
| Credits | n/a |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-cgvq-9xfq-c54j |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

## Impact

Besu's `TransactionDecoder.decodeOpaqueBytes` — the entry point that decodes each element of the Engine API `ExecutionPayload.transactions` array — accepts a typed transaction whose canonical opaque encoding (`0x02 || rlp(payload)` for an EIP-1559 transaction) has been wrapped one extra time as a generic RLP byte-string (`0xb8<len><canonical bytes>`). The extra wrapper is silently stripped and the inner transaction is decoded into a `Transaction` object identical (same hash) to the one decoded from the canonical bytes.

Because `BodyValidation.transactionsRoot` re-encodes transactions canonically before hashing, a block built from the wrapped bytes derives the **same** `transactionsRoot` and block hash as the canonical block, and Besu imports it as `VALID`. Geth, Reth, and Nethermind reject the wrapped encoding outright as malformed RLP for a typed transaction. Because the consensus layer treats `transactions` as opaque byte-lists and never parses the transaction RLP, a malicious or buggy block proposer — or a builder/relay bug that mutates the payload after `getPayload` — can sign and gossip a block that Besu accepts as canonical while every other major client family rejects it. The result is a **client-line consensus split** affecting Besu nodes.

## Root cause

`decodeOpaqueBytes` fell back to a generic RLP decode whenever the leading byte did not map to a typed-transaction marker (`0x01`–`0x04`) or a legacy list prefix. That fallback (`decodeRLP` → `readBytes`) strips exactly one RLP string-length wrapper and retries type detection on the inner bytes, which then resolve to a legitimate type and decode successfully. The strict, standalone opaque-bytes entry point has no surrounding RLP container, so it should require the top-level byte to be a bare type marker or a genuine legacy-list prefix, rather than reinterpreting an unexpected leading byte as generic RLP.

## Patches

Fixed in Besu **26.8.0**. The strict rejection is scoped to the block-body encoding context: a leading byte that is not a typed-transaction marker or a legacy list prefix is now rejected outright instead of being reinterpreted as generic RLP. The pooled-transaction path used by `eth_sendRawTransaction` keeps the existing leniency, which only affects local acceptance of a slightly malformed raw-transaction submission and does not influence any hash shared across the network (transactions are normalized canonically before further use or propagation).

## Workarounds

None. Upgrade to Besu 26.8.0 or later.

## References

PR: #11103 

Reported by an external security researcher through the Besu bug bounty program.

