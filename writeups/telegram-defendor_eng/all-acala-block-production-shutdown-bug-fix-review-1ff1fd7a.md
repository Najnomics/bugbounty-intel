# 🛑 Critical vulnerability in Acala could have stopped block production

- **Source URL:** https://immunefi.com/blog/all/acala-block-production-shutdown-bug-fix-review
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/183 (id 183)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*•*5 min read

# Acala Block Production Shutdown Bug Fix Review

### Introduction

Acala, a Polkadot parachain, received a report from whitehat @Lastc0de on Immunefi and quickly patched the vulnerability that could have allowed an attacker to fully stop block production on the parachain.

The project quickly acknowledged the vulnerability, and after some discussions between Immunefi, the project, and the whitehat, both parties agreed on a bounty of $70,000 USDT for the reported bug.

### Overview of the Project

Acala is a DeFi platform and parachain built on the Polkadot network. The Acala Foundation nurtures applications in the fields of decentralized finance protocols. One of their products is Homa. Homa is a Tokenized Liquidity Staking Protocol.

Today, we need to mostly be focused on parachain and the Homa module.

**Let’s start by understanding what Polkadot parachains are and how they work:**

Polkadot has a Relay Chain. The Relay Chain serves as the foundational layer, responsible for coordinating the network while maintaining minimal functionality — excluding features like smart contract execution. Instead, it delegates processing tasks to parachains, which operate as independent blockchains with customizable functionality.

The relay chain can support a number of execution cores (i.e. in the picture above 8 cores), like cores on a computer’s processor. Each one of these cores can run one process at a time, or in our case one parachain at a time. A project must secure a parachain slot through a voting mechanism to operate within the network. Acala successfully obtained a parachain slot, allowing it to run its independent blockchain within Polkadot’s ecosystem.

In parachains, para-validators are a group of validators selected each epoch to validate parachain blocks for all parachains connected to the relay chain. Selected validators are responsible to finalize the block on the selected parachain. They are responsible for finalizing the block within a set time. But if it would take too long to finalize the block, such a situation will lead to a halt of a parachain.

**What is Homa?**

Each parachain within Polkadot has the flexibility to introduce unique functionalities. For example, Moonwell integrated Ethereum Virtual Machine (EVM) compatibility, enabling smart contract execution. Similarly, Acala introduced the Homa module, designed to optimize staking liquidity.

Homa is a Tokenized Staking Liquidity Protocol that allows users to stake their DOT (Polkadot tokens) in exchange for LDOT. Holders of LDOT can continue earning staking rewards. It has the same idea as a liquid staked tokens of Ethereum.

To redeem DOT from the staking protocol, users submit an unbond request. Requests are processed approximately every 24 hours, after which the unbond action will be performed on Polkadot.

### Vulnerability Description

So whenever a user sends a redeem request, the request is saved in a map. About every 24 hours, `on_initialize` function of Homa module is called by the validator, which iterates over this map to do some calculation and finalize the withdrawals.

The vulnerability is that a module has no limit on the size of the map to process for a validator on one call. This allows a malicious actor to create many redemption requests from different accounts, which increases the time required to run `on_initialize` and require more time to finalize the block. In some cases this will force the network to halt.

Let’s dive into the code to find the root cause of the vulnerability

The `on_initialize` function calls `bump_current_era` function, whenever it is not zero.

modules/homa/src/lib.rs

```
fn on_initialize(_: BlockNumberFor<T>) -> Weight {
    let bump_era_number = Self::era_amount_should_to_bump(T::RelayChainBlockNumber::current_block_number());
    if !bump_era_number.is_zero() {
        let _ = Self::bump_current_era(bump_era_number);
        /* snippet of code */
    } else {
/* snippet of code */
    }
}
```
Then `bump_current_era()` calls `process_redeem_requests()`

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
And the root cause is in the `process_redeem_requests` function.

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
As we can see, there is a `for` loop that goes through every redeem request and processes it.

A design flaw results in a processing bottleneck when handling a high volume of requests; the linear processing of each request leads to increased latency.

Acala finalizes the withdrawals approximately every 24 hours, giving an attacker that time to prepare for an attack. In that period, the attacker needs to allocate `RedeemThreshold` amount to 22000 wallets and submit a redeem request from each one. All these redeem requests will be added to the map, which the validator would have to go through to finalize the block and process the withdrawal requests. However, since the map will hold 22000 withdrawal requests, the validator will not be able to go through all of them in a `for` loop. This will make it impossible to process redeem requests. Therefore, the block can not be created. As a result, Acala will not be able to produce new blocks.

### Prerequisites for the Exploit:

After tests, it is concluded that anyone who had more than 12000 DOT was able to spam the network and eventually cause the block production to stop due to the overwhelming amount of requests. After spam an attacker will be able to claim back their DOT from 22000 accounts, so the only expense for an attack are gas fees.

To wrap it up, here is the step-by-step breakdown of the attack from the attacker's perspective:

1. **Attacker possesses 12,000+ DOT:** The attacker has the required 12,000+ DOT to initiate the attack.
2. **Attacker observes 24-hour redeem cycle:** Acala processes withdrawals every 24 hours, giving the attacker time to prepare.
3. **Attacker allocates `RedeemThreshold` amount:** Minimum redeem amount of tokens is distributed to 22,000 different wallets.
4. **Attacker submits redeem requests:** Each of the 22,000 wallets submits a redeem request.
5. **Redeem requests fill the map:** All 22,000 requests are added to the Homa module’s `RedeemRequests` map.
6. **Validator calls `on_initialize` to process requests:** The validator’s call to `on_initialize` function begins iterating through the massive map of redeem requests in a `for` loop.
7. **Processing exceeds create block time limit:** The `for` loop in `process_redeem_requests` takes too long to execute due to the high number of requests.
8. **Block creation fails:** The validator cannot validate the block within the allotted time.
9. **Acala parachain halts:** Failure to create the block leads to the Acala parachain stopping block production.
10. **Attacker claims DOT:** After the blockchain goes back live, an attacker will be able to claim their DOT from the 22,000 wallets, so the only expense being gas fees.

In order to mitigate the attack, and get the chain back to working state, a fork of a chain will be required. Since Acala is a parachain, in order to make a soft-fork, it has to be proposed to the Polkadot Governance, and it usually takes between 15–24 days to be approved. That means that the Acala network would be down for 15 days. By the time of a submission, according to DefiLlama Acala’s volume over 15 days was $712,420. This can be considered as an impact of an attack, and the whitehat received a bounty equal to \~10% of it.

### Mitigation/Fix

Acala fixed the vulnerability by limiting a number of redeem requests to process in the following pull request: [https://github.com/AcalaNetwork/Acala/pull/2806](https://github.com/AcalaNetwork/Acala/pull/2806?ref=immunefi.com).

### Closing Acknowledgements

We would like to thank the whitehat [@Lastc0de](https://x.com/thel4stc0de?s=11&ref=immunefi.com) for doing an amazing job in responsibly disclosing such an important bug. Big props also to the Acala team who quickly responded to the report and patched the issue.

If you’re a developer or a whitehat considering a lucrative bug-hunting career in web3 — this message is for you. With 10–100x the rewards commonly found in web2, your efforts will pay off exponentially by switching to web3.

Check out the [Web3 Security Library](https://github.com/immunefi-team/Web3-Security-Library?utm_source=immunefi), and start earning rewards on Immunefi — the leading bug bounty platform for web3 with the world’s biggest payouts.

### **Resources:**

[https://github.com/AcalaNetwork/Acala-white-paper/blob/master/Acala\_Whitepaper.pdf](https://github.com/AcalaNetwork/Acala-white-paper/blob/master/Acala_Whitepaper.pdf?ref=immunefi.com)
