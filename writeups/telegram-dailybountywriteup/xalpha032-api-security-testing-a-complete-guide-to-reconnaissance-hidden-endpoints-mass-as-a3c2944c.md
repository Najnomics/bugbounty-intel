# API Security Testing

- **Source URL:** https://medium.com/@xalpha032/api-security-testing-a-complete-guide-to-reconnaissance-hidden-endpoints-mass-assignment-and-de89b28b2b3c
- **Fetched from:** https://medium.com/@xalpha032/api-security-testing-a-complete-guide-to-reconnaissance-hidden-endpoints-mass-assignment-and-de89b28b2b3c?source=rss-8d87fb21d94c------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14967 (id 14967)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Shadow / Sun, 01 Nov 2026 22:59:51 GMT

APIs are one of the most important components of modern web applications. They connect front-end interfaces with back-end services, handle authentication, process user data, and allow different systems to communicate.

However, APIs also introduce a significant attack surface. An application may appear secure through its graphical interface while exposing undocumented endpoints, accepting unexpected HTTP methods, trusting hidden parameters, or incorrectly processing user-controlled input.

For penetration testers, testing the API directly can reveal vulnerabilities that are difficult or impossible to discover through normal browser interaction.

This article explores API security testing from a penetration testing perspective, covering reconnaissance, endpoint discovery, API documentation, HTTP methods, content types, hidden parameters, mass assignment, Server-Side Parameter Pollution (SSPP), Burp Suite workflows, OWASP API Security, and defensive techniques.

An API (Application Programming Interface) is a mechanism that allows different software components to communicate with each other.

In a typical web application, the browser does not necessarily communicate directly with the database. Instead, it sends HTTP requests to an API, which processes the request and communicates with the back-end infrastructure.

A simplified architecture looks like this:

+----------------------+

| User Browser |

+----------------------+

|

| HTTP Request

v

+----------------------+

| Front-End App |

+----------------------+

|

| API Request

v

+----------------------+

| API Server |

+----------------------+

|

| Database Query

v

+----------------------+

| Database |

+----------------------+

For example, when a user opens their profile, the application might send:

GET /api/users/123 HTTP/1.1

Host: example.com

Authorization: Bearer \<TOKEN>

The API processes the request and returns information about the requested user.

**REST API**

REST (Representational State Transfer) is an architectural style commonly used with HTTP methods and resource-based URLs.

Example:

GET    /api/users

GET /api/users/123

POST /api/users

PATCH /api/users/123

DELETE /api/users/123

**GraphQL API**

GraphQL allows clients to request specific data through a structured query language.

```
query {
    user(id: 123) {
        username
        email
    }
}
```
Unlike traditional REST APIs, GraphQL commonly uses a single endpoint to handle multiple operations.

**SOAP API**

SOAP (Simple Object Access Protocol) is a messaging protocol that commonly uses XML-based messages and structured service definitions.

This article primarily focuses on RESTful and JSON-based APIs, while also discussing structured-data injection and internal API communication.

API reconnaissance is the first stage of API penetration testing.

The objective is to understand how the application communicates with its back-end services and identify as much of the available attack surface as possible.

Before testing vulnerabilities, a penetration tester should identify:

An endpoint is a specific URL where an API receives requests for a particular resource or operation.

For example:

GET /api/books

The endpoint is /api/books.

Another endpoint might be:

GET /api/books/123

This could retrieve a specific book.

During reconnaissance, look for URL patterns such as:

/api/

/api/v1/

/api/v2/

/rest/

/graphql

/users/

/admin/

/internal/

These paths are examples of naming conventions, not guaranteed endpoint locations.

One of the most effective ways to discover API endpoints is to browse the application while Burp Suite intercepts the traffic.

Recommended workflow:

Pay particular attention to:

A front-end application may communicate with several API endpoints without displaying their URLs directly to the user.

JavaScript files can reveal API endpoints that have not been accessed through normal browser navigation.

`fetch("/api/v1/account/details");`
Or:

`axios.get("/api/admin/users");`
These references may reveal additional functionality.

Useful approaches include:

Remember that discovering an endpoint does not automatically mean that it is vulnerable or accessible.

API documentation explains how developers are expected to interact with an API.

It may contain:

Documentation can be human-readable or machine-readable.

Human-readable documentation explains how to use an API through descriptions and examples.

Common documentation paths include:

/api

/docs

/swagger

/swagger-ui

/swagger/index.html

/api-docs

These are common examples worth checking during authorized reconnaissance.

Machine-readable documentation allows tools to process API specifications automatically.

Common formats include:

Example OpenAPI-style JSON:

```
{
  "openapi": "3.0.0",
  "paths": {
    "/api/users": {
      "get": {
        "summary": "Retrieve users"
      },
      "post": {
        "summary": "Create a user"
      }
    }
  }
}
```
This document reveals that /api/users supports GET and POST operations.

When documentation is discovered, compare its information with the actual application behavior.

Look for:

Useful tools include:

ToolPurposeBurp SuiteIntercept and analyze HTTP trafficOpenAPI ParserParse OpenAPI documentationPostmanSend and organize API requestsSoapUITest API servicesBurp RepeaterManually modify requests

An important point: documentation is not always accurate or up to date. Always verify discovered functionality against the actual API.

After discovering endpoints, the next step is to understand how they behave.

A useful testing approach is to send requests through Burp Repeater and observe the application’s responses.

Consider:

GET /api/tasks HTTP/1.1

Host: example.com

The API might return:

```
{
  "tasks": [
    {
      "id": 1,
      "title": "Complete security assessment"
    }
  ]
}
```
Now investigate whether the endpoint supports other operations.

HTTP methods define the intended operation performed on a resource.

MethodTypical PurposeGETRetrieve informationPOSTCreate a resource or perform an operationPUTReplace a resourcePATCHPartially update a resourceDELETEDelete a resourceOPTIONSDiscover communication options, including supported methods

GET /api/tasks

Retrieves tasks.

POST /api/tasks

Content-Type: application/json

```
{
  "title": "New task"
}
```
Creates a task.

PATCH /api/tasks/1

Content-Type: application/json

```
{
  "title": "Updated task"
}
```
Updates part of an existing task.

DELETE /api/tasks/1

Deletes a task.

An API endpoint may support multiple methods, even if the front-end only uses one.

During authorized testing:

The OPTIONS method may also provide information about supported methods:

OPTIONS /api/tasks HTTP/1.1

Host: example.com

A response might contain:

Allow: GET, POST, OPTIONS

This is useful reconnaissance information, although the Allow header is not always a complete or reliable representation of the server's actual behavior.

**Important:** Test state-changing methods only against authorized test resources. Use low-impact objects to avoid unintended modifications or deletions.

An API may accept different request formats.

Common content types include:

**JSON**

Content-Type: application/json

```
{
  "username": "testuser",
  "email": "test@example.com"
}
```
**URL-Encoded Form Data**

Content-Type: application/x-www-form-urlencoded

username=testuser&email=test%40example.com

**Multipart Form Data**

Content-Type: multipart/form-data; boundary=----Boundary123

Commonly used for forms containing file uploads.

**XML**

Content-Type: application/xml

\<user>

\<username>testuser\</username>

\<email>test@example.com\</email>

\</user>

Different content types can be processed by different parsers and application components.

This may introduce inconsistent security behavior.

A tester should determine which formats are actually supported and whether validation is consistent across them.

In Burp Suite, modify the Content-Type header and ensure that the body matches the selected format.

Burp’s Content Type Converter extension can help convert request bodies between supported formats.

Not every API endpoint is linked from the application’s front-end.

Some endpoints may exist for administrative operations, internal features, legacy functionality, or mobile applications.

For example, you might discover:

PUT /api/user/update

However, other operations could exist under similar naming conventions.

Potential naming patterns include:

/api/user/update

/api/user/delete

/api/user/create

/api/user/export

/api/user/search

These are illustrative examples.

Burp Intruder can automate endpoint discovery by replacing a selected part of a request with values from a wordlist.

A basic workflow:

For example, the request:

can be used as a starting point for discovering related operations.

Pay attention to differences such as:

ResponsePossible Meaning200 OKRequest processed successfully201 CreatedResource created204 No ContentSuccessful operation without response body400 Bad RequestInvalid request401 UnauthorizedAuthentication required or invalid403 ForbiddenAccess denied404 Not FoundResource or route not found405 Method Not AllowedHTTP method unsupported

These responses are clues, not definitive vulnerability indicators.

A 403 response does not prove that an endpoint is secure, and a 404 response does not always prove that a route does not exist.

An API may accept parameters that are not documented or displayed in the front-end.

These parameters may influence application behavior.

GET /api/users?id=123

The application visibly uses only the id parameter.

However, additional parameters might be supported internally.

Potential examples include:

role

isAdmin

status

debug

email

access\_level

These are examples of parameter names, not evidence that a particular application supports them.

Burp Intruder can help discover undocumented parameters by testing candidate parameter names.

GET /api/users?id=123&§parameter§=test

A wordlist is inserted into the selected position.

Compare responses to identify parameters that influence application behavior.

Param Miner is a Burp Suite extension designed to discover hidden parameters and headers.

It can automatically guess parameter names using information gathered from the application.

It is especially useful when manually testing a large number of potential parameters would be inefficient.

Burp’s Content Discovery functionality can help identify resources that are not directly linked from the application’s visible pages.

This can reveal additional paths and functionality that should be included in the API attack surface assessment.

Mass Assignment is a vulnerability that occurs when an application automatically binds user-supplied request parameters to internal objects without properly restricting which properties users are allowed to modify.

It is also known as:

Consider an application that allows users to update their profiles.

The front-end sends:

PATCH /api/users/123 HTTP/1.1

Host: example.com

Content-Type: application/json

```
{
  "username": "wiener",
  "email": "wiener@example.com"
}
```
The server processes these properties and updates the corresponding user object.

Internally, the user object may contain additional properties:

```
{
  "id": 123,
  "username": "wiener",
  "email": "wiener@example.com",
  "isAdmin": false,
  "accountStatus": "active"
}
```
The problem occurs when the application automatically binds every submitted property to the internal object.

Instead of allowing only username and email, it might also accept properties such as isAdmin.

A tester can compare the properties returned by a GET request with the properties accepted by a legitimate update operation.

**GET request:**

GET /api/users/123

Response:

```
{
  "id": 123,
  "username": "wiener",
  "email": "wiener@example.com",
  "isAdmin": false
}
```
**Normal PATCH request:**

The response reveals that the user object contains an isAdmin property, even though the normal update interface does not expose it.

This creates a testing hypothesis: perhaps the API accepts properties that the front-end does not allow users to modify.

In an authorized lab, a tester can compare how the application handles an additional property.

```
{
  "username": "wiener",
  "email": "wiener@example.com",
  "isAdmin": "invalid"
}
```
Then compare it with a valid Boolean value:

```
{
  "username": "wiener",
  "email": "wiener@example.com",
  "isAdmin": true
}
```
Observe:

A different response to an invalid value can provide evidence that the property is being processed.

However, response differences alone do not confirm exploitation. The actual server-side state and authorization behavior must be verified.

Successful mass assignment can result in:

The impact depends on which internal properties are exposed and how the application uses them.

Developers should:

A secure update operation should explicitly select permitted properties instead of accepting arbitrary fields.

Server-Side Parameter Pollution occurs when an application inserts user-controlled input into a server-side request without correctly encoding or validating it.

This is particularly important when an application communicates with internal APIs.

Consider the following architecture:

+----------------------+

| User Browser |

+----------------------+

|

| User Request

v

+----------------------+

| Public Website |

+----------------------+

|

| Internal API Request

v

+----------------------+

| Internal API |

+----------------------+

|

v

+----------------------+

| Database |

+----------------------+

The user cannot directly access the internal API.

However, the public website sends requests to that API on the user’s behalf.

If user input is inserted into those requests without proper encoding, the user may be able to manipulate the resulting request.

Potential impacts include:

Consider a public endpoint:

GET /userSearch?name=peter&back=/home

The application internally constructs:

GET /users/search?name=peter&publicProfile=true

The important detail is that the public application is generating a second request.

If the name parameter is not encoded correctly, special query characters may affect the internal request.

A URL-encoded # character can potentially cause the remainder of an internal URL to be interpreted as a fragment.

For example, in an authorized test:

GET /userSearch?name=peter%23foo&back=/home

The application may construct:

GET /users/search?name=peter#foo&publicProfile=true

In URL processing, the fragment begins at # and is not normally sent as part of an HTTP request target.

This could effectively remove the remaining query string from the internal request.

The result may change how the internal API processes the request.

**Important:** The # must be URL-encoded in the original request so that the browser or HTTP client does not interpret it as a client-side fragment before sending it.

An encoded ampersand may introduce another parameter into a poorly constructed internal query string.

GET /userSearch?name=peter%26foo=xyz&back=/home

The internal application might generate:

GET /users/search?name=peter&foo=xyz&publicProfile=true

If the internal API ignores the unknown parameter, the response may remain unchanged.

This does not necessarily mean the injection failed. It may simply indicate that the parameter has no effect.

If a tester identifies a parameter that the internal API recognizes, it may be possible to influence its behavior.

For example, suppose the internal API accepts an email parameter.

A test request could introduce that parameter through user-controlled input:

GET /userSearch?name=peter%26email=test&back=/home

The resulting internal request could resemble:

GET /users/search?name=peter&email=test&publicProfile=true

The response should be compared with a normal request to determine whether the additional parameter is being processed.

One important SSPP test is determining how an internal API handles duplicate parameters.

GET /userSearch?name=peter%26name=carlos&back=/home

The internal request may become:

GET /users/search?name=peter&name=carlos&publicProfile=true

Different technologies may process duplicate parameters differently.

Technology / Parser BehaviorPossible ResultPHPCommonly uses the last scalar valueNode.js / ExpressCommonly uses the first scalar valueASP.NETMay combine repeated values

Actual behavior depends on the framework, parser configuration, and application code.

This difference is important because the public application and internal API may interpret duplicate parameters differently.

SSPP is not limited to query strings.

Some APIs place resource identifiers directly inside URL paths.

/api/users/123

The URL can be interpreted as:

/api       -> API root

/users -> Resource

/123 -> Resource identifier

Consider a public request:

GET /edit\_profile.php?name=peter

The application internally generates:

GET /api/private/users/peter

If the input is not correctly encoded, path manipulation may affect the internal resource path.

GET /edit\_profile.php?name=peter%2f..%2fadmin

The internal request may resemble:

/api/private/users/peter/../admin

If the server normalizes the path, it could resolve to a different resource.

This demonstrates why server-side URL construction must use proper encoding and strict validation.

SSPP can also affect structured formats such as JSON and XML.

Consider a public application that allows users to update their names.

The browser sends:

POST /myaccount

Content-Type: application/x-www-form-urlencoded

name=peter

The server internally creates:

PATCH /users/7312/update

Content-Type: application/json

```
{
  "name": "peter"
}
```
If the server inserts user input directly into the JSON string instead of using a proper JSON serializer, special characters may alter the resulting structure.

The security problem is not JSON itself. It is unsafe construction of structured data using untrusted strings.

The same principle applies when JSON data is built from user-controlled input.

**Key distinction:** Properly parsing and serializing JSON is fundamentally different from concatenating raw strings to construct JSON documents.

Burp Suite can assist with identifying suspicious input transformations.

Automated findings should always be manually verified.

A suspicious transformation does not automatically establish a vulnerability.

A structured workflow makes API testing more effective and helps prevent missed functionality.

Objective: Understand the application and discover its API attack surface.

Activities:

Objective: Discover additional API functionality.

Objective: Determine which operations each endpoint supports.

Objective: Understand how the API processes different request formats.

Objective: Identify undocumented parameters and sensitive object properties.

Objective: Verify that API operations enforce the correct permissions.

Objective: Determine whether untrusted input can influence server-side processing.

Objective: Confirm findings and document their security impact.

For every finding, record:

The OWASP API Security Top 10 identifies major security risks affecting APIs.

Understanding these categories helps penetration testers build a broader testing methodology.

IDVulnerabilityDescriptionAPI1Broken Object Level Authorization (BOLA)Users can access objects they are not authorized to access.API2Broken AuthenticationAuthentication mechanisms can be bypassed or abused.API3Broken Object Property Level AuthorizationUnauthorized access to or modification of sensitive object properties.API4Unrestricted Resource ConsumptionAPIs lack sufficient controls over resource usage.API5Broken Function Level AuthorizationUsers can access functions beyond their permissions.API6Unrestricted Access to Sensitive Business FlowsSensitive business operations lack adequate protection.API7Server-Side Request Forgery (SSRF)Server-side requests can be manipulated to reach unintended destinations.API8Security MisconfigurationInsecure configurations expose the API to attacks.API9Improper Inventory ManagementOld, undocumented, or forgotten API versions remain exposed.API10Unsafe Consumption of APIsApplications do not safely validate or process responses from external APIs.

API reconnaissance helps identify undocumented versions and endpoints.

Authorization testing helps discover BOLA and BFLA vulnerabilities.

Mass assignment testing is particularly relevant to object property authorization.

Resource and rate-limit testing helps assess unrestricted resource consumption.

SSRF testing examines whether APIs can be abused to make unintended server-side requests.

This demonstrates that API security testing is not limited to finding hidden endpoints. It requires understanding the complete security model of the application.

API security should be implemented at the application and infrastructure levels.

The following checklist can be used during an authorized web application penetration test.

**Reconnaissance**

**Endpoint Testing**

**Parameter Testing**

**Authorization**

**Server-Side Parameter Pollution**

**Reporting**

API security testing is an essential part of modern web application penetration testing.

A web application may expose only a small portion of its functionality through the front-end, while its API provides additional operations, parameters, and resources that require independent security assessment.

Understanding API architecture, performing effective reconnaissance, identifying hidden endpoints, testing HTTP methods, examining content types, and discovering undocumented parameters can reveal weaknesses that ordinary browser testing may overlook.

Mass assignment demonstrates the risks of automatically binding user input to internal objects, while Server-Side Parameter Pollution highlights the dangers of constructing internal requests from untrusted data.

Most importantly, successful API testing requires more than sending unusual requests. It requires understanding how the application processes input, enforces authorization, communicates with internal services, and protects sensitive operations.

**The key principle is simple: never assume that an API is secure just because its front-end interface appears restricted. Every exposed endpoint, method, parameter, and object property should be evaluated within the application’s intended security model.**

*Disclaimer: This article is intended for educational purposes and authorized security testing. Only assess systems for which you have explicit permission.*
