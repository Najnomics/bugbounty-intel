# Privilege Escalation via Response Manipulation

- **Source URL:** https://medium.com/@HBlackGhost/privilege-escalation-via-response-manipulation-1bdb829c8748?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250821171005/https://medium.com/@HBlackGhost/privilege-escalation-via-response-manipulation-1bdb829c8748
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10177 (id 10177)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Privilege Escalation via Response Manipulation

(وَقُل رَّبِّ زِدْنِي عِلْمًا) (طه: 114)

نَحمدك على عطاءك مرة وعلى منعك ألف مرة فأنت الخير وما مَنعت خيرًا.

**Hello, I’m Ahmed Alaa Ghazala!**

I’m a **Bug Hunter** and **Penetration Tester**, and I’m excited to share my **first bug** with you. Let’s dive in and break things down — the right way.

While I was hunting on a target let’s call it **example.comcollaborative workspace platform for web developers**. The application allows users to create, share, and modify websites depending on their assigned **role** within a project.

role in this program

```
Admin
Has full privileges across the platform, including user management, settings access, and site configuration.
Site Manager / Owner
Can modify all website settings, publish content, and manage collaborators within the workspace.
Reviewer
Has view-only access. They can see the site but cannot modify any part of it.
```
To begin my testing, I set up my environment and started diving into the target application.

I created **two accounts** for simulation:

- **Account A** → Assigned the role of **Site Manager / Owner**
- **Account B** → Assigned the role of **Reviewer**

Once both accounts were created, I used **Account A** to invite **Account B** to its workspace.

By default, **Account B** can only see the website and has no access to any workspace information.

After spending several hours exploring the application and understanding its functionality, I returned to **Burp Suite** and started digging deeper into the **HTTP history** — analyzing the **requests and responses** more closely.

Boom! I saw this response With this Value.

I quickly went to Match and Replace in Burp Suite and changed this value to that one.

Then I refreshed the page — boom! I got this juicy message: I became an admin.

After that, I was able to access all the information of the organization I was part of (even though I was just a Reviewer) and view all its settings.

ابلللللع 💻🔥

والسلام عليكم ورحمه الله وبركاته
