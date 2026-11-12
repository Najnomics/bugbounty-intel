# GHSA-qfmh-cxw4-9h66: debug_traceTransaction and trace_* RPC methods missing server-side EVM step cap — incomplete fix for GHSA-4776-8c3f-fx7g

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-qfmh-cxw4-9h66 |
| CVE | none assigned |
| Severity | medium |
| CWE | CWE-400 |
| Published | 2026-10-07T23:15:24Z |
| Updated | 2026-10-07T23:15:24Z |
| Affected | org.hyperledger.besu:besu <= 26.8.1 (patched: 26.9.0) |
| Credits | Maybeyes111 |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-qfmh-cxw4-9h66 |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

### Summary

GHSA-4776-8c3f-fx7g introduced a server-side EVM step cap to bound `debug_traceCall`, `trace_call`, and `trace_callMany`. The accompanying changelog entry for that fix incorrectly claimed coverage of `debug_traceTransaction`. The fix never touched `DebugTraceTransaction.java` and that class is constructed without an `ApiConfiguration`, so no server ceiling is available to it. The same gap applies to the entire `trace_*` block family and `debug_traceBlock/*`.

Any caller with access to these namespaces can trigger unbounded heap growth with a single cheap request, causing OOM and consensus drop — the same impact class as GHSA-4776.

### Affected methods

| Method | Issue |
|--------|-------|
| `debug_traceTransaction` | No `ApiConfiguration` injected; step limit is always 0 (unlimited) |
| `debug_traceBlock` / `ByHash` / `ByNumber` | No step limit |
| `trace_block` / `trace_blockByHash` / `trace_blockByNumber` | No step limit |
| `trace_replayBlockTransactions` | No step limit |
| `trace_rawTransaction` | No step limit |
| `trace_filter` | No step limit |

**Not affected** (fixed in GHSA-4776): `debug_traceCall`, `trace_call`, `trace_callMany`.

### Details

`DebugOperationTracer.capturePreExecutionState()` only enforces a step ceiling when `options.limit() > 0`. When no second argument is supplied to the RPC call, `TraceOptions.DEFAULT` sets `limit=0`, so every step is captured until the transaction's gas budget is exhausted.

With `enableMemory: true`, each step retains a full memory snapshot. At Besu's own step ceiling (1,000,000 steps) and a 1,024-word memory frame, that is ~32 GiB retained per request. Multiple concurrent requests multiply until the RPC worker heap is exhausted.

`AbstractTraceCall.applyServerStepLimit()` — the choke point from GHSA-4776 — is never called on any of the above paths.

### Impact

Remote unauthenticated denial of service via heap exhaustion on any node that has enabled `debug_*` or `trace_*` via `--rpc-http-api` / `--rpc-ws-api`. These namespaces are non-default but documented and commonly enabled. No fund loss, no chain corruption, no consensus impact beyond the affected node's liveness.

### Patches

Fixed in a forthcoming release. Public PR and merge SHA will be added once merged.

### Workarounds

Disable the `DEBUG` and `TRACE` RPC namespaces, or place the RPC endpoint behind a reverse proxy that restricts access to trusted callers.

### References

- GHSA-4776-8c3f-fx7g (incomplete predecessor fix)

## Patches and references

Fixed in Besu 26.9.0.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/e4d39ad64cc4
- Pull request: https://github.com/besu-eth/besu/pull/11378
