# BAC Leads To Full Takeover Of Any Organisation

- **Source URL:** https://medium.com/@ismailsaid1603/bac-leads-to-full-takeover-of-any-organisation-0fc21cf4cb5e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240309133255/https://medium.com/@ismailsaid1603/bac-leads-to-full-takeover-of-any-organisation-0fc21cf4cb5e
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5480 (id 5480)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# BAC leads to full takeover of any store within the organisation

Hello everyone, I’m Esmail and this is my first write-up, so today i’m gonna talk about one of the most interesting vulnerabilities I've discovered.

***Introduction:***
This is a public bug bounty program in bugcrowd, The program is about managing stores, you have products, customers, orders, etc..

One of these functions that caught my eyes, It was using third-party applications to help you manage your store, and yes you are right in order to install an application you need to give it some permissions.

*Discovery:*

During installing an application I intercepted the request and it looked like:

As you can see there is 2 interesting parameters, scope and context.

The scope is what can the app access, and the context contains the store hash that the app will be install in.

So until now everything seems normal, but what if we changed the store hash of our store to the victim store! Bingo you have installed it in the victim store without any access.

**Until now it’s considered P2 due to two problems:**1. How to get the victim store hash?

2\. What are you able to do after installing the app in victim’s store?

1\. How to get the victim store hash?


To get the victim store hash you just need to open the store as normal user and view page source, the hash will be like this: 

https://cdn11.redacted.com/s-yekne1dmpo

2\. What are you able to do after installing the app in victim’s store?


To answer this question we need to go back to the scope parameter.

First we need to know all possible scope values and to do that we need to go back to another function which is responsible for creating “Store Level API Keys”.

So let’s create an API-key and intercept the request it will be like that:

hmm, looks interesting.

Let’s save it and go back to the app instilling process and edit the scope & context.

The request will be like that:

Now we have installed an app in the victim store with all roles.

To my surprise I was redirected to the application with the victim store, Sadly I didn’t find users, products, customers, or anything, So I was really disappointed.

But after less than half hour i went back to burp-suite history and started searching all requests.

The luck smiled on me again and I found a request ends with “Platform-data” that contains an “Access Token” I was like: OMG!!!

So I went back to the API documentation and started the fire.

I was able to perform all actions just like the owner.

In the end I hope you enjoyed the write-up.

Happy hunting ❤
