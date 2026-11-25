# Unauthenticated Spring Boot Actuator

- **Source URL:** https://medium.com/@abdoalkaser53/unauthenticated-spring-boot-actuator-credential-shaped-secrets-leaking-from-actuator-env-and-4f9649a41656
- **Fetched from:** https://medium.com/@abdoalkaser53/unauthenticated-spring-boot-actuator-credential-shaped-secrets-leaking-from-actuator-env-and-4f9649a41656?source=rss-f83275467ea4------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14964 (id 14964)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Abdo Alkaser / Fri, 30 Oct 2026 06:09:12 GMT

Unauthenticated Spring Boot Actuator: Credential-Shaped Secrets Leaking from /actuator/env and /actuator/loggers

When a sanitizer masks everything except the two values that matter

TL;DR

The management endpoints of a financial company’s Factoring backend (/actuator/\*\*) were reachable with no authentication at all. /actuator/env returned an AWS-style access key and an HMAC signing secret in clear text, while masking every other sensitive property as \*\*\*\*\*\*. The same two values also showed up in /actuator/loggers, in a field that should only ever hold a log level. I reported it as Standoff365 report #37252 (CWE-200, rated High by me). It was closed as a duplicate of #37053 about 15 hours later.

Background

Spring Boot Actuator is a built-in monitoring panel for Java apps. It exposes health, metrics, and configuration through simple HTTP endpoints. It is meant to be locked behind authentication or kept off the public internet, because two of its endpoints are very informative:

/actuator/env lists configuration properties and environment variables. Spring masks values whose names look sensitive (key, secret, password, token) by showing \*\*\*\*\*\*.

/actuator/loggers lists logger names and their log levels, such as INFO or DEBUG.

The target matched the program’s published wildcard scope, so it was in scope.

A level field should only contain TRACE, DEBUG, INFO, WARN, ERROR, or FATAL. Here it held values shaped like an AWS access key ID and a 32-character hex secret.

The same two values appeared here under their real property names (\*\*.integration.s3.access-key and \*\*.integration.signing.hmac-secret). Meanwhile every other sensitive property was correctly masked:

encryption.aes-key, jwt.signing-key, keycloak.client-secret, spring.datasource.password, and several API tokens all returned \*\*\*\*\*\*.

/actuator/configprops also returned a differently named S3 credential, correctly masked.

So the sanitizer was working. Only those two properties slipped through, which looks like a targeted override or allow-list entry, not a disabled security control.

The four requests (loggers, env, heapdump, configprops). Hostnames and response bodies are redacted.

3\. Extra information the env endpoint gave away

The real name of the production Kubernetes secret and an internal service hostname.

A property pointing to an admin path for key rotation. I checked only that it exists: it answered 401 Unauthorized with a Bearer challenge, and I did not probe it further.

A different x-powered-by: ASP.NET header on that path, which suggests it is served by a separate .NET backend.

4\. The controls

/actuator/heapdump returned 404 Not Found. That tells me the Actuator surface was not uniformly open, and the exposed endpoints were specific misconfigurations, not a scanning artifact.

A Note on Whether These Credentials Are Real

In my original report I argued that the values were live production credentials, because the key and the secret both changed across three requests over about two hours. Looking back, that argument is weaker than I made it sound:

Real AWS access keys do not normally change every 20 minutes. Fast-changing values can just as well mean a rotation process, a decoy, or generated placeholder data.

The configuration pointed at a bucket region that looks like a Yandex Cloud region, while the key had the AWS AKIA shape. That mismatch does not prove anything, but it does not support a clean AWS story either.

I never used the values against AWS, a signing service, or the admin endpoint, and that was deliberate: the program rules forbid exploitation, so I could not confirm validity. The honest description is credential-shaped values exposed in clear text, validity unconfirmed. If they were decoys (honeytokens), the real finding is still an unauthenticated Actuator leaking internal configuration and infrastructure names.

So What’s the Actual Risk

If the values are real: object-storage access and the ability to forge signed documents, which matters a lot in a factoring product that signs invoices.

Even if they are not: internal hostnames, a Kubernetes secret name, an admin path, and the stack layout. That is a ready-made map for a later attack.

Fix: require authentication on /actuator/\*\* or remove it from the public ingress, expose only health if needed, fix the sanitizer override so every credential-like property is masked, and rotate the exposed values anyway.

Timeline

Oct 22, 05:46: Submitted as report #37252.

Oct 22, 20:43: Closed as a duplicate of #37053, with read access granted to the original.

Lessons Learned

Actuator is the first thing to check on Spring apps. One request to /actuator/env and /actuator/loggers shows whether the panel is exposed.

Read the fields that look wrong. A log level field that contains a long random string is a signal that something is misconfigured.

Look at what is masked, then at what is not. A sanitizer that works everywhere except two properties points to a deliberate override, which is useful for the report.

Do not claim more than you proved. If you cannot test a credential, say it is unconfirmed. The honest version survives triage better, and it costs nothing if the values turn out to be decoys.

Speed matters. This one was a duplicate again, filed within a day of the original. On wildcard scopes, a clean report minutes earlier beats a perfect one later.
