# Finding Critical bugs in Android application — (Part 1)

- **Source URL:** https://medium.com/@rudramsaraf90/finding-critical-bugs-in-android-application-part-1-88bd41807eda?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260214071745/https://medium.com/@rudramsaraf90/finding-critical-bugs-in-android-application-part-1-88bd41807eda
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3260 (id 3260)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# OTP bypass worth $300 — (Part 1)

Hey guys so i am back with another report for bugs that i have found in an Android application.

In this i am going to tell about all OTP related bugs that i found in the application

So, as I created account on the app, I directly started for testing the password reset functionality because usually there are lots of chances for finding bugs there

### **“Response manipulation**
Response manipulation is a technique where attackers make changes in the response before it reaches to the browser. With the help of response manipulation, sometimes you can bypass 2FA or Authentication and many more things.”

So I tried forget password, there i checked for responses of correct OTPs and incorrect OTPs requests.

So as we can see there is no verification method other than just “is\_valid” parameter here, so we can just change the response of the server an Boom! we can set new password for our account very simple, by this we can reset password for anyone's account, and do account takeover.

**2. Correct OTP Being Sent with ‘Random OTP’ Request**

I was just checking the requests of the forget password function, there i just caught a very interesting thing

So, the things was that the OTP was being generated in the client side only, and whenever we enter a random OTP, a request is sent to server alongside correct OTP, so the server just basically matches both the value if they matches, we are proceeded to update our password, so a attacker could easily change the values of OTP to match them and can easily perform account takeover. it was a big security risk for the users.

**3. No Rate-Limit on OTPs:**

It is that we can enter as many OTPs as we can as their was no rate limit on number of OTPs we can enter, so with a simple bruteforce attack with Burpsuite intruder with payload of numbers from 100000–999999, we could find the correct OTP, within an hour.

So these are all OTP related bugs that I have found in the application, in the other part i will share about the XSS, SQL and some other bugs that I found and the Bounty Amount that i have received 😁.

Edit: I have received a $300 bounty for this bugs

Stay tuned.
