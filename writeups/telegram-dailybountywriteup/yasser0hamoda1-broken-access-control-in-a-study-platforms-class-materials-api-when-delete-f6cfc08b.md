# Broken Access Control in a Study Platform’s Class Materials API When “Delete My Own Stuff” Became “D

- **Source URL:** https://medium.com/@yasser0hamoda1/broken-access-control-in-a-study-platforms-class-materials-api-when-delete-my-own-stuff-became-d-89160bd2c583
- **Fetched from:** https://medium.com/@yasser0hamoda1/broken-access-control-in-a-study-platforms-class-materials-api-when-delete-my-own-stuff-became-d-89160bd2c583?source=rss-ddc9357992e5------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14949)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Yasser Hamoda / Thu, 15 Oct 2026 23:42:20 GMT

Not every bug needs a fancy GraphQL schema or a chained exploit to be fun. Sometimes the best ones are embarrassingly simple: a feature meant for teachers quietly forgets to check *which* teacher. Or, in this case, forgets to check that the person deleting something is a teacher at all.

This is the story of how a standard student account could reach into a virtual classroom and delete study materials that the teacher, not the student, had added. No admin panel required. Just a modified JSON body and a request that should never have succeeded.

(Target name withheld per responsible disclosure norms; I’ll just call it “**the Platform.**”)

Like most of my testing sessions, this one started with two browser profiles and a healthy amount of curiosity: a **Teacher** account and a **Student** account, both enrolled in the same class.

The Platform lets teachers curate a class’s study materials: sets, practice tests, the usual. Teachers can optionally flip a setting that lets class *members* (students) add and remove sets too, presumably so study groups can self-organize without pinging the teacher every five minutes.

Reasonable feature. Let’s see if **“remove sets”** actually means ***“remove sets you added”*** or just *“remove sets, full stop.”*

As the Teacher, I added an official study set to the class materials and noted its setId and the class’s classId. Then I switched to the Student account, joined the class, and, with an intercepting proxy running, removed a set I myself had added as a student, just to see what a “legitimate” delete request looked like.

DELETE /webapi/x.x/class-sets HTTP/2

Host: \[redacted\]

Cookie: \[session cookies — redacted\]

Content-Type: application/json

{"data":\[{"setId":\<STUDENT\_OWNED\_SET\_ID>,"classId":\<CLASS\_ID>}\]}

```
{"responses":[{"models":{"classSet":[{"setId":<ID>,
"isDeleted": true,...}]
}}]}
```
So far, completely normal for a student to clean up a set *they* added. Nothing wrong yet.

Here’s where I got nosy. I took the exact same request, same Student session, and simply swapped in the setId the **Teacher** had added for a set the student had no relationship to whatsoever.

DELETE /webapi/x.x/class-sets HTTP/2

Host: \[redacted\]

Cookie: \[session cookies — redacted\]

Content-Type: application/json

{"data":\[{"setId":\<TEACHER\_SET\_ID>,"classId":\<CLASS\_ID>}\]}

HTTP/2 200 OK

{

"responses": \[{

"models": {

"classSet": \[{

"setId": \<TEACHER\_SET\_ID>,

"classId": \<CLASS\_ID>,

"isDeleted": true,

"lastModified": 1780871388

}\]

}

}\]

}

200 OK. isDeleted: true. The server didn’t ask *“wait, did this student actually add this set?”,* it just checked that the student was *a* member of the class with delete rights, and happily nuked a resource that belonged to someone else entirely.

In other words: the endpoint validated **membership**, but never validated **ownership**. Classic confusion between “can this user delete sets in this class” and “can this user delete *this specific* set.”

I’ll be upfront: this isn’t an account takeover, and it doesn’t leak PII. It’s an **authorization gap at the object level:** the student can’t read the teacher’s private data, but they *can* unilaterally sever the link between the teacher’s set and the class. A few reasons that’s still worth a teacher’s (and a security team’s) attention:

**1. Check ownership, not just membership.**

Before honoring a delete, verify the requesting user is either the one who originally added that specific setId, or holds an admin/teacher role on the classId.

**2. Separate the permission model.**

“Can add/remove sets” and “can remove *any* set in this class” should be two different privilege levels, not one toggle.

**3. Test the inverse case.**

If the “allow members to manage sets” setting is disabled, does the endpoint still accept the request? If yes, that’s the clearest possible signal the check is missing entirely rather than just scoped wrong.

**4. Log and alert on cross-user deletions.**

A student deleting a set they didn’t add is a meaningfully different event than deleting their own, worth flagging even if it’s allowed by policy.

No stolen credentials, no admin panel, no exotic GraphQL trickery, just one JSON field that pointed somewhere it shouldn’t have been allowed to point. It’s a good reminder that **“the user has permission to perform this action”** and **“the user has permission to perform this action on this specific object”** are two different questions, and APIs that only ask the first one are an IDOR waiting to happen.

Until the next one… bye
