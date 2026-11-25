# Inside a Bug Bounty Investigation

- **Source URL:** https://medium.com/@Akarsh_Chaturvedi/inside-a-bug-bounty-investigation-from-reconnaissance-to-a-reproducible-security-finding-1b7c3cce9165
- **Fetched from:** https://medium.com/@Akarsh_Chaturvedi/inside-a-bug-bounty-investigation-from-reconnaissance-to-a-reproducible-security-finding-1b7c3cce9165?source=rss-42087a213b30------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14951 (id 14951)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Akarsh_¢haturvedi / Sat, 17 Oct 2026 19:25:41 GMT

Every good assessment starts with a question narrow enough to answer and important enough to matter. Mine for this lab engagement was deceptively simple: after a user logs in, what stops them from asking the application for someone else’s data? Most modern APIs authenticate requests beautifully and authorize objects carelessly. A JSON Web Token proves who you are; it says nothing about whether invoice #8842 belongs to you. That gap between “you are logged in” and “you may touch this object” is where broken object-level authorization (BOLA/IDOR) lives, and it has held the top spot on the OWASP API Security Top 10 for good reason.

This article walks through a complete investigation lifecycle on a fictional SaaS invoicing platform: scoping, reconnaissance, trust boundary analysis, hypothesis formation, controlled validation, severity reasoning, responsible disclosure, remediation, and retesting. The goal is not the bug itself; it is the reproducible method that finds it and the engineering that fixes it properly.

Methodology starts before the first request. In this lab scenario, a written authorization defines the rules of engagement: the target is a self-hosted staging deployment of a multi-tenant invoicing application (api.lab-internal.example, resolved to a private lab address), the test accounts are two synthetic users attacker@lab.test (User A) and victim@lab.test (User B) and testing is limited to passive observation and authenticated object-access attempts with those two accounts. Denial-of-service, data destruction, and testing against other tenants are explicitly out of scope.

· **Assessment objective.** Determine whether object identifiers accepted by the API can be manipulated to disclose or modify data belonging to User B while authenticated only as User A.

· **Success criteria.** A minimal, repeatable sequence of requests demonstrating unauthorized access, plus a defensible severity argument.

· **Evidence handling.** All requests and responses logged to a dedicated evidence directory with timestamps; no real personal data exists anywhere in the environment.

The OWASP Web Security Testing Guide treats authorization testing as its own phase precisely because it is so often skipped in a rush toward “deeper” bugs; this article follows that structure.

Reconnaissance here is quiet and mostly manual. I mapped the application the way a real user would: register the two accounts, walk every visible feature, and record which routes consume object identifiers. Invoicing apps are ideal IDOR territory because nearly every interesting action view invoice, download PDF, update status, share link is keyed by an enumerable ID.

The mapping exercise produced a shortlist of promising endpoints: GET /api/v2/invoices/{id} and GET /api/v2/invoices/{id}/pdf, both of which return complete invoice bodies; PATCH /api/v2/invoices/{id}/status, a state-changing operation; and an export endpoint that accepts a list of IDs. Anything keyed by a sequential integer and returned in full is a candidate; anything returning only the caller’s own aggregate data is not worth burning time on early.

Endpoint discovery continued from the two synthetic accounts side by side. I compared route tables, JavaScript bundles, and API responses between User A and User B sessions and flagged every route where the response shape suggested per-object rather than per-user data. The PDF download endpoint rose to the top: it took a raw invoice ID, returned the full rendered document in a single request, and appeared in the bundle with no additional client-side checks the classic precondition for a direct object reference.

Trust-boundary analysis is where an investigation becomes a hypothesis. The application’s architecture makes a quiet assumption: because the API gateway validates the JWT, the handlers downstream can “trust” the request. But the gateway authenticates; it does not authorize objects. The real question is where, if anywhere, the application tier verifies that invoice.owner\_id equals the caller’s identity. Comparing a known-owned object (User A requesting invoice #7701, which belongs to A) with a cross-user guess (User A requesting #8842, which belongs to B) tests that assumption with exactly one variable changed the ID.

The hypothesis, stated falsifiably: the invoice endpoints enforce authentication but not object-level authorization, so replacing an invoice ID with one belonging to another user returns that user’s data. A hypothesis you cannot disprove is not a hypothesis; this one is testable in a single request pair, which is what makes it valuable.

Validation was deliberately boring. From User A’s session:

GET /api/v2/invoices/7701 HTTP/1.1

Host: api.lab-internal.example

Authorization: Bearer \<synthetic JWT for attacker@lab.test (User A)>

HTTP/1.1 200 OK

{ “id”: 7701, “owner”: “user-a@lab.test”, “total”: “3,150.00”, “status”: “paid” }

Then, changing exactly one thing — the ID, to an invoice observed to belong to User B:

GET /api/v2/invoices/8842 HTTP/1.1

{ “id”: 8842, “owner”: “user-b@lab.test”, “total”: “12,400.00”, “status”: “overdue” }

The response is fully formed, belongs to a different account, and requires no elevated role. Repeating the exchange five times across five of User B’s invoice IDs (discovered only by sequential probing, itself a finding about ID predictability) produced the same result. That consistency is what elevates a hunch to a vulnerability: the behavior is deterministic, not accidental.

This is the conceptual heart of the finding. Authentication answers “who are you?” the JWT signature, the session, the login. Authorization answers “may you touch this specific object?” Those are different decisions requiring different evidence. A valid token for User A is evidence about User A’s identity; it contains no claim about invoice #8842. When the handler fetched the invoice by primary key and returned it without comparing invoice. owner\_id to the caller’s subject, it effectively delegated the authorization decision to the client because the only thing that ever chose the ID was the client. Server-side authorization is non-negotiable for the same reason server-side validation is: the client is an untrusted, attacker-controlled environment.

Not every suspicious response is a bug. A 200 on a cross-ID request can be legitimate when the object is intentionally shared, public, or when the ID is an unguessable capability rather than a sequential identifier. Distinguishing the cases requires reading the business intent: were invoices ever designed to be addressable across users? In this lab, no invoices were per-user with no sharing feature, so a 200 to the wrong owner was a genuine violation. The discipline is to ask “was this access supposed to be possible?” before writing it up, and to test the negative case confirming User A could not access User B’s data through the intended UI to rule out intended functionality.

Impact reasoning precedes score selection. What an attacker with a normal account gains here: confidentiality breach of arbitrary invoices across tenants (customer names, amounts, banking references in PDF attachments), with integrity exposure if the PATCH endpoint shares the flaw. There is no direct availability impact. Labeled clearly as an illustrative rating for this synthetic scenario a real finding must be scored against its real deployment context the vector set AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N computes to 6.5 (Medium) under CVSS v3.1. The assumptions behind that number matter more than the number: low privileges required because any registered account works, low complexity because the IDs are sequential, high confidentiality impact because complete financial documents are exposed. If cross-tenant reach were proven or the write path confirmed, scope and integrity would push the rating higher. FIRST’s CVSS specification is the authoritative reference for the metric definitions, and any real report should document its vector string explicitly.

Evidence quality decides whether a report gets fixed or debated. I archived: the two request/response pairs above with full headers, a minimal reproduction script that recreates the exchange from fresh tokens, affected endpoint inventory with parameter locations, timestamps, and the exact test accounts used. The disclosure itself follows the program’s channel and template, states impact in business terms, avoids any payload beyond proof, and requests a triage timeline. The professional habit that earns trust: demonstrate the smallest possible impact and offer to verify the fix privately before public discussion.

*The following illustrative report is written the way I would submit it to a program. All data is synthetic.*

Broken Object Level Authorization on invoice retrieval endpoints (/api/v2/invoices/{id}, /api/v2/invoices/{id}/pdf) hypothetical lab finding for demonstration purposes.

OWASP API Security Top 10 — API1:2023 Broken Object Level Authorization (BOLA/IDOR).

Authenticated users can retrieve arbitrary invoices including those owned by other accounts by supplying a sequential invoice ID, because object ownership is never verified server-side. The PDF download endpoint exhibits the same flaw.

Any registered account (attacker@lab.test used in lab). Tested only against the authorized staging deployment and synthetic accounts per the rules of engagement.

1\. Authenticate as User A (attacker@lab.test) and obtain a session JWT.

2\. Identify an invoice ID belonging to User B via sequential probing (e.g., 8842).

3\. Issue: GET /api/v2/invoices/8842 with User A’s Authorization header.

4\. Observe: HTTP 200 with the complete invoice body belonging to User B.

Expected: 403 Forbidden for any object the caller does not own. Actual: 200 OK with full object contents, deterministic across tested IDs.

Full confidentiality breach of arbitrary invoices (financial amounts, customer details, banking references via attached PDFs). The state-changing PATCH endpoint is suspected to share the root cause and should be reviewed under the same ticket.

CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N = 6.5 Medium (illustrative, synthetic scenario). Justification and assumptions documented in section 1.10.

Enforce object-level authorization in the application tier: resolve the object, compare its owner/tenant to the authenticated principal, deny with 403 on mismatch, and log the denial. See section 1.13 for reference code.

After the fix, repeat steps 1–4 and confirm 403 responses for all cross-user IDs, 200 for owned IDs, and that non-existent IDs return 404 without leaking existence via timing.

Root cause is a single missing decision in the handler. The vulnerable code (FastAPI, used as the illustrative backend for this lab) fetches by ID and returns authentication happened upstream, so the code never asks the authorization question:

\# VULNERABLE — object ID trusted from the client; ownership never checked

@app.get(“/api/v2/invoices/{invoice\_id}”)

def get\_invoice(invoice\_id: int, user: User = Depends(get\_current\_user)):

return db.query(Invoice).filter(Invoice.id == invoice\_id).one()

The fix moves the authorization decision onto the server and makes it fail closed — unknown object, mismatched owner, or cross-tenant ID all deny, and every denial is logged for monitoring:

\# SECURE — authorization enforced server-side, fail-closed

def get\_invoice\_secure(invoice\_id: int, user: User = Depends(get\_current\_user)):

invoice = db.get(Invoice, invoice\_id)

if invoice is None or invoice.owner\_id != user.id:

audit\_log(event=”object\_access\_denied”,

principal=user.id, object\_id=invoice\_id)

raise HTTPException(status\_code=403, detail=”Not authorized”)

return invoice

Regression testing is mechanical and repeatable: an automated suite re-runs the original attack sequence (expect 403), the legitimate access sequence (expect 200), and the not-found sequence (expect 404), plus equivalent cases on the PDF and PATCH endpoints. Ideally this becomes a CI check, because authorization regressions love to creep back in during refactors.

Common investigation mistakes I have learned to avoid: treating a login as proof of authorization; testing only one endpoint when a root cause is shared; over-scoring impact before confirming the write path; submitting noisy evidence instead of a minimal reproduction; and forgetting the negative test that rules out intended functionality.

**☐** Written authorization and scope reference for the target environment

**☐** Two synthetic accounts with a known object-ownership relationship between them

**☐** Minimal reproduction: one variable changed between the allowed and denied cases

**☐** Full request/response pairs with timestamps, archived verbatim

**☐** Negative test proving the intended UI does not expose the data

**☐** Business-impact statement in the program’s own terms

**☐** Fix denies cross-owner access with 403 (not 404-redirect to login, not 200)

**☐** Owned-object access still returns 200 with correct data

**☐** Non-existent IDs return 404 without existence-timing leaks

**☐** Shared root cause reviewed on every sibling endpoint (PDF, PATCH, export)

**☐** Denials are logged and monitored

**☐** Regression tests added to CI

Further Reading:

· [OWASP Web Security Testing Guide — https://owasp.org/www-project-web-security-testing-guide/](https://owasp.org/www-project-web-security-testing-guide/)

· [FIRST CVSS v3.1 Specification — https://www.first.org/cvss/](https://www.first.org/cvss/)
