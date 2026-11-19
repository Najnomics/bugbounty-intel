# Bug Bounty Findings

- **Source URL:** https://medium.com/@maakthon/bug-bounty-findings-10-major-vulnerabilities-exposed-in-cloverleafs-application-idor-part-2-932746b6b445?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241213210831/https://medium.com/@maakthon/bug-bounty-findings-10-major-vulnerabilities-exposed-in-cloverleafs-application-idor-part-2-932746b6b445
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8169 (id 8169)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bug Bounty Findings: 10 Major Vulnerabilities Exposed in Cloverleaf’s Application - IDOR - Part 2

Welcome to the second part of my series on security issues found in Cloverleaf’s web application (app.cloverleaf.me). In this article, I’ll talk about **Insecure Direct Object References (IDOR)** — a serious problem that allows attackers to access or change data they shouldn’t be able to. Following Part 1, where I explained [**Open Redirect**](/@maakthon/bug-bounty-findings-10-major-vulnerabilities-exposed-in-cloverleafs-web-application-part-1-95f659ff7d0a), this article will show how IDOR vulnerabilities were discovered, why they are dangerous, and how they can be fixed.

## **Vulnerability Findings:**

**Vulnerability 2: Insecure Direct Object Reference (IDOR)**

**What is IDOR vulnerability:**


IDOR (Insecure Direct Object Reference) is a type of security vulnerability that occurs when an application exposes direct access to objects (database records, files, or resources) based on user-supplied input, without properly verifying whether the user is authorized to access that object.

**Description:**


The application is vulnerable to an Insecure Direct Object Reference (IDOR) in the billing page of the application, where an attacker can manipulate the *organizationId* parameter to gain unauthorized access to sensitive billing information for other organizations. This issue arises because the server does not validate whether the authenticated user has the necessary permissions to access the data tied to a specific *organizationId*.

**How Was It Identified:**


While browsing the web application, I came across a billing page with the following path:

`https://myorg.cloverleaf.me/billing?planId=team_monthly&organizationId=123`
I noticed that the *organizationId* parameter was numeric and guessed it could be easily manipulated. Testing this hypothesis, I modified the value of *organizationId* to other numbers and observed that the server granted access to billing details of unrelated organizations.

To facilitate discovery, I found an additional endpoint in API:

`/api/organizations/validate`
This endpoint accepted a subdomain parameter in a POST request and returned the corresponding organization’s ID in the response. By systematically querying this endpoint, I could map the organizationId of any organization, making it trivial to exploit the IDOR vulnerability.

**Impact:**


1. **Access to Sensitive Billing Information:** An attacker can view billing details, including the number of users in the organization and other payment details.
2. **Privacy Violation:** Attackers can infer organization-specific information, such as team size and payment amounts.
3. **Potential Financial Exploitation:** If the attacker manipulates the checkout process, they could disrupt billing or impersonate another organization during payment.

**Mitigation:**


1. Access Control Validation:

- Ensure that the backend validates whether the authenticated user has permission to access the resource associated with the organizationId.

2\. Avoid Exposing Predictable IDs:

- Replace numeric or easily guessable organizationId values with non-sequential, globally unique identifiers (GUIDs).

**References:**


Tools used: [Burp Suite Community Edition](https://portswigger.net/burp/communitydownload)

LinkedIn : [https://www.linkedin.com/in/abdalkarim](https://www.linkedin.com/in/abdalkarim/)
