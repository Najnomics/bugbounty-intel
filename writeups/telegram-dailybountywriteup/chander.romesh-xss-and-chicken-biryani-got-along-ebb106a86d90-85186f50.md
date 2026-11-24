# XSS and chicken biryani got along.

- **Source URL:** https://medium.com/@chander.romesh/xss-and-chicken-biryani-got-along-ebb106a86d90?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230311183710/https://medium.com/@chander.romesh/xss-and-chicken-biryani-got-along-ebb106a86d90
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1785 (id 1785)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS and chicken biryani got along.

Food for thought.

It was wordpress website this time. They had implemented WPE W.A.F to block all xss payloads. No \</ , no encoding , no script kiddie stuffs.

One thing I noticed was when I use flower bracket { the application accepts the input. No blocking. Since, the app did not break / sanitize the flower bracket { i was curious to check if its vulnerable for SSTI and CSTI {{7\*7}} but no .

# Silver lining during challenges.

I went for lunch break with frustration ordered chicken biryani which costed ₹100. He said no egg, no baingan which led to more frustration. After collecting the plate I looked around and noticed all tables were full. Those pricks who don’t move out of the place even after completing the meal \*sighs\*. After managing to complete the meal. I came to desk opened the application and reminded of the XSStriker tool which i read long back.

# **The Trigger**

I installed XSStriker tool [https://github.com/s0md3v/XSStrike](https://github.com/s0md3v/XSStrike) . This is really simple to install and use tool. Follow the instruction.

All you have to do is go to the tool directory cd /yourdirectory/xssstrike

Run python3 xsstrike.py -u example.com/vulnerableparameter and wait for the magic payloads to flash on your screen.

Now copy the vulnerable url and past it in the browser to see the magic xss pop-up.

Never stop just because some of the payloads gets stopped by WAF. Like everyone says recon is important. Do the information gathering about the target like the web server details, CMS etc which will help you understand the target better. Apart from just Burp suite i always check for tools based out from linux and use browser extensions which will solve the purpose soon .
