# Apps SDK sandbox escape

- **Source URL:** https://medium.com/@jokodfir/apps-sdk-sandbox-escape-app-reaches-native-window-android-window-androidbridge-de7ef00e4bc3
- **Fetched from:** https://medium.com/@jokodfir/apps-sdk-sandbox-escape-app-reaches-native-window-android-window-androidbridge-de7ef00e4bc3?source=rss-637030b9c7b7------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14921)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Joko Purwanto / Wed, 23 Sep 2026 03:53:06 GMT

The \*\*\* editor’s WebView registers two native @JavascriptInterface objects using the old, frame-unscoped addJavascriptInterface() API:

// jc/q.java — WebViewFactory.kt, where the main editor WebView is created

webView.addJavascriptInterface(webViewJavascriptInterface.new JsInterface(), "Android");

// com/\*\*\*/crossplatform/core/bus/WebXMessageBusNegotiator.java

webView.addJavascriptInterface(new JsInterface(), "AndroidBridge");

addJavascriptInterface() exposes the object to every frame of the WebView, not just the top document. That matters here because \*\*\* Apps (Google Drive, Brandfetch, anything built with @ \*\*\*/cli) run as sandboxed iframes inside that same WebView, on their own origin (https://app-id.\*\*\*-apps.com) — a different origin than the trusted top-level document at [www.\*\*\*.com.](http://www.canva.com.)

I built an ordinary \*\*\* App through the public Apps SDK/Developer Portal, installed it like any real third-party app, and from inside its normal sandboxed iframe on a real device:

window.Android is reachable and none of its methods check where the call came from. typeof window.Android is “object”, Android.getPageLocation() returns “editor” (a real value from \*\*\* own native code, not undefined), and calling Android.onPageBuildIdentityReady() with a made-up JSON payload just works — no exception, no rejection. I went through WebViewJavascriptInterface.java line by line and there’s no origin check in that class at all.

That forged data doesn’t just sit there, either. onPageBuildIdentityReady() writes it into a shared AtomicReference\<PageBuildIdentity> (jc.j). The only other place that reference is read is WebViewRenderProcessGoneHandler.b() — which runs whenever the WebView’s renderer gets killed or reclaimed (a routine low-memory event on Android, not something rare). It pulls the value with getAndSet(null) and hands it straight to ReportWebViewCrashWorker, which WorkManager enqueues to persist and send as a crash-telemetry report to \*\*\* backend. So the fake stack/variant/version/releaseName/deploymentGroup fields I set end up attributed as real build metadata in whatever gets reported to \*\*\*.

window.AndroidBridge is reachable too, and requestMessagePort() can be called without throwing, from the same untrusted frame. This one’s a bit different: AndroidBridge’s handshake logic (in h.java) does check the origin before actually handing over a real MessagePort — it compares webView.getUrl() against a trusted \*\*\*.com URI. I set up a listener before calling requestMessagePort() and waited 4 seconds; no port ever arrived, so I’m not claiming a full bypass there.

But the synchronous part of requestMessagePort() runs before that check: it unconditionally calls webXMessageBusNegotiator.f9409j.a(), which I traced to RxJava’s Disposable.dispose() (via the xs.d EmptyDisposable class), on a single shared field that holds whatever handshake is currently pending. Any call to this method, from any frame regardless of origin, kills whatever handshake was already in progress — including, potentially, a legitimate one \*\*\* own trusted code just started. That’s a cross-frame DoS that doesn’t need the origin check to fail at all, because it happens before the check ever runs.

Both bugs come from the same root cause: a native bridge that should only be reachable from \*\*\*\* own top-level document is instead exposed to every iframe in the WebView, because addJavascriptInterface() isn’t frame-scoped. The frame-aware replacement, WebViewCompat.addWebMessageListener(), takes an explicit allowed-origins list and would have stopped both of these.

Any third-party \*\*\* App — no scopes, no permissions, no user interaction beyond just being opened — can write fake build/release metadata into \*\*\* own crash-reporting pipeline. Since the renderer-reclaim event that triggers this is routine (not just hard crashes), it’s easy to hit during normal use, and a malicious app publisher could use it to pollute \*\*\* own crash dashboards and release-health data with fabricated attribution.
