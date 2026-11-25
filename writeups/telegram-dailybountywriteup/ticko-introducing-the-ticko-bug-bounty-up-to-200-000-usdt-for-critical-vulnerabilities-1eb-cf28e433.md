# Introducing the Ticko Bug Bounty

- **Source URL:** https://medium.com/ticko/introducing-the-ticko-bug-bounty-up-to-200-000-usdt-for-critical-vulnerabilities-1ebdf48df341
- **Fetched from:** https://medium.com/ticko/introducing-the-ticko-bug-bounty-up-to-200-000-usdt-for-critical-vulnerabilities-1ebdf48df341?source=rss----b3340ecfbc8f---4
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14965 (id 14965)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ticko / Sat, 31 Oct 2026 04:01:22 GMT

*The Ticko Bug Bounty is a long-term program that rewards security researchers who find and responsibly disclose vulnerabilities, with up to 200,000 USDT for a Critical finding. Here is what the program covers, how rewards are set, and how to submit a report that qualifies.*

Ticko Mainnet runs on real deposits, positions, and withdrawals. Every trade on Ticko is matched and settled onchain, so a flaw in the matching logic, the margin engine, or the way a signature is checked could affect real balances. Safety is part of Ticko’s mission, and a market is only as safe as the system that runs it.

We want to hear about a vulnerability from the researcher who found it, before anyone can exploit it. The Ticko Bug Bounty gives researchers a direct channel to our team and, for eligible reports, rewards scaled to severity. It is an ongoing program, and its terms live on a dedicated page in the Ticko docs.

On Ticko Mainnet, the program covers security vulnerabilities that could cause loss or freezing of user funds; unauthorized state changes, withdrawals, or transfers; incorrect order matching; or errors in margin, liquidation, funding rate, or settlement calculations. It also covers oracle or mark prices that can be manipulated or misused because of a flaw in Ticko’s logic. A price moved only by extreme market conditions or by large amounts of capital does not count.

Ticko’s trading sessions let a session key sign orders within the permissions a trader grants. Misuse of session keys or signatures is in scope, such as placing orders or withdrawing beyond those permissions, or replaying a signature. So are vulnerabilities that could cause node or API outages or state divergence between nodes, along with logic errors in Ticko Core, which comprises the Ticko VM and the onchain order book.

On testnet, the program covers testnet-only features and their interaction with Ticko Core, nodes, and APIs. Rewards for a testnet-only issue may be lower than for a Mainnet issue of the same severity. Other experimental testnet features fall outside the scope unless we announce otherwise, though we still welcome reports about them.

Ticko Mainnet is currently in Beta and already uses real funds, so vulnerabilities that affect it are assessed by Mainnet standards. A Beta limit published before a report is submitted, such as the deposit cap, counts as a vulnerability only if a report shows a way to bypass it.

Rewards are issued in USDT. Each tier sets a maximum, and the actual amount depends on the impact of the vulnerability and the likelihood that it could be exploited. The examples for each tier are illustrative and may change.

A Critical finding can earn up to 200,000 USDT. This tier covers significant loss of user funds, unauthorized withdrawals or asset transfers, permanently frozen funds, and bypassing session key permissions to place orders or withdraw as another user. It also covers violations of Mainnet execution invariants, such as total assets increasing or decreasing with no valid cause, and permanent or repeatable corruption of Mainnet state. Matching, margin, liquidation, funding rate, or settlement errors belong here when they produce an incorrect final state or a loss of funds.

A High finding can earn up to 25,000 USDT. This tier covers a Mainnet outage, temporarily frozen funds, and severe unavailability of Ticko Core, nodes, or APIs. It also covers state divergence or processing failures that do not produce an incorrect final state or a direct loss of funds. A Medium finding can earn up to 3,000 USDT. This tier covers API authentication or authorization issues, material data integrity issues, and service degradation with meaningful security impact.

Not every useful report is a security finding. Reports sent to [security@ticko.market](mailto:security@ticko.market) that don’t fit the tiers above fall under the Others tier, with rewards of up to 50 USDT. Examples include reproducible bugs, deposit and withdrawal issues with no security impact, and product suggestions. The amount depends on the quality of the report, and each issue is rewarded once, for the earliest valid submission. Like the Critical, High, and Medium tiers, the Others tier is ongoing and has no set end date.

Send your report directly to [security@ticko.market](mailto:security@ticko.market). We do not accept reports submitted through third-party bug bounty platforms unless we announce otherwise. A complete report describes the vulnerability, assesses its impact, gives detailed steps to reproduce it, and includes a proof of concept where one applies. We must be able to reproduce the issue for the report to qualify.

If several people report the same issue, only the first valid report we receive is eligible for a reward. An issue does not count as a new finding if, before your submission, it was already recorded internally by Ticko, disclosed in any published audit report, under investigation or remediation, or covered by an earlier valid report from someone else. Ticko determines whether an issue was already known. Contributors to the affected code are not eligible for a reward related to that code. Keep the vulnerability and all related communications confidential until we authorize disclosure, and do not share details in [Discord](https://discord.gg/PJVtbUaVrF), on X, or in any other channel, public or private.

Some reports do not qualify. These include reports without enough detail, such as step-by-step instructions, a reproducible example, or a proof of concept. Issues that require highly unusual or unreasonable user behavior are excluded, as are issues caused by outdated software, unsupported environments, or systems we no longer support. So are issues that require root access, a jailbroken or compromised device, or an operator compromise unrelated to a Ticko vulnerability. Issues in third-party libraries, extensions, tools, wallets, or applications qualify only if they lead directly to a Ticko vulnerability. Scanner output, reports the submitter has not personally verified, and issues that depend on extreme or unrealistic market conditions are also excluded. Non-security bugs, including minor performance issues with no meaningful security impact, do not qualify for the Critical, High, or Medium tiers; they may be considered under the Others tier.

Before a reward is issued, you will need to complete any applicable KYC or KYB checks, sanctions screening, and reward distribution procedures, and be able to receive USDT through the method and network we designate. Ticko determines the validity, classification, and reward amount of every submission at its sole discretion, and may use all submissions for remediation, testing, and security improvements.

All testing must take place on Ticko testnet or another non-production environment. The [Testnet Guide](https://docs.ticko.xyz/testnet-guide) explains how to sign in, claim test USDT from the faucet, and start trading, and you can get a testnet invitation code in our [Discord](https://discord.gg/PJVtbUaVrF). Testing on Ticko Mainnet or any other production system is prohibited, and reports based on it are disqualified.

Phishing and other social engineering are prohibited, as are extended or large-scale DDoS attacks. If you need to show that the system mishandles a short traffic spike, generate only as much load as the demonstration requires and avoid any material disruption. Testing third-party systems, apps, wallets, browser extensions, or websites is not allowed unless the issue you are investigating leads directly to an in-scope Ticko vulnerability.

You must not attempt extortion or make threats, disclose a vulnerability before a fix ships and Ticko authorizes disclosure, or publish or threaten to publish personal or other sensitive information without consent. Exploiting a vulnerability for financial gain beyond the program’s rewards is prohibited, including any trading or liquidation advantage. If you encounter someone else’s credentials, private keys, or session keys during testing, do not use them. Bypassing the program’s reporting process or acting outside the stated scope is also prohibited.

In return, Ticko will not take legal action against good-faith security research that complies with the program. Any change to the terms will be announced on the [Bug Bounty page](https://docs.ticko.xyz/resources/ticko-bug-bounty), and reports already submitted are assessed under the terms in effect when they were submitted.

Some reports are valid but do not qualify for a reward, for example because the issue is already known or is outside the reward scope. They remain genuine, high-quality contributions, and we offer public acknowledgment in place of a reward.

Acknowledgment is opt-in, so request it in your report or in your reply after our initial review, and tell us the name or handle you want credited and whether to include a link. Credit is published only after the issue is fixed and Ticko authorizes disclosure, and confidentiality applies until then. You can decline credit or ask to be listed anonymously. Acknowledgment is not a reward and does not change the reward decision. If your report earns a reward, you can request acknowledgment as well.

Whenever you find a vulnerability, send it to [security@ticko.market](mailto:security@ticko.market) with the details and steps to reproduce it. General bugs and product suggestions can go to the same address and fall under the Others tier. The full terms are on the [Bug Bounty page](https://docs.ticko.xyz/resources/ticko-bug-bounty).

Everyone is welcome to join our [Discord](https://discord.gg/PJVtbUaVrF) to follow product updates and talk with the team. Our mission is to make every market accessible, fair, and safe for everyone, and every vulnerability disclosed to us responsibly makes Ticko safer for the traders who use it.

Follow us on [X](https://x.com/tickoxyz) so you don’t miss what comes next, and visit [ticko.xyz](https://ticko.xyz/) or our [docs](https://docs.ticko.xyz/) to learn more.

*Disclaimer: This article is for general information only. It is not investment, financial, legal, or tax advice, and it is not an offer or solicitation to buy or sell any asset. Trading involves risk, and Beta Mainnet uses real funds while the product is still being validated. Bug Bounty rewards are subject to the terms on the Bug Bounty page in the Ticko docs, which Ticko may change; changes are announced on that page. The Ticko trading interface is operated by Fusio Digital Limited. Making the interface available does not mean that Fusio Digital Limited owns or operates the Ticko chain; the chain and the interface are provided separately, and the interface is not the only way to access the Ticko chain. Ticko is not available in restricted jurisdictions. See the Terms of Use for details.*

[Introducing the Ticko Bug Bounty: Up to 200,000 USDT for Critical Vulnerabilities](https://medium.com/ticko/introducing-the-ticko-bug-bounty-up-to-200-000-usdt-for-critical-vulnerabilities-1ebdf48df341) was originally published in [Ticko](https://medium.com/ticko) on Medium, where people are continuing the conversation by highlighting and responding to this story.
