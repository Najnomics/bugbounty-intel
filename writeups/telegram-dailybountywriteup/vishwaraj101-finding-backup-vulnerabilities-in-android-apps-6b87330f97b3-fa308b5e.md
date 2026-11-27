# Finding backup vulnerabilities in android apps

- **Source URL:** https://medium.com/@vishwaraj101/finding-backup-vulnerabilities-in-android-apps-6b87330f97b3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126141920/https://medium.com/@vishwaraj101/finding-backup-vulnerabilities-in-android-apps-6b87330f97b3
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3443 (id 3443)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Finding backup vulnerabilities in android apps

Hi everyone this post is just an elaboration of the **10th** point that I made it in my [previous post](https://vishwarajbhattrai.wordpress.com/2017/02/28/mobile-app-security-bugs-which-are-actually-counted/) which is being often missed by dev/hunters while looking for bugs in android apps although this issue is not new and more then a vulnerability it is a misconfiguration.

**Why backup?**

Just like any other OS android system allows a user to make the backup of their app that’s cool but from our end, we are concerned about whether any sensitive information is being leaked in the backup or not and whether it has been loosely configured.

**Tools Required?**

1. Adb
2. Abe
3. Apktool
4. Genymotion

**How to proceed :**

1. To check whether any app allows the backup you need to first reverse the apk and find the manifest file to do so execute ***apktool d \<app-name.apk>***
2. Check-in **AndroidManifest.xml** file for the attribute
**android:allowBackup=” true”** if this is present and its value is set to **true** it means we can backup the app internal data which resides under
***/data/data/\<app-package>***
3. To backup the app hit the ***adb backup -f \<backup-name.ab>
\<app-package-name>***
4. Accept the backup confirmation from the device.
5. Now you will have the **app-backup.ab** file in your working directory
6. To read this you need to convert this .**ab** file into a ***.*tar** format using the tool
[Android Backup Extractor](https://github.com/nelenkov/android-backup-extractor)
**Command *: java -jar abe.jar unpack app-backup.ab***
7. Then you can extract this tar file using ***tar xvf app-backup.tar*** t
8. To make this process short I have written a custom tool [pentdroid](https://github.com/vishwaraj/PentDroid) which automates all the above android operations.

1. Just select the operation **6** for reversing an app, **4** (For taking backup of an app ) then finally select option **5** to convert the ***backup.ab*** into ***backup.tar.***
2. Once you will get .tar file extract it using **WinRAR**
3. Once it has been extracted you will get the folder residing in ***/data/data*** directory.
4. Try to explore the various files including assets like ***.db, sharedprefs.xml*** and search for sensitive information sometimes you will find **developers secrets, pass, auth token for API’s** etc
5. Here I got one such case while reporting to one of the android programs where I was able to obtain auth token stored in one of the ***.db*** files.

1. I have used [SQLite browser](http://sqlitebrowser.org/) to see the info of .**db** files.
2. By using the obtained token we can make calls to the API endpoint to fetch more information.

**Why bother about this if we can find something by just rooting the device?**

With this, you don’t need a rooted device to obtain data from apps internal directory ! and well this respect the program scope too as compared to the other OWASP-M2 issues which require you to have a rooted device.

**Any Patch or recommendation?**

1.)Try to Implement sqlcipher which encrypts the SQLite DB check out > [http://lomza.totem-soft.com/tutorial-add-sqlcipher-to-your-android-app/](http://lomza.totem-soft.com/tutorial-add-sqlcipher-to-your-android-app/)

2.) Set ***android:allowBackup=false*** within the android manifest file to disallow the access.

3.)Even do not let apps to upload backups in clouds containing sensitive info in clear text.

#signoff
