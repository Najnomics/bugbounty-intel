# Turning a Harmless Self-XSS Into a Full Profile Takeover

- **Source URL:** https://medium.com/@oopssec-store/turning-a-harmless-self-xss-into-a-full-profile-takeover-d06cac1c50c3
- **Fetched from:** https://medium.com/@oopssec-store/turning-a-harmless-self-xss-into-a-full-profile-takeover-d06cac1c50c3?source=rss-9143a4639fd4------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14900)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** OopsSec Store / Sun, 06 Sep 2026 19:01:00 GMT

A Self-XSS is usually a shrug — it only fires in your own browser, so triagers close it as low severity. But pair it with a profile endpoint that has no CSRF token, and that same harmless bug lets you inject JavaScript into anyone’s profile.

You’ll do it locally against [OopsSec Store](https://github.com/kOaDT/oss-oopssec-store), a deliberately vulnerable shop built for this kind of practice.

Open a terminal in an empty directory and run:

npx create-oss-store oss-store

cd oss-store

npm start

That one sequence installs the dependencies, spins up a database, seeds it with test data, and serves the app.

Give it a minute. When it’s done, head to localhost:3000 and you'll land on the store.

If you’d rather not install Node.js, Docker works too:

docker run -p 127.0.0.1:3000:3000 leogra/oss-oopssec-store

Log in and click your way to the profile page at /profile. There's a form there with a bio textarea, the kind of *"tell people about yourself"* field you've seen a thousand times.

Here’s the catch. That bio gets rendered back to the page with React’s dangerouslySetInnerHTML, and nothing sanitizes it first. Whatever HTML you save comes straight back into the DOM.

On its own that’s Self-XSS. You can only poison your *own* profile, which is why bug bounty programs usually wave it off.

The second target is the endpoint behind that form: POST /api/user/profile. It authenticates you with an HTTP-only cookie, but it doesn't check a CSRF token, an Origin header, or anything else that proves the request actually came from your own page.

Neither bug is scary alone. Chained, they let an attacker run JavaScript inside someone else’s profile.

There are two flags here. The first proves the XSS. The second chains it with CSRF for the real payoff.

**Log in.** Use the seeded test account:

**Go to /profile.** Find the bio textarea in the form.

**Drop in a payload.** You don’t need anything fancy.

**Hit Save Profile.** The page re-renders with your saved bio, the \<img> tries to load a source that doesn't exist and an alert() pops. That's your confirmation — the browser executed HTML you controlled.

This one plants the XSS in a *victim’s* profile instead of your own. You need admin access to reach the exploit page, so start there.

For **Flag 1**, the API notices the HTML tag in your bio and hands you the flag right in the response. You’ll also watch the alert() fire once the profile re-renders — two independent signs the injection landed.

For **Flag 2**, the endpoint checks the Referer header. Because the request came from the exploit page and not from /profile, the server flags the account as CSRF-exploited. The phishing page then bounces you over to /profile, the profile page sees that flag on the account, and it prints your prize.

You’ll see the stored XSS fire in the bio area at the same time. That’s the “proof of hack” — a request you never intended rewrote your profile *and* seeded it with running JavaScript.

Start with the XSS. The bio goes into the page through dangerouslySetInnerHTML, which shoves raw HTML into the DOM with no filtering.

Now the CSRF. The update endpoint trusts a cookie and nothing else:

POST /api/user/profile   ← authenticates via HTTP-only cookie

← no CSRF token

← no Origin check

← no meaningful Referer validation

The cookie uses sameSite: "lax". Lax feels safe, but it still sends the cookie on top-level navigations — and a form submission that navigates the user counts as one. Since the endpoint also accepts application/x-www-form-urlencoded, a plain auto-submitting \<form method="POST"> from any origin would work too.

The failed assumption is the same one behind most CSRF: “if the cookie is attached, the user meant to do this.” The browser attaches cookies automatically. Intent was never verified.

Fix both bugs. Each one is a real hole even if the other gets patched.

**Sanitize the bio.** Never hand untrusted content to dangerouslySetInnerHTML unfiltered. Run it through [DOMPurify](https://github.com/cure53/DOMPurify) first:

import DOMPurify from "dompurify";

\<div dangerouslySetInnerHTML={{ \_\_html: DOMPurify.sanitize(bio) }} />

Better still, if the bio is meant to be text, render it as text and let React escape it for you. No dangerouslySetInnerHTML at all.

**Add real CSRF protection.** Put an anti-forgery check on every state-changing endpoint. Synchronizer tokens, double-submit cookies, or sameSite: "strict" on the auth cookie all close the door. Here's the token check in the handler:

```
const csrfToken = request.headers.get("X-CSRF-Token");
const expectedToken = session.csrfToken;
if (!csrfToken || csrfToken !== expectedToken) {
  return NextResponse.json({ error: "Invalid CSRF token" }, { status: 403 });
}
```
Don’t lean on Referer as your defense — it can be missing or stripped, and it's the wrong tool for the job. A per-session token that the server issues and verifies is what you actually want.

Chained bugs are how a lot of real incidents happen. No single finding looks alarming on the triage board, so each gets deprioritized — and then someone stitches them together. Self-XSS plus CSRF is a textbook pairing, and stored-XSS-via-CSRF has shown up in real disclosures against major platforms for years.

That’s the whole reason to care as a developer. You don’t get to close a bug as “low severity” in isolation, because attackers don’t attack in isolation. The unsanitized field and the missing token are each one dependency away from being critical.

Practicing on something like OopsSec Store is the cheap way to internalize that.

**Do not deploy OopsSec Store on a production server.** This application is intentionally vulnerable and should only be used in isolated, local environments for educational purposes.

**Do not exploit vulnerabilities on systems you don’t have explicit authorization to test.** Unauthorized access to computer systems is illegal. Always obtain proper permission before performing security testing.

**AI assistance was used in the writing of this writeup.**

Having trouble following this writeup? Found a typo or have suggestions for improvement?

Feel free to [open an issue](https://github.com/kOaDT/oss-oopssec-store/issues) or [start a discussion](https://github.com/kOaDT/oss-oopssec-store/discussions) on GitHub.

👉 If you find this project useful, consider giving it a star or forking it to show support!
