# From API Access Bypass to Campaign Takeover

- **Source URL:** https://medium.com/@udaytrivedi35/from-api-access-bypass-to-campaign-takeover-e20c7db6c999
- **Fetched from:** https://medium.com/@udaytrivedi35/from-api-access-bypass-to-campaign-takeover-e20c7db6c999?source=rss-20a92da8d7f0------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14875 (id 14875)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Udaytrivedi / Wed, 26 Aug 2026 14:29:26 GMT

During one of my security tests, I found an interesting chain involving **API access, 2FA bypass, and privilege escalation**.

The application normally doesn’t give users direct API access. According to the API documentation, you first have to request API access. So initially, I assumed this was another security boundary that I would have to go through.

While testing the application, I found another subdomain related to the API. What caught my attention was that this flow only required the **victim’s email address** to provide API access.

So the first part of the chain was basically:

**Victim email → API access obtained**

After getting API access, I started looking at the authentication flow. I found that I could obtain the API token using the victim’s username and password.

The interesting part was that **2FA was not enforced when getting the token**.

Normally, the flow should have been:

**Username + Password → 2FA → API Token**

But instead, it was:

**Username + Password → API Token**

At this point, I wanted to see what I could actually do with the token instead of stopping at the 2FA bypass.

While testing the API, I found a campaign invitation endpoint where I could specify the user’s campaign and invite an email with a specific role.

I tested whether I could invite my own account as OWNER.

And it worked. 👀

I could then accept the invitation from my account and remove the legitimate user from the campaign.

So the complete chain became:

Victim Email

↓

API Access Bypass

↓

Username + Password

↓

2FA Bypass

↓

API Token

↓

Invite Attacker as OWNER

↓

Remove Victim

↓

Campaign Takeover 🚨

The interesting part wasn’t just the 2FA bypass.

If I had stopped after getting the API token, I would have missed the bigger impact.

The important thing was following the access I gained and checking **what privileged actions I could perform with it**.

This is something I’ve started paying more attention to while testing APIs:

***Don’t stop when you find the bypass. Follow the chain and see where it can actually take you.***

In this case, a combination of multiple weaknesses turned an API access issue into a **full campaign takeover**.

Target details have been redacted for responsible disclosure.
