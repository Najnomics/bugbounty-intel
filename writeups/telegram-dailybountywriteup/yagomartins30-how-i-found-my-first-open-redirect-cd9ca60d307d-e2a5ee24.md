# How i found my first open redirect

- **Source URL:** https://medium.com/@yagomartins30/how-i-found-my-first-open-redirect-cd9ca60d307d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501140005/https://medium.com/@yagomartins30/how-i-found-my-first-open-redirect-cd9ca60d307d
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7525 (id 7525)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How i found my first open redirect

Yago Martins.

Hello everyone, this is my first bugbounty report, so I apologize if I make any mistakes.

The first step is to explain what an open redirect vuln is.

It’s a web vulnerability that allows an attacker to use an official website to redirect a user to another site, without their consent.

Due to policy, we’re going to call [https://target.com](https://target.com,)

First I started with a basic standard recognition, and I tested some endpoints, in the manual tests I noticed an interesting feature, whenever I entered to buy a product without being logged in, the application took me to the link **target.com/Account/Login.aspx?ReturnUrl=/Market/Products.aspx&sw\_sc=internet**

In other words, the application sends me to the login page, keeping the route I was on previously.

After logging in, as expected, I was redirected to /Market/Products.aspx.

To test that I could redirect to other endpoints, I added the same login endpoint to the ReturnUrl parameter:

**target.com/Account/Login.aspx?ReturnUrl=/Account/Login.aspx&sw\_sc=internet**

And as expected, after logging in, I was redirected again to log in LOL.

After confirming that this parameter could be manipulated, I started doing some tests to see if a 401 code bypass was possible.

If I put anything with / before it, I was redirected to a non-existent 404 endpoint, but if I took the / out, there was some treatment that the page simply reloaded and nothing happened.

So I started trying some known openredirect bypasses and when I put **target.com/Account/Login.aspx?ReturnUrl=//google.com&sw\_sc=internet**, the site kept loading for a few seconds until I was redirected to the main again.

Analyzing the requests, I noticed that when I was directed to some endpoint of the site itself, which was not foreseen, the same sw\_sc parameter was added.

So I added this parameter **sw\_sc=internet**, but before the parameter i added a **question mark (?)** to my malicious request for the parameter to be seen as a parameter of my payload and booommmm.

So my final payload was: **//google.com?sw\_sc=Internet**

I was automatically redirected from **target.com** to **google.com**

Remember, I could redirect the user to any site I wanted, using the reputation of the official site to gain credibility.

That’s it guys, unfortunately the report was screened for not applicable because it was outside the scope provided, but I’m still on the hunt.

Thanks for reading.
