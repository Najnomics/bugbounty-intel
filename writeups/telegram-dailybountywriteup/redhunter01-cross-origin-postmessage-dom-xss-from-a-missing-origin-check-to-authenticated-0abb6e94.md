# Cross-Origin postMessage DOM XSS

- **Source URL:** https://medium.com/@redhunter01/cross-origin-postmessage-dom-xss-from-a-missing-origin-check-to-authenticated-account-compromise-759589196176
- **Fetched from:** https://medium.com/feed/@redhunter01
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14936)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### Introduction

Some of the best bug bounty findings do not begin with a suspicious API endpoint.

They begin with a few lines of client-side JavaScript.

During reconnaissance of a large consumer web application, I found a window.postMessage handler associated with a third-party voting integration.

At first glance, the code appeared simple:

```
window.addEventListener("message", function (event) {
    if (
        event.data &&
        event.data.action === "redirect" &&
        event.data.options &&
        event.data.options.link
    ) {
        window.location.href = sanitize(event.data.options.link);
    }
});
```
The problem was subtle but extremely important:

**the application trusted messages from every origin.**

There was no:

if (event.origin !== TRUSTED\_ORIGIN) return;

That alone does not automatically mean XSS.

But it gives us an attacker-controlled source.

The next question becomes:

*Where does that attacker-controlled value go?*

Following the data flow revealed something far more interesting.

The supplied URL eventually reached:

window.location.href

That transformed an ordinary missing-origin-check bug into a potential DOM XSS.

And after following the application architecture further, the issue escalated from JavaScript execution to authenticated account actions.

This write-up explains the methodology behind finding vulnerabilities like this rather than focusing only on the final payload.

### 1. Start With Message Handlers

A valuable JavaScript reconnaissance pattern is searching bundles for:

`addEventListener("message"`
and:

window.onmessage

Cross-window communication appears everywhere:

- OAuth integrations
- payment widgets
- surveys
- voting systems
- embedded forms
- customer-support widgets
- advertising
- authentication flows
- third-party SDKs

The security boundary is important because postMessage allows documents from different origins to communicate.

A safe handler normally verifies the sender.

For example:

```
window.addEventListener("message", event => {
    if (event.origin !== "https://trusted.example") {
        return;
    }
```
// process message

});

During review, the handler I found performed multiple actions based entirely on event.data.

Conceptually:

event.data.action === "redirect"

caused:

location.href = event.data.options.link

But there was no validation of:

event.origin

That immediately created a useful hypothesis:

*Any website may be able to instruct the victim application to navigate somewhere.*

The next task was understanding whether that navigation could become JavaScript execution.

### 2. Trace Source → Transformation → Sink

When auditing DOM vulnerabilities, thinking in terms of data flow is extremely useful.

For this bug:

### Source

event.data.options.link

An external page could potentially control this through postMessage.

### Transformation

The value passed through a function that appeared to sanitize it.

Conceptually:

sanitizeHtml(value)

### Sink

The output reached:

window.location.href

So the data flow became:

Cross-origin postMessage

↓

event.data.options.link

↓

HTML sanitizer

↓

window.location.href

At this point, one detail mattered enormously:

**What exactly did the sanitizer protect against?**

### 3. Never Trust a Function Because It Is Called “Sanitize”

This was the most important lesson from the finding.

Developers often assume:

sanitize(userInput)

means:

*The value is now safe everywhere.*

That is incorrect.

Sanitization is context-specific.

Different sinks require different validation.

For example:

HTML context        → HTML sanitization

HTML attribute → attribute encoding

JavaScript context → JS escaping

SQL query → parameterization

URL destination → URL scheme validation

The application used an **HTML sanitizer** before assigning the value to a **URL navigation sink**.

Those are different security contexts.

An HTML sanitizer is designed for input resembling:

\<b>Hello\</b>

\<script>alert(1)\</script>

It may remove unsafe HTML elements.

But a plain URL-like string may contain no HTML at all.

Therefore a dangerous URI scheme can survive because there is nothing for the HTML parser to sanitize.

The bug was not:

*The sanitizer was broken.*

The real bug was:

*The wrong type of sanitizer was used for the sink.*

That distinction matters when analyzing applications.

### 4. Classify the Sink Correctly

Consider:

window.location.href = attackerControlledValue;

Possible values include:

https://example.com

/about

/profile

mailto:user@example.com

javascript:...

data:...

The browser interprets the scheme.

Therefore the security question is not:

*Is this valid HTML?*

The security question is:

*Which URL schemes are allowed?*

A safer pattern would be:

const url = new URL(value, window.location.origin);

```
if (url.protocol !== "https:") {
    return;
}
```
window.location.href = url.href;

Potentially with hostname restrictions as well:

const allowedHosts = new Set(\[

"trusted.example.com"

\]);

```
if (!allowedHosts.has(url.hostname)) {
    return;
}
```
This is a recurring bug bounty pattern:

correct-looking sanitizer

+

wrong security context

=

vulnerability

### 5. Verify the Library Instead of Guessing

Another important methodology lesson is verifying dependency behavior.

The bundle contained minified module references, so the next task was identifying which library implemented the sanitizer.

Useful clues included strings relating to:

allowedSchemes

naughtyHref

sanitize-html

This identified the dependency as an HTML sanitization library.

Rather than assuming its behavior, reproduce it locally.

For example:

`const sanitizeHtml = require("sanitize-html");`
console.log(

sanitizeHtml("SOME\_TEST\_VALUE")

);

Testing the exact installed version is even better.

This answers questions such as:

- Does it normalize whitespace?
- Does it lowercase schemes?
- Does it remove URLs?
- Does it behave differently on raw strings?
- Does configuration change the output?

This methodology is reusable across nearly every bug bounty target.

When a bundle uses:

DOMPurify

sanitize-html

validator.js

lodash

marked

axios

React Router

Next.js helpers

do not rely solely on documentation.

Test the exact behavior.

### 6. Understand the Browser Primitive

A missing postMessage origin validation bug usually looks like this:

victimWindow.postMessage(

{

action: "redirect",

options: {

link: attackerControlledValue

}

},

"\*"

);

The browser delivers a MessageEvent.

The receiving application gets information such as:

event.data

event.origin

event.source

If the application only checks:

event.data

and ignores:

event.origin

then it has lost one of the browser’s primary trust boundaries.

Conceptually:

Attacker origin

|

| postMessage()

v

Victim origin

|

| missing origin verification

v

Trusted application logic

This is why message handlers deserve special attention during JavaScript auditing.

### 7. Do Not Stop at “postMessage Bug”

A common bug bounty mistake would be stopping here and reporting:

*Missing origin validation in postMessage handler.*

That might receive a low severity rating.

Instead ask:

*What security-sensitive operation does the message control?*

Possible sinks include:

location.href

location.assign()

location.replace()

innerHTML

outerHTML

insertAdjacentHTML()

eval()

Function()

document.write()

script.src

iframe.src

form.action

Also search for application-specific actions such as:

logout()

redeemReward()

changeEmail()

linkAccount()

purchase()

updateProfile()

The vulnerability’s real severity depends on the sink.

In this case the chain became:

Untrusted cross-origin message

↓

Missing origin validation

↓

Attacker-controlled navigation

↓

Dangerous URL interpretation

↓

JavaScript execution

That is fundamentally different from a harmless cross-origin message bug.

### 8. Check Whether the Vulnerable Route Actually Loads

Finding vulnerable code in a JavaScript bundle does not guarantee that users can reach it.

The next question should always be:

*What conditions cause this component to mount?*

The vulnerable handler belonged to a voting modal.

A route resembling:

/voting/:activityId

rendered the relevant component.

The component then created a third-party iframe.

The message listener was registered when that integration loaded.

This introduced an important condition:

**the vulnerable code existed permanently, but the trigger depended on an active campaign.**

This distinction is important in bug bounty reports.

There are three different states:

Code exists

↓

Feature reachable

↓

Exploit trigger active

Do not treat them as identical.

### 9. Test Deep-Link Routing

Modern SPAs frequently return the application shell for arbitrary routes.

For example:

/voting/123

/voting/456

/voting/test

may all return:

\<div id="root">\</div>

\<script src="/static/main.js">\</script>

and React Router decides what component to render.

This matters because attackers may be able to directly open the vulnerable application state.

During testing, verify:

GET /interesting/route

and inspect whether the response includes the main SPA bundle.

Also inspect router definitions.

Useful searches include:

path:

createBrowserRouter

\<Route

useParams

/voting/

Understanding routes often turns theoretically vulnerable code into a reproducible attack surface.

### 10. Analyze Authentication Context

JavaScript execution becomes significantly more serious when it occurs inside an authenticated origin.

The next question was:

*What authenticated APIs become accessible once script executes in this origin?*

The application exposed same-origin APIs for things such as:

profile validation

wallet / point balances

rewards

challenges

polls

surveys

Because injected JavaScript executes as the application origin, browser requests inherit the victim’s authenticated session.

Conceptually:

```
fetch("/api/profile", {
    credentials: "include"
});
```
The browser automatically supplies eligible session cookies.

This is an important XSS concept:

**HttpOnly cookies do not prevent XSS from using the victim’s session.**

HttpOnly protects against:

document.cookie

But an attacker-controlled script can still do:

```
fetch("/api/account")
fetch("/api/rewards")
fetch("/api/profile")
```
because the browser sends cookies automatically.

Therefore the real impact may be:

XSS

↓

authenticated API access

↓

PII exposure

↓

account actions

↓

account compromise

rather than simply:

alert(1)

### 11. Map the Application’s Authenticated API Surface

Once XSS is confirmed, do not immediately jump to destructive testing.

Instead create an impact map.

Look through:

- network requests
- JavaScript bundles
- API clients
- route definitions
- GraphQL operations
- Redux actions
- service modules

Classify endpoints.

For example:

CategoryExampleIdentityprofile / account detailsFinancial-like valuepoints / credits / rewardsState changeschallenge participationUser contentvotes / surveysAccount securityemail / password / MFAPrivileged actionsadministration

This gives you a structured picture of what XSS means inside that origin.

For this case, the interesting classes were:

profile information

loyalty identifiers

points balance

reward redemption

challenge actions

voting actions

That changed the report from:

*DOM XSS exists.*

into:

*Attacker-controlled JavaScript executes inside an authenticated loyalty application and can interact with privileged same-origin APIs.*

Much stronger.

### 12. Check Browser Differences

Browser behavior matters.

An exploit primitive that works in Chromium may behave differently in Firefox or Safari.

Therefore cross-browser validation should be part of serious client-side testing.

Useful environments:

Chrome

Chromium

Edge

Firefox

Safari / WebKit

With Playwright:

chromium.launch()

firefox.launch()

webkit.launch()

For this particular class of navigation behavior, Chromium-family browsers allowed the relevant programmatic navigation behavior while Firefox imposed stricter user-activation requirements.

That means the correct report should not say:

*All users are vulnerable.*

It should say something closer to:

*The demonstrated exploit chain affects Chromium-family browsers under the tested conditions.*

Honest limitations improve a report.

They do not weaken it.

They make the report more credible.

### 13. Check Security Headers

Whenever you find a client-side injection issue, inspect the response headers.

Important headers include:

Content-Security-Policy

X-Frame-Options

Cross-Origin-Opener-Policy

Cross-Origin-Resource-Policy

Referrer-Policy

For XSS specifically, CSP can provide additional defense.

A strong policy might contain:

script-src 'self' 'nonce-...'

object-src 'none'

base-uri 'none'

frame-ancestors 'none'

But remember:

CSP is **defense in depth**.

The primary bug still needs to be fixed.

For postMessage, that means validating the sender.

For URL navigation, that means validating the destination.

### 14. Understand Popup vs. Iframe Authentication

Another useful lesson came from authentication behavior.

Modern cookies may use:

SameSite=Lax

SameSite=Strict

SameSite=None

Whether cookies are sent can depend on browsing context.

An embedded third-party iframe may not receive the same cookies that a top-level browser navigation receives.

So when assessing a cross-origin attack, consider:

iframe

popup

top-level navigation

same-site navigation

cross-site subresource request

The relevant question is:

*Under what browser context does the authenticated session actually accompany the request?*

Do not simply assume:

cookie exists → every context gets it

Modern browser cookie rules make that incorrect.

### 15. Build a Local Replica When Production Testing Is Limited

One of the most useful bug bounty techniques is building a minimal replica of the vulnerable behavior.

This becomes particularly valuable when:

- bot protection blocks automation,
- login requires unavailable credentials,
- destructive actions must be avoided,
- the feature is temporarily inactive,
- reproducing against production would affect users.

A good replica can contain:

attacker origin

victim origin

message listener

same sanitizer version

same sink

mock authenticated endpoint

browser automation

The goal is not to invent behavior.

It is to reproduce the verified production data flow.

Conceptually:

attacker.test

|

| cross-origin postMessage

v

victim.test

|

| vulnerable listener

v

navigation sink

|

v

script execution

|

v

mock authenticated API

This allows the researcher to mechanically prove:

input → sink → execution → authenticated request

without abusing a production account.

That is significantly more convincing than a theoretical explanation.

### 16. Keep Production Evidence and Replica Evidence Separate

This is critical.

A strong report should clearly distinguish:

### Verified directly in production

For example:

message handler exists

origin validation missing

specific sanitizer library present

dangerous sink present

SPA route reachable

security headers absent

authenticated API endpoints present

### Verified in a controlled replica

For example:

browser executes the navigation

script executes in victim origin

authenticated API response can be accessed

data can leave the origin

Never write:

*Full account takeover reproduced in production.*

if you only reproduced the complete chain locally.

Instead explain exactly which links in the chain were verified where.

Triagers appreciate this.

### 17. Think in Exploit Chains

The best vulnerability research often comes from chaining individually modest observations.

This case can be represented as:

\[1\] Cross-origin communication

↓

\[2\] Missing event.origin validation

↓

\[3\] Attacker controls redirect destination

↓

\[4\] HTML sanitizer used instead of URL validator

↓

\[5\] Dangerous navigation scheme survives

↓

\[6\] JavaScript executes in trusted origin

↓

\[7\] Victim session is available

↓

\[8\] Same-origin authenticated APIs become accessible

↓

\[9\] PII and loyalty actions exposed

If you stop at step two, you have a low-level bug.

If you follow the chain to step nine, you understand the security impact.

That mindset is one of the biggest differences between ordinary scanning and high-quality bug bounty research.

### 18. A Reusable postMessage Hunting Methodology

When auditing JavaScript bundles, use the following workflow.

### Step 1 — Find message handlers

Search:

```
addEventListener("message"
onmessage
postMessage(
```
### Step 2 — Look for origin validation

Search nearby code for:

event.origin

e.origin

allowedOrigins

trustedOrigins

If none exists, investigate further.

### Step 3 — Identify controllable fields

Examples:

event.data.url

event.data.redirect

event.data.link

event.data.html

event.data.command

event.data.action

Ask:

*Which part of the message controls application behavior?*

### Step 4 — Trace those fields to sinks

High-value sinks include:

location.href

location.assign

location.replace

innerHTML

outerHTML

insertAdjacentHTML

document.write

eval

Function

script.src

iframe.src

form.action

### Step 5 — Understand every transformation

If data goes through:

sanitize()

escape()

encode()

validate()

normalize()

identify the actual library and behavior.

Never assume safety from the function name.

### Step 6 — Reproduce library behavior locally

Use the exact package version where possible.

Test:

normal input

mixed case

whitespace

encoded characters

scheme variations

relative URLs

absolute URLs

The goal is understanding the parser.

### Step 7 — Determine reachability

Find:

route

feature flag

campaign ID

iframe condition

component lifecycle

authentication requirement

A vulnerable function that never executes has different risk from one reachable by every visitor.

### Step 8 — Determine execution context

Ask:

Does it execute in an iframe?

A popup?

The top-level page?

A sandboxed frame?

Security behavior changes significantly depending on context.

### Step 9 — Map authenticated capabilities

Once execution is established, inspect same-origin APIs.

Prioritize:

profile

account

billing

wallet

rewards

email

security settings

administrative functions

Do not perform destructive actions unless explicitly permitted.

### Step 10 — Validate multiple browsers

Do not assume browser behavior is universal.

Test Chromium, Firefox, and WebKit where relevant.

### Step 11 — Document conditions

Examples:

requires login

requires one click

Chromium only

feature only active during campaigns

specific account state required

Good researchers communicate constraints instead of hiding them.

### 19. Interesting Search Patterns

During JavaScript bundle auditing, searches like these can uncover similar issues:

```
addEventListener("message"
event.origin
postMessage(
location.href
location.assign
location.replace
sanitize
redirect
options.link
event.data
```
Using ripgrep:

rg 'addEventListener\(\["'\''\]message' .

`rg 'postMessage\(' .`
rg 'location\.(href|assign|replace)' .

rg 'event\.origin|e\.origin' .

The interesting pattern is often:

message handler found

+

no origin validation nearby

+

security-sensitive sink

That combination deserves manual review.

### 20. Common False Positives

Not every missing origin check is exploitable.

For example:

```
window.addEventListener("message", e => {
    console.log(e.data);
});
```
is generally not a security vulnerability.

Likewise:

```
window.addEventListener("message", e => {
    if (e.data === "resize") resizeWidget();
});
```
may have little security impact.

Severity increases when attacker-controlled messages influence:

navigation

HTML

authentication

account state

sensitive APIs

payments

tokens

privileged actions

Always follow the data.

### 21. Reporting Strategy

A strong title should describe the full chain.

For example:

**Cross-Origin postMessage DOM XSS via Missing Origin Validation Leading to Authenticated Account Actions**

The summary should answer four things immediately:

What can the attacker control?

Where does it go?

Why does the existing protection fail?

What can the attacker accomplish?

For example:

*A cross-origin postMessage listener accepts redirect messages without validating the sender. The attacker-controlled destination is passed through an HTML sanitizer and assigned to a browser navigation sink. Because HTML sanitization does not enforce safe URL schemes, an unsafe navigation value can survive and execute within the trusted application origin. In authenticated sessions, this gives attacker-controlled JavaScript access to same-origin profile and loyalty functionality.*

That communicates the entire vulnerability without requiring a triager to reverse-engineer the report.

### 22. Remediation

There are multiple layers to fix.

### Validate the message origin

const TRUSTED\_ORIGINS = new Set(\[

"https://trusted-widget.example"

\]);

`window.addEventListener("message", event => {````
    if (!TRUSTED_ORIGINS.has(event.origin)) {
        return;
    }
```
// handle message

});

For stronger validation, also verify:

event.source

when the expected window reference is known.

### Validate URLs as URLs

Do not use an HTML sanitizer for navigation security.

Instead:

```
function safeRedirect(value) {
    const url = new URL(value, window.location.origin);
```
```
    if (url.protocol !== "https:") {
        throw new Error("Unsupported protocol");
    }
```
return url.href;

}

Restrict hostnames if external navigation is unnecessary.

### Prefer semantic actions over arbitrary URLs

Even better than accepting:

```
{
    action: "redirect",
    link: "https://..."
}
```
is accepting:

```
{
    action: "openRewards"
}
```
and mapping the action internally:

```
const destinations = {
    openRewards: "/rewards",
    openProfile: "/profile"
};
```
The external sender never supplies the destination at all.

### Add CSP

A strong Content Security Policy provides another security boundary.

CSP should not replace the application-level fix, but it can significantly reduce the impact of future injection bugs.

### 23. The Bigger Lesson: Context Matters More Than Sanitization

The most important technical lesson from this finding is simple:

Sanitized ≠ safe.

A value can be safe for HTML while dangerous as:

a URL

JavaScript

CSS

SQL

a shell command

an HTTP header

Security controls must match the parser that ultimately consumes the value.

In this case:

HTML sanitizer

↓

URL sink

was the architectural mistake.

The correct model should have been:

Untrusted URL

↓

URL parser

↓

scheme allowlist

↓

hostname allowlist

↓

navigation

### 24. The Research Mindset

There are several broader lessons bug bounty hunters can take from this case.

Do not stop when you find suspicious code.

Ask:

Can I control it?

Where does it flow?

What parser handles it?

Can I reach the component?

What browser context executes it?

What privileges does that origin have?

What happens when the victim is authenticated?

Do not stop at:

missing origin check

Trace the message.

Do not stop at:

XSS

Map the authenticated APIs.

Do not stop at:

there is a sanitizer

Determine whether it matches the sink.

Do not stop at:

works in my browser

test browser differences.

And when production conditions prevent a safe full-chain test, reproduce the verified behavior in a controlled environment and clearly separate:

production evidence

from:

controlled exploit-chain evidence

That combination of technical depth and disciplined validation is what turns an interesting JavaScript bug into a strong vulnerability report.

### Final Attack-Chain Mental Model

Whenever you encounter cross-window communication, mentally run this checklist:

Who can send the message?

↓

Is event.origin validated?

↓

Which message properties are attacker controlled?

↓

Where do those values flow?

↓

What sink consumes them?

↓

Is sanitization appropriate for that sink?

↓

Can the vulnerable feature actually be reached?

↓

What origin will attacker-controlled code execute under?

↓

What authentication context exists?

↓

Which sensitive APIs become reachable?

That methodology applies far beyond this particular case.

It can uncover vulnerabilities in:

OAuth implementations

payment widgets

embedded checkout flows

SSO integrations

marketing widgets

support systems

survey platforms

authentication popups

loyalty applications

third-party SDK integrations

The important part is not memorizing one payload.

It is learning to identify a broken trust boundary and following attacker-controlled data all the way to its security impact.
