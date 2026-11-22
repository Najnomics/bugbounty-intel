# How I Found My First Bug in Android

- **Source URL:** https://medium.com/@severustalin/how-i-found-my-first-bug-in-android-41153093ba57?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230127222116/https://medium.com/@severustalin/how-i-found-my-first-bug-in-android-41153093ba57
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1519 (id 1519)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Found My First Bug in Android App

## Bypass the Password and Biometrics Functionalities

*A simple story about me*

*Learned about web application testing online during the COVID-19 period. Did testing on multiple web apps but if I reported any bugs it may informational and duplicates. Then I was curious about android app development so I learned about developing apps. Then I could able to find security issues in android apps. It is like low-hanging fruit — bugs*

**Analyzing**

I used an app for 2FA to get TOTP. Little curious about the applock function so I decompiled the app using JADX-GUI(a tool to decompile the apk) and saw the Androidmanifest.xml file to get the details of the app. \[com.demo.app.HandleRedirectionActivity\] is exported=true(means any app can call this activity ) so read the code of the activity it doesn’t have anything to read it is just redirection\_handler activity. Jumped into app\_lock \[com.demo.app.PinLock while analyzing the code I get to know it doesn’t validate the activity call.

**Exploiting**

Then I call the redirection activity directly using ADB. Haa!! app lock activity doesn’t authenticate the redirection\_handler activity.

*$ adb shell am start -n com.demo.app/.HandleRedirectionActivity*

**Creating POC**

Most of the VDP programs don’t allow to use of the ADB. So I Created an Android Application in Android Studio.

*intent intent = new Intent();*

*intent.setClassName(“com.demo.app”, “com.demo.app.HandleRedirectionActivity”);*

*startActivity(intent);*


Just Create an app to call the redirection\_handler activity, when you open the attacker app it bypassed the biometric entry into the TOTP activity

*LinkedIn profile: Barath Stalin*
