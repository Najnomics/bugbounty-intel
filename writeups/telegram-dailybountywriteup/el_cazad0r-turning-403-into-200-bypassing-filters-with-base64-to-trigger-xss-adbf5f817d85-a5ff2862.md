# Turning 403 into 200

- **Source URL:** https://medium.com/@EL_cazad0r/turning-403-into-200-bypassing-filters-with-base64-to-trigger-xss-adbf5f817d85?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250410162158/https://medium.com/@EL_cazad0r/turning-403-into-200-bypassing-filters-with-base64-to-trigger-xss-adbf5f817d85
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9320 (id 9320)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Turning 403 into 200: Bypassing Filters with Base64 to Trigger XSS**

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

Ever landed on a 403 Forbidden and just walked away?

Next time, try this: Base64 encode your payload — it might just flip the script from forbidden to fabulous. In this post, I’ll show you how a simple Base64 trick helped me bypass filtering mechanisms and land a working XSS (Cross-Site Scripting) payload.

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

**The Trick: Base64 to the Rescue**

Let’s say you’re testing an endpoint like this:

`https://target.com/?q=<img src=q onerror=prompt(8)>`
But the response?

403 Forbidden or just a silent block. Classic.

Now here’s where the fun starts. Instead of sending the raw payload, you Base64 encode it:

```
<img src=q onerror=prompt(8)>
→ Base64 → PGltZyBzcmM9cSBvbmVycm9yPXByb21wdCg4KT4=
```
Now hit the same endpoint with:

`https://target.com/?q=PGltZyBzcmM9cSBvbmVycm9yPXByb21wdCg4KT4=`
If the backend decodes the input and reflects it directly into the DOM — boom, you’ve got XSS.

**Why This Works**

Some applications decode Base64 values before processing or rendering them, especially when data is expected to be passed obfuscated or encoded. This is common in:

• Analytics/tracking parameters

• Dynamic UI rendering

• Frontend preview or builder tools

• Custom APIs that decode data internally

In such cases, even if WAFs or input filters block obvious tags like \<script> or \<img>, the encoded versions slip through undetected.

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻**Bonus:** Where Else to Use It

This Base64 trick isn’t limited to XSS. You can try encoding payloads in:

• SQL Injection

• SSTI (Server-Side Template Injection)

• LFI (Local File Inclusion)

• Command Injection

Any time you’re working with inputs that are getting blocked or sanitized — it’s worth checking if Base64 decoding is happening silently in the background.

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

**Final Payload Recap**

Here’s a full working example:

**Raw Payload**

\<img src=q onerror=prompt(8)>

**Encoded**

PGltZyBzcmM9cSBvbmVycm9yPXByb21wdCg4KT4=

**Full Request**

`https://target.com/?q=PGltZyBzcmM9cSBvbmVycm9yPXByb21wdCg4KT4=`
**Takeaway**

Always test your payloads in different formats. Base64 can be a powerful bypass mechanism when dealing with restricted endpoints or aggressive filters.

Next time you hit a dead-end, remember — encoding might be all it takes to revive your payload.

Happy hacking!
