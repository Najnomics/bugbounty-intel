# 5000$ |Broken Access Control Let Me Delete Other Users’ Tasklists (ZVE-2025–2842)

- **Source URL:** https://medium.com/@aminefarah802/broken-access-control-let-me-delete-other-users-tasklists-zve-2025-2842-717dced47b0a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250912230632/https://medium.com/@aminefarah802/broken-access-control-let-me-delete-other-users-tasklists-zve-2025-2842-717dced47b0a
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10221 (id 10221)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 5000$ |Broken Access Control Let Me Delete Other Users’ Tasklists (ZVE-2025–2842)

2 min readJul 14, 2025

## Discovering an API Authorization Flaw

During a routine security assessment of target.com, I uncovered a concerning Broken Access Control vulnerability that allowed low-privilege users to delete tasklists belonging to other users. Here’s the full breakdown of my finding.

## Vulnerability Overview

- OWASP Category: Missing Function Level Access Control (A5:2017)
- Severity: Medium
- Bounty: $5000
- CVE: ZVE-2025–2842

## The Vulnerability Breakdown

implements a role-based access control system where:

- Owners have full privileges
- Employees have restricted access

While the UI properly hid the delete functionality from employees, the API endpoint lacked proper authorization checks.

## Technical Details

The vulnerable endpoint:

`DELETE /restapi/portal/[PORTALID]/projects/[PROJECTID]/tasklists/[TASKLISTID]/`
Missing Controls:

1. No verification of tasklist ownership
2. No validation of user role permissions
3. CSRF protection (via X-ZCSRF-TOKEN) was present but didn’t prevent the core authorization flaw

## Step-by-Step Reproduction

1. Setup:

- Create an owner account
- Invite a user with employee role
- Create a tasklist as owner

## Exploitation:

- From employee account, observe delete function is hidden in UI
- Extract tasklist ID from URL when accessing the tasklist
- Craft direct API request:

```
DELETE /restapi/portal/[PORTALID]/projects/[PROJECTID]/tasklists/[TASKLISTID]/
Host: xxxx.xxx.com
X-ZCSRF-TOKEN: [valid_token]
Cookie: [session_cookies]
```
1. Result:

- 200 OK response
- Tasklist successfully deleted despite employee privileges

## The Impact

This vulnerability could have allowed:

- Disruption of project workflows
- Potential data loss
- Escalation of privileges through indirect means
- Damage to organizational trust in the platform
