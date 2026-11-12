# 🌉 Fake Events Could Have Drained Across Bridge Relayers

- **Source URL:** https://blog.asymmetric.re/across-solana-event-spoofing
- **Fetched from:** https://asymmetric.com/blog/across-solana-event-spoofing/
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1513 (id 1513)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
[← All posts](https://asymmetric.com/blog/)

# Across Solana Event Spoofing

By Maxwell Dulin

In the EVM world, events are first-class citizens emitted via dedicated opcodes and stored in searchable receipts. In Solana, there is no canonical way to handle events. Solana "events" are often reconstructed from instruction data or program logs via results returned by the getTransaction RPC method. This architectural shift introduces a subtle but consequential friction point: the burden of disambiguation shifts from the protocol to the off-chain observer.

In this post, we’re going to discuss strategies for Solana event handling, an easy-to-make oversight that can lead to a loss of funds, and how this vulnerability impacted the Across protocol. Fortunately, the Across team responded quickly, immediately remediating the issue, and no funds were lost.

## Across Architecture

Across is an *intent-based* bridge that facilitates native-to-native asset transfers without relying on wrapped tokens. Instead of bridging an asset directly across chains, the protocol receives a native asset from the user on the source chain and fulfills the intent by releasing another native asset to the recipient on the destination chain. For instance, a user can deposit USDC on Ethereum, and Across will deliver native USDC to them on Base. It also supports cross-chain swaps, meaning a user can deposit ETH on Ethereum and have native USDC released to them on Base.

Across relies on the [relayer](https://docs.across.to/reference/actors-in-the-system#relayer) to *fill* these orders cross-chain. This shifts the capital burden onto the relayer, not the protocol itself. Since the fees are fixed, the relayers compete on *speed* to win, which normally results in faster-than-finalization fills. Effectively, the relayers are taking on the risk of source-chain rollbacks in exchange for fee revenue.

After the order is filled, Across will pay the relayer. Refunds are done in batches via the HubPool contract on Ethereum, with some of the funds originating from user orders. If an order has not already been filled by the relayers, a user can request a *slow fill* (i.e. waiting for source chain finality) that will be filled from the HubPool.

This post provides a high-level overview of the context needed to understand the rest of the post. If you want to learn more, read through their [documentation](https://docs.across.to/).

## Solana Event Indexer

Unlike most chains, Solana doesn’t have a simple *events* API. So, Solana events are typically done in one of three ways:

1. Instruction Data
2. Program Logs
3. Accounts

This post will focus on the first approach: **Instruction Data**. In Solana, the entire transaction trace is logged and returned. For each contract that is executed, the program ID (equivalent to program address), instruction data, accounts, and result are all visible in the trace. Below is an [example](https://solscan.io/tx/3GdfP2z66tdL7emrV5yEivza8i7md32TMp1XJtuhxCeK1hDDJE6bnK5vEvouxHCKEjzETghbX9wtRDEgaKJcRgun) of a trace for an Across Solana Event:

When extracting trusted event information, off-chain infrastructure often looks for self-CPIs (Cross-Program Invocations in which a program calls back into itself). The first step in verifying these events is checking the target program address. Then, to ensure the event emission is actually legitimate, the execution requires a Program Derived Address (PDA) signer. Because the Solana runtime natively enforces PDA signing rules, this guarantees that only the program itself could have authorized the CPI. Now, the event data can be deserialized and used.

To learn more about self-CPI events, read the [Anchor documentation](https://www.anchor-lang.com/docs/features/events#emit_cpi) on the subject.

## Vulnerability

A standard Solana transaction consists of top-level instructions that frequently execute further logic via Cross-Program Invocations (CPIs). This cascading sequence of calls is recorded on-chain as a nested execution trace, which the Across event handler parses by iterating directly through meta.InnerInstructions (1). Within each inner instruction, the program searches for the Across program address (2) and the PDA signer event authority (3) to be present. Once they are found, the event is deemed legitimate, and the data is deserialized (4).

```
for (const ixBlock of txResult.meta?.innerInstructions ?? []) { // 1
  for (const ix of ixBlock.instructions) {
    const ixProgramId = messageAccountKeys[ix.programIdIndex];
    const singleIxAccount = ix.accounts.length === 1 ? messageAccountKeys[ix.accounts[0]] : undefined;
    if (
      ixProgramId !== undefined &&
      singleIxAccount !== undefined &&
      this.programAddress === ixProgramId && // 2
      this.programEventAuthority === singleIxAccount // 3
    ) {
      const ixData = bs58.decode(ix.data);
      const eventData = Buffer.from(ixData.slice(8)).toString("base64");
      const { name, data } = decodeEvent(this.idl, eventData); // 4
      events.push({ program: this.programAddress, name, data });
    }
  }
}
return events;
```
However, the code above has a subtle flaw: **failed events have instruction data**. The transaction status must be verified. The code above for parsing the event never checked whether the transaction had failed. The missing check was added in Across SDK commit `a9ca75b`.

For exploitation, the idea is to trigger an event and then force the transaction to fail after the protocol is used. The off-chain infrastructure will process the event, even though no token transfer ever occurred due to the state revert. The attacker would keep the funds while the protocol continued to operate as normal.

This appears to be a common issue in Solana's off-chain infrastructure. This mirrors a related finding by AR researcher [0xAlphaRush](https://x.com/0xalpharush) in a [Sherlock contest for Zetachain](https://audits.sherlock.xyz/contests/857).

## Exploitation of Event Rollback

Profiting from this bug is specific to Across’s architecture. There are three potential paths for exploitation:

1. Relayer fills the order from Solana.
2. HubPool slow fill transfer from Solana.
3. Relayer falsifies a refund on HubPool.

We will explore the first of these in more detail below, though all three represent viable attack vectors.

### Relayer Incorrect Fill

The relayers listen for FundsDeposited events on Solana. Upon seeing this event, relayers will perform various checks on their capital and current risk profile for source-chain reorgs. After these checks, the relayer will send the funds to the recipient on the specified destination chain.

By creating a fake event, an attacker can trick the relayer into performing a fill and keeping the capital. This attack works as follows:

1. The attacker takes a flash loan for the largest amount a solver will fill, given the solver's risk profile. Solvers won’t fill arbitrarily large transfers.
2. The attacker performs a deposit transaction as usual. This will emit a FundsDeposited event.
3. Force the transaction to revert on the next instruction. The token transfer initiated by the deposit call has now been reverted.
4. The relayer will view the transaction event and queue the transfer.
5. The relayer will fill the transfer on the destination chain. The attacker now has funds on both sides of the transaction: the original collateral and the filled transfer.
6. The relayer would get their refund from the pool, or the refund bundle would be rejected. Regardless, the attacker receives the fill without having deposited any funds.

## Conclusion

Solana integrations require careful attention to subtle architectural differences that have no direct EVM equivalent. Whether it's a missing status check or improper indexing of account addresses, the responsibility for correctness falls entirely on the integrator, and the margin for error is narrow.

While the vulnerability provided a clear mechanism for spoofing events, executing a profitable, large-scale exploit introduces significant practical constraints. Relayers implement strict internal checks and generally will not fill an order larger than the HubPool can currently refund. During our observation of outgoing fills on Solana, we identified only a single active relayer, though others likely operate in stealth. Because relayers often run heavily modified implementations, an attacker cannot reliably predict how their spoofed events will be processed.

Across had further reduced their exposure by keeping Solana in a trial stage, allowing only USDC-to-USDC transfers. The vulnerability was fixed within several hours, demonstrating their dedication to security. Across was generous with their bounty reward, and we appreciated working with them throughout this process.

Asymmetric Research dedicates significant time to securing the Solana ecosystem, as shown by this post and others. If you’re a strong security engineer or researcher looking to work on some of the hardest security challenges in web3, [we’d love to hear from you](https://asymmetric.com/careers/).
