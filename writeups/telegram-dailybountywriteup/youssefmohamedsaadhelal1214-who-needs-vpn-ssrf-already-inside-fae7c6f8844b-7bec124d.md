# Who Needs VPN?? SSRF Already inside

- **Source URL:** https://medium.com/@youssefmohamedsaadhelal1214/who-needs-vpn-ssrf-already-inside-fae7c6f8844b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260324194432/https://medium.com/@youssefmohamedsaadhelal1214/who-needs-vpn-ssrf-already-inside-fae7c6f8844b?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13139 (id 13139)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Who Needs VPN?? SSRF Already inside

A bug bounty story about quiet nights, one suspicious parameter, and an unauthenticated path straight into example.com’s internal network.


It was past midnight. The kind of hour where the world goes silent and your terminal glow feels like the only light left. I had a fresh cup of coffee, a target scope, and nothing but time.

### Prologue — The Late-Night Hunt

Some of my best findings happen in the dark. Not metaphorically — literally. There’s something about 2 AM, a quiet room, and the soft hum of a fan that sharpens focus in a way daylight never does. I was deep into example.com’s bug bounty scope on HackerOne, going through API endpoints one by one, sipping coffee, half-expecting nothing.

Then I saw it.

A parameter called

`swaggerUrl`
Something about it felt… off.

## Chapter 1 — The Suspicious Endpoint

The endpoint in question:

`GET /api/v1/home/GetSwaggerEndpoints?swaggerUrl=<USER_INPUT>`
**Host: plasma-coreapi.example.com**

**Authentication required:** None

**Rate limiting:** None

At first glance, it looked like a documentation helper — something to fetch \`Swagger/OpenAPI\` specs from a given URL. But the moment I saw a user-controlled URL being accepted by a server-side HTTP client, my instincts kicked in.

*What if it just… fetches whatever I tell it to?*

I spun up Burp Suite, loaded Burp Collaborator, and sent the simplest possible test:

`swaggerUrl=http://<my-collaborator-payload>`
I leaned back. Took a sip of coffee.

Then the callbacks hit.

## Chapter 2 — Burp Collaborator Lights Up

**DNS callback. Then another. Then HTTP.**

```
Source IP: [REDACTED]
Time: 2026-Mar-15 00:06:06 UTC
Type: HTTP
```
*The server pinged me back.*

This confirmed out-of-band SSRF — the application was making real HTTP requests to my controlled URL, and the outbound source IP was now identified as example.com’s `plasma-coreapi` server address. A detail that would become important later.

## Chapter 3 — Going Deeper: The Internal Network

If the server fetches external URLs, would it fetch *internal* ones too?

I tried the classic:

`swaggerUrl=http://169.254.169.254/latest/meta-data/`
Then I tried the internal RFC-1918 range. And that’s when things got interesting.

`swaggerUrl=http://10.0.1.1/`
The response came back:

```
{
  "IsSuccess": true,
  "Data": "<!DOCTYPE html>\n<html>\n<head>\n<title>Juniper Web Device Manager</title>...",
  "Message": "Success"
}
```
I stared at my screen.

*Juniper Web Device Manager.*

**A firewall admin panel. In production. Unauthenticated.**

I refilled my coffee. My hands were steady, but my mind was racing.

## Chapter 4 — Port Scanning via Error Oracle

Here’s where it became methodical. The endpoint behaved differently depending on what it found at the target:

This was a perfect **error-based port scanner** built right into example.com’s own API.

I started mapping the subnet `10.0.1.x`.

## Chapter 5 — The Internal Map

What I found over the next hour painted a clear picture of example.com’s internal Kubernetes cluster:

## Chapter 6 — The Impact

Let me be clear about what this meant:

## Juniper SRX1600 Firewall — J-Web Exposed

The Juniper SRX1600 is a **production network security gateway**. Its J-Web admin interface controls firewall rules, routing policies, and security zones for the entire example.com cluster. An attacker with access to J-Web (via default credentials, credential stuffing, or a known CVE) could:

- Modify or delete firewall rules
- Redirect or intercept internal traffic
- Disable security policies
- Cause full network disruption

## NETCONF/YANG (Port 830)

NETCONF is a **programmatic network management protocol** — essentially an API for reconfiguring network devices. If authentication could be bypassed or credentials obtained, an attacker could automate full reconfiguration of example.com’s network infrastructure.

## MySQL Access Vector

MySQL is confirmed running at `10.0.1.254:3306`. Combined with database credentials found in a separate finding, this SSRF creates a chained attack path to interact directly with production databases.

## Full Network Reconnaissance

With no credentials and no rate limiting, I could enumerate the entire `10.0.1.x/24` subnet — building a complete infrastructure map that would normally require insider access or a separate network breach.

## Chapter 7 — The Attack Chain

```
Attacker (unauthenticated)
        ↓
GET /api/v1/home/GetSwaggerEndpoints?swaggerUrl=http://10.0.1.1/
        ↓
plasma-coreapi.example.com
        ↓  [internal network hop]
10.0.1.1 — Juniper SRX1600 J-Web Admin Panel
        → HTML returned = admin login accessible
        → Port 830 NETCONF reachable
        → Potential: full firewall takeover
```
## Chapter 8 — Disclosure

I documented everything carefully — the Burp Collaborator callbacks, the Juniper HTML, the MySQL handshake, the SSH banner, the internal map — and submitted the report to example.com via HackerOne.

The report was marked **Duplicate**.

Another researcher had found the same SSRF 12 days earlier. My submission was 12 days late to the party.

That stings a little. But that’s the nature of bug bounty — sometimes you’re second. And honestly, knowing someone else also found it independently just validates that it was a real, significant vulnerability.

The important thing is that example.com was notified, and (hopefully) the endpoint has been taken offline or patched.

*Thanks for reading. If you found this useful, follow for more bug bounty writeups.*

*— tyrion404*
