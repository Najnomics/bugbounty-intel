# GHSA-hp3q-vfr4-v8m6: GetMempoolStream Global Mutex Held During Uncancellable RPC

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-hp3q-vfr4-v8m6 |
| CVE | none assigned |
| Severity | high (CVSS 7.5) |
| CWE | CWE-833 |
| Published | 2026-11-18T00:38:26Z |
| Updated | 2026-11-18T00:38:26Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.1 (patched: 0.6.2) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-hp3q-vfr4-v8m6 |

## Description (verbatim)

### Summary

The `GetMempoolStream` gRPC handler in lightwalletd calls `common.GetMempool()`, which acquires a process-global mutex (`g_lock`, [`common/mempool.go:39`](https://github.com/zcash/lightwalletd/blob/d16d4812/common/mempool.go#L39)) and holds it across multiple sequential, uncancellable JSON-RPC calls to the zcashd backend. Because `GetBlockChainInfo()` uses `context.Background()` ([`common/common.go:278`](https://github.com/zcash/lightwalletd/blob/d16d4812/common/common.go#L278)) instead of the client's request context, client cancellation cannot interrupt the in-flight RPC. When zcashd is slow to respond, the mutex is held for up to 60 seconds (the HTTP client timeout at [`frontend/rawrequest.go:26`](https://github.com/zcash/lightwalletd/blob/d16d4812/frontend/rawrequest.go#L26)), serializing and blocking all concurrent `GetMempoolStream` callers. This enables a pre-auth, network-reachable denial of service against all mempool-streaming light wallet clients.


### Details


1. A gRPC client calls `GetMempoolStream` ([`frontend/service.go:684`](https://github.com/zcash/lightwalletd/blob/d16d4812/frontend/service.go#L684)), which invokes `common.GetMempool(ctx, callback)` ([`common/mempool.go:38`](https://github.com/zcash/lightwalletd/blob/d16d4812/common/mempool.go#L38)).

2. `GetMempool` acquires the global mutex `g_lock` at line 39:
   ```go
   g_lock.Lock()
   defer g_lock.Unlock()
   ```

3. Within the critical section, it calls `GetBlockChainInfo()` at line 57. This function ([`common/common.go:277-278`](https://github.com/zcash/lightwalletd/blob/d16d4812/common/common.go#L277-L278)) hardcodes `context.Background()`:
   ```go
   func GetBlockChainInfo() (*ZcashdRpcReplyGetblockchaininfo, error) {
       result, rpcErr := RawRequest(context.Background(), "getblockchaininfo", []json.RawMessage{})
   ```
   The `context.Background()` call means the HTTP request to zcashd is immune to client cancellation. The only timeout is the 60-second HTTP client timeout ([`frontend/rawrequest.go:26`](https://github.com/zcash/lightwalletd/blob/d16d4812/frontend/rawrequest.go#L26)).

4. Still holding `g_lock`, `GetMempool` calls `refreshMempoolTxns()` at line 71. This makes 1 `getrawmempool` RPC plus N sequential `getrawtransaction` RPCs for each uncached mempool transaction, all within the critical section.

5. The 2-second debounce at line 56 does NOT mitigate this. When the lock is held for >2s, the next goroutine to acquire it sees stale `g_lastTime` and triggers its own full RPC refresh cycle, perpetuating the contention.

6. No `MaxConcurrentStreams` is configured on the gRPC server ([`cmd/root.go:144,172`](https://github.com/zcash/lightwalletd/blob/d16d4812/cmd/root.go#L144)), so there is no server-side limit on concurrent `GetMempoolStream` connections.

### Distinction from Prior Advisories

- **GHSA-f9pw-q493-7qvh** fixed mutex scope and context threading in `GetMempoolTx` ([`frontend/service.go:709+`](https://github.com/zcash/lightwalletd/blob/d16d4812/frontend/service.go#L709)), a *different handler* using a different mutex (`s.mutex`) and different state variables (`mempoolMap`, `mempoolList`).
- **GHSA-4hp3-3494-3f2m** fixed bounds on the exclude list in `GetMempoolTx`, also a different function.
- **GHSA-5h96-xw2v-jxgq / GHSA-9x94-88pq-6v7h** fixed cancel hygiene for streaming RPCs, but the PR description for commit `0e91815` explicitly stated it did NOT fix the lock-amplification issue in `GetMempool`.
- This finding targets `common/mempool.go` and the global `g_lock`, which is a completely separate code path from all prior advisories.

### Cancel-Aware Sleep is Not a Fix

Commit `0e91815` added a cancel-aware sleep between lock acquisitions ([`common/mempool.go:90-93`](https://github.com/zcash/lightwalletd/blob/d16d4812/common/mempool.go#L90-L93)):
```go
select {
case <-ctx.Done():
    return ctx.Err()
case <-time.After(interval):
}
```
This handles client disconnect *between* lock acquisitions, but NOT during the critical section (lines 39-81 hold `g_lock` continuously through the RPC call). A goroutine blocked on `g_lock.Lock()` at line 39 is not in a `select` and cannot observe `ctx.Done()`.

### Proof of concept
```go
// PoC: GetMempoolStream head-of-line blocking via uncancellable GetBlockChainInfo
// under global g_lock.
//
// This test proves that concurrent GetMempool callers are blocked for the
// full duration of a slow GetBlockChainInfo() RPC call because the call
// uses context.Background() (uncancellable) and runs while holding g_lock.
//
// To run: copy this file to common/common_test.go's directory and execute:
//   cd common && go test -run TestPoCMempoolLockContention -timeout 30s -v
package common

import (
	"context"
	"encoding/json"
	"sync"
	"sync/atomic"
	"testing"
	"time"

	"github.com/zcash/lightwalletd/walletrpc"
)

func TestPoCMempoolLockContention(t *testing.T) {
	testT = t
	defer resetGlobals()

	// Track how long GetBlockChainInfo holds the lock by making it slow.
	const slowRPCDelay = 3 * time.Second
	var rpcCallCount atomic.Int32

	// Stub RawRequest: getblockchaininfo is artificially slow (simulating
	// zcashd under load); getrawmempool returns empty; the second
	// getblockchaininfo returns a new block hash to let GetMempool exit.
	RawRequest = func(ctx context.Context, method string, params []json.RawMessage) (json.RawMessage, error) {
		callNum := rpcCallCount.Add(1)
		switch method {
		case "getblockchaininfo":
			// Simulate slow zcashd: sleep for slowRPCDelay.
			// This runs UNDER g_lock because GetMempool calls
			// GetBlockChainInfo() at mempool.go:57 while holding g_lock,
			// and GetBlockChainInfo() hardcodes context.Background()
			// so client cancellation does NOT abort this.
			time.Sleep(slowRPCDelay)

			if callNum <= 2 {
				// First two calls: same block hash 
				r, _ := json.Marshal(&ZcashdRpcReplyGetblockchaininfo{
					BestBlockHash: "aabbcc",
					Blocks:        100,
				})
				return r, nil
			}
			// Later calls: new block hash, lets GetMempool exit
			r, _ := json.Marshal(&ZcashdRpcReplyGetblockchaininfo{
				BestBlockHash: "ddeeff",
				Blocks:        101,
			})
			return r, nil

		case "getrawmempool":
			r, _ := json.Marshal([]string{})
			return r, nil
		}
		return nil, nil
	}

	// Use real time functions (not stubs) so we measure actual blocking.
	Time.Sleep = time.Sleep
	Time.Now = time.Now
	Time.After = time.After

	// Force the 2-second debounce to fire immediately by setting
	// g_lastTime far in the past.
	g_lastTime = time.Time{}

	//  Launch two concurrent GetMempool callers 
	var wg sync.WaitGroup
	startTimes := make([]time.Time, 2)
	endTimes := make([]time.Time, 2)
	errs := make([]error, 2)

	for i := 0; i < 2; i++ {
		wg.Add(1)
		go func(idx int) {
			defer wg.Done()
			startTimes[idx] = time.Now()
			errs[idx] = GetMempool(context.Background(), func(tx *walletrpc.RawTransaction) error {
				return nil
			})
			endTimes[idx] = time.Now()
		}(i)
		// Stagger slightly so goroutine 0 acquires g_lock first.
		if i == 0 {
			time.Sleep(50 * time.Millisecond)
		}
	}

	wg.Wait()

	// Assert the harm: goroutine 1 was blocked for the full duration
	// of goroutine 0's slow GetBlockChainInfo call 
	for i, err := range errs {
		if err != nil {
			t.Fatalf("GetMempool[%d] returned error: %v", i, err)
		}
	}

	dur0 := endTimes[0].Sub(startTimes[0])
	dur1 := endTimes[1].Sub(startTimes[1])

	t.Logf("Goroutine 0 duration: %v", dur0)
	t.Logf("Goroutine 1 duration: %v", dur1)
	t.Logf("RPC calls made: %d", rpcCallCount.Load())

	// Goroutine 0 should take at least slowRPCDelay,it calls
	// GetBlockChainInfo which sleeps.
	if dur0 < slowRPCDelay {
		t.Errorf("Goroutine 0 completed too fast (%v < %v): slow RPC not simulated", dur0, slowRPCDelay)
	}

	// Goroutine 1 should also take at least slowRPCDelay
	// because it is blocked on g_lock while goroutine 0 holds it during
	// the slow GetBlockChainInfo call. In a healthy design, goroutine 1
	// would not be blocked by goroutine 0's RPC call.
	if dur1 < slowRPCDelay {
		t.Errorf("FINDING DISPROVED: Goroutine 1 was NOT blocked (%v < %v)", dur1, slowRPCDelay)
	} else {
		t.Logf("CONFIRMED: Goroutine 1 was head-of-line blocked for %v "+
			"(>= %v) by goroutine 0's uncancellable GetBlockChainInfo under g_lock",
			dur1, slowRPCDelay)
	}

	if rpcCallCount.Load() < 3 {
		t.Logf("Note: only %d RPC calls, debounce may have prevented the second getblockchaininfo", rpcCallCount.Load())
	} else {
		t.Logf("CONFIRMED: Debounce perpetuation observed: %d total RPC calls (>2 means both goroutines called getblockchaininfo)", rpcCallCount.Load())
	}
}
```
### Impact

- The gRPC endpoint requires no authentication (`cmd/root.go:144,172` have no auth interceptor). Any network client can trigger this.
-  A single slow `GetMempoolStream` response serializes ALL concurrent mempool stream callers. It leads to denial of service to every connected light wallet.
- Goroutine accumulation: Each blocked client occupies one goroutine (~8KB stack). With no `MaxConcurrentStreams`, 1000 concurrent connections accumulate ~8MB of stack memory plus channel allocations.
-  Up to 60s per iteration (HTTP timeout). With N=100 new mempool txids at 200ms/RPC, lock hold = 200ms + 100*200ms = 20.2 seconds. Under zcashd load (1s/RPC), lock hold exceeds the HTTP timeout cap.
- Affected clients includes : All mobile and desktop light wallets using `GetMempoolStream` for unconfirmed transaction visibility.


