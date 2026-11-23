# IDOR is NOT only on the ID

- **Source URL:** https://medium.com/@mshulkhan/idor-is-not-only-on-the-id-8e94b5cc193e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250122150219/https://medium.com/@mshulkhan/idor-is-not-only-on-the-id-8e94b5cc193e
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7965 (id 7965)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR is NOT only on the ID

# **What’s IDOR?**

**IDOR (Insecure Direct Object Reference)** is a security flaw that occurs when a website lets anyone access specific information by knowing its address. For example, if you can see someone else’s private order details by simply changing a number in the URL, that’s an IDOR vulnerability. This weakness is a major security risk and is often exploited by hackers.

# IDOR is NOT ONLY on id

Commonly IDOR is associated with user ID manipulation, the vulnerability can also arise with other sensitive parameters, such as email addresses, filenames, or transaction references. Any user-supplied input used to identify a resource without adequate validation can lead to an IDOR exploit.

It’s important to check all of the possibilities of an IDOR by checking the response. If the server’s response includes sensitive identifiers like **id**, **email**, or **phone\_number** in a structured format (e.g., JSON), these could be potential entry points for exploitation.

Example:

If the response contains *"id": "123"*

Try requesting:


`GET /example?id=124`
If the response contains *"email": "user@example.com"*

Try requesting:


`GET /example?email=victim@example.com`
If the response contains `"phone_number": "1234567890"`Try requesting:


`GET /example?phone_number=0987654321`
# Why it’s important?

Many developers secure only obvious parameters like user IDs but may overlook others, such as email or phone numbers. Attackers who explore all possible fields can exploit these overlooked vectors. By systematically checking the application’s responses and testing them in requests, you can uncover hidden IDOR vulnerabilities that might otherwise be missed.

If you want to learn about hacking you can start by looking at this [blog](https://sysbraykr.com/blog/all)
