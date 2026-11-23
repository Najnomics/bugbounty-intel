# Chaining bugs for Account Takeover

- **Source URL:** https://medium.com/@hbenja47/chaining-bugs-for-account-takeover-0b90a2d952af?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240624002128/https://medium.com/@hbenja47/chaining-bugs-for-account-takeover-0b90a2d952af
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6492 (id 6492)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 😎 Chaining bugs for Account Takeover

I’m going to share with you my second account takeover for which I was rewarded in the wonderful world of bug bounty hunting. I want to emphasize that what allowed me to find this Account TakeOver was chaining together two specific bugs combined with the account lockout policy after failed authentication attempts.

This was the seventh bug I reported in a private Bugcrowd program, so I can’t disclose the company’s name, but I can tell you that it’s a platform offering various services, including AI, for team collaboration. From now on, I’ll refer to it as vulnerable.com.

I will divide this write-up into two sections: in the first, **I’ll share my journey to achieving the ATO, and in the second, I’ll provide a step-by-step guide to reproducing the ATO** to clarify the exploitation flow.

# **Journey**

I started investigating this when I came across an endpoint called `/auth/update-password` during my tests.

To change your password, the platform sent a POST request that included in the body the parameters “user”, which contained a UUIDv4 identifying the user, “password”, which specified the new password, and “token”, which provided security for the password update:

One of the tests I performed was deleting the token from the body and sending it like this:

To my surprise, I received a response with status code 409 and the user’s data. I tried logging in with the previous password and it didn’t work, but when I tried with “OtherPassword$1”, the password had indeed been changed. The “user” identifier, which as you can see is a UUIDv4, could be seen each time I logged in. The next problem to solve was how to obtain the “user” identifier for any other victim user.

Next, I tried removing the “user” parameter and replacing it with “email”, but I got an error in the response.

I considered several paths for my next tests. One was to look for URLs revealing the UUIDv4 that identifies users in services like Wayback Machine, but I had no luck. So, I went for the next option: what happens if I invite a user who already has their email registered to my workspace?

I created two workspaces, one for the attacker (attacker@bronxi.io) and one for the victim (victim@bronxi.io). From the attacker’s workspace, I went to the invitations section, wrote the victim’s email (victim@bronxi.io), and invited them. In the response, I received the UUIDv4 that identified the victim. However, it was different from the UUIDv4 I could see in the victim’s workspace. This meant the platform assigned a different UUID for each workspace even if it was the same email.

There was something strange here. I accepted the invitation as the victim and was taken to the workspace where the attacker had invited the victim. I logged out and when I logged back in, I entered the victim’s original workspace. Here was another bug that by itself wasn’t a security issue, so I continued pulling the thread.

I tried changing the password using the UUID obtained after the invitation in the attacker’s workspace, but the response was that it didn’t recognize that user. So, I understood that to change the password, I had to use the UUID generated in the victim’s original account. Therefore, the UUID generated in subsequent invitations couldn’t be used to exploit that bug.

I decided to check what would happen if I did a forgot password for the victim user (victim@bronxi.io). After updating the victim’s password following the normal forgot password process, receiving the email with the URL, and changing the password, I logged in again and this time was taken to a dashboard where I had to choose which workspace to enter: the victim’s original one or the attacker’s workspace where the victim had been previously invited.

**Again, I tried using the victim’s UUID obtained within the attacker’s workspace. I used the POST request for update-password and to my pleasant surprise, it did change the victim’s password!**

But this whole flow didn’t add up. For this account takeover to work, the victim had to reset their password after the attacker invited them to their own workspace: for the new UUID assigned in the exploitation to work. In previous tests, the platform had locked me out of accounts after failed login attempts. I conducted a test specifically to find out how many attempts it took to lock the account, and after six attempts with an incorrect password, the account was locked and the user had to perform a forgot password to regain access to their account. The attack flow was complete!

# **Steps to reproduce:**

1. The attacker creates a workspace and invites the victim’s email address as a user of the workspace (Victim’s acceptance of the invitation is not required).
2. The attacker attempts to access the victim’s account six times with any password to lock the victim out.
3. When the victim attempts to access their account, they receive a message stating it is locked and proceeds to perform the password recovery action. They receive the email and reset their password.
4. The attacker copies the victim’s UUID found in their workspace.
5. The attacker uses this UUID in the request shown below to change the victim user’s password:
6. The attacker can then access the victim’s account with the new password. The victim has lost access.

In this step, you will notice that both the victim’s workspace and the workspace to which they were invited by the attacker appear. Even if the invitation has not been accepted. This occurs when resetting the password.

## **Two important considerations:**

1. The linking of the UUID of the victim’s pre-existing account (where they have their own workspace) with the new UUID generated upon inviting them occurs when the victim resets their password through the password recovery link. At that moment, the UUIDs are linked. I have a hypothesis regarding this: since it’s the same email, when querying the database with the email, the first UUID is taken as the primary one when resetting the password, which is the one from the invitation made by the attacker. Thus, both UUIDs are linked to the same email, i.e., the same account.
2. After the attacker has performed the account takeover and the victim notices their password doesn’t work, the victim can perform a forgot password action. However, the attacker can change the password again as many times as they want WITHOUT NEEDING to redo all the steps. They only need to perform step 5 and nothing else.

- ***Reported on April 2, 2024.***
- ***Triaged on April 9, 2024.***
- ***Rewarded on April 19, 2024.***
