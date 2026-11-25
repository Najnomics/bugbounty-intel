# Reflected XSS in a Public Event Waitlist Application

- **Source URL:** https://medium.com/@redhunter01/reflected-xss-in-a-public-event-waitlist-application-d1ef92f10e21
- **Fetched from:** https://medium.com/@redhunter01/reflected-xss-in-a-public-event-waitlist-application-d1ef92f10e21?source=rss-1a8706ec0593------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14928)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** redhunter01 / Wed, 30 Sep 2026 05:48:19 GMT

**Severity:** Medium

**CVSS 3.1:** 6.1

**CWE:** CWE-79 — Cross-Site Scripting

**Vulnerability Type:** Reflected XSS

During a security assessment of a public-facing event waitlist application, I discovered a reflected Cross-Site Scripting vulnerability in a language-selection parameter.

The vulnerability allowed an attacker to construct a malicious link that caused attacker-controlled JavaScript to execute in a victim’s browser under the application’s origin.

The interesting part of this finding was not simply discovering that a parameter was reflected. The key was identifying that the parameter was reflected **inside an HTML attribute without proper contextual encoding**, allowing the attribute to be terminated and arbitrary HTML to be injected.

To keep the affected organization and application undisclosed, identifying information has been intentionally omitted from this writeup.

The application exposed a public waitlist endpoint with parameters conceptually similar to:

/event-waitlist?event=\<EVENT>&lang=\<LANGUAGE>

The language parameter normally accepted short language identifiers.

I started by replacing the expected value with a unique marker:

TEST123

The marker appeared in the server response.

At this point, reflection alone was not enough to establish XSS.

The next question was:

*Where exactly is the attacker-controlled value being reflected?*

Inspecting the response showed that the value was inserted into an HTML attribute.

Conceptually, the application generated markup similar to:

\<input type="hidden" name="lang" value="USER\_INPUT">

This was the critical discovery.

The application was placing attacker-controlled input inside a quoted HTML attribute without appropriate output encoding.

Therefore, an attacker could attempt to terminate the attribute using:

">

For example:

lang=test">

could result in markup conceptually equivalent to:

\<input type="hidden" name="lang" value="test">

Once the existing attribute was terminated, additional attacker-controlled HTML could be introduced.

I used a minimal HTML injection primitive:

">\<img src=x onerror="window.\_\_xss\_fired='XSS\_CONFIRMED\_'+document.domain">

The payload performs three important actions:

The payload was URL-encoded before being supplied to the vulnerable parameter.

The resulting request therefore followed this general structure:

/event-waitlist?event=\<EVENT>&lang=\<URL\_ENCODED\_PAYLOAD>

No target-specific URL is included here intentionally.

The vulnerable application effectively transformed the input into something similar to:

\<input type="hidden"

name="lang"

value="test">

\<img src=x

onerror="window.\_\_xss\_fired='XSS\_CONFIRMED\_'+document.domain">

">

The browser no longer interpreted the injected content as part of the original attribute.

Instead, it parsed the injected \<img> as a new HTML element.

Because the image source was intentionally invalid:

src=x

the browser triggered:

onerror

which executed the attacker-controlled JavaScript.

The important transition was:

Untrusted parameter

↓

HTML attribute

↓

Attribute breakout

↓

Injected HTML element

↓

JavaScript execution

I validated the issue in a real Chromium browser rather than relying exclusively on HTTP response inspection.

After navigating to the crafted URL, I checked:

window.\_\_xss\_fired

The value contained the application’s origin, confirming that the JavaScript had executed in the browser under the vulnerable origin.

This established actual reflected XSS rather than simple HTML reflection.

The validation also confirmed that the payload survived the application’s request/response processing and was interpreted by the browser as executable markup.

During analysis, the same user-controlled parameter was observed in multiple locations within the generated page.

The value appeared in contexts including:

The hidden input was sufficient to achieve XSS.

The additional reflection points were useful because they demonstrated that the underlying problem was not necessarily isolated to a single HTML element.

I also checked whether a Content Security Policy prevented inline JavaScript execution.

The affected page did not have a restrictive CSP that blocked the inline event handler used for validation.

Therefore, the injected:

onerror="..."

handler was able to execute.

However, the absence of CSP was treated as a **defense-in-depth issue**, not the root cause.

The fundamental vulnerability was unsafe insertion of attacker-controlled data into an HTML context.

After confirming JavaScript execution, I investigated the actual capabilities available to the injected script rather than automatically treating the vulnerability as an account-takeover issue.

The testing did not identify:

This significantly constrained the demonstrated impact.

The vulnerability nevertheless provides meaningful browser-side control over the affected page.

The affected application contains a public waitlist form that collects information from visitors.

Because injected JavaScript executes within the page, an attacker could manipulate the DOM and alter the behavior or presentation of the form.

A potential attack flow is:

Attacker creates malicious URL

↓

Victim opens legitimate waitlist page

↓

XSS executes

↓

Attacker-controlled JavaScript modifies the page

↓

Victim interacts with the modified form

↓

Attacker-controlled functionality processes submitted information

This makes the vulnerability more significant than a simple visual defacement.

The attacker could also modify the legitimate page to display convincing phishing content.

Legitimate application

↓

Injected JavaScript

↓

DOM manipulation

↓

Fake login / payment / verification interface

The victim would still be interacting with the legitimate application’s origin, which can increase the credibility of the social-engineering attack.

The injected JavaScript can also modify page content, links, and form elements.

Potential consequences include:

A major part of the assessment was determining whether the XSS could be escalated.

I checked the vulnerable origin for authentication material such as:

Cookies

JWTs

localStorage

sessionStorage

No sensitive authentication material was identified.

I also investigated whether the vulnerable origin was trusted by related authenticated APIs through permissive CORS configuration.

The tested APIs did not grant the vulnerable origin the required cross-origin read access.

Therefore, I could not demonstrate:

Account takeover

or:

Cross-origin authenticated data theft

and did not rely on those claims when determining severity.

The following is intentionally presented in an anonymized form.

Open the public event waitlist functionality.

Identify the language parameter.

Example:

lang=en

Replace the value with an HTML attribute-breakout payload:

URL-encode the payload and submit it through the vulnerable parameter.

Open the resulting URL in a real browser.

Open DevTools and execute:

A value containing the application’s origin is returned, demonstrating JavaScript execution.

The root cause was improper output handling of attacker-controlled data.

Conceptually, the vulnerable server-side logic behaved like:

echo '\<input type="hidden" name="lang" value="' . $language . '">';

The problem is that $language originates from an HTTP request and is subsequently inserted directly into HTML.

An attacker can therefore provide:

test">\<payload>

and change the structure of the generated document.

Because the language parameter is expected to contain only a small number of predefined values, strict validation is the preferred approach.

$allowedLanguages = \['en', 'dk'\];

$language = $\_GET\['lang'\] ?? 'en';

```
if (!in_array($language, $allowedLanguages, true)) {
    $language = 'en';
}
```
This prevents arbitrary input from reaching the HTML sink.

If arbitrary values are legitimately required, encode the value before inserting it into an HTML attribute:

echo '\<input type="hidden" name="lang" value="' .

htmlspecialchars(

$language,

ENT\_QUOTES | ENT\_HTML5,

'UTF-8'

) .

'">';

The encoding must match the output context.

A restrictive CSP should also be deployed as defense in depth:

Content-Security-Policy:

default-src 'self';

script-src 'self';

object-src 'none';

base-uri 'self';

CSP should not be considered a replacement for correct output encoding.

This finding also demonstrates a repeatable approach for discovering reflected XSS.

Look for parameters such as:

lang

language

search

query

name

redirect

next

return

url

id

Send a unique marker:

XSS\_TEST\_123

Then determine whether it appears in the response.

Identify whether the reflection occurs inside:

HTML

HTML attributes

JavaScript

CSS

URLs

DOM-generated content

For an HTML attribute, investigate characters such as:

"

'

>

">\<img src=x onerror=alert(1)>

A browser-side marker is preferable for automated testing:

window.\_\_xss\_fired = true

Confirm that the browser actually parses and executes the payload.

After confirming XSS, examine:

Authentication

Cookies

Browser storage

Same-origin APIs

Forms

Administrative functionality

CORS

Sensitive data

A strong report should clearly distinguish between:

Confirmed impact

and:

Theoretical impact

This prevents severity inflation and makes the report substantially more defensible.

A public event waitlist application reflected an attacker-controlled language parameter directly into an HTML attribute without proper contextual encoding.

By terminating the existing attribute and injecting an HTML element containing an event handler, it was possible to execute arbitrary JavaScript in a victim’s browser under the application’s origin.

The demonstrated vulnerability provides browser-side control over the affected page and creates realistic opportunities for form manipulation, phishing, and content modification.

The investigation also showed the importance of analyzing the **actual security boundary** after discovering XSS. Authentication state, browser storage, same-origin functionality, and CORS behavior were examined to determine what could and could not be demonstrated.

The core remediation is straightforward:

**Validate expected values where possible, contextually encode all untrusted output, and use CSP as defense in depth.**
