# Finding an Exposed Admin Panel on a Government Portal

- **Source URL:** https://medium.com/@byteshubh1717/finding-an-exposed-admin-panel-on-a-government-portal-a-responsible-disclosure-story-ca8592f5b213
- **Fetched from:** https://medium.com/@byteshubh1717/finding-an-exposed-admin-panel-on-a-government-portal-a-responsible-disclosure-story-ca8592f5b213?source=rss-9911f21a3c5e------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14942 (id 14942)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Byteshubhx / Sat, 10 Oct 2026 18:03:01 GMT

As part of my ongoing practice as a SOC L1 trainee, I regularly do passive reconnaissance on publicly accessible websites — not to exploit anything, but to understand how real-world misconfigurations show up outside of lab environments. This is one of those findings.

I was running basic recon techniques — search engine dorking, directory/path enumeration patterns — against a category of websites that are notoriously under-resourced from a security standpoint: municipal/government portals. These sites are often built by third-party vendors, deployed once, and rarely revisited for security hardening after launch.

During this process, I came across a portal where the admin login panel was directly reachable from the homepage — no obscurity, no path restriction, nothing hiding it. That alone isn’t a vulnerability. What made it one was what came next.

Out of curiosity (and because this is a textbook SOC/pentest checklist item), I tested whether the panel was still running on default vendor credentials. It was.

Two things compounded the severity:

I did not log in beyond confirming access was possible. No data was viewed, modified, exported, or deleted. The moment I confirmed the issue existed, I stopped.

This is the part that actually matters more than the finding itself:

That last point is common, and it’s worth normalizing for anyone starting out in this space — most independent disclosures to under-resourced orgs go unanswered or take weeks. The professional move is persistence through proper channels, not escalation through public pressure, and definitely not continued access to “test” further.

This is where I want to pivot — because the point of sharing this isn’t “look what I found,” it’s “look what SOC/blue teams should be catching before someone less well-intentioned finds it.”

A few takeaways if you’re on the defensive side:

I’m sharing this not to call anyone out, but because stories like this are genuinely useful for anyone coming up in SOC/blue team work — recon and finding issues is one skill, but handling disclosure responsibly is the one that actually builds trust and a career.

If you’re a defender reading this: check your admin panels today. It takes five minutes and might save you from being my next case study.

If you found this useful or want to follow more of my Cybersecurity learning journey:
