# 🕵️ Three-Year-Old On-Chain Evidence Links Zunami Protocol Deployer to Its Own Hackers

- **Source URL:** https://rekt.news/zunami-protocol-case-file
- **Fetched:** 2026-11-15
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1859 (id 1859)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Zunami Protocol - Case File

*Three days after the [August 2023 hack](https://rekt.news/zunami-protocol-rekt), the [Zunami Protocol Deployer](https://etherscan.io/address/0xe9b2B067eE106A6E518fB0552F3296d22b82b32B) sent a direct transaction to the attacker's wallet.*

**Zero ETH transferred. Block 17928584, timestamp 2023-08-16 16:28:47 UTC, sitting on Etherscan in plain sight.**

**Transfer Transaction:** [0x91b41d5b5b30a941c65d5da952c4b11390f364b41cf81a1a87fba9b67b69fe22](https://etherscan.io/tx/0x91b41d5b5b30a941c65d5da952c4b11390f364b41cf81a1a87fba9b67b69fe22)

It went unnoticed in public coverage for three years.

**[Real-time security coverage flagged the exploit within the hour](https://x.com/peckshield/status/1690857760412610560):** Flash loans, price manipulation, 1,184 ETH drained, funds laundered through Tornado Cash. The standard post-mortem wrote itself. Case closed, move on, next victim.

The exploit got covered, the aftermath didn't.

[Independent forensic investigator NanoJS10 found a thread](https://github.com/NanoJS10/Zunami-protocol-Investigation-), then kept pulling.

[What came out of that thread](https://github.com/NanoJS10/Zunami-protocol-Investigation-) is no longer a post-mortem, it's a case file, with wallet addresses, exchange notifications, FBI and Interpol filings, and a Coinbase Senior Director on record confirming account data is ready for law enforcement upon subpoena.

[$2,969,000 across four exploits](https://github.com/NanoJS10/Zunami-protocol-Investigation-) in 28 months. [The last one in May of 2025](https://rekt.news/zunami-protocol-rekt2).

*When the real story is already written on a public ledger and nobody reads it for three years, what else has been hiding in plain sight?*

*Credit:[NanoJS10](https://github.com/NanoJS10/Zunami-protocol-Investigation-), [Zunami Protocol](https://zunamiprotocol.medium.com/the-zunami-protocol-has-come-under-two-attacks-e201a8a0ec6c), [Sterx](https://x.com/kirill_zunami/status/1928131508117651725)*

**Every protocol has a deployer wallet. It's the address that birthed the contracts, the wallet that signed the original deployment transactions, holds the keys to upgrade logic, and carries the highest level of trust the protocol's architecture can assign.**

In forensic analysis of blockchain exploits, a deployer wallet initiating contact with an attacker's wallet post-exploit is treated as anomalous.

In a genuinely external hack, those two addresses should not have a post-exploit relationship.

On August 16, 2023, three days after [Zunami lost millions to what was reported as an external price manipulation attack](https://rekt.news/zunami-protocol-rekt), the [Zunami Protocol Deployer](https://etherscan.io/address/0xe9b2B067eE106A6E518fB0552F3296d22b82b32B) initiated contact with the attacker's wallet.

*On August 16, 2023, three days after Zunami lost millions to what was reported as an [external price manipulation attack](https://rekt.news/zunami-protocol-rekt), the [Zunami Protocol Deployer](https://etherscan.io/address/0xe9b2B067eE106A6E518fB0552F3296d22b82b32B) sent a transaction to the attacker's wallet carrying a plain-text message embedded in the transaction input data.*

**Contact Transaction:** [0x91b41d5b5b30a941c65d5da952c4b11390f364b41cf81a1a87fba9b67b69fe22](https://etherscan.io/tx/0x91b41d5b5b30a941c65d5da952c4b11390f364b41cf81a1a87fba9b67b69fe22)

**Zunami Protocol Deployer:**
[0xe9b2B067eE106A6E518fB0552F3296d22b82b32B](https://etherscan.io/address/0xe9b2B067eE106A6E518fB0552F3296d22b82b32B)

**2023 Attacker EOA:**
[0x5f4C21c9Bb73c8B4a296cC256C0cDe324dB146DF](https://etherscan.io/address/0x5f4C21c9Bb73c8B4a296cC256C0cDe324dB146DF)

**[The message read](https://etherscan.io/tx/0x91b41d5b5b30a941c65d5da952c4b11390f364b41cf81a1a87fba9b67b69fe22):** "We're presenting a 20% reward for the funds taken from this hack, which you can keep by returning the remaining 80%. We believe this is a fair price and it will enable all parties to come out ahead. If not, we will bring our full force to address the issue with the utmost severity of the law. We anticipate the funds' return by August 19th at 09:00 UTC. Next, we raise the reward and open it to the public."

**No token movement. No contract interaction. [A settlement offer](https://etherscan.io/tx/0x91b41d5b5b30a941c65d5da952c4b11390f364b41cf81a1a87fba9b67b69fe22), written in plain text, sent from the protocol's own deployer wallet directly to the attacker's wallet, three days after the hack.**

[The deadline in that message](https://etherscan.io/tx/0x91b41d5b5b30a941c65d5da952c4b11390f364b41cf81a1a87fba9b67b69fe22) was August 19, 2023 at 09:00 UTC.

After that deadline passed, on August 24th, [the deployer wallet made a zero-ETH self-transaction](https://etherscan.io/tx/0x773db62b2328cf2173526ec346dfebffa96e9d9a08715abf7b99cc347ad6556d), then resumed ordinary protocol activity.

**On its own, a zero-value self-transfer is routine wallet housekeeping. What is notable is the sequence:** A plain-text settlement demand, a deadline, no visible public response, then a return to normal operations.

*The on-chain record shows no public announcement that the negotiation had failed, and no evidence of the promised public reward escalation.*

**The settlement window closed in silence.**

[NanoJS10 found the transaction](https://github.com/NanoJS10/Zunami-protocol-Investigation-), not in real time, but three years later. The message inside it took another set of eyes.

That is the difference between coverage and forensics.

The wallet cluster behind the message points in one direction.

The [deployer wallet](https://etherscan.io/address/0xe9b2B067eE106A6E518fB0552F3296d22b82b32B) that sent that message traces directly to [sterx.eth](https://etherscan.io/address/0xF9605D8c4c987d7Cb32D0d11FbCb8EeeB1B22D5d).

**Sterx.eth’s Wallet:**

[0xF9605D8c4c987d7Cb32D0d11FbCb8EeeB1B22D5d](https://etherscan.io/address/0xF9605D8c4c987d7Cb32D0d11FbCb8EeeB1B22D5d)

[sterx.eth funded an intermediate wallet, which in turn funded the Zunami Deployer at launch.](https://github.com/NanoJS10/Zunami-protocol-Investigation-)

**Intermediate Wallet:**
[0x76B70FC212F688104b2ae580D82b62877BCCB2d7](https://etherscan.io/address/0x76b70fc212f688104b2ae580d82b62877bccb2d7)

[According to NanoJS10's forensic investigation](https://github.com/NanoJS10/Zunami-protocol-Investigation-), sterx.eth funded the Deployer at launch, continued receiving funds from it across years of operation, and in April of 2026, the Deployer [sent 0.014 ETH directly to sterx.eth](https://etherscan.io/tx/0x3370d955b854a98b6578212e085c67ab94329740856dbd4da23ca05f0200d182), supporting the inference that the two wallets were under shared control. [sterx.eth also controls zunamidao.eth](https://github.com/NanoJS10/Zunami-protocol-Investigation-).

[Zunami - Rekt II identified sterx.eth as the wallet of Zunami CEO Kirill Kozlov](https://rekt.news/zunami-protocol-rekt2). The wallet that negotiated privately with the attacker and the CEO's personal wallet appear to belong to the same operational cluster, connected at launch and still transacting in 2026.

**No post-mortem in the public record noted the deployer-to-attacker message. No community discussion named it. Zunami's own incident response never addressed it.**

*Three years of silence on a negotiation encoded on a public ledger, so what else was on Etherscan that nobody went looking for?*

### 143 Days Out

*The August 2023 attack didn't start in August.*

[On-chain records show it started on March 23, 2023](https://github.com/NanoJS10/Zunami-protocol-Investigation-), exactly 143 days before the exploit, when 15.999 ETH arrived in a staging wallet from an OKX hot wallet.

**OKX Hot Wallet to Staging Wallet A:** [0x1b315017748bf8b7aca7d58771e172e88a5d9b08a972f8f7027dc7014433b5cb](https://etherscan.io/tx/0x1b315017748bf8b7aca7d58771e172e88a5d9b08a972f8f7027dc7014433b5cb)

**OKX Hot Wallet:**
[0x4E7b110335511F662FDBB01bf958A7844118c0D4](https://etherscan.io/address/0x4E7b110335511F662FDBB01bf958A7844118c0D4)

**Wallet A (Staging Wallet):**
[0xF00d0e11AcCe1eA37658f428d947C3FFFAeaDe70](https://etherscan.io/address/0xF00d0e11AcCe1eA37658f428d947C3FFFAeaDe70)

*OKX is a KYC exchange. Whoever funded that wallet has an identity on file.*

**Five months, two exchanges, and one staging wallet, filling up in silence.**

On day 96 of the 143-day window, a Binance account dropped in another 34.998 ETH.

**Binance to Staging Wallet A (34.998 ETH, 2023-05-27):** [0x27f5665edacc30a7bae57d27e964272087b7b9f8276c468a48b6b6fe13e653a1](https://etherscan.io/tx/0x27f5665edacc30a7bae57d27e964272087b7b9f8276c468a48b6b6fe13e653a1)

Two KYC exchanges, two identity trails, and one staging wallet.

From there, [Wallet A](https://etherscan.io/address/0xF00d0e11AcCe1eA37658f428d947C3FFFAeaDe70) began feeding [Wallet B](https://etherscan.io/address/0x12e98c4EBD742ca9465789570e5cf4Df9EEd0Fb0), a secondary accumulation wallet, across five transfers spanning the full 143 days.

**Wallet B:**
[0x12e98c4EBD742ca9465789570e5cf4Df9EEd0Fb0](https://etherscan.io/address/0x12e98c4EBD742ca9465789570e5cf4Df9EEd0Fb0)

*Day 46 - 0.00036 ETH. A test.*

**Wallet A to Wallet B (0.00036 ETH, 2023-04-07):** [0x5ad68e8ae2b68b3ffc76f94dbf6933ce234b5c0f47c2f310bb7f07f744ed770a](https://etherscan.io/tx/0x5ad68e8ae2b68b3ffc76f94dbf6933ce234b5c0f47c2f310bb7f07f744ed770a)

*Day 75 0.092 ETH.*

**Wallet A to Wallet B (0.092 ETH, 2023-05-07):** [0x2a1dc84d940feeb0253f926affe9d7a7639768c5475a2296401d1d099b111b17](https://etherscan.io/tx/0x2a1dc84d940feeb0253f926affe9d7a7639768c5475a2296401d1d099b111b17)

*Day 107 - 1.41 ETH.*

**Wallet A to Wallet B (1.41 ETH, 2023-06-06):** [0x216f1585d7e921c3fb5008a28ef8f09dadc69d214a8235cb7b7b90bd7a969af9](https://etherscan.io/tx/0x216f1585d7e921c3fb5008a28ef8f09dadc69d214a8235cb7b7b90bd7a969af9)

*Day 136 - 3.88 ETH.*

**Wallet A to Wallet B (3.88 ETH, 2023-07-07):** [0x297ca310dbe55b65a3b86a3fd5a88924c8dbdfc4835bfbe936d8fb7b3ce92bba](https://etherscan.io/tx/0x297ca310dbe55b65a3b86a3fd5a88924c8dbdfc4835bfbe936d8fb7b3ce92bba)

*Day 143 - 5.19 ETH. One week before the exploit. The staging chain was complete.*

**Wallet A to Wallet B - Final Staging (5.19 ETH, 2023-08-06):** [0x74454ddcdea146a6a0006acc1cef4adf9142475037f9c52ea517f7493cf05e7c](https://etherscan.io/tx/0x74454ddcdea146a6a0006acc1cef4adf9142475037f9c52ea517f7493cf05e7c)

Then on August 13, 2023, exploit day, Staging Wallet A had one more role to play.

**Exploit-Day Operational Link (2023-08-13 22:41:35 UTC):** [0x76b70f7c6a9a58388ffa98be0ff2b68f97c05237686693c5cf1c92da29dd713f](https://etherscan.io/tx/0x76b70f7c6a9a58388ffa98be0ff2b68f97c05237686693c5cf1c92da29dd713f)

[The 2023 attacker EOA](https://etherscan.io/address/0x5f4C21c9Bb73c8B4a296cC256C0cDe324dB146DF) routed 1,265.45 USDT to [Staging Wallet A](https://etherscan.io/address/0xF00d0e11AcCe1eA37658f428d947C3FFFAeaDe70) via the [0x Exchange Proxy](https://etherscan.io/address/0xDef1C0ded9bec7F1a1670819833240f027b25EfF).

**2023 Attacker EOA:**

[0x5f4C21c9Bb73c8B4a296cC256C0cDe324dB146DF](https://etherscan.io/address/0x5f4C21c9Bb73c8B4a296cC256C0cDe324dB146DF)

[Wallet A](https://etherscan.io/address/0xF00d0e11AcCe1eA37658f428d947C3FFFAeaDe70) returned 0.687995 WETH back to the exploiter through the same [0x Exchange Proxy](https://etherscan.io/address/0xDef1C0ded9bec7F1a1670819833240f027b25EfF) in that [same transaction](https://etherscan.io/tx/0x76b70f7c6a9a58388ffa98be0ff2b68f97c05237686693c5cf1c92da29dd713f).

**[NanoJS10's investigation identifies this as a direct operational link](https://github.com/NanoJS10/Zunami-protocol-Investigation-):** The OKX-funded staging wallet was used as a swap intermediary on the day of the attack itself.

Taken together, [the forensic record shows a wallet funded via KYC exchange 143 days in advance](https://github.com/NanoJS10/Zunami-protocol-Investigation-), topped up by a second KYC exchange at the halfway point, and operationally active during the exploit.

**[NanoJS10's assessment](https://github.com/NanoJS10/Zunami-protocol-Investigation-):** Deliberate advance staging using two separate CEX accounts is inconsistent with opportunistic exploitation.

**The blockchain recorded every step. Does this give the appearance that someone planned this?**

*When five months of documented preparation preceded the attack, and the staging wallet connected directly to the exploit on the day, does the forensic picture still fit the word "hack"?*

### Same Playbook

[Four exploits. Four different technical vectors](https://github.com/NanoJS10/Zunami-protocol-Investigation-). One deployer wallet confirmed at the centre of the two largest.

[Before August 2023 became the headline](https://rekt.news/zunami-protocol-rekt), 2023 had [already recorded two incidents Zunami absorbed](https://github.com/NanoJS10/Zunami-protocol-Investigation-), explained, and moved past.

On January 26th, [a routine swap was sandwiched in the mempool](https://zunamiprotocol.medium.com/the-zunami-protocol-has-come-under-two-attacks-e201a8a0ec6c), draining roughly over $49K.

A month later, [price gaps between Zunami's pools became the entry point](https://zunamiprotocol.medium.com/the-zunami-protocol-has-come-under-two-attacks-e201a8a0ec6c). Flash loan attackers minted ZLP tokens at discount prices and cashed out at inflated rates, repeating the cycle across thirteen transactions.

[Zunami's own Medium post](https://zunamiprotocol.medium.com/the-zunami-protocol-has-come-under-two-attacks-e201a8a0ec6c) put the February damage at $260K.

[Two incidents, one month apart](https://github.com/NanoJS10/Zunami-protocol-Investigation-). $309K in losses before the year had found its stride.

**August 13, 2023 was the one that made the record.**

[Flash loans hit zETH and UZD on Curve](https://rekt.news/zunami-protocol-rekt). Both pools depegged, 85% and 99% respectively. The root cause was a flawed LP price calculation in the [totalHoldings function](https://x.com/BlockSecTeam/status/1690931111776358400), where SDT and sdtPrice were artificially inflated via large token swaps, allowing the attacker to drain funds against a manipulated valuation.

[PeckShield confirmed](https://x.com/peckshield/status/1690877589005778945) the price manipulation vector within the hour. [Rekt covered it at the time](https://rekt.news/zunami-protocol-rekt).

Nearly two years of silence followed.

[Then came May 14, 2025](https://rekt.news/zunami-protocol-rekt2). No flash loans. No price manipulation. No complex smart contract vulnerability to exploit. [Just the Zunami Protocol Deployer granting admin roles to two privileged contracts twelve seconds apart](https://github.com/NanoJS10/Zunami-protocol-Investigation-), and an attacker draining both six minutes later.

**Grant Role:**
[0x2697a6f04bb4aff65f9ce2e7a3cac8addeafc52131495ef4d1760316b5aee3b0](https://etherscan.io/tx/0x2697a6f04bb4aff65f9ce2e7a3cac8addeafc52131495ef4d1760316b5aee3b0)

**Zunami Protocol Deployer:**
[0xe9b2B067eE106A6E518fB0552F3296d22b82b32B](https://etherscan.io/address/0xe9b2B067eE106A6E518fB0552F3296d22b82b32B)

**Attack Transaction:** [0xd7ce50992b36acbc746a821a74e5600230cfe5b36cfc155841581e376f4c14d2](https://etherscan.io/tx/0xd7ce50992b36acbc746a821a74e5600230cfe5b36cfc155841581e376f4c14d2)

**2025 Attacker EOA:**
[0x051370419b871F7C05dEE8f7134401530832e250](https://etherscan.io/address/0x051370419b871F7C05dEE8f7134401530832e250)

[296,456 LP tokens transferred clean](https://rekt.news/zunami-protocol-rekt2). No cryptographic puzzle. No complex mechanics. The attacker had admin access and used it.

[Twenty-six Tornado Cash deposits followed](https://github.com/NanoJS10/Zunami-protocol-Investigation-), totaling \~204.2 ETH, completed within thirteen minutes of the drain.

[The same deployer wallet](https://etherscan.io/address/0xe9b2B067eE106A6E518fB0552F3296d22b82b32B) that [sent a settlement message to the 2023 attacker](https://etherscan.io/tx/0x91b41d5b5b30a941c65d5da952c4b11390f364b41cf81a1a87fba9b67b69fe22) three days after that hack, [later granted admin roles](https://rekt.news/zunami-protocol-rekt2) to the [2025 attacker's contracts](https://github.com/NanoJS10/Zunami-protocol-Investigation-).

**[Zunami Founder Sterx surfaced two weeks after the May 2025 exploit with studied ambiguity](https://x.com/kirill_zunami/status/1928131508117651725):** "We're investigating the exploit and considering both scenarios: a compromised deployer or malicious intent by the key holder."

[That was his last public post](https://x.com/kirill_zunami/status/1928131508117651725), he has not posted anything since.

**In Zunami's Discord server, [documented as part of Rekt's investigation at the time](https://rekt.news/zunami-protocol-rekt2), [Zunami’s CTO Mikhail Zelenin](https://x.com/MikhailZelenin) at the time, offered [a more cinematic explanation](https://rekt.news/zunami-protocol-rekt2). His laptop had been seized at a Russian border crossing, held for many hours, with all protocol source code stored on it without cryptographic protection.**

**[His working hypothesis](https://rekt.news/zunami-protocol-rekt2):** Cloned hard drive.

[He also acknowledged the protocol strategies had never been transferred to DAO control as the team had promised](https://rekt.news/zunami-protocol-rekt2), citing developer burnout and absent investment. ["I was the only developer," he said. "I made simple mistakes."](https://rekt.news/zunami-protocol-rekt2)

At least one Discord member was less measured. ["You're either a thief or completely incompetent and responsible for the protocol getting hacked three times."](https://rekt.news/zunami-protocol-rekt2)

[Four exploits with four explanations](https://github.com/NanoJS10/Zunami-protocol-Investigation-). The deployer wallet at the center of the story.

[When the same address links the 2023 attacker and the 2025 admin role grant](https://github.com/NanoJS10/Zunami-protocol-Investigation-), coincidence stops being an explanation and starts looking like a script.

*If the pattern is the argument, what does the money trail say?*

### Almost Every Road Leads to KYC

*For most coverage, Tornado Cash was where the trail ended. It wasn't.*

**After [the August 2023](https://rekt.news/zunami-protocol-rekt2) exploit, [the attacker EOA](https://etherscan.io/address/0x5f4C21c9Bb73c8B4a296cC256C0cDe324dB146DF) made [35 rapid Tornado Cash deposits](https://github.com/NanoJS10/Zunami-protocol-Investigation-).**

Most post-mortems stop here. The funds go dark, the trail goes cold, and the story ends.

[The MetaSleuth flow map shows a fund-flow architecture](https://github.com/NanoJS10/Zunami-protocol-Investigation-/blob/main/metasleuth_full_exploiter_map.png) that ran for nearly two years, tracing stolen funds from the exploit wallet through multiple intermediate wallets and DEX routing layers before surfacing at centralized exchanges under KYC.

Follow [Wallet B](https://etherscan.io/address/0x12e98c4EBD742ca9465789570e5cf4Df9EEd0Fb0) long enough and it leads to Coinbase.

**[The first documented transfer](https://github.com/NanoJS10/Zunami-protocol-Investigation-):** November 10, 2023.

**Wallet B:**

[0x12e98c4EBD742ca9465789570e5cf4Df9EEd0Fb0](https://etherscan.io/address/0x12e98c4EBD742ca9465789570e5cf4Df9EEd0Fb0)

**Wallet B to Coinbase (21.354 ETH, 2023-11-10 23:39:11 UTC):** [0x9e323610282c86c356be8792b864f820e86b6cc3ea2cf42ab4eeb7927d98c6e1](https://etherscan.io/tx/0x9e323610282c86c356be8792b864f820e86b6cc3ea2cf42ab4eeb7927d98c6e1)

**Receiving Coinbase Deposit Address:**

[0x10e3d0699b2eFa3Af238B88bbFEecc971BcCbf83](https://etherscan.io/address/0x10e3d0699b2efa3af238b88bbfeecc971bccbf83)

It wasn't the last stop either.

**Five more cashout sequences followed, spanning February 2024 to October 2025.**

**Each follows the same pattern:**  [Wallet B](https://etherscan.io/address/0x12e98c4EBD742ca9465789570e5cf4Df9EEd0Fb0) to an intermediary wallet, then immediately to a Coinbase deposit address.

**16.961 ETH, 2024-02-08:** [0x2aee51b7fd22c6979db0010fd9a3835bafc2d5a3efeefb1f611e71105a74fe44](https://etherscan.io/tx/0x2aee51b7fd22c6979db0010fd9a3835bafc2d5a3efeefb1f611e71105a74fe44)

**Intermediary Wallet:**
[0x119bDFB802f7723bCDEc281e6BEc12F1A2A9F231](https://etherscan.io/address/0x119bdfb802f7723bcdec281e6bec12f1a2a9f231)

**Coinbase Deposit Address:**
[0x77696bb39917C91A0c3908D577d5e322095425cA](https://etherscan.io/address/0x77696bb39917C91A0c3908D577d5e322095425cA)

**7.461 ETH, 2024-03-25:** [0xabb8c57d57f5b30dd4ecb3ac451b9a3eb13ca72431835c158d8f4a36ecfada0c](https://etherscan.io/tx/0xabb8c57d57f5b30dd4ecb3ac451b9a3eb13ca72431835c158d8f4a36ecfada0c)

**Intermediary Wallet:**
[0x2ad9a351b98Fd39C30DDb52D37415D0f01eF5D00](https://etherscan.io/address/0x2ad9a351b98fd39c30ddb52d37415d0f01ef5d00)

**Coinbase Deposit Address:**
[0x95A9bd206aE52C4BA8EecFc93d18EACDd41C88CC](https://etherscan.io/address/0x95A9bd206aE52C4BA8EecFc93d18EACDd41C88CC)

**23.291 ETH, 2024-07-11:** [0xff527b48e6eb4469af56cf1bb0eaba0d767720d928f015e1cdd1049ef1b91aaa](https://etherscan.io/tx/0xff527b48e6eb4469af56cf1bb0eaba0d767720d928f015e1cdd1049ef1b91aaa)

**Intermediary Wallet:**
[0x2A06c43A6f9805739893C0553A0fa8A062F5B22D](https://etherscan.io/address/0x2a06c43a6f9805739893c0553a0fa8a062f5b22d)

**Coinbase Deposit Address:**
[0xA9D1e08C7793af67e9d92fe308d5697FB81d3E43](https://etherscan.io/address/0xA9D1e08C7793af67e9d92fe308d5697FB81d3E43)

**4.39 ETH, 2025-03-11:** [0xbd1907140754f805acf15daf8dfcb6ae740dca53b8af2ea63ef0eb285c55f2f5](https://etherscan.io/tx/0xbd1907140754f805acf15daf8dfcb6ae740dca53b8af2ea63ef0eb285c55f2f5)

**Intermediary Wallet:**
[0x62ADe071746Cb288Ece3022F89ABd0df5Af53322](https://etherscan.io/address/0x62ade071746cb288ece3022f89abd0df5af53322)

**Coinbase Deposit Address:**
[0xb5d85CBf7cB3EE0D56b3bB207D5Fc4B82f43F511](https://etherscan.io/address/0xb5d85CBf7cB3EE0D56b3bB207D5Fc4B82f43F511)

**1.773 ETH, 2025-10-05:** [0x8a77cd859d68d93206e58e5e5a06b735853b4cb14cbe1a757189caaeb5fc435b](https://etherscan.io/tx/0x8a77cd859d68d93206e58e5e5a06b735853b4cb14cbe1a757189caaeb5fc435b)

**Intermediary Wallet:**
[0xd7ED915293dC004851f5738A080eD4e22da04293](https://etherscan.io/address/0xd7ed915293dc004851f5738a080ed4e22da04293)

**Coinbase Deposit Address:**
[0xb5d85CBf7cB3EE0D56b3bB207D5Fc4B82f43F511](https://etherscan.io/address/0xb5d85CBf7cB3EE0D56b3bB207D5Fc4B82f43F511)

**[Total](https://github.com/NanoJS10/Zunami-protocol-Investigation-):** \~75.2 ETH. Six alleged cashout sequences, spanning nearly two years.

[The sterx.eth wallet](https://etherscan.io/address/0xF9605D8c4c987d7Cb32D0d11FbCb8EeeB1B22D5d) carries its own exchange trail.

**Two transfers arrived from Binance hot wallets to sterx.eth on the same day in August 2020 - years before the exploits, years before the staging chain.**

*If control of sterx.eth remained consistent, those transfers could place Binance’s identity records at the wallet’s earliest known activity.*

**Binance to sterx.eth (4.995 ETH, 2020-08-22):**  [0x4694566855ce96809a9266d9cfa64e30fea5843234089c84771757b8843e1d29](https://etherscan.io/tx/0x4694566855ce96809a9266d9cfa64e30fea5843234089c84771757b8843e1d29)

**Binance to sterx.eth (12.71 ETH, 2020-08-22):**  [0xf46c03f33110ad986dd9ee3d9ab1ff274933d17710c736cfcbb5ee9664cf3fd0](https://etherscan.io/tx/0xf46c03f33110ad986dd9ee3d9ab1ff274933d17710c736cfcbb5ee9664cf3fd0)

OKX holds identity records tied to the pre-exploit staging wallet, funded on day one of the 143-day chain.

**OKX to Staging Wallet A (15.999 ETH, 2023-03-23):** [0x1b315017748bf8b7aca7d58771e172e88a5d9b08a972f8f7027dc7014433b5cb](https://etherscan.io/tx/0x1b315017748bf8b7aca7d58771e172e88a5d9b08a972f8f7027dc7014433b5cb)

By May 2, 2026, [sterx.eth](https://etherscan.io/address/0xF9605D8c4c987d7Cb32D0d11FbCb8EeeB1B22D5d) was depositing to a ByBit address that also received 25.2 ETH routed through [zunamiteam.eth](https://etherscan.io/address/0xb056b9a45f09b006ec7a69770a65339586231a34) in two transactions during the pre-exploit staging period.

*Both transactions were initiated by sterx.eth via a Safe multisig, with zunamiteam.eth forwarding the ETH to the ByBit deposit address.*

**If the same operator controlled both wallets, that would place the deployer cluster and the personal wallet on the same ByBit account path.**

**ByBit Deposit Address:**
[0xA7b7Bc3fC962614d51553829717D6e1884458039](https://etherscan.io/address/0xA7b7Bc3fC962614d51553829717D6e1884458039)

**sterx.eth via zunamiteam.eth to ByBit Deposit (22.2 ETH - 2024-05-07):** [0x1f409282738219c7031ebfb679a7a956d162e591f4b5165960541da37c4fda07](https://etherscan.io/tx/0x1f409282738219c7031ebfb679a7a956d162e591f4b5165960541da37c4fda07)

**sterx.eth via zunamiteam.eth to ByBit Deposit (3 ETH- 2024-05-07):** [0x5cc7b5d25c652bea32cb731c1b6098d3ceda673171c3afe27c2334adac8217b3](https://etherscan.io/tx/0x5cc7b5d25c652bea32cb731c1b6098d3ceda673171c3afe27c2334adac8217b3)

**sterx.eth to ByBit Deposit (Active as of May 2, 2026):** [0x456189d606fcade0a47221ec3e054c655d3134c3be0f0caff8843faa5512881d](https://etherscan.io/tx/0x456189d606fcade0a47221ec3e054c655d3134c3be0f0caff8843faa5512881d)

ByBit could tie that deposit address to an account holder through its own records.

[The obfuscation didn't stop with the original attack](https://github.com/NanoJS10/Zunami-protocol-Investigation-). In December 2025, sterx.eth called the Tornado Cash L1 Helper register function, a preparatory step for using Tornado Cash's privacy infrastructure, more than two years after the August 2023 exploit.

**sterx.eth Tornado Cash L1 Helper Registration (December 2025):** [0xbf03b63adb606901a3d6db1b7b47ba17682267cd7468f510a87c5ca18a01ef8a](https://etherscan.io/tx/0xbf03b63adb606901a3d6db1b7b47ba17682267cd7468f510a87c5ca18a01ef8a)

Someone setting up Tornado Cash infrastructure in late 2025, long after the last known exploit, is not acting like the story is over.

**[NanoJS10's investigation maps deposits through four exchanges with KYC records linked to this chain](https://github.com/NanoJS10/Zunami-protocol-Investigation-):** Binance, OKX, Coinbase, and ByBit. All accessible via formal legal process.

The [Zunami Deployer](https://etherscan.io/address/0xe9b2B067eE106A6E518fB0552F3296d22b82b32B) was [last active April 26, 2026](https://etherscan.io/tx/0xb04598c196fcb89db1851d251f528e0450ce02360c6a34b24a79741f43b62d75), transferring SAFE governance tokens from zunamiteam.eth to sterx.eth. [sterx.eth](https://etherscan.io/address/0xF9605D8c4c987d7Cb32D0d11FbCb8EeeB1B22D5d) was [last active May 13, 2026](https://etherscan.io/tx/0xe40779bd6808a7819a9af44811c1b7cc91c0d1ab0eaec3c330c4ab0cd0c0d6fb), depositing to the same ByBit address documented above.

**The money trail doesn't read like aftermath. It reads like infrastructure. The same addresses keep surfacing across every stage of the story.**

*Why route stolen funds through multiple wallets and token conversions only to cash out at a KYC exchange?*

### The Case File

[The forensic package went out on May 16, 2026](https://github.com/NanoJS10/Zunami-protocol-Investigation-): Every identified exchange, plus the FBI IC3 under Case Reference ZNM-NANOJS02-INV.

[Interpol received a separate submission](https://github.com/NanoJS10/Zunami-protocol-Investigation-) the same day.

[ByBit acknowledged receipt](https://github.com/NanoJS10/Zunami-protocol-Investigation-) and directed law enforcement to their dedicated compliance channel.

Coinbase had [a Senior Director personally review the submission](https://github.com/NanoJS10/Zunami-protocol-Investigation-).

**A second email response was confirmed in writing:** “Thank you for providing the additional details regarding the Zunami Protocol exploit proceeds. We are prepared to explain the relevant transactions and provide the requested account data should law enforcement contact us regarding this case. As previously noted, they may request this information via a formal subpoena.”

**Source note:** Coinbase’s second email response was shared with Rekt News via PDF, sent from [NanoJS10](https://x.com/NanoJS10).

[MEXC confirmed a freeze on a related submission by NanoJS10 under the same investigative series](https://github.com/NanoJS10/Zunami-protocol-Investigation-), Ticket #20260507000124, demonstrating that the reporting pipeline works when the forensic package is built correctly.

Binance, OKX, Chainalysis, and TRM Labs submissions [remain pending as of the last update](https://github.com/NanoJS10/Zunami-protocol-Investigation-).

The Zunami Protocol has made no public statement addressing the deployer-to-attacker message. No post-mortem accounts for it. No community discussion has named it until now.

Three weeks after the [May 2025 exploit](https://rekt.news/zunami-protocol-rekt2), [Zunami Founder sterx told users that the team was](https://x.com/kirill_zunami/status/1928131508117651725) “considering both scenarios: a compromised deployer or malicious intent by the key holder.”

[The community moderator in Thailand set a June 13th deadline for meaningful progress](https://rekt.news/zunami-protocol-rekt2), threatening to file a police report himself if the founder didn't respond.

**The deadline passed. The founder's update did not come. Neither [sterx](https://x.com/kirill_zunami) nor the [Zunami Protocol](https://x.com/ZunamiProtocol) account has posted publicly since.**

The wallets, however, have kept moving.

[The deployer](https://etherscan.io/address/0xe9b2B067eE106A6E518fB0552F3296d22b82b32B) was last active [April 26, 2026](https://etherscan.io/tx/0xb04598c196fcb89db1851d251f528e0450ce02360c6a34b24a79741f43b62d75). [sterx.eth](https://etherscan.io/address/0xF9605D8c4c987d7Cb32D0d11FbCb8EeeB1B22D5d) was last active [May 13, 2026](https://etherscan.io/tx/0xe40779bd6808a7819a9af44811c1b7cc91c0d1ab0eaec3c330c4ab0cd0c0d6fb).

[The CTO's explanation](https://rekt.news/zunami-protocol-rekt2), a cloned hard drive at a Russian border crossing, remains his only hypothesis.

*The admin keys were never transferred to DAO control as promised. The protocol strategies were never secured.*

**The full forensic investigation is publicly available as [NanoJS10's Zunami Protocol Investigation](https://github.com/NanoJS10/Zunami-protocol-Investigation-).**

Every transaction hash in this article is independently verifiable on Etherscan.

The on-chain record cannot convict anyone. [What it can do is draw a map](https://github.com/NanoJS10/Zunami-protocol-Investigation-), and this map leads directly to KYC records held at Binance, OKX, Coinbase, and ByBit, with MEXC also active in the broader investigative series.

**All of them can be obtained through formal legal process, with account data accessible by subpoena where jurisdiction and policy allow.**

*When the forensic work is done, the exchanges have responded, and law enforcement filings are on record, what exactly is the investigation waiting for?*

*The blockchain doesn't forget. It doesn't misremember, doesn't issue corrections, doesn't go silent for three weeks while users demand answers.*

**Every transaction in this piece has been sitting on Etherscan since the day it was made, permanent and publicly verifiable, waiting for someone to look in the right direction.**

[NanoJS10 looked further than others](https://github.com/NanoJS10/Zunami-protocol-Investigation-).

**[What he found was a record that had never been read](https://github.com/NanoJS10/Zunami-protocol-Investigation-):** A deployer wallet encoding a settlement offer to an attacker, a 143-day staging chain funded through KYC exchanges, and a cashout architecture that ran for nearly two years before surfacing repeatedly at regulated exchanges under verified identities.

**The forensic work is done. The exchanges have been notified. The filings are active.**

Identity trails sit at Binance, OKX, Coinbase, ByBit, and MEXC, each accessible through a process law enforcement already knows how to use.

This is the first Case File. There will be others.

**If you work in law enforcement and are reading this, the file is built.**

*The wallets are still moving. How long can it sit before someone opens it?*

REKT serves as a public platform for anonymous authors, we take no responsibility for the views or content hosted on REKT.

**donate (ETH / ERC20): [0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C](https://etherscan.io/address/0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C)**

disclaimer:

REKT is not responsible or liable in any manner for any Content posted on our Website or in connection with our Services, whether posted or caused by ANON Author of our Website, or by REKT. Although we provide rules for Anon Author conduct and postings, we do not control and are not responsible for what Anon Author post, transmit or share on our Website or Services, and are not responsible for any offensive, inappropriate, obscene, unlawful or otherwise objectionable content you may encounter on our Website or Services. REKT is not responsible for the conduct, whether online or offline, of any user of our Website or Services.
