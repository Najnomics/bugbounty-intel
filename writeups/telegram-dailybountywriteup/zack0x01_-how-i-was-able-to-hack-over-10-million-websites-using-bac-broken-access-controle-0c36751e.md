# How i was able to hack over 10 million websites using BAC

- **Source URL:** https://medium.com/@zack0x01_/how-i-was-able-to-hack-over-10-million-websites-using-bac-broken-access-controle-ce6b704e3dcb?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251119083610/https://medium.com/@zack0x01_/how-i-was-able-to-hack-over-10-million-websites-using-bac-broken-access-controle-ce6b704e3dcb
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5370 (id 5370)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hey awesome hackers, I’m Zack0x01, and today I’m excited to tell you about an amazing discovery I made while searching for bugs. Get ready for a thrilling story about a popular web hosting platform with 10 million websites.

Thanks to some luck and my hacking skills, I found a major security hole called a broken access control vulnerability. It let me access any website on their platform without permission. And the best part? I got free domains, web hosting, servers, and email accounts. Interested? Let’s explore how it all works.

Unlike some bug hunters who spend a lot of time gathering information, I chose to jump right into testing the application’s features. I started by trying out a technique called XSS, where I inserted a carefully designed code into the system to see how it reacts.

(“‘>\</textarea>\</div>\</script>\<script>prompt(1)\</script>\<img\src=x onerror=confirm(1)>)


I tried injecting my code into different parts of the system, like usernames, full names, descriptions, and WHOIS setting records. Sadly, my XSS attempts didn’t work as I hoped.

Undeterred, I switched my focus to finding broken access control vulnerabilities. Since the platform was a web hosting service, I came up with a plan. I got two domain names, let’s say domainone.com and domaintwo.com, using different accounts. Here’s where things got interesting.

I used the platform’s AI website builder to change the website name on my landing page to the second account’s domain. But, doing it manually wasn’t my style. I turned to Burp Suite, a helpful tool in hacking. Using its match and replace feature, I smoothly swapped every instance of domainone.com with domaintwo.com, all without much effort.

With my setup ready, I carefully designed my landing page. Meanwhile, Burp Suite handled the domain switch. After customizing the page, I stopped Burp Suite and went to the second account’s domain — domaintwo.com. Get ready for the surprise: I not only got access but also took control of the other account’s domain settings. I uploaded new pages, adjusted settings — it was a hacker’s dream scenario.

reported on 20/01/2024

triaged same day

bounty on $$$$ 04/02/2024


Thanks for joining me on this exciting bug bounty journey. Stay tuned for more detailed explanations as we explore further into the world of hacking. Until next time, happy hacking!

**Tap into my world , follow me on :**

🕶️ [Instagram](https://www.instagram.com/zack0x01)

👁️ [Twitter (X)](https://x.com/zack0x01)

🕳️ [Medium](/@zack0x01_)

🔥Check out my YouTube channel here🔥 [https://www.youtube.com/@ZACK0X01](https://www.youtube.com/@ZACK0X01)

Stay lurking. Stay hacking. 🖤💻
