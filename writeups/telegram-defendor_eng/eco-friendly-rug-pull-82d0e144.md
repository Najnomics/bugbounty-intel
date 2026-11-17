# 🌿 Green scam Rowan Energy: clean energy or fraud?

- **Source URL:** https://rekt.news/eco-friendly-rug-pull
- **Fetched:** 2026-11-17
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/276 (id 276)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The Eco-Friendly Rug Pull

*Clean energy meets crypto innovation - or so the marketing promised.*

**Rowan Energy pitched a revolution: carbon-neutral mining, clean energy rewards, and sustainable profits for the eco-conscious crypto crowd.**

But behind the slick branding and "SmartMiner" hardware lay a five-year fraud run by serial scammer David Duckworth - complete with a hidden mint function and 400 million ghost tokens.

A curious researcher blew it open, reverse-engineering their so-called "private" blockchain through exposed RPC endpoints, [minting a billion tokens as proof, then burning them to leave a trail](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A).

Meanwhile, thousands of investors watched their funds vanish as Duckworth spent 69 days gaslighting the community before disappearing with tens of millions.

**Turns out the only thing Rowan Energy ever mined was their investors’ bank accounts.**

*When your clean energy company runs the dirtiest token scheme imaginable - who’s really being sustainable?*

*Credit:[Anonymous Researcher 1](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A), [Anonymous Researcher 2](https://mirror.xyz/0xC246f0cCc7a9f153C041bb1eF8A4d20bB1155187/jM18CQhT9xKRNw8Mp_fQNo4WBwEPmtnJQRnID89lFYI), [PropertyTribes](https://www.propertytribes.com/david-duckworth-gone-missing-t-3687-1.html), [TrustPilot](https://uk.trustpilot.com/review/rowanenergy.com) (Rowan Energy’s Page), [Connor Quinn](https://www.linkedin.com/posts/conor-quinn-02a24821b_rowan-energy-is-rated-average-with-29-activity-7343946045644582912-bLrd), [Victim Telegram](https://t.me/Rowanenergyunofficial), [Newbury Today](https://www.newburytoday.co.uk/news/solar-panel-firm-ese-group-convicted-of-deceiving-customers-9305357/), [Decrypt](https://decrypt.co/216485/rowan-energy-and-ese-solar-unite-to-drive-decentralised-energy-adoption)*

**Crypto's green revolution has attracted every flavor of grifter, but few have perfected the art quite like David Duckworth.**

Rowan Energy's pitch sounded almost too good to question: "tokenized Renewable Energy Certificates and tokenized peer-to-peer energy trading" that would revolutionize home solar.

Their private blockchain would track actual energy output from thousands of SmartMiner devices installed in homes across the UK, [paying owners £450 annually](https://www.linkedin.com/posts/conor-quinn-02a24821b_rowan-energy-is-rated-average-with-29-activity-7343946045644582912-bLrd) for their carbon-negative contribution to the network.

[The whitepaper promised](https://rowanblockchain.com/wp-content/uploads/2024/06/RowanEnergy-Concept-document-1.pdf) "services in the home renewable energy markets not previously available... providing a better ROI for those active participants in renewable energy."

*Marketing materials sparkled with buzzwords - sustainable mining, carbon credits, eco-friendly consensus mechanisms.*

[Professional exchange listings on MEXC and ProBit](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A) gave the project legitimacy, while slick YouTube videos showed David Duckworth touring solar installations and explaining the revolutionary technology.

But something stank beneath the green veneer.

Solar installers across the UK [started refusing Rowan partnerships](https://www.linkedin.com/posts/conor-quinn-02a24821b_rowan-energy-is-rated-average-with-29-activity-7343946045644582912-bLrd).

The promised "energy generation proofs" never materialized on-chain.

Most damning of all, the tokenomics looked suspiciously familiar to anyone who'd seen a basic ERC-20 contract - except this one lived behind the closed doors of a "private blockchain for security."

**Private blockchains in crypto are like gated communities in Detroit - usually there's a reason they don't want you looking around.**

*But what happens when someone finds the key to the gate?*

### Private Blockchain, Public Humiliation

*An anonymous researcher stumbled into Rowan's dirty secret through pure accident - and a poorly secured wallet app.*

**Users had been complaining that [the official Rowan wallet was transmitting their seed phrases over HTTPS](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A) instead of signing transactions locally.**

Even [AnkerPay, their alternative wallet solution, was leaking RPC endpoints](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A) to anyone running network analysis tools.

But this security flaw became the thread that unraveled everything.

Curious about the wallet's architecture, the researcher fired up network analysis tools and watched the mobile app's traffic.

*Instead of seeing encrypted local signing, [packets were flowing to a publicly exposed RPC endpoint: 3.19.248.157:8504](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A).*

**A private blockchain with public access? Amateur hour.**

Standard Ethereum RPC calls worked perfectly against Rowan's supposedly proprietary network.

A [simple totalSupply() query revealed the first smoking gun](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A): 945,000,010 tokens in circulation.

Not the 545 million claimed by [David Duckworth himself in Telegram](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A): "The maximum total supply of RWN token is now 545 million with approx 139 million in circulation."

*Contract bytecode doesn't lie.*

[After pulling the complete code](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A) from 0x3D3F6CeDe89a048CfC3F6eCEbAccA97684202317 and running it through a decompiler, there it was - sitting pretty among the standard ERC-20 functions [like a turd in a punchbowl](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A): mintToken(address,uint256).

The [researcher's methodology was bulletproof](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A) - standard curl commands against the exposed RPC endpoint.

A simple totalSupply() call to the contract address revealed everything.

[The response](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A): 0x83252505cfe7e800 = 945,000,010 tokens when adjusted for 10 decimal places.

Unlimited token creation at the click of a button. The nuclear option for any project claiming "fixed supply."

**But finding the smoking gun wasn't enough. Time to see if it actually fired.**

*When you discover a loaded weapon, sometimes you have to pull the trigger to prove it's real?*

### Billionaire for 4 Minutes

*The researcher didn't just talk about the exploit - they demonstrated it with style.*

**One function call later, boom: [1,000,000,000 fresh RWN tokens materialized out of thin air](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A). Total supply jumped from 945 million to 1.945 billion in seconds.**

David Duckworth's "fixed supply" narrative just got nuked from orbit.

Then came the power move. [Every single freshly minted token got torched immediately](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A).

**The proof of burn:** [0xf55d021088c9bfa078248be8fad2fae2a0837263288c34cf49c565f0ba8d8392](https://explorer.rowanblockchain.com/tx?tx=0xf55d021088c9bfa078248be8fad2fae2a0837263288c34cf49c565f0ba8d8392)

No profit motive, no theft - just cold, hard proof that Rowan's entire tokenomics story was fiction.

Here's the kicker: Rowan's block explorer showed absolutely nothing. [The mint transaction vanished](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A) like it never happened, but the burn transaction was there for all to see.

Did their "transparent" blockchain had selective vision?

[Four minutes and four seconds](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A). That's how long the researcher held their billion-token fortune before sending it to the burn address. Long enough to screenshot the balance, short enough to prove a point.

[But the math told a different story](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A): even with just 2.84% of all transactions visible from the limited explorer data, wallet balances already added up to 589 million tokens.

[MEXC alone held 266 million -](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A) nearly half the supposed "total supply" sitting in one exchange wallet.

[Known wallet balances](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A) painted the full picture: - MEXC: 266 million - ProBit: 34 million - Buyback wallet: 7 million - Burned tokens: 302,199

[At 2024's price peak, those hidden 400 million tokens were worth approximately $132 million](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A). That's not a rounding error—that's grand theft auto money.

Rowan's block explorer? Didn't show a damn thing. [Their "transparent" blockchain had selective vision—only displaying transactions that fit the narrative](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A). Convenient.

[The researcher dumped it all online: hashes, bytecode, RPC calls, wallet screenshots](https://mirror.xyz/0x78754D3cc91f7f819Eb889d36c255F319a632D9D/M9Mtypim2vL609kLCndB91rKC91jZSMssh3E5IRa90A). A forensic autopsy of a dead project, signed and delivered.

**Duckworth went silent. Hard to spin your way out of mathematical proof.**

*What do you say when the blockchain calls you a liar?*

### Is David a Serial Scammer?

*David Duckworth didn't stumble into fraud - he may have been perfecting it for over a decade.*

**PropertyTribes forum, August 2011: "[David Duckworth gone missing](https://www.propertytribes.com/david-duckworth-gone-missing-t-3687-1.html)?" Users scrambling to contact their property investment guru who'd vanished with their cash. Sound familiar?**

"Anyone have David's number? Mobile would be best?" [posted John Corey](https://www.propertytribes.com/david-duckworth-gone-missing-t-3687-1.html), one of many left hanging when Duckworth pulled his first documented disappearing act.

Alleged property investment schemes, designer fees unpaid, partners left hanging - was the 2011 playbook maybe just a rough draft of what was coming?

Different industry, same disappearing act when the heat turned up?

*If so, the playbook hasn't changed: promise innovative returns, collect investor money, go radio silent when questioned, then vanish completely.*

**Duckworth just swapped property investments for blockchain tokens and scaled up the damage.**

If the allegations about the previous scam are true, then here we are 14 years later, same guy, same tricks, bigger pile of victims.

The only evolution was adding crypto buzzwords to the pitch deck.

**The man knows his audience. Green energy attracts true believers, and true believers make the best marks.**

They want to save the world so badly they'll ignore every red flag waving in their faces.

[But alleged patterns tell a story](https://www.propertytribes.com/david-duckworth-gone-missing-t-3687-1.html), and Duckworth's history raised questions for anyone who bothered looking.

**Why do questionable operators surface again and again? Because people rarely dig into the past.**

*But what happens when the receipts are carved in blockchain stone and a researcher just lit them on fire?*

### 69 Days of Gaslighting

*Blockchain evidence doesn't lie, but David Duckworth sure does.*

**[April 16th](https://mirror.xyz/0xC246f0cCc7a9f153C041bb1eF8A4d20bB1155187/jM18CQhT9xKRNw8Mp_fQNo4WBwEPmtnJQRnID89lFYI):** "Claims are entirely false and misleading." Deny everything, admit nothing - classic move.

**[April 21st](https://mirror.xyz/0xC246f0cCc7a9f153C041bb1eF8A4d20bB1155187/jM18CQhT9xKRNw8Mp_fQNo4WBwEPmtnJQRnID89lFYI):** "Circulating supply has NOT increased." Bold strategy lying about something anyone can verify with a single RPC call.

**[Same day, new story](https://mirror.xyz/0xC246f0cCc7a9f153C041bb1eF8A4d20bB1155187/jM18CQhT9xKRNw8Mp_fQNo4WBwEPmtnJQRnID89lFYI):** "Security lockdown initiated after discovering exploited unauthorized access point." Oh, now it's a hack? Make up your mind.

**[April 22nd](https://mirror.xyz/0xC246f0cCc7a9f153C041bb1eF8A4d20bB1155187/jM18CQhT9xKRNw8Mp_fQNo4WBwEPmtnJQRnID89lFYI):** "Investigation ongoing, blockchain fully operational." Code for: buying time while we craft better lies.

*Then came the endless parade of empty promises. [Variations of "next week" and "almost ready"](https://mirror.xyz/0xC246f0cCc7a9f153C041bb1eF8A4d20bB1155187/jM18CQhT9xKRNw8Mp_fQNo4WBwEPmtnJQRnID89lFYI) became his stalling strategy, recycled more times than a McDonald's cup.*

[Each deadline came and went](https://mirror.xyz/0xC246f0cCc7a9f153C041bb1eF8A4d20bB1155187/jM18CQhT9xKRNw8Mp_fQNo4WBwEPmtnJQRnID89lFYI) like clockwork. Each excuse was more pathetic than the last.

**[June 6th](https://mirror.xyz/0xC246f0cCc7a9f153C041bb1eF8A4d20bB1155187/jM18CQhT9xKRNw8Mp_fQNo4WBwEPmtnJQRnID89lFYI):** After seven weeks of silence: "Update coming early next week."

Still no acknowledgment of the hidden mint function. Still no audit. Still no transparency.

**[June 21st](https://mirror.xyz/0xC246f0cCc7a9f153C041bb1eF8A4d20bB1155187/jM18CQhT9xKRNw8Mp_fQNo4WBwEPmtnJQRnID89lFYI):** This day brought the killing blow to any pretense of legitimacy - Duckworth locked the Telegram group to announcement-only mode.

No more pesky questions from investors asking where their money went.

**[June 24th](https://mirror.xyz/0xC246f0cCc7a9f153C041bb1eF8A4d20bB1155187/jM18CQhT9xKRNw8Mp_fQNo4WBwEPmtnJQRnID89lFYI):** Project shutdown. "Retiring the token due to technical and reputational challenges."

Not fraud. Not theft. Not hidden mint functions. Just "challenges."

*When your response to mathematical proof takes longer than most college degrees, what are you really buying time for?*

### Double-Dipping the Damage

*Crypto rugs are a dime a dozen, but Duckworth had bigger ambitions than just token theft.*

**While investors were getting fleeced on RWN, another scam may have been humming along in parallel - physical SmartMiner devices sold to homeowners across the UK.**

[The pitch was slick](https://www.linkedin.com/posts/conor-quinn-02a24821b_rowan-energy-is-rated-average-with-29-activity-7343946045644582912-bLrd): install this £1,500 device alongside your solar panels and earn £450 annually from carbon credits.

Three-year payback, pure passive income, save the planet while padding your wallet.

Thousands bought in. Real hardware got installed in real homes by real contractors who had no clue they were pushing pyramid scheme accessories.

**TrustPilot tells the ugly truth now. [One-star reviews](https://uk.trustpilot.com/review/rowanenergy.com?stars=1) flood the page:**

*"Zero stars if I could. Repeated promises, zero payments."*

*"Device installed, money gone, support vanished."*

*"Three months past due, no payments, no contact."*

[ESE Group handled installations](https://decrypt.co/216485/rowan-energy-and-ese-solar-unite-to-drive-decentralised-energy-adoption) - another outfit [with its own legal baggage](https://www.newburytoday.co.uk/news/solar-panel-firm-ese-group-convicted-of-deceiving-customers-9305357/) that should have raised red flags.

**The warning signs were everywhere, but greed has a way of making people colorblind to red flags.**

*Was Duckworth running two separate cons, or did the hardware business just get caught in the token scam's blast radius?*

*Duckworth's cleanup operation moved faster than his exit scam.*

**YouTube videos - gone. Twitter posts - scrubbed. Telegram history - wiped. LinkedIn profile sanitized like a crime scene.**

RWN got booted from exchanges. Blockchain servers went dark. Those fancy SmartMiner devices now collect dust in UK homes, fancy paperweights that cost £1,500 each.

But victims don't stay quiet forever. [Underground Telegram groups](https://t.me/Rowanenergyunofficial) popped up. Evidence got saved. Lawyers started making calls.

*The same bastard, same vanishing act, same talent for disappearing when things get hot.*

**This time though, the blockchain remembered everything. Transaction hashes carved in digital stone. The contract bytecode sits there like a smoking gun.**

The only thing green about Rowan Energy was the cash Duckworth made off with.

Clean energy turned into dirty money.

Sustainable innovation became sustained extraction.

Carbon-neutral mining? Just carbon-copy fraud.

Scammers don’t evolve - they just change wrappers.

**So when the next David Duckworth shows up, pitching private chains and planet-saving profits…**

*Will anyone bother to check the receipts?*

REKT serves as a public platform for anonymous authors, we take no responsibility for the views or content hosted on REKT.

**donate (ETH / ERC20): [0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C](https://etherscan.io/address/0x3C5c2F4bCeC51a36494682f91Dbc6cA7c63B514C)**

disclaimer:

REKT is not responsible or liable in any manner for any Content posted on our Website or in connection with our Services, whether posted or caused by ANON Author of our Website, or by REKT. Although we provide rules for Anon Author conduct and postings, we do not control and are not responsible for what Anon Author post, transmit or share on our Website or Services, and are not responsible for any offensive, inappropriate, obscene, unlawful or otherwise objectionable content you may encounter on our Website or Services. REKT is not responsible for the conduct, whether online or offline, of any user of our Website or Services.
