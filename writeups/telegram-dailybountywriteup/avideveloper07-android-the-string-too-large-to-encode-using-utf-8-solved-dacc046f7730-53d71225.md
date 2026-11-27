# Android — The STRING_TOO_LARGE to encode using utf-8 — Solved!

- **Source URL:** https://medium.com/@avideveloper07/android-the-string-too-large-to-encode-using-utf-8-solved-dacc046f7730?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142817/https://medium.com/@avideveloper07/android-the-string-too-large-to-encode-using-utf-8-solved-dacc046f7730
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2081 (id 2081)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Android — The **STRING\_TOO\_LARGE** to encode using utf-8 — Solved!

**What is the issue?**

Sometimes while building an android app you get this weird compile time error *“string too large to encode using UTF-8 written instead as STRING\_TOO\_LARGE”*. No matter how hard you try to find a solution you won’t be able to find it over the internet. After a lot of research, I have found an approach to fix it permanently. Without wasting much time let’s jump over the solution.

**The root cause of the issue?**

The answer to this question is, somewhere in the project source code you have a very long string. To which compiler is not encoding while building the project.

**How to trace the file containing this String?**

In the android studio, the error is shown while compiling, sometimes build compiles successfully and sometimes failed. If you are using build tools like Jenkins, TeamCity or QuickBuild to build the app then most of the time build will fail.

1. **A temporary solution-** Build project in the android studio — Clean build, Clear cache, Restart android studio, and make the project. But this is not the fixing of the issue forever.

2\. **The permanent solution** — Find the culprit file and delete it or modify it.

**Step 1:** Compile the project and generate the build then go to **app/build/intermediates/apk/{env\_name}/debug/{apk file}** if the build is failed still you found the build in this location.

**Step 2:** Then **unzip/uncompress** this APK file or Decompile APK using any tools like **apktool**

**Step 3:** Open this unzip code in Android studio itself.

**Step 4:** Then global search for the “**STRING\_TOO\_LARGE”** (cmd + shift + F)

**Step 4:** You will get the exact culprit file. Most of the time this issue is found in vector drawable in the android:pathData attribute.

**Fixing the issue -**

Simply change the drawable from the UI designer and again convert it into a vector drawable if the issue is with the drawable. If it is in some other part of the code reduce the size of that string.

Problem Solved!

**How many characters are allowed in a string to encode using UTF-8?**

I could not find any max limit for this on the internet. But with trial and error methodology I could get some numbers after which this issue start appearing at compile time. Here are my observations

The STRING\_TOO\_LARGE issue is pretty easy to reproduce. The easiest way is to add a string resource to your app that is longer than 0x7FFF = 32767 characters and then display it in a TextView. That’s it!

Please don’t forget to hit the clap button👏🏻 if this article added some value to your code.
