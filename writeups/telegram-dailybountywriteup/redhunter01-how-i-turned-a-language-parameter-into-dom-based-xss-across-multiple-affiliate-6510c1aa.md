# How I Turned a Language Parameter Into DOM-Based XSS Across Multiple Affiliate Portals

- **Source URL:** https://medium.com/@redhunter01/how-i-turned-a-language-parameter-into-dom-based-xss-across-multiple-affiliate-portals-9111364b7678
- **Fetched from:** https://web.archive.org/web/20261111075314/https://medium.com/@redhunter01/how-i-turned-a-language-parameter-into-dom-based-xss-across-multiple-affiliate-portals-9111364b7678
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14951 (id 14951)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Turned a Language Parameter Into DOM-Based XSS Across Multiple Affiliate Portals

*From a harmless-looking URL parameter to browser-confirmed JavaScript execution: a deep dive into unsafe jQuery HTML construction and client-side trust boundaries.*

## Introduction

During a bug bounty investigation of a production affiliate platform, I discovered a reflected DOM-based cross-site scripting (XSS) vulnerability affecting multiple regional affiliate portals.

The entry point was surprisingly simple: a `lang` parameter used to control the language displayed by the application.

Normally, this parameter should contain a supported language identifier, such as `en`, `pt`, or `el`.

However, the application read the value directly from the URL and inserted it into an HTML string without proper validation or encoding.

The dangerous part was what happened next.

The application passed the constructed string into an outdated version of jQuery, which interpreted the string as HTML rather than harmless text.

By breaking out of the intended HTML attribute, I was able to inject a new element containing an event handler.

When the victim opened the crafted URL, the browser executed the injected JavaScript in the legitimate affiliate portal’s origin.

I confirmed the behavior end-to-end in a real Chromium browser.

The same vulnerable code pattern was also present across multiple regional portals.

This case study explains the methodology behind the discovery, the root cause, the proof of concept, and the security implications.

## 1. Vulnerability Overview

PropertyDetailsVulnerabilityReflected DOM-Based Cross-Site ScriptingClassificationCWE-79Entry point`lang` query parameterVulnerable componentClient-side language selectorJavaScript libraryjQuery 1.11.1Authentication requiredNoUser interactionOpening a crafted URLRoot causeUnsafe HTML-string constructionExecution contextVulnerable page's originConfirmed resultJavaScript execution in Chromium

The vulnerability affected language-selection functionality on several affiliate portal pages, including login, password-recovery, and landing-page interfaces.

The vulnerable request followed this general structure:

`GET /login.asp?lang=<USER_INPUT>`
The language parameter was supposed to select one of the application’s supported languages.

Instead, it became an attacker-controlled HTML injection source.

## 2. Finding the Entry Point

The investigation began by examining how the affiliate portal handled language selection.

The application supported multiple languages and used a query parameter to determine which language should be active.

For example:

`/login.asp?lang=en`
or:

`/login.asp?lang=pt`
These requests were legitimate.

But the interesting question was:

**What happens if the lang parameter contains something other than a valid language code?**

A secure implementation would restrict the value to the languages supported by the application.

Instead, the JavaScript accepted the raw parameter value and reused it while constructing the language selector.

This created a potentially dangerous data flow:

```
URL query parameter
        |
        v
JavaScript reads lang
        |
        v
Value stored without validation
        |
        v
HTML string construction
        |
        v
jQuery parses string as HTML
```
The next step was identifying exactly how the value reached the HTML parser.

## 3. Tracing the Vulnerable JavaScript

The vulnerable functionality was implemented in a client-side internationalization script.

The application read the language parameter using the browser’s URL parsing APIs.

Conceptually, the code performed the following operation:

`const currentUrl = new URL(window.location.href);````
const langidactive =
    currentUrl.searchParams.get("lang");
```
At this point, `langidactive` contained whatever the user supplied.

There was no effective allowlist limiting the value to known language identifiers.

The application then loaded its language configuration and constructed a language-picker element.

The dangerous code followed this pattern:

```
jQuery(
    '<a langid="' + langidactive + '">Language</a>'
).appendTo("#langpicker");
```
This is the critical sink.

The application was not inserting the language value as text.

It was building an HTML string and passing the entire string to jQuery.

In jQuery 1.11.1, that string is parsed as HTML.

Therefore, special HTML characters inside `langidactive` can change the structure of the generated DOM.

This turns the language parameter into an HTML injection primitive.

## 4. Understanding the Root Cause

The intended output was something like:

`<a langid="en">English</a>`
The application expected the `langid` attribute to contain a short language identifier.

However, the value was concatenated directly into the attribute.

The vulnerable construction was:

`'<a langid="' + langidactive + '">Language</a>'`
An attacker could supply characters that terminate the attribute and introduce additional HTML markup.

For example, a controlled test value could follow this structure:

`1"><img src=x onerror=alert(document.domain)>`
When inserted into the HTML string, the resulting markup becomes:

```
<a langid="1">
  <img src=x onerror=alert(document.domain)>
  ">Language
</a>
```
The browser no longer interprets the entire attacker-controlled value as an attribute.

Instead, it creates an additional HTML element.

Because the image source is invalid, the browser triggers the image’s error event.

The event handler then executes JavaScript.

The underlying vulnerability is not the language parameter itself.

It is the decision to interpret untrusted input as HTML markup.

## 5. Building the Proof of Concept

After identifying the source and sink, I created a harmless proof-of-concept payload.

The objective was to confirm JavaScript execution without accessing sensitive information or modifying application data.

The decoded payload was:

`1"><img src=x onerror=alert(document.domain)>`
The crafted URL followed this structure:

`https://affiliate.example/login.asp?lang=<URL_ENCODED_PAYLOAD>`
The payload was URL-encoded so that it could be transported safely inside the query string.

When the page loaded, the application extracted the parameter, constructed the language-picker HTML, and passed it to jQuery.

The browser then parsed the injected element.

The proof of concept caused a JavaScript alert displaying the page’s origin.

This demonstrated that the injected code executed within the security context of the affected affiliate portal.

## 6. Confirming Execution in a Real Browser

Source-code analysis showed that the vulnerable pattern existed.

But a potentially vulnerable code path is not the same as confirmed XSS.

To establish exploitability, I validated the behavior using a real Chromium browser through Playwright.

The test followed this sequence:

1. Open the crafted URL.
2. Allow the application to load its language configuration.
3. Wait for the language picker to be constructed.
4. Observe whether the injected event handler executes.
5. Confirm the browser’s execution origin.

The browser displayed the expected JavaScript alert.

The alert contained the affected portal’s domain, confirming that the payload executed within that origin.

The execution chain was:

```
Attacker-controlled lang parameter
               |
               v
URLSearchParams reads input
               |
               v
Unvalidated value stored
               |
               v
HTML string concatenation
               |
               v
jQuery 1.11.1 parses HTML
               |
               v
Injected image element created
               |
               v
Image error event fires
               |
               v
Attacker-controlled JavaScript executes
```
This established actual browser-side script execution rather than simple parameter reflection.

## 7. The Hidden Condition: Multiple Languages

An interesting aspect of this vulnerability was that the dangerous code did not execute unconditionally.

The application first loaded a language configuration file.

The language-picker construction was gated by a condition equivalent to:

```
if (langcount > 1) {
    // Build language picker
}
```
This means the vulnerable sink was reachable only when the active template supported more than one language.

That detail mattered during validation.

A single-language template might never enter the vulnerable branch.

But the affected regional portals used multilingual configurations.

One template supported two languages.

Another supported four.

Both satisfied:

`langcount > 1`
Therefore, the vulnerable language-picker construction executed on both portals.

This demonstrates why identifying the sink alone is not always enough.

A complete investigation must also establish whether the conditions required to reach that sink are satisfied.

## 8. The Same Vulnerability Across Multiple Portals

The investigation identified the same vulnerable JavaScript logic across two regional affiliate portals.

Both applications used the same language-selection implementation.

Both read the attacker-controlled `lang` parameter.

Both loaded multilingual templates.

Both reached the unsafe jQuery HTML constructor.

The relevant pages included:

```
/login.asp
/password_reminder.asp
/default.asp
```
This suggested that the vulnerability was not an isolated issue in a single page.

Instead, it originated from a shared client-side component.

The first portal was confirmed with a real-browser JavaScript execution test.

The second portal contained the same source-to-sink pattern and satisfied the same multilingual condition. The supplied evidence did not include a separately documented alert trace for that second host.

The broader lesson is important:

**When a vulnerability exists in a shared JavaScript component, its impact may extend across every application that imports that component and reaches the vulnerable code path.**

## 9. Why the Outdated jQuery Version Mattered

The application used jQuery 1.11.1.

The vulnerable code relied on jQuery’s ability to create DOM elements from HTML strings.

For example:

`jQuery('<a langid="en">English</a>');`
This is legitimate functionality when the HTML string is trusted.

The problem appears when untrusted data is concatenated into that string.

For example:

```
jQuery(
    '<a langid="' + userInput + '">English</a>'
);
```
Now the browser’s HTML parser can interpret attacker-controlled markup.

It is important to distinguish two things.

The old jQuery version increased maintenance and security concerns.

However, the fundamental vulnerability was unsafe HTML construction using untrusted input.

Simply upgrading jQuery would not automatically make this coding pattern safe.

The application must also stop treating untrusted values as HTML.

## 10. Investigating Content Security Policy

After confirming the injection, I examined whether the application used a Content Security Policy to restrict script execution.

The response contained a policy equivalent to:

`Content-Security-Policy: frame-ancestors 'self'`
This directive controls which origins are permitted to embed the page in a frame.

It does not restrict inline JavaScript execution.

There was no effective `script-src` directive blocking the injected event handler.

Therefore, the browser was permitted to execute the inline JavaScript introduced through the HTML injection.

A restrictive CSP could have provided an additional layer of protection.

For example, a properly deployed policy that disallows inline event handlers could prevent this particular execution technique.

However, CSP should be treated as defense-in-depth.

The primary fix remains removing the unsafe HTML injection sink.

## 11. Understanding the Security Impact

The confirmed vulnerability allowed an unauthenticated attacker to execute JavaScript in the affected affiliate portal’s origin when a victim opened a crafted link.

This is significantly different from CSS injection or harmless HTML reflection.

JavaScript running in a page’s origin can interact with the DOM and make requests subject to the browser’s same-origin and cookie rules.

## Credential phishing

The vulnerable functionality was present on login-related pages.

## Get redhunter01’s stories in your inbox

Join Medium for free to get updates from this writer.

An attacker-controlled script could potentially modify the visible login interface or insert deceptive elements.

Because the victim is viewing a legitimate application origin, malicious UI changes could be more convincing than those on an unrelated phishing website.

The investigation demonstrated JavaScript execution, not an actual credential-harvesting attack.

## Reading accessible page content

JavaScript executing within the origin can read DOM content accessible to the page.

This could include information rendered into the page during the victim’s session.

However, access to specific sensitive records was not demonstrated.

## Session-riding opportunities

The injected JavaScript could potentially issue same-origin requests while the victim is authenticated.

Browsers automatically attach eligible cookies to requests according to their normal cookie rules.

This means that an XSS payload does not necessarily need to read the session cookie directly to interact with authenticated functionality.

Whether meaningful authenticated actions can be performed depends on the application’s endpoints, authorization controls, and session behavior.

No specific authenticated state-changing action was demonstrated in the supplied proof of concept.

## 12. HttpOnly Cookies Do Not Eliminate XSS

An important observation during testing was that the session cookie used the `HttpOnly` attribute.

That is a useful security control.

It prevents JavaScript from reading the cookie through:

`document.cookie`
However, `HttpOnly` does not stop JavaScript from running in the page.

It also does not prevent the browser from attaching an eligible session cookie to requests made by the page.

This distinction is critical.

Consider the difference:

```
Reading a session cookie
         |
         v
Blocked by HttpOnly
```
versus:

```
JavaScript executes in the origin
         |
         v
Browser sends eligible authenticated requests
         |
         v
Server processes requests according to permissions
```
The second behavior can still occur even when the cookie is protected by `HttpOnly`.

Therefore, the absence of readable session cookies does not make an XSS vulnerability harmless.

It changes the possible exploitation paths.

## 13. Avoiding Unsupported Escalation Claims

During the investigation, a possible cross-origin data-access scenario was also considered.

However, that larger chain was not proven end-to-end.

I therefore kept it separate from the confirmed XSS finding.

The proven facts were:

- The attacker controlled the `lang` parameter.
- The parameter reached an unsafe HTML constructor.
- The vulnerable code path executed in a multilingual template.
- The browser parsed attacker-controlled markup.
- An injected event handler executed JavaScript.
- The execution occurred in the vulnerable application’s origin.
- No authentication was required to deliver the crafted link.

The investigation did not establish:

- Theft of an `HttpOnly` session cookie
- Successful account takeover
- Cross-origin extraction of sensitive customer information
- Successful execution of a privileged authenticated action
- Persistent or stored XSS

This separation between proven behavior and potential consequences makes the finding more technically defensible.

## 14. Root Cause Analysis

The vulnerability resulted from three interacting design decisions.

## First: Untrusted input was accepted without validation

The application read the language identifier directly from the query string.

```
const langidactive =
    new URLSearchParams(window.location.search)
        .get("lang");
```
The input was not restricted to the application’s supported language codes.

## Second: The value was concatenated into HTML

The application constructed markup using string concatenation.

`'<a langid="' + langidactive + '">Language</a>'`
This allowed special characters to change the resulting HTML structure.

## Third: The HTML string was parsed by jQuery

The application passed the constructed string to jQuery.

`jQuery(htmlString);`
The result was interpreted as HTML markup.

That completed the source-to-sink chain.

The underlying trust-boundary failure was:

```
Untrusted URL parameter
          |
          v
Application assumes language code
          |
          v
Raw value inserted into HTML
          |
          v
HTML parser interprets attacker input
          |
          v
JavaScript event handler executes
```
## 15. Recommended Remediation

The most effective remediation is to eliminate the unsafe HTML construction pattern.

## 1. Strictly allowlist language identifiers

If the application supports only known languages, it should reject every other value.

For example:

```
const allowedLanguages = new Set([
    "en",
    "pt",
    "fr",
    "es",
    "el"
]);
```
const requestedLanguage =

new URLSearchParams(window.location.search)

.get("lang");const activeLanguage =

allowedLanguages.has(requestedLanguage)

? requestedLanguage

: "en";

Ideally, the allowed values should come from the active template’s language configuration rather than a global list.

This ensures the parameter cannot contain arbitrary HTML markup.

## 2. Use safe DOM construction

Instead of building HTML strings, construct elements through DOM APIs.

For example:

`const link = document.createElement("a");`
link.setAttribute("langid", activeLanguage);

link.textContent = "Language";document.querySelector("#langpicker")

.appendChild(link);

This approach treats the language identifier as an attribute value rather than executable HTML.

## 3. Upgrade outdated dependencies

The application should upgrade from the obsolete jQuery version to a maintained release.

However, the unsafe HTML-construction pattern must still be corrected.

A dependency upgrade alone is not a reliable remediation.

## 4. Deploy a restrictive CSP

A restrictive `script-src` policy can help prevent injected inline event handlers from executing.

The application should avoid unsafe inline execution patterns and adopt a policy compatible with its legitimate scripts.

## 5. Review shared components

Because the vulnerability originated from shared language-selection functionality, every page and regional deployment using that component should be reviewed.

Fixing only one affected URL may leave the same vulnerable code active elsewhere.

## 16. My Bug Bounty Methodology

This case illustrates a practical workflow for investigating DOM-based XSS.

## Step 1 — Identify user-controlled inputs

Start with URL parameters and other browser-controlled sources.

Examples include:

```
?lang=
?locale=
?language=
?redirect=
?returnUrl=
```
These parameters often influence client-side behavior.

## Step 2 — Trace input into JavaScript

Search for operations such as:

```
URLSearchParams
location.search
location.hash
```
Determine where the resulting values are stored and reused.

## Step 3 — Identify dangerous DOM sinks

Pay particular attention to operations that parse strings as HTML.

For example:

```
jQuery(htmlString)
.innerHTML
insertAdjacentHTML()
```
These operations can become dangerous when their inputs contain untrusted data.

## Step 4 — Identify execution conditions

Determine whether the vulnerable code is reachable.

In this case, the language-picker code executed only when:

`langcount > 1`
The multilingual template configuration was therefore an important part of the proof.

## Step 5 — Test attribute-context escaping

When untrusted input appears inside an HTML attribute, determine whether it can terminate the attribute and introduce new markup.

Start with harmless markers and controlled test cases.

## Step 6 — Confirm in a real browser

Use a harmless execution marker or alert to demonstrate that JavaScript actually runs.

Static reflection alone is insufficient to establish executable XSS.

## Step 7 — Check browser defenses

Review:

- Content Security Policy
- Cookie attributes
- Same-origin restrictions
- Session behavior
- Accessible DOM content

## Step 8 — Investigate shared components

If the vulnerability exists in a common JavaScript file, identify other pages and applications that use it.

Confirm which deployments actually reach the vulnerable branch.

## Step 9 — Establish realistic impact

Separate demonstrated JavaScript execution from hypothetical account takeover or data theft.

A precise report is more valuable than an exaggerated one.

## 17. Lessons Learned

This investigation reinforced several important lessons.

**1. Small parameters can create serious vulnerabilities.**

A language selector may appear low-risk, but its security depends on how the value is handled.

**2. DOM-based XSS is about data flow.**

The vulnerability becomes clear when tracing attacker-controlled input from the URL to an HTML-parsing sink.

**3. HTML-string construction is dangerous with untrusted data.**

Building markup through string concatenation can transform ordinary text into executable HTML.

**4. Conditional code paths matter.**

A vulnerable sink may only be reachable when particular configuration conditions are satisfied.

**5. Shared JavaScript can create shared vulnerabilities.**

One insecure component can affect multiple pages and regional deployments.

**6. HttpOnly is not an XSS fix.**

It protects cookie confidentiality but does not prevent JavaScript execution or all forms of session-riding.

**7. CSP must restrict scripts to mitigate XSS.**

A policy containing only `frame-ancestors` does not block injected event handlers.

**8. Browser validation is essential.**

The decisive evidence was JavaScript execution in a real browser, not merely suspicious source code.

## 18. Final Takeaway

This vulnerability began with a simple language parameter.

The application expected a harmless value such as:

`en`
But instead of validating the input and treating it as data, the application concatenated it into an HTML string.

The resulting markup was passed to jQuery 1.11.1, which parsed the attacker-controlled content as HTML.

The complete vulnerability chain was:

```
Attacker-controlled lang parameter
                |
                v
URLSearchParams extracts input
                |
                v
No effective language allowlist
                |
                v
Raw value inserted into HTML string
                |
                v
jQuery parses the constructed markup
                |
                v
Injected HTML element created
                |
                v
JavaScript event handler executes
                |
                v
Arbitrary JavaScript runs in the page's origin
```
The investigation also demonstrated how shared frontend components and multilingual configuration can expand the affected surface across multiple pages and regional portals.

The most important lesson is straightforward:

**Never assume a parameter is safe because its intended purpose is harmless. Security depends on where the value flows, how it is interpreted, and whether untrusted data can cross into an executable context.**

For bug bounty hunters, the methodology is equally valuable:

**Trace the source, identify the sink, understand the parser, verify the execution conditions, confirm the result in a real browser, and report only the impact supported by evidence.**

Sometimes, all it takes to turn an ordinary language selector into a serious client-side vulnerability is one unsafe HTML constructor.
