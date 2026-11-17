# How I Escalated from Operator to Admin on a Leading Travel Platform on Hackerone Via GraphQL…

- **Source URL:** https://medium.com/@sebasvargas2/cross-supplier-privilege-escalation-how-i-escalated-from-operator-to-admin-on-a-leading-travel-614a67f459ab
- **Fetched from:** https://medium.com/feed/@sebasvargas2
- **Fetched:** 2026-11-17
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14986 (id 14986)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### How I Escalated from Operator to Admin on a Leading Travel Platform on Hackerone Via GraphQL Mutation

#### Cross-Supplier Privilege Escalation

Hello everyone! Today, I want to share an interesting authorization vulnerability that I recently discovered on the supplier portal of a leading global travel and booking platform. It allowed an attacker holding a low-privilege role (such as a Operator or Guide) on a target supplier to completely escalate their account role to **ADMIN** across different suppliers.

Let’s dive into how I found it, how it worked, and how it was successfully patched!

### Reconnaissance & Setup

While exploring the supplier portal’s GraphQL endpoint (POST /graphql), I started analyzing how user roles and permissions are managed across different supplier organizations.

To test this scenario properly, I registered two completely independent accounts from scratch using the supplier registration flow:

- **Attacker Account:** Created with full **ADMIN** privileges on *Supplier A* (Attacker Company).
- **Victim Account:** Created with full **ADMIN** privileges on *Supplier B* (Victim Company).

### Linking the Accounts

Next, I simulated a real-world scenario where the victim wants to add a new team member. From the Victim’s dashboard, the admin invited the Attacker’s email address and assigned a low-privilege role: **Ticketing**.

Once the invitation was sent, the attacker received a notification email. The interesting behavior here was that no confirmation handshake was required, the attacker simply needed to log out and log back in. Upon logging back in, a multi supplier selection prompt appeared, allowing the user to choose between *Supplier A* (where they were an Admin) and *Supplier B* (where they were just a Finance or Ticketing).

### Finding the Authorization Flaw

When logged into the Victim’s supplier profile (*Empresa de Pepe*), my access was properly restricted as a FINANCE. However, when logged into my own company (*Empresa maligna*), I had full **ADMIN** capabilities.

I navigated to the account management section under my own attacker company (*Empresa maligna*) to modify user information:

1. I triggered an update request in the UI.
2. Without making any changes yet, I intercepted the HTTP request using **Burp Suite** and sent it over to **Repeater**.

Inspecting the GraphQL mutation (accountUpdate), I noticed a critical authorization gap: the backend authorization layer checked whether my JWT contained the supplier:admin role claim, but **it failed to verify whether that admin role actually corresponded to the specific supplierId being mutated in the request body**.

### Exploiting the GraphQL Mutation

In Burp Repeater, I modified the intercepted request by replacing the session JWT:

- I swapped out the session token and replaced it with the active **JWT belonging to my Attacker account** (where I held full **ADMIN** privileges on *Empresa Maligna*).
- I ensured the mutation payload targeted the appropriate fields and role configuration as **ADMIN**.

When I sent the crafted request using the attacker’s admin JWT, the backend failed to validate whether that administrative session actually corresponded to the target supplier, responding with a clean

To verify the impact, I logged out and logged back into my attacker account, selected the Victim Supplier ID (*Empresa Pepe*), and boom! I now had complete **ADMIN** access to all administrative functionalities, bookings, financials, inventory, and sensitive traveler PII belonging to the victim company.

### Impact

An attacker who is an admin on their own supplier and holds a minimal non-privileged role on a target supplier can:

- Elevate their own account to **ADMIN** on any target supplier.
- Gain full access to bookings, financial records, inventory, products, and reviews.
- Modify the target supplier’s company details, terms and conditions, and privacy policies.
- Create, manage, or delete user accounts within the victim organization.

### Remediation & Timeline

I reported this vulnerability to the platform’s security team through their Bug Bounty program. Their triage and engineering teams were super responsive and handled the fix quickly:

- **July 29, 2026:** Report submitted and triaged.
- **July 30, 2026:** Clarified the multi-supplier login behavior and provided a video PoC.
- **August 7, 2026:** The engineering team deployed a patch ensuring that the accountUpdate mutation derives the supplier directly from the authenticated session and ignores any external supplierId sent in the request body.
- **August 7, 2026:** Retested, confirmed the fix, and the report was marked as **Resolved**.

The proper fix implemented by the developers required validating that the authenticated session’s admin privileges directly match the target supplierId being modified:

IF user.role == "supplier:admin" THEN

VERIFY user.supplier\_id == input.supplierId

Thank you for reading! I hope this write up helps fellow bug bounty hunters and developers understand the importance of strict context-aware authorization checks in GraphQL APIs.

I have made a Video PoC where I show you all the full process:

[https://www.youtube.com/watch?v=PGUb1ZGxrb8&t=63s](https://www.youtube.com/watch?v=PGUb1ZGxrb8&t=63s)

Stay safe and happy hacking! 🚀
