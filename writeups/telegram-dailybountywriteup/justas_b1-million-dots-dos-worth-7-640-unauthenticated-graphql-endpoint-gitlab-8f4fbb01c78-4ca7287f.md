# Million Dots Dos — Worth $7,640 — Unauthenticated GraphQL Endpoint — Gitlab

- **Source URL:** https://medium.com/@justas_b1/million-dots-dos-worth-7-640-unauthenticated-graphql-endpoint-gitlab-8f4fbb01c782?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251021225241/https://medium.com/@justas_b1/million-dots-dos-worth-7-640-unauthenticated-graphql-endpoint-gitlab-8f4fbb01c782
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10693 (id 10693)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# A Million Dots Dos On Gitlab — Worth $7,640 — Unauthenticated Graphql Endpoint

Most companies on H1 don’t accept DoS vulnerabilities for one simple reason: proving their existence can be quite challenging.

Some programs, however, accept them since you can install their software on your own cloud server, that’s just large enough where a **proof of taking it down counts as eligible vulnerability.**

## Why Stability Matters

It is important to ensure that a Gitlab server remains stable because a crash can break interconnected processes, like CI/CD pipelines, leading to failed builds and potential downtime in customer-facing applications.

Stability is very important for world’s largest enterprises that use Gitlab, like **NVIDIA, Goldman Sachs, Lockheed Martin, NASA, Alibaba, Sony, and others.**

## Technically, It’s Not a Million Dots

Graphql endpoint didn’t strictly validate input size, so anyone could send large payloads of 10–100MB, but a bunch of 15MB payloads was enough to cause **OOM based crash.**

**Machine type:** n2-custom-8–16384 (8 vCPUs, 16 GB Memory)

**CPU platform:** Intel Cascade Lake

**Architecture:** x86/64

## The Impact

### Yo-Yo Attack on Kubernetes Auto-Scaling

Attackers send **periodic bursts of traffic** to overload auto-scaling mechanisms in cloud environments. This leads to **oscillation between scale-up and scale-down phases**, causing performance degradation and economic damage due to the increased resource usage.

### Mitigation Costs

Getting servers back up takes some time and effort, time is money.

### Reputational damage

A visible outage or degraded performance can lower customer trust and investor confidence, particularly for largest customers who rely on GitLab for critical workloads.

Failing to meet uptime commitments during a DoS incident/attack could also breach contractual obligations with enterprise (highest paying) customers. Many organizations that use GitLab have strict SLAs in place, and an **outage caused by a easily fixable vulnerability could force GitLab to provide financial compensation.**

Unaddressed Denial of Service issues could **open the door for class-action lawsuits from customers** who suffered measurable damages due to downtime or lost productivity.

## CVSS Rating & Severity

**CVSS Vector:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H`

**Score:** 7.5 (High)

## Proof of Concept

[Python script](https://github.com/justas-b1/writeup_dos_1/blob/main/PoC.py) used in video POC. Copy paste code into LLM for explanation.
