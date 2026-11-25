# I Verified One Email and Claimed Another’s Invitation

- **Source URL:** https://scriptjacker.medium.com/i-verified-one-email-and-claimed-anothers-invitation-5c372c83ba77
- **Fetched from:** https://scriptjacker.medium.com/i-verified-one-email-and-claimed-anothers-invitation-5c372c83ba77?source=rss-d1a41cbb187a------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14922 (id 14922)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Parth Narula / Thu, 24 Sep 2026 06:22:38 GMT

Hey Hackers, I am Parth Narula. A penetration tester, bug hunter, red teamer and overall a security researcher. I live for those moments where a bit of out of the box thinking cracks open a critical vulnerability.

This is the story of a business logic flaw I found in an invitation flow. The application invited one email address, but allowed me to complete registration using another. I verified my second email, created a password, and entered the circle under the original invited address. No warning about the different email. No request to sign in as the invited user.

It started when I was examining the member management feature on REDACTED. The platform allowed users to create communities called circles. As the owner of a test circle, I could invite people by email and give them a role.

The member management page URL: /circles/{circle\_slug}/manage?tab=members

I sent an invitation to scriptjacker+pentester@gmail.com with the Contributor role. The application delivered an email containing an Accept invitation button.

I opened the invitation link from my test inbox. Its structure looked like this, with the circle name, invitation ID, and token replaced with placeholders: https://REDACTED/circles/{circle\_slug}/membership-invitations/{id}?token={token}

The URL pointed to a particular invitation and included a token. I wanted to see how the application connected that invitation to the person completing registration.

The application used a separate authentication service for signing in. When its login page opened, the invited email was already filled in.

But here is what caught my attention. The email field was editable.

Then I asked myself a simple question. What if I verify a different email while completing this invitation?

I changed scriptjacker+pentester@gmail.com to scriptjacker+anotheremail@gmail.com and continued. I did this directly through the page. There was no need to intercept a request to change the field.

The authentication service sent a verification code to the alternate address. I opened the inbox, copied the code, and entered it on the verification page. After that, I created a password.

Notice something important here. I had verified the second email. The invitation was still addressed to the first one.

The next page confirmed that I was signed inscriptjacker+anotheremail@gmail.com. It showed a button to return to the application.

I clicked it and waited to see what would happen.

The application continued into /profile/onboarding. It did not ask me to go back and authenticate with the invited address.

I switched back to the circle management page and refreshed the member list.

Previously, there were three members. Now there were four. The new member had the Contributor role, and the email shown beside that member was scriptjacker+pentester@gmail.com. The original invited address.

I had completed authentication with one email, but the application had added me under another. To check this further, I opened /profile in the new session.

The profile also displayed scriptjacker+pentester@gmail.com.

At this point, I wanted to check whether this was only a display issue or something that affected access to the account.

So I logged out and opened /session/new and tried signing in with the original invited address, scriptjacker+pentester@gmail.com. The authentication service asked me to verify that email and create a password. I completed those steps through my test inbox.

The browser then returned to the application through an authentication callback with this visible URL structure: [/session/auth/callback?id\_token={REDACTED}](https://REDACTED/session/auth/callback?id_token={REDACTED})

The page displayed this result: Authentication failed. Please try again.

I could not access the account using the email shown on its profile.

Next, I tried the alternate address, scriptjacker+anotheremail@gmail.com. I entered the password I had created while accepting the invitation.

This time, it worked.

The application opened /circles, showed the circle I had joined.

I opened /profile again to check the email.

It still showed scriptjacker+pentester@gmail.com.

The results were consistent in my tests:

So the mismatch remained after logging out. The alternate identity could still access the invited membership, while the original identity could not access it in my tests.

What made this interesting was how ordinary each step looked. Open an invitation. Enter an email. Verify a code. Create a password. But when I changed the email between those steps, the application continued without resolving the mismatch.

I hope you learn something new. Follow for more amazing articles and give claps if you like this one :)

Need expert pentesting services? Visit [https://scriptjacker.in](https://scriptjacker.in) or let’s collaborate on your next project! 🤝

Want to learn from my experiences? Check out my articles on [https://blogs.scriptjacker.in](https://blogs.scriptjacker.in)
