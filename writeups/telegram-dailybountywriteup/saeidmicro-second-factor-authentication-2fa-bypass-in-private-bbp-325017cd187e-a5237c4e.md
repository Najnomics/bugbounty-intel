# Second Factor Authentication (2FA) Bypass in Private BBP

- **Source URL:** https://medium.com/@saeidmicro/second-factor-authentication-2fa-bypass-in-private-bbp-325017cd187e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240525190946/https://medium.com/@saeidmicro/second-factor-authentication-2fa-bypass-in-private-bbp-325017cd187e
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6207 (id 6207)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Second Factor Authentication (2FA) Bypass in BBP**

**Overview of the Vulnerability:**

In cybersecurity, two-factor authentication (2FA) is one of the most effective ways to secure online accounts. This method adds an extra layer of security alongside a password, such as a code sent via SMS or an authenticator app. However, if two-factor authentication is not implemented properly, attackers can exploit vulnerabilities to bypass this layer of security.

**Steps:**

1. Create account by email, I am using this email free@Palestine.com
2. Now app send verification code to your email “free@Palestine.com” and you will be redirect to this page https://app.\[Redacted\].com/register/code-verification

3\. write any random code, I used 5555 as 2FA

4\. Enable a HTTP interception proxy, such as Burp Suite or OWASP ZAP

Request:

```
POST /api/auth/resolve-email-verification-code HTTP/2
Host: app.Redacted.com
Cookie: [Redacted]
Content-Length: 38
Sec-Ch-Ua: "Not_A Brand";v="8", "Chromium";v="120"
Pragma: no-cache
Sec-Ch-Ua-Mobile: ?0
X-Site-Context: [Redacted]
User-Agent: [Redacted]
Content-Type: application/json
Accept: application/json, text/plain, */*
X-Client-Data: [Redacted]
Sec-Ch-Ua-Platform: "Linux"
Origin: [Redacted]
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: [Redacted]
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Priority: u=1, i
{"email":"free@Palestine.com","code":5555}
```
5\. I used the intruder in burp, select part of the verification code and my payload is a number from 0000 to 9999.

6\. After starting and few minutes i can bypass this code by valid code “6712”, and **login was successful.**

The site was also affected by the same vulnerability on another endpoint: https://app.\[Redacted\].com/login/code-verification 

Which also allows you to bypass two-factor authentication

This is due to two reasons, even if there is a temporary ban “**Rate limit**” to confirm the verification code, **but the code is valid for a time longer than the mentioned “10 minutes”.**The second reason is that the

**verification code must be 6 or more numbers or a combination of letters and numbers**, depending on the

**secure design**.

## Impact

1. Account Take over
2. Creating a lot of fake accounts
3. Consumption of server resources
4. The cost of sending an email
5. Reduce confidence

Duplicate ):
