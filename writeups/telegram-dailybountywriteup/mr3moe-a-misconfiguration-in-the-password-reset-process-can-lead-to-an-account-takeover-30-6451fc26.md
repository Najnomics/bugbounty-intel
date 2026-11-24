# A misconfiguration in the password reset process can lead to an account takeover.

- **Source URL:** https://medium.com/@Mr3Moe/a-misconfiguration-in-the-password-reset-process-can-lead-to-an-account-takeover-30c43e17d744?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240110013206/https://medium.com/@Mr3Moe/a-misconfiguration-in-the-password-reset-process-can-lead-to-an-account-takeover-30c43e17d744
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4707 (id 4707)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**what’s an account takeover**

**Account takeover** (ATO), also known as **account hijacking** , is a Attack in which an unauthorized person or entity gains access to a user’s online account, such as an email, social media, bank, or e-commerce account.

**Description**

While I was conducting testing on a web application, I came across the **Reset Password** page. Since this page often contains vulnerabilities that could lead to an account takeover, I spent some time analyzing the requests from the page using **burp suite** , one request catch my eye the request was made after I put my email and clicked on **reset password** .

the request lead to the link below which that link sent to my email and by using that link I could change my password .

`https://example.com/Account/ResetPassword?uid=MTAwNzI5&v=6wR3uhoKkkkvyPczPSdvN%2bdSPrvGnhuibE%3d&ts=637581561547&dd=XcviVw9v2oMde/Q4VnMI`
The first thing I did was to try using the link to change my password and then reuse it, and it worked! I could have reported it, but I decided to escalate the severity to an account takeover.

So, I started to dig deeper and found out that if I remove the **ts** and **v** parameter, they do not affect the password-changing process, and there’s no validation from the application so the **uid** was the only parameter the application checking it .

If you notice that the **uid** is base64 encoded, I decoded it in Burp, and the result was **100729** , which is much easier to guess because the **uid** is only a number in a small range, and it never changes. This **uid** serves as a static ID for each user, and by guessing the **uid** using burp intruder by set the **uid** range from **100000** to for example **200000** , I was able to change the users password in that range .
