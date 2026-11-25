# How Claude Code Landed Me a $500 Supabase Bug Bounty

- **Source URL:** https://yaseenzubair.medium.com/how-claude-code-landed-me-a-500-supabase-bug-bounty-91f7455f6bfe
- **Fetched from:** https://yaseenzubair.medium.com/how-claude-code-landed-me-a-500-supabase-bug-bounty-91f7455f6bfe?source=rss-c9ce047e6154------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14911 (id 14911)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Yaseen Zubair / Mon, 14 Sep 2026 17:55:19 GMT

As more applications are being developed, I’ve noticed a clear rise in Supabase usage. More and more teams are using it to handle authentication, databases, storage, and APIs without building everything from scratch.

That speed is one of Supabase’s biggest strengths.

But if the underlying access controls are misunderstood, it can also introduce a serious security gap.

I was performing reconnaissance on a target that was using Supabase.

While continuing my manual testing, I spawned Claude Code and invoked the reconnaissance skill I usually use for this target. I left it running in the background and continued with my own testing.

After a while, I looked at the terminal again.

It had returned a finding with a heading along the lines of:

**PII Disclosure: More Than 1,200 Records Exposed**

Obviously, that caught my attention.

I manually verified the result, dug deeper into the root cause, and eventually received a **$500 bounty** for the finding.

The vulnerability was not in Supabase itself. It was caused by how the application had configured access to its Supabase database.

Supabase applications commonly include a public anonymous or publishable key in their frontend code.

That is expected behavior.

The key is used by the frontend to communicate with Supabase, and its presence in a JavaScript bundle is not a vulnerability by itself.

Security does not depend on keeping this key secret. It depends on correctly configured PostgreSQL privileges and Row Level Security policies.

In this case, the legacy anonymous JWT could be located in a JavaScript bundle using a command similar to this:

bash

curl -s "https://www.example.ai/\_next/static/chunks/example.js" \

| grep -oE 'eyJ\[A-Za-z0-9\_-\]+\.eyJ\[A-Za-z0-9\_-\]+\.\[A-Za-z0-9\_-\]+' \

| head -1

This returned the anonymous key embedded in the application:

\<REDACTED\_DEMO\_ANON\_KEY>

Again, finding this key was not the vulnerability.

The interesting question was:

What did the database allow this anonymous role to access?

Supabase exposes database tables through its PostgREST API, commonly under:

/rest/v1/

I used the anonymous key to check whether records containing an email address were accessible:

ANON\_KEY="\<REDACTED\_DEMO\_ANON\_KEY>"

SUPABASE\_URL="https://signin.example.ai"

curl -sI \

-H "apikey: $ANON\_KEY" \

-H "Authorization: Bearer $ANON\_KEY" \

-H "Prefer: count=exact" \

-H "Range: 0-0" \

"$SUPABASE\_URL/rest/v1/projects?lead\_email=not.is.null&select=id" \

| grep -i content-range

The response revealed that more than 1,200 matching records were accessible:

Content-Range: 0-0/12XX

At this point, the count showed the potential scale of the exposure, but I still needed to confirm what kind of information the records contained.

I requested only one record:

curl -s \

-H "apikey: $ANON\_KEY" \

-H "Authorization: Bearer $ANON\_KEY" \

"$SUPABASE\_URL/rest/v1/projects?select=lead\_name,lead\_email,id,private&limit=1"

The response contained a project lead’s name, email address, project ID, and privacy status:

\[

{

"lead\_name": "REDACTED",

"lead\_email": "REDACTED",

"id": "00000000-0000-0000-0000-000000000000",

"private": false

}

\]

One sample was enough to demonstrate the issue. There was no need to extract the remaining records.

The affected table used a policy that allowed the anonymous role to read projects where:

private = false

Conceptually, the policy looked similar to this:

create policy "Anonymous users can view public projects"

on public.projects

for select

to anon

using (private = false);

The developer may have intended to make public project information accessible.

The problem was that the allowed rows also contained sensitive fields such as:

lead\_name

lead\_email

The anonymous role had sufficiently broad SELECT privileges to request those columns directly through the REST API.

This is where an important distinction comes in:

RLS controls which rows a caller can access. It does not automatically decide which columns from those rows are safe to disclose.

The policy successfully filtered out projects marked as private, but the public rows still carried personal information that should not have been returned to anonymous users.

The frontend did not need to display these fields. An attacker could simply bypass the interface and request them directly from the Supabase API.

It would be easy to look at this issue and say:

“Just mark every project as private.”

That might stop this particular query, but it does not address the underlying design problem.

Some projects may legitimately need to remain public. The application should still prevent anonymous users from retrieving private lead information attached to those projects.

The correct remediation depends on the application’s requirements.

This was not a Supabase vulnerability.

The anonymous key behaved exactly as expected, and the REST API enforced the permissions it had been given.

The vulnerability existed because the database authorization model did not match the application’s intended data exposure.

When testing a Supabase application, don’t stop after confirming that authentication works through the interface.

The database had simply been instructed to disclose more than the application intended, and finding that gap resulted in a $500 bounty.

So, if Supabase appears during your next assessment, add RLS and database privileges to your testing checklist.
