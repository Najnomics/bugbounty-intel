# Critical IDOR Chain — Edit Any User’s Role, Activate/Deactivate Accounts, and Escalate Privileges

- **Source URL:** https://medium.com/@abdelrahmanyousef33/critical-idor-chain-edit-any-users-role-activate-deactivate-accounts-and-escalate-privileges-12637b0f2485?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260306113048/https://medium.com/@abdelrahmanyousef33/critical-idor-chain-edit-any-users-role-activate-deactivate-accounts-and-escalate-privileges-12637b0f2485
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10181 (id 10181)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🔓Critical IDOR Chain — Edit Any User’s Role, Activate/Deactivate Accounts, and Escalate Privileges

## Summary:

During a security assessment of Target.com, I discovered a **critical Insecure Direct Object Reference (IDOR)** vulnerability affecting user account management. By manipulating user IDs in privileged API requests, I was able to **edit the roles, capabilities, and activation status of any user, including admin accounts**. This allowed for full **privilege escalation**, including assigning oneself admin-level permissions.

## Attack Process:

First I was analyzing website endpoints using [FindSomething](https://chromewebstore.google.com/detail/kfhniponecokdefffkpagipffdefeldb?utm_source=item-share-cb) extension which is used extract interesting information (e.g., API endpoints, secrets, tokens, environment variables, passwords) from the HTML source code or JS code of the web page.

I usually rely on a this extension to list all JavaScript endpoints, which I then analyze individually to better understand the website’s functionality and potential attack surface.

During my analysis, I came across an interesting JavaScript file that appeared to expose several API endpoints along with their endpoints and parameters. Normally this is like a treasure for each function, method and endpoint.

Two particular snippet caught my attention:

```
async function getUserRoles(userId) {
    let userRolesData;
    await fetchData2(`${baseURL2}/identity-management/user-details/${userId}`, {}, {}, "GET").then(async (response) => {
      userRolesData = await response;
    });
    return userRolesData ? userRolesData.roles : [];
  }
```
This endpoint appeared to return user details and roles based on the provided user ID. Using this, I discovered that user IDs were incremental, starting from 1 by fuzzing, which allowed me to enumerate and retrieve details of all users and their roles.

So this was considered as the first IDOR.

```
const payload = {
      user_id: userId,
      roles_to_be_added: rolesAdded,
      roles_to_be_removed: rolesRemoved,
      status: isActive ? "active" : "disabled"
    };
    try {
      const response = await fetchData2(`${baseURL2}/identity-management/update-user`, {}, {}, "POST", payload);
      const responseData = await response;
      console.log(responseData);
```
Second code appeared to interact with an API endpoint responsible for updating user data. Specifically, it sends a POST request to `/identity-management/update-user` with a payload/body that includes:

- **User ID**
- **User role to add**
- **User role to remove**
- **User account status (active or disabled)**

So next, I needed to determine three key things to proceed:

1. How to obtain valid user IDs.
2. How to identify the role number, since the API only accepted numeric values.
3. Most importantly, whether this request could be performed by **any user** or was restricted **only to admins**.

Eventually, I was able to gather this information through the initial IDOR that exposed user details by fuzzing user IDs until I retrieved the admin’s data, which revealed that the admin role ID is **1** — obviously 😁.

Final request body was as follow:

```
{
  "user_id": My_Account_ID,
  "roles_to_be_added": [1],
  "roles_to_be_removed": [352], //This was just any other role 
  "status": "active"  // This used to activate or deactivate user accounts
}
```
And after sending this request I got 200 status code 😀.

Finally, I logged out and logged back in — and immediately noticed a I have access to admin dashboard!!

This final field (`status`) was particularly interesting, as it allowed not just role management but also **activating or deactivating any user account**, including admin accounts—opening the door to both **privilege escalation** and **account disruption**.

Unfortunately after all this work both IDORS was marked as duplicates.

Thank you so much for reading this. See you in the next write-up! 👋
