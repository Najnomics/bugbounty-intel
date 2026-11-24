# Account takeover through Response Manipulation

- **Source URL:** https://medium.com/@tanyago/account-takeover-through-response-manipulation-db66c2f8830?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260514110436/https://medium.com/@tanyago/account-takeover-through-response-manipulation-db66c2f8830
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3305 (id 3305)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Account takeover through Response Manipulation

Hello everyone, I am back again with another bug. In this blog, I will discuss a bug that I encountered through response manipulation. Without further delay, let’s delve into the bug.

If you’re unfamiliar with response manipulation, let me explain it in simple terms. When you attempt to register on a website, you receive an OTP (One-Time Password) in your email. Let’s say you entered the correct OTP and captured the request using Burp Suite. If you send the request to the server using the repeater tool and examine the response, you will typically receive a “200 OK” status code, along with some headers, and ultimately a “success” message. However, what happens if you enter an incorrect OTP? In such cases, you usually receive a “400 Bad Request” status code, along with some headers, and finally an “Error” message.

Now, the interesting part begins. By manipulating the response of an incorrect OTP to mimic the response of a correct OTP, it may be possible to bypass the OTP verification process. If this concept is still unclear, allow me to explain how I discovered this bug in a particular domain.

## How I reproduce this bug

I found a parameter called “change password.” It is a common feature on most websites, allowing users to update their passwords. However, imagine if it were possible to change anyone’s password without knowing their current password.To test if this vulnerability exists, I first entered the correct password and the new password to see if it was indeed vulnerable.

I then sent this request to the repeater tool and examined the response.

Next, I attempted to change the password again, but this time I entered an incorrect password. The response I received was:

I can see that it is possible to change the response.

So I again captured the request but this time with the wrong password

By performing this method, I was able to see the response which was of course an error message but I changed the whole response with the response of the correct password and yess, I can change the password without using the correct password. However, I encountered an issue when I tried to log in with the new password. It didn’t work.

To address this, I repeated the entire process with an additional step. I changed my password using the new password obtained through response manipulation as the current password and entered a new password in the “new password” field.

For example, I initially entered “pass@123” as the incorrect password and “Light0001@” as the new password. By manipulating the response, I obtained “Light0001@” as the current password. Then, without capturing any requests, I changed my password again. This time, I entered “Light0001@” as the current password and “giyu123@” as the new password.

By doing this, I was able to successfully log into the victim’s account, leading to an account takeover.

I hope you liked this blog and learned something new from this. Let’s meet in the next blog then. Keep spreading knowledge.

You can also check some cybersecurity content here : [https://www.instagram.com/cyber\_sakhi/](https://www.instagram.com/cyber_sakhi/)
