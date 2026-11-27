# Privilege Escalation via IDOR Allows Unauthorized User Injection

- **Source URL:** https://medium.com/@omerasraan/privilege-escalation-via-idor-allows-unauthorized-user-injection-f822aa64b528?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@omerasraan
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 11014)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**بسم الله الرحمن الرحيم**

**اللهم صلي وسلم وزد وبارك على سيدنا محمد وعلى آله وصحبه وسلم , اللهم علمنا ما ينفعنا وانفعنا بما علمتنا**

Hi again, it’s Omar and today i want to share with you my first bounty on a public yeswehack program, and an interesting privilege escalation.

**A quick overview over the program:**

The program is simply make you manage devices remotely, by adding these devices to groups and you also can assign managers to these groups to manage the devices with different permissions.

First it took between 2 to 3 days of reviewing the program before start testing.

As said we can add contacts in this app so i created two accounts and connected them.

After, navigate to the devices tap where you can add managers from your contacts and assign them permissions.

After adding managers to my devices and assign him a role you can change his permission later.

**The request looks like this:**

As we can see there is a parameter called “contactId”.

Yes it’s what you though i will change the id to any arbitrary ID.

And it’s 200 OK✅!!!!!!!!!! Quickly navigating to the website to see what happened.

Actually it was kinda funny to see arbitrary user added to your group😂.

Note that this is not an IDOR because i was able to add users as an owner (which is normal), but the difference was that i was able to bypass my range of adding users which was my contacts.

That’s it reported and got the bounty.

At the end i want to say that i found this bug after nearly test every possible idea and function i could test, and it was the only one that worked after a while of testing, so be patient.
