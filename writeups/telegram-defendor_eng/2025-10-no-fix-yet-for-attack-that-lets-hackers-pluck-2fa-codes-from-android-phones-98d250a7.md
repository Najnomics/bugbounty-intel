# 📱 New Attack on Android Steals 2FA Codes Without Permissions

- **Source URL:** https://arstechnica.com/security/2025/10/no-fix-yet-for-attack-that-lets-hackers-pluck-2fa-codes-from-android-phones
- **Fetched:** 2026-11-12
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/872 (id 872)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
Android devices are vulnerable to a new attack that can covertly steal two-factor authentication codes, location timelines, and other private data in less than 30 seconds.

The new attack, named Pixnapping by the team of academic researchers who devised it, requires a victim to first install a malicious app on an Android phone or tablet. The app, which requires no system permissions, can then effectively read data that any other installed app displays on the screen. Pixnapping has been demonstrated on Google Pixel phones and the Samsung Galaxy S25 phone and likely could be modified to work on other models with additional work. Google released mitigations last month, but the researchers said a modified version of the attack works even when the update is installed.

## Like taking a screenshot

Pixnapping attacks begin with the malicious app invoking Android programming interfaces that cause the authenticator or other targeted apps to send sensitive information to the device screen. The malicious app then runs graphical operations on individual pixels of interest to the attacker. Pixnapping then exploits a [side channel](https://en.wikipedia.org/wiki/Side-channel_attack) that allows the malicious app to map the pixels at those coordinates to letters, numbers, or shapes.

“Anything that is visible when the target app is opened can be stolen by the malicious app using Pixnapping,” the researchers wrote on an [informational website](https://www.pixnapping.com). “Chat messages, 2FA codes, email messages, etc. are all vulnerable since they are visible. If an app has secret information that is not visible (e.g., it has a secret key that is stored but never shown on the screen), that information cannot be stolen by Pixnapping.”

The new attack class is reminiscent of [GPU.zip](https://arstechnica.com/security/2023/09/gpus-from-all-major-suppliers-are-vulnerable-to-new-pixel-stealing-attack/), a 2023 attack that allowed malicious websites to read the usernames, passwords, and other sensitive visual data displayed by other websites. It worked by exploiting side channels found in GPUs from all major suppliers. The vulnerabilities that GPU.zip exploited have never been fixed. Instead, the attack was blocked in browsers by limiting their ability to open iframes, an HTML element that allows one website (in the case of GPU.zip, a malicious one) to embed the contents of a site from a different domain.

It's a side channel attack. Basically the attacker renders something transparent in front of the target app, then using a timing attack exploiting the GPU's graphical data compression to try finding out the color of the pixels. It's not something as simple as "give me the pixels of another app showing on the screen right now." That's why it takes time and can be too slow to fit within the 30 seconds window of the Google Authenticator app.

My understsanding from the paper is that they use intent to launch the victim app, then SurfaceFlinger combines the windows together. By setting SurfaceControl's blur radius they can achieve this without the permission.

doesn'thave access to another app's rendering.
The app makes detailed time measurements of how long it takes to render

its owngraphics. Depending on what is already displayed on the screen (from the other app), individual pixels take longer to render in one color versus another. To the human eye the difference is imperceptible but it's long enough to measure statistically by an on-device process with access to precise time measurement APIs.
That's the nature of a side channel. The malicious app doesn't have direct access to what is rendered to the screen from another app. It must

inferwhat is rendered on the screen through timing measurements (or sometimes power measurements, vibration measurements, etc. depending on the side channel).
First, passkeys are a subset of FIDO-2/WebAuthn – I've been using Yubikeys for FIDO-2 across multiple devices and operating systems for almost half a decade and it's completely painless: faster than TOTP/SMS and easier to setup, and it works on mobile and desktop devices without any additional software installs required (unlike TOTP) so you can use it on locked-down devices, too.

Second, even for passkeys that article is old and not everything you mentioned is accurate in 2025. For example, if you are a Mac user who wants to use your passkey in Chrome, Edge, Firefox, and Safari that just works because they've all all shipped support for the system password store. Similarly, if you're a cross-platform user using 1Password, Bitwarden, etc. that's been fine for a while. The one remaining issue is support for the Passkey CXP protocol (which has shipped from Apple, Bitwarden, but not everyone) but that's only important for people who need cross-platform / cross-password manager support so e.g. the people who are all in on a single vendor like Apple, Google, or Microsoft or who use a single portable password manager don't need to wait for that.

It's also a relatively manageable problem since anyone implementing WebAuthn correctly allows multiple keys to be registered and so instead of being blocked, it just means that each family of password manager you use gets registered twice or, in the case of something like GitHub, you register your personal and work identities once and never think about it for years, except if you remember how it used to be slower to login but now it's fast.

It's caught on in sectors which care about security, and that includes most of the big tech companies – Google, Microsoft, Apple, AWS, Facebook, etc. and all of the major SSO providers support it, for example. Some less capable companies like banks haven't upgraded yet but that's largely because they tend to be very complacent about things which are not required by regulation and they can get away with that as long as people pretend that TOTP/SMS aren't routinely phished. I brought it up because we have to stop pretending those qualify as secure so the slackers feel the need to step into the current century.

As a similar comparison, remember when companies used to treat someone's social security number as an authenticator but after that was abused enough it became common to recognize that as negligence on the business's part? We need that same awareness for code-based MFA so they stop thinking of secure options like FIDO-2/WebAuthn as an extra cost and start seeing them as a way of saving money versus their insurers charging more to cover thefts involving easily-phished authentication and their auditors flagging it as a risk.
