# GHSA-f9pw-q493-7qvh: Deadlock and Uncontrolled Resource Consumption in github.com/zcash/lightwalletd

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-f9pw-q493-7qvh |
| CVE | none assigned |
| Severity | medium (CVSS 5.3) |
| CWE | CWE-400, CWE-833 |
| Published | 2026-07-30T18:59:18Z |
| Updated | 2026-07-30T18:59:18Z |
| Affected | github.com/zcash/lightwalletd >= 0.4.13, <= 0.5.1 (patched: 0.5.2) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-f9pw-q493-7qvh |

## Description (verbatim)

### Summary

In `lightwalletd`'s `GetMempoolTx` handler (`frontend/service.go:591-697`), the per-server `s.mutex` is held across the entire mempool-refresh path, which on a cache-cold tick issues `1 + N` sequential blocking `RawRequest` calls to `zcashd` (one `getrawmempool` plus one `getrawtransaction` per uncached txid). Because none of the `RawRequest` calls is context-aware, two things follow: (a) a cancelling client cannot interrupt the refresh — every queued zcashd RPC runs to completion before the handler returns; (b) every concurrent `GetMempoolTx` caller serializes behind the active refresher, even when each caller only needs a consistent snapshot of the mempool. The result is per-client *amplified resource consumption* and *server-wide head-of-line blocking* on a single un-authenticated streaming RPC.

This is the same defect class that PR #560 (`0b155d5`) fixed for `GetBlockRange`/`GetBlockRangeNullifiers` (producer-channel pattern), surfaced by re-auditing the handlers PR #560's own sibling-audit table named clean under a coarser rule. `GetMempoolTx` was on that named-clean list and was incorrectly cleared because the audit checked only for the `make(chan…) + go …` antipattern, not for "ctx-observability on every blocking op."

Comparable maintainer precedent (PR #538, LarryRuane, 2025-12-09) brackets the *class* as bountyworthy code-hygiene ("a good catch and a nice improvement") but the present finding is materially worse than that precedent because the per-iteration RPC count is unbounded by mempool size and the mutex is lock-amplified across all concurrent callers, not just the first.

### Affected products

- **Ecosystem**: Go
- **Package**: `github.com/zcash/lightwalletd` (per `go.mod` line 1, current `main`)
- **Affected versions**: **`>= 0.4.13`** (commit `2d3943b` "add required locking (mutex) to GetMempoolTx" introduced the `s.mutex`-guarded multi-RPC refresh path; first tagged in v0.4.13). Includes every released tag from **v0.4.13 through v0.4.19** (latest tagged release, 2026-03-26), plus current `main` HEAD `0b155d5` (`v0.4.19-3-g0b155d5`). Subsequent commits added pool-type filtering (`3f9398f`) and changed txid endianness (`eb8a721`) but did **not** modify the lock-held-across-multi-RPC pattern.
- **Patched versions**: (leave empty — to be filled when the fix is released, expected v0.4.20)

### CWE

Primary: **CWE-833 (Deadlock / Lock Held with Blocking Call)** — `s.mutex` is held across blocking JSON-RPC roundtrips.
Secondary: **CWE-400 (Uncontrolled Resource Consumption)** — per-cancelled-client amplification (1 client RPC → up to `1 + N` zcashd RPCs that continue past cancel).

### Details

**Vulnerable code (`frontend/service.go:591-699`, HEAD `0b155d5`):**

```go
func (s *lwdStreamer) GetMempoolTx(exclude *walletrpc.Exclude,
    resp walletrpc.CompactTxStreamer_GetMempoolTxServer) error {
    s.mutex.Lock()
    defer s.mutex.Unlock()
    // ...
    if time.Since(s.lastMempool) > 2*time.Second {
        s.lastMempool = time.Now()
        params := []json.RawMessage{}
        result, rpcErr := common.RawRequest("getrawmempool", params)  // line 615
        // ...
        for _, txidstr := range mempoolList {
            // ...
            params := []json.RawMessage{txidJSON, json.RawMessage("1")}
            result, rpcErr := common.RawRequest("getrawtransaction", params)  // line 642
            // ...
        }
    }
    // ... filter + resp.Send loop ...
}
```

`common.RawRequest` (`common/common.go:64`) is the btcd `rpcclient.RawRequest` wrapper and accepts no `context.Context`; the underlying `http.Client` is constructed without a `Timeout` (`btcd@v0.24.2/rpcclient/infrastructure.go`). There is no path by which client-side `<-ctx.Done()` can preempt an in-flight `getrawtransaction`.

Concurrent `GetMempoolTx` callers all take `s.mutex` (verified by `grep -n 's\.mutex' frontend/service.go` — `s.mutex` is referenced only in `GetMempoolTx`; mempool state itself — `mempoolMap`, `mempoolList`, `lastMempool` at lines 583-589 — is package-global, so the mutex is the only coordination primitive across concurrent calls of this RPC). The mutex is held across the full refresh path, so the second caller waits for the first caller's full sequential RPC chain before its own refresh check (and the 2-second cache window) even begins.

**Re-audit framing.** PR #560's body listed `GetMempoolTx` among handlers that "iterate inline and propagate cancellation through `resp.Send` errors." That claim was correct only for the *final send loop* of `GetMempoolTx` (lines 690-697, where `resp.Send` errors are checked) and missed the *refresh path* held under `s.mutex` (lines 611-680). The present GHSA corrects that audit miss.

### PoC

Standalone regtest sketch (not a runnable harness; intended for the reviewer to validate the mechanism):

```go
// Setup: regtest lightwalletd + zcashd. Pre-populate mempool with N=2000
// distinct transactions (synthetic, regtest-only) so that the first
// GetMempoolTx call must issue 1 + 2000 sequential RawRequest calls.

func ExploitLockAmplifiedHeadOfLineBlocking(t *testing.T) {
    nClients := 50
    var wg sync.WaitGroup
    start := time.Now()
    p99 := make([]time.Duration, nClients)

    for i := 0; i < nClients; i++ {
        wg.Add(1)
        go func(i int) {
            defer wg.Done()
            t0 := time.Now()
            stream, err := client.GetMempoolTx(ctx, &walletrpc.Exclude{})
            if err != nil { return }
            // Read first response then cancel
            _, _ = stream.Recv()
            cancel()
            p99[i] = time.Since(t0)
        }(i)
    }
    wg.Wait()
    sort.Slice(p99, func(i, j int) bool { return p99[i] < p99[j] })

    // EXPECTED on unmodified build: p99 dominated by 1 + N RawRequest
    // roundtrips × nClients serialized behind s.mutex.
    // (Plus the goroutines that issued cancelled-but-still-in-flight
    // getrawtransaction calls continue running on zcashd until completion.)
    fmt.Printf("p50=%v p99=%v total=%v\n",
        p99[len(p99)/2], p99[len(p99)*99/100], time.Since(start))
}
```

For the maintainer: a `pprof goroutine` profile during the burst shows N goroutines parked at `common.RawRequest` (`zcashd` JSON-RPC roundtrip), and `s.mutex.Lock` in the handler stack.

I have not had the chance to wire this up against a live regtest+zcashd before filing; happy to do so on request to lock in concrete latency numbers.

### Impact

- **Pre-auth, network-reachable**: any client that can open a gRPC stream can trigger this. lightwalletd is the public-facing endpoint for mobile wallets (Zashi, Nighthawk, YWallet) and is commonly internet-exposed behind a load balancer.
- **Server-wide head-of-line blocking**: contention is not localized to the misbehaving client. All concurrent `GetMempoolTx` callers (legitimate mobile wallets at sync time) wait behind the active refresher.
- **Cancel-disrespect amplification**: a cancelling client cannot abort its own queued zcashd RPCs. An attacker who opens-and-cancels at sustained rate burns zcashd CPU/IO well past the client's TCP-RST.
- **No operator-side mitigation short of source patching**: the bug is in the handler logic, not in a configurable knob; rate-limiting at the gRPC edge would partially mask the symptom but not the underlying contention.

Severity-bracketing precedent: PR #538 (LarryRuane, 2025-12-09) characterized a *single-thread serialization-only* concurrency bug in lightwalletd as *"this bug probably doesn't make a significant difference in practice (it prevents simultaneous GetLatestBlock calls from executing concurrently), but this is a good catch and a nice improvement."* The present finding is materially worse than that precedent because (a) the protected operation is multi-RPC, not a single RPC; (b) the cancel-disrespect amplification has no analog in PR #538; (c) at typical mainnet mempool sizes (sub-100 txns) the per-refresh cost is modest, but at adversarial mempool sizes the cost is unbounded by N.

**CVSS 3.1**: `AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L` → **5.3 (Medium)**.

### Suggested fix

Two changes, neither structurally complex:

**1.** In `GetMempoolTx`, check `<-resp.Context().Done()` between RPCs in the refresh loop and return early on cancel:

```go
for _, txidstr := range mempoolList {
    if err := resp.Context().Err(); err != nil {
        return status.FromContextError(err).Err()
    }
    // existing per-txid fetch...
}
```

**2.** Restructure the refresh path so `s.mutex` is released across the per-txid `RawRequest` loop (refresh into a local map, re-acquire to publish). Mirrors the pattern `common/mempool.go:GetMempool` already uses for `sendToClient` (lines 70-79):

```go
// Snapshot under lock; refresh without lock; publish under lock.
s.mutex.Lock()
if time.Since(s.lastMempool) > 2*time.Second {
    s.mutex.Unlock()
    newMap, newList, err := refreshMempoolUnlocked(resp.Context())
    if err != nil {
        return err
    }
    s.mutex.Lock()
    s.mempoolMap = newMap
    s.mempoolList = newList
    s.lastMempool = time.Now()
}
// Filter and Send still under lock (cheap, in-memory).
defer s.mutex.Unlock()
// ...
```

The minimal hardening is change (1) alone (~10 lines). The full fix including (2) is a larger restructure but eliminates the head-of-line class entirely. I can produce a patch on request; deferring here to give the maintainer freedom on the structural shape.

### Notes

- This GHSA is filed privately while a companion **public PR (`#561`, in flight)** addresses two sibling cancellation-hygiene bugs found in the same re-audit pass (`GetMempoolStream`, `GetSubtreeRoots`). PR #561 explicitly marks `GetMempoolTx` as "under separate disclosure" and does not touch the GetMempoolTx code or reference this specific defect. They are separable code paths.
- A separate follow-up will address a soft `GetTransaction(ctx)` dead-letter `ctx` parameter (PR #562, ~2 weeks out) — that one is code-quality, not security.
- One additional adjacent finding (no server-side `MaxEntries` cap on `GetSubtreeRoots`) will be filed as a public issue, not a GHSA.

### AI disclosure

This finding was identified through a re-audit pass, and this advisory body was drafted, with assistance from Claude (Anthropic). The reporter reviewed each step and is the responsible author.

