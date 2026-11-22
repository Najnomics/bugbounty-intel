# Broken Access Control

- **Source URL:** https://medium.com/@BhaktiKhedkar/broken-access-control-a64597d52039?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221211192044/https://medium.com/@BhaktiKhedkar/broken-access-control-a64597d52039
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/178 (id 178)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# ***Broken Access Control***

Hey folks, hope you all are doing well! In OWASP Top 10 2021, the Broken Access Control (BAC) grabbed the first position with the most serious security risk. Broken Access Control issues are present when the restrictions imposed are only on the frontend and the backend APIs are never secured. Using the easily enumerable IDs is the root cause of Insecure Direct Object References (IDORs).

In this blog, I will be mostly focusing on my approach and scenarios which I encountered.

**What is access control?**

Authentication identifies the user and verifies them.

Session management identifies which subsequent HTTP requests are being made by that same user.

Access control determines whether the user is allowed to carry out the action which they are attempting to perform.

**Vertical access controls**

Vertical access controls are mechanisms that restrict access to sensitive functionality that is not available to other users. The key difference that this mechanism facilitates, is selective control.

For example, an administrator might be able to modify or delete any user’s account, while an ordinary user has no access to these actions.

**Horizontal access controls**

Horizontal access controls are mechanisms that restrict access to resources only to the assigned users.

For example, a banking application will allow a user to view transactions and make payments from their own accounts, but not the accounts of any other user.

**Context-dependent access controls**

Context-dependent access controls prevent a user from performing actions in the wrong order.

For example, a retail website might prevent users from modifying the contents of their shopping cart after they have made payment.

# **Broken Access Control**

Broken Access Control issues are present when the restrictions imposed are only on the frontend and the backend APIs are never secured. Broken Access Control in simple words means performing the actions outside the set of allowed permissions.

To put simply, broken access control allows attackers to bypass authorization which can allow them to view sensitive data or perform tasks as if they were a privileged user.

**Examples of broken access controls**

Broken Access Control happens when a user can perform actions he must not do.

**Vertical privilege escalation**

Access to a function that a user isn’t permitted to access.

EX: User can Access the admin panel and delete any user account

**Horizontal privilege escalation**

Horizontal privilege escalation arises when a user is able to gain access to resources belonging to another user, For example, if an employee should only be able to access their own employment and payroll records, but can in fact also accesses the records of \*\*other employees.\*\*

For example, a user might ordinarily access their own account page using a URL like the following: \[https://insecure-website.com/myaccount?id=123\] (https://insecure-website.com/myaccount?id=123), in that scenario if the attacker could able to modify the id parameter leads to horizontal privilege escalation.

**Horizontal to vertical privilege escalation**

For example, a horizontal escalation might allow an attacker to reset or capture the password belonging to another user. If the attacker targets an administrative user and compromises their account, then they can gain administrative access and so perform vertical privilege escalation.

Attacker might gain horizontal access to another user account and if he is an admin he will make a vertical privilege escalation

**Insecure direct object references (IDOR)**

It’s an Access Control Vulnerability that arises when an application uses user-supplied input to directly access the objects.

IDOR vulnerabilities are most commonly associated with horizontal privilege escalation but can also arise with vertical one.

**Functionality Related Questions**

Whenever testing any application which has user roles, always think for the following questions:

• What are the permissions of this user?

• Is the user having permission to perform this action?

• Can this user view this data?

• What will be the business impact if the imposed access control can be broken?

**Scenarios Encountered While Testing Applications for Broken Access Control**

Let’s see some of the scenarios which I have encountered.

**Scenario 1 — Insecure Direct Object Reference (IDOR) leads sensitive information disclosure**

The application was a public fund management. The application allowed the user to check payment files.

During the testing process, I opened the file and noticed the file id in the URL, which I changed to an another id. I was surprised to see that the file was contained other user’s sensitive bank details. Hence, Insecure Direct Object Reference (IDOR) led me to enumerate the bank details of all other users leading to simple broken access control issue.

**Scenario 2 — Breaking the Business Logic in Deliverable Management Platform**

In this scenario, the application was some sort of deliverable management platform. In this, the records had to be approved by an other user (Checker) as a maker cannot approve his own records.

The business logic imposed in this application is similar where same user cannot approve own records. For example if USER1 created RECORD1 and tried to approve it. The response shows Maker and checker could not be the same. Then I tried to approve record of USER2 which is RECORD2. After observing the POST request for approval I came to know that the record ID is passing in URL and request body. So I changed ID to RECORD1 and forwarded the request. To my surprise, the record got approved. So by changing the ID, I was able to bypass the imposed access control.

**Scenario 3 — Forced browsing**

This application was for Fund management. This is banking application contains 2 types of user Internal user (Bank Employees) and external user (Customers). While working on it, I noticed a dashboard where the user role was mentioned in the URL. I changed it to admin and saw that the admin dashboard opened. Admin functions and bank user details, such as name, role, mobile number, and email address, are exposed to external users. As a result, I was able to break the access control imposed by changing the URL.

**Scenario 4 — Breaking the Business Logic by modifying client side check**

In this case, the application was dealing with settlement amount between two banks for ATM/POS transactions where threshold percentages are maintain. The maker cannot approve his own records. When I was testing Maker-Checker functionality, the application said: “Maker and Checker should not same” for the approving own created record. After observing message in debugger we can see the function responsible for client side check: if (Checker==Maker \[0\]) shows error message, So I modified the request containing logic with (Checker!=Maker\[0\]). Then I tried to approve my own records the record got approved successfully.

**How to Protect Yourself**

Use of an access control matrix to define the access control rules is strongly recommended. Without documenting the security policy, there is no definition of what it means to be secure for that site. The policy should document what types of users can access the system, and what functions and content each of these types of users should be allowed to access to.

Access control vulnerabilities can generally be prevented by taking a defense-in-depth approach and applying the following principles:

- Never rely on obfuscation alone for access control.
- Unless a resource is intended to be publicly accessible, deny access by default.
- Wherever possible, use a single application-wide mechanism for enforcing access controls.
- At the code level, make it mandatory for developers to declare the access that is allowed for each resource, and deny access by default.
