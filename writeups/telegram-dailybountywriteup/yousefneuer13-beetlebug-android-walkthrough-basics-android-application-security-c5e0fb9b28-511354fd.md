# Beetlebug Android Walkthrough & Basics Android application security

- **Source URL:** https://medium.com/@yousefneuer13/beetlebug-android-walkthrough-basics-android-application-security-c5e0fb9b284b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240603063248/https://medium.com/@yousefneuer13/beetlebug-android-walkthrough-basics-android-application-security-c5e0fb9b284b
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5769 (id 5769)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Beetlebug Android Walkthrough & Basics Android application security

Hello researchers, How is your day? 

My name is Youssef Elsheikh. I’m a security researcher. Today we will talk about Beetlebugs.

Beetlebug is an Android application that aims to inspire interest in mobile application security. It is geared towards developers, mobile penetration testers, and bug hunters. Features include tracking the user’s progress, flag completion state, and so much more!


Prerequisites and install the lab

1-we will need any emulator (in this writeup I will use android studio )

2-adb (Android Debug Bridge )

3- jadix-gui (Command line and GUI tools for producing Java source code from Android Dex and Apk files) you can learn more about jadix from here : [https://github.com/skylot/jadx](https://github.com/skylot/jadx)

4- You can download the application from here : 

[https://github.com/hafiz-ng/Beetlebug](https://github.com/hafiz-ng/Beetlebug) 

5- basics of Java


# **Hardcore secrets**

Let’s open “Jadx-GUI” to see how this application works. 

Drag the apk and drop it in “jadx-gui”; then the files will appear.

There are some checks we will do first.


1. Check the “AndroidManifest.xml” file. 

The “AndroidManifest.xml” file is a crucial part of an Android application as it provides the Android system with essential information about the app’s components, permissions, configurations, and requirements, enabling the system to properly install, manage, and run the application on Android devices. 

“Resources/AndroidManifest.xml”

2-Check Strings.xml 

Strings.xml in Android development serves as centralized storage for string literals, facilitates localization and internationalization, promotes code reuse and consistency, improves accessibility, and enables easy editing and maintenance of text content in your Android application. 

Sometimes developers forget important and sensitive data.You will find Strings.xml in the path “Resources/resources.arsc/res/values/strings.xml”

Now what? 

We want to know how this activity works. so? We want the name of the activity.


adb shell dumpsys window | findstr /i mFocused Dumpsys is a tool that runs on Android devices and provides information about system services.

findstr: search for the specific word you want (because I’m using Windows, not Linux; you can use the “grep” in Linux).

Let’s review and analyze this code. 

This code is used to unlock a folder using a secret PIN input. The code checks the PIN entered by the user (V98bFQrpGkDJ == user input), and if it is correct, it unlocks the folder and performs certain actions. If the PIN is empty, it displays a message asking the user to try again and shows an error message.

So let’s search for this value (V98bFQrpGkDJ) to see if it leaks here or there.

Here we go! We found the key! As you can see, we found it in the strings.xml file, hardcoded.

Let’s move on to the other challenge:

# **Embedded Secret**

Explain the code: when the user inputs the value of the promo code, it will get a 50% discount; if he doesn’t enter the correct value of the promo code, it will show “Wrong discount code.” 

Let’s search to see if the promo is stored in the code, like a plain text or strings.xml file.

Hold CTRL and mouse over the specific variable. 

quick note: 

You can get additional information about a word or code element by quickly viewing its definition or declaration, displaying the type and input/output information of a specific method, and accessing related documentation or comments. 

This feature helps you understand code, explore APIs, and navigate within large code projects quickly and easily without leaving the code editor.

When you click on it, it will show you the declaration of the variable and the promo code to get you the discount.

I submit the promo code, then I get a 50% discount, and as you can see, I now have a new price, so let’s check if there are any restrictions or rate limits for using the promo code many times.

As you can see, when I try to submit the promo code many times now, I’m able to buy the product for free!

# **Data Storage**

**Shared preferences** 

In this challenge, we will talk about how developers store data in an insecure way.

When you try to sign up, a flag box will appear. As you can see from the behavior of the activity, you sign up and then login successfully, so nothing suspicious here. So let’s check the source code to know what is happening here.

Code explain: when the user fills out the form, it will store the data on the device and appear the flag box to put the flag. If you don’t input anything, it will show you error messages like “UUsername cannot be blank and “ Password field is empty.”.

In the second block, if you submit the right flag, it will add to your point and pass the challenge; if you submit the wrong flag, it will show “Try again.” 

If we open Jadx for analysis, the code will find the flag, but I want to know where the developer stores the data. I’m just submitting there.

We can use this command to get into the device.

`adb shell` Can you see the difference? In the first line, it says where you exist on your PC. In the second line, it says where you exist on the device (emulator).

Let’s enter the application installation path.

`cd data/data/app.beetlebug/` cd: change directory 

then let’s check the directories here using ls: 

Note: We use ls to list all directories and files in the directory.

As you can see, we found a directory with the name “shared\_pref\_flag.” Let’s check it out.

 `cat shared_pref_flag.xml` # **External Storage**

Code explain: it’s similar to the previous code that takes input and does a message error if it’s blank, but there is a difference. The application creates a file called “user.txt” and stores the data inside it, but I found the flag as plain text. 

Note: In this challenge, there are some issues with the storage, so we take the flag from the source code.!

If we notice the behavior of the application, we will see that it will expose the path of storage.

# **SQLite Storage**

Let’s check the behavior of the application. As you can see, when I enter a complex password, it shows me that the password is saved, so there is nothing unusual here. Let’s check the code to see if there are any leaks or something. Can I use it.

code explain: The developer specifies regex for the user to choose a complex password; there is nothing here; let’s check the application package.

I checked every file in “shared\_prefs” but I couldn’t find anything, so I moved on to review the code again. Line by line, I noticed that line, so I clicked on it to see what it was..

So I started to read the code, and I found the name of the file “DB\_NAME” which may contain the flag and the password.

So I entered the “databases” directory and viewed the file. 

then I replace the “DB\_NAME” with the real value we found in the code, and you will get the flag to submit it.

# **Insecure Database**

What is SQL injection? 

An SQL injection is a security flaw that allows attackers to interfere with database queries in an application. 

Impact:

This vulnerability can enable attackers to view, modify, or delete data they shouldn’t access, including information about other users or any data the application can access. Such actions may result in permanent changes to the application’s functionality or content, or even compromise of the server or denial of service.

As you can see, when we search for a random user name, we will see (not found). Let’s add a quote mark (‘).

nothing happened It’s suspicious for me anyway. Let’s enter a logical operation to test this search bar.

As you can see we solve the challenge but let’s understand the payload :

zz’ : when you add the quote you end the line in the code 

OR true condition : From a programming perspective, when using the “OR” conditional 

If one of the two conditions is true, the query is implemented. Don’t forget to close your query with a comment or semicolon.

```
The original code be like this :
"SELECT * FROM sqliuser WHERE user = '"
when you add your input :
"SELECT * FROM sqliuser WHERE user = 'zz'OR 2=2;"
```
I could see the query from Logcat, then I noticed it in source code using Jadx.

# **Firebase Database**

Firebase is a platform developed by Google that provides a suite of tools and services for building and managing web and mobile applications. It offers features such as real-time databases, authentication, hosting, cloud storage, machine learning, and analytics, among others. Developers use Firebase to streamline the development process, improve app performance, and enhance the user experience by leveraging its robust backend infrastructure and ready-to-use functionalities.

Firebase Database Misconfiguration

Let’s open Jadx and see if we can see something useful in the code or search for leaked data that could be useful for our hunt.

Nothing important here; let’s dig.

You can search using the keyword “firebase,” but you will have a lot of results to review and analyze. If you add the underscore \_\_, you will get fewer results. 

As you can see, I found a “firebase\_database\_url.” This URL points to the location where your app’s data is stored in the cloud, allowing your application to read from and write to the database in real-time. It is a crucial setting that connects your front-end application to the back-end database, enabling seamless data synchronization and management across devices and users.

You can add “.json” after the URL like this: 

“[www.example.com/.json](http://www.example.com/.json)" to access the data in JSON format.

additional stuff : if u enter to this website [https://jsonformatter.curiousconcept.com/#](https://jsonformatter.curiousconcept.com/#) and copy and paste all the data you have been found the website will handle and arrange it to you can read it easily

`It is important to be organized to be a successful penetration tester.`
# **Sensitive Info Disclosure**

In the last challenge for the writeup, we will talk about something important. 

In this activity, the user enters information about his credit card and then pays (don’t enter real numbers). Alright, let’s see the code.

As you can see in {log.e} 

log.e: is a valuable tool for Android developers to log error messages and troubleshoot issues during the development and testing phases of their applications. 

interesting! 

Let’s use Logcat to view the logs and what’s happened there. 

Note: When you log in, Logcat will see a lot of things and understand nothing, so search with a tag; in our case, it’s 

“beetle-log”

The application exposes credit card numbers in logs

summary, logging sensitive data like credit card information or personally identifiable information (PII) can have severe consequences

# **Additions stuff :**

If you have any comments, let me know. 

Wait for Part 2.

Social Media:

[LinkedIn](https://www.linkedin.com/in/yousef-elsheikh-b1573a1b0/)
