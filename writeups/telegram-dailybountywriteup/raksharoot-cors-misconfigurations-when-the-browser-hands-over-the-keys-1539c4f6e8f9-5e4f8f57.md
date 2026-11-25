# CORS Misconfigurations

- **Source URL:** https://medium.com/@raksharoot/cors-misconfigurations-when-the-browser-hands-over-the-keys-1539c4f6e8f9
- **Fetched from:** https://medium.com/@raksharoot/cors-misconfigurations-when-the-browser-hands-over-the-keys-1539c4f6e8f9?source=rss-4206d471b207------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14952)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Raksharoot / Sun, 18 Oct 2026 18:37:36 GMT

Disclaimer: Educational content only. Only test systems you own or have written permission to test. Never test CORS bypasses against live users without explicit authorization

CORS is one of those features that everyone uses and almost nobody configures correctly.

***The idea is simple:*** the same-origin policy blocks a page on *attacker.com* from reading responses from *bank.com* . CORS lets *bank.com* say “actually, *partner.com* can read this.” It’s an opt-in relaxation.

But the way most developers implement it is… creative. They copy a snippet from Stack Overflow, add a wildcard, and move on. Or they reflect whatever origin the browser sends, because that “just works” during development.

And that’s how you get a bug where *attacker.com* can read a victim’s private data using their own cookies.

Let me walk through how this actually breaks.

Two servers are same-origin if they share:

Everything else is cross-origin, and the browser blocks the reading of cross-origin responses by default.

CORS is the server’s way of saying “this origin is allowed.” It does that with response headers:

The one that matters most for exploitation is the combination of *Allow-Origin* and *AllowCredentials*.

Before a “non-simple” cross-origin request (anything that isn’t *GET* , *HEAD* , or *POST* with a basic content type), the browser sends an *OPTIONS* request first. That’s the preflight.

It tells the server: “I want to send a *PUT* with these custom headers from *example.com* . Is that okay?”

The server responds with what’s allowed. If the preflight fails, the actual request never happens. Here’s what a preflight looks like:

And the response:

For simple *GET* and *POST* requests, no preflight is sent, the request goes straight through. But the response still needs *Access-Control-Allow-Origin* for the browser to let the page read it. Without that header, the request happens but the response is invisible to JavaScript.

That’s why CORS doesn’t protect against CSRF. The request always goes through. CORS only controls whether the attacker’s page can read the response.

You’ll see this configuration a lot:

*Access-Control-Allow-Origin: \**

*Access-Control-Allow-Credentials: true*

That looks dangerously permissive. And it is. But the browser rejects it.

The CORS spec says you cannot use \* with credentials. The browser will refuse to send cookies in that case, and the attack doesn’t work.

So if you see \* alone, it’s usually not exploitable, unless the page is doing something weird with authentication tokens in URLs or headers.

*The dangerous pattern is different:Allow-Origin* reflects the request’s *Origin* header, and *Allow*-*Credentials* is *true* .

The vulnerable pattern is dead simple:

Developers do this because they want to allow multiple origins and they don’t want to maintain an allowlist. So they just echo the Origin back. And the browser happily lets *attacker.com* read authenticated responses.

Here’s the exploit:

The victim visits *attacker.com*. The script sends a request to *victim.com* with *withCredentials = true*. The cookies go along. The server reflects the origin, sets *Allow-Credentials: true*, and the browser hands the response back to JavaScript.

The attacker reads it. Then exfiltrates it.

Game over.

You can test for this by sending a request with *Origin: https://attacker.com* and checking if the server returns *Access-Control-Allow-Origin: https://attacker.com*. If it does, and Allow-Credentials is true — you’ve got a finding.

Some apps whitelist *null* as an allowed origin. The reasoning is usually: “we need to support local HTML files during development” or “we redirect and the origin becomes null.”

That’s a bug.

You can get a *nu*ll origin from a sandboxed iframe:

The iframe runs with a *null* origin. The request goes out. If the server’s allowlist includes *null*, the response comes back, with the victim’s cookies attached.

I’ve seen this on real targets. It’s not theoretical.

Most apps don’t reflect arbitrary origins. They use a regex allowlist. Something like:

*if (preg\_match(‘/^https:\/\/.\*\.trusted\.com$/’, $origin)) { … }*

That looks reasonable. It’s also trivially bypassed.

If the regex checks for “contains *trusted.com* ”, try:

Both contain the trusted string. Neither is the trusted domain.

If the allowlist includes *\*.trusted.com* and one of those subdomains is vulnerable to XSS or takeover, you can use it as a pivot. Your XSS on *sub.trusted.com* can read from *api.trusted.com*.

Chrome and Firefox accept underscores in hostnames, even though the DNS spec doesn’t. That breaks regexes that expect only alphanumerics, dots, and hyphens.

*Origin: https://target.application\_.attacker.com*

If the regex is *^https://target\.application.\** , and it doesn’t anchor properly, this passes. And the browser treats *target.application\_.attacker.com* as a valid hostname.

Safari is even more permissive. It accepts curly braces and other special characters that break naive parsers:

*Origin: https://target.application}.attacker.com*

If the server-side regex allows *target.application* followed by anything, and the browser still treats *attacker.com* as the actual origin, you win.

PortSwigger’s cheat sheet has a whole family of these. Worth fuzzing when you see Origin validation:

If the app does *startsWith(“https://trusted.com")* , try:

*Origin: https://trusted.com.attacker.com*

It starts with the trusted string. It’s not the trusted domain. If it does *endsWith(“trusted.com”)* , try:

*Origin: https://attacker.com/trusted.com*

Path traversal in the origin. It ends with the trusted string. The browser normalizes it.

Some regexes forget to anchor the scheme or port:

Test all of these.

There’s a separate standard called Private Network Access (PNA) that governs requests from a public origin to a private IP address.

The preflight for PNA looks like:

And the server must respond with:

The rollout of PNA enforcement has been messy. Chrome paused preflight enforcement at various points because of compatibility issues. So it’s worth testing both the spec-compliant flow and the “it works because enforcement is incomplete” flow.

*One thing to note:0.0.0.0* used to bypass local network restrictions because it wasn’t treated as “local.” Chrome has since changed this — *0.0.0.0/8* is now part of PNA. Don’t assume the old trick works; test it per browser.

***Another quirk:*** if you can reach a local endpoint through its public IP, you may bypass PNA entirely. If the public IP routes back to the private network, the browser sees it as a public-to-public request. This is environment-dependent and worth probing.

Two cache poisoning variants matter here.

If the app reflects the *Origin* header into *Access-Control-Allow-Origin* without sanitizing, and it doesn’t set *Vary: Origin*, the response can be cached and served to other users.

The header injection variant is nastier. Old Internet Explorer and Edge treated 0x0d as a header terminator. So:

*Origin: z\[0x0d\]Content-Type: text/html; charset=UTF-7*

became:

Now the response is served as UTF-7, which is a classic XSS bypass. If the response gets cached, every subsequent visitor gets the malicious response.

You can’t trigger this from a browser directly, modern browsers sanitize the header. You’d have to craft it in Burp or curl. But once it’s cached, everyone gets it.

If a page reflects a custom header’s value into its own HTML without encoding, you can inject via *X-Custom-Header*.

**The attack:** send a request with a malicious header. If the response is cached and *Vary: Origin* isn’t set, the cached response includes your payload. Then navigate to the URL, the browser renders the cached response, and your script executes.

This is a niche variant, but it’s worth knowing.

Cross-Site Script Inclusion (XSSI) abuses the fact that *\<script>* tags are not subject to the same-origin policy.

When you load a script from another origin, it runs in your page. That’s by design, it’s how you load third-party libraries. But it also means any data served as JavaScript can be read.

Older APIs served JSON as a top-level array, which is valid JavaScript. So:

*\<script src=”https://victim.com/api/user?callback=...">*

would execute the JSON as JavaScript and leak data through error messages, side channels, or by overriding array methods.

***Modern defenses:*** serve JSON with *Content-Type: application/json*, prepend *)\]}’,\n* to JSON responses, use *X-Content-Type-Options: nosniff*.

JSONP is a deliberate XSSI-like pattern. The API wraps the response in a callback:

*callback({“username”: “victim”, “email”: “victim@example.com”})*

If the callback name is user-controlled, you can use it as an XSS sink. If the endpoint is authenticated via cookies, you can read the response.

The victim’s cookies go along with the script request (assuming *SameSite* doesn’t block it). The API returns the JSON wrapped in *steal(…) .* Your function runs. You get the data.

JSONP is mostly dead, but it still shows up on legacy endpoints. If you see *?callback= , ? jsonp= ,* or *?jsonpcallback=* , pay attention.

Not exhaustive, but this is the order I go in:

For developers, the correct pattern is:

CORS is a browser feature, not a server security control. It doesn’t stop requests, it stops reads. That means a misconfigured CORS policy doesn’t prevent attackers from making requests, it just determines whether they can read the response.

When you find a CORS misconfiguration, ask: what can the attacker read that they shouldn’t?

If the answer is “a session token” or “a private profile” or “the victim’s email,” you have account takeover or data leakage.

If the answer is “a public API response,” it might be a low-severity finding.

The severity lives in what’s behind the CORS policy, not in the header itself.

Test with a browser, not just curl — preflight, credentials, and the same-origin policy all behave differently in a real browser context. And always verify the bypass works end-to-end before writing it up.

That’s Part 8. Read the whole series in order: [Web Pentesting: A Complete Guide.](https://medium.com/@raksharoot/list/web-pentesting-a-complete-guide-ad31d529002a)
