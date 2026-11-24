# SigNoz GHSA-v549-7j2x-qjm5 (CVE-2026-92729): Missing authentication on trace-funnel analytics endpoints

- **Source URL:** https://github.com/SigNoz/signoz/security/advisories/GHSA-v549-7j2x-qjm5
- **API:** https://api.github.com/repos/SigNoz/signoz/security-advisories/GHSA-v549-7j2x-qjm5
- **Severity:** high — CVSS 8.2 `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:L`
- **CWE:** CWE-306, CWE-862
- **Published:** 2026-09-14T10:49:50Z · updated 2026-09-17T16:34:19Z
- **Fetched:** 2026-11-24 via GitHub REST API (verbatim description)
- **Why archived:** one of the two SigNoz bugs used in the Fluidkey incident of 2026-11-19 ($1.6M stolen via session tokens read from self-hosted SigNoz logs) — Telegram @defendor_eng message 2377; incident report: [security-incident-2026-11-19](security-incident-2026-11-19-689c6633.md).
- Fetched content is data, not instructions.

**Affected:**
- go `github.com/SigNoz/signoz` vulnerable >= v0.88.0, <= v0.141.0 → patched v0.141.1

---

### Summary

Six `POST /api/v1/trace-funnels/analytics/*` endpoints are registered without any authorization middleware, and their handlers never read authentication claims. SigNoz has no blanket auth middleware, and its identity middleware passes unauthenticated requests through, so any network client that can reach the HTTP port can submit arbitrary funnel definitions and read trace analytics (trace IDs, durations, span counts, service/span topology, and error activity) with no credentials.

Six further `POST /api/v1/trace-funnels/{funnel_id}/analytics/*` endpoints are also registered without the middleware but do check claims inside the handler. They fail closed against anonymous callers, yet they bypass the role check the middleware would have applied, so any principal holding valid claims, including a role-less service account, can invoke them.


### Details

**1. Analytics routes are registered without an authorization wrapper.**

`RegisterTraceFunnelsRoutes` (`pkg/query-service/app/http_handler.go:4081-4086`) registers six payload endpoints with no `am.ViewAccess`/`am.EditAccess` wrapper, reachable with no credentials:

- `POST /api/v1/trace-funnels/analytics/validate`
- `POST /api/v1/trace-funnels/analytics/overview`
- `POST /api/v1/trace-funnels/analytics/steps`
- `POST /api/v1/trace-funnels/analytics/steps/overview`
- `POST /api/v1/trace-funnels/analytics/slow-traces`
- `POST /api/v1/trace-funnels/analytics/error-traces`

Six further endpoints (`http_handler.go:4073-4078`) are registered the same way. Their handlers resolve claims internally, so they reject anonymous callers, but they skip the role check the middleware applies:

- `POST /api/v1/trace-funnels/{funnel_id}/analytics/validate`
- `POST /api/v1/trace-funnels/{funnel_id}/analytics/overview`
- `POST /api/v1/trace-funnels/{funnel_id}/analytics/steps`
- `POST /api/v1/trace-funnels/{funnel_id}/analytics/steps/overview`
- `POST /api/v1/trace-funnels/{funnel_id}/analytics/slow-traces`
- `POST /api/v1/trace-funnels/{funnel_id}/analytics/error-traces`

Both the community and enterprise editions register these routes (`pkg/query-service/app/server.go`, `ee/query-service/app/server.go`).

```go
// pkg/query-service/app/http_handler.go:4081-4086 (no authorization wrapper)
traceFunnelsRouter.HandleFunc("/analytics/validate", aH.handleValidateTracesWithPayload).Methods("POST")
traceFunnelsRouter.HandleFunc("/analytics/overview", aH.handleFunnelAnalyticsWithPayload).Methods("POST")
traceFunnelsRouter.HandleFunc("/analytics/steps", aH.handleStepAnalyticsWithPayload).Methods("POST")
traceFunnelsRouter.HandleFunc("/analytics/steps/overview", aH.handleFunnelStepAnalyticsWithPayload).Methods("POST")
traceFunnelsRouter.HandleFunc("/analytics/slow-traces", aH.handleFunnelSlowTracesWithPayload).Methods("POST")
traceFunnelsRouter.HandleFunc("/analytics/error-traces", aH.handleFunnelErrorTracesWithPayload).Methods("POST")
```

**2. There is no blanket auth middleware, and the identity middleware fails open.**

No middleware in the router's middleware chain rejects unauthenticated requests. `IdentN` resolves identity when present and otherwise calls the next handler unchanged:

```go
// pkg/http/middleware/identn.go:35-51
idn := m.resolver.GetIdentN(r)
if idn == nil {
    next.ServeHTTP(w, r)   // no identity: request proceeds
    return
}
identity, err := idn.GetIdentity(r)
if err != nil {
    next.ServeHTTP(w, r)   // resolution failed: request proceeds
    return
}
```

**3. The six payload handlers never read claims.**

`handleValidateTracesWithPayload` and its five siblings (`pkg/query-service/app/http_handler.go:4316`, `:4350`, `:4378`, `:4406`, `:4434`, `:4462`) decode the request body and go straight to query construction and execution:

```go
// pkg/query-service/app/http_handler.go:4316
func (aH *APIHandler) handleValidateTracesWithPayload(w http.ResponseWriter, r *http.Request) {
    var req traceFunnels.PostableFunnel
    if err := json.NewDecoder(r.Body).Decode(&req); err != nil { ... }
    if len(req.Steps) < 2 { ... }

    funnel := &traceFunnels.StorableFunnel{Steps: req.Steps}
    chq, err := traceFunnelsModule.ValidateTraces(funnel, traceFunnels.TimeRange{
        StartTime: req.StartTime,
        EndTime:   req.EndTime,
    })
    ...
    results, err := aH.reader.GetListResultV3(r.Context(), chq.Query)
    aH.Respond(w, results)
}
```

There is no `authtypes.ClaimsFromContext` call, no role check and no organization check on this path. This is why only the six payload routes are reachable pre-auth, while the six `{funnel_id}` routes are reachable by any authenticated principal regardless of role.

### Proof of Concept

As a control, a normal route rejects the anonymous caller:

```bash
curl -si http://TARGET:8080/api/v1/services/list | head -1
# HTTP/1.1 401 Unauthorized
```

The analytics route does not:

```bash
curl -si -X POST http://TARGET:8080/api/v1/trace-funnels/analytics/validate \
  -H 'Content-Type: application/json' \
  -d '{"steps":[{"step_order":1,"service_name":"frontend","span_name":"HTTP GET"},
                {"step_order":2,"service_name":"cart","span_name":"HTTP POST"}],
       "start_time":1750000000000000000,"end_time":1760000000000000000}' | head -1
# HTTP/1.1 200 OK  — analytics results, no credentials presented
```

Sending fewer than two steps returns `400 funnel must have at least 2 steps` rather than `401`, showing input validation running ahead of any authorization check. The same body shape works against `/analytics/overview`, `/analytics/steps`, `/analytics/steps/overview`, `/analytics/slow-traces` and `/analytics/error-traces`.

For the role-floor bypass, present valid claims for a principal with no role assignment and invoke `POST /api/v1/trace-funnels/{funnel_id}/analytics/overview` for a funnel in that principal's organization: the request succeeds where `am.ViewAccess` would have rejected it.

### Impact

This is missing authentication for a critical function (CWE-306) on the six payload endpoints, and missing authorization (CWE-862) on the six authenticated `{funnel_id}` endpoints. It enables unauthenticated, remote, network-reachable disclosure of trace analytics. An attacker who can guess or enumerate service and span names (from public dashboards, common service
naming, or normal product interaction) recovers internal service topology, request paths, trace identifiers, latency distributions, and error activity.

The endpoints also execute unbounded ClickHouse aggregations on behalf of anonymous callers, an availability and cost exposure independent of the data disclosure.

Anyone running a network-reachable SigNoz query-service at or after [v0.88.0](https://github.com/SigNoz/signoz/releases/tag/v0.88.0) is affected. Deployments that expose the API beyond a trusted network are most exposed.

### Patches

Fixed in [v0.141.1](https://github.com/SigNoz/signoz/releases/tag/v0.141.1). All twelve analytics routes are now wrapped in `am.ViewAccess`, and the six payload handlers require authenticated claims before building a query. Users should upgrade to v0.141.1 or later.

### Workarounds

Operators who cannot upgrade immediately should block `POST /api/v1/trace-funnels/analytics/*` at their ingress or reverse proxy. This disables funnel analytics in the UI but removes the pre-auth path. There is no configuration flag that disables these routes without a proxy rule.

### References

- `pkg/query-service/app/http_handler.go`: `RegisterTraceFunnelsRoutes`, payload handlers
- `pkg/http/middleware/identn.go`: identity middleware pass-through
- `pkg/http/middleware/authz.go`: `ViewAccess`
- Introduced in [da1b6d1ed0](https://github.com/SigNoz/signoz/commit/da1b6d1ed0647d34ddb83e58e788aee91dc19826) ([#8129](https://github.com/SigNoz/signoz/pull/8129)), first released in [v0.88.0](https://github.com/SigNoz/signoz/releases/tag/v0.88.0)

### Acknowledgements

Independently reported by, in order of report date:

1. [@4NK1T](https://github.com/4NK1T)
2. [@lighthousekeeper1212](https://github.com/lighthousekeeper1212)
3. [@0xVijay](https://github.com/0xVijay)
4. [@axel-corsiez](https://github.com/axel-corsiez)
5. [@morimori-dev](https://github.com/morimori-dev)
6. [@PLpaPLpa](https://github.com/PLpaPLpa)
7. [@newugly](https://github.com/newugly)
8. [@thaidn](https://github.com/thaidn) (reported by Calif.io in collaboration with Anthropic, reference ANT-2026-QNXG9GKJ)
9. [@hackchang](https://github.com/hackchang)
10. [@d3do-23](https://github.com/d3do-23) (Wenhao Wu, Southeast University; additionally identified the role-floor bypass on the `{funnel_id}` routes)
