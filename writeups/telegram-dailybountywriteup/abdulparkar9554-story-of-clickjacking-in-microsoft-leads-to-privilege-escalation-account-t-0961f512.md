# Story of Clickjacking on Microsoft Leads To Privilege Escalation & Account Takeover Of Admin

- **Source URL:** https://medium.com/@abdulparkar9554/story-of-clickjacking-in-microsoft-leads-to-privilege-escalation-account-takeover-of-admin-a04453ed47fc?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230725043259/https://medium.com/@abdulparkar9554/story-of-clickjacking-in-microsoft-leads-to-privilege-escalation-account-takeover-of-admin-a04453ed47fc?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3302 (id 3302)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Story of Clickjacking on Microsoft Leads To Privilege Escalation & Account Takeover Of Admin

--

Hello researchers,

I hope you all are doing well. My name is [**Abdul Rehman Parkar**](https://web.archive.org/web/20230725043259/https://www.linkedin.com/in/abdulrehmanparkar/?originalSubdomain=in), and I work at **IZYITS**.

Today, I am going to share with you how I discovered a high severity clickjacking in one of Microsoft’s well-known products. So let’s begin.

So, after getting duplicate of the high-severity clickjacking vulnerability on Facebook/Instagram, I decided to take a two-day break. Then, I thought, “Why not try to find the same vulnerability on Microsoft?”

Microsoft has several portals, so I searched for “Microsoft portals” on Google, and I came across a link: [https://msportals.io/](https://web.archive.org/web/20230725043259/https://msportals.io/).

This website contained links to all Microsoft portals. I started visiting each portal and began checking if any of them were vulnerable to clickjacking, which could pose a high security risk if exploited.

During my search, I found some URLs that were vulnerable, but they didn’t offer anything particularly interesting for exploitation.

If I were to report these vulnerabilities, they would likely be considered informative but not critical. However, I was looking for something more high severity and sensitive.

Finally, I found three portals, out of which two were the same but with different names: [**admin.microsoft.com**](https://web.archive.org/web/20230725043259/https://admin.microsoft.com/), [**portal.office.com/adminportal/**](https://web.archive.org/web/20230725043259/https://portal.office.com/adminportal/) and **portal.microsoftonline.com/account#personalinfo.**

These portals were storing quite sensitive data. Upon further investigation, I discovered that the first two portals had options for creating, deleting, and managing user roles etc.

I created a payload that demonstrated how a normal user could use clickjacking to elevate their privileges and become a global admin, gaining access to all organization portals.

Additionally, I presented another proof of concept in which I explained how an attacker could add their email to the admin’s alternate email and reset the password, thereby taking over the admin’s account using clickjacking.

After discovering the privilege escalation vulnerability in the portals **admin.microsoft.com and portal.office.com/adminportal** (since they were the same), I created a report for that issue.

Additionally, I created another report for the account takeover vulnerability in the portal **portal.microsoftonline.com/account#personalinfo.**

Within one day, the first report went into the review process. Surprisingly, within a day, without any status change in the report, the vulnerabilities in all three portals were fixed.

However 2nd Report I submitted are still showing as “New” and have not been updated yet.

Afterward, I received a response from Microsoft regarding my first report, and they marked its status as “Complete.”

The response received after the fix stated that it does not meet their bar for immediate servicing.

This was quite disappointing for me because it has a high impact, and most users don’t have a background in cybersecurity, being unaware that such attacks are possible.

They don’t even think twice before clicking on something, especially when a website offers rewards. But even if 10 out of 100 organizations were affected by this attack and the attacker successfully gained access to their portals, it could result in a complete compromise of their data, causing significant losses.

Moreover, people might think that the administrator of the portal was responsible for the breach, further increasing the risk. Therefore, it is a high-risk vulnerability.

Microsoft places great emphasis on securing their customers’ data, and customer data and security are important to them. That’s why they fixed this vulnerability within a day. However, it is disappointing that they consider the severity of this vulnerability as moderate, despite the demonstrated impact of how an attacker can take over an organization.

\# No Bounty Rewarded

POC 1 : Microsoft Admin Privilege Escalation

POC 2 : Microsoft Admin Account Takeover

I hope you find my write-up informative.

Thanks.
