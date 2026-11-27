# An IDOR and Auth Bypass That Led to Mass Account Takeover — KSFE

- **Source URL:** https://1-day.medium.com/an-idor-and-auth-bypass-that-led-to-mass-account-takeover-ksfe-db04cec8d730?source=rss------bug_bounty-5
- **Fetched from:** https://1-day.medium.com/feed
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 7780)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### An IDOR and Auth Bypass That Led to Mass Account Takeover — KSFE

### INTRODCUTION

Hello friends, I’m a 3rd year BCA student & part-time Bug hunter who is very passionate about cybersecurity (Mainly web). Here is a quick article on how I was able to find a mass account takeover / Data breach vulnerability on KSFE pravasi portal (Online Chit Platform 

introduced for the welfare of Malayalees living outside Kerala.)

YOU CAN JOIN MY DISCORD SERVER HERE : https://discord.gg/xSs964qF

### THE DISCOVERY

On a Monday night, I was bug hunting on Bugcrowd. My father walked into my room and suggested that I try hunting on KSFE’s Pravasi Chitty website, as he was struggling to log in due to its complexity (lol it’s actually easy, he’s just not a tech-savvy).

Quickly I closed my all tabs and visited portal.pravasi.ksfe.com and saw a Customer login page.

I didn’t do any subdomain discovery because my goal was to find an Auth bypass vulnerability in this subdomain.

And it started . . .

### TARGET

KSFE pravasi portal is a organisation partially owned by Kerala government which is for the Malayalees who live outside Kerala, for managing their chit stuff online. It does require sensitive information of a user in-order to create an account. (Government ID card, License, other data).

### ENTRY POINT

It’s a login page which has a forgot password functionality, I tried the user login feature but it’s pretty secure, So I’m now on to the forgot password functionality.

The forgot password requires 2 parameters which are “username” and either the Phone number or Email linked to that account.

So if I have an account username, I also need its phone number/email linked to that account.

I found a way to bypass that checks, Here’s how I did it…

### STAGE 1 (Response Manipulation)

- Enter a valid username of a valid user and enter random phone number like 9999999999
- As the account details provided is incorrect, I was sure it will respond with a failure response.
- The response was a “200 OK” but with the response body as “38”, Yes, Just the number 38.

We could easily guess that it was now performing some client-side validation of the response “38” before further processing. So, I checked the JavaScript source code and found something interesting.

Here you can see an “If” statement which checks the response from server.

If the response is “38", It will just print error message and will not proceed.

But if it is “9”, The client side proceeds to the next step of validation which sends the OTP to the registered email address.

In short, 38 is for error and 9 is for success.

- I started Burpsuite response capturing, Entered a valid username and random phone number, captured the response.
- Now change the 38 to 9 and forward.

SUCCESS!!! The first step is bypassed and now it asks for the OTP.

### STAGE 2

The first step is bypassed, now it asks for OTP sent to the registered phone number/email.

I thought, if it was vulnerable to response manipulation, why wouldn’t it work on this step too?

I entered a random OTP and checked the response:

Here you can see the response returns the letter “N” for invalid OTP

So it can be easily guessed that the success response would be “Y”.

I tried another OTP and changed the response to “Y” and forwarded.

BOOM! it worked, and redirected me to the password change page.

Now I can change the password of the user, I tried changing my password and it was changed successfully.

And I tried logging in to the account and I was able to login to the account with the changed password.

### THE FUN PART (Mass account takeover + Data breach)

Now straight to the fun part…

I captured the password change request and I can see the parameters used for password change are:

The interesting part is that, The website creates you a default username like user5555, user9388, user6747 which is in a sequential order.

Most of the website’s users are non-techy old people, So most of them will not change the default username created by the website.

I was able to capture the password change request and replay it using tampered “username” parameter and it worked successfully. A successful IDOR.

I can change any user’s password by just changing the username parameter.

### MASS ACCOUNT TAKEOVER / DATA BREACH

Now i can easily create a script which sends this request many times and looping from user1 to user999999, which will change every user’s password. (I didn’t created it, As it is against the responsible disclosure policy).

After logging an account (My test account), I can see the sensitive information being disclosed such as Address, Aadhar card, License, images and more.

An attacker can create a script which changes all user’s password, login and scrape the data from user’s dashboard, and can even download the government ID, License, Pictures from the portal.

This can lead to a mass data breach of user’s PII.

### RESPONSIBLE DISCLOSURE

I reported this vulnerability to CERT IN immediately and they fixed the vulnerability in a span of 1 week.

The vulnerability was patched and it was no longer exploitable.

### CONCLUSION

This was my quick writeup on how I was able to find a potential data breach and account takeover on KSFE pravasi portal.

Please clap for my writeup if you liked it!

Thank You
