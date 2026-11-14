# 🔌 Rekt: Ledger Implants Read Recovery Phrases Off the Screen

- **Source URL:** https://rekt.news/factory-sealed
- **Fetched:** 2026-11-14
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/2224 (id 2224)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Factory Sealed

*Twenty-four words, a ribbon of copper, a thumbnail-sized screen, and a cellular modem nobody ordered, listening in between.*

**On October 9, [wallets tied to devices sold through CryptoBilis](https://www.theblock.co/news/business/2026-10-09-ledger-cryptobilis-fund-losses-418163), an authorized Ledger reseller in Southeast Asia, [started emptying across six chains](https://www.bitquery.io/investigations/ledger-cryptobilis-hack).**

Bitquery's on-chain analysis put the suspected haul at [$102 million across 324 wallets](https://www.bitquery.io/investigations/ledger-cryptobilis-hack), though [Ledger has not verified that figure or the number of affected users](https://x.com/Ledger/status/2109896739985453358).

**[The vault never cracked](https://x.com/Ledger/status/2109896739985453358):** Ledger's Secure Element did what it promised, while a planted board read the seed off the display during setup and phoned it home over LTE.

**Ledger's own threat model [concedes its Genuine Check cannot see added hardware while the original chip stays intact](https://donjon.ledger.com/threat-model/device-genuineness/).**

None of it was new. In August 2025, [a Thai Reddit user flagged suspicious circuitry in a Ledger Nano X](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/); hardware hacker Joe Grand later determined it was an implant and said he briefed Ledger on it in March 2026.

By October, [one of Karpelès’s specimens carried a silk-screened part number with a revision tag](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), and reports had followed the implant into Flex devices, [a reported implant in a German MediaMarkt purchase](https://x.com/Ledger/status/2109984923343782374), and an [airport buy in Singapore](https://x.com/MagicalTux/status/2109916873689280900).

**Somebody appears to have built a supply chain inside the supply chain, [and for over a year much of the closest scrutiny came from independent researchers buying suspect devices through third-party marketplaces](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/).**

*When the packaging, the reseller, and the authenticity check all said genuine, who was left to tell a buyer the truth?*

*Credit:[The Block](https://www.theblock.co/news/business/2026-10-09-ledger-cryptobilis-fund-losses-418163), [Bitquery](https://www.bitquery.io/investigations/ledger-cryptobilis-hack), [Ledger](https://x.com/Ledger/status/2109896739985453358), [Zero Day](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), [Mark Karpelès](https://x.com/MagicalTux/status/2109916873689280900), [Tropicon 2026](https://www.youtube.com/watch?v=e8FWAIuO_l8), [hardwear.io](https://www.youtube.com/watch?v=WNpW52x-EWY), [Grand Idea Studio](https://grandideastudio.com/portfolio/security/ledger-hardware-implant/), [Tibane Labs](https://www.tibane.net/research/ledger-nano-x-implant), [Wentrre](https://x.com/wentrre/status/2109339646102778306), [tanuki42](https://x.com/tanuki42_/status/2108527923766399243), [Specter](https://x.com/SpecterAnalyst/status/2108534068564373687), [YFarmX](https://x.com/YFarmX/status/2109001938704670908), [Arravind Prabu](https://x.com/PrabuArravind/status/2108579734833738143), [cryptonews](https://cryptonews.com/news/ledger-wallet-exploit-implant-cryptobilis-investigation/), [Changpeng Zhao](https://x.com/cz_binance/status/2109395636907032838), [Ben Yorke](https://x.com/BenYorke/status/2109083315424891296), [Johannes](https://x.com/0xJohannes_/status/2109285908079915305), [CoinTelegraph](https://cointelegraph.com/news/ledger-cellular-implants-wallets-sold-cryptobilis), [Danny Sanders](https://x.com/Trezor/status/2110000774314873020), [Karpelès Lab](https://karpeleslab.github.io/ledger_implant_osint/)*

**August 2025. [A Reddit user in Thailand bought a Ledger Nano X from an online marketplace](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), cracked open the case, and found extra circuitry that had no business being there.**

[He sent the device to Joe Grand](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), a hardware hacker who had heard rumors of wallet implants for years but had never seen one in the wild.

[Grand found an extra board, an antenna](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), an LTE module, and an eSIM.

The implant waited for setup, [copied each character of the recovery phrase as the wallet sent it to the screen](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), then used the LTE module, antenna, and eSIM to connect to a nearby cell tower and transmit it.

*By Grand's account, [he ordered eight more Nano X units from Lazada sellers shipping out of Thailand](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), and four came back implanted.*

[On March 4, 2026, Grand says, he reported the findings to Ledger and had a Zoom call with a team there](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/). He says Ledger told him it would investigate who was behind the implants, but that he received no follow-up on the investigation until he asked months later.

**[The answer, as he tells it](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/):** Ledger had found no evidence anyone was using the implants to steal crypto.

Grand kept going. [He presented the teardown at Tropicon in April](https://www.youtube.com/watch?v=e8FWAIuO_l8) and [hardwear.io USA in May](https://www.youtube.com/watch?v=WNpW52x-EWY), then [posted the slides](https://grandideastudio.com/media/ledger_hardware_implant_slides.pdf) and the [implant's extracted firmware online](https://grandideastudio.com/media/ledger_hardware_implant_fw.zip).

[Conversations moved into a Signal group with Ledger technical staff and a Japan-based researcher](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/) who had found implants in wallets of his own.

**In September, [Mark Karpelès came across Grand’s research, obtained two Ledger wallets, and found implants in both](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/). Each held a newer, cleaner version of the same idea, [which he documented on Tibane Labs’ research page](https://www.tibane.net/research/ledger-nano-x-implant) and [discussed on Twitter](https://x.com/MagicalTux/status/2108651005617607082).**

*The teardown and firmware were public by May. Who else was taking notes, and what did Ledger do with the warning?*

### Bill of Materials

*Grand's unit looked like a prototype. [A bundle of hand-soldered wires ran from the extra board to the screen](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), obvious to anyone who opened the case.*

**The next specimens looked like nobody's weekend project.**

[One Nano X Karpelès analyzed carried a custom polyimide flex circuit laminated flat across the back of Ledger’s own board and soldered at select points](https://www.tibane.net/research/ledger-nano-x-implant), so no loose wires showed. Under the battery and antenna sat an ST STM32G431KBU6 microcontroller, a 2×2 mm eSIM, and a shielded LTE module, with a smaller replacement battery making room.

Markings [suggested assembly no earlier than late December 2025](https://www.tibane.net/research/ledger-nano-x-implant).

Another unit, [shipped from Malaysia by a China-based seller on Amazon Japan](https://www.tibane.net/research/ledger-nano-x-implant), arrived [at half price](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/). Inside, [the flex circuit had been coated black to match the main board, and the part markings scraped off](https://www.tibane.net/research/ledger-nano-x-implant).

*The original battery stayed put, [and the implant filled the space where foam padding normally cushions the screen](https://www.tibane.net/research/ledger-nano-x-implant). A Nordic nRF9151 modem handled communications.*

**The only giveaway was a thin black antenna along the top edge, [and someone had silk-screened a part number onto it](https://www.tibane.net/research/ledger-nano-x-implant):** AC-A2016-NANO-V1.1.

Karpelès read the label as a deliberate product designation. NANO appeared to name the target, he argued, and V1.1 suggested at least one revision had come before it. [“That is a production run, not a one-off,”](https://www.tibane.net/research/ledger-nano-x-implant) he wrote.

[Tibane’s research noted the flex board was panelized](https://www.tibane.net/research/ledger-nano-x-implant), the kind of board a commercial fabrication house turns out, not a hand-built one-off.

[The Japan-based researcher bought ten Nano X units from unauthorized sellers](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), mostly through Amazon Japan, and found implants in every one, spread across five different layouts.

**Around July or August, he says, [the listings he watched switched from Nano X to Flex](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), and the two Flex units he bought were implanted too.**

[Photos of a Ledger Stax with a hidden LTE modem surfaced on Twitter](https://x.com/wentrre/status/2109339646102778306) in October; [nobody has independently confirmed them](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/).

None of it trips Ledger’s Genuine Check. The company’s own threat model says the test [authenticates the Secure Element and cannot detect added hardware sitting beside it](https://donjon.ledger.com/threat-model/device-genuineness/).

[Karpelès says his black-coated unit arrived in a flawless shrink-wrapped box from Malaysia](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/) and [passed Ledger’s Genuine Check](https://x.com/MagicalTux/status/2108585908077568277).

*A hobbyist builds one and moves on. What kind of operation pays for a second revision?*

### Forty-Seven Minutes

*The heist started with a withdrawal slip.*

[On September 24, 14,512 TRX left Bybit and landed in a wallet that funded the thief’s TRON address](https://www.bitquery.io/investigations/ledger-cryptobilis-hack) the next day.

**Bybit withdrawal transaction:**

[b284a2542afed3f5e00a4f9370cae1a9675b94c29967d49d8c45819cb1d7686e](https://tronscan.org/transaction/b284a2542afed3f5e00a4f9370cae1a9675b94c29967d49d8c45819cb1d7686e/overview)

**Receiving wallet that funded the TRON control address:**

[TWGHw7ZsDdXaP6Jw3vJgJ35FHKUvetBf3E](https://tronscan.org/address/TWGHw7ZsDdXaP6Jw3vJgJ35FHKUvetBf3E/transactions)

[Three minutes before that TRON address got its first funds](https://www.bitquery.io/investigations/ledger-cryptobilis-hack), the Ethereum control address got its own.

**Ethereum control address:**

[0x381825deb972b3d0a031a9ce86902ac8b22df8f2](https://etherscan.io/address/0x381825deb972B3d0a031A9ce86902AC8b22Df8F2)

**Then came the dress rehearsal. [Over two weeks, the two control addresses ran 41 test loops, 21 on TRON and 20 on Ethereum](https://www.bitquery.io/investigations/ledger-cryptobilis-hack):** Send a wallet a few dollars and some gas, have it sign an approval, pull the dollars back.

**The [last two ran 23 seconds apart on October 7](https://www.bitquery.io/investigations/ledger-cryptobilis-hack).**

[October 9, 04:59:57 UTC. Thirty TRON wallets added the same new key](https://www.bitquery.io/investigations/ledger-cryptobilis-hack), weighted to move funds on its own.

**Key added to 30 TRON wallets:**

[TEqZsE39aNXRnuTwrXJ9ooWMc87puuZxpK](https://tronscan.org/address/TEqZsE39aNXRnuTwrXJ9ooWMc87puuZxpK/permissions)

Only a wallet’s own key can make that change, [so whoever made it already held all thirty](https://www.bitquery.io/investigations/ledger-cryptobilis-hack). The owners were locked out of their money and didn’t know it yet.

*Eight minutes later, the pull began. [Thirteen TRON wallets signed the same approval in one block, twelve more in the next](https://www.bitquery.io/investigations/ledger-cryptobilis-hack), and [$29 million in USDT was gone within six seconds](https://www.bitquery.io/investigations/ledger-cryptobilis-hack) of the first signature.*

**At 05:54 UTC, [111 Bitcoin wallets emptied in a single block](https://www.bitquery.io/investigations/ledger-cryptobilis-hack).**

Inside 47 minutes, [the thief had hit TRON, Ethereum, BNB Chain, Polygon, Solana, and Bitcoin](https://www.bitquery.io/investigations/ledger-cryptobilis-hack).

**[Bitquery weighed a phishing explanation and rated it unlikely](https://www.bitquery.io/investigations/ledger-cryptobilis-hack):** The choreography belonged to software already holding every key.

Researchers [tanuki42](https://x.com/tanuki42_/status/2108527923766399243) and [Specter](https://x.com/SpecterAnalyst/status/2108534068564373687) posted the drain addresses around noon UTC, and [Tether started blocking addresses about ten minutes after the first public post](https://www.bitquery.io/investigations/ledger-cryptobilis-hack). It blocked 37 in all and froze $10 million sitting in 20 of them.

*The thief had already parked [23.7 million USDT in USDD](https://www.bitquery.io/investigations/ledger-cryptobilis-hack), a stablecoin Tether cannot freeze, and over the following days pushed [26.9 million USDT through THORChain for 10,636 ETH](https://www.bitquery.io/investigations/ledger-cryptobilis-hack).*

**About [6,840 ETH went through Tornado Cash over five days](https://www.bitquery.io/investigations/ledger-cryptobilis-hack), with much of it continuing through Zcash. [Bitquery](https://www.bitquery.io/investigations/ledger-cryptobilis-hack) and analyst [YFarmX](https://x.com/YFarmX/status/2109001938704670908) matched [39 of the 41 Zcash lots](https://www.bitquery.io/investigations/ledger-cryptobilis-hack), down to the smallest unit.**

The news didn’t stop the drains. [At 20:49 UTC on October 9th, nine more TRON wallets lost 8.8 million USDT](https://www.bitquery.io/investigations/ledger-cryptobilis-hack).

The next afternoon, [a victim’s regular payer sent 70,000 USDT to an already-emptied wallet](https://www.bitquery.io/investigations/ledger-cryptobilis-hack), and the thief took it ten minutes later using the previous day’s approval.

[The 203.8 BTC had not moved as of Bitquery’s October 13](https://www.bitquery.io/investigations/ledger-cryptobilis-hack) analysis.

Karpelès had [started posting about the implants on Twitter the day before the drain](https://x.com/MagicalTux/status/2108095743525625998), and [Kim Zetter from Zero Day suggests the attention may have pushed the thief to cash out early](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/).

**One actor held the keys to every drained wallet.**

*Who had access to the devices before they reached their owners?*

### Change of Ownership

*CryptoBilis carried an unrelated complication of its own, and it surfaced only after the drains became public.*

**On October 9, [co-founder Arravind Prabu posted that CryptoBilis had been acquired earlier in the year](https://x.com/PrabuArravind/status/2108579734833738143) and that he and his co-founder had [“fully stepped down from all operations, system access, and management.”](https://x.com/PrabuArravind/status/2108579734833738143)**

[In a longer statement reproduced by Kim Zetter from Zero Day](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), Prabu and co-founder Vimalatheethan said the handover was completed in March of 2026 and that they have since had zero access, credentials, visibility, or administrative control over CryptoBilis systems, customer data, or order histories.

The acquisition agreement, Prabu wrote, [barred every party from announcing the deal until mid-October 2026](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/). He added that all suppliers had been told about the new management.

He did not name the buyer. Questions, he said, should go to [Nicholas Chang, whom older posts describe as CryptoBilis’s marketing director](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/). Chang did not respond to an inquiry from Zero Day.

**[Corporate filings reported by the Philippine outlet BitPinas fill part of the gap](https://cryptonews.com/news/ledger-wallet-exploit-implant-cryptobilis-investigation/):** 100% of CryptoBilis shares moved on August 3, 2026, to an individual listed as “Jiaming,” with a registered address in Heilongjiang, China.

[Binance co-founder Changpeng Zhao alleged that hackers had bought the reseller](https://x.com/cz_binance/status/2109395636907032838), an allegation for which no public evidence has been published.

[Nobody has tied the new owner, the founders, or anyone at CryptoBilis to the implants](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/) or the drain.

The ownership trail also cannot carry the whole story, because the timeline does not fit it.

[Grand’s Thai implants surfaced in August 2025](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), seven months before the handover.

*The specimens from Japan, Thailand, Singapore, and Germany came through [Lazada storefronts, Amazon sellers](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), an [airport retailer in Singapore](https://x.com/BenYorke/status/2109083315424891296), and [MediaMarkt](https://x.com/0xJohannes_/status/2109285908079915305), not CryptoBilis.*

**What keeps recurring is geography. [Karpelès’s black-coated unit shipped from Malaysia](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), where CryptoBilis is based.**

[The Japan-based researcher’s devices arrived from Malaysia, Thailand, and an Osaka shipping hub](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), the last listing a seller address at a house he says serves as the registered address for numerous companies.

[CryptoBilis has since suspended every hardware wallet brand it sells across Malaysia](https://cointelegraph.com/news/ledger-cellular-implants-wallets-sold-cryptobilis), the Philippines, and Indonesia, closed its physical stores, and brought in outside specialists to review its processes.

**One storefront went dark.**

*Who was still on the receiving end of the implants?*

### Phone Home

*Every implant has to report somewhere, and that is where the trail gets colder and stranger.*

[The most detailed answer comes from a single source](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/): The Japan-based researcher, who asked Zero Day not to name him. He pulled data from the implants in his own devices and says two things leak out of them.

The first is location. [The planted eSIMs work in any country, and an uninitialized one still remembers the last cell tower it touched](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/). Reading those records from his unused wallets, he says, pointed to what he believes are manufacturing hubs. He has not named them publicly.

The second is the destination. Data in the implant firmware, he says, points to [command-and-control servers in a Hong Kong data center managed by Alibaba](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/).

*By his count, [at least 90 implanted Ledgers were sending seed phrases to those servers in June](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), and he believes the real number is higher. That was roughly four months before the first wallet was drained.*

**None of it has been independently verified. [He could not say whether the same group was behind every design or whether different actors took inspiration from an original design and advanced it.](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/)**

**[Karpelès has a theory that fits the evidence without proving it](https://x.com/MagicalTux/status/2109701581780459742):** The implant is itself a product, with its production lines and a manual sold to someone else, who is installing these on ledgers prior to sale.

**[Grand calls the technique hardware espionage](https://grandideastudio.com/portfolio/security/ledger-hardware-implant/), and the label fits the tradecraft:** Covert hardware, concealment, a beacon, and a listening post. The motive, as far as the chain shows, was money.

**The tradecraft looked like espionage and the payout looked like theft.**

*Who was supposed to be guarding the shelf?*

### Authorized Channels

**For years the advice never changed:** Buy from the manufacturer or an authorized reseller.

[CryptoBilis was authorized](https://www.theblock.co/news/business/2026-10-09-ledger-cryptobilis-fund-losses-418163). So was [MediaMarkt](https://shop.ledger.com/pages/resellers?continent=europe&country=austria).

**[Johannes said the Ledger incident was not limited to Asia](https://x.com/0xJohannes_/status/2109240472933671125):** Highlighting a device bought from an official reseller in Europe, and found a spy implant that should not be there.

In a follow-up, [he identified the seller as MediaMarkt](https://x.com/0xJohannes_/status/2109285908079915305).

[Zero Day reports that the purchase was at a German MediaMarkt in August](https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/), that Johannes opened the device only after the drain became news, and that he then bought a second unit at another branch and found an implant in that one too.

[A MediaMarkt employee told him the device he purchased was not a return,](https://x.com/0xJohannes_/status/2109634513957527974) and that returned Ledgers are sent directly back to the manufacturer rather than resold.

**On October 11, [Ledger had reminded resellers to source only through authorized channels and never restock returns](https://x.com/Ledger/status/2109331538072494364).**

On October 13, [MediaMarkt Saturn pulled every Ledger product from its stores and website, with Ledger's agreement](https://x.com/Ledger/status/2109984923343782374), after one customer report and no reported losses, according to Ledger.

The same day, [Ledger asked resellers in Indonesia, Singapore, Thailand, the Philippines, Vietnam, Malaysia and Hong Kong to suspend sales of Ledger devices and take the products off the shelves](https://x.com/Ledger/status/2110129361382994076), while stressing it [had not verified a drain tied to a device bought outside CryptoBilis](https://x.com/Ledger/status/2109896739985453358).

Trezor moved too, [telling an undisclosed number of resellers their authorization ends January 1, 2027](https://x.com/Dantoshi/status/2110000117856248141).

[Chief Commercial Officer Danny Sanders said there was "not a single piece of evidence"](https://x.com/Trezor/status/2110000774314873020) that Trezor devices had been compromised.

[Grand wrote to Trezor on August 10 about a Model T that someone else had bought through Facebook Marketplace in Canada in 2025](https://www.zetter-zeroday.com/trezor-wallets-also-compromised-with-implants/). Its microcontroller had been swapped for one that generated one of roughly a dozen attacker-known seed phrases rather than a random one.

[Trezor replied within three days and, in September, asked for a heads-up before he published](https://www.zetter-zeroday.com/trezor-wallets-also-compromised-with-implants/). Both units came from unauthorized sellers, so Trezor's denial holds only if "compromised" excludes hardware tampered with after it left official channels.

**[A public tracker assembled by Mark Karpelès now offers readers a partial map of the problem](https://karpeleslab.github.io/ledger_implant_osint/):** 15 devices from nine named sellers, ranging from a CryptoBilis Stax and MediaMarkt Nano X units to devices bought through Lazada, Amazon Japan, Yahoo! Flea Market, JD.com, a Russian marketplace, and Singapore retailers, including one at the airport.

[Most are Ledger devices with an added circuit carrying its own antenna](https://karpeleslab.github.io/ledger_implant_osint/), added after they left the factory, and on the units examined in detail, that circuit reads the recovery phrase off the screen; others are counterfeits with no secure element.

[The list covers only publicly reported cases](https://karpeleslab.github.io/ledger_implant_osint/report/2026-10-13-coinjoined-nano-x/), and one MediaMarkt purchase is still pending examination, but it gives buyers somewhere to check whether their seller or model has already appeared.

Even the warning window lagged. [Ledger’s first notice covered only CryptoBilis buyers from the previous 90 days](https://x.com/Ledger_Support/status/2108551100613714002), but [Bitquery found more than eight in ten victim wallets were first funded from June onward, before that window began](https://www.bitquery.io/investigations/ledger-cryptobilis-hack).

**By then, the word “authorized” had already failed more than once.**

*If authorized means a name on a list, what exactly were buyers paying for?*

*Was self-custody a ruse?*

**Not quite. But not your keys, not your crypto always assumed the enemy was a custodian.**

**This attack suggests another:** Not your hardware, not your keys either.

The cryptography held. [The keys never left the chip.](https://x.com/Ledger/status/2109896739985453358)

**But the words that could recreate them [slipped out through the screen](https://x.com/Ledger/status/2109896739985453358), the one surface built to be read by a human.**

Self-custody did not fail because the math broke. It failed because trust was outsourced: to a sealed box, a familiar logo, an authorized name, a supply chain.

Each one became another man in the middle.

**The lesson is not that self-custody is worthless. It is that self-custody is only as strong as the least trustworthy link between the factory and your hands.**

*If you didn’t seal it, ship it, or open it yourself, whose wallet is it really?*

REKT serves as a public platform for anonymous authors, we take no responsibility for the views or content hosted on REKT.

**donate (ETH / ERC20): [0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C](https://etherscan.io/address/0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C)**

disclaimer:

REKT is not responsible or liable in any manner for any Content posted on our Website or in connection with our Services, whether posted or caused by ANON Author of our Website, or by REKT. Although we provide rules for Anon Author conduct and postings, we do not control and are not responsible for what Anon Author post, transmit or share on our Website or Services, and are not responsible for any offensive, inappropriate, obscene, unlawful or otherwise objectionable content you may encounter on our Website or Services. REKT is not responsible for the conduct, whether online or offline, of any user of our Website or Services.
