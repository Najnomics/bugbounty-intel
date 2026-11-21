# How I Find IDOR Vulnerabilities

- **Source URL:** https://samadhanshimple.medium.com/how-i-find-idor-vulnerabilities-my-complete-bug-bounty-hunting-methodology-8344cbecfde8
- **Fetched from:** https://samadhanshimple.medium.com/feed
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14994 (id 14994)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
IDOR (Insecure Direct Object Reference) is one of the most interesting vulnerabilities I look for during bug bounty hunting.

What makes IDOR interesting is that it does not always require complicated payloads or advanced exploitation techniques. Sometimes, a small change in an object identifier can reveal a serious authorization problem.

During my security testing, I learned that finding IDOR vulnerabilities is not just about changing numbers in URLs. It requires understanding how an application handles user data, manages permissions, and verifies access to different resources.

In this article, I will explain my approach to finding IDOR vulnerabilities, the techniques I use, the tools that help me, and some important things I check during testing.

### 1. Understanding How IDOR Works

Before starting IDOR testing, I first try to understand how the application identifies and accesses different objects.

For example, imagine an application where users can view their profiles through an API endpoint:

GET /api/users/1042/profile

Here, 1042 represents a user ID.

The important question is whether the application checks that the currently authenticated user is actually authorized to access that particular profile.

If the application only checks whether someone is logged in but does not verify ownership of the requested resource, another user might be able to access information they should not see.

This is the basic idea behind an IDOR vulnerability.

IDOR is closely related to Broken Object Level Authorization (BOLA), which is one of the important API security risks described by OWASP.

### 2. Map All Object References

One of the first things I do during IDOR testing is understand how the application uses object identifiers.

I explore different application features and intercept requests using Burp Suite.

I pay particular attention to requests that contain identifiers because they often represent resources belonging to individual users.

Here are some common places where I look:

**URL Paths**

- /api/users/123
- /documents/456
- /orders/ORD-123

**Query Parameters**

- ?user\_id=123
- ?account\_id=456
- ?order\_id=789

**Request Body**

```
{
  "account_id": 123,
  "document_id": 456
}
```
**HTTP Headers and Cookies**

I also inspect custom headers and cookie values to understand whether they contain references to user accounts or other application objects.

Some common parameter names I pay attention to include:

id, user\_id, account\_id, order\_id, document\_id, file\_id, invoice\_id, and transaction\_id.

However, I never assume that every identifier is vulnerable. The important part is understanding how the server validates access to the referenced object.

### 3. Create Two Test Accounts

For me, having two separate test accounts is one of the most useful parts of IDOR testing.

I usually create:

- **Account A:** My primary testing account.
- **Account B:** A second account with the same permissions.

Both accounts should have their own profiles, orders, documents, or other resources wherever possible.

I use these accounts to understand how the application separates data between different users.

For example:

1. Log in using Account A.
2. Open a feature that displays account-specific information.
3. Capture the HTTP request using Burp Suite.
4. Repeat the same action using Account B.
5. Compare the requests and responses.

This helps me identify which parameters represent user-specific objects.

It also gives me a reliable way to verify whether the application properly enforces authorization.

### 4. Test Object References Using Burp Suite Repeater

After identifying interesting parameters, I move to Burp Suite Repeater.

Repeater is useful because it allows me to resend requests and compare how the application responds to different authorized test scenarios.

For example, suppose Account A accesses:

GET /api/users/1042/profile

Account B has a different profile:

GET /api/users/1043/profile

I can use the resources belonging to my own two test accounts to check whether Account A is allowed to access Account B’s information.

The important thing is not simply whether the server returns HTTP 200.

I carefully examine the response body and check whether it contains information belonging to the other account.

I also check whether the server returns an authorization error, an empty response, or the expected resource.

**My observation:** A successful HTTP response does not automatically mean an IDOR exists. I need to confirm that the application actually exposes or modifies an object without proper authorization.

### 5. Don’t Focus Only on GET Requests

One mistake I see in basic IDOR testing approaches is focusing entirely on GET requests.

IDOR vulnerabilities can also affect operations that modify application data.

For this reason, I pay attention to different HTTP methods.

HTTP MethodWhat I investigateGETAccess to another user’s informationPOSTUnauthorized creation of resourcesPUTUnauthorized modification of resourcesPATCHUnauthorized partial updatesDELETEUnauthorized deletion of resources

For example, imagine an application where users can update their profile information.

I check whether the backend verifies ownership before accepting an update request.

The same approach applies to orders, saved addresses, uploaded documents, invoices, and other account-specific resources.

These tests should only be performed against accounts and resources I am authorized to use.

### 6. Look for IDOR in Less Obvious Locations

Not every IDOR vulnerability appears in a normal profile or account endpoint.

Some interesting authorization issues can exist in features that are easy to overlook.

During testing, I pay attention to:

**File Management**

- Viewing uploaded documents.
- Downloading private files.
- Accessing user-specific attachments.

**Order Management**

- Viewing order details.
- Accessing invoices.
- Updating order information.

**Account Management**

- Updating profile information.
- Managing saved addresses.
- Changing account preferences.

**Business Logic Features**

- Managing folders.
- Sharing documents.
- Creating resources.
- Managing team members.

I also review GraphQL APIs when available because they can expose object references through query arguments and mutations.

The main idea is to understand what objects each feature accesses and whether the backend checks the user’s permissions for every operation.

### 7. Testing GraphQL for IDOR

Modern applications increasingly use GraphQL instead of traditional REST APIs.

Because GraphQL uses queries and mutations, object identifiers may appear in different locations.

For example:

```
query {
  user(id: "1042") {
    id
    name
    email
  }
}
```
While reviewing GraphQL requests, I look for arguments that reference users, documents, orders, or other resources.

I also review the available API documentation and schema information when the application provides access to them.

I then use my authorized test accounts to compare access permissions.

The important thing to remember is that hiding an object from the frontend does not provide security. The backend must enforce authorization independently.

### 8. Tools I Use for IDOR Testing

Manual testing is extremely important when hunting for IDOR vulnerabilities.

However, some tools can make the process more organized and help identify interesting requests.

Here are some tools and features worth exploring.

### 1. Burp Suite

Burp Suite is one of the main tools I use during web application security testing.

Its Proxy feature helps me intercept application traffic, while Repeater allows me to inspect and compare individual requests.

I also use its HTTP history to identify endpoints and parameters that may reference sensitive objects.

### 2. Autorize

[https://github.com/Quitten/Autorize](https://github.com/Quitten/Autorize)

Autorize is a Burp Suite extension designed to help test authorization issues.

It can help identify situations where requests made under one user’s session may expose resources that should be restricted to another user.

It is particularly useful when reviewing access-control behavior across multiple endpoints.

### 3. AuthMatrix

[https://github.com/SecurityInnovation/AuthMatrix](https://github.com/SecurityInnovation/AuthMatrix)

AuthMatrix helps test authorization across different users and permission levels.

It is useful when an application has multiple roles and access-control rules that need to be compared.

### 4. Burp Suite Comparer

Comparer is useful when I need to compare HTTP requests and responses.

For example, I can compare the responses received from two test accounts and look for differences in returned information.

This can help identify unexpected access to account-specific resources.

### 5. Custom Python Scripts

Sometimes, I use small Python scripts to organize requests and compare responses.

Custom automation can be useful when testing many endpoints, but I always review the results manually.

An automated scanner may identify suspicious behavior, but it cannot always understand the application’s business logic or determine whether an action was actually unauthorized.

**Important:** Some additional tools and extensions are advertised as automated IDOR or BOLA scanners. Before using or recommending them, verify that their repositories, documentation, and functionality are genuine. I prefer tools with publicly available source code and clear documentation.

### 9. Understanding the Impact of IDOR

Not every IDOR vulnerability has the same severity.

The impact depends on what information or functionality becomes accessible without authorization.

Here are some examples:

VulnerabilityPotential ImpactReading another user’s public profileLowAccessing private account informationMedium to HighViewing private invoices or documentsHighModifying another user’s account dataHighUnauthorized access to sensitive financial recordsHigh or Critical, depending on impact

When I evaluate an IDOR, I consider:

- What information can be accessed?
- Can another user’s information be modified?
- Does the issue affect multiple accounts?
- Is authentication required?
- Does the issue expose sensitive personal or financial information?

I also consider the actual business impact instead of assigning severity based only on the endpoint or HTTP response.

### 10. How Developers Can Prevent IDOR

From a security perspective, changing an object ID should never be enough to gain access to another user’s resources.

Developers should implement proper authorization checks on the server side.

Some important recommendations include:

1. **Implement Object-Level Authorization:** Verify that the authenticated user has permission to access the requested object.
2. **Validate Every Request:** Apply authorization checks to GET, POST, PUT, PATCH, and DELETE operations.
3. **Use Server-Side Ownership Checks:** Never rely only on frontend validation or hidden interface elements.
4. **Apply Role-Based Access Control:** Ensure that users can only perform actions allowed by their assigned permissions.
5. **Test APIs Regularly:** Include authorization testing in application security assessments.
6. **Log Suspicious Access Attempts:** Monitor unusual patterns involving repeated access to different object identifiers.

Using UUIDs instead of sequential IDs may make identifiers harder to guess, but it does not fix IDOR. Proper authorization checks are still necessary.

### Final Thoughts

IDOR hunting is not just about changing an ID from one number to another.

It is about understanding how an application handles user resources and whether the backend properly checks ownership and permissions.

During my bug bounty journey, I have found that spending time understanding application functionality is often more valuable than blindly running automated scanners.

I recommend starting with two test accounts, mapping important endpoints, reviewing requests in Burp Suite, and carefully comparing the application’s responses.

Most importantly, always test within the scope of an authorized security program and avoid accessing or modifying real users’ data.

**Remember: Authentication tells an application who you are. Authorization determines what you are allowed to access.**

*AI assistance: I used an AI-powered grammar and spelling checker to review this article. The ideas, research, technical analysis, and final content are my own.*

*Have questions or want to share your own workflow? Drop a comment below or connect with me on :*

🔗Linkdin: [https://www.linkedin.com/company/sam-shield/](https://www.linkedin.com/company/sam-shield/)

🔗Youtube: [https://www.youtube.com/@sam\_shield-w7l](https://www.youtube.com/@sam_shield-w7l)

🔗Medium: [https://medium.com/@samadhanshimple](https://medium.com/@samadhanshimple)
