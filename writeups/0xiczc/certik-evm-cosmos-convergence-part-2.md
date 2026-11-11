# certik-evm-cosmos-convergence-part-2

- **Source URL:** https://certik.com/resources/blog/evm-cosmos-convergence-research-from-security-base-part-2
- **Fetched:** 2026-11-11
- **Researcher:** 0xiczc
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

**TL;DR:** In [Part 1](/blog/5qV6J92hIMutH80pzRGHD3-evm-cosmos-convergence-research-from-security-base-part-1) of this blog series, we examined the integration of EVM and Cosmos at the application layer, and the risks associated with merging these stacks. Part 2 introduces a novel method for interacting with Cosmos through EVM transactions. Specifically, it details the workflow of specialized precompiled contracts engineered to overcome functional limitations and establish a connection between the two ecosystems.

## Overview

With the development of the convergence of the Ethereum Virtual Machine (EVM) stack over Cosmos, there is a new pattern of interoperability of `precompile` to interact with the native Cosmos stack from the EVM.

By adding custom EVM precompiles to Ethereum’s basic feature set, Cosmos EVM allows developers to use previously unavailable functionality in smart contracts, such as staking and governance operations. This will allow more complex smart contracts to be built on a Cosmos EVM chain and further improves the interoperability between Cosmos and Ethereum.

## EVM Precompiles Work Flow

EVM precompiles are built-in contracts within the EVM, offering specialized functions accessible to other smart contracts. They are typically employed for impractical or costly operations to execute via standard smart contracts, including hashing, elliptic curve cryptography, and modular exponentiation.

To facilitate functionalities that necessitate altering the blockchain’s state, Cosmos introduces stateful precompiled smart contracts. Unlike the standard EVM precompiles, which are limited to reading state information, these stateful precompiles can ultimately change the chain state (i.e. the underlying Cosmos state including `staking`, `bank`, `vesting`, .etc.).

The picture above illustrates how EVM precompiles enable interoperability between the EVM and Cosmos SDK modules within a Cosmos chain application:

1. The application starts with both an EVM state (managed by the `x/evm` module) and the chain’s native Cosmos SDK states.
2. The EVM keeper initializes available static precompiles, which include: 
  - EVM legacy precompiles, such as those from the Berlin hardfork.
  - Stateless precompiles, such as `p256` for the secp256r1 algorithm and `bech32` for Bech32 encoding.
  - Stateful precompiles, which provide access to various Cosmos SDK modules:
    - `stakingPrecompile` for `x/staking` operations
    - `distributionPrecompile` for `x/distribution` operations
    - `ibcTransferPrecompile` for IBC transfer operations
    - `vestingPrecompile` for `x/vesting` operations
    - `bankPrecompile` for `x/bank` operations
    - `govPrecompile` for `x/gov` operations
    - `slashingPrecompile` for `x/slashing` operations
    - `evidencePrecompile` for the evidence module
Through these precompiles, a wide range of underlying Cosmos SDK states become accessible via the EVM.
3. When an EVM transaction is executed and routed to a precompile, it can interact with the corresponding Cosmos SDK state.
4. This mechanism allows single EVM transactions to handle and manage native Cosmos SDK functionalities, effectively enforcing EVM interoperability with Cosmos.

## Security Issues By Inconsistency in States

To effectively bridge the gap between the EVM and the native Cosmos, a comprehensive understanding of their respective state management is indispensable. The fundamental differences in how state is maintained and altered between these two distinct stacks present a complex challenge that demands meticulous attention.

Primarily, when alterations to the state occur within the independent native Cosmos stacks, the resulting changes are not automatically reflected within the EVM. This divergence creates potential synchronization issues that could undermine the integrity and reliability of the interoperability between them. Therefore, continuous and robust examination of state transitions within the Cosmos is not merely advisable, but essential. This must encompass a detailed tracking of all interactions that might influence the EVM state or its associated processes.

Furthermore, a detailed investigation into precompiled contracts within the Cosmos is necessary. Precompiles, which are essentially pre-programmed functions designed to perform complex operations, can introduce unique attack vectors if not correctly implemented or securely managed. These investigations must delve into existing precompile issues and diligently identify any security vulnerabilities that could be exploited. A thorough security audit should be conducted, focusing specifically on the potential for unauthorized state changes, data breaches, or denial-of-service attacks that might be triggered via these precompiles.

By rigorously examining these aspects, one can develop strategies to ensure the seamless operation and security of hybrid EVM-Cosmos architectures. This proactive approach is crucial for maintaining system stability and preventing significant disruptions.

### Precompiles Executions Reflects Partial State Transition Changes

In EVM, the stateDB provides the primary interface for accessing accounts and manages a map of stateObjects, incorporating two memory storage variables: originStorage and dirtyStorage. Following the execution of an EVM transaction, the EVM state is updated via `stateDB.Commit()`. The process iterates through all modified storage entries, i.e. dirtyStorage. If it is different from the originStorage, the Cosmos SDK KVStore will be updated to reflect the new state. Essentially, only the changed storage entries are written back to the underlying Cosmos key-value store, just as below code snippet shows:

A relevant code reference can be found [here (opens in a new tab)](https://github.com/evmos/evmos/blob/v16.0.3/x/evm/statedb/statedb.go#L445). However, prior to `evmos` @v16.0.4, there was no state transition in different states, such as `bank` and `distribution`. In precompiles/bank, a relevant code reference can be found [here (opens in a new tab)](https://github.com/evmos/evmos/blob/v16.0.3/precompiles/bank/bank.go#L102).

The 2nd output `stateDB` is shadowed, and commit has not been executed along with the bank state.

The same issue happened in `distribution` ([code reference (opens in a new tab)](https://github.com/evmos/evmos/blob/v16.0.3/precompiles/distribution/distribution.go#L86)) and `ics20` ([code reference (opens in a new tab)](https://github.com/evmos/evmos/blob/v16.0.3/precompiles/ics20/ics20.go#L85)). `stateDB.commit` has not been executed along with the distribution and ibc Transfer state, respectively.

Exploitation could stem from the reliance on the `stateDB.Commit()` method for synchronizing Cosmos SDK and EVM states. Potential steps to execute the attack could be taken as following:

1. A user initiates a transaction to a smart contract (SC) which, in turn, calls a precompile.
2. The SC transitions its state from A to B.
3. The SC then calls the precompile.
4. Subsequently, the SC reverses the previous state transition, returning from state B back to A.
5. Upon transaction execution and final commit in stateDB, state A remains uncommitted to the store, as it is identical to the origin storage state.

A critical vulnerability exists when a contract storage state remains unchanged before and after a transaction, but is modified during the transaction. If an external contract call is made after this intermediate change, the transaction can lose its atomicity. This flaw is severe and could result in fund drainage through sophisticated smart contract interactions.

The issue, identified as `GHSA-3fp5-2xwh-fxm6` in `evmos` at [GHSA-3fp5-2xwh-fxm6 (opens in a new tab)](https://github.com/evmos/evmos/security/advisories/GHSA-3fp5-2xwh-fxm6), has been addressed. A patch was implemented, which was reflected in commit [08982b5e (opens in a new tab)](https://github.com/evmos/evmos/commit/08982b5ee726b97bc50eaf58d1914829648b6a5f). This patch has been incorporated into `evmos` version 17.0.0 onward.

### Precompiles Execution Reversion Collides States Between EVM and Cosmos

From the previous section we observed the partial synchronization between EVM and Cosmos states, specifically within the `bank`, `distribution`, and other states after a successful precompile execution. However, what happens if the precompile execution reverts?

Consider `staking` delegation as an example. If an external EVM transaction intentionally reverts, how can the underlying Cosmos state, such as the `staking` state, remain consistent and reflect the changes? Let's dive into the [following code (opens in a new tab)](https://github.com/evmos/evmos/blob/v18.1.0/precompiles/staking/tx.go#L169) as a reference:

From the code above, the execution of the `staking` precompile necessitates two distinct access roles: the contract caller and `EVM.origin`. Ordinarily, these roles are identical. However, circumstances may arise where they diverge. Specifically, when a smart contract initiates an invocation of a precompiled contract, `EVM.origin` corresponds to the initial sender of the EVM transaction, which is typically an Externally Owned Account (EOA). In such instances, the contract caller for the precompiled contract is the invoked smart contract, identifiable by its respective contract address.

An exploit arises when an attacker-controlled contract, holding X tokens, delegates these tokens to validator Y. This vulnerability occurs because the attacker contract invokes the precompiled delegate function (an external call) to modify the Cosmos delegation state, but then immediately reverts the EVM state changes using a try/catch block. Consequently, the delegated tokens return to the attacker contract within the EVM environment.Due to the try/catch capturing the external EVM call failure (delegate), the EVM transaction commits without errors. However, the Cosmos staking state remains as it was before the reversion.

To resolve this issue, the solution is straightforward: since the transaction is an EVM transaction, the application currently relies on the EVM state as the definitive source. Consequently, precompile transactions result in incorrect state changes, and should revert as well accordingly during the course of EVM transaction execution.

The issue, identified as `GHSA-68fc-7mhg-6f6c` in `evmos` at [GHSA-68fc-7mhg-6f6c (opens in a new tab)](https://github.com/evmos/evmos/security/advisories/GHSA-68fc-7mhg-6f6c), has been addressed. A patch was implemented, which is reflected in commit [bb2d504 (opens in a new tab)](https://github.com/evmos/evmos/commit/bb2d504eec9078d6eff6981fc0cb214e8a3ca496). One piece of code could be found at [this reference (opens in a new tab)](https://github.com/evmos/evmos/blob/v19.0.0/precompiles/staking/tx.go#L227):

This guarantees that the EVM `stateDB` accurately reflects the modifications made in the bank keeper when invoking the precompile from a smart contract. This patch has been merged into `evmos` version 19.0.0 onward.

Different teams have different solutions to address the issue, but fundamentally, they all align with the previous solution strategy regarding the reversion to rollback of states accordingly in both EVM and Cosmos.

### Precompiles Out-of-Gas Leads To Partial State Write

Stateful precompiled smart contracts, herein referred to as `precompiles`, could mutate the Cosmos states, as previously elaborated. To facilitate these precompile functionalities, a low gas configuration has been instituted at a foundational layer, exemplified in the [provided code (opens in a new tab)](https://github.com/evmos/evmos/blob/main/precompiles/common/precompile.go#L61).

A gas limit of several thousands would typically suffice for `precompile` execution. However, this minimal gas allocation allows users to initiate precompiles and then encounter errors mid-execution. Consequently, partial state changes resulting from this process might not be reverted.

Specifically, a vulnerability during the distribution precompile and fund claims process could lead to illicit fund transfers without clearing corresponding claimable rewards. Moreover, this security vulnerability permits indeterminate code execution. The validators can be effectively halted through the induction of errors at differing locations within the codebase.

In order to mitigate the identified vulnerability, a modification was implemented to ensure the atomicity of each precompile execution. This procedural adjustment guarantees that, upon the occurrence of any error, all incomplete state modifications will be reverted, thereby successfully resolving the security concern.

The issue, identified as `GHSA-mjfq-3qr2-6g84` in `cosmos/evm` at [GHSA-mjfq-3qr2-6g84 (opens in a new tab)](https://github.com/cosmos/evm/security/advisories/GHSA-mjfq-3qr2-6g84), has been addressed. For each EVM-compatible Cosmos chain, a manual patch implementation is required, as outlined in the corresponding documentation [evm os patch file (opens in a new tab)](https://drive.google.com/file/d/1LfC0WSrQOqwTOW3qfaE6t8Jqf1PLVtS_/).

Each Run method of the `precompiles` must be modified by encapsulating every switch statement and its corresponding return values within `p.RunAtomic` to make the execution atomic. As an example, consider the following codes:

`p.RunAtomic` mandates error handling through the implementation of a rollback to the EVM stateDB snapshot upon the detection of an error during the execution of core precompile logic, as below code snippet shows:

Only through this approach can the partial states (specifically the Cosmos states) write issue be properly addressed in conjunction with EVM transaction execution throughout the entire transaction lifecycle.

## Summary

A novel approach to engaging with the Cosmos stack is presented in this article, utilizing EVM transactions and demonstrating the operation of specialized precompiled contracts that bridge functionality gaps. However, vulnerabilities arise throughout the EVM transaction lifecycle due to inconsistencies between EVM and Cosmos states. This includes synchronization issues, partial reversion, and problems with state writing, as previously discussed, creating potential attack vectors.

As the evolution of convergence of EVM and Cosmos ecosystems, the integration between them has facilitated the emergence of a novel architectural strategy known as layered chains. This methodology, modeled on the post-merge Ethereum Mainnet, delineates execution and consensus layers to enhance the incorporation of EVM functionalities.

A detailed analysis of these layered chains and the confluence of the EVM and Cosmos ecosystems will be presented in Part 3 of this series. Stay tuned for the upcoming release!
