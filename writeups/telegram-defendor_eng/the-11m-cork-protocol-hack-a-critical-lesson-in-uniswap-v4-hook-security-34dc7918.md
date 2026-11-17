# 🔐 $11M Cork Protocol Hack Exposed Critical Uniswap V4 Hook Flaws

- **Source URL:** https://dedaub.com/blog/the-11m-cork-protocol-hack-a-critical-lesson-in-uniswap-v4-hook-security
- **Fetched:** 2026-11-17
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/63 (id 63)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The $11M Cork Protocol Hack: Uniswap V4 Hook Vulnerability | Dedaub

On 28th of May 2025, Cork Protocol suffered an $11M exploit due multiple security weaknesses, culminating in a critical access control vulnerability in their Uniswap V4 hook implementation. The attacker exploited missing validation in the hook’s callback functions fooling the protocol into thinking that valuable tokens (Redemption Assets) were deposited by the attacker, thus crediting the attacker with a number of derivative tokens that could be exchanged back to other valuable tokens. The attacker also exploited a risk premium calculation, which compounded the attack. Among other things, this incident highlights the importance of proper access control in Uniswap V4 hooks and the risks of highly flexible open designs, which are very hard to secure.

## **Background**

### **Understanding Cork Protocol**

Cork Protocol is a depeg insurance platform built on Uniswap V4 that allows users to hedge against stablecoin or liquid staking token depegs. The protocol operates with four token types per market:

- **RA (Redemption Asset)** : The “original” asset (e.g., wstETH)
- **PA (Pegged Asset)** : The “riskier” pegged asset (e.g., weETH)
- **DS (Depeg Swap)** : Insurance token that pays out if PA depegs from RA
- **CT (Cover Token)** : The counter-position that earns yield but loses value if depeg occurs

Another way to think of the DS is a put option at a fixed strike price denominated in RA, while CT is the corresponding short put.

Users can mint DS + CT by depositing RA, effectively splitting the redemption asset into two complementary positions. A legitimate transaction demonstrating this in action can be found [here](https://app.dedaub.com/ethereum/tx/0xc5f5f1cfa0e572684c2d345abadb930625251fafc556dc2f45b6985aeecd9f29?line=1,0,0,11,5).

Unlike modern options protocols such as Opyn, the DS is fully collateralized with RA, which simplifies trust assumptions.

### **Understanding Uniswap V4**

Uniswap V4 represents a significant architectural shift, moving to a central `PoolManager` (Singleton pattern) and introducing ‘hooks’ - external contracts that the `PoolManager` calls at various points in a pool’s lifecycle (e.g., before or after swaps, liquidity changes). This design, as [highlighted by security experts](https://x.com/drdr_zz/status/1928474034666131848) like Damien Rusinek, offers immense flexibility and customization but, as the Cork Protocol incident demonstrates, also introduces new, critical security considerations for developers.

## **Vulnerability 1: Missing Access Control**

An important vulnerability in the CorkHook contract was a critical oversight directly echoing a common pitfall warned about by many security researchers. Cork’s Uniswap hooks were called by the attacker’s smart contract directly, mid-transaction. Let’s examine the vulnerable `beforeSwap` function:

```
function beforeSwap(
   address sender,
   PoolKey calldata key,
   IPoolManager.SwapParams calldata params,
   bytes calldata hookData
) external override returns (bytes4, BeforeSwapDelta delta, uint24)
```
Critical Issue: This function lacks an onlyPoolManager modifier (allowing only calls from a trusted Uniswap v4 manager), meaning anyone can call it directly with arbitrary parameters. While the contract inherits from BaseHook, which provides access control for unlockCallback, it fails to protect other hook callbacks.

```
// BaseHook provides this for unlockCallback: 
modifier onlyPoolManager()
```
## **Vulnerability 2: Risk premium calculation rollover**

Risk premium, which affects the price of derivative (CT) tokens had an extreme value when close to expiry. The exploiter acquired a small amount of DS tokens close to the expiry, manipulating the price ratio of CT to RA tokens. On rollover (for a new expiry period), this skewed ratio was used to compute how many tokens of CT and RA to deposit to the AMM. With a skewed ratio of CT to RA tokens deposited, the exploiter could convert a very small amount of 0.0000029 wstETH to 3760.8813 weETH-CT.

**The Attack**

Cork Protocol allowed DS (Insurance) tokens from one market to be used as RA (Safe assets) tokens in another market. This was likely not an intentional design choice, and the protocol authors probably didn’t think of this possibility. An unintentional consequence of this is that relatively valuable tokens (DS tokens) from a good market can potentially be accessed from another market if there’s a vulnerability.

This relatively obscure security weakness compounded the exploit perpetrated by this attacker in a very complex, multi-step attack.

### STEP 1: CROSS-MARKET TOKEN CONFUSION

The attacker created a new market configuration that used one of the DS token in another market as an RA token in the new market.

```
// Legitimate market
Legit Market: {
   RA: wstETH,
   PA: weETH,
   DS: weETH-DS,
   CT: weETH-CT
}
// Attacker's new market 
New Market: { 
   RA: weETH-DS, // Using DS token as RA!
   PA: wstETH,
   DS: new_ds,
   CT: new_ct
}
```
### Step 2: Malicious Hook Contract

The attacker deployed their own contract implementing the hook interface and [rate provider interface](https://app.dedaub.com/ethereum/tx/0xfd89cdd0be468a564dd525b222b728386d7c6780cf7b2f90d2b54493be09f64d?line=1,0,21,0,0,21). The custom rate provider appears to be a red herring in this attack - it simply returns a fixed rate.

The new market utilized a fresh Uniswap v4 pool created as part of the new market. The attacker also created (in a separate transaction) a Uniswap pool with the same tokens as a the newly created pool (trading new\_CT and weETH-DS) but with the hacker’s contract as the hook!

### Step 3: Direct Hook Manipulation

This is where the action takes place. Due to the missing access control, the attacker could directly call `beforeSwap` to fool the protocol:

This pool id of the maliciously-created pool was passed into the beforeSwap callback. The hook data supplied as part of the callback directed the protocol to an execution flow by which RAs are deposited and CT and DS tokens are returned. However, in such a transaction no RAs were deposited by the attacker. Instead an amount of roughly 3761 weETH-DS were credited towards the attacker. The carefully crafted hook data payload fooled Cork protocol into thinking that the attacker had deposited 3761 weETH-DS. By doing so the attacker illegitimately gains 3761 new\\\_ct and 3761 new\\\_ds tokens.

### Step 4: DS Token Extraction

Once the attacker has gained the new\\\_ct and new\\\_ds tokens, the attacker used these to redeem weETH-DS tokens.

### Step 5: wstETH Token Extraction

Note that in a previous step the attacker has also exploited another edge case to cheaply acquire weETH-CT tokens. Since writing this article, a clearer explanation was posted by the Cork protocol team about the [miscalculations involved](https://www.cork.tech/blog/post-mortem), however the essence is that the exploiter acquired a small amount of DS tokens close to the expiry, manipulating the price ratio of CT to RA tokens in the next expiry period. With this manipulation, the exploiter could convert 0.0000029 wstETH (a very small amount) to 3760.8813 weETH-CT.

Now, all that remains to be done by the attacker is to redeem these weETH-CT and weETH-DS tokens through the protocol, as intended, to withdraw $11m of wstETH.

## Technical Deep Dive: Hook Manipulation

The `_beforeSwap` function contains complex logic for handling swaps, including reserve updates and fee calculations:

```
function _beforeSwap(
 PoolState storage self,
 IPoolManager.SwapParams calldata params,
 bytes calldata hookData,
 address sender
) internal returns (int256 unspecificiedAmount) {
   // ... swap calculations ...
   // Update reserves without validation
   self.updateReservesAsNative(Currency.unwrap(output), amountOut, true);
   // Settle tokens
   settleNormalized(output, poolManager, address(this), amountOut, true);
   // ... more logic ...
}
```
Without access control, an attacker can:

- Manipulate reserve ratios before legitimate trades
- Force the hook to settle tokens with arbitrary amounts
- Bypass normal swap routing through the PoolManager

Parsing the arguments used in hookData, the attacker crafted a payload intended to indicating that they deposited 3761 of weETH-DS tokens into the new market.

## Contributing Factors

### 1. Decentralized Market Creation

The protocol allowed anyone to create markets with any token pair. This is a courageous design decision, however it’s clearly hard to pull off correctly.

```
function beforeInitialize(address, PoolKey calldata key, uint160) external ... {
   address token0 = Currency.unwrap(key.currency0);
   address token1 = Currency.unwrap(key.currency1);
   
   // Dedaub: No validation on token types!
   // Allows DS tokens to be used as RA tokens
}
```
### 2. Insufficient Token Validation

The `_saveIssuedAndMaturationTime` function attempts to validate tokens but fails to ensure proper token types:

```
function _saveIssuedAndMaturationTime(PoolState storage self) internal {
   IExpiry token0 = IExpiry(self.token0);
   IExpiry token1 = IExpiry(self.token1);
   // Dedaub: Only checks if tokens have expiry, not their type
   try token0.issuedAt() returns (uint256 issuedAt0) {
       self.startTimestamp = issuedAt0;
       self.endTimestamp = token0.expiry();
       return;
   } catch {}
   // ... similar for token1 ...
}
```
### 3. No Pool Whitelisting

The callback allowed pools that had the same tokens, but a different hook contract. There was no validation on the pool id nor the hook contract address.

```
mapping(PoolId => bool) public allowedPools;
modifier onlyAllowedPool(PoolKey calldata key) {
   require(allowedPools[key.toId()], "Pool not allowed");
   _;
}
```
### 4. Singleton Design

Tokens from the different markets co-mingled (Singleton pattern). Therefore, a vulnerability that was applied to the new market managed to extract tokens pertaining to another market.

## Previous Cork Protocol Audits

Unfortunately, although the Cork protocol had undergone security reviews by four different audit providers, this incident still happened. The protocol team had clearly invested resources in security, making this exploit all the more tragic for both the team and users.

However, among the four auditors, three of them didn’t audit the vulnerable hook contracts, and it is uncertain whether the risk premium issue could have been easily found just by looking at the code. It is likely that Cantina/Spearbit had the vulnerable CorkHook contract within their audit scope. A [pull request with recommendations](https://github.com/Cork-Technology/Cork-Hook/pull/19/files) shows they did identify some issues and suggested improvements.

Runtime Verification (another auditor who did not have CorkHook in their scope) presciently noted in their report:

“An interesting follow-up engagement would be to prove the invariants for the CorkHook functions that are being invoked by different components verified within the scope of this engagement, as well as the functions of other contracts, such as CorkHook, Liquidator and HedgeUnit.”

This observation now seems particularly prophetic, as it was precisely the CorkHook’s interaction with other components that enabled the exploit.

## Recommendations for Hook Developers

If you’re building a project that interacts with Uniswap v4 Hooks in a meaningul way, get your code audited by experts in the area. Dedaub is Uniswap-whitelisted audit provider, with plenty of experience securing high-stakes projects. Since Dedaub is whitelisted by Uniswap, the audit can also be paid for via a Uniswap Foundation grant. In the meantime, follow the guidelines below. We also recommend listening to Damien Rusinek’s talk.

### **Master Access Control and Permissions**

**Strict `PoolManager`-Only Access:** This is non-negotiable. Every external hook function that can modify state or is intended to be called by the `PoolManager` (e.g., `beforeSwap`, `afterSwap`, `beforeInitialize`) *must* implement robust access control, typically an `onlyPoolManager` modifier. This was a primary failing in the Cork exploit. As Damien and Hacken emphasize, allowing direct calls by arbitrary addresses is a direct path to state manipulation and fund loss. *Cork didn’t follow this recommendation.*

**Correct Hook Address Configuration:** Uniswap V4 derives hook permissions (which functions the `PoolManager` will call) directly from the hook contract’s address.

**Address Mining:** Deploy hooks using `CREATE2` with a salt that ensures the deployed address correctly encodes *all* intended permissions (e.g., `Hooks.BEFORE_SWAP_FLAG | Hooks.AFTER_SWAP_FLAG`). *Cork didn’t follow this recommendation.*

**Mismatch Avoidance:** A mismatch between the functions implemented in your hook and the permissions encoded in its address will lead to functions not being called or `PoolManager` attempting to call non-existent functions, causing reverts (DoS).

**Future-Proofing Upgrades:** If you plan to add new hookable functions in future upgrades (for UUPS-style proxies), ensure the initial deployment address *already encodes these future permissions*. Alternatively, include placeholder functions for them.

**Inherit from `BaseHook`:** Whenever possible, inherit from Uniswap’s `BaseHook` contract. It provides foundational security checks (like `onlyPoolManager` for `unlockCallback`) and helps ensure correct interface adherence, reducing the risk of configuration errors.

### **Rigorous State Management and Pool Interaction**

**Restrict Pools.** If a hook is designed for a specific pool or set of pools, it *must* validate the `PoolKey` in its functions (especially initialization) to prevent unauthorized pools from using it. Consider implementing an `allowedPools` mapping and a modifier like `onlyAllowedPool`. Ensure the hook can only be initialized once (e.g., in `beforeInitialize`) to restrict it to a single pool if that’s the design. *Cork didn’t follow this recommendation.*

**Isolate State for Reusable Hooks:** If a hook is intended to be shared across multiple legitimate pools, its internal state must be meticulously segregated (e.g., using `mapping(PoolId => PoolSpecificData)`). Failure to do so can lead to one pool’s activity corrupting another’s state, potentially locking funds or creating exploitable conditions.

**Prevent Cross-Market Token Contamination:** As seen in the Cork exploit, avoid designs where tokens (especially sensitive ones like derivatives or collateral) from one market can be misinterpreted or misused as different token types in another market. Enforce strict token type validation at market creation and within hook logic.

**Understand `sender` vs. `msg.sender` vs. Transaction Originator**. In hook functions like `beforeSwap(address sender, ...)` the `sender` parameter is typically the `PoolOperator` or the `PoolManager` itself, *not* the end-user (EOA) who initiated the transaction. If your hook logic needs the actual end-user, that address must be securely passed via the `hookData` parameter by a trusted `PoolOperator`.

**Understand Delta Accounting.** `BeforeSwapDelta` and `BalanceDelta` are from the *hook’s perspective*. If the hook takes a fee, it must be a *negative* delta. If it grants a rebate, it’s a *positive* delta. Ensure the correct order of token deltas (e.g., specified vs. unspecified, or token0 vs. token1) based on the swap direction (`params.zeroForOne`). **Crucially, all deltas must net to zero by the end of the `unlockCallback`**. The `PoolManager` tracks this with `NonzeroDeltaCount`. Unsettled balances will cause the transaction to revert. Hooks modifying balances must ensure they (or the user) settle these amounts correctly (e.g., via `settle()` or `take()`).

**Upgradability:** If your hook is upgradeable, recognize this as a significant trust assumption. A malicious or compromised owner can change the hook’s logic entirely. Ensure the upgrade mechanism is secure and governed transparently.

## Conclusion

The Cork Protocol hack demonstrates that Uniswap V4 hooks, while powerful, introduce new security considerations that developers must carefully address. The combination of missing access controls and insufficient token validation created a perfect storm for exploitation. As the DeFi ecosystem continues to evolve with more composable protocols, developers must prioritize security at every layer of their architecture.
