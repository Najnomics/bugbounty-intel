# XSS + Firewall Bypass And Detection

- **Source URL:** https://medium.com/@mohammedthoufeeq_25137/xss-firewall-bypass-and-detection-7aa67492f0c3?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20231012105026/https://medium.com/@mohammedthoufeeq_25137/xss-firewall-bypass-and-detection-7aa67492f0c3
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3700 (id 3700)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# XSS + Firewall Bypass And Detection

## Bug Bounty POC Preparation Guide For XSS Vulnerability

--

In this blog, we’re delving into the fascinating realm of web security by harnessing the power of two essential tools: WAFW00F and XSser. Our journey will revolve around not just detecting Cross-Site Scripting (XSS) attacks, but also skillfully navigating the intricacies of firewall detection and bypass and we harness the power of two tools:

- ***wafw00f*** for uncovering concealed firewalls, and
- ***xsser*** for detecting and potentially overcoming XSS vulnerabilities, even within fortified systems. Join us in mastering web security for a safer online experience.

**Installation**

WAFW00F:

Python Installation: Ensure you have Python installed. You can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Install WAFW00F: Open a terminal/command prompt and run the following command

`pip install wafw00f`
Verify Installation: To confirm that WAFW00F is installed correctly, type the following command in the terminal:

`wafw00f --version`
**XSSER**

If you are using kali linux, you can install it by

`sudo apt install xsser -y`
**Or**

Python Installation: Make sure you have Python installed, as XSser also requires Python to run.

Clone XSser Repository: Open a terminal/command prompt and navigate to the directory where you want to install XSser. Then, run the following command to clone the XSser repository:

`git clone https://github.com/epsylon/xsser.git`
Navigate to the XSser Directory: Change into the XSser directory using the following command:

`cd xsser`
Install XSser Dependencies: Run the following command to install the required dependencies:

`pip install -r requirements.txt`
Verify Installation: To ensure XSser is installed correctly, you can run a test command like this:

`python xsser.py --version`
WafW00f Usage :

To use WAFW00F, open a terminal/command prompt and run the command followed by the URL of the target website you want to check for the presence of a web application firewall (WAF):

`wafw00f <target_url>`
Example: Let’s say you want to check if the website “[http://www.example.com](http://www.example.com/)" is protected by a web application firewall. You would run:

`wafw00f http://www.example.com`
Advanced Options: WAFW00F offers several advanced options to customize the scan. For example, you can use the `-a` flag to show all detected firewalls, or the `-v` flag for verbose output.

`wafw00f -a -v http://www.example.com`
Help: If you need more details on available options, you can access the help menu by typing:

`wafw00f --help`
XSSER

Basic Usage: To use XSser, open a terminal/command prompt and navigate to the XSser directory where you’ve cloned the repository. Then, run the following command followed by the target URL

`xsser -u <target_url>`
Example

`xssr -u http://www.example.com`
Advanced Options: XSser provides various options for customizing the scan. For instance, you can use the `-v` flag for verbose output, or the `-e` flag to specify the URL encoding type.

`xsser -u http://www.example.com -v -e UTF-8`
Help: If you need more information about available options and parameters, you can access the help menu by typing:

`xsser -h`
To use XSser with multiple targets, you can provide a text file containing a list of URLs as input. XSser will then process each URL in the list and perform XSS vulnerability testing on them. Here’s how you can do it:

Create a Text File: Create a text file (let’s say `targets.txt`) in the same directory where you have XSser. In this file, list the URLs you want to test, each on a new line. For example:

```
http://www.example1.com 
http://www.example2.com 
http://www.example3.com
```
Run XSser with the Text File: Open a terminal/command prompt and navigate to the directory where XSser is located. Then, run the following command:

`xsser -l targets.txt`
This command tells XSser to load the URLs from the `targets.txt` file and perform XSS vulnerability testing on each of them.

If you want to use GUI, use this command

`xsser --gtk`
**Let\`s drive into the real world of hacking..,**

I utilized WAFW00F and XSser in tandem to automatically discern the presence of a firewall and identify potential XSS vulnerabilities. To enhance clarity, I’ve included a screenshot illustrating a proof of concept (PoC). This visual aid is a valuable resource for compiling comprehensive bug bounty reports.

**Firewall Check**

Result: No WAF Detected

XSS Check

`sudo xsser -u example.com/forum?q=XSS`
**Note: The Variable “XSS” is mandatory that it indicates to be tested.**


Result: Successfully discovered XSS.

U can use -auto mode to check for all xss payloads.(But it can trigger target and possibly detected)

Final part what if the website uses firewall.

So this website uses ModSecurity Firewall, you can bypass it by using the command,

`xsser -u <target_url> --Modsec` If you detect other type of firewall, try these arguments depending on your need.

**Follow for more …:)**

Comment if you want BeEF \[Browser Exploitation Framework\]+ Xss method
