# Hack The Galaxy: Hunting Bugs in the Samsung Galaxy S6 Edge - Project Zero

Source: https://projectzero.google/2015/11/hack-galaxy-hunting-bugs-in-samsung.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Natalie Silvanovich, Planner of Bug Bashes

Recently, Project Zero researched a popular Android phone, the Samsung Galaxy S6 Edge. We discovered and reported 11 high-impact security issues as a result. This post discusses our motivations behind the research, our approach in looking for vulnerabilities on the device and what we learned by investigating it.


The majority of Android devices are not made by Google, but by external companies known as Original Equipment Manufacturers or OEMs which use the Android Open-Source Project (AOSP) as the basis for mobile devices which they manufacture. OEMs are an important area for Android security research, as they introduce additional (and possibly vulnerable) code into Android devices at all privilege levels, and they decide the frequency of the security updates that they provide for their devices to carriers.


Having done some previous research on Google-made Nexus devices running AOSP, we wanted to see how different attacking an OEM device would be. In particular, we wanted to see how difficult finding bugs would be, what type of bugs we would find and whether mitigations in AOSP would make finding or exploiting bugs more difficult. We also wanted to see how quickly bugs would be resolved when we reported them. We chose the Samsung Galaxy S6 Edge, as it is a recent high-end device with a large number of users.


We decided to work together on a single problem for a week, and see how much progress we could make on the Samsung device. To get our competitive spirits going, we decided to have a contest between the North American and European members of Project Zero, with a few extra participants from other Google security teams to make the teams even, giving a total of five participants on each side.


Each team worked on three challenges, which we feel are representative of the security boundaries of Android that are typically attacked. They could also be considered components of an exploit chain that escalates to kernel privileges from a remote or local starting point.


1. Gain remote access to contacts, photos and messages. More points were given for attacks that don’t require user interaction, and required fewer device identifiers.
2. Gain access to contacts, photos, geolocation, etc. from an application installed from Play with no permissions
3. Persist code execution across a device wipe, using the access gained in parts 1 or 2


A week later, we had the results! A total of 11 issues were found in the Samsung device.


Samsung WifiHs20UtilityService path traversal


Perhaps the most interesting issue found was [CVE-2015-7888](https://code.google.com/p/google-security-research/issues/detail?id=489&q=samsung), discovered by Mark Brand. It is a directory traversal bug that allows a file to be written as system. There is a process running a system on the device that scans for a zip file in /sdcard/Download/cred.zip and unzips the file. Unfortunately, the API used to unzip the file does not verify the file path, so it can be written in unexpected locations. On the version of the device we tested, this was trivially exploitable using the Dalvik cache using a technique that has been used to exploit [other directory traversal bugs](https://www.nowsecure.com/blog/2015/06/16/remote-code-execution-as-system-user-on-samsung-phones/), though an SELinux policy that prevents this specific exploitation technique has been pushed to the device since.


Samsung SecEmailComposer QUICK\_REPLY\_BACKGROUND permissions weakness


Another interesting and easy-to-exploit bug, [CVE-2015-7889](https://code.google.com/p/google-security-research/issues/detail?id=490&q=samsung) was found in the Samsung Email client by James Forshaw. It is a lack of authentication in one of the client’s intent handlers. An unprivileged application can send a series of intents that causes the user’s emails to be forwarded to another account. It is a very noisy attack, as the forwarded emails show up in the user’s sent folder, but it is still easy access to data that not even a privileged app should be able to access.


Samsung SecEmailUI script injection


James Forshaw and Matt Tait also found a script injection issue in the Samsung email client, [CVE-2015-7893](https://code.google.com/p/google-security-research/issues/detail?id=494&q=samsung). This issue allows JavaScript embedded in a message to be executed in the email client. It is somewhat unclear what the worst-case impact of this issue is, but it certainly increases the attack surface of the email client, as it would make JavaScript vulnerabilities in the Android WebView reachable remotely via email.


Driver Issues


There were three issues found in drivers on the device. [CVE-2015-7890](https://code.google.com/p/google-security-research/issues/detail?id=491&q=samsung), found by Ian Beer, and [CVE-2015-7892](https://code.google.com/p/google-security-research/issues/detail?id=493&q=samsung), found by Ben Hawkes, are buffer overflows in drivers that are accessible by processes that run as media. These could be used by bugs in media processing, such as libstagefright bugs, to escalate to kernel privileges. [CVE-2015-7891](https://code.google.com/p/google-security-research/issues/detail?id=492&q=samsung), found by Lee Campbell of the Chrome Security Team is a concurrency issue, leading to memory corruption in a driver that could be used to escalate from any unprivileged application or code execution to kernel.


Image Parsing Issues


Five memory corruption issues on the device in Samsung-specific image processing by myself, Natalie Silvanovich. Two of these issues, [CVE-2015-7895](https://code.google.com/p/google-security-research/issues/detail?id=497&q=samsung) and [CVE-2015-7898](https://code.google.com/p/google-security-research/issues/detail?id=500&q=samsung) occur when an image is opened in Samsung Gallery, but the three others, [CVE-2015-7894](https://code.google.com/p/google-security-research/issues/detail?id=495&q=samsung), [CVE-2015-7896](https://code.google.com/p/google-security-research/issues/detail?id=498&q=samsung) and [CVE-2015-7897](https://code.google.com/p/google-security-research/issues/detail?id=499&q=samsung) occur during media scanning, which means that an image only needs to be downloaded to trigger these issues. They allow escalation to the privileges of the Samsung Gallery app or the media scanning process.

Severity and Mitigations


Overall, we found a substantial number of high-severity issues, though there were some effective security measures on the device which slowed us down. The weak areas seemed to be device drivers and media processing. We found issues very quickly in these areas through fuzzing and code review. It was also surprising that we found the three logic issues that are trivial to exploit. These types of issues are especially concerning, as the time to find, exploit and use the issue is very short.


SELinux made it more difficult to attack the device. In particular, it made it more difficult to investigate certain bugs, and to determine the device attack surface. Android disabling the setenforce command on the device made this even more difficult. That said, we found three bugs that would allow an exploit to disable SELinux, so it’s not an effective mitigation against every bug.


Reporting the Issues


We reported these issues to Samsung soon after we discovered them. They responded recently, stating that they had fixed eight of the issues in their October Maintenance Release, and the remaining issues would be fixed in November. We greatly appreciate their efforts in patching these issues.


Testing for the vulnerabilities on the same device we found them on, with the most recent security update (G925VVRU4B0G9) applied confirmed this.


| Issue | Status | 
|  | Fixed | 
|  | Fixed | 
|  | Fixed | 
|  | Fixed | 
|  | Fixed | 
|  | Unfixed | 
|  | Fixed | 
|  | Unfixed | 
|  | Fixed | 
|  | Fixed | 
|  | Unfixed | 


The majority of the issues are fixed, however three will not be patched until November. Fortunately, these appear to be lower severity issues. [CVE-2015-7898](https://code.google.com/p/google-security-research/issues/detail?id=500&q=samsung) and [CVE-2015-7895](https://code.google.com/p/google-security-research/issues/detail?id=497) require an image to be opened in Samsung Gallery, which does not have especially high privileges and is not used by default to open images received remotely via email or SMS (so an exploit would require the user to manually download the image and open it in Gallery). The other unfixed issue, [CVE-2015-7893](https://code.google.com/p/google-security-research/issues/detail?id=494&q=samsung) allows an attacker to execute JavaScript embedded in emails, which increases the attack surface of the email client, but otherwise has unclear impact.


Conclusion


A week of investigation showed that there are a number of weak points in the Samsung Galaxy S6 Edge. Over the course of a week, we found a total of 11 issues with a serious security impact. Several issues were found in device drivers and image processing, and there were also some logic issues in the device that were high impact and easy-to-exploit.


The majority of these issues were fixed on the device we tested via an OTA update within 90 days, though three lower-severity issues remain unfixed. It is promising that the highest severity issues were fixed and updated on-device in a reasonable time frame.
