# bad bug bounty in smm.socnet.pro

- **Source URL:** https://medium.com/@mamatneo30/bad-bug-bounty-in-smm-socnet-pro-86ef166ed682
- **Fetched from:** https://medium.com/@mamatneo30/bad-bug-bounty-in-smm-socnet-pro-86ef166ed682?source=rss-fd3664347995------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14954 (id 14954)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Xface / Tue, 20 Oct 2026 16:35:17 GMT

bad bug bounty in smm.socnet.pro

Hello,

I am writing to share my recent experience participating in the bug bounty program for smm.socnet.pro, which has been deeply frustrating due to the conduct of both the development and support teams.

I submitted three vulnerabilities simultaneously: an account takeover (ATO) issue arising from a weak "forgot password" implementation—which allows an attacker to lock a user out of their account using only their email address—and a reflected host header injection. Although all three issues were eventually patched, the support team classified them as "non-functional." This assessment is difficult to reconcile with the fact that I provided a clear, detailed proof-of-concept (PoC) that worked perfectly. How they could reach such a conclusion remains unclear.

More concerningly, regarding the critical-severity issue, the support team asked, "How would an attacker even obtain the user's/target's Gmail address?" For anyone experienced in bug hunting, this question is fundamentally misguided—it demonstrates a clear lack of familiarity with OSINT (Open-Source Intelligence) and reconnaissance techniques. The same question was raised regarding the vulnerability that allows an attacker to lock a user out via their email. It is baffling that a developer would fail to consider the practical implications of such a vulnerability.

They refused to classify these as actual vulnerabilities, yet they proceeded to patch them anyway. When I challenged them—asking, "If these aren't vulnerabilities, then revert the changes; don't bother fixing them"—I received no response and no action. If they were not vulnerabilities, why fix them in the first place? This inconsistency is bizarre.

In short, they remained adamant that these were not vulnerabilities, even after having patched them. Ultimately, the reward was capped at just $50 for issues that were actually critical, medium, and high severity.

A piece of advice: if they choose to be dishonest, that very dishonesty will ultimately be their undoing.
