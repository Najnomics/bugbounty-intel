# Hidden in Plain Sight

- **Source URL:** https://medium.com/@domenicoveneziano/hidden-in-plain-sight-uncovering-rce-on-a-forgotten-axis2-instance-86ddc91f1415?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240915112246/https://medium.com/@domenicoveneziano/hidden-in-plain-sight-uncovering-rce-on-a-forgotten-axis2-instance-86ddc91f1415
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7058 (id 7058)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Hidden in Plain Sight: Uncovering RCE on a Forgotten Axis2 Instance

# Introduction

While looking for interesting assets on one of [**Tryber**](https://www.tryber.me/ethical-hacking-community)’s bug bounty programs, I identified a simple yet impactful vulnerability. 

The affected asset, which could not be located via other well known methods like **Google Dorking** or **Wayback Machine** logs, was discovered using the **SecurityTrails API**. 

This hidden asset was hosting an Apache **Axis2** instance, which, when accessed, revealed an admin login page. 

The login page was vulnerable due to **default credentials** being left in place, that allowed me to access the **administration panel** and ultimately obtain a **remote code execution**.

# Getting Access

The discovery of the Axis2 admin panel was not straightforward. 

After identifying the asset using the SecurityTrails API, I proceeded to **brute-force** potential directories using a set of **known paths**. 

To avoid detection by the **Akamai WAF** protecting the site, I employed **residential rotating proxies** while using a **Nuclei template** (CVE-2010–0219) for the scan. 

Once the **Axis2 login page** was found, I could access it using the **default credentials**. 

Although the website did not handle the login process correctly, it was still possible to navigate the admin panel by **manually managing session cookies**, which the server inconsistently applied.

# Getting RCE

With access to the Axis2 admin panel, I was able to exploit the system further by **uploading a malicious .aar file**.

This file was crafted to **implement** a **new service** that could **execute arbitrary commands** on the **server**. 

After successfully uploading the exploit, I gained **remote code execution** (RCE) capabilities, confirmed by accessing the reverse shell at **redacted.com/axis2/services/config/exec?cmd=dir**

# Conclusions

This report shows that sometimes the best finds are in places where no one else has thought to look. 

Even websites that seem basic or unimportant can have serious vulnerabilities like RCE just a click away. 

Using some creative techniques to **bypass** a strong web application firewall — like **custom wordlists** and **rotating proxies** — eventually pays off in these scenarios.

**Don’t overlook any site**, no matter how unappealing it might seem, because you never know where a major vulnerability might be hiding.
