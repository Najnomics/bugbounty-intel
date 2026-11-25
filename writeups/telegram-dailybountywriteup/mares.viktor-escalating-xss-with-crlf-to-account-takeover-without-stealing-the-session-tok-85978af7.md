# Escalating XSS with CRLF to Account Takeover (without stealing the Session token)

- **Source URL:** https://medium.com/@mares.viktor/escalating-xss-with-crlf-to-account-takeover-without-stealing-the-session-token-a705e4363cf1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231012104959/https://medium.com/@mares.viktor/escalating-xss-with-crlf-to-account-takeover-without-stealing-the-session-token-a705e4363cf1?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3696 (id 3696)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Escalating XSS & CRLF to Account Takeover (without stealing the Session token)

--

Hi Everyone,

Today I want to show you a quite unique (hopefully) way to **escalate a Cross-Site Scripting Vulnerability combined with a CRLF Injection to a full Account Takeover**. We will take advantage of a simple Business Logic vulnerability, to then steal another user’s account. This **took me about 2 days to fully exploit**, so I hope it will make for an interesting read!

As usual, we will anonymize the victim website and give it the usual example domain -> ‘example.com’. We are interested in the subdomain that allows us to login within the application at ‘**accounts.example.com**’

After ‘playing around’ with the web application for a while, which usually consists of navigating all endpoints and executing all possible requests, we see that there are 2 interesting things. The Web Gateway’s vendor, version & path are leaked.

The fact that the path starts with ‘**mwg-internal**’ seems quite suspicious to me straight away. So, I started researching and found a very interesting vulnerability -> related to **CVE-2022–1254**

**Description**: “*The website allows a remote attacker to craft MWG-specific internal requests with URL paths to any third-party website, causing arbitrary content to be injected into the response when accessed through MWG (McAfee Web Gateway). Static content is loaded from URL paths prefixed with “/mwg-internal/de5fs23hu73ds/”. Paths with this prefix are intercepted and directly handled by the MWG. It is possible to derive the API of the ‘Ssos’ plugin’s ‘SetLoginToken’ action”*

With the above in mind, we craft the following request:

From the above request, you can see that we use the vulnerable ‘p’ parameter to do the following:

1. Inject **%0d%0a** -> **CRLF** (carriage return line feed) characters which the web server uses to understand when new HTTP header begins and another one ends
2. Inject a **Content-Type** header with the value of **text/html** to specify that we want the web server to interpret the body of the response as html
