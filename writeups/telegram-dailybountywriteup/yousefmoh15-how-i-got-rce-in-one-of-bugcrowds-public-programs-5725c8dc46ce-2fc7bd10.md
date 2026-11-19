# How I got RCE in one of Bugcrowd's Public Programs

- **Source URL:** https://medium.com/@yousefmoh15/how-i-got-rce-in-one-of-bugcrowds-public-programs-5725c8dc46ce?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250830174434/https://medium.com/@yousefmoh15/how-i-got-rce-in-one-of-bugcrowds-public-programs-5725c8dc46ce
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5209 (id 5209)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# **How I got RCE in one of Bugcrowd's Public Programs**

Hello everyone,

Today I am going to share how I got RCE on one of Bugcrowd Public Programs. This is my first bug bounty write-up so, pardon me for my mistakes. A bit of introduction about me, My name is Yousef I’m a Cybersecurity Engineer and a part-time bug bounty hunter.

So, let’s Begin with the findings we will explain in this report.

While Looking for a program to hack on I always look for wide and open scoop programs as they give me so much freedom to look for assets that can match my skills. So, after I decided to start hacking on one of the public programs and after doing subdomain enumeration I decided to look at Shodan for assets that belong to the company via this query **org: Company. Inc**

and after spending some time I found an interesting asset to start hacking on, the reason to chose this asset is that I found non-normal ports open and both running **Tomcat/8.5.32**

So, The first thing I do is to run a full port scan on this IP and pass the output to **httpx** to check the HTTP Services

`naabu -host <ip> -p - -Pn -o portscan | httpx -sc -td -server` To My Surprise, I found more open ports, and one of the newly discovered ones has an HTTP service running

Now, we found port 8333 with another version of Tomcat, Great let’s start investigating.

First, let's search for CVEs related to this version using searchsploit `searchsploit "tomcat 7"`

Unfortunately none of those worked on my target including **CVE-2017–12617** and **CVE-2020–1938**

Back again to the home page, I decided to start directory and file fuzzing, First of all, I tried diresearch with the default wordlist

`dirserach -u http://x.x.x.x:8333`

However, there were no interesting findings but the `manager` and `host-manager` directory which gave me 401 so, I decided to check for default creds with Hydra

`hydra -L ~/tomcat-usernames -P ~/tomcat-passwords  x.x.x.x -s 8333 http-get /manager/html`
Again, No valid user found.

Back to fuzzing again but this time I used the shortlist from [https://github.com/six2dez/OneListForAll](https://github.com/six2dez/OneListForAll)

`dirsearch -u <http://x.x.x.x:8333/> -w ~/wordlist/OneListForAll/onelistforallshort.txt`
and this time I found a new directory /sdp/ >> 302 >> /sdp/validateUser.action with a login form

so, I immediately started testing for SQLi but with no luck.

Then I remembered the CVE-2017–5638 so I used the nuclei templates on this endpoint but again no results were found.

Back to directory Fuzzing after /sdp/ endpoint and this time, I got a new directory I found `/sdp/struts/webconsole.html?debug=console`

At that moment I was very happy thinking that I got MY RCE but again for the hundreds of times I stoppered against a lot of JS errors in the console and every time I fixed one another one appeared.

And, I ended up printing the html code in the OGNL console with no command execution.

Back to the history tab of my BURP session and while scrolling I found a new file called showLogin.action out of desperation I decided to try one payload I found while searching in labs and write-ups related to Apache Struts 2 and OGNL Injection

The payload was

which executes the command id on the server, now I added this payload to `showLogin.action` and sent it as a get request.

Suddenly what I never expected happened

And this was my reaction

Next, I reported this issue to BugCrowd and they triaged it immediately but the program later downgraded it to P2 saying that it was an old asset, and resolved it by deleting the IP.

## We are done!

Thanks for reading, hope you learned something new.
