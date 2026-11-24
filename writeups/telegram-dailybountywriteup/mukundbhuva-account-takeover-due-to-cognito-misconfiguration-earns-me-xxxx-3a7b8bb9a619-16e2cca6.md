# Account Takeover Due to Cognito Misconfiguration Earns Me $xxxx

- **Source URL:** https://medium.com/@mukundbhuva/account-takeover-due-to-cognito-misconfiguration-earns-me-xxxx-3a7b8bb9a619?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230330172645/https://medium.com/@mukundbhuva/account-takeover-due-to-cognito-misconfiguration-earns-me-xxxx-3a7b8bb9a619
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1218 (id 1218)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Account Takeover Due to Cognito Misconfiguration Earns Me €xxxx

Hello Guys, I haven’t written anything in a long time.

**Vulnerability : Cognito Misconfiguration**

**Impact : Account Takeover**

**Severity : Critical**

TL;DR

I was looking for a target late at night. I find a target with a medium scope. So I picked the target. I was doing my reconnaissance and found that the target was using AWS services, and more specifically, cognito, for customer identity and access management. I recall an exercise I did a while back.

While looking into the application workflow, I discovered that the data was fetched from execute-api by email.

So I grabbed an access token and tried to get user details from the AWS CLI.

`aws cognito-idp get-user --region $REGION --access-token $TOKEN`
And I got the details as expected.

So, created 2 account :

```
Attacker : mukundbhuva+attacker@tld.me
Victim : mukundbhuva+victim@tld.me
```
I created a new token for the account mukundbhuva+attacker@tld.me and tried to change the email to mukundbhuva+victim@tld.me.

`aws cognito-idp update-user-attributes --region $REGION --access-token $TOKEN --user-attributes Name=email,Value=mukundbhuva+victim@tld.me`
I got an error :

`An error occurred (AliasExistsException) when calling the UpdateUserAttributes operation: An account with the given email already exists.`
I’m not able to change an email.

**Problem** : If the email is already registered.


However, the congito email structure is case-insensitive. So, I tried to change my email to **MUKUNDbhuva+victim@tld.me**

`aws cognito-idp update-user-attributes --region $REGION --access-token $TOKEN --user-attributes Name=email,Value=MUKUNDbhuva+victim@tld.me` Now, I was able to change attacker’s email to the victim’s.

But there was a problem: the API was not fetching victim details.


I recheck the details

`aws cognito-idp get-user --region $REGION --access-token $TOKEN`
The email was changed, but I was perplexed as to why the app couldn’t retrieve the victim’s information. After some research, I decoded the token in jwt.io. I found that the email was still the attacker’s email.

And execute-api will decode the token, grab the email, and then fetch the details.

So I’m curious what would happen if I could create a token using the victim’s email address, but JWT signature validation was a problem.

After reading some documentation, I grab the token and craft a new token from the refresh token using the AWS cli.

`aws cognito-idp initiate-auth --region $REGION --auth-flow REFRESH_TOKEN_AUTH --client-id $CLIENT_ID --auth-parameters REFRESH_TOKEN=$REFRESH_TOKEN`
I got the new access token, checked the token with jwt.io, and the email was changed to **mukundbhuva+victim@tld.me.**

The problem was solved. I tried to access account details with execute-api, and it worked. Now I could access all the details about the victim.

When it was reported to the appropriate bug bounty program, it was quickly triaged and received a €XXXX bounty.

Resolve :

I got an invite to have a drink with the team.

Timeline :

# References

Thanks For Reading✌️, Keep Hunting! 😇

👏
