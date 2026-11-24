# 💀 Rekt: Lighter's $10.39M Loss Traced to Reused Signing Value

- **Source URL:** https://rekt.news/lighter-rekt
- **Fetched:** 2026-11-24
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2380 (id 2380)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Lighter - Rekt

*The keys were never stolen. They were solved.*

**The affected accounts’ signing code kept reusing a value it was meant to use only once per signing key, [according to Lighter](https://x.com/Lighter_xyz/status/2122394446343946717).**

Every [signature it produced sat in public view](https://x.com/Lighter_xyz/status/2122394446343946717).

Two different messages signed with the same key and that same value can turn a private key into a homework problem. [On November 16, someone turned in the answer](https://x.com/Lighter_xyz/status/2122394446343946717).

**[Those API keys could not withdraw directly to a stranger’s wallet. So the attacker took a detour](https://x.com/Lighter_xyz/status/2122394446343946717):** Create a public pool under the victim’s account, mint shares through a separate, attacker-controlled account, then pour the victim’s funds into the pool without minting additional shares. The pool grew richer. The attacker’s shares captured the increase.

**At 10:11 UTC, [$10.39 million USDC left Lighter’s Ethereum contract](https://etherscan.io/tx/0x5b6f27ded0e9a66ef6fa107083e28db9914e46d7635cc5112d760b9cb2f958c9).**

*Within minutes, [the funds were being swapped into ETH](https://bitquery.io/investigations/lighter-hack); some would later reach a Monero-linked token on Hyperliquid.*

[The reported $15.5 million covered two accounts](https://x.com/0xTria/status/2122280548047671629); [Bitquery traced 10.39 million USDC leaving Lighter](https://bitquery.io/investigations/lighter-hack).

[Lighter reported returning roughly 5 million USDC](https://x.com/Lighter_xyz/status/2122394446343946717), but gave no final loss total. The theft figure used here is $10.39 million, the traced withdrawal.

**[Lighter’s explanation drew a sharp boundary](https://x.com/Lighter_xyz/status/2122394446343946717):** Its protocol, contracts and official SDKs were unaffected.

**The affected accounts, it said, [had used signing code outside its official SDKs](https://x.com/Lighter_xyz/status/2122394446343946717).**

*That still left a question. If the signatures were public and the weakness was mathematical, why wasn’t it caught before someone used it?*

*Credit:[Lighter](https://x.com/Lighter_xyz/status/2122394446343946717), [Bitquery](https://bitquery.io/investigations/lighter-hack), [0xTria](https://x.com/0xTria/status/2122280548047671629), [Mlm onchain](https://x.com/0xTria/status/2122279354134909376), [TechFlow](https://www.techflowpost.com/en-US/article/35444), [AMLBot](https://x.com/AMLBotHQ/status/2122299878697263214), [Arkham](https://arkm.com/explorer/address/0x66Cf2f85115CC20bF439720927C1f93De9672068), [Lookonchain](https://x.com/lookonchain/status/2122574870605385787), [Unchained](https://unchainedcrypto.com/lighter-pins-drain-on-traders-leaked-api-key-says-contracts-were-not-hit/), [Protos](https://protos.com/tether-backed-abraxas-may-have-lost-17m-in-lighter-api-leak/), [EmberCN](https://x.com/EmberCN/status/2122887233678319803)*

**The public alarm traced here [began with a Telegram observation credited to Mlm onchain](https://x.com/0xTria/status/2122279354134909376), not with Lighter.**

**[0xTria relayed it to X at 10:43 UTC with the caveats still attached](https://x.com/0xTria/status/2122279354134909376):** Something weird going on with lighter, might be an exploit, not confirmed.

By then, the money had been moving for more than half an hour.

0xTria [said the wallet had been funded with roughly $10k through Relay half an hour earlier](https://x.com/0xTria/status/2122279354134909376).

Bitquery separately [records an initial gas top-up at 06:44 UTC](https://bitquery.io/investigations/lighter-hack).

*At 10:11 UTC, Lighter’s Ethereum contract [paid that wallet roughly 10.39 million USDC in a single withdrawal](https://etherscan.io/tx/0x5b6f27ded0e9a66ef6fa107083e28db9914e46d7635cc5112d760b9cb2f958c9).*

**Beginning at 10:13 UTC, [the wallet swapped 10.36 million USDC for roughly 5,752 ETH across five CoW Swap orders in four minutes, according to Bitquery](https://bitquery.io/investigations/lighter-hack). A sixth order at 10:46 brought the total to roughly 5,764 ETH.**

From 10:19 UTC, [the ETH began leaving in twelve 160 ETH lots](https://bitquery.io/investigations/lighter-hack). Bitquery linked the recipient wallets to XMR1 purchases by same-address accounts on Hyperliquid. It found LI.FI deposits for eleven of the twelve; the cross-chain links rested on matching addresses, timing and amounts.

Those transfers [moved 1,920 ETH along the route into XMR1](https://bitquery.io/investigations/lighter-hack),, roughly 3,845 ETH remained at the time.

[At 10:48 UTC, 0xTria relayed a theory from “Korean friends”](https://x.com/0xTria/status/2122280548047671629): Two large market-maker accounts had suffered API-key leaks, not a protocol hack. “If it’s right,” the post cautioned.

**[The breakdown relayed by 0xTria put the combined loss at roughly $15.5 million](https://x.com/0xTria/status/2122280548047671629):** $10.39 million from account #714710 and $5.09 million from account #714723.

[Lighter spoke at 11:02 UTC](https://x.com/Lighter_xyz/status/2122284181422284986), 51 minutes after the USDC left. The incident, it said, “appears to involve a single compromised external party.” Withdrawals and pool creation had been suspended.

Lighter’s announcement did not explain why pool creation had been suspended.

**[The next update landed at 12:49 UTC](https://x.com/Lighter_xyz/status/2122311006604984497):** Lighter attributed the incident to a leaked API key for “a specific trader’s account” and said its protocol and smart contracts were unaffected.

[Guardian mode had been enabled](https://x.com/Lighter_xyz/status/2122311006604984497). The Security Council would carry out a contract upgrade aimed at recovering funds involved in “an additional withdrawal attempt by the attacker.” Lighter also identified the same wallet the community had already flagged.

**Attacker Wallet:**
[0xb3fffca23d4444eE73349825ACD84f7b5020e387](https://etherscan.io/address/0xb3fffca23d4444eE73349825ACD84f7b5020e387)

**Withdrawal Transaction, 10.39 million USDC:** [0x5b6f27ded0e9a66ef6fa107083e28db9914e46d7635cc5112d760b9cb2f958c9](https://etherscan.io/tx/0x5b6f27ded0e9a66ef6fa107083e28db9914e46d7635cc5112d760b9cb2f958c9)

[Lighter’s incident report later said its Guardian contract tripped on the anomaly itself](https://x.com/Lighter_xyz/status/2122394446343946717). It doesn’t say when.

[If the attacker needed no access to the accounts or Lighter’s systems](https://x.com/Lighter_xyz/status/2122394446343946717), how did public signatures give up a private key?

### Once Means Once

*Every transaction on Lighter carries a signature from an API key, and every one of those signatures depends on a number the signer is supposed to generate fresh, use once and discard.*

**Cryptographers call it a nonce. Lighter’s postmortem describes it as a one-off random value that “[must be unique and unpredictable every time](https://x.com/Lighter_xyz/status/2122394446343946717).”**

**Picture each signature as an equation with two unknowns:** The signer’s private key and that one-time number. One signature does not ordinarily reveal either secret. Publish signatures on two different messages using the same key and the same one-time number, and the repeated value can be eliminated. [The private key becomes calculable](https://x.com/Lighter_xyz/status/2122394446343946717).

Two signatures. One repeated secret. One private key, recovered.

[Lighter says the affected accounts ran signing code that reused those numbers](https://x.com/Lighter_xyz/status/2122394446343946717). At the time, their signatures were public. The attacker needed no access to the accounts or to Lighter’s systems, only their publicly available signatures.

[That gives new meaning to the “leaked API key” in Lighter’s 12:49 update](https://x.com/Lighter_xyz/status/2122311006604984497), which did not explain how the key had been exposed.

**[The later incident report supplied the mechanism](https://x.com/Lighter_xyz/status/2122394446343946717):** The keys had “leaked through the accounts’ own signatures.” Rather than stealing a stored key, the attacker could calculate it from signatures already in public view.

**The failure mode is old, [and Lighter says as much](https://x.com/Lighter_xyz/status/2122394446343946717):** The same rule binds Bitcoin and Ethereum signatures.

[Android Bitcoin wallets suffered thefts in 2013](https://bitcoinmagazine.com/technical/critical-vulnerability-found-in-android-wallets-1376273924) after a faulty random-number generator reused the same values to sign transactions.

*Lighter’s position is that its own tools were never the problem. [It says its official Python, Go and TypeScript SDKs, along with the Agent Kit](https://x.com/Lighter_xyz/status/2122394446343946717), generate signing nonces with a cryptographically secure random number generator and were unaffected.*

[The affected accounts used signing code outside those official SDKs](https://x.com/Lighter_xyz/status/2122394446343946717), Lighter says.

[Lighter’s incident report does not identify the signing code or who wrote it](https://x.com/Lighter_xyz/status/2122394446343946717). Nor does it say how long the code had been reusing nonces, how many matching signature pairs were exposed, or when the attacker first found them.

Coverage filled the gap anyway.

**[TechFlow supplied a more specific account](https://www.techflowpost.com/en-US/article/35444):** An unofficial SDK used for quantitative high-frequency trading, repeating the same nonce across consecutive orders.

[Lighter’s incident report does not identify that SDK](https://x.com/Lighter_xyz/status/2122394446343946717) or describe those trading patterns.

[The word “nonce” also has another meaning in Lighter’s documentation](https://docs.lighter.xyz/developers#nonce). Its developer docs use it for a per-key transaction counter, fetched through a next-nonce API call or incremented locally. That number orders transactions; it is not the secret one-time value used to create a signature.

The repeated value that exposed these keys was the secret signing nonce, not the transaction counter. Same word, different job, with very different consequences.

[Lighter’s incident report warns anyone using custom or third-party signing code never to derive a signing nonce from a timestamp](https://x.com/Lighter_xyz/status/2122394446343946717), a counter, a weakly seeded random number generator, transaction contents or a cached value.

That is a list of unsafe practices, not a finding that timestamps caused this incident. The report identifies reused signing nonces as the failure, without saying how those values were generated.

**Recovering the key still left the attacker with a restriction, [an API key on Lighter can withdraw funds only to the account owner’s own wallet](https://x.com/Lighter_xyz/status/2122394446343946717).**

*So how did the attacker get the money out?*

### Around the Fence

*Lighter fences in API-key permissions. A key can trade, manage positions and move funds between accounts tied to the same wallet.*

[Withdrawals go only to the owner’s own wallet](https://x.com/Lighter_xyz/status/2122394446343946717); transferring funds to a public pool now requires the owner’s wallet signature.

**[The attacker exploited those permissions to get around the withdrawal restriction](https://x.com/Lighter_xyz/status/2122394446343946717):** Lighter counted a public pool created by an account as one of that account’s own sub-accounts.

[According to Lighter’s incident report](https://x.com/Lighter_xyz/status/2122394446343946717), the attacker used the recovered key to create a public pool from the affected account.

Pool shares were minted in a separate, attacker-controlled account. The victim’s funds then went into the pool, [raising its value without minting any additional shares](https://x.com/Lighter_xyz/status/2122394446343946717).

**Redeem the shares. Withdraw the proceeds. [Lighter says its protocol and smart contracts were unaffected](https://x.com/Lighter_xyz/status/2122394446343946717). The attacker had routed the victim’s funds through a pool into an account they controlled. The fence never moved; the money walked around it.**

**[0xTria’s Korean sources added detail that neither Lighter’s incident report nor Bitquery’s trace verifies](https://x.com/0xTria/status/2122280548047671629):** The victim’s positions closed first, the pool set to a 0% fee, roughly $10k buying 99.99% of it, and the USDC moved in roughly $1 million chunks.

The pool creation, share minting, transfer and redemption happened inside Lighter’s rollup. [On Ethereum, the trail began with the receiving wallet’s funding at 06:44 UTC, more than three hours before the withdrawal](https://bitquery.io/investigations/lighter-hack).

**Attacker Wallet:**

[0xb3fffca23d4444eE73349825ACD84f7b5020e387](https://etherscan.io/address/0xb3fffca23d4444eE73349825ACD84f7b5020e387)

**Before the withdrawal, two wallets sent ETH to the receiving address:** 0.02761 ETH in the first transfer, followed by 0.02771 ETH in the second.

**ETH funding transaction 1, 0.02761 ETH:**

[0x9a2bd93046a3f25df9428d9b2a4eae5557aec44fd19d4dd9444490f09baa81c4](https://etherscan.io/tx/0x9a2bd93046a3f25df9428d9b2a4eae5557aec44fd19d4dd9444490f09baa81c4)

**ETH funding transaction 2, 0.02771 ETH:**

[0x15f0da66f434f05424c51fb53bc83f75b4fbb1fed9f1808eea86f526bfaafe5d](https://etherscan.io/tx/0x15f0da66f434f05424c51fb53bc83f75b4fbb1fed9f1808eea86f526bfaafe5d)

*At 08:45 UTC, according to Bitquery’s timeline, [the wallet received 10,525.84 USDC through Across](https://etherscan.io/tx/0xe6b8e54bb04420c42b20062d6941813f02b7e09556c44cc6e27bf6abcd78ca07). At 09:35, [it sent 10,200 USDC through Relay’s router and an intermediary address into Lighter’s Ethereum contract, all within the same transaction](https://etherscan.io/tx/0x155076049c3992e82546009c840ad2d79e311522491c401dc380c51c592dc050).*

**Across inflow, 10,525.84 USDC:**

[0xe6b8e54bb04420c42b20062d6941813f02b7e09556c44cc6e27bf6abcd78ca07](https://etherscan.io/tx/0xe6b8e54bb04420c42b20062d6941813f02b7e09556c44cc6e27bf6abcd78ca07)

**Relay-routed transfer into Lighter’s Ethereum contract, 10,200 USDC:**

[0x155076049c3992e82546009c840ad2d79e311522491c401dc380c51c592dc050](https://etherscan.io/tx/0x155076049c3992e82546009c840ad2d79e311522491c401dc380c51c592dc050)

At 10:11 UTC, Lighter’s contract paid the attacker 10.39 million USDC.

**Lighter Ethereum Contract (ZkLighter):**

[0x3B4D794a66304F130a4Db8F2551B0070dfCf5ca7](https://etherscan.io/address/0x3b4d794a66304f130a4db8f2551b0070dfcf5ca7)

**Lighter Withdrawal to Attacker, 10.39 million USDC at 10:11 UTC:**

[0x5b6f27ded0e9a66ef6fa107083e28db9914e46d7635cc5112d760b9cb2f958c9](https://etherscan.io/tx/0x5b6f27ded0e9a66ef6fa107083e28db9914e46d7635cc5112d760b9cb2f958c9)

Ten minutes later, at 10:21 UTC, [the same wallet deposited 10,200 USDC into Lighter’s contract](https://bitquery.io/investigations/lighter-hack), the same amount it had sent into Relay earlier.

**Deposit from Attacker Wallet into Lighter Contract, 10,200 USDC at 10:21 UTC:**

[0x196838a707b02403dca4c4e4f64067ec45b0bdee4c7673b9e05afd08f89213fb](https://etherscan.io/tx/0x196838a707b02403dca4c4e4f64067ec45b0bdee4c7673b9e05afd08f89213fb)

Most of the USDC didn’t sit. Between 10:13 and 10:17 UTC, [five CoW Swap orders sold 10.36 million USDC for about 5,752 ETH](https://bitquery.io/investigations/lighter-hack), according to Bitquery; the largest alone sold 5,000,000 USDC for 2,775.37 ETH. A sixth order at 10:46:23 UTC swapped another 23,183 USDC for 12.84 ETH, bringing the six-order total to roughly 5,764 ETH.

**Largest CoW Swap Order, 5 million USDC for 2,775.37 ETH at 10:15:11 UTC:**

[0x2a5f6efd130af6900596069b4a48c74c0e1b1dc5742577482e42c59a590060d2](https://etherscan.io/tx/0x2a5f6efd130af6900596069b4a48c74c0e1b1dc5742577482e42c59a590060d2)

*Then the ETH started leaving in identical pieces. Twelve 160 ETH lots went out between 10:19 and 11:55 UTC, each to a fresh wallet. [Bitquery linked each recipient to a Hyperliquid account at the same address and found LI.FI deposits for eleven of the twelve](https://bitquery.io/investigations/lighter-hack); the cross-chain links rest on matching addresses, timing and amounts.*

[Bitquery did not read the bridge’s own records; it linked the deposits to the Hyperliquid accounts by their shared addresses, timing and amounts](https://bitquery.io/investigations/lighter-hack). Together, the twelve accounts bought 6,705.09 XMR1 for $3,461,245 and still held about 6,700 XMR1 at the 12:44 UTC snapshot.

**160 ETH transfer to recipient 1 at 10:19 UTC:**

[0xdedaf598b2f9a1c91377222acc50b3b62191eb02c8d1b16f6fd36003291345e0](https://etherscan.io/tx/0xdedaf598b2f9a1c91377222acc50b3b62191eb02c8d1b16f6fd36003291345e0)

**160 ETH transfer to recipient 2 at 10:20 UTC:**

[0xa7226316cc6a6c12bebc0d09b0fd01ee42bdb0c72d223bbf1132d8417d8cd3ba](https://etherscan.io/tx/0xa7226316cc6a6c12bebc0d09b0fd01ee42bdb0c72d223bbf1132d8417d8cd3ba)

**160 ETH transfer to recipient 3 at 10:39 UTC:**

[0x46f65b0784dd909f42a026a5848b2fb047471624753acc370ca635af766e7d9e](https://etherscan.io/tx/0x46f65b0784dd909f42a026a5848b2fb047471624753acc370ca635af766e7d9e)

**160 ETH transfer to recipient 4 at 10:40 UTC:**

[0xc52c7f47a0b8dcd2e818618f7d208ec3dcc53c34231cecbfb185f12099abaeed](https://etherscan.io/tx/0xc52c7f47a0b8dcd2e818618f7d208ec3dcc53c34231cecbfb185f12099abaeed)

**160 ETH transfer to recipient 5 at 10:57 UTC:**

[0xaca58d110852249da9948fd83fbe418a8acfe126517b412d5d07621a6f7e9d3a](https://etherscan.io/tx/0xaca58d110852249da9948fd83fbe418a8acfe126517b412d5d07621a6f7e9d3a)

**160 ETH transfer to recipient 6 at 10:58 UTC:**

[0x86e22d2e9b11405010875104d346e55f1d9c86518f940fccab7bb27399d827f2](https://etherscan.io/tx/0x86e22d2e9b11405010875104d346e55f1d9c86518f940fccab7bb27399d827f2)

**160 ETH transfer to recipient 7 at 11:17 UTC:**

[0x8638e4d2773c36e3a2e5d2d8390f7c878259469ad7b86659d6d8fd928c6afea7](https://etherscan.io/tx/0x8638e4d2773c36e3a2e5d2d8390f7c878259469ad7b86659d6d8fd928c6afea7)

**160 ETH transfer to recipient 8 at 11:17 UTC:**

[0x3a14e58298e9af2b95e6afcdc6712ea32998357db4d6f1f7de654834927b61bf](https://etherscan.io/tx/0x3a14e58298e9af2b95e6afcdc6712ea32998357db4d6f1f7de654834927b61bf)

**160 ETH transfer to recipient 9 at 11:36 UTC:**

[0x6d789a0edfd7a1733906bb8fe211213b0eb04757c10c6b794729785ddae6b41b](https://etherscan.io/tx/0x6d789a0edfd7a1733906bb8fe211213b0eb04757c10c6b794729785ddae6b41b)

**160 ETH transfer to recipient 10 at 11:36 UTC:**

[0x966255baae6e655ad0b73b5ec2d2e1def643f78b82e908fc29691aaf0645e0a2](https://etherscan.io/tx/0x966255baae6e655ad0b73b5ec2d2e1def643f78b82e908fc29691aaf0645e0a2)

**160 ETH transfer to recipient 11 at 11:54 UTC:**

[0x3a1608cc390a7ca221904b881a4a472b2386836a3c1408e95e830c11d01aec27](https://etherscan.io/tx/0x3a1608cc390a7ca221904b881a4a472b2386836a3c1408e95e830c11d01aec27)

**160 ETH transfer to recipient 12 at 11:55 UTC:**

[0xac70c7a21ce011070b76f0b4241e549151a832d0ba030d8382c0c7b039c320ab](https://etherscan.io/tx/0xac70c7a21ce011070b76f0b4241e549151a832d0ba030d8382c0c7b039c320ab)

**At 11:55 UTC, after the twelfth lot, [roughly 3,845 ETH remained in the main wallet](https://bitquery.io/investigations/lighter-hack).**

**[Bitquery reports five further outgoing payments totaling 760 ETH](https://bitquery.io/investigations/lighter-hack). But 320 ETH returned:** Two new wallets each received 160 ETH and sent it back about 20 minutes later. The other three payments totaled about 440 ETH. By 22:35 UTC, Bitquery recorded a balance of roughly 3,404 ETH in the main wallet.

The attacker’s wallet, [0xb3ff…e387](https://etherscan.io/address/0xb3fffca23d4444eE73349825ACD84f7b5020e387), did not stay quiet. A [later Etherscan transaction listing](https://etherscan.io/txs?a=0xb3fffca23d4444eE73349825ACD84f7b5020e387) showed 19 outgoing transactions totaling roughly 3,139 ETH to THORChain, [including a final displayed deposit of about 214.67 ETH on November 20th](https://etherscan.io/tx/0x0ce542525c06f8128f59c281bfead7dc3ba5b23f073dd45afe66a82832e3b922).

Another [299 ETH went to Maya Protocol’s ETH router](https://etherscan.io/tx/0x0cb252b31b389b890a92a4dcc042165d8451bbd0aefef93e90d4b8c72ecbb3f4).

The attacker’s wallet also made four outgoing transfers totaling about 625 ETH to other addresses.

**Outgoing transfer of 50.01 ETH:**

[0xa4c99dc3d3da3479c3f73990ed5b7751b23af5d7da9ae5416b600967d84d70f9](https://etherscan.io/tx/0xa4c99dc3d3da3479c3f73990ed5b7751b23af5d7da9ae5416b600967d84d70f9)

**Outgoing transfer of 100 ETH:**

[0x4a7412796faa5d8db47e1b4aa3470a20aa0e3ec355538b1ecc65ead839fd8432](https://etherscan.io/tx/0x4a7412796faa5d8db47e1b4aa3470a20aa0e3ec355538b1ecc65ead839fd8432)

**Outgoing transfer of 160 ETH:**

[0x511fa3c04bee8de70ee85de62a8b92e11c8b029850cff8917d6a43d4eacb0966](https://etherscan.io/tx/0x511fa3c04bee8de70ee85de62a8b92e11c8b029850cff8917d6a43d4eacb0966)

**Outgoing transfer of 315 ETH:**

[0x44a744d4f49dde04fcac3db223e906fd667338b1e6c357bd972ff4008c945bd2](https://etherscan.io/tx/0x44a744d4f49dde04fcac3db223e906fd667338b1e6c357bd972ff4008c945bd2)

[Lighter’s incident report](https://x.com/Lighter_xyz/status/2122394446343946717) did not name the affected trader.

**The trail points to Abraxas Capital, though neither the firm nor Lighter has confirmed the identification.**

[AMLBot linked the two affected Lighter accounts to Abraxas Capital](https://x.com/AMLBotHQ/status/2122299878697263214), naming two Ethereum wallets.

[Arkham labels one of them as “Abraxas Capital Mgmt (Heka Funds)”](https://arkm.com/explorer/address/0x66Cf2f85115CC20bF439720927C1f93De9672068).

**First Ethereum wallet linked to Abraxas by AMLBot; also labeled by Arkham as “Abraxas Capital Mgmt (Heka Funds)”:**

[0x66Cf2f85115CC20bF439720927C1f93De9672068](https://etherscan.io/address/0x66Cf2f85115CC20bF439720927C1f93De9672068)

**Second Ethereum wallet linked to Abraxas by AMLBot:**

[0x0d1D09312665D31Ed68231b88079a245E0458F6F](https://etherscan.io/address/0x0d1D09312665D31Ed68231b88079a245E0458F6F)

Both wallets had a history of receiving USDC from Lighter and forwarding it to Binance-labeled deposit addresses. [The Arkham-labeled wallet](https://arkm.com/explorer/address/0x66Cf2f85115CC20bF439720927C1f93De9672068) received a payment valued at roughly $9.44 million, then sent USDC with the same displayed value to its Binance-labeled destination eight blocks later. The second wallet received a payment valued at roughly $9.86 million and made a matching-value onward transfer five blocks later.

**Lighter payment to the Arkham-labeled wallet, displayed value approximately $9.44 million:**

[0x22b176f4ffc5fc999157f613729d92ac981b7f3ec373032ba39d4fb32f45f65d](https://etherscan.io/tx/0x22b176f4ffc5fc999157f613729d92ac981b7f3ec373032ba39d4fb32f45f65d)

**Onward USDC transfer to its Binance-labeled deposit address, eight blocks later:**

[0x053c94d4155b8fdbbd29b32b89651850c97f07faad54c98c28497be1b60db1d9](https://etherscan.io/tx/0x053c94d4155b8fdbbd29b32b89651850c97f07faad54c98c28497be1b60db1d9)

**Lighter payment to the second AMLBot-listed wallet, displayed value approximately $9.86 million:**

[0xa3d406e2ae991da141cb1e6708e52b0c25f7dde349812d4ee69b532f2b14880a](https://etherscan.io/tx/0xa3d406e2ae991da141cb1e6708e52b0c25f7dde349812d4ee69b532f2b14880a)

**Onward USDC transfer to its Binance-labeled deposit address, five blocks later:**

[0x89c5703a9c00a25a1ff36ed05d23fe4cb5ebf1a25d6cf6c9cffa5f4c05abb257](https://etherscan.io/tx/0x89c5703a9c00a25a1ff36ed05d23fe4cb5ebf1a25d6cf6c9cffa5f4c05abb257)

[Arkham’s label supports the Abraxas attribution](https://arkm.com/explorer/address/0x66Cf2f85115CC20bF439720927C1f93De9672068), while the transfer records show both wallets receiving USDC from Lighter and forwarding it to Binance-labeled deposit addresses:  [The first wallet’s receipt](https://etherscan.io/tx/0x22b176f4ffc5fc999157f613729d92ac981b7f3ec373032ba39d4fb32f45f65d) and [onward transfer](https://etherscan.io/tx/0x053c94d4155b8fdbbd29b32b89651850c97f07faad54c98c28497be1b60db1d9), and [the second wallet’s receipt](https://etherscan.io/tx/0xa3d406e2ae991da141cb1e6708e52b0c25f7dde349812d4ee69b532f2b14880a) and[onward transfer](https://etherscan.io/tx/0x89c5703a9c00a25a1ff36ed05d23fe4cb5ebf1a25d6cf6c9cffa5f4c05abb257).

*These movements are separate from [the 10.39 million USDC withdrawal to the identified attacker’s wallet](https://etherscan.io/tx/0x5b6f27ded0e9a66ef6fa107083e28db9914e46d7635cc5112d760b9cb2f958c9). Bitquery also examined a later payment of roughly $2.4 million to the first wallet, received 96 seconds before the attacker’s withdrawal, and [did not link that payment to the theft](https://bitquery.io/investigations/lighter-hack).*

The Abraxas identification remains an attribution, not a confirmed finding.

Separately from the attacker’s money trail, analysts reported the Abraxas-linked accounts unwinding their Hyperliquid exposure.

**On November 17, [Lookonchain described Abraxas as potentially affected by the Lighter API-key leak and reported that almost all its Hyperliquid shorts had been closed](https://x.com/lookonchain/status/2122574870605385787), leaving roughly $11.6 million in open positions.**

[On-chain analyst EmberCN reported that Abraxas had fully closed its on-chain positions following the reported 10.39 million USDC theft through its compromised Lighter API key](https://x.com/EmberCN/status/2122887233678319803). According to the post, it closed $200 million in Hyperliquid positions, then transferred all 109 million USDC in remaining margin to Binance and requested unstaking of its entire 219,000 HYPE balance, valued at about $15 million. EmberCN linked the unwind to the theft but provided no statement from Abraxas confirming its reason for the moves.

[Abraxas Capital Management has not made any announcements](https://x.com/AbraxasCM) on this situation as of November 20th.

**The focus now shifts from the accounts linked to Abraxas to the permissions that let the attacker move the money.**

*If the money could move this far without breaking the withdrawal rules, what needed fixing before Lighter could reopen?*

### Closing the Detour

*A little over seven hours after announcing the freeze, [Lighter said the exits were open again](https://x.com/Lighter_xyz/status/2122394446343946717).*

[Lighter’s 11:02 UTC alert](https://x.com/Lighter_xyz/status/2122284181422284986) had suspended all withdrawals and pool creation.

The incident report, posted at 18:20 UTC, [announced that Guardian mode had been disabled and pending withdrawals were being processed](https://x.com/Lighter_xyz/status/2122394446343946717).

**[It also handed the Guardian the credit](https://x.com/Lighter_xyz/status/2122394446343946717):** The contract was triggered by the anomaly, paused withdrawals and let the Security Council return \~5MM USDC to the affected trader.

The public account leaves the intervention only partly explained. At 12:49 UTC, [Lighter said it was trying to recover funds involved in an additional withdrawal attempt and that the Security Council would perform a contract upgrade](https://x.com/Lighter_xyz/status/2122311006604984497).

[The incident report did not specify what anomaly triggered the Guardian](https://x.com/Lighter_xyz/status/2122394446343946717), when it intervened, or what the upgrade changed.

**By the time Lighter announced withdrawals had reopened, it listed two fixes as completed.**

[Moving funds into a public pool now requires a wallet signature, so an API key alone can’t do it](https://x.com/Lighter_xyz/status/2122394446343946717). And API-key signatures are no longer public.

Requiring a wallet signature closes the public-pool route the attacker used. Making API-key signatures non-public removes the public data the attacker used to calculate the private keys.

Making signatures non-public does not erase the ones already published. [Lighter told anyone unsure whether their code had ever reused a nonce to rotate all their API keys and switch to an official SDK](https://x.com/Lighter_xyz/status/2122394446343946717).

*Under “What we’re doing,” [Lighter also listed monitoring for nonce reuse, contacting affected accounts and proactively voiding affected API keys](https://x.com/Lighter_xyz/status/2122394446343946717). Making new signatures non-public also removes a source of data outside observers could use to detect nonce reuse.*

**A stolen key had other options, too. The same report warns that whoever holds one could [place orders from the victim’s account against their own orders at bad prices](https://x.com/Lighter_xyz/status/2122394446343946717), moving value to themselves, a tactic that works best in thinly traded markets.**

They could also [open large or highly leveraged positions that expose the victim’s account to heavy losses or liquidation](https://x.com/Lighter_xyz/status/2122394446343946717).

Lighter said it was [adding IP allowlists and configurable per-key permissions and limits](https://x.com/Lighter_xyz/status/2122394446343946717) to reduce the damage a compromised key could cause, but did not list those protections as completed when withdrawals reopened.

**Put plainly:** On reopening day, a leaked key alone could no longer move an account’s funds into a public pool. A key with trading permissions could still trade the account into the ground.

**The victim’s side of the story stayed quiet. [The report says nothing about whether the trader would be covered for the 10.39 million USDC that left](https://x.com/Lighter_xyz/status/2122394446343946717).**

[Protos said it sought comment from Abraxas and Lighter](https://protos.com/tether-backed-abraxas-may-have-lost-17m-in-lighter-api-leak/), and reported no response.

[Lookonchain reported the Abraxas-linked Hyperliquid account closing shorts and withdrawing funds over the preceding 24 hours](https://x.com/lookonchain/status/2122318038301397353), with its account value down about $150 million.

**That decline is not, by itself, a measure of trading losses or additional funds stolen.**

*If a leaked key can still bleed an account without ever touching a pool, how much did closing the detour actually fix?*

*The keys were solved outside Lighter. The stolen $10.39 million USDC left through it.*

**According to Lighter’s incident report, [a trader’s signing code repeated a number it was meant to use once, and public signatures were enough to hand an outsider the keys](https://x.com/Lighter_xyz/status/2122394446343946717).**

Those keys could not withdraw directly to a stranger’s wallet. [But a public pool created by the victim’s account counted as one of its sub-accounts](https://x.com/Lighter_xyz/status/2122394446343946717), giving the attacker a route around that restriction.

**[The incident report drew its boundary cleanly](https://x.com/Lighter_xyz/status/2122394446343946717):** The protocol, contracts and infrastructure, by Lighter’s account, were unaffected. So were its official SDKs. The failed signing code belonged elsewhere.

**But the signing failure and the exit route were different problems. One exposed the keys. The other let those keys move value beyond the protection the withdrawal restriction appeared to provide. [Lighter subsequently required a wallet signature for transfers into public pools](https://x.com/Lighter_xyz/status/2122394446343946717).**

[Its incident report named neither the trader nor the failed signing implementation](https://x.com/Lighter_xyz/status/2122394446343946717). API-key signatures are no longer public, and Lighter says it will monitor for nonce reuse, contact affected accounts and void exposed keys.

The cryptography did not fail. The signing code reused a number it could not safely repeat.

**The signing failure explains how the attacker got the keys. [The pool permissions explain how those keys became an exit](https://x.com/Lighter_xyz/status/2122394446343946717).**

*What did the withdrawal restriction really protect if the same key could move the money somewhere the attacker could claim it?*

REKT serves as a public platform for anonymous authors, we take no responsibility for the views or content hosted on REKT.

**donate (ETH / ERC20): [0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C](https://etherscan.io/address/0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C)**

disclaimer:

REKT is not responsible or liable in any manner for any Content posted on our Website or in connection with our Services, whether posted or caused by ANON Author of our Website, or by REKT. Although we provide rules for Anon Author conduct and postings, we do not control and are not responsible for what Anon Author post, transmit or share on our Website or Services, and are not responsible for any offensive, inappropriate, obscene, unlawful or otherwise objectionable content you may encounter on our Website or Services. REKT is not responsible for the conduct, whether online or offline, of any user of our Website or Services.
