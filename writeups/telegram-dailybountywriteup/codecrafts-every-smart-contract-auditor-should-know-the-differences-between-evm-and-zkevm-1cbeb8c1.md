# Every smart contract auditor should know the differences between EVM and zkEVM

- **Source URL:** https://medium.com/codecrafts/every-smart-contract-auditor-should-know-the-differences-between-evm-and-zkevm-1ee9abe270b8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142327/https://medium.com/codecrafts/every-smart-contract-auditor-should-know-the-differences-between-evm-and-zkevm-1ee9abe270b8
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4150 (id 4150)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Every smart contract auditor should know the differences between EVM and zkEVM

In the zkEVM (Zero-Knowledge Ethereum Virtual Machine), the way memory and data are handled is different from the traditional Ethereum Virtual Machine (EVM).

let’s discuss —

**The technical details of the memory areas in the Ethereum Virtual Machine (EVM) —**

Suppose you have a smart contract for a simple voting system. When someone wants to vote for a candidate, they send a transaction. The candidate’s name and the voter’s address are part of the **calldata**. The contract then uses the **stack** (Local variables are stored here) to perform calculations like verifying the voter’s eligibility and counting the votes. If the contract interacts with other contracts to update the voting results, the data returned from those contracts would be stored in the **returndata** for further processing in the contract.

**Memory**: The memory in EVM is like a temporary scratchpad where data can be stored and manipulated during the execution of a smart contract. For instance, if you’re calculating the sum of two numbers, you can store the numbers in memory, add them, and then retrieve the result.

It is a continuous byte array that starts empty. The contract can use opcodes like `MSTORE` to write data to memory and `MLOAD` to read data from memory.

**Calldata**: Calldata is a special type of memory that contains the input data of a transaction. It’s immutable, meaning you can’t modify it, and it…
