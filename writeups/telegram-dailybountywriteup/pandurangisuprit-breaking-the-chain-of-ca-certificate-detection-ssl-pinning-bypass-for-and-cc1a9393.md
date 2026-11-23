# Breaking the chain of CA Certificate detection & SSL Pinning bypass for Android applications

- **Source URL:** https://medium.com/@pandurangisuprit/breaking-the-chain-of-ca-certificate-detection-ssl-pinning-bypass-for-android-applications-65c4ac66d9f2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260314133141/https://medium.com/@pandurangisuprit/breaking-the-chain-of-ca-certificate-detection-ssl-pinning-bypass-for-android-applications-65c4ac66d9f2
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8892 (id 8892)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Breaking the chain of CA Certificate detection & SSL Pinning bypass for Android applications (Native & Flutter)

Hi there, my name is Suprit Pandurangi aka s3ctat0r let's get started without any further delay!! While testing an Android app, I encountered one with proxy certificate detection enabled. This blog sets out to bypass this check, potentially allowing me to intercept the application’s traffic.

I assume you have prior experience in Android testing, as this blog covers advanced techniques. When testing native mobile applications, the device is configured to route traffic through a proxy tool like Burp Suite with its CA certificate installed. However, the challenge lies in the app detecting the proxy certificate and restricting execution.

Let us call this Android application as “XYZ”

To ensure the smooth execution of the XYZ application, I removed the installed CA certificate from the device’s root certificates. Now, let me introduce you to HTTP Toolkit, which we used to capture the device’s traffic.

HTTP Toolkit is an advanced debugging tool for intercepting, inspecting, and modifying HTTP(S) traffic across web and mobile applications. It simplifies API testing, SSL pinning bypass, and traffic analysis with an intuitive interface.

When I was running HTTP Toolkit to capture the device traffic, the target application rejected to share its traffic due to SSL Pinning check as shown below:

For using HTTP Toolkit, I had connected the tool with ADB services and configured with Upstream proxy to the loopback IP address where Burp suite was installed.

NOTE: To use Upstream proxy services, licensed version of Toolkit is required.

While using Frida and its script to bypass SSL pinning, the application kept crashing, forcing me back to the device’s lock screen. This happened because HTTP Toolkit was already connected via ADB, and since Frida requires ADB to execute the Frida server, the conflict led to instability

So, I navigated to **App info** > **Battery optimization settings** > select **Don’t optimize**

Now, run the Frida server using ADB shell locating into /data/local/tmp and run the SSL Pinning bypass script as shown in the below screenshot.

B00M!! Application traffic was captured successfully.

I hope you found the methodology insightful and engaging.

Happy Hacking :D
