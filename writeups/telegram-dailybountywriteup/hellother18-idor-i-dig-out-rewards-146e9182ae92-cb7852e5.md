# IDOR

- **Source URL:** https://medium.com/@hellother18/idor-i-dig-out-rewards-146e9182ae92?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230725101351/https://medium.com/@hellother18/idor-i-dig-out-rewards-146e9182ae92
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3357 (id 3357)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR: “I Dig Out Rewards!” $$$

--

**Greetings**, readers! I’m Manthan, an 18-year-old passionate cybersecurity researcher, and today I’m sharing recently found IDOR vulnerability on a private program. let’s call that program xyz.com.

So, there I was, navigating through xyz.com, hoping to find some common bugs. The program had such a vast functionality that I felt like a tiny fish in a big ocean. But hey, I didn’t give up! One feature particularly caught my eye — the option to create and share QR codes with your team. The twist was, only team members were allowed to access that specific QR code. Challenge accepted!

With curiosity taking the lead, I decided to find a way around this limitation. After some exploration, I stumbled upon a small feature that allowed me to share the QR code via email. Ding! That’s when the “Idea Door” (IDOR) light bulb lit up in my mind.

Now, IDOR is like the cool magic trick of the cybersecurity world. It stands for **Insecure Direct Object Reference, where you can play around with parameters to access resources you shouldn’t be able to access. In this case, I got my hands on the ID parameter by capturing the request in Burp Suite. I changed the ID parameter and QR code for a different team member appeared in my email inbox.**

**Impact : U**nauthorized access to sensitive user data.

Reward with **$150** : )

**Well if you love this write up drop a clap 👏**

Thanks for reading !!
