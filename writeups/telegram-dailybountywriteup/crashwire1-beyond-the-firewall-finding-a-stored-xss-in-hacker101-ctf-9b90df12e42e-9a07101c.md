# Beyond the Firewall

- **Source URL:** https://medium.com/@crashwire1/beyond-the-firewall-finding-a-stored-xss-in-hacker101-ctf-9b90df12e42e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240219022715/https://medium.com/@crashwire1/beyond-the-firewall-finding-a-stored-xss-in-hacker101-ctf-9b90df12e42e
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5247 (id 5247)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Introduction**

Participation in bug bounty programs or Capture The Flag (CTF) competitions plays a pivotal role in uncovering vulnerabilities and strengthening security measures. Recently, my involvement in a Hacker101 CTF event led to the discovery of a stored Cross-Site Scripting (XSS) vulnerability — a vulnerability that must have gone previously unnoticed by the organizers, since this exploit is not a Flag within the challenge.

This article recounts my exploration of the vulnerability and underscores the importance of thorough testing and continuous vigilance in safeguarding our digital ecosystems.

***Note:*** Although the Hacker101 domain is within the scope of HackerOne's Bug Bounty program, the Challenges/instances themselves are not. That being said, I went ahead and submitted an informative report prior to publishing this article, in the event they wanted to update the challenge or include the vulnerability as a flag.

The team at HackerOne was very prompt and professional in their response, but opted to close the report after reviewing. So if you want to replicate this attack vector on the Postbook CTF Challenge, you can check it out [**here**](https://ctf.hacker101.com/)!


**Discovery**As I navigated through the “Postbook” CTF virtual machine (VM), I stumbled upon a seemingly innocuous feature: the username update function. While the initial sign-up and sign-in page appeared to validate input against special characters my curiosity prompted me to dig deeper.

As we see in the image above, the application is performing input validation on the “sign-up” source. While I could have attempted a client-side bypass, I opted to simply create an account within the parameters and explore the application further. To my surprise, I found that the update username feature within the “Settings” page lacked any input validation, opening a potential security loophole.

**Vulnerability**

This input validation oversight ultimately allowed me to inject malicious JavaScript string into my username, which was then stored and displayed on the homepage alongside blog posts. The gravity of this stored XSS vulnerability cannot be overstated — it enables malicious actors to execute arbitrary JavaScript code within other users’ browsers.

**Steps to Reproduce:**

1\. Create a sign-up profile with the username “test” and password “test”


2\. Log in through the “Sign-in” page and create a blog post with the title “test” and body “test”


3\. Navigate to the “Settings” section


4\. Update the username with the following payload:


`<script>alert('Username XSS')</script>`
5\. Return to the homepage and refresh the page to observe the XSS payload firing in the browser


6\. We can further verify that the XSS is stored within the Home page by viewing our blog post in the page source code


**Impact**

The discovery of this vulnerability highlights the importance of thorough testing in web-app development. Despite the initial input validation on the sign-up page, the oversight in the username update function exposed a critical flaw.

When exploited, a stored XSS could allow attackers to steal session cookies or authentication tokens of logged-in users (leading to account takeover), conduct data-theft, distribute further malware, etc. This incident serves as a reminder that even seemingly minor features can harbor hidden threats, emphasizing the need for constant vigilance in security practices during web-app development.

**Recommendations**

To mitigate the risk posed by such vulnerabilities, it is crucial to implement robust input validation mechanisms across all user input fields. By diligently validating and sanitizing user input, developers can prevent the execution of arbitrary scripts and strengthen defenses against XSS attacks. Additionally, promoting user awareness about selecting secure usernames can enhance overall security and reduce the likelihood of future exploits.

**Conclusion**

My experience in uncovering this previously unlisted XSS vulnerability during the Hacker101 CTF underscores the importance of proactive testing and continuous vigilance in cybersecurity. By sharing this discovery, I hope to raise awareness about the latent dangers lurking within seemingly benign features and advocate for a proactive approach to security. Together, let us strive to create a safer and more resilient digital landscape for all.

**Thanks for reading! Follow me here on Instagram for more content**
