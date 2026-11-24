# XSS Context

- **Source URL:** https://medium.com/techiepedia/xss-context-448b8a0cc904?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250505073146/https://medium.com/techiepedia/xss-context-448b8a0cc904
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4355 (id 4355)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# XSS Context

XSS vulnerabilities are a common “first bug” for people getting into cybersecurity. It is also a mainstay vulnerability that professionals will continue to report well into their careers.

# Finding XSS

One of the differences an experienced pentester has when looking for XSS is an understanding of DOM context. Different HTML tags do different things depending on where they are being rendered.

So when you are copying & pasting XSS payloads all around a site take a moment to see where and how they are rendered in the DOM so that you can find a valid XSS to report.

First example: HTML will be ignored inside Title tags.

For this to work you need to first close the title tag \</title>

Second example: Similarly HTML tags have no power inside of \<script> tags, except for \</script>

Below are two examples of an image tag being rendered inside of a \<script> tag. Neither will work, it doesn’t matter if it is rendered into a string context.
