# Subdomain Takeover

- **Source URL:** https://medium.com/@Xt3sY/subdomain-takeover-d734da4d2d41?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142140/https://medium.com/@Xt3sY/subdomain-takeover-d734da4d2d41
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3948 (id 3948)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Subdomain Takeover

**Greetings, Community! Today, I am excited to present my discoveries concerning the “P2 Bug — Subdomain Takeover.”**

But first, let’s clarify what a subdomain is in simple terms:

A subdomain is like a smaller section within a larger domain. Think of it as the child of the main parent domain.

Moreover, there are two key categories of subdomains:

Vertical Correlation: These are subdomains related to the main domain, like all the various subdomains under apple.com, such as cloud.apple.com or istore.apple.com.

Horizontal Correlation: These are subdomains affiliated with the main domain but may also be interconnected. A prime example is Facebook’s subsidiaries, such as WhatsApp, LiveRail, Onavo, and more.

Let’s continue exploring this intriguing topic together.

What is Subdomain Takeover ?

When attackers gain complete control of their target subdomain this happens when the CNAME of the subdomain is miss config.

Let’s dive in.

It’s a tale from just yesterday when I was engrossed in my bug bounty hunt on a target. After completing an exhaustive reconnaissance phase, I stumbled upon a valuable lesson: never underestimate the significance of a 404 error page of Wix engine.

As soon as I encountered this page, my instinct led me to fire up the ‘dig’ command.

Using dig to Check for Possible Subdomain Takeover Vulnerabilities

With all that information you should be able to verify that a domain is not affected by a possible subdomain takeover.

dig +trace sub.vul.com [@8](http://twitter.com/8).8.8.8

My ‘dig’ command revealed the hosting location of the website.


1. **Register to wix**
2. **Create a new site**
3. **Publish > Connect your own customized domain (Need premium account)**

**Note** : “You cannot connect a subdomain in your Wix account if the main domain is in a different Wix account. You must create the subdomain in the same Wix account as the main domain.”

**But It is possible even if the root domain is in another account. When you publish your site and have a premium account, go to connect a domain.**

**Then choose I’m looking for a subdomain :**

So just go at the end and click verify.

**If we can impersonate the target, or maybe due to wix support mistakes, you can takeover the subdomain even if the main domain is in a different account.**
