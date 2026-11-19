# When Pre-Account Takeover Actually Means Pre-Account Takeover

- **Source URL:** https://medium.com/@mostvvfv/when-pre-account-takeover-actually-means-pre-account-takeover-84ee9dd2263c
- **Fetched from:** https://web.archive.org/web/20261111075321/https://medium.com/@mostvvfv/when-pre-account-takeover-actually-means-pre-account-takeover-84ee9dd2263c
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14903 (id 14903)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# When Pre-Account Takeover Actually Means Pre-Account Takeover

**بِسْمِ اللَّهِ رَبِّ الْعَالَمِينَ، وَالصَّلَاةُ وَالسَّلَامُ عَلَى رَسُولِنَا الْأَمِينِ.**

Hello mate! I’ve been putting the writing off forever, but I finally bit the bullet and wrote my first writeup. Today, we’re walking through a business logic flaw to see how a simple design choice has multiple consequences.


When people describe a vulnerability as a *Pre-Account Takeover (Pre-ATO)*, the term itself often fails to convey what is actually happening under the hood. In many cases, the underlying issue is simply an email verification bypass: an attacker can register an account using an email address they do not control before its legitimate owner does. While this can certainly be undesirable, labeling it as “Pre-ATO” does not inherently make the vulnerability more severe. In its more common forms, the practical impact may remain limited to account squatting or premature account creation, often resulting in a Medium-severity finding. Calling such a vulnerability Pre-ATO can therefore be somewhat misleading, and in some cases feels more like severity-driven terminology than a precise description of the security impact.

The case discussed in this write-up, however, is different.

Here, the attacker is not merely registering an account with someone else’s email address. The platform actually provisions the identity that the legitimate user is expected to adopt, establishes it as an active platform account, and grants the attacker authenticated access to that identity before the legitimate owner has ever interacted with the platform. In other words, the attacker gains control of the account **before its legitimate owner even begins using it**.

That distinction is what makes this a genuine Pre-Account Takeover scenario — and not simply an email verification bypass wearing a more impressive name.


## The Bug Some People Would Call Pre-ATO

The investigation initially started with something much more straightforward.

The registration flow accepted an arbitrary email address and immediately provisioned an account for it:

```
POST /api/user?projectId=...
    &login_url=https://api.target.com/org/login/session
Host: login.target.com
{
  "email": "email_we_dont_own@tar.com",
  "password": "<any>",
  "username": "email_we_dont_own@tar.com"
}
```
The response returned a signed session token for the newly created identity:

```
HTTP/2 200
{
  "login_url": "https://api.target.com/org/login/session?token=eyJ...&is_new=1"
}
```
In the normal browser flow, the user is then taken to the email-verification page. That is the point at which the platform expects the user to prove ownership of the email address.

But the session token is already sitting in the registration response.

Intercept the request, take the token, and open the returned `login_url` directly — and the account opens without any email verification taking place.

The important detail is what happens **after** the account is opened. The platform does not treat this as an unverified session that still needs to prove email ownership. The token is accepted as an authenticated session, and the account is handled as though the verification step has already been satisfied.

So the actual bypass is straightforward:

```
Register account
      ↓
JWT returned in response
      ↓
Intercept JWT
      ↓
Open account with JWT
      ↓
Authenticated access without email verification
```
What makes this interesting is the verification boundary itself.

The platform formally enforces email verification for registered accounts; a newly registered user is sent to the email-confirmation flow and is not supposed to gain normal account access until that step is completed. The assumption appears to be that a session token capable of granting normal account access would only be issued after the user had completed the verification flow.

But that assumption breaks at the registration endpoint.

The session token is issued **before email ownership has been established** and is exposed in the registration response. If the request is intercepted and that token is used directly, the account opens normally and is treated as though the email has already been verified.

The application is therefore accepting possession of a token issued **before verification** as sufficient authentication for a state that is supposed to exist **after verification**.

That is the entire bypass, and this behavior was in fact already represented by a **Medium-severity duplicate**.


*Using someone else’s email to create an account does not make this a Pre-ATO, because the legitimate owner was never meant to use that account. The account was created by the attacker, rather than provisioned for the legitimate email owner to adopt.*

*A true Pre-ATO is different. The platform creates the identity that the legitimate user is actually expected to use, while the attacker gains control of that identity before the legitimate user ever establishes control of it.*

*That distinction is what matters here.*

## What an Actual Pre-ATO Looks Like

The answer was sitting in the organization invitation flow.

An Owner could invite an email address that did not have an existing platform account.

### **The usual invitation model in a RBAC system**

An invitation normally works as an authorization mechanism for an identity that is established by the recipient:

```
Invitation link
      ↓
Recipient accepts
      ↓
Recipient establishes their identity
      ↓
Account is created / activated
      ↓
Identity joins the organization
```
The platform does not need to create an account for an email address before its owner has interacted with the invitation.

### The invitation model here

The invitation flow here operates at the **platform identity** level rather than simply issuing an invitation link.

When an Owner invites an email address that is not yet registered, the platform first needs that identity to exist so it can invite it to the organization. That immediately creates a design requirement: the platform needs to provision the account first and only then sends the invitation.

## Get Mostafa’s stories in your inbox

Join Medium for free to get updates from this writer.

The implementation handled this by having the inviter’s browser trigger the same account-provisioning mechanism used by the normal registration flow.

When an unregistered email was invited, the browser first performed in the background:

```
POST /api/user?projectId=...
    &login_url=https://api.target.com/org/login/session
Host: login.target.com
{
  "email": "email_we_dont_own@target.com",
  "password": "<attacker-controlled-password>",
  "username": "email_we_dont_own@target.com"
}
```
The platform created the identity through the normal registration flow and returned an authenticated session for it.

The browser then associated that newly created identity with the Owner’s organization:

```
POST /org/current/org/{id}/users
Host: api.target.com
Authorization: Bearer <owner JWT>
{
  "email": "email_we_dont_own@target.com",
  "role": "ROLE_WHATEVER",
  "permission_to_refund": true,
  "privileges": []
}
```
`HTTP/2 204`
Only after those operations was the invitation sent to the email address.

That ordering is the important part:

```
Owner invites unregistered email
              ↓
Platform provisions the identity
              ↓
Inviter establishes its credentials
              ↓
Identity is associated with the organization
              ↓
Invitation is sent
```
The platform had effectively reversed the trust boundary of an invitation.

An invitation normally represents an offer:

*We have an organization account. Come here and establish yourself as this invited user.*

Here, the platform was doing something fundamentally different:

*We will establish the identity for you first, then tell you to join .*

And because the provisioning request was being executed in the inviter’s browser, the inviter was the party controlling the credentials established for that identity.

That is the point where the finding becomes fundamentally different from the registration bug.

With the registration issue, the attacker says:

*I am going to register an account using an email address I don’t own.*

With the invitation issue, the platform says:

*I will create the platform identity associated with this email address,*

and the attacker is the one who establishes its initial credentials.

The legitimate owner of the email address has not registered anything, has not authenticated, has not accepted anything, and has not interacted with the platform yet.

Yet their platform identity already exists — and someone else has established control over it.

That is a genuine **Pre-Account Takeover**. The real impact here is not just that the attacker gains initial access — it’s that the victim will receive the invitation, accept it, and start using the account completely normally. they will join other organizations, accumulate privileges, and build their presence on the platform, all while the attacker retains the original credentials from day one. The bigger the account grows, the more the attacker benefits — without ever needing to do anything again.

And that design decision had consequences beyond the initial takeover.

The newly created identity was a platform-level identity, not something permanently confined to the organization that created it. The identity could subsequently participate in other organizations and receive additional privileges there.

When that identity is later invited into another organization and granted a higher role — even an Owner-level role — the original credentials remain valid and under the attacker’s control for that same underlying identity.

The attacker therefore retains a foothold in an identity whose privileges can grow independently of the organization to which it was originally invited.

The same architectural decision also creates another problem in the opposite direction.

The attacker can provision arbitrary unregistered email addresses simply by inviting them.

That means the attacker can occupy those email addresses as existing platform identities before their legitimate owners arrive. Even if the identity is later removed from the attacker’s organization, the email remains associated with the existing platform identity rather than becoming available for a clean registration.

## But Wait — MFA Was Enforced

There is one more detail that makes the first exposed session token especially interesting.

In this case, our target had MFA enforced by default for account login. So even if an attacker somehow obtained the credentials of the newly provisioned identity, that alone would not normally be enough to access the account. The attacker would still have to pass the MFA challenge required by the platform.

But there was nothing to worry about — the provisioning flow had already handed us a valid authenticated session.

The session token returned when the identity was provisioned could be used directly to establish an authenticated session, without going through the normal login flow. As a result, no MFA challenge was ever required.

This is important because the token was not merely allowing access to the account before email verification. It effectively provided an already-authenticated session outside the authentication flow where MFA was enforced.

So, in this target, the attacker did not just end up with credentials for an unverified account. The provisioning flow gave them **attacker-controlled credentials and a ready-to-use authenticated session**, completely sidestepping the MFA enforcement that would otherwise have protected the account. This is where the two issues meet.

And in the actual invitation scenario, this meant that before the legitimate owner had ever interacted with the platform, the attacker already had everything needed to use the newly provisioned identity: credentials they controlled, an authenticated session, and no MFA challenge standing in the way.
