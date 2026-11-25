# The Bouncer Who Only Read IPv4

- **Source URL:** https://medium.com/@mohamed.adel.887275/the-bouncer-who-only-read-ipv4-ssrf-in-wordpress-playgrounds-cors-proxy-bcfeac7b37d3
- **Fetched from:** https://web.archive.org/web/20261106110833/https://medium.com/@mohamed.adel.887275/the-bouncer-who-only-read-ipv4-ssrf-in-wordpress-playgrounds-cors-proxy-bcfeac7b37d3
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14970 (id 14970)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The Bouncer Who Only Read IPv4: SSRF in WordPress Playground’s CORS Proxy

An errand-boy proxy, a split-personality hostname, and a delivery to the proxy’s own mailroom.

## The Setup

Inside the WordPress Playground ecosystem lives a **CORS proxy** — a server whose entire job description is:

“Give me a URL and I’ll fetch it for you.”


A universal errand boy. Historically speaking, “fetch whatever URL you’re given” is exactly the job where somebody eventually asks the errand boy to knock on doors he really, truly should not.

Naturally, this proxy has a bouncer at the door: before fetching your URL, it validates the destination is **not a private/internal IP**. You don’t want strangers using your errand boy to knock on your own back doors.

Here’s the bouncer, paraphrased from `url_validate_and_resolve()` in the open-source repo:

```
$ips = gethostbynamel($host);        // ← resolve hostname to IPs
foreach ($ips as $ip) {
    if (is_private($ip)) reject();   // ← no internal deliveries!
}
// then pin the validated IP so DNS can't swap mid-flight:
curl_setopt($ch, CURLOPT_RESOLVE, array(
    "$host:80:$resolvedIp",
    "$host:443:$resolvedIp",
));
```
Spot the problems? No? Good — that’s the whole bug. Let me point at them.

## Problem 1: The Bouncer Is Monolingual

`gethostbynamel()` is a PHP function that returns **IPv4 addresses only**. A records. That's it. That's the whole vocabulary.

The bouncer checks the English side of the business card and has never flipped it over.

Every hostname on the internet has **two** sides:

- The **A record** (IPv4) → what the bouncer checks ✅
- The **AAAA record** (IPv6) → what the bouncer has never heard of ❌

So I gave a free DuckDNS hostname a split personality:

```
A    = 1.1.1.1      ← public, innocent, passes the check ✅
AAAA = ::1          ← "the proxy server's own localhost" 💀
```
Setting it up took exactly two clicks. Behold, the split-personality hostname factory:

The bouncer reads the IPv4 side: *“1.1.1.1? Totally public. Come on in.”* Then curl — which, like every modern piece of software, speaks both languages — happily dials the **IPv6** address: `::1`. The proxy's own loopback.

The errand boy just delivered a package to his own house’s mailroom. With the boss’s blessing. In writing.

## Problem 2: The VIP Pin Only Covers Two Doors

Even the IP-pinning — meant to stop DNS from changing between validation and fetch — is only applied to ports 80 and 443. Any other port? No pin at all, so curl re-resolves the hostname itself and picks whichever address family it likes.

The validated IP isn’t a rule. It’s a suggestion. And the bouncer takes suggestions from nobody.

## The Proof

Three requests against the production proxy:

```
# Baseline: literal private IP? Blocked. Good bouncer.
GET /?http://127.0.0.1:8080/           → 400 "Private IPs are forbidden"
# Baseline 2: public IPv4 on an internal port — validation covers this
GET /?http://1.1.1.1:3306/probe        → 500 "Failed to connect to 1.1.1.1:3306"
# The bypass: my dual-stack hostname, same port
GET /?http://<redacted>.duckdns.org:3306/probe
                                       → 500 "curl_exec error: Received HTTP/0.9
                                          when not allowed"
```
That last error is the money shot: curl **connected to something non-HTTP on the proxy’s own loopback** — consistent with the internal MySQL the proxy’s rate-limiter uses, at `[::1]:3306`. Connected. Reply received.

## Get Burrito’s stories in your inbox

Join Medium for free to get updates from this writer.

A second probe on port 11211: connection established, silent close. Two internal services reachable with one DNS trick and zero rebinding — the A and AAAA records coexist permanently; no TTL games needed.

And because AAAA could be set to `::ffff:<any IPv4>` (IPv4-mapped IPv6), the proxy turned into a **port scanner for its own internal network** — open, closed, and filtered states were all distinguishable from its error messages:

- AAAA = `::1` → proxy says *"Received HTTP/0.9"* → port **OPEN**, service replied
- AAAA = `::1`, port 49999 → *"Failed to connect after 1003 ms"* → port **CLOSED**
- AAAA = `::ffff:192.0.2.1` → *"Failed to connect after 538 ms"* → dialed the IPv4 **I chose**

That last one is the sneaky one: an otherwise-unreachable IPv4 got dialed *because I asked the proxy to*. Full destination control, one DNS record at a time.

## What a Real Attacker Gets

- **Protocol-speaking access to internal services** — the proxy relays arbitrary methods and bodies, so an attacker can hold conversations with internal daemons
- **A free internal port scanner** with three distinguishable states
- **No authentication, no user interaction** — the attacker fires the requests directly

## The Verdict 💸

“This is a duplicate of an existing report we have already received.”


Duplicate — an earlier report by another researcher, a DNS rebinding bypass of the same pin, submitted **four days** before mine. Different technique (rebinding vs. dual-stack), same root cause.

Four. Days. Earlier.

## Lessons

1. **“It’s always DNS” applies to validations too.** If your security check runs on DNS, it inherits all of DNS — both address families, or it protects half the internet.
2. **Pins must cover the actual port.** Pinning `host:80` and `host:443` while allowing any port is checking the lock on two doors of a thousand-door building.
3. **Read the source. It’s open source. That’s the whole cheat code.** The bouncer’s monolingual brain was sitting in a file, waving.
4. **Speed is a skill.** Someone read the same file and hit submit 96 hours before I did. The bounty wasn’t for finding it — it was for finding it *first*.

## TL;DR

- **Bug:** SSRF — IPv4-only validation (`gethostbynamel`) ignores AAAA records; `CURLOPT_RESOLVE` pin only covers ports 80/443
- **One-liner:** The bouncer only reads the English side of the business card
- **Severity:** Medium
- **Live proof:** Proxy’s own MySQL at `[::1]:3306` reached + built-in internal port-scanning via `::ffff:` mapped IPv4
- **Result:** Duplicate — someone beat me by four days
- **Bounty:** $0
- **Lesson:** It’s always DNS — even when it isn’t DNS rebinding
