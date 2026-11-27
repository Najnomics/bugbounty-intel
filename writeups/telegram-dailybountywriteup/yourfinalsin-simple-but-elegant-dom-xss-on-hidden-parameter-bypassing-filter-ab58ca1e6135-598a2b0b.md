# DOM XSS — Simple but Elegant on Hidden Parameter— Bypassing Filter

- **Source URL:** https://medium.com/@YourFinalSin/simple-but-elegant-dom-xss-on-hidden-parameter-bypassing-filter-ab58ca1e6135?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@YourFinalSin
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 6970)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### DOM XSS - Simple but Elegant on Hidden Parameter— Bypassing Filter

Hello Everyone,

I discovered this DOM XSS on a public program on a website that looked in the first glance like a static website, but had some hidden functionality on one of it’s directories. I found the hidden directory by crawling and manually browsing the site.

The website didn’t use any frameworks, it looked like it was just plain PHP on a Apache web server — This instantly triggers things like XSS, SQLi, LFI, etc. in my head when I see that.

The first thing I did, was checking the source code for some interesting JavaScript and to my surprise I found a parameter “t” that looked like I would be able to control. Also there was no CSP configured and no HttpOnly flag on the cookie set. Here is the a part of the client-side source code:

Instantly I checked if I can control this “t” parameter, the following way:

*www.redacted.com?t=test*

And as you can see in the image above, it was reflected in the source code! Now to my convenience the parameter was already embedded into \<script> tags, so I just needed to break out of the parenthesis and trigger an “alert()” or something like that.

So this time I tried to break out of the parenthesis by sending the following URL to the backend:

*www.redacted.com?t=”test”*

And again it worked! I was able to break out — There was no filtering in place. This is how the source code looked now:

Now the last step of the mission was to execute JavaScript successfully in form of “alert()” or “prompt()” etc. Since the vulnerable parameter was already reflecting my input in viable \<script> tags, I knew I didn’t need to add them in my payload, so I just tried to execute an “alert()”, like this:

*www.redacted.com?t=”alert(0)”*

No alert popup was triggered. It seemed like there was a filter in place that was supposed to mitigate arbitrary JavaScript execution. I assumed it was just some type of blacklist filter. In this case you can just add dashes to your payload and it will still execute. So this time I used the following payload:

*www.redacted.com?t=”-alert(0)-”*

I was able to successfully bypass the filter and trigger the popup! This is how the final source code looked like.

I reported it and it was triaged — Thank you for reading.

*Subscribe to my YouTube for more* — [S̶I̶N̶ — YouTube](https://www.youtube.com/@YourFinalSin)

*Follow on Twitter or ask me anything here* — [SIN (@YourFinalSin) / X](https://x.com/YourFinalSin)
