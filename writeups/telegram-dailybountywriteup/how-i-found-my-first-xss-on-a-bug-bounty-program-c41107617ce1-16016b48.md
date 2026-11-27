# How I found my first XSS on a Bug Bounty Program

- **Source URL:** https://kingcoolvikas.medium.com/how-i-found-my-first-xss-on-a-bug-bounty-program-c41107617ce1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260716233132/https://kingcoolvikas.medium.com/how-i-found-my-first-xss-on-a-bug-bounty-program-c41107617ce1
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1150 (id 1150)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I found my first XSS on a Bug Bounty Program

Hello there, Welcome back to my Article.

In this article, I will tell how I found my first valid XSS on a bug bounty program. So let’s start

I’m Vikas Anand, a security researcher and a bug bounty hunter from Bihar, India.

First, I tried to find the program through Google Dork. The dork I used is: **intext:Cryptocurrency Exchange intext:Bug bounty**

After finding the program, I checked the scope of the program, but unfortunately there was only one domain, and that was the main domain.

So I said to myself, “Let’s hunt on this and go deep into the target and try to find at least one valid bug.”

I gave up after about 2–3 days because I hadn’t found anything. After 2 weeks, I again visited the site, and I see that it has implemented some new features. New features mean new bugs. let’s hack

I went through all of the features and captured all of the requests with BurpSuite, and one feature caught my eye, where you can translate the word into different languages.

An input box, let’s try for XSS. After that, I type **“>img src=x onerror=alert(1)>** and then looking at the source code, the value is well sanitised.

Now I sent the request to the repeater tab and tried some XSS bypasses but didn’t find anything useful. And lastly, I sent the request to the intruder tab, and I fuzzed with some XSS payload lists, and after finishing the intruder attack, when clicking on the length tab, I got a few payloads of bigger length.

The XSS payload is successfully fired when you click on show response.

XSS polygot was the payload that was executed :

**javascript:/\* →\</title>\</style>\</textarea>\</script>\</xmp>\<details/open/ontoggle=’+/\`/+/”/+/onmouseover=1/+/\[\*/\[\]/+alert(/@PortSwiggerRes/)//’>**


And after reporting the bug, they said that your bug is eligible for a $200 bounty, and I received the bounty in crypto.

So that’s all from this Article. I hope you like it. And please ignore my grammatical mistake, as I’m not good at writing Articles.

If you have any questions, you can connect with me.

[https://twitter.com/kingcoolvikas](https://twitter.com/kingcoolvikas)

[https://www.linkedin.com/in/kingcoolvikas/](https://www.linkedin.com/in/kingcoolvikas/)

Cheers✌️and thanks for Reading at the end of this Article.
