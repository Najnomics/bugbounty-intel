# Persistent XSS via Cookie Injection

- **Source URL:** https://medium.com/@ayushkr99732/xss-via-cookie-injection-a-deep-dive-into-the-discovery-9ef70e22eceb?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240923053018/https://medium.com/@ayushkr99732/xss-via-cookie-injection-a-deep-dive-into-the-discovery-9ef70e22eceb
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7341 (id 7341)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Persistent** XSS via Cookie Injection: A Deep Dive into the Discovery

# Introduction

In this blog post, I will take you through an XSS vulnerability I discovered via cookie injection, allowing the exploitation of a `redirect_url` parameter. This vulnerability, while common, demonstrates how seemingly simple flaws can lead to severe security breaches.

**Disclaimer:** The domain names used in this write-up are anonymized as `redacted.com` for privacy and security reasons.


# How It All Began: A Password Reset Link

Like many bug bounty stories, this one began with a simple password reset link that was sent to my email when I requested a password reset on a website. Here’s how the URL appeared:

At first glance, this looks like a typical password reset link. However, one parameter, `redirect_url`, caught my attention. This parameter seemed to define where the user would be redirected after resetting their password. Naturally, I wondered: what would happen if I tampered with this parameter?

# Exploiting the Redirect: Crafting the Payload

To test my theory, I edited the `redirect_url` parameter to inject a JavaScript payload:

In this case, I changed the `redirect_url` to:

`javascript:alert(1)`
By injecting this payload, I aimed to see if I could redirect users to a JavaScript function, effectively triggering an XSS alert.

# **The Chain Reaction: Redirecting to XSS**

Once I accessed the tampered URL, the application redirected me to another link:

This URL was still asking me to change my password, but now the `redirect_url` parameter was carrying the JavaScript payload encoded within it. After successfully setting a new password, I was redirected to:

[https://accounts.redacted.com/success](https://accounts.redacted.com/success)

Together with “password reset success” page, I was met with the familiar pop-up of `alert(1)`, confirming the presence of an XSS vulnerability.

# The Role of Cookies: Analyzing the Session

As part of my analysis, I delved deeper into how the application was handling my request and identified that a specific session cookie was playing a crucial role in this vulnerability. Upon accessing the malicious URL, a session cookie was created on the domain `accounts.redacted.com`:

```
[
    {
        "name": "_keychain_session",
        "value": "nEYZxyg6xBPAX3mg5geLIppLxk5ti8N%2FG06Jq6uJEbGBLcewW6nO%2FGG9Lel97TzeDlY%2FsPtmO%2BHNz%2BnOiaLJ%2FJXpi7Uz7ixHUO6n%2FVHSszXdT%2BNR8%2BU2h31vZ4t4Di5wKgFY2RXuJSzDMwV4dNQ%3D--Nb4itlwLx6Y2GqrK--xDCcuymYnCYQm5MqtAfOUg%3D%3D",
        "domain": "accounts.redacted.com"
    }
]
```
# What Does This Cookie Do?

This cookie stores the value of the `redirect_url` parameter, meaning the payload I injected (`javascript:alert(1)`) was now stored in the session. Whenever I navigated to `https://accounts.redacted.com/success`, the browser would automatically execute the JavaScript code from the cookie, leading to the XSS attack being triggered.

# The Severity of the Vulnerability

This vulnerability posed a high security risk due to the following reasons:

- **Persistent XSS:** Since the payload is stored in a session cookie, it persists, which means whenever the user would be to visit [https://accounts.redacted.com/success](https://accounts.redacted.com/success)
`_keychain_session` cookie value, allowing multiple XSS attacks during that time frame.
- **Trust Exploitation:** Users trust password reset processes, making them less suspicious of malicious activity during such interactions.

# Conclusion

This XSS vulnerability via cookie injection highlights the importance of thoroughly validating and sanitizing input in web applications, especially in sensitive processes like password resets. As a bug bounty hunter, it’s always satisfying to uncover such issues and contribute to securing online platforms. Hopefully, this write-up sheds light on how a simple manipulation of a URL parameter can lead to significant security breaches.
