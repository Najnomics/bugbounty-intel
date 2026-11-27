# Hunting for Firebase Enums in Android Application

- **Source URL:** https://medium.com/@tanish.saxena26/hunting-for-firebase-enums-in-android-application-42b79e9b76f8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251019232656/https://medium.com/@tanish.saxena26/hunting-for-firebase-enums-in-android-application-42b79e9b76f8
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6690 (id 6690)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Hunting for Firebase Enums in Android Application

## **Here is how I found 2 Insecure Firebase**

A few weeks back I was doing bounty hunting on Android apps, I came across two mobile applications (apps) that were vulnerable to Firebase enumeration.

## **Firebase**

Firebase = Google Backend Development Platform, Due to insecure Configurations, it was possible to enumerate resources without proper Authorisation and access unsafe data.

These are commonly used in Android apps although there is slightly less Chance of getting one, there is always a possibility that once you start looking For these you will find one

Although I didn’t get any bounty for this vulnerability (“this vulnerability has a severity of 9–10 in one of HackerOne bug bounty reports”, “link of this report is in the last”)even tho this company was listed on a bug bounty program they both are huge brands in the Indian market still they didn’t even give Hall of Fame I Felt just like being betrayed 😂😂

Anyway, I Just wanted to make this Blog because I found it interestingly easy To find, you need to automate most of the process so it will be a Piece of cake to find it, if you are looking for example 20–30 apps then there Is a chance you could find one.

**So the process is as follows**

Choose any Android app that is listed in any bug bounty platform or is open For a vulnerability discloser program and then you can go ahead and Perform the following steps:-

1. You will need the APK file you can use either Geny-motion

Geny-motion is an emulator for Android or any device you want to emulate [https://www.genymotion.com/](https://www.genymotion.com/)

Or you can also get the APK file from a platform such as apkpure.net but there is a possibility that the APK is of an older version so it is always best to go with an emulator

but if using Emulator, once you get it all set up install the APK in the emulator then move to the next part if you haven’t already got the APK file

2\. Pulling the APK from the Emulator for this we will be using ADB

(Android Debug Bridge) [https://developer.android.com/tools/adb](https://developer.android.com/tools/adb)

Once you also get it set up just write the following commands

`adb shell pm list packages -f | grep <APK name>`
you will get the full path of that APK it should look something like this

As you get the full path just copy it also do not copy (package:) Copy whatever is written after this

`adb pull <path_to_the_APK_file_till_base.apk>`
By now you must have got the APK file

3\. Decompile the APK for this you can use Apktool which I also use there are a bunch of tools out there but I have personally used Apktool

`apktool d base.apk`
Once the tool is done you will see it has created a folder that folder contains all the files that are in APK you should see one folder named /res

4\. look for the Firebase link in the /res/values/strings.xml file

`cat /res/values/strings.xml | grep firebase`
you should see a Firebase link something similar to this

The Firebase link follows a link pattern which is

`*.firebaseio.com`
once you get the URL there are 2 conditions to check if the Firebase is vulnerable to Firebase Enums

Now on visiting the URL followed by /.json if it returns null data or supplies data then

`Curl -x Get https://somefirebase-database.firbaseio.com/.json`
Something just like this then it is vulnerable to Insecure Firebase Enum we can further exploit this

but if it returns “Permission denied” then it is properly configured and it cannot be exploited

So let’s exploit this and input some data into the database

Let’s make a POST Request with some data

```
curl -X POST https://somefirebase-database.firebaseio.com/testing1.json -d
'{"cat": "meow", "dog": "bowbow"}'
```
Now visit the /testing1.json On visiting the link you should get a result Something like this

Thank me later 😆

I hope this has helped you to understand how to find Insecure Firebase Enum, I also suggest to reading these articles/blogs about Insecure Firebase Enum
