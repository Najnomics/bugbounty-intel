# 🛡️ Sui Move: A New Model for Secure Contracts

- **Source URL:** https://www.adevarlabs.com/blog/sui-move-for-evm-and-svm-developers-part-1-mental-models
- **Fetched from:** https://web.archive.org/web/20250729184748/https://www.adevarlabs.com/blog/sui-move-for-evm-and-svm-developers-part-1-mental-models
- **Fetched:** 2026-11-26
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/318 (id 318)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
## Mental Models: From Storage to Objects

EVM organizes state around storage slots within smart contracts, where all your variables live in sequential 256-bit slots. Solana treats everything as an account: Programs are stateless and data lives in separate account structures. Sui treats everything as an object with unique IDs and clear ownership: You own things in the literal sense, even the permissions (more on this later). Each approach changes how you think about organizing and accessing data.

### EVM: Monolithic Contract Storage

EVM treats each smart contract like a mini-computer with its own storage space. When you deploy a contract, all your state variables, mappings, balances, and/or arrays get packed into sequential 256-bit slots within that contract's address. Everything lives together in one place, which makes it straightforward to reason about but can get messy when contracts become large and complex. It's the most familiar model for developers coming from traditional programming, where you'd naturally group related data and functions into a single class or module.

### SVM: The Account-Based Architecture

Solana operates on the principle that everything is an account: programs, data, even the system itself. Smart contract code lives in program accounts, user balances live in token accounts, and any persistent data gets stored in dedicated data accounts. This means you can't just declare a variable and expect it to persist; You need to design account structures to hold your data and explicitly manage which accounts your program interacts with. The benefit is massive parallelization since the runtime knows exactly which accounts each transaction will touch, but it requires thinking in terms of account relationships rather than traditional contract storage.


### Sui Move: The Object-Centric Model

Sui treats everything as objects with unique IDs and clear ownership rules—coins, NFTs, smart contracts, and system resources all exist as individual objects rather than data stored within contracts or accounts. Unlike other blockchains where logic and data are bundled together, Sui separates code (module objects) from data (instance objects). Your coin balance exists as a standalone object that references shared module objects for its behavior. When you transfer value or update state, you're literally moving or modifying these objects, and simple operations like token transfers can bypass validator consensus entirely since they only affect single-owner objects. This object-centric model makes composability natural since objects can contain other objects or references, but requires rethinking application architecture around ownership patterns and object interactions rather than traditional contract-based logic.

## Basic Operations Across Ecosystems

Now, let's discuss the basic operations that are involved in every smart contract and see **how they are implemented in Move compared to SVM and EVM.**

### Native Token Transfers

#### Ethereum

In Ethereum, native ETH transfers work through direct balance updates in the global blockchain state. When Alice sends 1 ETH to Bob, the EVM decrements Alice's account balance and increments Bob's account balance atomically within a single transaction. Both balances are stored in the global state trie, which means that every ETH transfer requires aworld state update and full validator consensus. This is the simplest form of value transfer in Ethereum - no smart contracts involved, just direct account-to-account balance modifications that the protocol handles natively through the state transition function.

#### Solana

In Solana, native SOL transfers are handled by the System Program, which manages account creation and SOL balance updates. When Alice sends 1 SOL to Bob, she creates a transaction containing a system\_instruction::transfer instruction that invokes the System Program. The System Program then decrements the lamports (SOL's smallest unit) from Alice's account and adds them to Bob's. Unlike EVM's global state model, each user has their own account that stores their SOL balance as account data. The System Program executes this transfer by reading both accounts, validating ownership through cryptographic signatures, and atomically updating both account balances. This account-based approach allows Solana to process multiple non-conflicting transfers in parallel since the runtime can identify which accounts each transaction will modify.

#### Sui

In Sui Move, native SUI transfers work through object manipulation rather than balance updates. When Alice sends 1 SUI to Bob, her existing Coin object is split into two separate objects:

- one remains with Alice containing the remaining balance, and
- a new Coin object is created containing the transfer amount. This new object is then transferred to Bob by changing its ownership field.

Since each Coin object has a unique ID and clear ownership, simple transfers don't require consensus from validators - they're processed immediately as the transaction only involves objects with single owners. This object-centric approach eliminates the need for global state updates, making peer-to-peer transfers more efficient than traditional blockchain architectures where every transaction must go through validator consensus.

### Access Control

#### **Ethereum**

EVM handles access control through function modifiers and runtime validation using the caller's address. When a function like mint() is called, the contract checks **msg.sender** (the transaction originator) against stored permission mappings like the **owner** address or the **admins** mapping. If the caller doesn't have the required permissions, the **require()** statement in the modifier fails and the entire transaction reverts, consuming gas but making no state changes. This pattern is enforced at the contract level through modifiers like **onlyOwner** or **onlyAdmin**, which act as gatekeepers that run before the actual function logic. In the example below, only the contract owner can call **addAdmin()** and **emergencyStop()**, while both the owner and designated admins can call **mint()**. The beauty of this system is its simplicity: Permissions areaddress comparisons stored in contract state using variables like **address public owner** and **mapping(address => bool) public admins**, making it easy to implement role-based access control, multi-signature requirements, or complex permission hierarchies.

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract TokenContract {
    address public owner;
    mapping(address => bool) public admins;
    uint256 private totalSupply;
    constructor() {
        owner = msg.sender;
    }
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }
    modifier onlyAdmin() {
        require(admins[msg.sender] || msg.sender == owner, "Not an admin");
        _;
    }
    function addAdmin(address admin) external onlyOwner {
        admins[admin] = true;
    }
    function mint(address to, uint256 amount) external onlyAdmin {
        // Only admins can mint tokens
        totalSupply += amount;
        // ... minting logic
    }
    function emergencyStop() external onlyOwner {
        // Only owner can stop the contract
        // ... emergency logic
    }
}
```
### Solana

Solana's access control follows similar principles to EVM but uses a different approach. Both systems verify authorization before allowing restricted actions. EVM compares **msg.sender** against stored addresses while Solana verifies transaction signatures against stored pubkeys using **require!(ctx.accounts.admin.key() == ctx.accounts.config.admin)**. The key difference is that Solana relies more heavily on cryptographic signatures for authorization, while EVM adds runtime permission checks on top of the signature verification. PDAs make Solana unique by allowing programs to have their own signing authority - the **authority** account derived from **\["authority"\]** seeds can sign transactions programmatically through **CpiContext::new\_with\_signer()**, eliminating the need for humans to hold protocol keys. Both approaches achieve the same goal of restricting access, just through different mechanisms.

```
use anchor_lang::prelude::*;
declare_id!("9UPnoepLi34JnCrq6qJPVo9fSxZeHsJbnJZyfovt6eoZ");
#[program]
pub mod simple_access_control {
    use super::*;
    pub fn initialize(ctx: Context<Initialize>, admin: Pubkey) -> Result<()> {
        let config = &mut ctx.accounts.config;
        config.admin = admin;
        config.value = 0;
        Ok(())
    }
    pub fn update_value(ctx: Context<UpdateValue>, new_value: u64) -> Result<()> {
        // Simple access control: only admin can update
        require!(
            ctx.accounts.signer.key() == ctx.accounts.config.admin,
            ErrorCode::Unauthorized
        );
        ctx.accounts.config.value = new_value;
        Ok(())
    }
    pub fn change_admin(ctx: Context<ChangeAdmin>, new_admin: Pubkey) -> Result<()> {
        // Only current admin can change admin
        require!(
            ctx.accounts.signer.key() == ctx.accounts.config.admin,
            ErrorCode::Unauthorized
        );
        ctx.accounts.config.admin = new_admin;
        Ok(())
    }
}
#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = payer, space = 8 + 32 + 8)]
    pub config: Account<'info, Config>,
    #[account(mut)]
    pub payer: Signer<'info>,
    pub system_program: Program<'info, System>,
}
#[derive(Accounts)]
pub struct UpdateValue<'info> {
    #[account(mut)]
    pub config: Account<'info, Config>,
    pub signer: Signer<'info>,
}
#[derive(Accounts)]
pub struct ChangeAdmin<'info> {
    #[account(mut)]
    pub config: Account<'info, Config>,
    pub signer: Signer<'info>,
}
#[account]
pub struct Config {
    pub admin: Pubkey,
    pub value: u64,
}
#[error_code]
pub enum ErrorCode {
    #[msg("Unauthorized: Only admin can perform this action")]
    Unauthorized,
}
```
### Move

Move handles access control through capability objects that must be explicitly owned, like an NFT in EVM, but enforced at the type system level. In Move, ownership isn't stored in a contract state but directly owned by your address. The **AdminCap** in our example is a real object in your wallet, and to call **update\_balance()**, you have to pass it as a parameter: **public fun update\_balance(\_: &AdminCap, treasury: &mut Treasury, new\_balance: u64)**. No capability object? You can't call the function - the compiler stops you. Unlike other systems where you might pass fake account addresses, Move's object system ensures you can only pass capabilities you actually own - there's no way to forge or fake a capability reference. When the module initializes with **init()**, it creates an **AdminCap** and transfers it directly to the publisher using **transfer::transfer(admin\_cap, tx\_context::sender(ctx))**. If you want to give someone admin rights later, you simply transfer your **AdminCap** object to them. No complex permission mappings needed - if you own the capability, you're authorized.

```
module treasury::admin {
    use sui::object::{Self, UID};
    use sui::transfer;
    use sui::tx_context::{Self, TxContext};
    // Capability object that proves admin rights
    public struct AdminCap has key, store {
        id: UID,
    }
    // Treasury that holds funds
    public struct Treasury has key {
        id: UID,
        balance: u64,
    }
    // Only called once during module initialization
    fun init(ctx: &mut TxContext) {
        let admin_cap = AdminCap {
            id: object::new(ctx),
        };
        let treasury = Treasury {
            id: object::new(ctx),
            balance: 1000,
        };
        // Transfer AdminCap to module publisher
        transfer::transfer(admin_cap, tx_context::sender(ctx));
        transfer::share_object(treasury);
    }
    // Only callable if you own an AdminCap
    public fun update_balance(
        _: &AdminCap,               // Proof of authorization
        treasury: &mut Treasury,    // Treasury to update
        new_balance: u64
    ) {
        treasury.balance = new_balance;
    }
}
```
## Conclusion

We've covered the fundamental differences in how EVM, Solana, and Sui Move handle basic operations like token transfers and access control. EVM uses storage slots and runtime checks, Solana separates code from data with signature validation, and Sui treats everything as ownable objects with compile-time safety.

Understanding these mental models is crucial because they shape how you approach every aspect of development(from data organization to permission management). The same business logic gets implemented very differently depending on the underlying architecture.

In **Part 2**, we'll dive into Move-specific patterns that developers coming from other ecosystems need to master. We'll cover the witness pattern for type safety, testing strategies, time handling, working with collections, dynamic object fields, and other Move idioms that make the language powerful for building secure smart contracts.

Stay tuned for more deep dives, real-world bugs, and smart contract best practices.

#### Follow @AdevarLabs on [X](https://web.archive.org/web/20250729184748/https://twitter.com/AdevarLabs) / [LinkedIn](https://web.archive.org/web/20250729184748/https://linkedin.com/company/adevarlabs) - Ship Safely.
