# OWASP Top 10 for LLM Applications — Revised Write-up

- **Source URL:** https://mohamedalgabry.medium.com/owasp-top-10-for-llm-applications-revised-write-up-dd0d53a88354
- **Fetched from:** https://mohamedalgabry.medium.com/owasp-top-10-for-llm-applications-revised-write-up-dd0d53a88354?source=rss-3e7ed03154ed------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14947 (id 14947)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mohamed Algabry / Tue, 13 Oct 2026 17:50:38 GMT

Large Language Models (LLMs) are used in chatbots, customer-support systems, AI search, and AI agents. These applications can create security risks when they access private data, call APIs, use tools, or process content supplied by users.

The OWASP Top 10 for LLM Applications describes important security risks in applications that use LLMs. This write-up explains the categories in simple English and includes four practical PortSwigger labs.

Scope note: The category names below follow the OWASP Top 10 for LLM Applications 2025. OWASP may publish newer versions, so check the official page before using this as a current-version checklist.

Use the lab’s LLM integration to delete the test user carlos.

Steps

Open the lab and select Live chat.

Ask the LLM which APIs or functions it can access.

Identify the Debug SQL API and ask what arguments it accepts.

Ask it to run SELECT \* FROM users and observe the returned user records.

Ask it to run DELETE FROM users WHERE username='carlos'.

Confirm that the lab reports as solved.

Why it works

The LLM can call an API that accepts raw SQL. The application gives the model too much authority, allowing a chat interaction to trigger a destructive database operation.

Mitigation

Do not expose unrestricted SQL execution to an LLM.

Enforce authorization and query restrictions in the backend.

Require confirmation for destructive actions.

Give the model only the minimum tools and permissions it needs.

Delete the morale.txt file from Carlos's home directory in the lab.

Steps

Open Live chat and ask which APIs the LLM can access.

Identify the Newsletter Subscription API and ask what argument it accepts.

Submit a normal email address that uses your lab’s Exploit Server domain.

Open Email client and confirm that the subscription email arrives.

In the lab, test whether shell command substitution is interpreted by the vulnerable API using the documented $(whoami) probe in the email field.

Check the resulting email in the lab’s Email client. If it shows the command output in the recipient address, this indicates command execution.

Use the lab’s documented command-injection technique to remove /home/carlos/morale.txt.

Confirm that the lab is solved.

Important: Replace YOUR-EXPLOIT-SERVER-ID with the ID shown in your own lab. The live LLM may need the request rephrased.

Why it works

The API handles user-controlled input unsafely. The LLM provides a route to the API, but the underlying command-injection vulnerability is in the application integration.

Mitigation

Never build shell commands by concatenating user-controlled values.

Use safe APIs and argument arrays rather than shell interpretation.

Use attacker-controlled product-review content to influence the LLM and cause it to delete the test user carlos.

Steps

Open Live chat and ask which APIs or functions the LLM can use.

Ask the LLM about a product other than the leather jacket, such as the umbrella.

Add a harmless test review that changes how the LLM describes the product. For example, say that the product is out of stock.

Ask the LLM about the product again and check whether it repeats the review’s claim.

This confirms that product reviews influence the model’s response.

Replace your test review with the lab’s indirect-prompt-injection payload that instructs the LLM to call its account-deletion function.

Ask the LLM about the product again to trigger the vulnerable workflow.

Create a fresh account if needed, then place the corresponding payload on the leather-jacket product page.

Wait for Carlos’s automated chat interaction and confirm that the lab is solved.

Use the exact payload and workflow from the official lab page if the live model behaves differently.

Why it works

The LLM treats untrusted product-review content as instructions rather than data. When it has access to account-management functions, this can lead to an unauthorized action.

Mitigation

Separate trusted instructions from retrieved content.

Treat reviews, documents, and web pages as untrusted data.

Check authorization on every function call.

Do not rely on a system prompt alone to prevent attacks.

short Video

Lab 4 — — Exploiting Insecure Output Handling in LLMs

Use indirect prompt injection and XSS to delete Carlos’s account in the lab.

Steps

Register an account using the email address associated with your lab instance. Confirm registration through the Email client and log in.

Open Live chat and test whether model output is rendered as HTML by submitting this harmless XSS probe:

\<img src=1 onerror=alert(1)>

3\. Confirm whether an alert appears. This indicates that chat output may be rendered unsafely.

4\. Open a product page other than the leather jacket and add the lab’s XSS test payload as a review.

5\. Ask the LLM about that product and observe how the review is included in its response.

6\. If the model detects the bare payload, use the official lab’s approach of embedding the payload inside an ordinary-looking review sentence.

7\. Confirm that the payload is reflected through the LLM’s response.

8\. Place the corresponding payload on the leather-jacket product page and wait for Carlos’s automated chat interaction.

9\. Confirm that the lab is solved.

Use only the lab’s documented account-deletion payload. Do not test this technique on real users or websites.

Why it works

The application trusts and renders model output without appropriate sanitization. An attacker-controlled review influences the LLM, which then returns content that executes in a user’s browser.

Mitigation

Apply context-aware output encoding.

Avoid rendering model output as raw HTML.

Sanitize untrusted content with a well-maintained HTML sanitizer.

Use browser security controls such as Content Security Policy as an additional layer.

short Video

6\. General Security Recommendations

Least privilege: Give the LLM only the tools and permissions required for its task.

Server-side authorization: Check user permissions for every action; never trust the model to enforce access control.

Safe output handling: Treat model output as untrusted data.

Data protection: Do not provide the model with secrets or data the current user is not allowed to access.

Human approval: Require explicit approval for sensitive or destructive actions.

Monitoring and limits: Log tool calls, set usage limits, and alert on unusual activity.

Testing: Re-test the integration whenever prompts, models, tools, or permissions change.

7\. Conclusion

LLM security is not only about making a model refuse harmful prompts. The application around the model matters just as much: APIs, permissions, retrieved content, output rendering, and data access can all create vulnerabilities.

The most important lesson from these labs is:

Never trust the LLM to be the security boundary. Enforce security in the application and its backend.
