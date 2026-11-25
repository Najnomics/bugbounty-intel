# Meta Paid $1.2 Million to Break Its Own AI Agent. The Biggest Bug Wasn’t Even an AI Bug.

- **Source URL:** https://medium.com/@Aacle/meta-paid-1-2-million-to-break-its-own-ai-agent-the-biggest-bug-wasnt-even-an-ai-bug-d1707e8b5675
- **Fetched from:** https://medium.com/@Aacle/meta-paid-1-2-million-to-break-its-own-ai-agent-the-biggest-bug-wasnt-even-an-ai-bug-d1707e8b5675?source=rss-7e0eec04e74c------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14976 (id 14976)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Abhishek meena / Tue, 10 Nov 2026 06:58:47 GMT

Bugs.

Meta just published their bug bounty numbers for Muse — their AI agent that reads your email, manages your calendar, and runs inside its own virtual machine.

630+ reports. 64 valid. \~$1.2 million paid out.

For a product that launched publicly in September.

Here’s every bounty Meta disclosed, biggest to smallest:

Now count how many of those are actually *AI* bugs.

One. Out of five.

And the biggest one — the $300k one — was a trust-boundary misconfiguration. The kind of bug that’s been paying bounties since before LLMs existed. That’s the story here.

Four months *before* Muse launched, a researcher got access to conversations and tokens on the VMs Meta’s own engineers were using to test the product.

The cause is painfully simple.

An auth check treated a header — added by a local HTTPS proxy — as proof that a request came from a trusted source. One source of truth. Fine in theory.

Then a system migration added a second proxy layer.

Outside requests could suddenly carry the trusted header too.

One migration. One broken assumption. $300,000.

I love Meta’s response here: they didn’t just patch it. They shut the service down and removed all trust in the local machine entirely. Structural fix, not a band-aid.

The three smaller bugs are old friends too:

One-time passcode redaction bypass ($90,000). Muse redacts OTPs from emails. Certain formatting slipped past the filter. Meta called it “one part of an end-to-end attack” — someone chained it toward something real.

Android web view credential theft ($50,000). A malicious app passed a link into a privileged web view. The link handler recognized the path without validating the host. Attacker-controlled page grabs the credentials. This bug would feel at home in a 2016 writeup.

Mac auto-update hijack ($1,000). Local attacker abuses the auto-updater to run code with the app’s privileges. Honest price for a local-access bug.

This is the $90k prompt injection, and it’s clever.

A researcher built a webpage that, when a user asked Muse to summarize it, **imitated the status messages of Muse’s own browsing tool**.

Read that again. The page didn’t attack the model directly. It pretended to *be the agent’s own tool talking to it*.

The agent believed it. And executed actions it should have refused.

Meta’s fix: new detection signals, plus classifiers that now catch the original attack and **100 variations** of it.

The lesson underneath: an agent that can’t tell data from instructions will treat a well-crafted lie as authority. That’s not a Muse problem. That’s every AI agent shipping right now.

The remaining bugs? You already know these:

**One-time passcode redaction bypass ($90,000).** Muse redacts OTPs from emails. Certain formatting slipped past the filter. Meta called it “one part of an end-to-end attack” — meaning someone chained it toward something real.

**Android web view credential theft ($50,000).** A malicious app passed a link into a privileged web view. The link handler recognized the path **without validating the host**. Attacker-controlled page grabs the credentials. That bug would feel at home in a 2016 writeup.

Strip the AI branding off these five bugs and count the classes:

**The new attack surface doesn’t replace the old one. It stacks on top of it.**

Every AI agent is still a web app behind proxies, a mobile app with web views, a redaction layer, an updater.

The LLM in the middle just adds **one more trust boundary to misconfigure** — and one more place where “this is data” gets confused with “these are instructions.”

You don’t need to become an ML researcher to hunt here. You need the instinct for where systems make unexamined assumptions. You already have that.

Some numbers worth knowing if you’re thinking about this space:

**Up to $300,000** per valid report — which Meta claims is several times higher than other major AI labs’ maximums.

**Up to $130,000** for a prompt injection affecting a single user.

**Up to $250,000** for a fleetwide compromise. And they’ll double your bounty if you donate it to charity.

But here’s my favorite stat from the whole disclosure:

**630 reports. 64 valid.** Roughly a **10% validity rate**.

AI targets are new and everyone’s piling in — and most reports don’t land. Precision beats volume here, the same as it always has.

Taking the Muse findings as a hunting map rather than news:

**Trust boundaries around internal tooling.** Every “requests from X are trusted” assumption is a $300k-shaped hole. Migrations love to quietly break these.

**Tool output handling.** If the agent summarizes pages, reads email, processes files — what happens when content impersonates its own tools? That’s a $90k question.

**Redaction and filtering logic.** Pattern-based filters have formatting blind spots. Find the pattern matcher, find what it misses.

**Link and web view handlers.** Agents that open links inherit every classic open-redirect and validation bug. Plus credentials.

**Update paths.** Unsexy. On the payout list anyway.

The AI boom didn’t change what makes targets break.

It just added a very well-funded new set of them.

Muse’s bounty is still open, by the way. Up to $300k a report.

You know what to do.
