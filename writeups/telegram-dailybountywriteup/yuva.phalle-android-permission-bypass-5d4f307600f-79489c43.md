# Android Permission Bypass

- **Source URL:** https://medium.com/@yuva.phalle/android-permission-bypass-5d4f307600f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142838/https://medium.com/@yuva.phalle/android-permission-bypass-5d4f307600f
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3580 (id 3580)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Android Permission Bypass:

## Unauthorized Access through READ\_EXTERNAL\_STORAGE / WRITE\_EXTERNAL\_STORAGE

## Introduction

Through my own experimentation, *I was able to uncover a rather easy but critical vulnerability in Android*. This article details the nature of the bug, its potential ramifications for user data, the steps to reproduce it, the acknowledgment date, and subsequent actions taken to remedy the issue, complemented with a Proof of Concept (POC) video.

## **The Security Issue**

The vulnerability involves the **“READ\_EXTERNAL\_STORAGE / WRITE\_EXTERNAL\_STORAGE”** permissions in my Android app. When you install apps on your Android device, sometimes they ask for permission to access your photos and other files, right? There’s an **“Allow” or “Deny”** option. I discovered that even if you choose **“Deny”**, apps might still be able to see your files. *Think of it like a door you thought you locked, but someone still finds a way in*.

## **Potential Consequences**

What’s the big deal? Well, if an app can access your files without your knowledge, it might see your photos, learn about the apps you use, or even gather some information about your device. And if the wrong people use this information, it can lead to issues like unwanted access to your personal details or targeted ads based on your data.

## **Discovery Process**

Being curious, *I decided to do some detective work on Android’s security.* And, to my surprise, I found this hidden issue. Denying the *“READ\_EXTERNAL\_STORAGE” / “WRITE\_EXTERNAL\_STORAGE”* permission still allowed the app to access files from external storage. Realizing the implications, I promptly reported this to the Google Android Security Team.

## **Acknowledgment and Resolution**

On **July 7th, 2023,** the Google Android Security Team acknowledged the seriousness of the issue and classified its severity as Moderate. Consequently, the bug qualified for **Android Security Rewards (ASR)**, and I was rewarded for responsibly disclosing it.

To address the vulnerability, the *Android Security Team plans to include a fix* in an **upcoming quarterly update for Android (2023)**, demonstrating their commitment to a secure app ecosystem.

## **Proof of Concept (POC) Video**

For a visual demonstration of this vulnerability, I’ve prepared a POC showcasing unauthorized access to external storage. 

*Not shown: I was able to perform CRUD operations without having appropriate permissions.*

If you’ve gotten this far, either my discovery intrigued you or you’re just a big fan of Android quirks. Either way, share the fun and spread the word. Cheers, and keep those apps in check! #StaySeucre😉
