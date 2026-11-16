# Broken Access Control (BAC & IDOR)

- **Source URL:** https://medium.com/@pirlo0x/broken-access-control-bac-idor-understanding-the-quiet-killer-of-web-app-security-5dc44dcf224b?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@pirlo0x
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 11323)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Let’s be real — most mature web apps today have solid defenses against the classics like SQL injection and XSS..etc. Between modern frameworks, WAFs, and automated scanners, those bugs are getting harder to land. But Broken Access Control? That’s a whole different game.

BAC isn’t about bypassing filters — it’s about slipping through logic gaps. It’s the kind of vulnerability that hides in plain sight: a forgotten endpoint, a missing role check, a multi-step flow that assumes too much. And that’s exactly why it’s become one of the most exploited and rewarded flaws in bug bounty programs today.

In this writeup, I’ll break down what BAC really means, how IDOR fits into the picture, and share some practical tricks and testing methodology to help you find and exploit these flaws — because once you understand how these bugs work, you’ll see them everywhere.

### 🧭 What Is Access Control?

Access control is the mechanism that decides **who can do what** inside a web application. It governs which users can access specific resources, perform certain actions, or view sensitive data — based on roles, permissions, or context.

For example, it decides whether:

- A user can view another user’s profile
- An endpoint is restricted to admins
- A low-privileged user can perform a restricted function meant for higher roles

### 🔓 What Is Broken Access Control (BAC) & IDOR?

**Broken Access Control (BAC)** happens when an application fails to properly enforce what a user is allowed to do. It’s not about bypassing authentication — it’s about performing actions or accessing data that should be restricted based on your role or context.

These flaws often show up when:

- Role checks are missing or weak
- Sensitive endpoints are exposed without proper validation
- The app assumes the frontend will enforce access rules

One of the most common BAC variants is **IDOR** — Insecure Direct Object Reference. This type of vulnerability arises when user-controlled parameter values are used to access resources or functions directly, without verifying whether the current user is authorized to access the referenced object.

For example:

- Changing user\_id=123 to user\_id=124 in a request and getting someone else's data

These bugs are quiet. They don’t crash the app. They don’t throw errors. But they expose sensitive data, allow privilege escalation, and often lead to high-severity bounty payouts.

### 🧪 Methodology & Testing Tricks for BAC

Before diving into Broken Access Control testing, you need to set your mindset right. This isn’t about throwing payloads — it’s about understanding the app’s logic, roles, and flow.

Start by observing what you’re allowed to do and what seems restricted. Ask yourself:

- What actions can I perform as a logged-in user?
- What data can I access?
- What’s blocked or hidden from me?

Then start mapping the roles. For example:

- **Guest**: Can browse public pages, maybe register
- **User**: Can access their own dashboard, profile, and basic features
- **Admin**: Can manage users, view sensitive data, or perform system-level actions

Your goal is to understand what each role is supposed to do — and then test what happens when you step outside those boundaries.

### 🔍 Recon Tips

- Crawl the app with different roles and compare behavior
- Inspect your Burp history for endpoints with juicy parameters like:
- userId=, orgId=, username=, role=, accountId=, etc.
- Check the page source for hidden URLs or endpoints
- Look at /robots.txt for disallowed paths—sometimes they reveal internal routes

### 🧨 Testing Tricks & Payload Ideas

#### Header Manipulation

If you’re blocked from accessing a URL, try bypassing with headers like:

GET /

X-Original-URL: /admin/deleteUser

Or:

GET /

X-Rewrite-URL: /admin/deleteUser

Some apps honor these headers due to reverse proxy setups.

#### URL Variants

Try different casing or extensions:

- /ADMIN, /admin/, /admin.json, /admin.xml
- Spring apps with useSuffixPatternMatch may treat /admin.anything as valid

#### Referrer Spoofing

Some apps check if the request came from an internal page. Try:

Referer: /admin

Especially when accessing sensitive endpoints like /admin/deleteUser.

#### ID Manipulation

If you see something like userId=123, try changing it:

- To another number (124, 999, etc.)
- To another username (Pirlo → anotherUser)
- Even if the ID is unpredictable, try using one from another account or something leaked in the response

#### Role Tampering

If you spot a parameter like role=1, try changing it:

- role=2, role=admin, isAdmin=true
- Sometimes these values are echoed back in responses — try injecting them into update or login flows

#### Redirection Leakage

Even if tampering a userId redirects you to the login page, inspect the response carefully. Some apps leak data during the redirect process—check headers, body, and any embedded info.

#### Step-Skipping Logic

Some apps enforce access control only on early steps. For example:

1. Select user
2. Confirm action
3. Submit deletion

If step 3 doesn’t revalidate access, you can skip steps 1 and 2 and directly hit the final endpoint with the required parameters.

### 🧠 Final Thoughts

Always remember that Broken Access Control isn’t about using the same trick everywhere — it’s about understanding the scenario, adapting your approach, and testing based on what the app exposes. Headers, role tampering, step-skipping, ID manipulation — they all depend on context. The more you observe, the more patterns you’ll catch.

Here we’ve reached the end of this writeup. I hope you enjoyed it and found it useful ❤️

Feel free to connect with me on [LinkedIn](https://linkedin.com/in/mohamedibrahim000).
