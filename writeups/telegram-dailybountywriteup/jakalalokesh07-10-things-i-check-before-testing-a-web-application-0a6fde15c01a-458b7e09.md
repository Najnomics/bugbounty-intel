# 10 Things I Check Before Testing a Web Application

- **Source URL:** https://medium.com/@jakalalokesh07/10-things-i-check-before-testing-a-web-application-0a6fde15c01a
- **Fetched from:** https://medium.com/@jakalalokesh07/10-things-i-check-before-testing-a-web-application-0a6fde15c01a?source=rss-84fb2c27a498------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14910 (id 14910)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Jakkali Lokesh / Sun, 13 Sep 2026 20:11:14 GMT

When I get access to a new web application for security testing, I don’t immediately start testing random payloads.

That’s usually inefficient.

Before testing individual vulnerabilities, I want to understand what I’m actually dealing with.

So I built a simple checklist for myself.

These are the first things I look at.

The main domain is rarely the entire attack surface.

Look for things like:

api.example.com

dev.example.com

staging.example.com

admin.example.com

old.example.com

Different subdomains often run completely different applications.

After finding subdomains, I want to know where they’re pointing.

For example:

dig example.com

dig subdomain.example.com +short

I’m particularly interested in external CNAMEs.

Why?

Because third-party infrastructure can introduce completely different security risks.

I want to know what the application is built with.

Nginx

Apache

Node.js

Java

PHP

React

Next.js

WordPress

Django

Technology fingerprinting helps me understand what attack surfaces might exist.

But I don’t blindly attack based on the technology version.

Modern applications often expose a lot of information through JavaScript.

I look for:

API endpoints

Internal routes

Feature flags

Environment references

Third-party services

Interesting parameters

Sometimes the frontend tells you more about the backend than the homepage does.

If the application has APIs, I want to understand them.

/api/users

/api/profile

/api/orders

/api/admin

Then I think about authorization.

The important question is:

***Can one user access another user’s resources?***

That’s where many serious bugs live.

I check how login works.

Questions I ask:

I’m not trying to break accounts.

I’m trying to understand the authentication architecture.

This is one of my biggest areas of interest.

Suppose I have:

/user/123

Can I access:

/user/124

when I shouldn’t?

That’s the basic idea behind many IDOR/BOLA-style vulnerabilities.

I look for external infrastructure:

AWS

Azure

GCP

CloudFront

S3

CDNs

Serverless services

The goal isn’t simply to find cloud resources.

It’s to understand whether the application’s cloud configuration creates unintended access.

Modern applications rarely operate alone.

They integrate with:

Payment providers

Email platforms

Analytics

Cloud hosting

Marketing platforms

CI/CD systems

Every integration creates another trust relationship.

And broken trust relationships can create vulnerabilities.

This is probably one of the most underrated areas.

Look for:

old.example.com

legacy.example.com

beta.example.com

staging.example.com

dev.example.com

Old infrastructure tends to receive less attention.

That’s exactly why it’s worth checking.

My reconnaissance process now looks something like:

Subdomains

↓

DNS

↓

Technologies

↓

JavaScript

↓

APIs

↓

Authentication

↓

Authorization

↓

Cloud

↓

Third-party services

↓

Old infrastructure

Only after understanding these pieces do I start deeper vulnerability testing.

Good reconnaissance isn’t about collecting the biggest list of tools.

It’s about asking better questions.

Instead of:

*“Which payload should I run?”*

Start with:

***“How does this application actually work?”***

Once you understand the system, finding weaknesses becomes much easier.
