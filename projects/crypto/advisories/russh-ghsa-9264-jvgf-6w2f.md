# GHSA-9264-jvgf-6w2f: russh kex_done: Shared-secret callback runs before server host-key verification

| Field | Value |
| --- | --- |
| Ecosystem | Rust (crates.io) |
| GHSA | GHSA-9264-jvgf-6w2f |
| CVE | CVE-2026-128087 |
| Severity | low |
| CWE | CWE-696, CWE-863 |
| Published | 2026-11-13T19:20:16Z |
| Updated | 2026-11-13T19:20:17Z |
| Affected | russh >= 0.55.0, < 0.65.1 (patched: ) |
| Advisory URL | https://github.com/advisories/GHSA-9264-jvgf-6w2f |
| Captured | 2026-11-14 (WAT), daily update |

## Description (verbatim)

### Summary

A malicious SSH server whose host key is rejected can still cause russh's `client::Handler::kex_done()` callback to execute with the raw key-exchange shared secret. Applications using the callback for its documented protocol-bridging purpose may derive keys, initialize a secondary data channel, or perform another externally visible action before russh calls `check_server_key()` and rejects the server.

### Details

During the initial key exchange, russh calls `kex_done()` immediately after the server proves possession of the presented host key, but before the application decides whether that key belongs to the intended server:

```rust
let shared_secret = newkeys.kex.shared_secret_bytes();
handler
    .kex_done(shared_secret, &newkeys.names, session)
    .await?;

// Initial KEX only checks trust afterwards.
if let Some(certificate) = server_host_certificate {
    if !handler.check_server_key(&certificate.into()).await? {
        return Err(crate::Error::UnknownKey.into());
    }
} else if let Some(server_host_key) = server_host_key {
    let check = handler.check_server_key(&server_host_key.into()).await?;
    if !check {
        return Err(crate::Error::UnknownKey.into());
    }
}
```

This is in `russh/src/client/mod.rs` at lines 2036-2078 of commit `183a22e8f8f490fa09b6eb7bd044ef99d8c4414f`.

The API documentation describes `check_server_key()` as the important trust decision that prevents man-in-the-middle attacks. It describes `kex_done()` as the callback for deriving keys for secondary encrypted channels. The feature request that introduced the callback specifically lists VPN-over-SSH, UDP data planes, file transfer, and custom enterprise transports as intended uses.

Cryptographic verification of the KEX signature does not establish peer identity: an attacker operating its own SSH server can always produce a valid signature with its own host key. Identity is established only when `check_server_key()` accepts that key or certificate.

### Expected behavior

For the initial key exchange, `check_server_key()` should accept the server identity before `kex_done()` exposes the shared secret for secondary-channel initialization.

### Actual behavior

`kex_done()` runs first. An untrusted server can therefore trigger application-defined secondary-channel actions even though `check_server_key()` subsequently rejects it with `UnknownKey`.

The callback was introduced by commit `500bef1eccc1c48ac674e2a262aa7887777431eb` and is present from `v0.55.0` through current `v0.65.0`.

### Proof of concept

The following self-contained Cargo project starts a local russh server with a fresh, untrusted host key. The client models the documented bridge use case by exporting the shared secret in `kex_done()`, while `check_server_key()` rejects the server. It asserts both the failed connection and the callback order.

Create an empty directory and add `Cargo.toml`:

```toml
[package]
name = "russh-kex-before-host-trust-poc"
version = "0.1.0"
edition = "2024"

[dependencies]
rand = { version = "0.10", features = ["thread_rng"] }
russh = "=0.65.0"
tokio = { version = "1", features = ["macros", "net", "rt-multi-thread"] }
```

Create `src/main.rs`:

```rust
use std::sync::{Arc, Mutex};

use russh::keys::{Algorithm, PrivateKey, PublicKeyOrCertificate};
use russh::{Names, client, server};

#[derive(Clone)]
struct TestServer;

impl server::Handler for TestServer {
    type Error = russh::Error;
}

#[derive(Clone)]
struct RejectingClient {
    events: Arc<Mutex<Vec<&'static str>>>,
    exported_secret: Arc<Mutex<Option<Vec<u8>>>>,
}

impl client::Handler for RejectingClient {
    type Error = russh::Error;

    async fn kex_done(
        &mut self,
        shared_secret: Option<&[u8]>,
        _names: &Names,
        _session: &mut client::Session,
    ) -> Result<(), Self::Error> {
        self.events.lock().unwrap().push("kex_done");

        // Model a bridge exporting KEX material to a secondary protocol.
        *self.exported_secret.lock().unwrap() = shared_secret.map(ToOwned::to_owned);
        Ok(())
    }

    async fn check_server_key(
        &mut self,
        _server_public_key: &PublicKeyOrCertificate,
    ) -> Result<bool, Self::Error> {
        self.events.lock().unwrap().push("check_server_key");
        Ok(false)
    }
}

#[tokio::main]
async fn main() {
    let mut server_config = server::Config::default();
    server_config.inactivity_timeout = None;
    server_config
        .keys
        .push(PrivateKey::random(&mut rand::rng(), Algorithm::Ed25519).unwrap());
    let server_config = Arc::new(server_config);

    let listener = tokio::net::TcpListener::bind("127.0.0.1:0").await.unwrap();
    let address = listener.local_addr().unwrap();
    tokio::spawn(async move {
        let (stream, _) = listener.accept().await.unwrap();
        let _ = server::run_stream(server_config, stream, TestServer).await;
    });

    let events = Arc::new(Mutex::new(Vec::new()));
    let exported_secret = Arc::new(Mutex::new(None));
    let client = RejectingClient {
        events: events.clone(),
        exported_secret: exported_secret.clone(),
    };

    let result = client::connect(
        Arc::new(client::Config::default()),
        address,
        client,
    )
    .await;

    println!("connection accepted: {}", result.is_ok());
    println!("callback order: {:?}", events.lock().unwrap());
    println!(
        "secret exported before rejection: {}",
        exported_secret.lock().unwrap().is_some()
    );

    assert!(matches!(result, Err(russh::Error::UnknownKey)));
    assert_eq!(
        events.lock().unwrap().as_slice(),
        &["kex_done", "check_server_key"]
    );
    assert!(exported_secret.lock().unwrap().is_some());
}
```

Run:

```sh
cargo run --quiet
```

Observed with russh `v0.65.0`:

```text
connection accepted: false
callback order: ["kex_done", "check_server_key"]
secret exported before rejection: true
```

The connection fails with `russh::Error::UnknownKey`, but the security-sensitive callback and its modeled external side effect have already occurred.

### Impact

Applications overriding `kex_done()` to bootstrap a secondary encrypted transport are affected. An unauthenticated attacker who can impersonate the SSH endpoint can complete KEX with an attacker-owned host key and trigger secondary channel initialization before that key is rejected. Depending on the bridge, this can expose early secondary-channel data or make the application act on a session established with an untrusted peer.

Ordinary clients that leave `kex_done()` at its no-op default, or implementations that independently defer all callback-derived actions until host trust has been confirmed, are not affected.

## References

- https://github.com/Eugeny/russh/security/advisories/GHSA-9264-jvgf-6w2f
- https://github.com/Eugeny/russh/pull/808
- https://github.com/Eugeny/russh/commit/43a46d67a80a7355fcd2fb25e7e00d79aec8184c
- https://github.com/Eugeny/russh/releases/tag/v0.65.1
- https://github.com/advisories/GHSA-9264-jvgf-6w2f
