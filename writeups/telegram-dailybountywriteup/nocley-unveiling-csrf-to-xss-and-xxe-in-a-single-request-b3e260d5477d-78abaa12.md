# Unveiling CSRF-to-XSS and XXE in a Single Request

- **Source URL:** https://medium.com/@nocley/unveiling-csrf-to-xss-and-xxe-in-a-single-request-b3e260d5477d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905175024/https://medium.com/@nocley/unveiling-csrf-to-xss-and-xxe-in-a-single-request-b3e260d5477d?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9973 (id 9973)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Unveiling CSRF-to-XSS and XXE in a Single Request

**Free Link**

Welcome back to our bug bounty hunting journey, ngosytuan and fatman.

Bug bounty is a battle, and every bug hunter is a warrior. Here’s how we triumphed in one such fight. This is the story of two vulnerabilities discovered in a single request: one high-severity bug and one critical bug.

Initially, Fatman discovered an interesting request while manually testing. The request contained a “data” variable with a base64-encoded string as its value. He tried decoding it and found that it was an XML string. When the request was sent, the response would return it wrapped in a different XML structure.

I immediately had some ideas in mind. I told Fatman to try testing for an XXE bug right away. Meanwhile, I would work on a PoC for a CSRF-to-XSS bug by injecting an XML string containing JavaScript to execute XSS via SVG. This was familiar territory since I often test SVG uploads for XSS. After a while, the bugs were fully developed, and we wrote the report.
