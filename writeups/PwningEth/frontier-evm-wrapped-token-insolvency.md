# frontier-evm-wrapped-token-insolvency

- **Source URL:** https://pwning.mirror.xyz/RFNTSouIIlHVNmTNDThUVb1obIeN5c1LAiQuN9Ve-ok
- **Fetched:** 2026-11-11
- **Researcher:** PwningEth
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

People are joking around the seeming depegging of WETH. The wrapped ETH token contract, the most simple and fundamental contract in the Ethereum ecosystem, is used in almost every DeFi protocol. If the depegging happens, the empire of Ethereum will collapse. Trust me, the depegging of WETH is the last thing you should worry about in Ethereum. Because when that happens, both your ETH and WETH would be worthless.

Will we see the doomsday of Ethereum? What if a catastrophic vulnerability is discovered and exploited in the Ethereum network? Considering the security model of Ethereum, I don’t think that could happen. The execution of smart contracts and the consensus of the network are implemented in multiple independent software clients, a single flaw or discrepancy that affects a minority of the clients will be discarded by the network. Even if we see a nuclear-level bug that destroys all the Ethereum nodes, the community can always fork a new secured chain as the canonical Ethereum, like we have done in [the DAO fork](https://ethereum.org/en/governance/#dao-fork).

However, not all EVM compatible chains are guarded at the same security level and with the same decentralization as Ethereum. In fact, most “Ethereum killer” chains only have one single implementation of their protocol. The lack of diversity is the Achilles’ heel of public chains: if anything goes wrong in their official implementation, the giant will be knocked down easily.

A few months ago, I found a critical vulnerability in [paritytech/frontier](https://github.com/paritytech/frontier), an EVM implementation written in rust and mainly used in Polkadot parachains. When I was writing my [previous blog post](https://pwning.mirror.xyz/okyEG4lahAuR81IMabYL5aUdvAsZ8cRCbYBXh8RHFuE), I decided to take one more quick review of the code used in the Moonbeam network, in case I missed anything trivial but critical. My hacker instinct led me to a tricky integer truncation bug!

Frontier executes normal Ethereum smart contracts, but uses a Polkadot substrate as the ledger. This has a quirk: while balance amounts are 256 bit integers in normal Ethereum, the currency in the Polkadot substrate is only 128 bit. To convert to Polkadot, frontier truncates the 256 bit transfer balance amount to 128 bits. This is the code that handles value transferring in the frontier EVM:

Since the balance can never be greater than 128 bit, and the transfer will be validated by the balance substrate eventually, what could go wrong?

The key is that the `transfer.value` here, or `msg.value` in EVM, is a totally controlled 256 bit value provided by the user. If we pass (1 \<\< 128) in the `msg.value`, `T::Currency::transfer` will do nothing because it’s transferring a truncated zero, and we’ll finish the EVM execution smoothly. We won’t get any extra balance by transferring the zero, but what if the giant untruncated `msg.value` is accepted by some contract that does give us credit? We could achieve the impossible and attack WETH to make it depeg!

The WETH contract allows users to deposit native ETH that users specify through `msg.value`. It stores this value internally after transferring the appropriate amount of tokens. Normally if you don’t have enough balance for the transfer, the transaction will be rejected or reverted. However, since we have bypassed the transfer validation by truncating to 0, the contract is willing to add our gigantic credit to our address in its internal balance mappings. Suddenly we have an astronomical balance in the contract and can drain all the deposited native tokens from the wrapped token contract!

To clarify, it’s not the WETH token itself on Ethereum that is vulnerable (but the title made you click, didn't it!), but the analogous wrapped native tokens of the polkadot parachains powered by the frontier EVM, such as WASTR in Astar, WGLMR in Moonbeam, and WMOVR in Moonriver, which are implemented using the standard WETH contract but on their respective parachains!

WETH contracts are not the only vulnerable targets. The Uniswap-like DEX trading pair contract accepts direct swapping from native ETH to ERC20 tokens. It trusts the `msg.value` too. Compound-like lending protocols usually provide a dedicated native token vault, handling both the deposit and withdrawal of native tokens. DEXes and lending protocols are the fundamental infrastructure of the DeFi world, any insolvency would be contagious. As I mentioned, any critical vulnerability that could depeg WETH is actually the nightmare of the whole ecosystem.

The [previous bug](https://pwning.mirror.xyz/okyEG4lahAuR81IMabYL5aUdvAsZ8cRCbYBXh8RHFuE) had a similar effect, but required a tricky exploit. This bug is trivial but more destructive.

The impact of the bug is complex. The direct exploit could drain all the wrapped token contracts. In addition to taking over the balance of the wrapped token, you can purchase other tokens from DEX by spending the rubber check from the wrapped token. Worse, a more sophisticated exploit could leverage the lending protocol to borrow all the other valuable tokens against the fake deposit.

At the time I reported the bug, the major victims were:

- **WMOVR**[https://moonriver.moonscan.io/address/0x98878b06940ae243284ca214f92bb71a2b032b8a](https://moonriver.moonscan.io/address/0x98878b06940ae243284ca214f92bb71a2b032b8a) 560,369.286709772080185324 MOVR $6,511,491.11 (@ $11.62/MOVR)
- **WMOVR**[https://moonriver.moonscan.io/address/0xf50225a84382c74cbdea10b0c176f71fc3de0c4d](https://moonriver.moonscan.io/address/0xf50225a84382c74cbdea10b0c176f71fc3de0c4d) 39,495.093378689025337841 MOVR $458,932.99 (@ $11.62/MOVR)
- **MGLMR**[https://moonbeam.moonscan.io/address/0xacc15dc74880c9944775448304b263d191c6077f](https://moonbeam.moonscan.io/address/0xacc15dc74880c9944775448304b263d191c6077f) 22,509,169.750566904824477505 GLMR $15,462,674.16 (@ $0.69/GLMR)
- **Wrapped Astar**[https://blockscout.com/astar/address/0xAeaaf0e2c81Af264101B9129C00F4440cCF0F720](https://blockscout.com/astar/address/0xAeaaf0e2c81Af264101B9129C00F4440cCF0F720) 233,903,992.470478147048553875 ASTR ($12,110,613 USD)
- **WASTR**[https://blockscout.com/astar/address/0x19574c3c8FaFc875051b665Ec131b7E60773d2C9](https://blockscout.com/astar/address/0x19574c3c8FaFc875051b665Ec131b7E60773d2C9) 98,294,128.445114886025015582 ASTR ($5,080,234 USD)
- **Wrapped Shiden**[https://blockscout.com/shiden/address/0x0f933Dc137D21cA519ae4C7E93f87a4C8EF365Ef](https://blockscout.com/shiden/address/0x0f933Dc137D21cA519ae4C7E93f87a4C8EF365Ef) 9,348,196.210407926441765242 SDN ($3,310,196)

The direct loss from wrapped token contracts could be more than **$44M**.

In lending pools the assets under risk is even larger:

- ***Moonwell Apollo*** Total Supply $89,023,722 Total Borrow $41,595,374.52
- ***Moonwell Artemis*** Total Supply $179,023,716.01 Total Borrow $94,486,490.85
- ***Starlay Finance*** Total Deposited $37,163,238.35 Total Borrowed $18,769,822.51

The remaining borrowable assets would be somewhere around **$150M**.

The vulnerability disclosure was troublesome as well. This bug affected at least two parachains: Moonbeam network and Astar network. I had to report to them simultaneously otherwise one team with earlier knowledge of the bug could conceivably launch an attack on the other one (I didn’t know if they were competitors). Furthermore, I noticed Acala network also shipped the same code, but they didn’t have as rich an EVM-based ecosystem as the other two, and the bug had no explicit impact on their system as a result, so I decided to postpone the bug disclosure to them.

All the three projects have their bug bounty program listed on Immunefi: [Moonbeam network](https://web.archive.org/web/20220521163014/https://immunefi.com/bounty/moonbeamnetwork/), [Astar network](https://web.archive.org/web/20220625225821/https://immunefi.com/bounty/astarnetwork/) and [Acala](https://web.archive.org/web/20220625224811/https://immunefi.com/bounty/acala/). Each project has a maximum bug bounty of **$1M** 😮. I was worried that the triage process on Immunefi might be delayed, so I tried to contact the first two teams as soon as I finished my [POC and reports](https://app.ardrive.io/#/drives/b7ecc2e5-bbe6-4ac3-91a2-c4d5a6bb2fff?name=FRONTIER). Thanks to the help from the [Moonwell](https://moonwell.fi/) team, they set up a telegram channel between me and Moonbeam, who later invited the Astar and Polkadot guys to the group. All the bugs were quickly [patched](https://github.com/paritytech/frontier/pull/753). A [security advisory](https://github.com/paritytech/frontier/security/advisories/GHSA-hc8w-mx86-9fcj) (CVE-2022-31111) was published later. This has been recorded on Moonbeam’s [blog](https://moonbeam.network/blog/security-patch-for-integer-truncation-bug/).

Another interesting fact about the bug: a few hours after my report, the Moonbeam team identified a suspicious [transaction](https://moonriver.moonscan.io/tx/0xbb8913dfb35b70caa42da03fb874dc42768700c15b858d9fb30a2d672a497262) that triggered the vulnerability. You can see the transfer of 340,282,366 (T) MOVR! I believe the bug is dead now, but the corpse is living on the blockchain permanently.

The vulnerable substrate `frontier` is built by [paritytech](https://www.parity.io/), the team behind [Polkadot](https://polkadot.network/). The Moonbeam team maintains its own fork at [https://github.com/PureStake/frontier](https://github.com/PureStake/frontier). The Astar team forks from Moonbeam’s repo to [https://github.com/AstarNetwork/frontier](https://github.com/AstarNetwork/frontier). All of them agreed to offer a bug bounty, but they decided to split a $1M bounty after months of negotiation🤣. To my surprise, Acala offered a huge bounty (compared to their negligible potential loss), which was also counted in the split. The final payout is $1M:

- ***Moonbeam*** $430k
- ***Astar*** $250k
- ***Polkadot*** $250k, in DOT
- ***Acala*** $70k, in DOT

Whether the result is $2M or $1M, since the bounty pays out in tokens living on the Ethereum blockchain, I guess I'm pretty lucky that WETH wasn't vulnerable to this bug after all!
