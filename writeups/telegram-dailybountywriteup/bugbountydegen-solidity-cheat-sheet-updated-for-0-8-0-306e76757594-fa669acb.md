# Solidity Cheat Sheet (Updated for ^0.8.0)

- **Source URL:** https://medium.com/@bugbountydegen/solidity-cheat-sheet-updated-for-0-8-0-306e76757594?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142004/https://medium.com/@bugbountydegen/solidity-cheat-sheet-updated-for-0-8-0-306e76757594
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3722 (id 3722)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Solidity Cheat Sheet (Updated for ^0.8.0)

## Quick review to the most relevant global variables used in Solidity smart contracts

Solidity is a programming language specifically designed for writing smart contracts on the Ethereum blockchain platform. Solidity enables developers to create and deploy decentralized applications (DApps) and smart contracts that run on the Ethereum Virtual Machine (EVM).

Developers use Solidity to create various types of applications, including decentralized finance (DeFi) protocols, non-fungible tokens (NFTs), governance systems, and more, contributing to the broader ecosystem of blockchain-based applications.

Let’s quickly review the main keywords that the Solidity language provides.

## Solidity Global Variables

### block methods:

- **block.coinbase**: Current block miner’s address
- **block.difficulty**: Current block difficulty
- **block.gaslimit**: Current block gaslimit
- **block.number**: Current block number
- **block.timestamp**: Current block timestamp as seconds since unix epoch. *INSECURE! DO NOT RELY on this value*
- **now**: Alias of **block.timestamp**, removed in version 0.7.0
- **block.blockhash** (uint blockNumber): Hash of the given block when the block is one of the most recent 256 blocks, otherwise 0! *INSECURE! DO NOT RELY on this value*
- **block.chainid**: Current chain id (For Ethereum Mainnet this value is 1) [https://docs.goquorum.consensys.net/concepts/network-and-chain-id](https://docs.goquorum.consensys.net/concepts/network-and-chain-id)

### msg methods:

- **msg.data (bytes calldata)**: complete calldata passed in the arguments of a method
- **gasleft()**: It was called **msg.gas** prior to solidity 0.4.21. Returns remaining gas
- **msg.sender**: Sender of the message. (Immediate account that invoked the function)
- **msg.sig**: First four bytes of the calldata (Function identifier)
- **msg.value**: Number of wei sent with the message

### tx methods:

- **tx.gasprice**: Gas price of the transaction
- **tx.origin**: Sender of the transaction. (External account that initiated the tx). *INSECURE! DO NOT RELY on this value*

### contract methods:

- **contract.this**: The current contract
- **contract.selfdestruct(recipient)**: Destroys the current contract and sends the remaining funds to recipient
- **contract.suicide(recipient)**: Removed in version 0.5.0. Use **selfdestruct()** instead

### address methods:

- **address.balance**: Returns address balance in wei
- **address.transfer(amount)**: Send given amount to address and reverts on failure. Forwards a fixed 2300 gas stipend
- **address.send(amount)**: Send given amount to address and returns false on failure, also sends a fixed 2300 gas stipend. *INSECURE! Avoid to use as it does not revert on failure!*
- **address.call(memory)**: Issue low-level call with the given payload. *INSECURE! Avoid to use as it does not perform type checking!*
- **address.callcode(memory)**: Removed in 0.5.0. Use **delegatecall()** instead
- **address.delegatecall(memory)**: Issue a low-level **DELEGATECALL** with the given payload and returns success condition and data
- **address.staticcall(memory)**: Issue a low-level **STATICCALL** with the given payload. Returns success condition and data

### error handling:

- **require(\<CONDITION> \[, message\])**. Reverts if the condition is not met. message is optional. Used for parameters, inputs or external components
- **assert(\<CONDITION>)**. Causes a panic error and reverts changes if the condition is not met. Used for internal errors
- **revert(\[reason\])**. Abort execution and revert state changes. reason is optional

### cryptographic functions:

- **keccak256(memory):** sha3() alias was removed in version 0.5.0. Hashing function
- **sha256(memory)**: sha2() alias was removed. Hashing function
- **ecrecover(hash, v, r, s):** Recover the address associated with the public key or 0x00 if error
- **recover(hash, signature)**: Returns the address that signed the message or Zero address if error
- **abi.encodePacked(“string1”, “string2”)**: Concatenates two or more strings. Be aware that abi.encodePacked(“a”, “bc) = abi.encodePacked(“ab”, “c”). To be secure, at least one parameter must be static prior to hash the final string with keccak256(). abi.encode() is preferred

## Solidity data types:

- **bool**
- **uint/int**
- **address**: Holds a 20 byte value
- **address payable**: Same as address but with additional members send() and transfer()
- **mapping**: Be aware that is very gas intensive
- **enum**
- **struct**
- **bytes**: Type of array
- **string**: Type of array

## Solidity function visibility:

- **internal**: Default state. Variables can be accessed from this or inherited or derived contracts
- **private**: Variable only accessible from the current contract, not inherited or derived contracts
- **public**: Variable can be accessed from another contract
- **external**: This function is part of the contract interface. Cannot be called internally unless we use *this* variable

### Additional qualifiers for class methods:

- **view**: The function declares that no state variable will be changed
- **pure**: The function declares that no state variable will be changed or read
- **payable**: Function that can accept Ether from a caller

## State variables modifiers:

- **constant**: The value is fixed at compile time and cannot be changed
- **immutable**: The value is assigned at construction time and cannot be changed

## Solidity data locations:

- **storage**: Global memory available to all functions
- **memory**: Local memory
- **calldata**: Contains arguments passed to a function. Read-only memory region. Use less gass than memory
- **stack**: EVM stack (Only 1,024 depth levels)

## Solidity time units:

- seconds
- minutes
- hours
- days
- weeks
- years (Removed in version 0.5.0)

You can find more info in the Solidity official documentation:

**Follow me** on Twitter: [@bugbountydegen](https://twitter.com/intent/follow?original_referer=https%3A%2F%2Fmedium.com%2F%40bugbountydegen%2F&screen_name=bugbountydegen)
