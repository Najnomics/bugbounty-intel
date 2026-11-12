# GHSA-pr92-c4mc-x48r: `P256VerifyPrecompiledContract.computePrecompile` (the EIP-7951 precompile that becomes mainnet-active in Osaka) writes to `System.err` directly via `System.err.println(...)` in its catch-all error handler. The handler runs on the EVM transaction-pro

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-pr92-c4mc-x48r |
| CVE | none assigned |
| Severity | medium |
| CWE | CWE-400 |
| Published | 2026-10-02T03:51:25Z |
| Updated | 2026-10-19T03:56:29Z |
| Affected | org.hyperledger.besu:besu <= 26.7.1 (patched: 26.8.0) |
| Credits | macfarla |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-pr92-c4mc-x48r |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

**Summary**: `P256VerifyPrecompiledContract.computePrecompile` (the EIP-7951 precompile that becomes mainnet-active in Osaka) writes to `System.err` directly via `System.err.println(...)` in its catch-all error handler. The handler runs on the EVM transaction-processing path for *every* failed verification, which is reachable by any contract call made by any transaction. An attacker can craft a contract that calls `0x0000…0100` (P256VERIFY) with malformed input in a tight loop; each call triggers the `System.err.println`, which serialises on the JVM's stderr stream and stalls every thread that touches stderr (block import, P2P, RPC, metrics). At ~10⁵ calls/sec the node is unresponsive.

**Severity**: Medium

**Affected file/line**:
- `evm/src/main/java/org/hyperledger/besu/evm/precompile/P256VerifyPrecompiledContract.java:170-174`

## Vulnerability

The catch-all in `computePrecompile`:

```java
// P256VerifyPrecompiledContract.java:158-175
try {
  if (useNativeBoringSSL) {
    res = computeNative(input);
  } else {
    res = computeDefault(input);
  }

  if (enableResultCaching) {
    p256VerifyCache.put(cacheKey, res);
  }
  return res.cachedResult();

} catch (Exception e) {
  LOG.warn("P256VERIFY verification failed: {}", e.getMessage());
  System.err.println("P256VERIFY verification failed: " + e.getMessage());     // <-- direct stderr write
  return PrecompileContractResult.success(INVALID);
}
```

`System.err.println(...)` is a synchronised method on `PrintStream`. Every thread that calls it acquires the same monitor and flushes the line. On Linux with stderr redirected to a tty or a non-buffered file (which is the default for `besu` when invoked from systemd, docker `-it`, or most containers), each call performs a `write(2)` syscall plus a flush. That's ~5-50 µs per call under low contention and 100-500 µs under contention from multiple threads.

`computeDefault` can throw on a number of inputs, and `computeNative` can also throw (`BoringSSLPrecompiles.p256Verify` is a JNI call that surfaces native errors as Java exceptions). The most reliable trigger is in `computeDefault`:

```java
// P256VerifyPrecompiledContract.java:227-244
try {
  final org.bouncycastle.math.ec.ECPoint ecPoint = R1_PARAMS.getCurve().createPoint(qx, qy);
  signatureAlgorithm.getCurve().validatePublicPoint(ecPoint);
} catch (IllegalArgumentException e) {
  LOG.trace("Public key not on curve: {}", e.getMessage());
  return new PrecompileInputResultTuple(...);                                  // <-- caught here, returns INVALID
}
final SECPSignature signature = signatureAlgorithm.createSignature(r, s, (byte) 0);
final SECPPublicKey publicKey = signatureAlgorithm.createPublicKey(pubKeyBytes); // <-- can throw IllegalArgumentException
final boolean isValid = signatureAlgorithm.verifyMalleable(messageHash, signature, publicKey);
```

`createSignature` and `createPublicKey` accept `BigInteger`/raw bytes and throw `IllegalArgumentException` when the values are out of curve or otherwise invalid. Those throws **escape** the inner `try/catch` at lines 227-234 (which only covers `R1_PARAMS.getCurve().createPoint` and `validatePublicPoint`) and are caught by the outer `catch (Exception e)` at line 170 — the one with `System.err.println`.

Concretely, the following input shape exits at the outer catch:

- 160 bytes long (passes the length check at line 127)
- `r`, `s` in `(0, n)` (passes the r/s range check at line 208)
- `qx`, `qy` in `[0, p)` (passes the qx/qy range check at line 215)
- `(qx, qy)` is *on* the secp256r1 curve (so `createPoint` and `validatePublicPoint` succeed)
- but the message hash and signature when fed to `createSignature(r, s, 0)` or `createPublicKey(pubKeyBytes)` triggers an `IllegalArgumentException` (for example, by feeding `pubKeyBytes` whose two halves both equal a small valid scalar that the underlying signature library rejects).

A simpler trigger that hits the outer catch reliably is when **`signatureAlgorithm.verifyMalleable` itself throws**. This depends on which `SignatureAlgorithm` implementation is wired (the `SECP256R1` class delegates to BouncyCastle; specific malformed inputs surface as `IllegalArgumentException` deep in BC).

The same `System.err.println` was likely intended to be a debug statement that was meant to be removed before commit (it duplicates the line above which already calls `LOG.warn`). It is not present in the equivalent BLS12 precompile or the SHA256 precompile.

## Impact

- **EVM-reachable: any user transaction can call P256VERIFY** at gas cost `getP256VerifyPrecompiledContractGasCost()` (typically a few thousand gas). 30M gas / ~5000 gas per call = ~6000 calls per block at maximum density. With each call performing a synchronised `System.err.println`, block import is slowed by milliseconds-to-seconds depending on stderr destination.
- **Cross-thread contention**: stderr is shared between the block import thread, the JSON-RPC worker pool, the P2P thread pool, and the metrics thread. A single thread doing tight `System.err.println` calls can pin the others while they wait for the `PrintStream` monitor.
- **Disk full / log rotation amplification**: when stderr is captured by systemd-journald or by `docker logs`, each call pays a journal-write cost. Over an hour, an attacker with a ~$5 transaction can pump millions of stderr lines into the operator's log infrastructure, potentially filling disk and triggering log-rotation interlocks.
- **Reachable from any caller**: P256VERIFY is at address `0x0000000000000000000000000000000000000100` on networks where EIP-7951 is active. No special permissions needed.
- **Sneaks past the JSON-RPC layer**: even if the operator firewalls JSON-RPC, the precompile is reachable via any submitted transaction, so the attack works against validator-only nodes too.
- **Minor secondary issue**: the precompile result cache (line 94-95) is keyed by hash of the *input*; failed-input results are still cached, so the second call with the same bad input is fast. But the first call always pays the `System.err.println` cost.

## PoC

Solidity-style pseudocode for a contract that hammers P256VERIFY with bad input:

```solidity
contract P256Hammer {
    function hammer(uint256 n) external {
        bytes memory bad = new bytes(160);
        // Fill `bad` with a 160-byte input that is well-formed length-wise
        // and whose qx/qy lie on the curve but whose pubKeyBytes encoding
        // makes signatureAlgorithm.createPublicKey throw.
        // (Construction details: pick (qx, qy) on secp256r1, then mutate
        // r or s to a value that BouncyCastle's signature path rejects
        // late — e.g. r == n, which fails the (0, n) check inside
        // createSignature even after the precompile-level r in (0,n)
        // check passed.)
        for (uint256 i = 0; i < n; i++) {
            (bool ok, bytes memory ret) = address(0x0100).staticcall(bad);
            ok; ret;
        }
    }
}
```

Sending a transaction that calls `hammer(N)` with N sized to fit in the gas limit hits the outer catch on every iteration and writes to stderr. With block gas limit 30M and a P256VERIFY cost of ~5000 gas, N can reach ~6000 per block. Across the 12-second block time, that is 500 stderr writes per second per attacker transaction in the block — and any inclusion-attempt of the transaction (including failed simulations via `eth_call`/`eth_estimateGas`/`debug_traceCall`) does the same.

For maximum amplification, use `eth_call`/`debug_traceCall` to force the node to do the work without paying gas. The simulator runs the same precompile, hits the same outer catch, and writes the same lines to stderr. This is unauthenticated (assuming the `eth_call` JSON-RPC namespace is exposed) and free.

## Recommendation

1. **Drop the `System.err.println`**. The line directly above already logs at WARN. The whole catch block becomes:

   ```java
   } catch (Exception e) {
     LOG.warn("P256VERIFY verification failed: {}", e.getMessage());
     return PrecompileContractResult.success(INVALID);
   }
   ```

2. **Downgrade to `LOG.debug` or `LOG.trace`** instead of `LOG.warn`. P256VERIFY is reachable from arbitrary user-submitted EVM input; treating any verification failure as a WARN-level log gives every transaction author a free WARN-level log line, which is the same amplification problem at lower magnification.

3. Audit the codebase for other accidental `System.err.println` / `System.out.println` / `printStackTrace` calls on the EVM, RLP, or RPC critical path. A grep already found one more on the log-bloom-cache read path (`BlockchainQueries.java:925`); both should be replaced with structured logging.

4. Consider rate-limiting log emission in EVM-reachable paths via a token-bucket logger wrapper, so even debug logs cannot be amplified by malicious calldata.

**Payment / Contact**
If this finding qualifies for a reward, payment can be sent to:
`0x83e033dd8ddb93052cc880227b06a8ee38f25eb2`
(EVM address — any chain)

Filing through GitHub PVR because the platform that hosts the official bounty has KYC requirements I have not been able to clear from my jurisdiction.

## Patches and references

Fixed in Besu 26.8.1.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/fbfb5f9ecdec
- Pull request: https://github.com/besu-eth/besu/pull/11092
