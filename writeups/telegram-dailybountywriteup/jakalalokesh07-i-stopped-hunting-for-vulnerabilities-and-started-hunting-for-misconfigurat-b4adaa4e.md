# I Stopped Hunting for Vulnerabilities and Started Hunting for Misconfigurations

- **Source URL:** https://medium.com/@jakalalokesh07/i-stopped-hunting-for-vulnerabilities-and-started-hunting-for-misconfigurations-00b0aa6a5e65
- **Fetched from:** https://medium.com/@jakalalokesh07/i-stopped-hunting-for-vulnerabilities-and-started-hunting-for-misconfigurations-00b0aa6a5e65?source=rss-84fb2c27a498------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14907 (id 14907)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Jakkali Lokesh / Thu, 10 Sep 2026 20:59:02 GMT

When I first started learning bug bounty, I thought finding vulnerabilities meant discovering complicated exploits.

SQL injection.

XSS.

Authentication bypasses.

Remote code execution.

Those are obviously interesting, but there’s a problem with focusing only on them:

**You can miss a lot of real security issues.**

Over time, I started paying more attention to something much less exciting on the surface:

**misconfigurations.**

And honestly, that’s where things started getting interesting.

A misconfiguration is basically when a system is deployed or maintained in a way that creates unnecessary security exposure.

It doesn’t necessarily mean someone wrote vulnerable code.

Sometimes the code is perfectly fine.

The problem is how the infrastructure around it was configured.

For example:

Application

↓

Cloud service

↓

DNS

↓

Storage

↓

Permissions

One wrong configuration somewhere in that chain can create a security problem.

One of the clearest examples is a dangling DNS record.

Imagine:

old.example.com

↓

old-app.herokuapp.com

The company deletes the Heroku application but forgets the DNS record.

Now:

old.example.com

↓

Deleted resource

If someone else can claim that resource, the attacker may be able to control content served through the company’s subdomain.

That’s how a seemingly harmless DNS record can turn into a security issue.

When I get a new authorized target, I don’t immediately start throwing payloads at it.

I first try to understand the attack surface.

Look for:

dev.example.com

staging.example.com

old.example.com

api.example.com

assets.example.com

Old infrastructure is particularly interesting because it is more likely to contain forgotten resources.

Check where those domains actually point.

dig subdomain.example.com +short

I’m interested in CNAMEs and external services.

Look for publicly accessible buckets or accidentally exposed resources.

The important question isn’t simply:

*“Is this cloud storage?”*

It’s:

*“Who can access it, and what can they do?”*

Development and monitoring systems sometimes end up publicly accessible.

Examples include:

Jenkins

Grafana

Kibana

Argo CD

Kubernetes dashboards

Again, exposure doesn’t automatically mean vulnerability.

You need to determine whether authentication and authorization are properly implemented.

Companies depend on hundreds of external services.

That’s a huge attack surface.

A forgotten integration can sometimes be more interesting than the main application itself.

The biggest change for me was stopping the mindset of:

*“What payload should I try?”*

and replacing it with:

***“What is this system trusting that it shouldn’t?”***

That question leads to much better reconnaissance.

Look at:

DNS

Permissions

Cloud resources

Third-party services

Authentication

Access control

Deployment configuration

before trying to exploit anything.

Not every misconfiguration is a vulnerability.

A public endpoint isn’t automatically vulnerable.

A CNAME isn’t automatically a takeover.

A cloud bucket isn’t automatically exploitable.

A dashboard isn’t automatically a critical finding.

**Context matters.**

The job isn’t to find something that looks strange.

The job is to prove that the strange configuration creates a security impact.

You don’t always need a sophisticated exploit to find a security vulnerability.

Sometimes you just need to look at the things developers forgot about.

That’s why misconfigurations are now one of the first things I look for during reconnaissance.

**The boring infrastructure is often where the interesting bugs are hiding.**
