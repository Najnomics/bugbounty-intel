# ADB (Android Debug Bridge) — The Ultimate Cheat Sheet for Developers

- **Source URL:** https://medium.com/@povzayd/adb-android-debug-bridge-the-ultimate-cheat-sheet-for-developers-d3af4863fa81?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@povzayd
- **Fetched:** 2026-11-17
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 12107)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### If you’ve ever built, debugged, or reverse-engineered Android apps, ADB has probably been your best friend. 

The Android Debug Bridge (ADB) is a versatile command-line tool that lets you communicate with Android devices — whether connected via USB or over Wi-Fi.

With ADB, you can manipulate device files, gather system information, simulate user input, or even record the screen — all without touching the phone. 

Below is a comprehensive, hands-on cheat sheet to supercharge your ADB workflow.

#### 🧩 Device Management

List all connected devices

adb devices

This shows all devices recognized by ADB along with their serial numbers and connection status.

#### 🖇️ Connect to a device over Wi-Fi


adb connect \<device\_ip>:5555

Useful when you want to debug wirelessly. 

Make sure you’ve enabled *USB debugging* first and the device is on the same network.

#### 💻 Open a shell on a specific device


adb -s \<device\_name> shell

Opens a command-line shell on the chosen device. Use it to run Linux commands directly inside the Android OS.

#### ⚙️ Device Properties

- Get all device properties


adb shell getprop

Displays a complete list of system-level properties such as build ID, model, and network configuration.

See a specific property

adb shell getprop "property.name"

For example:


adb shell getprop ro.build.version.release

This shows the Android version the device is running.

#### 📂 File Operations

#### 📤 Send a file to the device


adb push \<local\_file> \<device\_path>

Example:


adb push myapp.apk /sdcard/Download/

#### 📩 Download a file from the device


adb pull \<device\_path> \<local\_directory>

Example:


adb pull /sdcard/Download/log.txt \~/Desktop/

These commands work like SCP — they let you move files easily between your computer and Android.

#### 📸 Screenshots and Screen Recording

#### 🖼️ Take a screenshot


adb exec-out screencap -p > screenshot.png

This captures the current screen and saves it directly to your computer as a PNG image.

#### 📽️ Record the screen


adb shell screenrecord /sdcard/demo.mp4

adb pull /sdcard/demo.mp4 .

Perfect for capturing debugging sessions or in-app demonstrations. 

You can stop the recording anytime with Ctrl + C.

#### 🧠 Simulating User Input

ADB can mimic human interactions on a device — taps, swipes, text entry, or button presses.

Simulate a tap


adb shell input tap \<x> \<y>

Example:


adb shell input tap 500 800

You can find coordinates using P*ointer Location* under Android Developer Options.

#### ⌨️ Type text


adb shell input text "HELLO"

To insert spaces, replace them with %s, e.g.:


adb shell input text "HELLO%sWORLD"

#### 🔘 Press a button


adb shell input keyevent \<keycode>

Example:


adb shell input keyevent 26 # Power button

adb shell input keyevent 3 # Home button

adb shell input keyevent 4 # Back button

#### 📦 App and System Information

List all installed packages


adb shell pm list packages

Use the -3 flag to list only third-party apps:


adb shell pm list packages -3

#### 🔍 Inspect package details


adb shell dumpsys package com.example.app

This gives deep system-level information about an app: **permissions, activities, services, version codes**, and more.

You can also query other subsystems:


adb shell dumpsys battery

adb shell dumpsys wifi

adb shell dumpsys activity

Extremely useful for debugging device states during automation or performance testing.

#### 🔧 Bonus Tips

\- Restart ADB server:


adb kill-server

adb start-server


- Reboot the device:

adb reboot


- Install or uninstall apps:

adb install myapp.apk

adb uninstall com.example.app


#### 🚀 Wrapping Up

ADB is much more than just a debugging tool — it’s a complete bridge between your desktop and Android’s Linux-based environment. 

Once you know these commands by heart, you can configure, automate, and even pentest Android devices like a pro — all without even touching the screen.
