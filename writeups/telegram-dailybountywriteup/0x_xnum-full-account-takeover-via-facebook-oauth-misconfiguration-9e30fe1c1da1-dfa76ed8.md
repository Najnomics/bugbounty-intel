# Full Account Takeover via Facebook OAuth Misconfiguration

- **Source URL:** https://medium.com/@0x_xnum/full-account-takeover-via-facebook-oauth-misconfiguration-9e30fe1c1da1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250925053545/https://medium.com/@0x_xnum/full-account-takeover-via-facebook-oauth-misconfiguration-9e30fe1c1da1
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7399 (id 7399)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Full Account Takeover via Facebook OAuth Misconfiguration

hey there,

Today, I’m going to share with you an interesting bug I found in one of Bugcrowd’s programs. It was in a program that had a “Login via Facebook” feature.

Grab your coffee, and let’s get started! 😉

So, in the target login page, and there it was an option to log in with Facebook.

I clicked on it and logged in. After that, I found myself on the page where I could edit the access permissions (you might see it as “ modify access permissions” or “Edit Access” ):

I clicked on it and I unchecked the checkbox that shares my email address with the app:

then, I clicked Continue to proceed with the login without sharing my email. After disabling email sharing, the target site prompted me to provide an email address since it couldn’t retrieve it from Facebook.

So, I entered the victim’s email address (and this step didn’t require any verification or proof of ownership). to my surprise, I got redirected straight to the victim’s account! Just like that, I took over the account!

but yeah, of course happy endings only happen in movies. My report was marked as a duplicate of another pre-account report submitted four days before me, saying it was the same root cause (OAuth misconfiguration).

## Lesson Learned!

Always verify user data after OAuth login. Make sure the system properly checks critical details like email addresses, even if they aren’t shared by the OAuth provider. Test how the system handles missing or altered data to prevent account takeovers and ensure user security.

## Contact :

Also, feel free to check out my **bug hunting notes and resources**:
