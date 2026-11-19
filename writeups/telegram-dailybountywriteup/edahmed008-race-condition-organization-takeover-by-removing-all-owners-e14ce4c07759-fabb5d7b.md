# Race Condition → Organization Takeover by Removing All Owners

- **Source URL:** https://medium.com/@edahmed008/race-condition-organization-takeover-by-removing-all-owners-e14ce4c07759?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260430151806/https://medium.com/@edahmed008/race-condition-organization-takeover-by-removing-all-owners-e14ce4c07759
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13431 (id 13431)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Race Condition → Organization Takeover by Removing All Owners**

“سُبْحَانَكَ لا عِلْمَ لَنَا إِلَّا مَا عَلَّمْتَنَا إِنَّكَ أَنْتَ الْعَلِيمُ الْحَكِيمُ”

Hi, I’m Ahmed Mahmoud, I work as a penetration tester, today I will show you how I was able to remove all Owners from an organization by exploiting a race condition vulnerability… So let’s get started.

## Overview of the Vulnerability:

The application enforces a rule to ensure that at least one Owner always exists in the organization. However, this protection is not safe against concurrent requests.

By exploiting a race condition, I was able to bypass this validation and remove all Owners at the same time, leaving the organization without any Owner.

## Scenario:

At first, I tested common scenarios like:

- Privilege escalation
- Manipulating role IDs
- Direct role modification

But nothing worked… and honestly, it was a bit frustrating.

But I didn’t give up… I started thinking differently.

*What if the issue is not in the logic itself… but in the timing?*


## Steps To Reproduce:

1. Create an organization with :
At least**two users with Owner role**
One user with **Admin role**

2\. Log in using the **Admin account**

Normally:

- Admin **cannot remove the last Owner**
- The system prevents breaking this rule

3\. *As an Admin, I intercepted the deletion requests for both Owners and sent them to Repeater..*

Capture the request using a proxy (like Burp Suite).

4\. Add two requests in a group.

5\. Send both requests at the same time (Single-Packet Attack)

Here’s the trick:

Instead of sending requests one by one, send them **concurrently**.

6\. Result: Both Owners are deleted successfully.

Organization now has **zero Owners.**

7\. Try to assign a new Owner as Admin

You will notice:

- Admin **cannot assign new Owners**
- Ownership is **not recoverable**

### Impact:

### Ownership Loss:

The system allows an organization to exist without any Owner, violating core access control rules.

### Unauthorized Takeover Risk:

An Admin can remove all Owners and gain **uncontested control** over the organization.

### Admin cannot restore ownership once all Owners are removed.

## Suggested Remediation:

To fix this issue, the application should:

- Enforce **validation** when removing Owners
- Prevent deletion if it results in **zero Owners**, even under concurrent execution
- Implement stricter **role hierarchy rules** (e.g., only Owners can manage Owners)

## Final Thoughts:

This bug shows how **race conditions** can completely break business logic, even when proper validation exists.

Sometimes the issue is not *what* the system checks…

but *when* it checks it.

**Thanks for reading!!**
