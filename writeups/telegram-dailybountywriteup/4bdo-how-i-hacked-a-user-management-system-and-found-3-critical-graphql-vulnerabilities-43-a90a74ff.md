# How I Hacked a User Management System and Found 3 Critical GraphQL Vulnerabilities

- **Source URL:** https://medium.com/@4bdo/how-i-hacked-a-user-management-system-and-found-3-critical-graphql-vulnerabilities-4362eff1a38f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250126150138/https://medium.com/@4bdo/how-i-hacked-a-user-management-system-and-found-3-critical-graphql-vulnerabilities-4362eff1a38f
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/8562 (id 8562)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# How I Hacked a User Management System and Found 3 Critical GraphQL Vulnerabilities

*Hi, I’m Abdo Maged, a bug hunter with 7 months of experience in identifying and reporting security vulnerabilities.*

# **First Bug :**

# **“Taking Over an Admin Account: A Story of GraphQL Exploitation”**

It all started when I decided to explore the admin panel of a target application hosted at `https://admin-example.com`. My objective was to test for common vulnerabilities, focusing on the GraphQL endpoint at `/graphql`. I had a hunch that improper access controls might lead to serious security flaws, and my curiosity paid off.

# Step 1: Uncovering the Endpoint

Using basic recon techniques, I discovered the GraphQL endpoint. Visiting `https://admin-example.com/graphql` in a browser confirmed the endpoint was live and accessible. The first thing I noticed was that I could freely interact with it, even without authentication.

I decided to investigate further by exploring the available mutations. My goal was simple: see if any sensitive fields could be tampered with.

# Step 2: Crafting a Mutation

To my surprise, I found that the mutation `updateUsersPermissionsUser` could be used to modify user details. I hypothesized that this mutation might allow me to change the email associated with an admin account.

I constructed the following mutation:

```
mutation {
  updateUsersPermissionsUser(id: 6, data: {
    email: "attacker@example.com",
    blocked: false,   # Bypass block functionality
    confirmed: true   # Skip email confirmation
  }) {
    data {
      id
      attributes {
        username
        email
        confirmed
        blocked
      }
    }
  }
}
```
To test this, I submitted the query and observed the response. While the server claimed the operation had failed, I verified that the email associated with the admin account had indeed been updated.

# Step 3: Resetting the Password

At this point, I controlled the email for an admin account. My next move was to gain full access by resetting the password. I used the “Forgot Password” functionality via the following mutation:

```
mutation {
  forgotPassword(email: "attacker@example.com") {
    ok
  }
}
```
Shortly afterward, I received an email with a token to reset the password. This token became the key to my next steps.

# Step 4: Setting a New Password

Armed with the reset token, I crafted another mutation to set a new password:

```
mutation {
  resetPassword(password: "NewSecurePassword123", passwordConfirmation: "NewSecurePassword123", code: "VALID_CODE") {
    jwt
    user {
      id
      username
      email
    }
  }
}
```
The response contained a privileged JWT token, granting me administrative access to the system.

# Step 5: Full Account Takeover

With the token in hand, I added it to the Authorization header of my requests:

`Authorization: Bearer <JWT_TOKEN>`
I now had full access to the admin account, including all its privileges.

# “ Privilege Escalation: Discovering a Hidden Flaw in GraphQL “

I knew there was more lurking behind the GraphQL endpoint at [https://admin-example.com/graphql](https://admin-heritage.neom.com/graphql). The earlier findings had already hinted at weak access controls, so I set out to test how far these flaws extended. I wasn’t just looking for vulnerabilities; I was piecing together a story of a system ripe for privilege escalation.

# Step 1: The Curious Mutation

I started by exploring the available GraphQL mutations, particularly focusing on `updateUsersPermissionsUser`. The documentation wasn’t visible, but by testing and observing the responses, I uncovered hints that this mutation allowed role changes for users.

This intrigued me: Could I modify roles without proper authorization? It was time to get creative and find out.

# Step 2: Crafting the Escalation

Using my standard user account, I submitted the following mutation:

```
mutation {
  updateUsersPermissionsUser(id: 5, data: {
    role: 5   # ID of the "Super Editor" role
  }) {
    data {
      id
      attributes {
        username
        email
        role {
          data {
            id
            attributes {
              name
              description
            }
          }
        }
      }
    }
  }
}
```
Initially, the server responded with what seemed like a denial. “Operation failed,” it claimed. But I wasn’t convinced. I dove deeper, verifying the actual impact on the database. Moments later, I found it — my account’s role was updated to “Super Editor.”

# The Doors Open

With my new role, I explored the admin panel. Every locked door was now open. Actions reserved for top-level users were suddenly within my reach. From managing content to accessing sensitive configurations, the possibilities were staggering.

But that wasn’t all. Testing the same mutation on other admin accounts revealed another disturbing flaw: I could demote admins by changing their roles to something less privileged. This system lacked not just locks, but any notion of a proper guard.

# The Bigger Picture

This wasn’t just a bug; it was a gaping hole in the application’s security model. Imagine an attacker escalating their privileges to “Super Editor” or sabotaging critical admin accounts. The potential for damage was almost limitless.

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

# The Third Bug : Unauthorized GraphQL access Led to Admins PII User Info

Disclosure.

After stumbling upon multiple vulnerabilities in the GraphQL endpoint at `https://admin-example.com/graphql`, my instinct told me there was more to discover. The endpoint was proving to be a treasure trove of security misconfigurations, so I decided to test if it could reveal sensitive information about admin accounts. What I uncovered was both surprising and critical.

# Step 1: Setting the Stage

As I navigated the GraphQL playground, I decided to explore potential queries that might expose user data. My focus shifted to discovering whether sensitive Personally Identifiable Information (PII) of admins was accessible.

I wrote the following query to fetch user details:

```
query GetAllUsers {
  usersPermissionsUsers {
    data {
      id
      attributes {
        username
        email
        failedAttempt
        recoveryToken
        lastPasswords
        createdAt
        confirmed
        blocked
        role {
          data {
            id
            attributes {
              name
              description
            }
          }
        }
      }
    }
  }
}
```
Executing this query, I was astonished to find that it not only worked without authentication but also returned a wealth of sensitive data about all users — including admins.

# Step 2: Unearthing Sensitive Admin Information

The response revealed critical information:

- Admin usernames and emails
- Password recovery tokens and past passwords
- Account statuses such as `confirmed`, `blocked`, and `failedAttempt`
- Creation dates and role details

This level of exposure meant an attacker could gather data to launch targeted phishing attacks, perform account takeovers, or build detailed profiles for further exploitation.

# Step 3: Testing Scope and Validation

I dug deeper, testing whether this issue was limited to specific accounts or applied universally. The results were consistent — anyone with access to the endpoint could retrieve the data.

The problem stemmed from the GraphQL endpoint treating all users equally, without enforcing proper authorization checks. High-privilege data was as easily accessible as public information.

# Step 4: The Danger of Unchecked Access

The implications of this vulnerability are severe:

- **Privacy Violation:** Exposing sensitive data of admin and user accounts is a clear breach of privacy.
- **Potential Exploits:** Information such as recovery tokens and past passwords could aid attackers in gaining unauthorized access.
- **Reputational Risk:** Public exposure of such sensitive details could damage user trust and the organization’s reputation.

# Lessons Learned and Recommendations

This vulnerability underscores the importance of strict authorization controls. To address this issue:

1. **Enforce Role-Based Access Control (RBAC):** Only authorized users should be able to query sensitive data.
2. **Filter Returned Fields:** Sensitive data like recovery tokens and past passwords should never be included in public API responses.
3. **Implement Token Validation:** All queries should require a valid and authorized token before processing.

والسَلآْم عَلْيُكّمٌ وٍرٍحَمُةّ الله وٍبُرٍكآتُهْ

Contact Me

facebook : [https://www.facebook.com/profile.php?id=100014962988014](https://www.facebook.com/profile.php?id=100014962988014)
