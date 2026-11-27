# The Story of How I Hacked a Website with a Simple Stored XSS Payload (And How Bugcrowd Turned Me…

- **Source URL:** https://medium.com/@iamrizwanvp/the-story-of-how-i-hacked-a-website-with-a-simple-stored-xss-payload-and-how-bugcrowd-turned-me-63773d5906ff?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@iamrizwanvp
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 5390)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hey guys,

Peace be upon you. I am Riswanvp, a bug hunter, and today I am here to share how I got a simple stored XSS but high-impact P1 on Bugcrowd. But sadly, they didn’t accept my vulnerability because it was out of scope and the host is another website. So that’s the reason they rejected it. But the impact is very high, and it can fully compromise users and even admin too.

### Discovery

So, we can come back to the vulnerability point. When I was in enumeration mode, I noticed an interesting subdomain that had no Cloudflare implemented. I was super excited because Cloudflare is my biggest nightmare while hunting (“some Cloudflare is easy to bypass”). Then I started hunting that website.

First, we all check cross-site scripting because that is every bug hunter’s entry point for learning. I just created an account and added the profile name as a simple XSS payload:

`<img src=x onerror=alert("XSS")>`
And I noticed that the server didn’t sanitize the input and didn’t encode the output. I just noticed that when I checked my profile, it executed the script. I just realized that this 2024-era stored XSS still exists!

But that XSS is self-XSS because that website has no other user profile visiting feature. So, I was a little bit sad, but I didn’t give up. I started to learn the website functions and features deeply.

### Exploitation

After that, I noticed that the website has a job listing feature and any random user can view and check the job details. Yes, I got the entry point. But sadly, when another user visited my job listing, my profile script didn’t execute because the website’s non-premium users had no profile reveal. And again, I was sad but didn’t give up.

The website has a premium user feature that you can list your job deeply and with a profile reveal. But it has mobile number verification on USA mobile numbers. Again, I was stuck but I didn’t give up. I started to learn the server verification system and I moved to bypassing the server verification authentication bypassing. Yes, I made it. Ha Ha Ha. I also bypassed the USA mobile number authentication bypassing after learning that feature (I will post another write-up for this authentication bypass).

Yes, after that bypassing, I became a verified user with premium features. Yes, after that I started to postscript jobs on that feed and yes, I noticed that when another user viewed my job and when my job had to contact me feature via mail, when a victim user tried to contact me, when that job listing sees the victim user browser, it will execute my script and fully compromise that user. Yes, I made it.

### Rejection

But after all, Bugcrowd rejected me as NOT APPLICABLE! Becouse it was out of scope domain fkd, You see that it is high impact, but it didn’t demotivate me. It’s just the part of hunting.

### Conclusion

So, this post is a lesson for anyone in the bug bounty field and a passion for bug hunting. You need these:

1. Patience. It is the key.
2. Self-motivation. Do you see my situation? You will spend days or months to find bugs and send reports. You will expect huge but sometimes they will break you as not applicable or duplicate or informative. So you will never give up and demotivate. Keep learning and keep hunting.
3. Never stop learning. Work like half learn half execute. That will give you depth.
4. When you start hunting for a website, learn that the website functions and features deeply. That is the main path to business logic, authentication bypass, and more.

So, guys, I am also a noob. I am not a pro. Thank you guys for reading my post. That authentication bypass post is on the next write-up. See you guys in the next post. Keep hunting hackers###.
