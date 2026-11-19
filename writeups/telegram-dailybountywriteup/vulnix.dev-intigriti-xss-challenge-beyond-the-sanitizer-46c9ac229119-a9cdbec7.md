# Intigriti XSS Challenge

- **Source URL:** https://medium.com/@vulnix.dev/intigriti-xss-challenge-beyond-the-sanitizer-46c9ac229119
- **Fetched from:** https://web.archive.org/web/20261111075311/https://medium.com/@vulnix.dev/intigriti-xss-challenge-beyond-the-sanitizer-46c9ac229119
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14968 (id 14968)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Intigriti XSS Challenge: Beyond the Sanitizer

*How a DOM injection and a same-origin script gadget led to JavaScript execution despite HTML sanitization and CSP.*

## Introduction

I recently solved Intigriti’s BRP XSS challenge, which involved exploiting a missing-person registry called *Pray For Nepal*.

The interesting part was that traditional XSS payloads weren’t enough. The application sanitized HTML input and implemented a Content Security Policy (CSP) that restricted script execution.

However, by combining an HTML injection with an existing JavaScript gadget, I was able to execute `alert(document.domain)` and retrieve the challenge flag.

Here’s how the vulnerability worked.

## 1. Finding the Injection Point

The vulnerable endpoint was:

`https://challenge-brp.challenges.intigriti.io/challenge.php`
The application accepted a `person` parameter, which was processed client-side:

`new URLSearchParams(location.search).get('person')`
When the provided name didn’t match an existing registry entry, the application parsed the input through a `<template>` element and inserted the resulting HTML into the page using `profile.innerHTML`.

This allowed attacker-controlled HTML to enter the DOM.

The application did have a sanitizer. It removed dangerous elements such as `<script>`, `<iframe>`, `<object>`, and `<embed>`, along with attributes beginning with `on`.

However, it preserved attributes such as `id` and `data-*`.

These seemingly harmless attributes turned out to be the key to exploitation.

## 2. Discovering the JavaScript Gadget

While examining the application’s JavaScript, I identified logic that searched for two specific DOM elements:

```
document.getElementById('archive-latch')
document.getElementById('record-anchor')
```
The first element needed `data-key="river-lantern"`, while the second needed a `data-index` attribute containing a specific path.

When these conditions were satisfied, the application dynamically created a `<script>` element and appended it to the document.

The expected script URL was:

`/echo.php?channel=echo&listener=alert(document.domain)//`
This was the crucial discovery.

Rather than injecting executable JavaScript directly, I could inject HTML elements that activated the application’s own script-loading functionality.

## 3. Building the Payload

The final payload was:

```
<div id="archive-latch" data-key="river-lantern">
  <a id="record-anchor"
     data-index="/echo.php?channel=echo&listener=alert(document.domain)//">
    signal
  </a>
</div>
```
The sanitizer allowed this payload because it contained neither prohibited HTML elements nor event-handler attributes.

Once inserted into the live DOM, the elements satisfied the JavaScript gadget’s conditions, causing the application to load `/echo.php` as an external script.

## 4. Why CSP Didn’t Stop the Attack

The application enforced a Content Security Policy with a nonce and a same-origin script allowance. The relevant directive was structured as follows (nonce value abbreviated):

`Content-Security-Policy: script-src 'nonce-xxx' 'self'`
The nonce restricted unauthorized inline scripts, but `'self'` permitted scripts loaded from the application's own origin.

## Get Vulnix Dev’s stories in your inbox

Join Medium for free to get updates from this writer.

Since `/echo.php` was a same-origin endpoint, the dynamically created script was allowed to execute without a nonce.

The endpoint reflected the `listener` parameter into a JavaScript response:

`alert(document.domain)//({"signal":"received"});`
The `//` commented out the remaining expression, leaving an executable `alert(document.domain)` call.

In other words, the CSP wasn’t technically violated. The exploit used a resource that the policy already trusted.

This demonstrates why allowing same-origin scripts can still be dangerous when an application hosts endpoints that return attacker-influenced JavaScript.

## 5. Getting the Flag

The challenge had another interesting mechanism: its JavaScript overrode the browser’s `alert()` function.

Calling `alert()` triggered an authenticated POST request to `/reveal.php`, and the returned content was displayed in the page's `#vault` element.

Therefore, executing:

`alert(document.domain)`
both demonstrated JavaScript execution and activated the flag-reveal mechanism.

The result was:

`ARCHIVE OPEN: INTIGRITI{f2cb05a5-5cc1-4d1d-b7cd-084306cbd5a0}`
The challenge was successfully solved, and my submission was accepted by Intigriti.

## 6. Root Cause and Impact

The vulnerability resulted from three behaviors working together:

1. **Incomplete sanitization:** The application allowed attacker-controlled HTML attributes into the DOM.
2. **DOM-based script gadget:** Existing JavaScript interpreted those attributes and dynamically loaded a script.
3. **Same-origin JavaScript reflection:** `/echo.php` returned executable JavaScript that the CSP permitted.

In this challenge, exploitation revealed the flag through a purpose-built mechanism.

In a real application, similar XSS behavior could allow an attacker to execute authenticated actions, access JavaScript-readable sensitive data, or manipulate content within the victim’s session.

The key issue wasn’t simply that HTML injection was possible. It was that untrusted HTML could influence an existing script-loading mechanism.

## Conclusion

This challenge was a good reminder that XSS doesn’t always require a `<script>` tag or an event handler.

Sometimes, seemingly harmless HTML attributes are enough when the application’s own JavaScript gives them special meaning.

The sanitizer blocked conventional XSS techniques, and CSP restricted inline JavaScript, but neither prevented the combination of a DOM gadget and a same-origin JavaScript endpoint.

**The takeaway: Sanitizing HTML isn’t enough if application logic can turn that HTML into executable behavior.**

Thanks to the Intigriti team for the challenge!

*Security research conducted within Intigriti’s authorized challenge environment.*
