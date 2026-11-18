# Insecure Direct Object Reference (IDOR) — Unauthorized Product Price Modification

- **Source URL:** https://medium.com/@mo.muwafak2001/insecure-direct-object-reference-idor-unauthorized-product-price-modification-4a4b3da74aad
- **Fetched from:** https://medium.com/feed/@mo.muwafak2001
- **Fetched:** 2026-11-18
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14953)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello fellow security researchers and bug bounty hunters!

In this article, I am going to share my experience of finding an Insecure Direct Object Reference (IDOR) vulnerability in a global marketplace platform that allows users to buy and sell goods worldwide. The vulnerability enables an attacker to modify the price of any product on the platform, even products they do not own, by simply changing the product ID in a legitimate request.

Description :

The target is a worldwide buy-and-sell marketplace. The application implements strong anti-proxy protections and actively blocks Burp Suite, which forced the use of an older version of mitmproxy to intercept traffic without being detected.

When publishing or updating a product, the price is included in the same request. The application allows the same request to be replayed, and product data can be modified by changing parameters in that request.

The product is identified solely by an id parameter inside the request. The application does not properly verify ownership or authorization when this id is modified. As a result, an attacker can replace the id with any other product’s ID and successfully update its data (including the price), even if the product does not belong to them.

Obtaining Victim Product IDs :

To exploit this vulnerability, the attacker needs the target product’s ID.

When requesting information about any product (for example, viewing a product page), the server returns the product’s id in the response. This allows the attacker to easily collect the ID of any product on the platform.

**Exploitation flow:**

1. Browse or search for a target product.
2. Capture the product information request and extract the product id from the response. (Test3)
3. Replay the product update request, replacing the original id with the target product’s id and modifying the price.

4\. The price of the target product is successfully updated.

5\. The attacker can then purchase the product at the newly modified (lower) price.

Impact :

- Change the price of any product on the platform without authorization.
- Lower the price of expensive items and purchase them at a fraction of the original cost.
- Cause financial loss to legitimate sellers.
- Disrupt the integrity of the marketplace pricing system.

This is a clear Broken Access Control issue with direct financial impact.

Thank you for reading my article. If you have any questions or want to learn more about my experience, feel free to reach out to me.

Linkedin — [www.linkedin.com/in/](http://www.linkedin.com/in/)muwafakhelal

Telegram — [@MH\_CyberSec](http://twitter.com/MH_CyberSec)

Youtube — [www.youtube.com/@CyberSec-h6v](https://www.youtube.com/@CyberSec-h6v)
