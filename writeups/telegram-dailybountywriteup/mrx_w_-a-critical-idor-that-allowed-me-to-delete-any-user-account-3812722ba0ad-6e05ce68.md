# A Critical IDOR That Allowed Me to Delete Any User Account

- **Source URL:** https://medium.com/@mrx_w_/a-critical-idor-that-allowed-me-to-delete-any-user-account-3812722ba0ad?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260713193621/https://medium.com/@mrx_w_/a-critical-idor-that-allowed-me-to-delete-any-user-account-3812722ba0ad
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13506 (id 13506)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# A Critical IDOR That Allowed Me to Delete Any User Account

Hi, I’m mrx\_w\_ (Adem Ziane Berroudja), a bug bounty hunter on Bugcrowd. You can find me on [Twitter](https://x.com/MrxXb12) and [LinkedIn](https://www.linkedin.com/in/adem-ziane-berroudja-499628253/) under mrx\_w\_. In this write-up, I’ll share how I discovered a critical IDOR vulnerability that allowed arbitrary user deletion by manipulating a simple numeric ID in the application.

Our target was a private program on Bugcrowd with a wildcard scope of `*.redacted.com`.

When working with wildcard scopes, I usually start with subdomain discovery to map the target’s attack surface. For this, I rely on a mix of tools like [Subfinder](https://github.com/projectdiscovery/subfinder), [Amass](https://github.com/owasp-amass/amass), Google dorking, and [SecurityTrails](https://securitytrails.com/).

Once I gather a list of subdomains, I filter out the live ones and begin testing them individually to identify any interesting entry points or misconfigurations.

During this process, I came across the following subdomain:

`business.redacted.com`

Unlike the other assets I tested, this one exposed a public registration feature. After creating an account and exploring the application, it became clear that the platform was designed for employee and business account management.

After spending some time exploring the application, I decided to focus on the user management functionality since these areas often contain interesting authorization issues.

I started testing basic scenarios such as editing and deleting users through IDOR-style attacks, but the application appeared to handle them correctly and consistently returned `Errors` responses.

After exploring the application further, I noticed something interesting in the user deletion workflow.

The application was using two completely different requests depending on where the deletion action was triggered from.

When deleting a user directly from the main user management page, the application sent the following request:

`POST /business/Portal/bulkPeopleDelete`
However, when opening a user profile and deleting the user from there, the application used a different endpoint:

`POST /business/Portal/bulkPeopleUpdate`
Unlike the first endpoint, this one turned out to be vulnerable to an IDOR issue. By simply modifying the numeric user ID in the request, I was able to delete users belonging to other accounts without any authorization checks or validation in place.

I reported the issue to the security team with a complete proof of concept and reproduction steps. After review, the vulnerability was successfully triaged and classified as a critical severity issue.
