# GHSA-6ppp-r2gc-9q6v: lightwalletd SendTransaction oversized raw transactions can OOM a targeted node before backend rejection

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-6ppp-r2gc-9q6v |
| CVE | none assigned |
| Severity | high |
| CWE | CWE-400 |
| Published | 2026-07-28T18:24:37Z |
| Updated | 2026-07-28T18:24:37Z |
| Affected | github.com/zcash/lightwalletd <= 0.5.0 (patched: 0.5.1) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-6ppp-r2gc-9q6v |

## Description (verbatim)

## Summary

`lightwalletd`'s public `SendTransaction` gRPC method accepts attacker-controlled `RawTransaction.data` without an application-level raw transaction size cap. The handler only checks for nil input, then hex-encodes the full byte slice, JSON-marshals the expanded hex string, and forwards it to the backend node's `sendrawtransaction` RPC.

This allows an unauthenticated client to send oversized invalid transaction bytes that are eventually rejected by the backend, but only after `lightwalletd` has performed large local allocations and the backend has spent work decoding/parsing the JSON-RPC payload.

A local regtest PoC using a real `zcashd`, an unmodified `lightwalletd`, and public gRPC demonstrates both the single-request amplification and process-level impact:

- One 3.9 MB invalid raw transaction increased request latency from 14 ms to 11505 ms and added about 30 MB of `lightwalletd` heap before rejection.
- Twelve parallel 3.9 MB invalid `SendTransaction` requests OOM-killed a 256 MiB victim `lightwalletd` container with `exit_code=137` and `oom_killed=true`.

## Affected Product

Primary affected target:

- lightwalletd

Product metadata:

- Product: `github.com/zcash/lightwalletd`
- Category: Supporting Infrastructure
- Verified affected version: `v0.4.19-4-g45b2f4c`
- Verified affected commit: `45b2f4cdd4aeb51f0683d43e96a04b5f8a4af683`
- Fixed version: not observed in the reviewed checkout

Validation was performed only on local regtest/local Docker infrastructure. No public mainnet or testnet services were contacted.

## Affected Code

Relevant implementation:

- `frontend/service.go:445`: `SendTransaction` forwards raw transaction bytes to backend JSON-RPC
- `frontend/service.go:456-458`: only nil validation is applied
- `frontend/service.go:461-463`: full `rawtx.Data` is hex-encoded and JSON-marshaled
- `frontend/service.go:467`: expanded payload is forwarded to backend `sendrawtransaction`

Vulnerable code:

```go
func (s *lwdStreamer) SendTransaction(ctx context.Context, rawtx *walletrpc.RawTransaction) (*walletrpc.SendResponse, error) {
    ...
    if rawtx == nil || rawtx.Data == nil {
        return nil, status.Error(codes.InvalidArgument, "bad transaction data")
    }

    params := make([]json.RawMessage, 1)
    txJSON, err := json.Marshal(hex.EncodeToString(rawtx.Data))
    if err != nil {
        return nil, status.Errorf(codes.InvalidArgument, "cannot marshal tx: %s", err.Error())
    }
    params[0] = txJSON
    result, rpcErr := common.RawRequest("sendrawtransaction", params)
    ...
}
```

There is no size check before `hex.EncodeToString`. A 3.9 MB gRPC byte field becomes about 7.8 MB of hex string before JSON-RPC overhead and backend processing.

## Protocol-Level Mechanism

`SendTransaction` is the public wallet-facing broadcast API. The client provides raw transaction bytes, and `lightwalletd` acts as a bridge to the backend node's `sendrawtransaction` JSON-RPC method:

```text
public gRPC RawTransaction.data -> lightwalletd hex encoding -> JSON-RPC sendrawtransaction -> backend rejection
```

The issue is not that the backend accepts the payload. It rejects the PoC payload with `-22`, which is expected for invalid transaction bytes. The issue is that `lightwalletd` performs expensive local expansion and forwards a large invalid payload before applying any service-level size bound.

This creates a cross-layer amplification problem. The gRPC request is near the generic inbound message limit, but the handler expands it into a much larger JSON string and makes the backend process it. A wallet broadcast endpoint should reject oversized or obviously out-of-policy raw transaction payloads before hex/JSON expansion and backend forwarding.

## Finding Description

An unauthenticated attacker can trigger the issue through the normal public wallet-facing gRPC API:

1. The attacker connects to `CompactTxStreamer/SendTransaction`.
2. The attacker sends `RawTransaction{data: <large byte string>}` close to the gRPC inbound message-size limit.
3. The byte string does not need to be a valid transaction.
4. `lightwalletd` accepts the non-nil `data` field.
5. `lightwalletd` hex-encodes the full byte slice, approximately doubling its size.
6. `lightwalletd` JSON-marshals the expanded hex string.
7. `lightwalletd` sends the expanded payload to backend `sendrawtransaction`.
8. The backend rejects the payload, but only after both services have spent CPU and memory on a request that could have been rejected locally.

The PoC uses a 1-byte invalid transaction as the control and a 3.9 MB invalid transaction as the attack payload. Both return backend error code `-22`, confirming the backend path is reached in both cases.

## Impact

Impact level: Medium.

This is a targeted resource-exhaustion issue against an individual `lightwalletd` instance and its backend node.

Single-request localnet evidence:

```text
rawtx_bytes=1 response_code=-22 response_msg_len=91 duration_ms=14
rawtx_bytes=3900000 response_code=-22 response_msg_len=91 duration_ms=11505
baseline_ms=14 attack_ms=11505 slowdown_x=793.34
heap_before=1068656 heap_after_baseline=2499608 heap_after_attack=32677080 heap_delta_attack=30177472 objects_before=4330 objects_after_attack=4739 objects_delta_attack=409
```

Process-death localnet/cgroup evidence:

```text
zcashd_bridge_ip=172.17.0.2 victim_memory=256m rawtx_bytes=3900000 parallel=12
rawtx_bytes=1 response_code=-22 response_msg_len=91 duration_ms=9
parallel=11 rawtx_bytes=3900000 response_code=-22 response_msg_len=91 duration_ms=13600
parallel=7 rawtx_bytes=3900000 grpc_error=rpc error: code = Unavailable desc = error reading from server: EOF duration_ms=13896
parallel_total=12 rawtx_bytes=3900000 duration_ms=13897
client_exit_code=1
victim_status=exited running=false exit_code=137 oom_killed=true
```

Practical impact:

- A public unauthenticated client can force large heap allocations in `lightwalletd`.
- A public unauthenticated client can force backend `sendrawtransaction` decode/parse work for oversized invalid payloads.
- Repeated or parallel requests can degrade the transaction broadcast endpoint and backend RPC service.
- Under a 256 MiB memory limit, twelve parallel requests OOM-killed the targeted `lightwalletd` process.
- Wallet clients using that instance lose service until the operator or supervisor restarts it.
- The attack is non-distributed: each `lightwalletd` endpoint/backend pair must be targeted individually.

This does not affect Zcash consensus, does not steal funds, does not compromise wallet keys, and does not automatically propagate across nodes. The proposed severity is Medium because the demonstrated outcome is targeted supporting-infrastructure denial of service, not a network-wide outage or consensus failure.

## Likelihood

Likelihood level: Medium.

The reachable entry point is public and unauthenticated in normal `lightwalletd` deployments that expose wallet gRPC. The attack does not require:

- valid transaction bytes,
- funded addresses,
- backend RPC credentials,
- host access,
- a reorg,
- mempool timing,
- chain history setup,
- privileged flags such as Darkside or Ping.

The main practical constraints are request size, concurrency, and victim memory. A single near-limit request reliably causes large latency and heap amplification. Process death in the PoC uses twelve concurrent near-limit requests and a 256 MiB victim memory limit. This is realistic for memory-constrained service deployments, but it is not universal. Larger deployments may experience latency and memory pressure rather than immediate OOM.

Likelihood is therefore Medium rather than High.

## Severity Discussion

Per the ZCG Security & Vulnerability Disclosure Initiative, `lightwalletd` is Supporting Infrastructure. This report recommends Medium because the bug allows repeated, unauthenticated targeted denial of service against one wallet-supporting infrastructure node.

The issue fits Medium better than Low because the PoC demonstrates both strong single-request amplification and process-level availability loss under a bounded-memory victim:

- one request caused about 793x latency increase and about 30 MB additional heap,
- twelve parallel requests OOM-killed the victim process.

The report does not claim High because the impact is targeted and non-distributed. It does not affect consensus, does not propagate through the Zcash network, and does not compromise funds or wallet secrets.

## Attacker Model, Scope, and Triage Notes

Attacker model:

- The attacker can connect to the public `lightwalletd` gRPC service.
- The attacker does not need access to the `lightwalletd` host.
- The attacker does not need backend RPC credentials.
- The attacker does not need wallet keys, validator privileges, mining power, or admin access.
- The attacker sends one or more large `SendTransaction` requests with invalid raw bytes.

Scope fit:

- `lightwalletd` is listed under Supporting Infrastructure.
- The affected method is a normal public wallet-facing gRPC API.
- The issue is a targeted non-distributed DoS/resource-amplification finding against one supporting-infrastructure instance.
- The PoC is isolated to local regtest and does not touch public mainnet or testnet infrastructure.
- The PoC does not use Darkside APIs, `--ping-very-insecure`, or any test-only gRPC method.

Expected pushback:

- Pushback: "The payload is invalid and rejected by the backend."
  - Response: Correct. The vulnerability is that invalid oversized data is expanded and forwarded before local service bounds are enforced. Rejection happens after the expensive work.

- Pushback: "The process-death PoC uses a 256 MiB memory limit."
  - Response: The memory limit is a safe localnet way to demonstrate process death without risking the host. The same amplification is also measured directly through Go heap metrics in the single-request PoC and the eight-parallel near-OOM run.

- Pushback: "A larger deployment may not OOM from twelve requests."
  - Response: That is why severity is Medium. Larger deployments still spend unnecessary CPU, memory, and backend RPC time on public invalid payloads, and repeated requests can maintain pressure.

## Proof of Concept

[poc.zip](https://drive.google.com/file/d/1uk2iiPHiHtStPg8VE2x0VE2UYVP2XATI/view?usp=sharing)

### Archive Contents

PoC file list:

- `poc/sendtx_try.sh`
- `poc/sendtx_cgroup_try.sh`
- `poc/sendtx_client.go`
- `poc/localnet-observed-output.txt`

### Reproduction

Run from the root of a `github.com/zcash/lightwalletd` checkout after unpacking `poc.zip`.

Single-request amplification:

```bash
unzip poc.zip
LARGE=3900000 bash poc/sendtx_try.sh
```

Process-death cgroup PoC:

```bash
unzip poc.zip
LWD_MEM=256m PARALLEL=12 LARGE=3900000 bash poc/sendtx_cgroup_try.sh
```

The single-request script performs the following sequence end-to-end:

1. Builds `lightwalletd` from the reviewed repository.
2. Starts a local `zcashd` regtest Docker container with `txindex=1`, `lightwalletd=1`, and `experimentalfeatures=1`.
3. Mines one local regtest block.
4. Starts an unmodified `lightwalletd` instance against the local backend.
5. Calls public `SendTransaction` with a 1-byte invalid raw transaction control payload.
6. Calls public `SendTransaction` with a large invalid raw transaction payload.
7. Prints request latency, slowdown, heap growth, and heap object growth.

The cgroup script starts the victim `lightwalletd` instance in a Docker container with a configurable memory limit, then sends parallel large invalid `SendTransaction` requests and prints the victim container status.

### Expected Output

Expected vulnerable single-request output includes:

```text
rawtx_bytes=1 response_code=-22 response_msg_len=91 duration_ms=14
rawtx_bytes=3900000 response_code=-22 response_msg_len=91 duration_ms=11505
baseline_ms=14 attack_ms=11505 slowdown_x=793.34
heap_before=1068656 heap_after_baseline=2499608 heap_after_attack=32677080 heap_delta_attack=30177472 objects_before=4330 objects_after_attack=4739 objects_delta_attack=409
```

Expected vulnerable cgroup output includes:

```text
zcashd_bridge_ip=172.17.0.2 victim_memory=256m rawtx_bytes=3900000 parallel=12
rawtx_bytes=1 response_code=-22 response_msg_len=91 duration_ms=9
parallel_total=12 rawtx_bytes=3900000 duration_ms=13897
client_exit_code=1
victim_status=exited running=false exit_code=137 oom_killed=true
```

### Environment Notes

Requirements:

- Docker
- Go
- `curl`

The PoC may pull `electriccoinco/zcashd:latest` if it is not already present locally. The PoC uses only local regtest containers and host-local services. It does not contact public mainnet or public testnet infrastructure.

## Reproduction Notes

The default `LARGE=3900000` is intentionally close to the generic gRPC inbound message-size limit while remaining accepted by the tested server.

The backend error code `-22` is expected. It confirms that the payload reached backend `sendrawtransaction`; the security issue is the work performed before rejection.

An additional cgroup run with `PARALLEL=8` did not kill the process but reached near-OOM pressure:

```text
parallel_total=8 rawtx_bytes=3900000 duration_ms=9557
baseline_ms=9 attack_ms=9557 slowdown_x=966.91
heap_delta_attack=132232024
victim_status=running running=true exit_code=0 oom_killed=false
victim_memory_usage=255.4MiB / 256MiB victim_memory_percent=99.77%
```

This supports that the process-death result is caused by progressive memory pressure from accepted public requests, not by a privileged or test-only path.

## Recommended Fix

Reject oversized raw transaction payloads before hex encoding, JSON marshaling, or backend forwarding.

Recommended root-cause fixes:

1. Add an application-level maximum raw transaction byte length for `SendTransaction`.
2. Align the limit with Zcash transaction acceptance constraints and deployment policy.
3. Return `codes.ResourceExhausted` or `codes.InvalidArgument` before `hex.EncodeToString` for oversized payloads.
4. Add metrics and rate limits for rejected oversized `SendTransaction` requests.
5. Consider per-method concurrency limits for `SendTransaction` so multiple large broadcasts cannot exhaust the process.

Example sketch:

```go
const maxSendTransactionBytes = 2_000_000 // choose a consensus-aware/configurable cap

func (s *lwdStreamer) SendTransaction(ctx context.Context, rawtx *walletrpc.RawTransaction) (*walletrpc.SendResponse, error) {
    if rawtx == nil || rawtx.Data == nil {
        return nil, status.Error(codes.InvalidArgument, "SendTransaction: missing transaction data")
    }
    if len(rawtx.Data) == 0 {
        return nil, status.Error(codes.InvalidArgument, "SendTransaction: empty transaction data")
    }
    if len(rawtx.Data) > maxSendTransactionBytes {
        return nil, status.Errorf(
            codes.ResourceExhausted,
            "SendTransaction: raw transaction is too large: %d bytes",
            len(rawtx.Data),
        )
    }

    txHex := hex.EncodeToString(rawtx.Data)
    txJSON, err := json.Marshal(txHex)
    if err != nil {
        return nil, status.Errorf(codes.InvalidArgument, "cannot marshal tx: %s", err.Error())
    }

    result, rpcErr := common.RawRequest("sendrawtransaction", []json.RawMessage{txJSON})
    ...
}
```

Defense in depth:

- Configure per-method request size limits below the generic gRPC default for `SendTransaction`.
- Add a bounded worker pool or semaphore around backend `sendrawtransaction`.
- Propagate request context/deadlines to backend RPC calls where supported.
- Log and metric oversized transaction rejections separately from backend transaction validation failures.

## References

- `frontend/service.go`
- `walletrpc/service.proto`
- `CompactTxStreamer/SendTransaction`
- `RawTransaction.data`
- ZCG category: Supporting Infrastructure

