# 🦊 Mass thefts from MetaMask via fake updates

- **Source URL:** https://cryptoslate.com/hundreds-of-evm-wallets-drained-what-to-check-before-you-update
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/1090 (id 1090)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
On-chain security researcher ZachXBT flagged hundreds of wallets across multiple EVM chains getting drained for small amounts, typically under $2,000 per victim, funneling into a single suspicious address.

The theft total climbed past $107,000 and kept rising. The root cause is still unknown, but users reported receiving a phishing email disguised as a mandatory [MetaMask](https://cryptoslate.com/products/metamask/) upgrade, complete with a party-hat fox logo and a “Happy New Year!” subject line.

This attack arrived when developers were on holiday, support channels were running skeleton crews, and users were scrolling through inboxes cluttered with New Year promotions.

Attackers exploit that window. The small per-victim amounts suggest the drainer operates off contract approvals rather than full seed-phrase compromise in many cases, which keeps individual losses below the threshold where victims immediately sound alarms but allows the attacker to scale across hundreds of wallets.

The industry is still processing a separate Trust Wallet browser extension incident in which malicious code in Chrome extension v2.68 harvested private keys and drained [at least $8.5 million from 2,520 wallets](https://cryptoslate.com/trust-wallet-just-issued-an-emergency-warning-for-chrome-users-after-a-hidden-script-was-caught-harvesting-private-keys/) before Trust Wallet patched to v2.69.

Two different exploits, same lesson: user endpoints remain the weakest link.

## Anatomy of a phishing email that works

The MetaMask-themed phishing email demonstrates why these attacks succeed.

The sender identity shows “MetaLiveChain,” a name that sounds vaguely DeFi-adjacent but has no connection to MetaMask.

The email header contains an unsubscribe link for “reviews@yotpo.com,” revealing that the attacker lifted templates from legitimate marketing campaigns. The body features MetaMask's fox logo wearing a party hat, blending seasonal cheer with manufactured urgency about a “mandatory update.”

That combination bypasses the heuristics most users apply to obvious scams.

MetaMask's official security documentation establishes clear rules. Support emails come only from verified addresses, such as support@metamask.io, and never from third-party domains.

The wallet provider does not send unsolicited emails demanding verification or upgrades.

Additionally, no representative will ever ask for a Secret Recovery Phrase. Yet these emails work because they exploit the gap between what users know intellectually and what they do reflexively when an official-looking message arrives.

Four signals expose phishing before damage occurs.

First, brand-sender mismatch, as MetaMask branding from “MetaLiveChain” signals template theft. Second, manufactured urgency around mandatory updates that MetaMask explicitly says it will not send.

Third, destination URLs that don't match claimed domains, hovering before clicking reveals the actual target. Fourth, requests that violate core wallet rules, such as asking for seed phrases or prompting for signatures on opaque off-chain messages.

The [ZachXBT](https://cryptoslate.com/people/zachxbt/) case demonstrates signature-phishing mechanics. Victims who clicked the fake upgrade link likely signed a contract approval granting the drainer permission to move tokens.

That single signature opened the door to ongoing theft across multiple chains. The attacker chose small per-wallet amounts because contract approvals often carry unlimited spend caps by default, but draining everything would trigger immediate investigations.

Spreading theft across hundreds of victims at $2,000 each flies under the individual radar while accumulating six-figure totals.

## Revoking approvals and shrinking blast radius

Once a phishing link is clicked or a malicious approval is signed, priority shifts to containment. MetaMask now lets users view and revoke token allowances directly inside MetaMask Portfolio.

Revoke.cash walks users through a simple process: connect your wallet, inspect approvals per network, and send revoke transactions for untrusted contracts.

Etherscan's Token Approvals page offers the same functionality for manual revocation of ERC-20, ERC-721, and ERC-1155 approvals. These tools matter because victims who act fast could cut off the drainer's access before losing everything.

The distinction between approval compromise and seed-phrase compromise determines whether a wallet can be salvaged. MetaMask's security guide draws a hard line: if you suspect your Secret Recovery Phrase has been exposed, stop using that wallet immediately.

Create a new wallet on a fresh device, transfer remaining assets, and treat the original seed as permanently burned. Revoking approvals helps when the attacker only holds contract permissions; if your seed is gone, the entire wallet must be abandoned.

Chainalysis documented roughly 158,000 personal wallet compromises affecting at least 80,000 people in 2025, even as total stolen value fell to [approximately $713 million](https://www.chainalysis.com/blog/2025-crypto-crime-mid-year-update/).

Attackers hit more wallets for smaller amounts, the pattern ZachXBT identified. The practical implication: organizing wallets to limit blast radius matters as much as avoiding phishing.

A single compromised wallet should not mean total portfolio loss.

## Building defense-in-depth

Wallet providers have shipped features that would have contained this attack if adopted.

MetaMask now encourages setting spending caps on token approvals rather than accepting the default “unlimited” permissions. Revoke.cash and De.Fi's Shield dashboard advocate treats approval reviews as routine hygiene alongside hardware wallet use for long-term holdings.

MetaMask enables transaction security alerts from Blockaid by default, flagging suspicious contracts before signatures are executed.

The [Trust Wallet](https://cryptoslate.com/products/trust-wallet/) extension incident reinforces the need for defense-in-depth. That exploit bypassed user decisions, and malicious code in an official Chrome listing automatically harvested keys.

Users who segregated holdings across hardware wallets (cold storage), software wallets (warm transactions), and burner wallets (experimental protocols) limited exposure.

That three-tier model creates friction, but friction is the point. A phishing email that captures a burner wallet costs hundreds or a few thousand dollars. The same attack against a single wallet holding an entire portfolio costs life-changing money.

The ZachXBT drainer succeeded because it targeted the seam between convenience and security. Most users keep everything in one MetaMask instance because managing multiple wallets feels cumbersome.

The attacker bet that a professional-looking email on New Year's Day would catch enough people off guard to generate profitable volume. That bet paid off, with $107,000 and counting.

## What's at stake

This incident poses a deeper question: who bears responsibility for endpoint security in a self-custodial world?

Wallet providers build anti-phishing tools, researchers publish threat reports, and regulators warn consumers. Yet the attacker needed only a fake email, a cloned logo, and a drainer contract to compromise hundreds of wallets.

The infrastructure that enables self-custody, permissionless transactions, pseudonymous addresses, and irreversible transfers also makes it unforgiving.

The industry treats this as an education problem: if users verified sender addresses, hover over links, and revoke old approvals, attacks would fail.

Yet, [Chainalysis's](https://cryptoslate.com/companies/chainalysis/) data on 158,000 compromises suggests education alone doesn't scale. Attackers adapt faster than users learn. The MetaMask phishing email evolved from crude “Your wallet is locked!” templates to polished seasonal campaigns.

The Trust Wallet extension exploit proved that even careful users can lose funds if distribution channels get compromised.

What works: hardware wallets for meaningful holdings, ruthless approval revocation, wallet segregation by risk profile, and skepticism toward any unsolicited message from wallet providers.

What doesn't work: assuming wallet interfaces are safe by default, treating approvals as one-time decisions, or consolidating all assets in a single hot wallet for convenience. The ZachXBT drainer will be shut down because the address is flagged, and exchanges will freeze deposits.

But another drainer will launch next week with a slightly different template and a new contract

address.

The cycle continues until users internalize that the convenience of crypto creates an attack surface that eventually gets exploited. The choice isn't between security and usability, but somewhat between friction now and loss later.
