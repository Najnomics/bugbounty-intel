# Random account takeover via misconfigured OAuth

- **Source URL:** https://medium.com/@Berserker1337/random-account-takeover-via-misconfigured-oauth-5dc2cbbbe905?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240630223516/https://medium.com/@Berserker1337/random-account-takeover-via-misconfigured-oauth-5dc2cbbbe905
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5826 (id 5826)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Introduction:**

Hey, I hope y’all are doing great. This vulnerability is an account takeover for random users and I believe that this might be common. I will be explaining this in detail below.

# Recon:

Let’s start by recon, the program scope was only the main website and mobile app. I tested the mobile app API and found a bunch of bugs then I thought of testing subdomains and finding a critical vulnerability that could reflect on the main website/mobile app. I found a staging subdomain that has a different database and I confirmed that by logging in with the credentials of the main app. Then moving on to the vulnerability.

# The vulnerability:

The vulnerability itself is simple to exploit but first let’s understand how this vulnerability works. What seems the problem is the developers used the same signature and structure of JWT for the stage and main site which led to random account takeover then using an account JWT created in stg-redacted.com on redacted.com would be valid due to the misconfiguration that was done by the developers. So, when I tried to find a critical vulnerability I thought of this immediately then I noticed in the staging app every user created has a sequential ID with the same structure. Then I instantly created an account and copied the JWT for the account I created.

As you can see in the response the ID is \[1000987\]. When copying in the JWT of the staging app and then pasting it in the main app it logged me in a random account with a user ID of \[1000987\] the same user ID as my account in the staging app.

The image attached shows the PoC with a random user with the same user ID of the staging app. You might ask why is it a random account takeover because you basically cannot control which user ID you want to take over. However, this might be named a mass takeover because of the potential destruction that might lead to the app. I forgot to mention that the same JWT could be used in the main website and mobile app it depends on how your target configures their environment.

# Steps to reproduce:

1. Navigate to the Staging Environment
2. Account Registration: Complete the sign-up process with your details. Note the sequential ID assigned to your new account, for example, ID `1000987`.
3. Authorization Token Extraction: After successful registration and login, access the browser’s developer tools or inspect the API response to find the `Authorization` token. Copy the `Authorization` token for the next step.
4. Account Takeover on Main Site: Navigate to the main site. Using the browser’s developer tools or your API testing tool, replace the existing `Authorization` token with the token copied from the staging environment.
5. Access a functionality that requires authentication. You’ll observe that you’re now authenticated as the user with the specific ID `1000987` from the staging environment, effectively taking over random accounts in the main environment.

# Remediation:

The developers should use different secrets for signing JWTs in different environments. This change ensures that a token from one environment cannot be used in another.

# Conclusion:

In conclusion, finding a critical vulnerability might be easy but you have to think outside of the box. Furthermore, try to test every staging subdomain with an Oauth configured as I explained today you don’t know how a developer thinks.
