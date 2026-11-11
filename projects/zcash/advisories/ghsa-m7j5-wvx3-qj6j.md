# GHSA-m7j5-wvx3-qj6j: lightwalletd can serve old-fork and new-fork blocks in one live GetBlockRange response during reorg repair

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-m7j5-wvx3-qj6j |
| CVE | none assigned |
| Severity | low |
| CWE | CWE-362 |
| Published | 2026-08-05T03:51:20Z |
| Updated | 2026-08-05T03:51:20Z |
| Affected | github.com/zcash/lightwalletd <= 0.5.2 (patched: 0.5.3) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-m7j5-wvx3-qj6j |

## Description (verbatim)

## Summary

`lightwalletd` can serve an internally impossible compact-block chain during a live backend reorg, without requiring a service restart or cache-file corruption.

The public `GetBlockRange` path reads each requested height independently through `common.GetBlock`. `common.GetBlock` first returns cached blocks and only falls back to the backend for cache misses. If the local cache still contains old-fork blocks through height `N`, while the backend has already reorganized and advanced to height `N+1`, a single public `GetBlockRange(N, N+1)` request can return:

- height `N` from the old cached fork, and
- height `N+1` from the current backend fork.

No continuity check is performed before streaming the response, so the returned sequence can violate the core compact-chain invariant:

```text
GetBlockRange(N..N+1)[1].prevHash == GetBlockRange(N..N+1)[0].hash
```

A local regtest PoC using real `zcashd`, a host-run `lightwalletd`, mined regtest blocks, and the public `GetBlockRange` gRPC method demonstrates:

```text
range height=120 hash=<old cached fork block>
range height=121 hash=<new backend fork block> prev=<new backend height 120>

VULNERABLE: live GetBlockRange served old cached height 120 followed by new backend height 121.
```

## Affected Code

Primary affected target:
- lightwalletd

Reviewed relative root:
- `./lightwalletd`

Impacted areas:
- `frontend/service.go`
- `common/common.go`
- `common/cache.go`

Relevant code:

- `frontend/service.go:230`: public `GetBlockRange`.
- `frontend/service.go:236-240`: starts `common.GetBlockRange` in a producer goroutine.
- `frontend/service.go:243-253`: streams blocks exactly as returned by the producer, without validating adjacency.
- `common/common.go:579`: `common.GetBlockRange`.
- `common/common.go:601`: each height in the requested range is resolved independently through `GetBlock(cache, j)`.
- `common/common.go:498-514`: `GetBlock` returns `cache.Get(height)` first and only fetches from the backend when the cache misses.
- `common/common.go:423-489`: the background ingestor repairs reorgs asynchronously by detecting that the backend no longer extends the cached tip and then rewinding one height at a time.
- `common/cache.go:325-342`: `BlockCache.Get` returns cached blocks by height without checking whether the cached block is still on the backend's current best chain.

Validation was performed against the local repository snapshot using:

- source review of the reported paths,
- a live local `zcashd` regtest backend,
- a host-run `lightwalletd` instance,
- real mined regtest blocks,
- a local backend reorg created with `invalidateblock`,
- the public `CompactTxStreamer/GetBlockRange` gRPC method,
- `poc/live_reorg_deterministic.sh`,
- `poc/rpc_freeze_proxy.go`,
- `poc/client.go`.

Validation was not performed on public mainnet or public testnet.

## Finding Description

`lightwalletd` assumes that the cache and backend are interchangeable sources for the same `GetBlockRange` stream. That assumption is invalid during live reorg repair.

The vulnerable state is:

1. `lightwalletd` has cached fork A through height `N`.
2. The backend `zcashd` reorganizes at or below height `N`.
3. The backend advances to height `N+1` on fork B.
4. Before the background ingestor finishes rewinding and refilling the stale cache, a public client requests `GetBlockRange(N, N+1)`.
5. Height `N` is returned from the cache, still fork A.
6. Height `N+1` is not cached, so `lightwalletd` fetches it from the backend, now fork B.
7. The response is streamed without checking that height `N+1` connects to height `N`.

The result is a compact-block stream that cannot exist on any valid Zcash chain.

The vulnerable composition happens because `GetBlockRange` resolves every height independently:

```go
for i := low; i <= high; i++ {
    j := i
    if span.Start.Height > span.End.Height {
        j = high - (i - low)
    }

    block, err := GetBlock(cache, j)
    if err != nil {
        select {
        case errOut <- err:
        case <-ctx.Done():
        }
        return
    }

    block.Vtx = filterBlockPool(block.Vtx, span.PoolTypes)
    select {
    case blockOut <- block:
    case <-ctx.Done():
        return
    }
}
```

`GetBlock` then prefers cache data whenever a height is present, and falls back to the backend only when that height is missing:

```go
if cache != nil {
    block := cache.Get(height)
    if block != nil {
        return block, nil
    }
}

block, err := getBlockFromRPC(height)
```

There is no range-level snapshot, no "cache-only or backend-only" source selection, and no adjacent block continuity check before streaming each block to the wallet client.

This is distinct from the restart/cache-stitch bug. It is not caused by `BlockCache.latestHash` being zero after restart, and it does not require appending a bad block to the on-disk cache. This issue is a live read-path consistency bug: public reads are allowed to mix stale cached data and current backend data while asynchronous reorg repair is still in progress.

## Impact Explanation

Impact level: High.

This is a wallet-facing chain-data integrity issue in supporting infrastructure. It does not affect Zcash consensus, does not kill the backend `zcashd` or `zebrad`, and does not automatically propagate to other `lightwalletd` nodes. However, it can cause clients of the targeted `lightwalletd` instance to receive an impossible compact chain.

Practical impact:

- A public `GetBlockRange` response can contain blocks from two different forks.
- The response violates `next.prevHash == current.hash`.
- Strict wallet clients can reject the response and fail to sync through the affected endpoint.
- Less strict clients, indexers, or services can temporarily index wallet state against an impossible chain view.
- Wallet-facing confirmation, history, witness, or note-detection state can be interrupted or corrupted until the client recovers or resyncs.

The issue is stronger than generic denial of service because the server returns semantically invalid chain data, not merely a slow response or an error.

## Likelihood Explanation

Likelihood level: Medium.

The public trigger is a normal unauthenticated `GetBlockRange` request. The attacker does not need backend RPC credentials, filesystem access, wallet keys, validator privileges, or operator access.

The required condition is a backend reorg while `lightwalletd` still has stale cached blocks and before its background ingestor completes repair. This is a timing condition, but it is a normal chain-state condition rather than a malicious backend assumption.

An attacker can improve reliability by repeatedly requesting ranges near the cached tip or near a recently observed reorg boundary:

```text
GetBlockRange(N, N+1)
```

The localnet PoC uses a small local JSON-RPC proxy to make this timing window deterministic. After height 120 is actually present in the cache, the proxy freezes only `getbestblockhash` at the old tip so the background ingestor cannot repair the cache before the client request. Ordinary `getblock` RPCs still reach the reorged backend, so the public `GetBlockRange` call demonstrates the read-path mix.

## Severity Discussion

Per the ZCG Security & Vulnerability Disclosure Initiative, `lightwalletd` is Supporting Infrastructure. This report recommends High because the demonstrated outcome is a wallet-facing integrity failure in supporting infrastructure: a public API can return compact block data that violates the chain-continuity invariant relied on by light wallet clients.

This is not a network-wide halt or consensus failure. The affected system is the targeted `lightwalletd` instance and clients that rely on it. The High argument is that the issue can break the correctness of wallet synchronization data served by a public infrastructure endpoint during normal live reorg repair.

Compared with a persistent cache-corruption variant, this issue has a shorter impact window. However, it does not require a `lightwalletd` restart or operator action. Any public client can continuously request tip-adjacent ranges and catch the inconsistent response while the node is repairing from a live reorg.

## Attacker Model, Scope, and Triage Notes

Attacker model:

- The attacker does not need access to the `lightwalletd` host.
- The attacker does not need backend RPC credentials.
- The attacker does not need wallet keys, validator privileges, or admin access.
- The attacker needs access to the public `lightwalletd` gRPC endpoint.
- The attacker needs a backend reorg window while `lightwalletd` still has stale cached blocks.

Scope fit:

- `lightwalletd` is listed under Supporting Infrastructure.
- The affected method is a public wallet-facing gRPC API.
- The demonstrated impact is invalid wallet synchronization data served by the targeted instance.
- The PoC is isolated to local regtest and does not touch public mainnet or testnet infrastructure.
- The PoC does not use darkside APIs, `--ping-very-insecure`, or any test-only gRPC method.

Expected pushback:

- Pushback: "The PoC uses `invalidateblock`."
  - Response: `invalidateblock` is only used to deterministically create a local regtest reorg for validation. The vulnerable lightwalletd behavior is the public read-path mixing of stale cached blocks and current backend blocks during reorg repair.

- Pushback: "The response is only invalid during a timing window."
  - Response: Correct. The timing window affects likelihood, but the window is real. The deterministic PoC only holds the ingestor in that window; the invalid response is produced by the unmodified public `GetBlockRange` path. Public reads are not paused during repair and no continuity check is enforced before streaming.

- Pushback: "This does not affect consensus or other nodes."
  - Response: Correct. This is a supporting-infrastructure wallet data integrity issue for the targeted `lightwalletd` instance, not a Zcash consensus failure.

- Pushback: "Wallet clients should validate block continuity."
  - Response: Clients should validate, but `lightwalletd` is still expected not to serve an internally impossible chain from one `GetBlockRange` response. Even strict validation turns this into a sync failure for users of the affected endpoint.

## Proof of Concept

[poc.zip](https://drive.google.com/file/d/1iL7NkFf2T5j7AmFznOI_PgtL09eWa6ah/view?usp=sharing)

PoC file list:

- `poc/live_reorg_deterministic.sh`
- `poc/live_reorg_try.sh`
- `poc/rpc_freeze_proxy.go`
- `poc/client.go`
- `poc/localnet-observed-output.txt`

The PoC performs the following sequence end-to-end:

1. Starts a local `zcashd` regtest node in Docker.
2. Mines 120 real regtest blocks.
3. Starts a local JSON-RPC proxy that forwards to `zcashd`.
4. Builds and starts `lightwalletd` from the reviewed repository, pointed at the proxy.
5. Waits until the cache file proves height 120 is actually cached.
6. Freezes only `getbestblockhash` at the old height 120 hash so the background ingestor cannot repair the cache before the client request.
7. Reorganizes the backend at height 120 and mines a replacement height 120 plus height 121.
8. Without restarting `lightwalletd`, calls the public `GetBlockRange(120, 121)` gRPC method.
9. Checks whether height 120 is the old cached block while height 121 points to the new backend height 120.

Observed output:

```text
cached old height 120: 00dd98825edab21b1d9951f651e23799e9beca65beedf86b813ccc77cf935fa8
freezing getbestblockhash at old height 120 so the ingestor cannot repair before the client request
invalidateblock returned 137; restarting zcashd container and continuing
backend new height 120: 0396b321ef7788a10bd8295f0336d55a01b4601816c9ba59624f0f2e03937865
backend new height 121: 09abeca1ea0b66c2570ffa7d1d644504f3ef3470c0c1736b59122ed80f59d305

requesting live GetBlockRange while the cache still contains old height 120:
range height=120 hash=00dd98825edab21b1d9951f651e23799e9beca65beedf86b813ccc77cf935fa8 prev=03e89aae1167d95be21b93eb868fea4d7e90beac42cf54102f41bca3dec64f05 txs=1
range height=121 hash=09abeca1ea0b66c2570ffa7d1d644504f3ef3470c0c1736b59122ed80f59d305 prev=0396b321ef7788a10bd8295f0336d55a01b4601816c9ba59624f0f2e03937865 txs=1

VULNERABLE: live GetBlockRange served old cached height 120 followed by new backend height 121.
```

The invariant is broken because:

```text
height 120 hash = 00dd98825edab21b1d9951f651e23799e9beca65beedf86b813ccc77cf935fa8
height 121 prev = 0396b321ef7788a10bd8295f0336d55a01b4601816c9ba59624f0f2e03937865
```

Those hashes are different.

## Reproduce

Requirements:

- Docker
- Go
- an unpacked `zcash/lightwalletd` repository

From the `lightwalletd` repository root:

```bash
ROOT="$(pwd)" /path/to/poc/live_reorg_deterministic.sh
```

The script builds the local `lightwalletd` binary, starts `electriccoinco/zcashd:latest` in regtest, mines local blocks, creates a backend reorg, and calls the public `GetBlockRange` gRPC method. The deterministic script is preferred because it verifies that height 120 is cached and holds the ingestor in the pre-repair window.

Expected vulnerable output:

```text
VULNERABLE: live GetBlockRange served old cached height 120 followed by new backend height 121.
```

No public Zcash infrastructure is contacted. All blocks are mined on local regtest.

## Live Validation Notes

Validation was performed with:

- `electriccoinco/zcashd:latest`,
- host-run `lightwalletd` built from the reviewed repository,
- local regtest mined blocks,
- a local JSON-RPC proxy to hold `getbestblockhash` at the old tip after the cache reached height 120,
- public `CompactTxStreamer/GetBlockRange` gRPC calls.

The `invalidateblock returned 137` line is a local `zcashd` regtest behavior already observed in related reorg testing. The script restarts the local container and continues after the invalidation has taken effect. The relevant `lightwalletd` issue is independent of that backend process exit: after the backend exposes a replacement height 120 and new height 121, the still-running `lightwalletd` can mix its old cached height 120 with the new backend height 121 in one public range response.

The proxy does not modify `lightwalletd` and does not synthesize block data. It only keeps the background ingestor from observing the new best hash before the client request. The key invariant check was performed through `lightwalletd`'s gRPC API. The invalid chain was not inferred from cache files or direct local calculations.

## Remediation

`lightwalletd` should not serve a range by mixing cache and backend data unless it validates that the resulting sequence is contiguous.

At minimum:

- before sending a range response, verify each adjacent pair satisfies `next.prevHash == current.hash`;
- if a cache/backend discontinuity is detected, return a retryable error and trigger or wait for reorg repair;
- consider pausing cache-backed public block reads while the ingestor has detected a reorg and is rewinding/refilling;
- ensure `GetTreeState` and subtree APIs cannot be combined with stale cached compact blocks from a different fork.

One minimal defensive sketch is to validate continuity inside `common.GetBlockRange` before emitting each block:

```go
var prev *walletrpc.CompactBlock

for i := low; i <= high; i++ {
    j := i
    if span.Start.Height > span.End.Height {
        j = high - (i - low)
    }

    block, err := GetBlock(cache, j)
    if err != nil {
        sendErr(ctx, errOut, err)
        return
    }

    if prev != nil {
        forward := span.Start.Height <= span.End.Height
        if forward && !bytes.Equal(block.PrevHash, prev.Hash) {
            sendErr(ctx, errOut, status.Error(codes.Aborted,
                "GetBlockRange: chain discontinuity during reorg repair"))
            return
        }
        if !forward && !bytes.Equal(prev.PrevHash, block.Hash) {
            sendErr(ctx, errOut, status.Error(codes.Aborted,
                "GetBlockRange: chain discontinuity during reorg repair"))
            return
        }
    }

    block.Vtx = filterBlockPool(block.Vtx, span.PoolTypes)
    select {
    case blockOut <- block:
    case <-ctx.Done():
        return
    }
    prev = block
}
```

The exact patch can be structured differently, but the security property should be explicit: if a range response crosses a stale cache/current backend boundary, `lightwalletd` must return a retryable error or wait for repair rather than streaming an impossible chain.

Minimal security goal: a single `GetBlockRange` response must always describe one contiguous chain.

