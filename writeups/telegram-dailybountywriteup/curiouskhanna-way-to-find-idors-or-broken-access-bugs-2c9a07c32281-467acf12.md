# Way to find IDORs or Broken access bugs

- **Source URL:** https://medium.com/@curiouskhanna/way-to-find-idors-or-broken-access-bugs-2c9a07c32281?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250128002817/https://medium.com/@curiouskhanna/way-to-find-idors-or-broken-access-bugs-2c9a07c32281
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8614 (id 8614)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Way to find IDORs or Broken access bugs

Access control bugs and Insecure Direct Object References (IDORs) are some of the easiest vulnerabilities for beginners to understand and exploit. They don’t require advanced technical skills but rely on logic and careful observation. Let’s break them down in simple terms to get you started.

# What Are Access Control Bugs?

Imagine a lock and key system where only certain people have the key to open a specific lock. Access control ensures that only the right people can unlock and access certain resources.

When access control breaks, it’s like being able to open the lock without a key. Essentially, the system doesn’t properly verify if you’re allowed to access something. This is where bugs like IDORs come into play.

# Types of Access Control

There are three main types of access control:

# 1. Role-Based Access Control (RBAC)

In this system, users are assigned roles, and each role comes with specific permissions. For instance:

- If you have a YouTube channel, you can assign someone the role of an editor or a moderator.
- An editor can upload and edit videos, while a moderator can manage comments.

This ensures that users can only perform actions relevant to their assigned roles.

# 2. Discretionary Access Control (DAC)

This is like sharing a file from your cloud storage with specific people. Here, permissions are granted at the discretion of the owner. For example:

- You share a document with someone using a special link.
- However, if the link settings aren’t properly configured, unauthorized users could still access it.

This kind of access control can be tricky because mistakes in sharing settings can lead to vulnerabilities.

# 3. Attribute-Based Access Control (ABAC)

ABAC is less common in web applications but combines elements of RBAC and DAC. Permissions are assigned based on a list of attributes. For example:

- You might allow a user to add captions to a video but not delete it.

While ABAC is flexible, it can quickly become complex and challenging to manage. The real question is: *What should a user be allowed to do?*

# Spotting Access Control Bugs

Access control vulnerabilities often show up in APIs (Application Programming Interfaces). APIs handle requests for resources like files or data, and if developers make mistakes, these bugs can slip through.

Here are some key types of access control issues:

# 1. Broken Object Level Authorization (BOLA)

- A user can access an object (like a file or record) owned by someone else.

# 2. Broken Function Level Authorization

- A regular user gains access to admin-level functions.

# 3. Missing Access Control

- A user can access resources without even logging in.

# 4. Cross-Tenant Access

- In multi-tenant systems (where multiple organizations use the same software), a user from one organization can access data from another organization.

# What Are IDORs?

IDORs are a type of broken access control. They occur when an application doesn’t verify if the user requesting a resource owns it. Here’s an example:

1. A user (let’s call him Blue) requests access to file ID 1000. The system checks and confirms that Blue owns this file, so it grants access.
2. Blue changes the file ID in the request to 1002, which belongs to another user (Green).
3. If the system doesn’t check ownership again, it will allow Blue to access Green’s file. This is an IDOR.

# Why IDs Are Important

Most websites rely on databases with IDs to organize data. For example:

- **Primary Key:** Uniquely identifies a record (e.g., User ID or File ID).
- **Foreign Key:** Links records across tables (e.g., linking a product to its category).

When testing for vulnerabilities:

- Look for IDs in URLs, API endpoints, or hidden fields in forms.
- Check if changing an ID grants access to unauthorized data.

# Protecting Against IDORs

Using unpredictable IDs like UUIDs (randomly generated identifiers) can help mitigate IDORs. However, this doesn’t entirely solve the problem. If the system doesn’t check permissions, the vulnerability still exists.

# Testing for Access Control Bugs

Here are some steps you can take:

1. **Log Out:** Can you still access resources while logged out?
2. **Switch Accounts:** Can you access resources belonging to another user?
3. **Test Admin Functions:** Can a regular user perform admin-level actions?
4. **Check Multi-Tenancy:** Can a user from one organization access another organization’s resources?

# Why Beginners Should Focus on These Bugs

Access control bugs are a great starting point because they rely more on logical thinking than technical expertise. Finding them requires patience and attention to detail, especially when testing APIs and exploring how data is accessed and managed.

By understanding access control and IDORs, you’ll not only develop critical skills as a security researcher but also make a real impact by identifying vulnerabilities that protect users and organizations from potential threats. Happy hunting!
