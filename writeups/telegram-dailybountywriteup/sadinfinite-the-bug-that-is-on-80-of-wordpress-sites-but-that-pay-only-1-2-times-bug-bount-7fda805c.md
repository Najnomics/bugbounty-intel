# The “Bug” that is on 80% of WordPress sites but that pay only 1/2 times | Bug Bounty Story

- **Source URL:** https://medium.com/@sadinfinite/the-bug-that-is-on-80-of-wordpress-sites-but-that-pay-only-1-2-times-bug-bounty-story-f98506a146e7
- **Fetched from:** https://medium.com/@sadinfinite/the-bug-that-is-on-80-of-wordpress-sites-but-that-pay-only-1-2-times-bug-bounty-story-f98506a146e7?source=rss-6ebfbfd68929------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14958 (id 14958)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** SadInfinite / Sat, 24 Oct 2026 10:00:10 GMT

Hello there ! Wassup ? 

Thanks for reading my story !

I am going to talk about a common wordpress “bug” that happens really often, it’s an information disclosure via REST API.

For those who doesn’t know REST API is a functionality of WP (WP=WordPress) that stores informations about posts, users, etc… and it’s used to monitor/configure the site when you have some privileges.

It’s starts by \`/wp-json/\`

The probably most interesting route is \`/wp-json/wp/v2/users\`.

That can leak usernames (with sometimes real names), some times e-mails, and other informations depending on configuration and plugins.

It’s a low-medium impact but sometimes it can be escalated. For exemple, you can use that username for bruteforce of the wp-admin login (searching for weak credentials) or use a leaked email for OSINT/CSINT investigations because some programs accepts leaks (if you know that the email have some leaked passwords you can try them on the WP login).

But before reporting you need to verify 2 things :

Here was the last time I reported it :

So when you feel it , try !

Thanks for reading.

Don’t hesitate to contact me :
