# IDOR To Delete Hall Of Fame Page.

- **Source URL:** https://medium.com/@pratikkaran/idor-to-delete-hall-of-fame-page-273724bd03ed?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126143103/https://medium.com/@pratikkaran/idor-to-delete-hall-of-fame-page-273724bd03ed
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3269 (id 3269)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# IDOR To Delete Hall Of Fame Page.

Hacking through GUID’s

Hey Hacker’s, This is [Pratik Karan](https://www.linkedin.com/in/pratik-karan-310b06214/), I’m Sharing My One of my finding with you all. Hope you enjoy and Learn Something New.

## **What Is IDOR?**

IDOR is nothing but insecure direct object reference it is one of the access control vulnerabilities

This happens when they give direct access to the resource which the users cannot able to access that resource without any validation

You Can Learn Here More: [https://portswigger.net/web-security/access-control/idor](https://portswigger.net/web-security/access-control/idor)

Lets Get Straight To The Point:)

**Target Info:**


I Was doing Pentesting on One of the privately hosted Program consider as *redacted.com*. They have option to Host Websites Same Like WordPress\[Web Content Management System\]. So We can just have to make changes in the content that we want on our website and we can Set the Web Page Live And Other users can access it on On Internet through Page URL.

**Hosted URL Looks like this: *https://redacted.com/page-name-abcdef***

**Page Structure:**


Whole Page Is divided in blocks which have particular ID’s, You can imagine as this:

So When Any User Host their Web Page Live this block ID’s also get leaked In the source code of the Page. \[GOT THE GUID’s🤫\]

**Summary:**


So Here While Editing Page I found one endpoint which sorts the block ID’s in ascending order:

So Here as we put Victim’s Page Block ID*\[That we got from LIVE Page Source Code\]*. It Just Simply Copies the particular block from Victim’s Page to Attacker’s Page. **😢NO SEVERE IMPACT.**

Lets see Further..

**STEPS TO REPRODUCE:**


1. Login to Attacker Account > Turn on burp Proxy > Create a Page and Create some blocks in it.
2. Vulnerable request will get captured in Burp history > Send it to Repeater tab\[/api/project/xxxxxxx/sort-order\]
3. Go to Repeater tab > Replace the Attacker ID’s with the Victim block ID and Send the request. As now you already know that it will simply copy the block as it is from victim live page to attacker’s page.
4. Now our block is been copied and saved, Our Page is Ready to Set LIVE:)
5. But I Didn’t Liked the Page And I Simply Deleted the Page. And Guess What😁**Victim’s Block Also gets Disappear from the LIVE PAGE.**

**Conclusion:**


Attacker Sets the Victim’s Block GUID in his own Page and When Attacker Deletes the Whole Page All the Blocks and its associated ID’s also Get Deleted.

**IMPACT:**


Attacker is Able to Take Down\[or Make it disappear\] Any Users LIVE Hosted Page.

In This Way, I Was Able to take Down the Target Company’s Hall Of Fame which Was hosted on their Own Web App*{****https://redacted.com/hall-of-fame-abcdef}***.

Thank you for reading so far.

In case you want to reach out, here’s where you can find me.

**Twitter:** [https://twitter.com/pratikkarankr](https://twitter.com/pratikkarankr)

**Linkedin:** [https://www.linkedin.com/in/pratik-karan-310b06214/](https://www.linkedin.com/in/pratik-karan-310b06214/)
