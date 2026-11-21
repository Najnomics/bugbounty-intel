# Full Privilege Escalation from Agent to Admin Leads to Team Takeover

- **Source URL:** https://medium.com/@abdelrahman0x01/full-privilege-escalation-from-agent-to-admin-leads-to-team-takeover-2819507af2f1?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20241008181309/https://medium.com/@abdelrahman0x01/full-privilege-escalation-from-agent-to-admin-leads-to-team-takeover-2819507af2f1
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7472 (id 7472)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Full Privilege Escalation from Agent to Admin Leads to Team Takeover

## Description

During a pentesting engagement at [CyberAR](https://cyberar.io/), I discovered a privilege escalation vulnerability that allowed low-privilege users to escalate their privileges and take over any team.

## Exploit Begins

While exploring the website, I examined the teammate section and found that I could invite any person to my team. The platform offers three roles team admin, agent, and operator and super admin (reserved for team owners).

I focused on testing the invitation process, to identify potential security flaws,

As part of my testing, I invited a user to my team as an agent.

While intercepting the HTTP request using a proxy tool like burb suite, I noticed the request had a parameter named roleType with the value set to 2, which corresponds to the agent role.

To test privilege escalation, I modified the roleType parameter in the intercepted request, changing its value from 2 to 1

and I observed that the user role was successfully changed from agent to admin, effectively granting admin privileges without any checks or validation by the server

During further investigation, I noticed the request also contained an applicationId parameter, which identified the specific team. To test the boundaries of this parameter, I changed the applicationId to that of another team. and updating the roleType to 1 (admin) for this new team and resending the request, I successfully take over the other team with admin privileges., demonstrating a clear path to take over any team on the platform.

Lastly, I discovered that even after a super admin deleted an admin from the team, I could still access the team without needing a new invitation. This was possible because the invitation did not expire, allowing me to use the same invitation multiple times to regain access, even after being removed.

## **Summary:**

The vulnerability discovered allowed for privilege escalation from agent to admin by manipulating the roleType parameter. Additionally, changing the applicationId parameter enabled taking over other teams with admin privileges. Even after being removed from the team, users could still access the team due to an expired invitation flaw. This exploit can lead to a complete team takeover.

*Thanks for reading.*
