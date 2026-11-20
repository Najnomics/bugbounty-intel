# How Did I Easily Find Stored XSS at Apple and earn $5000 ?

- **Source URL:** https://medium.com/@xrypt0/how-did-i-easily-find-stored-xss-at-apple-and-earn-5000-3aadbae054b2?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@xrypt0
- **Fetched:** 2026-11-20
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 5842)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### How Did I Easily Find Stored XSS at Apple And Earn $5000 ?

Hello there ! Today we’ll talk about stored XSS which I found in Apple. Without further ado let’s get into it !

First of all, our vulnerable Apple service **was**: [https://discussions.apple.com](https://discussions.apple.com)

This service is a community where Apple users and developers discuss their problems. If you register here you can create a profile for yourself and help others or get help from them !

Now let’s look at a simple example profile.

This is a simple profile that I have prepared for you. As you can see you can edit the “Location” and “Bio” sections as you wish.

#### **What If We Use A XSS Payload ?**

Payload that will be used is :

">\<svg/onload=alert(1)>

We’ll place this payload in the “Location” section of our Apple profile and take a look at the result together !

As you can see this is a Stored XSS vulnerability that is very easy to exploit ! Cookies of users and **employees** could be stolen, and it was very easy to achieve that with this way !

As soon as I found something like this, I immediately contacted Apple Security via e-mail. At the end of our **3-month process**, I received an e-mail like the one below and I was rewarded !

This is how I got the XSS vulnerability in Apple in a very easy way and completed it with great success ! I leave you with **Apple’s Hall Of Fame** list and my position on the list below.

[https://support.apple.com/en-us/102812](https://support.apple.com/en-us/102812) (June 2022) (@xrypt0)

Thank you for reading this far and paying attention. See you in future articles !

Crypto (@xrypt0)
