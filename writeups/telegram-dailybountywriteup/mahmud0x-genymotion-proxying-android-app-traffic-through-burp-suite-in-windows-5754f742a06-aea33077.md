# Genymotion — Proxying Android App Traffic Through Burp Suite in Windows

- **Source URL:** https://medium.com/@mahmud0x/genymotion-proxying-android-app-traffic-through-burp-suite-in-windows-5754f742a06?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251004141015/https://medium.com/@mahmud0x/genymotion-proxying-android-app-traffic-through-burp-suite-in-windows-5754f742a06
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3072 (id 3072)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Genymotion — Proxying Android App Traffic Through Burp Suite in Windows

First install genymotion from [here](https://www.genymotion.com/download/). Make sure to pick the version with virtualbox.

After that open genymotion and click the (+) icon

Now select any device and click next

Then start the device. Now we are required to install openssl.

Download from [here](https://slproweb.com/download/Win64OpenSSL_Light-3_1_1.exe) and install it. After the installation. Search for openssl and run it.

We need to install this certificate on our virtual android device. But first get this certificate from burpsuite.

Now we have out .der certifcate. But we are required to convert it .pem extension.

Run the below commands in the previously opened openssl terminal.

`openssl x509 -inform DER -in burp.der -out burp.pem``openssl x509 -inform PEM -subject_hash_old -in burp.pem`
Now install ADB from [here](https://www.xda-developers.com/install-adb-windows-macos-linux/) and extract it. Go to the extracted folder and open a terminal there. Run this commands

adb devices

adb connect 192.168.170.102:5555

adb root

adb remount


Now push the burp.pem into sdcard of the android device.

`adb push burp.pem /sdcard/`
Now open a adb shell using `adb shell`commandand run the below commands

```
mv burp.pem 9a5ba575.0
mv /sdcard/9a5ba575.0 /system/etc/security/cacerts/
chmod 644 /system/etc/security/cacerts/9a5ba575.0
```
After the use exit command to leave the adb shell. Then run these commands:

`adb shell settings put global http_proxy localhost:3333`
Now let’s configure burp to listen our requests.

Again go back to the adb terminal and run this command

`adb reverse tcp:3333 tcp:8082`
Let’s test if it works or not.

Result:

It works.
