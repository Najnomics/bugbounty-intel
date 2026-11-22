# sql injection in the http custom header fd117ba1435e

- **Source URL:** https://medium.com/@yoshimlutfi/sql-injection-in-the-http-custom-header-fd117ba1435e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230615183944/https://medium.com/@yoshimlutfi/sql-injection-in-the-http-custom-header-fd117ba1435e
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3008 (id 3008)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL Injection in The HTTP Custom Header

--

It has been a long time since my last write-up. in this short write up I wanna share my last year's findings about SQL Injection that I found in the custom HTTP header request.

So, I was doing my API penetration testing for a target. let's say redacted.com and after successful login, the request has one more HTTP header in the request, User header, and the value is a username that login to the application.

```
POST /abcd/abcd
Authorization: token
Host: redacted.com
User: user.abc
Postman-Token: token
...
{body request}
```
Now, I try to change the username for IDOR possibility but the server validates it by giving a message with a 500 internal error code and an error message that cannot get this API access.

Because this parameter is validated it is potential also for SQL Injection, so I put basic SQL Injection to the request **‘ OR 1=1- -** and send the request and with ease, the server accepts the request and gives valid information. No way :D

Okay, we got a valid SQL Injection and of course **sqlmap** will do the rest. But with this vulnerability, it turns out that we can also request to the server without an authorization token.

I hope you can take some points from my write-up, and I am sorry for being inactive for a couple of months. Have a nice day and keep learning!
