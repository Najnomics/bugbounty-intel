# Open Redirect to Xss

- **Source URL:** https://medium.com/@0x_karim/open-redirect-to-xss-d35eb8eb1cf4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250218040106/https://medium.com/@0x_karim/open-redirect-to-xss-d35eb8eb1cf4?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8822 (id 8822)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello, I’m 0x\_karim from Morocco, passionate about cybersecurity, particularly in discovering vulnerabilities in websites and applications. I enjoy analyzing systems, identifying weaknesses, and working on improving their security. I’m always eager to enhance my skills through continuous learning and participating in cybersecurity challenges. I believe in contributing to making the digital space safer for everyone.😊

let’s call the target test.example.com

1. the first thing I opened wayback machine for entered “\*.example.com” in search
2. “Ctrl + f” search for a word “=http”

After a While of searching throught records wayback

I found a link that has an open redirect vulnerabilty

It seems like this thing : ”https://test.example/redirect/?testURL=”

Since it is vulnerable to an open redirect, I decided to escalate the risk to XSS (Cross-Site Scripting)

I started by testing first “javascript:alert(1)” [https://test.example/redirect/?testURL=](https://web.archive.org/web/20250218040106/https://test.example/redirect/?testURL=)javascript:alert(1)

But the firewall blocks the payload, so I started trying to understand which word the firewall is blocking and looking for a bypass. I took control of the situation, and after an hour of trying, I found the solution

“**https://test.example.com/redirect/?testURL=javascript%3a%26%2337%26%2354%26%2349lert(1)**

Finally, the bypass succeeded, and the pop-up window appeared
