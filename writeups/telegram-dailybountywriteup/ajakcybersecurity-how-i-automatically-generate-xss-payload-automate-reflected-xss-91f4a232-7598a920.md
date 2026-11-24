# How I Automatically Generate XSS Payload & Automate Reflected XSS

- **Source URL:** https://medium.com/@Ajakcybersecurity/how-i-automatically-generate-xss-payload-automate-reflected-xss-91f4a232cd78?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240222100706/https://medium.com/@Ajakcybersecurity/how-i-automatically-generate-xss-payload-automate-reflected-xss-91f4a232cd78
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/5046 (id 5046)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Automatically Generate XSS Payload & Automate Reflected XSS😎

--

Hi, Ajak Amico’s welcome back to another blog. Today I will share How I would Automatically Generate XSS Payload and automate the reflected XSS in my bug bounty journey. kindly don’t skip the blog as I mentioned with step by step. Before starting, if you haven’t subscribed to our channel, do subscribe, guys. Contents related to cyber security, Bug Bounty, and Digital Forensics Investigation.👇

*Follow our Youtube Channel: @ajakcybersecurity (361Videos)*

*Follow on Instagram: @ajakcybersecurity*


# What is XSS?

Cross-site scripting (XSS) is a vulnerability in a web application that allows a third party to execute a script in the user’s browser on behalf of the web application. Cross-site Scripting is one of the most prevalent vulnerabilities present on the web today. The exploitation of XSS against a user can lead to various consequences such as account compromise, account deletion, privilege escalation, malware infection and many more.

# What is Payload?

A payload is a piece of data that is used to exploit a vulnerability. It can be a string of characters, a file, or even a command, The goal of a payload is to cause the target system to do something that it is not supposed to do. This could be anything from displaying a message to taking control of the system.

Do you want to generate a payload for XSS automatically and automate reflected XSS? this tool is for this, especially for XSS

# XSS Loader:

*To Download: XSS Loader*

**How to install it?**

```
git clone https://github.com/capture0x/XSS-LOADER/
cd XSS-LOADER
pip3 install -r requirements.txt
```
**To run:**

`python3 payloader.py`
**Let’s Learn Practically:**

After running this tool you will see an interface as I mentioned in the screenshot below, you will see 9 columns, and you can choose your payload based on your input query. and down below you can see 30 options, where you can choose your query based on your website behaviour.

# Practise Site:

To Practice this tool with different queries, you can go to the following practice site **XSS game spot.** it has a prebuilt XSS scanner tool you can use that particular option it generates various payloads with the website.

# Automating Reflected XSS with Payload Generator:

Here Comes the best part to automate the XSS using the payload generator tool, for this, you need to click on the **7th option XSS scanner.** upon clicking you will be promoted to enter your target URL input query as you can see I have given a test site to play with this tool.

Once you give enter, it will check the vulnerable link, the vulnerable link will be indicated in red as mentioned in below screenshot.

now simply copy-paste the URL and paste it into your browser, BOOM! XSS will be triggered as mentioned below.

That’s all about the tool you can use this is part of the bug bounty

**P.S:** My suggestion is to learn the manual method to find XSS as a beginner.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

**“கற்றவை பற்றவை🔥”**

**Learn Everyday, Happy Hacking 😁🙌**

# [https://www.buymeacoffee.com/Ajak](https://www.buymeacoffee.com/Ajak)

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

*Follow our Youtube Channel: @ajakcybersecurity*

*Follow on Instagram: @ajakcybersecurity.*
