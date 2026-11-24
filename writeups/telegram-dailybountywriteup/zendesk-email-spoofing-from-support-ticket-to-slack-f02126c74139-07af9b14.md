# Zendesk Email Spoofing

- **Source URL:** https://masimshahzad.medium.com/zendesk-email-spoofing-from-support-ticket-to-slack-f02126c74139
- **Fetched from:** https://masimshahzad.medium.com/feed
- **Fetched:** 2026-11-24
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14997 (id 14997)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Zendesk Email Spoofing: From Support Ticket to Slack

### A 15-year-old’s Zendesk bug let spoofed replies join any support ticket, and Sign in with Apple turned that into Slack access

*AI-assisted: drafted with AI help from public sources, then reviewed and edited. This is an analytical case study of a public disclosure, not my own discovery.*

A Zendesk email spoofing bug let outsiders read other customers’ support tickets, then walk into the company’s internal Slack. Researcher Daniel (hackermondev), 15 at the time, reports more than $50,000 in bounties from affected companies in 2024. Zendesk first rejected the report as out of scope, then fixed it and paid nothing.

***Disclaimer:*** *Educational and defensive use only. Zendesk confirmed a fix on 2 July 2024. Reproduction details are intentionally omitted.*

### Vulnerability Overview

- **Type:** Missing sender authentication on inbound email (spoofed replies add attacker CCs), chained with email-verified OAuth sign-in
- **CWE (analytical mapping, not from the source):** CWE-290 (Authentication Bypass by Spoofing), CWE-345 (Insufficient Verification of Data Authenticity)
- **CVE:** None (hosted service)
- **Severity/Bounty:** Severity not reported. $50,000+ in total from affected companies (researcher-reported); $0 from Zendesk, which per the researcher cited a disclosure-guideline breach

### How the Zendesk Email Spoofing Bug Worked (high level)

Zendesk threads replies into tickets using a reply address built from the ticket number, and ticket numbers are sequential. Its collaboration feature makes anyone CC’d on a reply a participant who can read the full history.

The missing control was sender verification. A reply that merely claimed to come from the requester was accepted, CC list included. A requester’s address plus a nearby ticket number made you a reader.

The escalation reused Inti De Ceukelaire’s 2017 TICKETTRICK idea. Many companies route support@ on their main domain into Zendesk, the same domain that gates Slack. Slack had hardened its own verification emails, but its Sign in with Apple path relied on Apple’s. Apple’s code landed in the support mailbox, became a ticket, and the spoofing bug exposed it: an Apple ID verified at the company domain, accepted by Slack.

### Business Impact

Tickets hold account details and sometimes credentials. The Slack chain reached internal channels at companies that trusted their email domain for access. The researcher reports hundreds of vulnerable instances; many companies disabled email collaboration.

Zendesk’s fix: a stricter spam score for mail threading into existing tickets, and suspension of Apple verification emails.

### Fixing Zendesk-Style Email Trust Gaps (my own analysis)

**1. Authenticate before you mutate.** Only DMARC-aligned mail should change who can read a ticket.

**2. Use unguessable reply tokens,** not sequential IDs.

**3. Keep shared mailboxes off your SSO domain,** or block sign-ups with role addresses.

**4. Don’t let “verified email” alone grant workspace access.**

\# Pseudocode: inbound mail may comment, but only authenticated mail changes readers

def handle\_inbound(msg):

ticket = tickets.by\_reply\_token(msg.to\_token) # random token, not the ticket number

if ticket is None:

if is\_account\_verification\_mail(msg):

return quarantine(msg, "verification\_mail")

return create\_ticket(msg)

auth = verify\_sender(msg) # DMARC-aligned SPF or DKIM

if not auth.aligned or msg.from\_addr not in ticket.participants:

return quarantine(msg, "unauthenticated\_reply") # no comment, no CC change

ticket.add\_comment(msg)

for addr in set(msg.cc) - ticket.participants:

ticket.pending\_cc.add(addr) # an agent approves new readers

# Test: spoofed From failing DMARC -> quarantined, participants unchanged

### Key Takeaways

- “Out of scope” describes a program, not a risk.
- SSO is only as strong as every mailbox on the domain it trusts.
- Each new login method needs the protections the old ones earned.

### Credit & Sources

Research by **Daniel (hackermondev)**: [1 bug, $50,000+ in bounties, how Zendesk intentionally left a backdoor in hundreds of Fortune 500 companies](https://gist.github.com/hackermondev/68ec8ed145fcee49d2f5e2b9d2cf2e52) (October 2024), which quotes Zendesk’s fix statement. Prior research: Inti De Ceukelaire’s [TICKETTRICK](https://medium.com/intigriti/how-i-hacked-hundreds-of-companies-through-their-helpdesk-b7680ddc2d4c) (2017). Facts come from those sources; analysis and code are original.

Next breakdown: another real bug bounty case. Follow @masimshahzad for daily bug bounty breakdowns.
