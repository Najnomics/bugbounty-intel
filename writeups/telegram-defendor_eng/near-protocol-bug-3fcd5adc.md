# 🛡️ Critical Vulnerability in NEAR Protocol P2P Network

- **Source URL:** https://www.zellic.io/blog/near-protocol-bug
- **Fetched:** 2026-11-17
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/220 (id 220)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
When on the topic of Web3 security, smart contract vulnerabilities are the first things that come to mind. But what if we took it a layer deeper?

We could take a look outside smart contract–related functionality and branch out to other components, such as the consensus layer or the networking layer. Can we find bugs there that an attacker could use to bring the entire blockchain network down?

Absolutely. In NEAR Protocol’s P2P networking layer, I found a vulnerability (now fixed) that would allow an attacker to crash any node on the network by sending a single malicious handshake message, giving it the capability to bring down the entire network in an instant. It would effectively be a [Web3 ping of death↗](https://twitter.com/farazsth98/status/1744981499533983995).

Many thanks to the NEAR team for their professional and timely handling of this report.

Let’s dig into how the mechanism functions, a proof-of-concept exploit, and the final severity classification.

## Introducing the Blockchain[](https://www.zellic.io/blog/near-protocol-bug#introducing-the-blockchain)

Most blockchains nowadays have support for smart contracts. These smart contracts can be EVM compatible (that is, compiled to EVM bytecode), but they can also be in a completely different representation such as WebAssembly. For these blockchains, I prefer dividing the internal components into multiple “layers”, where every layer is part of the blockchain as a whole.

I’ll list out a few of these layers, but note that the following list is not exhaustive:

- **The smart contract layer** — Smart contracts live in this layer. Smart contracts contain user-defined code and can be executed by other users on the network. Smart contracts are isolated from one another. They are only allowed to communicate with each other through external calls.
- **The consensus layer** — This layer handles consensus between the validator nodes.
- **The execution layer** — When smart contracts are executed, this layer handles executing each opcode/instruction within the smart contract as well as the state transition logic.
- **The storage layer** — This layer contains details about the storage internals, such as the data structures used to store all the different types of blockchain data. This includes contract storage state, account states, transaction data, and more.
- **The networking layer** — When nodes need to propagate transactions, blocks, and other data to other nodes, they do so using this layer. This layer is where the NEAR Protocol vulnerability described in this post was found.

Here is a diagram to illustrate how the layers might look in the context of the blockchain.

In order to understand the details of the vulnerability, I will now introduce some concepts about the networking layer.

### The Networking Layer[](https://www.zellic.io/blog/near-protocol-bug#the-networking-layer)

Nodes in the blockchain are typically called “peers” when they communicate with each other. This is how the term peer-to-peer, or P2P, was coined.

Each peer in the network typically dedicates one thread for every remote peer that it is connected to. It keeps a communication channel open at all times, which can be used to send data to, and receive data from, the remote peer.

The actual communication is usually done through a messaging system. For example, the initial P2P connection between two peers might be established like this:

Each time a message is received, the message-handler function determines what to do based on the message’s type and payload.

I will now introduce the handshake mechanism that NEAR protocol uses. This is the final component required to understand the vulnerability.

### NEAR Protocol’s Handshake Mechanism[](https://www.zellic.io/blog/near-protocol-bug#near-protocols-handshake-mechanism)

NEAR Protocol’s main codebase is [nearcore↗](https://github.com/near/nearcore/).

In the P2P system that NEAR protocol uses, handshakes go through three stages:

1. Initial P2P connection establishment
2. Handshake message verification
3. Handshake signature verification

#### Stage 1 — Initial P2P Connection Establishment[](https://www.zellic.io/blog/near-protocol-bug#stage-1-----initial-p2p-connection-establishment)

In the context of a local peer node, every remote peer node can be in one of two states:

1. **Connecting** — In this mode, only handshake-related messages from the remote peer are processed.
2. **Ready** — In this mode, all messages except handshake-related messages from the remote peer are processed.

The handshake mechanism comes into play when a TCP connection has just been established with the remote peer, but no P2P connection has been established yet. In this scenario, the remote peer would be in the `PeerStatus::Connecting` state.

Assuming that it is the remote peer connecting to the local peer (that is, the connection is inbound), the following flow is observed when successfully establishing a P2P connection:

1. The remote peer sends a `PeerMessage::Tier1Handshake` or `PeerMessage::Tier2Handshake` message. The differences between Tier 1 and Tier 2 do not matter for the purposes of this blog post.
2. The local peer verifies and processes this handshake message. If it is found to be valid, it sends back a corresponding `PeerMessage::TierXHandshake` message to establish the connection. This message also contains information about other nodes the local peer is connecting to, so the remote peer can also connect to them.

#### Stage 2 — Handshake Message Verification[](https://www.zellic.io/blog/near-protocol-bug#stage-2-----handshake-message-verification)

The actual structure of the `Handshake` message is shown below:

```
pub struct Handshake {
    /// Current protocol version.
    pub(crate) protocol_version: u32,
    /// Oldest supported protocol version.
    pub(crate) oldest_supported_version: u32,
    /// Sender's peer id.
    pub(crate) sender_peer_id: PeerId,
    /// Receiver's peer id.
    pub(crate) target_peer_id: PeerId,
    /// Sender's listening addr.
    pub(crate) sender_listen_port: Option<u16>,
    /// Peer's chain information.
    pub(crate) sender_chain_info: PeerChainInfoV2,
    /// Represents new `edge`. Contains only `none` and `Signature` from the sender.
    pub(crate) partial_edge_info: PartialEdgeInfo,
    /// Account owned by the sender.
    pub(crate) owned_account: Option<SignedOwnedAccount>,
}
```
Handshake messages are verified and processed using the `process_handshake()` function in NEAR protocol. The code for this function can be found [here↗](https://github.com/near/nearcore/blob/02c725ce96962e89f29b4c81e8178b4e0b0f6bd7/chain/network/src/peer/peer_actor.rs#L478).

Each remote peer is given its own `PeerInfo` structure:

```
pub struct PeerId(Arc<PublicKey>);
pub struct AccountId(pub(crate) Box<str>);
pub struct PeerInfo {
    pub id: PeerId,
    pub addr: Option<SocketAddr>,
    pub account_id: Option<AccountId>,
}
```
From the above structure, we understand that a remote peer primarily identifies itself via its public key. The connection address and account ID are optional; however, it is important to note that in the majority of cases, the connection address will also be provided.

There are a multitude of steps that the `process_handshake()` function takes to ensure that the remote peer sending the handshake is not acting maliciously. Some of these steps are listed below, but I encourage the reader to read through the `process_handshake()` function [here↗](https://github.com/near/nearcore/blob/02c725ce96962e89f29b4c81e8178b4e0b0f6bd7/chain/network/src/peer/peer_actor.rs#L478) to see all the checks in the code:

1. The `protocol_version` must match the local peer’s protocol version.
2. The `sender_chain_info` field’s `genesis_id` must match the local peer’s `genesis_id`.
3. The `target_peer_id` must match the local node’s peer ID.
4. The `owned_account` field is verified as follows.
  - The `owned_account.payload` field must be signed by the `owned_account.account_key`.
  - The `owned_account.account_key` must match the `sender_peer_id` in the handshake.
  - The `owned_account.timestamp` cannot be too far into the past or future.
5. The `partial_edge_info` field is verified in multiple steps.

The `owned_account` field in particular is interesting. It is an essential part of the verification because the signature check combined with the peer ID check proves that the remote peer that sent this handshake message owns the corresponding public key.

Let us take a deeper look at how the signature verification is done.

#### Stage 3 — Handshake Signature Verification[](https://www.zellic.io/blog/near-protocol-bug#stage-3-----handshake-signature-verification)

The `owned_account` field of the handshake is an instance of `SignedOwnedAccount`, whose structure is shown below.

```
pub struct OwnedAccount {
    pub(crate) account_key: PublicKey,
    pub(crate) peer_id: PeerId,
    pub(crate) timestamp: time::Utc,
}
pub struct AccountKeySignedPayload {
    payload: Vec<u8>,
    signature: near_crypto::Signature,
}
pub struct SignedOwnedAccount {
    owned_account: OwnedAccount,
    // Serialized and signed OwnedAccount.
    payload: AccountKeySignedPayload,
}
```
Here, the `AccountKeySignedPayload` structure’s `signature` is used with the `payload` to recover the public key that signed the `payload`. If this doesn’t match the `OwnedAccount` structure’s `account_key`, then the signature verification fails.

The signature-verification function ends up calling the `Signature::verify()` function. Looking at the code [here↗](https://github.com/near/nearcore/blob/02c725ce96962e89f29b4c81e8178b4e0b0f6bd7/core/crypto/src/signature.rs#L534-L565), it is evident that two key types are supported — `ED25519` and `SECP256K1`:

```
pub fn verify(&self, data: &[u8], public_key: &PublicKey) -> bool {
    match (&self, public_key) {
        (Signature::ED25519(signature), PublicKey::ED25519(public_key)) => {
            // [ ... ]
        }
        (Signature::SECP256K1(signature), PublicKey::SECP256K1(public_key)) => {
            // [ ... ]
        }
        _ => false,
    }
}
```
Diving a bit deeper into each case, let us look at how our inputs are handled. In this case, the arguments are mapped as follows:

- `self` — This is the `owned_account.payload.signature`. **Fully controlled**.
- `data` — This is the `owned_account.payload`. **Fully controlled**.
- `public_key` — This is the `owned_account.owned_account.account_key`. **Fully controlled**.

For `ED25519`, the code delegates the signature verification to the `ed25519-dalek` crate:

```
pub fn verify(&self, data: &[u8], public_key: &PublicKey) -> bool {
    match (&self, public_key) {
        (Signature::ED25519(signature), PublicKey::ED25519(public_key)) => {
            match ed25519_dalek::VerifyingKey::from_bytes(&public_key.0) {
                Err(_) => false,
                Ok(public_key) => public_key.verify(data, signature).is_ok(),
            }
        }
        // [ ... ]
    }
}
```
For `SECP256K1`, the code delegates the signature verification to the `secp256k1` crate:

```
pub fn verify(&self, data: &[u8], public_key: &PublicKey) -> bool {
    match (&self, public_key) {
        // [ ... ]
        (Signature::SECP256K1(signature), PublicKey::SECP256K1(public_key)) => {
            let rsig = secp256k1::ecdsa::RecoverableSignature::from_compact(
                &signature.0[0..64],
                secp256k1::ecdsa::RecoveryId::from_i32(i32::from(signature.0[64])).unwrap(),
            )
            .unwrap();
            let sig = rsig.to_standard();
            let pdata: [u8; 65] = {/* turns public_key into a slice of bytes */};
            SECP256K1
                .verify_ecdsa(
                    &secp256k1::Message::from_slice(data).expect("32 bytes"),
                    &sig,
                    &secp256k1::PublicKey::from_slice(&pdata).unwrap(),
                )
                .is_ok()
        }
        _ => false,
    }
}
```
Before continuing on to the next section, can you spot any vulnerabilities in the code snippets above?

Remember — these are the vulnerabilities that could be used to bring down the entire network.

## The Vulnerabilities[](https://www.zellic.io/blog/near-protocol-bug#the-vulnerabilities)

There are two vulnerabilities in the code that is used to verify the signed `data`. Specifically, the vulnerabilities are in the `SECP256K1` branch of the `match` arm in the code above. If you weren’t able to spot both of them before, can you spot them now?

### Vulnerability 1 — `data` Is Not 32 Bytes in Length[](https://www.zellic.io/blog/near-protocol-bug#vulnerability-1--data-is-not-32-bytes-in-length)

In the Rust language, there are two well-known constructs that can lead to a panic — `.unwrap()` and `.expect()`. Both these functions will panic if the variable it is being called on is an `Error` type.

In the `ED25519` `match` arm, the code calls the `public_key.verify()` function and then proceeds to call `.is_ok()` on the value. This will return either `true` or `false` depending on whether an error was returned. No panics would occur here.

In the `SECP256K1` `match` arm though, there are three calls to `.unwrap()`, and one call to `.expect()`. The vulnerability that I reported is specifically the one related to the usage of `.expect` here:

```
&secp256k1::Message::from_slice(data).expect("32 bytes"),
```
Remember that the `data` field is the `owned_account.payload`. Looking into the `secp256k1::Message::from_slice()` function, it returns an error if the `data` passed to it is not 32 bytes in length:

```
// constants::MESSAGE_SIZE = 32
pub fn from_slice(data: &[u8]) -> Result<Message, Error> {
    match data.len() {
        constants::MESSAGE_SIZE => {
            let mut ret = [0u8; constants::MESSAGE_SIZE];
            ret[..].copy_from_slice(data);
            Ok(Message(ret))
        }
        _ => Err(Error::InvalidMessage),
    }
}
```
The issue here is that the `owned_account.payload` field is not 32 bytes in size. This can be verified by looking at how the `send_handshake()` function generates the `owned_account.payload`. I’ll leave it to curious readers to follow the code [here↗](https://github.com/near/nearcore/blob/ca8ebb119b137426f1deaba4c860fbdbf492751d/chain/network/src/peer/peer_actor.rs#L444-L450) to see why this is the case.

Therefore, when `.expect()` is called here, the code will panic and crash the node. Since a handshake message is the first message to be sent when a remote peer connects to a local peer, this vulnerability effectively results in a [Web3 ping of death↗](https://twitter.com/farazsth98/status/1744981499533983995).

### Vulnerability 2 — `signature.0[64]` Can Be Between 0 and 255 Inclusive[](https://www.zellic.io/blog/near-protocol-bug#vulnerability-2--signature064-can-be-between-0-and-255-inclusive)

The other vulnerability is in the following line of code in the `SECP256K1` `match` arm:

```
secp256k1::ecdsa::RecoveryId::from_i32(i32::from(signature.0[64])).unwrap(),
```
Specifically, the inner `i32::from()` converts the last byte of the `signature` to a `u8`. Then, `secp256k1::ecdsa::RecoveryId::from_i32()` actually returns an error if this byte is not between 0 and 3 inclusive:

```
pub fn from_i32(id: i32) -> Result<RecoveryId, Error> {
    match id {
        0..=3 => Ok(RecoveryId(id)),
        _ => Err(Error::InvalidRecoveryId),
    }
}
```
Hitting this error condition is very easy because we control the `signature` entirely. The final `.unwrap()` would then cause a panic and crash the node.

I will now explain how I wrote a proof-of-concept exploit that I used to crash validator nodes on a localnet environment.

## Proof-of-Concept Exploit[](https://www.zellic.io/blog/near-protocol-bug#proof-of-concept-exploit)

When I started writing up a proof of concept to demonstrate this bug in the localnet environment, I found it somewhat surprising that there was no code path that allows a NEAR node to generate `SECP256K1` type keys.

This somewhat explains why the two bugs shown above are so simple in nature — there simply wasn’t a way to generate `SECP256K1` keys in the localnet environment, and therefore this code path ended up never being tested. All generated keys are hardcoded to be `ED25519` keys.

### Local Network Setup[](https://www.zellic.io/blog/near-protocol-bug#local-network-setup)

I first set up a local network with the following configuration:

- One validator node
- One full node

In this setup, the validator node would be a legitimate node that is running and continuously producing blocks. The full node would be the malicious node that I patch and introduce into the network.

The end goal is for the malicious full node to connect to the network and immediately crash the validator node.

To do this, I pulled the nearcore repo (found [here↗](https://github.com/near/nearcore/), commit `e0f0da5c3dde29122e956dfd905811890de9a570`) and ran `make neard-debug -j8` to build a debug version of the node. You can find the final node binary in `target/debug/neard`. I renamed the binary to `neard_legit` because I would be rebuilding the binary with my malicious patch applied later on.

I then used the following command to generate a localnet configuration with one validator node and one full node:

```
$ target/debug/neard_legit --home ./localnet_config localnet -v 1 -n 1
```
The validator node configuration can be found in `./localnet_config/node0`, while the full node can be found in `./localnet_config/node1`.

Before continuing, I would need to rebuild the `neard` binary, except this time with my malicious patches added.

### Maliciously Patching the Full Node[](https://www.zellic.io/blog/near-protocol-bug#maliciously-patching-the-full-node)

The final patch diff file can be found [here↗](https://gist.github.com/farazsth98/32764396061e4e5a46d006a39164be7f).

Note that the same `.expect()` vulnerability also existed in the `Signature::sign()` function in the same code file. However, this function is only used by the sending peer and thus would not lead to a security impact.

However, I’d still need to patch the vulnerability in the malicious node, as otherwise it would just crash when signing the `owned_account.payload`.

My patch does a few things:

1. It patches the `.expect()` vulnerability in the `Signature::sign()` and `Signature::verify()` functions. This allows the malicious node to create `SECP256K1` signatures without crashing.
2. It patches the code used by the `neard localnet` command to make it generate `SECP256K1` keys instead of `ED25519` keys.

The patch should apply cleanly to commit `e0f0da5c3dde29122e956dfd905811890de9a570`.

After this, I rebuilt the `neard` binary again. I used it to then generate a malicious network configuration. This allowed me to copy over the validator\_key.json and node\_key.json files of the malicious node into `./localnet_config/node1`, which means the malicious full node in my localnet environment will now use `SECP256K1` keys:

```
$ target/debug/neard --home ./localnet_malicious_config localnet -v 1
$ cat localnet_malicious_config/node0/validator_key.json
{
  "account_id": "node0",
  "public_key": "secp256k1:nUsQNkHfWWPWP5bkF73AN43VXKmztJdcuqL44yKT2GfyezYbWAu9wK8MLLjxPWxjJgeGu2qapnQVnGBZKW4tFcd",
  "secret_key": "secp256k1:E7rvMjFtqC1KddPt8pqF1HGBxqbAUJMkP8EXbNAUwokB"
}
$ cp localnet_malicious_config/node0/*key.json localnet_config/node1/
```
### Triggering the Crash[](https://www.zellic.io/blog/near-protocol-bug#triggering-the-crash)

To demonstrate the crash, I first started the legitimate validator node in one terminal:

```
$ target/debug/neard_legit --home ./localnet_config/node0/ run
```
I then started my malicious validator node in another terminal. Note that `target/debug/neard` is the malicious node as it was compiled second. It is also using the `SECP256K1` keys that were copied into its configuration directory:

```
$ target/debug/neard --home localnet_config/node1/ run
```
Immediately after starting this node, the legitimate validator node crashes with the following snipped stack trace (the logs can be found in `./localnet_config/node0/logs.txt`):

```
thread 'actix-rt|system:0|arbiter:11' panicked at core/crypto/src/signature.rs:557:63:
32 bytes: InvalidMessage
stack backtrace:
   0: rust_begin_unwind
             at /rustc/79e9716c980570bfd1f666e3b16ac583f0168962/library/std/src/panicking.rs:597:5
   1: core::panicking::panic_fmt
             at /rustc/79e9716c980570bfd1f666e3b16ac583f0168962/library/core/src/panicking.rs:72:14
   2: core::result::unwrap_failed
             at /rustc/79e9716c980570bfd1f666e3b16ac583f0168962/library/core/src/result.rs:1652:5
   3: core::result::Result<T,E>::expect
             at /rustc/79e9716c980570bfd1f666e3b16ac583f0168962/library/core/src/result.rs:1034:23
   4: near_crypto::signature::Signature::verify
             at ./core/crypto/src/signature.rs:551:27
   5: near_network::network_protocol::AccountKeySignedPayload::verify
             at ./chain/network/src/network_protocol/mod.rs:211:15
```
And there it was — the handshake of death. I could now say with 100% certainty that the vulnerability was real and could be used to crash any node on the network. As an added bonus, if any legitimate nodes come back online while the malicious node is still running, they end up instantly crashing again.

## Severity Classification and Bounty Amount[](https://www.zellic.io/blog/near-protocol-bug#severity-classification-and-bounty-amount)

Vulnerabilities that can crash validator nodes are typically classified as critical in severity due to the amount of impact a chain halt can have. However, after extensive discussion with HackenProof and NEAR, this specific vulnerability was classified as a High, with a CVSS rating of 8.8 (9.0 and above are considered Critical). The final bounty amount was $150,000, which I graciously accepted.

## Conclusion[](https://www.zellic.io/blog/near-protocol-bug#conclusion)

This is the most impactful vulnerability I have found thus far in my career. I was hesitant to classify it as such due to its simplistic nature, but I realized that such a vulnerability might come around *once in a lifetime*, and that is only if you’re lucky enough to spot it before anyone else.

I hope this blog post was informational to auditors and bounty hunters who are looking to start hunting for blockchain bugs, and I hope my detailed breakdown of the code helps make it easier for you to approach such complex codebases.

I also hope the proof-of-concept section showcases a reproducible method that can be used to confirm and validate any assumptions made while auditing the code. A quick method of verifying assumptions is a useful tool to have, and I hope I was able to showcase that such a method can generally be reproducible across any blockchain implementation.

## Disclosure Timeline[](https://www.zellic.io/blog/near-protocol-bug#disclosure-timeline)

- **December 25, 2023** — The vulnerability report was submitted through HackenProof, rated with a 10.0 and Critical severity.
- **January 3, 2024** — NEAR confirmed the issue and downgraded it to a High severity with a rating of 8.8.
- **January 9, 2024** — NEAR fixed the issue in [PR 10385↗](https://github.com/near/nearcore/pull/10385) by ensuring that the signature verification code handles any errors returned instead of panicking.
- **January 4 - July 6, 2024** — After extensive discussion with NEAR, I accepted the High severity classification and the $150,000 bounty.

## About Us[](https://www.zellic.io/blog/near-protocol-bug#about-us)

Zellic specializes in securing emerging technologies. Our security researchers have uncovered vulnerabilities in the most valuable targets, from Fortune 500s to DeFi giants.

Developers, founders, and investors trust our security assessments to ship quickly, confidently, and without critical vulnerabilities. With our background in real-world offensive security research, we find what others miss.

[Contact us↗](https://zellic.io/contact) for an audit that’s better than the rest. Real audits, not rubber stamps.
