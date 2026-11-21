# Day 13

- **Source URL:** https://medium.com/@danielbelay/day-13-chaining-improper-authentication-to-idor-and-no-rate-limit-for-mass-account-takeover-bd6be94a96c3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250630092146/https://medium.com/@danielbelay/day-13-chaining-improper-authentication-to-idor-and-no-rate-limit-for-mass-account-takeover-bd6be94a96c3
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8826 (id 8826)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Day 13: Chaining Improper Authentication to IDOR and No Rate Limit for Mass Account Takeover 🔹

Hey folks! Hope you’re all doing well. Today, I’ll share a vulnerability **Researcher** discovered in a bug bounty program that led to mass account takeovers. Let’s dive in!

🔍 Recon Phase While testing a domain, **he** noticed an X-Rate-Limit option. Initially, **he** ignored it, thinking no rate limit alone wouldn’t be impactful. **He** decided to dig deeper, spending a few hours fuzzing and brute-forcing parameters. Eventually, **he** found the endpoint:

📌 /api/v1/users/id

When **he** sent a request, it returned 401 Unauthorized. At first, **he** was stuck, but after analyzing the request headers, **he** saw a CSRF token. **He** removed it and resent the request.

💡 Boom! The server responded with 200 OK and returned a JSON response, confirming an IDOR (Insecure Direct Object Reference) vulnerability.

🚀 Exploitation **He** started fuzzing the id endpoint but initially found nothing. Then, while reviewing Burp Suite’s HTTP history, **he** saw a request containing a numeric ID linked to the forgot password request.

🛠 Steps to exploit:

Created a second account to extract a new user ID. Replaced the old account’s ID in the request with the new one. Received 401 Unauthorized — something was still wrong. Realized **he** forgot to remove the CSRF token 🤦♂️. Removed the CSRF token and got a 200 OK response. IDOR confirmed! 🎉

🔗 Chaining Bugs for Mass Takeover **He** debated reporting the issue immediately but decided to explore further. Then, **he** remembered the no rate limit bug **he** found earlier.

Captured the request to: \[https://redacted.com/api/v1/users/id/\](https://redacted.com/api/v1/users/id/) Created a payload and brute-forced 3K–5K numeric IDs. Left it running while doing other tasks. Came back to see multiple 200 OK responses. 📢 Impact: The responses contained session tokens, user IDs, and even passwords in plaintext — allowing mass account takeover. 😲

🛠 Lessons Learned & Tips

✔ Always focus on recon before jumping into high-severity vulnerabilities.

✔ Technical bugs matter — don’t just throw XSS, SQLi, SSRF, or SSTI payloads blindly.

✔ Be patient — spend time understanding the application’s logic.
