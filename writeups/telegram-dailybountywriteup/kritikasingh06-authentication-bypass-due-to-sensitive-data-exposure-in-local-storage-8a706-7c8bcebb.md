# Authentication Bypass due to Sensitive Data Exposure in Local Storage

- **Source URL:** https://medium.com/@kritikasingh06/authentication-bypass-due-to-sensitive-data-exposure-in-local-storage-8a706c798800?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240525183745/https://medium.com/@kritikasingh06/authentication-bypass-due-to-sensitive-data-exposure-in-local-storage-8a706c798800
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6184 (id 6184)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Authentication Bypass due to Sensitive Data Exposure in Local Storage

Hey Infosec buddies!

I’m Kritika. This is my very first blog post on Web Application Security. Today, I’m shining a spotlight on one of my recent finding: *Authentication Bypass due to data exposure* that I have found in a program on Bugcrowd. I hope you’ll find this post informative.

# **Introduction**

Basically, the target application was a social live-streaming app, where you can login or signup into your account using your phone number. You need to enter verification code sent to the provided phone number to create your account. *Simple!*

## Let’s dive into it

The very first thought came into my mind was to bypass this verification code using response manipulation method.

Firstly, I created an account using my Phone number and solved captcha.

A verification code was sent to my Phone number. I entered that correct 4-digit code and captured this request in burp. Right-clicked on the Request and selected **Do Intercept -> Response To This Request**. The response to that request looked something like this:

I again created an account using any arbitrary phone number. Then, entered a random 4-digit code and intercepted this request in burp. Captured the response to that request and this time the response body looked like this:

It seems that the following details specific to a victim user was required: Username, accountID, hostname and port to bypass the code. :\


I again visited the application to find these details.

I started looking for them in the application’s page source and in Storage tab. In local Storage tab, I observed that my account information such as username, accountID etc. were displayed.

I logged out of the application to check if the information was still visible after logging out. But It didn’t work. :(

I opened that application in a **private window of a browser (or in another browser)** and again checked Local Storage (without being logged in). And Guess what!?

I found the username, accountID, hostname and port number of other user. The application was disclosing the information of other users (different each time) in the Local Storage tab without being authenticated.

Then, I went to that captured response in burpsuite to try them. I compared both the responses, one with the correct OTP and other with incorrect OTP. After that, I modified the parameter values in this response body (of incorrect OTP request) as according to the values shown in the response body with the correct OTP request (e.g. “loginResult”: “LOGGED\_IN”). And entered the user specific information from the Local Storage and then forwarded the response.

Yay! It worked.🤩🥳

I successfully bypassed the verification code and entered into someone else’s account. :D

Note: I could not gain access to just any user account, but only to users whose data was disclosed within the app at a particular point in time. That’s why, the severity of the issue was decreased to P2.


You can follow me on **Twitter** or connect with me on [**LinkedIn**](https://www.linkedin.com/in/kritika-singh-6058421aa/).

Thank you. Happy hacking! 🥰
