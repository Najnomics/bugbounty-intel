# Azure AD Misconfiguration: The $40K Bing Takeover

- **Source URL:** https://masimshahzad.medium.com/azure-ad-misconfiguration-the-40k-bing-takeover-e36d49bacfa6
- **Fetched:** 2026-11-26
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14999)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Muhammad Asim Shahzad / Wed, 25 Nov 2026 05:01:08 GMT

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

Any Azure account on the planet could log in to the admin panel behind parts of Bing.com. In 2023, Wiz Research showed that a single Azure AD misconfiguration let outsiders edit live Bing search results and, through a script injection test, read a victim’s Office 365 data. Microsoft fixed it and paid $40,000.

***Disclaimer:*** *Educational and defensive use only. This was fixed in early 2023. Reproduction details are intentionally omitted.*

Azure App Services and Azure Functions offer login with a click. Mark the app multi-tenant and any Azure AD tenant can issue a valid token for it. The platform checks that the token is genuine. Deciding whether that tenant, or that user, belongs in your app is left to your code.

Wiz calls this shared-responsibility confusion, and its scans found about a quarter of multi-tenant apps exposed this way. One was a Microsoft content tool called Bing Trivia. The researchers signed in with a user from their own tenant and landed in its admin panel.

That panel fed real Bing content. They swapped one item in the carousel for a “best soundtracks” search, and the change appeared on Bing.com. A harmless script test also ran, meaning a malicious edit could have executed in every searcher’s browser.

During disclosure, Wiz showed that such a script could obtain an Office 365 token for the visitor, exposing mail, calendar, Teams chats and files. They tested only against their own account and reverted their edits.

Bing has a vast audience, so one poisoned popular result could reach a huge number of users. Wiz also found other exposed internal Microsoft apps, including an MSN newsletter panel and a file system it described as holding over 4 exabytes.

Microsoft said the apps were out of bounty scope but rewarded the AAD improvements the research prompted. Wiz notes AAD logs cannot show past abuse; app logs are the place to look.

**1. Single-tenant unless you truly need more.** It is a settings change.

**2. Authorize after you authenticate.** Check the tenant ID against an allowlist, then check the user is assigned to the app.

**3. Escape CMS output.** An admin tool that publishes to a public site is an XSS source.

\# Pseudocode: a valid token proves who signed it, not that they belong here

ALLOWED\_TENANTS = {"\<your-tenant-id>"}

def authorize(request):

claims = verify\_token(request.bearer) # signature, expiry, audience, issuer

if claims is None:

return deny(401)

if claims\["tid"\] not in ALLOWED\_TENANTS:

audit("foreign\_tenant\_login", claims\["tid"\], claims\["oid"\])

return deny(403, "tenant\_not\_allowed")

user = app\_users.find(tenant=claims\["tid"\], object\_id=claims\["oid"\])

if user is None or "cms\_editor" not in user.roles:

return deny(403, "not\_assigned")

return allow(user)

# Test: sign in with a brand-new account from an unrelated tenant -> 403, audit event written

Found by **Wiz Research** (Hillai Ben-Sasson, Shir Tamari, Nir Ohfeld, Sagi Tzadik and Ronen Shustin). Primary source: [BingBang: AAD misconfiguration led to Bing.com results manipulation and account takeover](https://www.wiz.io/blog/azure-active-directory-bing-misconfiguration) (Wiz blog by Hillai Ben-Sasson, 29 March 2023): root cause, Bing case, other apps, timeline and $40,000 bounty. Microsoft’s platform changes: [BleepingComputer, 30 March 2023](https://www.bleepingcomputer.com/news/security/bing-search-results-hijacked-via-misconfigured-microsoft-app/). Facts come from those sources; analysis and code are original.

Next breakdown: how one pasted session cookie handed a hacker a HackerOne analyst’s account. Follow @masimshahzad for daily bug bounty breakdowns.
