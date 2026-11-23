# How i created my first XSS tool

- **Source URL:** https://medium.com/@mithun_/how-i-created-my-first-xss-tool-xss-pro-bugbounty-982a16079baf?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240817013005/https://medium.com/@mithun_/how-i-created-my-first-xss-tool-xss-pro-bugbounty-982a16079baf
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/6780 (id 6780)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hi Guys,

I’m Mithun, a security researcher and bug hunter. Recently I have created an XSS tool for Pen testers and Bug hunters.

**What is an XSS?**

XSS, or Cross-Site Scripting, is a type of security vulnerability typically found in web applications. It allows attackers to inject malicious scripts into web pages viewed by other users. These scripts can be used to steal information, hijack user sessions, redirect users to malicious websites, or perform other malicious activities.

Types of XSS:


*Reflected XSS (Non-Persistent XSS)*

*Stored XSS (Persistent XSS)*

*DOM-Based XSS*

**Tools to detect XSS**

There are multiple tools available for testing XSS, such as XSStrike and Dalfox. However, one common issue with these tools is their tendency to produce false positives. So i thought of building my own tool.

*I’m focusing on Reflected XSS*

# **How I Build my tool?**

After having N number of failures..failuress…failures…… SUCCESS😁😁😁😁👨💻 [link](https://github.com/mith36/XSS-PrO.git)


My requirement is to test XSS on web applications so like every tool I do wayback on the domain to get all the URLs associated with it.

[Waybackurls](https://github.com/tomnomnom/waybackurls) is a command-line tool used for scraping URLs from the Wayback Machine. you can follow the [link](https://github.com/tomnomnom/waybackurls) to install waybacurls.

I injected XSS payloads in one of the post request URLs and analyzed the output.

`http://testfire.net/search.jsp?query=<script>alert(1)</script>`
Then using the python script, I sent the requests and analyzed each response. If response contains the payload, then XSS is possible. **BUT!!!! This IDEA is WRONG🤦♂️🤦♂️🤦♂️🤦♂** Soon i realized that though the payload returns in the response, it does not necessarily mean that XSS is possible due to presence of o/p encoding.

Again I conducted further research to determine how to detect whether an XSS popup appeared on the rendered response page. Here I use [Selenium](https://www.selenium.dev/)😉😎

Selenium has a feature to handle popups, allowing them to click on the OK or CANCEL button as needed.

Here is the game changer!! I appended a payload to all the post URLs and visited each one using Selenium. Using the alert testing functionality, I checked whether an XSS popup appeared or not.

```
 try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            alert.accept()
            return True, alert_text
```
based on this i built my own tool.

**BOOMM!!!🔥🔥**

*This method works perfectly and got ZERO false positive results.*


Here is the link to my [tool](https://github.com/mith36/XSS-PrO.git).

\### Steps

1. First, clone my GitHub repo

```
git clone https://github.com/mith36/XSS-PrO.git
cd XSS-PrO
```
`waybackurls <target>  > urls.txt`
2\. Paste your payloads in the ***payloads.txt*** file

3\. Run XSS-Pro:

`python XSS_PRO.py --payloads payload.txt --urls url.txt`
# I’m keeping my tool open source, so if you’d like to contribute to its enhancement, you’re welcome to do so.

*Happy HACKING!👨💻👨💻*


**Limitations of the tool**

*- Multi-threading is not implemented.*

*- WAF bypass not implemented.*


This tool was developed back in January 2024.
