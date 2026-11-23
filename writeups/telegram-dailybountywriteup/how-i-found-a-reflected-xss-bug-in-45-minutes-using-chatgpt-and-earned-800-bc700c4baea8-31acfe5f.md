# How I Found a Reflected XSS Bug in 45 Minutes Using ChatGPT — and Earned $800

- **Source URL:** https://theindiannetwork.medium.com/how-i-found-a-reflected-xss-bug-in-45-minutes-using-chatgpt-and-earned-800-bc700c4baea8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250505065024/https://theindiannetwork.medium.com/how-i-found-a-reflected-xss-bug-in-45-minutes-using-chatgpt-and-earned-800-bc700c4baea8
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9329 (id 9329)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Found a Reflected XSS Bug in 45 Minutes Using ChatGPT — and Earned $800

# 🧠 Summary:

Bug bounty isn’t always about months of recon or complex 0-days. Sometimes, a well-placed payload in the right context can pay off fast. In this post, I’ll walk you through how I stumbled upon a **reflected XSS** bug using a mix of manual testing, ChatGPT-assisted payload crafting, and good old persistence — earning me **$800 in just under an hour**.

This write-up includes:

- Real recon steps
- Dead ends and failed payloads
- ChatGPT prompt examples
- Live debugging moments
- A complete, realistic PoC
- Reporting strategy

# 🎯 Target Background

The program was private, but the company is a well-known SaaS platform in the productivity space. Scope included only:

`https://app.target.com`
No subdomains, no mobile apps — just the main web app.

# 🔍 Step 1: Light Recon (10 minutes)

I logged into the app, clicked around, and noticed a basic search feature in the dashboard:

`https://app.target.com/search?q=meeting+report`
I pasted a random test string:

`?q=TEST123`
And it reflected in the DOM like:

`<div class="result-info">Showing results for TEST123</div>`
It looked like a **safe reflection** — basic HTML escaping was happening. But I know modern apps often render this data inside React/JS templates.

# ❌ Step 2: Trying Obvious Payloads (10 minutes)

I tested the usual suspects:

- `<script>alert(1)</script>` — rendered as plain text
- `<img src=x onerror=alert(1)>` — escaped
- `"><svg onload=alert(1)>` — blocked

Then I opened Burp and looked at the response source.

Inside the HTML, I found this:

```
<script>
  window.searchQuery = "meeting report";
</script>
```
Ah ha! The input was being embedded inside a JS string. This meant **JavaScript context**, not HTML — completely different payload strategy.

# 🤖 Step 3: Asked ChatGPT for JS-Context Payloads (5 minutes)

I prompted:

*“Give me payloads for reflected XSS where input is embedded in JavaScript string context like: var x = "\<user input>";.*


ChatGPT gave back:

`";alert(1);//`
I tried this

`?q=";alert(1);//`
Nothing fired. The reflection looked fine.

# ⚠️ Step 4: False Positives and Debugging (10 minutes)

The response had:

```
<script>
  window.searchQuery = "";alert(1);//";
</script>
```
It looked like it should have worked.

So I:

- Tried in Chrome — nothing
- Tried in Firefox — nothing
- Thought: Maybe CSP is blocking?
- Opened DevTools → No CSP headers found
- Disabled extensions — still nothing

💡 Then I realized: **The app loads a second JS file dynamically after page load.** That JS was overriding the global `window.searchQuery` var immediately — before `alert(1)` executed.

This was the missing piece.

# 🧪 Step 5: Adjusting Payload Timing (5 minutes)

ChatGPT suggested wrapping the payload inside a `setTimeout()`:

`";setTimeout(()=>alert(1));//`
I URL encoded it:

`?q=%22%3BsetTimeout(()=>alert(1))%3B%2F%2F`
✅ Boom. Alert popped after 100ms delay.

Proof the payload survived long enough to execute before being overwritten by subsequent scripts.

# 🔒 Step 6: Evaluating the Impact

This XSS was:

- Reflected in **authenticated dashboards**
- No `Content-Security-Policy` headers present
- Session cookies were `HttpOnly=false` and **sent with every request**

💥 This meant I could craft a malicious link like:

`https://app.target.com/search?q=%22%3BsetTimeout(()=>alert(document.cookie))%3B%2F%2F`
And if a logged-in user clicked, I could:

- Steal session cookies
- Modify DOM (e.g., fake forms for phishing)
- Exfiltrate data via JS

# 📝 Step 7: Writing the Report (5 minutes)

My HackerOne report included:

- Vulnerable URL with PoC payload
- Explanation of JavaScript string injection
- Screenshots of live PoC
- Suggested fix: context-aware escaping + CSP
- Note: No customer data accessed, only my own session used

# ⏱ Timeline:

- 🕒 Bug found: \~45 mins after starting
- 📝 Reported: Immediately
- ✅ Triaged: Within 2 hours
- 💰 $800 bounty awarded the next day

# 🎓 What You Can Learn

🔹 **Always view the raw response** — DOM rendering can hide real context

🔹 **Know your contexts** — HTML, JS string, JS event handlers, URL — all need different payloads

🔹 **ChatGPT is a powerful assistant** — especially for payload brainstorming

🔹 **Don’t give up at first failure** — browser quirks and script order matter

🔹 **Even small bugs pay well** — if they’re exploitable in a real-world scenario

# 🧰 Tools Used:

- Chrome + Firefox
- Burp Suite Community
- DevTools
- ChatGPT
- URL-encoder.org

# 💬 Final Words

This wasn’t a fancy SSRF or chained 0-day. Just a well-timed, well-placed **reflected XSS**, found through smart testing and fast iteration. And for that, the program paid $800.

You don’t need to be a genius — just consistent, curious, and technically aware.

📖 Blog: [**TheIndianNetwork**](/)

📺 YouTube: **@TheIndianNetwork**

📧 Email: **theindiannetwork@protonmail.com**

💰 Go find your bug — even 45 minutes can make your day.
