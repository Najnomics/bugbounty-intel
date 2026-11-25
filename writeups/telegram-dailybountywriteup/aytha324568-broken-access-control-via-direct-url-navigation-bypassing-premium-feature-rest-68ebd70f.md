# Broken Access Control via Direct URL Navigation

- **Source URL:** https://medium.com/@aytha324568/broken-access-control-via-direct-url-navigation-bypassing-premium-feature-restrictions-6a190457ddfe
- **Fetched from:** https://medium.com/@aytha324568/broken-access-control-via-direct-url-navigation-bypassing-premium-feature-restrictions-6a190457ddfe?source=rss-2f09348bf5f9------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14967)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** A_box4 / Mon, 02 Nov 2026 00:42:27 GMT

يَرْفَعِ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ مِنكُمْ وَٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ دَرَجَـٰتٍ ۚ وَٱللَّهُ بِمَا تَعْمَلُونَ خَبِيرٌ

Modern SaaS applications often rely on subscription-based access controls to restrict premium features to users with paid plans. These restrictions should be enforced on both the frontend and backend to prevent unauthorized access.

During security testing of a web-based AI video creation platform, a Broken Access Control vulnerability was identified in the Personal Avatar creation workflow.

Initially, the Personal Avatars feature appeared restricted to premium subscribers. Free-tier users attempting to access it through the normal interface were presented with an upgrade prompt.

However, further investigation revealed multiple weaknesses in the subscription enforcement mechanism. By manipulating client-side responses and accessing the dedicated avatar recording route directly, it was possible to bypass the frontend restrictions and access the premium creation workflow using a free-tier account.

Further testing also revealed that the application allowed the creation of more than the advertised limit of five Personal Avatars.

The application failed to properly enforce subscription-based access restrictions on the Personal Avatar creation workflow.

Using Burp Suite’s **Match and Replace** feature, I modified the subscription value in the response body:

This caused the Pro features, including **Personal Avatars**, to appear in the UI. However, the feature was still inaccessible.

After inspecting the Burp Suite HTTP history, I discovered the direct creation route:

/#/avatars/record/

Accessing this route directly allowed me to bypass the frontend restriction and access the Personal Avatar creation workflow.

Further testing revealed that I could exceed the advertised limit of five Personal Avatars. I also reproduced the issue using a separate free-tier account in another browser, without any Match and Replace modifications, and successfully created more than five avatars.

5\. Manually navigate to this route through the browser’s address bar. Observe that the Personal Avatar creation interface becomes accessible.

6\. Continue testing the creation workflow and discover that it is possible to exceed the advertised limit of five Personal Avatars associated with the Pro plan.

7\. To verify that the issue does not depend on Match and Replace, open a completely separate browser and log in using another free-tier account, without applying any response modifications.

8\. Directly access the same route:

9\. Observe that the free-tier account can also access the Personal Avatar creation workflow and create more than five Personal Avatars without having a Pro subscription.

The identified weaknesses could have significant security and business consequences.

The underlying issue is the lack of consistent server-side authorization and subscription entitlement validation. Subscription tiers, feature permissions, and usage limits must be verified independently by the backend rather than relying on client-side response values or frontend navigation restrictions.

Written by **A\_box4**

CTF Player | Bug hunting | web pentest

contact me:
