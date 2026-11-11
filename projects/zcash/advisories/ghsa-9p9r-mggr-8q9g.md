# GHSA-9p9r-mggr-8q9g: lightwalletd GetMempoolTx holds shared mempool mutex across client-controlled streaming sends

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-9p9r-mggr-8q9g |
| CVE | none assigned |
| Severity | medium (CVSS 5.3) |
| CWE | CWE-400, CWE-667 |
| Published | 2026-07-30T19:30:20Z |
| Updated | 2026-07-30T19:30:20Z |
| Affected | github.com/zcash/lightwalletd >= 0.4.13, <= 0.5.1 (patched: 0.5.2) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-9p9r-mggr-8q9g |

## Description (verbatim)

## Summary

`GetMempoolTx` takes `s.mutex` near the start of the handler and defers unlock until the handler returns. The handler later streams filtered mempool compact transactions to the client while the same mutex is still held.

If one client is slow, stops reading, or otherwise blocks the server-side `resp.Send`, the mutex remains held. A second concurrent `GetMempoolTx` request then cannot enter the mempool refresh/filter/send path until the first stream releases.

This is endpoint-specific head-of-line blocking for `GetMempoolTx`, not a whole-service outage. The issue is still availability-relevant because `GetMempoolTx` is a wallet-facing streaming method and the lock covers shared mempool cache state.

## Target checked

- repository: `zcash/lightwalletd`
- commit: `3870883667dc95f85fe3810321735067be39eef3`

Affected versions and patched versions are unknown from the reporter side; maintainers should confirm.

## Affected code

At commit `3870883667dc95f85fe3810321735067be39eef3`:

- `frontend/service.go:581-599`: `GetMempoolTx` starts, validates request, then calls `s.mutex.Lock()` and `defer s.mutex.Unlock()`.
- `frontend/service.go:601-670`: refreshes shared mempool state while holding the mutex.
- `frontend/service.go:680-687`: iterates filtered mempool txids and calls `resp.Send(ftx)` while the mutex is still held.

Relevant shape:

```go
s.mutex.Lock()
defer s.mutex.Unlock()
...
for _, txid := range MempoolFilter(mempoolList, excludeHex) {
    if ftx := common.FilterTxPool((*mempoolMap)[txid], exclude.PoolTypes); ftx != nil {
        err := resp.Send(ftx)
        if err != nil {
            return err
        }
    }
}
```

The older mempool streaming helper already documents the safer pattern:

- `common/mempool.go:68-79`: copies `toSend`, unlocks, then sends because the send call may be flow-controlled.

## Impact

Availability impact against public lightwalletd gRPC endpoints:

- a slow or non-reading `GetMempoolTx` client can hold the shared mempool mutex during streaming;
- concurrent `GetMempoolTx` clients are blocked behind that stream;
- impact is bounded to the mempool transaction endpoint unless this mutex is later reused by broader state;
- no confidentiality, integrity, consensus, or fund-movement impact is claimed.

## Local validation

Disposable local test added in a private worktree:

- file: `frontend/frontend_test.go`
- test name: `TestPocGetMempoolTxSlowReaderBlocksConcurrentMempoolTx`

Observed validation output from the local test environment:

```text
cd /root/bounty-hunts/lightwalletd-head
go test ./frontend -run 'TestPocGetMempoolTxSlowReaderBlocksConcurrentMempoolTx' -count=1 -v

=== RUN   TestPocGetMempoolTxSlowReaderBlocksConcurrentMempoolTx
--- PASS: TestPocGetMempoolTxSlowReaderBlocksConcurrentMempoolTx (0.10s)
PASS
ok  	github.com/zcash/lightwalletd/frontend	0.107s
```

The test proves:

- first `GetMempoolTx` enters `Send`;
- the first stream blocks in `Send`;
- while the first stream is blocked, a second concurrent `GetMempoolTx` does not complete;
- after releasing the first stream, both requests complete.

## Suggested fix

Do not hold `s.mutex` across client-controlled streaming sends.

Suggested shape:

1. Lock only long enough to refresh/copy shared mempool state.
2. Build a local slice of filtered compact transactions or txids.
3. Unlock.
4. Stream the local slice to the client outside the mutex.

This preserves cache consistency without letting client backpressure hold the shared mempool lock.

## Overlap notes

Known existing lightwalletd lanes:

- `GHSA-x4m7-3gpp-xc36`: transparent-address gRPC resource exhaustion.
- `GHSA-6pvj-cgjw-wjgg`: allocation/throttling/deadlock.

This `GetMempoolTx` mutex-held streaming issue is not the same as the transparent-address materialization issue or the block-range cancellation worker leak.

Because `GHSA-6pvj-cgjw-wjgg` is broad and already uses a deadlock/throttling framing, maintainers may reasonably merge this as an addendum rather than create a separate advisory.

## Disclosure notes

This report is intentionally conservative: private GitHub advisory route only, no public disclosure, no bounty math, and no severity overclaim.

