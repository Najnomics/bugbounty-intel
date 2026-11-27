# Admin Account Takeover in Netflix Dispatch Project

- **Source URL:** https://ltsirkov.medium.com/0-click-admin-account-takeover-in-netflix-dispatch-project-feec37326004?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250801000836/https://ltsirkov.medium.com/0-click-admin-account-takeover-in-netflix-dispatch-project-feec37326004
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8912 (id 8912)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Admin Account Takeover in Netflix Dispatch Project

# Introduction

After taking a long break from Netflix bug bounty program, I decided to give it another try — this time collaborating with my friend

We discovered an interesting vulnerability in Netflix Dispatch Project that allowed us to takeover any account including Administrators without any user interaction. This was possible only when the default “**Basic**” authentication provider was used.

We would like to thank Netflix for allowing us to publish this report. **This vulnerability has been patched and the fix is rolled out.**

# Scope & Application

The scope of the program is wide so our first challenge was to decide what type of testing we would like to focus on. We had two options:

- Focusing on a heavy recon
- Deeply understand a single application and learn everything about it

In the meantime, I noticed that there was an ongoing group of researchers testing on Netflix organised by [nahamsec](https://x.com/NahamSec/status/1884564649829425360). There were amazing hackers out there already doing the heavy recon.

After spending some time thinking about it, we eventually decided to choose the second approach and focus on the open-source project named “D**ispatch”**.

**Netflix Dispatch Project Description:** https://netflix.github.io/dispatch/

*All of the ad-hoc things you’re doing to manage incidents today, done for you, and a bunch of other things you should’ve been doing, but have not had the time!*

*Dispatch helps us effectively manage security incidents by deeply integrating with existing tools used throughout an organization (Slack, GSuite, Jira, etc.,)*


The reason for choosing that target was its interesting functionality as it can be seen in the documentation: [https://netflix.github.io/dispatch/docs/administration.](https://netflix.github.io/dispatch/docs/administration.)

Additionally, we did research and discovered that this project already had several interesting vulnerabilities reported. This information is available in the security bulletin:

- **August 1, 2024 Server-Side Template Injection in Dispatch Message Templates**
- **August 17, 2023 Secret Key used for signing JWT tokens exposure in Dispatch**
- **November 6, 2020, Multiple Access Control Issues in Dispatch**
- **November 6, 2020, Multiple XSS Vulnerabilities in Dispatch**

By looking at the program guidelines again we saw that there is a specific limitation regarding Dispatch Project and its configuration.

Interestingly, the official documentation strongly recommends using Docker for installing that project, however, **there was a lack of documentation for installing it from scratch.**

Eventually, we found ourselves in the situation that:

- We must not use Docker to configure Dispatch(Hackerone)
- Official documentation strongly recommends using Docker
- There was no detailed documentation on how to install Dispatch without Docker
- The Docker-Dispatch project uses the main Dispatch project to set it up.

Challenge accepted.

In that case, what we did was to replicate steps from the “**docker-compose.yml**” of the out-of-scoped dispatch-docker and build it from scratch.

This step was necessary as we wanted our future reports to have detailed steps on how to install it from scratch. Otherwise, triagers **might mark our reports as Out of Scope.**

# Setup Debug Tools

At this stage, we already had the project running locally. In such cases, it’s useful to have all the queries monitored to the databases as well as enabling debug mode so that we can get better comprehension of the application.

In that specific case, we used **pgAudit(PostgreSQL)** to monitor the queries in real-time.

Additionally, there was a debug mode of the application which increased the verbosity of the errors.

# Authentication Provider Setup

We had everything configured. The next step was to choose an authentication provider and review all features and work on these that might have some interesting weaknesses.

Dispatch has two authentication providers:

As stated in their documentation, the default authentication provider is “**Basic**” which allows self-registration.

How it works is that you create an account on the application and you are assigned with the lowest privileged role “**Member**”. It was a good starting point for us.

Equipped with all the necessary tools, we created an account and began exploring the application.

## Discovery of the Account Takeover

It took us some time before we came across an interesting behaviour in the role-based access control.

Dispatch uses role-based access control (RBAC) for its UI. According to the documentation, this is only used to protect sensitive incidents whose visibility is set to restricted.

However, we confirmed that administrators have also access to secrets configured in the plugin section for all integrations.

So, if you are assigned with least-privileged role “Member” — you must not see private incidents or configuration of external integrations which might include secrets.

It’s important to note that all users in Dispatch have access to the member list of each organization. Only those assigned with the “Owner” role can edit other users.

We confirmed that by trying **to edit the role of other users as a low-privileged user — Member**. The following error was returned: “**You don’t have permissions to update the user’s role. Please, contact the organization’s owner.**”.

However, if you simply open the “**Edit**” page of any user including Administrators and just press “Save” **without changing any field**, you will be prompted with “**User updated successfully**”.

This message was a sign that something interesting was happening behind the scenes. After a few more attempts and observations, the database query from “**pgAudit**” confirmed that.

It was obvious that there was an executed “**UPDATE**” query that affected the password field when the “**Save**” button was pressed.

With that information we decided to take a look at the source code and we noticed a very interesting behaviour:

**Vulnerable Code:** [https://github.com/Netflix/dispatch/blob/699fd28a06eebe803f43fe449857b62d8b51554b/src/dispatch/auth/views.py#L178](https://github.com/Netflix/dispatch/blob/699fd28a06eebe803f43fe449857b62d8b51554b/src/dispatch/auth/views.py#L178)

```
    if user_in.role:
        # New user role is provided
        user_organization_role = user.get_organization_role(organization)
        if user_organization_role != user_in.role:
            # New user role provided is different than current user role
            current_user_organization_role = current_user.get_organization_role(organization)
            if current_user_organization_role != UserRoles.owner:
                # We don't allow the role change if user requesting the change does not have owner role
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=[
                        {
                            "msg": "You don't have permissions to update the user's role. Please, contact the organization's owner."
                        }
                    ],
                )
    # add organization information
    user_in.organizations = [
        UserOrganization(role=user_in.role, organization=OrganizationRead(name=organization))
    ]
    # we currently only allow user password changes via CLI, not UI/API.
    user_in.password = None
    return update(db_session=db_session, user=user, user_in=user_in)
```
The permission check is only triggered when the “**Role**” field is modified. If you attempt to change it from “**Member**” to “**Admin**” an error will occur.

However, if you click “Save” **without making any changes**, the permission validation is bypassed and the following code will execute:

```
# we currently only allow user password changes via CLI, not UI/API.
    user_in.password = None
```
In that context, “**user\_in.password**” was supposed to be assigned with a boolean value “**False**”, preventing any changes as stated in one of the commits.

Unexpectedly, the value was stored/hashed as a string allowing any user’s password to be set to string “**None**”.

Simply said, we could reset the password of any account including Administrators to “**None**” by opening the “**Edit**” page of the victim account and pressing the “**Save**” button.

This vulnerability was introduced as a fix of the previous reported vulnerability back in 2020 “[https://github.com/Netflix/security-bulletins/blob/master/advisories/nflx-2020-005.md](https://github.com/Netflix/security-bulletins/blob/master/advisories/nflx-2020-005.md)”

# Reporting to Netflix

When we reported the vulnerability, we explicitly mentioned that we installed the application from scratch and provided all necessary steps to the triagers.

Netflix Team evaluated the bug and decided to accept it, classifying it as a medium severity report on secondary target and awarding a bounty for it.

Testing this application was quite fun and there are more blog posts that will come from this engagement, so make sure to follow me and as there will be another post for another vulnerability that we were able to discover in the same application.
