# GHSA-pwwg-h8q5-hq28: lightwalletd cache can stitch old-fork and new-chain blocks after restart

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-pwwg-h8q5-hq28 |
| CVE | none assigned |
| Severity | low |
| CWE | CWE-345 |
| Published | 2026-07-31T04:47:45Z |
| Updated | 2026-07-31T04:47:45Z |
| Affected | github.com/zcash/lightwalletd <= 0.4.19 (patched: 0.5.0) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-pwwg-h8q5-hq28 |

## Description (verbatim)

## Summary

`lightwalletd` can serve an internally impossible compact-block chain after a backend reorg that occurs while the service is stopped or restarting.

On startup, `common.NewBlockCache` reconstructs the cache offsets and `nextBlock` height from the on-disk cache, but it does not restore `BlockCache.latestHash` from the last cached block. The ingestor then treats the first post-restart backend block as connected because `BlockCache.HashMatch` accepts `latestHash == hash32.Nil` as a match. If the backend chain reorganized at or below the cached tip while `lightwalletd` was down, the first newly ingested block can be appended after stale old-fork blocks without a prev-hash continuity check.

The result is a persistent wallet-facing chain-data integrity failure:

```text
GetBlock(H)     returns old-fork block H
GetBlock(H + 1) returns new-chain block H+1
GetBlock(H + 1).prevHash != GetBlock(H).hash
```

A local regtest PoC using real `zcashd` mined blocks demonstrates that `lightwalletd` serves the old cached height 120 followed by the new-chain height 121 after restart.

## Affected Code

Primary affected target:
- lightwalletd

Reviewed relative root:
- `./lightwalletd`

Impacted areas:
- `common/cache.go`
- `common/common.go`

Relevant code:

- `common/cache.go:154`: `NewBlockCache` reconstructs `starts` and `nextBlock` from the cache files.
- `common/cache.go:223`: `NewBlockCache` returns without restoring `latestHash`.
- `common/cache.go:55`: `HashMatch` treats `latestHash == hash32.Nil` as a successful match.
- `common/common.go:452`: `BlockIngestor` resumes from `cache.GetNextHeight()`.
- `common/common.go:471`: `BlockIngestor` appends the fetched block when `HashMatch(block.PrevHash)` returns true.

Validation was performed against the local repository snapshot using:

- source review of the reported paths,
- a live local `zcashd` regtest backend,
- a host-run `lightwalletd` instance using a persistent cache directory,
- real mined regtest blocks,
- `poc/cache_reorg_stitch_poc.sh`,
- `poc/query_blocks.go`.

Validation was not performed on public mainnet or public testnet.

## Finding Description

The cache stores the most recent cached block hash in `latestHash`, and the ingestor uses it to determine whether a newly fetched block connects to the cached tip:

```go
// common/cache.go
func (c *BlockCache) HashMatch(prevhash hash32.T) bool {
    c.mutex.RLock()
    defer c.mutex.RUnlock()
    return c.latestHash == hash32.Nil || c.latestHash == prevhash
}
```

During ordinary operation, `latestHash` is updated when a block is added:

```go
// common/cache.go
c.latestHash = hash32.FromSlice(block.Hash)
c.nextBlock++
```

However, after a process restart, `NewBlockCache` rebuilds the cache metadata from the `lengths` file but never restores `latestHash` from the last cached block:

```go
// common/cache.go
func NewBlockCache(dbPath string, chainName string, startHeight int, syncFromHeight int) *BlockCache {
    c := &BlockCache{}
    c.firstBlock = startHeight
    c.nextBlock = startHeight
    ...

    for i := 0; i < nBlocks; i++ {
        ...
        offset += int64(length) + 8
        c.starts = append(c.starts, offset)
        ...
        c.nextBlock++
    }
    Log.Info("Done reading ", c.nextBlock-c.firstBlock, " blocks from disk cache")
    return c
}
```

The block ingestor starts at `nextBlock`, fetches that height from the backend, and relies on `HashMatch` to detect whether the block connects to the cached tip:

```go
// common/common.go
height := c.GetNextHeight()
...
block, err = getBlockFromRPC(height)
...
if block != nil && c.HashMatch(hash32.FromSlice(block.PrevHash)) {
    if err = c.Add(height, block); err != nil {
        Log.Fatal("Cache add failed:", err)
    }
    ...
    continue
}
...
c.Reorg(height - 1)
```

After restart, `latestHash` is the zero value. Therefore, the first post-restart block from the backend bypasses the continuity check. If the backend reorganized while `lightwalletd` was offline, this block may be from a different fork than the cached tip, but it will still be appended.

Once appended, the bad sequence is persistent in the cache files. Clients querying the affected heights receive compact blocks whose hashes cannot form a valid chain.

## Impact Explanation

Impact level: Medium.

This is a wallet-facing chain-data integrity and availability issue in supporting infrastructure. It does not break Zcash consensus and does not directly demonstrate theft, supply inflation, or shielded privacy loss. However, it can make a standard `lightwalletd` instance serve an impossible compact chain to every wallet client connected to that instance until the cache is rebuilt or repaired.

Practical impact:

- Wallet clients can receive a sequence where `GetBlock(H+1).prevHash` does not equal `GetBlock(H).hash`.
- Wallet sync can stall, repeatedly rewind/rescan, or fail around the reorg boundary.
- Incoming transaction detection and confirmation status around the boundary can become unreliable for clients using the affected instance.
- The bad data persists across requests because it is written into the on-disk cache.
- Operators may need manual cache deletion, redownload, or targeted repair to restore service correctness.

The issue is not limited to an attacker consuming resources. It violates the core chain-continuity invariant that light wallet clients rely on when trusting a `lightwalletd` endpoint for compact block data.

## Likelihood Explanation

Likelihood level: Medium.

The bug requires a specific but realistic operational sequence:

1. `lightwalletd` is running with the normal disk cache enabled.
2. The cache contains blocks up to height `H`.
3. `lightwalletd` is stopped, restarted, crashes, or is redeployed.
4. While `lightwalletd` is down, the backend `zcashd` or `zebrad` reorganizes at or below `H`.
5. The backend then advances to at least `H+1`.
6. `lightwalletd` restarts using the same cache directory.

This is not a one-packet remote exploit. The timing requires a reorg during downtime. However, reorgs are a normal blockchain condition, and restarts/deploys/crashes are normal service lifecycle events. The affected configuration is also the standard production configuration: persistent disk cache enabled.

An external attacker does not need privileged access to the `lightwalletd` host if they can create or take advantage of a reorg window. The direct trigger is the chain/backend state and normal service restart behavior.

## Severity Discussion

Per the ZCG Security & Vulnerability Disclosure Initiative, `lightwalletd` is Supporting Infrastructure. Findings in this category are capped at High, but this report recommends Medium.

Medium is appropriate because the defect prevents an individual supporting-infrastructure instance from serving reliable chain data under best-practice operation, without by itself causing loss of funds, reversal of sufficiently confirmed transactions at network scale, supply inflation, or loss of shielded privacy.

The issue is stronger than a minor best-practice or logging problem because it causes persistent invalid wallet-facing chain data. It is weaker than a High finding because exploitation requires the reorg/restart condition and the demonstrated impact is confined to clients of the affected `lightwalletd` instance rather than the Zcash network as a whole.

If the remediation team weighs the compact-chain integrity violation more heavily, the strongest High argument is that the bug can cause all clients of a targeted supporting-infrastructure instance to follow an impossible chain view after a realistic reorg/restart event. The conservative classification remains Medium due to the conditional likelihood and the absence of direct fund loss or privacy break in the PoC.

## Attacker Model, Scope, and Triage Notes

Attacker model:

- The attacker does not need access to the `lightwalletd` host.
- The attacker does not need wallet keys, RPC credentials, validator privileges, or admin access.
- The attacker needs a reorg at or below the cached tip while `lightwalletd` is down, and the backend must advance beyond the cached tip before or during restart.
- In localnet, this is demonstrated with `zcashd` regtest mined blocks and an invalidated/replaced height.

Scope fit:

- `lightwalletd` is listed under Supporting Infrastructure.
- The finding affects wallet-facing chain data served by the light client backend.
- The PoC is isolated to local regtest and does not touch public mainnet or testnet infrastructure.

Expected pushback:

- Pushback: "This requires a reorg and restart."
  - Response: Correct. That is why the report recommends Medium. Reorgs and service restarts are normal operational events, and the bug turns their combination into a persistent invalid cache state.

- Pushback: "The Zcash network consensus is unaffected."
  - Response: Correct. The affected system is `lightwalletd`, not consensus. The impact is that wallet clients using the affected instance receive impossible compact-chain data.

- Pushback: "Wallets should verify block continuity."
  - Response: Clients may detect the inconsistency, but detection still results in sync failure or repeated rewind/rescan. The server should not persistently serve a chain sequence that cannot exist.

- Pushback: "Deleting the cache fixes it."
  - Response: Manual cache rebuild is a recovery path, not prevention. The vulnerable state persists until an operator detects and repairs it.

## Proof of Concept

[poc.zip](https://drive.google.com/file/d/1dHIonWidF1xkdEc_xeSV1MDI2dGHJiHm/view?usp=sharing)

PoC file list:

- `poc/cache_reorg_stitch_poc.sh`
- `poc/query_blocks.go`
- `poc/localnet-observed-output.txt`

The PoC performs the following sequence end-to-end:

1. Starts a local `zcashd` regtest node in Docker.
2. Mines 120 real regtest blocks.
3. Starts `lightwalletd` against that backend with a persistent cache directory.
4. Waits until the cache file proves height 120 is actually cached.
5. Stops `lightwalletd`.
6. Reorganizes the backend chain by invalidating the old height 120 and mining a replacement chain through height 121.
7. Restarts `lightwalletd` with the same cache directory.
8. Queries `GetBlock(120)` and `GetBlock(121)` over gRPC.
9. Confirms that `GetBlock(120).hash` is the old fork block while `GetBlock(121).prevHash` points to the new backend height 120.

Observed local output:

```text
cached old height 120: 09259dde7bd88c8fbc126b17a0a80ed1c3497dab408d8340c4c4035de2f76631
invalidateblock returned 137; restarting zcashd container and continuing
backend new height 120: 075f694c275d939fc404ec37c5fd202c56750b664016297b4422b30e53351776
backend new height 121: 0c51041a4c7cefe9dc019bb3a1f4557c9047943b3d381cf0299dafe573b70de8

lightwalletd after restart:
height=120 hash=09259dde7bd88c8fbc126b17a0a80ed1c3497dab408d8340c4c4035de2f76631 prev=09dd31aa6ccfbe548f950a000ce6788947a3d72aab3e059065a1907fcc090f99 txs=1
height=121 hash=0c51041a4c7cefe9dc019bb3a1f4557c9047943b3d381cf0299dafe573b70de8 prev=075f694c275d939fc404ec37c5fd202c56750b664016297b4422b30e53351776 txs=1

VULNERABLE: lightwalletd served old height 120 followed by new height 121.
Invariant broken: GetBlock(121).prevHash != GetBlock(120).hash
```

The `invalidateblock returned 137` line is a `zcashd v6.12.3` regtest behavior observed during local testing: the node process aborted while disconnecting the block, then restarted with the invalidation applied and the active chain reset. The PoC script handles this by restarting the container and continuing. The relevant `lightwalletd` vulnerability is independent of that backend abort; after the backend exposes a replaced height 120 and new height 121, `lightwalletd` appends new height 121 after its stale cached height 120.

## Reproduce

1. From the reviewed repository root:

```bash
git clone https://github.com/zcash/lightwalletd
cd lightwalletd
git checkout 45b2f4cdd4aeb51f0683d43e96a04b5f8a4af683
```

2. Copy the PoC directory from this report into the repository root, or keep it outside the repository and pass `ROOT` explicitly:

```text
poc/cache_reorg_stitch_poc.sh
poc/query_blocks.go
poc/localnet-observed-output.txt
```

3. Ensure Docker is available. The PoC pulls and runs `electriccoinco/zcashd:latest`.

4. Run the PoC:

```bash
chmod +x poc/cache_reorg_stitch_poc.sh
ROOT="$(pwd)" ./poc/cache_reorg_stitch_poc.sh
```

5. The vulnerable result is:

```text
VULNERABLE: lightwalletd served old height 120 followed by new height 121.
Invariant broken: GetBlock(121).prevHash != GetBlock(120).hash
```

No public Zcash infrastructure is contacted. All blocks are mined on local regtest.

## Live Validation Notes

Validation used:

- Go 1.24.1,
- Docker 28.4.0,
- `electriccoinco/zcashd:latest` reporting `zcashd v6.12.3`,
- host-run `lightwalletd` built from the reviewed repository,
- Docker-bridge-only backend RPC and loopback-only gRPC/HTTP ports,
- a temporary local cache directory.

The key invariant check was performed through `lightwalletd`'s gRPC API, not by reading cache files directly. The backend was also queried with `zcash-cli getblockhash` to confirm that backend height 120 had changed from the cached old height 120.

No public mainnet or public testnet endpoint was contacted.

## Remediation

The cache loader should restore `latestHash` from the last cached block before `BlockIngestor` starts. A minimal fix is to call `setLatestHash()` at the end of successful cache loading, or otherwise compute the cached tip hash while loading:

```go
// common/cache.go
Log.Info("Done reading ", c.nextBlock-c.firstBlock, " blocks from disk cache")
c.setLatestHash()
return c
```

After this change, the first post-restart block fetched from the backend will be checked against the cached tip. If it does not connect, the existing reorg path can drop stale cached blocks instead of appending across forks.

Also consider hardening startup by validating the cached tip against the backend before serving block-range requests from cache. At minimum, if the backend tip is not equal to or descended from the cached tip, the cache should rewind until the common ancestor is found.

Related hardening: the `--sync-from-height` / `--redownload` path should physically truncate both cache files to the retained prefix before appending replacement blocks. The current startup code slices the in-memory `lengths` buffer but opens both cache files with `O_APPEND`, which can leave stale suffix data and cause confusing cache behavior after manual resync attempts.

Minimal security goal: after restart, `lightwalletd` must never append a block whose `prevHash` does not equal the cached tip hash, and must never serve a cached sequence where `GetBlock(H+1).prevHash != GetBlock(H).hash`.

