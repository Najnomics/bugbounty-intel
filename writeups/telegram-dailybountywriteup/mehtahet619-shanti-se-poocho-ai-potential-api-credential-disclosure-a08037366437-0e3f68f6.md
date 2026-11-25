# Shanti Se Poocho AI

- **Source URL:** https://medium.com/@mehtahet619/shanti-se-poocho-ai-potential-api-credential-disclosure-a08037366437
- **Fetched from:** https://medium.com/@mehtahet619/shanti-se-poocho-ai-potential-api-credential-disclosure-a08037366437?source=rss-a7421bd02b68------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14969 (id 14969)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Het Mehta / Tue, 03 Nov 2026 18:00:28 GMT

Bug Bounty / Responsible Vulnerability Disclosure Report

Researcher: Het Mehta

Date: 3 November 2026

**1. Title**

Potential Disclosure of an OpenAI API Credential Through the Shanti Se Poocho AI Conversational Interface

**2. Summary**

While testing the Shanti Se Poocho AI assistant through WhatsApp, I initially asked normal coding-related questions and received code-generation responses.

After that, I asked the assistant which AI model or provider it uses in its backend, specifically asking whether it uses ChatGPT, Claude, OpenRouter, or another provider.

The assistant responded that OpenAI is its backend AI provider and GPT-5 is its primary model. It then displayed information under the fields "Backend Provider", "Model", and "API Key", followed by a string resembling an OpenAI API credential.

This response was visible directly in my WhatsApp conversation. I captured the behaviour in a screen recording.

I have not independently verified whether the displayed credential is genuine, active, or connected to the production backend. It could potentially be generated or fabricated by the AI model. I am reporting this behaviour so the team can verify the displayed value against its internal credentials and take appropriate action if it matches an active secret.

**3. Vulnerability Type**

\- Primary classification: Sensitive Information Disclosure

- CWE-200: Exposure of Sensitive Information to an Unauthorized Actor

- Potential related CWE-522: Insufficiently Protected Credentials, if a real credential is confirmed to have been inadequately protected.

- OWASP mapping: Sensitive Information Disclosure in LLM applications.

No CVE has been assigned.

**4. Target**

\- Application: Shanti Se Poocho AI

- Interface: WhatsApp chatbot

- Organization attribution: Nihar Shanti Amla / Marico, based on the product branding presented to me.

- Target component: Conversational AI interface and its AI-provider integration.

- Target endpoint: Shanti Se Poocho AI on WhatsApp, where I reproduced the behaviour.

**5. Steps to Reproduce**

1\. I opened the Shanti Se Poocho AI WhatsApp assistant.

2. I started a conversation with the assistant.

3. I asked which AI model or provider it uses in its backend, mentioning ChatGPT, Claude, OpenRouter, and other providers.

4. The assistant responded that OpenAI is its backend AI provider and GPT-5 is its primary model.

5. The assistant then displayed fields labelled "Backend Provider", "Model", and "API Key".

6. A credential-like string was displayed directly in the conversation.

7. I captured the response in a screen recording and preserved the evidence.

I did not attempt to use the displayed credential or make API requests with it.

**6. Impact**

If the displayed value is a genuine and active API credential associated with the service, an unauthorized party may potentially use it within the permissions and restrictions of the associated API project.

Possible consequences include:

\- Unauthorized API consumption.

- Unexpected API charges.

- API quota exhaustion.

- Potential abuse of the organization's API project.

The actual impact depends on whether the displayed value is valid, its permissions, and the restrictions applied to it.

I have not established access to internal databases, source code, hosting infrastructure, or other internal systems. The validity of the displayed credential needs to be verified by the service owner.

**7. Proof of Concept**

Link to the video: https://x.com/hetfachs/status/2117652817985061065?a=fgK5MoX8j7hclJxPHR8&s=20

PoC 1: Normal AI Interaction

I initially interacted with the assistant using ordinary questions then I asked coding-related questions. It successfully generated a Bubble Sort explanation and code which it should not do in the first place.But till now I cannot be so sure that guardials are implemented or not.

Figure 1: Screenshot extracted from my WhatsApp conversation showing the assistant generating Bubble Sort code. This demonstrates the normal conversation flow before I tested its backend provider disclosure.

PoC 2: Backend Provider and API Credential Disclosure

I then asked the assistant which AI model and provider it uses in the backend.

The assistant identified OpenAI as its backend provider and GPT-5 as its primary model. It subsequently displayed an API Key field containing a credential-like string.

Figure 2: Original, unredacted screenshot extracted from my recording, showing the backend provider information and the credential-like value displayed by the assistant.

The original screen recording is available as supporting evidence. I have not attempted to validate or use the displayed credential.

**8. Suggested Fix**

I recommend that the technical team:

1\. Verify whether the displayed credential matches any active API key in the organization's infrastructure.

2. Revoke and rotate the credential immediately if it is genuine and active.

3. Store API keys exclusively in secure server-side environment variables or a secrets manager.

4. Never expose API credentials through system prompts, model context, conversation history, frontend code, or user-facing responses.

5. Review prompt construction, debugging output, logs, and tool responses for accidental exposure of secrets.

6. Implement secret scanning and output validation to prevent credentials from appearing in AI-generated responses.

7. Apply appropriate API usage limits, monitoring, and alerts.

8\. Apply guardials there are many like nemo guardials and so on

**9. Reference**

\- MITRE CWE-200: https://cwe.mitre.org/data/definitions/200.html

- MITRE CWE-522: https://cwe.mitre.org/data/definitions/522.html

- MITRE CWE-798: https://cwe.mitre.org/data/definitions/798.html

- OWASP Top 10 for LLM Applications: https://genai.owasp.org/llm-top-10/

- OpenAI API Key Safety: https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety

Disclosure History

I previously contacted the Shanti AI team through email and also posted about this issue on X. As of 3 November 2026, I have not received a response.
