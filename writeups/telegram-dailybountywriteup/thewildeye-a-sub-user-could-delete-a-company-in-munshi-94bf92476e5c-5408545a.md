# A Sub-User Could Delete a Company in Munshi

- **Source URL:** https://medium.com/@TheWildEye/a-sub-user-could-delete-a-company-in-munshi-94bf92476e5c
- **Fetched from:** https://medium.com/@TheWildEye/a-sub-user-could-delete-a-company-in-munshi-94bf92476e5c?source=rss-388cd0542955------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14965 (id 14965)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** TheWildEye / Fri, 30 Oct 2026 16:22:52 GMT

*An authorization gap allowed an invited user to delete a company they could access, even without owner approval or an explicit delete permission.*

During a security assessment of Munshi, I identified an authorization issue in the company deletion workflow. An authenticated invited user who had access to a company could delete that company without being its owner or having a specific permission to perform the deletion.

The issue was not an authentication bypass. The user was signed in and had legitimate access to the company. The problem was that the application treated access to a company as sufficient authority to carry out a destructive action against it.

That distinction matters. Being invited into a company should allow a user to perform the tasks granted to their role. It should not automatically give them the ability to remove the company itself.

The affected endpoint was:

DELETE /api/companies/{company\_id}

The deletion workflow checked whether the authenticated user could access the requested company. It did not separately establish that the user was the company owner or had been granted permission to delete it.

The application already had a dedicated company\_delete permission in its role system, but the deletion workflow did not enforce that permission before proceeding. In practice, company membership became the only meaningful gate for a much more sensitive operation.

This meant an invited sub-user could reach the deletion action through their own authenticated session, even though company deletion should have remained restricted to the owner or a user explicitly trusted with that responsibility.

To validate the issue, the deletion request was made from an authenticated session that had access to the company but did not have owner-level authority.

The server returned HTTP 200 with {"success": true}. A subsequent request to retrieve the same company returned 404, indicating that the company was no longer available through the application.

**Figure 1: Redacted request and response from the authenticated company-deletion test. The request method, endpoint path, success response, and follow-up not-found result are retained.**

The result was also checked against the database state. The report records that the tested staging environment used a soft-delete marker, rather than immediately removing the company document. That confirms the application had changed the company’s state even though the request came from a user who should not have been allowed to delete it.

**Figure 2: Database record showing the deletion marker. Company and tenant identifiers are redacted.**

A company record is not an isolated object. It sits at the center of a tenant’s business data and can be associated with invoices, Tally configurations, chat sessions, embeddings, and other operational records.

Deleting the company without validating those dependencies can leave related resources in an inconsistent state or create orphaned references. The assessment identified the absence of dependency validation as an additional risk in the deletion flow. These are potential downstream effects; the report does not claim that every linked record was orphaned during the test.

There was also a deletion-model consistency concern. The assessment confirmed that the deletion functionality performed a hard delete rather than a soft delete, permanently removing the targeted record instead of retaining it in a recoverable state. This could result in irreversible data loss and impact data integrity.

The user did not need to steal another account or bypass the sign-in process. They were an invited user with valid access to the company.

The failure happened when the application decided what that access allowed them to do. A check that answers “Can this user access the company?” is not enough for an operation that removes the company. The application must also decide whether that user has authority to perform the deletion.

This is the core of the finding: the access boundary existed, but the required authorization boundary for a destructive action did not.

Company deletion should be limited to the owner or to users who have been explicitly granted deletion authority. The same decision needs to be applied consistently wherever a company can be removed, and the application should handle linked business records in a controlled way. Staging and repository behaviour should also agree on whether deletion is recoverable or permanent.

**Vulnerability:** Missing Authorization in Company Deletion

**Product:** Munshi by Petpooja

**Affected endpoint:** DELETE /api/companies/{company\_id}

**Primary CWE:** CWE-862, Missing Authorization

**Severity:** High, as classified in the assessment report

**Date:** 7 July 2026

**Remediation Status:** Fixed

**CVE ID:** *To be assigned*

This finding started with a user who was legitimately invited into a company. The application correctly recognized that the user could access the company, but it failed to distinguish that access from permission to delete it.

A company-level delete operation can affect far more than a single database record. It can interrupt business operations and put invoices, integrations, conversations, and other associated data at risk. Destructive actions need a stronger authorization boundary than ordinary access to the same resource.

**Researcher:** Vyom Nagpal
