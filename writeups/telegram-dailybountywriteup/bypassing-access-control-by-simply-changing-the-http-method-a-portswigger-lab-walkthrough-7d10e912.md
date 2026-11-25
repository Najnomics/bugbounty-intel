# 🐛 Bug Bounty Writeup

- **Source URL:** https://vivek0x.medium.com/bypassing-access-control-by-simply-changing-the-http-method-a-portswigger-lab-walkthrough-55084d92fa70
- **Fetched from:** https://vivek0x.medium.com/bypassing-access-control-by-simply-changing-the-http-method-a-portswigger-lab-walkthrough-55084d92fa70?source=rss-a3d6c85e9637------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14920 (id 14920)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Vivek Yadav / Mon, 21 Sep 2026 14:39:03 GMT

**Lab:** Method-based access control can be circumvented

**Difficulty:** Practitioner

**Category:** Access Control Vulnerabilities

If you’ve spent any time in web app security, you’ll know that access control bugs are some of the most satisfying ones to find — not because they’re technically flashy, but because they’re often *embarrassingly simple* once you spot them. This lab is a perfect example of that. It’s a reminder that developers sometimes build security checks around assumptions (“this endpoint will only ever be hit with a POST request”) instead of actual, robust logic — and that gap is exactly what we’re going to exploit today.

The lab description sets the stage clearly:

This lab implements access controls based partly on the HTTP method of requests. You can familiarize yourself with the admin panel by logging in using the credentials administrator:admin. To solve the lab, log in using the credentials wiener:peter and exploit the flawed access controls to promote yourself to become an administrator.

So the mission is straightforward on paper: start as a nobody (wiener), end up as an admin. How we get there is the fun part.

First things first — I clicked **“Access the Lab”** to spin up the environment.

Before trying to break anything, I wanted to understand how the *legitimate* admin functionality actually works. So I logged in using the admin credentials provided in the lab description: administrator:admin.

Once inside, I navigated to the **Admin Panel**, and found a pretty minimal interface — a list of three users, each with two buttons next to their name: **Upgrade** and **Downgrade**. Clearly, this is where an actual administrator would go to promote or demote other users’ privileges. Nothing fancy, but exactly what I needed to understand the mechanics of the feature I’d eventually be abusing.

With that understanding in hand, I logged out of the admin account and logged back in as the low-privileged user: wiener:peter.

This is the account I actually needed to escalate. Now the real work begins.

I fired up **Burp Suite** and started intercepting traffic. Specifically, I captured two requests that I knew would be important:

I sent both of these over to **Repeater**, since that’s where all the interesting tampering happens.

My initial idea was simple: take the wiener login request, swap out the relevant header/path so it pointed to /admin-roles instead, i also changes the request method from **POST to POSTX** and tack on the parameters I needed at the end of the request body:

The logic here was that if I could reuse wiener's authenticated session but redirect the request to the admin-only endpoint, maybe the server wouldn't check permissions properly.

I sent it off… and got smacked with an **“Missing Parameter ‘username’”** response.

Fair enough — that would’ve been too easy. Clearly the server *was* doing some kind of authorization check on that endpoint. But the lab title had already given me a big hint: **method-based** access control. That got me thinking about *how* the request was being sent, not just *where* it was being sent.

This is the part I genuinely enjoyed. Instead of trying to sneak the parameters into the request body via a POST request (which was clearly being checked and rejected), I decided to flip the approach entirely.

Essentially, I was now hitting the same endpoint, but via a different HTTP method (GET instead of POST), with the parameters passed differently.

I sent the request through Repeater and… nothing dramatic happened on screen, no fireworks, but the response looked different this time. No “Unauthorized” message. That’s usually a very good sign.

I refreshed the lab page to see if the change had actually taken effect server-side — and there it was: **the lab was marked as solved.**

Turns out, the access control check on /admin-roles was only being enforced for POST requests. The application's developers had (understandably, but incorrectly) assumed that since the "real" admin panel only ever sent POST requests to that endpoint, that was the only method they needed to lock down. GET requests to the same endpoint sailed right through, parameters and all, with zero authorization checks.

It’s easy to read this and think “well that’s a silly bug, who forgets to check GET requests too?” — but this exact pattern shows up in real-world applications more often than you’d expect. Developers often write access control logic tied to a specific framework route handler, a specific method, or a specific piece of middleware — and if that logic doesn’t apply *universally* across every possible way to hit that endpoint, attackers will find the gap.

The core lesson here is:

**Access control should be enforced based on *what* is being accessed and *who* is accessing it — never based on assumptions about *how* it will be accessed.**

If an endpoint performs a sensitive action, it needs to check permissions regardless of whether the request comes in as a GET, POST, PUT, PATCH, or any other method. Method-based inconsistency is a classic, low-effort attack vector — and as this lab shows, it doesn’t take much sophistication to find and exploit it. Just a willingness to try the “obvious” thing that a developer might not have thought to block.

This was a short lab, but a genuinely useful one to internalize. It’s not about writing a complicated exploit — it’s about being methodical: understand the legitimate functionality first, capture the relevant requests, and then start poking at the *assumptions* baked into the application’s logic. In this case, the assumption was “nobody will hit this endpoint with anything other than a POST” — and that assumption was wrong.

If you’re working through PortSwigger’s Access Control labs, this one’s a nice, quick confidence builder before moving on to the trickier ones involving multi-step processes and referer-based checks.

GoodByeeee….
