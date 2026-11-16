# How a Hidden GraphQL Endpoint Led Me to a Critical SQL Injection Worth €2,500

- **Source URL:** https://medium.com/@0x0sadat/how-a-hidden-graphql-endpoint-led-me-to-a-critical-sql-injection-worth-2-500-a2e39521944b?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@0x0sadat
- **Fetched:** 2026-11-16
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14707)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
A simple directory fuzzing session uncovered a hidden GraphQL endpoint. A harmless-looking search bar eventually turned into a confirmed Critical (P1) SQL Injection with backend database enumeration. This is the story of how it happened.

### Introduction

Every vulnerability starts with curiosity.

Sometimes you spend hours testing an application and find nothing.

Sometimes a single hidden endpoint changes everything.

This is the story of how I discovered a **Critical Time-Based Blind SQL Injection** in a GraphQL endpoint during a routine assessment. The finding was independently validated by the security team, classified as **P1 (Critical)**, and rewarded with **€2,500** because the vulnerable asset was hosted in a development environment rather than production.

What follows is the exact methodology I used, how I verified the issue, my conversations with the security team, and the lessons I learned throughout the disclosure process.

### The Beginning

While browsing the target application, I landed on:

https://dev.sp.redicted.net/

Instead of displaying an application, it immediately redirected me to:

https://dev.sp.redicted.net/de/block

At first glance, it looked like there wasn’t much to test.

Many researchers would probably move on.

I didn’t.

Whenever I encounter an unfamiliar application, one of my first steps is to enumerate hidden directories and endpoints.

So I started fuzzing the application.

After a while, one interesting endpoint appeared.

/graphql

Unlike every other path I had tested, this endpoint returned **HTTP 200 OK**.

That immediately caught my attention.

Opening the endpoint in the browser revealed something unexpected — a simple search interface.

It looked completely harmless.

But hidden behind that search box was an entire GraphQL backend.

### The Search Box That Started Everything

Whenever I find an input field, I begin with basic payloads.

Not because I expect them to work…

…but because applications often reveal unexpected behavior.

I started testing the search field with different payloads commonly used for input validation.

While experimenting, I entered:

'--++

Instead of behaving normally, the application responded with an SQL-related error.

That was the moment I knew this wasn’t just another search feature.

Somewhere behind the application, user input appeared to be reaching the database.

Now I needed to prove it.

### Confirming the SQL Injection

Error messages alone aren’t enough.

Applications sometimes expose misleading errors.

To verify whether the backend was actually executing SQL, I switched to a time-based payload.

I injected a PostgreSQL delay function using **PG\_SLEEP(10)**.

Immediately I noticed something interesting.

The application became unresponsive for approximately ten seconds before returning a response.

I repeated the test several times.

Every request containing the delay payload produced nearly the same timing difference.

This strongly suggested that the backend was executing my injected SQL.

The original report also documented consistent response delays when using PG\_SLEEP(), confirming server-side SQL execution rather than ordinary network latency.

### Automating the Verification

Once I had manually confirmed the behavior, I wanted to verify whether the vulnerability could be exploited safely.

I saved the intercepted HTTP request as:

request.txt

Then I replayed that request using an automated SQL injection testing tool against the vulnerable searchText parameter.

Within a short time, the tool confirmed:

- Time-Based Blind SQL Injection
- PostgreSQL (Greenplum) backend
- Successful schema enumeration
- Successful table enumeration

It also identified dozens of database tables belonging to the backend application.

### The security team later asked me to demonstrate that I could retrieve backend information beyond simple timing differences, and I safely provided schema and table enumeration without extracting sensitive records.

### Why I Stopped There

At this point I had enough evidence.

I could have continued dumping tables.

I could have extracted user information.

I could have retrieved application secrets.

I intentionally chose not to.

Responsible disclosure isn’t about collecting as much data as possible.

It’s about proving impact while minimizing risk.

I limited my testing to metadata enumeration only.

No user records were accessed.

No sensitive information was extracted.

The report explicitly notes that further exploitation was intentionally limited to avoid service disruption and unnecessary exposure of data.

### Reporting the Vulnerability

I documented everything carefully:

- The vulnerable endpoint
- The affected GraphQL parameter
- Manual proof of execution
- Timing analysis
- Database confirmation
- Root cause
- Remediation recommendations

A few days later, I received a response from the security team.

They had successfully reproduced the vulnerability.

However, before making a final decision, they asked one additional question.

***Can you show that you are able to retrieve information from the backend database?***

This was an important step.

Rather than simply trusting the timing delay, they wanted evidence that the vulnerability could actually retrieve database information.

I responded with safe database enumeration results that confirmed:

- Backend DBMS
- Current schema
- Multiple database tables

### without extracting sensitive content.

### The Confirmation

A few days later, the email I had been waiting for finally arrived.

The security team confirmed:

- The vulnerability was valid.
- Their specialists reproduced the issue.
- The issue would be fixed.
- I would receive a **€2,500** bounty.

Reading that email was incredibly satisfying after spending hours investigating, validating, documenting, and communicating the finding.

### The Reward Discussion

One detail immediately caught my attention.

The issue had clearly been classified as a **P1 (Critical)** vulnerability.

However, the reward was lower than the published P1 amount.

Instead of making assumptions, I simply asked.

*If this is a valid P1, why is the reward €2,500?*

The response was straightforward.

The team explained that the vulnerability **was indeed classified as P1**, but because it existed in a **development environment**, the bounty was reduced.

### Requesting a Re-evaluation

After reviewing their explanation, I respectfully requested a re-evaluation.

I explained that:

- The vulnerability had confirmed Critical impact.
- Backend schemas and tables could be enumerated.
- Development environments often closely mirror production.
- I had intentionally avoided extracting any sensitive data.

I wasn’t arguing about the technical severity.

I wanted to understand how the reward policy was being applied.

### The Final Decision

The security team reviewed the report again.

Their response was detailed.

They confirmed every point:

- Yes, it is a **P1 SQL Injection**.
- Yes, backend structures were accessible.
- Yes, development environments often indicate production risk.
- Yes, my handling of the vulnerability complied with their rules of engagement.

However, they also confirmed their final policy:

***P1 + Development Environment = €2,500***

That became the final reward decision.

Although it wasn’t the maximum payout for a P1 issue, I appreciated the transparency and professionalism throughout the process.

### Timeline

**January 31, 2026**

- Vulnerability reported with technical details and proof of concept.

**February 2**

- Security team requested proof of backend data retrieval.

**February 5**

- I demonstrated successful schema and table enumeration while intentionally avoiding sensitive data extraction.
**February 6**
- The security team confirmed they reproduced the issue and began impact assessment.

**February 13**

- The report was accepted and a €2,500 reward was announced.

**February 16**

- The team confirmed the issue was classified as P1 but explained that the reward was reduced because the affected asset was a development environment.

**February 17**

- After my re-evaluation request, the team reaffirmed the classification and reward policy, confirming the final bounty.

### Lessons Learned

This experience reinforced several important lessons:

- Never ignore development environments.
- Hidden GraphQL endpoints can expose powerful attack surfaces.
- A simple search field can sometimes become your highest-severity finding.
- Manual verification should always come before automation.
- Responsible disclosure means proving impact — not collecting data.
- Clear and professional communication with security teams is just as important as technical skill.

### Closing Thoughts

Looking back, this vulnerability wasn’t discovered through luck.

It started with following a redirect.

Then exploring hidden endpoints.

Then questioning why a simple search bar behaved strangely.

One small observation eventually uncovered a **Critical SQL Injection**, resulted in backend database enumeration, and concluded with a successful responsible disclosure.

Sometimes the biggest vulnerabilities begin with the smallest clues.

If there’s one lesson I hope readers take away from this story, it’s this:

**Never stop investigating just because an application looks simple. The most interesting findings are often hiding behind the most ordinary pages.**

**Author**

**MD SADAT TAMZIT (0x0SADAT)**

Web Security Researcher | Bug Bounty Hunter
