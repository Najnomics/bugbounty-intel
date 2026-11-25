# How an Android OAuth Custom Scheme Became a Full Account Takeover

- **Source URL:** https://medium.com/@mohamedatefsarhan123/how-an-android-oauth-custom-scheme-became-a-full-account-takeover-4a43cd9a51ac
- **Fetched from:** https://medium.com/@mohamedatefsarhan123/how-an-android-oauth-custom-scheme-became-a-full-account-takeover-4a43cd9a51ac?source=rss-25cced41232d------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 14916)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** 0xlight / Fri, 18 Sep 2026 00:10:50 GMT

OAuth is often treated as a solved problem: authenticate the user, issue an authorization code, exchange it for a token, and move on.

Mobile applications make that assumption dangerous.

While researching an Android application’s authentication flow, I encountered what initially looked like a relatively small implementation flaw: the application relied on a custom URI scheme to receive its OAuth callback. On its own, this creates an opportunity for another installed application to register the same scheme and intercept the callback.

The interesting part came next.

The intercepted authorization code was not protected by PKCE, meaning there was no cryptographic proof tying the code redemption to the application that originally initiated the authentication request. As a result, a code captured by an attacker-controlled application could be replayed from another device and exchanged for an authenticated session.

In this writeup, I’ll break down the vulnerability from the Android manifest level to the OAuth flow, show how the authorization code was intercepted and redeemed, explain why PKCE was the missing security boundary, and outline the changes that would prevent the attack.

The investigation started with the Android APK.

Rather than immediately attempting exploitation, I first mapped the authentication and deep-link behavior.

The main questions were:

How does the application start authentication?

Which OAuth client is used?

What redirect URI is registered?

How does Android receive the callback?

Is the callback protected by App Links?

Is PKCE used?

Can the authorization code be redeemed outside the application?

The APK was decoded and the Android manifest inspected.

For example:

apktool decode -f -s -o decoded victim.apk

grep -A5 'android:scheme' decoded/AndroidManifest.xml

The application contained two relevant intent filters.

The first was an HTTPS deep link using verification:

\<intent-filter android:autoVerify="true">

\<action android:name="android.intent.action.VIEW"/>

\<category android:name="android.intent.category.DEFAULT"/>

\<category android:name="android.intent.category.BROWSABLE"/>

\<data android:scheme="https"/>

\<data android:host="@string/deep\_link\_host"/>

\</intent-filter>

That is the expected Android App Link model.

The second was much more interesting:

\<intent-filter>

\<action android:name="android.intent.action.VIEW"/>

\<category android:name="android.intent.category.DEFAULT"/>

\<category android:name="android.intent.category.BROWSABLE"/>

\<data android:scheme="@string/custom\_scheme"/>

\</intent-filter>

There was no android:autoVerify="true".

The relevant scheme resolved to:

victim-app://

This immediately created a potential interception primitive.

Android custom URI schemes do not provide the same ownership verification mechanism as HTTPS App Links.

An application can register:

\<data android:scheme="victim-app"/>

without proving that it owns the namespace.

That means another application can declare the same scheme.

I created a minimal test application containing:

\<data android:scheme="victim-app"/>

\</intent-filter>

After installation, Android recognized the malicious application as a handler for:

victim-app://...

This could be verified with:

adb shell pm query-activities --brief \

-a android.intent.action.VIEW \

-d "victim-app://app/oauth-callback"

The malicious package appeared as an eligible handler.

At this point, there was a possible OAuth interception issue.

But interception alone does not automatically equal account takeover.

The next step was understanding the authentication flow.

The Android application did not perform the entire authentication process internally.

Instead, the application redirected the user into the system browser.

A decompiled portion of the application showed the authentication URL being constructed around the mobile OAuth client:

var loginLink =

webappUrl.origin +

"/oauth/login?client\_id=victim.mobile-app" +

"&redirect\_uri=" +

encodeURIComponent(

"victim-app://app/oauth-callback"

);

this.$window.location.href = loginLink;

This established several important facts:

OAuth client

↓

System browser

↓

Authentication

↓

Custom-scheme redirect

↓

Android Intent

↓

Application

The next question was whether the authorization request used PKCE.

A secure mobile OAuth authorization-code flow should normally use:

code\_challenge

code\_challenge\_method=S256

and later require:

code\_verifier

during token exchange.

I searched the client-side implementation and observed that the authorization request did not contain a PKCE challenge.

The request effectively looked like:

response\_type=code

client\_id=victim.mobile-app

redirect\_uri=victim-app://app/oauth-callback

with no:

code\_challenge=

code\_challenge\_method=S256

That was the first major indication that the authorization code might be usable by anyone who obtained it.

However, client-side behavior alone was not enough.

The server had to be tested.

I then examined the OAuth authorization endpoint.

A non-registered redirect URI was submitted as a control request.

Conceptually:

POST https://victim.com/api/oauth/authorize

Content-Type: application/x-www-form-urlencoded

response\_type=code

client\_id=victim.mobile-app

redirect\_uri=attacker://test

The server rejected the unknown redirect URI and indicated that the mobile client was restricted to its configured callback schemes.

The relevant observation was that the legitimate callback scheme was accepted:

victim-app://app/oauth-callback

The server therefore recognized the vulnerable custom scheme as a legitimate OAuth redirect target.

The next test was intentionally simple.

I compared authorization behavior with and without:

No meaningful enforcement difference appeared.

The authorization endpoint continued processing requests without requiring a challenge.

That meant PKCE was not merely absent from the mobile client.

It was also not enforced as a server-side requirement for the flow.

The security boundary that should have protected an intercepted authorization code was therefore missing.

To prove the Android side of the vulnerability, I created a minimal application that registered the same scheme:

The application extracted the authorization code from the incoming Intent:

Uri data = getIntent().getData();

String code =

(data != null)

? data.getQueryParameter("code")

: null;

The purpose was deliberately minimal:

Receive Intent

↓

Read code parameter

↓

Display captured authorization code

There was no special Android permission involved.

The vulnerability existed because the OAuth callback itself was claimable by another application.

The next step was to determine whether a callback containing an authorization code could actually reach the malicious application.

The OAuth redirect took the form:

victim-app://app/oauth-callback?code=\<AUTHORIZATION\_CODE>

I delivered the equivalent Android Intent:

adb shell am start \

-a android.intent.action.VIEW \

-d "victim-app://app/oauth-callback?code=\<AUTHORIZATION\_CODE>"

The interceptor application received it.

The application displayed:

This confirmed the first half of the attack chain:

OAuth Server

↓

Authorization Code

↓

Custom URI

↓

Android Intent Resolution

↓

Attacker-Controlled App

The authorization code was now in attacker-controlled memory.

The remaining question was whether the code could be exchanged for a session.

The authorization code was then submitted to the authentication backend from a separate machine.

The request was conceptually:

POST https://victim.com/api/auth/login

Content-Type: application/x-www-form-urlencoded

grant\_type=authorization\_code

code=\<STOLEN\_CODE>

No victim browser cookies were included.

No mobile-device state was included.

No password was included.

No MFA code was included.

Most importantly:

No code\_verifier

was supplied.

The server accepted the code and returned an authenticated access token.

The response indicated an authenticated session rather than a partially authenticated state.

The practical impact was **account takeover for affected mobile users under the demonstrated conditions**.

An attacker-controlled application required no special Android permission beyond being able to register the same custom URI scheme.

Once the victim completed authentication:

OAuth code

↓

intercepted

↓

redeemed

↓

authenticated session

The resulting session provided access to the victim’s authenticated API surface.

Depending on the application’s available permissions, this could include:

*— 0xlight*

Follow for more :

X : [Xaccount](https://x.com/lightx0yagumi) — — Linked : [account](https://www.linkedin.com/in/mohamed-sarhan-590b72279)
