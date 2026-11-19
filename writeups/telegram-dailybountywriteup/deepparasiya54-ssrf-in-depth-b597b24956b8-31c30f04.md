# SSRF IN-DEPTH…

- **Source URL:** https://medium.com/@deepparasiya54/ssrf-in-depth-b597b24956b8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20220924141830/https://medium.com/@deepparasiya54/ssrf-in-depth-b597b24956b8
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/321 (id 321)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SSRF IN-DEPTH…

Hello mates, welcome back to my another blog.

Will talk about what ssrf is , where to check for, how to exploit & multiple bypasses & reports which help to escalate ssrf to rce ,etc.

**WHAT SSRF IS?**


SSRF also know as Server Side Request Forgery is one of the OWASP TOP 10 critical web vulnerability found on websites. This vulnerability allow an attacker to make unintended HTTP request to target’s back-end server. ssrf is generally found when main application interact with 3rd party org or request data from it. eg: [https://abc.example.com/image?url=https://image.com/image.jpg](https://abc.google.com/image?url=https://image.com/image.jpg) in this case google.com fetches image from 3rd party website ,an attacker can exploit this by manipulating the **url=** parameter by replacing the 3rd party with the [http://127.0.0.1](http://127.0.0.1) or with burp collabrator link (jdfqweufbvjbf.ostify.net). If we get the ping back to our collabrator client then there are high chances that abc.google.com can be potentially vulnerable to ssrf.

- if you dont have burp pro then you can use [requestbin](https://requestbin.com/?gclid=Cj0KCQjw1bqZBhDXARIsANTjCPLJIU-SW7h_jL00S3mF8MwMYVAUjlM4qEv6Jq6bDyPzwzZItcXpqYAaAjDMEALw_wcB) by signing in (free).

**IMPACT**


SSRF can lead to perform internal port scan on the host or fetch internal files from the server. the attacker may also be able to read server configuration such as AWS metadata, connect to internal services like HTTP-enabled databases or perform POST requests towards internal services that are not intended to be exposed.

**AREAS TO CHECK FOR**


- It can be usually found on the urls containig parameters url=,redirect=,uri=,proxy=,etc.
- It can be tested on upload functionality in which collabrator payload can be sent inside pdf (also can be tested for lfi if there is no input validation the php shell can be uploaded which can lead to RCE).
- It can also be tested by changing the reffer header in request with collabrator client.

**TYPES OF SSRF**


There are 2 types of ssrf:

1. BLIND SSRF : blind ssrf can be use to do the internal port scan by putting the burp collabrator link & port after parameter it scans for internal port which can be be confirmed by looking at the response time bcoz doing port scan for port that doesn’t exist taks time(invalid port) which confirms that here is blind ssrf in which server actually looks for port.

eg: [https://abc.example.com/ssrf.php? url=*https://weghrweyeu.ostify.net:139(burp*](<https://abc.example.com/ssrf.php?url=https://weghrweyeu.ostify.net(burp>) *collabrator client) which scans for port 139(smb) if the port is open then it returns 200 ok else if the port is closed and the response time is high than it confirms the presence of ssrf (reason: as the responce time is high like 1000ms or can be more which confirms that server scans for that port internally). The port scan can be done by replacing the port no from 1–65535 with the help of burp intruder.*

2\. FULL RESPONSE SSRF: It gives whole response of the requested resourse from the server in this case the server blindly validates the user supplied input. eg: [http://abc.example.com/proxy?url=file:///etc](http://abc.google.com/proxy?url=file:///etc)/passwd this will fetch the contenet of etc/passwd file. [here](https://gist.github.com/Deep2142004/445144584b68eead11441d37670d60cf) are the protocols that can be used while reading the internal server data.

BYPASSES


There are high chances that the website will be protected by firewall so [here](https://gist.github.com/Deep2142004/ac50058c096f1de68eb525941de487ef) is the few header bypass list that can be used.

Now-a-days there are high chances that localhost/127.0.0.1 won’t work because that can be blacklisted , [here](https://h.43z.one/ipconverter/) are the few baypass that can be used.

If the website is hosted on any cloud instance like aws,gcp,etc. in that case localhost/127.0.0.1 won’t work .so [here](https://gist.github.com/Deep2142004/5c4fd294a536c400f4b792e2f4797beb) is the list containg multiple urls which can be used to fuzz the parameter to leak sensitive data.

tip:- burp’s extension called **collabrator everywhere** can be used which adds all the headers with collabrator payload in the request which can help to find ssrf.

**RESOURCES**


portswigger academy : [https://portswigger.net/web-security/ssrf](https://portswigger.net/web-security/ssrf)

this includes not only detailed explaination but also contains labs that can be solved which can give idea how ssrf can be present in realword scenario.

kathan patel’s github repo: [https://github.com/KathanP19/HowToHunt/tree/master/SSRF](https://github.com/KathanP19/HowToHunt/tree/master/SSRF)

payloadallthethings ssrf repo containg multiple test cases ,bypasses & few selected top ssrf h1 reports & multiple references:

REPORTS


[https://medium.com/@D0rkerDevil/how-i-convert-ssrf-to-xss-in-a-ssrf-vulnerable-jira-e9f37ad5b158](/@D0rkerDevil/how-i-convert-ssrf-to-xss-in-a-ssrf-vulnerable-jira-e9f37ad5b158)

If you found it informative do leave a clap , follow & turn on email notification to get early notified by my future blogs.

Till then Happy Hacking….

Thank you…

#ssrf #webapppentesting #bugbounty #infosec #hacking
