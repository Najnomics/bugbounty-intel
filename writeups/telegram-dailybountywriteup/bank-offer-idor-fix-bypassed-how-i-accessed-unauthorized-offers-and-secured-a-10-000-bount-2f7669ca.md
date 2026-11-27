# Bank offer IDOR Fix Bypassed

- **Source URL:** https://bxmbn.medium.com/bank-offer-idor-fix-bypassed-how-i-accessed-unauthorized-offers-and-secured-a-10-000-bounty-41052b31a2fc?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250825031714/https://bxmbn.medium.com/bank-offer-idor-fix-bypassed-how-i-accessed-unauthorized-offers-and-secured-a-10-000-bounty-41052b31a2fc
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8872 (id 8872)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bank offer IDOR Fix Bypassed: How I Accessed Unauthorized Offers and Secured a $10,000 Bounty — @bxmbn

# Summary:

I discovered a **new weakness** in the offer retrieval functionality that allows an attacker to access unauthorized offers.

This issue is **bypassing the previous fix**, which was based on the vulnerability outlined in the article [*“I Received a Bank Offer in My Mailbox and Discovered an IDOR Vulnerability — $5,000 Bounty”*](/i-received-a-bank-offer-in-my-mailbox-and-discovered-an-idor-vulnerability-5-000-bounty-bxmbn-5209cab1fba8). (I suggest reading that first if you haven’t!)

While that vulnerability was addressed, this new issue stems from the server **accepting any valid access code** tied to a **reservation number**, leading to improper access control.

An attacker can use their own access code for their reservation to access offers belonging to other users. This new attack method undermines the intended security controls around offer access.

# Steps to Reproduce:

**Example of Vulnerability Exploitation:**

Let’s consider the following reservation details for an offer:

- **Your Reservation Number:** 0076448013416688
- **Your Access Code:** 481232

Now, let’s look at the attacker’s reservation details:

- **Attacker’s Reservation Number:** 0076448013416689
- **Attacker’s Access Code:** 531631

As you can see, the **reservation numbers** follow a predictable pattern. The attacker’s reservation ends in 89, while yours ends in 88. This indicates that reservation numbers like **0076448013416690**, **0076448013416691**, and **0076448013416692** belong to different users. This is where we spot the IDOR vulnerability, as the reservation numbers are enumerable.

Now, let’s consider the **Access Code**. While the access code appears to be random, I discovered that by using the attacker’s access code with your reservation number, the server grants the attacker access to your offer. Here’s how it works:

- The attacker doesn’t know your **Access Code**, but they can exploit your **Reservation Number** (0076448013416688).
- By substituting the attacker’s own access code (531631) with your reservation number, they are surprisingly granted access to your reservation.

So, By altering the reservation number and using the attacker’s access code, the attacker can access **any offer associated with the valid reservation numbers**

# Impact:

- **Unauthorized Access:** Attackers can gain access to **any user’s offer**, including sensitive details tied to specific reservations.
- **Data Exposure:** The attacker can view offers and related data that they are not authorized to access.
- **Potential Abuse:** An attacker could leverage this flaw to exploit user data and potentially cause reputational damage, financial loss, or data breaches.

Thank you for reviewing this writeup! . I will also be Answering any Questions in [https://x.com/bxmbn](https://x.com/bxmbn)
