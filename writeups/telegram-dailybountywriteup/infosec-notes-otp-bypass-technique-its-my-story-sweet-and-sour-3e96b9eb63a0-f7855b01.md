# OTP BYPASS TECHNIQUE its My StOry [sweet and sour]

- **Source URL:** https://medium.com/infosec-notes/otp-bypass-technique-its-my-story-sweet-and-sour-3e96b9eb63a0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250131223803/https://medium.com/infosec-notes/otp-bypass-technique-its-my-story-sweet-and-sour-3e96b9eb63a0
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8503 (id 8503)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# OTP BYPASS TECHNIQUE its My StOry \[sweet and sour\]

Hi Hackers welcome back with another article. This is my story when i was struggling for **bypass rate limit** or some kind of restrictions.

I frustrated with this. I didn’t find any Possible way to bypass it and I was about to give up but my mind stuck there when I saw one header in the response.

This header is responsible for blocking my requests, when I try to brute force on my target. Let me explain what happened with me. The story is all about Coupon\_code, A person gave me a task to fetch all the coupon\_codes from this target’s server. These are the Free subscription coupons. Yeahh Sometimes I do these kind of activities.

Now When I tried to brute force on it , initial request is send normally and i got a good response but after that it sent me 401,Unauthorized responses. I tried a lot of tricks but I failed.

Now I try to understand how server block me. I analyse one header that is X-Request-Id:a457df-454-xXXXXX with this id server verify all the coming requests. If Its same in the all the requests instead of first request it will block that request and gives 401 response code. Now I tried to change this request Id with every requests and it worked. I bypass the security for brute force.
