# 5 Different Techniques to Perform Account Takeover

- **Source URL:** https://medium.com/@aakashrathee69/5-different-techniques-to-perform-account-takeover-1926901b461a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221128170620/https://medium.com/@aakashrathee69/5-different-techniques-to-perform-account-takeover-1926901b461a
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/921 (id 921)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 5 Different Techniques to Perform Account Takeover

# 1. No Rate-Limit / Brute-Forcing

1. First Check if weak password can be set.
2. If Yes, then Check for Brute Forcing.
3. If no rate-limit or 429 Too Many Requests response doesn’t come within few minutes of Brute-Forcing you can raise the Report by mention
Weak Password Policy with No Rate-Limit

# 2. Try to send Token in Reset Password

1. Click on Reset Password
2. Enter your Email ID
3. Intercept the Request
4. add Token Parameter

```
{
  email: "victim@gmail.com",
  token: "3w4e56re7t8yriuhrgjewifhwejgowe4liogjeoigrthisismytoken"
  }
Copy
```
5\. Check if you crafted token in sent or not.

# 3. Reset Password Poisoning

- Go for Reset Password Function
- Enter you Email iD
- Intercept the request
- Change the **Host** Header to Some other Header such at attacker.com
Example :
Host :**Target.com** -> Host : **Attacker.com**
- Along with this you can also try to add new Headers (Make sure you don’t change the host header when)
- **X-Forwarded-Host**: **attacker.com**
- **Referrer**: [**https://attacker.com**](https://attacker.com/)

# 4. Response Manipulation

1. Response manipulation is way for Auth bypass
2. Try with correct username and password
3. Check the response Status and Body
4. Try with wrong username and password
5. Intercept the request
6. change the response code and body with the response of correct username and password
7. Forward the request.

# 5. Try CSRF on Major Endpoint

1. Try CSRF on Password change
2. Try CSRF on Email Change
3. Try CSRF on Phone number changeTry CSRF on Security Question Change

- If Any one is found report it.

If you like this Don’t forget to suscribe my Youtube Channel.
