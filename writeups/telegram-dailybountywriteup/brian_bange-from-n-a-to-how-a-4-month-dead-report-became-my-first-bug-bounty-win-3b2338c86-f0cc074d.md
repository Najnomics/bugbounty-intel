# From N/A to $$$

- **Source URL:** https://medium.com/@Brian_Bange/from-n-a-to-how-a-4-month-dead-report-became-my-first-bug-bounty-win-3b2338c86a31
- **Fetched from:** https://medium.com/@Brian_Bange/from-n-a-to-how-a-4-month-dead-report-became-my-first-bug-bounty-win-3b2338c86a31?source=rss-d9d06d9d059b------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14908 (id 14908)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Brian Bange / Fri, 11 Sep 2026 14:00:02 GMT

If you’re grinding your first year in bug bounty, you know the feeling. You spend hours hunting, finally submit what looks like a great bug, and wake up to the dreaded “Not Applicable” (N/A) or “Duplicate.”

For months, my dashboard was a graveyard of rejected reports. But my very first bounty payout didn’t come from a fresh submission — it came from a 4-month-old N/A report that miraculously came back from the dead.

Here is the story of how I found a supply chain vulnerability, lost it to strict triage rules, and used a little bit of professional social engineering to secure the win.

While hacking on a massive private program (\[REDACTED\_COMPANY\]), I started digging through their compiled frontend JavaScript bundles. Inside a heavily obfuscated clientlib file, I spotted a recurring module path:

@redacted-scope/core

I immediately checked the public npm registry. **The @redacted-scope organization didn't exist.**

Knowing the risk of Dependency Confusion (where a misconfigured internal proxy pulls a public malicious package instead of the internal one), I moved fast. To protect the company and prove the concept, I registered the scope on the public npm registry and published a completely empty, benign PoC package. I secured the namespace before a real threat actor could.

I wrote up a detailed report and submitted it. I was hyped.

Days later, triage closed it as N/A.

Their reasoning? I didn’t provide a pingback or run whoami on the internal build servers. Without proof of execution, triage assumed the company's internal proxies successfully blocked public fallbacks. Because I played it safe and ethical—refusing to drop a reverse shell in my package—the report was killed. I took the reputation hit and moved on.

Four months passed. I was still grinding away when an email suddenly landed in my inbox from a Product Owner at \[REDACTED\_COMPANY\].

They noticed my PoC on npm. They politely explained they needed the namespace for their internal developers and asked if I would transfer ownership to them.

This was my golden ticket.

I replied immediately. I didn’t hold the scope hostage, and I didn’t demand money. I simply said:

*“I am happy to transfer this to your maintainers today. However, I actually responsibly disclosed this exact issue to your bug bounty program months ago, but it was closed as N/A because I refused to execute unauthorized code on your servers to prove impact. Could your security team take a second look?”*

A few days later, the client logged directly into the platform. They confirmed that while my package was technically blocked by their defenses, leaving the namespace vulnerable to hijacking was a major administrative oversight. They cited my report as highlighting a critical “best practice,” completely overruled the triage team, and reopened the ticket.

Shortly after, I was awarded my very first bounty **$$$**.

The first win is the hardest. Now, it’s back to the hunt!
