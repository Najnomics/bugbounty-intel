# When an AI Backend Forgot to Ask Who You Were

- **Source URL:** https://medium.com/@haykeenspaul/when-an-ai-backend-forgot-to-ask-who-you-were-finding-unauthenticated-llm-invocation-in-a-figmabot-cee4d5683ed7
- **Fetched from:** https://medium.com/@haykeenspaul/when-an-ai-backend-forgot-to-ask-who-you-were-finding-unauthenticated-llm-invocation-in-a-figmabot-cee4d5683ed7?source=rss-d9b730199ed9------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14896)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** PaulHaykeens / Wed, 02 Sep 2026 19:58:04 GMT

Hello, my name is Godwin Akinyomi, although I use Paul Haykeens as my public identity as a security researcher.

I’m an Offensive Security Researcher focused on Web, API and Mobile Security, with a particular interest in vulnerability research and understanding how applications enforce security boundaries.

This article is about one of the findings I discovered during an authorized security assessment of a FigmaBot backend.

The finding itself wasn’t a sophisticated exploit chain. It started with a simple question:

The answer turned out to be interesting.

The backend’s \`/chat\` endpoint accepted unauthenticated requests and proceeded to invoke model inference even when no valid pairing code or authenticated session was provided.

As I investigated further, I found that the backend identified itself as a Figma-oriented AI assistant and exposed information about an intended set of Figma-related tools.

I responsibly disclosed the issue to the affected organization, and the vulnerability was subsequently resolved.

Disclosure note: This article intentionally omits the organization’s name, hostname, infrastructure details, bounty information, internal evidence, and other sensitive information. The technical details have been retained where they are useful for understanding the vulnerability without exposing the affected environment.

While exploring the application’s API surface, I came across a \`/chat\` endpoint.

My first question was straightforward:

I wasn’t interested in doing anything destructive. I started with a completely harmless prompt designed simply to determine whether the backend would process a request.

I sent a request without a session cookie, without an \`Authorization\` header, and with the pairing value explicitly set to \`null\`.

The request looked roughly like this:


POST /chat HTTP/1.1

Host: \[REDACTED\]

Content-Type: application/json

Accept: application/json

{

"messages": \[

{

"role": "user",

"content": "Reply with exactly: PaulHaykeens"

}

\],

"pairing\_code": null

}

\`\`\`

The backend responded:

\`\`\`http

HTTP/1.1 200 OK

Content-Type: application/json

\`\`\`

and returned:

\`\`\`json

{

"content": "PaulHaykeens"

}

\`\`\`

That immediately caught my attention.

There was no authentication token.

There was no authenticated session.

There was no valid pairing code.

Yet the backend had processed the prompt and returned model-generated content.

At that point, I had a hypothesis:

The model invocation layer might be reachable before the application verifies the caller’s identity.

The next step was determining whether this was intentional or a genuine security boundary failure.

A successful unauthenticated request alone doesn’t necessarily mean a vulnerability.

Some AI services intentionally expose anonymous chat functionality.

So the next question was:

I looked at the publicly exposed OpenAPI specification.

The API documentation exposed endpoints including:

\`\`\`text

/chat

/pairing

/pairing/{code}/status

/health

\`\`\`

The presence of a pairing workflow was particularly interesting.

It suggested that the FigmaBot wasn’t simply intended to be an anonymous chatbot. There appeared to be a concept of establishing a relationship between a client and the backend.

That raised a more specific security question:

If pairing exists, why can \`/chat\` invoke the backend model without a valid pairing session?

At this point, I wanted to understand what was behind \`/chat\`.

I sent another harmless request asking the model to describe its role and the tools available to it.

The responses identified the service as a Figma-oriented assistant and referenced functionality such as:

\* \`get\_document\_info\`

\* \`get\_node\_info\`

\* \`create\_frame\`

\* \`create\_text\`

\* \`create\_component\_instance\`

\* \`set\_auto\_layout\`

\* \`set\_focus\`

\* \`delete\_node\`

This was useful context.

It indicated that the backend wasn’t merely providing generic text generation. It appeared to be part of an AI agent workflow designed around interaction with Figma.

That significantly changed how I viewed the authentication issue.

The problem wasn’t simply:

An unauthenticated user can talk to an AI.

It was:

An unauthenticated user could directly invoke an AI backend that appeared to sit behind a pairing-oriented Figma workflow.

I then tried to determine whether the missing authentication could be escalated into actual access to Figma documents or canvas operations.

This distinction was important.

I did *not* want to claim access that I couldn’t demonstrate.

The model described Figma-related tools, but my testing did not produce reliable evidence of actual Figma document access using \`pairing\_code: null\`.

I did not obtain:

\* real document names

\* Figma file keys

\* real node IDs

\* actual canvas contents

\* confirmed unauthorized canvas modifications

Some responses were also inconsistent, which made it inappropriate to treat the model’s description of available tools as proof that those tools were actually executable in the unauthenticated session.

So I kept the finding scoped to what I could prove:

Unauthenticated remote users could invoke the backend LLM functionality.

The Figma tooling exposure was supporting evidence about the intended role of the service, not proof of unauthorized Figma canvas access.

That distinction matters in vulnerability research.

I also checked the endpoint’s CORS behavior.

The API responded to a preflight request with:

\`\`\`http

Access-Control-Allow-Origin: \*

\`\`\`

and allowed the \`POST\` method.

This was interesting, but I did not treat it as the primary vulnerability.

CORS wasn’t required to exploit the authentication issue because the API was already directly reachable without authentication.

In other words:

CORS made the exposure more convenient for browser-based clients, but it wasn’t what caused the security boundary to fail.

This is an important distinction when chaining observations together. Not every security-relevant configuration should automatically become part of the severity argument.

The core issue was the order in which security controls appeared to be applied.

The application exposed a pairing mechanism, but \`/chat\` accepted:

\`\`\`json

"pairing\_code": null

\`\`\`

and proceeded to invoke model inference anyway.

A simplified representation of the intended flow would presumably look something like:


\`\`\`text

Client

│

├── Authenticate / Pair

│

▼

Validate session

│

▼

Authorize request

│

▼

Invoke FigmaBot / LLM

\`\`\`

The observed behavior instead looked closer to:

\`\`\`text

Unauthenticated Client

│

▼

/chat

│

▼

LLM invocation

\`\`\`

The authentication or pairing boundary was therefore not being enforced before model execution.

The most concrete impact I could demonstrate was *unauthorized consumption of the backend AI service.*

An attacker could remotely submit prompts and receive model responses without possessing a valid user session or pairing code.

Depending on the service’s underlying infrastructure and usage model, this could result in:

\* unauthorized consumption of LLM resources

\* abuse of model quotas

\* increased operational costs

\* automated prompt abuse

\* exposure of internal AI-agent behavior

\* disclosure of implementation or tooling information

There was also a potentially more significant concern around the Figma integration.

If the unauthenticated execution path had been connected to live Figma tools, the consequences could have included unauthorized access to or manipulation of Figma resources.

However, ***I could not confirm that escalation***, so I did not report it as demonstrated impact.

That distinction was important to me.

A good vulnerability report should clearly separate:

*what was proven*

from

*what could potentially happen if another control were also bypassed.*

For researchers working in an authorized environment, the core behavior can be reproduced with a minimal request:

\`\`\`bash

curl -i -sS 'https://\[authorized-host\]/chat' \

-H 'Content-Type: application/json' \

- data '{

"messages": \[

{

"role": "user",

"content": "Reply with exactly: PaulHaykeens"

}

\],

"pairing\_code": null

}'

\`\`\`

A vulnerable implementation would return a successful model response despite the absence of authentication or a valid pairing session.

The important part isn’t the specific string used in the prompt.

The important observation is:

\`\`\`text

No authentication

+

No valid pairing

+

Successful model invocation

\`\`\`

The remediation was straightforward conceptually:

1\. Authenticate before invoking the model

The \`/chat\` endpoint should verify the caller’s authentication state before allowing model execution.

2\. Enforce pairing server-side

If the FigmaBot workflow requires pairing, the server should validate the pairing/session state rather than accepting:

and continuing execution.

3\. Apply rate limits and quotas

Even authenticated AI services should have appropriate per-user, per-session, and per-IP controls to prevent resource abuse.

4\. Restrict CORS

If browser access is required, CORS should be limited to trusted application origins rather than allowing every origin.

5\. Minimize agent/tool disclosure

An AI agent shouldn’t unnecessarily expose internal tooling, implementation details, or privileged capabilities to unauthenticated callers.

What I found here wasn’t a sophisticated exploit chain.

It was something much simpler:

*The backend trusted the request before establishing who was making it.*

That’s one of the reasons I enjoy API security research.

An endpoint can look completely ordinary from the outside. You send a request, receive a \`200 OK\`, and everything appears normal.

But sometimes the interesting question isn’t:

*What does this endpoint return?*

It’s:

*What security boundary did the backend cross to produce that response?*

In this case, the backend crossed an LLM invocation boundary without first establishing authentication or pairing.

The investigation also reinforced something I try to apply to vulnerability research:

Don’t overclaim the impact.

I could prove unauthenticated LLM invocation.

I could observe the FigmaBot identity and its intended tool interface.

I could not prove unauthorized Figma canvas access.

So that’s where I stopped.

The finding was responsibly disclosed to the Program and subsequently resolved.

For me, that’s the interesting part of security research, not simply finding something that looks wrong, but systematically determining ***exactly how far the security boundary can be crossed, and being precise about what the evidence actually proves***.

Researcher

*Godwin Akinyomi (Paul Haykeens)*

Offensive Security Researcher || Web, API & Mobile Security

Vulnerability Research || Bug Bounty

*Curiosity is the only crime. 🧑💻*
