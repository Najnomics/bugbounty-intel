# Access control vulnerabilities and privilege escalation (Lab

- **Source URL:** https://medium.com/@TH3_4TC/access-control-vulnerabilities-and-privilege-escalation-lab-method-based-access-control-can-be-21ec73504083?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20230130005415/https://medium.com/@TH3_4TC/access-control-vulnerabilities-and-privilege-escalation-lab-method-based-access-control-can-be-21ec73504083
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/1557 (id 1557)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Access control vulnerabilities and privilege escalation (Lab: Method-based access control can be circumvented)

Hello everyone I’m Ahmed a new learner of bug bounty known as THE ATC TH3\_4TC I’m so happy share with you my first write-up of portswigger lab bug accsess control vurnablibty I hope it help someone till now I’ll hope you enjoy wish me the best to read my next writeup for my fisrt valid bounty or dup bug hhh

PS: sorry for my bad English

Link of lab : [https://portswigger.net/web-security/access-control/lab-method-based-access-control-can-be-circumvented](https://portswigger.net/web-security/access-control/lab-method-based-access-control-can-be-circumvented)

Degree : **PRACTITIONER**

**STEPS TAKEN :**

1. I logged in **admin account** with their credentials **administrator:admin**
2. I browsed his account to see his functionality in **admin** panel and options like **downgrade** and **upgrade**

**In the browser:**

3\. I Noticed the link of the requests of users **../admin-roles** and parameters **username & action**

4\. I logged out from admin account

5\. I logged in with normal user credentials **wiener:peter**

6\. I requested the link .**./admin-roles**

7\. I looked at burp i see that in the response that mark missing **‘username’ parameter**

8\. I added username parameter I get the same error

9\. I added username and action parameter i get the same error

10\. I changed the request from **get** to **post** i get error **‘unauthorized’ it make sense from previous labs I solved**

11\. I added the parameters **username and action** I get error **unauthorized**

12\. I changed the request from **post** to **put** and **BOOOM** I get **302** redirect then the best value **200 OK honey**

**LAB SOLVED**

My Tweeter is : [https://twitter.com/TH3\_4TC](https://twitter.com/TH3_4TC)
