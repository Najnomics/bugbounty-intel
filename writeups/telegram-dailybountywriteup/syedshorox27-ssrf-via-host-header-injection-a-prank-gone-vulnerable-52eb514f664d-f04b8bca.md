# SSRF via Host Header Injection — A Prank Gone Vulnerable

- **Source URL:** https://medium.com/@syedshorox27/ssrf-via-host-header-injection-a-prank-gone-vulnerable-52eb514f664d?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@syedshorox27
- **Fetched:** 2026-11-17
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 10369)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### SSRF via Host Header Injection — A Prank Gone Vulnerable

### 🕵️♂️ How I Made a Server Talk to Me (Host Header Injection to SSRF) 🎯💣

*When I told the server to call me back, and it actually did…* 😏

*“Knock knock.”
 “Who’s there?”
 “You… but inside your own network.”
 —* SSRF, probably

### 💡 What the Heck is SSRF?

**Server-Side Request Forgery (SSRF)** is like a digital prank: you convince a vulnerable server to make requests **on your behalf** — to internal systems, third-party servers, or even back to itself.

Imagine telling someone inside a secure building:

*“Hey, can you go knock on that door?”
 And they just do it. No questions asked. 🤷♂️*

### 🏁 Where It All Began

While poking around the application at https://example.com,

I noticed something *a little too friendly* about how the server handled headers.

So naturally, I thought…

*What if I pretend to be someone I’m not?
 And what if the server actually believes me?*

### 🐞 The Vulnerability: Host Header Injection

Most apps use the Host header to determine routing. But if the app trusts **any host header** — or worse, accepts **X-Forwarded-Host** without validation — it's game on.

So I added a sneaky line into my Burp Suite request:

X-Forwarded-Host: zy1fjueqyy9fujf7bcf6ynn5uw0nodc2.oastify.com

**And guess what?**

The server accepted it like an obedient intern. 🙃

### 🧪 The Setup: Here’s the full HTTP request I sent:

GET / HTTP/1.1

Host: example.com

X-Forwarded-Host: zy1fjueqyy9fujf7bcf6ynn5uw0nodc2.oastify.com

User-Agent: YourFriendlyNeighborhoodPentester

Then I sat back, opened Burp Collaborator, and waited like…

### 😱 The Response (from the server, not my ex)

BOOM! 🎉

Both **DNS** and **HTTP** interactions hit my \*.oastify.com domain.

That means the server was like:

*“Okay bro, calling your domain now. What do you want?”*

This was **confirmed SSRF** — triggered via **Host header injection**.

### 🎯 Real-World Impact

If I can make the server call my domain, I can also ask it to:

- Access internal systems like [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Grab AWS instance metadata via [http://169.254.169.254/latest/meta-data](http://169.254.169.254/latest/meta-data)
- Scan internal services
- Chain it into **RCE**, **data leakage**, or **privilege escalation**

Basically: 💀

### 🧰 Tools I Used

I also tried the legendary [**SSRFmap**](https://github.com/swisskyrepo/SSRFmap):

python3 ssrfmap.py -r request.txt -p X-Forwarded-Host -m readfiles,portscan --ssl

But it whined like:

\[ERROR\]: No injection point found! (use -p)

Classic tools-being-dramatic behavior. So I went manual — and it paid off!

### 🛡️ How to Fix It (for Devs)

1. **Do not trust user-controlled headers** (Host, X-Forwarded-Host, X-Forwarded-For, etc.)
2. Use a strict **allowlist** for valid hostnames.
3. If you rely on headers for routing, use a secure reverse proxy that sanitizes them.
4. Reject or filter suspicious requests before they touch your internal logic.
5. Monitor unexpected outbound traffic — you never know when your app becomes a middleman in someone else’s mischief.

### 🧠 Final Thoughts

What seemed like a boring header turned into a full-blown **SSRF exploit**. All because the server didn’t verify who it was talking to.

Host Header Injection is like giving someone a fake return address — and they blindly send you their secrets.

And SSRF? It’s that “guy inside the building” who doesn’t ask questions, just makes phone calls — and maybe even sends files 🤫.

### 💬 Gotchas, LOLs, and Lessons

- Don’t always rely on tools. Your brain and Burp Suite are a deadly combo 💥
- If you’re not getting hits in Burp Collaborator, try **redirects** or **iframes**
- Always monitor both DNS and HTTP interactions — sometimes the server’s just being sneaky, like my friend [Shazilrao](https://medium.com/u/20ae7253d293)🐍
Just kidding 😄 — he’s not sneaky (most of the time). He’s actually a sharp bug hunter and pentester! You can check out his blog too — full of cool tricks and techniques that’ll make your Burp smile.

[https://medium.com/@shazilrao620/from-image-upload-to-account-takeover-chaining-upload-storage-and-cors-issues-in-a-real-pentest-de5ac9862c31](https://medium.com/@shazilrao620/from-image-upload-to-account-takeover-chaining-upload-storage-and-cors-issues-in-a-real-pentest-de5ac9862c31)

### 🫶 Like What You Read?

Let’s connect on [LinkedIn](https://www.linkedin.com/in/syed-hasan-26a07b232/), or shout out in the comments!

And remember:

*With great SSRF comes great* ***liability disclosure forms*** *📝
 (and sometimes bounty 💰)*

Stay safe, stay curious!

— *YourFriendlyNeighborhoodPentester*

#BugBounty #WebSecurity #SSRF #HostHeaderInjection #Hacking #CyberSecurity #PenetrationTesting #InfoSec #SecurityResearch #EthicalHacking #RedTeam #BugBountyTips #CTF #OWASP #WebAppSecurity #SecurityVulnerabilities #HackThePlanet #BugHunters
