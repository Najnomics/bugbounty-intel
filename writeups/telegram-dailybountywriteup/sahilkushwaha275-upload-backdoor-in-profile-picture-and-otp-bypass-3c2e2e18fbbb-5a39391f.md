# Upload Backdoor in profile picture and OTP Bypass

- **Source URL:** https://medium.com/@sahilkushwaha275/upload-backdoor-in-profile-picture-and-otp-bypass-3c2e2e18fbbb?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240914102547/https://medium.com/@sahilkushwaha275/upload-backdoor-in-profile-picture-and-otp-bypass-3c2e2e18fbbb
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5488 (id 5488)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hey, Curious Hunter’s…💀

Today I am going to tell you how I Upload Backdoor with profile picture upload functionality and simple OTP bypass with the help of the burp suite intruder tab in a private program.

I started doing recon on the website of the company I worked for, I got a few subdomains from which I did not get much specific information, so I decided to create unique dorks of my own so that I can use it for this purpose which I can find bugs.

here is my dork looks like

`site:*domain.com intitle:Sign Up`
**OTP Bypass:-**

I Just Got a login page with OTP Authentication. When I entered my number to log in, I got a 4-digit OTP the thought came to my mind why can’t we bypass it?, so I opened my Burp suite and forwarded the request to Intruder and added 4 digits word list from [Seclists](https://github.com/danielmiessler/SecLists/blob/master/Fuzzing/4-digits-0000-9999.txt)

When the request went out, I got a request whose content was different in length, when I opened it, I got “your mobile OTP has been verified”

Boom :) We bypassed the OTP well.

**Backdoor Uploading:-**

When I logged in to that website, I saw the functionality of a profile photo in it and when I started selecting a file, All Files was by default selected already in it, which meant that we could upload any file in the profile photo, so I uploaded a PHP backdoor shell in the profile photo.

As you can see in the above image, the profile is not rendered because it is not an image but a PHP file,

When I opened this image in New Tab, I got exactly what I wanted. We uploaded our backdoor to this web server with the help of profile photo functionality and we can now access it from anywhere.

# TIPS:- Always try to log in or Sign up at the target

Thanks for reading📖

Follow for more about bug bounty and cyber security🔒
