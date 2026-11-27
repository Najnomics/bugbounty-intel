# Bug Bounty Findings

- **Source URL:** https://medium.com/@maakthon/bug-bounty-findings-10-major-vulnerabilities-exposed-in-cloverleafs-application-bac-in-graphql-0ae1ee0eb4d5?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@maakthon
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 8212)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Welcome to the third part of my **5-part series** exploring vulnerabilities in a web application. In our previous articles, we discussed **Open Redirect** and **IDOR (Insecure Direct Object References)** vulnerabilities. In this installment, we delve into **Broken Access Control (BAC)** within the application’s API, specifically through **GraphQL**.

Broken Access Control remains one of the most critical security issues in modern applications. When implemented incorrectly, access control flaws allow unauthorized users to access, modify, or delete resources they should not have permission to handle. In this article, we will analyze **two scenarios** of Broken Access Control in Target’s GraphQL implementation.

#### Vulnerability Findings:

**Vulnerability 3 : Broken access control in GraphQL**

**What is Broken Access Control in GraphQL?**

**Broken Access Control** occurs when an application fails to enforce proper permission checks on user actions. In a GraphQL API, this can happen due to:

- Missing or improper validation of user input.
- Lack of backend checks to validate authorization for sensitive operations.

**GraphQL**, by design, allows flexible queries and mutations, which can sometimes expose unintended functionalities if proper access control mechanisms are not enforced.

***Case 1:* Unauthorized Subdomain Changes in GraphQL**

In Target, administrators have the ability to create organizations. When a new organization is created, the application generates a subdomain for it, such as:

https://newsubdomain.target.me

The subdomain is tied to the organization and cannot be modified via the frontend. However, I discovered that by tampering with a GraphQL request, it was possible to bypass this restriction and change the subdomain alias.

***How Was It Identified:***

- **Navigating to Organization Settings by access *Admin settings***:

The admin user accesses the organization settings page:

https://newsubdomain.target.me/organization/123/settings/configuration/general

On this page, there is a section called **Organization Information** with two options:

- **Organization Name** (editable)
- **Organization Alias** (non-editable)

When the admin user attempts to change the **Organization Name** (from **newsubdomain** to **newsub1**), the application sends a **GraphQL** request to the backend. This request is responsible for updating the organization’s details.

"operationName": "UpdateOrganization",

"variables": {

"input": {

"id": "123",

"name": "new\_name"

}

},

"query": "mutation UpdateOrganization($input: UpdateOrganizationInput!) {\n updateOrganization(input: $input) {\n organization {\n id\n alias\n name\n \_\_typename\n }\n \_\_typename\n }\n}"

}

The input object here only contains the **id** and **name** parameters, as expected.

**Tampering with the Payload**:

By adding an additional **alias** parameter to the input object, the subdomain can be manipulated. For example:

```
{
  "operationName": "UpdateOrganization",
  "variables": {
    "input": {
      "id": "123",
      "name": "new_name1",
      "alias": "newsub1"
    }
  },
  "query": "mutation UpdateOrganization($input: UpdateOrganizationInput!) {\n  updateOrganization(input: $input) {\n    organization {\n      id\n      alias\n      name\n      __typename\n    }\n    __typename\n  }\n}"
```
This request successfully updates the organization’s subdomain from **newsubdomain.target.me** to **newsub1.target.me.**

***Case 2: Exposure of Private GraphQL Fields***

***How Was It Identified:***

When visiting a user profile in Target, such as:

https://app.target.me/p/adam

The public interface only displays limited information about the user, such as their **full name** and **title**. However, I discovered a vulnerability that allows an attacker to retrieve sensitive private information, including:

- Phone number
- Private email addresses
- City and country
- Organization and teams the user belongs to

This vulnerability was identified by analyzing the GraphQL requests sent when clicking the “**Add to Network**” button (similar to a friend request). One of the **GraphQL** operations sent during this action is:

This query has two objects:

1. **currentUser**: Represents the currently authenticated user.
2. **user**: Represents the target user whose profile is being accessed.

The **user** object accepts a **UserId** parameter to verify the existence of the target user. However, the backend does not limit the scope of data returned, allowing additional sensitive fields to be appended and retrieved.

By manually appending sensitive fields such as email, phone, city, and country to the query, an attacker can retrieve private data about any user, regardless of their privacy settings.

***Conclusion***

The two cases discussed in this article highlight critical vulnerabilities stemming from **Broken Access Control** in Target’s GraphQL API. In **Case 1**, the ability to manipulate subdomain aliases through unauthorized GraphQL mutations demonstrated the risks of inadequate backend validation. This flaw could lead to domain spoofing and reputational damage. In **Case 2**, the exposure of private user fields revealed the consequences of insufficient field-level access control, risking privacy violations and potential social engineering attacks.

***References:***

[Bug Bounty Insights: 10 Key Findings — Open Redirect — Part 1](https://medium.com/@maakthon/bug-bounty-findings-10-major-vulnerabilities-exposed-in-cloverleafs-web-application-part-1-95f659ff7d0a)

[Bug Bounty Insights: 10 Key Findings — IDOR — Part 2](https://medium.com/@maakthon/bug-bounty-findings-10-major-vulnerabilities-exposed-in-cloverleafs-application-idor-part-2-932746b6b445)

Tools used: [Burp Suite Community Edition](https://portswigger.net/burp/communitydownload)

LinkedIn : [https://www.linkedin.com/in/abdalkarim](https://www.linkedin.com/in/abdalkarim/)
