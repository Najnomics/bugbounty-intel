# GHSA-7jp4-mq53-4cvq: Mempool coinbase-maturity check does quadratic work per transaction, letting one peer pin verification threads

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-7jp4-mq53-4cvq |
| CVE | none assigned |
| Severity | high (CVSS 7.5) |
| CWE | CWE-400, CWE-407 |
| Published | 2026-10-22T14:55:09Z |
| Updated | 2026-10-22T14:55:09Z |
| Affected | zebrad >= 6.4.0, < 7.0.0 (patched: 7.0.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-7jp4-mq53-4cvq |

## Description (verbatim)

# Mempool coinbase-maturity check does quadratic work per transaction, letting one peer pin verification threads

| Field | Value |
|---|---|
| Severity | High (7.5) |
| CVSS 3.1 vector | `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H` (7.5) |
| CWE | CWE-407 (Inefficient Algorithmic Complexity); CWE-400 (Uncontrolled Resource Consumption) |
| Affected versions | zebrad 6.4.0, 6.4.1, 6.4.2 and 7.0.0-rc.0 (introduced by the `Transaction` newtype refactor, PR #10461, commit 8b91154) |
| Not affected | zebrad 6.3.0 and earlier; zebrad 7.0.0 and later |
| Patched version | zebrad 7.0.0 |
| Reported by | @janneh2000 |

## Am I affected?

You are affected if all of the following hold:

- You run zebrad 6.4.0, 6.4.1, 6.4.2 or 7.0.0-rc.0.
- Your node accepts peer connections or makes outbound connections (the default on every network).

No configuration setting changes exposure. Nodes on zebrad 7.0.0 or later, or on 6.3.0 or earlier, are not affected.

## Summary

Any connected peer can make a Zebra node spend tens of seconds of CPU on a single transaction by sending a transaction with many transparent inputs and many transparent outputs. The mempool's coinbase-maturity check calls `Transaction::coinbase_spend_restriction()` once per spent outpoint, and in the affected releases that call rebuilds and clones the transaction's whole output list each time, so the check costs inputs times outputs. The transaction needs no valid signatures and no attacker funds: it can spend any existing unspent outputs with empty scriptSigs, because the maturity check runs before the standardness check that eventually rejects it. The rejection is a policy rejection, which carries no misbehavior score, so the peer is not banned and can repeat the transaction as often as it likes.

## Details

The newtype refactor replaced the borrowed output slice with an allocating accessor:

- `zebra-chain/src/transaction.rs:201-207` (v6.4.2): `Transaction::outputs()` collects a new `Vec<transparent::Output>` and copies every output script on each call.
- `zebra-chain/src/transaction.rs:746-756`: `coinbase_spend_restriction()` evaluates `self.outputs().is_empty()` unconditionally (it is the left operand of `||`).
- `zebra-consensus/src/transaction/check.rs:637-647`: `tx_transparent_coinbase_spends_maturity()` calls `coinbase_spend_restriction()` inside the per-spend loop, although its result depends only on the transaction, network and height.

In the mempool verifier (`zebra-consensus/src/transaction.rs:513`) this check runs after the UTXO lookups and before `mempool_standard_input_scripts` (`:519`), so a transaction whose inputs carry empty scriptSigs reaches the loop and pays its full cost before being rejected as `NonStandardInputs`. That error maps to a misbehavior score of 0 (`zebra-consensus/src/error.rs:433-436`). The loop is synchronous inside the spawned verification task (`zebrad/src/components/mempool/downloads.rs:498-499`), so the 73 second verification timeout cannot interrupt it.

On zebrad 6.3.0 `outputs()` returned `&[transparent::Output]`, so the same loop cost O(inputs).

The same per-spend call existed on the block validation path (`zebra-state/src/service/check/utxo.rs:73`). Reaching it requires a mined block, so it is a smaller concern and was fixed together with the mempool path.

## Impact

A single peer can hold a verification worker for roughly 20 seconds per transaction (reporter measurement: 24,000 inputs and 111,000 outputs in about 1.98 MB, on a 4-core machine) and can queue up to five such transactions at once from one connection. On a node with four or five cores this occupies the whole async runtime, so block verification, peer message handling and sync stop progressing for as long as the attack continues. The node recovers when the attack stops. No consensus rule is affected, no funds are at risk, and nothing is written to disk.

## Patches

Fixed in zebrad 7.0.0 by commit 08743d669. `Transaction::has_transparent_inputs()` and `has_transparent_outputs()` now read the transparent bundle's lengths instead of rebuilding the input or output vector, `coinbase_spend_restriction()` uses the non-allocating check, and both the mempool and block-commit maturity loops compute the restriction once per transaction. The per-signature SIGHASH_SINGLE check in `zebra-script` was changed the same way. There is no fix on the 6.4.x line; operators on 6.4.x should upgrade to 7.0.0.

## Workarounds

None. Limiting inbound connections reduces the number of peers that can send the transaction but does not remove exposure, since any connected peer, inbound or outbound, can send it. Upgrade to zebrad 7.0.0.

## Credit

Thanks to @janneh2000 for reporting this with a reproduction against the production mempool verifier.

## References

- CWE-407: https://cwe.mitre.org/data/definitions/407.html
- Fix commit: https://github.com/ZcashFoundation/zebra/commit/08743d669b33a19bce2a5d54001bd468c03a196e
- Zebra 7.0.0 release: https://github.com/ZcashFoundation/zebra/releases/tag/v7.0.0
- PR #10461 (the refactor that introduced the allocating accessor): https://github.com/ZcashFoundation/zebra/pull/10461
- `outputs()` at v6.4.2: https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-chain/src/transaction.rs#L201-L207
- `coinbase_spend_restriction()` at v6.4.2: https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-chain/src/transaction.rs#L746-L756
- Maturity loop at v6.4.2: https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-consensus/src/transaction/check.rs#L637-L647
- Mempool check ordering at v6.4.2: https://github.com/ZcashFoundation/zebra/blob/v6.4.2/zebra-consensus/src/transaction.rs#L513-L519

