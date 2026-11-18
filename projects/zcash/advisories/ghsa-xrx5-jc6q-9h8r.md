# GHSA-xrx5-jc6q-9h8r: Incomplete GHSA-6ppp remediation: concurrent in-limit SendTransaction requests OOM lightwalletd

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-xrx5-jc6q-9h8r |
| CVE | none assigned |
| Severity | high |
| CWE | CWE-400, CWE-770 |
| Published | 2026-11-18T00:38:29Z |
| Updated | 2026-11-18T00:38:29Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.1 (patched: 0.6.2) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-xrx5-jc6q-9h8r |

## Description (verbatim)

## Severity

**High (CVSS 3.1: 7.5, `AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H`).** An unauthenticated client with network access to lightwalletd's wallet-facing gRPC service can OOM-kill the entire process using individually in-limit `SendTransaction` messages. The Zcash security policy places DoS against light-client server software in High when it enables sustained denial or unbounded resource consumption.

This is a process-availability issue. It does not cause consensus divergence, funds loss, or durable state corruption. A restart restores service, but the same bounded request wave kills the replacement process again.

## Affected asset and versions

- Repository: `zcash/lightwalletd`
- Method: `cash.z.wallet.sdk.rpc.CompactTxStreamer/SendTransaction`
- Affected incomplete-remediation range: `>= 0.5.1, <= 0.5.4`
- Released version reproduced: `v0.5.4`, commit `09593edbee4ee68d47e5a53f8ce1c83514c4e8e6`
- Current `master` verified affected by source identity: `d79cd1100575ff909d70e00d5514a4092df94934` on 2026-09-08

The load-bearing `cmd/root.go`, `frontend/service.go`, and `frontend/rawrequest.go` files are byte-identical between v0.5.4 and that current commit. Current master updates grpc-go from 1.82.1 to 1.83.1; the relevant `server.go` is also byte-identical and retains the unset `math.MaxUint32` stream default.

## Summary

The v0.5.1 remediation for [GHSA-6ppp-r2gc-9q6v](https://github.com/zcash/lightwalletd/security/advisories/GHSA-6ppp-r2gc-9q6v) rejects a `SendTransaction` body only when that individual body exceeds 2,000,000 bytes. It adds no process-wide concurrency or byte budget.

For every admitted call, gRPC first decodes and retains `RawTransaction.data`. Lightwalletd then hex-expands the data, JSON-marshals it, and starts an independent backend HTTP request. Concurrent messages below the repaired per-message limit therefore multiply several live representations until the process crosses its memory limit.

The controlling witness uses real TLS and an unmodified ingress-nginx controller in front of an exact, unmodified lightwalletd v0.5.4 process. It keeps ingress-nginx's rendered defaults of `client_max_body_size 1m` and `http2_max_concurrent_streams 128`. Seventeen ordinary client connections submit 2,000 messages with 900,000 data bytes each. The serialized protobuf is 900,004 bytes and the complete length-prefixed gRPC message is 900,009 bytes, below 1,048,576 bytes.

The victim has a 3 GiB cgroup limit and zero swap, matching the documented zec.rocks lightwalletd resource profile. It is OOM-killed with exit code 137. A fresh-process control uses the same 2,000 calls, 17 connections, TLS ingress, pacing, and immediate-reject backend with 100-byte data values; all 2,000 calls complete without error and the process remains alive. A new victim serves a request after restart, then the same attack kills it again.

## Root cause

### 1. The per-message repair is not aggregate admission control

`SendTransaction` accepts every non-nil body of at most 2,000,000 bytes, then hex-encodes and JSON-marshals the entire body before forwarding it:

- [`frontend/service.go:508-546`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/frontend/service.go#L508-L546)

Each 900,000-byte PoC data value passes the check. Its backend JSON-RPC body is 1,800,068 bytes.

### 2. Server concurrency is unbounded across attacker connections

Both server variants call `grpc.NewServer(...)` without `grpc.MaxConcurrentStreams`, a process-wide byte limiter, a per-client quota, or client authentication:

- [`cmd/root.go:138-181`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/cmd/root.go#L138-L181)
- [`grpc-go/server.go:188-196`](https://github.com/grpc/grpc-go/blob/v1.82.1/server.go#L188-L196)
- [`grpc-go/internal/transport/http2_server.go:181-191`](https://github.com/grpc/grpc-go/blob/v1.82.1/internal/transport/http2_server.go#L181-L191)

Ingress-nginx's default 128 concurrent HTTP/2 streams is per connection, not process-wide. The witness deliberately uses 17 connections, allowing all 2,000 control calls to traverse the proxy while leaving the default unchanged.

### 3. Backend work has no aggregate cap

The context-aware backend client has a 60-second request timeout and no per-host connection limit. Each request sets `Connection: close`. Transport failure can cause ten total attempts (at most nine retries):

- [`frontend/rawrequest.go:24-27`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/frontend/rawrequest.go#L24-L27)
- [`frontend/rawrequest.go:42-69`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/frontend/rawrequest.go#L42-L69)
- [`frontend/rawrequest.go:89-148`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/frontend/rawrequest.go#L89-L148)

The PoC backend does not exploit timeout or retention. It fully reads each JSON-RPC body and immediately returns an ordinary application rejection.

## Reachability and documented deployment boundary

The attacker needs only network access to an exposed lightwalletd gRPC listener. They need no wallet key, funded input, backend credential, node access, mining power, chain reorganization, or malformed transport frame.

The zec.rocks chart at commit `9c56ad4cd38e857d920ace0152ef1d92c5e554f0` documents a concrete profile:

- lightwalletd v0.5.4 is enabled and pinned by digest;
- one replica is configured;
- the lightwalletd memory limit is 3 GiB;
- the lightwalletd ingress is enabled with nginx, GRPC backend protocol, and TLS; and
- the default `lightwalletd.ingress.annotations` map contains no body-size override.

See [`values.yaml:285-353`](https://github.com/zecrocks/zcash-stack/blob/9c56ad4cd38e857d920ace0152ef1d92c5e554f0/charts/zcash-stack/values.yaml#L285-L353) and [`values.yaml:379-399`](https://github.com/zecrocks/zcash-stack/blob/9c56ad4cd38e857d920ace0152ef1d92c5e554f0/charts/zcash-stack/values.yaml#L379-L399). A separate, disabled grpc-web ingress has a 16 MiB override at lines 931-949; it is not the default lightwalletd ingress.

The public edge configuration documents HAProxy forwarding to regional TLS endpoints described by the chart. The PoC reproduces the chart's TLS ingress-nginx boundary locally without interacting with a public endpoint.

Ingress-nginx v1.15.1 defaults the body limit to `1m` and concurrent HTTP/2 streams to 128 per connection, and emits those values into the NGINX configuration:

- [`config.go`](https://github.com/kubernetes/ingress-nginx/blob/controller-v1.15.1/internal/ingress/controller/config/config.go)
- [`nginx.tmpl`](https://github.com/kubernetes/ingress-nginx/blob/controller-v1.15.1/rootfs/etc/nginx/template/nginx.tmpl)

The receipt captures the exact rendered values from the running controller. No proxy-body-size annotation is used, and every attack message is below the default limit.

## Exploit sequence

1. The attacker opens 17 ordinary TLS/gRPC connections to ingress-nginx.
2. They start 2,000 concurrent `SendTransaction` calls, distributed 117-118 per connection.
3. Every data value is 900,000 bytes; its complete gRPC message is 900,009 bytes and passes ingress's 1 MiB boundary.
4. Lightwalletd admits concurrent messages under its 2,000,000-byte application check.
5. Decoded protobuf bodies, hex strings, JSON bodies, and outbound HTTP work overlap without a global byte budget.
6. The 3 GiB victim crosses `memory.max`; Kubernetes records `OOMKilled` and exit code 137.
7. A restart restores service. Repeating the same request wave kills the new process.

## Demonstrated impact and controls

Environment:

- exact v0.5.4 source, built without source changes;
- Kind v0.30.0 / Kubernetes v1.34.0 on Linux/arm64;
- ingress-nginx v1.15.1 image digest `sha256:594ceea76b01c592858f803f9ff4d2cb40542cae2060410b2c95f75907d659e1`;
- TLS termination at ingress-nginx, GRPC upstream to lightwalletd;
- victim `memory.max=3221225472`, `memory.swap.max=0`;
- immediate-full-read/immediate-application-reject backend; and
- attacker and backend outside the victim cgroup.

Matched fresh-process control:

```text
calls=2000 connections=17 calls_per_connection=117..118
data=100 protobuf=102 grpc_frame=107
client started=2000 completed=2000 errors=0
backend arrived=2000 rejected=2000 bytes=536000
ingress status_413=0
victim phase=Running restart_count=0
```

First attack:

```text
calls=2000 connections=17 calls_per_connection=117..118
data=900000 protobuf=900004 grpc_frame=900009
client wire_bytes=1790766406 elapsed_ms=8471
backend complete bodies=89 rejected=89 bytes=160206052
ingress status_413=0
victim phase=Failed reason=OOMKilled exit_code=137
```

The client wire counter is a transport lower-bound observation; it is not used to claim that every requested application byte reached lightwalletd. The complete 1,800,068-byte backend bodies shown above prove that those calls traversed TLS ingress, gRPC decoding, hex/JSON expansion, and the outbound HTTP boundary. The terminal cgroup result proves the process impact.

Recovery and repeatability:

```text
fresh victim: one TLS SendTransaction completed with errors=0
second attack wire_bytes=1790110039
backend complete bodies=69 rejected=69 bytes=124204692
ingress status_413=0
victim phase=Failed reason=OOMKilled exit_code=137
```

The nominal pacing is 125 decimal Mbit/s per connection (2.125 Gbit/s aggregate). The observed attacks completed in approximately 7.6-8.5 seconds.

The request data is protobuf-valid and reaches every vulnerable lightwalletd allocation before backend transaction validation. Consensus validity is therefore irrelevant to this pre-validation resource boundary. The immediate-reject backend proves that backend slowness or transaction acceptance is not required.

## Public prior art and disclosure request

This is the same resource-exhaustion family as GHSA-6ppp-r2gc-9q6v, whose formal GitHub severity field is High. The advisory used oversized messages and recommended per-method concurrency limits. Its closing [commit `df3d199b`](https://github.com/zcash/lightwalletd/commit/df3d199b59a6d192193a36e79f34f1cb827c054e) added only the 2,000,000-byte per-message check.

This report demonstrates a surviving aggregate-admission failure after the published per-message repair. The shipped fix does not implement the per-method concurrency limit or bounded worker pool identified in GHSA-6ppp. Please amend or reopen that advisory, or create a separate advisory if that better fits your process.

## Proof of concept

The complete evidence bundle is provided as a base64-encoded archive in the one-file unlisted secret gist [`b7d6f1b480cbf93cd64fb2f4c9af3f5f`](https://gist.github.com/saxenism/b7d6f1b480cbf93cd64fb2f4c9af3f5f), with immutable raw URL [`ce3c720f.../lightwalletd-sendtransaction-concurrency-disclosure-v4.tar.gz.b64`](https://gist.githubusercontent.com/saxenism/b7d6f1b480cbf93cd64fb2f4c9af3f5f/raw/ce3c720ffbd7ce438356c5f676e841eef9b9e282/lightwalletd-sendtransaction-concurrency-disclosure-v4.tar.gz.b64). The decoded archive SHA-256 is `817d85bea51d9c3a99c8c508a29bd142f2bc7465e40fcea6b4894670d976c2a8`. GitHub secret gists are unlisted rather than access-controlled, so anyone holding the URL can retrieve the bundle. The archive is self-contained except for public source/image downloads. It never contacts a public Zcash service and deliberately OOM-kills only a local 3 GiB victim pod. Requirements: Docker with at least 10 GiB assigned, Kind v0.30.0, kubectl, Git, OpenSSL, and Bash.

Download, decode, and verify the exact archive:

```console
curl --fail --location \
  'https://gist.githubusercontent.com/saxenism/b7d6f1b480cbf93cd64fb2f4c9af3f5f/raw/ce3c720ffbd7ce438356c5f676e841eef9b9e282/lightwalletd-sendtransaction-concurrency-disclosure-v4.tar.gz.b64' \
  --output lightwalletd-sendtransaction-concurrency-disclosure-v4.tar.gz.b64
openssl base64 -d -A \
  -in lightwalletd-sendtransaction-concurrency-disclosure-v4.tar.gz.b64 \
  -out lightwalletd-sendtransaction-concurrency-disclosure-v4.tar.gz
printf '%s  %s\n' \
  '817d85bea51d9c3a99c8c508a29bd142f2bc7465e40fcea6b4894670d976c2a8' \
  'lightwalletd-sendtransaction-concurrency-disclosure-v4.tar.gz' \
  | shasum -a 256 -c -
tar -xzf lightwalletd-sendtransaction-concurrency-disclosure-v4.tar.gz
cd lightwalletd-sendtransaction-concurrency-disclosure-v4
```

From the extracted disclosure directory:

```console
bash verify-bundle.sh
bash poc/reproduce.sh
```

Expected final marker:

```text
C44_V3_PASS
LWD_POC_PASS
```

The script performs the following fail-closed checks:

1. clones and verifies clean exact lightwalletd v0.5.4 source;
2. builds lightwalletd and the client/backend harness in a pinned Go image;
3. creates a pinned Kind/Kubernetes cluster and deploys the packaged, hash-verified ingress-nginx v1.15.1 manifest;
4. generates a local TLS certificate and deploys the exact 3 GiB/no-swap victim;
5. captures the rendered 1 MiB body and 128-stream defaults;
6. runs the 2,000-call matched control;
7. runs the terminal attack and verifies OOMKilled/137, complete downstream bodies, and zero ingress 413s;
8. recreates the victim, verifies recovery, and repeats the terminal attack; and
9. deletes the isolated Kind cluster on exit.

## Remediation

Apply a process-wide admission policy before expensive expansion and backend dispatch. The budget should account for decoded input bytes and the hex/JSON amplification, and it should be shared across all client connections.

Also add transport/edge defenses that bound aggregate streams and connections per client and per process. `grpc.MaxConcurrentStreams` and ingress HTTP/2 stream limits are per connection, so neither is sufficient alone against multi-connection clients. A handler semaphore by itself is also too late to prevent the initial protobuf decode; pair application admission with a substantially lower receive limit or a transport/proxy design that bounds aggregate pre-handler bytes.

Add a regression test that sends many individually valid, in-limit bodies across multiple connections under a production memory limit. It should prove bounded resident memory and preserved service availability while retaining ordinary transaction throughput.

## References

- [Zcash security policy](https://github.com/zcash/zcash/blob/master/SECURITY.md)
- [GHSA-6ppp-r2gc-9q6v](https://github.com/zcash/lightwalletd/security/advisories/GHSA-6ppp-r2gc-9q6v)
- [Per-message remediation commit](https://github.com/zcash/lightwalletd/commit/df3d199b59a6d192193a36e79f34f1cb827c054e)
- [zec.rocks chart values](https://github.com/zecrocks/zcash-stack/blob/9c56ad4cd38e857d920ace0152ef1d92c5e554f0/charts/zcash-stack/values.yaml)
- [ingress-nginx request-size documentation](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/#custom-max-body-size)


---

[Rahul Saxena](https://x.com/saxenism)  
Founder, [Bluethroat Labs](https://bluethroatlabs.com)

