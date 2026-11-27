# 🚨 Three Cross-Chain Hacks in Two Days: Chainflip, Cyber and Fusionist

- **Source URL:** https://changenow.io/blog/cross-chain-crypto-hacks
- **Fetched:** 2026-11-27
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2391 (id 2391)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Three cross-chain crypto projects were hacked on November 21–22, 2026. **Chainflip lost approximately $12 million, Cyber's bridge released $1.1 million worth of tokens, and a Fusionist exploit led to $5.7 million in reported asset extraction and reserve withdrawals.**

- Chainflip's vaults accepted unauthorized withdrawals.
- Cyber's bridge processed messages that its source blockchain had never sent.
- Fusionist's bridge continued releasing genuine tokens after an attacker created unbacked ACE tokens.

Here is what happened in each attack and what investigators have established so far.

## Chainflip, Cyber and Fusionist Hacks: Key Figures

| Project | Date | Reported losses or impact | How the attack worked | 
|---|---|---|---|
| **Chainflip** | November 21 | \~$12 million stolen | Unauthorized withdrawals approved with a valid aggregate signature | 
| **Cyber** | November 21 | \~$1.1 million in CYBER released | Forged cross-chain messages signed by an authorized verifier | 
| **Fusionist** | November 22 | \~$2 million taken by the attacker; \~$3.7 million in subsequent bridge withdrawals | Unauthorized ACE minting followed by redemption of unbacked tokens | 

\*Fusionist's $5.7 million includes withdrawals made by traders after the original exploit, not just funds taken by the attacker.

## Chainflip Hack: $12 Million Stolen From Crypto Vaults

On November 21, 2026, cross-chain decentralized exchange **Chainflip** lost approximately $12 million in an attack on its Bitcoin and Ethereum vaults.

Chainflip Labs [confirmed the stolen amounts](https://chainflip.io/return):

- 122.861 BTC
- 520.224 ETH
- 3.249 million USDC
- 758,141 USDT

### How Was Chainflip Hacked?

The attacker withdrew funds from Chainflip's Ethereum vault using a valid signature. The transaction passed the vault's authorization checks, even though it had not followed the normal withdrawal process.

Chainflip uses a distributed validator system to approve vault transactions. On Ethereum, at least 100 of its 150 validators must participate in generating a valid aggregate signature.

In its [investigation](https://bitquery.io/investigations/chainflip-hack), Bitquery found that the attacker emptied the Ethereum vault at **07:10:59 UTC on November 21**.

Researchers examined 299,677 signatures accepted by the vault since 2023. Only the attacker's transaction contained a nonce that did not follow the expected sequence.

A nonce is a number used to identify a transaction and prevent certain forms of replay or duplication. In this case, the unusual value suggested that the withdrawal had been authorized outside Chainflip's normal process.

[SlowMist](https://hacked.slowmist.io/) also flagged the incident as a suspected private-key compromise. Its initial loss estimate of $4.86 million covered the Ethereum vault.

**The exact method of key exposure has not been made public.** Chainflip Labs said it had identified the cause and taken steps to prevent another attack.

### Where Did the Stolen Chainflip Funds Go?

The attacker moved the Ethereum assets almost immediately.

Bitquery found that the stolen USDC and USDT were swapped for ETH through Uniswap. Within roughly eight minutes, **2,909 ETH had been sent to Tornado Cash** in 38 transactions.

Source: [Bitquery](https://bitquery.io/investigations/chainflip-hack)

According to [The Block](https://www.theblock.co/news/defi/2026-11-22-chainflips-losses-climb-to-12-million-after-protocol-discloses-122-9-btc-theft-offers-hacker-bounty-444829), the stolen BTC remained at the attacker's receiving address as of Sunday afternoon.

In an exclusive comment to ChangeNOW, AMLBot shared new findings from its on-chain investigation.

"The drain wallet was brand new; its gas came from Tornado Cash 60 seconds before the exploit, both stablecoins were swapped to ETH within four minutes, and within nine minutes nearly all of the Ethereum-side funds were inside Tornado Cash, before either issuer could freeze anything."


AMLBot also confirmed that the stolen 122.86 BTC, accounting for more than half of Chainflip's losses, remained at a single address.

### What Did Chainflip Do After the Hack?

Chainflip activated safe mode and suspended swaps, deposits and withdrawals.

The team offered the attacker a **10% bounty for returning 90% of the stolen funds** by November 23 at 18:38 UTC.

Chainflip founder Simon Harman also said the team was working with investigators and law enforcement.

[Read Why Fast Cooperation With Law Enforcement Matters](https://changenow.io/blog/what-to-do-if-crypto-is-stolen)

The protocol had not announced a final compensation plan for affected liquidity providers at the time of reporting.

## Cyber Bridge Hack: Fake Messages Release $1.1 Million in CYBER

On November 21, an attacker exploited **Cyber's cross-chain bridge** to mint 5,213,000 CYBER on Solana and withdraw the same amount of genuine tokens from Ethereum.

The withdrawn CYBER was worth approximately **$1.1 million** at the November 21 reference price, according to [Bitquery's investigation](https://www.bitquery.io/investigations/cyber-bridge-hack).

### How Did the Cyber Bridge Hack Work?

Cyber's bridge uses LayerZero to pass messages between blockchains.

Before releasing or minting tokens, the receiving chain needs confirmation that a valid message came from the source chain.

Cyber's route relied on a single authorized verifier, known as a Decentralized Verifier Network (DVN). One valid signature from that verifier was enough for the bridge to accept a message.

Bitquery compared the messages recorded on Cyber's blockchain with those accepted on Solana.

The source chain had sent **329 legitimate messages**. Yet Solana had also accepted messages numbered 330 and 331. Neither message existed on the source chain.

Message 331 instructed the bridge to mint 5.21 million CYBER on Solana. The tokens appeared in the attacker's wallet at **16:13 UTC on November 21**.

The attacker then burned those tokens to initiate a transfer to Ethereum. About two minutes later, the Ethereum bridge contract released 5,213,000 genuine CYBER.

Before that withdrawal, the contract held 5,213,905 CYBER. **Only 905 tokens remained afterward.**

### Was LayerZero Hacked?

The attack used a bridge built on LayerZero messaging infrastructure, but investigators **did not establish a vulnerability in LayerZero** itself.

Bitquery traced the fraudulent messages to a signature from Cyber's authorized verifier.

The bridge accepted that signature as proof that the messages were genuine. It did not require confirmation from another independent verifier.

Researchers identified the key used to approve the fake messages. They could not establish how the attacker gained access to it.

### Did the Cyber Attacker Keep Access After the Exploit?

Bitquery found a second problem during its investigation.

After the first attack, the verifier's administrator replaced the signing key. The attacker then produced another fraudulent message using the replacement key.

The new message, numbered **332**, was approved on Solana but had not been executed when Bitquery last checked on November 22 at 10:00 UTC.

At that point, both keys associated with the suspicious messages remained authorized.

This raised a more serious question than the exposure of one private key: **could the attacker still access the system that generated or stored the verifier's keys?** Bitquery raised that possibility, but the root cause had not been confirmed.

"Cyber's key was replaced and the attacker signed again, so the weak point was the system that produces keys," AMLBot told ChangeNOW.


The problem extends beyond Cyber. AMLBot explained why valid signatures alone cannot guarantee that cross-chain transactions are legitimate:

"Cross-chain systems verify who signed, not whether the transaction should exist. Whether that is a single verifier, as with Cyber, or a 100-of-150 threshold, as with Chainflip, the signature becomes a single point of failure once key material leaks."


The company pointed to independent checks, including sequence counters, withdrawal limits, and delays on unusually large transfers, as ways to reduce this risk.

### Where Did the Stolen CYBER Go?

The attacker sold approximately 92% of the withdrawn tokens through decentralized exchange routes, including KyberSwap and MetaMask Swaps.

By 17:40 UTC on November 21, Bitquery had traced **575.286 ETH, worth approximately $965,000**, to one wallet.

According to AMLBot, approximately 575 ETH were transferred to a new wallet on November 23. At the time of its analysis, the funds had not been sent to a mixer.

Cyber warned users against using the affected bridge or depositing CYBER to exchanges during the investigation.

South Korean exchanges Upbit and Bithumb also suspended CYBER deposits and withdrawals, as [reported by The Block](https://www.theblock.co/news/defi/2026-11-21-cyber-investigating-suspected-1-million-bridge-exploit-as-upbit-bithumb-freeze-transfers-444810).

The project had not published a final explanation of the verifier compromise.

## Fusionist ACE Hack: $2 Million Exploit Leads to $3.7 Million Bridge Drain

On November 22, an attacker exploited the **Fusionist ACE bridge**, which connects BNB Smart Chain with the project's Endurance blockchain.

The attacker created ACE without depositing any tokens to back them. The newly minted tokens were then sold for approximately **$2 million**.

Other traders bought the discounted ACE and transferred them through Fusionist's bridge. In return, the bridge released approximately **53.7 million genuine ACE worth $3.7 million** from its reserves.

### How Was the Fusionist Bridge Hacked?

Security company Blockaid [identified unauthorized use of a privileged bridge-minter role](https://x.com/blockaid_/status/2124580794144322035).

That permission allowed to create ACE tokens on BNB Smart Chain.

According to [The Block's investigation](https://www.theblock.co/news/defi/2026-11-22-a-2-million-exploit-leads-to-a-3-7-million-free-for-all-as-traders-empty-fusionists-ace-bridge-444838), the first identified mint took place at approximately **17:55 UTC on November 22** and created 3.5 million ACE.

More minting transactions followed. In one transaction, the attacker **generated 10 quintillion ACE**. ACE's stated maximum supply was 147 million tokens.

The attacker sold the unbacked tokens through decentralized exchanges. The sudden flood of ACE pushed its price sharply lower on BNB Smart Chain.

Investigators linked the minting activity to a wallet that had previously received funding from Fusionist's deployer.

However, the available evidence does not establish how the attacker obtained control of the minting permission.

### Why Did Fusionist Lose Another $3.7 Million?

Fusionist's bridge continued processing transfers even after the unauthorized minting began. Normally, a user who burns ACE on BNB Chain can receive an equivalent amount of genuine ACE on Endurance.

After the exploit, ACE on BNB Chain was trading at a steep discount. Traders could buy those cheap tokens and use the bridge to receive genuine ACE from its reserves.

The bridge had no effective protection against those unbacked tokens being redeemed.

Between approximately **18:13 and 20:05 UTC on November 22**, it released 53.7 million ACE to 24 addresses.

One address alone received about 26.1 million ACE.

The bridge had held approximately 53.7 million ACE before the exploit. By the time the withdrawals stopped, **only 0.08 ACE remained**.

Another 27 withdrawal attempts, totaling roughly 1.36 billion ACE, reportedly failed because the bridge had run out of tokens.

The Block also identified a trader who turned an initial position of about $50 into approximately $17,670 by buying discounted ACE, bridging the tokens and selling them on an exchange.

The original attacker received approximately $2 million from token sales. The additional $3.7 million in reserve withdrawals went to other addresses.

But were all these traders acting independently?

AMLBot's analysis identified 15 wallets that received approximately 365 million newly minted ACE. According to the company, most of these wallets sent payments to the address that later supplied funds to Tornado Cash.

"The key is timing, as a coordinated wallet is prepared before the exploit; an opportunist reacts to public news," AMLBot explained.


These transaction patterns raise questions about possible coordination, although they do not establish that the wallet owners participated in the original attack.

### Where Did the Fusionist Attacker Move the Money?

Onchain Lens traced approximately **1,091.5 ETH, worth $1.87 million**, through Tornado Cash.

The Block separately tracked around 1,150 ETH, valued at approximately $2 million, moving into the mixer from wallets associated with the initial exploit.

The attacker had moved funds from BNB Chain to Ethereum using cross-chain swap services before the Tornado Cash deposits.

### What Happened to ACE After the Hack?

Fusionist warned users to stop trading, transferring and bridging ACE on BNB Smart Chain.

Gate announced that it would reverse ACE/USDT spot trades executed between 17:55 and 19:15 UTC on November 22.

The exchange also restricted ACE perpetual futures to reduce-only trading and scheduled their settlement and delisting for November 24 at 04:00 UTC.

On November 23, Bithumb [announced a suspension of ACE trading, deposits and withdrawals](https://feed.bithumb.com/notice/1655759).

The exchange said abnormally issued ACE tokens appeared to have reached exchanges. Trading was suspended from **07:30 KST on November 23**.

Bithumb did not announce a reopening date.

## How Were the Three Cross-Chain Hacks Different?

The attackers did not exploit the same weakness.

| Project | What went wrong | Result | 
|---|---|---|
| **Chainflip** | The vault accepted an unauthorized withdrawal with a valid aggregate signature | BTC, ETH and stablecoins were stolen | 
| **Cyber** | The bridge trusted messages signed by a compromised verifier | Genuine CYBER was released from Ethereum reserves | 
| **Fusionist** | An attacker minted unbacked tokens while the bridge continued accepting them | The attacker extracted \~$2 million, and traders withdrew another \~$3.7 million in ACE | 

The Fusionist case is particularly notable because the original attacker did not need to empty the bridge personally. Once cheap, unbacked ACE entered the market, other traders could use the bridge to withdraw genuine reserves.

Cyber's investigation revealed a different concern. Replacing a compromised verifier key did not immediately end the suspicious activity. Another unauthorized message was signed after the replacement.

For Chainflip, the most important unanswered question is how an attacker obtained a valid vault signature outside the normal transaction process.

The incidents also show why valid authorization alone may not be enough to protect cross-chain assets. As AMLBot noted, independent safeguards such as withdrawal limits, transaction sequence checks, and delays on unusually large transfers can help prevent a compromised signing key from enabling unrestricted withdrawals.

## Conclusion

ChangeNOW is following the Chainflip, Cyber, and Fusionist hacks. If stolen funds from these attacks pass through our platform, we'll investigate the transactions and work with law enforcement to help recover the assets.

We've helped victims of crypto theft many times before through our AML efforts. We also share practical security guides to help users avoid scams and protect their funds.

[Learn how to protect yourself from hacks](https://changenow.io/blog/category/aml-cases)

Stay safe!
