# Meet GitPay

- **Source URL:** https://medium.com/@random212/meet-gitpay-pay-contributors-with-a-single-comment-39f09ae32173
- **Fetched from:** https://medium.com/@random212/meet-gitpay-pay-contributors-with-a-single-comment-39f09ae32173?source=rss-d6fd349a97e9------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14965 (id 14965)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** duttlabs / Fri, 30 Oct 2026 18:35:41 GMT

Paying someone for a merged pull request should take one line, not a week of spreadsheets, invoices and wallet hand-offs. That is the idea behind GitPay, a new open-source project from Stability Nexus and the AOSSIE community.

If you maintain an open-source project, you probably know the drill. A contributor fixes a bug or ships a feature. You want to reward them. Then the friction starts: who tracks what is owed, who approves it, who sends it, and how does everyone know it actually happened? GitPay moves all of that into the place where the work already happens: the pull request.

GitPay started with a real pain point. In December 2025, Bruno from Stability Nexus shared this in our development channel:

Tracking the [CATs](https://docs.stability.nexus/) owed to contributors was being done entirely by hand. It was subjective and, in his words, “just boring accounting” that ate up a lot of his time that year.

His idea was simple: attach a reward amount to each issue, and when a PR closes it, share that reward between the PR author, the reviewers and perhaps the issue creator. A bot keeps the balances, and settling on-chain follows those balances.

GitPay is the first step toward that vision: rewards decided where the work happens, checked by clear rules, and recorded in public on the pull request, instead of in someone’s spreadsheet.

GitPay is a GitHub Action that pays contributors when a maintainer comments /send on a pull request. You add one small workflow file to your repository, and from then on a comment like /send 0xContributorAddress 10 USDC is all it takes to send a stablecoin payout.

Three things make it different from a typical payment tool:

It is built on x402, an open payments standard now hosted by the Linux Foundation, and it is released under the MIT license.

Before anything touches a blockchain, GitPay checks who sent the command, your per-payout cap and any custom rules. A payout it has already made is never sent twice.

Nobody has to sign each payment by hand. You set a spending limit once, either as a Safe spending limit or as a token approval from your everyday wallet, and that limit is what authorizes payouts from then on.

GitPay is designed so that a mistake, a re-run or even a leaked key has a hard ceiling.

**Maintainers** get a payout process that lives where they already review code. No separate dashboard, no manual bookkeeping, and a public record of every reward on the PR it belongs to.

**Contributors** get paid quickly and transparently. Share a wallet address, and the receipt on your pull request shows exactly when and how you were paid.

**Communities, DAOs and grant programs** that fund open-source work get a simple, auditable way to turn “this PR is worth a bounty” into an actual payment, with spending caps the owners set themselves.

You can see GitPay work without any wallet, keys or secrets, because dry-run is the default.

**Going live with a Safe:** Create a Safe on the Ethereum Sepolia testnet, set a spending limit for a delegate address in Safe{Wallet} (Settings → Setup → Spending limits), and give that address a little Sepolia ETH for gas. Then switch the workflow to mode: self and add your Safe, token, RPC URL and delegate key, keeping the key and RPC URL in repository secrets. The [settlement flow guide](https://github.com/StabilityNexus/GitPay/blob/main/SETTLEMENT-FLOW.md) walks through each step.

**Going live without a Safe:** Pay from the wallet you already use, like MetaMask, Rabby or a hardware wallet. Create a separate delegate address and give it a little Sepolia ETH for gas. Then, from the wallet holding your USDC, approve that delegate for an amount on the token contract (Etherscan’s *Write as Proxy* tab works). In the workflow, use scheme: approve and payer: "0xYourWallet" instead of safe. Unlike a Safe limit, the approval doesn't reset, so top it up when it runs out.

GitPay is early-stage and currently targets testnets, so it’s the perfect time to experiment, give feedback and help shape it.

GitPay is fully open source, and contributions of every size are welcome, from trying the quickstart and reporting what confused you to picking up an issue.

Open source runs on people’s time and talent. GitPay makes rewarding that work as easy as leaving a comment. Give it a try and tell us what you think.
