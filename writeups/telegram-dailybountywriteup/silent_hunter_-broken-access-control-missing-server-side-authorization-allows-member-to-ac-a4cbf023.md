# Broken Access Control Missing Server-Side Authorization Allows Member to Access Billing Data and…

- **Source URL:** https://medium.com/@silent_hunter_/broken-access-control-missing-server-side-authorization-allows-member-to-access-billing-data-and-b75a1569013f
- **Fetched from:** https://medium.com/@silent_hunter_/broken-access-control-missing-server-side-authorization-allows-member-to-access-billing-data-and-b75a1569013f?source=rss-c8d206bcfd66------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14982)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mahmoud_Elkholy / Thu, 12 Nov 2026 17:38:36 GMT

*A Broken Access Control writeup — on hidden administrative features, missing authorization checks, and a Member who was never supposed to manage anyone.*

*“You see, but you do not observe. The distinction is clear.”*

— Sherlock Holmes, *A Scandal in Bohemia* (1891)

The application provides a collaborative workspace where users are assigned one of two roles:

According to the application’s documentation and the behavior observed during testing, Member accounts are not allowed to access the team management functionality.

The application appeared to enforce this restriction correctly. When accessing the relevant section as a Member, the frontend blocked navigation and displayed a permission warning.

However, there was a distinction worth investigating:

**Was the application actually enforcing authorization on the server, or was it merely hiding the functionality from unauthorized users?**

Two accounts were created within a test workspace:

The objective was to determine whether the Member account could perform administrative operations against other workspace members without obtaining actual administrative privileges.

I first logged in using the Member account and attempted to access the team management section.

The application blocked access through its frontend interface :

The Member could not normally view or manage other workspace members.

At this point, the expected authorization boundary appeared clear:

The restriction was working at the interface level. That alone, however, did not establish whether the backend enforced it.

While inspecting the application’s HTTP traffic through Burp Suite, I identified a role-related property in the server response that controlled the administrative interface.

The response contained the following JSON property:

**Original response:**

```
{
  "tea_wRu2**********": "member"
}
```
Instead of treating the hidden interface as an authorization boundary, I examined how the frontend determined which features should be displayed.

By configuring a Burp Suite Match & Replace rule on the response body, I modified the role value locally:

**Modified response:**

```
{
  "tea_wRu2**********": "admin"
}
```
This caused the application to render the previously restricted administrative interface.

An important distinction: The modification affected only the response received by my browser. The actual account remained a Member, and its server-side role was never changed.

The first restriction had been bypassed.

With the modified response, I navigated to:

\[TEAM MANAGEMENT / BILLING & USERS PAGE\]

The application now displayed functionality that had previously been inaccessible to the Member account.

The previously displayed permission warning was no longer preventing access to the interface.

The application also loaded the relevant management functionality, including the team members section.

However, revealing a hidden interface is not, by itself, a security vulnerability.

A properly implemented application should independently validate the authenticated user’s permissions whenever a sensitive backend operation is requested.

The next step was to determine whether that authorization check actually existed.

I used the Member account to edit the Admin’s profile. I successfully changed the Admin’s name and profile picture, and added a new sending email address. All changes were saved successfully and remained after removing the Burp Suite Match & Replace rule and refreshing the page. This confirmed that the changes were actually saved on the server.

and it works

The vulnerability resulted from missing server-side authorization checks on administrative operations.

Although the frontend restricted Members from accessing team management functionality, the backend failed to consistently verify the authenticated user’s actual role before processing sensitive requests.

As a result, a Member could modify the profiles of other workspace users, including Admins, access their available personal information, and modify supported account settings.

The issue allowed a lower-privileged user to perform administrative operations without actually obtaining an Admin role.

The vulnerability was reported and subsequently fixed.

**The Member never had administrative privileges. The server simply failed to enforce them.**

*“I never guess. It is a shocking habit — destructive to the logical faculty.”.*

— Sherlock Holmes, The Sign of the Four (1890), Chapter 1.
