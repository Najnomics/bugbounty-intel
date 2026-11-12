# Breaking the Chain - Project Zero

Source: https://projectzero.google/2016/11/breaking-chain.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by James Forshaw, Wielder of Bolt Cutters.

Much as we’d like it to be true, it seems undeniable that we’ll never fix all security bugs just by looking for them. One of most productive ways to dealing with this fact is to implement exploit mitigations. Project Zero considers mitigation work just as important as finding vulnerabilities. Sometimes we can get our hands dirty, such as helping out Adobe and Microsoft in [Flash mitigations](/2015/07/significant-flash-exploit-mitigations_16.html). Sometimes we can only help indirectly via publishing our research and giving vendors an incentive to add their own [mitigations](/2015/08/windows-10hh-symbolic-link-mitigations.html).

This blog post is about an important exploit mitigation I developed for Chrome on Windows. It will detail many of the challenges I faced when trying to get this mitigation released to protect end-users of Chrome. It’s recently shipped to users of Chrome on Windows 10 (in M54), and ended up blocking the sandbox escape of an exploit chain being used [in the wild](https://security.googleblog.com/2016/10/disclosing-vulnerabilities-to-protect.html).

For information on the Chromium bug that contains the list of things we implemented in order to get this mitigation working, look [here](https://bugs.chromium.org/p/chromium/issues/detail?id=523278).

## The Problem with Win32k

It’s possible to lockdown a sandbox such as Chrome’s pretty comprehensively using Restricted Tokens. However one of the big problems on Windows is locking down access to system calls. On Windows you have both the normal NT system calls and Win32k system calls for accessing the GUI which combined represents a significant attack surface.


While the NT system calls do have exploitable vulnerabilities now and again (for example issue [865](https://bugs.chromium.org/p/project-zero/issues/detail?id=865)) it’s nothing compared to Win32k. From just one research project alone 31 issues were [discovered](https://bugs.chromium.org/p/project-zero/issues/list?can=1&q=vendor%3AMicrosoft+Nils), and this isn’t counting the many font issues Mateusz has found and the hundreds of other issues found by other researchers.

Much of Win32k’s problems come from history. In the first versions of Windows NT almost all the code responsible for the windowing system existed in user-mode. Unfortunately for 90’s era computers this wasn’t exactly good for performance so for NT 4 Microsoft moved a significant portion of what was user-mode code into the kernel (becoming the driver, win32k.sys). This was a time before Slammer, before Blaster, before the infamous [Trustworthy Computing Memo](https://www.wired.com/2002/01/bill-gates-trustworthy-computing/) which focussed Microsoft to think about security first. Perhaps some lone voice spoke for security that day, but was overwhelmed by performance considerations. We’ll never know for sure, however what it did do was make Win32k a large fragile mess which seems to have persisted to this day. And the attack surface this large fragile mess exposed could not be removed from any sandboxed process.

That all changed with the release of Windows 8. Microsoft introduced the [System Call Disable Policy](<https://msdn.microsoft.com/en-us/library/windows/desktop/hh871472(v=vs.85).aspx>), which allows a developer to completely block access to the Win32k system call table. While it doesn’t do anything for normal system calls the fact that you could eliminate over a thousand win32k system calls, many of which have had serious security issues, would be a crucial reduction in the attack surface.

However no application in a default Windows installation used this policy (it’s said to have been introduced for non-GUI applications such as on Azure) and using it for something as complex as Chrome wasn’t going to be easy. The process of shipping Win32k lockdown required a number of architectural changes to be made to Chrome. This included replacing the GDI-based font code with Microsoft’s DirectWrite library. After around two years of effort Win32k lockdown was shipping [by default](https://docs.google.com/document/d/1gJDlk-9xkh6_8M_awrczWCaUuyr0Zd2TKjNBCiPO_G4/edit).

## The Problems with Flash in Chrome

Chrome uses a multi-process model, in which web page content is parsed inside Renderer processes, which are covered by the Win32k Lockdown policy for the Chrome sandbox. Plugins such as Flash and PDFium load into a different type of process, a PPAPI process, and due to circumstance these could not have the lockdown policy enabled. This would seem a pretty large weak point. Flash has not had the best security track record ([relevant](https://bugs.chromium.org/p/project-zero/issues/list?can=1&q=product%3Aflash)), making the likelihood of Flash being an RCE vector very high. Combine that with the relative ease of finding and exploiting Win32k vulnerabilities and you’ve got a perfect storm.

It would seem reasonable to assume that real attackers are finding Win32k vulnerabilities and using them to break out of restrictive sandboxes including Chrome’s using Flash as the RCE vector. The question was whether that was true. The first real confirmation that this was true came from the Hacking Team breach, which occurred in July 2015. In the dumped files was an unfixed Chrome exploit which used [Flash as the RCE vector](https://bugs.chromium.org/p/project-zero/issues/detail?id=472) and a [Win32k exploit](https://bugs.chromium.org/p/project-zero/issues/detail?id=473) to escape the sandbox. While both vulnerabilities were quickly fixed I came upon the idea that perhaps I could spend some time to implement the lockdown policy for PPAPI and eliminate this entire attack chain.

## Analysing the Problem

The first thing I needed to do was to determine what Win32k APIs were used by a plugin such as Flash. There are actually 3 main system DLLs that can be called by an application which end up issuing system calls to Win32k: USER32, GDI32 and IMM32. Each has slightly different responsibilities. The aim would be to enumerate all calls to these DLLs and replace them with APIs which didn’t rely on Win32k. Still it wasn’t just Flash that might call Win32k API but also the [Pepper APIs](https://developer.chrome.com/native-client/pepper_stable) implemented in Chrome.


I decided to take two approaches to finding out what code I needed to remove, import inspection and dynamic analysis. Import inspection is fairly simple, I just dumped any imports for the plugins such as the Pepper Flash plugin DLL and identified anything which came from the core windowing DLLs.

I then ran Flash and PDFium with a number of different files to try and exercise the code paths which used Win32k system calls. I attached WinDBG to the process and set breakpoints on all functions starting with NtUser and NtGdi which I could find. These are the system call stubs used to call Win32k from the various DLLs. This allowed me to catch functions which were in the PPAPI layer or not directly imported.

Win32k system call using code in Flash and PDFium was almost entirely to enumerate font information, either directly or via the PPAPI. There was some [OpenSSL code](https://github.com/openssl/openssl/blob/99b00fd99330afb0be46265c3e28f25f938d3221/crypto/rand/rand_win.c) in Flash which uses the desktop window as a source of entropy, but as this could never work in the Chrome sandbox it’s clear that this was vestigial (or Flash’s SSL random number generator is broken, chose one or the other).

Getting rid of the font enumeration code used through PPAPI was easy. Chrome already supported replacing GDI based font rendering and enumeration with [DirectWrite](<https://msdn.microsoft.com/en-us/library/windows/desktop/dd368038(v=vs.85).aspx>) which does all the rendering in User Mode.  Most of the actual rendering in Flash and PDFium is done using their own TrueType font implementations (such as FreeType). Enabling DirectWrite for PPAPI processes was implemented in a number of stages, with the final enabling of DirectWrite in [this commit](https://chromium.googlesource.com/chromium/src.git/+/30ce0db09000893a6a44e9ade4912bbd3d45eccc).

Now I just needed to get rid of the GDI font code in Flash and PDFium itself. For PDFium I was able to repurpose existing font code used for Linux and macOS. After much testing to ensure the font rendering didn’t regress from GDI I was able to put the patch into PDFium. Now the only problem was Flash. As a prototype I implemented shims for all the font APIs used by Flash and emulated them using DirectWrite.

For a better, more robust solution I needed to get changes made to Flash. I don’t have access to the Flash source code, however Google does have a good working relationship with Adobe and I used this to get the necessary changes implemented. It turned out that there was a Pepper API which did all that was needed to replace the GDI font handling, pp::flash::FontFile. Unfortunately that was only implemented on Linux, however I was able to put together a proof-of-concept Windows implementation of pp::flash::FontFile and through Xing Zhang of Adobe we got a [full implementation](https://chromium.googlesource.com/chromium/src.git/+/eca2b40dd6ffacdf9e1772e5d18c3623d71b2946) in Chrome and Flash.

## Doomed Rights Management

From this point I could enable Win32k lockdown for plugins and after much testing everything seemed to be working, until I tried to test some DRM protected video. While encrypted video worked, any Flash video file which required output protection (such as High-bandwidth Digital Content Protection (HDCP)) would not. HDCP works by encrypting the video data between the graphics output and the display, designed to prevent people capturing a digital video.

Still this presents a problem, as video along with games are some of the only residual uses of Flash. In testing, this also affected the [Widevine](http://www.widevine.com/) plugin that implements the Encrypted Media Extensions for Chrome. Widevine uses PPAPI under the hood; not fixing this issue would break all HD content playback.

Enabling HDCP on Windows requires the use of a small number of Win32k APIs. I’d not discovered this during my initial analysis because, a) I didn’t run any protected content through the Flash player and b) all functions were imported at runtime using LoadLibrary and GetProcAddress only when needed. The function Flash was accessing was OPMGetVideoOutputsFromHMONITOR which is exposed by dxva2.dll. This function in turn maps down to multiple Win32k calls such as NtGdiCreateOPMProtectedOutputs.

The ideal way of fixing this would be to implement a new API in Chrome which exposed enabling HDCP then get Adobe and Widevine to use that implementation. It turns out that the Adobe DRM and Widevine teams are under greater constraints than normal development teams. After discussion with my original contact at Adobe they didn’t have access to the DRM code for Flash. I was able to have meetings with Widevine (they’re part of Google) and the Adobe DRM team but in the end I decided to go it alone and implement redirection of these APIs as part of the sandbox code.

Fortunately this doesn’t compromise the security guarantees of the original API because of the way Microsoft designed it. To prevent a MitM attack against the API calls (i.e. you hook the API and return the answer the caller expects, such as HDCP is enabled) the call is secured between the caller and graphics driver using a X.509 certificate chain returned during initialization.


Once the application such as Flash verifies this certificate chain is valid it will send back a session key to the graphics driver encrypted using the end certificate’s public key. The driver then decrypts the session key and all communication from then on is encrypted and hashed using variants of this key. Of course this means that the driver must contain the private key corresponding to the public key in the end certificate, though at least in the case on my workstation that shouldn’t be a major issue as the end certificate has a special Key Usage OID (1.3.6.1.4.1.311.10.5.8) and the root “Microsoft Digital Media Authority” certificate isn’t in the trusted certificate store so the chain wouldn’t be trusted anyway. Users of the API can embed the root certificate directly in their code and verify its trust before continuing.


As the APIs assume that it’s already been brokered (at minimum via Win32k.sys) then adding another broker, in this case one which brokers from the PPAPI process to another process in Chrome without the Win32k lockdown policy in place, doesn’t affect the security guarantees of the API. Of course I made best efforts to verify the data being brokered to limit the potential attack surface, though I’ll admit something about sending binary blobs to a graphics driver gives me the chills.


This solved the issue with enabling output protection for DRM’ed content and finally the mitigation could be enabled by default. The commit for this code can be found [here](https://chromium.googlesource.com/chromium/src.git/+/5ef755bb1a9e77e296b46a08e4cb61078e769609).

## Avoiding #yolosec

Implementation wise it turned out to be not too complex once I’d found all the different possible places that Win32k functions could be called. Much of the groundwork was already in place with the original Win32k Renderer lockdown, the implementation of DirectWrite and the way the Pepper APIs were structured. So ship it already!

Well not so fast, this is where reality kicks in. Chrome on Windows is relied upon by millions upon millions of users worldwide and Win32k lockdown for PPAPI would affect not only Flash, but PDFium (which is used in things like the Print Preview window) and Widevine. It’s imperative that this code is tested in the real world but in such a way that the impact on stability and functionality can be measured.

Chrome supports something called Variations which allow developers to selectively enable experimental features remotely and deploy them to a randomly selected group of users who’ve opted into returning usage and crash statistics to Google. For example you can do a simple A/B test with one proportion of the Chrome users left as a Control and another with Win32k lockdown enabled. Statistical analysis can be performed on the results of that test based on various metrics, such as number of crashes, hanging processes and startup performance to detect anomalous behaviour which is due to the experimental code. To avoid impacting users of Stable this is typically only done on Beta, Dev and Canary users. Having these early release versions of Chrome are really important for ensuring features work as expected and we appreciate anyone who takes the time to run them.

In the end this process of testing took longer than the implementation. Issues were discovered and fixed, stability measured until finally we were ready to ship. Unfortunately in that process there was a noticeable stability issue on Windows 8.1 and below which we couldn’t track down. The stability issues are likely down to interactions with third party code (such as AV) which inject their own code into Chrome processes. If this injected code relies on calling Win32k APIs for anything there’s a high chance of this causing a crash.

This stability issue led to the hard decision to initially only allow the PPAPI Win32k lockdown to run on Windows 10 (where if anything stability improved). I hope to revisit this decision in the future. As third party code is likely to be updated to support the now shipping Windows 10 lockdown it might improve stability on Windows 8/8.1.

As of M54 of Chrome, Win32k lockdown is enabled by default for users on Windows 10 (with an option to disable it remotely in the unlikely event a problem surfaces). As of M56 (set for release approximately the end of January 2017) it can only be disabled with a command line switch to disable all Win32k lockdown including Renderer processes.

## Wrap Up

From the first patch submitted in September 2015 to the final patch in June it took almost 10 months of effort to come up with a shipping mitigation. The fact that it’s had its first public success (and who knows how many non-public ones) shows that it was worth implementing this mitigation.

In the latest version of Windows 10, Anniversary Edition, Microsoft have implemented a Win32k filter which makes it easier to reduce the attack surface without completely disabling all the system calls which might have sped up development. Microsoft are also taking pro-active effort to improve the Win32k code base.

The Win32k filter is already used in Edge, however at the moment only Microsoft can use it as the executable signature is checked before allowing the filter to be enabled. Also it’s not clear that the filter even completely blocked the vulnerability in the recent in-the-wild exploit chain. Microsoft would only state it would “[stop all observed in-the-wild instances of this exploit](https://blogs.technet.microsoft.com/mmpc/2016/11/01/our-commitment-to-our-customers-security/)”. Nuking the Win32k system calls from orbit is the only way to be sure that an attacker can’t find a bug which passes through the filter.

Hopefully this blog post demonstrates the time and effort required to implement what seems on the face of it a fairly simple and clear mitigation policy for an application as complex as Chrome. We’ll continue to try and use the operating system provided sandboxing mechanisms to make all users on Chrome more secure.

## Thanks

While I took on a large proportion of the technical work it’s clear this mitigation could not have shipped without the help of others in Chrome and outside. I’d like to especially mention the following:

- Anantanarayanan Lyengar, for landing the original Win32k mitigations for the Renderer processes on which all this is based.
- Will Harris, for dealing with variations and crash reporting to ensure everything was stable.
- Adobe Security Team and Xing Zhang for helping to remove GDI font code from Flash.
- The Widevine team for advice on DRM issues.
