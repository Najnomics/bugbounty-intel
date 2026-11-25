# You Thought You Were Clicking a Button. You Weren’t. — A Beginner’s Guide to Clickjacking

- **Source URL:** https://medium.com/@l1m1nal_3ntr0py/you-thought-you-were-clicking-a-button-you-werent-a-beginner-s-guide-to-clickjacking-aca592ea489e
- **Fetched from:** https://medium.com/@l1m1nal_3ntr0py/you-thought-you-were-clicking-a-button-you-werent-a-beginner-s-guide-to-clickjacking-aca592ea489e?source=rss-80de666c3116------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14897 (id 14897)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** // l1m1nal_3ntr0py / Thu, 03 Sep 2026 21:34:41 GMT

*By // l1m1nal\_3ntr0py*

Imagine you walk into a shop and see a big sign that says “Click here to win a free gift!” You tap it excitedly. But behind that sign — invisible to you — was a different button entirely. One that just transferred all your money to someone else.

You thought you were claiming a prize. You were signing a blank cheque.

That is clickjacking. And it happens on real websites, to real people, every day.

Clickjacking — also called UI redressing — is an attack where a victim is tricked into clicking something they cannot see. The attacker places an invisible webpage on top of a fake one. The victim sees the fake page. But their click lands on the real page underneath.

The result? The victim unknowingly performs an action on a real website — liking a post, changing an email address, confirming a purchase, or deleting an account — without ever realising it.

You might have heard of CSRF — Cross-Site Request Forgery. Both attacks trick users into performing unintended actions. But they work very differently.

CSRF works silently in the background — no user interaction needed. The victim doesn’t click anything. The attack fires automatically.

Clickjacking requires the victim to actually click something. The click is real. The victim genuinely moved their mouse and pressed the button. They just had no idea what they were really clicking.

This distinction matters for defence — which we will get to later.

The technical heart of clickjacking is something called an **iframe**.

An iframe is an HTML element that loads one webpage inside another. You see iframes all the time — YouTube videos embedded in news articles, Google Maps inside restaurant websites. Completely normal and legitimate.

Attackers abuse this feature. Here is what a basic clickjacking attack looks like:

html

\<head>

\<style>

#target\_website {

position: relative;

width: 128px;

height: 128px;

opacity: 0.00001;

z-index: 2;

}

#decoy\_website {

position: absolute;

width: 300px;

height: 400px;

z-index: 1;

}

\</style>

\</head>

\<body>

\<div id="decoy\_website">

...fake content here...

\</div>

\<iframe id="target\_website" src="https://vulnerable-website.com">

\</iframe>

\</body>

Let me break down what each part does:

**opacity: 0.00001** — This makes the iframe almost completely invisible. The victim cannot see it. But it is there, sitting on top of the decoy page, waiting.

**z-index: 2** — This controls the stacking order. The iframe sits above the fake page. So when the victim clicks — even though they see the fake page — their click hits the iframe first.

**position: absolute / relative** — These CSS values ensure the iframe and the decoy page overlap precisely. The attacker carefully aligns the invisible button on the real site with the fake text on the decoy site.

The result — the victim sees “Click here to claim your prize!” They click it. But they actually clicked the “Delete my account” button on a bank website loaded invisibly behind it.

Here is a more targeted version of clickjacking that is surprisingly common.

Many websites allow form fields to be pre-populated via URL parameters. For example:

Normal URL:

https://site.com/my-account

Attacker's modified URL:

https://site.com/my-account?email=attacker@evil.com

When the victim visits the modified URL, the email field is already filled with the attacker’s email address. All the victim has to do is click Submit — and they have just changed their account email to the attacker’s address.

The attacker then overlays this pre-filled page inside an invisible iframe on a decoy website. The victim sees “Click here” and clicks. The form submits. Account hijacked.

The attacker never needed to know the victim’s password. The victim handed over access themselves — without knowing it.

Clickjacking on its own can cause real damage. Combined with a DOM XSS vulnerability — it becomes significantly more dangerous.

The attacker first finds a DOM XSS vulnerability in the target website. They craft a URL that triggers the XSS payload. Then they frame that URL inside an invisible iframe on the decoy page. When the victim clicks — the XSS executes.

This combination can steal session cookies, redirect users, or execute arbitrary JavaScript in the victim’s browser — all triggered by a single innocent-looking click.

Some actions require multiple clicks to complete — “Add to cart” then “Confirm order”, or “Delete account” then “Yes, I’m sure.”

Attackers solve this with multiple invisible layers — one decoy click for each required step. The victim clicks “Click me first!” then “Click me next!” thinking they are playing a game or claiming a reward. In reality they just completed a multi-step action on a real website.

PortSwigger built a tool called **Clickbandit** directly into Burp Suite to make finding and demonstrating clickjacking easy.

Instead of manually writing CSS to align invisible iframes, Clickbandit automates the whole process — generating the attack page in seconds. It lets you visually confirm whether a target page is vulnerable to being framed.

To use it:

Two main server-side defences exist against clickjacking:

This HTTP response header tells the browser whether the page is allowed to be loaded inside an iframe.

X-Frame-Options: deny

Completely prevents the page from being framed by anyone.

X-Frame-Options: sameorigin

Only allows the page to be framed by pages on the same origin.

X-Frame-Options: allow-from https://trusted-website.com

Only allows framing from a specific trusted website.

CSP is the modern, more flexible replacement for X-Frame-Options:

Content-Security-Policy: frame-ancestors 'none';

Nobody can frame this page — equivalent to X-Frame-Options: deny.

Content-Security-Policy: frame-ancestors 'self';

Only the same origin can frame this page.

Content-Security-Policy: frame-ancestors normal-website.com;

Only the named website can frame this page.

CSP is preferred over X-Frame-Options because it is more flexible and better supported across modern browsers.

Clickjacking works because:

It is stopped by:

The attack requires user interaction — but that interaction is genuine. The victim really does click. They just cannot see what they are clicking.

The most elegant attacks are not the most complex ones. Clickjacking works because it turns something completely normal — clicking a button — into something dangerous. No malware. No exploits. No stolen passwords. Just a carefully placed invisible layer between a user and the truth.

The button was always there. The victim just could not see it.

*Written by // l1m1nal\_3ntr0py — documenting my cybersecurity journey from scratch*

*Follow my journey:*
