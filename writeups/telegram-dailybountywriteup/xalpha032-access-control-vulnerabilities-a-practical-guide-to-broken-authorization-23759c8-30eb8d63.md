# Access Control Vulnerabilities

- **Source URL:** https://medium.com/@xalpha032/access-control-vulnerabilities-a-practical-guide-to-broken-authorization-23759c8d879b
- **Fetched from:** https://medium.com/@xalpha032/access-control-vulnerabilities-a-practical-guide-to-broken-authorization-23759c8d879b?source=rss-8d87fb21d94c------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14964 (id 14964)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Shadow / Thu, 29 Oct 2026 23:56:35 GMT

*Understanding vertical and horizontal privilege escalation, IDOR, and common access control weaknesses through PortSwigger Web Security Academy.*

Access control is one of the most important security mechanisms in modern web applications. It determines what authenticated users are allowed to access and which actions they can perform.

However, authentication does not automatically mean authorization. A user may successfully log in to an application while still attempting to access resources or functionality they are not permitted to use.

When an application fails to enforce these restrictions correctly, it can introduce **Broken Access Control** vulnerabilities.

Depending on the application and the permissions involved, these vulnerabilities may expose sensitive information, allow unauthorized modifications, or enable privilege escalation.

In this article, we will explore the fundamental concepts of access control, common vulnerability patterns, testing methodologies, and recommended security practices.

Before exploring access control vulnerabilities, it is important to understand three related concepts.

For example, logging in successfully proves that a user has authenticated. It does not mean that the user is authorized to access an administrator’s dashboard.

A secure application must verify permissions whenever a user attempts to access a protected resource or perform a sensitive operation.

Vertical access control restricts functionality according to privilege levels or user roles.

For example, an administrator may be allowed to manage user accounts, while a regular user can only manage their own profile.

**Vertical privilege escalation** occurs when a user gains access to functionality intended for a more privileged role.

Horizontal access control restricts access to resources belonging to individual users.

For example, a customer should be able to view their own orders but should not be able to access another customer’s private order history.

**Horizontal privilege escalation** occurs when a user accesses another user’s resources without obtaining a higher privilege level.

Some applications restrict actions according to the current state of a workflow.

For example, an application may allow a customer to modify an order before confirmation but prevent changes after the order has been finalized.

A vulnerability occurs when an application fails to enforce these restrictions consistently.

Administrative pages are often designed to be accessible only to privileged users.

Consider an endpoint such as:

If the application does not verify the current user’s permissions, an ordinary user might access administrative functionality simply by requesting the endpoint directly.

Removing an administrative link from the user interface does not prevent direct access to the underlying resource.

The server must independently enforce the appropriate permissions.

Some applications attempt to protect administrative functionality by using difficult-to-guess URLs.

For example:

[https://example.com/administrator-panel-x7k29](https://example.com/administrator-panel-x7k29)

Although an obscure URL may make discovery more difficult, it does not provide reliable authorization.

If the URL becomes known, the application must still prevent unauthorized users from accessing the resource.

**Key takeaway:** Hiding functionality is not the same as securing it.

Applications sometimes use request parameters or cookies to represent user roles and permissions.

GET /account?role=user

A poorly designed application may trust client-controlled information when deciding whether to grant access to privileged functionality.

If the server relies on such values without verifying the user’s actual permissions, the authorization mechanism may be bypassed.

Similar weaknesses can involve cookies, hidden form fields, and JSON request properties.

The fundamental problem is trusting information supplied by the client instead of enforcing authorization using trusted server-side data.

An Insecure Direct Object Reference occurs when an application uses a user-controlled identifier to retrieve an object without correctly checking whether the current user is authorized to access it.

Consider this request:

GET /account?id=1001

The application uses the identifier to select an account.

If it checks only whether the account exists, rather than whether the current user is allowed to access it, private information may be exposed.

IDOR vulnerabilities can affect user profiles, invoices, documents, private messages, orders, and API resources.

The identifier does not have to be numeric. UUIDs and other identifiers can also be involved.

**The essential issue is missing authorization, not the predictability of the identifier.**

These two vulnerability classes describe different authorization failures.

Horizontal escalation occurs when a user accesses resources belonging to another user at the same privilege level.

Vertical escalation occurs when a user obtains access to functionality associated with a higher privilege level.

In some cases, a horizontal access control flaw can expose information that contributes to a more serious privilege escalation.

Web applications may use reverse proxies, web servers, and application frameworks to process requests.

If these components interpret a URL differently, access restrictions may not be applied consistently.

Some environments recognize headers such as X-Original-URL or X-Rewrite-URL. When routing and authorization logic disagree about the effective request path, protected resources may become accessible.

The underlying problem is inconsistent request interpretation between application components.

Applications support different HTTP methods, including GET, POST, PUT, PATCH, and DELETE.

A poorly implemented authorization mechanism may restrict an operation when one method is used but fail to enforce the same restriction for another accepted method.

Authorization should apply to the underlying action, regardless of the HTTP method used to invoke it.

The HTTP Referer header can indicate the page from which a request originated.

However, this header can be manipulated by a client and should not be treated as proof of authorization.

If an application grants access to a sensitive operation based only on the presence of a particular Referer value, the restriction may be bypassed.

Authorization decisions must rely on trusted identity and permission checks.

Some sensitive operations require several steps.

An application may verify permissions during the first step but fail to repeat the necessary checks during a later step.

If the final operation can be reached independently, the workflow may allow unauthorized actions.

Every sensitive server-side operation must enforce its own authorization requirements.

Burp Suite is useful for examining HTTP requests and evaluating how an application enforces permissions.

Identify important pages, API endpoints, user roles, and sensitive operations.

Determine which actions should be available to regular users and which should be restricted to administrators.

Use Burp Suite Proxy and HTTP history to examine requests and responses.

Pay attention to:

These components help reveal how the application identifies resources and processes actions.

Where authorized test accounts are available, compare the behavior of users with different privilege levels.

Check whether the server correctly enforces the expected restrictions rather than relying on the user interface.

Review requests that retrieve or modify user-specific resources.

Determine whether the server verifies that the current user owns the requested object or has another explicit permission to access it.

Examine multi-step operations and verify that authorization checks are consistently enforced throughout the workflow.

Also consider whether supported HTTP methods and alternate application routes apply the same security restrictions.

A suspected issue should be validated using a controlled test account and an authorized, harmless test.

Record the affected endpoint, expected behavior, actual behavior, and demonstrated impact.

A successful HTTP response alone does not prove a vulnerability. The evidence must demonstrate that an unauthorized resource or operation was actually accessible.

The impact of a broken access control vulnerability depends on the permissions involved and the sensitivity of the affected resources.

Potential consequences include:

Not every access control issue has the same severity. Risk should be evaluated according to the demonstrated impact and realistic exploitability.

Every sensitive request must be checked against the authenticated user’s permissions before the requested operation is performed.

Access should be denied unless the application explicitly determines that the request is authorized.

When users request individual records, verify that they own those records or have an appropriate permission to access them.

Do not treat query parameters, hidden fields, or editable cookies as authoritative proof of a user’s privileges.

Use consistent authorization mechanisms across application endpoints to reduce the risk of individual routes implementing weaker checks.

Enforce authorization for API endpoints, administrative actions, and every relevant stage of multi-step workflows.

Perform regular security testing with accounts representing different privilege levels. Verify both allowed and denied operations.

Log appropriate authorization failures and sensitive administrative actions without unnecessarily recording secrets or session tokens.

Working through access control concepts highlights several important principles:

Broken access control is a significant web application security risk because it allows users to perform actions or access resources beyond their intended permissions.

Understanding vertical and horizontal privilege escalation, IDOR, URL-based restrictions, and workflow weaknesses provides a strong foundation for identifying these vulnerabilities.

Using Burp Suite to inspect requests, compare user roles, and validate authorization decisions can help security testers assess whether an application enforces its intended security boundaries.

Ultimately, effective access control depends on consistent server-side authorization, explicit permission checks, and systematic testing.
