# BAC + CSRF

- **Source URL:** https://medium.com/@rajveer_0101/bac-csrf-bceb26145135?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@rajveer_0101
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14015)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
It was a Self-Hosted program with limited scope, so I started exploring the main application

Exploring the features, understanding the application until I found one interesting feature

### The Feature

Members can invite another user to org using an invitation link

After the user accepts the invitation and joins, they will remain in a pending state until the owner approves them through the verification link sent to the owner’s email

#### **The Misconfiguration**

I copy the token and check the Http History for any leak, I found an api endpoint that return all the invitation token value

Now any member can access this endpoint but only the owner is authorized to approve it. For all other users, it returns → 403

I approve the invitation and observe the request. what? … 😯

It’s a GET method with no CSRF protection

I tested it for CSRF and it turned out to be vulnerable. At this point, I had confirmed a valid vulnerability

but I ask myself can I escalate it and came up with an idea

1. Invite multiple user
2. fetch all user invitation token
3. construct a custom CSRF payload with all the verification url
4. As the owner visit the link it triggers all embedded url’s
5. This way an attacker can leverage CSRF to onboard any no of user within the organization

I document everything and submit the report, and it was accepted and rewarded 💸
