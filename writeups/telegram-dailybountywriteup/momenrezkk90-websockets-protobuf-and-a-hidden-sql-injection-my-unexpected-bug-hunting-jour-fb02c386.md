# WebSockets, Protobuf, and a Hidden SQL Injection

- **Source URL:** https://medium.com/@momenrezkk90/websockets-protobuf-and-a-hidden-sql-injection-my-unexpected-bug-hunting-journey-c22e935cca72?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250901030403/https://medium.com/@momenrezkk90/websockets-protobuf-and-a-hidden-sql-injection-my-unexpected-bug-hunting-journey-c22e935cca72
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10376 (id 10376)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# WebSockets, Protobuf, and a Hidden SQL Injection: My Unexpected Bug Hunting Journey 🔍

When most people think of bug hunting, they imagine chasing down obvious vulnerabilities — broken access controls, exposed APIs, or outdated libraries. But sometimes, the biggest discoveries come when nothing seems wrong on the surface.

Recently, I was invited to test a **private bug bounty program**, and what I encountered completely changed how I look at modern web applications.

## The Curious Case of the Missing HTTP Requests

Everything looked normal at first. The site offered standard functionality: login, password resets, profile management, and more. But when I fired up **DevTools and Burp Suite**, I noticed something strange — **no HTTP requests** were being sent when actions were performed. No POSTs, no GETs, nothing.

It felt like hitting a wall. If no HTTP requests were being made… how was any data being transmitted?

## Enter WebSockets: The Real Backbone of the App 🌐

After digging deeper, I discovered the site wasn’t using REST or GraphQL APIs at all. **Every single action — from login to password changes — was handled via WebSockets.**

WebSockets are typically used for real-time features like chat, notifications, or live updates. But here? They were used **exclusively**. No standard API calls, no XHR — **just persistent, bidirectional WebSocket connections**.

This immediately raised the stakes. Testing WebSocket-based applications is more complex. Traditional security tools aren’t as effective, and the behavior can be less predictable.

## The Plot Twist: Protobuf Instead of JSON 🤯

At this point, I assumed the WebSocket payloads would at least be in **JSON**. But when I captured the data — it was **binary**. After some investigation, I realized the application used **Protocol Buffers (Protobuf)** — a compact binary serialization format developed by Google.

## Why combine WebSockets with Protobuf?

- **Performance**: Smaller, faster messages than JSON or XML.
- **Efficiency**: Reduced bandwidth and parsing overhead.
- **Obfuscation**: Binary data makes it harder to inspect and reverse-engineer (though it’s not true security).

While this combo boosts performance, it significantly raises the bar for **security testing**.

## Challenges in Testing WebSocket + Protobuf Apps 🛠️

This setup created several unique challenges for bug hunting:

- **No readable payloads**: Without decoding Protobuf, requests appear as raw binary blobs.
- **Tools require extra setup**: Burp Suite needs specific extensions to decode and inspect Protobuf data.
- **Request tampering is risky**: The server used integrity checks and random signatures. Modifying even a single byte broke the request entirely.

It was like trying to solve a puzzle in the dark.

## Persistence Pays Off: A Hidden SQL Injection 🏆

Despite the complexity, I didn’t give up. I adapted:

- Used **WebSocket traffic analyzers** to monitor real-time data.
- Employed **Protobuf decoders** to reconstruct message structures.
- Analyzed the binary payloads byte by byte to identify patterns.

And finally — I found a **SQL injection vulnerability** buried deep in one of the WebSocket request flows.

This discovery landed me in the program’s **Hall of Fame**, but more importantly, it was a powerful reminder: **even modern applications with advanced protocols are not immune to classic vulnerabilities**.

## What I Learned From This Experience ✨

- **Check for WebSockets** in every test — especially if something seems off.
- **Learn Protobuf** — it’s increasingly used in performance-focused apps.
- **Bug hunting is about adaptation** — every target has something new to teach you.

At the end of the day, this wasn’t just a technical win — it was a **learning experience** that pushed me beyond my comfort zone and helped me grow as a security researcher.

## Have You Encountered WebSockets + Protobuf?

If you’ve worked with or tested similar setups, I’d love to hear how you approached it. Let’s exchange ideas and techniques!

**❤️الحمدلله❤️  for the opportunity and the lessons learned.**

#BugBounty #WebSockets #Protobuf #CyberSecurity #PenetrationTesting #EthicalHacking #APIsecurity #InfoSec #SecurityResearch #SQLi #VulnerabilityResearch #DevSecOps #LearnInPublic
