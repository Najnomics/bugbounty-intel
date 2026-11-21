# $5375 Bounty

- **Source URL:** https://medium.com/@muriarfad/5375-bounty-idor-creating-a-share-link-for-any-campaign-planner-in-facebook-business-03f0994d4d16?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250719191638/https://medium.com/@muriarfad/5375-bounty-idor-creating-a-share-link-for-any-campaign-planner-in-facebook-business-03f0994d4d16
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10261 (id 10261)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# $5375 Bounty: IDOR — Creating a Share Link for Any Campaign Planner in Facebook Business Manager

This write-up details an Insecure Direct Object Reference (IDOR) vulnerability I discovered in the share link creation feature within Facebook Business Manager’s Campaign Planner. This vulnerability allowed me to generate a shareable link for another user’s campaign plan without proper authorization.

# Methodology: Service Analysis in Penetration Testing

When conducting penetration tests on web applications, it’s crucial to establish a clear schema and meticulously analyze each service involved. This approach entails mapping every “node” from the main application to its subsequent sub-nodes or related services. In this particular case, I identified that Facebook Business Manager incorporates an application known as “Campaign Planner.”

# Vulnerability Discovery: From CRUD Testing to Share Links

Initially, my focus was on performing IDOR testing against the CRUD (Create, Read, Update, Delete) operations within the Campaign Planner itself. The results of these tests indicated that all CRUD operations on campaign plans were securely implemented and were not vulnerable to IDOR flaws.

However, my investigation didn’t stop there. I subsequently discovered a sub-service of the Campaign Planner that specifically handled the functionality of sharing campaign plans and creating share links.

**This is where the vulnerability was found:** It turned out that the **create share link** feature was vulnerable to an IDOR flaw.

# Steps to Reproduce:

To reproduce this vulnerability, follow these steps:

1. **Prepare Two Accounts:** Log in to Facebook Business Manager using two distinct accounts.
2. **Create Campaign Plans:** In each account, create a separate campaign plan.
3. **Initiate Sharing (First Account):** From the first account, initiate the sharing process for the campaign plan you just created.
4. **Capture the Request:** Capture the HTTP request sent during the share link creation process (using a proxy tool like Burp Suite).
5. **Modify the Campaign Planner ID:** In the captured request, identify the parameter containing the campaign plan ID from the first account. Replace this ID with the campaign plan ID created by the second account.
6. **Send the Modified Request:** Send the modified HTTP request.

**Result:** The vulnerability is successfully exploited, you will receive a share link that actually points to the campaign plan belonging to the second account, even though the request originated from the first account, which should not have direct access to that campaign plan.

# Impact of the Vulnerability

This IDOR vulnerability allowed an attacker to create and distribute share links for campaign plans they should not have access to. While the immediate impact might not lead to arbitrary code execution or large-scale sensitive data exfiltration, it represents a significant breach of privacy and access control. An attacker could view details of campaign plans that are supposed to be private, potentially leading to reputational or strategic damage for businesses utilizing Facebook Business Manager.
