# GHSA-x4m7-3gpp-xc36: lightwalletd transparent-address gRPC resource-exhaustion DoS

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-x4m7-3gpp-xc36 |
| CVE | none assigned |
| Severity | high (CVSS 7.5) |
| CWE | CWE-400, CWE-770 |
| Published | 2026-07-26T18:54:49Z |
| Updated | 2026-08-27T18:59:45Z |
| Affected | github.com/zcash/lightwalletd <= v0.4.19 (patched: 0.5.0) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-x4m7-3gpp-xc36 |

## Description (verbatim)

# v2 update: lightwalletd transparent-address gRPC resource-exhaustion DoS

Advisory: `GHSA-x4m7-3gpp-xc36`
Repository: `zcash/lightwalletd`
Reporter: `Zk-nd3r` / Frontier Compute
Current validation commit: `3870883667dc95f85fe3810321735067be39eef3` (`master`, `v0.4.19-2-g3870883`)
Previously submitted commit: `028401c4c4a7c8c386c81212324cc8083eed7510` (`v0.4.19`)
Status requested: keep in private triage, update affected range and proof anchors.

## Executive Summary

This is a v2 update to the existing private advisory. The transparent-address gRPC resource-exhaustion issue is still present on current `master` at commit `3870883667dc95f85fe3810321735067be39eef3`, after `v0.4.19`.

On deployments that expose `lightwalletd` beyond localhost, unauthenticated clients can trigger unbounded client-stream accumulation and full-result materialization in transparent-address RPCs before server-side truncation can take effect. The affected paths are:

- `GetTaddressBalanceStream`: stores every client-streamed address in memory before validation and before the backend balance request.
- `GetTaddressTransactions` / `GetTaddressTxids`: materializes the full `getaddresstxids` result, then performs per-transaction backend hydration. The 30-second timeout starts after the txid-array unmarshal, and `GetTransaction(ctx, ...)` does not use the context for its raw backend RPC.
- `GetAddressUtxos` / `GetAddressUtxosStream`: materializes the full `getaddressutxos` response, then applies `StartHeight` and `MaxEntries`.

This is distinct from `GHSA-6pvj-cgjw-wjgg`, which covers `GetBlockRange` worker/goroutine leakage after stream send failure. This advisory covers transparent-address RPC accumulation and full-result materialization.

No public endpoint scanning or mainnet stress testing was performed for this update. Validation is source-based against current `master`, plus the previously submitted local UTXO materialization unit-test PoC.

## Metadata Pack

Proposed GHSA metadata:

- Severity: High
- CVSS 3.1: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H`
- CVSS score: 7.5
- CWEs:
  - `CWE-400`: Uncontrolled Resource Consumption
  - `CWE-770`: Allocation of Resources Without Limits or Throttling
- Ecosystem: Go
- Package: `github.com/zcash/lightwalletd`
- Vulnerable range: `<= v0.4.19`
- Patched versions: none known at time of this update
- Confirmed affected: `v0.4.19` and current `master` commit `3870883667dc95f85fe3810321735067be39eef3`

CVSS vector rationale:

- `AV:N`: the affected gRPC methods are network-accessible when lightwalletd is deployed as a public wallet backend.
- `AC:L`: ordinary valid gRPC requests are sufficient. No race, chain reorg, custom binary payload, or authentication bypass is required.
- `PR:N`: the affected wallet-service RPCs are not gated by application-layer authentication.
- `UI:N`: no user interaction is needed after the request is sent.
- `S:U`: impact is within the vulnerable lightwalletd service and its backend capacity.
- `C:N` and `I:N`: no confidentiality or integrity impact is claimed.
- `A:H`: the reachable outcome is resource exhaustion: memory growth, backend fanout, request starvation, and plausible OOM/restart under sustained or sufficiently large requests.

ZCG payout / project SECURITY.md intake mapping:

- Category: Supporting Infrastructure (`lightwalletd` is explicitly in scope as a light client / wallet infrastructure component).
- Proposed severity: High for public deployments because unauthenticated network clients can force unbounded memory growth or full backend materialization in wallet-service RPCs.
- Conservative fallback if maintainers require measured RSS/OOM data: Medium availability issue, still in the Supporting Infrastructure payout track.

## Current-Master Code Anchors

All line references below are for commit `3870883667dc95f85fe3810321735067be39eef3`.

### Public RPC Surface

`walletrpc/service.proto` exposes the affected methods:

- `service.proto:280`: `GetTaddressTxids`
- `service.proto:284`: `GetTaddressTransactions`
- `service.proto:287`: `GetTaddressBalanceStream`
- `service.proto:318`: `GetAddressUtxos`
- `service.proto:319`: `GetAddressUtxosStream`

### Server Construction

`cmd/root.go` constructs the gRPC server with Prometheus and logging interceptors but without an application-level request deadline, client-stream count cap, or max-concurrent-stream limit visible at this layer:

- `cmd/root.go:142-150`: insecure/no-TLS server path
- `cmd/root.go:169-177`: TLS server path

### Finding 1: `GetTaddressBalanceStream` Accumulates Before Validation

`frontend/service.go:540-552`:

- initializes `addressList := make([]string, 0)`
- loops on `addresses.Recv()`
- appends `addr.Address` to `addressList` for every received message
- validates only after EOF, when calling `getTaddressBalanceZcashdRpc(addressList)`

The important detail is ordering: `getTaddressBalanceZcashdRpc` validates addresses at `frontend/service.go:492-497`, but `GetTaddressBalanceStream` appends before that. A client can therefore hold memory with repeated streamed address messages before any validation or backend call occurs.

Impact: one long-lived client-stream can grow process memory linearly with message count and message size until the client closes, the process is restarted, or resource limits intervene.

### Finding 2: `GetTaddressTransactions` Materializes and Fans Out

`frontend/service.go:95-155`:

- validates a single t-address
- accepts a start height and optional end height
- calls backend `getaddresstxids`
- unmarshals the full result into `var txids []string` at `frontend/service.go:132-137`
- creates a 30-second timeout only after unmarshal at `frontend/service.go:139`
- loops every txid and calls `s.GetTransaction(timeout, ...)` at `frontend/service.go:142-147`

`frontend/service.go:386-414`:

- `GetTransaction(ctx, ...)` accepts a context parameter
- the backend `common.RawRequest("getrawtransaction", params)` call at `frontend/service.go:402` does not use that context

The timeout therefore does not bound the backend `getaddresstxids` call, the full txid-array allocation, or the per-transaction backend RPC fanout.

Impact: one request against a hot transparent address and large block span can allocate a large txid array and then occupy backend capacity with one raw-transaction lookup per txid.

### Finding 3: `GetAddressUtxos` Materializes Before `MaxEntries`

`frontend/service.go:730-795`:

- validates addresses
- sends backend `getaddressutxos` with only the address list
- unmarshals the full backend result into `var utxosReply []common.ZcashdRpcReplyGetaddressutxos` at `frontend/service.go:757-762`
- applies `StartHeight` and `MaxEntries` afterward at `frontend/service.go:763-770`

`frontend/service.go:798-810` exposes the unary `GetAddressUtxos` wrapper and collects replies into a fresh slice.

`frontend/service.go:883-891` exposes `GetAddressUtxosStream`.

Impact: `MaxEntries=1` does not bound backend work or typed-slice allocation. The process cost scales with the full UTXO set returned by the backend, not with the caller's cap.

## Reproduction Shapes

These are representative request shapes for maintainers to reproduce in an isolated environment. They should not be run against public infrastructure.

### Finding 1: Client-Stream Accumulation

Open `GetTaddressBalanceStream` and stream a large number of `Address` messages. EOF is not required to keep the server-side slice resident.

```python
import grpc
import service_pb2
import service_pb2_grpc

ch = grpc.insecure_channel("127.0.0.1:9067")
stub = service_pb2_grpc.CompactTxStreamerStub(ch)

def gen():
    for _ in range(500_000):
        yield service_pb2.Address(address="x" * 1024)

stub.GetTaddressBalanceStream(gen())
```

Expected result in an unpatched isolated service: server RSS grows roughly linearly with accepted streamed messages before validation occurs.

### Finding 2: Txid Materialization and Fanout

Call `GetTaddressTransactions` for a transparent address with heavy historical use and a broad block range:

```text
grpcurl -plaintext \
  -d '{"address":"t1...hot-address...","range":{"start":{"height":1},"end":{"height":2000000}}}' \
  127.0.0.1:9067 \
  cash.z.wallet.sdk.rpc.CompactTxStreamer/GetTaddressTransactions
```

Expected result in an unpatched isolated service: the full backend txid list is decoded before the 30-second timeout is created, then each txid triggers an uncontexted backend raw-transaction lookup.

### Finding 3: UTXO Materialize-Then-Filter

Call `GetAddressUtxos` with a caller cap:

```text
grpcurl -plaintext \
  -d '{"addresses":["t1...hot-address..."],"startHeight":1,"maxEntries":1}' \
  127.0.0.1:9067 \
  cash.z.wallet.sdk.rpc.CompactTxStreamer/GetAddressUtxos
```

Expected result in an unpatched isolated service: the full backend UTXO array is materialized before the returned list is truncated to one entry.

## Prior Submission and Duplicate Guard

Existing private lightwalletd advisories found in this repository:

- `GHSA-6pvj-cgjw-wjgg`: `GetBlockRange` worker/goroutine leak after send failure. State: triage. Severity: Medium. CWE: `CWE-770`, `CWE-833`. This is a different RPC family and different failure mode.
- `GHSA-x4m7-3gpp-xc36`: this advisory. State: triage. The v2 update here corrects current-master anchors and affected version range.

Adjacent public issues checked:

- `zcash/lightwalletd#314`: generic DoS research context, not this specific handler family.
- `zcash/lightwalletd#329`: generic DoS research context, not this specific handler family.
- `zcash/lightwalletd#387`: transparent RPC passthrough / timeout context, not this resource-exhaustion report.
- `zcash/lightwalletd#498`: large `GetTaddressTxids` results, not the same memory and timeout-bypass report.
- `zcash/lightwalletd#224`: parser DoS class from backend-supplied chain/mempool data, explicitly separate.

Adjacent internal finding:

- The Zaino UTXO materialization report is the same vulnerability class in a separate implementation and repository. It should not be merged with this lightwalletd advisory.

## Recommended Fix

Use defense in depth. Individual caps are useful, but the durable fix is to make every expensive public RPC enforce bounds before backend work and propagate cancellation to backend calls.

Recommended changes:

- Add a configured maximum streamed-address count and maximum streamed-address byte budget to `GetTaddressBalanceStream`.
- Validate each streamed address before appending, or reject invalid address strings immediately.
- Add a configured maximum transparent-history block span and maximum txid count to `GetTaddressTransactions`.
- Make backend JSON-RPC calls context-aware, or run them behind a cancellable worker with a hard timeout.
- For `GetAddressUtxos`, cap address-list size before backend work and avoid full typed-slice materialization before applying `MaxEntries`.
- If zcashd's `getaddressutxos` cannot push down `MaxEntries` / `StartHeight`, document that limitation and enforce server-side ceilings before the backend call.
- Add server-level stream duration / concurrency controls for expensive RPCs.

Example cap for the client-stream path:

```go
const maxStreamAddresses = 10_000
const maxStreamAddressBytes = 2 << 20

var totalBytes int
for {
    addr, err := addresses.Recv()
    if err == io.EOF {
        break
    }
    if err != nil {
        return status.Errorf(codes.Internal, "GetTaddressBalanceStream Recv error: %s", err.Error())
    }
    totalBytes += len(addr.Address)
    if len(addressList) >= maxStreamAddresses || totalBytes > maxStreamAddressBytes {
        return status.Error(codes.ResourceExhausted, "too many streamed addresses")
    }
    if err := checkTaddress(addr.Address); err != nil {
        return err
    }
    addressList = append(addressList, addr.Address)
}
```

## Validation Performed for This Update

- Confirmed private vulnerability reporting is enabled for `zcash/lightwalletd`.
- Confirmed existing advisory `GHSA-x4m7-3gpp-xc36` is in triage and should be updated rather than duplicated.
- Confirmed current local repository state:
  - branch: `master`
  - commit: `3870883667dc95f85fe3810321735067be39eef3`
  - describe: `v0.4.19-2-g3870883`
  - worktree: clean
- Confirmed code anchors listed above exist on current `master`.
- Ran focused package tests:

```text
cd /root/wide-audit/lightwalletd
go test ./frontend

ok  	github.com/zcash/lightwalletd/frontend	0.017s
```

## Request to Maintainers

Affected range metadata is now set to `<= v0.4.19`. The vulnerable code is also present on current `master` at commit `3870883667dc95f85fe3810321735067be39eef3`.

If you want measured RSS/OOM numbers before accepting High severity, I can provide an isolated local harness that exercises `GetTaddressBalanceStream` without touching public infrastructure.

## Residual Risk

- Finding 1 (`GetTaddressBalanceStream` Accumulates Before Validation): fixed in 0.5.0.
- Finding 2 (`GetTaddressTransactions` Materializes and Fans Out): fixed in 0.5.0.
- Finding 3 (`GetAddressUtxos` Materializes Before `MaxEntries`): narrowed in 0.5.4, still present. 0.5.4 collapses repeated addresses before the backend call, so a request naming one address n times no longer asks the backend to look it up n times and return n copies of its UTXOs. Against zcashd that was a real multiplier, since addresses are public and naming one costs the caller nothing, so the 10,000-address limit set the ceiling; zebrad already collapsed duplicates before querying its state, so it was never exposed. What remains is the finding as reported: `StartHeight` and `MaxEntries` are response filters applied after the whole backend result has been unmarshalled, so the UTXO set of even a single named address is still produced by the backend and materialized in full, however narrow a height range or however few entries the caller asked for. 0.5.4 also passes both arguments through to the backend `getaddressutxos` RPC. No released backend implements either argument (they simply ignore the extra JSON keys), so on its own that changes nothing. Zebra merged the other half on 2026-08-25 (ZcashFoundation/zebra#11317, `b2cc75b`), unreleased as of Zebra v6.3.0; a lightwalletd 0.5.4 or later paired with a Zebra release that includes it will bound the backend work as the arguments describe. Tracked separately as GHSA-932p-ww36-57vg.
- Related hardening in 0.5.4, outside the three findings: `GetTaddressBalance` now enforces the same 10,000-address cap as `GetTaddressBalanceStream`, `GetAddressUtxos` and `GetAddressUtxosStream`. Being unary, it takes its whole list in one protobuf message, so its only previous bound was gRPC's 4MB `MaxRecvMsgSize` -- roughly 113,000 addresses at 37 wire bytes each, an order of magnitude above the intended cap, returning an 8-byte balance. `GetTaddressBalance` and `GetTaddressBalanceStream` also deduplicate the address list now, which additionally corrects an inflated balance when the caller named the same address more than once against zcashd.

