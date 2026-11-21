# I Found a Critical XSS Everyone Missed

- **Source URL:** https://medium.com/@ibtissamhammadi1/i-found-a-critical-xss-everyone-missed-16dd284919c9?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250823081050/https://medium.com/@ibtissamhammadi1/i-found-a-critical-xss-everyone-missed-16dd284919c9
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10551 (id 10551)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# I Found a Critical XSS Everyone Missed

Most hunters dismissed this subdomain as low-risk. Here’s how an overlooked feature led to a critical XSS chain.

When a **Fortune 500 company’s bug bounty program** listed a seemingly harmless subdomain, most researchers scrolled past it.

However, what initially appeared to be a dead end turned out to be one of the most **impactful vulnerabilities** I’ve ever reported — a **stored XSS** that could’ve **compromised every employee’s device**.

This wasn’t just a **pop-up alert**. It was a **stealthy account takeover exploit**, hidden in plain sight.

Here’s how I found it, why everyone else missed it, and how you can avoid making the same mistake.

## The Google Dork That Exposed a Hidden Portal

The target’s main domain was heavily tested, but a **non-standard subdomain** caught my attention:

`10-10-10-16.mobile.REDACTED.com`  Most tools ignored it because it appeared to be an **internal IP address**. But a simple **Google dork** revealed it was publicly accessible:

`site:*.mobile.REDACTED.com inurl:config`  **Pro Tip:**

*Always look for unusual subdomains — they’re often less tested and full of security misconfigurations.*
