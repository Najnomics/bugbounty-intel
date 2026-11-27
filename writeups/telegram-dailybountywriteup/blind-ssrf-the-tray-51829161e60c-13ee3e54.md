# Blind SSRF - The Tray

- **Source URL:** https://p4n7h3rx.medium.com/blind-ssrf-the-tray-51829161e60c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126141835/https://p4n7h3rx.medium.com/blind-ssrf-the-tray-51829161e60c
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3458 (id 3458)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Blind SSRF — The Tray

Hi fellow hunters, in this write-up, I will explain how I found a Blind SSRF and got a red bull tray as a reward. The Redbull Bug Bounty program is on Intigriti’s Platform.

**Summary:**

Blind SSRF is a type of SSRF attack where the attacker cannot see the response from the server. This makes it more difficult to exploit, but it is still possible to use blind SSRF to gain access to sensitive information or to cause a denial of service.

One way to exploit blind SSRF is to use a technique called “tunnelling.” Tunnelling allows the attacker to send arbitrary commands to the server, even though they cannot see the response. Blind SSRF can be a very powerful attack, and it is important to be aware of it in order to protect your applications.

For this finding, I used an extension of BurpSuite known as Collaborator Everywhere and I also used Collaborator Client. So I’ll be discussing both of them here.

**How to add Collaborator Extension in your BurpSuite?**

1. Start your BurpSuite
2. Go to the extender and click on BApp Store
3. Find the extension

4\. Install it to your BurpSuite

One of the easiest ways to find Blind SSRF vulnerabilities is the out-of-band technique which means using an external server to find blind vulnerabilities. That external server should be under your control and can be used to monitor network interactions with the system.

If you don’t want to set up your own server then you can use [Burp Collaborator](https://portswigger.net/burp/documentation/collaborator).

**How I found this vulnerability?**

1. I went to my target website and navigated to robots.txt, In the background Collaborator Everywhere Plugin was enabled. I got a DNS pingback through referer header.
2. I Intercept the endpoint because I got DNS pingback from robots.txt and send it to the repeater.
3. While I was thinking about how to get HTTP Pingback I changed the hostname with my burp collaborator and Boom !! i got HTTP Pingback from the backend Server. I injected burp Collab link in referer and host header.

**Final Note**

Thank you very much for your attention and I wish you good luck in finding as many bugs as possible and getting big rewards!
