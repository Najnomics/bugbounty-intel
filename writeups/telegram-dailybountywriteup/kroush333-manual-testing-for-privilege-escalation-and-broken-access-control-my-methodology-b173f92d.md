# Manual Testing for Privilege Escalation and Broken Access Control My (Methodology)

- **Source URL:** https://medium.com/@kroush333/manual-testing-for-privilege-escalation-and-broken-access-control-my-methodology-a3b9f41b82a2?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250427213605/https://medium.com/@kroush333/manual-testing-for-privilege-escalation-and-broken-access-control-my-methodology-a3b9f41b82a2
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9481 (id 9481)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Manual Testing for Privilege Escalation and Broken Access Control My (Methodology)

بسم الله، والصلاة والسلام على رسول الله

الحمد لله الذي عَلَّمَ بالقلم.. عَلَّمَ الإنسانَ ما لم يَعْلَم والصلاةُ والسلامُ على خيرِ مُعَلِّمي الناسِ الخير محمد

# ***Who am I***

I’m **Mahmoud Kroush**, a third-year student at the Faculty of Engineering. I’m aiming to become a penetration tester and currently work part-time as a bug bounty hunter.

# Introduction:

In this write-up, I will walk you through my methodology for investigating websites, focusing on how I identify vulnerabilities, particularly in the areas of privilege escalation and broken access control (BAC). In this write-up, I will mention only manual testing — no tools, no scripting — just Burp Suite and Notion to take notes

# **Brief About the Target:**

I worked on a Vulnerability Disclosure Program (VDP) target on HackerOne. For this example, we’ll use the domain **freeplastain.com**. The platform’s core functionality is that when an email is created, it automatically generates an organization. This organization is responsible for managing projects, with varying privilege levels assigned to both the organization and the projects.

**Privilege Levels:**

- **Privilege Levels Organization:**
- **Organization User**: Regular user with limited access.
- **Contracts Manager**: Responsible for approving and creating contracts.
- **Projects Admin**: Can create and manage projects, including project details.
- **Organization Admin**: Manages the overall organization, including user roles and permissions.

These roles can be combined, granting different privilege combinations across the organization and projects.

**Project Privilege Levels:**

- **Member**: Standard user with basic access to the project.
- **Assessor**: Can review project details and provide feedback.
- **Manager**: Responsible for overseeing the project, including managing resources and tasks.
- **Admin**: Has full control over the project, including configuration and user management ( add , remove …etc ).

# Frist Step:

Begin by exploring the website thoroughly. Go through each feature and functionality one by one, observing how each part works. As you explore, make sure to document the following:

- **Permissions Check**: For each function, note who has the ability to perform specific actions (e.g., creating projects, approving contracts, managing users) and who does not have access.
- **Notion Documentation**: Record your findings in Notion, keeping track of which roles have permission for each function, ensuring clarity and organization for further analysis.

**Organization:**

Project:

# Second Step:

- **Launch Burp Suite**: Start by running Burp Suite to intercept and analyze the traffic between the browser and the web application.
- **Collect Tokens**: Log in with users of different privilege levels (e.g., Organization User, Projects Admin, Organization Admin) and collect their session tokens. Ensure you capture the tokens for each role to observe how the application handles authorization for different users.
- **Document Token Details**: Keep a record of each token , noting the user roles and the corresponding tokens. This will be essential when you analyze requests and look for privilege escalation opportunities

# Find Bug:

- As I go through each endpoint, I test different privilege levels to identify potential vulnerabilities like Broken Access Control (BAC), Insecure Direct Object References (IDOR), and privilege escalation issues.
- While testing, I identify an endpoint responsible for adding, removing, and modifying project privileges.

**Test Scenario**:

1- I attempt to reduce the privilege of a user by using a **Member privilege** token. However, the response I receive indicates that I am not authorized to perform this action, confirming that the system enforces access control to some extent at this point.

2- In the request body, users are identified by a JSON object.

For example:

3-I then attempted to delete the entire user object from the request body.

Surprisingly, the server responded with a `200 OK` status, indicating the deletion was successful, even though this action was not expected.

And when i try to login by using the deleted user Find that he not able to access the project

Using the same request, I went back to Burp Suite’s Repeater and sent the request again. the user was re-added to the project.

Ok let’s go I find bug , After successfully manipulating the user deletion and re-adding process, I decided to escalate my privileges further. I focused on the **permissions array** in the request body.

Where I tried to delete permissions but couldn’t, I forgot to try to add it. Ok, let’s try it. I copied the permission array of the Admin, edited mine, and guess what? Yes, I became Admin.

**User 4 Befor :**

**User 4 After :**

Let’s goooooooooooooo! It worked! I went and reported it,

but after two or three days, it was marked as duplicated. This was disappointing =\<

🤍اتمني تكون استفدت باي حاجه و ان شاء الله يكون في احسن الفتره الجايه 

😂🤍متنساش تدعي لو اخواتنا في غزه و ادعيلي انا كمان اطلع من الدبلكيت بقا
