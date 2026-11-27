# No rate limit to 2FA bypass

- **Source URL:** https://medium.com/@bug.hun3r/no-rate-limit-to-2fa-bypass-1d7ad12a86f0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105162708/https://medium.com/@bug.hun3r/no-rate-limit-to-2fa-bypass-1d7ad12a86f0
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4373 (id 4373)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
2FA bypass

🤧 I was not getting any bug, if I got they marked as duplicate or NA. But I remember consistency > perfection, so I started again and got $100 bounty, want to know how? Let’s get started.


🚀 In a bug bounty program I signed up and set up my account. Now the thing start from here …


# 1. In a security step I was asked to add my phone number.

# 2. As I clicked add phone number, a OTP is delivered.

# 3. Now I need to enter it for 2FA, if I didn’t do I would not able to access other settings.

# 4. I entered the OTP 000000 and intercepted the submit OTP request in burp proxy.

# 5. Then sent it to intruder tab and for demonstration I generated 70 payloads.

# 6. Every request was 200 OK with the message “OTP is incorrect”

## 🥸 In this way the attacker could bypass 2FA and can add victim’s phone number to his account without victim’s consent.

Consistency > Perfection ✌️
