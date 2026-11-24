# Easy Account Takeover on dell subdomain

- **Source URL:** https://medium.com/@2os5/easy-account-takeover-on-dell-subdomain-6297460741fd?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230319025804/https://medium.com/@2os5/easy-account-takeover-on-dell-subdomain-6297460741fd
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1626 (id 1626)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Easy Account Takeover on dell subdomain

السلام عليكم ورحمة الله وبركاته

My name is Mohamed fares and this is my first write up

hope you get benefit:

this account takeover took 3 hours to find it

I started collecting subdomains and then filtering them

I found a subdomain that has sign-up and login page

I made two accounts and started hunting

I tested every function there but nothing was found, and the last thing I was testing is reset the password I tried everything I know, and I was going to give up

while testing I found that the two emails received the same reset token!!!

how did I do that?? I did not know how I did that!

then I tried what did I do and I figured out that the request was not protected from rate limits like (capatche) or token

anyway here is the steps

1-hacker account trying to reset his password using forget password function

2- write the email in the reset field and intercept the request

3- hold that request and do not forward it

4- send the request to the repeater and in the repeater change the email to (victim email)

5- now you have two requests (one in intercept on) and (one on repeater)

6- send the two requests in the same time and you will get the same reset password token in the victim email and hacker email

AND YEAH I CHANGED THE VICTIM’S PASSWORD USING THAT RESET PASSWORD

Thanks for reading
