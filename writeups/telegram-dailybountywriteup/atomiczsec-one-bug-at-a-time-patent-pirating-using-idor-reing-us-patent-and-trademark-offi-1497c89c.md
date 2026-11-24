# One Bug at a Time

- **Source URL:** https://medium.com/@atomiczsec/one-bug-at-a-time-patent-pirating-using-idor-reing-us-patent-and-trademark-office-for-fun-813f6c389e44?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240109183529/https://medium.com/@atomiczsec/one-bug-at-a-time-patent-pirating-using-idor-reing-us-patent-and-trademark-office-for-fun-813f6c389e44
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4234 (id 4234)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# One Bug at a Time: Patent Pirating using IDOR | RE’ing US Patent and Trademark Office for fun

--

Hello readers! Today I will be going into a fun story on how I used an IDOR within the US Patent and Trademark Office for fun with a discord bot.

**Part 1: Introduction**

I was thinking of some fun ideas that would be cool to put into a discord bot, and one that came to mind was a bot that could show me random patents that have been published. I love looking at how things work so this would be a great bot to find new technologies or inventions that are being patented. So the first step was to find where I could lookup patents. I found this US website called “United States Patent and Trademark Office” which is at [https://www.uspto.gov/](https://www.uspto.gov/). Next, I needed to find where I could lookup specific patents or *how* I could do that. So I googled “United States Patent and Trademark Office patent lookup” and got to a new site called: [https://ppubs.uspto.gov/pubwebapp/static/pages/landing.html](https://ppubs.uspto.gov/pubwebapp/static/pages/landing.html). Great, I can now search for patents by their number or by using operators.

**2. Investigation**

I first tried searching with the “Basic search” but I was not really sure what to look for within this. I threw in some random keywords and the list was populated but I needed a better way to automate this. The first thing that came to mind was looking at how the “Quick lookup” works because it uses patent ID’s which made me start to think about IDORs. So after trying basic search I used the example patent number on Quick lookup. I get the same format for the list as before but now its only that one patent not an entire list because I am not searching with keywords. I clicked PDF when I searched and got taken to a new site???

**3. Exploitation**

I have now reached [https://image-ppubs.uspto.gov](https://image-ppubs.uspto.gov) which has the full directory of [https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/2021012345](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/20210123456)6
