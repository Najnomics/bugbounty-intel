# Insecure Refresh Token Usage Leads to Account Takeover (IDOR)

- **Source URL:** https://medium.com/@mhmodgm54/insecure-refresh-token-usage-leads-to-account-takeover-idor-14c4a9ec504b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250901015651/https://medium.com/@mhmodgm54/insecure-refresh-token-usage-leads-to-account-takeover-idor-14c4a9ec504b?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10399 (id 10399)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Insecure Refresh Token Usage Leads to Account Takeover (IDOR)

## Introduction

In this write-up, I detail an **IDOR vulnerability** found not in the main application domain, but in the **authentication domain**. This flaw allowed me to obtain the **JWT access token of any user** by abusing the OAuth2 refresh token flow. With this token, I could **fully impersonate** any user on the platform, resulting in complete **Account Takeover (ATO)**.How notice

## How I Noticed the Issue

While browsing the site, I often forward interesting requests to Burp Repeater for further testing. One day, after leaving a request in the Repeater for about 10 minutes, I sent it again and received a `401 Unauthorized` response.

This was unusual — because when I performed the same action via the browser, it worked without issues and didn’t ask me to log in again. That made me curious.

I decided to **passively monitor** the network requests from the browser to the server, without manually interacting with the page.

## Discovery Steps

I noticed a `POST` request being sent to the authentication domain:

`POST https://auth.target.com/oauth/token`
This request returned a **fresh JWT token** (access\_token) for the user. The only parameters being sent were:

```
grant_type=refresh_token
refresh_token=<token>
client_id=<client_id>
```
### Testing the Parameters

- I observed that the `client_id` was the **same** for different accounts using the same interface.
- Example: logging in via `www.target.com` → `client_id=xxxx`
- Logging in via `community.target.com` → `client_id=yyyy`
- The important parameter here was the **refresh_token**

To test further, I:

1. Created a second account.
2. Grabbed the `refresh_token` of the second account.
3. Used it in the same POST request, from the session of the **first account**.

The server responded with the **JWT token of the second account**.

This meant I could:

- Access the account of the second user.
- View and edit their profile.
- Perform any actions on their behalf.

## Misconfiguration

This vulnerability is due to two critical flaws in the authentication flow:

1. **Lack of Binding**: The server **does not verify** that the refresh token being used actually belongs to the currently authenticated user/session.
2. **Static Refresh Tokens**: The `refresh_token` remains the same for months, meaning a stolen/leaked token can be reused indefinitely.

## Tips

- Always **observe token exchanges**, especially between the front-end and authentication services.
- **Small abnormal behaviors** (like inconsistent errors or missing re-authentication) may lead to serious vulnerabilities.

## End

unfortunately cause the `refresh_token` is use uuid which not guessable and can’t get it when interact with victim profile they deal with it as P5
