# GHSA-4776-8c3f-fx7g: Besu ≤26.7.0 — operator-reachable DoS via debug_traceCall (OOM → consensus drop)

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-4776-8c3f-fx7g |
| CVE | none assigned |
| Severity | medium (CVSS 4.9) |
| CWE | CWE-400 |
| Published | 2026-10-02T02:26:16Z |
| Updated | 2026-10-02T02:26:16Z |
| Affected | org.hyperledger.besu:besu <= 26.7.1 (patched: 26.8.0) |
| Credits | jiapy97, macfarla |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-4776-8c3f-fx7g |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

### Summary
A single, ~318-byte `debug_traceCall` request can force Besu to materialize a multi-gigabyte `structLog` trace entirely in the JVM heap, triggering `java.lang.OutOfMemoryError: Java heap space`. The node freezes on a block and **drops out of consensus for ~10 minutes** (`eth_syncing` returns `false`, i.e. not a catch-up state), then self-recovers after GC with no DB corruption.

Deterministically reproducible on Besu **v26.7.0** (latest release). The other four execution clients (Geth, Nethermind, Erigon, Reth) all survive the same request by bounding or streaming trace output — so a safe behavior is clearly reachable (4:1).

This is an operator-reachable denial-of-service / liveness bug: any caller with access to the `debug_` namespace can knock the node out of consensus with one cheap request.

### Details
**Invariant violated.** A cheap input must not crash a node or drop it from consensus. A tracing RPC must bound its output (size/time/step limit) or stream it, rather than buffer an unbounded trace into the heap.

**Mechanism.** The request uses `stateOverrides` to inject a contract whose bytecode expands memory by ~1 KB and then loops until the RPC gas cap (50M) is exhausted:

- bytecode `0x600062000400525b600756` = expand memory to ~1 KB, then infinite loop.
- With `enableMemory: true`, each step emits the full memory snapshot. The amplification is ~173 bytes of `structLog` per gas, so a 318-byte request produces a ~8.6 GB trace.
- Besu buffers the entire trace in the JVM heap (default max ~15.6 GB). Observed heap: 8.8 GB → 16.4 GB → OOM, plus a Vert.x "Thread blocked" condition.

**Cross-client comparison (identical request).**

| Client | Behavior |
|--------|----------|
| **besu 26.7.0** | heap → 16.4 GB → OOM; RPC 4 ms → 3524 ms → no response; frozen on a block, **dropped from consensus**; unreachable ~10 min; self-recovers after GC and syncs to the same head hash |
| geth | rejects after ~5 s (`execution timeout` — time cap) |
| reth | rejects (`Response is too big` — 160 MB size cap) |
| nethermind | streams (~24.4 GB output), memory stable ~800 MB, stays in consensus |
| erigon | streams (~29.5 GB output), memory stable ~150 MB, stays in consensus |

Isolation confirmed: after self-recovery, replaying the same probe reproduces the OOM / block freeze / HTTP 504 deterministically. No DB corruption — Besu cleanly catches up to the same head hash after GC.

**Relationship to existing issues (we checked; we believe this is not covered).**

- `#9584` "Reduce memory usage of debug_trace* calls" is filed as a *performance enhancement* (redundant per-frame memory snapshots → GC pressure), not a crash/DoS, and is closed. Our finding is that the same underlying unbounded buffering is a remotely-triggerable node crash + consensus drop, still live in 26.7.0.
- `#3786` "OOM on trace_replayBlockTransactions" was a *different* method, fixed in PR `#5131` (v22.x); that fix does not cover the `debug_traceCall` + `stateOverrides` path.

**Suggested remediation.** Apply a size/time/step cap to `debug_trace*` output, or stream it (as Nethermind/Erigon do), instead of buffering the full trace in the heap. Consider `ExitOnOutOfMemoryError` hardening as defense in depth.

### PoC
**Warning:** this will OOM the target Besu node for ~10 minutes. It self-recovers; please do not repeat back-to-back.

Against a Besu 26.7.0 node with the `debug_` namespace enabled:

```bash
curl -s -X POST http://<besu-rpc> -H 'Content-Type: application/json' --data '{
  "jsonrpc":"2.0","id":1,"method":"debug_traceCall",
  "params":[{"to":"0x0000000000000000000000000000000000009999"},"latest",
    {"enableMemory":true,
     "stateOverrides":{"0x0000000000000000000000000000000000009999":
       {"code":"0x600062000400525b600756"}}}]}'
```

Observed on Besu 26.7.0: heap climbs to ~16.4 GB, `OutOfMemoryError`, RPC stops responding, the node freezes on a block and drops out of consensus for ~10 minutes, then recovers after GC. The other four clients reject (time/size cap) or stream the response without crashing.

**Environment.** Besu v26.7.0 (latest) vs Geth v1.17.5-unstable-dddbaa4b, Nethermind v1.39.1, Reth v2.4.1, Erigon 3.5.2 — each on its latest release; Kurtosis 5-client devnet, Lighthouse CL, all nodes fully synced.

### Impact
**Type:** operator-reachable denial-of-service / liveness (not a consensus-safety or fund-loss bug). A single ~318-byte request causes an OOM that takes the node out of consensus for ~10 minutes. Recoverable (JVM has no `ExitOnOutOfMemoryError`; GC reclaims and the node self-heals with no DB corruption).

**Who is impacted:** Besu operators who expose the `debug_` namespace. `debug_*` is not open to the public internet by default, but is commonly enabled on internal, L2, and infrastructure nodes; in those environments any caller that can reach the `debug_` endpoint can repeatedly stall the node and knock it out of consensus. Because a stalled validator/RPC node drops out of consensus while unreachable, this affects liveness/availability rather than just the RPC caller.

We intend to publish this work (an academic paper on differential RPC testing) and propose a disclosure window of the earlier of a fix shipping or 90 days from your acknowledgement. Happy to provide full artifacts on request.

— Peiyang Jia, School of Cyber Science and Technology, Beihang University  
(1120637483@qq.com)

## Patches and references

Fixed in Besu 26.8.0.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/47398b0e32c0
- Pull request: https://github.com/besu-eth/besu/pull/11100
