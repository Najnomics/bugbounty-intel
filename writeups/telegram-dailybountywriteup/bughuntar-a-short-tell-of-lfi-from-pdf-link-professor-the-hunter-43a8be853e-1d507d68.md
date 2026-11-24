# A short tell of LFI from PDF link → Professor the Hunter

- **Source URL:** https://medium.com/@bughuntar/a-short-tell-of-lfi-from-pdf-link-professor-the-hunter-43a8be853e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230329042016/https://medium.com/@bughuntar/a-short-tell-of-lfi-from-pdf-link-professor-the-hunter-43a8be853e
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2177 (id 2177)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# A short tell of LFI from PDF link → Professor the Hunter

**Who am I?**

Security Researcher at HackerOne. In 2022, I was in 60th place worldwide as per HackerOne leaderboard. Check out the result from this [link](https://hackerone.com/leaderboard/reputation?year=2022&quarter=4). You may follow me on Twitter to get some tips on Bug Bounty. My Twitter Handle: [https://twitter.com/bughuntar](https://twitter.com/bughuntar)

**Summary:**

Today, I found a Local File Inclusion ‘LFI’ Vulnerability in “Redacted’s Edge Network”. As it is known, the impacts of exploiting a Local File Inclusion (LFI) vulnerability vary from information disclosure to complete compromise of the system. Even in cases where the included code is not executed, it can still give an attacker enough valuable information to be able to compromise the system, as is the case of the security vulnerability we are reporting.

**How did I get the LFI vulnerability?**

During security testing on [https://erecruitment.redacted.com](https://erecruitment.redacted.com) I got a PDF file link.

[https://erecruitment.redacted.com/onlineapp/rocketpreepay.pdf](https://erecruitment.redacted.com/onlineapp/rocketpreepay.pdf) .

Then I tried to find LFI bug on that link but it was redirecting every time I entered the wrong link. I thought there is no LFI bug. But when I entered the right link, I am surprised it worked.

LFI exploit:

`https://erecruitment.redacted.com/onlineapp/rocketpreepay.pdf../../../../../../../etc/passwd`
**Conclusion:**

As I got it today I don’t know how many bounties I will get if it be accepted. Yet I am reciting ALHAMDULILLAH as I am successful to exploit. Feel free to reach out to me on [Twitter](https://twitter.com/bughuntar) or another platform: always my username is “@bughuntar”.
