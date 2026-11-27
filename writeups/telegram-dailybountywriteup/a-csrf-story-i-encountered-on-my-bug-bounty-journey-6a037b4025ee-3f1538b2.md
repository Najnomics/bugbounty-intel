# A CSRF Story I Encountered on My Bug Bounty Journey

- **Source URL:** https://enes478.medium.com/a-csrf-story-i-encountered-on-my-bug-bounty-journey-6a037b4025ee?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905085933/https://enes478.medium.com/a-csrf-story-i-encountered-on-my-bug-bounty-journey-6a037b4025ee
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9799 (id 9799)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# A CSRF Story I Encountered on My Bug Bounty Journey

Throughout my bug bounty journey, I have encountered many different vulnerabilities, but it was the first time I found a CSRF vulnerability. Although its impact was not very significant, this vulnerability gave me the opportunity to test and understand the CSRF concept through a real example.

I will name the target application 0x478.example.com. On this platform, users can share blog posts and collaborate with others to edit their content. After spending about a week on the application, I noticed that shared blog posts could be added to a private list.

At first, I decided to try vulnerabilities like IDOR or BAC (Broken Access Control) on this feature, but I was not successful. Then, while examining past requests in Burp Suite, I realized that the request to add a post to this private list did not have any CSRF token.

Following this, I prepared a simple CSRF PoC and tested it. The PoC was successful now, if the victim user was logged in and visited the page I prepared, I could add any blog post I wanted to their private list.

Although this CSRF vulnerability was not critical, it showed me how important manual testing is, how easily even seemingly ordinary features can be overlooked, and the value of thorough examination. Every vulnerability in the bug bounty process is educational. This small success boosted my motivation and encouraged me to discover more.

[Follow me](https://x.com/enes0x478) :)
