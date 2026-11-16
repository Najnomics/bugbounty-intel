# Escalating Self-Stored XSS to Complete Admin ATO

- **Source URL:** https://mugh33ra.medium.com/escalating-self-stored-xss-to-complete-admin-ato-7a7c98b324fe?source=rss------bug_bounty-5
- **Fetched from:** https://mugh33ra.medium.com/feed
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 13682)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### The Target

I have been hunting on this subdomain for about a month consistently. It is a feature-rich platform organizations, clubs, roles, permissions, image uploads, forms, invitations the kind of app that makes you excited as a bug hunter because more features means more attack surface.

But here is the thing. This is a **10 year old bug bounty program**. I even found an old YouTube video of someone hunting on this exact subdomain about a year ago and they only went after IDORs and access control issues. Which means by the time I got here, those were locked down tight. Every small harmless feature properly authorized. It was boring.

So I changed my approach.

I had already submitted 5 vulnerabilities on this target including a **1-Click Account Takeover** chained from a self-stored XSS but that is another story.

[https://mugh33ra.medium.com/escalating-self-stored-xss-to-complete-admin-ato-7a7c98b324fe](https://mugh33ra.medium.com/escalating-self-stored-xss-to-complete-admin-ato-7a7c98b324fe)

By this point I was looking for something different. Something that required deeper analysis.

That is when I started thinking about **CSPT**.

### What is CSPT?

Before I get into the story let me explain what Client-Side Path Traversal actually is because I see a lot of confusion around it.

Most people know **server-side path traversal** where you inject ../ into a file path parameter to read sensitive files like /etc/passwd. CSPT is completely different.

**CSPT is not about reading files. It is about hijacking which API endpoint gets called.**

Modern web applications make HTTP requests from the browser using fetch(), axios, XMLHttpRequest. These requests often include a path that is constructed dynamically using user-controlled values. If that value is not sanitized, you can inject ../ to traverse out of the intended path and redirect the request to a completely different endpoint.

The browser normalizes the traversal automatically. So if the app calls:

`fetch('https://target.com/api/v1/endpoint/../../user', { method: 'GET' })`
The browser resolves it to:

GET https://target.com/user

The app did it. The victim’s session did it. You just pointed it in the wrong direction.

### Sources and Sinks

To find CSPT you need to understand two things:

**Sources** where attacker-controlled input enters the application:

- URL query parameters ?id=value
- URL path segments /app/resource/value
- Form fields stored and reused later
- API response values stored client-side and used in future requests
- localStorage or sessionStorage values

**Sinks** where that input flows into an HTTP request path:

// Template literal sink

fetch(\`/api/resource/${userControlledValue}\`);

// String concatenation sink

axios.delete('/storage/file/' + storedPath);

// Stored value reused in request

const path = getStoredPath();

fetch(path, { method: 'DELETE' });

The goal is to find a **source → sink** chain where your controlled input reaches a fetch/XHR call without sanitization. If that request method is DELETE or POST targeting a state-changing endpoint you have something critical.

### Step 1 Finding the Sources First

My approach was backwards from what most people suggest. Instead of hunting for traversal first, I started by **mapping critical state-changing endpoints with no request body**.

Why no body? Because in CSPT you control the path not the request body. So your target endpoints need to work with just the path and no additional parameters.

I went through the app as a regular user and intercepted every destructive action:

**Source 1 Delete Account:** I clicked on delete account in my profile settings. The request was:

DELETE /user

No body. No token. Just the endpoint.

**Source 2 — Leave Organization:** I clicked leave organization:

`POST /organisation/{random-ORG-ID}/leave`
No body again. Another good candidate.

**Source 3 Delete Organization:** I logged in as admin and went to org settings and clicked delete org:

`DELETE /organisation/{ID}`
No body.

Now I had three critical targets. The goal was clear find a CSPT that can redirect a DELETE or POST request to any of these endpoints.

### Step 2 Hunting for the Sink:

I spent time manually going through every feature looking for path traversal. Form fields, image uploads, profile settings, club names anything that might feed into a URL. I found nothing that obviously worked.

This is where most people give up. I almost did.

Then I remembered I had a saved .md file from a previous JS analysis session where a CSPT candidate was flagged in the main bundle. It pointed to a deleteFile function:

```
async function fQ(t, e) {
 const n = (e.startsWith(“/”) ? “” : “/”) + e;
 return !!await t.apiMethod(`delete:storage/file${n}`)
 // Only check: does e start with “/”? No traversal prevention.
}
```
This function takes a path e, checks if it starts with /, and appends it to storage/file. That is it. No validation. No allowlist. No traversal check. Just a simple prefix concatenation.

If e is /../../user then the final call is:

delete:storage/file/../../user → DELETE /user

Now I needed to find where this function gets called and what controls the path value it receives.

### Step 3 Finding the Full Chain

I went to my profile settings and uploaded a profile image with DevTools network tab open.

The upload fired two things:

**First** a POST request to update user data with this in the body:

```
{
  "avatar.filesize": 67937,
  "avatar.path": "user/{Hashed-UserID}/{Some-Hash}.png"
}
```
**Second** when I uploaded a new image, the app automatically fired:

`DELETE https://target.com/storage/file/user/{UserID}/{someHash}.png`
The app was deleting the old image before saving the new one. And the path it deleted was the avatar.path value from the POST body the value I just sent. The value I fully control.

This is the sink. The chain is:

avatar.path in POST body (source)

→ stored server-side

→ auto-DELETE fires to stored path (sink)

→ no validation between storage and deletion

### Step 4 Calculating the Payload:

The DELETE fires to:

`https://target.com/storage/file/ + {avatar.path}`
I need to land on:

https://target.com/my-endpoint

So I need to escape two directory levels out of /storage/file/:

/storage/file/ + /../../my-endpoint

→ /storage/file/../../my-endpoint

→ resolves to → /my-endpoint

Payloads:

/../../user

For org deletion: orgID already leaked via an api-endpoint

`/../../organisation/{orgID}/delete`
### Step 5 Testing on Myself:

I intercepted the profile image upload POST request and changed avatar.path to:

/../../user

Forwarded. Got 200 OK. Payload stored.

Then I uploaded another image. The app auto-fired:

DELETE https://target.com/storage/file/../../user

→ DELETE https://target.com/user

My account was gone.

This is why I said 70% complete earlier self exploitation is not enough for a critical finding. I needed to prove real impact.

### Step 6 Escalating to Maximum Impact:

This is where it gets interesting.

I logged back in with a fresh account and noticed the platform has a **club settings** feature. The club has its own image separate from profile images. And club image upload is the **lowest possible permission** you can grant a member. No delete button. No admin features. Just image upload and name change. Completely harmless looking.

I gave this permission to a test account (the attacker). The attacker uploaded a club image and I intercepted the request same structure, same avatar.path field, same auto-DELETE behavior on next upload.

I changed avatar.path to /../../user and forwarded.

The club image now appeared blank to everyone in the org.

Now here is the beautiful part **I did nothing else.**

The owner saw the blank image and naturally tried to upload a new one. The app fired its auto-DELETE to the stored path:

DELETE https://target.com/user

Owner’s account gone.

Another member with club settings permission saw the blank image and tried to fix it. Same result. Account gone.

One by one. Every user who touched that upload button lost their account permanently. The attacker had already left the building after Step 1.

When the last member triggered it the org itself was destroyed since no accounts remained.

**Both goals achieved mass account deletion AND org deletion from the lowest possible privilege level.**

### Why This Bypasses Authorization

The org delete endpoint returns **403 Forbidden** when called directly by a low-privilege user. So how does this bypass it?

Because the DELETE request does not come from the attacker. It comes from the **victim’s own authenticated session** fired by the app’s own JavaScript. The server sees a legitimate request from someone who has session context. The attacker just redirected where that request goes.

This is what makes CSPT fundamentally different from a direct unauthorized API call. The app becomes the weapon.

### The Honest Timeline

- **Day 1–2:** Manual hunting for CSPT, found nothing
- **Day 3:** Revisited old JS analysis notes, found the deleteFile function
- **Day 4:** Connected the sink to the avatar.path source, confirmed exploitation
- **Two weeks later:** Finally submitted the report 😂

I knew it would not be duplicated so I took my time writing a proper report. No regrets.

already fixed

My favorite sentence:

“Consistency looks like nothing is happening until everything changes.”

### Final Words

Consistency is everything in bug bounty. I hunted this target for a month. Most sessions felt like nothing was happening. Then one saved note and one YouTube video connected everything.

Big shoutout to **@Magn4\_** for the CSPT explanation that made this possible. Go watch his content.

[https://youtu.be/T6BKQ2O06B0?si=m5d3gu7G6-OWds1k](https://youtu.be/T6BKQ2O06B0?si=m5d3gu7G6-OWds1k)

If you found this writeup helpful then make sure you smash the follow button for more writeups in the future 🙂

Let’s connect:

Happy Hunting 🎯
