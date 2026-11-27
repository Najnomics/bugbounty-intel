# Diving Deep

- **Source URL:** https://medium.com/@hackersdump0/diving-deep-a-comprehensive-guide-to-android-penetration-testing-part-3-99e86d021190?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240110121752/https://medium.com/@hackersdump0/diving-deep-a-comprehensive-guide-to-android-penetration-testing-part-3-99e86d021190
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4469 (id 4469)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Diving Deep: A Comprehensive Guide to Android Penetration Testing — Part 3

## Cracking the Code: A Beginner’s Guide to Decoding Android Apps

--

As we journey deeper into the realm of Android Penetration Testing, **Part 1, Part 2** equipped us with the tools and groundwork needed for our digital expedition. Now, in **Part 3**, titled “**Cracking the Code**,” we’re delving into the fascinating world of static analysis — a beginner-friendly guide to decoding Android apps. Picture this as the moment we put on our detective hats, examining the intricacies of app structures and unraveling the secrets they hold. So, after setting up our cyber camp in Part 2, get ready to embark on an adventure of code-cracking and unraveling the mysteries within Android apps. Let the decoding begin! 🕵️♂️💻🚀

## **App Magic: How to Grab an APK Easily**

**Option 1**Connect your device with computer

**get a list of the installed packages and their namespaces**

***adb shell pm list packages* (**This will list all packages on your smartphone

**)**

Once you’ve found the namespace of the package you want to reverse ( owasp.sat.agoat in this example ), let’s see what its physical path is:

Finally, we have the APK path:

Let’s pull it from the device

**Option2**To extract the Apk file from the device just download the Apk Extractor from

**Play Store**or


[**Clickhere**](https://mega.nz/file/uYMTTBpQ#5y8r1xUY-jm5Pq_nMjk-s8DX27b_3AOZIzZoSTEjPKM). In order to successfully extract an APK file on your Android using this app, follow these steps:

1\. Open the APK Extractor app on your Android device

2\. Tap on the APK file you want to extract.

It will save the APK file on the given folder. Locating the folder will get the APK file for the same.

**Option 3**Open these given link

[**https://apps.evozi.com/apk-downloader/**](https://apps.evozi.com/apk-downloader/)


Paste the Playstore link of the Application it will direct extract the apk

## **Decoding Apps: Easy APK Reversing with JADX-GUI**

If you haven’t got your hands on **JADX-GUI** yet, no worries! Just head back to [**Part 2**](/@hackersdump0/diving-deep-a-comprehensive-guide-to-android-penetration-testing-part-2-9c33c319a696) and grab your own copy to join the decoding fun.

*Now what is APK Signature ?*

After extracting the APK Open that APK with JADX-GUI

In Android app signing, the terms v1, v2, and v3 refer to different versions of the APK (Android Package) signature schemes.

**v1 (JAR Signature)**: The original and now legacy signing scheme for Android apps. It involves signing the entire APK file using a Java Archive (JAR) signing process. This method is compatible with all Android versions.

**v2 (APK Signature Scheme v2)**: Introduced in Android 7.0 (Nougat), v2 is an enhancement to the original signing process. It enables the addition of a separate APK Signature Block, improving the verification process and reducing signing-related errors.

**v3 (APK Signature Scheme v3)**: This is another enhancement to the signing process, introduced in Android 9.0 (Pie). Similar to v2, v3 adds additional features to strengthen the security of app signing, including support for key rotation.

What is Impact if application is only signed with V1 

**Security:** The v1 signature is considered less secure compared to the v2 and v3 signature schemes. It lacks some of the modern security features incorporated in the later versions, making the app potentially more susceptible to certain types of attacks.

2\. Open manifest file. Check for **Min SDK** Version it should be above 21 API level. 

**Api Levels** : Android API level is a numerical identifier assigned to each version of the Android operating system. It represents the set of features and capabilities available to developers when creating apps. As the API level increases with newer Android versions, developers can access additional functionalities and improvements in the platform. Official link of android developers. **https://apilevels.com/**

3\. Check for Unwanted Permissions

4\. Check for Components i.e 

**Android exported set to true (It should be false)**

If the Android `exported` attribute of a component in the AndroidManifest.xml file is set to `true` when it should be `false`, it can have significant real-life security implications. Here's the impact:

1. **Unauthorized Access**: Setting `exported` to `true` makes the component accessible from other applications or entities, potentially allowing unauthorized access to sensitive functionality.

2. **Data Leakage**: Components with improper export settings may expose sensitive data, leading to data leakage. This could include exposing content providers, services, or activities that should be restricted.

3. **Security Breaches**: Malicious apps or attackers could exploit the exposed component to perform actions that should be restricted, leading to security breaches, unauthorized control, or even remote code execution.

5\. Check for **Allowbackup = True** & **Debuggable = True**

**AllowBackup**: Enabling `allowBackup` by setting it to `true` in AndroidManifest.xml allows data backups for the app. While convenient for users, it poses security risks, exposing sensitive data and creating potential vulnerabilities. Attackers may target stored backups, compromising data integrity and violating privacy regulations. It's advisable to assess the necessity of backups, encrypt stored data, and ensure secure storage practices to mitigate these risks effectively.

**Debuggable :** Setting `debuggable` to `true` in the AndroidManifest.xml file allows the app to run in debug mode. While useful for development, it poses security risks in a production environment. Debuggable apps may expose sensitive information, making them vulnerable to reverse engineering and unauthorized access. To enhance security, set `debuggable` to `false` for production builds, reducing the risk of potential exploits and data exposure.

Can we exploit “allow backup = true “ ? yes, here is the reference you can go for it [https://securitygrind.com/exploiting-android-backup/](https://securitygrind.com/exploiting-android-backup/)

6\. Check for Cleartext traffic is set to true

Setting `android:usesCleartextTraffic` to `true` in the AndroidManifest.xml file allows the app to send unencrypted (clear text) network traffic. This poses a security risk as sensitive information may be exposed during transmission. To enhance security, it is recommended to set `usesCleartextTraffic` to `false` and use secure communication protocols such as HTTPS to encrypt data in transit, preventing potential interception and unauthorized access.

7\. Check for Source Code obfuscation

Identifying whether source code is obfuscated can involve both manual inspection and automated analysis. Here are some methods:

- **Variable and Method Names**: Obfuscated code often uses short, nonsensical names for variables and methods, making it challenging to understand the code’s purpose.
- **Code Structure**: Obfuscators may change the structure of the code, introducing redundant or convoluted constructs to impede readability.
- **Comments and Documentation**: Obfuscation tools might remove or alter comments and documentation, making it harder to understand the code’s logic.
- **Renaming Patterns**: Look for common obfuscation patterns like single-letter variable names or alphanumeric sequences.
- **Unused Code**: Obfuscation tools may introduce unused or unreachable code to confuse analysis tools.

8\. In **Strings.xml** file check for firebase URL, etc

**Firebase Databases** : It can be leveraged by application developers to store and sync data with a NoSQL cloud-hosted database. A misconfigured Firebase instance can be identified by making the following network call

Copy the URL and paste in the browser with /.json as shown below check the Output.

Copy the URL and paste in the browser with /.json as shown below check the Output

**To Exploit Firebase** [https://github.com/Sambal0x/firebaseEnum](https://github.com/Sambal0x/firebaseEnum)

9\. **Text Search** : In source code check API keys, Hardcoded Certificates, Internal IP Addresses, usernames, Passwords, etc.

10\. **Search for Webview** : A WebView in Android is a user interface component that allows developers to embed a web browser within their Android app. It enables the display of web content, such as websites or web pages, directly inside the app’s user interface.

**setJavascriptEnabled = true**

**Exploit XSS with WebView** [https://medium.com/mobis3c/exploiting-android-webview-vulnerabilities-e2bcff780892](/mobis3c/exploiting-android-webview-vulnerabilities-e2bcff780892)

## **Unlocking Secrets: Exploring/Exploiting Components with Drozer**

You could download and install Drozer, Below are links to download 

**Drozer installer and Drozer Agent**Install

**Drozer installer**in your windows system and

**Drozer agent**into Mobile

After installing both open CMD and Type these command

1. In drozer agent below we can see a toggle button just press ON

2\. Thereafter, we need to go to the terminal and start up Drozer and connect it to the emulator/device. To do this, we need to type in drozer console connect, as shown in the following screenshot:

We have successfully connect to drozer

3. To list the installed specific packages on the Android device with drozer

4\. To get info of a specific package for vulnerabilities (-a) Specific Package

5\. To check the attack surface

6\. To check the activity that can be vulnerable (We will exploit 2nd activity)

7\. We don’t have access to check what is behind these activity . As it is password protected and we don’t have PIN, it shows incorrect PIN

8\. you can start an activity(AccesscontrolViewActivity) and bypass these kind of authentication that should prevent you from launching it.

This is just the basics of how Drozer does its magic. For depth Knowledge of Drozer kindly go to **Hack Tricks Link**

Wrapping up **Part 3**, we’ve cracked the code and delved into the intricacies of Android app decoding. Get ready for the next stage in our cybersecurity saga as we seamlessly transition into [**Part 4**](/@hackersdump0/diving-deep-a-comprehensive-guide-to-android-penetration-testing-part-4-9bba2880b8cb). Stay connected as we continue to unravel the layers of Android Penetration Testing, anticipating more insights and challenges in the upcoming installment. The journey continues! 🚀

Feel free to connect with me on LinkedIn for more discussions and insights related to Android Penetration Testing.

You can find me on LinkedIn at **@Omkar Gaikwad**
