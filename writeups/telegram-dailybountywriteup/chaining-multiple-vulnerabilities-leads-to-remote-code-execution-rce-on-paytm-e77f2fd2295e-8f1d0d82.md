# Chaining Multiple Vulnerabilities Leads to Remote Code Execution (RCE).

- **Source URL:** https://rohit-soni.medium.com/chaining-multiple-vulnerabilities-leads-to-remote-code-execution-rce-on-paytm-e77f2fd2295e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250910205641/https://rohit-soni.medium.com/chaining-multiple-vulnerabilities-leads-to-remote-code-execution-rce-on-paytm-e77f2fd2295e
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/705 (id 705)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Chaining Multiple Vulnerabilities Leads to Remote Code Execution (RCE) on One of the Payment Service Companies.

Jenkins RCE through groovy script console.

*Hey everyone! I hope you all are doing well!*

Rohit Soni is back with another write-up and this time it’s about multiple security vulnerabilities I found and chained them together to achieve RCE on one of the payment service companies. Since I am not allowed to disclose the company name, let’s keep it example.in.

I’ve been hunting on their bug bounty program since a while and already reported few vulnerabilities but reporting any critical vulnerability (Such as LFI, SQLi, SSRF or RCE) was one of my goal from past few days.

### Simple Recon:

Hunting started from understanding the scope and enumerating subdomains (all subdomains are in-scope). I am not going much deep into subdomain enumeration because already so many nice blogs and write-ups are out there specifically for subdomain enumeration.

**Few Resources:**


I’ve collected all in-scope domains, used my favorite tools ([subfinder](https://github.com/projectdiscovery/subfinder), [assetfinder](https://github.com/tomnomnom/assetfinder) and [chaos](https://github.com/projectdiscovery/chaos-client)) to gather subdomains, clubbed output of different tools in single file and used [httpx](https://github.com/projectdiscovery/httpx) tool to filter out live/working subdomains.

While going through file containing live subdomains of example.in domain I discovered one of the subdomain has Jenkins instance running on it.

**What is Jenkins?**

Jenkins is an open source automation server. It helps automate the parts of software development related to building, testing, and deploying, facilitating continuous integration and continuous delivery (CI/CD).


### #1: Signup enabled on Jenkins instance.

As soon as I opened the subdomain.example.in it asked for credentials and to my surprise, signup was enabled.

I quickly created an account and login but unfortunately the newly created user was not having administrator permissions.

Since my account was kind of view only user account. I could not perform any administrative actions such as creating pipeline, running build, managing plugins, managing users, **executing OS level commands**, etc. Still I managed to find some interesting things, one of them was “people” menu.

People menu was showing list of all usernames existing in the Jenkins system. Though it was low vulnerability I was about to report it but I knew very few things about Jenkins so thought to ask somebody who have good knowledge of it.

One of my colleague had experience of working with Jenkins and CI/CD integration in his past job. I told him about the scenario and he explained me lot of things very nicely but we didn’t concluded with anything which can increase the impact of the vulnerability I’ve just discovered. At last he suggested me to bruteforce the passwords since I have all existing usernames.

### #2: Broken Authentication Due to Weak Password.

I dumped all the usernames. There were total 1228 users in the system. Bruteforcing even 10000 common passwords for 1228 users can eat up huge amount of time. So I thought to bruteforce same password as username. (For example, If the username is xyz, try xyz as a password). I used burp intruder functionality to perform bruteforce and to my surprise I found 277 out of 1228 users have same password as their usernames.

I again went to login form and entered the very first user seen in above image, in both username and password and it worked. I was lucky because the account I’ve logged in had administrative permission. After login I had access to plenty of stuff. I had access to all pipelines, plugins, script console, in short all admin functionalities which Jenkins provide.

### #3: Its RCE time !!

I installed terminal plugin using plugin manager. this plugin allows user to execute OS commands right from the Jenkins instance but when I try to run any command such as pwd or ls or any simple command, It was showing only 403 Forbidden. May be this was due to cloudflare WAF.

Nope….This was not my last hope. We have alternate way — “Groovy Script Console”.

I went to https://subdomain.example.in/computer/ to see all slave nodes connected with the master node.

I clicked on one of the slave node and navigated to script console from left side menu and entered below script and clicked on RUN button.

println “id”.execute().text


and yeah, id command was executed on the server. Wee weee RCE.!!

### Reporting is necessary skill for white hats.

I took enough time to prepare a nice report. I included everything from how I was able to login into their Jenkins as a view only user to how I obtained access to user account with admin privileges to RCE.

To show impact I have prepared scripts for all nodes to retrieve sensitive information. Such as AWS secrets and SSH private keys.

They fixed the vulnerability within few days and restricted access to this subdomain and rewarded me with my highest bounty till date.

### TL; DR

1\. Signup enabled on Jenkins instance.

2\. Created account and found valid usernames.

3\. Bruteforced to find if any user has same username and password. Found 277 out of 1228 user has same username and password.

4\. Found user with admin permissions.

5\. Used script console to execute OS commands.


Hope you enjoyed the write-up. If you have any questions or suggestions reach me through instagram, twitter or linkedin.

*Happy Hunting. :-)*


Instagram: [@street\_of\_hacker](http://instagram.com/street_of_hacker/)

Twitter: [@streetofhacker](https://twitter.com/streetofhacker)

LinkedIn: [Rohit Soni](https://www.linkedin.com/in/rohit-soni-r007/)
