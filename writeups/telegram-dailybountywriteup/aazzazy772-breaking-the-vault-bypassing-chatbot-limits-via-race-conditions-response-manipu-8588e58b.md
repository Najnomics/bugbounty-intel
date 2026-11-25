# Breaking the Vault

- **Source URL:** https://medium.com/@aazzazy772/breaking-the-vault-bypassing-chatbot-limits-via-race-conditions-response-manipulation-e8f68ce3e354
- **Fetched from:** https://medium.com/@aazzazy772/breaking-the-vault-bypassing-chatbot-limits-via-race-conditions-response-manipulation-e8f68ce3e354?source=rss-ea48db0a1e97------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14958 (id 14958)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Ahmed 3zzazy / Sat, 24 Oct 2026 13:34:49 GMT

In modern fintech and digital platforms, features like AI-powered chatbots aren’t just cool perks — they are massive cost drivers. Leveraging Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs) means every single prompt processed by the backend burns valuable API tokens and compute resources.

To keep operational costs in check, applications implement strict limits — such as a maximum of **5 active chatbot conversations** per user.

This write-up explores how an attacker can completely obliterate this business logic limit by chaining **three distinct vulnerabilities**: a **Race Condition**, a **Frontend Logic Bypass**, and a **Backend Logic Bypass**. The result? Infinite chat sessions, completely bypassed tier limitations, and a severe **Denial of Wallet (DoW)** vector.

The application’s limitation enforcement relies on two pillars:

**2. Backend Validation:** The /init endpoint checks the database count before allowing a new conversation. If a user tries to force it, the backend responds with an HTTP 429 Too Many Requests.

By combining concurrency with client-side trust, an attacker can bypass both layers entirely.

When a user has already created 4 conversations and attempts to create the 5th, normal sequential requests are safely blocked. However, computers operate on milliseconds.

2\. They intercept the request to create the 5th conversation using **Burp Suite**:

POST /redacted/api/v1/chatbot/conversations/init HTTP/2

Host: redacted.com

Authorization: Bearer eyJhbGci…\[TRUNCATED\]

Content-Type: application/json

{"platform":"website"}

3\. Using **Turbo Intruder** or **Burp Repeater’s “Send group in parallel”** feature, the attacker fires multiple concurrent requests (3–5 requests simultaneously) right before hitting the hard limit.

**4. The Flaw:** Due to a lack of proper database locking or atomic operations on the count check, the server races past the check and returns **200 OK** for multiple concurrent requests, generating several valid conversation\_id tokens in the database. The attacker saves one of these hidden IDs.

With the database now holding more than 5 conversations, the frontend naturally locks down the UI because its state reflects reality. Time to trick the client.

GET /redacted/api/v1/chatbot/conversations HTTP/2

Host: redacted.com

Authorization: Bearer eyJhbGci…\[TRUNCATED\]

2\. The server responds with the true list of 5 active chats:

```
{
 “conversations”: [
 {“id”:”97f242…”},
 {“id”:”74ec92…”},
 {“id”:”bd5887…”},
 {“id”:”943598…”},
 {“id”:”cc278a…”}
 ]
}
```
3\. **Response Manipulation 1:** The attacker intercepts this response in Burp Suite and deletes one JSON object from the array before forwarding it.

**4. The Result:** The frontend believes only 4 chats exist, instantly re-enabling the “New Conversation” button.

Now that the UI is unlocked, the attacker attempts to start a brand new conversation.

HTTP/2 429 Too Many Requests

Content-Type: application/json

{"detail":"You have reached the limit of active conversations. Please delete one of your previous conversations to start a new one."}

**3. Response Manipulation 2:** Instead of accepting defeat, the attacker intercepts this error response, changes the status code from 429 Too Many Requests to **200 OK**, and hot-swaps the body with a success message injecting the pre-harvested conversation\_id from Part 1:

```
{
 “status”: “success”,
 “conversation_id”: “[INSERT_RACE_CONDITION_ID_HERE]”,
 “platform”: “dashboard”,
 “message”: “User registered and initial conversation created.”
}
```
4\. **The Result:** The frontend happily accepts the payload. The attacker can now seamlessly chat in this new session. All subsequent message requests using this ID are processed normally by the backend, completely bypassing the limit!

This multi-stage chain is far more than a simple UI glitch; it introduces serious business risks:

*The report was triaged and accepted as* ***Low Severity (CVSS 3.1)*** *with a* ***$50 bounty****, acknowledging the valid logic flaw and concurrency issue in backend validation.*
