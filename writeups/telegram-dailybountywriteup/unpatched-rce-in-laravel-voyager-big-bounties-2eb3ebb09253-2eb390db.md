# Unpatched RCE in Laravel Voyager = Big Bounties!

- **Source URL:** https://osintteam.blog/unpatched-rce-in-laravel-voyager-big-bounties-2eb3ebb09253?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250226015042/https://osintteam.blog/unpatched-rce-in-laravel-voyager-big-bounties-2eb3ebb09253
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8881 (id 8881)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Unpatched RCE in Laravel Voyager = Big Bounties! 💰

# **Hi Bug Bounty Hunters! 👋**

I’m sharing this write-up on a **critical Remote Code Execution (RCE)** vulnerability in the Laravel admin package **Voyager**. While some of you may already know about it, it’s crucial to revisit these flaws as they remain unpatched, making them a high-impact target for bug bounty hunters.

**Laravel Admin Package Voyager Vulnerable to One-Click RCE Flaw**

Voyager, a Laravel admin package, contains three critical security vulnerabilities that could allow attackers to gain control over affected systems

These flaws are still not fixed and can be exploited when a logged-in user clicks on a malicious link.

Security experts at *SonarSource* reported the issues to Voyager maintainers, but no response was received within 90 days.

**Affected Versions:**

**Voyager \< v1.5.0** (Confirmed vulnerable)


# Details of the Vulnerabilities

The *SonarQube Cloud* security team found the first issue, an arbitrary file write flaw, and later discovered two more weaknesses…
