# 🐛 Bug Bounty Writeup

- **Source URL:** https://jerrome1.medium.com/http-request-smuggling-the-silent-killer-hiding-in-your-proxy-chain-5337e665fb32
- **Fetched from:** https://jerrome1.medium.com/http-request-smuggling-the-silent-killer-hiding-in-your-proxy-chain-5337e665fb32?source=rss-84ae8e69ad27------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14893 (id 14893)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Umair Majeed / Tue, 01 Sep 2026 19:21:25 GMT

How a decades-old ambiguity in the HTTP specification still lets attackers hijack sessions, poison caches, and bypass security controls.

Modern web applications are rarely a single server talking directly to a browser. In front of almost every application sits a chain of intermediaries — load balancers, reverse proxies, CDNs, WAFs, API gateways — each one receiving a raw HTTP request, parsing it, and forwarding it (often re-serialized) to the next hop.

**HTTP Request Smuggling** (also called *HTTP Desync Attacks*) exploits the fact that not every device in that chain agrees on where one request ends and the next one begins. When the front-end server and the back-end server disagree about a request’s boundary, an attacker can craft a single HTTP request that is interpreted as *two different requests* by the two servers. The result: one attacker-controlled request gets silently smuggled through the front-end and processed by the back-end as if it belonged to the *next* legitimate user’s connection.

This isn’t a theoretical bug. Request smuggling has been used to hijack authenticated sessions, bypass front-end access control and WAF rules, poison web caches at scale, and perform reflected XSS against victims who never clicked a malicious link. James Kettle’s research at PortSwigger (2019 onward) revived this attack class after it had been mostly forgotten since the mid-2000s, and it has remained a staple of high-severity bug bounty reports ever since.

This article breaks down exactly how the desync happens, walks through each smuggling variant with raw request examples, shows how to detect and exploit it safely, and covers the defenses that actually work.

HTTP/1.1 gives servers two different headers to determine the length of a request body:

The HTTP specification (RFC 7230, later RFC 9112) says that if *both* headers are present, Content-Length must be ignored in favor of Transfer-Encoding. In practice, not every piece of software follows this rule consistently — and some older or performance-optimized servers don't support chunked encoding at all on the front end, silently falling back to Content-Length.

When a front-end proxy and a back-end application server pick **different** headers to trust for the *same request*, they will disagree on where the request body ends. Whatever bytes are left over after the “official” end (as one server sees it) don’t disappear — they get treated as the beginning of the **next** request on that same TCP connection.

Because front-end-to-back-end connections are almost always **persistent and re-used across multiple clients** (for performance), that “leftover” fragment doesn’t just get dropped — it sits at the front of the queue, waiting to be glued onto whatever the *next unrelated user* sends. That is the entire mechanism of request smuggling in one sentence: **desynchronized parsing + connection reuse = attacker-controlled data prepended to a victim’s request.**

Security researchers classify smuggling attacks by which header each server trusts, written as \[Front-end\].\[Back-end\].

The front-end reads exactly Content-Length bytes and forwards everything. The back-end, however, looks for Transfer-Encoding: chunked first, processes the chunked body, hits the terminating 0, and then treats everything *after* that as a brand-new request.

http

POST /login HTTP/1.1

Host: vulnerable-app.com

Content-Length: 13

Transfer-Encoding: chunked

0

SMUGGLED

The reverse scenario. The front-end processes the request as chunked, but the back-end only understands Content-Length and reads a fixed number of bytes, leaving the rest of the chunked-encoded data to be reinterpreted as a separate request.

POST /login HTTP/1.1

Host: vulnerable-app.com

Content-Length: 3

Transfer-Encoding: chunked

8

SMUGGLED

0

Both servers claim to support chunked encoding, but the attacker obfuscates the Transfer-Encoding header so that one server fails to recognize it and falls back to Content-Length, effectively reproducing a CL.TE or TE.CL condition through header manipulation rather than genuine feature gaps. Classic obfuscation techniques include:

Transfer-Encoding: xchunked

Transfer-Encoding : chunked (space before colon)

Transfer-Encoding: chunked

Transfer-Encoding: x

Transfer-Encoding:\[tab\]chunked

Transfer-Encoding: chunked

Transfer-Encoding: cow

Some parsers only check the *first* Transfer-Encoding header when duplicates exist; others check the *last*; others normalize whitespace differently. Every discrepancy is a potential desync point.

Here is what actually happens on the wire when an attacker’s smuggled request “poisons” the next request on a re-used back-end connection:

Request smuggling is rarely the end goal by itself — it’s a primitive that unlocks other attacks:

Many architectures enforce access control at the reverse proxy or WAF layer (e.g., blocking /admin unless internal). By smuggling a request that the front-end never fully inspects, an attacker's back-end request can slip past those controls entirely, since the front-end only sees a truncated or disguised version of it.

By smuggling a partial request with no Host or trailing headers, the attacker forces the *next legitimate user's* request to be concatenated onto their own. When the back-end responds, the response meant for the smuggled fragment is returned to the **victim's** connection, and the response meant for the victim is returned to the **attacker's** connection — capturing session cookies, CSRF tokens, and personal data in transit.

If a CDN or caching proxy sits in front of the vulnerable stack, an attacker can smuggle a request that causes the cache to store a malicious response (e.g., a redirect to an attacker-controlled domain or a reflected XSS payload) under a legitimate, frequently-requested URL. Every subsequent visitor to that cached URL receives the poisoned response until the cache entry expires.

Because the attacker controls what the victim’s browser renders as a “response” to a request it never truly sent, request smuggling can deliver stored-like XSS to victims who simply happened to make a request on a shared connection at the wrong moment — no phishing link required.

Front-ends that accept HTTP/2 from the client but downgrade to HTTP/1.1 when talking to the back-end reintroduce the entire CL/TE ambiguity, even though HTTP/2’s binary framing has no such issue on its own. Confusion during the H2-to-H1 translation (e.g., trusting an injected content-length pseudo-header, or mishandling illegal headers that should be stripped) has produced a modern wave of "H2.CL" and "H2.TE" desync bugs.

The most reliable way to detect a potential desync without risking real users’ traffic is to send a request designed to make the **back-end** hang if it’s waiting for more data that never arrives, while the front-end considers the request already complete.

Example CL.TE probe:

POST / HTTP/1.1

Host: target.com

Content-Length: 4

Transfer-Encoding: chunked

1

A

X

If the application is vulnerable, the front-end forwards only 4 bytes (1\r\nA\r\n) and considers the request finished. The back-end, parsing chunked encoding, expects a terminating 0 chunk that never arrives — and hangs until timeout. A consistent, reproducible delay is a strong signal of CL.TE desync.

Send two requests back-to-back on the same connection: a suspected “smuggling” request followed by a normal, distinguishable request (e.g., GET /nonexistent-path-xyz). If the second request's response comes back mangled, truncated, or resolves to a completely different resource than expected, the first request successfully desynced the connection.

*Detection testing against production systems you don’t own or have explicit authorization to test is illegal in most jurisdictions. Always confirm scope and rules of engagement before probing.*

LayerDefenseProtocolUse **HTTP/2 end-to-end** between front-end and back-end wherever possible — HTTP/2’s length-prefixed binary framing removes the CL/TE ambiguity entirely, since there is no equivalent header confusion.Front-end configReject requests that contain **both** Content-Length and Transfer-Encoding headers outright, rather than trying to guess which one is authoritative.Front-end configNormalize and re-serialize every request before forwarding it, rather than passing raw bytes through — this guarantees the back-end only ever sees a canonical, unambiguous representation.Connection handlingDisable connection reuse between front-end and back-end for untrusted traffic, or close and re-establish the connection after any request with an ambiguous or malformed length header.Header hygieneStrip or reject obfuscated Transfer-Encoding variants (extra whitespace, invalid casing, duplicate headers) at the earliest parsing point.MonitoringLog and alert on 400/408 responses and unusual back-end connection timeouts, which are common side effects of failed smuggling attempts.ArchitectureWhere possible, use a single well-audited reverse proxy technology consistently across the stack rather than mixing multiple vendors with different parsing implementations.

No single control is bulletproof on its own — the strongest posture combines protocol-level fixes (HTTP/2 backend connections) with strict parsing hygiene at every hop.

HTTP request smuggling was first documented publicly around 2005, faded from mainstream attention for over a decade, and then came roaring back after 2019 as researchers realized that the explosion of microservices, CDNs, and layered reverse proxies had multiplied the number of places where two pieces of software might parse the *same bytes* differently. Every new intermediary added to a request’s path — API gateway, service mesh sidecar, WAF, load balancer — is another opportunity for a parsing disagreement.

As organizations continue to stack more infrastructure between the client and the application, request smuggling is likely to remain a high-value, high-impact bug class for years to come. Understanding the underlying desync mechanism — not just memorizing CL.TE and TE.CL payloads — is what separates testers who can find *novel* variants (like H2 downgrade smuggling) from those who can only replay known proof-of-concepts.

*If you found this useful, consider following for more deep dives into web application security internals, penetration testing methodology, and real-world vulnerability research.*
