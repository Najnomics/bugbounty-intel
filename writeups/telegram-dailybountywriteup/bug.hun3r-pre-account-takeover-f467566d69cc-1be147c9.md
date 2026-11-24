# Pre account takeover

- **Source URL:** https://medium.com/@bug.hun3r/pre-account-takeover-f467566d69cc?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231012161205/https://medium.com/@bug.hun3r/pre-account-takeover-f467566d69cc
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3965 (id 3965)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Pre Account Takeover

--

No rate limit on OTP verification

I got a target from google dork, on which I started hunting.

My approach is to give my 💯 % in recon part.


# 🎊Steps to reproduce-

1\. I went to shodan and simply searched target.com

2\. I got number of IPs, after checking them. I got one which shows account creation🥸

3\. The functionality was simple that is enter phone number > click on get OTP > enter OTP to verify✌️

4\. There was two flaws one is no rate limit on getting OTPs which can be used to launched bombing attack🔥

5\. But the second flaw was that after getting OTP on a random phone number, they asked me to enter the OTP for verification👋

6\. I started burp suite and entered 4 digits wrong OTP > intercept the request > send it to intruder🎉

7\. Then selected number payloads > add OTP’s value of the URL (OTP=$0000$) > generate payloads from 0000 to 9999👶

8\. I checked every response of the request its 200 OK 👍 (entered OTP is wrong)💥

9\. But one OTP got hit and this leads to pre account takeover🫂
