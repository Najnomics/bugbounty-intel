# New Web Feature gone wrong | SQL-Injection

- **Source URL:** https://medium.com/@Charon19d/new-web-feature-gone-wrong-sql-injection-3fcd07ff65f2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260102144328/https://medium.com/@Charon19d/new-web-feature-gone-wrong-sql-injection-3fcd07ff65f2
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/12228 (id 12228)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **New Web Feature gone wrong | SQL-Injection**

**Introduction**


*Hey, this is Charon a security researcher and aspiring penetration tester. Today, I want to share a real vulnerability I discovered last week. The goal of this write-up is not just to talk about the bug itself, but to give you insight into how I think during a hunt, so you can apply the same mindset in your own testing.*

**The Hunt**


L*ast week, I was hunting on an education platform for a client. Like everyone else, I started with the basics: reconnaissance, discovery, information gathering, enumeration, and digging deep into the main domain and its subdomains.*

*I explored features, endpoints, and different application flows but everything looked solid. No obvious misconfigurations, no easy wins. After spending a good amount of time, I started feeling stuck.*

*I even tried automation tools, but as we all know, automation doesn’t always work. Sometimes it’s skill, sometimes it’s timing, and sometimes it’s just luck.So I stopped for the day.*

*The next day, I decided to start again this time with a fresh mindset. I visited the homepage once more, and that’s when I noticed something new. It looked like a recently added feature.*

*This feature allowed students to enter their personal details and exam marks. After submitting the form, the platform would tell them whether they were eligible or not.*

*At first glance, everything worked normally. I submitted random data, and the result said I was not eligible which was expected. But something caught my attention.*

*The response redirected me to a page ending with thankyou.php. That single detail was enough to trigger curiosity.*

*I opened Burp Suite to analyze the request and understand how data was being sent from the client to the server. That’s when things started to get interesting.*

*I noticed that user input was being sent directly to the backend, and the behavior strongly suggested a database interaction. At this point, I didn’t waste time guessing.*

*I tested for injection.*

*Using crafted payloads (with some help from AI for speed), I confirmed it was a Blind SQL Injection. This meant data could only be extracted using true/false responses, not direct output.*

*Still, that was more than enough.*

*I quickly automated but there was a firewall as soon i start, It get detected and block me so i was having trick to bypass the detection and then i started using random user agent on each request exploitation using sqlmap.*

*The result was shocking.*

- *71 databases were accessible*
- *Sensitive data included:*
- *Student records*
- *Faculty details*
- *User credentials*
- *Admin and web panel login information*

*If a malicious actor had discovered this, it could have resulted in a large scale data breach and serious damage to the organization and its users.*

*I immediately stopped further exploitation, collected only the required proof, and prepared a professional vulnerability report.*

*I contacted the organization and submitted the report the same day. They acknowledged the issue and forwarded it to their security team for patching and mitigation. That’s exactly how responsible disclosure should work.*

*This was one of many real vulnerabilities I’ve found, and I wanted to share this story to show that bugs don’t always come from complex attacks. Sometimes, they come from patience, curiosity, and simply looking at the application one more time.*

*If you enjoyed reading this, feel free to connect with me on LinkedIn. My goal is simple: learn continuously, share knowledge, and contribute to making computer systems more secure.*

*Thank you for reading.*
