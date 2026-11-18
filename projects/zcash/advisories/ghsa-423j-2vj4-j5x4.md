# GHSA-423j-2vj4-j5x4: The mempool dispatches transactions above the standard sigop limit to script verification

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-423j-2vj4-j5x4 |
| CVE | none assigned |
| Severity | medium (CVSS 5.3) |
| CWE | CWE-400, CWE-407, CWE-696 |
| Published | 2026-11-17T10:04:54Z |
| Updated | 2026-11-17T10:04:54Z |
| Affected | zebrad >= 6.0.0, < 7.1.0 (patched: 7.1.0); zebra-consensus < 19.0.0 (patched: 19.0.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-423j-2vj4-j5x4 |

## Description (verbatim)

## Am I affected?

You are affected if all of the following hold:

- You run zebrad 6.0.0 or later, including 7.0.0, on Mainnet or Testnet.
- Your node accepts inbound peer connections or relays mempool transactions (the default configuration).

There is no configuration that disables the affected code path. The effect is much larger on releases before 7.0.0, where the signature hash cost of GHSA-j4cw-58mj-7w6v applied as well; upgrade to 7.0.0 first.

## Summary

zebrad 6.0.0 added a standardness gate that runs before script verification so that transactions with non-standard inputs are rejected cheaply (GHSA-84j3-rw4c-gqmj). That gate bounds each P2SH input's redeem script to 15 signature operations, but it does not bound the transaction's total. The per-transaction standard limit of 4,000 signature operations is still applied only after script verification has completed, when the transaction is inserted into mempool storage. A peer can therefore send a transaction that passes the gate with up to about 225,000 signature operations (15 per input over about 15,000 inputs in 2 MB), and Zebra verifies every one of them before rejecting the transaction as non-standard. zcashd applied the total limit before script checks.

On its own this makes the mempool's per-transaction verification cost about 50 times the standard limit: with reusable valid signatures the cost is real signature verification, on the order of ten to twenty CPU-seconds per 2 MB transaction on 7.0.0. On releases before 7.0.0 each of those signature checks also recomputed two transaction-wide digests, and the reporter measured about 1,800 CPU-seconds for one transaction; that cost is fixed in 7.0.0 and published as GHSA-j4cw-58mj-7w6v.

Because every script in the transaction succeeds and the rejection is a standardness rejection, no misbehavior score is applied to the peer; the 7.0.0 scoring of failing scripts (GHSA-jq45-ghw5-v37x) does not apply here. The verification timeout also applies no score and does not record the transaction in the rejection cache, and the rejection cache is keyed by exact transaction ID, so a one-byte change produces a fresh transaction. The same peer can repeat the transaction indefinitely at the per-peer concurrency limit.

## Impact

Availability only. One unauthenticated peer, holding about 15,000 small P2SH outputs that are never spent (under 0.3 ZEC, reusable), can keep a node's verification thread pool busy with signature checks that a correctly ordered policy check would have skipped. Verification work shares the Rayon pool with block script checks and shielded batch verification, so block verification slows while the transactions keep arriving; peer message handling and RPC continue. The effect scales down with core count and clears when the transactions stop. No theft, consensus divergence, state corruption, or crash.

Script jobs already queued when a transaction is rejected still run to completion; that is tracked separately as a public issue (#11888).

## Patches

Fixed in zebrad 7.1.0 (zebra-consensus 19.0.0). The mempool transaction verifier now counts a transaction's legacy and P2SH signature operations and rejects it as non-standard above `MAX_STANDARD_TX_SIGOPS` (4,000) before it dispatches script verification. This is a mempool policy change only: block validation and the consensus sigop accounting are unchanged. Upgrade to 7.1.0.

## Workarounds

None verified. Reducing `max_connections_per_ip` does not help (the default is already 1). Operators with more cores experience a smaller effect. Upgrading to 7.0.0 removes the quadratic signature hash cost that made this ordering expensive, but not the ordering itself.

## Credit

Reported by @janneh2000, whose report also carried the production-verifier measurement, the Rayon queueing probe and the block-level variant credited on GHSA-j4cw-58mj-7w6v, and the coinbase-maturity regression published as GHSA-7jp4-mq53-4cvq.

Independent finders: @john-lawniczak (standard-multisig shape with no per-input bound, the measured interpreter cost, the fix shape and integration test), @Maakai123 (the block-verification delay measurement and attacker-cost analysis), @sangsoo-osec (output-standardness and spend-conflict arms, the shielded shape), and Filipe Casal at Trail of Bits through the Patch the Planet program.

## References

- GHSA-84j3-rw4c-gqmj (the standardness gate whose scope this report extends)
- GHSA-j4cw-58mj-7w6v (the signature hash cost; fixed in 7.0.0)
- GHSA-jq45-ghw5-v37x (scoring of failing scripts; fixed in 7.0.0)
- #11888 (queued script jobs after rejection)
- ZIP 317 (mempool fee policy)
- CWE-400, CWE-696
- zebrad v7.0.0: `zebra-consensus/src/transaction.rs:530` (gate), `:543` (script verification dispatched), `:568` (awaited), `:572` (sigop count computed only afterwards); `zebra-consensus/src/transaction/check.rs:659` (`MAX_P2SH_SIGOPS` = 15), `:742` (`are_inputs_standard`), `:798` (per-input count, not summed), `:830` (gate); `zebrad/src/components/mempool/storage.rs:298-314` (per-transaction limit at insert), `storage/policy.rs:21` (`MAX_STANDARD_TX_SIGOPS` = 4000)
- zcashd v6.11.0 `src/main.cpp:1903` (total sigop limit before `ContextualCheckInputs` at `:1982`)

