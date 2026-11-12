# ⚙️ Fusaka Update: Important Ethereum Security Changes

- **Source URL:** https://blog.sigmaprime.io/fusaka-contract-security.html
- **Fetched from:** https://sigmaprime.io/blog/fusaka-contract-security/
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1211 (id 1211)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Following our [previous analysis of Ethereum's Pectra upgrade](https://sigmaprime.io/blog/pectra-contract-security/), the Fusaka upgrade represents the next phase in Ethereum's continued evolution. Building on the foundation laid by previous hard forks, Fusaka introduces scaling for blobs and several DoS-resistance measures alongside exciting new features. Several of these changes have important implications for smart contract developers and the security assumptions they rely on.

In this post, we will explore these key changes in the Fusaka upgrade and their potential impact on [smart contract security](https://sigmaprime.io/services/smart-contract-audit/).

## EIP-7825: Transaction Gas Limit Cap

[**EIP-7825**](https://eips.ethereum.org/EIPS/eip-7825) introduces a cap on the maximum gas usage of a single transaction, limiting it to `2^24` (approximately 16.78 million) gas. Previously, a transaction could take up an entire block, with a limit of 60 million gas.

**Considerations:**

- **Denial of service risks:** Smart contracts that assume large, complex functions can be completed in a single transaction may become unusable if those operations exceed the 16 million gas cap. Developers should ensure
that gas-intensive functions can be split across multiple transactions to avoid denial of service scenarios.

For example, the first `getUsers()` function noted below may become non-executable if it requires more than 16M gas. In contrast, the second function does not have this problem since it can be executed across multiple transactions.

Note that this is a very simple example. The same concept holds for more complex functions like liquidations or oracle updates.

## EIP-7823: MODEXP Input Size Limit

[**EIP-7823**](https://eips.ethereum.org/EIPS/eip-7823) sets an upper bound on valid input sizes for the `MODEXP` precompile. The `MODEXP` precompile performs modular exponentiation operations and is used in certain cryptographic operations like RSA verification. This EIP limits the size of the inputs to 8192 bits, whereas they could be of any arbitrary size before. After this EIP is activated, any call to `MODEXP` with inputs larger than 8192 bits will return an error and consume all gas.

**Considerations:**

- **Input size limits:** Smart contracts that rely on using `MODEXP` with inputs larger than 8192 bits will no longer work correctly after this upgrade. However, as noted in [EIP-7823](https://eips.ethereum.org/EIPS/eip-7823#analysis), no contract has ever successfully called `MODEXP` with an input larger than 513 bytes, so the actual impact is expected to be small in practice.

## EIP-7883: MODEXP Gas Cost Increase

[**EIP-7883**](https://eips.ethereum.org/EIPS/eip-7883) increases the gas cost for `MODEXP`, in some cases by a significant factor. Any smart contracts that call `MODEXP` will see their gas usage increase. The exact increase depends on the input parameters, so developers should check the [EIP-7883 specification](https://eips.ethereum.org/EIPS/eip-7883#specification) for the updated pricing algorithm.

**Considerations:**

- **Fixed gas stipends:** Contracts that call `MODEXP` with a fixed gas stipend may find the call reverting with an out-of-gas error after the upgrade, which may cause denial of service issues. Generally, using fixed gas stipends is strongly discouraged as gas costs are often changed in the EVM.

## EIP-7939: Count Leading Zeros (CLZ) Opcode

[**EIP-7939**](https://eips.ethereum.org/EIPS/eip-7939) introduces a new opcode `CLZ` that counts the number of leading zeros in a 256-bit value. This can greatly improve efficiency for certain mathematical operations, particularly those involving bit manipulation or logarithmic calculations.

**Considerations:**

- **L2 compatibility:** As with any new opcode, most layer 2 networks will not immediately support `CLZ`. Ensure the L2 you're deploying to supports this opcode before using it in your contracts. Calling an unsupported opcode will cause the transaction to revert, which may cause denial of service issues.
- **Solidity support:** Currently, Solidity does not use `CLZ` for optimisations during code generation. However, starting in [version 0.8.31](https://github.com/argotorg/solidity/releases/tag/v0.8.31), `CLZ` can be used in inline assembly.
- **Potential edge case:** For an input of `0`, `CLZ` returns `256`, indicating that all bits are zero. Ensure your code handles this edge case appropriately.

## EIP-7951: Precompile for secp256r1 Curve Support

[**EIP-7951**](https://eips.ethereum.org/EIPS/eip-7951) introduces a new precompile `P256VERIFY` that performs ECDSA signature verification over the secp256r1 (NIST P-256) curve. This curve is widely used in many existing systems, including WebAuthn, secure enclaves, and various hardware wallets, making integration with these systems significantly easier and more gas-efficient.

**Considerations:**

- **Input format:** The precompile expects exactly 160 bytes of concatenated input:
  - 32 bytes: message hash h
  - 32 bytes: signature component r
  - 32 bytes: signature component s
  - 32 bytes: public key x-coordinate
  - 32 bytes: public key y-coordinate
- **Return behavior:** The precompile returns `0x01` if the signature is valid. Critically, if the signature is invalid or the inputs are malformed, the precompile does NOT revert but instead returns empty data `0x`. Your contract must explicitly check for the `0x01` return value and treat empty return data as a failed verification.
- **Solidity support:** Solidity currently has no built-in support for this precompile, so it must be called using a low-level call to the precompile address specified in [the EIP](https://eips.ethereum.org/EIPS/eip-7951#precompile).
- **L2 compatibility:** Ensure the L2 network supports this precompile before deploying contracts that depend on it. Remember that a low-level call to a non-existing contract returns successfully with no return data, which could be mistaken for an invalid signature rather than an unsupported precompile.

## Other Changes

Several other EIPs were introduced in Fusaka but have minimal direct impact on smart contract security:

- [**EIP-7594: PeerDAS - Peer Data Availability Sampling**](https://eips.ethereum.org/EIPS/eip-7594) - increases the amount of data availability capacity for rollups.
- [**EIP-7917: Deterministic proposer lookahead**](https://eips.ethereum.org/EIPS/eip-7917) - ensures the beacon proposer schedule for the next epoch is fully deterministic.
- [**EIP-7918: Blob base fee bounded by execution cost**](https://eips.ethereum.org/EIPS/eip-7918) - adjusts blob pricing to ensure blobs pay at least a fraction of the market rate for the compute they request from nodes.
- [**EIP-7934: RLP Execution Block Size Limit**](https://eips.ethereum.org/EIPS/eip-7934) - sets a limit of 10MB on the size of an RLP-encoded block, with 2MB reserved for the beacon block.
- [**EIP-7935: Set default gas limit**](https://eips.ethereum.org/EIPS/eip-7935) - increases the default gas limit to 60 million to enhance L1 scaling.
- [**EIP-7892: Blob Parameter Only Hardforks**](https://eips.ethereum.org/EIPS/eip-7892) - introduces a framework for hard forks that only change blob parameters, allowing for quicker scaling with less coordination overhead.
- [**EIP-7642: eth/69 - Drop pre-merge fields**](https://eips.ethereum.org/EIPS/eip-7642) - introduces a new version of the `eth` protocol that modifies certain P2P messages.
- [**EIP-7910: eth\_config JSON-RPC Method**](https://eips.ethereum.org/EIPS/eip-7910) - adds an RPC method that returns the current, next, and last known forks for the node, useful for ensuring client readiness.

The Fusaka upgrade continues Ethereum's evolution with a focus on scaling. While most changes maintain backward compatibility, the transaction gas limit cap, `MODEXP` modifications, and new opcode and precompile may require attention from developers and security engineers. By understanding these changes and testing contracts thoroughly, developers can ensure their applications continue to function correctly on Ethereum's evolving platform.
