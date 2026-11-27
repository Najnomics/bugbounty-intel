# Bypassing iOS Application (17.x) SSL Pinning via Frida

- **Source URL:** https://pritessh.medium.com/bypassing-ios-application-17-x-ssl-pinning-via-frida-5bc26dc006f4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20260326070457/https://pritessh.medium.com/bypassing-ios-application-17-x-ssl-pinning-via-frida-5bc26dc006f4
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/13201 (id 13201)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bypassing iOS Application (17.x) SSL Pinning via Frida

## Introduction

SSL pinning is a security mechanism used by iOS applications to prevent man-in-the-middle (MITM) attacks by hardcoding or “pinning” the expected server certificate or public key directly into the app. While this is a great defence in production, it becomes an obstacle during mobile security assessments when you need to intercept HTTPS traffic using a proxy like Burp Suite or mitmproxy.

In this post I walk through a custom Frida script — `ios-ssl-pinning-bypass.js` - that I developed and tested on a **jailbroken iOS 17.4.1** device using **Frida 17.8.3**. The script tackles several pinning layers simultaneously, including low-level Security framework APIs, BoringSSL internals, Apple-specific pinning classes, and the popular Alamofire networking library.

### Environment

Component Version: iOS17.4.1 (jailbroken)

Frida: 17.8.3

Script: ios-ssl-pinning-bypass.js

Target: archARM64

### How SSL Pinning Works (Briefly)

When an iOS app enforces certificate pinning, it intercepts the TLS handshake and verifies the server’s certificate against a known-good value embedded in the app binary or bundle. If the check fails, the connection is dropped meaning your proxy certificate gets rejected even if it’s trusted system-wide.

Common pinning points on iOS include:

- **Security framework** — `SecTrustEvaluate`, `SecTrustEvaluateWithError`, `SecTrustGetTrustResult`
- **Network.framework / TLS** — `sec_protocol_options_set_verify_block`
- **BoringSSL** — `SSL_CTX_set_custom_verify`, `SSL_set_custom_verify`
- **Alamofire** — `SessionDelegate` challenge callbacks
- **Apple internal classes** — `AKCertificatePinning`, `AACertificatePinner`

## The Bypass Script — Hook by Hook

### 1. `SecTrustEvaluate` and `SecTrustGetTrustResult`

Both functions write a trust result via an output pointer. The bypass replaces the entire function with a `NativeCallback` that writes `1` (trust result `kSecTrustResultProceed`) to the result pointer and returns `errSecSuccess (0)`.

```
Interceptor.replace(addr, new NativeCallback(function (trust, result) {
    try { if (result && !result.isNull()) result.writeU32(1); } catch(e) {}
    return 0;
}, 'int', ['pointer', 'pointer']));
```
### 2. `SecTrustEvaluateWithError`

This modern API returns a `bool` and fills an `NSError **` on failure. The hook replaces it to return `true` and NULL-out the error pointer, making the caller believe trust evaluation passed cleanly.

```
Interceptor.replace(addr, new NativeCallback(function (trust, error) {
    try { if (error && !error.isNull()) error.writePointer(ptr("0x0")); } catch(e) {}
    return 1;
}, 'bool', ['pointer', 'pointer']));
```
### 3. `SecTrustSetExceptions`

Hooked with `Interceptor.attach` to force the return value to `1` (non-nil pointer, meaning the exceptions object was accepted), satisfying any caller that checks the return value before proceeding.

### 4. BoringSSL — `SSL_CTX_set_custom_verify` / `SSL_set_custom_verify`

These BoringSSL functions register a custom certificate verification callback. The bypass swaps the callback argument (`args[2]`) with a no-op that always returns `0` (SSL\_VERIFY\_OK).

```
var cb = new NativeCallback(function (ssl, out_alert) { return 0; }, 'int', ['pointer', 'pointer']);
Interceptor.attach(addr, { onEnter: function (args) { args[2] = cb; } });
```
### 5. `sec_protocol_options_set_verify_block` - The Tricky One

This was the most complex hook to get right. The function accepts an Objective-C block as the verify handler. On ARM64, calling a block’s invoke pointer with a `bool` argument hit a Frida type error: *"expected an integer"*.

The fix was to try five different type signatures for the block’s `complete()` callback in sequence - `int`, `uint32`, `uint8`, `pointer-only`, and `pointer+ptr(1)` - until one succeeds at runtime:

```
// Try 1: ARM64 bool treated as int
var fn1 = new NativeFunction(invokePtr, 'void', ['pointer', 'int']);
fn1(completeBlock, 1);
```
This trial-and-error approach gracefully handles variation across different iOS builds and apps without crashing.

### 6. Alamofire `SessionDelegate`

Both session-level and task-level `URLAuthenticationChallenge` delegate methods are hooked. The handler block is invoked directly with `.useCredential` disposition (`0`) and a credential built from the server trust, bypassing the app's own challenge logic.

```
var cred = ObjC.classes.NSURLCredential.credentialForTrust_(trust);
var fn   = new NativeFunction(invokePtr, 'void', ['pointer', 'long', 'pointer']);
fn(handlerArg, 0, cred.handle);
```
### 7. Apple Internal Pinning Classes

`AKCertificatePinning`, `AACertificatePinner`, and `AAFCertificateTrustValidator` are Apple-private classes used in some system and first-party apps. All instance methods are hooked to return `ptr(1)` (truthy), blinding any return-value-based pinning checks.

### Running the Script

Start frida-server on the iOS device and Run the script:

```
1. Attach mode (-n)
frida -l ios-ssl-pinning-bypass.js -n <AppName> -H <device-ip> --timeout=60
// -n : attach to already running app using app/process name (app must be opened manually before running Frida)
or
2. Spawn mode (-f)
frida -l ios-ssl-pinning-bypass.js -f <bundle-id> -H <device-ip>
// -f : spawn (launch) the app via Frida using bundle identifier (package name of iOS application)
```
Successful output looks like:

```
[*] SSL Bypass Starting...
[+] SecTrustEvaluate
[+] SecTrustEvaluateWithError
[+] SecTrustGetTrustResult
[+] SecTrustSetExceptions
[+] SSL_CTX_set_custom_verify
[+] SSL_set_custom_verify
[+] sec_protocol_options_set_verify_block hooked
[+] Alamofire.SessionDelegate - URLSession:didReceiveChallenge:completionHandler:
[+] AKCertificatePinning
[+] AACertificatePinner
[*] All hooks active.
```
And Burp starts showing HTTPS traffic from the app.

Find this script in the GitHub repository below.

### Key Takeaways

- **Multiple pinning layers exist simultaneously.** Modern iOS apps can use Security framework, BoringSSL, Network.framework, and third-party libraries all at once — you need to cover all layers.
- **ARM64 bool types are not** **bool**
 **in Frida.** Use `int` or `uint32` when calling block invoke pointers on ARM64 to avoid type errors.
- **Block invoke pointer layout matters.** The invoke function pointer lives at offset `+16` from the block pointer - always read from there, not from the block header itself.
- **Apple private classes change.** `AKCertificatePinning`, `AACertificatePinner`, and similar internal implementations may change or disappear across iOS versions so using `safeHook` wrappers prevents crashes when they're absent.
