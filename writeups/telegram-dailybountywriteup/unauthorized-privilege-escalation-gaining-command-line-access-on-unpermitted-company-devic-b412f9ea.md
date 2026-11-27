# Unauthorized Privilege Escalation

- **Source URL:** https://sp1der0x.medium.com/unauthorized-privilege-escalation-gaining-command-line-access-on-unpermitted-company-devices-1a67e55f1b63?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250304012934/https://sp1der0x.medium.com/unauthorized-privilege-escalation-gaining-command-line-access-on-unpermitted-company-devices-1a67e55f1b63
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7682 (id 7682)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **Unauthorized Privilege Escalation: Gaining Command Line Access on Unpermitted Company Devices $$$$**

بِسْمِ اللهِ الرَّحْمَنِ الرَّحِيمِ، الْحَمْدُ لِلَّهِ الَّذِي هَدَانَا لِهَذَا وَمَا كُنَّا لِنَهْتَدِيَ لَوْلَا أَنْ هَدَانَا اللهُ، وَالصَّلَاةُ وَالسَّلَامُ عَلَى خَيْرِ خَلْقِ اللهِ مُحَمَّدِ بْنِ عَبْدِ اللهِ، الَّذِي بُعِثَ لِيُتَمِّمَ مَكَارِمَ الْأَخْلَاقِ وَلِيُعَلِّمَنَا سَبِيلَ الْحِكْمَةِ وَالتَّقْوَى. أَمَّا بَعْدُ،

Hello, hackers. My name is Mohamed Ashraf(Sp1der0x). Today, I’ll be discussing a bug I recently discovered while hunting.

**Note: As the program is private, we will explain the example on spider.com**

**Note 2: My English could be better and also this is the first writeup I created so there may be some errors, thank you for your understanding, hackers.**

**Roles and Privileges:**

**At spider.com there are three types of members**

**The first type: System Administrator I think that’s pretty self-explanatory.**

**The second type: Technicians You can give him all the same powers as an administrator, except that he is not an administrator The most important ones are:**

- View, update, create, End User Sharing.
- View, update, create, Organization.
- View, update, create, Devices.

**The third type: End user Here are its privileges**

- Connect to selected features on enabled devices.
- Restore files from devices with backup enabled.
- View, update, create tickets.

**Summary**

In my recent vulnerability discovery, I uncovered a serious Privilege Escalation (PrivEsc) flaw within the spider.com system. This flaw enables any Technician with permissions on one company’s devices to gain command-line access to devices in a separate, unauthorized company by modifying specific request parameters. This access circumvents the permissions and allows unauthorized command-line control, posing a major security threat.

**Target and Setup**

While conducting an assessment on spider.com, I created a simulated environment with two companies:

- Company 1: Full access granted to a Technician.

- Company 2: No permissions given to the Technician.

This scenario ensured a controlled test environment to validate the permissions and to see if I could exploit any flaws to breach access on devices outside the Technician’s intended scope.

**The Vulnerability**

In Company 1, the Technician can add End Users to devices with specific permissions, including access to the command-line interface for device management. Here’s the breakdown of the exploitation process:

1\. Adding an End User with Command-Line Permissions: 

Within Company 1, I created a new End User with a role that includes access to the command-line on the designated company devices.

2\. Intercepting the API Request for Device Permissions: 

When the Technician assigns the End User to a device, the system sends a request that includes device identification information, specifically deviceId. The request looked something like this:

```
POST /ws/end-user/"enduser-id"/devices/addList HTTP/2
 Host: spider.com
 Cookie: sessionKey="Technician Session here"
 …
 {"deviceIds": [DEVICE_ID_OF_COMPANY_1]}
```
3\. Modifying the Device ID: 

To test unauthorized access, I intercepted the request and replaced the DEVICE\_ID\_OF\_COMPANY\_1 with the DEVICE\_ID of a device from Company

4\. This is a device for which the Technician theoretically had no permissions.

5\. Gaining Unauthorized Access: 

Surprisingly, the system accepted this modified request, and the End User was successfully granted command-line access to the Company 2 device. This action effectively bypassed any restrictions on device access within separate companies, granting unintended command-line privileges.

The flaw arises from a lack of validation on the deviceId parameter, allowing users to manipulate it and target any accessible device, even those in separate organizational scopes. This manipulation bypasses the boundaries designed to prevent inter-company access, compromising the isolation between companies
