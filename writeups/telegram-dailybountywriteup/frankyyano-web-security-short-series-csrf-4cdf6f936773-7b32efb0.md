# Web Security Short Series — CSRF.

- **Source URL:** https://medium.com/@frankyyano/web-security-short-series-csrf-4cdf6f936773?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240603070226/https://medium.com/@frankyyano/web-security-short-series-csrf-4cdf6f936773
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5696 (id 5696)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Fun Fact** — This is one of the most asked about questions in Appsec Interviews!

CSRF (XSRF) allows an attacker to trick a user’s browser into performing unauthorized actions on a trusted website, all without the user’s knowledge or consent.

**How Does CSRF arise in Applications?**

Consider a banking application that transfers money upon receiving a POST request with the recipient’s account number and amount, of course to complete this attack, the victim must be authenticated.

An attacker could embed a form on their malicious site that when submitted, sends a POST request to the bank’s transfer endpoint with the attacker’s desired malicious payload to conduct the fraudulent transaction. If the user is logged in to their bank account while visiting the attacker’s site, the bank might process the transfer due to the user’s valid cookies, even though the user never intended to make the transaction. 

Essentially, CSRF allows an attacker to partly bypass the same origin policy (SOP), which is designed to prevent different websites from interfering with each other.

Below is another simple illustration of a CSRF attack vector, as demonstrated by Rana Khalil.

What makes CSRF attacks possible?

- **Cookie-based session handling.** The target application should only be tracking user requests based only on session cookies. There are no other mechanisms in place to track subsequent requests made to the application. This is where CSRF Tokens would come in handy. Consider the below request:

- The application uses a session cookie to identify which user issued the request. There are no other tokens or mechanisms in place to track sessions and subsequent requests.
- If the values of the request parameters that are needed to perform the action can be easily predicted by an attacker, then based on these conditions, an attacker could craft a malicious payload.

If a victim user visits the attacker’s web page, that’s end game! First, the attacker’s page will trigger a HTTP request to the vulnerable website. If the victim has an authenticated session on the vulnerable website, their browser will automatically include their session cookie in the request. The caveat to this is that SameSite cookies should not be in use.

Because no other mechanisms exist to verify subsequent requests, the vulnerable application will process the request, as though it was made by the victim user.

**Defending Against CSRF.**

- **SameSite Cookie Attribute**: Setting the SameSite attribute of cookies to Strict or Lax helps mitigate CSRF attacks by restricting how cookies are sent in cross-site requests.
- **CSRF Tokens**: Random tokens generated server-side by the application and shared with the clients especially for critical actions and include them as hidden form fields or request parameters.

More reading and Labs:

I hope you enjoy this piece!
