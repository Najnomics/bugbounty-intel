# How I accidentally found an IDOR bug in Google slides and rewarded $3,133.70

- **Source URL:** https://medium.com/@atikqur007/how-i-accidentally-found-an-idor-bug-in-google-slides-and-rewarded-3-133-70-96866fac3af1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126141919/https://medium.com/@atikqur007/how-i-accidentally-found-an-idor-bug-in-google-slides-and-rewarded-3-133-70-96866fac3af1
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8285 (id 8285)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I accidentally found an IDOR bug in Google slides and rewarded **$3,133.70**

It was a lazy afternoon at the office. After lunch, I was sitting at my desk, preparing slides for an event speech on Google Slides. Once the slides were ready, I clicked on Presenter View to preview them. During the event, I wanted to do a live Q&A session with the audience, so I started searching online to see if Google Slides had such a feature. That’s when I stumbled upon Audience Tools. To enable Audience Tools, you need to go to Presenter View, click on Audience Tools, and then click “**Start**”

Once you start a session, you’re given a link that your audience can use to ask live questions while you’re presenting.

Curious, I copied the link and opened it in Chrome’s incognito mode to explore how the audience could ask questions. Anyone could ask questions without needing to log in! The user interface of the question box looked a bit outdated, and my bug hunter instincts kicked in. Something felt off, and I decided to dig deeper.

Without wasting any time, I fired up Burp Suite and started testing. I noticed that every time someone asked a question, a unique **clientId** was included in the POST request. So every comment has a unique clientId. That’s when it clicked — this could be a potential vulnerability.

```
POST /presentation/d/e/2QANgcCBH8YIx_f5yfCz0l5len6p5BDFsiROx_rcqbOqYgcByotn7pOpaS3kXb3YYffwepoOXCyzanE8ZCIw/submitquestion?includes_info_params=1 HTTP/1.1
Host: docs.google.com
Cookie: 
Content-Length: 84
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Accept: */*
Origin: https://docs.google.com
Referer: https://docs.google.com/presentation/d/e/2QANgcCBH8YIx_f5yfCz0l5len6p5BDFsiROx_rcqbOqYgcByotn7pOpaS3kXb3YYffwepoOXCyzanE8ZCIw/askquestion?seriesId=d90df436-a253-48a1-8aea-bf5c19761447
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Priority: u=1, i
Connection: keep-alive
seriesId=d90df436-a253-48a1-8aea-bf5c19761447&clientId=e5j7slqfku2&questionText=Test
```
Anyone clicks on the link, all the questions are loaded with different unique **clientId** assisnged to each comment.

Then I immediately understood what kind of bug there might be here. I logged into two different accounts and submitted a question — “Test” — from account-1. Then, using account-2 in another browser, I copied the **clientId** of account-1’s comment. While intercepting account-2’s request to submit a question, I replaced its clientId with the **clientId** of account-1.

The result? The question submitted by account-1 was modified using account-2’s request. This confirmed my hypothesis. Even more concerning, this could be exploited without logging in at all.

At this point I was a little surprised and shocked and kept retesting to see if there was any mistake on my side. And after testing many times I was sure that it was a valid bug.

And immediately reported it to Google. To my surprise, Google closed the report the next day, stating that the security risk was minimal.

But I knew the impact of this bug was clear: no user interaction was required to exploit it, and no guessing or brute-forcing of clientIds was necessary. The application itself provided the clientId. I politly re-played my valid points. Google reopened the issue and confirmed it. However, after ten days, the report was closed again with the reasoning that the security risk was still low due to the “**guessing**” of **clientId**.

At this stage, I was a little disappointed. That Google’s security team did not test the bug properly or they did not watch the poc video I provided. Because there was no need for guessing the **clientId** where the clientId was automatically loaded by the application itself. I explained this clearly once again, showing exactly how an attacker could extract the clientId without any effort. Finally, Google’s security team **triggered** the bug themselves, acknowledged its impact, and rewarded me **$3,133.70** in the S2 severity category.

One thing I learned at this stage is that before reporting a bug, you need to be very clear about its security impact. I was very clear about the security impact of the bug, which is why I was able to argue with the Google Security team with confidence and finally convince them.

Watch the Poc:

Thanks for reading! If you enjoyed this, follow me for more:

Follow me:
