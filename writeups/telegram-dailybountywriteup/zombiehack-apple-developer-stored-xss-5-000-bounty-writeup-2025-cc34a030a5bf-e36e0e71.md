# Apple Developer Stored XSS — $5,000 Bounty | Writeup 2025

- **Source URL:** https://medium.com/@ZombieHack/apple-developer-stored-xss-5-000-bounty-writeup-2025-cc34a030a5bf?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@ZombieHack
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 11868)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### **Apple Developer Stored XSS — $5,000 Bounty | Writeup 2025**

Hello Security Researchers & Bug Bounty Community,

My name is Youssef Desouki, also known in the cybersecurity community as Zombie Hack.

I’m excited to share one of my latest findings — a Stored XSS vulnerability affecting multiple Apple domains, including the highly sensitive developer.apple.com.

This write-up reflects my journey, the technical breakdown, and the collaborative work with Apple’s security team to ensure this issue was fully remediated.

I hope this report contributes value to the community and helps others in their own research paths.

#### #Summary

During a security review of Apple Discussions and related Apple web assets, I discovered a Stored Cross-Site Scripting (Stored XSS) vulnerability that allowed arbitrary JavaScript execution across multiple Apple domains.

The vulnerability was initially exploitable on discussions.apple.com, and after Apple applied a partial fix, I identified a bypass that re-enabled the vulnerability across several international mirrors and additional domains — including the highly sensitive developer.apple.com/forums.

The vulnerability was validated by Apple Security, triaged internally, fully remediated, and later rewarded Apple Security Bounty.

#### #Affected Domains

The stored XSS was initially identified on:

discussions.apple.com

After the first fix by Apple, I discovered a bypass affecting additional domains:

developer.apple.com

discussions-jp-prz.apple.com

discussions-cn-prz.apple.com

discussionskorea.apple.com

discussionsjapan.apple.com

discussionschinese.apple.com

communities.apple.com

This confirmed a shared vulnerability across multiple assets using the same backend codebase but deployed independently.

#### #Vulnerability Type

Stored Cross-Site Scripting (Stored XSS)

Impact level: High

Attack Vector

User-controlled input inside forum posts/comments was not properly sanitized, allowing HTML injection and JavaScript execution.

#### #Steps to Reproduce

- Login to: [https://discussions.apple.com](https://discussions.apple.com)
- Navigate to: **Ask the Community**
- Create a new thread or post a comment
- Insert the payload:

The payload is encoded for safety and responsible disclosure

- Submit the post
- Anyone opening the thread immediately triggers JavaScript execution

#### #Note

During my research, I was able to **bypass the initial sanitization layer** that Apple implemented on the forum platforms.

Despite the presence of a cleaning mechanism intended to filter out dangerous input, I identified an alternate vector that successfully allowed the payload to pass through the filtering stage and become stored server-side.

After submitting the bypass, I confirmed that the injected content executed **automatically upon loading** the affected pages — including the highly sensitive **developer.apple.com/forums** domain — without requiring any user interaction, URL manipulation, or additional parameters.

This behavior proved that the sanitization was incomplete and that the vulnerability was still reachable through a previously unfiltered pathway.

Apple later acknowledged the bypass, applied a broader system-wide fix across all impacted assets, and fully remediated the issue.

The vulnerability was validated by Apple Security, triaged internally, fully remediated, and later rewarded with a **$5,000 Apple Security Bounty**.

#### #Apple Security acknowledged:

Link :[https://support.apple.com/en-ae/102774](https://support.apple.com/en-ae/102774)

#### #Timeline

March 31, 2025 — Initial Stored XSS reported, PoC and URL provided

April 5, 2025 — Apple confirms issue is valid

April 8, 2025 — Bypass identified and reported

April–May 2025 — Apple investigates patching across all assets

May 13, 2025 — Apple confirms full remediation

May 29, 2025 — Report qualifies for a Security Bounty

July 31, 2025 — Payment issued: $5,000

#### #Conclusion

This case was one of the most impactful and technically insightful vulnerabilities I’ve worked on.

What started as a simple stored XSS observation quickly escalated into a multi-domain security weakness affecting both community users and Apple developers worldwide.

Through continuous testing, responsible disclosure, and close collaboration with Apple’s Product Security team, the vulnerability was fully understood, patched across all affected assets, and confirmed resolved.

Receiving the $5,000 bounty and an official acknowledgment from Apple was a great honor, but the true value was the experience itself — proving once again that even small input fields can hide high-severity vulnerabilities when deployed at scale.

I hope this write-up provides useful insight for researchers looking to deepen their web security skills, and serves as a reminder of the importance of thorough testing, revisiting patches, and always thinking beyond the first layer of sanitization.

Thanks for reading,

**— Youssef Desouki (Zombie Hack)**

Security Researcher | Apple Security Bounty 2025

Linkedin : [https://www.linkedin.com/in/zombiehack/](https://www.linkedin.com/in/zombiehack/)
