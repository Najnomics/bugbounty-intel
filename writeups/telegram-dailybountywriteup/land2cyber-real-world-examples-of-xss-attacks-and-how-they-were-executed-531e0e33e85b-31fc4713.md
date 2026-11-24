# Real-world examples of XSS attacks and how they were executed

- **Source URL:** https://medium.com/@Land2Cyber/real-world-examples-of-xss-attacks-and-how-they-were-executed-531e0e33e85b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126143039/https://medium.com/@Land2Cyber/real-world-examples-of-xss-attacks-and-how-they-were-executed-531e0e33e85b
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4184 (id 4184)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Real-world examples of XSS attacks and how they were executed

Cross-Site Scripting (XSS) attacks have been a persistent threat to web applications, with real-world examples demonstrating their potential for wreaking havoc on unsuspecting users and website owners. In this article, we’ll explore some prominent instances of XSS attacks, how they were executed, and the consequences they had. By understanding these examples, we can better appreciate the importance of mitigating XSS vulnerabilities and maintaining web application security.

1. **MySpace “Samy” Worm (2005)**

**Execution**

Samy Kamkar, a security researcher, executed one of the most famous XSS attacks by creating a worm that spread across MySpace, a popular social networking site. Kamkar injected JavaScript code into his profile, which, when viewed by other users, added them as friends and promoted his profile.

**Consequences**

The “Samy” worm infected over a million profiles within a matter of hours, leading to slow site performance and considerable disruption. MySpace had to temporarily shut down to address the issue.

2\. **Twitter Worm (2009)**

**Execution**

A hacker used a stored XSS vulnerability in Twitter to create a worm that exploited the “onmouseover” event of links. When users hovered over these links, the worm retweeted itself, causing it to spread.

**Consequences**

The worm affected numerous Twitter users and caused embarrassment for the social media platform. Twitter had to take immediate measures to address the vulnerability.

3\. **XSS on Google’s Blogspot (2015)**

**Execution**

A security researcher found an XSS vulnerability in Google’s Blogspot service. Attackers could execute arbitrary JavaScript code on Blogspot-hosted sites by injecting malicious code into the comments section.

**Consequences**

This vulnerability allowed attackers to deface websites and potentially steal user data, damaging the reputation of Blogspot. Google swiftly patched the vulnerability.

**4. XSS on Yahoo (2017)**

**Execution**

Yahoo’s popular email service was affected by a persistent XSS vulnerability. Attackers could send malicious emails containing JavaScript that, when opened, would execute in the recipient’s email client.

**Consequences**

This vulnerability put Yahoo email users at risk of having their accounts compromised and their personal information exposed. Yahoo took steps to rectify the issue, but not before it had been exploited by malicious actors.

**5. Uber’s P3 XSS Vulnerability (2019)**

**Execution**

A security researcher discovered an XSS vulnerability in Uber’s website. The attacker could craft a link that, when clicked by an Uber driver, would expose their account details and allow unauthorized actions.

**Consequences**

This vulnerability posed a significant risk to Uber drivers and their personal information. Uber responded promptly to fix the issue and enhance its security measures.

**6. WhatsApp Web XSS (2020)**

**Execution**

A security researcher found an XSS vulnerability in WhatsApp’s web client. The attacker could send a specially crafted message containing malicious code. When the recipient viewed the message in the web client, the code would execute.

**Consequences**

This vulnerability could have allowed attackers to compromise users’ data and potentially take control of their accounts. WhatsApp addressed the issue to protect its users.

These real-world examples of XSS attacks highlight the need for ongoing vigilance in the realm of web application security. Whether it’s through MySpace, Twitter, Google, Yahoo, Uber, or WhatsApp, XSS vulnerabilities have shown their potential to cause widespread disruptions and compromise user data. Web developers and organizations must continuously scan for and address these vulnerabilities to protect users and maintain the integrity of their platforms.

Understanding how XSS attacks are executed and their consequences serves as a stark reminder that cybersecurity is an ever-evolving field, and the battle against such threats is far from over. As technology advances, so too do the tactics of those who seek to exploit its vulnerabilities. It is incumbent upon the tech community to remain proactive and vigilant in the face of these ever-present challenges.
