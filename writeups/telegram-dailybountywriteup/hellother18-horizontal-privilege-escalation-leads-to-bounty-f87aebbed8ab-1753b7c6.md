# Horizontal Privilege Escalation Leads to Bounty

- **Source URL:** https://medium.com/@hellother18/horizontal-privilege-escalation-leads-to-bounty-f87aebbed8ab?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240307212018/https://medium.com/@hellother18/horizontal-privilege-escalation-leads-to-bounty-f87aebbed8ab
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5428 (id 5428)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Horizontal Privilege Escalation Leads to Bounty

Hey there, fellow Hackers! Today, I’ve got an exciting story to share about an interesting bug I found in a tool lots of folks use for managing projects. But shh, let’s keep it a secret which tool it is, so let’s dive in!

**The Bug :**

Alright, so the bug was Privilege escalation. It is when someone tricks a server into giving them more access or power than they’re supposed to have. It’s like finding a secret backdoor that lets you into places you shouldn’t be allowed to go.

**How I Found It :** Now, how did I stumble upon this bug? Well, I was just doing my usual bug hunting routine when I came across a problem with how this tool handles project sharing. It was like finding a hidden treasure, except instead of gold, it was a bug waiting to be fixed.

**Why It’s a Big Deal:** So, why should you care about this bug? Let me break it down. Imagine you’re using this tool to keep track of super secret projects. You’ve got all sorts of important stuff in there — client info, project plans, you name it. Now, picture someone sneaky getting access to all that stuff they’re not supposed to. Scary, right? That’s the kind of chaos this bug could cause.

**Steps to Reproduce:**

1. **Login with Limited Access:** Log in to your account, where you have restricted access to some projects owned by another user. Make sure the owner has multiple projects (e.g., three projects) and you only have access to one of them.
2. **Capture Project Sharing Request:** Go to the “Invite New Member” section or any feature that allows sharing project which is shared with you by owner. Use a proxy tool like Burp Suite to intercept and capture the request sent when sharing project access with a new member.
3. **Modify Request Parameters:** In the captured request, find the “project\_ids” parameter, which lists the projects to be shared. Replace the project ID in the “project\_ids” parameter with the ID of a project that you do not have access to (e.g., change “project\_ids”:\[2\] to the ID of a restricted project).
4. **Forward the Request:** Send the modified request back to the server.

Reward with **$100** : )

**Conclusion:** Alright, there you have it — a glimpse into the world of bug hunting and the rush of finding hidden problems. As bug hunters, it’s up to us to shine a light on these bugs and help keep the digital world safe. But remember, with great power comes great responsibility. So, let’s keep hunting, keep fixing bugs, and keep things safe for everyone.

**Well if you love this write up drop a clap 👏**

Thanks for reading !!
