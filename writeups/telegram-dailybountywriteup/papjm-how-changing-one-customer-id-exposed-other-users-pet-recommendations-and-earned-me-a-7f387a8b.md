# How Changing One Customer ID Exposed Other Users’ Pet Recommendations and Earned Me a $1,000 Bounty

- **Source URL:** https://medium.com/@papjm/how-changing-one-customer-id-exposed-other-users-pet-recommendations-and-earned-me-a-1-000-bounty-82c0179e62aa
- **Fetched from:** https://medium.com/@papjm/how-changing-one-customer-id-exposed-other-users-pet-recommendations-and-earned-me-a-1-000-bounty-82c0179e62aa?source=rss-b9c7797febe2------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14930 (id 14930)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Adini Rodini Rodney / Thu, 01 Oct 2026 16:12:01 GMT

**Researcher:** papjm

**Vulnerabilities:** Broken Access Control and Information Disclosure

**Reward:** $1,000

*The company, hostname, API path, customer identifiers, database objects and triager identity have been redacted. No SQL injection was confirmed.*

I discovered two related vulnerabilities in an online retailer’s product-recommendation API.

First, changing a user-controlled customer\_id parameter caused the API to return pet-product recommendations belonging to another customer.

Second, a Base64-encoded tracking\_id in the response exposed internal SQL queries, database table names and column names.

I signed in to my account and opened the account section while Burp Suite captured the application’s traffic.

In Burp’s HTTP history, I found a recommendation request containing several parameters:

GET /\[REDACTED\]?

category\_id=\[CATEGORY\_ID\]&

user\_id=\[USER\_IDENTIFIER\]&

customer\_id=\[MY\_CUSTOMER\_ID\]

I sent the request to Burp Repeater and changed only the customer\_id to a nearby value:

customer\_id=\[ANOTHER\_CUSTOMER\_ID\]

My authenticated session and the other parameters remained unchanged.

The server returned 200 OK with a different set of pet-product recommendations associated with the supplied customer ID.

This confirmed that the server trusted the customer ID from the URL without verifying that it belonged to the authenticated user.

If customer IDs were predictable or obtainable elsewhere, an attacker could potentially automate the process and enumerate recommendations belonging to multiple customers.

While examining the response, I noticed a long value inside a field named tracking\_id.

The format and padding suggested that it was Base64-encoded. Base64 is encoding — not encryption — so I decoded it.

The decoded value contained internal SQL filters similar to this sanitized example:

```
{
  "filters": [
    {
      "query": "SELECT 1 FROM [INTERNAL_TABLE] WHERE [INTERNAL_CONDITIONS]",
      "operation": "in"
    }
  ]
}
```
The data exposed internal SQL query templates, database table names and column names used by the recommendation engine.

This did not prove that the application was vulnerable to SQL injection. However, the information could help an attacker understand the database structure and prepare more targeted attacks if another injection vulnerability existed.

An attacker with a normal account could potentially:

Product recommendations may not appear highly sensitive, but this was still a cross-account authorization failure. A user should never be able to retrieve another customer’s personalized data by changing a URL parameter.

The server accepted a client-controlled customer\_id without confirming that it belonged to the authenticated session.

The client also received internal SQL information that was unnecessary for displaying recommendations.

The application should:

I reported the vulnerabilities through the company’s bug-bounty program.

The security team reviewed the evidence, triaged the report and awarded me a **$1,000 bounty** on February 9, 2024.

Whenever a request contains multiple identity-related parameters, change them one at a time and compare the responses carefully.

Also inspect values named tracking, metadata, debug, state or context. Data that appears opaque may simply be encoded.

The most important lesson is that personalized data must be selected using a server-verified identity — not an identifier controlled by the client.
