# Discovering 3 in a Row

- **Source URL:** https://medium.com/@robert0/discovering-3-in-a-row-bac-read-only-vulnerabilities-total-4-182-59c93b753eb8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250312164602/https://medium.com/@robert0/discovering-3-in-a-row-bac-read-only-vulnerabilities-total-4-182-59c93b753eb8
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8954 (id 8954)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Discovering 3 in a Row: BAC Read-only Vulnerabilities Total $4,182

# **Introduction:**

Hey everyone! I’m excited to share that I recently discovered three security vulnerabilities in a private program on HackerOne, earning rewards totaling $4,182. These vulnerabilities involved user permissions, specifically for “read-only” users.

**Explanation of the Vulnerabilities:**

**The Main Issue:**

\* I found that some application functions were not listed in the permissions list. This meant the company’s permissions system was not set up correctly.

\* From my long experience using the program, I noticed that every function in the application should be in the permissions list to control who can use it.

\* For example, the functions in the “Application Keys” section were included in the permissions list.

**How to Exploit the Vulnerability:**

\* If a function or section is not in the permissions list, it means there are no restrictions on who can use it.

\* In this case, a “read-only” user can try to create things in that section. If the process succeeds, it means there is a security vulnerability.

**Practical Example:**

\* In one of the vulnerabilities, I was able to make a “read-only” user create objects in a newly added section of the application, because this section was not included in the permissions list. And I got a $2,400 as a highest reward.

Also the other two have a similar scenario. And I got a $1000 and $782

**Important Tip:**

\* It is essential to monitor the applications you are testing regularly. Sometimes, new functions are added without updating the permissions list.

Steps to Reproduce:

\* Log in to the application with a “read-only” user account.

\* Look for a new section or function in the application. and check if it included within the permission list and Roles

\* Try to create something new in that section as “read-only” user.

\* If the process succeeds, it means there is a security vulnerability.
