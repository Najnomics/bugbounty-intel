# GHSA-q2c2-hpp9-58hm: lightwalletd GetTreeState oversized block hashes can OOM a targeted node before backend rejection

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-q2c2-hpp9-58hm |
| CVE | none assigned |
| Severity | high |
| CWE | CWE-400 |
| Published | 2026-07-28T18:14:43Z |
| Updated | 2026-07-28T18:17:51Z |
| Affected | github.com/zcash/lightwalletd <= 0.5.0 (patched: 0.5.1) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-q2c2-hpp9-58hm |

## Description (verbatim)

## Summary

`lightwalletd`'s public `GetTreeState` gRPC method accepts attacker-controlled `BlockID.hash` bytes without validating that a block hash is exactly 32 bytes. When `height` is zero and a hash field is supplied, the handler hex-encodes the full byte slice, JSON-marshals the expanded string, and forwards it to the backend node's `z_gettreestate` RPC.

This allows an unauthenticated client to send an oversized invalid block hash that is eventually rejected by the backend, but only after `lightwalletd` performs large local allocations and the backend spends work decoding/parsing the JSON-RPC payload.

A local regtest PoC using a real `zcashd`, an unmodified `lightwalletd`, and public gRPC demonstrates both the single-request amplification and process-level impact:

- One 3.9 MB invalid block-hash field increased request latency from 19 ms to 11400 ms and added about 29 MB of `lightwalletd` heap before rejection.
- Twelve parallel 3.9 MB `GetTreeState` hash requests pushed a 256 MiB victim container to 99.84% memory usage.
- Sixteen parallel 3.9 MB `GetTreeState` hash requests OOM-killed the same 256 MiB victim `lightwalletd` container with `exit_code=137` and `oom_killed=true`.

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

- `frontend/service.go:311`: public `GetTreeState` handler
- `frontend/service.go:312-315`: only checks that either height or hash is present
- `frontend/service.go:328-331`: hex-encodes and JSON-marshals `id.Hash` without checking `len(id.Hash) == 32`
- `frontend/service.go:340`: forwards the expanded payload to backend `z_gettreestate`

Vulnerable code:

```go
func (s *lwdStreamer) GetTreeState(ctx context.Context, id *walletrpc.BlockID) (*walletrpc.TreeState, error) {
    if id.Height == 0 && id.Hash == nil {
        return nil, status.Error(codes.InvalidArgument,
            "GetTreeState: must specify a block height or ID (hash)")
    }
    params := make([]json.RawMessage, 1)
    var hashJSON []byte
    if id.Height > 0 {
        ...
    } else {
        // id.Hash is big-endian, keep in big-endian for the rpc
        hash := hex.EncodeToString(id.Hash)
        common.Log.Debugf("gRPC GetTreeState(hash=%+v)\n", hash)
        hashJSON, err := json.Marshal(hash)
        if err != nil {
            return nil, status.Errorf(codes.InvalidArgument,
                "GetTreeState: cannot marshal block hash: %s", err.Error())
        }
        params[0] = hashJSON
    }
    ...
    result, rpcErr := common.RawRequest("z_gettreestate", params)
```

The neighboring transaction lookup path validates a fixed-size identifier before hex/JSON conversion:

```go
if txf.Hash != nil {
    if len(txf.Hash) != 32 {
        return nil, status.Errorf(codes.InvalidArgument,
            "GetTransaction: transaction ID has invalid length: %d", len(txf.Hash))
    }
    txidHex := hash32.Encode(hash32.Reverse(hash32.FromSlice(txf.Hash)))
    ...
}
```

`GetTreeState` lacks the equivalent length check for block hashes. A 3.9 MB gRPC byte field becomes about 7.8 MB of hex string before JSON-RPC overhead and backend processing.

## Protocol-Level Mechanism

`GetTreeState` is the public wallet-facing API for retrieving the note commitment tree state at a block. The request uses `BlockID`, which can identify a block by height or by hash. A Zcash block hash is a fixed 32-byte identifier; it is not a variable-length byte string.

The intended cross-layer mapping is:

```text
public gRPC BlockID.hash [32 bytes] -> hex block hash string [64 chars] -> JSON-RPC z_gettreestate -> backend lookup
```

The vulnerable implementation instead allows:

```text
public gRPC BlockID.hash [near gRPC message limit] -> huge hex string -> huge JSON-RPC z_gettreestate payload -> backend rejection
```

The issue is not that the backend accepts the oversized hash as a valid block. It rejects the PoC payload with `-5: Block not found`. The issue is that `lightwalletd` expands and forwards the malformed identifier before enforcing the protocol-level fixed-size hash invariant.

## Finding Description

An unauthenticated attacker can trigger the issue through the normal public wallet-facing gRPC API:

1. The attacker connects to `CompactTxStreamer/GetTreeState`.
2. The attacker sends `BlockID{height: 0, hash: <large byte string>}` close to the gRPC inbound message-size limit.
3. The byte string does not need to be a valid block hash.
4. `lightwalletd` only checks that either height or hash is present.
5. Since `height` is zero, `lightwalletd` enters the hash path.
6. `lightwalletd` hex-encodes the full byte slice, approximately doubling its size.
7. `lightwalletd` JSON-marshals the expanded hex string.
8. `lightwalletd` sends the expanded payload to backend `z_gettreestate`.
9. The backend rejects the payload, but only after both services have spent CPU and memory on a request that could have been rejected locally.

The PoC uses a 32-byte invalid block hash as the control and a 3.9 MB invalid block-hash field as the attack payload. Both return backend error code `-5`, confirming the backend `z_gettreestate` path is reached in both cases.

## Impact

Impact level: Medium.

This is a targeted resource-exhaustion issue against an individual `lightwalletd` instance and its backend node.

Single-request localnet evidence:

```text
hash_bytes=32 grpc_error=rpc error: code = InvalidArgument desc = GetTreeState: z_gettreestate failed: -5: Block not found duration_ms=19
hash_bytes=3900000 grpc_error=rpc error: code = InvalidArgument desc = GetTreeState: z_gettreestate failed: -5: Block not found duration_ms=11400
baseline_ms=19 attack_ms=11400 slowdown_x=576.88
heap_before=1036656 heap_after_baseline=3293672 heap_after_attack=32673064 heap_delta_attack=29379392 objects_before=4173 objects_after_attack=4586 objects_delta_attack=413
```

Near-OOM localnet/cgroup evidence:

```text
parallel_total=12 hash_bytes=3900000 duration_ms=14367
baseline_ms=10 attack_ms=14367 slowdown_x=1414.28
heap_before=1044208 heap_after_baseline=3174480 heap_after_attack=213034064 heap_delta_attack=209859584 objects_before=4151 objects_after_attack=7643 objects_delta_attack=3492
client_exit_code=0
victim_status=running running=true exit_code=0 oom_killed=false
victim_memory_usage=255.6MiB / 256MiB victim_memory_percent=99.84%
```

Process-death localnet/cgroup evidence:

```text
zcashd_bridge_ip=172.17.0.2 victim_memory=256m hash_bytes=3900000 parallel=16
hash_bytes=32 grpc_error=rpc error: code = InvalidArgument desc = GetTreeState: z_gettreestate failed: -5: Block not found duration_ms=64
parallel=7 hash_bytes=3900000 grpc_error=rpc error: code = InvalidArgument desc = GetTreeState: z_gettreestate failed: -5: Block not found duration_ms=23404
parallel=4 hash_bytes=3900000 grpc_error=rpc error: code = Unavailable desc = error reading from server: EOF duration_ms=23858
parallel_total=16 hash_bytes=3900000 duration_ms=23858
client_exit_code=1
victim_status=exited running=false exit_code=137 oom_killed=true
```

Practical impact:

- A public unauthenticated client can force large heap allocations in `lightwalletd`.
- A public unauthenticated client can force backend `z_gettreestate` decode/parse work for an invalid oversized block identifier.
- Repeated or parallel requests can degrade the tree-state API and backend RPC service.
- Under a 256 MiB memory limit, sixteen parallel requests OOM-killed the targeted `lightwalletd` process.
- Wallet clients using that instance lose service until the operator or supervisor restarts it.
- The attack is non-distributed: each `lightwalletd` endpoint/backend pair must be targeted individually.

This does not affect Zcash consensus, does not steal funds, does not compromise wallet keys, and does not automatically propagate across nodes. The proposed severity is Medium because the demonstrated outcome is targeted supporting-infrastructure denial of service, not a network-wide outage or consensus failure.

## Likelihood

Likelihood level: Medium.

The reachable entry point is public and unauthenticated in normal `lightwalletd` deployments that expose wallet gRPC. The attack does not require:

- a valid block hash,
- funded addresses,
- wallet keys,
- backend RPC credentials,
- host access,
- a reorg,
- mempool timing,
- chain history setup,
- privileged flags such as Darkside or Ping.

The main practical constraints are request size, concurrency, and victim memory. A single near-limit request reliably causes large latency and heap amplification. Process death in the PoC uses sixteen concurrent near-limit requests and a 256 MiB victim memory limit. This is realistic for memory-constrained service deployments, but it is not universal. Larger deployments may experience latency and memory pressure rather than immediate OOM.

Likelihood is therefore Medium rather than High.

## Severity Discussion

Per the ZCG Security & Vulnerability Disclosure Initiative, `lightwalletd` is Supporting Infrastructure. This report recommends Medium because the bug allows repeated, unauthenticated targeted denial of service against one wallet-supporting infrastructure node.

The issue fits Medium better than Low because the PoC demonstrates both strong single-request amplification and process-level availability loss under a bounded-memory victim:

- one request caused about 577x latency increase and about 29 MB additional heap,
- twelve parallel requests pushed a 256 MiB victim to 99.84% memory usage,
- sixteen parallel requests OOM-killed the victim process.

The report does not claim High because the impact is targeted and non-distributed. It does not affect consensus, does not propagate through the Zcash network, and does not compromise funds or wallet secrets.

## Attacker Model, Scope, and Triage Notes

Attacker model:

- The attacker can connect to the public `lightwalletd` gRPC service.
- The attacker does not need access to the `lightwalletd` host.
- The attacker does not need backend RPC credentials.
- The attacker does not need wallet keys, validator privileges, mining power, or admin access.
- The attacker sends one or more large `GetTreeState` requests with invalid block-hash bytes.

Scope fit:

- `lightwalletd` is listed under Supporting Infrastructure.
- The affected method is a normal public wallet-facing gRPC API.
- The issue is a targeted non-distributed DoS/resource-amplification finding against one supporting-infrastructure instance.
- The PoC is isolated to local regtest and does not touch public mainnet or testnet infrastructure.
- The PoC does not use Darkside APIs, `--ping-very-insecure`, or any test-only gRPC method.

Expected pushback:

- Pushback: "The hash is invalid and rejected by the backend."
  - Response: Correct. The vulnerability is that invalid oversized data is expanded and forwarded before local fixed-size hash validation is enforced. Rejection happens after the expensive work.

- Pushback: "The process-death PoC uses a 256 MiB memory limit."
  - Response: The memory limit is a safe localnet way to demonstrate process death without risking the host. The same amplification is also measured directly through Go heap metrics in the single-request PoC and the twelve-parallel near-OOM run.

- Pushback: "A larger deployment may not OOM from sixteen requests."
  - Response: That is why severity is Medium. Larger deployments still spend unnecessary CPU, memory, and backend RPC time on public invalid identifiers, and repeated requests can maintain pressure.

## Proof of Concept

[poc.zip](https://drive.google.com/file/d/1KUrzNIrwvappAW8Kn3WfbBq9ANpLdruO/view?usp=sharing)

### Archive Contents

PoC file list:

- `poc/tree_hash_amp_try.sh`
- `poc/tree_hash_amp_cgroup_try.sh`
- `poc/tree_hash_amp_client.go`
- `poc/localnet-observed-output.txt`

### Reproduction

Run from the root of a `github.com/zcash/lightwalletd` checkout after unpacking `poc.zip`.

Single-request amplification:

```bash
unzip poc.zip
LARGE=3900000 bash poc/tree_hash_amp_try.sh
```

Process-death cgroup PoC:

```bash
unzip poc.zip
LWD_MEM=256m PARALLEL=16 LARGE=3900000 bash poc/tree_hash_amp_cgroup_try.sh
```

The single-request script performs the following sequence end-to-end:

1. Builds `lightwalletd` from the reviewed repository.
2. Starts a local `zcashd` regtest Docker container with `txindex=1`, `lightwalletd=1`, and `experimentalfeatures=1`.
3. Mines one local regtest block.
4. Starts an unmodified `lightwalletd` instance against the local backend.
5. Calls public `GetTreeState` with a 32-byte invalid block-hash control payload.
6. Calls public `GetTreeState` with a large invalid block-hash payload.
7. Prints request latency, slowdown, heap growth, and heap object growth.

The cgroup script starts the victim `lightwalletd` instance in a Docker container with a configurable memory limit, then sends parallel large invalid `GetTreeState` requests and prints the victim container status.

### Expected Output

Expected vulnerable single-request output includes:

```text
hash_bytes=32 grpc_error=rpc error: code = InvalidArgument desc = GetTreeState: z_gettreestate failed: -5: Block not found duration_ms=19
hash_bytes=3900000 grpc_error=rpc error: code = InvalidArgument desc = GetTreeState: z_gettreestate failed: -5: Block not found duration_ms=11400
baseline_ms=19 attack_ms=11400 slowdown_x=576.88
heap_before=1036656 heap_after_baseline=3293672 heap_after_attack=32673064 heap_delta_attack=29379392 objects_before=4173 objects_after_attack=4586 objects_delta_attack=413
```

Expected vulnerable cgroup output includes:

```text
zcashd_bridge_ip=172.17.0.2 victim_memory=256m hash_bytes=3900000 parallel=16
parallel_total=16 hash_bytes=3900000 duration_ms=23858
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

The backend error code `-5: Block not found` is expected. It confirms that the payload reached backend `z_gettreestate`; the security issue is the work performed before rejection.

An additional cgroup run with `PARALLEL=12` did not kill the process but reached near-OOM pressure:

```text
parallel_total=12 hash_bytes=3900000 duration_ms=14367
baseline_ms=10 attack_ms=14367 slowdown_x=1414.28
heap_delta_attack=209859584
victim_status=running running=true exit_code=0 oom_killed=false
victim_memory_usage=255.6MiB / 256MiB victim_memory_percent=99.84%
```

This supports that the process-death result is caused by progressive memory pressure from accepted public requests, not by a privileged or test-only path.

## Recommended Fix

Reject malformed block hashes before hex encoding, JSON marshaling, or backend forwarding.

Recommended root-cause fixes:

1. Add a `len(id.Hash) == 32` check in the `GetTreeState` hash path.
2. Reject empty hash slices explicitly instead of treating any non-nil `[]byte` as a hash selector.
3. Consider rejecting requests that specify both `height` and `hash`, or document and enforce one clear precedence rule.
4. Return `codes.InvalidArgument` before `hex.EncodeToString` for malformed hashes.
5. Add a regression test that sends a long `BlockID.hash` and verifies no backend RPC call is made.

Example sketch:

```go
const blockHashLen = 32

func (s *lwdStreamer) GetTreeState(ctx context.Context, id *walletrpc.BlockID) (*walletrpc.TreeState, error) {
    if id == nil {
        return nil, status.Error(codes.InvalidArgument, "GetTreeState: missing block identifier")
    }
    if id.Height == 0 {
        if len(id.Hash) == 0 {
            return nil, status.Error(codes.InvalidArgument,
                "GetTreeState: must specify a block height or block hash")
        }
        if len(id.Hash) != blockHashLen {
            return nil, status.Errorf(codes.InvalidArgument,
                "GetTreeState: block hash has invalid length: %d", len(id.Hash))
        }
    }

    params := make([]json.RawMessage, 1)
    if id.Height > 0 {
        heightJSON, err := json.Marshal(strconv.Itoa(int(id.Height)))
        if err != nil {
            return nil, status.Errorf(codes.InvalidArgument,
                "GetTreeState: cannot parse block height: %s", err.Error())
        }
        params[0] = heightJSON
    } else {
        hashJSON, err := json.Marshal(hex.EncodeToString(id.Hash))
        if err != nil {
            return nil, status.Errorf(codes.InvalidArgument,
                "GetTreeState: cannot marshal block hash: %s", err.Error())
        }
        params[0] = hashJSON
    }

    result, rpcErr := common.RawRequest("z_gettreestate", params)
    ...
}
```

Defense in depth:

- Add shared validation helpers for all `BlockID.hash` and transaction hash fields.
- Configure per-method request size limits below the generic gRPC default for APIs that only accept fixed-size identifiers.
- Add metrics for locally rejected malformed identifiers.
- Propagate request context/deadlines to backend RPC calls where supported.

## References

- `frontend/service.go`
- `walletrpc/service.proto`
- `CompactTxStreamer/GetTreeState`
- `BlockID.hash`
- `z_gettreestate`
- ZCG category: Supporting Infrastructure

