# The More You Know, The More You Know You Don’t Know - Project Zero

Source: https://projectzero.google/2022/04/the-more-you-know-more-you-know-you.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

A Year in Review of 0-days Used In-the-Wild in 2021

Posted by Maddie Stone, Google Project Zero


This is our third annual year in review of 0-days exploited in-the-wild \[[2020](/2021/02/deja-vu-lnerability.html), [2019](/2020/07/detection-deficit-year-in-review-of-0.html)\]. Each year we’ve looked back at all of the detected and disclosed in-the-wild 0-days as a group and synthesized what we think the trends and takeaways are. The goal of this report is not to detail each individual exploit, but instead to analyze the exploits from the year as a group, looking for trends, gaps, lessons learned, successes, etc. If you’re interested in the analysis of individual exploits, please check out our [root cause analysis repository](https://googleprojectzero.github.io/0days-in-the-wild/rca.html).


We perform and share this analysis in order to make 0-day hard. We want it to be more costly, more resource intensive, and overall more difficult for attackers to use 0-day capabilities. 2021 highlighted just how important it is to stay relentless in our pursuit to make it harder for attackers to exploit users with 0-days. We heard [over](https://forbiddenstories.org/about-the-pegasus-project/) and [over](https://citizenlab.ca/2021/07/hooking-candiru-another-mercenary-spyware-vendor-comes-into-focus/) and [over](https://www.amnesty.org/en/latest/research/2021/11/devices-of-palestinian-human-rights-defenders-hacked-with-nso-groups-pegasus-spyware-2/) about how governments were targeting journalists, minoritized populations, politicians, human rights defenders, and even security researchers around the world. The decisions we make in the security and tech communities can have real impacts on society and our fellow humans’ lives.


We’ll provide our evidence and process for our conclusions in the body of this post, and then wrap it all up with our thoughts on next steps and hopes for 2022 in the conclusion. If digging into the bits and bytes is not your thing, then feel free to just check-out the Executive Summary and Conclusion.

# Executive Summary

2021 included the detection and disclosure of 58 in-the-wild 0-days, the most ever recorded since Project Zero began tracking in mid-2014. That’s more than double the previous maximum of 28 detected in 2015 and especially stark when you consider that there were only 25 detected in 2020. We’ve tracked publicly known in-the-wild 0-day exploits in [this spreadsheet](https://docs.google.com/spreadsheets/d/1lkNJ0uQwbeC1ZTRrxdtuPLCIl7mlUreoKfSIgajnSyY/edit#gid=0) since mid-2014.


While we often talk about the number of 0-day exploits used in-the-wild, what we’re actually discussing is the number of 0-day exploits detected and disclosed as in-the-wild. And that leads into our first conclusion: we believe the large uptick in in-the-wild 0-days in 2021 is due to increased detection and disclosure of these 0-days, rather than simply increased usage of 0-day exploits.


With this record number of in-the-wild 0-days to analyze we saw that attacker methodology hasn’t actually had to change much from previous years. Attackers are having success using the same bug patterns and exploitation techniques and going after the same attack surfaces. Project Zero’s mission is “make 0day hard”. 0-day will be harder when, overall, attackers are not able to use public methods and techniques for developing their 0-day exploits. When we look over these 58 0-days used in 2021, what we see instead are 0-days that are similar to previous & publicly known vulnerabilities. Only two 0-days stood out as novel: one for the technical sophistication of its exploit and the other for its use of logic bugs to escape the sandbox.


So while we recognize the industry’s improvement in the detection and disclosure of in-the-wild 0-days, we also acknowledge that there’s a lot more improving to be done. Having access to more “ground truth” of how attackers are actually using 0-days shows us that they are able to have success by using previously known techniques and methods rather than having to invest in developing novel techniques. This is a clear area of opportunity for the tech industry.


We had so many more data points in 2021 to learn about attacker behavior than we’ve had in the past. Having all this data, though, has left us with even more questions than we had before. Unfortunately, attackers who actively use 0-day exploits do not share the 0-days they’re using or what percentage of 0-days we’re missing in our tracking, so we’ll never know exactly what proportion of 0-days are currently being found and disclosed publicly.


Based on our analysis of the 2021 0-days we hope to see the following progress in 2022 in order to continue taking steps towards making 0-day hard:

1. All vendors agree to disclose the in-the-wild exploitation status of vulnerabilities in their security bulletins.
2. Exploit samples or detailed technical descriptions of the exploits are shared more widely.
3. Continued concerted efforts on reducing memory corruption vulnerabilities or rendering them unexploitable.Launch mitigations that will significantly impact the exploitability of memory corruption vulnerabilities.

# A Record Year for In-the-Wild 0-days

2021 was a record year for in-the-wild 0-days. So what happened?



Is it that software security is getting worse? Or is it that attackers are using 0-day exploits more? Or has our ability to detect and disclose 0-days increased? When looking at the significant uptick from 2020 to 2021, we think it's mostly explained by the latter. While we believe there has been a steady growth in interest and investment in 0-day exploits by attackers in the past several years, and that security still needs to urgently improve, it appears that the security industry's ability to detect and disclose in-the-wild 0-day exploits is the primary explanation for the increase in observed 0-day exploits in 2021.


While we often talk about “0-day exploits used in-the-wild”, what we’re actually tracking are “0-day exploits detected and disclosed as used in-the-wild”. There are more factors than just the use that contribute to an increase in that number, most notably: detection and disclosure. Better detection of 0-day exploits and more transparently disclosed exploited 0-day vulnerabilities is a positive indicator for security and progress in the industry.


Overall, we can break down the uptick in the number of in-the-wild 0-days into:

- More detection of in-the-wild 0-day exploits
- More public disclosure of in-the-wild 0-day exploitation

## More detection

In the [2019 Year in Review](/2020/07/detection-deficit-year-in-review-of-0.html), we wrote about the “Detection Deficit”. We stated “As a community, our ability to detect 0-days being used in the wild is severely lacking to the point that we can’t draw significant conclusions due to the lack of (and biases in) the data we have collected.” In the last two years, we believe that there’s been progress on this gap.


Anecdotally, we hear from more people that they’ve begun working more on detection of 0-day exploits. Quantitatively, while a very rough measure, we’re also seeing the number of entities credited with reporting in-the-wild 0-days increasing. It stands to reason that if the number of people working on trying to find 0-day exploits increases, then the number of in-the-wild 0-day exploits detected may increase.



We’ve also seen the number of vendors detecting in-the-wild 0-days in their own products increasing. Whether or not these vendors were previously working on detection, vendors seem to have found ways to be more successful in 2021. Vendors likely have the most telemetry and overall knowledge and visibility into their products so it’s important that they are investing in (and hopefully having success in) detecting 0-days targeting their own products. As shown in the chart above, there was a significant increase in the number of in-the-wild 0-days discovered by vendors in their own products. Google discovered 7 of the in-the-wild 0-days in their own products and Microsoft discovered 10 in their products!

## More disclosure

The second reason why the number of detected in-the-wild 0-days has increased is due to more disclosure of these vulnerabilities. Apple and Google Android (we differentiate “Google Android” rather than just “Google” because Google Chrome has been annotating their security bulletins for the last few years) first began labeling vulnerabilities in their security advisories with the information about potential in-the-wild exploitation in November 2020 and January 2021 respectively. When vendors don’t annotate their release notes, the only way we know that a 0-day was exploited in-the-wild is if the researcher who discovered the exploitation comes forward. If Apple and Google Android had not begun annotating their release notes, the public would likely not know about at least 7 of the Apple in-the-wild 0-days and 5 of the Android in-the-wild 0-days. Why? Because these vulnerabilities were reported by “Anonymous” reporters. If the reporters didn’t want credit for the vulnerability, it’s unlikely that they would have gone public to say that there were indications of exploitation. That is 12 0-days that wouldn’t have been included in this year’s list if Apple and Google Android had not begun transparently annotating their security advisories.


Kudos and thank you to Microsoft, Google Chrome, and Adobe who have been annotating their security bulletins for transparency for multiple years now! And thanks to Apache who also annotated their release notes for [CVE-2021-41773](https://httpd.apache.org/security/vulnerabilities_24.html) this past year.


In-the-wild 0-days in Qualcomm and ARM products were annotated as in-the-wild in Android security bulletins, but not in the vendor’s own security advisories.


It's highly likely that in 2021, there were other 0-days that were exploited in the wild and detected, but vendors did not mention this in their release notes. In 2022, we hope that more vendors start noting when they patch vulnerabilities that have been exploited in-the-wild. Until we’re confident that all vendors are transparently disclosing in-the-wild status, there’s a big question of how many in-the-wild 0-days are discovered, but not labeled publicly by vendors.

# New Year, Old Techniques

We had a record number of “data points” in 2021 to understand how attackers are actually using 0-day exploits. A bit surprising to us though, out of all those data points, there was nothing new amongst all this data. 0-day exploits are considered one of the most advanced attack methods an actor can use, so it would be easy to conclude that attackers must be using special tricks and attack surfaces. But instead, the 0-days we saw in 2021 generally followed the same bug patterns, attack surfaces, and exploit “shapes” previously seen in public research. Once “0-day is hard”, we’d expect that to be successful, attackers would have to find new bug classes of vulnerabilities in new attack surfaces using never before seen exploitation methods. In general, that wasn't what the data showed us this year. With two exceptions (described below in the iOS section) out of the 58, everything we saw was pretty “[meh](https://www.dictionary.com/browse/meh#:~:text=unimpressive%3B%20boring%3A)” or standard.


Out of the 58 in-the-wild 0-days for the year, 39, or 67% were memory corruption vulnerabilities. Memory corruption vulnerabilities have been the standard for attacking software for the last few decades and it’s still how attackers are having success. Out of these memory corruption vulnerabilities, the majority also stuck with very popular and well-known bug classes:

- 17 use-after-free
- 6 out-of-bounds read & write
- 4 buffer overflow
- 4 integer overflow


In the next sections we’ll dive into each major platform that we saw in-the-wild 0-days for this year. We’ll share the trends and explain why what we saw was pretty unexceptional.

## Chromium (Chrome)

Chromium had a record high number of 0-days detected and disclosed in 2021 with 14. Out of these 14, 10 were renderer remote code execution bugs, 2 were sandbox escapes, 1 was an infoleak, and 1 was used to open a webpage in Android apps other than Google Chrome.


The 14 0-day vulnerabilities were in the following components:

- 6 JavaScript Engine - v8 ([CVE-2021-21148](https://chromereleases.googleblog.com/2021/02/stable-channel-update-for-desktop_4.html), [CVE-2021-30551](https://chromereleases.googleblog.com/2021/02/stable-channel-update-for-desktop_4.html), [CVE-2021-30563](https://chromereleases.googleblog.com/2021/07/stable-channel-update-for-desktop.html), [CVE-2021-30632](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-30632.html), [CVE-2021-37975](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-37975.html), [CVE-2021-38003](https://chromereleases.googleblog.com/2021/10/stable-channel-update-for-desktop_28.html))
- 2 DOM Engine - Blink ([CVE-2021-21193](https://chromereleases.googleblog.com/2021/03/stable-channel-update-for-desktop_12.html) & [CVE-2021-21206](https://chromereleases.googleblog.com/2021/04/stable-channel-update-for-desktop.html))
- 1 WebGL ([CVE-2021-30554](https://chromereleases.googleblog.com/2021/06/stable-channel-update-for-desktop_17.html))
- 1 IndexedDB ([CVE-2021-30633](https://chromereleases.googleblog.com/2021/09/stable-channel-update-for-desktop.html))
- 1 webaudio ([CVE-2021-21166](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-21166.html))
- 1 Portals ([CVE-2021-37973](https://chromereleases.googleblog.com/2021/09/stable-channel-update-for-desktop_24.html))
- 1 Android Intents ([CVE-2021-38000](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-38000.html))
- 1 Core ([CVE-2021-37976](https://chromereleases.googleblog.com/2021/09/stable-channel-update-for-desktop_30.html))


When we look at the components targeted by these bugs, they’re all attack surfaces seen before in public security research and previous exploits. If anything, there are a few less DOM bugs and more targeting these other components of browsers like IndexedDB and WebGL than previously. 13 out of the 14 Chromium 0-days were memory corruption bugs. Similar to last year, most of those memory corruption bugs are use-after-free vulnerabilities.


A couple of the Chromium bugs were even similar to previous in-the-wild 0-days. [CVE-2021-21166](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-21166.html) is an issue in ScriptProcessorNode::Process() in webaudio where there’s insufficient locks such that buffers are accessible in both the main thread and the audio rendering thread at the same time. [CVE-2019-13720](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2019/CVE-2019-13720.html) is an in-the-wild 0-day from 2019. It was a vulnerability in ConvolverHandler::Process() in webaudio where there were also insufficient locks such that a buffer was accessible in both the main thread and the audio rendering thread at the same time.


[CVE-2021-30632](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-30632.html) is another Chromium in-the-wild 0-day from 2021. It’s a type confusion in the  TurboFan JIT in Chromium’s JavaScript Engine, v8, where Turbofan fails to deoptimize code after a property map is changed. [CVE-2021-30632](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-30632.html) in particular deals with code that stores global properties. [CVE-2020-16009](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2020/CVE-2020-16009.html) was also an in-the-wild 0-day that was due to Turbofan failing to deoptimize code after map deprecation.

## WebKit (Safari)

Prior to 2021, Apple had only acknowledged 1 publicly known in-the-wild 0-day targeting WebKit/Safari, and that was due the sharing by an external researcher. In 2021 there were 7. This makes it hard for us to assess trends or changes since we don’t have historical samples to go off of. Instead, we’ll look at 2021’s WebKit bugs in the context of other Safari bugs not known to be in-the-wild and other browser in-the-wild 0-days.


The 7 in-the-wild 0-days targeted the following components:

- 4 Javascript Engine - JavaScript Core ([CVE-2021-1870](https://support.apple.com/en-us/HT212146), [CVE-2021-1871](https://support.apple.com/en-us/HT212146), [CVE-2021-30663](https://support.apple.com/en-us/HT212336), [CVE-2021-30665](https://support.apple.com/en-us/HT212336))

- 1 IndexedDB ([CVE-2021-30858](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-30858.html))
- 1 Storage ([CVE-2021-30661](https://support.apple.com/en-us/HT212317))
- 1 Plugins ([CVE-2021-1879](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-1879.html))


The one semi-surprise is that no DOM bugs were detected and disclosed. In previous years, vulnerabilities in the DOM engine have generally made up 15-20% of the in-the-wild browser 0-days, but none were detected and disclosed for WebKit in 2021.


It would not be surprising if attackers are beginning to shift to other modules, like third party libraries or things like IndexedDB. The modules may be more promising to attackers going forward because there’s a better chance that the vulnerability may exist in multiple browsers or platforms. For example, the webaudio bug in Chromium, [CVE-2021-21166](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-21166.html), also existed in WebKit and was fixed as [CVE-2021-1844](https://support.apple.com/en-us/HT212223), though there was no evidence it was exploited in-the-wild in WebKit. The IndexedDB in-the-wild 0-day that was used against Safari in 2021, [CVE-2021-30858](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-30858.html), was very, very similar to a [bug fixed in Chromium in January 2020](https://bugs.chromium.org/p/chromium/issues/detail?id=1032890).

## Internet Explorer

Since we began tracking in-the-wild 0-days, Internet Explorer has had a pretty consistent number of 0-days each year. 2021 actually tied 2016 for the most in-the-wild Internet Explorer 0-days we’ve ever tracked even though Internet Explorer’s market share of web browser users continues to decrease.



So why are we seeing so little change in the number of in-the-wild 0-days despite the change in market share? Internet Explorer is still a ripe attack surface for initial entry into Windows machines, even if the user doesn’t use Internet Explorer as their Internet browser. While the number of 0-days stayed pretty consistent to what we’ve seen in previous years, the components targeted and the delivery methods of the exploits changed. 3 of the 4 0-days seen in 2021 targeted the MSHTML browser engine and were delivered via methods other than the web. Instead they were delivered to targets via Office documents or other file formats.


The four 0-days targeted the following components:

- MSHTML browser engine ([CVE-2021-26411](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-26411.html), [CVE-2021-33742](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2021/CVE-2021-33742.html), [CVE-2021-40444](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-40444))
- Javascript Engine - JScript9 ([CVE-2021-34448](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-34448))


For [CVE-2021-26411](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-26411.html) targets of the campaign initially received a .mht file, which prompted the user to open in Internet Explorer. Once it was opened in Internet Explorer, the exploit was downloaded and run. [CVE-2021-33742](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-33742.html) and [CVE-2021-40444](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-40444) were delivered to targets via malicious Office documents.


[CVE-2021-26411](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-26411.html) and [CVE-2021-33742](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-33742.html) were two common memory corruption bug patterns: a use-after-free due to a user controlled callback in between two actions using an object and the user frees the object during that callback and a buffer overflow.


There were a few different vulnerabilities used in the exploit chain that used [CVE-2021-40444](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-40444), but the one within MSHTML was that as soon as the Office document was opened the payload would run: a CAB file was downloaded, decompressed, and then a function from within a DLL in that CAB was executed. Unlike the previous two MSHTML bugs, this was a logic error in URL parsing rather than a memory corruption bug.

## Windows

Windows is the platform where we’ve seen the most change in components targeted compared with previous years. However, this shift has generally been in progress for a few years and predicted with the end-of-life of Windows 7 in 2020 and thus why it’s still not especially novel.


In 2021 there were 10 Windows in-the-wild 0-days targeting 7 different components:

- 2 Enhanced crypto provider ([CVE-2021-31199](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31199), [CVE-2021-31201](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31201))
- 2 NTOS kernel ([CVE-2021-33771](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-33771), [CVE-2021-31979](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31979))
- 2 Win32k ([CVE-2021-1732](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-1732.html), [CVE-2021-40449](https://securelist.com/mysterysnail-attacks-with-windows-zero-day/104509/))
- 1 Windows update medic ([CVE-2021-36948](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-36948))
- 1 SuperFetch ([CVE-2021-31955](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31955))
- 1 dwmcore.dll ([CVE-2021-28310](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-28310))

- 1 ntfs.sys ([CVE-2021-31956](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31956))


The number of different components targeted is the shift from past years. For example, in 2019 75% of Windows 0-days targeted Win32k while in 2021 Win32k only made up 20% of the Windows 0-days. The reason that this was expected and predicted was that 6 out of 8 of those 0-days that targeted Win32k in 2019 did not target the latest release of Windows 10 at that time; they were targeting older versions. With Windows 10 Microsoft began dedicating more and more resources to locking down the attack surface of Win32k so as those older versions have hit end-of-life, Win32k is a less and less attractive attack surface.


Similar to the many Win32k vulnerabilities seen over the years, the two 2021 Win32k in-the-wild 0-days are due to custom user callbacks. The user calls functions that change the state of an object during the callback and Win32k does not correctly handle those changes. [CVE-2021-1732](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-1732.html) is a type confusion vulnerability due to a user callback in xxxClientAllocWindowClassExtraBytes which leads to out-of-bounds read and write. If NtUserConsoleControl is called during the callback a flag is set in the window structure to signal that a field is an offset into the kernel heap. xxxClientAllocWindowClassExtraBytes doesn’t check this and writes that field as a user-mode pointer without clearing the flag. The first in-the-wild 0-day detected and disclosed in 2022, [CVE-2022-21882](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2022/CVE-2022-21882.html), is due to [CVE-2021-1732](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-1732.html) actually not being fixed completely. The attackers found a way to bypass the original patch and still trigger the vulnerability. [CVE-2021-40449](https://securelist.com/mysterysnail-attacks-with-windows-zero-day/104509/) is a use-after-free in NtGdiResetDC due to the object being freed during the user callback.

## iOS/macOS

As discussed in the “More disclosure” section above, 2021 was the first full year that Apple annotated their release notes with in-the-wild status of vulnerabilities. 5 iOS in-the-wild 0-days were detected and disclosed this year. The first publicly known macOS in-the-wild 0-day ([CVE-2021-30869](https://blog.google/threat-analysis-group/analyzing-watering-hole-campaign-using-macos-exploits/)) was also found. In this section we’re going to discuss iOS and macOS together because: 1) the two operating systems include similar components and 2) the sample size for macOS is very small (just this one vulnerability).



For the 5 total iOS and macOS in-the-wild 0-days, they targeted 3 different attack surfaces:

- IOMobileFrameBuffer ([CVE-2021-30807](https://support.apple.com/en-us/HT212623), [CVE-2021-30883](https://support.apple.com/en-us/HT212846))
- XNU Kernel ([CVE-2021-1782](https://support.apple.com/en-us/HT212146) & [CVE-2021-30869](https://blog.google/threat-analysis-group/analyzing-watering-hole-campaign-using-macos-exploits/))
- CoreGraphics ([CVE-2021-30860](/2021/12/a-deep-dive-into-nso-zero-click.html))
- CommCenter ([FORCEDENTRY sandbox escape](/2022/03/forcedentry-sandbox-escape.html) - CVE requested, not yet assigned)


These 4 attack surfaces are not novel. IOMobileFrameBuffer has been a target of public security research for many years. For example, the Pangu Jailbreak from 2016 used [CVE-2016-4654](https://www.blackhat.com/docs/us-16/materials/us-16-Wang-Pangu-9-Internals.pdf), a heap buffer overflow in IOMobileFrameBuffer. IOMobileFrameBuffer manages the screen’s frame buffer. For iPhone 11 (A13) and below, IOMobileFrameBuffer was a kernel driver. Beginning with A14, it runs on a coprocessor, the DCP.  It’s a popular attack surface because historically it’s been accessible from sandboxed apps. In 2021 there were two in-the-wild 0-days in IOMobileFrameBuffer. [CVE-2021-30807](https://support.apple.com/en-us/HT212623) is an out-of-bounds read and [CVE-2021-30883](https://support.apple.com/en-us/HT212846) is an integer overflow, both common memory corruption vulnerabilities. In 2022, we already have another in-the-wild 0-day in IOMobileFrameBuffer, [CVE-2022-22587](https://support.apple.com/en-us/HT213053).


One iOS 0-day and the macOS 0-day both exploited vulnerabilities in the XNU kernel and both vulnerabilities were in code related to XNU’s inter-process communication (IPC) functionality. [CVE-2021-1782](https://support.apple.com/en-us/HT212146) exploited a vulnerability in mach vouchers while [CVE-2021-30869](https://blog.google/threat-analysis-group/analyzing-watering-hole-campaign-using-macos-exploits/) exploited a vulnerability in mach messages. This is not the first time we’ve seen iOS in-the-wild 0-days, much less public security research, targeting mach vouchers and mach messages. [CVE-2019-6625](https://support.apple.com/en-us/HT209443) was exploited as a part of [an exploit chain targeting iOS 11.4.1-12.1.2](/2019/08/in-wild-ios-exploit-chain-5.html) and was also a [vulnerability in mach vouchers](/2019/01/voucherswap-exploiting-mig-reference.html).


Mach messages have also been a popular target for public security research. In 2020 there were two in-the-wild 0-days also in mach messages: [CVE-2020-27932](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2020/CVE-2020-27932.html) & [CVE-2020-27950](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2020/CVE-2020-27950.html). This year’s [CVE-2021-30869](https://blog.google/threat-analysis-group/analyzing-watering-hole-campaign-using-macos-exploits/) is a pretty close variant to 2020’s [CVE-2020-27932](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2020/CVE-2020-27932.html). Tielei Wang and Xinru Chi actually [presented on this vulnerability at zer0con 2021](https://github.com/wangtielei/Slides/blob/main/zer0con21.pdf) in April 2021. In their presentation, they explained that they found it while doing variant analysis on [CVE-2020-27932](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2020/CVE-2020-27932.html). [TieLei Wang explained via Twitter](https://twitter.com/WangTielei/status/1486266258152726530) that they had found the vulnerability in December 2020 and had noticed it was fixed in beta versions of iOS 14.4 and macOS 11.2 which is why they presented it at Zer0Con. The in-the-wild exploit only targeted macOS 10, but used the same exploitation technique as the one presented.


The two FORCEDENTRY exploits ([CVE-2021-30860](/2021/12/a-deep-dive-into-nso-zero-click.html) and the [sandbox escape](/2022/03/forcedentry-sandbox-escape.html)) were the only times that made us all go “wow!” this year. For [CVE-2021-30860](/2021/12/a-deep-dive-into-nso-zero-click.html), the integer overflow in CoreGraphics, it was because:

1. For years we’ve all heard about how attackers are using 0-click iMessage bugs and finally we have a public example, and
2. The exploit was an impressive work of art.

The sandbox escape (CVE requested, not yet assigned) was impressive because it’s one of the few times we’ve seen a sandbox escape in-the-wild that uses only logic bugs, rather than the standard memory corruption bugs.


For [CVE-2021-30860](/2021/12/a-deep-dive-into-nso-zero-click.html), the vulnerability itself wasn’t especially notable: a classic integer overflow within the JBIG2 parser of the CoreGraphics PDF decoder. The exploit, though, was described by Samuel Groß & Ian Beer as “one of the most technically sophisticated exploits \[they\]’ve ever seen”. [Their blogpost shares all the details](/2021/12/a-deep-dive-into-nso-zero-click.html), but the highlight is that the exploit uses the logical operators available in JBIG2 to build NAND gates which are used to build its own computer architecture. The exploit then writes the rest of its exploit using that new custom architecture. From their blogpost:


Using over 70,000 segment commands defining logical bit operations, they define a small computer architecture with features such as registers and a full 64-bit adder and comparator which they use to search memory and perform arithmetic operations. It's not as fast as Javascript, but it's fundamentally computationally equivalent.


The bootstrapping operations for the sandbox escape exploit are written to run on this logic circuit and the whole thing runs in this weird, emulated environment created out of a single decompression pass through a JBIG2 stream. It's pretty incredible, and at the same time, pretty terrifying.


This is an example of what making 0-day exploitation hard could look like: attackers having to develop a new and novel way to exploit a bug and that method requires lots of expertise and/or time to develop. This year, the two FORCEDENTRY exploits were the only 0-days out of the 58 that really impressed us. Hopefully in the future, the bar has been raised such that this will be required for any successful exploitation.

## Android

There were 7 Android in-the-wild 0-days detected and disclosed this year. Prior to 2021 there had only been 1 and it was in 2019: [CVE-2019-2215](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2019/CVE-2019-2215.html). Like WebKit, this lack of data makes it hard for us to assess trends and changes. Instead, we’ll compare it to public security research.


For the 7 Android 0-days they targeted the following components:

- Qualcomm Adreno GPU driver ([CVE-2020-11261](https://source.android.com/security/bulletin/2021-01-01), [CVE-2021-1905](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2021/CVE-2021-1905.html), [CVE-2021-1906](https://source.android.com/security/bulletin/2021-05-01))
- ARM Mali GPU driver ([CVE-2021-28663](https://source.android.com/security/bulletin/2021-05-01), [CVE-2021-28664](https://source.android.com/security/bulletin/2021-05-01))
- Upstream Linux kernel ([CVE-2021-1048](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-1048.html), [CVE-2021-0920](https://source.android.com/security/bulletin/2021-11-01#kernel-components))


5 of the 7 0-days from 2021 targeted GPU drivers. This is actually not that surprising when we consider the evolution of the Android ecosystem as well as recent public security research into Android. The Android ecosystem is quite fragmented: many different kernel versions, different manufacturer customizations, etc. If an attacker wants a capability against “Android devices”, they generally need to maintain many different exploits to have a decent percentage of the Android ecosystem covered. However, if the attacker chooses to target the GPU kernel driver instead of another component, they will only need to have two exploits since most Android devices use 1 of 2 GPUs: either the Qualcomm Adreno GPU or the ARM Mali GPU.


Public security research mirrored this choice in the last couple of years as well. When developing full exploit chains (for defensive purposes) to target Android devices, [Guang Gong](https://github.com/secmob/TiYunZong-An-Exploit-Chain-to-Remotely-Root-Modern-Android-Devices/blob/master/us-20-Gong-TiYunZong-An-Exploit-Chain-to-Remotely-Root-Modern-Android-Devices-wp.pdf), [Man Yue Mo](https://securitylab.github.com/research/one_day_short_of_a_fullchain_android/), and [Ben Hawkes](/2020/09/attacking-qualcomm-adreno-gpu.html) all chose to attack the GPU kernel driver for local privilege escalation. Seeing the in-the-wild 0-days also target the GPU was more of a confirmation rather than a revelation. Of the 5 0-days targeting GPU drivers, 3 were in the Qualcomm Adreno driver and 2 in the ARM Mali driver.


The two non-GPU driver 0-days ([CVE-2021-0920](https://source.android.com/security/bulletin/2021-11-01#kernel-components) and [CVE-2021-1048](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-1048.html)) targeted the upstream Linux kernel. Unfortunately, these 2 bugs shared a singular characteristic with the Android in-the-wild 0-day seen in 2019: all 3 were previously known upstream before their exploitation in Android. While the sample size is small, it’s still quite striking to see that 100% of the known in-the-wild Android 0-days that target the kernel are bugs that actually were known about before their exploitation.


The vulnerability now referred to as [CVE-2021-0920](https://source.android.com/security/bulletin/2021-11-01#kernel-components) was actually found in September 2016 and [discussed on the Linux kernel mailing lists](https://lore.kernel.org/lkml/CAOssrKcfncAYsQWkfLGFgoOxAQJVT2hYVWdBA6Cw7hhO8RJ_wQ@mail.gmail.com/). A [patch was even developed back in 2016](https://lore.kernel.org/lkml/1475150954-10152-1-git-send-email-mszeredi@redhat.com/), but it didn’t end up being submitted. The bug was finally [fixed in the Linux kernel in July 2021](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=cbcf01128d0a92e131bd09f1688fe032480b65ca) after the detection of the in-the-wild exploit targeting Android. The patch then made it into the [Android security bulletin in November 2021](https://source.android.com/security/bulletin/2021-11-01#kernel-components).


[CVE-2021-1048](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-1048.html) remained unpatched in Android for 14 months after it was patched in the Linux kernel. The Linux kernel was actually only vulnerable to the issue for a few weeks, but due to Android patching practices, that few weeks became almost a year for some Android devices. If an Android OEM synced to the upstream kernel, then they likely were patched against the vulnerability at some point. But many devices, such as recent Samsung devices, had not and thus were left vulnerable.

## Microsoft Exchange Server

In 2021, there were 5 in-the-wild 0-days targeting Microsoft Exchange Server. This is the first time any Exchange Server in-the-wild 0-days have been detected and disclosed since we began tracking in-the-wild 0-days. The first four ([CVE-2021-26855](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-26855.html), [CVE-2021-26857](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26857), [CVE-2021-26858](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26858), and [CVE-2021-27065](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-27065))  were all disclosed and patched at the same time and used together in a [single operation](https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/). The fifth ([CVE-2021-42321](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-42321)) was patched on its own in November 2021. [CVE-2021-42321](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-42321) was demonstrated at Tianfu Cup and then discovered in-the-wild by Microsoft. While no other in-the-wild 0-days were disclosed as part of the chain with [CVE-2021-42321](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-42321), the attackers would have required at least another 0-day for successful exploitation since [CVE-2021-42321](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-42321) is a post-authentication bug.


Of the four Exchange in-the-wild 0-days used in the first campaign, [CVE-2021-26855](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-26855.html), which is also known as “ProxyLogon”, is the only one that’s pre-auth. [CVE-2021-26855](https://googleprojectzero.github.io/0days-in-the-wild//0day-RCAs/2021/CVE-2021-26855.html) is a server side request forgery (SSRF) vulnerability that allows unauthenticated attackers to send arbitrary HTTP requests as the Exchange server. The other three vulnerabilities were post-authentication. For example, [CVE-2021-26858](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26858) and [CVE-2021-27065](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-27065) allowed attackers to write arbitrary files to the system. [CVE-2021-26857](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26857) is a remote code execution vulnerability due to a deserialization bug in the Unified Messaging service. This allowed attackers to run code as the privileged SYSTEM user.


For the second campaign, [CVE-2021-42321](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2021-42321), like [CVE-2021-26858](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26858), is a post-authentication RCE vulnerability due to insecure deserialization. It seems that while attempting to harden Exchange, Microsoft inadvertently introduced another deserialization vulnerability.


While there were a significant amount of 0-days in Exchange detected and disclosed in 2021, it’s important to remember that they were all used as 0-day in only two different campaigns. This is an example of why we don’t suggest using the number of 0-days in a product as a metric to assess the security of a product. Requiring the use of four 0-days for attackers to have success is preferable to an attacker only needing one 0-day to successfully gain access.


While this is the first time Exchange in-the-wild 0-days have been detected and disclosed since Project Zero began our tracking, this is not unexpected. In 2020 there was [n-day exploitation of Exchange Servers](https://www.cisa.gov/uscert/ncas/current-activity/2020/03/10/unpatched-microsoft-exchange-servers-vulnerable-cve-2020-0688). Whether this was the first year that attackers began the 0-day exploitation or if this was the first year that defenders began detecting the 0-day exploitation, this is not an unexpected evolution and we’ll likely see it continue into 2022.

# Outstanding Questions

While there has been progress on detection and disclosure, that progress has shown just how much work there still is to do. The more data we gained, the more questions that arose about biases in detection, what we’re missing and why, and the need for more transparency from both vendors and researchers.


Until the day that attackers decide to happily share all their exploits with us, we can’t fully know what percentage of 0-days are publicly known about. However when we pull together our expertise as security researchers and anecdotes from others in the industry, it paints a picture of some of the data we’re very likely missing. From that, these are some of the key questions we’re asking ourselves as we move into 2022:

## Where are the \[x\] 0-days?

Despite the number of 0-days found in 2021, there are key targets missing from the 0-days discovered. For example, we know that messaging applications like WhatsApp, Signal, Telegram, etc. are targets of interest to attackers and yet there’s only 1 messaging app, in this case iMessage, 0-day found this past year. Since we began tracking in mid-2014 the total is two: a WhatsApp 0-day in 2019 and this iMessage 0-day found in 2021.


Along with messaging apps, there are other platforms/targets we’d expect to see 0-days targeting, yet there are no or very few public examples. For example, since mid-2014 there’s only one in-the-wild 0-day each for macOS and Linux. There are no known in-the-wild 0-days targeting cloud, CPU vulnerabilities, or other phone components such as the WiFi chip or the baseband.


This leads to the question of whether these 0-days are absent due to lack of detection, lack of disclosure, or both?

## Do some vendors have no known in-the-wild 0-days because they’ve never been found or because they don’t publicly disclose?

Unless a vendor has told us that they will publicly disclose exploitation status for all vulnerabilities in their platforms, we, the public, don’t know if the absence of an annotation means that there is no known exploitation of a vulnerability or if there is, but the vendor is just not sharing that information publicly. Thankfully this question is something that has a pretty clear solution: all device and software vendors agreeing to publicly disclose when there is evidence to suggest that a vulnerability in their product is being exploited in-the-wild.

## Are we seeing the same bug patterns because that’s what we know how to detect?

As we described earlier in this report, all the 0-days we saw in 2021 had similarities to previously seen vulnerabilities. This leads us to wonder whether or not that’s actually representative of what attackers are using. Are attackers actually having success exclusively using vulnerabilities in bug classes and components that are previously public? Or are we detecting all these 0-days with known bug patterns because that’s what we know how to detect? Public security research would suggest that yes, attackers are still able to have success with using vulnerabilities in known components and bug classes the majority of the time. But we’d still expect to see a few novel and unexpected vulnerabilities in the grouping. We posed this question back in the 2019 year-in-review and it still lingers.

## Where are the spl0itz?

To successfully exploit a vulnerability there are two key pieces that make up that exploit: the vulnerability being exploited, and the exploitation method (how that vulnerability is turned into something useful).


Unfortunately, this report could only really analyze one of these components: the vulnerability. Out of the 58 0-days, only 5 have an exploit sample publicly available. Discovered in-the-wild 0-days are the failure case for attackers and a key opportunity for defenders to learn what attackers are doing and make it harder, more time-intensive, more costly, to do it again. Yet without the exploit sample or a detailed technical write-up based upon the sample, we can only focus on fixing the vulnerability rather than also mitigating the exploitation method. This means that attackers are able to continue to use their existing exploit methods rather than having to go back to the design and development phase to build a new exploitation method. While acknowledging that sharing exploit samples can be challenging (we have that challenge too!), we hope in 2022 there will be more sharing of exploit samples or detailed technical write-ups so that we can come together to use every possible piece of information to make it harder for the attackers to exploit more users.


As an aside, if you have an exploit sample that you’re willing to share with us, please reach out. Whether it’s sharing with us and having us write a detailed technical description and analysis or having us share it publicly, we’d be happy to work with you.

# Conclusion

Looking back on 2021, what comes to mind is “baby steps”. We can see clear industry improvement in the detection and disclosure of 0-day exploits. But the better detection and disclosure has highlighted other opportunities for progress. As an industry we’re not making 0-day hard. Attackers are having success using vulnerabilities similar to what we’ve seen previously and in components that have previously been discussed as attack surfaces.The goal is to force attackers to start from scratch each time we detect one of their exploits: they’re forced to discover a whole new vulnerability, they have to invest the time in learning and analyzing a new attack surface, they must develop a brand new exploitation method. And while we made distinct progress in detection and disclosure it has shown us areas where that can continue to improve.


While this all may seem daunting, the promising part is that we’ve done it before: we have made clear progress on previously daunting goals. In 2019, we discussed the large detection deficit for 0-day exploits and 2 years later more than double were detected and disclosed. So while there is still plenty more work to do, it’s a tractable problem. There are concrete steps that the tech and security industries can take to make it even more progress:

1. Make it an industry standard behavior for all vendors to publicly disclose when there is evidence to suggest that a vulnerability in their product is being exploited,
2. Vendors and security researchers sharing exploit samples or detailed descriptions of the exploit techniques.
3. Continued concerted efforts on reducing memory corruption vulnerabilities or rendering them unexploitable.


Through 2021 we continually saw the real world impacts of the use of 0-day exploits against users and entities. Amnesty International, the Citizen Lab, and others highlighted [over](https://citizenlab.ca/2021/10/breaking-news-new-york-times-journalist-ben-hubbard-pegasus/) and [over](https://www.amnesty.org/en/documents/doc10/4491/2021/en/) how governments were using commercial surveillance products against [journalists](https://forbiddenstories.org/pegasus-the-new-global-weapon-for-silencing-journalists/), [human rights defenders](https://www.amnesty.org/en/latest/research/2021/11/devices-of-palestinian-human-rights-defenders-hacked-with-nso-groups-pegasus-spyware-2/), and [government officials](https://www.reuters.com/technology/exclusive-us-state-department-phones-hacked-with-israeli-company-spyware-sources-2021-12-03/). We saw many enterprises scrambling to remediate and protect themselves from the [Exchange Server 0-days](https://www.microsoft.com/security/blog/2021/03/02/hafnium-targeting-exchange-servers/). And we even learned of peer [security researchers being targeted by](https://blog.google/threat-analysis-group/update-campaign-targeting-security-researchers/) [North Korean government hackers](https://blog.google/threat-analysis-group/update-campaign-targeting-security-researchers/). While the majority of people on the planet do not need to worry about their own personal risk of being targeted with 0-days, 0-day exploitation still affects us all. These 0-days tend to have an outsized impact on society so we need to continue doing whatever we can to make it harder for attackers to be successful in these attacks.


2021 showed us we’re on the right track and making progress, but there’s plenty more to be done to make 0-day hard.
