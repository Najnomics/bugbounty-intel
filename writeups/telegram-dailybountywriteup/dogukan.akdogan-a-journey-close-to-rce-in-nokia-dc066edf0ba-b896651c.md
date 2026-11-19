# A Journey Close to RCE in Nokia

- **Source URL:** https://medium.com/@dogukan.akdogan/a-journey-close-to-rce-in-nokia-dc066edf0ba?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251129101212/https://medium.com/@dogukan.akdogan/a-journey-close-to-rce-in-nokia-dc066edf0ba
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3615 (id 3615)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# A Journey Close to RCE in Nokia

Hello everyone. In this article, I will share the story of how I came very close to discovering an RCE (Remote Code Execution) vulnerability in Nokia’s Bug Bounty program.

While exploring Bug Bounty programs, I noticed an abundance of subdomains under Nokia’s umbrella, which caught my attention. I decided to set my sights on Nokia as a target. After listing the target domains in a file named “domain.txt,” I kicked off the reconnaissance process.In the days leading up to this, I had already discovered **2 Dom XSS (Cross-Site Scripting)** vulnerabilities and **1 instance of information disclosure**. Finding an **RCE** would be a fantastic final touch.

During the reconnaissance phase, I employed multiple tools. Especially, my custom-built automation tool significantly sped up my efforts and streamlined the process for me. I ran the following command using my “recon” tool, which I had aliased to a Python script:

```
alias  recon='python3 /path/to/py/file/full-auto.py'
recon -dL domain.txt -o /path/to/output/out.txt
```
This tool contained various subdomain discovery utilities, URL finders, and many more helpful features.

While waiting for the results from my reconnaissance tool, I began manually crawling the site using my methodology in “Xmind.” I had already outlined my methodology and continued my research without deviating from my plan. It was during this time that the notifications for the recon results came in.

While analyzing the results, I noticed a subdomain entry indicating the presence of an Oracle WebLogic Server in the “interest” section of the recon output. I proceeded to investigate the site and found that it was using Oracle WebLogic Server version 10.3.6.0.0 ;

My first step was to use the searchsploit tool:

`searchsploit Oracle WebLogic | grep "10.3.6.0"`
After this search, I identified the existence of an RCE vulnerability.

This was a critical juncture where I made a mistake by not checking if this vulnerability had been previously discovered for Nokia. With the excitement, I conducted a few more searches and realized I needed an IP address and port to proceed with the exploit. I had the IP address, but I couldn’t determine the port. During these testing days, I was facing VPN-related issues, causing my Nmap scans to be interrupted.

Wait a minute, an idea struck me. I quickly coded a small Python script that looped through the ports in the format “ip:{port}” and used the httpx tool to test them. I noticed the process was slow, so I revised the code to loop through all 65,536 ports without making requests, listing them all in a file:

I then ran the following command to scan all ports:

`httpx file all.txt -silent -probe >> httpx_result.txt`
Okay now lets check;

Now it’s time to proceed with trying out the exploit. We have found the required IP and port. After executing the commands in the exploit, I need to observe these results. For this purpose, I require Burp Collaborator. I copied my Burp Collaborator domain and added it to the exploit.

Now, I reached the more challenging part — trying different exploit methods. Despite my numerous attempts, I couldn’t reach a successful conclusion. I refused to give up and was trying every avenue until I stumbled upon a report stating that the vulnerability had been patched by Nokia. It was a bit disappointing, but I had gained valuable experience during this journey.

Thank you for reading my article. I hope this story serves as a guide to help you avoid the issues I faced. Good luck to everyone.
