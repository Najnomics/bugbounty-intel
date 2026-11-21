# How I Chained Template Injections Across Pages to Trigger Reflected XSS

- **Source URL:** https://medium.com/@zoningxtr/how-i-chained-template-injections-across-pages-to-trigger-reflected-xss-5d4ef68efac5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250502080016/https://medium.com/@zoningxtr/how-i-chained-template-injections-across-pages-to-trigger-reflected-xss-5d4ef68efac5
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9468 (id 9468)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🛑 How I Chained Template Injections Across Pages to Trigger Reflected XSS

# **By** [**@zoningxtr**](/@zoningxtr)

In this write-up, I’ll walk you through how I successfully chained a series of unsanitized template injections across multiple pages to exploit a **Reflected Cross-Site Scripting (XSS)** vulnerability using a classic payload: `javascript:alert(1)`.

# 🔍 The Application Flow

I was given access to a simple web app with the following structure:

1. **Welcome Page** — Presents a sign-up link:

`<a href="/frame5/signup?next=confirm">Sign up</a>`
**2. Signup Page (signup.html)** — Renders a link to the next step:

`<a href="{{ next }}">Next >></a>`
**3. Confirmation Page (confirm.html)** — Redirects users after a few seconds:

`setTimeout(function() { window.location = '{{ next }}'; }, 5000);`
**4. Backend Code (Python, GAE webapp)** — Passes `next` as-is to both templates:

`if "signup" in self.request.path:     self.render_template('signup.html', {'next': self.request.get('next')}) elif "confirm" in self.request.path:     self.render_template('confirm.html', {'next': self.request.get('next', 'welcome')})`
# ⚠️ The Vulnerability

Both `signup.html` and `confirm.html` directly embed the `next` parameter from the URL into their templates **without sanitization**. This means any input is rendered **verbatim** into the page.

This is extremely dangerous when those values are embedded inside **JavaScript (confirm.html)** or **HTML attributes (signup.html)**.

# 💡 The Insight

The `signup.html` page contains:

`<a href="{{ next }}">Next >></a>`
If I control the value of `next`, I can inject arbitrary JavaScript using the `javascript:` URI scheme:

`<a href="javascript:alert(1)">Next >></a>`
Boom — XSS with one click.

# ✅ Final Payload

Here’s the link that triggered the vulnerability:

`/frame5/signup?next=javascript:alert(1)`
When this is visited:

- The rendered `href` becomes `javascript:alert(1)`
- Clicking the link instantly executes the payload

# 🔗 Why This Works

- The app trusts `next` blindly across pages
- `signup.html` outputs `next` in an `href` — no sanitization
- `javascript:` links **execute directly** on clic
- There’s **no Content Security Policy (CSP)** or URL validation to prevent this

# 🛠️ How to Fix It

- ✅ Whitelist safe URLs for redirection (e.g., internal paths only
- ✅ Never allow `javascript:` or `data:` in `href` attributes
- ✅ Escape or sanitize template variables based on context
- ✅ Consider using a templating engine that automatically escapes output

# 🎯 Final Thoughts

This was a textbook example of **contextual XSS** — where unescaped data is injected into HTML attributes or JavaScript. The clever bit? The vulnerability wasn’t in one place — it was **chained across templates**, and the real win was recognizing the use of `next` in multiple contexts.

If you’re building web apps — never pass user input into templates unsanitized. And if you’re hunting bugs — always trace parameters across multiple pages. That’s where the fun begins. 🕵️♂️

Let me know if you’d like this turned into a downloadable PDF or if you want to publish it on a blog or GitHub as part of a write-up series!
