# Broken Access Control

- **Source URL:** https://vivek0x.medium.com/broken-access-control-multi-step-admin-role-change-portswigger-lab-walkthrough-6fa5f7672a1c
- **Fetched from:** https://vivek0x.medium.com/broken-access-control-multi-step-admin-role-change-portswigger-lab-walkthrough-6fa5f7672a1c?source=rss-a3d6c85e9637------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14929)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Vivek Yadav / Wed, 30 Sep 2026 18:19:06 GMT

**Lab:** Multi-step process with no access control on one step (Practitioner)

**Category:** Broken Access Control

**Goal:** Log in as wiener:peter and exploit flawed access controls to promote yourself to administrator.

This lab simulates a common real-world mistake: developers assume that because a *sensitive action* is split across multiple steps (like a confirmation step), an attacker can’t easily reach the “dangerous” part without going through the “safe” part first. In reality, if the server doesn’t independently verify permissions at *every* step of a multi-step process, an attacker can skip straight to the step that actually performs the privileged action — bypassing any access control checks that only exist on the earlier steps.

Here’s how I found and exploited that flaw.

I started by clicking **Access the lab**, then logged in with the provided admin credentials, administrator:admin. This let me explore the admin panel and understand the intended workflow before trying to break it.

Inside the panel, I found two actions: **Upgrade user** and **Downgrade user**. To see exactly what happens under the hood, I selected a test target — the user carlos — and clicked **Upgrade**.

With Burp Suite’s proxy running, I intercepted the resulting request and sent it to **Repeater** for closer inspection. The key request was a POST to:

/admin-roles

This confirmed the mechanism: the admin panel doesn’t perform the role change directly from a single click. Instead, it appears to go through a multi-step process — likely a “select action” step followed by a “confirm/execute” step, where /admin-roles is the final step that actually applies the change, based on parameters like username and action.

The critical question in any multi-step process is: **does the server re-check the user’s privileges at every step, or only at the first one?**

Often, developers add an access control check on the *initial* step (e.g., “only admins can see the upgrade/downgrade buttons” or “only admins can reach the confirmation screen”), but forget to enforce the same check on the step that actually performs the sensitive action. If that final endpoint just trusts that “if you got this far, you must be authorized,” it becomes exploitable by anyone who can reach it directly — regardless of role.

Since /admin-roles appeared to be that final, action-performing endpoint, it was the natural target to test.

I logged out of the administrator account and logged back in with the standard low-privileged credentials: wiener:peter.

As wiener, I obviously had no access to the admin panel UI. But that didn't matter — the UI isn't the access control, the server-side check is (or in this case, *isn't*).

I captured a normal authenticated request from this session in Burp Suite to grab wiener’s **session cookie**, and sent it to Repeater as well.

Back in Repeater, I took the original /admin-roles request (captured earlier while logged in as admin, targeting carlos) and made two modifications:

Modified Request Looked Like This —

POST /admin-roles HTTP/2

Host: 0a4d008303cf779f80f57677009200c4.web-security-academy.net

Cookie: session=W3Ro5AAncpdeRVpDhECwqmkNULeudojG

Content-Length: 45

Cache-Control: max-age=0

Sec-Ch-Ua: "Chromium";v="151", "Not=A?Brand";v="99"

Sec-Ch-Ua-Mobile: ?0

Sec-Ch-Ua-Platform: "Windows"

Accept-Language: en-US,en;q=0.9

Upgrade-Insecure-Requests: 1

Content-Type: application/x-www-form-urlencoded

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36

Origin: https://0a4d008303cf779f80f57677009200c4.web-security-academy.net

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7

Sec-Fetch-Site: same-origin

Sec-Fetch-Mode: navigate

Sec-Fetch-User: ?1

Sec-Fetch-Dest: document

Referer: https://0a4d008303cf779f80f57677009200c4.web-security-academy.net/admin-roles

Accept-Encoding: gzip, deflate, br

Priority: u=0, i

action=upgrade&confirmed=true&username=wiener

The server responded with:

HTTP/2 302 Found

Location: /admin

X-Frame-Options: SAMEORIGIN

Content-Length: 0

A 302 redirect here was the tell — it meant the server processed the request successfully instead of rejecting it with a 401 Unauthorized or 403 Forbidden. This confirmed that /admin-roles performs **no independent access control check** of its own; it simply trusts that reaching this step implies authorization, which is exactly the flaw the lab is designed to illustrate.

I refreshed the lab page, and the banner updated to:

**“Congratulations, you solved the lab!”**

wiener had been silently promoted to administrator — without ever touching the admin panel UI.

The vulnerability boils down to a classic **broken access control** pattern in multi-step workflows:

To fix this class of vulnerability, the application should:

GoodByeee…
