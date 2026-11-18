# GHSA-hj54-2mfv-4xg8: One-block balance-query amplification can OOM Zebra through public wallet requests

| Field | Value |
| --- | --- |
| Repo | ZcashFoundation/zebra |
| GHSA | GHSA-hj54-2mfv-4xg8 |
| CVE | none assigned |
| Severity | high (CVSS 7.5) |
| CWE | CWE-400 |
| Published | 2026-11-17T09:38:21Z |
| Updated | 2026-11-17T09:38:21Z |
| Affected | zebrad < 7.1.0 (patched: 7.1.0); zebra-state < 17.0.0 (patched: 17.0.0) |
| Advisory URL | https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-hj54-2mfv-4xg8 |

## Description (verbatim)

## Am I affected?

You are affected if you run zebrad 7.0.0 or earlier, or use zebra-state earlier than 17.0.0, and untrusted clients can reach one of these interfaces:

- **The JSON-RPC server**, directly or through a wallet service such as lightwalletd that forwards wallet requests to it. The affected methods are `getaddressbalance`, `getaddressutxos`, and `getaddresstxids`. They are always available when the RPC server is enabled.
- **The lightwalletd-compatible gRPC server** (`rpc.lightwalletd_listen_addr`), through `GetTaddressBalance` and the related address calls. This server has no authentication, and cookie authentication does not apply to it.

Both servers are disabled by default: `rpc.listen_addr` and `rpc.lightwalletd_listen_addr` have no default value, so Zebra binds no RPC port unless you set one. The documented examples use `127.0.0.1`. Cookie authentication is on by default for JSON-RPC, but it does not protect a node whose wallet service holds the cookie and accepts public requests. The example `docker/docker-compose.lwd.yml` binds RPC to `0.0.0.0:8232`, turns cookie authentication off, and publishes the port.

A node with both servers disabled, or reachable only by trusted clients, is not affected.

## Summary

Anyone who can send wallet balance requests to a Zebra node can make it run out of memory and be killed. Each transparent address balance request makes a full copy of the node's recent, non-finalized chain data, even for an address with no recent activity. A recent block with many transparent outputs makes each copy large, so a burst of concurrent balance requests can exhaust memory. The node recovers on restart, but the same requests can kill it again while that block is still in the non-finalized chain.

## Details

Line references are pinned to [v7.0.0](https://github.com/ZcashFoundation/zebra/tree/v7.0.0).

`getaddressbalance` ([`zebra-rpc/src/methods.rs:1483-1495`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-rpc/src/methods.rs#L1483-L1495)) and the gRPC `GetTaddressBalance` handler ([`zebra-rpc/src/lightwalletd/methods.rs:274-283`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-rpc/src/lightwalletd/methods.rs#L274-L283)) send `ReadRequest::AddressBalance` to the read state service. It passes the shared `Arc<Chain>` handle for the current best non-finalized chain to `transparent_balance` ([`zebra-state/src/service.rs:1765-1769`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/service.rs#L1765-L1769)).

`chain_transparent_balance_change` calls `Arc::make_mut` on that handle before it checks whether the chain overlaps the finalized state ([`zebra-state/src/service/read/address/balance.rs:98-134`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/service/read/address/balance.rs#L98-L134)):

```rust
let chain = Arc::make_mut(&mut chain);
```

The state keeps its own reference to the chain, so `make_mut` always clones it. A `Chain` owns its indexes in plain maps: transaction locations, created and spent UTXOs, nullifiers, and the per-address transparent transfers ([`zebra-state/src/service/non_finalized_state/chain.rs:48-252`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/service/non_finalized_state/chain.rs#L48-L252)). The mutable copy is only needed when the chain root is below the finalized tip, so that `pop_root` can drop the overlapping blocks. In the usual case there is no overlap, but every request still pays for the full copy and then only looks up the requested addresses.

The non-finalized chain can hold up to 1,000 blocks, so a block with many transparent outputs stays in every copy for a long time. Requests run concurrently, and each holds its own copy until it finishes.

`getaddressutxos` and `getaddresstxids` have a smaller version of the same problem. For the requested addresses, they collect every recent UTXO or transaction ID from the non-finalized chain, and apply the `max_entries` limit only after collecting ([`zebra-state/src/service/read/address/utxo.rs:277-432`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/service/read/address/utxo.rs#L277-L432), [`tx_id.rs:123-273`](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/service/read/address/tx_id.rs#L123-L273)).

## Impact

A client that can send balance requests can stop the node through memory exhaustion. The node stops syncing, relaying, and serving RPC until it restarts.

The reporter showed this on the documented minimum hardware, 2 CPUs and 4 GB of RAM, with zebrad 6.4.2 behind Go lightwalletd 0.5.4. One consensus-valid block held a 1.76 MB transaction with 55,000 transparent outputs. Concurrent one-address balance requests over a single gRPC connection then got the Zebra process killed for running out of memory, and balance requests from an unrelated wallet timed out. The same load against a matching chain without that block left the node running.

To make each copy large, an attacker has to get a transaction with many transparent outputs mined and pay its fee. The test transaction paid about 2.59 ZEC. Recent chain data from ordinary activity also counts toward each copy.

There is no consensus impact, no state corruption, and no effect on funds.

## Patches

Fixed in zebrad 7.1.0 and zebra-state 17.0.0. Address balance, UTXO, and transaction ID requests no longer copy the non-finalized chain:

- `ReadRequest::AddressBalance` reads the requested addresses' balance changes above the finalized tip directly from the shared chain, through `Chain::partial_transparent_balance_change_from`, instead of cloning the chain and popping its root blocks.
- `ReadRequest::UtxosByAddresses` and `ReadRequest::TransactionIdsByAddresses` collect at most `max_entries` non-finalized UTXOs and transaction IDs, instead of copying all the recent UTXOs and transactions of the requested addresses on every request.

Upgrade to 7.1.0.

## Workarounds

If you cannot upgrade yet:

- Do not expose the JSON-RPC port or the lightwalletd gRPC port to untrusted clients. Bind them to a loopback or private address.
- If you run a public wallet service in front of Zebra, put it behind rate limits on balance and address requests. This reduces the exposure but does not remove it.
- Run zebrad under a supervisor that restarts it on failure, such as systemd `Restart=on-failure` or a container restart policy. This shortens outages but does not prevent them.

## Credit

Reported by @saxenism, with an end-to-end reproduction on the documented minimum hardware and a matched control.

## References

- CWE-400: Uncontrolled Resource Consumption.
- Zebra 7.1.0 release notes: https://github.com/ZcashFoundation/zebra/releases/tag/v7.1.0
- GHSA-j8gf-c4rj-6jv5: memory exhaustion through per-chain copies of the non-finalized output index, fixed in the same release.
- [`zebra-state/src/service/read/address/balance.rs` at v7.0.0](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-state/src/service/read/address/balance.rs)
- [`zebra-rpc/src/config/rpc.rs` at v7.0.0](https://github.com/ZcashFoundation/zebra/blob/v7.0.0/zebra-rpc/src/config/rpc.rs)

