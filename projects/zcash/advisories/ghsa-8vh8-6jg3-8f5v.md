# GHSA-8vh8-6jg3-8f5v: Repeated poolTypes in GetBlockRange saturate lightwalletd CPU and slow wallet scans

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-8vh8-6jg3-8f5v |
| CVE | none assigned |
| Severity | medium |
| CWE | CWE-400 |
| Published | 2026-11-18T00:38:28Z |
| Updated | 2026-11-18T00:38:28Z |
| Affected | github.com/zcash/lightwalletd <= 0.6.1 (patched: 0.6.2) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-8vh8-6jg3-8f5v |

## Description (verbatim)

# Repeated `poolTypes` in `GetBlockRange` saturate lightwalletd CPU and slow wallet scans

**Affected asset:** `zcash/lightwalletd` v0.5.4, `CompactTxStreamer/GetBlockRange`.

**Severity:** Moderate (CVSS 3.1 AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L, 5.3).

An unauthenticated gRPC client can submit two valid, below-limit historical
range requests that fill a two-core lightwalletd instance's CPU quota and
slow independent wallet scans. In the stock-daemon Regtest run preserved in
the linked PoC bundle, 6,000 legitimate scans in ten other processes all
succeeded with five-second deadlines, but their p95 latency rose from
**28.613 ms to 64.934 ms** (2.27×).
The observed effect is reduced wallet-service availability through sustained
CPU pressure and higher latency. The experiment did not produce a crash,
timeout, or complete outage.

## Vulnerability details

[`BlockRange.poolTypes`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/lightwallet-protocol/walletrpc/service.proto#L39-L43)
is a repeated enum with no count limit. The released
[`GetBlockRange` handler](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/frontend/service.go#L279-L306)
passes the caller's list to the range worker without canonicalization. The
worker filters every compact transaction in every selected block
([`common/common.go`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/common/common.go#L618-L689)).
For each transaction, `FilterTxPool` performs four linear membership tests
against that list
([`common/common.go`](https://github.com/zcash/lightwalletd/blob/09593edbee4ee68d47e5a53f8ce1c83514c4e8e6/common/common.go#L559-L577)).

Repeating the **valid** `IRONWOOD=4` selector four million times yields a
4,000,014-byte protobuf request, below the default 4 MiB gRPC receive limit.
Three of the four membership tests scan the full list for each compact
transaction. A cached historical range supplies transactions without the
attacker publishing or mining anything. Two concurrent streams keep the
server's CPU quota occupied while ordinary clients share the same instance.

The prior
[GHSA-4hp3-3494-3f2m](https://github.com/zcash/lightwalletd/security/advisories/GHSA-4hp3-3494-3f2m)
addressed large `GetMempoolTx` exclusion-suffix lists and expressly
recommended canonicalizing repeated `poolTypes` as defense in depth. Its
published fix did not remove this `GetBlockRange` processing path: released
v0.5.4 still passes the unbounded list into per-transaction linear scans.
This report therefore identifies an **incompletely remediated repeated-field
resource-amplification surface**, not a wholly new selector design flaw.

## Stock-daemon impact witness

The linked bundle's receipts came from unmodified lightwalletd v0.5.4 commit
`09593edbee4ee68d47e5a53f8ce1c83514c4e8e6`, backed by pinned zcashd
v6.20.0 in a private Regtest network. Ten batches of 1,000 blocks were mined;
lightwalletd's disk cache held 10,001 compact blocks including genesis and
10,000 transactions in the requested heights 1–10,000. Backend checks and
disk caching remained enabled. The wallet-serving container was limited to
two CPUs and 2 GiB RAM; gRPC was published only on host loopback.

After a separate unscored warm-up, ten wallet processes, each on its own
gRPC connection, scheduled
600 legitimate 1,000-block scans at 33 ms intervals: roughly 300 aggregate
offered scans per second. Each wallet call had a five-second deadline. The
attacker ran in an eleventh process, opened two concurrent `GetBlockRange`
streams over the same cached 10,000-block range, and supplied four million
valid `IRONWOOD` selectors per stream.

| Arm | Wallet calls / errors | Wallet p95 / p99 / max | Peak server CPU | Attack duration |
| --- | ---: | ---: | ---: | ---: |
| No attacker | 6,000 / 0 | 28.613 / 31.980 / 65.382 ms | 151.51% | — |
| Two attack streams | 6,000 / 0 | 64.934 / 83.962 / 117.381 ms | 201.38% | 43.940 s |
| After attack | 6,000 / 0 | 28.374 / 32.563 / 61.130 ms | 150.14% | — |

The two valid attack streams completed with zero errors. A one-selector
request over the same historical range completed in 0.074 s. Two equally
large requests filled with the **invalid** enum returned the expected
application errors in 0.089 s; request size alone did not cause the observed
work. All measured legitimate scans succeeded, including after the attack.
The positive arm used about the full two-core quota while wallet p95 rose
2.27×. Once attack traffic ended, wallet p95 returned to 28.374 ms. Raw
per-process JSON, CPU/RSS samples, chain/cache controls, and build
provenance are in `receipts/` and `CONFIG.md`.

This witness uses real stock daemons and a real backend/cache path on Regtest.
It measures one two-core wallet-service instance under the stated offered
load; it does not assert a network-wide outage or production traffic rate.

## Reproduction

The complete PoC, raw receipts, and `README.md` are in the
[unlisted secret Gist](https://gist.github.com/saxenism/e68491744c61083c296bbfc7e6251498)
as one base64-encoded copy of the frozen bundle. Its decoded archive SHA-256
is `943d1dab911b156a17a609501d11e1c9183a06983458738eecd1ad6e0ab7434f`.
Secret Gists are unlisted, not access-controlled; anyone holding the URL can
read the PoC. Download, decode, and verify it before running the included
`README.md` commands:

```sh
set -o pipefail
curl -fsSL 'https://api.github.com/gists/e68491744c61083c296bbfc7e6251498' |
  python3 -c 'import base64,json,sys; f=json.load(sys.stdin)["files"]["lightwalletd-pooltypes-cpu-v5.tar.gz.b64"]; assert not f["truncated"]; sys.stdout.buffer.write(base64.b64decode(f["content"]))' > lightwalletd-pooltypes-cpu-v5.tar.gz
printf '%s  %s\n' '943d1dab911b156a17a609501d11e1c9183a06983458738eecd1ad6e0ab7434f' 'lightwalletd-pooltypes-cpu-v5.tar.gz' | shasum -a 256 -c -
tar -xzf lightwalletd-pooltypes-cpu-v5.tar.gz
cd lightwalletd-pooltypes-cpu
```

From that directory, the first local check is:

```sh
python3 verify.py receipts
shasum -a 256 -c SHA256SUMS
```

The decisive comparison is between `receipts/control-300rps/` and
`receipts/positive-300rps/`; `receipts/recovery-300rps/` demonstrates that
ordinary scans continue after attack traffic ends. The full replay script is
path-parameterized and leaves its test data available for independent review.

## Remediation

Canonicalize `poolTypes` to the small set of defined values once per request,
or reject overlong lists, before iterating blocks. Use constant-time set or
bitset membership for each transaction. Bound range-wide work and concurrent
requests as separate safeguards.

---

[Rahul Saxena](https://x.com/saxenism)  
Founder, [Bluethroat Labs](https://bluethroatlabs.com)

