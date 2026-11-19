# Account Takeover on International Exchange — Bug Bounty Tuesday

- **Source URL:** https://medium.com/@kerstan/account-takeover-on-international-exchange-bug-bounty-tuesday-cf41a54bc4b7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240105163525/https://medium.com/@kerstan/account-takeover-on-international-exchange-bug-bounty-tuesday-cf41a54bc4b7
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4887 (id 4887)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Subscribed to:** [https://medium.com/@kerstan](/@kerstan)

Hello everyone, I’m Kerstan.

Today is Bug bounty Tuesday, I will share you about how i find Account Takeover on international exchange .Our target is a top international exchange. Due to the confidentiality rules of vulnerability mining, I will refer to the target as: example.com in this article.

So, let’s dive right in.

# 1. Start

Starting my journey, I embarked on gathering intelligence about the target.

This protracted process did unearth occurrences of sensitive data leaks, akin to PHPINFO leaks, which, though intriguing, didn’t quite quench my investigative thirst.

So, turning my gaze towards the main trading platform and its OTC offshoot, I meticulously probed the numerous functional aspects of their operations.

Through my persistent endeavours, I stumbled onto a peculiar \`getToken API\`. When a request is fired at this API, it responds with the current user’s Token. Yet, in stark contrast, every user functionality endpoint exceptionally scrutinized the Referer, barring one critical outlier → \`getToken\`.

# 2 CORS Account Takeover

The server’s authentication process relies on the Authorization and Cookie request headers — both having identical Token fields.

Not expecting much initially, I tweaked the Referrer, stripped the Authorization, and fired a fresh request to find, to my surprise, the Token nestled within the response. This Token was the linchpin of user authentications, and its possession meant complete control over account permissions. A quick manipulation of the Origin header to match my server address echoed a successful return of my server’s address in the Access-Control-Allow-Origin response header, clearly signalling a security anomaly here: CORS cross-domain grants access to user Tokens, leading straight to Account takeover.
