# How I Discovered a Hidden XSS and What I Learned

- **Source URL:** https://medium.com/@issam.qsous/how-i-discovered-a-hidden-xss-and-what-i-learned-9a34995ebbd2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240906044732/https://medium.com/@issam.qsous/how-i-discovered-a-hidden-xss-and-what-i-learned-9a34995ebbd2
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7163 (id 7163)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Discovered a Hidden XSS and What I Learned

Hello everyone! Sorry for not writing for over six months, but I’ve been busy since I started working at a company that focuses on physical security, like IP cameras and access controls. I’ve been diving into this new world, and to be honest, I was a bit unsure at first. As many of you know from my previous blogs, I’m passionate about ethical hacking and penetration testing. But so far, everything’s going smoothly, and I’m enjoying learning new skills every day.

Five months ago, when I moved to the US, I started getting into bug bounty hunting, and honestly, I’m hooked. It’s incredible to apply everything I’ve learned to real-world scenarios, test my skills, and earn good money. I chose a target and began testing. I follow a checklist during engagements or when hunting for bugs, so I was going through my usual process and methodology. At first, everything seemed secure, until…..

One day, I was reading an article about subdomain enumeration, and it mentioned a tool called Subfinder. Although it’s a standard tool that many hunters use regularly, I had never tried it myself, even though I knew about it and had studied its capabilities. So, I decided to give it a shot. To my surprise, Subfinder revealed a subdomain that I hadn’t discovered during my earlier enumeration. I started digging into this new subdomain, and guess what? I found an…
