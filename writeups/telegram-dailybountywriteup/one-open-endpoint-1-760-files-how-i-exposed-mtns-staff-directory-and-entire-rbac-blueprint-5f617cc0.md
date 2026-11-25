# One Open Endpoint, 1,760 Files

- **Source URL:** https://nowisar.medium.com/one-open-endpoint-1-760-files-how-i-exposed-mtns-staff-directory-and-entire-rbac-blueprint-2ee0e5c134a0
- **Fetched from:** https://nowisar.medium.com/one-open-endpoint-1-760-files-how-i-exposed-mtns-staff-directory-and-entire-rbac-blueprint-2ee0e5c134a0?source=rss-57e4c76743c7------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14892 (id 14892)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Mohamed Nowisar  / Mon, 31 Aug 2026 15:24:25 GMT

Hello everyone! I’m **Nowisar**, and today I’m thrilled to share one of my recent findings against MTN Group. It was an incredible experience hunting through such a massive infrastructure and successfully uncovering a high-impact vulnerability chain. A production Directus CMS instance left its /files REST API open to the public role — no auth, no token, nothing. That alone let anyone list every asset on the platform, and digging through that list turned up admin-exported schema/config dumps sitting right there as downloadable files: a full internal staff directory, the entire RBAC permission matrix, internal hostnames, and a (since-rotated) API token baked into an automation flow. The same misconfiguration was reproducible across three separate production instances.

Now, let’s start.

I was mapping the attack surface of a set of digital-experience platforms built on **Directus**, an open-source headless CMS. Directus exposes a REST/GraphQL API for every collection it manages, and access to each collection is governed by role-based permissions — including a special **“Public” role** that defines what an unauthenticated visitor can see.

Misconfigured Public role permissions are a known Directus footgun: if an admin accidentally grants read on a system collection like directus\_files to Public, anyone on the internet inherits that access. That's exactly what I went looking for.

The first thing I probe on any Directus target is the system collections — /users, /roles, /files, /permissions — just to see what the Public role can touch. Most of the time these are locked down. On this target, /files wasn't:

curl -s "https://\<redacted-subdomain>.mtn.com/files?limit=-1&fields=id,filename\_download,type,folder,uploaded\_on"

Response: **HTTP 200**, a JSON array of **1,760 file records** — no cookie, no token, no header. Every asset ever uploaded to that instance’s media library was fully enumerable: filenames, folder structure, upload timestamps, internal IDs.

My first instinct was to hit /assets/ directly to see if the raw asset store was also browsable:

curl -s "https://\<redacted-subdomain>.mtn.com/assets/"

That came back as:

`{"errors":[{"message":"Route /assets/ doesn't exist.","extensions":{"path":"/assets/","code":"ROUTE_NOT_FOUND"}}]}`
No directory listing — expected, since /assets/ isn't a route by itself in Directus, it's a prefix that needs a specific file id/UUID appended. So instead of trying to browse blindly, I went back to the /files enumeration output, picked out the id (UUID) of individual records, and requested each one directly:

curl -s "https://\<redacted-subdomain>.mtn.com/assets/\<file-uuid>"

That worked immediately, and it turned an “I can see filenames” bug into “I can download every file in the CMS.” Most of the 1,760 assets were unremarkable — campaign images, marketing collateral. But scrolling through the filenames, a batch stood out: users.json, roles.json, permissions.json, flows.json, operations.json, settings.json, uploaded from the CMS back office across at least 8 separate export sessions on the same day. These are the exact filenames Directus produces when an admin uses its **schema/data export** feature — meaning someone had exported sensitive internal configuration *through* the CMS, and it landed in the same publicly-readable asset store as the marketing images.

**users.json — Internal staff directory (87 records).** Each record included full name, corporate email address (@mtn.com / @ayoba.me), SSO provider (mostly Microsoft), role assignment, account status, and the last admin page the user had visited. Example structure (values genericized):

```
{
  "id": "UUID",
  "status": "active",
  "first_name": "[REDACTED]",
  "last_name": "[REDACTED]",
  "email": "[REDACTED]@mtn.com",
  "password": null,
  "token": null,
  "last_access": "2026-07-27T12:17:32.874Z",
  "last_page": "/content/documents?bookmark=XXXX",
  "external_identifier": "[REDACTED]@mtn.com",
  "tfa_secret": null,
  "auth_data": null,
  "provider": "XXXXX",
  "role": "UUID",
  "language": null,
  "email_notifications": true
}
```
The Directus **Public role** was granted read access to the directus\_files system collection (and, by extension, the /assets/:id download endpoint, which only checks that the referenced file record is readable). This is a classic "default-open" trap: Directus doesn't expose system collections to Public by default, so this had to be an explicit misconfiguration — likely made at some point to allow public access to specific media (e.g., website images) without realizing it grants blanket access to *every* file ever uploaded, including internal admin exports.

If you enjoyed this, follow for more writeups like this:

#BugBounty #InfoSec #CyberSecurity #PenetrationTesting #Directus #APISecurity #VulnerabilityDisclosure #HackerOne
