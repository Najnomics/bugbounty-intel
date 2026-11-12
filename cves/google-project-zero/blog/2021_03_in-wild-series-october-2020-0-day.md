# In-the-Wild Series: October 2020 0-day discovery - Project Zero

Source: https://projectzero.google/2021/03/in-wild-series-october-2020-0-day.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Maddie Stone, Project Zero


In October 2020, Google Project Zero discovered seven 0-day exploits being actively used in-the-wild. These exploits were delivered via "watering hole" attacks in a handful of websites pointing to two exploit servers that hosted exploit chains for Android, Windows, and iOS devices. These attacks appear to be the next iteration of the campaign discovered in February 2020 and documented in [this blog post series](/2021/01/introducing-in-wild-series.html).


In this post we are summarizing the exploit chains we discovered in October 2020. We have already published the details of the seven 0-day vulnerabilities exploited in our [root cause analysis (RCA) posts](https://googleprojectzero.github.io/0days-in-the-wild/rca.html). This post aims to provide the context around these exploits.

# What happened

In October 2020, we discovered that the actor from the [February 2020 campaign](/2021/01/introducing-in-wild-series.html) came back with the next iteration of their campaign: a couple dozen websites redirecting to an exploit server. Once our analysis began, we discovered links to a second exploit server on the same website. After initial fingerprinting (appearing to be based on the origin of the IP address and the user-agent), an iframe was injected into the website pointing to one of the two exploit servers.


In our testing, both of the exploit servers existed on all of the discovered domains. A summary of the two exploit servers is below:


Exploit server #1:

- Initially responded to only iOS and Windows user-agents
- Remained up and active for over a week from when we first started pulling exploits
- Replaced the Chrome renderer RCE with a new v8 0-day (CVE-2020-16009) after the initial one (CVE-2020-15999) was patched
- Briefly responded to Android user-agents after exploit server #2 went down (though we were only able to get the new Chrome renderer RCE)


Exploit server #2:

- Responded to Android user-agents
- Remained up and active for \~36 hours from when we first started pulling exploits
- In our experience, responded to a much smaller block of IP addresses than exploit server #1



The diagram above shows the flow of a device connecting to one of the affected websites. The device is directed to either exploit server #1 or exploit server #2. The following exploits are then delivered based on the device and browser.


| Exploit Server | Platform | Browser | Renderer RCE | Sandbox Escape | Local Privilege Escalation | 
| 1 | iOS | Safari | Stack R/W via Type 1 Fonts (CVE-2020-27930) | Not needed | Info leak via mach message trailers (CVE-2020-27950) Type confusion with turnstiles (CVE-2020-27932) | 
| 1 | Windows | Chrome | Freetype heap buffer overflow (CVE-2020-15999) | Not needed | cng.sys heap buffer overflow (CVE-2020-17087) | 
| 1 | Android \*\* Note: This was only delivered after #2 went down and CVE-2020-15999 was patched. | Chrome | V8 type confusion in TurboFan (CVE-2020-16009) | Unknown | Unknown | 
| 2 | Android | Chrome | Freetype heap buffer overflow (CVE-2020-15999) | Chrome for Android head buffer overflow (CVE-2020-16010) | Unknown | 
| 2 | Android | Samsung Browser | Freetype heap buffer overflow (CVE-2020-15999) | Chromium n-day | Unknown | 


All of the platforms employed obfuscation and anti-analysis checks, but each platform's obfuscation was different. For example, iOS is the only platform whose exploits were encrypted with ephemeral keys, meaning that the exploits couldn't be recovered from the packet dump alone, instead requiring an active MITM on our side to rewrite the exploit on-the-fly.


These operational exploits also lead us to believe that while the entities between exploit servers #1 and #2 are different, they are likely working in a coordinated fashion. Both exploit servers used the Chrome Freetype RCE (CVE-2020-15999) as the renderer exploit for Windows (exploit server #1) and Android (exploit server #2), but the code that surrounded these exploits was quite different. The fact that the two servers went down at different times also lends us to believe that there were two distinct operators.

# The exploits

In total, we collected:

- 1 full chain targeting fully patched Windows 10 using Google Chrome
- 2 partial chains targeting 2 different fully patched Android devices running Android 10 using Google Chrome and Samsung Browser, and
- RCE exploits for iOS 11-13 and privilege escalation exploit for iOS 13 (though the vulnerabilities were present up to iOS 14.1)


\*Note: iOS, Android, and Windows were the only devices we tested while the servers were still active. The lack of other exploit chains does not mean that those chains did not exist.


The seven 0-days exploited by this attacker are listed below. We’ve provided the technical details of each of the vulnerabilities and their exploits in the [root cause analyses](https://googleprojectzero.github.io/0days-in-the-wild/rca.html).

- [CVE-2020-15999](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2020/CVE-2020-15999.html) - Chrome Freetype heap buffer overflow
- [CVE-2020-17087](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2020/CVE-2020-17087.html) - Windows heap buffer overflow in cng.sys
- [CVE-2020-16009](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2020/CVE-2020-16009.html) - Chrome type confusion in TurboFan map deprecation
- [CVE-2020-16010](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2020/CVE-2020-16010.html) - Chrome for Android heap buffer overflow
- [CVE-2020-27930](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2020/CVE-2020-27930.html) - Safari arbitrary stack read/write via Type 1 fonts
- [CVE-2020-27950](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2020/CVE-2020-27950.html) - iOS XNU kernel memory disclosure in mach message trailers
- [CVE-2020-27932](https://googleprojectzero.github.io/0days-in-the-wild/0day-RCAs/2020/CVE-2020-27932.html) - iOS kernel type confusion with turnstiles


We were not able to collect any Android local privilege escalations prior to exploit server #2 being taken down. Exploit server #1 stayed up longer, and we were able to retrieve the privilege escalation exploits for iOS.


The vulnerabilities cover a fairly broad spectrum of issues - from a modern JIT vulnerability to a large cache of font bugs. Overall each of the exploits themselves showed an expert understanding of exploit development and the vulnerability being exploited. In the case of the Chrome Freetype 0-day, the exploitation method was novel to Project Zero. The process to figure out how to trigger the iOS kernel privilege vulnerability would have been non-trivial. The obfuscation methods were varied and time-consuming to figure out.

# Conclusion

Project Zero closed out 2020 with lots of long days analyzing lots of 0-day exploit chains and seven 0-day exploits. When combined with [their earlier 2020 operation](/2021/01/introducing-in-wild-series.html), the actor used at least 11 0-days in less than a year. We are so thankful to all of the vendors and defensive response teams who worked their own long days to analyze our reports and get patches released and applied.
