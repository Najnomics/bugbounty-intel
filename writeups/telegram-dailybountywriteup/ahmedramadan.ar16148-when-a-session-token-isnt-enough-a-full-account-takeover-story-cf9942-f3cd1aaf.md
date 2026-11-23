# When a Session Token Isn’t Enough, A Full Account Takeover Story

- **Source URL:** https://medium.com/@ahmedramadan.ar16148/when-a-session-token-isnt-enough-a-full-account-takeover-story-cf99421bb1e3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240925103412/https://medium.com/@ahmedramadan.ar16148/when-a-session-token-isnt-enough-a-full-account-takeover-story-cf99421bb1e3
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7357 (id 7357)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# When a Session Token Isn’t Enough, A Full Account Takeover Story

Hello, I’m Ahmed Ramadan, but most people call me Rmdn. I’m a dentist by day and a pentester and bug hunter by night. I love finding and fixing issues, whether it’s in someone’s smile or in an app’s security. Let me share one of the latest bugs I came across.

Authentication bugs are some of the most critical and interesting vulnerabilities you can find. They can open doors to unauthorized access, allowing attackers to .

In this case, I discovered a flaw in how the app handled session tokens, leading to a Full Account Takeover (ATO) without any user interaction. Let’s dive into the details.

*The OAuth Process: Everything Starts Out Smooth*


**Login in consists of two steps:**

Step 1: The user hits “Log in with Google,” and the app sends a POST request to **/auth/login/google-v3**. This request exchanges the user’s Google token for a new token that the app uses to verify them.

Step 2: The app then sends another POST request to **/oauth2/exchange**, trading the previous token for an **access\_token**. This **access\_token** is the key to unlocking all of the app’s features and personal data.

*Everything seems secure, right? Two steps, tokens flying back and forth — what could go wrong? Well, a lot, as it turns out.*

*The Structure of a Session Token*


The token returned in Step 1 response, which is then used in Step 2 to obtain the access\_token, followed a specific structure that initially seemed secure and complex enough to protect user accounts. Here’s how it appeared:

**UKP!75ac38XX-XXXX-XXXX-XXXX-XXX144f8cbf4!e3f1f9XX-XXX-XXXX-XXXX-XXX1f9835e034**

**This token is made up of two parts:**

\- **First part:** The USER\_ID, which identifies the user.

- **Second part:** A unique session value that ties the user’s session to their identity.

At this point, I started thinking: how much can I trust this structure? What if the app isn’t validating both parts of the token correctly? Could there be a loophole hiding in plain sight?

*Digging Deeper: It’s Not Just About URLs*


Now, before we get to the fun part, let’s talk about something important. When testing for vulnerabilities like Insecure Direct Object Reference (IDOR), it’s easy to assume that the manipulation happens in the usual suspects — URL parameters or the body of POST requests. But that’s just the tip of the iceberg.

Sometimes, the real action is hiding in places like **headers** or **cookies**, areas that are often overlooked during testing. And in this case, the key to unlocking the bug was sitting in the **Authorization header**.

This is a good reminder: don’t just stop at the obvious. If there’s a way to manipulate an ID — whether it’s in the endpoint, request body, or header — you should be testing it.

*The Moment of Realization: The Bug*


Okay, now let’s get to the fun part — the bug. The application was doing what it was supposed to, up until the point where it wasn’t. You see, during the login process, the app was only validating the second part of the session token — the unique session value. The USER\_ID? It was essentially just window dressing.

The app didn’t validate who you were, as long as your session value was valid. So, naturally, I decided to see what would happen if I swapped out the USER\_ID in the Authorization header for someone else’s. And guess what? The app didn’t even blink. It handed me the access\_token of the user I had impersonated.

**In a nutshell, the application was validating the session, but not the authority of the user. I could pretend to be anyone, and the app would happily give me access to their account.**

*Thanks for reading!*
