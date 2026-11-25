# IDOR(Insecure Direct Object Referece) Price Manipulation Through Encoded Url Parameter

- **Source URL:** https://medium.com/@bry4nzheng/idor-insecure-direct-object-referece-price-manipulation-through-encoded-url-parameter-4232fa4758b0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240219021210/https://medium.com/@bry4nzheng/idor-insecure-direct-object-referece-price-manipulation-through-encoded-url-parameter-4232fa4758b0?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5265 (id 5265)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Price Manipulation Through Encoded Url Parameter on Private Program

--

**Introduction:**

Upon scrutinizing the payment invoice URLs within the platform’s ecosystem, an unsettling discovery surfaced. It became apparent that the encoded data embedded within these URLs, upon decoding, divulged sensitive information, notably pricing details. Although implemented as a security measure, the base64 encoding technique inadvertently unveiled a vulnerability. This loophole permits malicious actors to exploit the URL parameters, specifically the pricing components, thereby manipulating the payment amount to their advantage.

**Discovery:**

The revelation of this vulnerability stemmed from a thorough examination of the platform’s payment invoice URLs. Upon decoding the encoded information within these URLs, it became evident that crucial details, including pricing information, were exposed. This discovery raised significant concerns regarding the platform’s security posture, as the base64 encoding method, while intended to enhance security, inadvertently facilitated the unauthorized manipulation of payment parameters within the URLs.

**Exploitation:**

Subsequent exploration and experimentation led to the exploitation of this vulnerability. By manipulating the decoded parameters within the payment invoice URLs, particularly the pricing values, attackers could adjust the payment amount to their liking. This exploitation involved decoding the URL, modifying the pricing parameters to meet specific criteria (e.g., minimum value of 100), and re-encoding the manipulated URL. Through this process, attackers could effectively bypass payment restrictions and manipulate the payment amount to defraud the system.

Begin by visiting the checkout page using the URL provided by the platform. Once there, proceed with selecting any product and completing the checkout process. After the checkout is completed, an invoice will be sent to your email address. Copy the invoice link from the email.

Next, decode the base64-encoded URL found after the **/invoicing/pay?**

Original URL

Change the price value into 100

Copy the manipulated value encoded url

Once the pricing parameters are modified, encode the URL back into base64 format. Finally, replace the existing URL in the address bar with the modified, encoded URL. Navigate to the URL to submit the modified payment details.

By following these steps, i able exploit this vulnerability to manipulate the payment amount within the invoice URL. This poses a significant risk to the platform’s security, potentially leading to unauthorized alterations in payment details and financial losses.

Mitigation Recommendations:

1. Input Validation and Sanitization: Implement rigorous input validation and sanitization mechanisms to ensure that user-modifiable parameters, such as pricing information in URLs, are properly validated and sanitized before being processed by the server. This includes enforcing constraints such as minimum and maximum price thresholds.
2. Server-Side Price Verification: Perform server-side price verification to cross-check the pricing information received from the client with the server’s database. This helps prevent manipulation of prices by ensuring that the prices specified in the URL correspond to valid and authorized values stored in the server’s database.
