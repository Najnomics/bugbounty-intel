# Unauthorized Access to Enterprise Policies Management

- **Source URL:** https://medium.com/@a13h1/unauthorized-access-to-enterprise-policies-management-500-bac-bug-60f04419fed4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251103012630/https://medium.com/@a13h1/unauthorized-access-to-enterprise-policies-management-500-bac-bug-60f04419fed4
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/11306 (id 11306)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Member-only story

# Unauthorized Access to Enterprise Policies Management: $500 BAC Bug

During beta testing of the **Policies Management** feature in CodeCollabHub, I discovered a **Broken Access Control (BAC)** vulnerability. Despite the official documentation stating that only **admins** should be able to create and manage policies, I was able to **view, edit, and delete organization-wide policies as a non-admin user**.

For this report, I received a **$500 bounty**.

## Understanding the Target

CodeCollabHub is a cloud-based collaboration platform that provides secure project hosting, package management, and organizational controls.

The **Policies Management feature** is designed to enforce:

- Package usage restrictions (e.g., only MIT-licensed dependencies).
- Repository access rules.
- Security compliance across projects.

According to official documentation, **only administrators** are allowed to create, edit, or delete these policies. Regular project members (like developers or contributors) should only be able to view policies relevant to their projects.

However, while exploring the application, I noticed there was **no visible “create policy” option in the UI** for my non-admin test account. That’s when I switched gears and decided…
