# Insecure Authorization on *** Android — mobile application

- **Source URL:** https://medium.com/@jokodfir/insecure-authorization-on-android-mobile-application-89472e4f468b
- **Fetched from:** https://medium.com/@jokodfir/insecure-authorization-on-android-mobile-application-89472e4f468b?source=rss-637030b9c7b7------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14921)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Joko Purwanto / Tue, 22 Sep 2026 22:16:43 GMT

Assalamualaikum wr.wb.

Bismillah

This is my thirteenth article, I hope it proves useful to readers

com.\*\*\*.editor/com.\*\*\*.browserflow.feature.CustomTabFlowActivity (intent-filters: com.\*\*\*.editor://oauth, \*\*\*editor://sso, [https://www.\*\*\*.com/oauth/transfer,](https://www.canva.com/oauth/transfer,) /login/sso/transfer)

com.\*\*\*.browserflow.feature.CustomTabFlowActivity is exported (android:exported=”true”) and registered as the redirect target for several sensitive browser-based OAuth/SSO flows, including:

I decompiled the app and traced the native code that handles an incoming redirect (CustomTabFlowActivity -> CustomTabFlowViewModel.f(Uri) -> BrowserFlowResultManager.a(Uri)). At no point in this path is there a check that the incoming URI’s state/code/token parameters actually correspond to a flow this same app instance initiated (no nonce/state comparison, no PKCE verifier check, no caller-identity check). The method simply republishes whatever Uri it receives as “flow completed” to whatever business logic is currently listening.
