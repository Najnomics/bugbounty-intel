# 5 Recon Mistakes That Waste Hours in Bug Bounty

- **Source URL:** https://medium.com/@Rakeshjoshi7/5-recon-mistakes-that-waste-hours-in-bug-bounty-7b530d2d19b8
- **Fetched from:** https://medium.com/@Rakeshjoshi7/5-recon-mistakes-that-waste-hours-in-bug-bounty-7b530d2d19b8?source=rss-a32f2a443db2------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14932 (id 14932)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Rakesh Joshi / Sun, 04 Oct 2026 06:22:45 GMT

Reconnaissance is the foundation of effective bug bounty hunting.

Before testing authentication, authorization, APIs, business logic, or other vulnerabilities, you need to understand the target’s attack surface.

But there is a common problem:

**Many hunters spend hours doing recon without actually improving their understanding of the target.**

More tools do not automatically mean better recon.

The goal is not to collect the largest number of subdomains, URLs, ports, or parameters.

The goal is to identify **interesting attack surfaces and prioritize them intelligently.**

Here are five common recon mistakes that waste hours — and how to fix them.

A common workflow looks like this:

Tool → Tool → Tool → Tool → Tool

A hunter runs multiple subdomain enumeration tools, URL collectors, scanners, DNS tools, port scanners, and crawlers — but never defines what they are actually looking for.

This creates enormous amounts of duplicate and low-value data.

Suppose you discover:

10,000 URLs

2,000 subdomains

15,000 parameters

That sounds impressive.

But if you don’t know which assets matter, you now have a **data-management problem rather than a vulnerability-discovery advantage**.

Start with a hypothesis.

Ask:

Then choose tools based on the question you’re trying to answer.

**Step 1 — Define scope**

Read the program’s policy carefully.

Identify:

**Step 2 — Build an initial asset inventory**

Start with known domains and applications.

**Step 3 — Expand the attack surface**

Look for:

**Step 4 — Remove duplicates**

Normalize domains, URLs, parameters, and endpoints.

**Step 5 — Prioritize**

Don’t treat every discovered asset equally.

Finding subdomains is only the beginning.

One of the biggest recon mistakes is treating this:

api.example.com

dev.example.com

blog.example.com

cdn.example.com

status.example.com

app.example.com

as one homogeneous list.

They aren’t.

Each hostname can represent a completely different attack surface.

Consider:

www.example.com

versus:

api.example.com

admin.example.com

The applications, authentication mechanisms, endpoints, and security assumptions may be completely different.

Create categories such as:

CategoryExamplesProductionapp, wwwAPIapi, graphqlAuthenticationauth, loginAdministrationadmin, manageDevelopmentdev, developmentTestingtest, qaDocumentationdocsInfrastructurestatus, monitoringStaticcdn, assets

The exact naming conventions vary by organization, so treat the hostname as a **lead**, not proof of its function.

**Step 1 — Enumerate candidate subdomains**

Collect potential hostnames from authorized sources.

**Step 2 — Resolve them**

Determine which hosts are actually active.

**Step 3 — Check HTTP services**

Identify which hosts expose web applications.

**Step 4 — Fingerprint the application**

Record useful information such as:

**Step 5 — Assign a priority**

For example:

Critical-interest:

admin

api

auth

High-interest:

app

portal

Medium-interest:

dev

test

Lower-interest:

cdn

static

status

This isn’t a vulnerability ranking. It’s simply a way to decide where to spend your testing time.

Another common mistake is immediately crawling every discovered URL.

The result can look like:

100,000 URLs

But quantity doesn’t equal quality.

Many URLs may be:

Instead of asking:

*“How many URLs can I find?”*

***“Which application functions can I interact with?”***

That’s a much more useful question.

**Step 1 — Start with the application’s primary entry points**

Understand:

**Step 2 — Map the application’s functionality**

Create a simple structure:

Application

│

├── Authentication

│ ├── Login

│ ├── Registration

│ └── Password recovery

│

├── User Account

│ ├── Profile

│ ├── Settings

│ └── Sessions

│

├── Data

│ ├── Search

│ ├── Export

│ └── Import

│

└── API

├── User endpoints

├── Data endpoints

└── Administrative endpoints

**Step 3 — Identify state-changing functionality**

Pay particular attention to functions that:

These areas often deserve deeper manual investigation.

**Step 4 — Deduplicate your results**

Normalize URLs and remove obvious duplicates before analysis.

Modern applications frequently move significant functionality into JavaScript.

A common mistake is focusing only on visible HTML pages.

JavaScript can reveal useful information about how an application works, including references to:

This does **not** mean that every string discovered in JavaScript is a vulnerability.

The value comes from understanding what those references tell you about the application’s architecture.

**Step 1 — Identify JavaScript assets**

Collect scripts loaded by the application’s pages.

**Step 2 — Separate first-party from third-party scripts**

Prioritize scripts belonging to the target application.

**Step 3 — Search for endpoint references**

Look for patterns such as:

/api/

graphql

/v1/

and other application-specific routes.

**Step 4 — Map discovered functionality**

Connect JavaScript references to the application inventory.

JS bundle

↓

API route

↓

Authentication requirement

↓

User functionality

↓

Potential testing area

**Step 5 — Validate manually**

Never assume that a discovered endpoint is active, sensitive, or vulnerable simply because it appears in JavaScript.

This is perhaps the biggest recon mistake.

You discover hundreds or thousands of assets.

Then you start testing them randomly.

That creates **recon fatigue**.

Instead of:

Asset → Test

Use:

Asset

↓

Classify

↓

Understand functionality

↓

Assess potential impact

↓

Prioritize

↓

Test

Imagine you discover:

www.example.com

blog.example.com

cdn.example.com

api.example.com

admin.example.com

dev.example.com

You could initially prioritize:

**Tier 1**

admin.example.com

api.example.com

**Tier 2**

app.example.com

auth.example.com

**Tier 3**

dev.example.com

test.example.com

**Tier 4**

blog.example.com

cdn.example.com

Again, this isn’t saying that Tier 4 assets cannot contain vulnerabilities.

It means your **limited research time should initially go toward assets with richer functionality or potentially higher impact**.

Putting everything together, a practical workflow looks like this:

Program Policy

↓

In-Scope Assets

↓

Testing Restrictions

↓

Rate Limits

Never skip this phase.

Known Domains

↓

Subdomains

↓

Applications

↓

APIs

↓

Supporting Services

The objective is visibility.

Remove:

You want a **clean dataset**, not a huge dataset.

For every meaningful asset, record:

Hostname

Application

Technology

Functionality

Authentication

API

Environment

Priority

A simple spreadsheet can be enough.

Understand what the application actually does.

Authentication

Authorization

User Management

Data Access

File Handling

Payments

Administration

APIs

Integrations

Use a simple scoring model:

Priority =

Business Impact

+

Attack Surface

+

Authentication Complexity

+

Interesting Functionality

You don’t need a complicated mathematical formula.

The purpose is simply to prevent random testing.

Now move from:

**Reconnaissance**

to:

**Hypothesis-driven security testing.**

Instead of saying:

*“I’ll scan everything.”*

Think:

*“This application has a multi-user API. I should understand how it distinguishes users and controls access to objects.”*

That shift in thinking is where recon becomes valuable.

**Recon isn’t about collecting the most data.**

It’s about collecting the **right data** and turning it into actionable hypotheses.

A beginner might say:

*“I found 50,000 URLs.”*

An experienced hunter asks:

*“Which five endpoints expose the most interesting functionality?”*

That’s the difference.

Before moving from recon into deeper testing, ask:

The biggest recon mistake isn’t using the wrong tool.

It’s **using tools without a strategy**.

Effective bug bounty reconnaissance should progressively reduce uncertainty:

Unknown Attack Surface

↓

Asset Discovery

↓

Validation

↓

Classification

↓

Application Mapping

↓

Prioritization

↓

Security Testing

The objective isn’t to become the hunter with the **largest recon output**.

It’s to become the hunter who can look at a large attack surface and quickly identify **where the interesting security questions are**.

**Better recon → better hypotheses → better testing → better findings.**
