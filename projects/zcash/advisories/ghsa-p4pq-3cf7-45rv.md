# GHSA-p4pq-3cf7-45rv: Post-decode cardinality caps allow unauthenticated protobuf requests to OOM-kill lightwalletd

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-p4pq-3cf7-45rv |
| CVE | none assigned |
| Severity | high |
| CWE | CWE-400 |
| Published | 2026-11-18T00:38:32Z |
| Updated | 2026-11-18T00:38:32Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.1 (patched: 0.6.2) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-p4pq-3cf7-45rv |

## Description (verbatim)

## Severity

**High — CVSS 3.1: 7.5 (`AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H`).**

An unauthenticated client can deterministically terminate a public `lightwalletd` process using a small number of ordinary maximum-size gRPC requests over one connection. Four 4 MiB requests OOM-kill a 256 MiB process; 8 kill 512 MiB; and 16 kill 1 GiB. Repeating the wave after an operator or service manager restarts the process restores the denial.

This matches Zcash's formal **High** category for a DoS against light-client server software that enables sustained service denial. The impact is confined to the targeted `lightwalletd` instance: no consensus, funds, privacy, or network-wide effect is claimed.

## Affected asset

- Repository: [`zcash/lightwalletd`](https://github.com/zcash/lightwalletd)
- Components: public gRPC request decoding for `CompactTxStreamer`
- Demonstrated RPCs:
  - `GetMempoolTx`
  - `GetTaddressBalance`
- Confirmed release: [`v0.5.4`](https://github.com/zcash/lightwalletd/releases/tag/v0.5.4), commit `09593edbee4ee68d47e5a53f8ce1c83514c4e8e6`
- Confirmed development revision: `d79cd1100575ff909d70e00d5514a4092df94934`

The relevant protocol, generated-handler, application-handler, and server-construction files are byte-identical at both confirmed revisions. The release pins grpc-go `v1.82.1`; the reviewed development revision pins `v1.83.1`, whose relevant receive defaults and decode order are unchanged.

## Summary

This is an incomplete-remediation bypass of the application-level cardinality caps added for `GHSA-4hp3-3494-3f2m` and `GHSA-x4m7-3gpp-xc36`, not a claim of a novel denial-of-service family. `lightwalletd` bounds expensive repeated request fields with a 20,000-suffix cap in `GetMempoolTx` and a 10,000-address cap in `GetTaddressBalance`, but both caps execute only after grpc-go has fully decoded the caller's protobuf into Go objects. A wire-valid 4 MiB message can encode 2,097,152 empty repeated values, forcing tens to hundreds of MiB of allocation before either cap can protect the process. Four concurrent messages over one normal gRPC connection OOM-kill an unmodified 256 MiB release process without reaching the backend. Supplementary proportional runs killed 512 MiB and 1 GiB victims. Equal-wire controls containing one large field instead of millions of empty fields reach the intended application rejection and leave the process healthy.

## Exposure and attacker model

`lightwalletd` is a wallet-facing backend service whose [documented purpose](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/README.md#L21-L29) is to expose a bandwidth-efficient Zcash interface to mobile and other wallets. The demonstrated methods are part of its normal public `CompactTxStreamer` service, not Darkside, debug, or test-only APIs.

The production server has TLS and no-TLS branches, but neither branch configures request authentication, a method-specific pre-decode limit, or a deliberate `MaxConcurrentStreams` setting ([`cmd/root.go:138-181`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/cmd/root.go#L138-L181)). grpc-go therefore uses its `math.MaxUint32` default for concurrent streams. TLS protects transport; it does not change the protobuf decode order or require a wallet identity. The PoC uses plaintext only inside an isolated Docker network.

The attacker needs only:

- network access to the wallet-facing gRPC service;
- one ordinary gRPC client connection for the demonstrated 256 MiB case; and
- 16 MiB of serialized protobuf payload, plus ordinary gRPC/HTTP/2 framing, sent as four concurrent 4 MiB calls.

No backend RPC credentials, valid address, transaction, chain state, mempool contents, race, or code modification is required. The 1 GiB case used 16 calls and 64 MiB of serialized protobuf payload over one connection.

## Root cause

### 1. Wire-valid repeated fields have no pre-decode cardinality bound

The protocol exposes the two affected repeated fields:

- [`AddressList.addresses`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/walletrpc/service.proto#L151-L153): `repeated string`
- [`GetMempoolTxRequest.exclude_txid_suffixes`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/walletrpc/service.proto#L158-L174): `repeated bytes`

An empty length-delimited value for field 1 is encoded as two bytes:

```text
0a 00
```

Therefore an exact 4,194,304-byte request contains:

```text
4,194,304 / 2 = 2,097,152 repeated values
```

This is valid protobuf. It is intentionally application-invalid because its cardinality exceeds the published cap; the vulnerability is that the process can die while constructing the object needed to perform that rejection.

On a 64-bit process, the raw element-header floor alone is:

- `[][]byte`: 2,097,152 × 24 bytes = 48 MiB per request;
- `[]string`: 2,097,152 × 16 bytes = 32 MiB per request.

Those floors exclude slice-capacity growth, the 4 MiB wire buffer, grpc-go materialization, protobuf runtime bookkeeping, garbage-collector overhead, and all existing process memory. The exact packaged measurement recorded 90,799,616 bytes (86.6 MiB) of live `Alloc` growth and 250,988,008 bytes (239.4 MiB) of cumulative `TotalAlloc` for one repeated-empty `GetMempoolTxRequest`, versus 4,194,424 bytes for a same-wire-size one-field request.

### 2. Generated handlers decode before application validation

The generated server-streaming handler performs `RecvMsg(m)` before calling `GetMempoolTx` ([`service_grpc.pb.go:769-774`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/walletrpc/service_grpc.pb.go#L769-L774)). The unary handler likewise calls `dec(in)` before dispatching `GetTaddressBalance` or its interceptor ([`service_grpc.pb.go:744-759`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/walletrpc/service_grpc.pb.go#L744-L759)).

Only after those operations complete does application code enforce:

- the 10,000-address limit at [`frontend/service.go:581-586`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/frontend/service.go#L581-L586), reached through [`GetTaddressBalance`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/frontend/service.go#L632-L650); and
- the 20,000-suffix limit at [`frontend/service.go:703-725`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/frontend/service.go#L703-L725).

The intended defenses are therefore bypassed at an earlier allocation boundary: they correctly prevent handler work and backend work, but they cannot prevent the decode allocation required to reach them.

### 3. The generic transport limit bounds wire bytes, not decoded representation

The release's pinned grpc-go v1.82.1 dependency defaults the server receive limit to exactly 4 MiB and the server stream quota to `math.MaxUint32` ([`server.go:60-62`](https://github.com/grpc/grpc-go/blob/v1.82.1/server.go#L60-L62), [`server.go:188-197`](https://github.com/grpc/grpc-go/blob/v1.82.1/server.go#L188-L197)). Its parser rejects only when the encoded length is greater than the configured maximum, so an exact-limit message is accepted ([`rpc_util.go:785-808`](https://github.com/grpc/grpc-go/blob/v1.82.1/rpc_util.go#L785-L808)).

`RecvMsg` passes that buffer into `recv` ([`stream.go:1794-1825`](https://github.com/grpc/grpc-go/blob/v1.82.1/stream.go#L1794-L1825)); `recv` invokes the codec's `Unmarshal` before returning ([`rpc_util.go:1053-1067`](https://github.com/grpc/grpc-go/blob/v1.82.1/rpc_util.go#L1053-L1067)); and the protobuf codec materializes the buffer and calls `proto.Unmarshal` ([`encoding/proto/proto.go:85-96`](https://github.com/grpc/grpc-go/blob/v1.82.1/encoding/proto/proto.go#L85-L96)). The reviewed development revision's grpc-go v1.83.1 dependency retains the same [defaults and exact-limit comparison](https://github.com/grpc/grpc-go/blob/v1.83.1/rpc_util.go#L785-L808) and the same [`RecvMsg` → `recv` → codec path](https://github.com/grpc/grpc-go/blob/v1.83.1/stream.go#L1809-L1839). The transport limit never counts the resulting Go objects.

## Exploit chain

1. The attacker opens one normal connection to the public `CompactTxStreamer` service.
2. They concurrently call either demonstrated RPC four times.
3. Each request has an exact 4 MiB protobuf body containing 2,097,152 empty field-1 values.
4. grpc-go accepts each body because it is not greater than the default receive limit.
5. Before application code runs, protobuf unmarshal repeatedly appends element headers to `[][]byte` or `[]string` values.
6. The overlapping decode allocations exhaust the victim's memory cgroup.
7. The kernel kills `lightwalletd`; Docker records `OOMKilled=true` and exit 137, and all four RPCs terminate.
8. No `getrawmempool` or `getaddressbalance` request reaches the backend.
9. Restart restores the process because the state is not persistent. The same unauthenticated request wave can immediately repeat the kill.

## Demonstrated impact

The exact clean `v0.5.4` release produced:

| Victim memory | Concurrent calls | Protobuf payload | Outcome |
|---:|---:|---:|---|
| 256 MiB | 4 | 16 MiB | `OOMKilled=true`, exit 137 |
| 512 MiB | 8 | 32 MiB | `OOMKilled=true`, exit 137 |
| 1 GiB | 16 | 64 MiB | `OOMKilled=true`, exit 137 |

The 256 MiB row is the controlling self-contained reproduction in this bundle. The 512 MiB and 1 GiB rows are supplementary proportional observations made with the same request construction before the exact-final harness freeze; they are not additional executable modes of the packaged script.

The 256 MiB end-to-end matrix passed three consecutive times using the exact packaged script. Both `GetMempoolTx` and `GetTaddressBalance` were killed in every run. Two mempool runs returned four prompt `Unavailable` statuses; one returned four `DeadlineExceeded` statuses after the container had already recorded the OOM kill. Client status timing is not the success oracle—the independent victim state (`running=false`, `OOMKilled=true`, exit 137) is.

As a supplementary currency check, the reviewed development revision was also built without modification and OOM-killed by four `GetMempoolTx` calls:

```text
LWD_PROTOBUF_CLIENT_DONE started=4 completed=4 errors=4 codes=Unavailable:4 elapsed=124.785084ms
running=false oom=true exit=137
```

### Matched negative controls

For each RPC, the PoC sends four messages with exactly the same 4,194,304-byte wire size but only one field value. Each field contains 4,194,299 bytes; its one-byte tag plus four-byte length varint makes the total exactly 4 MiB.

Those controls:

- return four terminal `InvalidArgument` statuses from application validation;
- leave the 256 MiB victim running;
- record `oom 0` and `oom_kill 0`; and
- leave backend counters unchanged.

A 1 GiB control with 16 same-wire one-field calls also remained alive. This isolates the failure to protobuf representation expansion, rather than the generic 4 MiB body size, startup backend, request count, or cgroup configuration.

## Proof of concept

GitHub private vulnerability reports do not accept file attachments. The complete frozen recipient archive—including the self-contained `reproduce.sh`, small Go harness, manifest, and this report—is available as a base64-encoded file in this unlisted secret gist:

- Gist: https://gist.github.com/saxenism/b7256dc5c5e62c0fe15dc4015f5b8bd1
- Raw base64 payload: https://gist.githubusercontent.com/saxenism/b7256dc5c5e62c0fe15dc4015f5b8bd1/raw/9741ce7030f36340c2dc06dc39f0ddc7658bbca9/lightwalletd-protobuf-decode-disclosure-v1.tar.gz.b64
- Decoded archive SHA-256: `0cc4441cd0a044d290490e43072d7893edafb699babe305c5a2520174088d964`

Download, decode, verify, and reproduce it with:

```bash
curl -fL "https://gist.githubusercontent.com/saxenism/b7256dc5c5e62c0fe15dc4015f5b8bd1/raw/9741ce7030f36340c2dc06dc39f0ddc7658bbca9/lightwalletd-protobuf-decode-disclosure-v1.tar.gz.b64" -o lightwalletd-protobuf-decode-disclosure-v1.tar.gz.b64
base64 -d lightwalletd-protobuf-decode-disclosure-v1.tar.gz.b64 > lightwalletd-protobuf-decode-disclosure-v1.tar.gz
printf "%s  %s\n" "0cc4441cd0a044d290490e43072d7893edafb699babe305c5a2520174088d964" "lightwalletd-protobuf-decode-disclosure-v1.tar.gz" | shasum -a 256 -c -
tar -xzf lightwalletd-protobuf-decode-disclosure-v1.tar.gz
cd lightwalletd-protobuf-decode-disclosure-v1
./verify-bundle.sh
./reproduce.sh
```

The archive never contacts a public Zcash service. GitHub secret gists are unlisted rather than access-controlled, so anyone holding the URL can read the payload.

Requirements:

- Docker with Linux cgroup v2 memory-controller support;
- Git; and
- outbound access to GitHub and the pinned Docker image on the first run.

Run:

```bash
./verify-bundle.sh
./reproduce.sh
```

The script clones and asserts clean `v0.5.4`, builds unmodified `lightwalletd`, creates an isolated Docker network, and runs the client and synthetic startup backend outside the victim cgroup. It then runs both positive cases, restart checks, and equal-wire controls. Every security assertion uses an explicit fail-closed branch.

Expected final output:

```text
LWD_PROTOBUF_RESULT release=v0.5.4 mempool_oom=true balance_oom=true equal_wire_controls_oom=false backend_requests_during_cases=0 restart_recovers=true
```

Load-bearing intermediate output includes:

```text
LWD_PROTOBUF_CONNECTIONS method=mempool observed=1 expected=1
LWD_PROTOBUF_POSITIVE method=mempool running=false oom=true exit=137
LWD_PROTOBUF_CONTROL method=mempool running=true oom=false events=low 0,high 0,max 0,oom 0,oom_kill 0,oom_group_kill 0,
LWD_PROTOBUF_POSITIVE method=balance running=false oom=true exit=137
LWD_PROTOBUF_CONTROL method=balance running=true oom=false events=low 0,high 0,max 0,oom 0,oom_kill 0,oom_group_kill 0,
```

### Fault-injection clarification

The PoC does not modify `lightwalletd`, grpc-go, or protobuf and uses no failpoint. The 256 MiB cgroup-v2 limit is a controlled victim-memory configuration used to make the terminal effect inexpensive to reproduce. Supplementary 512 MiB and 1 GiB proportional checks demonstrate that the condition is not created by that specific limit.

The backend is synthetic only because `lightwalletd` requires startup metadata. It runs outside the victim cgroup, and the script snapshots its per-method counters after every victim starts. Exact counter equality before and after each request wave proves that no mempool or balance backend operation occurs. The vulnerable allocation necessarily precedes application cardinality validation; the evidence does not require claiming that no handler invocation completes before process death. Backend behavior is not an exploit precondition.

## Operational realism and recovery

The PoC uses the full production server binary and the normal TCP → HTTP/2 → grpc-go → generated handler → protobuf path. One actual connection is observed through `lightwalletd`'s own `grpc_server_connections_current` metric before the requests are released. The attack uses no compression, custom codec, raw frame injection, malformed protobuf, or reduced gRPC message-size setting.

The process loss is not durable. Starting the killed container again restores the RPC and the one-field control returns `InvalidArgument`. This does not prevent sustained denial: the attacker can send the same finite request wave after each automatic or operator restart. A larger instance requires proportionally more calls; the tested 1 GiB construction remains within one ordinary client connection.

No successful attack against a public Mainnet or Testnet service was attempted or observed.

## Relationship to public prior art

This report is an incomplete-remediation follow-up, not a claim of a novel resource-exhaustion family.

- [`GHSA-4hp3-3494-3f2m`](https://github.com/zcash/lightwalletd/security/advisories/GHSA-4hp3-3494-3f2m) documented unbounded `GetMempoolTx` suffix-list processing. The 0.5.1 fix added the current 20,000-element application cap and moved transformation before the method mutex.
- [`GHSA-x4m7-3gpp-xc36`](https://github.com/zcash/lightwalletd/security/advisories/GHSA-x4m7-3gpp-xc36) documented transparent-address resource exhaustion. Version 0.5.4 added the current 10,000-address cap to the unary balance path.
- Public [PR #574](https://github.com/zcash/lightwalletd/pull/574) records the first fix's intent and tests.

Those fixes stop post-decode application and backend amplification. The current failure occurs earlier: generic protobuf unmarshal expands an accepted wire message before either cap can execute. The same construction crossing both independently added defenses demonstrates the shared boundary.

This is distinct from oversized single-blob handler work such as `SendTransaction`: here, the dangerous allocation happens while materializing repeated-field structure, before application cardinality validation can protect the process, and no backend operation occurs.

## Recommended remediation

Protobuf is behaving according to its repeated-field semantics; the application-level defect is relying on post-decode cardinality caps while admitting a representation whose decoded cost can exceed the server's memory budget. Enforce semantic field cardinality before protobuf constructs the repeated Go slices. A durable fix can use a type-aware gRPC codec or generated unmarshal path that performs an allocation-free `protowire` preflight for the affected request types, rejecting field 1 once its occurrence count exceeds the corresponding cap. The preflight must run before `proto.Unmarshal`; a validator or interceptor invoked after standard unary decoding is too late.

Defense in depth should also include:

1. an aggregate admission budget for concurrent inbound request decoding across all connections;
2. a deliberate `MaxConcurrentStreams` value plus connection/per-source limits;
3. smaller method-specific receive limits where protocol compatibility permits; and
4. integration tests that send exact-limit repeated-empty messages concurrently under a memory cgroup and assert rejection without process loss.

Regression tests should cover both generated handler shapes—unary and server-streaming—and retain the same-wire one-field controls.

## References

- [Zcash security policy and High DoS category](https://github.com/zcash/zcash/blob/558f686599586f55def3db86955d74d3be44605e/SECURITY.md#L25-L31)
- [Zcash organization private-report routes, including `lightwalletd`](https://github.com/zcash/.github/blob/main/SECURITY.md#receiving-disclosures)
- [`lightwalletd` v0.5.4 source](https://github.com/zcash/lightwalletd/tree/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6)
- [Reviewed development revision](https://github.com/zcash/lightwalletd/commit/d79cd1100575ff909d70e00d5514a4092df94934)
- [grpc-go v1.82.1 server defaults](https://github.com/grpc/grpc-go/blob/v1.82.1/server.go#L60-L62)

---

[Rahul Saxena](https://x.com/saxenism)  
Founder, [Bluethroat Labs](https://bluethroatlabs.com)

