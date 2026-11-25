# PortSwigger Access Control Notes

- **Source URL:** https://medium.com/@furkannyildiizz05/portswigger-access-control-notes-mass-assignment-and-idor-variants-c10b2a70cd50
- **Fetched from:** https://medium.com/@furkannyildiizz05/portswigger-access-control-notes-mass-assignment-and-idor-variants-c10b2a70cd50?source=rss-53768bce8ff1------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14941)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Furkannyildiizz / Fri, 09 Oct 2026 17:41:01 GMT

[🇹🇷 Türkçe okumak için tıklayın:](https://medium.com/@furkannyildiizz05/portswigger-access-control-masterclass-mass-assignment-ve-idor-%C3%A7e%C5%9Fitleri-440255ab46e4)

While progressing through the Access Control learning path on PortSwigger Web Security Academy, I solved three interconnected labs. In this write-up, I break down the exploitation steps and backend mechanics for Mass Assignment, basic IDOR, and GUID-based IDOR vulnerabilities.

1\. User Role Can Be Modified in User Profile (Mass Assignment)

Concept and Analogy:

Imagine filling out an address update form at a gym and handwriting “Membership: VIP” at the bottom. The front desk scans the document directly into the system without verifying payment or authorization.

Walkthrough:

1. Logged in with the provided credentials (wiener:peter) and navigated to /my-account.

2. Submitted an email change request to trigger the profile update functionality.

3. Located the POST /my-account/change-email request in Burp Suite’s HTTP history and forwarded it to Repeater (Ctrl + R).

4. Noticed the default “roleid”: 1 structure in the JSON body and modified the payload to include “roleid”: 2:

{“email”: “[test@test.com](mailto:test@test.com)”, “roleid”: 2}

5\. Pressed Send; the server accepted the request and reflected “roleid”: 2 in the response.

6. Refreshed the page to load the Admin Panel link, navigated to the panel, and deleted user carlos to complete the lab.

Root Cause:

The backend framework automatically binds untrusted JSON input directly to internal data models without parameter whitelisting (Mass Assignment).

2\. User ID Controlled by Request Parameter (Basic IDOR)

Concept and Analogy:

Asking a hotel receptionist for the key to Room 101 and receiving it without ID verification. Then asking for Room 202’s key and receiving that one as well without any question.

Walkthrough:

1. Authenticated as wiener:peter and opened the profile page.

2. Checked Burp Suite’s HTTP history to identify the account retrieval request: GET /my-account?id=wiener

3. Sent the request to Repeater and replaced id=wiener with id=carlos.

4. Hit Send to receive Carlos’s profile page containing his API key, which I submitted to complete the lab.

Root Cause:

The backend retrieves records using the client-supplied id parameter without verifying whether the authenticated session user matches the requested account.

3\. User ID Controlled by Request Parameter, with Unpredictable User IDs (GUID IDOR)

Concept and Analogy:

The hotel replaces simple room numbers (101, 102) with complex alphanumeric codes (A9-X7-K2). While harder to guess, the receptionist still fails to check IDs — meaning anyone who spots a room code on a bulletin board can claim access.

Walkthrough:

1. Logged in as wiener:peter and observed a complex GUID assigned to my account URL (/my-account?id=YOUR-GUID).

2. Sent the profile request to Repeater. To target Carlos, I needed to retrieve his GUID through reconnaissance.

3. Browsed the main blog page and located a post written by carlos.

4. Clicked on the author profile link and inspected Burp’s HTTP history to extract Carlos’s GUID (/blog?userId=carlos-guid).

5. Replaced my GUID in Repeater with Carlos’s GUID and sent the request.

6. Extracted Carlos’s API key from the HTTP response body and submitted it as the final solution.

Root Cause:

Relying on unpredictable identifiers like GUIDs creates a false sense of security (Security through Obscurity). Without server-side authorization checks, obtaining a target’s identifier leads directly to unauthorized access.

Remediation Strategies

- Mass Assignment: Use strict Data Transfer Objects (DTOs) and explicitly whitelist editable fields on profile update endpoints.

- IDOR: Implement strict server-side authorization checks to verify that the authenticated session owns the requested object (Session.UserID == RequestedObject.OwnerID).
