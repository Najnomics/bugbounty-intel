# Joomla Security

- **Source URL:** https://medium.com/@aswinchandran274/joomla-security-insights-rce-f521b762acba?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126142033/https://medium.com/@aswinchandran274/joomla-security-insights-rce-f521b762acba
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/3678 (id 3678)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Joomla Security: Insights & RCE

## Introduction:

Hello Friends, In this blog, I will discuss Joomla CMS and its vulnerabilities. Additionally, I will provide the proof of concept (PoC) for exploiting the Joomla CVE-2023–23752 vulnerability, which can lead to code execution. Please note that the Joomla instance used for this demonstration is installed on my local machine.

## 1. What is Joomla?

Joomla is an open-source Content Management System (CMS), which is used to build websites and online applications. It is free and extendable which is separated into front-end and back-end templates (administrator). Joomla is developed using PHP, Object Oriented Programming, software design patterns and MySQL (used for storing the data).

It is the second most popular CMS for a website with more than 4.5% of market share and growing. Security is as important as website design and content, but we often ignore this until negatively impacted us. Not correctly configured/hardened Joomla server can be vulnerable to many including remote code execution, SQL Injection, Cross-Site Scripting, Information leakage, etc. Security is a process cycle, which one should always perform against web applications.

**Content Management System (CMS)**

The Content Management System (CMS) is a software which keeps track of the entire data (such as text, photos, music, document, etc.) which will be available on your website. It helps in editing, publishing and modifying the content of the website.

## 2. What are Joomla’s vulnerabilities?

The Joomla vulnerabilities are a flaw in the software that could allow an attacker to access sensitive information on a website.

If exploited, this vulnerability could allow the attacker to steal user passwords, delete files, or even take over a website.

## 3. Vulnerabilities found in Joomla

Joomla is an award-winning CMS It is a popular choice for many businesses. Owing to its large user base, this CMS regularly encounters a wide range of security-related issues.

It does not properly sanitize user input, which can allow attackers to inject malicious code into the application. This can lead to the execution of arbitrary code, disclosure of sensitive information, or denial of service.

Another issue is It does not properly validate session cookies, which can allow an attacker to hijack a user’s session and gain access to the application. This can lead to the disclosure of sensitive information or the execution of arbitrary code.

Joomla is also vulnerable to cross-site scripting (XSS) and SQL injection attacks. These attacks can allow an attacker to execute malicious code or SQL commands on the server, which can lead to the disclosure of sensitive information or the execution of arbitrary code.

It is recommended that users update to the latest version of Joomla as soon as possible to mitigate these vulnerabilities. Additionally, users should consider using a web application firewall.

### **Recently discovered common vulnerabilities in Joomla**

**1. SQL Injection Vulnerability**

Joomla 3.7 became victim to an SQL Injection Vulnerability: CVE-2017–8917. Easily exploited, the vulnerability stems from a new component, com\_fields, which first appeared in version 3.7. Due to public access to this component, the vulnerability stands to be exploited by any individual visiting your Joomla site with a malicious intent.

Deemed as one of the most rampantly occurring web attacks today, an SQL Injection attack is carried out when an attacker inserts a malicious code in SQL statements. Joomla, WordPress, and PHP are largely affected by this vulnerability due to the widespread use of the SQL database on such web platforms. The ramifications of such a security breach vary from authentication bypass to information disclosure to extending the malicious code to other application users.

In the case of Joomla, the vulnerable component is accessible on the public-facing site making it extremely easy to exploit. All the attacker has to do is craft malicious URLs, insert his own SQL operations, and access the URL. The solution lies in updating to the latest Joomla version which has reportedly patched up this vulnerability

**2. Cross Site Scripting Vulnerability (XSS)**

Joomla has also been prone to two Cross-Site Scripting (XSS) vulnerabilities: CVE-2017–7985 and CVE-2017–7986. which ended up affecting Joomla versions 1.5.0 through 3.6.5.

An XSS vulnerability exists in these versions because Joomla fails to sanitize malicious user input when users post or edit an article. To exploit this, an attacker would run a malicious code in the victim’s browser, in turn gaining control of his/her Joomla account. If the victim has admin permissions, the attacker could gain full control of the server.

An attacker can add this code to Joomla by exploiting this XSS vulnerability, Although Joomla has its own XSS filters, one could still find a way to bypass these filters. Its existing filters sterilize dangerous code like “javascript:alert()”, “background:url()” and so on when a user posts something with HTML attributes.

**3. Privilege Escalation Vulnerability**

The privilege escalation vulnerability has been deemed as a critical vulnerability in Joomla versions 3.4.4 through 3.6.3. In this, a module creates an arbitrary account with administrative privileges. Thereafter, an e-mail is sent to activate the account, if an email server is configured in the CMS.

After activating the account, the attacker will have a valid account with permissions to log in to the administrator/ interface, edit one of the templates, and inject PHP code. Affected versions can allow users in Administrator group to install extensions, thus creating further scope for code executions.

Privilege escalation is achieved by passing extra parameters in a call to the user.register and parameters stored in the database is passed as an array of user.

By exploiting this feature, an attacker could upload the PHP backdoors on the website and gain access to the server. Moreover, the attacker could also gain full access to the system while trying to elevate the limited Linux user.

## 4. Juumla

**Description:**

Juumla is a Python tool designed for Joomla websites. It serves to quickly determine the version of the Joomla CMS in use, and also performs scans to detect potential vulnerabilities and sensitive files within the Joomla installation.

**Features of Juumla**

**1. Fast Scan:** Juumla offers efficient and rapid scanning of Joomla websites, saving time during security assessments.

**2. Resource Efficiency:** The tool is designed to use minimal RAM and CPU resources, preventing significant impact on system performance.

**3. Version Detection:** Juumla can accurately identify the Joomla version in use, aiding in assessing the site’s software status.

**4. Config and Backup Files:** It can locate configuration and backup files, which can be crucial for identifying potential security gaps.

**5. Vulnerability Scanning:** Juumla assesses vulnerabilities based on the Joomla version, assisting in pinpointing potential security risks

**Advantages of Juumla**

**1. Efficiency:** Juumla’s speed and low resource usage make it suitable for quickly assessing multiple Joomla sites.

**2. Accuracy:** Accurately identifying the Joomla version and vulnerabilities aid in targeted security measures.

**3. Resource-Friendly:** The tool’s efficient resource usage minimizes disruption to the website’s normal operation during scanning.

**4. Comprehensive Scan:** Juumla’s ability to find config files, backup files, and vulnerabilities enhances its utility in identifying potential security gaps.

**Installation**

**Step 1:** Run the following command to install Juumla

**$ git clone https://github.com/oppsec/juumla.git**

$ cd juumla

$ pip3 install -r requirements.txt

**Step 2:** Now run the following command to use Juumla

**$ python3 main.py -u URL**

**JOOMLA RCE POC**

**Step 1:** Here, I installed a vulnerable version of Joomla on my local Machine.

**Step 2:** Next, I scanned the Joomla installation using a Juumla tool to identify the Joomla version for any associated vulnerabilities and then the tool successfully identified the Joomla version and provided information about vulnerabilities related to that specific version.

**Step 3:** After identifying the vulnerabilities, I searched to find an exploit that would target the identified vulnerability.

**Step 4:** After finding the exploit, we successfully exploited the vulnerability by directly accessing this endpoint [**https://localhost/Joomla/api/index.php/v1/config/application?public=true**](https://localhost/Joomla/api/index.php/v1/config/application?public=true) of Joomla. It leaks the system configuration which contains Joomla MySQL Credentials ***root:password123*** in the plain text.

**Notes:** This vulnerability leaks the MySQL credentials, in default and most common configurations MySQL will be exposed only on 127.0.0.1 which makes the attack ineffective. But if the database is exposed publicly, we can see how it affects the site

**Step 5:** we access the database by using the credentials found in the information disclosure that allows an attacker to access the Joomla super user’s password. The following demonstrates enumerating the password of the Joomla admin web interface using the MySQL client.

**Step 6:** Check the hashing algorithm used in the password to crack the password or update the password of the Joomla admin web interface. Now we Identified the hashing algorithm used in joomla.

**Step 7:** After Identifying the hash algorithm we can try to update our password by hashing using the same algorithm. Here I used the online tool to hash our password

**Step 8:** Now update our hashed password in the user table.

**Notes:** Instead of updating our password we can try to crack the admin password by using hash cat but this method is not effective.

**Step 9:** we can try to access the Joomla admin web interface by using the updated password

**Step 10:** we successfully login into the Joomla admin web interface by using an updated password.

**Step 11:** Now we modify a template in Joomla to include malicious PHP. The image below demonstrates the addition of a tiny web shell to index.php. This will allow the attacker to execute arbitrary code.

**Step 12:** Finally, we can access the tiny web shell from the URL cmd parameter

**Link:** [https://localhost/Joomla/index.php?cmd=uname%20-a](https://localhost/Joomla/index.php?cmd=uname+-a)

**Notes:** In CVE-2023–23752 Instead of leaking the MySQL credentials, the attacker can leak the Joomla user database also by accessing this endpoint directly **https://localhost/Joomla/api/index.php/v1/users?public=true**

Here the database output contains usernames, emails, and assigned groups (e.g. Super Users). This should be enough for credential stuffing or brute force to achieve Admin access.

## Conclusion

Thank you for reading my blog. I would love to hear your feedback and suggestions to improve future posts. Stay tuned for more cybersecurity insights!
