# ipspoof

- **Source URL:** https://exript.medium.com/ipspoof-an-open-source-tool-for-automated-testing-of-http-header-based-access-controls-15fe11b9cace
- **Fetched from:** https://exript.medium.com/ipspoof-an-open-source-tool-for-automated-testing-of-http-header-based-access-controls-15fe11b9cace?source=rss-f04f1e0e0d20------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14918 (id 14918)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Exript / Sat, 19 Sep 2026 19:09:01 GMT

*Discover a commonly overlooked vulnerability class in seconds during pentests and bug bounties*

Nearly every modern web application runs behind a reverse proxy, load balancer, or CDN. These layers pass client information to the application using various **HTTP headers**:

These headers are **user-controllable**. If the application trusts them to make decisions — such as “this user is from the internal network,” “this request comes from the admin IP,” or “this traffic originates from an allowed country” — then access controls can be bypassed by **adding a single HTTP header**.

This vulnerability class is:

ipspoof was built to find this vulnerability class **automatically and quickly**.

Consider a simple scenario. An application’s /admin endpoint is only accessible from the internal network (10.0.0.0/8). The application checks the client like this:

```
client_ip = request.headers.get("X-Forwarded-For")
if client_ip and client_ip.startswith("10."):
    return admin_panel()
else:
    return "Access denied"
```
The application assumes X-Forwarded-For comes from a **trusted** source. But in reality, **any user** can add this header:

curl -H "X-Forwarded-For: 10.0.0.1" https://target/admin

By adding a single header, you just accessed the admin panel.

This vulnerability appears in several forms:

**1. IP Allowlist Bypass** — access is restricted to a specific IP block, you’re outside it, and you spoof the header to get in.

**2. Admin Panel Access** — panel only open from localhost; X-Forwarded-For: 127.0.0.1 gets you in.

**3. Internal API Access** — internal API only callable from the internal network; spoof the header and call it from outside.

**4. Rate Limit Bypass** — rate limiting is per IP; send a different IP each request to bypass it.

**5. Geo-Restriction Bypass** — content is locked to specific countries; spoof the header to access it.

**6. Cache Poisoning** — the cache mechanism keys on the header; poison it with fake headers.

The common thread: **the application trusts a client-controllable header.**

ipspoof automatically discovers this vulnerability class using a **two-phase** pipeline.

**Phase 1 — Header Discovery:**

It sends different **client-IP headers** to the application. It detects which header the application reads, which one it trusts, and which value changes its behavior. It works with 100+ headers and a curated “trusted IP” list.

**Phase 2 — IP Fuzzing:**

After finding which header works, it locks that header and fuzzes the **IP range** you specify (e.g., 10.0.0.1-254). This tells you exactly which IP block bypasses the allowlist.

The result: **which header** and **which IP** combination bypasses access controls — within seconds.

The tool never sends anything malicious. It only adds headers to ordinary HTTP requests.

Those who try manual testing hit this wall:

ipspoof compresses this process:

In short: it replaces manual testing — and it’s not just faster, it’s more **reliable** and more **comprehensive**.

The cleanest path is pipx:

pipx install ipspoof

Alternatively:

pip install ipspoof

With Tor support:

pipx install "ipspoof\[tor\]"

Dependencies are lightweight: requests and urllib3. Installation takes 10 seconds.

ipspoof -u https://target.com/endpoint --follow

**Output:**

\[\*\] Phase 1: Header discovery (105 headers x 11 IPs)

\[+\] HIT: X-Forwarded-For: 10.0.0.1 -> status=200 size=1770

\[+\] HIT: X-Real-IP: 10.0.0.1 -> status=200 size=1770

\[\*\] Phase 1 complete in 39.0s. 4 anomalies.

**Interpretation:** In \~39 seconds you learned that two headers can be spoofed and that internal IPs are accepted.

ipspoof -u https://target.com/endpoint \

--phase2 --ip-pattern "10.0.0.n" --ip-range 1-254 \

--follow

Locks onto the headers found in Phase 1 and fuzzes 10.0.0.1-254. Lists which IPs are accepted.

ipspoof -u https://target.com/api/admin \

-X POST -d "action=delete" \

--header "Authorization: Bearer xyz" \

--body-regex "success"

For login forms, REST APIs, and GraphQL endpoints.

ipspoof -u https://target.com/ --rate 30 \

--proxy-file proxies.txt \

--tor --tor-new-every 10

Max 30 req/s, round-robin proxy rotation, Tor identity rotation every 10 requests.

ipspoof -i

**Comprehensive Header Discovery:**

100+ client-IP headers. X-Forwarded-For, X-Real-IP, Forwarded, Client-IP, CF-Connecting-IP, X-Originating-IP, Via, Proxy-Client-IP, and derivatives.

**Four Detection Modes:**

Status, size, body hash, and body regex. Even same-size different-content responses are caught.

**XFF Chain Variations:**

With --chain:

Bypasses are caught even when the app reads only the first value.

**POST/PUT/PATCH/JSON Support:**

Full support for login forms, REST APIs, and GraphQL.

**Proxy and Tor:**

--proxy-file for round-robin rotation, --tor for SOCKS5, --tor-new-every for periodic identity renewal.

**Rate Limiting:**

--rate N for max req/s. Reduces WAF/IPS ban risk.

**JSON Output:**

-o results.json saves findings in a machine-readable format. For reporting and re-running.

**Interactive Mode:**

Step-by-step prompts. Ideal for beginners.

The program scope includes a SaaS application. In the API docs you spot an endpoint marked “internal.” You try:

ipspoof -u https://api.target.com/internal/users --follow

Phase 1 runs. You see that X-Forwarded-For: 10.0.0.1 returns 200. **You found a critical access control vulnerability.**

The client says, “our admin panel is only open from the internal network.” You test:

ipspoof -u https://admin.client.com/ -i

In interactive mode, you enter the URL, say yes to --follow. Phase 1 shows X-Real-IP: 127.0.0.1 works. **A reportable finding for the client.**

Before going live, you check:

ipspoof -u https://staging.myproduct.com/admin --phase2

You only allow 10.0.0.0/8, but Phase 1 shows X-Forwarded-For can be spoofed. You fix it before shipping.

**1. Baseline Capture:**

Sends a request without spoof headers. Records the status, size, and body hash of the “default” response. This is the reference point.

**2. Header Discovery (Phase 1):**

Sends parallel requests for each (header, trusted IP) pair. Compares responses against baseline. Different status, size, hash, or regex match = **HIT**.

**3. IP Fuzz (Phase 2):**

Locks onto Phase 1’s working headers and fuzzes the IP range. Lists which IPs bypass the allowlist.

**4. Output:**

Prints live HITs to the console, saves findings as JSON.

ipspoof's edge: **specialized for a specific vulnerability class**, two-phase, smart detection, with production features like proxy/Tor/rate-limit.

This tool is for **authorized security testing only**. Use it against:

Unauthorized use against third-party systems is illegal in most jurisdictions. The author cannot be held responsible for misuse. If you’re doing bug bounties, always respect the program’s scope and rules.

☕️ [Support me on Buy Me a Coffee](https://buymeacoffee.com/exript)
