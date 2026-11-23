# Hidden Reflected XSS on 403 Page.

- **Source URL:** https://medium.com/@Hacker_Yogi/hidden-reflected-xss-on-403-page-0cbb46683138?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250226031350/https://medium.com/@Hacker_Yogi/hidden-reflected-xss-on-403-page-0cbb46683138
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7184 (id 7184)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Hidden Reflected XSS on 403 Page.

## **Introduction:-**

In this blog post, I’m going to walk you through how I discovered a hidden vulnerability in an application that led to a Reflected Cross-Site Scripting (RxSS) exploit. The vulnerability was found in an unexpected place — the password reset functionality — hidden behind a 403 page that most researchers might overlook. This post will cover the methods I used, including bypass techniques, fuzzing, and manual testing, which ultimately led to uncovering a significant security flaw.

**Discovery of the Target:-**

While exploring the **example.com** domain, I initially encountered a **403 Forbidden** page. Normally, I would skip fuzzing these kinds of pages since they usually block further exploration, but something urged me to dig deeper. Experience told me that there might be something valuable hidden behind this block.

**Fuzzing:-**

Many researchers tend to avoid 403 pages after a few bypass attempts, but by using **FFUF** tool I discovered the `/console/` directory, which revealed the login page of the application. I tried injecting my payloads on the login and password parameter but nothing was returned on the response.

After this, I thought about giving up but decided to try my luck by using recursive fuzzing on the `/console/` endpoint. After a few minutes, I was shocked to find the password reset page hidden

Upon accessing the password reset page, I found several input fields and parameters. I started with the usual payload injections on the visible fields, but nothing seemed to work at first. However, a deeper look at the Burp Suite request history revealed something interesting: **multiple hidden parameters** were involved in communication with the server on the reset page

**Exploit:**-

I decided to run further tests using **Burp Suite’s Intruder,** I loaded payloads into various parameters and tested them against the server. During the process I found a key hidden parameter “**hdnPwdMinChar”.** Upon injecting payloads into the “**hdnPwdMinChar”** parameter, I successfully triggered the traditional alert popup. payload:-”**\<script>alert(4443)\</script>”**

**Key Takeaways:**

- Always test beyond the obvious inputs; hidden parameters can be a gold mine for vulnerabilities.
- Use fuzzing and automation, but don’t underestimate the power of manual testing.
- Hidden endpoints, especially those behind 403 pages, should be explored thoroughly.
