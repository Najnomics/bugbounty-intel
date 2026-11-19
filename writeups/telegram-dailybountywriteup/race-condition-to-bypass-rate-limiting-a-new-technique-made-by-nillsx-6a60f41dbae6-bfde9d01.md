# Race Condition to Bypass Rate-Limiting

- **Source URL:** https://infosecwriteups.com/race-condition-to-bypass-rate-limiting-a-new-technique-made-by-nillsx-6a60f41dbae6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250527060427/https://infosecwriteups.com/race-condition-to-bypass-rate-limiting-a-new-technique-made-by-nillsx-6a60f41dbae6
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8446 (id 8446)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Race Condition to Bypass Rate-Limiting: A new technique made by Nillsx

**Hi, Security Researchers!**

First of all, I hope you’re doing well today. In this article, I’ll walk you through how I chained multiple vulnerabilities (**Rate-limiting bypass with race condition and host header injection, and non-expiring password reset link**) to create a powerful exploit. This vulnerability can easily be **overlooked**. Before we dive into the technical details, let me introduce myself for those who don’t know me.

**Whoami❓**


**Hello,** my name is **Snillx.** I am a **self-taught** and **bilingual Brazilian** who has been deeply involved in studying **cybersecurity** to help create a **safer internet** and assist **companies** in keeping their **users** protected from cyber threats. My experience includes identifying vulnerabilities such as **Reflected XSS** (RXSS), **Insecure direct object references** (IDOR), **One Time Password Bypass** (OTP Bypass) and **SQL Injection** (SQLi).

Without wasting any more time, let’s dive into the article!

## **Introduction**

This time, I was searching for vulnerabilities in a **bug bounty program** on the [*Intigriti*](https://www.intigriti.com/) platform. While reviewing the scope, I came across a **subdomain** which, due to the program’s guidelines, we’ll refer to as **carbrand.redacted.com**. Upon accessing the domain, I noticed a **login** and **registration section**, and from there, I knew exactly what to do.

## Time to exploit

I decided to create a account with the name ***“nillsx-victim@intigriti.me”***. I then began a **reconnaissance** process on the application. After some exploration in the **logged-in session**, I returned to the **login page** and started testing the “Forgot password” feature. I captured the **request** sent to initiate a **password reset** and began my exploration.

Initially, I sent a **password reset link** to my email and **forgot** about it. After analyzing the request (about **two minutes** later), I decided to send **another link**. I used the most recent link in my **email** to **change** my **password**. After updating the password, I noticed the first link and thought, **“Why not try opening it?”** To my surprise, clicking the link redirected me to the **password change page** again. I was shocked.

I decided **not** to **change** the password right away and instead **updated** my email from “***nillsx-victim@intigriti.me”*** to “***nillsx-victim2@intigriti.me”***. After the email change, I returned to the **unused link** and used it to change my password. When I returned to the **main site**, I found my actual session closed, and my **password** had been **changed** — even though the reset link was sent to ***nillsx-victim@intigriti.me***, the account was now associated with **nillsx-victim2@intigriti.me**. Them i decided to know how the flow works.

I returned to the saved **request** in my **Burp Suite** and attempted to send **two consecutive** reset links for **further testing**. When I sent the two links with a **minimal time interval**, I noticed that only **one** link arrived in my email. With this in mind, and knowing it would be ideal for the **triager** to have clear **step-by-step** reproduction steps, I began searching for a way to **bypass** the **rate limiting** imposed in this area.

## Rate-limiting bypass with Race condition and Host Header Injection

At this point, I was trying **everything** to make the **race condition** work, as I only needed **two** immediate requests to **succeed**. I labeled the requests as **“request 1”** and **“request 2”**, grouped them in a tab as **shown** in the **image** below, and set them to be **sent in parallel**. I then began testing various injections:

Eventually, I decided to use [**Burp Collaborator**](https://portswigger.net/burp/documentation/collaborator) to test for password reset poisoning. By injecting the **Burp Collaborator** link in this format: **“burpcollaborator.carbrand.redacted.com”** I received two links **simultaneously** in my email. Although the password reset poisoning **didn’t** work, I discovered a unique way to **bypass** protections against **race conditions**.

*If you’re interested in using this technique and manage to find a valid bug or something similar, feel free to email me. I’d be thrilled to know that a technique I developed helped the community.*


Now that I have everything set up, it’s time for the **PoC** (Proof of Concept).

## **Proof of Concept (PoC)**

**Description**

The application contains a vulnerability in the password reset mechanism, allowing an attacker to bypass request limitations through a combination of Host Header Injection and a Race Condition. This ultimately enables an Account Takeover, even after the account’s email and password have been changed.

**Steps to Reproduce**

1. **Create an account:**

- Register a new account using the email [victim@intigriti.me](mailto:victim@intigriti.me).

**2. Initiate a password reset request:**

- Navigate to `https://carbrand.redacted.com/index.php` with Burp Suite open.
- Turn the intercept on and request a password reset for your account.
- Intercept the password reset request in Burp Suite and send it to the Repeater tab.
- Drop the intercepted request in Burp’s Intercept tab (to avoid sending it directly).

**3. Set up multiple requests in Burp Suite:**

- In the Repeater tab, duplicate the request twice, so you have three identical requests.
- Modify the Host header in each request as follows:
- Request 1: `Host: carbrand.redacted.com`
- Request 2: `Host: test1.carbrand.redacted.com`
- Request 3: `Host: test2.carbrand.redacted.com`

**4. Trigger a race condition:**

- Group the three requests into a Group Tab in Burp Suite.
- Click the arrow next to the Send button and select **Send group in parallel (last-byte sync)**.
- Click **Send Group (Parallel)** to send the requests simultaneously.

**5. Observe the result:**

- Check the **inbox** for [victim@intigriti.me](mailto:victim@intigriti.me).
- You will receive two password reset emails instead of one, **bypassing the request limitation**.

**6. Reset the password:**

- Use the link in the last email to reset your password.

**7. Log in and change account details:**

- Log in to the account at `https://carbrand.redacted.com/index.php` using the new password.
- Change the email associated with the account to [victim2@intigriti.me](mailto:victim2@intigriti.me).

**8. Exploit the outdated password reset link:**

- Open the unused password reset email link sent to [victim@intigriti.me](mailto:victim@intigriti.me).
- Use the link to reset the password again, even though the email address was changed.

**9. Verify account takeover:**

- Log in to the account using the new email ([victim2@intigriti.me](mailto:victim2@intigriti.me)) and the password you just reset.
- You now have full access to the account.

**Key Observations**

- The Race Condition and Host Header Injection were used to bypass request limitations.
- However, the account takeover is also possible without these techniques if you wait for around one minute to send another request manually.

I was quite excited to have discovered something **new** and **unexplored**. However, the report ended up being marked as **“out of scope”** due to the requirement of a c**ompromised user account**. And because the race condition didn’t have a **big role** in this, they say that make a **separate report** wouldn’t be great. Despite this, the **discovery** itself made it all worthwhile.

**In conclusion, always look for different ways to approach something you already know how to do. Never underestimate your knowledge.**
