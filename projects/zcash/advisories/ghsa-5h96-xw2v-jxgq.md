# GHSA-5h96-xw2v-jxgq: Goroutine Leak in `GetBlockRange`

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-5h96-xw2v-jxgq |
| CVE | none assigned |
| Severity | high |
| CWE | n/a |
| Published | 2026-07-19T16:51:28Z |
| Updated | 2026-07-20T19:51:17Z |
| Affected |  <= v0.4.19 (patched: v5.0) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-5h96-xw2v-jxgq |

## Description (verbatim)

### Summary
`GetBlockRange` spawns a producer goroutine that fetches blocks and sends them on an unbuffered channel. While the code includes `ctx.Done()` cases in its selects to handle client disconnection, the producer can still get **stuck deep inside `GetBlock`/`getBlockFromRPC`**—which perform synchronous JSON-RPC calls to `zcashd` that do **not** accept a context for cancellation. When the gRPC handler returns early (e.g., because `resp.Send` fails or the client disconnects), the goroutine remains alive until the RPC call completes, leaking goroutines and consuming RPC connections. Under adversarial load this exhausts both goroutine scheduler capacity and the `zcashd` RPC connection pool.

### Details
The handler in `frontend/service.go` lines 230-256:
```go
func (s *lwdStreamer) GetBlockRange(span *walletrpc.BlockRange, resp ...) error {
    ctx := resp.Context()
    blockChan := make(chan *walletrpc.CompactBlock)
    errChan := make(chan error)
    go common.GetBlockRange(ctx, s.cache, blockChan, errChan, span)
    for {
        select {
        case <-ctx.Done():
            return ctx.Err()
        case err := <-errChan:
            return err
        case cBlock := <-blockChan:
            err := resp.Send(cBlock)
            if err != nil {
                return err // <--- handler returns, goroutine may be stuck in GetBlock
            }
        }
    }
}
```

The producer in `common/common.go` lines 579-623:
```go
func GetBlockRange(ctx context.Context, cache *BlockCache, blockOut chan<- *walletrpc.CompactBlock, errOut chan<- error, span *walletrpc.BlockRange) {
    ...
    for i := low; i <= high; i++ {
        block, err := GetBlock(cache, j) // <--- synchronous, no ctx cancellation
        if err != nil {
            select {
            case errOut <- err:
            case <-ctx.Done():
            }
            return
        }
        select {
        case blockOut <- block:
        case <-ctx.Done():
            return
        }
    }
    ...
}
```

`GetBlock` (lines 498-520) calls `getBlockFromRPC` (lines 320-401) when the block is not in cache. `getBlockFromRPC` makes **two** synchronous JSON-RPC HTTP requests to `zcashd` (one verbose, one raw). Neither `getBlockFromRPC` nor the underlying `rpcclient` accept a `context.Context`; therefore the HTTP calls cannot be interrupted even if the gRPC stream context is cancelled.

If a malicious client opens a `GetBlockRange` stream requesting a block that requires an RPC call, then immediately disconnects (causing `resp.Send` to fail or the handler to return), the handler returns but the producer goroutine is still blocked waiting for `zcashd` to respond. The goroutine will eventually exit once the RPC returns and it hits the `ctx.Done()` case, but until then it is leaked.

`GetBlockRangeNullifiers` (`frontend/service.go:261-305`) uses the **identical pattern** and is equally vulnerable.

### Mitigations
- **None** in the RPC path. The `ctx.Done()` cases in the select statements only help when the goroutine is actually at the select; they do not abort an in-flight HTTP request to `zcashd`.
- A bounded goroutine pool or per-request timeout wrapping the RPC calls would mitigate the issue, but neither exists.

### Additional Attack Vectors
- **Connection pool exhaustion:** The `btcsuite/btcd/rpcclient` maintains persistent HTTP connections to `zcashd`. Each leaked goroutine may hold or wait for a connection, exhausting the pool and causing subsequent legitimate requests to block or fail.
- **Amplification via cache misses:** An attacker can request block ranges that are guaranteed to miss the local cache (e.g., very old heights after `--redownload`), forcing every request to hit `zcashd` and maximizing the hang time.
- **Synergy with `GetBlockRangeNullifiers`:** The attacker can interleave requests to both streaming endpoints, doubling the goroutine consumption rate.
- **Potential deadlock:** If the handler returns while the producer is blocked in the `select` trying to send on `blockOut`, and for some reason the stream context is not promptly cancelled (e.g., a slow gRPC transport teardown), the goroutine can remain blocked on the channel send indefinitely.
