# Bypassing an AWS WAF Challenge Through URL-Encoding

- **Source URL:** https://medium.com/@redhunter01/bypassing-an-aws-waf-challenge-through-url-encoding-an-edge-versus-origin-normalization-mismatch-626d2430f45d
- **Fetched from:** https://medium.com/@redhunter01/bypassing-an-aws-waf-challenge-through-url-encoding-an-edge-versus-origin-normalization-mismatch-626d2430f45d?source=rss-1a8706ec0593------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14951 (id 14951)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** redhunter01 / Sun, 18 Oct 2026 02:04:40 GMT

*How a single percent-encoded path character caused a production authentication request to bypass an edge-level anti-automation challenge and reach the real backend handler.*

During a security assessment of a production authentication API, I identified a mismatch between how the web application firewall (WAF) evaluated request paths and how the backend routed them.

The authentication endpoints were protected by an AWS WAF challenge action at the CDN edge. Requests to the normal login, registration, and password-recovery paths received a challenge response before reaching the application.

However, the protection depended on matching the literal request path.

By percent-encoding a single character in the path, I found that the edge no longer applied the expected challenge. The request was forwarded to the origin, where the path was decoded and routed to the same authentication handler.

The result was a security-control bypass: an automated client could reach the production authentication logic without triggering the intended edge challenge.

The behavior was reproduced across three authentication endpoints. A separate rate-limit test also showed that the application-level rate limiter did not consistently compensate for the missing challenge during the tested request burst.

This case study explains the underlying normalization mismatch, how the evidence established the bypass, why the distinction between edge and origin behavior matters, and how to remediate the issue.

The application used a layered request-processing architecture.

At a high level, requests passed through the following components:

The intended security boundary looked like this:

Incoming authentication request

|

v

CDN / AWS WAF

|

v

Challenge enforcement

|

v

Backend authentication API

When the WAF challenge fired, the request was stopped at the edge.

The backend did not receive the authentication request.

The problem was that the edge and the origin did not interpret every representation of the same path identically.

HTTP requests can represent a path using percent-encoded characters.

For example, %6c represents the lowercase letter l, %66 represents f, and %72 represents r.

Consequently, a URL-encoded path can represent the same logical endpoint as its ordinary spelling.

In this investigation, the following pairs were relevant:

Canonical pathEncoded representation/api/v1/login/api/v1/%6cogin/api/v1/register/api/v1/%72egister/api/v1/forgotPassword/api/v1/%66orgotPassword

The security issue was not percent-encoding itself.

The issue was that the WAF evaluated the incoming path in a form that did not match the protected literal path, while the origin subsequently decoded the encoded character and routed the request to the real authentication handler.

This created a discrepancy between the security decision and the application behavior.

The WAF effectively saw a different path representation from the one ultimately processed by the backend.

Before investigating the encoded paths, I established the behavior of the ordinary authentication routes.

A request to the canonical login endpoint produced a response with these characteristics:

HTTP/2 202

server: CloudFront

x-amzn-waf-action: challenge

content-length: 0

The response had an empty body and included the WAF challenge indicator.

This was important because it established the intended control behavior.

The request was being challenged at the edge rather than processed normally by the authentication application.

The same general challenge behavior was observed for the canonical registration and password-recovery paths.

With the baseline established, the next step was to determine whether an alternative representation of the same path would receive identical treatment.

I then compared the response from the canonical login path with the response from its percent-encoded equivalent.

The encoded request used the same HTTP method, host, content type, and controlled invalid credentials. The path was the relevant difference.

Instead of receiving the empty edge challenge response, the encoded request returned a response resembling:

HTTP/2 200

server: awselb/2.0

content-type: application/json

The response body contained an application-level authentication error:

```
{
  "error": true,
  "errorCode": "InvalidCredential",
  "errors": [
    {
      "code": 4318
    }
  ],
  "data": {
    "sessionAttemptId": "..."
  }
}
```
The identifiers and session-related values above are illustrative and have been omitted or generalized.

This response was materially different from the baseline.

The canonical request received an edge challenge, while the encoded request reached the real login handler and returned its normal application-level response.

The evidence supporting this conclusion included:

The important finding was not simply that the encoded URL returned HTTP 200.

An HTTP status code alone does not establish a security bypass.

The stronger evidence was that the response changed from an edge-generated challenge to the expected behavior of the backend authentication handler.

The same normalization mismatch was observed on three authentication routes.

FunctionalityEncoded characterObserved behaviorLoginl → %6cReached the login handlerRegistrationr → %72Reached registration validationPassword recoveryf → %66Reached the password-recovery handler

The ordinary forms of these paths continued to receive the WAF challenge.

The encoded forms reached the corresponding application handlers.

For registration, the application returned a field-validation error. This showed that the request had progressed into application-level processing rather than being stopped by the edge challenge.

For password recovery, the handler returned its normal success-shaped response. That response established handler reachability, but it did not independently prove that an email was delivered or that a password was changed.

These distinctions matter when assessing impact.

The evidence established that the edge challenge could be bypassed to reach the authentication handlers. It did not establish successful account compromise or successful password recovery against a real user.

The underlying failure involved inconsistent interpretation of the request path.

The observed processing sequence was:

Client sends percent-encoded path

|

v

CDN / WAF evaluates literal path

|

v

Expected path rule does not match

|

v

Request passes without the challenge

|

v

Origin decodes the encoded character

|

v

Decoded path matches an authentication route

|

v

Real application handler processes request

The edge applied its security decision before the request representation had been normalized consistently with the origin’s routing behavior.

The WAF and the backend therefore disagreed about the effective request path.

This is an example of a **parser or normalization differential**.

Different components may interpret the same input differently because they apply transformations at different stages.

When security rules depend on one representation and application routing depends on another, an attacker may be able to reach functionality that the edge was intended to protect.

A path-normalization difference is not automatically a vulnerability.

It becomes a security issue when the difference defeats an intended security control.

In this case, the edge challenge was specifically intended to restrict automated access to authentication entry points.

The canonical requests were challenged, while encoded requests reached the backend without that challenge.

That established a direct relationship between the normalization mismatch and the security-control bypass.

The finding was therefore not based solely on unusual URL parsing. It was based on a demonstrated difference in enforcement.

The critical question was:

**Did the alternative path representation reach a handler that the normal representation could not reach without passing the challenge?**

The observed responses supported the conclusion that it did.

After confirming the challenge bypass, I examined whether application-level rate limiting compensated for the missing edge control.

In a controlled burst test, 30 requests were sent to the encoded login path.

The reported results were:

MeasurementObserved resultTotal requests30Requests that reached the handler22Handler-reaching rate73.3%Requests not counted as reaching the handler8

Some responses included an application-level rate-limit error, identified by code 4331.

However, rate-limit responses appeared intermittently rather than consistently blocking the burst.

The encoded path also continued to avoid the edge challenge.

These results indicated that the application-level rate limiter did not fully replace the bypassed edge control under the tested conditions.

There are important limits to this measurement.

A single 30-request burst does not establish the application’s behavior under every traffic pattern, account configuration, source address, or time window. Nor does it establish a sustainable attack rate.

It does, however, provide evidence that the remaining rate limit was not an effective substitute for the challenge during this specific test.

The primary impact was the removal of an intended anti-automation barrier from production authentication endpoints.

Because the encoded paths reached the actual handlers, automated clients could interact with the login, registration, and password-recovery logic without triggering the configured challenge.

The bypass could reduce the effectiveness of an edge challenge intended to discourage or interrupt automated login attempts.

Depending on the application’s remaining controls, this could increase exposure to credential stuffing or password spraying.

The test demonstrated handler reachability and inconsistent rate-limit responses. It did not demonstrate a successful login using another user’s credentials.

The registration handler could be reached without the intended edge challenge.

This could facilitate automated registration attempts if additional application-level protections are insufficient.

The test established handler reachability, not successful abuse of real registrations at scale.

The password-recovery handler could also be reached without the edge challenge.

This could facilitate repeated password-recovery requests, depending on the application’s additional controls.

The observed response did not prove that messages were sent or that any user’s account was compromised.

The broader concern is that a protection configured at the edge did not reliably cover the backend functionality it was meant to protect.

Any security assessment that considers only the canonical URL could therefore miss an alternative path representation that reaches the same handler.

A strong report distinguishes the security-control bypass from its potential downstream consequences.

The distinction is important: the demonstrated vulnerability was the bypass of the edge challenge. Downstream account abuse was a realistic risk, not a confirmed outcome of the supplied proof of concept.

The core fix is to make the security decision consistent with the application’s eventual route interpretation.

The edge should evaluate a canonical representation of the request path, using well-defined normalization behavior consistent with the origin.

Equivalent path representations should not receive different protection merely because a character is percent-encoded.

Normalization must be implemented carefully so that it does not introduce new routing ambiguities or alter legitimate application behavior.

Where possible, associate the anti-automation control with the actual authentication route rather than relying solely on a literal path match at the edge.

An origin-level or application-level control can provide defense-in-depth if a request reaches the handler through an unexpected representation.

Login, registration, and password recovery should have consistent anti-abuse protections.

The fix should cover every supported version and route, not just the first endpoint discovered.

Rate limiting should be independently enforced at the authentication layer.

Appropriate controls may include account-based and source-based limits, progressive delays, monitoring, and additional verification when abuse is detected.

These controls should not depend exclusively on the WAF challenge being present.

Regression tests should compare canonical and encoded path variants.

They should verify that equivalent paths receive the same security treatment and that unexpected representations cannot bypass the challenge.

If the same path-matching strategy is used elsewhere, other protected endpoints may share the same design weakness.

The review should prioritize authentication and other sensitive operations, while confirming any additional findings individually.

This finding demonstrates a repeatable approach to identifying edge-versus-origin security discrepancies.

Send a normal request to the protected endpoint.

Record the status code, response headers, response body, and any explicit WAF challenge indicators.

Determine whether the request is stopped at the edge or reaches the backend.

Do not assume that an HTTP response proves which component handled the request.

Investigate whether URL-encoded characters or other equivalent path representations are handled consistently across the request-processing chain.

Only test systems and endpoints for which you have authorization.

Change the path representation while keeping the method, body, headers, and other relevant variables constant.

A controlled comparison makes it easier to isolate the factor responsible for the difference.

Look for evidence that the backend processed the request, such as application-specific validation errors or structured responses that differ from the edge challenge.

Avoid treating a changed status code alone as conclusive proof.

A shared WAF rule may affect several routes, but each endpoint should be checked to establish the actual scope.

Determine whether application-level rate limits continue to operate and document the precise test conditions.

Avoid extrapolating a small test burst into claims about unlimited throughput.

Demonstrating that an authentication handler can be reached without the intended challenge is sufficient to establish the control bypass.

There is no need to attempt account takeover, attack real users, or generate large volumes of authentication traffic to prove the underlying issue.

**1. Security rules must match application behavior.**

If the WAF and origin interpret a request differently, a security rule can fail even when it appears correct.

**2. URL encoding is not inherently malicious.**

The issue was the inconsistent treatment of equivalent path representations, not the existence of percent-encoding itself.

**3. Edge controls should not be the only line of defense.**

Authentication endpoints should have independent protections against automation and abuse.

**4. A backend response is useful evidence.**

The change from an edge-generated challenge to a structured application response helped establish that the encoded request reached the real handler.

**5. Measure rate limits rather than guessing.**

The 30-request test supplied a concrete observation, but it did not justify claims about unlimited throughput or universal rate-limit failure.

**6. Report the control bypass separately from hypothetical abuse.**

The bypass was demonstrated. Successful account compromise was not necessary to prove it.

The root cause was a disagreement between the path representation evaluated by the WAF and the path representation ultimately used by the origin.

A single percent-encoded character caused the edge rule to miss the request, while the origin decoded the character and routed the request to the intended authentication handler.

The result was an anti-automation challenge bypass affecting three production authentication endpoints.

The complete chain was:

Percent-encoded authentication path

|

v

Edge rule misses literal-path match

|

v

Challenge action is not applied

|

v

Origin decodes the path

|

v

Authentication handler is reached

|

v

Application-level rate limiting remains

|

v

Automated access is less constrained

The broader lesson is that security controls must operate on the same effective request semantics as the application they protect.

**When a WAF and an origin disagree about which endpoint a request represents, the gap between those interpretations can become a security boundary failure.**
