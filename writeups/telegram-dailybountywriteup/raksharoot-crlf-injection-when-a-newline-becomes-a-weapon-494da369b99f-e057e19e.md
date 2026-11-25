# CRLF Injection

- **Source URL:** https://medium.com/@raksharoot/crlf-injection-when-a-newline-becomes-a-weapon-494da369b99f
- **Fetched from:** https://medium.com/@raksharoot/crlf-injection-when-a-newline-becomes-a-weapon-494da369b99f?source=rss-4206d471b207------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14963 (id 14963)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Raksharoot / Wed, 28 Oct 2026 16:50:48 GMT

**Disclaimer:** Educational content only. Only test systems you own or have written permission to test. Never use CRLF injection to poison caches or sessions on production systems.

CRLF injection is the bug that looks boring until it isn’t.

**Two characters -** *\ r* and *\n,* that mark the end of a line in HTTP. Carriage return, line feed. That’s it. That’s the whole mechanism.

But the entire HTTP protocol is built on the idea that these two characters separate headers from body, and headers from each other. So when user input reaches an HTTP response, a log file, a session file, or a memcache command **with these characters intact**, the parser downstream sees a new line and treats whatever follows as something else.

Often something the attacker controls.

The shallow version of this bug gets you open redirects and reflected XSS. The deep version gets you HTTP request smuggling, session file poisoning, and, in one 2026 case, full authentication bypass on cPanel.

Let me walk through how it actually works.

Here’s a normal HTTP response:

The CRLF after each header line tells the parser “this header is done, here’s the next one.” The double CRLF at the end tells the parser “headers are done, here’s the body.”

Now imagine the app does this:

And the attacker sends *?input=value%0d%0aSet-Cookie:%20admin=true*.

The response becomes:

The app set one header. The attacker set two. The browser reads both, and the second one is theirs.

That’s the bug. Everything else is variations on where the CRLF lands.

Before the exploit, look at how it can show up in logs.

Consider an admin panel that logs requests like this:

If the attacker hits ?page=home%0d%0a127.0.0.1%20-%2008:15%20-%20/index.php? page=home&restrictedaction=edit , the log becomes:

The second line looks like it came from localhost. The admin reading the log sees a request from 127.0.0.1 trusted infrastructure — not from the attacker.

The attacker hides their activity by forging their own log entries. It’s not RCE, but it’s how you avoid getting caught while doing everything else in this article.

If you’re a defender, this is why you should never render logs into an HTML page without encoding, and why you should parse structured log formats instead of string-matching.

The direct exploitation path.

If the app reflects user input into a response header without encoding, you can terminate the header block and start a body:

The *%0d%0a%0d%0a* is CRLFCRLF, the double CRLF that marks the end of headers. Whatever follows is treated as the body, and the browser renders it.

If the app is reflected-only and the server doesn’t sanitize, this is a full XSS with no *\<script>* tag needed in the URL.

Same trick, different payload:

The server responds with:

The app was never supposed to redirect. The attacker injected the *Location* header through the URL path.

This is useful because the response itself comes from *trusted.com*. Phishing filters, link scanners, and email gateways will see the domain as legitimate. Only the redirect destination is malicious.

It’s also a great chaining primitive, combine it with SSRF or client-side path traversal and you can bounce a trusted-origin redirect to anywhere.

The Acunetix classic, and still worth understanding:

Read that carefully. The attacker is injecting:

Depending on the proxy, the browser, and how they handle the injected bytes, the second response gets parsed as a new message. Sometimes the browser renders it. Sometimes a cache stores it under the attacker’s URL. Sometimes a proxy desyncs and serves it to the next user.

This is where CRLF injection stops being “reflected XSS with extra steps” and starts being infrastructure-level.

If the injection point is itself an HTTP client (an SSRF target, a webhook handler, a soap client), you can inject a second request rather than a second response.

The classic example is PHP’s *SoapClient*. The *user\_agent* parameter is used verbatim in the HTTP request it constructs:

The user\_agent contains CRLFs, so the request the SoapClient sends to *127.0.0.1:9090* is actually:

If there’s a service listening on that port (a proxy, an admin API, anything), it processes both requests. The first one looks innocuous. The second one does whatever the attacker wants.

PortSwigger’s research on “response queue poisoning” takes this further: by injecting *Connection: keepalive* plus a second request, you can poison the response queue that the next user’s request will read from. That’s not just XSS — that’s a shared-infrastructure bug where every user after you gets your response.

Here’s a bug class that’s genuinely underrated.

Memcache speaks a plaintext protocol. Commands are separated by CRLF. If an app builds a memcache command from user input without sanitizing, the attacker can inject additional commands.

**The Zimbra case** (Sonarsource writeup) is the canonical example. Cache keys were used to store the IP:port a user should connect to. Attackers injected memcache commands via CRLF to poison the cache, redirecting victims to attacker-controlled servers that harvested usernames and passwords.

***There was a second primitive in the same bug:*** response desynchronization. By injecting into one request, the attacker could make memcache return responses intended for a different user — leaking the attacker’s IP : port to users whose email the attacker didn’t even know.

That’s the level of bug you get when a text protocol meets unsanitized input. If the target uses memcache, Redis, or any other line-oriented protocol and reflects user input into commands, this is worth testing.

This is the one I want to spend time on, because it’s the modern example of how CRLF turns into an auth bypass.

In 2026, cPanel and WHM had a pre-auth session file poisoning bug (CVE-2026–41940). The details:

An attacker who could inject:

would produce a session file with:

The session was never authenticated. But the file now says it was.

There’s a subtle detail that made this much worse.

cPanel used structured session cookies where one component selected the storage file and another component enabled encryption. Specifically, *session\_id,* and *session\_id* resolved to the **same raw file**, but omitting *\<secret>* disabled password encoding.

So an attacker could:

Without the optional secret, the whole session file was written raw. The CRLF sanitizer wasn’t in the writer — it was in some callers, and the caller the attacker used wasn’t one of them.

The bug got deeper.

*cPanel maintained two session stores:* a canonical text file and a preferred JSON cache. The text parser treats *\r* and *\n* as record boundaries. The JSON serializer preserves them inside a single string.

A successful write to the raw store didn’t immediately break authentication, because the app reads from the JSON cache first. But the app also had maintenance path - error handlers, repair routines, counter updates,that did this:

At step 2, the forged keys get promoted into the map. At step 4, the promoted keys get written into the JSON cache. Now the app reads the forged keys during normal session loads.

***The trigger in the cPanel chain was simple:*** request a protected route without the URI security-token prefix. That hits a token-denied handler, which increments a counter, which reads the raw file, which promotes the forged keys, which regenerates the cache.

The authorization path then checked *successful\_internal\_auth\_with\_timestamp,* a forged truthy value, and returned success **without consulting */etc/shadow***. Combined with the forged *user=root*, *hasroot=1* , and *tfa\_verified=1*, the pre-auth session became a root-authenticated admin session.

All from a newline in a password field.

Session file poisoning is one of those bugs that only exists because of an architectural pattern: **persist session state as line-oriented text before authentication finishes**. If any request-derived value reaches that file with CRLF intact, the attacker can create new session keys.

The fix isn’t a sanitizer in every caller. It’s a sanitizer in the writer, the single choke point where session values get serialized. And it’s removing the “optional secret” pattern that let one component silently downgrade to unencoded writes.

The same primitive showed up in a different product in a different way.

Infoblox NetMRI exposed *SetRawCookie.tdf* and *SetCookie.tdf* , endpoints that let authenticated users write a cookie to a session file. The URL-decoded value was stored with CRLF intact.

An attacker with Process Manager access could send:

The decoded value is *xyz\r\nUserName=admin*. The session file gets a second line. The reader trusts the injected *UserName=admin* line as the session identity.

Same bug, different sink. The prerequisite is “authenticated user with Process Manager access” instead of “preauth session”, but the impact, impersonating any user — is just as bad.

***The takeaway***: *any endpoint that writes to a line-oriented file is a CRLF sink*. Cookie writers, config managers, log rotators, session savers. All of them.

Unicode and control-character bypasses

Modern WAFs and rewriters strip literal *\r* and *\n* . Some of them forget about the other characters that many back-ends treat as line terminators.

When CRLF is filtered, try:

Apache HttpClient had a bug (HTTPCLIENT-1974) where a “sanitized” header value could still introduce a newline via a Unicode character. The sanitizer had been validated against ASCII CRLF only.

*Payload:*

If the filter normalizes UTF-8 first, turning the Unicode separator into a regular line-feed — the injected header gets accepted. If it doesn’t, the backend still treats the character as a line boundary when it parses.

Test the exact client, proxy, and back-end chain. Different components in the same chain may disagree about which characters count as newlines.

One more trick, because it’s clever.

If you have full header injection, including control over *Content-Length* and *Content-Encoding,* you can confuse the response framing.

*Payload fragment:*

*Content-Encoding: identity* means “no encoding applied.” Some intermediaries (proxies, CDNs, WAFs) treat this as a signal that the body is safe to pass through unmodified. If they do, and the injected *ContentLength* matches the attacker’s body bytes, the response framing gets reinterpreted, and the attacker’s bytes after the header block become the response body.

Exploitability depends heavily on the proxy and browser behavior. Test carefully, on authorized targets only.

Six patterns worth memorizing.

Check if the response contains the injected *Set-Cookie*.

**2. CRLF + open redirect:**

**3. CRLF → XSS:**

**4. Filter bypass via Unicode:**

**5. URL path injection:**

**6. Header injection to smuggling:**

These are valuable because they show CRLF injection is not a legacy bug, it’s in modern libraries.

*The pattern:* **any internal component that performs HTTP requests or sets response headers is a CRLF sink**. Not just the web server edge. Not just the user-facing endpoint. Every library, every client, every wrapper.

This is why you should include library versions in your recon and search for their CRLF advisories.

Not exhaustive, but this is the order I go in:

For developers, the correct pattern is:

CRLF injection is a bug class that only exists because HTTP is a text protocol built on line terminators.

Every layer that parses text, response headers, log files, session files, memcache commands, HTTP client requests, has the same weakness: *a newline in user input is a new instruction*.

The shallow bugs get you XSS and open redirects. The deep bugs get you request smuggling, session poisoning, and authentication bypass.

And the pattern keeps reappearing in new places, libraries in 2024, session files in 2026. It’s not going away. Every time someone builds a new line-oriented format, they forget that CRLF is data, not decoration.

When you’re testing, don’t just look at the URL. Look at what happens to the input after it leaves the URL, where it gets stored, what it gets concatenated into, what parser eventually reads it.

That’s where the bug lives.

That’s Part-11. Read the whole series in order: [Web Pentesting: A Complete Guide.](https://medium.com/@raksharoot/list/web-pentesting-a-complete-guide-ad31d529002a)
