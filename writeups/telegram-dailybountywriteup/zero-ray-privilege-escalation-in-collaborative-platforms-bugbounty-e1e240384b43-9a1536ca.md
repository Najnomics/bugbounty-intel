# Privilege Escalation in Collaborative Platforms — BugBounty

- **Source URL:** https://medium.com/@Zero-Ray/privilege-escalation-in-collaborative-platforms-bugbounty-e1e240384b43?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250225230827/https://medium.com/@Zero-Ray/privilege-escalation-in-collaborative-platforms-bugbounty-e1e240384b43
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7967 (id 7967)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Privilege Escalation in Collaborative Platforms — BugBounty

بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ وبه نستعين والصلاة والسلام على اشرف الانبياء والمرسلين سيدنا محمد صلى اللًّه عليه وسلم اللهم ارزقنا مع العلم تقوى تعصمنا من السيئات وتعيننا على الطاعات

اللهم انصر اخواننا المستضعفين في كل بقاع الأرض واجمع شمل المسلمين ووحدهم على كلمه الحق والدين

# Introduction

we discuss a critical privilege escalation vulnerability identified in a widely-used collaborative platform. This vulnerability allows attackers to retain elevated permissions even after their privileges have been downgraded, presenting a significant security risk.

Through this detailed writeup, we’ll explore the vulnerability, its exploitation, and its implications, followed by recommendations to mitigate such risks.

# Vulnerability Overview

The issue lies in how session tokens are handled in relation to user roles. When a user’s role is downgraded, their session tokens are not invalidated, enabling attackers to reuse previously captured tokens to perform unauthorized actions. This opens up a path for privilege escalation, where attackers can maintain administrative control or carry out restricted actions even after their roles have been limited.

# Impact

The exploitation of this vulnerability enables attackers to:

- Retain administrative privileges on boards or projects.
- Modify or delete sensitive data or settings.
- Remove legitimate administrators from the platform.
- Disable or disrupt organizational workflows.

# Steps to Reproduce

# Prerequisites

1. **Victim Account (Admin):** This account will be used to set up a workspace and grant administrative privileges.
2. **Attacker Account (Member):** A secondary account with initially limited permissions but elevated to Admin temporarily during the setup.

# Phase 1: Setup and Preparation

**Victim Account Setup:**

- Create an account and log in as an Admin user.
- Set up a workspace or organization and invite the attacker to join.
- Navigate to the workspace’s member management page.
- Temporarily grant Admin privileges to the attacker.

**Board Creation:**

- From the Victim account, create a new board within the workspace.
- Share this board with the attacker, granting them administrative permissions.

# Phase 2: Capturing the Session

Using tools such as **Burp Suite**, intercept and analyze HTTP requests made during actions involving administrative permissions. Focus on requests related to modifying user roles or permissions.

# Capturing a “Delete Admin” Request:

1. Identify the request responsible for removing an Admin from the board. This typically involves:

- HTTP `DELETE` method targeting an endpoint for member management.
- Session tokens or cookies validating the user’s identity and permissions.
- Relevant headers and payloads specifying the target user and board.

Example intercepted request:

```
DELETE /1/Board/<board_id>/members/<member_id> HTTP/2
Host: platform.example.com
Cookie: session.token=***
Content-Type: application/json
...
{
    "dsc": "*************"
}
```
# Phase 3: Exploitation

**Role Downgrade:**

- The Victim downgrades the Attacker from Admin to Member and updates board settings to restrict actions to Admin-only users.

**Replaying the Captured Request:**

- Using the previously captured `DELETE` request, the attacker replaces the old session token with a valid session token from their current login.
- Resend the modified request using a tool like Burp Suite.

**Outcome:**

- Despite being downgraded, the request successfully executes with a `200 OK` response.
- The attacker remains capable of performing actions reserved for Admins, such as removing other users or even deleting the board.

# Technical Analysis

# Root Cause

**Session Token Persistence:**

- Session tokens are not invalidated when a user’s permissions change. This allows attackers to reuse previously issued tokens tied to higher privileges.

**Insufficient Role Verification:**

- The platform relies on session tokens for authentication but does not adequately verify the user’s current role when processing requests.

واخيرالحمداللَّه الذي وفقنا

Our LinkedIn account for any questions :-

Mahmoud Fawzy :-[https://www.linkedin.com/in/mahm0ud-fawzy/](https://www.linkedin.com/in/mahm0ud-fawzy/)

Alamin Alaa:-[https://www.linkedin.com/in/alaminalaa8/](https://www.linkedin.com/in/alaminalaa8/)
