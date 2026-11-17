# 🛡️ Invariants in Smart Contracts: Code-Level Protection

- **Source URL:** https://getrecon.substack.com/p/implementing-your-first-few-invariants
- **Fetched:** 2026-11-17
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/297 (id 297)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## Introduction

Invariants are incredibly powerful in telling us how a smart contract system should behave.

One of the best known memes in the crypto industry is the `k = x * y` invariant formula from Uniswap, which has secured trillions of dollars in transactions across several versions and forks.

More broadly, invariants are statements that should always be true about a system. We can also define statements that should only be true in certain circumstances. We call these properties. All of these help us determine how our system should behave.

We can use the documentation, whitepaper, and READMEs to define the following property types for any system. They describe how a system should work:

- Valid States
- State Transitions
- Variable Transitions
- High-Level Properties

In our [previous post](https://getrecon.substack.com/p/how-to-define-invariants), we saw how to define one of each of these property types for the commonly used ERC4626 vault standard. In this post we’ll look at how we actually implement these properties as code so we can test them with a fuzzer.

Once we have our properties in code, we’re one step away from fuzzing them using thousands of call sequences to simulate user interactions. This is how we can find critical bugs!

## Invariants As Code

We’ll be testing the following properties we defined in the previous post:

1. **[Share solvency](https://getrecon.substack.com/i/150729898/valid-state)** - The `totalSupply` of the share tokens must be >= the shares accounted to each user.
2. **[Vault balance increase](https://getrecon.substack.com/i/150729898/state-transition)** - The vault balance of the underlying asset must increase proportional to the amount of shares minted.
3. **[totalSupply after redemption](https://getrecon.substack.com/i/150729898/variable-transition)** - `totalSupply` must decrease proportional to the shares burned on a redemption.
4. **[Price per share](https://getrecon.substack.com/i/150729898/high-level-property)** - The price per share should not change, except for calls to `deposit`/`withdraw`

For simplicity, each of the implementations of these properties below use assertions with Chimera’s standardized [assertion wrapper](https://github.com/Recon-Fuzz/chimera/blob/main/src/Asserts.sol) so they work with [Echidna](https://github.com/crytic/echidna), [Medusa](https://github.com/crytic/medusa) and [Foundry](https://github.com/foundry-rs/foundry).

### Global vs Inline

Before we dive into our property implementations, we need to define two types of properties: global and inline.

Global properties are checked by the fuzzer after any call to one of the target functions and therefore always must hold. These are our textbook *invariants*, because they define characteristics of the system that should be true regardless of what operations were called. The Uniswap `k = x * y` formula is an example of this, as it should hold under all circumstances.

Inline properties are defined within a target function's handler. Handlers are the functions we use to wrap the call to the target contract. So, these properties are only checked for calls to one of these handlers. These allow us to assert that a function call had some effect on state, but by definition aren’t required to hold for other function calls. These are useful for implementing properties that only need to hold for certain state-changing operations.

In our example below, we'll implement both global and inline properties.

## Setup

We’ll be implementing invariants for the example provided in [this repo](https://github.com/Recon-Fuzz/vaults-fuzzing-example). It's a simple `ERC4626Tester` contract. It inherits from the OpenZeppelin implementation and adds some features for integration testing.

As we covered in a [prior post](https://getrecon.substack.com/p/first-day-at-invariant-school?r=34r2zr), we've used the Recon builder to scaffold all the relevant target functions for us. We then deployed our test contracts using the following [Setup](https://github.com/Recon-Fuzz/vaults-fuzzing-example/blob/7bfce3b93bf0039c3ef6888adb369444ee340613/test/recon/Setup.sol#L10-L20) contract:

*If you’re unfamiliar with how to create a scaffolding for invariant testing, check out [this](https://getrecon.substack.com/p/first-day-at-invariant-school?r=34r2zr) post.*

## Helper Tracking Variables

Before we can start implementing our invariants, we’ll need to add some helpers in our scaffolding to make our job easier.

Tracking variables in the [BeforeAfter](https://github.com/Recon-Fuzz/vaults-fuzzing-example/blob/main/test/recon/BeforeAfter.sol) contract help us track the system's state before and after any operation in our target function handlers.

For our ERC4626 vault, we can use this to track the `totalSupply` of shares and the sum of user shares:

The `ghostTotalShares` is a ghost variable. It tracks state values that aren't defined in the system but can be derived from other state values. In our case, the sum of user shares.

Since we only use one actor (`address(this)`) in our setup, we don't need to sum user shares over multiple users for `ghostTotalShares`. We can assume it's the same as the actor's shares since our actor, the address that will call our target functions, will be the only one depositing into the vault. We will explain how to use several actors in a future post.

These ghost variables let us make assertions about what these values should be with our properties.

## Defining Solidity Invariants

Now with all the necessary setup and helpers in place, we can start translating our invariants from English to Solidity.

### 1. Share solvency

For [this global property](https://github.com/Recon-Fuzz/vaults-fuzzing-example/blob/7bfce3b93bf0039c3ef6888adb369444ee340613/test/recon/Properties.sol#L15-L17), **the** `totalSupply` **of the share tokens must be >= the shares accounted to each user**, we can use the `BeforeAfter` variables we set up before:

To translate our invariant from English to Solidity, we simply read the cached values that get updated in our `BeforeAfter` variables and make an assertion on them, which turns our written property into a logical assertion.

This property is a public function, so the fuzzer will randomly call it. It’s also a global property, so it must always hold. The fuzzer will look for a call sequence that falsifies the logical statement, or in other words, that breaks the invariant. If this is possible, we’ll be shown the call sequence in our terminal so that we can understand how the invariant was broken.

The echidna and medusa fuzzers are "smart," so they use shrinking to reduce a random call sequence to the minimum needed to break the invariant, cutting out any unnecessary calls.

### 2. Vault balance increase

For the property that states that **the vault balance of the underlying asset must increase proportional to the amount of shares minted,** we can use the `previewMint` function from the ERC4626 spec in our [property definition](https://github.com/Recon-Fuzz/vaults-fuzzing-example/blob/7bfce3b93bf0039c3ef6888adb369444ee340613/test/recon/TargetFunctions.sol#L24-L32). This will let us check how many shares a user would get for a given deposit of the underlying asset.

In our property implementation, we use this to check the number of assets the vault expects to receive before a call to the `mint` function. Then, we can compare this with the actual amount of assets received by the vault, like so:

We just need to assert that the vault's balance after is equal to its balance before plus the number of assets that need to be deposited to receive a given number of shares, which we can get by calling `previewMint`.

### 3. `totalSupply` after redemption

Our property states that the `totalSupply` **must decrease proportional to the shares burned on a redemption**.

To verify this, we check the `totalSupply` of shares by reading the contract state directly in [our implementation](https://github.com/Recon-Fuzz/vaults-fuzzing-example/blob/7bfce3b93bf0039c3ef6888adb369444ee340613/test/recon/TargetFunctions.sol#L34-L41). We record the values before and after the function call using the variables `totalSupplyBefore` and `totalSupplyAfter`. Finally, we assert that `totalSupply` decreases by the amount of shares redeemed:

In this property we call the `__before()` and `__after()` functions directly because we need to read the value after the function call to make our assertion. This wouldn’t be possible with the `updateBeforeAfter` modifier because the `__after()` function would only get called after the handler function finishes executing.

### 4. Price per share

When implementing the [property](https://github.com/Recon-Fuzz/vaults-fuzzing-example/blob/bddeeb1cb9b42cc829cc65e747ef1542f68199eb/test/recon/TargetFunctions.sol#L12-L26) **the price per share should not change, except for calls to** `deposit`**/**`withdraw`, we’ll quickly realize that the ERC4626 interface lacks a direct function for querying price.

However, we can use the amount of assets we’re expected to pass in to mint 1 share via the `previewMint` function as an analog for price. So we just need to add tracking for this amount in our `BeforeAfter` contract:

Now we can call the `__before()` and `__after()` functions to update these variables in our handlers where we implement the property, similar to how we did in property 3. We can then read these values to determine if it has changed for calls to any of the handlers of interest.

We only care about changes to price from calls other than `deposit`, `mint`, `redeem`, and `withdraw`. So, we only add this property's assertion to the following target functions of interest:

We use the equality assertion wrapper to assert that the `pricePerShare` is the same for any calls to the `approve` and `transfer` functions.

## Next Steps

Now that we have real properties, we need to test them. We must check if they hold under all conditions with long fuzzing runs.

This is why we built the [Recon cloud runner](https://getrecon.xyz/), which allows you to execute fuzzing jobs that can last weeks if they need to. This allows a better exploration of the system's possible states. It gives us more confidence that our defined properties hold for all reachable states.

After long fuzzing jobs, there are three outcomes: the properties hold, they break due to an incorrect spec, or they break due to a real bug.

If your properties do hold, either the system conforms to the spec, or you lack coverage over the functions you're targeting.

In future posts, we'll see how to sort through all of these cases. This will help you determine if your setup needs fixing.

## Conclusion

We’ve looked at how to setup helpers in our Recon scaffolding that allow us to define properties in Solidity in a more straightforward manner. This helps streamline our tests with reusable tracking variables that read from state and don’t need to be redefined in each test.

The properties we implemented can be categorized as global or inline. Global properties allow us to check properties that should hold after all function calls, which we call invariants. Inline properties allow us to check if a logical statement about the system state holds only after specific function calls.

We saw how to translate these properties from English to Solidity functions using assertions. We did this by using `BeforeAfter` tracking helpers and reading state values directly from the contracts when necessary and making an assertion on what their value should be.

In the next post, we’ll look at what we need to do to ensure that our tests are effectively executed.

In the meantime, what happens when you run the above properties? Do you get any valid breaks or breaks due to misimplementation?

If you've made it this far you value the security of your protocol.

At Recon we offer boutique audits powered by invariant testing. With this you get the best of both worlds, a security audit done by an elite researcher paired with a cutting edge invariant testing suite.

Sound interesting? [Reach out to us here](https://getrecon.xyz/):
