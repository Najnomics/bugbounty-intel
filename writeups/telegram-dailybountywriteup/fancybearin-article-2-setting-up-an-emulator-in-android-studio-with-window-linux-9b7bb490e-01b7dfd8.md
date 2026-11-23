# Article 2

- **Source URL:** https://medium.com/@fancybearIN/article-2-setting-up-an-emulator-in-android-studio-with-window-linux-9b7bb490edb7?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250505190722/https://medium.com/@fancybearIN/article-2-setting-up-an-emulator-in-android-studio-with-window-linux-9b7bb490edb7
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9019 (id 9019)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Article 2: Setting Up an Emulator in Android Studio with Window ,Linux

**Setting Up an Android Emulator for Pentesting (Pixel 6 API 30, No Play Store)**

# 1. Installing Dependencies

Before setting up Android Studio, ensure all dependencies are installed. This includes:

- Android Studio
- ADB (Android Debug Bridge)
- Frida
- Burp Suite (for intercepting network traffic)

# 2. Setting Up Android Studio for Pentesting (Windows & Linux)

The method used in this guide relies on the **Android Virtual Device (AVD)** from Android Studio. AVD supports Mac computers with ARM processors, making it an excellent choice for this approach.

## Steps:

1. Download **Android Studio** from the [official website](https://developer.android.com/studio).
2. If using **Mac with an Apple Silicon (ARM) chip**, select **Mac (Apple Chip)** when downloading Android Studio.
3. Install Android Studio and set up the **Android SDK 14**.

# 3. Creating an Android Emulator

1. Open **Android Studio** and navigate to **AVD Manager**.
2. Click **Create Virtual Device** and select **Pixel 6**.
3. Choose **API 30** as the system image, ensuring you select the version **without the Play Store**.
4. Set the **target to R (Android 11)** and proceed with the emulator creation.

# 4. Troubleshooting Emulator Startup Issues

- If the emulator does not launch properly (e.g., stuck on the boot screen), restart your system.

# 5. Configuring Proxy for Intercepting Traffic

**Case 1: Burp Suite on Linux, Android Studio on Windows**

1. Open **VMware settings** and set the Linux VM network adapter to **NAT**.
2. Check the Linux system’s IP address (e.g., `172.168.2.14`).
3. Open **Burp Suite** and set the proxy to `172.168.2.14:8080`.
4. Remove the default Burp proxy `127.0.0.1:8080`.

**Case 2: Both Burp Suite and Android Studio on the Same System**

- Simply use the system’s IP address to configure Burp Suite.

**Adding Proxy to Emulator:**

1. Open **Device WiFi Settings**.
2. Click on the connected WiFi network and select **Edit**.
3. Add a **manual proxy** and enter the Burp Suite proxy details.
4. Open a browser on the emulator and download Burp’s CA certificate from [http://burpsuite](http://burpsuite.)
[.](http://burpsuite.)
5. Install the certificate in the emulator.

# 6. Downloading APKs for Pentesting

- You can use [Evozi APK Downloader](https://apps.evozi.com/apk-downloader/) to download APK files for testing.

# 7. Verifying Frida Installation

1. Run `frida-ps -Uai` to check if Frida services are running.
2. **Windows users:** If you encounter an environment variable error, check if Frida is installed in the correct location.
3. **Linux users:** If a Python environment issue occurs, fix it with:

`mkdir ~/python python -m venv ~/python`
# 8. Setting Up Frida Server

1. Download the Frida server matching your emulator’s architecture.
2. Push the Frida server binary to the emulator:

`adb push frida_server /data/local/tmp/`
3\. Grant necessary permissions:

`adb root adb shell chmod +x /data/local/tmp/frida_server`
4\. Start the Frida server:

`adb shell /data/local/tmp/frida_server &` 5\. Confirm that Frida is running:

`adb shell ps | grep frida`
6\. If you see a process named `frida`, it means the server is running.

# 9. Performing SSL Pinning Bypass with Frida

- Use Frida scripts to bypass SSL pinning in pentesting applications.
- Run the appropriate Frida SSL pinning bypass script for your target application.

# Github automation

[https://github.com/FancybearIN/Anoy](https://github.com/FancybearIN/Anoy)

This setup ensures your emulator is correctly configured for Android pentesting, including network interception and Frida-based dynamic analysis.
