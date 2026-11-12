# GHSA-xg9p-226c-vxvw: Bonsai parallel block processor retains transaction futures after block rejection, causing unbounded memory growth and node outage

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-xg9p-226c-vxvw |
| CVE | none assigned |
| Severity | high |
| CWE | CWE-400, CWE-401 |
| Published | 2026-10-02T05:57:01Z |
| Updated | 2026-10-02T05:57:01Z |
| Affected | org.hyperledger.besu:besu <= 26.7.1 (patched: 26.8.0) |
| Credits | n/a |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-xg9p-226c-vxvw |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

## Summary

Besu's Bonsai parallel transaction processor submits all transactions in a block speculatively before validity is known. When the sequential fallback rejects the block at transaction 0 (e.g. nonce-invalid), the futures for all remaining transactions continue executing and hold references, causing unbounded memory growth until the node dies. The node does not recover.

## Details

`ParallelBlockTransactionProcessor.runAsyncBlock` allocates a result array and submits all transactions (up to the EIP-7825 block maximum of 16,384) before any validity check. When sequential processing fails at index 0, it returns `INVALID` with no block-level cancel. The per-index cleanup in `OptimisticConcurrentTransactionProcessor.removeFuture` is only reached for indices that sequential processing actually visits — indices 1 through 16,383 are never visited, so their futures are never cancelled. The workers keep executing expensive transactions against the pre-block state and their results remain referenced until the JVM exhausts memory.

Affected code:
- `ethereum/core/src/main/java/org/hyperledger/besu/ethereum/mainnet/parallelization/ParallelBlockTransactionProcessor.java` — `runAsyncBlock` (L37–L77)
- `ethereum/core/src/main/java/org/hyperledger/besu/ethereum/mainnet/parallelization/OptimisticConcurrentTransactionProcessor.java` — `getProcessingResult`/`removeFuture` (L192–L204)
- `ethereum/core/src/main/java/org/hyperledger/besu/ethereum/mainnet/parallelization/MainnetParallelBlockProcessor.java` — `processBlock` (L137–L163)

## Impact

A single crafted beacon block — one nonce-invalid transaction at index 0 followed by 16,383 expensive but individually valid transactions — kills any stock Besu node that receives it over normal gossip, after the node has already rejected the block. The attacker requires one legitimately assigned proposer slot and one preparatory transaction; no access to the victim's Engine API or privileged network position is needed.

Measured outcomes on v26.7.1:
- 16 GB container (heap at 100%): `OOMKilled=true`, `ExitCode=137` within 39 seconds
- Stock 25% ergonomics (3.8 GiB heap): JSON-RPC dead at t+26 s, Engine API gone by t+65 s, 24-slot gap, no recovery

This is a single-client availability failure. The attack does not cause a chain split; reference clients continue advancing normally.

Bonsai parallel transaction processing is enabled by default. No non-default configuration is required to be vulnerable.

## Patches and references

Fixed in Besu 26.8.0.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/2ae506fa5875
- Pull request: https://github.com/besu-eth/besu/pull/11104
