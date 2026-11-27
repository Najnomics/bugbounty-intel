# Diving Deep

- **Source URL:** https://medium.com/@hackersdump0/diving-deep-a-comprehensive-guide-to-android-penetration-testing-part-2-9c33c319a696?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240110135150/https://medium.com/@hackersdump0/diving-deep-a-comprehensive-guide-to-android-penetration-testing-part-2-9c33c319a696
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4454 (id 4454)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Diving Deep: A Comprehensive Guide to Android Penetration Testing — Part 2

## Preparing Your Ground: Setting Up for Android Penetration Testing

--

Welcome back, cyber explorers! If [**Part 1**](/@hackersdump0/diving-deep-a-comprehensive-guide-to-android-penetration-testing-part-1-392cf9abf93f) was our map to navigate the Android Abyss, consider **Part 2** as the toolkit to set up camp in the digital realm. In “**Preparing Your Ground: Setting Up for Android Penetration Testing**,” we’re diving into the nitty-gritty of getting ready for the real action. Think of it as gearing up for an epic adventure — getting your tools sharp, your environment ready, and your mindset geared for the challenges ahead. So, tighten your virtual shoelaces, because we’re about to kick off the next phase of our Android Penetration Testing expedition! 🛠️💻🚀

## **Android device**

The primary asset for Android penetration testing is an **Android device**, and it should be **rooted**. Rooting is like giving your device superpowers, allowing for enhanced control and customization. You can root the device with Magisk. Here, you can download the **Magisk** 

For rooting the device you can go through the following reference 

[https://preethiraopn1992.medium.com/rooting-android-phones-using-magisk-d56ace15e9bb](https://preethiraopn1992.medium.com/rooting-android-phones-using-magisk-d56ace15e9bb)

[https://www.androidauthority.com/root-android-277350/](https://www.androidauthority.com/root-android-277350/) 

[https://medium.com/@MosamShambharkar/rooting-android-all-you-need-to-know-from-scratch-4b9fee06f90c#:\~:text=Rooting%20is%20a%20process%20that,t%20normally%20allow%20you%20to](/@MosamShambharkar/rooting-android-all-you-need-to-know-from-scratch-4b9fee06f90c#:~:text=Rooting%20is%20a%20process%20that,t%20normally%20allow%20you%20to).

## **To setup an Emulator(Memu) of Android Device**

For those without an Android device, there’s a viable alternative — an emulator. Emulator (Memu), specifically designed for Windows PCs, serves as an Android emulator software. This tool enables users to simulate a virtual Android environment on their desktop or laptop computers, facilitating the running of Android apps for purposes such as testing, development, and entertainment. So, even if you don’t have an Android device at hand, Memu opens up a virtual gateway to the Android experience on your computer. 🖥️📱✨

**To download Memu Emulator , Click here to Download.**

## **Setting up Android Debug Bridge (ADB)**

Android Debug Bridge is a client-server program that allows the user to interact with the emulator or the connected Android device.

The default port used by the client for ADB communication is 5037 in all cases where the device uses ports ranging from 5555 to 5585.

Here is the [**Link**](https://androidsdkmanager.azurewebsites.net/Platformtools) to download the Platform tools (ADB) for windows, linux, mac. Add these platforms tool to your environment variables to access adb from any where. 

**Basics of ADB**Once the device is connected via a USB, we could simply type in adb devices

To Restart the ADB Server

To install APK file in device with ADB

To list all the Installed Packages in Android

To execute the shell

To dump all the Memory Consumption of all the list applications

To read the logs of events of an Android device

The -d flag here specifies dumps of the full log file and exits

The -f flag specifies to write to a file instead of printing on the terminal

The Log file saved in **/data/local/** in Android Device

For Adb cheatsheet you can go through given reference 

[https://www.hackingarticles.in/android-pentest-lab-setup-adb-command-cheatsheet/](https://www.hackingarticles.in/android-pentest-lab-setup-adb-command-cheatsheet/)

[https://3os.org/android/adb-cheat-sheet/](https://3os.org/android/adb-cheat-sheet/)

## **APK TOOL**

One of the most important tools in Android reverse engineering is APKTool.

**To download APKTool, Click here to Download (These APK tool is GUI Based )**

## **Jadx GUI**

JADX GUI is a graphical user interface (GUI) tool used for decompiling and analyzing Android application (APK) files. It allows developers and security researchers to reverse engineer Android apps by converting bytecode (DEX files) into Java source code. With JADX GUI, users can explore an app’s source code, inspect its functionality, and understand its inner workings for various purposes, including debugging, security analysis, or learning from existing apps. The tool simplifies the process of decompilation and makes it more accessible to those without deep expertise in reverse engineering.

To download JADX GUI**, Click here to Download.**

## **Drozer**

Drozer, also known as “drozer2,” is an Android security assessment and penetration testing tool used by cybersecurity professionals and ethical hackers. It helps identify vulnerabilities and potential security issues in Android applications by providing dynamic analysis capabilities. Drozer allows users to interact with an Android app’s components, test for security weaknesses, and generate reports to improve app security.

Below are links to download Drozer **Drozer installer and Drozer Agent**

## **Frida**

Frida is an open-source dynamic instrumentation toolkit for injecting code into running processes. It’s used for real-time inspection and manipulation of software behavior on various platforms, such as Android, iOS, Windows, macOS, and Linux. Frida is valuable for security research, reverse engineering, and dynamic analysis. It allows developers to interact with and modify the memory and execution of target applications using custom JavaScript code. It’s a versatile tool for various applications, including security testing and debugging.

**Frida installation in Windows  Open Command Prompt and enter the command #pip install frida-tools #pip install frida**Verify the installed frida version using below command

**#frida –version**

Note down the installed version for installing Frida server in mobile devices

## **Setting up Frida-server on Android Emulator/Device**

**What is Frida-server ?**

Frida tools need the Frida server because they operate in a client-server architecture. The Frida server is responsible for handling communication between the Frida tools (client) and the target application (server).


*Before installing Frida on Android, you need a rooted Android device or rooted emulators.*

First, you need to download the Frida server for your specific android arch version (arm, arm64, X86, X86\_64).

**Connect the device to ADB**To find out the arch version of the device, run the following command.

**#adb shell getprop ro.product.cpu.abi**

As I have my android arch as **x86\_64**We can download the Frida server from their official release page (

[https://github.com/frida/frida/releases](https://github.com/frida/frida/releases)).

Download according to your frida version that you have downloaded before in the windows.

As I have 16.0.19 so i have downloaded frida -server 16.0.19 — android x86\_64.xz

Now push these file to android device

# **adb push /path/to/frida-server-file /data/local/tmp**

Now go to android shell and check the file has been successfully pushed in the location

Give permission to execute the frida-server

Now just execute the file with ./frida-server

## **Objection**

A runtime mobile exploration toolkit, powered by Frida, built to help you assess the security posture of your mobile applications, without needing a jailbreak.

## **MobSF**

Mobile Security Framework (MobSF) is an automated, all-in-one mobile application (Android/iOS/Windows) pen-testing, malware analysis and security assessment framework capable of performing static and dynamic analysis.

**Installation of Mobsf in kali**

[https://allabouttesting.org/quick-tutorial-mobsf-installation-on-linux-windows/](https://allabouttesting.org/quick-tutorial-mobsf-installation-on-linux-windows/)

## **Burp Suite**

Burp Suite is a cybersecurity tool for web application testing. It acts as a proxy, scans for vulnerabilities, and enables manual and automated testing. Its features include intercepting and analyzing web traffic, detecting security flaws, and customizing extensions. Burp Suite helps professionals secure web applications by identifying and addressing potential vulnerabilities.

**Download Burp suite**

[https://portswigger.net/burp/communitydownload](https://portswigger.net/burp/communitydownload)

**Download crack Burp suite** 

[https://mega.nz/folder/LB9XhDob#LsE1tE7H-YxGDfwgjCB40g](https://mega.nz/folder/LB9XhDob#LsE1tE7H-YxGDfwgjCB40g)

As we conclude **Part 2**, stay tuned for the seamless transition into [**Part 3**](/@hackersdump0/diving-deep-a-comprehensive-guide-to-android-penetration-testing-part-3-99e86d021190), ensuring a connected and cohesive exploration of our Android Penetration Testing journey.

Feel free to connect with me on LinkedIn for more discussions and insights related to Android Penetration Testing.

You can find me on LinkedIn at **@Omkar Gaikwad**
