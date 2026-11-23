# IDOR — Exposing private forms $$$

- **Source URL:** https://medium.com/@hellother18/idor-exposing-private-forms-0204c1ed560a?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240816152404/https://medium.com/@hellother18/idor-exposing-private-forms-0204c1ed560a
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6936 (id 6936)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR — Exposing private forms $$$

Hey, everyone! I’m Manthan, and today I’m going to share an interesting find from one of my recent explorations on a target which is something like forms sharing platform, we’ll refer to as “forms.com.” This discovery involves a sneaky little vulnerability known as Insecure Direct Object References (IDOR), and it allows someone to share private forms with anyone, without the owner’s permission.

# The Scenario

Imagine you’re on forms.com, a platform that lets users create and share forms. While digging around, I uncovered a vulnerability that lets you share a form from any user with one of your friends — or in this case, with one of your own alternate accounts.

# How I Found It:

1. **Create Two Accounts**: I started by setting up two accounts on formsproviding.com.
2. **Send a Friend Request**: I sent a friend request from Account 1 to Account 2.
3. **Share form with account 2** : Next, I navigated to the share form section, and fired up Burp Suite to intercept the request while sharing my form with account 2.
4. **Capture and Modify the Request**: In the captured request, I found two key parameters: `relation_id=123` and `form_id=345`. The `relation_id` corresponds to Account 2, and the `form_id` represents the form I’m about to share. By simply changing the `form_id` to another form's ID and forwarding the request, I was able to share a different form.

`relation_id=39818&forms_ids%5B%5D=82271&ajax=1`
# The Outcome?

When I logged into Account 2 and checked the “Forms to Fill” section, the form I had shared from Account 1 appeared there. I could fill out the form, see the responses, and access any private forms from any user without their knowledge.

# Why This Matters:

- **Unauthorized Access**: This vulnerability allows anyone with the right know-how to access and share private forms without the owner’s permission.

Reward with Є 200 : )

**Well if you love this write up drop a clap 👏**

Thanks for reading !!
