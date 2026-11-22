# How I found Subdomain Takeover on Red Bull

- **Source URL:** https://medium.com/@neverl0gbughunt/how-i-found-subdomain-takeover-on-red-bull-57540158a18?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230728212004/https://medium.com/@neverl0gbughunt/how-i-found-subdomain-takeover-on-red-bull-57540158a18
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3412 (id 3412)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I found Subdomain Takeover on Red Bull

--

Hello, world. Right? I hope so!

I am going to narrate how I discovered a subdomain takeover vulnerability at Red Bull using the Takeover tool!

I had the thought, “Today, I will sit down, take my notebook, and I will not leave until I find a vulnerability!”

That’s when I decided to select Red Bull as my hunting target and began examining the program.

Then we captured the scope.

After downloading the scope to my machine, I began to contemplate what I could search for and where I should focus my efforts. It was at that moment I thought, “Well, I have some friends who have already found subdomain takeovers here, so why not try to discover a domain for myself?

With everything decided and my excitement and determination to find a vulnerability and discover a vulnerable domain, I commenced the process of reconnaissance and exploration.

RECONNAISSANCE:

With the list of domains and subdomains in scope gathered, I made the decision to employ the “takeover” tool developed by m4ll0k.

Using this specialized tool, I began the process of scanning the collected domains and subdomains to identify potential subdomain takeover vulnerabilities. The tool leverages various techniques and checks for common misconfigurations or outdated DNS entries that could lead to a takeover.

During the scanning process, I remained vigilant and attentive, carefully examining each result and analyzing any potential issues that the tool highlighted. I made sure to record all findings for further investigation and verification.

By utilizing the “takeover” tool, I aimed to expedite the discovery of potential vulnerabilities and streamline the identification process. My goal was to find any subdomains that might be susceptible to takeover and take appropriate actions to report the findings responsibly.

As the reconnaissance phase progressed, I maintained a meticulous approach, understanding the importance of accurate and comprehensive data for the subsequent stages of this endeavor.

Discovery:

After a few minutes of running the tool, I discovered a vulnerable domain hosted on Heroku.

Exploitation:

Having identified the vulnerable domain and knowing that it is hosted on Heroku, it was time to take action. Below is a step-by-step account of the exploitation process:

1\. \*\*Verify Vulnerability\*\*: To ensure that the domain is genuinely vulnerable to subdomain takeover, I conducted additional checks and confirmed that the subdomain’s DNS configuration was misconfigured or outdated, leading to the potential takeover.

2\. \*\*Obtain Control of the Subdomain\*\*: With the vulnerability confirmed, I proceeded to take control of the subdomain. The process involved creating a new account on the Heroku platform or using an existing one, which allowed me to claim the affected subdomain.

3\. \*\*Verify Ownership\*\*: After taking control of the subdomain, I had to verify ownership through Heroku’s verification process. This step was necessary to establish my authority over the subdomain and proceed with the exploitation.

4\. \*\*Configure Subdomain\*\*: Once ownership was verified, I set up the configuration for the subdomain. This involved pointing the subdomain to a specific Heroku app or website of my choosing.

5\. \*\*Testing\*\*: After configuring the subdomain, I tested the setup to ensure that it was working correctly and the takeover was successful. I accessed the subdomain through the browser and confirmed that it directed traffic to the desired location.

6\. \*\*Documenting\*\*: Throughout the process, I meticulously documented each step taken and the changes made to the subdomain’s configuration. Detailed documentation is crucial for later reporting and responsible disclosure.

7\. \*\*Ethical Considerations\*\*: As an ethical hacker, I remained mindful of the impact of my actions. I refrained from causing any harm or unauthorized access to sensitive data during the exploitation process.

8\. \*\*Reporting\*\*: With the successful exploitation and takeover complete, I prepared a comprehensive report detailing the vulnerability, the steps taken, and potential mitigation measures. This report would be submitted to the appropriate stakeholders, such as Red Bull’s security team or their responsible disclosure program, ensuring that the issue is addressed promptly and responsibly.

9\. \*\*Post-Exploitation Cleanup\*\*: After reporting the vulnerability, I made sure to remove any traces of my actions and revert the subdomain to its original state. This step is essential to maintain the security and integrity of the affected system.

By following this methodical and responsible approach, I ensured that the subdomain takeover was conducted ethically, with the aim of improving the overall security of Red Bull’s online infrastructure.

And that’s how I won 3 cases of Red Bull! I want to thank everyone who read this far. I want to express my gratitude to two special individuals: OFJAAAH for supporting me throughout this hacking journey, and m4cddr for helping and encouraging me to write this first article.

I’m delighted to have succeeded in this ethical hacking endeavor, and receiving recognition for my discovery. I would like to emphasize that ethical hacking is a responsible practice that aims to identify and rectify vulnerabilities, contributing to the digital security of companies and users.

I appreciate the opportunity to share my story and acknowledge those who provided support along the way. Remember always to act ethically and responsibly in your information security activities, respecting laws and responsible disclosure policies of the affected companies.

If you have any other questions or need further assistance in the future, I’ll be here to help. Congratulations once again, and keep honing your cybersecurity skills ethically and positively!
