# From ‘alert(1)’ to Account Takeover

- **Source URL:** https://medium.com/@saltify/from-alert-1-to-account-takeover-a-story-of-4-digit-bounties-and-bypassing-html-sanitisers-dd8ca0ac502b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250318014852/https://medium.com/@saltify/from-alert-1-to-account-takeover-a-story-of-4-digit-bounties-and-bypassing-html-sanitisers-dd8ca0ac502b
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9069 (id 9069)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From ‘alert(1)’ to Account Takeover: A Story of 4-digit Bounties and Bypassing HTML Sanitisers

Hello everyone! For this bug bounty write-up I will be detailing my recent experience with introducing XSS testing into my methodology. I reported my first XSS vulnerability in February of 2025, and wanted to share my learning experience with the hope that some of you find it useful.

The target is a program on Intigriti that I will refer to as `redacted.com` since I can’t fully disclose the vulnerabilities.

*What is XSS, anyway?*

Cross-Site Scripting (XSS) is a client-side vulnerability which allows an attacker to inject malicious JavaScript (JS) into a webpage, tricking a victim’s browser into running your code. This vulnerability can range from popping a simple alert box to achieving full Account Takeover when the page is tied to an authenticated session.

# Chapter 1: The first XSS

After a few weeks of trying to find reflected and stored XSS vulnerabilities on the main application with no success, I found a subdomain called `saltify.promotion.redacted.com` which allows for limited customisation of a publicly-facing webpage used for advertising.

After testing the usual `asdf"<>` payloads in every field to see if any characters were left unescaped in HTML, I noticed that one of the parameters was getting reflected in two different places:

- Once in a `<p>` tag, where it was displayed to the user.
- And once inside a `<script>` tag:

```
<script>
  ...
  window.title = `${companyName} | asdf"<>`
  ...
</script>
```
As you can see, my payload was escaped using HTML encoding, and trying to break out of the string with a backtick was escaped using a backslash, meaning that a`` `;alert(1) `` payload would still be kept within the string.

`` window.title = `${companyName} | \`;alert(1)` ``
There was clearly some sort of sanitiser at work here which was insisting on making my life difficult. However, there was one more option — my payload was getting passed into a [JavaScript template literal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals).

This technology allows for expressions to be used within a string to dynamically generate content. In this case, updating the window title to contain my company name. However, template literals aren’t limited to just variable names — they will run any valid JS expression you throw at them.

By using the payload `asdf${alert(1)}` the string became:

```
<script>
  ...
  window.title = `${companyName} | asdf${alert(1)}`
  ...
</script>
```
allowing me to inject arbitrary JS into the page, popping the alert!

## Escalation

Since this page wasn’t a core piece of functionality and getting a victim to land on it was unlikely, I wanted to escalate this vulnerability to maximum impact — Account Takeover.

The session cookie for the app had the `HttpOnly`flag meaning that I couldn’t access it using JavaScript, but I noticed that it was scoped to the root domain `*.redacted.com`, meaning it would be included in HTTP requests from my site `saltify.promotion.redacted.com` to `victim.redacted.com`.

I quickly coded up a JavaScript exploit which did the following via a series of API calls using the victim’s session cookie:

- Fetch all users from the victim’s organisation
- Extract the emails and IDs of all users with the ‘Admin’ role
- Change the passwords of all Admins to `newPassword123` (Admin users in this company have permissions to change the password of other users)
- Send all admin email addresses to my server

I then Base64 encoded this JavaScript exploit and used the payload `${eval(atob('PASTE HERE'))}` to inject it into the page.

This exploit would give me full access to any company if an Admin user visited my page. The company rewarded this finding with a 4-digit bounty with a ‘High’ severity according to the CVSS scoring.

# Chapter 2: Bypassing the HTML sanitiser

After getting rewarded for the previous XSS, I wondered if I could find another vulnerability on the same subdomain, since the target allows for limited customisation of the HTML within the advertising page.

Functionality like this is great place to search for XSS since the only thing preventing JS injection is usually a HTML sanitiser, such as [DOMPurify](https://github.com/cure53/DOMPurify). Thankfully, the target was running their own self-built sanitiser, and these tend to be a lot easier to bypass.

## Beginning the search

I began by fuzzing HTML tags, and the only interesting ones that the sanitiser allowed were `<img>`, `<style>`and `<a>`. After fuzzing the attributes, I noticed that most attributes that could execute JS were blocked, ruling out payloads such as `<img src=x onerror=alert(1)>`.

Links like `<a href="https://example.com">`were allowed, so I tried the JavaScript URL scheme `javascript:alert(1)` , but this was removed by the sanitiser. In situations like this, it’s important to understand which part of the payload is blocked. Is the word “javascript” blacklisted? Is it the colon? Or are brackets not allowed in URLs?

Upon further testing, `href="aa”`was allowed but `href="a:a”` was removed, likely revealing a blacklist against single colons not followed by `//`. This would usually be a pretty effective fix, but I noticed one thing…

The tag was embedded into the DOM using JavaScript, more specifically the `element.innerHTML()` function — which will HTML-decode certain input.

## With a little help from innerHTML…

This finding revealed a lot of options, since the payload `<a href="javscript:alert(1)">link</a>` would be HTML decoded by the `innerHTML`function, and should pass the blacklist since it doesn’t contain any colons.

I sent the payload, clicked the link and… it worked!

I then used the same JavaScript exploit from before to escalate this to Account Takeover, and submitted a report. The vulnerability is still in the Pending state, but I’m hoping for another bounty from the company once it gets reviewed!

# Key takeaways

- **Thoroughly test custom-built HTML sanitisers** — If it’s not a hardened library like DOMPurify, there’s a good chance the developer made a mistake writing it.
- **Blacklist-based sanitisers are much easier to bypass than whitelist-based ones** — Blocking bad stuff is good, but only allowing good stuff is better.
- **Context is everything** — A payload’s power depends on where it lands, like a template literal or an innerHTML call.
- **Always escalate XSS**— An alert(1) is great and might land you a quick bounty, but always try to demonstrate full impact.
