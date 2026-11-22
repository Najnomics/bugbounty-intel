# Null Byte Injection in Token Name Blocks Admin From Deleting It

- **Source URL:** https://medium.com/@islmhmdymhmed/null-byte-injection-in-token-name-blocks-admin-from-deleting-it-25a4c1c24069
- **Fetched from:** https://medium.com/feed/@islmhmdymhmed
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14995 (id 14995)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*Always think if the input you give to the app is going to be used in another request as a fetch process*

**● High** · **CVSS 7.1** · CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H

*Cairo, Egypt — June 5, 2026 · 3:00 PM GMT*

### About the Target

The target is a feature flag app with organizations, members and roles. You can create API tokens to communicate with the API with any role that is Reader+. It will be called target.com. A token can be deleted only by the token owner and the admin.

### Discovery

I was navigating the app normally, and luckily this was the first thing I tested. I tried to understand its flow. This is the request:

POST /api/v2/tokens HTTP/2

Host: target.com

Accept: application/json

Content-Type: application/json

{"name":"apitoken","role":"reader","defaultApiVersion":20240415,"serviceToken":false,"creationDate":0}

"name":"apitoken" decides the token name. To delete the token, you need to type the name again as a sort of confirmation. The idea here is to inject a hidden byte into the name, so when the admin types it again in the confirmation, it doesn't match the real name. I used a [null byte](https://community.owasp.org/attacks/Embedding_Null_Code) to embed it inside the text itself without it being visible.

*Another idea is to make the name itself empty. I tried this, but if you type spaces the confirmation button works, so it’s not a valid issue with real impact.*

### Exploitation

The payload is test\u0000hidden. The parser used in JS treats this as only test, ignoring the rest of the name.

POST /api/tokens HTTP/2

Host: target.com

Accept: application/json

Content-Type: application/json

{"name":"test\u0000hidden","role":"reader","defaultApiVersion":20240415,"serviceToken":false,"creationDate":0}

The token name looks totally normal here:

Trying to delete it by copying its name or typing it manually → the delete button won’t work. There is parsing confusion; even typing it as test\u0000hidden won't make it work.

### Chaining

1 undeletable token + an org can have 200 tokens max = 200 undeletable tokens → the whole token management feature is DoS’d and the admin can’t delete any of them!

#### They all can’t be deleted

### The Chain

1. A Reader creates an access token whose name contains a null byte (test\u0000hidden).
2. The null byte is stored in the token name, but only test is shown.
3. The admin types the visible name to confirm deletion.
4. The parser compares the typed name with the stored name → mismatch.
5. The delete button stays disabled → the token can’t be deleted.
6. Repeat up to the 200-token cap (or chain with a race condition) → the Access Tokens feature is blocked and unrecoverable.

### Impact

An attacker with a Reader role can chain this null byte injection to achieve a complete and unrecoverable Denial of Service on the organization’s token management system.
