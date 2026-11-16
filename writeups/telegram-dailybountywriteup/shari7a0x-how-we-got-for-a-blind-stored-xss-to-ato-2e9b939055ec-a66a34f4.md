# How We Got $$$$$ For a Blind Stored XSS To ATO

- **Source URL:** https://medium.com/@shari7a0x/how-we-got-for-a-blind-stored-xss-to-ato-2e9b939055ec?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@shari7a0x
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 6314)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**السلام عليكم**

.بِسْم اللَّه الرَّحْمن الرَّحِيم . . اللَّهمَّ صَلِّ وَسلَّم وبارك على نَبِينَا مُحمَّد

My Name is El-Sayed Mohammed (Shari7a0x) , I will show you How I got a Zero-Click Account Takeover For Admin Support Through Password Update in a Public Bug Bounty Program on HackerOne.

first Read this [https://medium.com/@shari7a0x/how-we-got-for-a-blind-stored-xss-to-ato-2e9b939055ec](https://medium.com/@shari7a0x/how-we-got-for-a-blind-stored-xss-to-ato-2e9b939055ec) I explained in it How I reached Admin Support.

After the Program Resolved the bug I tried to take account again

1. I tried to inject Blind Xss again but nothing.

then I Opened domain support to try the same password, but it was wrong.

what about resetting the password?

I got two options .

reset link or put the answer for back up question .

I try to guess the answer and It’s okay .

I tried to put new password but nothing happened and got didn't update password .

I opened burp and tried to catch the request and got it then moved it to repeater .

I see request It didn't have any data ?

Then i tried to but same info in request and guess what happened password changed

I logged in account to get random user to try again the bug ,

guess what bug worked again without putting answer the question.

I reported and got two different results

Now I want to know what is ture ???

thanks for reading .
