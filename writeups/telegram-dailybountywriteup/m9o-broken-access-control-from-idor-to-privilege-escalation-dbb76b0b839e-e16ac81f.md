# Broken Access Control

- **Source URL:** https://medium.com/@m9o/broken-access-control-from-idor-to-privilege-escalation-dbb76b0b839e?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@m9o
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 12983)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
بسم الله الرحمن الرحيم…وَقُل رَّبِّ زِدْنِى عِلْمًۭ

### Introduction

Broken Access Control (BAC) is ranked first among all web application vulnerability categories in the [OWASP Top 10](https://owasp.org/Top10/2025/), as every analyzed application was found to contain some form of access control weakness.

**The danger of this vulnerability does not lie in its technical complexity, but in the fact that it represents a failure in the system’s underlying logic.**

This can occur for several reasons, including:

- Inconsistent request interpretation or authorization policy enforcement across different platform layers.
- Hiding sensitive endpoints instead of enforcing proper permission checks, based on the incorrect assumption that obscuring a directory prevents users from accessing it.
- Relying on multi-step workflows where authorization checks are performed only at the final step, under the mistaken belief that users cannot bypass earlier stages.

The root cause, however, is the reliance on untrusted assumptions rather than explicitly validating permissions at the server level.

The impact of exploiting this vulnerability often includes:

- Exposure of sensitive information.
- Modification or deletion of data.
- Execution of business functions beyond the user’s intended privileges.

### Quick Review of Key Concepts

Before diving into the vulnerability itself, it is important to understand a few foundational concepts:

Access control, its types, its core elements, and the distinction between authentication and authorization.

#### Access Control

**Access control refers to the mechanisms and policies that determine whether a subject is permitted to access a specific resource or perform a particular action (read, write, delete, modify, etc.), based on policies enforced at request time.**

The objective is to prevent users from accessing other users’ accounts or data, and to ensure that regular users cannot perform actions reserved for privileged roles such as administrators.

Core Elements of Access Control

1. **Subject**: The entity requesting access or attempting to perform an action (user, process, or service).
2. **Object**: The resource being accessed (file, API endpoint, database record, etc.).
3. **Action**: The operation being requested (read, write, delete, modify, etc.).
4. **Policy**: The set of rules used to determine whether access should be granted or denied.
5. **Policy Enforcement Point (PEP)**: The component responsible for enforcing the authorization decision (application layer, server, database, etc.).

Conceptual Model

### Access Control in the Context of Web Security

In web security, access control relies on three core components:

1. **Authentication**: Verifying the identity of the user.
2. **Session Management**: Associating multiple HTTP requests with the same authenticated user.
3. **Authorization**: Determining whether the user is permitted to perform a specific action.

A very important point:

Do not confuse authentication with authorization.

For example, if you gain access to an admin account through a password leak or session hijacking, this represents a failure of authentication.

However, if a regular user is able to perform administrative functions due to missing or improperly enforced authorization checks, this constitutes Broken Access Control.

### Types of Access Control

#### Vertical Access Control

According to PortSwigger, vertical access control refers to mechanisms that restrict access to sensitive functionality to specific privileged roles.

For example, an administrator may be able to create, modify, or delete records, while a regular user should not have access to those capabilities.

#### Horizontal Access Control

Horizontal access control prevents users from accessing resources that belong to other users at the same privilege level.

For example, a banking application allows users to view transactions and perform operations on their own accounts, but they must not be able to access accounts belonging to other users.

#### Context-Dependent Access Control

Context-dependent access control enforces restrictions based on the state of the application or the user’s workflow.

For example, after completing a purchase on a website like Amazon and finalizing payment, users should not be able to return and modify their shopping cart.

### Broken Access Control

### Vertical Privilege Escalation

#### 1. Hidden or Unprotected Functions

In some applications, developers hide important functionality from the user interface (UI), such as removing the admin page button so it is not visible to regular users. However, the application relies solely on UI restrictions instead of enforcing authorization checks at the controller or middleware level.

Let’s assume the user cannot see the admin page link in the interface. After inspecting the website’s files, they discover the path admin-panel/ and manually enter it into the URL. The application then grants them access to the admin page. This clearly indicates that authorization was not enforced on the server side.

Now consider another scenario where the developer attempts to be more “secure” by making the admin page name unpredictable, for example by adding a random suffix and not exposing the link in the UI. This approach is known as **Security by Obscurity**, and its goal is to prevent attackers from guessing the protected endpoint.

However, this approach is ineffective. An attacker can still discover the endpoint by analyzing JavaScript files, enumerating hidden endpoints, or identifying exposed administrative functionality in the codebase.

The issue is not the URL path itself, but the complete absence of proper authorization enforcement. Security by Obscurity reduces discoverability, but it does not enforce policy. This is the key difference between access control and simply hiding resources.

In this scenario:

- **Subject**: A regular user
- **Action**: Accessing administrative functionality
- **Object**: The admin page
- **Policy**: Access must be restricted to users with the administrator role
- **Point of failure**: Absence of a server-side Policy Enforcement Point (PEP)

Technical Example of the Problem:

**Incorrect Implementation:**

```
@app.route("/admin-panel")  
def admin():  
    return render_admin_dashboard()
```
The issue here is that no role verification is performed.

Now compare this to the **corrected example:**

```
@app.route("/admin-panel")  
@login_required  
@require_role("admin")  
def admin():  
    return render_admin_dashboard()
```
In this implementation, two conditions are enforced:

- @login\_required ensures that the user is authenticated.
- @require\_role("admin") ensures that only users with the administrator role can access this functionality.

In conclusion, this scenario represents **Vertical Privilege Escalation**, as a lower-privileged user was able to execute functionality intended for a higher-privileged role.

### Horizontal Privilege Escalation

This refers to a user’s or attacker’s ability to access resources or data belonging to another user at the same privilege level.

This is still an authorization issue, specifically categorized as a **Failure of Ownership Enforcement**.

### Examples

#### 1. User ID Controlled by a Request Parameter

This scenario occurs when an application receives a request to access an account identified by a specific ID, for example:

/account?userId=3003

If the application allows access to account 3003 without verifying that the requesting user actually owns that account, then proper authorization checks are missing.

A developer might attempt to “improve” security by replacing predictable numeric IDs with something like a UUID. While this makes identifiers harder to guess, it does not solve the core issue. The real problem is the absence of an ownership validation check on the server side, such as:

WHERE id = ? AND user\_id = currentUser

Without enforcing ownership in the query or business logic, the application remains vulnerable.

#### 2. Data Leakage in Redirects

In this case, a user attempts to access a resource that does not belong to them. The application detects the lack of authorization and redirects the user to another page (for example, the homepage).

However, the HTTP response generated before the redirect may still contain sensitive data.

This typically happens because:

- The data is retrieved from the database before verifying ownership, or
- The data is attached to the response object before the redirect decision is made.

The correct approach is to first validate ownership and permissions, and only then proceed with any data retrieval or response construction.

Authorization checks must occur before any sensitive operation is performed.

### Horizontal to Vertical Privilege Escalation

Consider the following scenario:

A penetration tester discovers a userID parameter and modifies its value to access another user's account. This is a classic horizontal privilege escalation.

The tester then decides to try the administrator’s ID. Upon doing so, they successfully gain access to the admin account.

The question is:

Is this horizontal or vertical privilege escalation?

How should it be described in a security report?

The answer:

- **Original vulnerability**: Horizontal Privilege Escalation (IDOR).
- **Resulting impact**: Vertical Privilege Escalation due to compromise of an administrative account.
- **Report description**:
*“IDOR leading to administrative account takeover.”*

### In the end

If you want to truly understand the concept, don’t just rely on theory. Try Broken Access Control scenarios in PortSwigger and analyze each lab: Why did the vulnerability occur? Where was the flaw? How should the verification have been implemented?

Reading Bug Bounty reports on IDOR and Privilege Escalation is also crucial. Analyzing these reports gives you a realistic perspective: how the vulnerability was discovered, how it was exploited, and how it was presented in the report.

*See you soon*
