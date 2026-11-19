# How I Found Xss In A Inactive Hackerone Program With My Mobile

- **Source URL:** https://medium.com/@mrraghavop12/how-i-found-xss-in-a-inactive-hackerone-program-34464552256e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240313234956/https://medium.com/@mrraghavop12/how-i-found-xss-in-a-inactive-hackerone-program-34464552256e
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5398 (id 5398)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Found Xss In A Inactive Hackerone Program With My Mobile

Hello Freinds My Name Is Raghav.I Am Learning Hacking And Also Intermediate At My Work Today I Will Share How I Found A Stored Xss On A Inactive Hackerone Program So Let’s Begin.

# Story

So I am wondering about a Vulnerability that I found on a website and seeing Hacktivity I found that also many people found that I seen everyone reports and then I had decided to check the program in which the person find same bug as mine when I gone to there.there is written that this program is not active but I tried to find something on it.

# Xss

While doing research I logged in it and then I saw a chatbot in which I can ask any question related to website so I decided to try xss it don’t worked so I tried to detect it’s waf so I used the nuclei and then I got the waf which was a ckoudflare waf I tried to find payloads to bypass it on internet I found one on internet

\<a"/onclick=(confirm)()>Click Here!

This payload worked but I don’t know why it not worked at starting than I understood the code I clicked on it and then I got the bug also whenever I use the website it pop ups on my screen I reported it to the website by the found a bug feature on there

Thanks For Reading 😁 Also Comment Your First Bug Or Any Quote For Hacking. And Also Tell Me Any Hacking Tool Created By You Because I AM Working On A Hacking Tool Project That Would Find Pii On A Target
