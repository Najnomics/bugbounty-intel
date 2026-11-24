# Bugbounty Write-up

- **Source URL:** https://medium.com/@spydernox/bugbounty-write-up-idor-insecure-direct-object-references-b1cd15ae5e3b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240110044353/https://medium.com/@spydernox/bugbounty-write-up-idor-insecure-direct-object-references-b1cd15ae5e3b
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4628 (id 4628)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bugbounty Write-up: IDOR (Insecure Direct Object References)

--

I found an Insecure Direct Object Reference (IDOR) in the payment process for users of a web application. This flaw enabled me to access sensitive information such as cardholder names, addresses, emails, and transaction details. The potential consequences of this vulnerability are significant.

# What is IDOR?

Insecure Direct Object Reference (IDOR) is a type of security vulnerability that occurs when an application provides direct access to objects based on user-supplied input. In this context, an “object” refers to a database key, file, directory, or other data that can be directly accessed. An IDOR vulnerability arises when an application uses user-supplied input to access objects directly without performing proper authorization checks to ensure that the user should have access to the object, this can lead to unauthorized access or disclosure of data, and in some cases, users may be able to modify or delete data they shouldn’t have access to.

# Methodology

when I started to place an order, I came across a request containing a “paymentID” parameter allowing me to have the details of the transactions via a PUT request.

```
PUT /api/payment/v4
....
{"PaymentID":"Payment_ID", .....}
```
I intercepted the request and replaced the “PaymentID” with a valid user ID. This allowed me to gain access to transaction details, including the status and personal data of the user, but the server generates UUID for each user that can not be predictable so it’s difficult to exploit , the only way was to find another endpoint which retrieve other users UUID.

After working on the target for a few days I discovered an interesting endpoint on Javascript files.

```
 function o(e, t, r) {
 var a = "/api/transactions/" + e + "?version=v4";
```
The only task now is to test the transaction IDs. I started by testing my own ID, and it worked I accessed my transaction details without authentication, including status, name, and UUID . Next, I need to find other valid IDs to exploit the vulnerability. I used online archives and GitHub Dorks for this.

and **BOOoooooooooooOM!!**

I found valid IDs, which gave me unauthorized access to users’ data.

**Tools Used:**

Thank you for taking the time to read this [@SpyderNox](https://medium.com/u/50fda51e45cf?source=post_page-----b1cd15ae5e3b--------------------------------)
