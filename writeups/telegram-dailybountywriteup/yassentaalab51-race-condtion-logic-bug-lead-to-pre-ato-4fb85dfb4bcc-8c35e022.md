# Race condtion & Logic Bug lead to Pre-ATO

- **Source URL:** https://medium.com/@yassentaalab51/race-condtion-logic-bug-lead-to-pre-ato-4fb85dfb4bcc?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251121175956/https://medium.com/@yassentaalab51/race-condtion-logic-bug-lead-to-pre-ato-4fb85dfb4bcc
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9397 (id 9397)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Race condtion & Logic Bug lead to Pre-ATO

## الحمد لله الذي عَلَّمَ بالقلم.. عَلَّمَ الإنسانَ ما لم يَعْلَم والصلاةُ والسلامُ على خيرِ مُعَلِّمي الناسِ الخير محمد أما بعد

Hello everyone! In this write-up, I’ll share how I discovered a **logic bug and a race condition** that led to **Pre-Account Takeover (Pre-ATO)** in an application. This vulnerability allowed an attacker to **completely hijack a victim’s account without user interaction ,** And user can’t recover his account

Lets Understanding the Application Workflow :

This application allows users to

**sign up using two methods :** Traditional Email & Password — Google SSO (Single Sign-On)

If a user **signs up with a normal email & password**, they can **change their email** in the account settings.

However, if a user **signs up using Google SSO**, the frontend **disables the email change option**.

But this is in front-end. what about the back-end?

I try to change the email in the normal account and intercepted the request and i found this parameter “ user%5Bemail%5D ”

So, I tried do any changing and adding the same parameter to a request while using **Google SSO account to** chang the email to `victim@gmail.com`.

what you think i found ??!

I received a `302 Found` response, meaning the **email change was accepted!**

But there was one problem…

The application sends a **confirmation email** to the new email address (`victim@gmail.com`). Until the victim clicks the confirmation link , the attacker cannot take over the account.

At this point we need to bypass this confirm email

So I try some techniques like response manipulation use code send to another email but not work so i can’t do any thing at this point

I say let report it and will be closed as low because it need user interaction but what is the impact ??

if the user click the confirm email now the attacker gain full access to the victim email and the victim can’t signup new account with this email or sign in because it linked to google account for the attacker .

When he try to change the password to recover the email he will find :

So, I reported it to HackerOne, expecting it to be classified as **low severity**.

After two weeks, I received this response:

So I accept the challange to bypass the confirm email .

I ask for help from my friend Mahmoud and we started testing different bypass techniques : Host Header attack , Manipulating email parameter and try send the confirm code to attacker and when click the link add the victim email in the request but Failed.

Then, I thought: **Why not try a race condition?**???

The idea was simple:

- **Send two email change requests at the same time**, one for `victim@gmail.com` and another for `attacker@gmail.com`.
- If timed correctly, the system might get confused and **confirm the wrong email**.

At this point I add the two requests to group in burp repeater and send them in parallel

what I found is email send to both accounts when I click on link sent to victim I got that “ link is invalid please try again “

When I click on link sent to attacker i found “ the email is confirmed “

I go back to the app and refresh the page found that my account be

“ [victim@gmail.com](mailto:victim@gmail.com) ”

I asked my friend Mahmoud to confirm that and record poc to update our report

after one month he response with that

Honestly, I was a bit disappointed by the response from HackerOne.

But **thanks to Allah**, that disappointment pushed me to think harder, and eventually uncover the full exploitation path.

Steps to Reproduce

1-Sign up with your own Google account.

2-Navigate to Settings → Modify your name → Click Save.

3-Capture the request to in burp .

4-Send the request to the repeater twice and add this :

(&user%5Bemail%5D=victim@gmail.com)

(&user%5Bemail%5D=attacker@gmail.com)

5-Add both requests to Burp Repeater group and send them in parallel to create a race condition.

6-Both the victim and the attacker receive an email verification request.

7-The attacker only clicks their own verification link ([attacker@gmail.com](mailto:attacker@gmail.com)).

8-Due to a race condition, the system mistakenly verifies the victim’s email instead of the attacker’s.

9-Log out and sign back in using Google SSO → The attacker is now fully logged into the victim’s account.
