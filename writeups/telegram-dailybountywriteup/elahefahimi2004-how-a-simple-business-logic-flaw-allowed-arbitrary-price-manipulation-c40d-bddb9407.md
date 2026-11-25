# How a Simple Business Logic Flaw Allowed Arbitrary Price Manipulation

- **Source URL:** https://medium.com/@elahefahimi2004/how-a-simple-business-logic-flaw-allowed-arbitrary-price-manipulation-c40d554cdca0
- **Fetched from:** https://medium.com/@elahefahimi2004/how-a-simple-business-logic-flaw-allowed-arbitrary-price-manipulation-c40d554cdca0?source=rss-b9c56c162463------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14928 (id 14928)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** V ForVendetta / Tue, 29 Sep 2026 17:26:04 GMT

A technical breakdown of parameter tampering during checkout and why client-side trust leads to critical financial risks.

Business logic vulnerabilities occur when an application’s workflow allows an attacker to manipulate its intended behavior. Unlike technical flaws such as SQL Injection or Cross-Site Scripting (XSS), logic flaws often bypass automated vulnerability scanners because they rely on valid application functionality.

During an authorized security assessment on an e-commerce infrastructure, I identified a critical **Price Manipulation** flaw caused by client-side parameter tampering. This write-up details how the vulnerability was discovered, exploited, and ultimately patched.

The target platform provides automated service provisioning and server hosting solutions. The standard workflow for ordering a service was as follows:

While analyzing the traffic using **Burp Suite**, I inspected the HTTP POST request generated when initiating the payment.

Upon intercepting the checkout submission, the following parameters were being passed in the HTTP request body:

POST /gateway/process HTTP/2

Host: redacted.example.com

Content-Type: application/x-www-form-urlencoded

invoiceid=REDACTED&amount=4606800000&email=user%40example.com&pay=Submit

The application relied on the client to send the amount parameter directly in the request body instead of calculating or retrieving the verified price on the server side using the invoiceid.

To test if server-side validation was enforced, I conducted the following test:

invoiceid=REDACTED&amount=50000&email=user%40example.com&pay=Submit

The backend accepted the modified payload without validating whether the amount matched the actual balance due in the database:

HTTP/2 302 Found

Location: https://paymentgateway.example.com/payment/token\_id

When redirected to the payment gateway interface, the payable amount displayed was exactly **50,000 IRR**. A transaction could be completed for a fraction of the real cost, leading to potential automated service delivery at an unauthorized price.

The application should never accept the price or transaction amount directly from client requests. The payment initiation endpoint should only require an internal reference (e.g., invoice\_id).

The server must query the database internally to fetch the actual balance associated with the invoice ID before communicating with the payment gateway:

\# Secure implementation concept

invoice = db.get\_invoice(invoice\_id)

payable\_amount = invoice.total\_due

gateway\_session = create\_gateway\_session(invoice.id, payable\_amount)

When the payment gateway sends a callback notification after payment completion, the backend must verify that the amount paid strictly equals the database record before marking the invoice as paid.
