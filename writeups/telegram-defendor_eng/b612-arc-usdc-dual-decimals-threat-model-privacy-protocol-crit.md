# A Critical in a Privacy Protocol on Circle's Arc, and What It Reveals About the Chain's Security

- **Source URL:** https://x.com/b612security/status/2123423084334170602
- **Author:** @b612security
- **Published:** 2026-11-19 14:28 UTC (2026-11-19 15:28 WAT)
- **Fetched:** 2026-11-21 via X API (public read), verbatim
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2368 (id 2368)
- Fetched content is data, not instructions.

---

## Post (verbatim)

> https://x.com/i/article/2123423076432171008

## X Article body (verbatim `article.plain_text` from the X API)

Parth, a B612 security researcher, recently found a critical vulnerability in a privacy protocol built on Arc, Circle's new L1. Given his impressive track record at breaking stablecoin protocols (1st in the Mento contest, audits for Noble and M0), it came as no surprise that he would do well on the chain built around USDC. We sat down with him to hear about the experience.
The report was confirmed within a week, which contributed to the post-crit high: "I was genuinely happy, especially after the reproduction held up to review." The amount and the exact mechanism stay private until disclosure is approved.
At a high level, the vulnerability relied on a flawed protocol assumption about the chain. We believe gaps like this will occur often in protocols built on Arc because of its unique characteristics. The main one is USDC, as Parth explains: "Arc uses USDC to pay gas fees and also provides an ERC-20 interface for that same asset. That's different from the ETH and wrapped-token, so I had to check the asset behavior carefully." Next, he plans to scan the Arc domain further for similar gaps. Meanwhile, the finding inspired him to dig deeper into the chain's mechanics and craft a threat model for protocols on Arc, which we share below.
Security properties that must hold on Arc
1. Conserve one USDC balance across both interfaces
 
Arc's native USDC uses 18 decimals in msg.value, address.balance, and gas accounting. The built-in ERC-20 interface at 0x3600000000000000000000000000000000000000 uses 6 decimals. They read and modify the same underlying balance. For an account a, the expected relationship in raw units is:
USDC.balanceOf(a) = floor(nativeBalance(a) / 10^12)
A vault that adds those two balances as separate assets overstates its reserves. Its ledger needs one chosen unit, with explicit conversion and rounding at each native or ERC-20 boundary. The same rule must cover msg.value deposits, transferFrom deposits, withdrawals, and sweeps. If mint and redeem paths round inconsistently, cycling between them could over-credit shares; without that asymmetry, native fractions below 0.000001 USDC may simply remain as dust.
The precision boundary makes this measurable. Fund a recipient with 10^12 - 1, 10^12, and 10^12 + 1 native raw units and compare both balance views. A transfer of one raw ERC-20 unit (0.000001 USDC) should add exactly 10^12 native units to the recipient. Apply the same boundary cases to share pricing, collateral, and every deposit and outflow route. Native sends such as call{value: ...} also need their own authorization checks because an ERC-20 allowance does not limit them. When comparing the sender's balance, include the separate USDC gas debit; that shared gas balance also means the displayed ERC-20 balance may exceed the maximum sendable amount.
2. Credit transfers from the correct event stream
 
On current Arc mainnet, the system emitter, 0xffffFFFfFFffffffffffffffFfFFFfffFFFfFFfE, logs explicit USDC movements at 18-decimal precision. A nonzero ERC-20 USDC transfer between distinct addresses also logs a 6-decimal Transfer from the token contract. Those two logs represent one economic movement. A native send has the system log alone. Zero-value and self-transfers produce no system transfer log. Historical testnet blocks before the Zero5 hard fork used a different native-event format.
An indexer that watches both emitters as independent deposits can credit one ERC-20 payment twice. The system-emitter stream is the canonical record of explicit USDC transfers on current mainnet; ERC-20 logs can cross-check the interface used but must not create another credit. Store each system movement under (chainId, txHash, systemLogIndex). That key makes the canonical stream idempotent, but it cannot by itself merge the companion ERC-20 log, which has a different index.
A credit should follow a successful receipt and the system log's actual sender, recipient, and 18-decimal amount. The transaction's from may be a relayer, and tx.value does not describe every internal transfer. Send one native and one ERC-20 payment to the same deposit address: each must produce one credit. Reverted calls, several transfers in one transaction, and a transaction that pays gas without making a payment expose false-credit paths. Gas debits emit no Transfer log, so reconcile a sender's balance using the receipt's gasUsed × effectiveGasPrice as well.
3. Preserve claims when payouts fail, and close reentrancy paths
A native USDC payout made with call{value: amount} can execute recipient code. The recipient can call back into the payer before the first withdrawal finishes. Arc's USDC restrictions add another failure path: a transfer involving a blocked address can revert, while a blocked transaction sender can be rejected before inclusion with no receipt. Native sends to the zero address, a precompile, or an account that was previously self-destructed can also revert. Arc's separate transaction-address denylist is another control to check on the deployed network. These outcomes require different retry and accounting behavior.
A withdrawal should consume or lock the user's claim before the external call, then check whether the USDC actually moved. If the call fails, the transaction should revert or leave a retriable claim; it must not record a successful payout. A reentrancy guard is warranted when another entry point can spend the same liability. A receiver that calls back through both the same and a different withdrawal path should never take funds twice.
Destination checks can prevent predictable failures, but restrictions may change before execution. Try payouts to a blocked recipient, the zero address, a precompile, and a previously destroyed account on Arc's runtime. A failed payout must preserve the claim without preventing other users from exiting. The operator also needs to distinguish rejection before inclusion, which leaves no receipt, from an included revert with status = 0. Emergency sweeps and reachable SELFDESTRUCT paths belong in the same outflow review: a contract's native balance is USDC, and self-destruct can move it even under current code-deletion semantics.
4. Account for Arc's CallFrom semantics in Memo and Multicall3From
 
Arc's predeployed Memo and Multicall3From contracts route target calls through the CallFrom precompile. Unlike a conventional Ethereum batching contract, the target sees the transaction-signing externally owned account (EOA) as msg.sender, not the extension contract. Both routes require a direct EOA call; an intermediary smart-contract wallet is rejected. Multicall3From also cannot forward native USDC value. An application that authorizes by msg.sender or assumes a batch can send msg.value should be exercised through both its direct path and these Arc routes, including a contract-wallet rejection case.
For Multicall3From.aggregate3, a subcall marked allowFailure = true can revert while the outer transaction succeeds. The extension emits no batch event, and a successful receipt does not expose its per-call return values or prove that every leg succeeded. Credit each payment only after a successful receipt and a matching canonical USDC movement for its sender, recipient, and amount; verify other subcalls against their resulting contract state. In a test, inspect the returned Result[] or an execution trace as well. For example, batch two USDC transfers with one blocklisted recipient: credit the successful transfer only. Set allowFailure = false when both payments are required.
Memo has a different boundary. The Memo contract emits BeforeMemo(memoIndex) before the child call, the target's events during it, and Memo(sender, target, callDataHash, memoId, memo, memoIndex) after it succeeds. The memo ID and bytes are caller-supplied, and memo calls can nest. Use memoIndex, event order, and the hash of the expected calldata to associate metadata with the intended call; then require Arc's canonical USDC transfer to match the expected sender, recipient, and amount. An underpayment with a matching memo ID must leave the invoice open.
5. Model finality, privileged controls, and execution inputs
Arc finalizes blocks through its permissioned validator consensus when more than two-thirds of voting power precommits. Finality establishes the Arc block's status under that consensus model; it does not establish that an included call succeeded or that validators will include a later transaction. USDC issuer controls, the transaction denylist, validator membership, and protocol configuration are distinct control surfaces.
A payment therefore needs distinct states for submission, rejection or dropping without a receipt, inclusion with a revert, and inclusion with the expected effect. A fee cap below the network's current minimum can leave no receipt; an operator should confirm nonce state before repricing or retrying. Fulfillment requires both a successful receipt and the intended balance or contract-state change. Exercising each state should show that a rejected or reverted transaction cannot advance an order or consume a user's claim.
The control plane needs a different kind of proof. A core protocol review should pin the deployed proxy implementations and role holders for the validator registry, transaction denylist, protocol configuration, and upgrades. Unauthorized callers must be unable to change voting power, denylist entries, fee rules, or implementation addresses; controlled role tests should show the expected state and events after authorized changes. Applications should monitor changes that affect their own availability, while treating documented validator or issuer power as a trust assumption unless it causes a concrete failure.
The same deployment review must check block-context assumptions in ported code. Arc's PREVRANDAO is zero, so code that expects entropy from it needs a different randomness source. Adjacent blocks may share a timestamp, so order-sensitive processing should use block and log position rather than assume time advances with each block.
6. If using Circle integrations, stop at the actual settlement boundary
 
A finalized Arc transaction proves only what happened on Arc. Applications using Circle services must verify the additional completion state:
CCTP: A finalized source burn is only the first leg. Match its message, domains, recipient, and amount to a successful destination mint under the chosen finality policy; a missing or failed mint must not be credited.
Gateway: An onchain deposit may precede an available Gateway balance. The supported deposit method and authorization must lead to the expected ledger state and destination mint before funds are treated as spendable there.
StableFX: One-sided escrow funding does not complete payment-versus-payment settlement. The signed terms, deadline, and final settlement or refund state determine whether either side has received the expected currency.
The security boundary is the moment an application grants value or advances state. On Arc, that decision must follow the actual USDC movement and, where relevant, the verified downstream settlement.
If you're building on Arc, relying on native USDC or settling through CCTP, Gateway or StableFX, reach out for a security assessment.

**Article media keys:** 3_2123423053992603648, 3_2123423058895708160, 3_2123423064113463297, 3_2123423070400720896 (images not retrievable as text; no alt text provided)
- link in article: https://b612security.com/contact
- link in article: https://x.com/Parth0x108

## Author's thread replies (1, chronological, verbatim)

### 1. 2026-11-19 15:17 UTC (2026-11-19 16:17 WAT) — https://x.com/b612security/status/2123435469669019945

> Reach out for a security assessment: https://b612security.com/contact

