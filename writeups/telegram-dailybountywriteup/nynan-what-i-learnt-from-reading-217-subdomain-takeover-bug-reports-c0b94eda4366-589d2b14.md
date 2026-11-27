# What I learnt from reading 217* Subdomain Takeover bug reports.

- **Source URL:** https://medium.com/@nynan/what-i-learnt-from-reading-217-subdomain-takeover-bug-reports-c0b94eda4366?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230811015758/https://medium.com/@nynan/what-i-learnt-from-reading-217-subdomain-takeover-bug-reports-c0b94eda4366
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/688 (id 688)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*A comprehensive analysis of Subdomain Takeovers (SDTO), DNS Hijacking, Dangling DNS, CNAME misconfigurations…*

Considering becoming a member on medium? Use this link at no extra cost to yourself, and support me :) ([https://medium.com/@nynan/membership](/@nynan/membership))

My two prior blogs, [**What I Learnt From Reading 220 IDOR bug reports**](/@nynan/what-i-learnt-from-reading-220-idor-bug-reports-6efbea44db7), and [*What I Learnt From Reading 126 Information Disclosure Writeups*](/@nynan/what-i-learnt-from-reading-126-information-disclosure-writeups-d896c5d5a2a4)\*, were well received, so I’m continuing the series. I once more scraped **ALL** 143 SDTO bug reports from hackerone, **and** 74 detailed write-ups, then went into hiding as I read and took notes on them. I’m here to show you my actionable findings, and show you how to properly hunt for SDTOs.

In this analysis we will *cover*:

1. a **tldr** of SDTO for beginners.
2. The types of subdomains — **what should you look for**
3. **How** were the subdomains found?
4. Should you use **Can-I-Take-This-Over-XYZ**?
5. Types of **hosting platforms**
6. SDTO **over time** — Is this bug worth looking for anymore?
7. **Impact** — How to get a bigger bounty
8. Miscellaneous bug bounty **tips**!

# Subdomain Takeovers TLDR;

I won’t go into detail here, because this blog is intended to provide more intermediate-advanced insights, however, I have still tried to make this as accessible as possible for new hunters.

Subdomain takeover is a bug with **high** (or *potentially* critical) severity. When an asset, usually a subdomain, points to a third-party hosting provider via CNAME dns record, it will fetch content from that third-party provider. If a company stops paying for that provider but **keeps** the CNAME reference, an attacker can potentially register with that third party and the company subdomain will point to an *attacker-controlled resource*.

# The types of subdomains — What should you look for?

Going into this, *for some reason*, I assumed that most of the subdomains that would be vulnerable would be internal subdomains, which were never supposed to be for users and were forgotten about by developers…
