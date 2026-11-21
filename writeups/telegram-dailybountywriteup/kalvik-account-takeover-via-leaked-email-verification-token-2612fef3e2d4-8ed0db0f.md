# Account Takeover via Leaked Email Verification Token

- **Source URL:** https://medium.com/@kalvik/account-takeover-via-leaked-email-verification-token-2612fef3e2d4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250328003328/https://medium.com/@kalvik/account-takeover-via-leaked-email-verification-token-2612fef3e2d4
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9192 (id 9192)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Account Takeover via Leaked Email Verification Token

Greetings, Hunters!!!!

As you know email-based token verification is a common security mechanism in web applications, used for **email verification, password resets, and email changes**. However, if these tokens are improperly handled, they can introduce severe security vulnerabilities.

In this article, I will describe how I initially discovered an **email verification token leak** and later escalated it into **a full account takeover**.

# Step 1: Identifying the Email Token Leak

While testing the application’s email change functionality, I noticed that when a user updates their email address, the system sends **two separate verification links**:

1. One to the **old email** to confirm the change.
*https://redacted.com/authorize-email-change/{token}*
2. One to the **new email** to complete the transition.
*https://redacted.com/confirm-email-change/{token}*

To successfully update the email address, user needs to click on both the links.

Upon inspecting the response after clicking either of these links, I found that **the both verification tokens was exposed in the response body**. This meant that user can update the email address by just getting either of the verification link.

Till now, I have a found a email verification bypass. As I attacker I can update my email address to any email by following these steps -

1. Create an account using **my own email address** (**attacker@email.com**)
2. Go to profile setting -> **Change email.**
3. Type the **new email address**(lets say **victim@email.com**)
4. **Two verification links will be sent**, one to attacker@email.com, other to victim@email.com
5. As **both the tokens are getting leaked in response** of either of the verification link, as attacker I can just click on the link received in my inbox i.e attacker@email.com and get both the tokens.
6. Finally replace the token in this endpoint [*https://redacted.com/confirm-email-change/{token}*](https://redacted.com/confirm-email-change/{token}) and email will be successfully updated.

I could have reported it as it is but it will be marked a LOW-MEDIUM issue depending on the program and on BugCrowd when I checked the severity of Email verification bypass, it was considered as Informational(P5). I was like -

I thought of **chaining this vulnerability** with something else to make a bigger impact. Then I remember the app I was testing on **deals with Creating Organisations, Adding users, Roles and Permissions, etc.**

# Step 2: Escalating the Issue to Account Takeover

I noticed if I have Admin or similar permissions within the organisation, I can actually manage other users and Admins(their name, email address, etc). I tested whether I could leverage this flaw to gain full control over a user’s account.

# Exploitation Steps:

1️⃣ As an admin, change a target user’s email to an attacker-controlled email **(attacker@example.com).**

2️⃣ As one verification link will be sent to attacker’s inbox, I can **Capture the leaked verification token that was supposed to sent to user’s email** from the HTTP response.

3️⃣ **Use the leaked token to confirm the email change**, successfully linking the target account to the attacker’s email.

4️⃣ **Trigger a password reset request** for the newly updated email address (`attacker@example.com`).

5️⃣ **Complete the password reset process**, gaining full control over the victim’s account.

# Step 3: Further Escalation — Inviting & Hijacking External Users

While analysing the impact, I discovered another serious consequence:

- The application allows **admins to invite new users** to their organisation.
- Since email verification tokens were leaked, an attacker could invite a victim to their organisation, as soon as the victim clicks on the invitation link, I can trigger the email change and hijack the account.
- This would allow the attacker to confirm the invite on behalf of the victim and take over their account before they even sign in.

**The report was accepted as Valid with Critical severity(P1).**Thats how I escalated a simple email verification bypass vulnerability into a Critical \[P5 -> P1\].

# Tips —

If you ever find email verification bypass, always to chain it with something and check there are any inconsistencies with token and email.

For example — 

 *— Check where reset password link is sent when email verification is pending.* 

— *Check if your reset password link is still linked to the account after email update.* 

 *— What happens when two people requests for same email address change.*

You might find some business logic vulnerabilities with these approaches.

Hope I was able to explain the vulnerability properly, if anything feel free to reach out to me or put a comment.

Thanks for reading!!!


Vikash Maurya

LinkedIn — [https://www.linkedin.com/in/vikash-maurya-669845172/](https://www.linkedin.com/in/vikash-maurya-669845172/?lipi=urn%3Ali%3Apage%3Acompanies_company_people_index%3B208700cb-6559-4727-9a8e-0ecb2521d90d)
