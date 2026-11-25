# From IDOR to Fraud

- **Source URL:** https://medium.com/@romene.mohtadi.it/from-idor-to-fraud-breaking-access-control-in-a-travel-booking-platform-ef63f6b0bb2b
- **Fetched from:** https://medium.com/@romene.mohtadi.it/from-idor-to-fraud-breaking-access-control-in-a-travel-booking-platform-ef63f6b0bb2b?source=rss-0c8b34f211d5------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14916)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mohtadi Romene / Thu, 17 Sep 2026 18:32:59 GMT

During a recent **application security assessment conducted within a professional engagement**, I identified a critical **Broken Access Control (IDOR)** vulnerability affecting a production travel booking platform.

What initially appeared as a simple parameter manipulation quickly evolved into a **multi-step attack chain** with real-world implications, including potential account takeover and financial fraud.

This article walks through the vulnerability, its impact, and how it can be chained into realistic exploitation scenarios.

The issue lies in multiple API endpoints that expose user data based on a bookingId parameter:

GET /fr/account/getbooking?bookingId=XXXX

GET /fr/account/getbookingFlight?bookingId=XXXX

By modifying the bookingId, it was possible to access data belonging to other users.

No ownership validation was enforced server-side.

This is a classic **Insecure Direct Object Reference (IDOR)**, categorized under **Broken Access Control (OWASP Top 10)**.

A valid user session is used to capture a request:

GET /fr/account/getbookingFlight?bookingId=180845

The bookingId is modified to another valid identifier:

GET /fr/account/getbookingFlight?bookingId=180844

The server returns another user’s data, including:

This confirms a **complete failure of object-level authorization**.

The vulnerability allows access to:

This creates a direct privacy breach and potential regulatory risk.

The real impact goes beyond data exposure.

Using leaked information, an attacker can perform:

This demonstrates how a simple IDOR can evolve into a **complete exploitation chain**.

The following threat model illustrates how the vulnerability propagates across the application:

The diagram highlights how a lack of authorization control enables data exposure, which can be leveraged in downstream attack scenarios leading to account compromise and fraud.

The vulnerability originates from:

This represents a **systemic Broken Access Control issue rather than an isolated flaw**.

To mitigate this vulnerability:

This case reinforces a fundamental principle:

**Access control must never rely on client input and must be consistently enforced across all application layers.**

A single missing validation can lead to:

This assessment demonstrates how a seemingly simple vulnerability can escalate into a real-world attack scenario with tangible consequences.

In modern API-driven architectures, security must be enforced consistently to prevent such escalation paths.

*Disclosure handled responsibly prior to publication.*

#CyberSecurity #Pentest #AppSec #OWASP #IDOR #BugBounty #RedTeam
