# Privilege Escalation, worth of €300

- **Source URL:** https://medium.com/@kashyapherry147/privilege-escalation-worth-of-300-b9a6eac3b0fa?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142239/https://medium.com/@kashyapherry147/privilege-escalation-worth-of-300-b9a6eac3b0fa
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1987 (id 1987)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Privilege Escalation, worth of €300

Hi folks, Hemant here. Today i’m going to tell you about one of my finding. Which is Privilege Escalation to demote the owner of the organization. **About target type**: I was hunting on multiple roles website. Websites has many user roles like: Owner, Managed Owner, Store owner, and integrator.

**Let’s start the story**

So, I created an account with owner privileges. And i invited a user with Store owner permission. Store owner doesn’t have access to demote the Owner, but he/she can demote lower privilege users like, Integrator, store manager. Then i logged into the store owner account, and playing with the functionality. So, i invited a user with permission of store read access from store owner account, and then i edited permission to integrator, and i captured this request in burpsuite. Request is like this:

You can see the request line.

POST /api/v1.0/fd25374/teammates/Base64-encoded-email-address|team-id. So, i decoded this base64 email address. And i found that, this email is belongs to invited user ( Store read access user email). So, i encoded owner email and team-id with base64. And replace with store read access user. And then **request look like this:**

POST /api/v1.0/fd25374/teammates/**ZmQyNTM3NHx0ZWthdDk4ODc3QGZzb3VkYS5jb20=**

And send the request, and i got 200 OK.It’s mean Owner is demoted succesfully. Also i checked in browser, and is successfully demoted.

I reported this vulnerability, and i rewarded with 300 Euros.

Linkedin: [https://www.linkedin.com/in/hemant-k-714564199/](https://www.linkedin.com/in/hemant-k-714564199/)

Instagram: [https://www.instagram.com/cyber\_\_hawk/](https://www.instagram.com/cyber__hawk/)
