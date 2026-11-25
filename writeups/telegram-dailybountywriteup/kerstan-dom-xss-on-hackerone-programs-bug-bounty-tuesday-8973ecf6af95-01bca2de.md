# URL Redirection To DOM XSS on Hackerone Programs -Bug Bounty Tuesday

- **Source URL:** https://medium.com/@kerstan/dom-xss-on-hackerone-programs-bug-bounty-tuesday-8973ecf6af95?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105163122/https://medium.com/@kerstan/dom-xss-on-hackerone-programs-bug-bounty-tuesday-8973ecf6af95?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4824 (id 4824)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# URL Redirection To DOM XSS on Hackerone Programs — Bug Bounty Tuesday

**Subscribed to:** [https://medium.com/@kerstan](https://web.archive.org/web/20240105163122/https://medium.com/@kerstan)

Hello everyone, I am excited to introduce a new series I’ve been preparing titled ‘Bug Bounty Tuesdays’, where each week I’ll be sharing an article discussing vulnerabilities, bug bounties, or related tools. I hope to sustain this series and if you find these pieces useful, feel free to follow or cap me.

In today’s piece, I’d like to delve into the process of uncovering a DOM xss bug bounty, a fascinating case from the past. So, let’s dive right in.

# 1 Find Endpoint

While engaging with burp history, I spotted a link, [https://XXX/qrcode?k=url&v=https://testtest.com/&s=0.](https://web.archive.org/web/20240105163122/https://xxx/qrcode?k=url&v=https%3A%2F%2Ftesttest.com%2F&s=0.) I proceeded with examining its front-end code and observed that:

1. It retrieves the values of parameters \`k\` and \`v\`.
2. When \`k\` equals \`url\`, The value of \`v\` is fed into the handleUrl function for processing.

# 2 URL redirection

I was curious about his handleUrl function and learned:

Initially, it gets the value of parameter ‘v’ and performs URL decoding.

It checks if the current User-Agent request embeds ‘xxxboxapp’.

The aim is to verify whether the link has been opened within XXX’s APP. Now, conventionally when we employ a browser to navigate, the User-Agent request won’t house this string sequence, thus we land into the \`else\` branch. Here, \`location.href\` redirects to the URL decoded value of \`v\`.

Consequently, I was able to perform URL redirection. :)

# 3 DOM XSS

Nevertheless, not entirely satisfied, I endeavored to implement XSS using \`javascript:alert1\` but discovered, much to my dismay, that I couldn’t . :(

I realized the presence of a regex check when appraising \`v\` value to ensure it…
