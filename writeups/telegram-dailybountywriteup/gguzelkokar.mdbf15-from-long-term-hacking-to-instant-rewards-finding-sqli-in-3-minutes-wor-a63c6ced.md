# From Long-Term Hacking to Instant Rewards

- **Source URL:** https://medium.com/@gguzelkokar.mdbf15/from-long-term-hacking-to-instant-rewards-finding-sqli-in-3-minutes-worth-3125-ac36c6e950bf?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250827091714/https://medium.com/@gguzelkokar.mdbf15/from-long-term-hacking-to-instant-rewards-finding-sqli-in-3-minutes-worth-3125-ac36c6e950bf
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6618 (id 6618)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From Long-Term Hacking to Instant Rewards: Finding SQLi in 3 Minutes Worth $3125

I believe that if you want to succeed in bug bounty, you should focus on programs that you have been hacking for a long time, like 2–3 years. You should know the company’s structure, features, APIs, and everything else about their assets.

In this story, I’ll show you how I easily found an SQL injection in my program. Please don’t focus on the SQL injection, bounty, or anything specific; instead, focus on the logic of working with a company for many years. Before I start, I’ll provide some examples of other bug bounty hunters’ profiles.

d0xing had 131k points, and he has 13k points from one program, which is \~10%.

try\_to\_hack had 102k point and he has 78k points from one program, which is \~%75!

zseano had 26k point and he has 16.5k points from one program, which is \~%63!

So I have a couple of programs too. One of my favorites is a program I’ve been hacking for over 2 years. I can quickly notice when a developer changes a button in the main application. I’ve tested over 300 endpoints and 40 domains. If I see a new one, I can notice it too. I also follow API documentation releases, the program’s social media channels, and newsletters.

### How I Found SQLi in 3 Minutes in this Private Program

I woke up at 03:00 a.m., and I need to edit my presentation for an upcoming session. Then I visited my bug bounty program and noticed there was a new feature added. I saw that from my staging envorinment.

When I used the new feature, I discovered a PUT request, and all I did was add a single quote to the ‘id’ parameter, which resulted in an error-based SQL injection. After some trials, I executed ‘(select sleep(4))’ and the database slept for 12 seconds because it executed 3 times.

I was rewarded $3125 for it. That’s the story. In this story, I wanted to explain the benefits of hacking in a program for a long time. Thanks for reading. Have a great weekend!
