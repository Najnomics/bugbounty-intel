# “Insights from Android VAPT”

- **Source URL:** https://medium.com/@darshchaudharydc007/insights-from-android-vapt-3b585ca7dbba?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230626224132/https://medium.com/@darshchaudharydc007/insights-from-android-vapt-3b585ca7dbba
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2977 (id 2977)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Are you intrigued by the world of cybersecurity and fascinated by the realm of mobile applications? Android Pentesting might just be the perfect entry point for you. In this blog, we will explore the basics of Android Pentesting and dive into the detailed scenarios of common bugs that can be found in Android applications.

Now, let’s delve into the Android file system and explore its various folders within the file hierarchy. Understanding these folders is essential for Android Pentesting and conducting security assessments. Here are the commonly encountered folders in the Android file system:

1. /boot: Bootable files consisting of the Android kernel and ramdisk
2. /system: The entire Android OS is stored inside this folder. It also consists of the pre-installed system applications which are stored inside /system/app
3. /recovery: This folder is designed for backup and is considered as an alternate boot option.
4. /cache: This folder stores frequently accessed app data and components
5. /misc: Contains miscellaneous system settings
6. /sdcard: This folder is the space that is available to users to store their files and data.
7. /data: This particular folder consists of all user data.

- /data/data: Consists of all applications data installed by the user
- /data/app: Consists of all APKs of the application installed by the user
- /data/system: Consists of files such as gesture.key, password.key
- /data/local/tmp: This folder is used for storing temporary or local files. It can be utilized by various applications for storing transient data.

During Android Pentesting, it is crucial to examine certain files and folders that are typically created during the application’s development process. These files and folders play a significant role in understanding the application’s structure and potential security vulnerabilities. Let’s take a closer look at these important files and folders in the context of Android Pentesting:

1. AndroidManifest.xml: has the structure and metadata of the application. Usually, all permissions, API keys, etc. are stored inside this particular file.
2. Java: This particular folder contains the Java source code files.
3. drawable: All images, videos, gifs, etc. are stored inside this particular folder.
4. layout: A layout defines the visual structure for a user interface, such as the UI for an Android application.
5. mipmap: The image Asset folder that usually contains different icons.
6. colors.xml: Color resource file of the Android application.
7. lib: Contains native libraries with compiled code, for different device architectures.
8. res: Contains predefined application resources, like XML files that define a state list of colors, user interface layout, fonts, values, etc.
9. resources.arsc: Contains precompiled resources. It holds information that will link the code to resources.
10. strings.xml: contains a collection of string resources used for displaying text in the user interface. It serves as a central repository for storing labels, titles, descriptions, error messages, and other UI-related strings.
11. styles.xml: Styles resource file of the Android application.
12. build.gradle: This particular file is used to add various dependencies. This file also has the SDKVersion number and other important details.

Now, let’s shift our focus to the Android Data Storage Model. Android utilizes five primary methods for storing data, each serving different purposes and offering unique characteristics. These storage options play a crucial role in the overall functionality and data management of Android applications. Let’s explore these five ways in which Android stores data:

1. Shared Preferences: Store private data in key-value pairs on the device.
2. Internal Storage: Store private data on the device’s memory.
3. External Storage: Store public data on the shared external storage.
4. SQLite Databases: Stored structured data on private databases.
5. Network Connection: Store data on the web with your Network Server.

Perfect! Now since we have learned the android architecture, let’s learn about how the actual pentesting methodology works!! There are two types of analysis which is usually done while performing Android pentesting.

1. Static Analysis: This means viewing the source code of the APK and finding out vulnerabilities by reviewing the APK. This is kinda similar to Source Code Review. We usually look out for different Intent functions, Sources, and Sinks, Dangerous Permissions, Hardcoded API Keys, etc. This was the reason we went into the details of the Android Architecture.
2. Dynamic Analysis: Dynamic Analysis is all about playing with requests and responses. But here is a catch, like normal Web Pentesting, Sometimes in Android (as well as iOS) the requests and responses are not caught directly. We first need to bypass Root Detection and then bypass SSL Pinning. We will be learning more about this in the upcoming articles.

Now, let’s explore the process of static analysis for Android applications and identify the potential bugs that can be detected through it.

1. CleartextTraffic Enabled for APP:

CWE : 312 Cleartext Storage of Sensitive Information

The “Clear Text Traffic Enabled” bug refers to a vulnerability in an Android application where the app allows unencrypted network communication over HTTP instead of using secure HTTPS connections. This vulnerability is identified by analyzing the AndroidManifest.xml file.

lets, understand what is difference between `android:usesCleartextTraffic=true` and `android:usesCleartextTraffic=false` in an Android application manifest file

The difference between `android:usesCleartextTraffic=true` and `android:usesCleartextTraffic=false` in an Android application manifest file lies in how the application handles network traffic and whether it allows unencrypted (clear text) communication.

- `android:usesCleartextTraffic=true`: This attribute indicates that the application permits clear text traffic over unencrypted HTTP connections. With this setting, the application can send and receive data over HTTP without any encryption. It means that sensitive information, such as usernames, passwords, or other user data, can be transmitted without encryption, posing a security risk.
- `android:usesCleartextTraffic=false`: This attribute signifies that the application does not allow clear text traffic and enforces the use of encrypted connections, typically over HTTPS. With this setting, the application restricts network communication to secure channels, ensuring that sensitive data is encrypted during transmission.

From a pentesting perspective, `android:usesCleartextTraffic=true` is considered a vulnerability or bug. Allowing clear text traffic means that sensitive information can be intercepted by attackers who have access to the network traffic, potentially leading to data breaches or unauthorized access to user data. It is recommended to set `android:usesCleartextTraffic=false` to enforce secure communication protocols and protect sensitive data from interception.

Pentesters analyze the Android application manifest file to identify instances where `android:usesCleartextTraffic=true` is enabled. By finding this configuration, they can highlight the vulnerability and recommend developers to disable clear text traffic by setting `android:usesCleartextTraffic=false`. This is an important step in securing the application's network communication and protecting user data from potential attackers.

- Severity : The severity of this vulnerability is typically classified as low; however, its impact may vary depending on the sensitive information transmitted through the application like, if the application handles highly sensitive information, such as financial data, healthcare records, or personal identification information. In such cases, the risk and potential impact of data exposure are significantly higher. Any unauthorized access or interception of this sensitive data can have severe consequences, leading to legal and regulatory issues, financial losses, and reputational damage for the affected individuals or organizations.

Steps to Reproduce:

To identify the “android:usesCleartextTraffic=true” vulnerability using jadx, a tool for reverse engineering Android applications, follow these simplified steps:

- Install jadx: Download and install jadx from the official repository or preferred source.
- Obtain the target APK: Obtain the APK file of the Android application you want to analyze for the cleartext traffic vulnerability.
- Launch jadx: Open jadx from the command line or using the graphical interface.
- Import the APK: Use jadx to import the target APK by selecting the “Open” or “Import” option within the tool.
- Analyze the decompiled code: Once the APK is loaded, jadx will decompile it and present the source code.
- Search for the vulnerability: Within the decompiled source code, search for the AndroidManifest.xml file.
- Inspect the AndroidManifest.xml: Open the AndroidManifest.xml file to locate the “usesCleartextTraffic” attribute.
- Identify “usesCleartextTraffic=true”: Check if the “usesCleartextTraffic” attribute is set to “true.” This indicates that the application allows clear text traffic, making it vulnerable to potential security risks.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

2\. Debug Enabled for App:

CWE: 489 Active Debug Code

The `android:debuggable="true"` vulnerability refers to a configuration setting in an Android application that allows it to be debugged and analyzed by external tools. When `android:debuggable` is set to true, it enables developers or attackers to attach a debugger to the application, granting them access to sensitive information, including log messages, debug logs, internal data structures, and potentially even modifying the application's behavior.

This vulnerability is a security risk because it exposes the application to potential exploitation and unauthorized access. Attackers could leverage debugging capabilities to extract sensitive data, inject malicious code, or gain insights into the application’s inner workings, making it easier to identify vulnerabilities or weaknesses.

To address this vulnerability, it is essential to set `android:debuggable="false"` in the application manifest file before releasing it to production. This prevents unauthorized individuals from debugging the application and significantly reduces the risk of data exposure and unauthorized access to the application's internals. With debuggable set to false, it restricts the ability to attach debuggers, limiting access to the application’s internals and reducing the risk of unauthorized access, code injection, or information leakage.

- Sevrity: The severity of the “android:debuggable=true” vulnerability in an Android application is generally considered low.

Steps to Reproduce:

- Install jadx: Download and install jadx from the official repository or preferred source.
- Obtain the target APK: Obtain the APK file of the Android application you want to analyze for the debuggable vulnerability.
- Launch jadx: Open jadx from the command line or using the graphical interface.
- Import the APK: Use jadx to import the target APK by selecting the “Open” or “Import” option within the tool.
- Analyze the decompiled code: Once the APK is loaded, jadx will decompile it and present the source code.
- Search for the vulnerability: Within the decompiled source code, search for the AndroidManifest.xml file.
- Inspect the AndroidManifest.xml: Open the AndroidManifest.xml file to locate the “android:debuggable” attribute.
- Identify “android:debuggable=true”: Check if the “android:debuggable” attribute is set to “true.” This indicates that the application can be debugged, potentially exposing sensitive information or vulnerabilities.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

3\. Insecure Data Storage:

Insecure data storage in Android refers to the vulnerability in which sensitive user information is stored in an unsafe manner, making it susceptible to unauthorized access or retrieval. This vulnerability can arise when developers choose weak encryption methods, fail to securely store cryptographic keys, or store sensitive data in easily accessible locations such as shared preferences or local storage. Insecure data storage poses a significant threat to user privacy and can lead to identity theft, and unauthorized disclosure of personal information.

Here are some specific examples of insecure data storage in Android apps:

- Storing passwords in plain text in the app’s local file.
- Storing login credentials or financial information in the app’s shared preferences.
- Storing data in an unsecured local database: If an Android app uses an SQLite database to store sensitive information, but fails to implement proper security measures such as encryption, the data becomes vulnerable to unauthorized access. Attackers can gain access to the device or the app’s database file and extract or modify the stored data.
- Failing to encrypt sensitive data before storing it on the device.
- Granting the app excessive permissions that allow it to access sensitive data.
- Caching sensitive data without proper protection: Some apps cache sensitive data locally to improve performance, but if the cache is not appropriately protected, it can be easily accessed by other apps or individuals with physical access to the device. This can lead to data leaks and privacy breaches.

Files and folders that are commonly affected by insecure data storage vulnerabilities:

- Log files: Log files often contain sensitive information, such as user names, passwords
- SQL databases: Databases can contain sensitive information, such as credit card numbers and social security numbers. If databases are not properly secured, they can be accessed by malicious users.
- Plain text files: Plain text files that contain sensitive information should be avoided. If these files are stored on the device, they can be easily accessed by malicious users.
- XML data stores on manifest files
- Binary data stores
- Cookie stores
- SD card

In the event that sensitive data, such as login credentials, API keys, financial information like credit card numbers, or personal identification data, is discovered within the aforementioned files or folders without the implementation of encryption or suitable obfuscation techniques, it can be classified as an insecure data storage vulnerability.

Severity: The severity classification of this vulnerability is often considered medium to low since sometimes it typically requires physical access to the device for an attacker to exploit it.

Proof Of Concepts for Reference

- During my penetration testing, I use ADB tool to access the path “/data/data/application-packagename/database”. Upon opening the database folder, I discovered a list of files. While examining these files, and I came across a specific file that contained a Username and Password. I have attached the POC for your reference.
- You can use ADB tool to access the above mentioned path or you can use Nox player.

Here is a step-by-step guide on how to access the database folder using Nox Player:

- To access the desired location, please launch the Amaze file management software within the Nox emulator.
- From there, navigate to the Root directory and proceed to open the “data” folder.
- Inside the “data” folder, there will be another “data” folder that you should open.
- Look for the folder with the name corresponding to your target APK package name, and you will be able to access the database and other folders within it.
- Now, you can open and examine each file and folder, and find Insecure Data Storage vulnerability by identifying secrets or sensitive information within the files and folders.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

4\. Hardcoded Credentials:

CWE-798: Use of Hard-coded Credentials

A hardcoded credential vulnerability \`is a security flaw that occurs when sensitive information, such as usernames and passwords, are stored in the source code of an Android application. This information can then be easily accessed by anyone who has access to the source code, including attackers. Hardcoded credentials vulnerabilities can be exploited to gain unauthorized access to an Android application, steal sensitive data, or even take control of the device.

Here’s an example of a hardcoded credentials vulnerability in Android Vapt:

In the source code of an Android application, a developer includes the following line:

- String username = “admin”;
- String password = “password123”;

These hardcoded credentials are then used for authentication within the application, granting access to sensitive features or services. However, this approach presents a significant security risk because the credentials are easily discoverable by reverse engineering the APK file or decompiling the application. Attackers could gain unauthorized access to the application by simply extracting the credentials from the code, compromising the security of user accounts and potentially leading to data breaches.

Severity: The severity of the hardcoded credentials vulnerability depends on the specific user credentials that are discovered and the level of access they provide. The impact also varies based on the type of data or functionality that can be accessed by an unauthorized actor. The potential consequences can range from minimal if the credentials belong to a low-privileged user with limited access, to critical if they grant high-privileged access, allowing unauthorized actors to compromise sensitive data or perform unauthorized actions within the application or associated systems. Therefore, the severity of this vulnerability is directly linked to the level of privileges associated with the compromised credentials and the potential impact on the security and integrity of the application and its data.

Proof Of Concepts for Reference:

During my penetration testing, I actively search for hardcoded credentials within the source code of APK file. In an application that does not have a signup or registration page, I discovered that there are eight distinct user types. Despite this, I managed to find default credentials for one of the users within the main.js file located at the specific path “assets > www > build > main.js”. By using these default credentials on the login page, I successfully gained access to the application as a high privilege user. This allowed me to utilize privileged functionalities and perform actions. I have attached the POC for your reference.

Here’s a step-by-step guide to help you find hardcoded credentials vulnerabilities during your penetration testing:

1. Obtain the APK file: Obtain the APK file of the Android application you want to test. This can typically be done by either downloading the app from official app stores or by using tools like APK Extractor to extract the APK file from an installed application on a device.
2. Decompilation: Use a suitable decompilation tool, such as JADX, apktool to decompile the APK file and retrieve the application’s source code.
3. Code analysis: Analyze the decompiled source code to search for any instances where sensitive credentials might be hardcoded. Look for variables or strings that may indicate usernames, passwords, or API keys.
4. Analyze configuration files: Check for any configuration files, such as XML or JSON, that may contain hardcoded credentials. These files may be accessed through the code or loaded dynamically during runtime.
5. Search patterns: Utilize powerful search functionalities provided by the decompilation tool or text editors to search for common keywords like “password,” “username,” “token,” or other related terms. This helps to identify potential areas of interest where credentials might be present.

- I recommend the following approach: decompile the APK file using a tool like apktool and open the decompiled files in Android Studio. Then, use the “Ctrl + Shift + F” keyboard shortcut to perform a search within the codebase, specifically looking for strings related to credentials, such as “username” or “password”. “Ctrl + Shift + F” allows you to search for a string of text in all of the files in your project, including the source code, the resources, and the Gradle files. You can also specify the scope of the search, such as the current module, the current directory, or the entire project.

And, don’t forget to Validate finding: Once you identify potential hardcoded credentials, validate them by attempting to authenticate or gain access using the discovered credentials.

Recommended Mitigation:

1. Avoid hardcoded credentials: Instead of embedding credentials directly into the source code, utilize secure methods for storing and retrieving credentials, such as using environment variables, configuration files, or a dedicated credential management system.
2. Utilize encryption: If storing credentials is necessary, encrypt them using strong encryption algorithms. This adds an extra layer of protection to prevent unauthorized access even if the credentials are discovered.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

5\. Insecure Logging:

CWE-532 Insertion of Sensitive Information into Log File

Logging is a common practice among developers for tracking and monitoring code execution, including capturing warnings and errors. However, a potential risk arises when developers inadvertently include sensitive data in the logs. In such cases, other applications or unauthorized entities may exploit this vulnerability to gain access to the logs and extract the sensitive information, potentially leading to data theft or unauthorized access.

Insecure logging occurs when an application generates logs that include sensitive data such as:

- personally identifiable information (PII) such as names, addresses, phone numbers, email addresses, and social security numbers.
- Exposure of authentication credentials like usernames, passwords, and access tokens.
- Financial data like credit card numbers or bank account details.
- If developers include any confidential or proprietary information such as API keys, encryption keys, or internal system configurations in logging statements.

I will provide instructions on how to set up pidcat or logcat to generate logs specifically for the target application soon.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

6\. Unauthorized Goggle Map api key:

During one of my penetration tests, I discovered a Google Maps private API key stored in the strings.xml file. By storing the API key in this easily accessible file, it becomes vulnerable to extraction through reverse engineering of the APK file. This allows malicious actors to obtain the API key and potentially misuse it for unauthorized access to Google Maps services or perform other malicious activities.

Proof of Concept:

I strongly recommend referring to mentioned blog that provides more in-depth information about this vulnerability. “[https://ozguralp.medium.com/unauthorized-google-maps-api-key-usage-cases-and-why-you-need-to-care-1ccb28bf21e](https://ozguralp.medium.com/unauthorized-google-maps-api-key-usage-cases-and-why-you-need-to-care-1ccb28bf21e)”.

- Once you have identified the Google Maps API key, visit the following link: “[https://github.com/streaak/keyhacks#Google-Maps-API-key](https://github.com/streaak/keyhacks#Google-Maps-API-key)". This resource can be used to assess whether the API key is vulnerable or has any known security issues.
- Another option for validating the vulnerability of the Google Maps API key is to visit “[https://googlekey.blindf.com/](https://googlekey.blindf.com/)". This website provides a convenient method to check if the API key is vulnerable or not by entering the key into an input box. However, as this involves sharing the target or client application’s API key with a third-party service, which carries certain risks.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

6\. Insecure Firebase Database

Firebase, a popular backend-as-a-service (BaaS) platform offered by Google, provides developers with a robust and scalable solution for managing app data. However, if not properly secured, Firebase databases can become vulnerable to unauthorized access and data breaches.

This vulnerability arises when developers fail to implement proper access controls and security measures within their Firebase database configurations. Attackers can exploit this flaw by leveraging weak or missing authentication mechanisms, misconfigured security rules, or poor data validation practices. Once an attacker gains unauthorized access to a Firebase database, they can manipulate or steal sensitive user data, compromise user privacy, and potentially disrupt the functionality of the affected Android app.

In an Android app, developers commonly store the Firebase Database URL in a configuration file or a dedicated class. Here are the common files where you may find the Firebase Database URL:

1. `google-services.json`: This file is usually provided by Firebase when setting up an Android app with Firebase services. It contains configuration information, including the Firebase Database URL. The URL can be found under the `"firebase_url"` field in the JSON file.
2. `build.gradle` (App-level): The `build.gradle` file for the app module often contains dependencies and configuration settings. It may include the Firebase Database URL as a variable or a constant. Look for any references to `firebaseDatabaseUrl` or similar variables.
3. `strings.xml`: Developers sometimes store the Firebase Database URL as a string resource in the `strings.xml` file located in the `res/values/` directory. Look for a string resource with a key like `"firebase_database_url"` or any custom key used by the developer.
4. Custom configuration files: Developers might create their own configuration files to store app-specific settings, including the Firebase Database URL. These files could have any name or location, so it’s essential to search for any custom configuration files within the app’s source code.

After identifying the Firebase Database URL during an Android VAPT, a common approach to confirming its vulnerability involves adding **.json** at the end of the URL like “[https://msdict-dev.firebaseio.com**/.json**](https://msdict-dev.firebaseio.com)”, By doing so, you can assess the response to determine if the database is vulnerable to insecure Firebase database vulnerabilities.

If the response returns a “permission denied” error or restricts access, it suggests that the database is not vulnerable. However, if the response discloses data or returns null values, it indicates vulnerability to insecure Firebase database issues, potentially allowing for further exploitation.

To learn how to exploit the insecure firebase database vulnerability, visit the following links:

[https://hackerone.com/reports/684099](https://hackerone.com/reports/684099)

[https://medium.com/@Dhamuharker/firebase-allow-anonymous-read-and-write-access-63be48a7cef4](/@Dhamuharker/firebase-allow-anonymous-read-and-write-access-63be48a7cef4)

Thank you for reading the blog. I hope it proves helpful for beginners in the field of Mobile Pentesting.
