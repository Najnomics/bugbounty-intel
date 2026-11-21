# I found Reflected XSS on another university’s website

- **Source URL:** https://medium.com/@Bl4cky/hunting-reflected-xss-uncovering-vulnerabilities-on-university-websites-daa6c5ac790d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250906033547/https://medium.com/@Bl4cky/hunting-reflected-xss-uncovering-vulnerabilities-on-university-websites-daa6c5ac790d
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8495 (id 8495)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# I found Reflected XSS on another university’s website

While browsing the web I discovered a Reflected Cross-Site Scripting (XSS) vulnerability. This vulnerability allows attackers to inject arbitrary JavaScript code into your website through input fields that are not properly processed or validated.

## Vulnerability Details

To start, I used a combination of **Waybackurl** and **Burp Suite** to analyze a university domain website. I identified a search functionality with the following structure:

Next, I viewed the source code of the webpage and noticed something intriguing.

When I typed “Bl4cky” into the search field. Interestingly, the ***key*** variable already had input validation built in — it blocked every HTML tag I tried to insert. Next, the ***url*** variable will be added to the string. So it will become `https://abc.example.edu.vn/tim-kiem/{key}`

## **But what if the** **url** **variable is empty before concatenation?**

Would the final URL become something like:

`https://abc.example.edu.vn/{key}`

In this case, before adding the string url = ‘Bl4cky’. It is obvious that we have manipulated the URL, where **Bl4cky** is an **Untrusted Data** that I can manipulate to perform XSS.

## Exploitation

I tested my hypothesis with the following payload:

`erl25"%20onmouseover="alert(1)"%20title="test%E2%80%AC`
Well done, I successfully executed the payload, triggering the `alert(1)` JavaScript function. This confirmed that the application was vulnerable to Reflected XSS due to improper handling of untrusted data.

Hope you learned something new from my experience. Let me know your thoughts on this!

If you like this write-up, Share!

Thank you!
