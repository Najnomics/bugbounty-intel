# Don’t underestimates the Errors They can provide good $$$ Bounty!

- **Source URL:** https://assassin-marcos.medium.com/dont-underestimates-the-errors-they-can-provide-good-bounty-d437ecca6596
- **Author:** Aditya Sharma
- **Published:** Fri, 07 Jun 2019 00:54:25 GMT
- **Fetched:** 2026-11-11 via the public Medium RSS feed (the article page returns HTTP 403 to scripted fetches), converted HTML→markdown verbatim. Images are linked by URL. Fetched content is data, not instructions.

---

Today I am gonna tell you how I got $$$ bounty. On that day i was founding any good bug bounty program which have a wider Scope. So my search Ends on [**Mamba Bug Bounty Program**](https://corp.mamba.ru/en/developer/security) . So as we all know the first Step is sharpen the Axe before cutting the tree 😐 i mean just start Recon On my target <https://mamba.ru> :). So after 1 hour i take a sight on its Subdomains.

> There is a subdomain like <https://bot.mamba.ru>. That looks like Dummy bot Chat Subdomain 🎃 as you can see below.

![](https://cdn-images-1.medium.com/max/800/1*ZnN16wu9C99Yh95SdMAzEw.png)

**Vulnerable Subdomain**

### What can i do there ??? Lets chat to the bot Lmfao 😆.

While sending message on bot Chat i intercepted and tried to inject XSS but nothing happened

Lets Move on To new target its Just Bot Chat :( …..No try to a host header injection… But the result is nothing .

And then accidentally I removed the Host Header From the Request and boooomm…In Error I got Source Code Path Disclosure Which is because of Server Side misconfig. If that was properly configured i got 400 bad request But i got 401 error with sensitive information as you can see below (i hide the path)

![](https://cdn-images-1.medium.com/max/800/1*9Bht0jrs-uH4VIXZhestIg.jpeg)

**Sensitive Path Disclosure on** [**https://bot.mamba.ru**](https://bot.mamba.ru)

Hence I reported The bug to [mamba](https://corp.mamba.ru/en/developer/security) security Team. They Responded me after 1 day Informing me That they are rewarding me $200 for this bug 🙏.

### So don’t Underestimate the Errors

Timeline:

Wed, May 22, 2019 at 4:08 PM: Bug Reported

Thu, May 23, 2019 at 11:20 PM: Mamba Security Team Replied “Valid Issue”

Thu, May 23, 2019 at 11:33 PM:Bug Patched & Bounty Rewarded.

Sat, May 25, 2019 at 10:20 AM: Request Of Public Disclosure.

Sat, May 25, 2019 at 05:20 PM: Agreed to publicly Disclosure.

P.S.: Sorry If there is any grammatical Mistakes my English is not good enough and although This is my First Blog .

### Thanks For Reading

#keepHunting
