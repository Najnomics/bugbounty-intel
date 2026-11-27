# How I Discovered Critical Bugs in an Android Employee Management App

- **Source URL:** https://mrshan.medium.com/how-i-discovered-critical-bugs-in-an-android-employee-management-app-8a842173d2dc?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260602080903/https://mrshan.medium.com/how-i-discovered-critical-bugs-in-an-android-employee-management-app-8a842173d2dc
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14046 (id 14046)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Discovered Critical Bugs in an Android Employee Management App

Hey folks,

Welcome back to another story from my Android pentesting journey. Myself Shan, A Application Security Analyst Doing penetration testing on Web, Mobile applications, and Penetration testing on Linux, Windows environment.

**Note:** This blog content is human‑generated, with spelling and grammar refined using AI tools. Please continue reading.


The application name has been redacted. The app’s primary function is simple: **Punch In** and **Punch Out**. In addition, it provides features such as applying for leave and checking work hours. During punch‑in, the application also collects the user’s geolocation to record where the punch‑in occurred.

## Finding #1: Geolocation Manipulation

While logging into the application, I noticed that geolocation data was being used. I assumed this was to determine whether the user was punching in from home or the office. This led me to a question:

*What if someone tries to punch in from a completely different location by spoofing their coordinates?*


Turns out — it was possible.

I triggered a punch‑in request and captured it using **Burp Suite**. In the request, I modified the **latitude** and **longitude** values and then forwarded it. The punch‑in was completed successfully using the spoofed location.

To confirm this, I checked the admin portal’s web application, and the manipulated location was correctly reflected there.

## Finding #2: Weak Face Registration (Liveness Bypass)

Next, I created a new user via the admin portal and attempted to log in. During the process, the application prompted me to complete **face registration**.

I immediately wondered whether this could be bypassed using a pre‑recorded video. The required actions were static and minimal — mainly an eye blink. I recorded a video of myself using my phone and played it back in front of the face‑scanning screen.

Surprisingly, the system accepted it, and the face registration was completed successfully. 😄

## Finding #3: Broken Object Level Authorization (BOLA)

After some time analyzing requests, I noticed that certain headers contained a **userId**. This made me consider testing for a **BOLA (Broken Object Level Authorization)** issue.

I first tried changing the userId in the headers, but those requests were properly validated and blocked. 😞

However, I noticed that the **punch‑in request** included the same userId inside the **JSON request body**. I modified this userId to that of another user and sent the request.

The punch‑in was successful.

To verify, I checked the admin portal — and sure enough, the punch‑in had been recorded under the manipulated user’s account.

WOWWWW!!!!

Thanks for reading! I’ll continue sharing interesting findings from my security assessments. Feel free to check out my previous walkthroughs as well. 🙂
