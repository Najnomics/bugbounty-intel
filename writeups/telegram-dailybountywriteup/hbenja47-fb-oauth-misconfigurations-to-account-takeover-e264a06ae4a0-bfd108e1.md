# FB OAuth Misconfigurations to Account Takeover

- **Source URL:** https://medium.com/@hbenja47/fb-oauth-misconfigurations-to-account-takeover-e264a06ae4a0?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240519220613/https://medium.com/@hbenja47/fb-oauth-misconfigurations-to-account-takeover-e264a06ae4a0
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5765 (id 5765)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# FB OAuth Misconfigurations to Account Takeover 😎

Today I’m going to share my experience through a bug, my first account takeover in bug bounty through authentication via Facebook. It was in a private program that had login via Facebook or Google. We’ll give it the fictional name of [www.vulnerable.com](http://www.vulnerable.com).

Vulnerabilities in Oauth Last year I learned in depth about the most common bugs in Open Authentication, that is Oauth. It could also be Auth0, which is a third-party service that uses Oauth, which is open-source (it can be freely implemented in any application). There are common vulnerabilities known for misconfigurations of Oauth. To study and practice this, the portswigger academy is very good, I recommend it -> portswigger.net/web-security/oauth.

*Note: I clarify that this bug is not from Facebook. It is a misconfiguration of the app that uses FB as a means of authentication through OAuth.*

## **1. How did the register work via Oauth on www.vulnerable.com?**

The first thing I did was to open Burpsuite, configure the scope, and activate the proxy so that all requests and responses are stored in the Burp history, so later I could review the entire login flow.

I started by reviewing the option to log in via Google. I didn’t find anything interesting and moved on to review the option to register via Facebook (FB).

I enabled login via FB, meaning I gave permissions in FB to the app to enter through, in other words, I gave permission to [www.vulnerable.com](http://www.vulnerable.com) to read the data from my Facebook account and thus obtain a user on [www.vulnerable.com](http://www.vulnerable.com). Then I logged out and logged back in. There I found this POST:

## 2. **Login Request**

As you can see, it’s a POST request to the application’s API and it sends a JSON with five values in the body, of which only two are important: loginType and oauthId. The first two, the rest can have a random value and nothing happens. It accepts the request without any problems.

*Note: I always try removing values to understand what is important in that request, to answer “what is needed and what is optional?”. This is valid for JSON values, parameters in GET, or cookies.*

Pay attention to the peculiarity that the second value is not the FB token, but the FB userId. This userId is not the global FB ID. When an APP is allowed to link to FB to share information, each app has an APPID and a USERID that varies in each linked app. In other words, it’s a unique number that FB provides to the user of that particular app and it doesn’t repeat for any other app.

## 3. **Login Response**

To my surprise, the authentication method only needed the previous POST with a valid oauthId in the body. All the login security relied on the oauthId. Yes!, knowing the 16-digit number of that unique number that Facebook provides, the api responded with valid session cookies for that user:

## 4. **Current State of Affairs**

So I said to myself, “bronxi, it’s 16 digits, brute force could be possible, copy the obtained cookies and access the account of any user of [www.vulnerable.com](http://www.vulnerable.com) that has their account associated with Facebook”. But, brute force? The program didn’t say anything about prohibiting brute force, do I report it or keep looking? My dilemma was whether to report it as it is, with brute force or not, because I ran the risk of being told that if brute force is required, it is not valid for them. So I said to myself “bronxi, calm down, focus and keep looking for a way to get that Facebook userID”.

## 5. **Findings with automation**

Previously, in this program, I had already done the reconnaissance task. In that recon, I had obtained many parameters with paramspider. I used those parameters to run nuclei using fuzzing templates of @[0xKayala](https://github.com/0xKayala) [(templates)](https://github.com/0xKayala/fuzzing-templates). There I had found some XSS, but I hadn’t reported them because in the policies of the [www.vulnerable.com](http://www.vulnerable.com) program they made it clear that they did not accept XSS.

But maybe, if I used one of those XSS to obtain the Facebook userID, maybe they would accept it. I thought this because the vulnerability itself is the Account Take Over and I would use another bug for it, an XSS. The XSS itself is not the vulnerability in this scenario. So, I started checking the storage in the browser to understand how it stored the FB userID.

## 6. **LocalStorage & XSS to my server**

I found the FB token in localStorage in a value called *fblst\_666450503370175*. You read that right, yes, the token! not the user ID that was what I was looking for.

I used one of the reflected values that I found with nuclei and after several tests, I came up with a payload that worked correctly to send me that value stored in localStorage to my server:

## 7. **But…**

However, since the implementation of authentication via FB was incorrectly configured with the userID, it did not use the FB token which would be correct. So, even though I got the token, I couldn’t log in with it. This struck me as funny. I had the FB token but it didn’t work to log in, I needed the 16-digit userID. So I got more critical information, like an auth token unlike a userID, and due to an incorrect configuration, the token was not used but only the userID.

## 8. **Report it with Plan A**

I pondered and said to myself, I’ll propose plan A with Brute Force, and I’ll mention that maybe I could exploit it in a targeted way to a certain user using XSS to obtain it. Although I still hadn’t figured out how to link the FB token with the userID. I reported it like this but got an **N/A**. The response, which makes sense, was that a **brute force attack on 16 digits was not a reasonable attack**. That gave me a dose of motivation to exploit it in a targeted way with XSS, i.e., plan B.

## 9. **Plan B: XSS**

I went for plan B at the risk of being told it doesn’t apply because I’m using an XSS. But since I got the FB token and not the userID, I couldn’t exploit it. So I started investigating if it was possible to obtain the userID through the FB token. I found the FB API, where there was an endpoint to which you sent the user’s token via GET parameter and it responded with the userID :).

## 10. **These were the reproduction steps for this plan B:**

1. The attacker sends a malicious link to the victim to obtain their Facebook token stored in localStorage.
2. The victim receives that malicious link and opens it.
3. The attacker receives the Facebook token on their server.
4. The attacker uses the Facebook API to obtain the User ID. [https://graph.facebook.com/me?fields=id&access\_token=XXXXXX](https://graph.facebook.com/me?fields=id&access_token=XXXXXX)
5. The attacker uses the userID to obtain the victim’s session cookies and logs into the victim’s account.

## **I reported it like this**

Days later, they closed the report as **N/A** and the triager told me that it’s the same as a previous report of mine, that if I report the same thing again they will deduct points (yes, sometimes triagers don’t read the entire report)

I had to “**Submit a reques**t” to make a review request, which is a kind of mediation, in which I explained that it’s not the same report, but here I use an XSS and in the previous one I used brute force, so I modified the way to exploit it by replacing the brute force, which they didn’t consider a reasonable attack, with an XSS.

**Another triager reviewed i**t, reopened it as **New**, changed the severity to **High (P2)**, **triaged** it, and two weeks later I got paid the **reward**.

## **Final comments**

This was the **first time I was able to use a bug found with automation**, referring to XSS, in a chaining where I obtained a reward. Everything I have found automatically before has been duplicated.

While the FB token I obtained through XSS, stored in localStorage (please, devs, do not store anything related to authentication in localStorage), could be considered more critical data than the userID, **that token had an expiration, whereas using the FB userID to obtain the victim user’s cookies had no expiration at all**.

😎 Happy hunting!!!
