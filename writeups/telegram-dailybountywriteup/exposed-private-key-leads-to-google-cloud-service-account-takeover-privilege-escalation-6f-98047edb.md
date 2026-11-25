# Exposed private key leads to Google cloud service account takeover — Privilege Escalation

- **Source URL:** https://vettrivel007.medium.com/exposed-private-key-leads-to-google-cloud-service-account-takeover-privilege-escalation-6f031e20c819?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250501135714/https://vettrivel007.medium.com/exposed-private-key-leads-to-google-cloud-service-account-takeover-privilege-escalation-6f031e20c819?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/7404 (id 7404)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Exposed private key leads to Google cloud service account takeover — Privilege Escalation

In today’s cloud-driven world, safeguarding sensitive data is crucial.

Recently, I came across a critical vulnerability in Google Cloud Service that could lead to a full service account takeover through exposed private keys. This discovery highlights the importance of keeping cloud credentials secure, and in this post, I’ll walk you through the vulnerability, how it can be exploited, and its devastating impact on Google Cloud resources.


**Description:**

An attacker with access to a private key associated with a Google Cloud service account can gain full control over the account and its resources.

This includes changing admins to normal user. Also we can viewing, modifying, and even deleting data across the cloud environment. The risk posed by this vulnerability is massive, considering the sensitive nature of data stored and managed on cloud platforms.

**Why JavaScript Files are Targets for Recon ?**

When performing recon, one key target is JavaScript files, as they often contain sensitive information like API keys, tokens, and service credentials that developers accidentally expose.

By inspecting `.js` files loaded by a website or using automated tools, you can search for keywords like Private tokens or credentials, Endpoint URLs for internal services, Client secrets, Google Cloud or AWS credential, Database connection string **,**`api-Key`, `auth`, `token`, or `password` to identify exposed secrets. It’s crucial for developers to avoid embedding sensitive data in client-side code and ensure proper security configurations.

# STEPS TO REPRODUCE :

During a recon session, I discovered an exposed Google Cloud private key at the following URL:

- **https://storage.googleapis.com/x-y-z.js**

List of Sensitive data :


- **Project-id**
- **Private-key-id**
- **Private-key**
- **Client-email**
- **Client-id**
- **Auth-uri**
- **Token-uri**
- **Auth-provider**

**Step 01:**


- Save the sensitive Google Cloud service account information as a `.json` file. This key file contains credentials to access the cloud account.

**Step 02:**


- Activate the service account using the following command:

`gcloud auth activate-service-account --key-file="C:\path_to_the_file\Desktop\service-account-key.json"`
- **Note:** Ensure you have Google Cloud SDK installed.

**Step 03:**


- Verify authentication and check which account is currently active

```
gcloud auth list
gcloud config list
```
- You can also view the list of projects the account has access to

`gcloud projects list`
**Step 4:**


- Retrieve a list of IAM roles

`gcloud iam roles list`
- This command reveals all the roles within the Google Cloud environment, including sensitive permissions.

**Step 5:**


- Describe a specific role to view its full details

`gcloud iam roles describe <role-name>`
- This allows you to access descriptions, stages, and detailed information about each role.

# Impact

By exploiting this vulnerability, an attacker can gain complete control over the Google Cloud Service account, which has severe consequences:

- **View and Manage Roles:** The attacker can list roles, retrieve role details, and perform critical role-based actions.
- **Modify Permissions:** They can create, delete, or update custom roles, essentially gaining the power to escalate privileges.
- **Access Sensitive Data:** Depending on the roles and permissions associated with the compromised service account, the attacker may access critical databases, services, and resources within the cloud environment.

**Key Capabilities an Attacker Gains:**


1. **List Roles:** View all available roles within the project.
2. **Get Role Details:** Retrieve detailed information on any role.
3. **Create Custom Roles:** Add new roles with potentially dangerous permissions.
4. **Delete Custom Roles:** Remove existing roles, potentially disrupting operations.
5. **Update Roles:** Modify existing roles to escalate privileges or reduce restrictions.

# Mitigations :

- **Use Cloud Secret Managers**: Store and manage sensitive information securely in secret management tools provided by cloud services (e.g., Google Secret Manager, AWS Secrets Manager).
- **Avoid Hardcoding Secrets**: Never embed keys, tokens, or credentials directly in frontend code. Use server-side environments to handle sensitive data securely.
- **Use Environment Variables**: Store sensitive data on the backend and access it securely from there.

I’ll catch up with you later with another interesting topic.

Stay tuned, and feel free to connect with me on LinkedIn: [https://www.linkedin.com/in/vettrivel2006](https://web.archive.org/web/20250501135714/https://www.linkedin.com/in/vettrivel2006) .

Thank you for reading :)
