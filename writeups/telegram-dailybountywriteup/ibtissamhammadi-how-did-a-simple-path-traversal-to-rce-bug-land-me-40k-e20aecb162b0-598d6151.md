# How Did a Simple Path Traversal to RCE Bug Land Me $40K?

- **Source URL:** https://medium.com/@ibtissamhammadi/how-did-a-simple-path-traversal-to-rce-bug-land-me-40k-e20aecb162b0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250119044735/https://medium.com/@ibtissamhammadi/how-did-a-simple-path-traversal-to-rce-bug-land-me-40k-e20aecb162b0?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8518 (id 8518)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How Did a Simple Path Traversal to RCE Bug Land Me $40K?

## 5 Mind-Blowing Steps That Turned an RCE Discovery Into a Massive Bounty

*I’m a security researcher, and one day, a routine check for bugs led me to a big discovery — a simple issue turned into a major Remote Code Execution (RCE) find.*

“Sometimes the biggest security vulnerabilities hide in the most unexpected places.”


Most people think [RCE engineering](https://web.archive.org/web/20250119044735/https://youtube.fandom.com/wiki/Real_Civil_Engineer) is all about tricky hacks, but for me, it started with a simple mistake — a file path that wasn’t supposed to be open.

**The Initial Discovery**

Like many security researchers, I began by studying the application’s structure. What stood out wasn’t a big, obvious vulnerability but a small issue with how paths were managed.

The target was a big RCE company (name hidden for safety) that managed sensitive financial data, like in RCE mortgage systems.

*The Breakthrough Moment*

After investigating for days, I found something interesting: how the app handles paths in the education portal has a serious flaw.

“Security is not about finding complex vulnerabilities — it’s about understanding simple systems deeply.”


**The Technical Journey**

The process felt like a game, with each step opening up new possibilities.

1. Initial path traversal discovery
2. Privilege escalation identification
3. System command injection vector
4. Payload development
5. Full system compromise

*Understanding the Impact*

The vulnerability’s scope exceeded the typical **RCE in insurance** systems I’d encountered before. It could potentially affect:

- User data security
- System integrity
- Financial transactions
- Administrative controls

**The Responsible Disclosure**

The process of reporting this vulnerability taught me valuable lessons about:

1. Clear documentation
2. Proof of concept development
3. Impact assessment
4. Professional communication

“The biggest rewards in security research come from responsible disclosure and clear communication.”


*The Resolution*

Working with the security team, we:

- Identified the root cause
- Developed mitigation strategies
- Implemented security patches
- Verified the fixed effectiveness

**Lessons Learned**

This experience taught me that:

1. Simple vulnerabilities can have a critical impact
2. Thorough documentation is crucial
3. Patient investigation pays off
4. Professional communication is key
5. Responsible disclosure matters

*Key Takeaways for Researchers*

1. Always start with the basics
2. Document everything
3. Think creatively
4. Stay persistent
5. Communicate professionally

**The Final Reward**

The $40,000 bounty wasn’t about the money — it represented recognition of:

- Thorough research
- Professional approach
- Responsible Disclosure
- Real security impact

“The true reward in security research isn’t just the bounty — it’s the impact you make on digital security.”


*Looking Forward*

This experience has taught me that the best security discoveries often come from:

- Patient investigation
- Creative thinking
- Professional Conduct
- Clear communication
