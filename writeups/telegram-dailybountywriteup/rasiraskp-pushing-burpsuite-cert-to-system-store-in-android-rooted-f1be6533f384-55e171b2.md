# Pushing Burpsuite cert to system store in Android(rooted)

- **Source URL:** https://medium.com/@rasiraskp/pushing-burpsuite-cert-to-system-store-in-android-rooted-f1be6533f384?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221018065334/https://medium.com/@rasiraskp/pushing-burpsuite-cert-to-system-store-in-android-rooted-f1be6533f384
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/499 (id 499)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Pushing Burpsuite cert to system store in Android(rooted)

Having your burpsuite ca certificate pushed to system store provides you greater advantage in your testing. certificates in system store are usually those comes pre installed with the device and is trusted by the all apps in device unlike the user certs . client installed certificates are only trusted if this is explicitly mentioned by the application in the network security config file

There are various ways which you can use to push your certs to system store.

# 1. Root certificate manager app:

Root certificate manager app is one of the apps out there which can be used to push our certificated to the system store. but i have seen this only working in lower versions of android (below android 7).

To push cert to system store with the app:

1. Download app from [palystore](https://play.google.com/store/apps/details?id=net.jolivier.cert.Importer&hl=en_IN&gl=US)
2. from your PC, open Burpsuite and export a certificate
3. rename this to .cer extension and copy to your android device
4. once copied, open the root certificate manager app and click on folder icon to import certificate

5\. select the certificate and add it

6\. once imported, we can see that this certificate has been added to the system store!!

# 2. Using Magisk module by NVISOsecurity

Magisk manager is an utility tool that works with rooted android and this allows you to highly customize your rooted android phones.

There are plenty of third party modules available for magisk that are build to accomplish various tasks seamlessly .

This magisk [module](https://github.com/NVISOsecurity/MagiskTrustUserCerts) by NvisoSecurity makes this steps a lot easier

1. download the zip file of module from the given link
2. Open magisk, go to modules and install the module from zip file
3. once the module is installed, enable the proxy settings in wifi
4. visit [http://burp](http://burp)
5. download the certificate and install it normally
6. restart the device
7. once restart is complete, we can see that the certificate is now pushed to the system store by the magisk module

read the original blog post including more technical details of the module here: [Link](https://blog.nviso.eu/2017/12/22/intercepting-https-traffic-from-apps-on-android-7-using-magisk-burp/)

Once your device has certificate added to system store the certificate is considered as trusted by all the apps in your device .Now you can start intercepting the traffic of your app (also check is SSL Pinning is implemented)
