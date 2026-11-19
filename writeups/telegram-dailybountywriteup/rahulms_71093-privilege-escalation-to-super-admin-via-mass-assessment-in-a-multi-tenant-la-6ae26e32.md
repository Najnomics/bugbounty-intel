# Privilege Escalation to Super Admin via Mass Assessment in a Multi-Tenant Laravel App

- **Source URL:** https://medium.com/@rahulms_71093/privilege-escalation-to-super-admin-via-mass-assessment-in-a-multi-tenant-laravel-app-526d1309de73?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250821171152/https://medium.com/@rahulms_71093/privilege-escalation-to-super-admin-via-mass-assessment-in-a-multi-tenant-laravel-app-526d1309de73
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9530 (id 9530)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Privilege Escalation to Super Admin via Mass Assessment in a Multi-Tenant Laravel App

*They say the best exploits aren’t zero-days they’re the ones hiding in plain sight, quietly ignored by developers who assume their front-end UI logic is enough to hold back a determined adversary.*

This was one of those cases. A multi-tenant SaaS product built on Laravel, featuring RESTful APIs, token-based authentication, and a role-based access model spanning:

• GeneralUser

• CompanyAdmin

• BusinessAdmin

• SuperAdmin

My session token belonged to a GeneralUser the lowest rung on the hierarchy. Access was expected to be read only, restricted to their own company’s resources. But access control was implemented in fragments: some logic in the middleware, some in Laravel policies, and shockingly some purely in the frontend JavaScript.

*Yes. Let that sink in.*

Phase 1: Reconnaissance & Route Pattern Inference

A quick static and dynamic recon of the application yielded endpoint schemas like

```
/api/company/{company_id}/users  
/api/company/{company_id}/reports  
/api/user/{user_id}/profile  
```
The URLs suggested predictable routing, and since Laravel uses route model binding, I hypothesized that backend lookups were tied directly to ID parameters. I began capturing requests in Burp Suite and quickly noticed a recurring anti-pattern:

The server responded to unauthorized ID changes with 200 OK – no RBAC validation, no object ownership checks.

Phase 2: Automated Mass Assessment

To operationalize the discovery, I crafted a multi-threaded Python tool using requests, concurrent.futures, and Burp exports. The goal was to perform mass-assessment-based fuzzing on multiple combinations of company\_id, user\_id, and role\_id against all known endpoints.

Within minutes of execution

• Company 42’s invoice data was fetched while authenticated as a user from Company 19.

• Profiles of Admin users were accessible by enumerating /user/{id}/profile.

• /admin/ and even /super-admin/ endpoints began responding with 200 OKs instead of 403s.

I paused. Took a breath. Checked my logs.

I was crawling across privilege boundaries – horizontally, vertically, and diagonally.

Phase 3: Targeted Role Manipulation

Then I found the goldmine

```
POST /api/users/assign-role  
Content-Type: application/json  
Authorization: Bearer <user-token>
```
Payload

```
{
  "user_id": 1058,
  "role": "SuperAdmin"
}
```
Despite originating from a low-privileged account, the request succeeded. There was no role verification, no server-side ACL binding, and no action logging in the response headers. I refreshed the dashboard and saw new modules:

• AuditTrailManager

• GlobalCompanyOverview

• SecurityPolicyHandler

I had assumed SuperAdmin context within two HTTP requests – no injection, no exploits, just logic flaws.

Phase 4: Impact Expansion Through Post-Escalation Enumeration

Post-escalation, I initiated another enumeration sweep to assess the expanded blast radius:

• Queried /api/super-admin/audit-logs to fetch system-wide activity logs.

• Used /api/super-admin/companies to extract metadata of all tenants in the SaaS environment.

• Accessed /api/super-admin/users/create to spin up backdoor users with high privileges.

• Inspected /env and debug mode routes to confirm production misconfigurations.

I had effectively compromised the entire system across vertical and horizontal boundaries – and no alerts had been triggered.

*When the SIEM sees nothing and you’re creating Super Admins on a Monday morning*

Root Cause Analysis – Developer Oversights in Role Context Validation

Upon decompiling the frontend JS bundle and examining the route guards, I confirmed that the client was trusted to hide admin routes from non-privileged users. Role-based feature gating was entirely UI-dependent, relying on flags passed from the initial /me response.

The backend had no consistent implementation of:

• Per-object access validation (OLAC)

• Scoped token validation

• Authorization policies tied to context hierarchy (Company → User → Role)

Most dangerously, critical endpoints accepted arbitrary role values without cross-checking issuer context or privilege level – a fatal flaw in multi-tenant SaaS environments.

Final Thoughts – A Logical Exploitation Masterclass

This wasn’t about CVEs. It wasn’t about zero-days. It was about chained business logic failures that led to complete system compromise.

Using mass assessment, role fuzzing, and ID manipulation, I:

• Enumerated and accessed unauthorized tenants

• Performed horizontal privilege abuse across user accounts

• Escalated vertically to Super Admin via insecure role assignment APIs

• Maintained persistence using newly created high-privileged accounts

All without tripping a single firewall rule, rate limit, or SIEM alert.

*Sometimes, the loudest hacks are the quietest ones.*

*Still think access control is just a dev thing? Think again :)*
