# Privilege Escalation to Admin through an Import Feature

- **Source URL:** https://cristivlad.medium.com/privilege-escalation-to-admin-through-an-import-feature-ac8ac6b6abad?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251118104019/https://cristivlad.medium.com/privilege-escalation-to-admin-through-an-import-feature-ac8ac6b6abad
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5945 (id 5945)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Privilege Escalation to Admin through an Import Feature

I usually skip the introduction when posting a writeup because I don’t need to teach you what privesc or BOLA are, you can google that yourself.

I was pentesting a web app for a client recently. This was a learning-oriented app with multiple roles, two relevant ones being `admin`and `student`.

As you might guess, the admin has full access, while the student has limited access. One of the features in the admin panel allows the admin to conveniently import users by CSV (in the required format — for which you are given a sample CSV file).

1\. As an `admin`, I added a user through this import feature, I intercepted the request, and replaced the admin session token with that of the student. The import was successful and the new user has been invited to the platform.

- This means that we have a BOLA/IDOR issue for the very least.

2\. What I did next was to look closer at the parameters of the problematic request, which let me learn of a parameter `willUpdate` that was set to true. That led me to think this parameter could be used to update existing users through the same CSV import feature. A user would be updated if the `email` parameter was set to a value (email) that already existed on the platform.

3\. Thus, as `student` I repeated the request, using my registered email and setting the `role` parameter to “admin”. See the top screenshot.

4\. Refreshing my student dashboard, a whole host of admin features popped up. Hence, I upgraded myself to `admin` .
