# Bypassing the Group Member Limit via Race Condition

- **Source URL:** https://medium.com/@khaledelnabet/bypassing-the-group-member-limit-via-race-condition-2442ad33739e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250906075929/https://medium.com/@khaledelnabet/bypassing-the-group-member-limit-via-race-condition-2442ad33739e
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10035 (id 10035)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bypassing the Group Member Limit via Race Condition

## In this write-up, I demonstrate how I was able to bypass the 100-member limit in a group by exploiting a race condition, using parallel requests through Burp Suite.

### By Khaled Mohamed Elnabet — Bug Hunter & Computer Science Student at Benha University

### 1. **Normal Invite Attempt After 100 Users**

*When trying to invite a user after the group has reached 100 members, the system returns an error stating the maximum number has been reached.*

📸 **Screenshot showing the error when trying to exceed the limit**

### 2. Drop to 99 Members, Then Trigger Parallel Invites

I removed one user, bringing the group down to 99 members.

Next, I used Burp Suite Repeater to create a group of requests targeting multiple user IDs (e.g., user100, user101, user102, etc.).

I sent these requests in parallel at the exact same time.


📸 **Screenshot of Burp Repeater showing the prepared parallel requests**

### 2. Group Ends Up with More Than 100 Members

All the parallel requests were accepted, and the users were successfully invited.

As a result, the group now contains more than 100 members, which violates the platform’s logic.


📸 Screenshot showing the final group with over 100 members

### 💥 Impact

Bypasses business logic for group size limitation.

Can lead to abuse scenarios such as spamming or flooding groups.

Might cause performance issues, unexpected UI behavior, or resource overuse.


### 🛠️ Recommendation

The backend should implement atomic checks or proper locking mechanisms to validate the number of users before accepting new invites — especially when requests are made in parallel.
