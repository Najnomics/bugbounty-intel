# IDOR Explained

- **Source URL:** https://medium.com/@vigneshkumaroffsec/idor-explained-the-types-where-it-hides-and-how-to-find-it-4adfe01b9023
- **Fetched from:** https://medium.com/feed/@vigneshkumaroffsec
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14995 (id 14995)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
*IDOR is consistently one of the most reported — and best paid — web vulnerabilities, because it’s simple, everywhere, and easy to miss. Here’s what it is, its types, the exact places it hides, and the method that finds it. Authorized testing only.*

By Vignesh Kumar | Security Researcher

Here’s a bug that pays bounties every single day, needs no exotic skill, and lives in almost every application: **IDOR**, Insecure Direct Object Reference. You change a number in a URL from 1043 to 1044 and you're reading someone else's invoice. That's it. The simplicity is exactly why it's everywhere and why it keeps topping bug bounty reports.

This guide covers what IDOR actually is, its types, every place it tends to hide, and the repeatable method to find it. Everything here is for applications **you own or are explicitly authorized to test** — with accounts you control.

### What IDOR actually is

An application constantly refers to objects — an invoice, a message, a profile, a file — by some **reference**: an ID, a filename, a token. An IDOR exists when the app lets you **supply that reference and returns the object without checking that you’re allowed to access it.**

The critical word is *authorization*. The app authenticated you fine — you’re logged in. But it never asked the second question: *is this object yours?* IDOR is the gap between “who you are” and “what you’re allowed to touch.” (In API terms this is Broken Object Level Authorization, OWASP API #1.) The reference being “direct” — a database ID you can see and change — is what makes it trivial to exploit.

### The types of IDOR

IDOR isn’t one shape. Classifying it helps you test for all of it.

**By what the reference looks like:**

- **Sequential / numeric IDs** — ?id=1044. The easy case: increment and decrement.
- **UUIDs / GUIDs** — ?id=3fa85f64-.... Harder to guess, but *guessability is not a control* — if the app leaks the UUID anywhere (in a list, a share link, an email, another response), you can still swap it.
- **Encoded or hashed IDs** — base64, hex, or a hash of the real ID. Decode it, change it, re-encode it. Obfuscation is not authorization.
- **Filenames / paths** — /download?file=invoice\_1043.pdf. Often overlaps with path traversal.
- **Composite / predictable tokens** — user-2024-00042. Predictable patterns are enumerable.

**By what access it grants:**

- **Horizontal IDOR** — accessing another user’s data *at the same privilege level* (your fellow user’s orders). The most common.
- **Vertical IDOR** — reaching higher-privilege objects or actions (a regular user hitting an admin object). Overlaps with Broken Function Level Authorization.

**By the operation:**

- **Read IDOR** — view another object (GET). The one people test first.
- **Write IDOR** — *modify or delete* another object (PUT/PATCH/DELETE/POST). Often higher impact and frequently missed, because testers stop at reads.
- **Create IDOR** — create an object *as* or *for* another user by supplying their ID.

**By how it behaves:**

- **Direct IDOR** — the object comes straight back in the response.
- **Blind IDOR** — nothing obvious returns, but the action still happened (you changed someone’s setting, triggered their password reset, deleted their item). Confirm it via side effects, not the response body.
- **Second-order / stored IDOR** — the ID you tampered with is stored and used later in a different flow, where the missing check bites.

### Where IDOR hides

Every place the client hands the server an object reference is a candidate. Check them all:

- **URL query parameters** — ?id=, ?user\_id=, ?account=, ?invoice=, ?order=.
- **URL path segments** — /users/123, /orders/456/items, /api/v1/documents/789.
- **Request body fields** — form fields and **JSON keys**: {"user\_id": 123}, {"account": "...", "to": "..."}. Body IDOR is heavily under-tested.
- **Headers and cookies** — custom headers like X-User-Id, or an identifier tucked in a cookie the app trusts.
- **API endpoints** — REST resources by ID, and **GraphQL** node(id:) lookups and mutations, where a single endpoint exposes many objects.
- **File and document access** — /download, /invoice/123.pdf, /export?report=, attachment URLs.
- **Hidden form fields and client-side state** — IDs the UI sends but never shows.
- **Secondary flows** — sharing, exporting, notifications, webhooks, “resend”, “print” — the forgotten endpoints where the main authorization check often wasn’t copied.
- **Mobile app traffic** — mobile APIs frequently trust the client more than the web app does; proxy the app and look.

### How to find it

The method is simple and reliable. The whole trick is **two accounts**.

**1. Create two accounts you control — A and B.** Put distinct, identifiable data in each (orders, messages, a profile). This is the entire foundation: A is your attacker, B is the victim you’re allowed to victimize because it’s yours.

**2. Map the object references.** Browse the app as each account through an intercepting proxy (Burp, or similar). Note every request that carries an object reference — IDs in URLs, paths, bodies, headers. Record B’s object IDs (B’s order id, B’s message id).

**3. Swap, using A’s session.** Take a request that returns *A’s* object and replace the ID with *B’s*, keeping **A’s authentication**. Send it.

- If you get **B’s data back → horizontal IDOR.**
- If it’s refused (403/404/empty) → that object is protected. Move to the next.

\# As user A (A's cookie/token), requesting B's object:

GET /api/orders/1044 -> returns B's order? = IDOR

returns 403/404? = protected

**4. Test every operation, not just reads.** Re-run the swap with PUT, PATCH, DELETE, POST. Can A *edit* or *delete* B's object? Write IDOR is where the serious impact (and bounty) usually is, and it's the step people skip.

**5. Defeat obfuscation.** If IDs are encoded, decode (base64/hex), change the value, re-encode, and send. If they’re UUIDs, hunt for where B’s UUID leaks — a list endpoint, a share link, an error message — then swap it. Unguessable ≠ unauthorized.

**6. Confirm blind cases by side effect.** If a tampered request returns nothing useful but should have acted on B’s object, check B’s account: did the setting change, the item disappear, the email send? The proof is the effect, not the response.

**7. Try the bypass variations** when a check seems present:

- Change the HTTP method (GET blocked but POST allowed).
- Switch content type (form vs JSON) or wrap the ID in an array (id\[\]=1044).
- Add a second parameter (parameter pollution): ?id=1043&id=1044.
- Supply both your ID and the victim’s and see which one wins.

**8. Report it cleanly.** The affected request, the two-account reproduction, the exact IDs, what A could read or change about B, and the fix. Only ever with accounts and targets you’re authorized to use.

### The fix

The only real fix is **server-side object-level authorization on every request** — verify the authenticated user owns or may access the specific object, for the specific action.

\# Vulnerable: fetch by id alone — any valid id works (IDOR)

order = db.get\_order(order\_id)

# Fixed: the authenticated user is part of the lookup. Not a convenience —

# a security control. Another user's order simply isn't found.

order = db.get\_order(order\_id, owner\_id=current\_user.id)

if order is None:

raise NotFound() # same response whether it's missing or not yours

Supporting controls (defense in depth, **not** substitutes):

- **Centralize the authorization check** so it isn’t re-implemented, differently, per endpoint — and copy it into every secondary flow.
- **Scope database queries to the caller** rather than filtering after fetch.
- **Use unguessable references (UUIDs)** to raise the bar — but never rely on them as the control.
- **Default to deny**, and return the *same* response for “doesn’t exist” and “not yours” so you don’t leak which IDs are valid.

### Common Mistakes to Avoid

- Testing against accounts or targets you aren’t authorized to use.
- Only testing read (GET) IDOR and stopping — missing the higher-impact write/delete cases.
- Assuming UUIDs or encoded IDs are safe. Guessability is not authorization.
- Testing only URL parameters, ignoring JSON bodies, headers, and GraphQL.
- Forgetting secondary flows (export, share, resend) where the check wasn’t copied.
- Missing blind IDOR because you only looked at the response, not the side effect.
- On the defense side: “hiding” the ID in the UI instead of checking ownership server-side.
- Returning different responses for “not found” vs “forbidden,” leaking valid IDs.

### A Quick IDOR Checklist

- You’re testing with your own accounts on an authorized target.
- Two accounts (A and B) with distinct, identifiable data exist.
- Every object reference is mapped — URL params, paths, JSON bodies, headers, cookies, GraphQL.
- Each reference tested by swapping B’s ID into A’s authenticated request.
- All operations tested: read **and** write/delete/create — not just GET.
- Encoded/UUID IDs decoded, swapped, or leaked-and-swapped.
- Blind cases confirmed by checking B’s account for the side effect.
- Bypass variants tried: method change, content-type, array wrap, parameter pollution.
- On fix: every endpoint scopes the lookup to the authenticated user and fails closed.

### Final Thoughts

IDOR endures because the happy path works perfectly — the app returns the right object to the right user every time a developer tests it as themselves. The bug only appears when *someone else’s* ID goes into *your* session, and nobody wrote the check that catches it. That’s also why it’s so findable: you don’t need a clever payload, you need a second account and the discipline to try every reference, every operation, every flow.

If you’re starting in bug bounty or testing your own app, do this one thing: make two accounts, and try to read and change one account’s data while logged in as the other. Whatever comes back tells you whether the app knows the difference between *authenticated* and *authorized* — which is the whole bug.

### About me

I’m Vignesh Kumar, a security researcher working across application security, DevSecOps, cloud security, and vulnerability research.

I share practical findings from security assessments and responsible disclosures to help improve the security of real-world systems.

*The techniques in this article are described for defending and testing systems you own or are authorized to assess.*
