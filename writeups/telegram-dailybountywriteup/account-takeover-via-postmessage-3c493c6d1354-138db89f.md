# Account Takeover via postMessage

- **Source URL:** https://phlmox.medium.com/account-takeover-via-postmessage-3c493c6d1354?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250829162006/https://phlmox.medium.com/account-takeover-via-postmessage-3c493c6d1354
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9027 (id 9027)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Account Takeover via postMessage

This write-up is about how I found that one line of JavaScript code was leading to an account takeover. The target has its own bug bounty program, so it wasn’t an illegal act, but I will still keep the program name private.

This target has a main web application and another domain for OAuth login purposes. Let’s call them **redacted.com** and **redacted-login.com**. Now, let’s get back to the bug.

When you click “Login” on **redacted.com** and choose one of the OAuth providers, you are redirected to the login page of your OAuth provider (e.g., Google) through the API of **redacted-login.com**. After you log in, your OAuth provider redirects you to the callback URL of **redacted-login.com**. Everything is fine up to this point.

The last page we see before being redirected to the main web app is the result/success page on the **redacted-login.com** domain. And this page has one `postMessage` method called in it.

If you don’t know what postMessage is:

And here is the code from my target:

I am pretty sure you have already realized the issue here.

- The `application` variable is assigned to `window.opener` OR `window.parent`. This means that if I use `window.open` to start the authentication process, I will be the parent window.
- The `data` variable to be sent includes the user's token.
- The `postMessage` target origin is a wildcard. See:

What I did to steal the tokens was simple. I created an HTML page with `window.open` code in it, then created a listener for the `postMessage`, and we were done. See the PoC page:

Here is the captured code:

Thanks for reading.
