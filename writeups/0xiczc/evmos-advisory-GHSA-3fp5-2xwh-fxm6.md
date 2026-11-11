# evmos-advisory-GHSA-3fp5-2xwh-fxm6

- **Source URL:** https://github.com/evmos/evmos/security/advisories/GHSA-3fp5-2xwh-fxm6
- **Fetched:** 2026-11-11
- **Researcher:** 0xiczc
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

### Context

- [`stateObject`](https://github.com/evmos/evmos/blob/b196a522ba4951890b40992e9f97aa610f8b5f9c/x/evm/statedb/state_object.go#L53-L68): represents the state of an account and is used to store its updates during a state transition. This is accomplished using two in memory Storage variables: `originStorage` and `dirtyStorage`
- [`StateDB`](https://github.com/evmos/evmos/blob/b196a522ba4951890b40992e9f97aa610f8b5f9c/x/evm/statedb/statedb.go#L33-L55): it is the general interface to retrieve accounts and holds a map of stateObjects.

### Impact

An external contributor, [@iczc](https://github.com/iczc), discovered a way to mint arbitrary tokens due to the possibility to have two different states not in sync during the execution of a transaction. The exploit is based on the fact that to sync the Cosmos SDK state and the EVM one, we rely on the `stateDB.Commit()` method. When we call this method, we iterate though all the `dirtyStorage` and, **if and only if** it is different than the `originStorage`, we [set the new state](https://github.com/evmos/evmos/blob/b196a522ba4951890b40992e9f97aa610f8b5f9c/x/evm/statedb/statedb.go#L460-L465). Setting the new state means we update the Cosmos SDK KVStore.

Below, are described the steps to perform the attack:

- User send a tx to a smart contract (SC) that is calling a precompile.
- The SC perform a state transition of its state from A to B.
- The SC call the precompile.
- The SC perform a state transition of its state from B to A (revert of the previous).
- Once the transaction is executed, and the final **Commit** is performed, the state A will not be committed to the store because A is the same as `originStorage`.

If the tx is executed correctly, this is what happens at the store level:

- Initial state A is loaded from the KVStore and the dirtyStorage is set to B.
- Before running the precompile, the `dirtyStorage` is committed to the KVStore without changing the `originStorage`.
- Now, since we have a `dirtyStorage`, it is updated to the previous value A without changing the `originStorage`.

Since the tx executed correctly, the evm calls the commit to persist the dirtyStorage. However, since dirtyStorage is equal to originStorage, nothing will be changed.

To summarize, if a contract storage state that is the same before and after a transaction, but is changed during the transaction and can call an external contract after the change, it can be exploited to make the transaction similar to non-atomic. The vulnerability is **critical** since this could lead to drain of funds through creative SC interactions.

### Severity

Based on [ImmuneFi Severity Classification System](https://immunefisupport.zendesk.com/hc/en-us/articles/13332717597585-Severity-Classification-System) the severity was evaluated to `Critical` since the attack could have lead to direct loss of funds.

### Patches

The issue has been patched in versions >=V17.0.0.

## For more information

If you have any questions or comments about this advisory:

Reach out to the Core Team in [Discord](https://discord.gg/evmos)

Open a discussion in [evmos/evmos](https://github.com/evmos/evmos/discussions)

Email us at [security@evmos.org](mailto:security@evmos.org) for security questions

## Context

`stateObject`: represents the state of an account and is used to store its updates during a state transition. This is accomplished using two in memory Storage variables:`originStorage`and`dirtyStorage``StateDB`: it is the general interface to retrieve accounts and holds a map of stateObjects.
## Impact

An external contributor, @iczc, discovered a way to mint arbitrary tokens due to the possibility to have two different states not in sync during the execution of a transaction. The exploit is based on the fact that to sync the Cosmos SDK state and the EVM one, we rely on the

`stateDB.Commit()`method. When we call this method, we iterate though all the`dirtyStorage`and,if and only ifit is different than the`originStorage`, we set the new state. Setting the new state means we update the Cosmos SDK KVStore.
Below, are described the steps to perform the attack:

Commitis performed, the state A will not be committed to the store because A is the same as`originStorage`.
If the tx is executed correctly, this is what happens at the store level:

`dirtyStorage`is committed to the KVStore without changing the`originStorage`.`dirtyStorage`, it is updated to the previous value A without changing the`originStorage`.
Since the tx executed correctly, the evm calls the commit to persist the dirtyStorage. However, since dirtyStorage is equal to originStorage, nothing will be changed.

To summarize, if a contract storage state that is the same before and after a transaction, but is changed during the transaction and can call an external contract after the change, it can be exploited to make the transaction similar to non-atomic. The vulnerability is

criticalsince this could lead to drain of funds through creative SC interactions.
## Severity

Based on ImmuneFi Severity Classification System the severity was evaluated to

`Critical`since the attack could have lead to direct loss of funds.
## Patches

The issue has been patched in versions >=V17.0.0.

## For more information

If you have any questions or comments about this advisory:

Reach out to the Core Team in Discord

Open a discussion in evmos/evmos

Email us at security@evmos.org for security questions
