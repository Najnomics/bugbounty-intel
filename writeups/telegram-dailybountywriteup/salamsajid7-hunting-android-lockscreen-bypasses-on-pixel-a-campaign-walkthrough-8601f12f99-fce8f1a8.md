# Hunting Android Lockscreen Bypasses on Pixel

- **Source URL:** https://medium.com/@salamsajid7/hunting-android-lockscreen-bypasses-on-pixel-a-campaign-walkthrough-8601f12f9963?source=rss------bug_bounty-5
- **Fetched from:** https://medium.com/feed/@salamsajid7
- **Fetched:** 2026-11-27
- **Channel:** @dailybountywriteup
- **Telegram message:**  (id 13859)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
We ran a focused campaign against the Android secure keyguard on a stock Pixel 9a (tegu, build CP1A.260505.005, locked bootloader, May 2026 ASB). The goal was the Google VRP top-tier category: Lock Screen Bypass — dismissing or escaping the secure keyguard *without* the user's PIN, pattern, password, or biometric.

This series documents every step: what we read, why we read it, what we ran, and what came back. Spoiler: zero full bypasses (so far), one incidental High-severity DoS and a much sharper map of where the soft spots are.

### Part 0 — Setup

- [01 — Threat Model & Campaign Design](https://markdownlivepreview.com/01-threat-model.md): why “lockscreen bypass” is five different problems, attacker tiers, and what counts as a win.

### Part I — Phase A: Static Source Review

Deep-reads of the AOSP source tree, one per component that participates in the keyguard state machine. Each produced a table of “observations” — concrete code paths that *might* dismiss the keyguard without auth, with file:line citations.

- [02 — L1: LockSettingsService](https://markdownlivepreview.com/02-L1-locksettings.md) — the credential store. Permission gates, the early-verify callback, and Resume-on-Reboot’s missing verified-boot check.
- [03 — L2: SystemUI Keyguard](https://markdownlivepreview.com/03-L2-systemui-keyguard.md) — the UI gate. Sixteen dismiss paths catalogued; the “half-unlocked window” confirmed.
- [04 — L3: TrustManagerService](https://markdownlivepreview.com/04-L3-trustmanager.md) — Extend Unlock. An inverted boolean guard, and why it (mostly) doesn’t matter.
- [05 — L4: Biometric Framework](https://markdownlivepreview.com/05-L4-biometrics.md) — why the keyguard never actually checks your fingerprint’s HardwareAuthToken.
- [06 — L5: WindowManager Occlusion](https://markdownlivepreview.com/06-L5-wm-occlusion.md) — the showWhenLocked machinery, and the one inheritance flag that matters.
- [07 — L6: SIM-PIN/PUK & Emergency](https://markdownlivepreview.com/07-L6-sim-emergency.md) — re-auditing CVE-2022–20465 in 2026.
- [08 — L7: Prior-Art Knowledge Base](https://markdownlivepreview.com/08-L7-prior-art.md) — eighteen historical bypasses distilled into seven invariants.

### Part II — Synthesis

- [09 — From 27 Observations to a Test Plan](https://markdownlivepreview.com/09-synthesis.md) — ranking, closing, and turning static notes into dynamic test tracks.

### Part III — Phase B: Dynamic Execution

What we actually ran on the device, and what came back.

- [10 — V12: Enumerating the Keyguard Binder Surface](https://markdownlivepreview.com/10-V12-binder-enum.md) — firing every ILockSettings/ITrustManager/IActivityTaskManager transaction from an unprivileged app.
- [11 — Incidental: Crashing system\_server From Any App](https://markdownlivepreview.com/11-V12-incidental-dos.md) — the registerTrustedPresentationListener(null) finding.
- [12 — V13: Occlusion Desync Baseline](https://markdownlivepreview.com/12-V13-occlusion-baseline.md) — eight ways to try to confuse KeyguardController, all of which held.
- [13 — V13b: The](https://markdownlivepreview.com/13-V13b-inherit-inventory.md) [inheritShowWhenLocked Inventory](https://markdownlivepreview.com/13-V13b-inherit-inventory.md) — scanning 233 system APKs for the one manifest attribute that grants lockscreen inheritance.
- [14 — V17(a): The Inverted Escrow-Token Guard, On Device](https://markdownlivepreview.com/14-V17a-escrow-config.md) — confirming O-L3–1 reads the way we thought it did.
- [15 — V22: Pivoting Out of Gemini Over the Lockscreen](https://markdownlivepreview.com/15-V22-assistant-pivot.md) — the Payatu/KB-LSB-18 sibling hunt: every button on the assistant overlay, and where each one goes.

### 01 — Threat Model & Campaign Design

*Why “lockscreen bypass” is five different problems wearing one trenchcoat.*

### The pivot

This campaign didn’t start as a lockscreen project. Lock Screen Bypass is its own top-tier reward category, separate from the AOSP severity rubric. A clean physical-access lockscreen bypass on a flagship Pixel pays at the top of the scale — and unlike kernel memory corruption, it's a *logic* problem space where careful reading can compete with fuzzing infrastructure.

### Step 1: Define the attacker

The first thing we did — before reading a single line of keyguard code — was nail down *who* the attacker is. Vulnerability research without a threat model produces findings that are technically true and practically worthless (“if you’re root, you can unlock the phone”).

We defined three tiers, ordered by VRP value:

TierCapabilityVRP standingTest rigLSB-APhysical only. Holds the locked device. No pre-installed app, no adb, no developer mode. May insert SIMs, attach USB accessories, use any UI affordance reachable from the lock screen (camera, emergency dialer, assistant, notifications).Top tierManual UI walks. Input scripted via USB-HID (Raspberry Pi Pico as a fake keyboard) where automation is needed; adb is observer-only — dumpsys/screencap/uiautomator dump to record state, never to drive the attack.LSB-BA pre-installed untrusted\_app (third-party APK, no special permissions) running in the background while the device is locked.Discounted ("requires installed app" modifier) but still High in the AOSP rubricOur poc-app/ test APK, with attack code firing from a Direct-Boot-aware service.LSB-CProximal radio — Bluetooth, NFC, Wi-Fi, cell broadcast — hitting a locked device with no installed app.Top tier (remote modifier)Out of scope for this iteration; needs RF hardware we didn't have on the bench.

Why this matters: a finding that needs adb shell is worthless for LSB-A (adb implies developer mode, which implies a prior unlock). A finding that needs a pre-installed app is real but discounted. We tagged every observation and every test with its tier so we'd never accidentally inflate a result.

### Step 2: Define “bypass”

“The lockscreen is bypassed” sounds binary. It isn’t. We wrote down four exit criteria, any one of which would qualify a finding for a FINDING-lsb-\*.md writeup:

1. EC1 — Keyguard dismissed. KeyguardManager.isKeyguardLocked() == false on a device with a secure LSKF (Lock Screen Knowledge Factor — PIN/pattern/password) set, without that LSKF or a valid biometric ever being supplied. The classic "you're at the home screen" outcome.
2. EC2 — Non-SWL activity interactive. An arbitrary activity that does *not* declare showWhenLocked is rendered, focused, and accepting input on top of the lockscreen, with home/recents/back routing to the launcher. The keyguard still *thinks* it's locked, but you're past it.
3. EC3 — CE data readable pre-unlock. Credential-Encrypted storage (the user’s actual files) readable before first unlock. This is the File-Based Encryption escape — arguably more valuable than EC1.
4. EC4 — Credential reset without proof. LockSettingsService clears or changes the user's credential without being given the old one.

Anything weaker — notification content already visible on the lockscreen, or denial-of-service against the keyguard — goes to ROBUSTNESS.md, not the findings list.

### Step 3: Decompose the surface

Here’s the insight that shaped the whole campaign: “the lockscreen” is not a component. It’s a distributed state machine spread across at least five processes, and a bypass is any edge in that state machine that goes from {locked, !authenticated} to {unlocked ∨ occluded-with-escape} without passing through the credential verifier.

We carved it into seven layers:

L#ComponentProcessWhy it matters

L1LockSettingsServicesystem\_serverStores the credential. Verifies it (via Weaver/Gatekeeper). Owns Synthetic Password, Resume-on-Reboot, escrow tokens. If you can make LSS say "no credential is set," you win.

L2KeyguardViewMediator + bouncercom.android.systemuiThe actual UI gate. Receives "verified" signals and decides whether to animate away. If you can make it call keyguardDone() without a real verify, you win.

L3TrustManagerServicesystem\_serverExtend Unlock (née Smart Lock). Trust agents can grant trust → keyguard dismisses without credential. If you can become a trust agent or spoof a grant, you win.

L4Biometric frameworksystem\_serverFingerprint/face. The HAL says "match" → framework tells keyguard. If you can inject a fake match, you win.

L5WM/ATMS KeyguardControllersystem\_serverDecides which activities are visible while the keyguard is up. Owns "occlusion" — showWhenLocked apps drawing over the lockscreen. If you can get a non-SWL activity resumed and focused while WM thinks the keyguard is occluded, you win EC2.

L6SIM-PIN/PUK + emergencysystemui + com.android.phonePhysical SIM swap drives keyguard state transitions. CVE-2022-20465 lived here. The emergency dialer is a showWhenLocked activity with a *lot* of buttons.

L7Prior art—Every public lockscreen bypass since 2013, abstracted into reusable patterns. Don't reinvent; variant-hunt.

### Step 4: Two-phase plan

Phase A — Static. Seven parallel source-code reviews, one per layer, no device required. Each review produces an *observation table*: rows of the form “at file:line, under trigger X, the code might do Y, which would be a bypass because Z, confidence W.” Observations get IDs (O-L1-1, O-L3-3, …) so we can reference them across documents.

Why static first? Because the keyguard surface is enormous and device time is expensive. Reading the code lets us throw away 90% of the hypothesis space before we touch the phone — and the remaining 10% comes with file:line citations we can put a debugger on.

Phase B — Dynamic. A synthesis step ranks all Phase-A observations by (impact if true) × (probability) × (attacker tier) ÷ (cost to test), groups them into V-tracks (V12, V13, …), and executes them on the live device in priority order.

### Step 5: Standing constraints

Three rules we held for the entire campaign:

1. The bootloader stays locked. A bypass that requires fastboot oem unlock isn't a bypass.
2. No adb in the LSB-A attack path. If a “physical only” finding needs adb shell input tap, it's not physical-only — it's "physical plus the victim left developer mode on." We use adb to *observe* (dumpsys, screencap, uiautomator dump) but never to *act* in any test we'd report as tier-A.
3. Verify on the actual build. Our on-disk AOSP source snapshot is slightly older than the device’s CP1A.260505.005 build. Every file:line citation in a finding gets re-checked against the running device before we'd write it up.

That’s the design. The next seven posts walk through Phase A — what we found in each layer, and why.

### 02 — L1: LockSettingsService — The Credential Store

*Phase A static review · frameworks/base/services/core/java/com/android/server/locksettings/*

LockSettingsService (LSS) is where the user's credential lives. It owns the Synthetic Password (the actual key that protects Credential-Encrypted storage), talks to Weaver and Gatekeeper (the hardware that rate-limits guesses), and exposes the ILockSettings binder interface that everything else calls to verify a PIN. If we can make LSS believe there's no credential, or make it emit "verified" without a real verify, we win outright.

So we read it. All of it. Here’s the process and the seven things we flagged.

### Step 1: Map every binder transaction to its permission gate

The first question for any system service is: what can an unprivileged app call? We went through ILockSettings.aidl method by method and traced each implementation in LockSettingsService.java to its permission check.

The answer: almost nothing. LSS guards essentially every method with one of two signature-level permissions — ACCESS\_KEYGUARD\_SECURE\_STORAGE (the big one) or MANAGE\_BIOMETRIC. An untrusted\_app holds neither.

A representative slice of the table:

AIDL methodGate (LSS line)untrusted\_app reachable?setLong / setString / setBooleancheckWritePermission (:1404–1418)NosetLockCredentialACCESS\_KEYGUARD\_SECURE\_STORAGE ∨ SET\_AND\_VERIFY\_… ∨ (SET\_INITIAL\_LOCK ∧ savedCred=None) (:1850–1857)NoverifyCredential / checkCredentialcheckPasswordReadPermission (:2352, :2366)NouserPresentcheckWritePermission (:2705)NorequireStrongAuthcheckWritePermission (:2687)No — and only ever *raises* the barhasSecureLockScreennone (:1336)Yes — but it's a benign one-bit readstartRemoteLockscreenValidationnone in LSS (:2858) — delegatedsee

O-L1-6

Out of \~50 transactions, exactly one (hasSecureLockScreen) is ungated, and it's a harmless boolean read. Two more (startRemoteLockscreenValidation / validateRemoteLockscreen) have *no check inside LSS itself* — they delegate to RecoverableKeyStoreManager.

We flagged that for a closer look (O-L1-6) and later closed it dynamically in V12: the delegated check (CHECK\_REMOTE\_LOCKSCREEN, signature) holds.

Reasoning behind doing this first: if there were an ungated mutator, the campaign would be over on day one. There isn’t. The binder boundary is closed for tier-B attackers — which means every L1 attack path needs a *confused deputy* (a privileged app we can trick into calling LSS for us). That reframes the rest of the L1 work.

### Step 2: Look for unlock-signal-before-verify ordering bugs

LSS doesn’t just store the credential; it verifies it. The verify flow is doVerifyCredential → SyntheticPasswordManager.unlockLskfBasedProtector → Weaver/Gatekeeper → unwrap SP blob → second verifyChallenge → onCredentialVerified → unlock CE storage / keystore / strong-auth.

We walked that flow asking one question at every step: is there any signal emitted to the outside world before the hardware verify completes?

We found one. At SyntheticPasswordManager.java:1499–1505:

// SPM:1497 — comment: "should be correct"

if (progressCallback != null) {

progressCallback.onCredentialVerified(); // ← fires HERE

}

result.syntheticPassword = unwrapSyntheticPasswordBlob(...); // SPM:1506

// ...

result.gkResponse = verifyChallenge(...); // SPM:1510

progressCallback.onCredentialVerified() fires *after* the first-stage Weaver/Gatekeeper match (so the user did type the right PIN) but before the SP blob unwrap and before the second verifyChallenge. If either of those later stages fails — corrupt blob, Keystore key gone, GK hiccup — LSS will return ERROR, but the keyguard UI has *already received "verified"*.

This became O-L1–2, and the obvious next question — “does SystemUI actually dismiss on that early callback alone?” — got handed to the L2 review. (Spoiler from post 03: yes, it does. The combination became our V18 test track.)

Why this ordering matters: it’s not a credential *bypass* — Weaver matched, the user knew the PIN. But it’s a window where the UI says “unlocked” while CE storage and keystore say “nope.” On a device where an attacker can *induce* the stage-2 failure (full /data, wedged Keystore), they get a launcher with no credential-bound keys. We logged it as confidence L for exploitability but M for "this is a real ordering gap."

### Step 3: Audit Resume-on-Reboot

Resume-on-Reboot (RoR) is the mechanism that lets your phone apply an OTA update overnight and come back unlocked without you typing your PIN. It works by escrowing the Synthetic Password before reboot: SP → E(K\_k, E(K\_s, SP)) on disk, where K\_s is held by a HAL (or server-wrapped) and K\_k is an Android Keystore key.

The trigger chain is: LockSettingsService.systemReady() → RebootEscrowManager.loadRebootEscrowDataIfAvailable → getAndClearRebootEscrowKey → restoreRebootEscrowForUser → onRebootEscrowRestored (LSS:3867) → onCredentialVerified → full unlock chain.

We asked: between reading the encrypted blob from disk and calling onCredentialVerified, what cryptographic checks gate the path?

GateVerdictK\_s retrieval from HALNo challenge. IRebootEscrow.retrieveKey returns 32 bytes; if non-zero, accepted (HalImpl:85–99).K\_k from KeystoreCreated with no setUserAuthenticationRequired (RebootEscrowKeyStoreManager.java:110–118) — usable from cold boot. By design.AES-GCM decrypt of the SP blobReal gate. Wrong K\_s or K\_k → GCM tag fails → IOException → abort.verifyChallenge(GK, sp, 0, userId) at LSS:3873Return value discarded. onCredentialVerified (LSS:3876) runs unconditionally.vbmeta-digest match (REM:690–717)Computed, but fed only to metrics (REM:733–754). Mismatch does not abort.

That’s two observations:

- O-L1–3: the framework adds no GK/Weaver/HAT check on top of the escrowed SP. If a vendor IRebootEscrow HAL persists K\_s across a cold boot or battery pull, the framework will happily reconstitute the SP and unlock. Security rests entirely on the HAL doing the right thing. Confidence M (framework correctness), exploitability vendor-dependent.
- O-L1–4: the verified-boot binding is decorative. An attacker who can boot a *different* signed image while preserving the HAL’s K\_s and /data blobs gets the SP without the framework noticing the vbmeta digest changed. AVB rollback protection *should* block this independently — but the framework's own check is a metric, not a gate. Confidence L–M.

We parked both for a possible later track (V18 variant b) — they’re real defence-in-depth gaps but need HAL- or boot-chain-level preconditions we couldn’t reach from our threat model on Pixel.

### Step 4: Can user 0’s credential be cleared without the old one?

We inventoried every code path that destroys or rewrites the Synthetic Password protector for user 0:

PathOld credential required?setLockCredentialInternal → setLockCredentialWithSpLockedYes — unlockLskfBasedProtector(savedCredential) must succeed first (LSS:1952–1968)removeUserState (user-removal lifecycle)UMS refuses to remove user 0removeStateForReusedUserIdIfNecessaryExplicit if (userId == USER\_SYSTEM) return; (LSS:886–888)setLockCredentialWithToken (escrow)Needs a valid escrow token (DPC-provisioned)setLong("sp-handle", 0, 0) via binderNo old credential — only ACCESS\_KEYGUARD\_SECURE\_STORAGE

That last row is O-L1–5, and it’s the most interesting thing in L1. setLong (LSS:1410–1414) has no key allowlist — a caller with the signature permission can write *any* key, including CURRENT\_LSKF\_BASED\_PROTECTOR\_ID\_KEY ("sp-handle"). Set it to 0 and:

- getCurrentLskfBasedProtectorId (LSS:3035) returns NULL\_PROTECTOR\_ID
- → getCredentialTypeInternal (LSS:1515–1517) returns CREDENTIAL\_TYPE\_NONE
- → LockPatternUtils.isSecure() returns false
- → KeyguardSecurityModel picks SecurityMode.None
- → swipe to dismiss.

The real protector blob, Weaver slot, and GK enrollment are all still on disk — so CE storage stays locked at next boot — but on the *current* boot, on an already-AFU device, the keyguard UI is gone.

This needs a confused deputy: some app holding ACCESS\_KEYGUARD\_SECURE\_STORAGE (SystemUI, Settings, NFC, possibly OEM additions) that we can trick into calling ILockSettings.setLong with our key. We didn't find one in Phase A; the deputy hunt became V19.

### Step 5: The remaining flags

Two more observations rounded out the table:

- O-L1–1 (userPresent, LSS:2704–2707): clears all STRONG\_AUTH\_REQUIRED\_\* flags for any user with no proof of credential — only the signature permission. Not itself a dismiss, but a strong-auth *downgrade* primitive: it re-enables biometric/trust-agent unlock when policy demanded the PIN. Pair with L3/L4 for impact.
- O-L1–7 (setLockCredential, LSS:1850–1857): the SET\_INITIAL\_LOCK permission branch checks savedCredential.isNone() — a *caller-supplied* value — rather than !isUserSecure(userId). The inner crypto check still catches it (real stored type ≠ NONE → unlockLskfBasedProtector fails), so it's not exploitable, but the outer policy gate is weaker than intended. Confidence L.

### Output: the L1 observation table

Seven observations, summarised:

IDWhatTierO-L1–1userPresent(uid) clears strong-auth with no proofB (deputy)O-L1-2progressCallback.onCredentialVerified() fires before SP unwrapA/BO-L1-3RoR verifyChallenge return ignored; HAL is sole gateA (HAL)O-L1-4RoR vbmeta-mismatch is metrics-only, doesn't abortA (boot)O-L1-5setLong("sp-handle",0,0) → swipe-to-dismissB (deputy)O-L1-6Remote-lockscreen validation: no LSS-side check (delegated)BO-L1-7SET\_INITIAL\_LOCK checks caller-supplied savedCredential.isNone()B (role)

The headline result for L1: the binder surface is closed to unprivileged apps. Every interesting L1 attack needs either a signature-permission confused-deputy (O-L1–1, O-L1–5) or a way to wedge the verify pipeline mid-flight (O-L1–2, O-L1–3). Those became the V19 and V18 dynamic tracks respectively.

Three explicit hand-offs to other layers:

- → L2: does the early progressCallback (O-L1-2) actually drive KeyguardViewMediator to keyguardDone?
- → L2/L3: what’s the blast radius of O-L1–1 — does clearing strong-auth alone let a policy-blocked biometric dismiss the keyguard?
- → L7/V19: map every holder of ACCESS\_KEYGUARD\_SECURE\_STORAGE on stock Pixel for the deputy hunt.
