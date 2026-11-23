# Joining the Same Organization Multiple Times Using a Race Condition

- **Source URL:** https://medium.com/@khaledelnabet/joining-the-same-organization-multiple-times-using-a-race-condition-8844d219b769?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250905092701/https://medium.com/@khaledelnabet/joining-the-same-organization-multiple-times-using-a-race-condition-8844d219b769
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10037 (id 10037)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 🐞 Joining the Same Organization Multiple Times Using a Race Condition

In this write-up, I demonstrate how I exploited a **race condition** to join the **same organization multiple times using the same account**, bypassing logic intended to restrict users to a single membership.

**By Khaled Mohamed Elnabet — Bug Hunter & Computer Science Student at Benha University**

## concept:

The platform issues invitation links to allow users to join an organization. Normally, each user can **only join once per invite**, and the system prevents re-use.

However, by **delaying and replaying** the sign-up/join request **in parallel**, I was able to **join multiple times with the same user account**, and later even **modify the joined profiles**.


## 🪜 Steps to Reproduce

### 1. Normal Invite

I sent a normal invite to my own user account.

Once I opened the invite link in the browser, the platform started the join process.


📸 **Screenshot showing a normal invite sent to a user**

### 2. Intercept and Replay Join Request in Parallel

As soon as the **join request** was initiated, I **intercepted it in Burp Suite** using the proxy.

Then, I dropped the request before it was completed and **sent it to a Burp Repeater group**.

I then triggered the same **join/signup request in parallel** (e.g., 10 requests at once) using the same invite link and the same account.


📸 **Screenshot of Burp Repeater sending join request in parallel**

### 3. Joined Multiple Times with Same Account

As a result, the same user account was added to the organization **multiple times**.

The UI confirmed duplicated entries of the same user ID.


📸 **Screenshot showing same account joined multiple times**

### 4. Modify Each Joined Profile Separately

**After joining multiple times, I was able to**:

Change the **email**

Update the **password**

Modify **display names**


Each duplicated instance behaved as a separate logical user within the system — despite all originating from the same base account.

## ⚠️ Why This Is a Race Condition

The system lacks **atomic validation** or locking to ensure a user can **only join once**.

By triggering **multiple concurrent requests**, I bypassed the business logic that should have enforced **unique membership per invite/account**.


### 💥 Impact:

Breaks intended membership constraints

May cause billing anomalies (e.g., charging for extra seats)

Can lead to privilege escalation or permission conflicts

Abused to create fake users under same identity


## 🛠️ Recommendation

### **The backend must:**

Use **locking mechanisms** or **atomic operations** to prevent duplicate joins.

Associate invite links with **single-use tokens** validated server-side.

Track join attempts and block reuse across concurrent sessions.
