# Multiple Organization Full account Take-over via privilege escalation

- **Source URL:** https://medium.com/@gb452011/multiple-organization-full-account-take-over-via-privilege-escalation-9d164ba10444?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251127032350/https://medium.com/@gb452011/multiple-organization-full-account-take-over-via-privilege-escalation-9d164ba10444
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/4064 (id 4064)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Multiple Organization Full account Take-over via privilege escalation

A High severity security flaw in the organization’s web application allows an attacker to takeover user accounts, including high-privileged users such as recruiters, admins, and even the CEO/CTO. This flaw exposes sensitive user data and grants unauthorized access to confidential information, posing significant business and technical risks. The vulnerability arises from improper access control mechanisms and inadequate input validation in the web application. Attackers exploit this flaw to navigate to unauthorized endpoints, access restricted resources, and manipulate user roles to takeover high-privileged account of same organization as well as different organization users.

let see how I was able to perform this :)

**Steps to Reproduce:**

1. Login using candidate details to access the web application.

**2)** Identify unique alphanumeric user IDs from the URL.

**3)** Now refresh the above page and intercept the below request in burp suite and sent the request to repeater tab in burp suite.

**4)** Attempt to access the /employer endpoint with unauthorized user IDs, leading to 404 errors.

**5)** Attempt to change the request method to POST, receiving 403 error, we can see that the request is valid but we don’t have enough permission.

**6)** On fuzzing the request with Param Miner *{burp Suite Extension}* for hidden headers and parameters, we got to know the hidden header “*X-Original-URL”* and *“employerId” parameter* present into particular request.

**7)** Add the “*X-Original-URL”* header with value *“/employer/search” and “employerId”* parameter value “*637f69562527bb2840XXXXX”,* which we got from main URL (*Fig 3*)

**Header-> X-Original-URL: /employer/search**

**Body-> {“employerId”:”637f69562527bb2840XXXXX”}**

Send the request and we can see all the user present in the current.

**8)** By above request, we can see the meta data of the current organization users including candidates and recruiters.

**9)** Now to take over the account of different user from the same organization. We will use edit “User Details” functionality of candidate user which is vulnerable for client validation bypass in which the restriction is implemented only on client side for the email field.

**10)** After click on apply, Intercept the edit “*User Details”* request in burp suite from the profile section.

**11)** To take over the account of different user from the same organization replace user id with recruiter’s id which we got from previous step and email value with attacker email.

**12)** By using reset password functionality, we successfully reset recruiter account in below step.

**13)** As we take over the Recruiter account, Now login with recruiter account. In the Recruiter account, we got to know about “*searchByEmail” & “SearchByName”* functionality, by which we search for CTO/CEO email which we got from approval section of recruiter.

**14)** Again, by using reset password functionality, we successfully takeover CEO/CTO account. *(Follow step number 12 to reset password of the any account)*

**15)** In the Admin panel, we can Manage Campaign, Job Credits, campaign Analysis, Manage Users functionality.

**16)** By Navigating into Manage Users tab, we can see all the high privilege operational user present into organization.

**17)** By using Search by Email functionality, search for any candidate, recruiter, HR, sales or CEO/CTO email, whose organization is managing the interview process through the current application. We can get their EmployerId, which are sufficient to perform admin account takeover attack for that particular organization from a different organization candidate user.

**Mind map:** To Enhance high level understanding of Application data flow and Attack Scenario.
