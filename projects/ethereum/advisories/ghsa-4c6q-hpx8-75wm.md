# GHSA-4c6q-hpx8-75wm: Data race in `requestData` due to read lock on `cacheRequest`

| Field | Value |
| --- | --- |
| Repo | erigontech/erigon |
| GHSA | GHSA-4c6q-hpx8-75wm |
| CVE | none assigned |
| Severity | low |
| CWE | n/a |
| Published | 2026-11-13T13:08:01Z |
| Updated | 2026-11-13T13:08:01Z |
| Affected |  >=v3.1.0 and  <v3.4.0 (patched: v3.4.0) |
| Advisory URL | https://github.com/erigontech/erigon/security/advisories/GHSA-4c6q-hpx8-75wm |

## Description (verbatim)

### Summary

Data race in `downloadRequest.requestData` in `cl/das/peer_das.go` caused by writing to `cacheRequest` while holding a read lock (`RLock`). Under concurrent access this can lead to undefined behavior and potential node crashes / instability. The bug appears to have been fixed already (e.g. by PR `Data race issue in das request`), and this report is mainly to document the original finding and clarify the disclosure timeline.

### Details

Affected function (commit `cb4d196b3b485988daaeb5ef19bc1cbc803342da`):

https://github.com/erigontech/erigon/tree/cb4d196b3b485988daaeb5ef19bc1cbc803342da/cl/das/peer_das.go#L818-L839

```go
func (d *downloadRequest) requestData() *solid.ListSSZ[*cltypes.DataColumnsByRootIdentifier] {
    d.mutex.RLock()
    defer d.mutex.RUnlock()
    if d.cacheRequest != nil {
        return d.cacheRequest
    }
    payload := solid.NewDynamicListSSZ[*cltypes.DataColumnsByRootIdentifier](int(d.beaconConfig.MaxRequestBlocksDeneb))
    for entry, columns := range d.downloadTable {
        id := &cltypes.DataColumnsByRootIdentifier{
            BlockRoot: entry.blockRoot,
            Columns:   solid.NewUint64ListSSZ(int(d.beaconConfig.NumberOfColumns)),
        }
        for column := range columns {
            id.Columns.Append(column)
        }
        if id.Columns.Length() > 0 {
            payload.Append(id)
        }
    }
    d.cacheRequest = payload
    return payload
}
````

`requestData` is protected by `d.mutex.RLock()`, but inside this read lock the code _writes_ to the shared field `d.cacheRequest` and returns a pointer to the constructed payload. When multiple goroutines call `requestData` concurrently:

- They can all observe `d.cacheRequest == nil` and proceed to build and assign a new payload concurrently.
- There are concurrent writes to `d.cacheRequest` under a read lock, and concurrent reads/writes to the pointed `payload` object once returned.

This pattern can trigger Go race detector warnings and, in the worst case, undefined behavior or crashes in production when DAS requests are processed concurrently.

A straightforward mitigation is to use a write lock while potentially modifying `d.cacheRequest`, e.g.:

```go
func (d *downloadRequest) requestData() *solid.ListSSZ[*cltypes.DataColumnsByRootIdentifier] {
    d.mutex.Lock()
    defer d.mutex.Unlock()
    if d.cacheRequest != nil {
        return d.cacheRequest
    }
    payload := solid.NewDynamicListSSZ[*cltypes.DataColumnsByRootIdentifier](int(d.beaconConfig.MaxRequestBlocksDeneb))
    for entry, columns := range d.downloadTable {
        id := &cltypes.DataColumnsByRootIdentifier{
            BlockRoot: entry.blockRoot,
            Columns:   solid.NewUint64ListSSZ(int(d.beaconConfig.NumberOfColumns)),
        }
        for column := range columns {
            id.Columns.Append(column)
        }
        if id.Columns.Length() > 0 {
            payload.Append(id)
        }
    }
    d.cacheRequest = payload
    return payload
}
```

I noticed that this has already been addressed in a later commit/PR (data race fix in DAS request handling), so this report is primarily for record‑keeping and for clarifying the timeline of the original external report.

Regarding timeline / prior exposure: this issue was first reported externally by me via a Sherlock contest (as “Data race in `requestData` due to read lock on `cacheRequest`”), and later I saw it referenced via an internal ticket (`erigontech/security#52`) in the fixing PR. Since the security repository is private, I cannot see the internal history. If possible, I would appreciate a brief confirmation of whether my external report corresponds to that internal ticket or whether there was any prior internal discovery, for my own records.

Related fix PR: https://github.com/erigontech/erigon/pull/17571
Related security issue: https://github.com/erigontech/security/issues/52
