# Mastering Logic Bugs

- **Source URL:** https://medium.com/@mahdisalhi0500/mastering-logic-bugs-a-checklist-for-bug-hunters-part-2-idor-6f411e90509d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250626060804/https://medium.com/@mahdisalhi0500/mastering-logic-bugs-a-checklist-for-bug-hunters-part-2-idor-6f411e90509d
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9212 (id 9212)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Mastering Logic Bugs: A Checklist for Bug Hunters PART 2 { IDOR 🐱👤}

## إِنَّ اللَّهَ وَمَلائِكَتَهُ يُصَلُّونَ عَلَى النَّبِيِّ يَا أَيُّهَا الَّذِينَ آمَنُوا صَلُّوا عَلَيْهِ وَسَلِّمُوا تَسْلِيمًا

2 min readMar 29, 2025

## **Salam Alikom, guys!** I hope you are doing well…❤

## Thank you for the motivation about this playlist! Today, I will share some good tips for IDOR. I have read from other hunters, and I will give you the full resources for these tips.

## I hope you enjoy this blog! Inshallah, I will make it easy to read, and I hope it helps someone.

## Lest Start

# Pull The Door

- ever time when you see id and when you change to victem id say no try **id=200&id=201** [*🚪*](https://h4ck.run/ctf/fawazeer-cyber?fbclid=IwY2xjawI82ppleHRuA2FlbQIxMQABHZPpFcz8XCX40MpJlsibkR9Xfkd--Ps0VFgrNd28cdY9_rimEi32BIn-tg_aem_vkhU8_Kw_bODmdvGkOwBzA#pr1v)
- Invite someone to your organization with **admin access**, but change the **organization ID** to the victim’s. This might let you gain elevated privileges! 💫 [Learn more](https://www.blogger.com/blog/post/edit/5008454893818540078/5814852115999410279#)
- Try this API path, it might lead to **P2 impact** → `/api/users?page=1&size=1` [👻 Learn more](/@bxrowski0x/how-to-find-idors-like-a-pro-158cf23baf23)
- Every time you see an **ID** in `PUT`, `POST`, or the **URL path**, try changing the **ID** or switching the request method (`PUT/POST/PATCH → GET`). This might expose vulnerabilities! [❤🤍 Learn more](/@esmailallali8/idor-vulnerability-discovered-exposes-pii-information-f6687cc1d7e2)
- Use **DevTools** to find hidden IDs and test for IDOR vulnerabilities! It can reveal useful information. [😀 Learn more](https://infosecwriteups.com/i-mean-idor-is-not-only-about-others-id-2d26115072ba)
- If finding **IDs** is hard and you want to see which endpoint provides them, just copy and paste the request into **Burp Intruder** to analyze the responses! [😀 Learn more](https://www.youtube.com/watch?v=Dd2t4jw9UZI)
- Try changing the **ID** to `-05458` → Sometimes it works and bypasses restrictions! [🔗 Learn more](/@0d-amr/unauthenticated-idor-in-employee-login-exposes-pii-to-more-than-100k-users-830fa8121b33)
- If token generation is possible, try different approaches to **get or manipulate tokens** for access! This can sometimes expose vulnerabilities. [🔗 Learn more](/@h4x0r_dz/paypal-idor-via-billing-agreement-token-closed-informative-payment-fraud-3245202fab38)
- When you see **callback** in URLs, it might be vulnerable to **IDOR** or **XSS** by bypassing ASP protections! Always test it. [⚠️ Learn more](https://www.youtube.com/watch?v=ojwEl4Rtw3Q)
- **SaaS integrations** might allow **IDOR-based downloads** to other users. [👊 Learn more](https://infosecwriteups.com/sensitive-data-leak-using-idor-in-integration-service-d9301be9c91e)
- Check if **cookies contain an ID parameter** — this could be vulnerable to IDOR! [🔗 Learn more](/@YourFinalSin/idor-how-i-leaked-data-of-50k-users-bc44201e777a)
- **Look for** `request_id` **values** in **Wayback URLs** and the **Internet Archive**—they might expose sensitive data! [🏌️♂️ Learn more](https://infosecwriteups.com/email-and-home-address-disclosure-using-unauthenticated-api-endpoint-worth-500-4a497ff0678c)

# Coming soon inshallah :

I have a Telegram channel where I share private POCs and live hacking sessions to help anyone find their first bug bounty. You don’t need to use any tools — just you and your mind! If you’re interested, send me a message on Telegram: [https://t.me/+lhoymPjQ8mI2YzA0](https://t.me/+lhoymPjQ8mI2YzA0).

## **Account Takeover (ATO)**

**Improper Access Control — Generic**

**mass assignment**

**OAuth Secret**

**tips form bug hunters**

**JavaScript Analysis**
