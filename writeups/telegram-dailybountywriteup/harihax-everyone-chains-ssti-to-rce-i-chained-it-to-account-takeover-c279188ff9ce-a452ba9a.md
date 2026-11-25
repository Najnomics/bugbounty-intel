# Everyone Chains SSTI to RCE. I Chained It to Account Takeover.

- **Source URL:** https://medium.com/@HariHax/everyone-chains-ssti-to-rce-i-chained-it-to-account-takeover-c279188ff9ce
- **Fetched from:** https://medium.com/@HariHax/everyone-chains-ssti-to-rce-i-chained-it-to-account-takeover-c279188ff9ce?source=rss-88f7f86bd7c7------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14899)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** HariHax / Sat, 05 Sep 2026 17:24:43 GMT

*Three attempts at code execution paid nothing. One template expression that just read a variable paid $1,000.*

Hello hackers,

Second write-up. I found a **template injection** — a bug where text I type gets treated as code by the server instead of as plain text — and went straight for remote code execution, like everyone does. Failed three times. Then got paid $1,000 for an expression that only *read* a variable.

Before any of the bug makes sense, you need to know what this product is.

It’s a **subscription billing platform**. Companies use it to bill their own customers on a recurring basis — think a gym billing its members monthly, or a software company billing its subscribers.

So there are two very different sets of people using it, with **two completely separate login systems**:

**1. Company staff** log into the admin panel. They add customers, create invoices, and configure how the billing works. Anyone can get one of these accounts — the free trial signup is public, no invite needed, and it gives you full settings access straight away. **This is the only account I ever had.**

**2. That company’s customers** log into a separate customer portal, using their own email and password. They go there to view their invoices and pay them. It’s a different login page and a different set of credentials.

One of the things company staff can configure is the **emails the platform sends to those customers** — the invoice email, the receipt, the payment reminder. There’s an editor where you write the wording, and the platform fills in the details (customer name, amount due, due date) before sending.

**That editor is where this bug lives.**

**The wall I was trying to break:** as company staff, I can write the emails customers receive. I cannot see their portal passwords, and I cannot log into their portal accounts.

By the end of this, I could.

**One note before we go further:** every “customer” in this write-up is a test account I created myself, inside my own trial company, using email addresses I control. Nobody real was involved and no real customer data was touched.

I wasn’t fuzzing anything. I opened the email editor and read the default wording that shipped with the product. It already looked like this:

```
{% if %} … {% endif %}
{{invoice.balance|number_format(2)}}
```
Those {{ }} and {% %} markers are how a **template engine** works. You write placeholders, and the server swaps in real values before sending. {{invoice.balance}} becomes the actual amount owed.

That specific syntax — {% %} blocks with |filter(args) pipes — is **Twig**, the template engine used by PHP applications.

Which raises the obvious question. The app runs this text through a template engine. I can edit this text. **Can I write my own placeholder and make the server run it?**

Before touching the email editor, I tested a smaller field — the setting that controls your invoice number format. Classic probe:

`A{{7*7}}Z`
If a template engine processes it, {{7\*7}} comes back as 49.

The app replied HTTP 200 — success. The next invoice came out normal. No 49. I tried three more variations. Three more 200s. Nothing.

Four saves, four success responses, zero evaluation. The natural conclusion: *my text was stored and printed exactly as typed, so this field doesn’t run a template engine.* Dead end.

**That would have been the wrong conclusion.**

Instead of trusting the response, I reloaded the settings page and looked at what was actually saved. **The field was unchanged.** My payload wasn’t in there at all. The app had silently thrown my input away and replied 200 regardless.

So there were two completely different things that could be happening, and they looked identical from my side:

A success response can’t tell those apart. Only reloading and re-reading the saved value can.

*(That field turned out to be genuinely safe — it only accepts six specific placeholders from a fixed list. But I’d nearly used that one safe field to write off the whole feature.)*

This is the part people ask me about, so let me be exact. **The attack needs two separate requests, and they do completely different things.**

In the email editor, I put my expression into the **subject line** of the invoice email template and hit save:

POST /…/settings/messages/save

`message[message_subject]={{ my expression here }}`
**This is the injection point.** My expression is now stored inside my company’s email template. It just sits there until something renders that template.

Nothing happens yet. I can’t see any result — which was the whole problem for a while.

To see a template actually render, an email normally has to be sent. But the platform has an **email preview screen**: it builds the email on the server and shows you the finished result, before anything goes out.

GET /…/customer/email?ref\_id=1000

**ref\_id is the invoice number I want to preview.**

Here’s the key. When the server builds that preview, it needs real values to fill the placeholders — so it loads **the details of whichever customer that invoice belongs to**. Their name, their email, their account record.

So the arrangement is:

I inject once. After that I just change ref\_id and preview again to aim the same expression at a different customer.

First check:

`ARITHMETIC[{{7*7}}]   →   ARITHMETIC[49]`
It’s evaluating. But 49 proves very little on its own — even a properly locked-down template engine is allowed to do arithmetic. So I asked for something a locked-down one is supposed to refuse:

`PHP[{{constant("PHP_VERSION")}}]   →   PHP[8.2.28]`
constant() is a PHP function that reads values out of the language itself. Getting a real version number back means my expression was running inside the actual application, and that constant() wasn't blocked.

**To be clear: constant() is only proof.** It plays no part in the attack that follows. I used it once to confirm the engine was genuinely evaluating my input, and never touched it again.

*(*The vendor later told me their protection was switched on — just not configured to block constant(). I've since confirmed it myself: {{ \[1,2\]|reduce("max") }} aborts while the arrow-function form renders, which only happens under a sandbox.*)*

Template injection in a PHP app, so obviously the next step is remote code execution. That’s the reflex, and it’s what nearly every write-up with this fingerprint does.

Three separate attempts. All failed, for one simple reason.

To run code, you need to reach a **function you can call**. Every value available inside this template was plain data — names, numbers, text. No functions attached to any of them. I worked through roughly 200 possible function names across all 25 values the template could see.

There was nothing to call.

Clean negative. Zero dollars.

Instead of trying to *do* something with the template, I finally asked what was already *inside* it:

`{{_context|json_encode}}`
\_context is Twig's name for "everything this template can currently see." Encoding it as JSON prints the whole lot. About **20 KB** of internal data came back.

And sitting in there was users\[0\].

**This is the important bit.** users\[0\] is **the customer portal account belonging to the customer who owns the invoice I previewed** — the exact account they use to log in. And it wasn't the tidy version the app shows elsewhere. **It was the raw row straight out of the database, with every column included.**

So I asked for three of those columns:

```
[hash={{users[0].saas_password}}]
[salt={{users[0].saas_salt}}]
[tok={{users[0].login_token}}]
```
Back came three things:

That last one is the dangerous one. A **login token** is a single-use code that logs you straight into the portal with **no password at all** — it’s what sits behind the “click here to reset your password” link in a reset email.

Now put this together with Part 3.

users\[0\] is filled in from whichever invoice I named in ref\_id. So **changing one number in the preview URL changes whose password hash and whose login token get printed back to me.**

That’s the whole vulnerability in one sentence: **I choose the customer, and the app hands me their login credentials.**

The hash is crackable offline, which is worth reporting by itself. The login token is better — it’s a working credential right now, no cracking required.

One catch: **a login token only exists in the database after something creates one.** A customer who has never requested a password reset has an empty token field. So I had to make one appear.

The password reset form is public — logged out, normal browser, no account needed. I know my target’s email address because they’re my company’s customer and it’s listed in my own admin panel.

POST /…/reset\_do

email=customer@example.com

This writes a fresh login\_token into that customer's database row, and emails them a link containing it.

**Two things matter here:**

Back in my admin account, I look up that customer’s invoice number. They’re my company’s customer, so their invoices are listed right there in my admin panel.

Then I preview the invoice email against **their** invoice:

GET /…/customer/email?ref\_id=\<their invoice number>

The server fills my saved template with their record — including the token it created seconds ago.

My template subject line contains {{users\[0\].login\_token}}. The preview screen prints it back to me in plain text.

I now hold a working login credential for someone else’s portal account, and I never went near their inbox.

Logged out, fresh browser, no cookies. I use the token exactly the way the reset email link would:

GET /…/logintoken/\<token>

**And I’m inside their customer portal.**

That’s how I know the token works — not because it looked important in the JSON, but because I redeemed it and it logged me in. Their profile page showed their real name and email address. Then I ran the entire chain again against a second customer to prove it wasn’t a fluke.

**Two things make it worse than it first looks:**

***The app has a clean version of a user and a raw database version, and it handed the template the raw one.***

Here’s what makes it hard to argue with. The platform’s **own API** returns a user object with no password hash, no salt, and no login token. Those fields aren’t included at all.

So the app already knows exactly which fields are secret. It applies that knowledge in the API and forgets it in the template.

Same story with the template protection — not missing, just incomplete. Switched on, and still allowing constant(). A half-finished control looks exactly like a working one until somebody asks it the right question.

CVSS 8.5 · High · CWE-1336 → CWE-522 / CWE-640 A05:2025 Injection · A02:2025 Security Misconfiguration

**Bounty: $1,000** — the maximum this programme pays. The vendor confirmed both problems and opened two separate fixes.

**Reading can beat executing.** Code execution is the reflex, and it’s often the hardest thing a template injection can actually do. Three rounds of trying got nothing. One command that simply listed what the template could see got me password hashes.

**A success response doesn’t mean it saved.** Four responses said 200 and stored nothing. Reload the page and check what the app actually kept.

**Ask what a template can *see* before you ask what it can *do*.** Dump the contents on your first successful render, read the list of what’s in there, and then decide where to spend your time. I did it backwards and burned three rounds.

If you’ve chained a template injection to something other than code execution, tell me in the comments — I think “look at what it can read first” is under-rated advice and I’d like more examples.

See you in the next one 👋

**HariHax**
