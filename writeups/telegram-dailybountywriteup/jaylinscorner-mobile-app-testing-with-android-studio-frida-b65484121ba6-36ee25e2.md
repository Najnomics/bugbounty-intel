# Mobile App Testing with Android Studio & Frida

- **Source URL:** https://medium.com/@jaylinscorner/mobile-app-testing-with-android-studio-frida-b65484121ba6?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240718011414/https://medium.com/@jaylinscorner/mobile-app-testing-with-android-studio-frida-b65484121ba6
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6583 (id 6583)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Mobile App Testing with Android Studio & Frida

Security testing on Android applications is crucial for ensuring the safety and integrity of mobile apps. For ethical hackers and penetration testers, this process is invaluable. By rigorously testing Android apps, ethical hackers help developers understand potential security flaws and improve their defenses.

Here is an easy way to set up an Android environment to test Play Store Applications to add to your mobile security testing toolkit.

**Prerequisites:** The Android emulator is unable to run on a system without Hyper-V enabled for acceleration. Windows 10 comes preloaded with this by default.

To confirm your system meets the requirements for Hyper-V and/or enable this feature, refer to the Microsoft forum for more guidance:

\~ **Downloading Android Studio**

First, we need to download Android Studio.

- Download Android Studio Koala (2024) on Windows *With Default Settings*

When visiting the Virtual Device Manager, there is a default device present after downloading the Android emulator. You can use this API or download one of your choice (I prefer downloading my own)

Once you select your device, you will prompted to select a system image.

**NOTE: For some reason at this day in time, Frida has been having problems executing the frida-server on API 35. There are currently open issues on GitHub, to keep track, follow these links:**

Next screen, you can verify the configuration of your device.

Once you are finished with your configuration, boot up your device from the virtual device manager with the Play button.

**\~ Rooting the Android Phone:**

**Rooting the device gives us the ability to fully customize the device and have more administrative control.**

- First, we need to ensure we have access to our device through ADB (Android Debug Bridge)
- ADB is a command-line tool that gives us the ability to communicate with the emulated device we have just configured
- This tool comes downloaded by default with SDK Tools once Android Studio is installed, but if it doesn’t you can download it independently.

- Unzip this file into a new folder and navigate to the platform-tools folder
- Open the command prompt from this folder (Type cmd in the platform-tools folder)

`adb devices`
- Run this command to verify that the emulator is active through ADB

1. Download this repository as a full Zip File:

1. Unzip the file and place it into a separate directory
2. Navigate to this location in the command prompt and run

`RootAVD.bat ListAlllAVDs`
Take note in the Android Studio Device Manager of the API # and the System architecture of the system image that you installed on the device in the Device Manager. This will be needed to root the device; we will change our input to our specified configuration

Ex:

rootAVD.bat system-images\**android-20**\google\_apis\_playstore\**x86**\ramdisk.img

We run it, and let it do its work! The device should shut off after this process has been finished.

Cold Boot your device from the Device Manager, and navigate to the settings > “About emulated device” > Click on the Build Number (5 times) to enter Developer Mode

- Now we navigate back to our command prompt and run adb shell to gain a shell directly to our device.
- Next, we will type su, to get root privileges
- A pop-up will appear on the emulated device and you will have 10 seconds to approve that you would like root privileges from the command prompt.

We now have root privileges!

**\~ Downloading Frida:**

Frida is a versatile toolkit for dynamic instrumentation. Think of it as a collection of tools that allow you to inject custom code into running applications in real time.

We can use this tool to inject code into an application we are testing and see if there is an interesting response returned to us.

Navigate to this repository, and download the Frida Server for the configuration of your emulated device.

- I renamed my specific file *frida-server*. After renaming it, we will push it to the temporary folder on the emulated device with:

`adb push frida-server /data/local/tmp`
We then execute adb shell again, and navigate to the /data/local/tmp folder

```
adb shell
cd /data/local/tmp/
```
Change permissions of the file so it can be executed:

`chmod 755 frida-server`
Activate the frida-server on the device with:

`./frida-server`
Open another command prompt in the location where your frida tools are, and run frida-ps.

Frida-ps is a tool apart of the Frida command line tool that lists processes running on the device the frida-server is executed on.

You can run the command below to find out more info about the tool:

`frida-ps -h`
By just running frida-ps and connecting the the device by USB, you will have access to the emulated device running processes.

Simply run:

`frida-ps -U`
With Frida, you can:

- Hook Android functions dynamically.
- Bypass Certificate Pinning dynamically. A function made to make applications more secure
- Dynamically hook APIs
- Create custom modules to perform specific actions in certain applications
- Inject custom JavaScript

and much more!

**Conclusion:**

This is an awesome tool for Android penetration testing or testing an application’s security (with permission, of course). Frida lets you interact with Android apps on a deep level, making it super valuable for developers, testers, and security researchers!
