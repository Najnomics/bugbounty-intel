# Oauth via Flawed CSRF protection

- **Source URL:** https://medium.com/@akostak/oauth-via-flawed-csrf-protection-1c6340629e82?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230725070304/https://medium.com/@akostak/oauth-via-flawed-csrf-protection-1c6340629e82?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3361 (id 3361)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**What is this “OAuth2”**

OAuth2 is a standardized protocol used for authorization processes. Using OAuth2, you can authorize the user’s account and use it in your own application.

- **Client Application: The application that receives permission to access the user’s account**
- **Authorization Server(Provider)**:**is the server that issues Access Tokens after obtaining the required authorization**

Now let’s get to know some information defined after being redirected with provider.

- **Scope: The level of access requested by the user**
- **Code**: **It is the part with the user information that will be valid on “example.com” by the Authorization Server**
- **State: İs a csrf token specific to each user on the client application side**

## **How was my report ?**

Steps to reproduce the problem

- 1**-There is an oauth flow on the “example.com” site, which is used for both membership and login, and can even be connected to the account within the account.I opened a normal account and logged into the account and started to examine the oauth flow in the account.**
- 2- **We said that after the authorization on the Provider is completed, it returns with a few definitions while redirecting.these were as follows**

`/social/complete/google-oauth2/?state=&code=&scope=&authuser=&prompt=none`
- 3- **First I wanted to examine the “state” and “code” parameters and realized that they are disposable. In fact, it is always available in some client applications, but here the situation was different.Then I tested whether the state parameter is for a single user only and found that it can be used for any user**
- 4-**Your request immediately after
Reminding that there is a “GET” method. I made a csrf poc**

`<img src="https://example.com/social/complete/google-oauth2/?state=&code=&scope=&authuser=&prompt="></img>`
- 5- **The poc you see above will work. When the image tag goes to the browser domain, it will automatically add the attacker link to the victim account on “example.com”.In this way, the attacker can add her own link to the victim account and log in to the victim account with provider, as I mentioned at the beginning.**

Hope it was clear Have a nice day everyone.
