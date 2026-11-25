# Escalating SSTI to Reflected XSS using curly braces { }

- **Source URL:** https://sagarsajeev.medium.com/escalating-ssti-to-reflected-xss-using-curly-braces-825685bd93ec?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221211013039/https://sagarsajeev.medium.com/escalating-ssti-to-reflected-xss-using-curly-braces-825685bd93ec?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/318 (id 318)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SSTI to XSS using curly braces {}

Hello everyone! My name is Sagar Sajeev and this is my writeup explaining how I was able to escalate a Server Side Template Injection (P4) to a much more severe XSS.

Note:

For those who haven't heard of Server Side Template Injection or SSTI, I’ll recommend you to get some understanding about SSTI before reading this writeup.

I’ve made a specific writeup explaining SSTI. You can check it out by clicking [here](https://web.archive.org/web/20221211013039/https://sagarsajeev.medium.com/server-side-template-injection-something-distinct-f0ac234e379).

Basically, it’s a way to inject something(payload) into the template engine which in turn gets executed on server side.


# Target Scenario

- After hours of hardwork of trying to find an endpoint vulnerable to XSS, I finally came to an one which seemed interesting to me.
- It was exposing a sign up page. What was interesting about this was, it was kept hidden. The url looked something like:

https://www.redacted.com/engine/signup/create.php


- I tried XSS payloads there, but it was filtering everything. It was then I thought of adding curly braces {} to the first name, last name and address field.
- To my surprise, all three of the fields did not carry out any specific filtering for curly braces.
- I tried the following payload:-

{{ <svg/onload=prompt("XSS")> }}


- I know the payload looks complicated. It’s just that all entities are URL-encoded.

This is how decoded payload looks:

{{ \<svg/onload=prompt(“XSS”)> }}


- The thing is that, direct payload was not going through for some reason. I had to intercept the request using burp and then add the encoded payload.
- XSS was fired. Well, the thing is that this is just self-XSS.

# Self XSS to Stored XSS

- The target website had a section where you could create projects. Think of the project as a folder where you can store files.
- The project admin can share this to other “authenticated users”.
- The project must be given a name and is shared using a link.
- Well, I named the project with the payload. Thus, now the file name is:-

{{ <svg/onload=prompt("XSS")> }}


- Insane bruh moment. No File name restrictions were kept and I could name the project in however way I want.
- Copy the share project link and sent it to other authenticated users. As I mentioned before, only authenticated users can view the project. So, the application forces the user to login before being able to see the shared project.
- When an authenticated user clicks on the link, Voilà and here it is! The XSS pop-up.

# Quick Recap

- SSTI based Self-XSS payload was created.
- Self-XSS was escalated to Reflected XSS (differs according to attack scenario).
- SSTI → Self XSS → Reflected XSS
- This ,in fact, could be escalated to more severity. The attacker could just create a project and share its link on social media. If ,by chance an authenticated user randomly clicks on the link, XSS could be triggered.
- My SSTI writeup can be found here:- [https://sagarsajeev.medium.com/server-side-template-injection-something-distinct-f0ac234e379](https://web.archive.org/web/20221211013039/https://sagarsajeev.medium.com/server-side-template-injection-something-distinct-f0ac234e379)

Tips:-

- Make sure you spend time understanding the target. I spent nearly a week on this target to find this.
- Don’t keep on changing from one program to another just because you aren’t able to find a specific bug. Make a list of vulnerabilities you have learned and test each of them accordingly.
- Also, make sure to explain the impact to the highest severity. Let them know of the most potential impact that the vulnerability could have.
- I recommend you to make notes. May it be handwritten or in Notion. Make sure that you take notes. It will help in the long run.

Timeline

Submitted : 18–09–2022

Accepted : 19–09–2022

Rewarded with Amazon gift card : 22–09–2022


I do occasionally share some tips about Bug Bounties and related stuff over at my Twitter and LinkedIn handle. So do follow me there. If you’ve got any queries, feel free to message me. I will be more than happy to help.

LinkedIn : [https://www.linkedin.com/in/sagar-sajeev/](https://web.archive.org/web/20221211013039/https://www.linkedin.com/in/sagar-sajeev/)

Twitter : [https://twitter.com/Sagar\_\_Sajeev](https://web.archive.org/web/20221211013039/https://twitter.com/Sagar__Sajeev)

Thanks for going through my writeup and I hope it was useful to you. I’ve made many other writeups on my [Medium handle](https://web.archive.org/web/20221211013039/https://medium.com/@sagarsajeev). Please do check those out as well.

*Happy Hunting!*
