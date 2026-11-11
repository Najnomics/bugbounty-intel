# GHSA-95m2-vx53-v2jw: Block template omits header and transaction-count size, allowing oversized invalid blocks and wasted mining work

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-95m2-vx53-v2jw |
| CVE | none assigned |
| Severity | low (CVSS 3.7) |
| CWE | n/a |
| Published | 2026-07-17T18:26:23Z |
| Updated | 2026-07-17T18:26:23Z |
| Affected | zebrad 6.0.0 (patched: 6.1.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-95m2-vx53-v2jw |

## Description (verbatim)

# Block template omits header and transaction-count size, allowing oversized invalid blocks and wasted mining work

| Field | Value |
|---|---|
| Severity | Low |
| CVSS 3.1 | AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L (3.7) |
| CWE | CWE-131 (Incorrect Calculation of Buffer Size) / CWE-682 (Incorrect Calculation) |
| Affected versions | through v6.0.0 |
| Patched versions | 6.1.0 |
| Reporter credit | @ebfull (partner disclosure) |
| Fix PR | #10995  |

## Am I affected?

You are affected if you mine with Zebra's block templates (you run `getblocktemplate` or the built-in miner) on an affected version. The bug causes Zebra to occasionally hand a miner a template that, once solved, produces a block larger than the consensus size limit; that solved block is then rejected by every validating node, wasting the proof-of-work. Nodes that only validate (do not mine) are not harmed: oversized blocks are correctly rejected, and there is no consensus divergence.

## Summary

When Zebra builds a block template, its ZIP-317 transaction selector budgets mempool transactions against the full maximum block size, subtracting only the coinbase transaction. It does not reserve space for the serialized block header or the transaction-count field, both of which count toward the maximum block size. On Mainnet and Testnet this omits roughly 1,490 bytes (a ~1,487-byte header plus a 3-byte transaction-count field). If the selected transactions fill that margin, the assembled block exceeds the consensus size limit, so the miner performs proof-of-work on a block that every node (including via `submitblock`) rejects. An attacker able to place valid, selectable transactions in a victim miner's mempool could deliberately shape templates into the affected size range.

## Details

Verified on v6.0.0.

`MAX_BLOCK_BYTES` is 2,000,000 and, per its own definition, is the maximum size of the whole serialized block including the header and transaction count (`zebra-chain/src/block/serialize.rs:22-24`).

The template selector budgets against that full value but reserves only the coinbase:

```rust
// zebra-rpc/src/methods/types/get_block_template/zip317.rs
let mut remaining_block_bytes: usize = MAX_BLOCK_BYTES.try_into().expect("fits in memory");   // :95
// ...
remaining_block_bytes -= fake_coinbase_tx.data.as_ref().len();                                 // :100
```

Nothing between the budget setup and transaction admission reserves space for the header or the transaction-count CompactSize. Because those bytes are part of `MAX_BLOCK_BYTES` (not additional to it), the selector can fill the block with transactions up to a total that, once the ~1,487-byte header and ~3-byte count field are prepended, exceeds 2,000,000 bytes.

The block header size is network-specific: Mainnet and Testnet use the full Equihash(200,9) solution (~1,344 bytes), giving a ~1,487-byte header; regtest uses a much smaller solution. So the amount that must be reserved differs per network.

When such a template is solved and submitted, the oversized block is rejected during bounded deserialization (serialize.rs enforces `MAX_BLOCK_BYTES`), both locally via `submitblock` and by every peer. This is correct rejection behaviour, so there is no consensus divergence; the harm is the wasted proof-of-work and the potential reuse of the same invalid long-poll template until the tip or mempool changes.

## Patches

6.1.0. The fix is to reserve, before admitting the coinbase and mempool transactions, the network-specific serialized block-header size plus the maximum possible transaction-count CompactSize width: initialize the transaction budget to `MAX_BLOCK_BYTES` minus header size minus maximum transaction-count width minus coinbase size. The reservation must use the maximum CompactSize width the transaction count could reach for a full block so it is safe regardless of how many transactions are selected. This is a template-construction fix only and does not change consensus block-size validation, which is already correct. Add boundary tests proving a transaction set exactly filling the safe budget is accepted and one additional byte is rejected.

## Workarounds

Miners can reduce exposure by not relying on Zebra-produced templates at the size boundary, but there is no clean configuration-only workaround. Upgrading once a patch is available is the durable fix. Non-mining nodes require no action.

## Impact

Availability and mining-integrity, scoped to mining. A Zebra miner can be handed a template that yields an oversized, universally-rejected block, wasting that block's proof-of-work and the associated mining revenue, with possible repetition while the same long-poll template is reused. An attacker with valid, selectable transactions spending real UTXOs could deliberately shape a victim miner's templates into the affected size range, turning the latent bug into a bounded griefing vector against miners at the cost of real transaction fees. There is no consensus divergence (oversized blocks are correctly rejected), no crash of other nodes, and no state corruption. The reporter has confirmed the issue would invalidate blocks produced by at least one real mainnet miner.

## Credit

Reported by @ebfull via coordinated disclosure, including the byte-level accounting of the omitted header and transaction-count size, the network-specific header figure, the deliberate-shaping attacker vector, and confirmation against a real mainnet miner.

## References

- `zebra-rpc/src/methods/types/get_block_template/zip317.rs:55,95,100` (the selector budget and the coinbase-only subtraction)
- `zebra-chain/src/block/serialize.rs:22-24` (`MAX_BLOCK_BYTES` includes header and transaction count; bounded deserialization)
- `zebrad/src/components/miner.rs` (built-in miner and long-poll template reuse)
- CWE-131, CWE-682
