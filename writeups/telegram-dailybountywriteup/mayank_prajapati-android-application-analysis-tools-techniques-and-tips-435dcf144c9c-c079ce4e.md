# Android Application Analysis

- **Source URL:** https://medium.com/@mayank_prajapati/android-application-analysis-tools-techniques-and-tips-435dcf144c9c?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250421123847/https://medium.com/@mayank_prajapati/android-application-analysis-tools-techniques-and-tips-435dcf144c9c
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9407 (id 9407)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Android Application Analysis: Tools, Techniques and Tips

Hi Guys,

In this blog we would cover how can we setup environment/tools required for android application penetration testing. Mostly we would focus on basic part that includes tools setup, debugging emulator issues, frida/objection setup for SSL and root detection bypass and much more. Lets start:)

# Topics that we will cover📗

1. Android Emulators
2. Setting up ADB (Android Debug Bridge)
3. Installing Frida and Objection
4. Pulling APKs from Android Device
5. Invoking Activities (exported=”true”)
6. Configuring Burp with Android Device/Emulator
7. SSL Pinning Bypass using Objection
8. SSL Pinning Bypass using Frida

# Android Emulators📱

It is a virtual device that mimics the behavior of a real android device on your computer. It allows us to assess Android applications without requirement of a physical device. There are large number of emulators that could be utilized for this purpose. Some of those are Memu, Genymotion, Nox Player etc.

## Resolving Empty adb Devices Output in Nox Player⏯️

I had challenges setting up Genymotion and Memu Player in my computer . Hence, I will be proceeding with Nox Player. If you cannot list your devices using adb then you can use this as a quick fix.

You might see adb error as below and adb devices would not list anything.

This is because NOX comes with its own adb that is causing conflict here. We can simply resolve this issue by connecting over a well known local port 62001 which NOX uses.

# ADB (Android Debug Bridge)🌉

ADB aka Android Debug Bridge is a command-line tool that allows us to communicate and control Android devices or emulators from main host.

Download SDK Platform Tools for Windows from the below link.

Extract the zip files and add the directory of platform-tools in your environment variables.

# Installing Frida and Objection🔨

## Frida

Frida is a toolkit that lets us spy on, intercept, and modify what an app is doing while it’s running without needing to modify the app’s code or recompile it.

```
pip install frida-tools
frida --version
16.7.13
```
In our case frida version is 16.7.13, accordingly only we have to download the frida-server script. Lets grab the architecture of our android.

`adb shell getprop ro.product.cpu.abi`
It was **x86**. Navigate to frida github repo given below, expand the Assets and search for your required version. In our we are searching for: **frida-server-16.7.13-android-x86**

Download and unzip this file. It should contain a file, rename it as frida-server. We will push this file in ***/data/local/tmp*** directory in our android device or emulator that would be helpful in bypassing root and SSL Pinning checks.

## Objection

We can install objection using a simple pip command. It automates most of the tasks in android SSL pinning and root detection bypass process in runtime.

`pip install objection`
# Pulling APKs from Android Device using adb🪢

Install the application from Play Store on Android emulator (Nox Player). Let’s first identify the application's package name. An easy way to get the package name is by browsing the app on the Google Play Store using Chrome or any browser — it’ll be visible in the URL as shown below.

Now we can list the path using adb.

`adb shell pm path com....`
Let’s pull the APK file (base.apk) on host machine.

`adb pull /data/app/com.PACKAGE_NAME/base.apk App.apk`
# Invoking Activities (exported=true)🔐

When an Activity is marked with exported=”true” in the application AndroidManifest.xml file, it indicates that the other applications/processes can invoke this activity. From where would you get AndroidManifest.xml file?? This file you can simply read by reversing the application using tools such as JADX-GUI, apktool etc.

`adb shell am start -n PACKAGE_NAME/ACTIVITY_NAME`
# Configuring Burp with Android Device📲

Import certificate from Burp in der format from Proxy tab and rename it with extension as .cer

Push this certificate into Android Device in Download folder.

`adb push burpca.cer /sdcard/Download`
Install this certificate in the device.

Do proxy settings in your android device and configure Burp Suite accordingly. It is mandatory to select **All Interfaces** while creating a new Proxy Listner in BurpSuite.

Browse any URL in android browser and confirm if the traffic getting intercepted by the burp Proxy.

# SSL Pinning Bypass using Objection👨💻

```
adb shell
cd /data/local/tmp
chmod +x frida-server
./frida-server
```
Now run the objection commands as shown below in other window.

```
objection -g PACKAGE_NAME explore
android sslpinning disable
```
# SSL Pinning Bypass using Frida👨💻

```
adb shell
cd /data/local/tmp
chmod +x frida-server
./frida-server
```
Now run any code share SSL Pinning bypass script using the below command in another window.

`frida --codeshare SCRIPT_NAME_ON_CODESHARE -f PACKAGE_NAME -U`
We can find above command while we navigate to different projects in codeshare.

**Codeshare link:**

Hope you find this blog useful:) 

Thanks for reading..😇
