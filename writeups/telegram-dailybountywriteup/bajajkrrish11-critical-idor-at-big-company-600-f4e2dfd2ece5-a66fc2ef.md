# Critical IDOR At Big company $600

- **Source URL:** https://medium.com/@bajajkrrish11/critical-idor-at-big-company-600-f4e2dfd2ece5?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230424041307/https://medium.com/@bajajkrrish11/critical-idor-at-big-company-600-f4e2dfd2ece5
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2439 (id 2439)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Critical IDOR At Big company $600

# Who am I ?

So hello everyone am krrish, Aapka dost aur companies ka saver :) ok ok majak se bhar, am krrish and I started hunting abt 1years ago, this is my 1st Medium Article and So let’s Begin with Amazing Story that leads to 600$ bounty at biggest mobile company(XIAOMI).

**Introduction:**

Xiaomi is a popular Chinese electronics company known for producing smartphones, laptops, and other consumer electronics. Recently, a bug was discovered on Xiaomi’s web servers where the Spring Actuator endpoints were publicly available.

**Overview of the Bug:**

Insecure Direct Object Reference (IDOR) vulnerabilities are a common security flaw in which applications unintentionally expose sensitive internal objects such as files, databases, and user details. The Open Web Application Security Project (OWASP) has ranked IDOR vulnerabilities among the top 10 most critical web application security risks.

**Game Changer**:

During a day after all testing and basic testing at Main Xiaomi Domain I don’t got any bug then, I wanna quit and move to other site but at a same time wanna give a one more try so I started Analysing all subdomains at \*.mi.com and got my Eyes at **https://Redacted.mi.com/** in this subdomain any User can provide service related queries at mi.com so I register at mi.com and from registered account i now login at [**https://Redacted.mi.com**](https://miservicemanager.mi.com/) and create an service query and as soon i created it i got an ID at my email for tracking the Service Request which is **MXXXXXX** So now i put this id in tracking code and got all my information.

Now, since the ID MXXXXXX is having a numerical Digits so its easy to brute force and I fired up my BurpSuite and Add my Intruder Request with Number Payloads and BOOM got All Service ID’S and that Leads to IDOR LEADING in Information Disclosure.

**I reported this at HackerOne and they Fix this issue :**

**Impact**:

1. *Critical IDOR* leading to Personal Information Disclosure(Emails, Name, Number, Etc).

2\. *Sensitive information disclosure*: Attackers could gain access to sensitive information about the application’s configuration, such as database credentials, system properties, and environment variables.

**Conclusion** :

In conclusion, IDOR on Xiaomi’s web servers is a serious security risk that should be addressed as soon as possible. By following the recommended steps, Xiaomi can mitigate the risks associated with this bug and ensure the security of their web servers.

*Reported*: March 17, 2023

*Triaged*: March 17, 2023

*FIX & Bounty*: Mar 21, 2023

**Bonus Point**: Don’t Forget to check Support Panels Request In BurpSuite :)

To Milte hai jld hi, jab tak ke liye Happy Hunting and Keep Grasping Skills.
