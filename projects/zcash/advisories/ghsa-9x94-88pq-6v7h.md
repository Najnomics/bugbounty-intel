# GHSA-9x94-88pq-6v7h: Lightwalletd cancelled block-range streams leak worker goroutines

| Field | Value |
| --- | --- |
| Repo | zcash/lightwalletd |
| GHSA | GHSA-9x94-88pq-6v7h |
| CVE | none assigned |
| Severity | high |
| CWE | n/a |
| Published | 2026-07-28T19:10:36Z |
| Updated | 2026-07-28T19:10:36Z |
| Affected | github.com/zcash/lightwalletd <= 0.4.19 (patched: 0.5.0) |
| Advisory URL | https://github.com/zcash/lightwalletd/security/advisories/GHSA-9x94-88pq-6v7h |

## Description (verbatim)

## Summary

The lightwalletd compact block, range, tree, and transaction query serving workflow leaks one worker goroutine when a client cancels or fails a `GetBlockRange()` stream after response delivery begins. Severity is assessed as **High** under the provided matrix because the direct impact is temporary denial of service for supporting infrastructure, and the likelihood is high for any attacker who can reach the gRPC service and make range-stream requests.

## Finding Description

The affected behavior is in the gRPC range serving path. `GetBlockRange()` and `GetBlockRangeNullifiers()` delegate block production to `common.GetBlockRange()` through unbuffered channels. The server-side stream handler returns immediately if `resp.Send()` fails, but the delegated worker has no cancellation signal and the handler does not drain the channels before returning.

The relevant code areas are:

- `zcash-bbp-scope/repos/lightwalletd/frontend/service.go:230-249`, where `GetBlockRange()` starts the range worker and sends blocks to the client stream.
- `zcash-bbp-scope/repos/lightwalletd/frontend/service.go:256-291`, where `GetBlockRangeNullifiers()` follows the same channel and worker pattern.
- `zcash-bbp-scope/repos/lightwalletd/common/common.go:573-604`, where `common.GetBlockRange()` loops through the requested range and sends blocks/errors on unbuffered output channels.

The intended path is straightforward. A client opens a block-range stream, the handler starts the range worker, the worker sends each compact block to the handler, and the handler forwards each block to the gRPC stream. When the client disconnects, all per-request resources should be released.

The unexpected path occurs when stream sending fails after the worker has started:

1. A client requests any non-empty compact-block range.
2. The handler creates unbuffered `blockChan` and `errChan` channels and starts `common.GetBlockRange()` in a goroutine.
3. The worker sends the first compact block through `blockChan`.
4. The handler receives that block and calls `resp.Send(cBlock)`.
5. The client has cancelled or dropped the stream, so `resp.Send()` returns an error.
6. The handler returns immediately.
7. The worker continues to the next send or final status send, but no goroutine is left to receive from the unbuffered channels.
8. The worker remains blocked indefinitely.

The proof of concept constructs a cache-backed lightwalletd streamer, simulates cancelled client streams, and repeats the request twenty times. The regression-style test expects no meaningful goroutine growth, but vulnerable code leaks one worker per cancelled stream and the test fails with `leaked=20`.

## Impact Explanation

The direct impact is resource exhaustion on an individual lightwalletd instance. A remote client that can access the gRPC service can repeatedly cancel range streams and accumulate blocked goroutines, increasing memory use and scheduler overhead until the service degrades or requires restart. The issue does not affect consensus validity, issuance, or transaction finalization directly, but it can interrupt wallet sync/query availability for users depending on the affected service.

## Likelihood Explanation

Likelihood is **High** for exposed or otherwise reachable lightwalletd gRPC services. The exploit does not require authentication material, local filesystem access, malformed cache files, backend compromise, or expensive computation. A client only needs to request a non-empty range and cause the stream send to fail after delivery begins.

## Proof of Concept
[WF-025.zip](https://github.com/user-attachments/files/27979358/WF-025.zip)


## Recommendation

Consider passing the gRPC stream context, or an explicit cancellation channel, into `common.GetBlockRange()` so the worker stops when the client stream is cancelled. Another approach could be to make the range handler responsible for draining and terminating the worker before returning on `resp.Send()` errors. The most direct fix is to ensure every early return from `GetBlockRange()` and `GetBlockRangeNullifiers()` either cancels the producer or leaves no producer blocked on unbuffered sends.
