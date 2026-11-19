# How i’ve found

- **Source URL:** https://medium.com/@zack0x01_/how-ive-found-idor-xss-all-users-account-takeover-a49d59cf5108?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@zack0x01_
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 6515)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### How i’ve found : ( IDOR + XSS ) = all USERS account takeover :) ?

### Hello, Hackers! 👋

My name is zack0x01. In today’s blog, I’m excited to share one of my wild findings in bug bounty hunting:

#### IDOR chained with stored self-XSS, leading to a complete platform account takeover for all users! 😲

### Let’s begin:

I’ve been testing this app for a while now. It’s an event organizer application where event managers can organize events and manage registrants. My goal was to understand how the application handles authorization and authentication of requests.

#### Attack Process:

1. Account Creation: I created two accounts with some random customer data for each account.
2. Data Access Attempt: I tried to access the data of Account Two from Account One (the attacker account).

3\. Customers Tab: I went to the “Customers” tab on my account where I could see all my clients.

4\. Intercepting and Modifying Requests:

- I intercepted the request and modified it from:

```
{
  "eventID": 23423423
}
```
to

```
{
  "eventID": victimID
}
```
- Unfortunately, I got a 403 Unauthorized response from the server. 🚫

**5. New Idea:** Since they were using numerical IDs to access data, I used Burp’s “Autorepeater” extension to match every request with my “eventID” to the victim’s “victimEventID”.

**6. Testing Every Function:** I tested every function of the app while the requests were being modified in the background, but unfortunately, no success until now. 😢

**Giving Up? Not Yet! 💪**

After some shawarmas and fresh orange juice, it was time to get back to the game.

**7. Email Template Edit Function:**

- I tested every function separately and found an email template edit function.
- I discovered that I could add a new block to the email template. I added a text block with “this is test123”.
- Intercepting the request showed it was being saved like this

```
{
  "json": "%7b%0a%22%64%61%74%61%22%3a%22%7b%74%65%78%74%3a%74%68%69%73%20%69%73%20%74%65%73%74%31%32%33%7d%22%2c%0a%65%76%65%6e%74%49%44%3a%32%33%34%32%33%0a%7d",
  "eventID": 43534
}
```
The json parameter contained the URL-encoded version of our added text.

**Decoding and Injecting XSS:**

- I decoded it, resulting in :

```
{
  "data": "{text:this is test123}",
  "eventID": 23423
}
```
- injected an XSS payload into the text parameter: \<img/src=x onload=confirm(1)>.

```
{
  "data": "{text:<img/src=x onload=confirm(1)>}",
  "eventID": 23423
}
```
- Encoded it back and sent it.

```
{
  "json": "%7b%0a%20%20%22%64%61%74%61%22%3a%20%22%7b%74%65%78%74%3a%3c%69%6d%67%2f%73%72%63%3d%78%20%6f%6e%6c%6f%61%64%3d%63%6f%6e%66%69%72%6d%28%31%29%3e%7d%22%2c%0a%20%20%22%65%76%65%6e%74%49%44%22%3a%20%32%33%34%32%33%0a%7d",
  "eventID": 43534
}
```
- On refreshing the page, my XSS payload was executed! 🎉 But it was still self-XSS. 🤔

### **Final Steps to Success:**

1. **Modifying the Event ID:**

- I modified the eventID to the victimID and got a 200 OK response with a null body.
- I quickly checked the victim’s account to see if I modified the email template. Guess what? It got executed! 😱

**Whats the impact here ?**

We can brute-force through the eventID parameter as it is a numeric ID, inject our payload into all platform users, and steal all their accounts! 😈

Thank you so much for reading this. See you in the next write-up! 👋

*💡 Want to learn how I actually find real bugs like this? Check out my full course — it’s built step-by-step for hunters who wanna level up fast. Also join the* ***101 Coaching Program*** *for hands-on guidance and live feedback.*

*🔍Learn more :* [*https://lureo.shop/*](https://lureo.shop/)

**Tap into my world , follow me on :**

🕶️ [Instagram](https://www.instagram.com/zack0x01)

👁️ [Twitter (X)](https://x.com/zack0x01)

🕳️ [Medium](https://medium.com/@zack0x01_)

🔥Check out my YouTube channel here🔥 [https://www.youtube.com/@ZACK0X01](https://www.youtube.com/@ZACK0X01)

Stay lurking. Stay hacking. 🖤💻
