# Finding Broken Access Control in Multi-Tenant Systems

- **Source URL:** https://medium.com/@afi0pchik/finding-broken-access-control-in-multi-tenant-systems-2fa95ee0dfa6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251230183929/https://medium.com/@afi0pchik/finding-broken-access-control-in-multi-tenant-systems-2fa95ee0dfa6
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/12344 (id 12344)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Finding Broken Access Control in Multi-Tenant Systems

Hi everyone 👏

In this article, I want to share my practical experience and mindset for finding **Broken Access Control vulnerabilities in multi-tenant systems**.

You will learn how to approach and identify real-world **Auth Bypass**, **BOLA**, and **BFLA** issues — and, more importantly, how to start finding them yourself.

## What Is a Multi-Tenant System?

A **multi-tenant system** is an architecture where a single instance of an application or service serves multiple customers (tenants).

Each tenant usually has:

- its own users
- its own data
- its own permissions

But all of this lives inside the **same application, same codebase, and often the same database**. This is exactly why access control bugs are so common here.

## Start With the Right Questions

When hunting for Broken Access Control in multi-tenant environments, you should constantly ask yourself:

- Where does the system trust the user too much?
- Where does the backend blindly accept user-controlled values?
- Where is the boundary between *my tenant* and *someone else’s tenant* — and how can it be crossed?

Most critical bugs appear when this boundary exists **only logically**, not technically.

## Common Vulnerability Types in Multi-Tenant Systems

From real-world experience, these issues appear again and again:

- **Broken Access Control**
- **BOLA / BFLA (Broken Object / Function Level Authorization)**
- **Race Conditions**

Often, these bugs are not “complex” — they are the result of **missing or inconsistent checks**.

## How to Hunt in Practice

Start by using the application normally.

Then open **Burp Suite** and carefully analyze the traffic.

The **Target** tab is especially useful for mapping endpoints and understanding how data flows.

Pay close attention to parameters like:

- `id`
- `user_id`
- `user`
- `org_id`
- `workspace_id`
- `shard_id`
- `url`

Any identifier is a potential access control boundary.

Also check for:

- `isAdmin` flags
- role-related parameters
- Role-Based Access Control patterns(role:user\_id, admin:12345)

## My Real-World Case

In real life, multi-tenant vulnerabilities are often **absurdly simple** — and that was the case here.

The issue was that the backend trusted a `user_id` parameter too much.

Instead of providing a valid `user_id`, I replaced it with an **org\_id belonging to another organization**.

The backend did not validate:

- whether the ID belonged to the authenticated user
- whether it belonged to the same tenant

As a result, I was able to retrieve **data from another organization**.

## Conclusion

Multi-tenant systems are extremely powerful — and extremely fragile when it comes to access control.

If you:

- think in tenants, not just users
- question every ID parameter
- look for trust boundaries

you will consistently find impactful vulnerabilities.

That’s all for this article.

If you found it useful, I’d really appreciate a clap 👏

Good luck hunting — and happy hacking :D
