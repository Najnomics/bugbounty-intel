# How I Got $$$$ for Bypassing a PIN Lock in an Android App

- **Source URL:** https://medium.com/@0xk3r0/how-i-got-for-bypassing-a-pin-lock-in-an-android-app-6c1b48f615e3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251101144612/https://medium.com/@0xk3r0/how-i-got-for-bypassing-a-pin-lock-in-an-android-app-6c1b48f615e3
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9887 (id 9887)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Got $$$$ for Bypassing a PIN Lock in an Android App

In one of my recent Android app assessments, I came across an interesting behavior that led to a valid vulnerability—nothing major, but still worth sharing.

I started by downloading the app and running it on an emulator. Upon opening it, I noticed it uses a **PIN lock screen** for authentication. Naturally, I got curious and decided to dive deeper.

I decompiled the APK using **Jadx**, and as usual, I started checking the `AndroidManifest.xml`.

Here’s what I found:

1. The`MainActivity` was marked as `exported=true`, which is normal.
2. However, there’s a **PIN lock activity** was also `exported=true`, which raised a red flag.
3. I examined the code but couldn’t find any reason for it to be exported.

So, I ran a quick test:

Using **ADB**, I tried launching the PIN lock activity *directly* without opening the app first. It worked—the PIN screen appeared.

I entered the correct PIN, and immediately after that, the app closed (without doing anything).

Then I launched the app *normally* from the icon, and to my surprise, it logged in directly, without asking for the PIN again.

Apparently, the app **creates a session** after PIN entry that remains active for a certain period, even if the app gets closed immediately after.

## My PoC Exploit

I created a simple PoC application that does two things:

1. Launches the exported **PIN lock activity** and waits for the user to enter their PIN.
2. After the app closes, my PoC app launches the **MainActivity** directly.
3. Because the session was still active, the app logged in immediately granting access to user data without any further authentication.

## Impact & Report

While this requires user interaction (i.e., the user has to enter their real PIN), it still poses a risk—especially because the app belongs to a **FinTech company**, where sensitive data is involved.

I reported the issue and recommended:

- Making the **PIN lock activity non-exported**
- Properly handling the session lifecycle (e.g., clearing session state on exit or inactivity).

The report was acknowledged and accepted with a **Medium severity** rating — so overall, a nice catch.

Always keep an eye on exported components.

THANKS FOR READING ❤️

*If you want to connect with me, feel free to reach out to me on LinkedIn*
