# Account takeover in ChatGPT

- **Source URL:** https://medium.com/@diegotellaroli05/account-takeover-in-chatgpt-e134ed11654d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251127112700/https://medium.com/@diegotellaroli05/account-takeover-in-chatgpt-e134ed11654d
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2230 (id 2230)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Account takeover in ChatGPT

Hello everyone. My name is Diego Tellaroli, and in today’s article, I am going to explain how a hacker could exploit a critical vulnerability that allowed him to take over an account in ChatGPT. This way, the hacker could invade any ChatGPT user’s account with just a single click, potentially gaining access to confidential information and being able to perform any action on the victim’s account. This vulnerability was found by [**Nagli**](https://twitter.com/naglinagli/status/1639343866313601024?t=NWfpbt6npG_QN-PERHOOiQ&s=19) so all credits go to him.

To understand this vulnerability first, let’s understand what an account takeover is: An account takeover is a type of cyber attack where a hacker gains unauthorized access to a user’s online account, typically by stealing the user’s login credentials or exploiting vulnerabilities in the system. Once the hacker gains access to the account, they can perform various malicious activities, such as stealing personal information, making fraudulent transactions, or spreading malware.

To achieve an account takeover on ChatGPT and successfully obtain the victim’s account, we exploited another vulnerability, a **web cache deception** vulnerability. With this vulnerability, it is possible to hack into any user’s account with just one click.

## Ok, but what is a web cache deception?

Web Cache Deception (WCD) is an attack in which an attacker deceives a caching proxy into improperly storing private information sent over the internet and gaining unauthorized access to that cached data. It was proposed by Omer Gil, a security researcher in 2017.

When the browser makes a request to a website, the connection usually passes through the CDNs (Content Delivery Network).

CDNs are a geographically distributed network of proxy servers and their data centers, which caches the local copies of web content to provide faster access to the users by reducing their network latency, and thus reducing the load on web servers.

Caching servers have no safeguards to authenticate users and prevent information, and it only stores non-user specific static or public content. And all the user-specific dynamic contents get routed to the main servers of the website or service a user interacts with.

The web caching deception (WCD) attack works by the technique of path confusion attack. It manipulates the URL path by which the cache server is forced to store, and the sensitive data gets revealed as public content.

## What can be cached?

We can cache public and static files that do not contain any sensitive information, such as:

- General JavaScript files
- Style sheets
- Downloadable content
- Media files

To exploit the vulnerability in ChatGPT to take over an account, an attacker could craft a .css path to the session endpoint and send the link to the victim. When the victim opens the link, the response is cached and the attacker can harvest the victim’s credentials and take over their account. It is a critical web cache deception bug that could have allowed attackers to access user information such as names, emails, and access tokens, which OpenAI’s API would fetch from the server.

## The attack

We could access [https://chat.openai.com/api/auth/session](https://chat.openai.com/api/auth/session) and the API will return our account data, such as name, email, ID, and the most critical one: our access token.

Now if we go to [https://chat.openai.com/api/auth/session/victim.css](https://chat.openai.com/api/auth/session/victim.css), we will find the same content as /api/auth/session, regardless of whether the victim.css file exists on the server. It will return the user’s data, such as the access token.

This way, the server’s web cache will see the “.css” extension and interpret it as a Cascading Style Sheets (CSS) file. As the server is configured to cache Style Sheets files, ***victim.css*** will be cached by the server with the victim’s session content (data and access token).

Now that victim.css has been cached with the victim’s authentication data, the hacker could simply go to [https://chat.openai.com/api/auth/session/victim.css](https://chat.openai.com/api/auth/session/victim.css) and retrieve all of the victim’s authentication data, such as the access token. With the access token, the hacker could be able to authenticate himself and gain access to the victim account.

As victim.css was cached by the server because it was mistaken for a style sheet file, the hacker can easily view the victim’s session data without any blocking or difficulty.

In this way, the hacker would successfully achieve an Account takeover on the victim’s account. He would only need to wait for the victim to click on a link with a non-existent css, and then immediately obtain their access token, making this an account takeover with just one click.

## How to prevent web cache deception?

Web cache deception is easier to exploit and hence it belongs to the group of the most critical vulnerabilities.

The following are the most opted mitigation methodologies:

1. The cache server should run based on the cache-control headers set by your application, and only cache the files if their HTTP caching headers allow it.
2. Cache the files only depending upon their Content-Type header, rather than solely checking the file extensions.
3. The server should return HTTP-errors such as 302, or 404 based on the non-existent files being requested.

I hope you have enjoyed this article and learned new things, such as what an Account Takeover and a web cache deception are. This article was made for educational purposes only. The vulnerability has already been fixed in ChatGPT at the time this article was published. You can check the original twitter thread [here](https://twitter.com/naglinagli/status/1639343866313601024?t=NWfpbt6npG_QN-PERHOOiQ&s=19).
