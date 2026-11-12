# Repository security advisories: electron/electron (70 published)

Verbatim from GitHub API `repos/electron/electron/security-advisories` on 2026-11-12.

## GHSA-6vrv-94jv-crrg — Context isolation bypass via Promise.then bug in V8
- CVE: CVE-2020-15096 | Severity: high | CVSS: None `None` | CWE: 
- Published: 2020-07-06T19:16:54Z | URL: https://github.com/electron/electron/security/advisories/GHSA-6vrv-94jv-crrg
- Affected npm/electron: vulnerable >=9.0.0-beta.0 <=9.0.0-beta.20 || >=8.0.0-beta.0 <=8.2.3 || >= 7.0.0-beta < =7.2.3 || >= 6.0.0-beta.0 <= 6.1.10 || <= 6 patched 9.0.0-beta.21, 8.2.4, 7.2.4, 6.1.11
- Credits: MarshallOfSound

### Impact
Apps using `contextIsolation` are affected.

This is a context isolation bypass, meaning that code running in the main world context in the renderer can reach into the isolated Electron context and perform privileged actions.

### Workarounds
There are no app-side workarounds, you must update your Electron version to be protected.

### Fixed Versions
* `9.0.0-beta.21`
* `8.2.4`
* `7.2.4`
* `6.1.11`

### For more information
If you have any questions or comments about this advisory:
* Email us at [security@electronjs.org](mailto:security@electronjs.org)


## GHSA-f9mq-jph6-9mhm — Arbitrary file read via window-open IPC
- CVE: CVE-2020-4075 | Severity: low | CVSS: None `None` | CWE: 
- Published: 2020-07-06T19:16:58Z | URL: https://github.com/electron/electron/security/advisories/GHSA-f9mq-jph6-9mhm
- Affected npm/electron: vulnerable >=9.0.0-beta.0 <=9.0.0-beta.20 || >=8.0.0-beta.0 <=8.2.3 || >= 7.0.0-beta < =7.2.3 || <7 patched 7.2.4,8.2.4,9.0.0-beta.21

### Impact
The vulnerability allows arbitrary local file read by defining unsafe window options on a child window opened via window.open.

### Workarounds
Ensure you are calling `event.preventDefault()` on all [`new-window`](https://electronjs.org/docs/api/web-contents#event-new-window) events where the `url` or `options` is not something you expect.

### Fixed Versions
* `9.0.0-beta.21`
* `8.2.4`
* `7.2.4`

### For more information
If you have any questions or comments about this advisory:
* Email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-m93v-9qjc-3g79 — Context isolation bypass via leaked cross-context objects
- CVE: CVE-2020-4076 | Severity: high | CVSS: None `None` | CWE: 
- Published: 2020-07-06T19:17:01Z | URL: https://github.com/electron/electron/security/advisories/GHSA-m93v-9qjc-3g79
- Affected npm/electron: vulnerable >=9.0.0-beta.0 <=9.0.0-beta.20 || >=8.0.0-beta.0 <=8.2.3 || >= 7.0.0-beta < =7.2.3 || <7 patched 7.2.4,8.2.4,9.0.0-beta.21

### Impact
Apps using `contextIsolation` are affected.

This is a context isolation bypass, meaning that code running in the main world context in the renderer can reach into the isolated Electron context and perform privileged actions.

### Workarounds
There are no app-side workarounds, you must update your Electron version to be protected.

### Fixed Versions
* `9.0.0-beta.21`
* `8.2.4`
* `7.2.4`

### Non-Impacted Versions
* `9.0.0-beta.*`

### For more information
If you have any questions or comments about this advisory:
* Email us at [security@electronjs.org](mailto:security@electronjs.org)


## GHSA-h9jc-284h-533g — Context isolation bypass via contextBridge
- CVE: CVE-2020-4077 | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2020-07-06T19:17:05Z | URL: https://github.com/electron/electron/security/advisories/GHSA-h9jc-284h-533g
- Affected npm/electron: vulnerable >=9.0.0-beta.0 <=9.0.0-beta.20 || >=8.0.0-beta.0 <=8.2.3 || >= 7.0.0-beta < =7.2.3 || <7 patched 7.2.4,8.2.4,9.0.0-beta.21

### Impact
Apps using both `contextIsolation` and `contextBridge` are affected.

This is a context isolation bypass, meaning that code running in the main world context in the renderer can reach into the isolated Electron context and perform privileged actions.

### Workarounds
There are no app-side workarounds, you must update your Electron version to be protected.

### Fixed Versions
* `9.0.0-beta.21`
* `8.2.4`
* `7.2.4`

### For more information
If you have any questions or comments about this advisory:
* Email us at [security@electronjs.org](mailto:security@electronjs.org)


## GHSA-56pc-6jqp-xqj8 — Context isolation bypass via prevented window.open
- CVE: CVE-2020-15215 | Severity: low | CVSS: None `None` | CWE: 
- Published: 2020-10-05T21:32:05Z | URL: https://github.com/electron/electron/security/advisories/GHSA-56pc-6jqp-xqj8
- Affected npm/electron: vulnerable >=11.0.0-beta.0 <=11.0.0-beta.5 || >=10.0.0-beta.0 <=10.1.1 || >=9.0.0-beta.0 <=9.3.0 || >=8.0.0-beta.0 <=8.5.1 <= 8 patched 11.0.0-beta.6, 10.1.2, 9.3.1, 8.5.2
- Credits: nornagon, MarshallOfSound

### Impact
Apps using both `contextIsolation` and `sandbox: true` are affected.
Apps using both `contextIsolation` and `nativeWindowOpen: true` are affected.

This is a context isolation bypass, meaning that code running in the main world context in the renderer can reach into the isolated Electron context and perform privileged actions.

### Workarounds
There are no app-side workarounds, you must update your Electron version to be protected.

### Fixed Versions
* `11.0.0-beta.6`
* `10.1.2`
* `9.3.1`
* `8.5.2`

### For more information
If you have any questions or comments about this advisory:
* Email us at [security@electronjs.org](mailto:security@electronjs.org)


## GHSA-2q4g-w47c-4674 — Unpreventable top-level navigation
- CVE: CVE-2020-15174 | Severity: high | CVSS: None `None` | CWE: 
- Published: 2020-10-05T21:32:11Z | URL: https://github.com/electron/electron/security/advisories/GHSA-2q4g-w47c-4674
- Affected npm/electron: vulnerable >=10.0.0-beta.0 <=10.0.0 || >=9.0.0-beta.0 <=9.2.1 || >=8.0.0-beta.0 <=8.5.0 <= 8 patched 11.0.0-beta.1, 10.0.1, 9.3.0, 8.5.1
- Credits: masatokinugawa

### Impact
The `will-navigate` event that apps use to prevent navigations to unexpected destinations [as per our security recommendations](https://www.electronjs.org/docs/tutorial/security) can be bypassed when a sub-frame performs a top-frame navigation across sites.

### Patches

* `11.0.0-beta.1`
* `10.0.1`
* `9.3.0`
* `8.5.1`

### Workarounds
Sandbox all your iframes using the [`sandbox` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-sandbox).  This will prevent them creating top-frame navigations and is good practice anyway.

### For more information
If you have any questions or comments about this advisory:

* Email us at security@electronjs.org


## GHSA-hvf8-h2qh-37m9 — ID collision when routing IPC messages to renderers containing OOPIFs
- CVE: CVE-2020-26272 | Severity: medium | CVSS: None `None` | CWE: 
- Published: 2021-01-26T22:21:40Z | URL: https://github.com/electron/electron/security/advisories/GHSA-hvf8-h2qh-37m9
- Affected npm/electron: vulnerable >=9.0.0-beta.0 < 9.4.0 || >= 10.0.0-beta.0 < 10.2.0 || >= 11.0.0-beta.0 < 11.1.0 || >= 12.0.0-beta.0 < 12.0.0-beta.9 || <= 8 patched 9.4.0, 10.2.0, 11.1.0, 12.0.0-beta.9
- Credits: nornagon

### Impact
IPC messages sent from the main process to a subframe in the renderer process, through `webContents.sendToFrame`, `event.reply` or when using the `remote` module, can in some cases be delivered to the wrong frame.

If your app does ANY of the following, then it is impacted by this issue:
- Uses `remote`
- Calls `webContents.sendToFrame`
- Calls `event.reply` in an IPC message handler

### Patches
This has been fixed in the following versions:

- 9.4.0
- 10.2.0
- 11.1.0
- 12.0.0-beta.9

### Workarounds
There are no workarounds for this issue.

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org).


## GHSA-mpjm-v997-c4h4 — Sandboxed renderers can obtain thumbnails of arbitrary files through the nativeImage API
- CVE: CVE-2021-39184 | Severity: medium | CVSS: 6.8 `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:N/A:N` | CWE: CWE-668
- Published: 2021-10-12T18:41:08Z | URL: https://github.com/electron/electron/security/advisories/GHSA-mpjm-v997-c4h4
- Affected npm/electron: vulnerable >=10.1.0 <11.0.0-beta.1 || >=11.0.0-beta.1 < 11.5.0 || >=12.0.0-beta.1 < 12.1.0 || >=13.0.0-beta.1 <13.3.0 || >=14.0.0-beta.1 <14.0.0 || >=15.0.0-alpha.1 <15.0.0-alpha.10 patched 11.5.0, 12.1.0, 13.3.0, 14.0.0, 15.0.0-alpha.10
- Credits: nornagon

### Impact
This vulnerability allows a sandboxed renderer to request a "thumbnail" image of an arbitrary file on the user's system. The thumbnail can potentially include significant parts of the original file, including textual data in many cases.

All current stable versions of Electron are affected.

### Patches
This was fixed with #30728, and the following Electron versions contain the fix:

- 15.0.0-alpha.10
- 14.0.0
- 13.3.0
- 12.1.0
- 11.5.0

### Workarounds
If your app enables `contextIsolation`, this vulnerability is significantly more difficult for an attacker to exploit.

Further, if your app does not depend on the `createThumbnailFromPath` API, then you can simply disable the functionality. In the main process, before the 'ready' event:
```js
delete require('electron').nativeImage.createThumbnailFromPath
```

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org).

## GHSA-3p22-ghq8-v749 — Renderers can obtain access to random bluetooth device without permission
- CVE: CVE-2022-21718 | Severity: low | CVSS: 3.4 `CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:C/C:L/I:N/A:N` | CWE: 
- Published: 2022-03-21T22:53:45Z | URL: https://github.com/electron/electron/security/advisories/GHSA-3p22-ghq8-v749
- Affected npm/electron: vulnerable < 13.6.6 || >=14.0.0-beta.1 < 14.2.4 || >=15.0.0-beta.1 <15.3.5 || >=16.0.0-beta.1 <16.0.6 || >=17.0.0-alpha.1 <17.0.0-alpha.6 patched 13.6.6, 14.2.4, 15.3.5, 16.0.6, 17.0.0-alpha.6
- Credits: PalmerAL

### Impact
This vulnerability allows renderers to obtain access to a random bluetooth device via the [web bluetooth API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Bluetooth_API) if the app has not configured a custom `select-bluetooth-device` event handler.  The device that is accessed is random and the attacker would have no way of selecting a specific device.

All current stable versions of Electron are affected.

### Patches
This has been patched and the following Electron versions contain the fix:
* `17.0.0-alpha.6`
* `16.0.6`
* `15.3.5`
* `14.2.4`
* `13.6.6`

### Workarounds
Adding this code to your app can workaround the issue.

```js
app.on('web-contents-created', (event, webContents) => {
  webContents.on('select-bluetooth-device', (event, devices, callback) => {
    // Prevent default behavior
    event.preventDefault();
    // Cancel the request
    callback('');
  });
});
```

For more information
If you have any questions or comments about this advisory, email us at security@electronjs.org.

## GHSA-mq8j-3h7h-p8g7 — Compromised child renderer processes could obtain IPC access without nodeIntegrationInSubFrames being enabled
- CVE: CVE-2022-29247 | Severity: medium | CVSS: 5.5 `CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:C/C:L/I:L/A:L` | CWE: 
- Published: 2022-06-13T20:13:48Z | URL: https://github.com/electron/electron/security/advisories/GHSA-mq8j-3h7h-p8g7
- Affected npm/electron: vulnerable < 15.5.5 || >= 16.0.0-beta.1 < 16.2.6 || >= 17.0.0-beta.1 < 17.2.0 || >= 18.0.0-beta.1 < 18.0.0-beta.6 patched 15.5.5, 16.2.6, 17.2.0, 18.0.0-beta.6
- Credits: TheGrandPew, msrkp

### Impact
This vulnerability allows a renderer with JS execution to obtain access to a new renderer process with `nodeIntegrationInSubFrames` enabled which in turn allows effective access to `ipcRenderer`.

Please note the misleadingly named `nodeIntegrationInSubFrames` option does not implicitly grant Node.js access rather it depends on the existing `sandbox` setting.  If your application is sandboxed then `nodeIntegrationInSubFrames` just gives access to the sandboxed renderer APIs (which includes `ipcRenderer`).

If your application then additionally exposes IPC messages without IPC `senderFrame` validation that perform privileged actions or return confidential data this access to `ipcRenderer` can in turn compromise your application / user even with the sandbox enabled.

### Patches
This has been patched and the following Electron versions contain the fix:

* `18.0.0-beta.6`
* `17.2.0`
* `16.2.6`
* `15.5.5`

### Workarounds
Ensure that all IPC message handlers appropriately validate `senderFrame` as per our [security tutorial here](https://github.com/electron/electron/blob/main/docs/tutorial/security.md#17-validate-the-sender-of-all-ipc-messages).

### For more information

If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org).

## GHSA-77xc-hjv8-ww97 — AutoUpdater module fails to validate certain nested components of the bundle on macOS
- CVE: CVE-2022-29257 | Severity: medium | CVSS: 6.6 `CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H` | CWE: 
- Published: 2022-06-13T20:13:54Z | URL: https://github.com/electron/electron/security/advisories/GHSA-77xc-hjv8-ww97
- Affected npm/electron: vulnerable < 15.5.0 || >= 16.0.0-beta.1 < 16.2.0 || >= 17.0.0-beta.1 < 17.2.0 || >= 18.0.0-beta.1 < 18.0.0-beta.6 patched 15.5.0, 16.2.0, 17.2.0, 18.0.0-beta.6

### Impact
This vulnerability allows attackers who have control over a given apps update server / update storage to serve maliciously crafted update packages that pass the code signing validation check but contain malicious code in some components.

Please note that this kind of attack would require **significant** privileges in your own auto updating infrastructure and the ease of that attack entirely depends on your infrastructure security.

### Patches
This has been patched and the following Electron versions contain the fix:

* `18.0.0-beta.6`
* `17.2.0`
* `16.2.0`
* `15.5.0`

### Workarounds
There are no workarounds for this issue, please update to a patched version of Electron.

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org).

## GHSA-p2jh-44qj-pf2v — Exfiltration of hashed SMB credentials on Windows via file:// redirect
- CVE: CVE-2022-36077 | Severity: medium | CVSS: 5.4 `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:L/I:N/A:L` | CWE: CWE-200
- Published: 2022-11-07T18:36:51Z | URL: https://github.com/electron/electron/security/advisories/GHSA-p2jh-44qj-pf2v
- Affected npm/electron: vulnerable < 18.3.7, >= 19.0.0-beta.1 < 19.0.11, >= 20.0.0-beta.1 < 20.0.1 patched 18.3.7, 19.0.11, 20.0.1
- Credits: coolcoolnoworries

### Impact
When following a redirect, Electron delays a check for redirecting to file:// URLs from other schemes. The contents of the file is not available to the renderer following the redirect, but if the redirect target is a SMB URL such as `file://some.website.com/`, then in some cases, Windows will connect to that server and attempt NTLM authentication, which can include sending hashed credentials.

### Patches
This issue has been fixed in all current stable versions of Electron. Specifically, these versions contain the fixes:

- 21.0.0-beta.1
- 20.0.1
- 19.0.11
- 18.3.7

We recommend all apps upgrade to the latest stable version of Electron.

### Workarounds
If upgrading isn't possible, this issue can be addressed without upgrading by preventing redirects to file:// URLs in the `WebContents.on('will-redirect')` event, for all WebContents:

```js
app.on('web-contents-created', (e, webContents) => {
  webContents.on('will-redirect', (e, url) => {
    if (/^file:/.test(url)) e.preventDefault()
  })
})
```

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org).

### Credit
Thanks to user @coolcoolnoworries for reporting this issue.

## GHSA-gxh7-wv9q-fwfr — Content-Secrity-Policy disabling eval not applied consistently in renderers with sandbox disabled
- CVE: CVE-2023-23623 | Severity: high | CVSS: 7.5 `CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H` | CWE: 
- Published: 2023-09-06T08:36:35Z | URL: https://github.com/electron/electron/security/advisories/GHSA-gxh7-wv9q-fwfr
- Affected npm/electron: vulnerable >= 22.0.0-beta.1 < 22.0.1, >= 23.0.0-alpha.1 < 23.0.0-alpha.2 patched 22.0.1, 23.0.0-alpha.2
- Credits: andreasdj

### Impact
A Content-Security-Policy that disables eval, specifically setting a `script-src` directive and _not_ providing `unsafe-eval` in that directive, is not respected in renderers that have sandbox and contextIsolation disabled.  i.e. `sandbox: false` and `contextIsolation: false` in the `webPreferences` object.

This resulted in incorrectly allowing usage of methods like `eval()` and `new Function`, which can result in an expanded attack surface.

### Patches
This issue only ever affected the 22 and 23 major versions of Electron and has been fixed in the latest versions of those release lines. Specifically, these versions contain the fixes:

- 22.0.1
- 23.0.0-alpha.2

We recommend all apps upgrade to the latest stable version of Electron, especially if they use `sandbox: false` or `contextIsolation: false`.

### Workarounds
If upgrading isn't possible, this issue can be addressed without upgrading by enabling at least one of `sandbox: true` or `contextIsolation: true` on all renderers.

```js
const mainWindow = new BrowserWindow({
  webPreferences: {
    sandbox: true,
  }
});
```

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org).

### Credit
Thanks to user @andreasdj for reporting this issue.

## GHSA-p7v2-p9m8-qqg7 — Context isolation bypass via nested unserializable return value
- CVE: CVE-2023-29198 | Severity: medium | CVSS: 6.0 `CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:L/I:L/A:L` | CWE: 
- Published: 2023-09-06T08:38:46Z | URL: https://github.com/electron/electron/security/advisories/GHSA-p7v2-p9m8-qqg7
- Affected npm/electron: vulnerable < 22.3.6 || >= 23.0.0-alpha.1 < 23.2.3 || >= 24.0.0-alpha.1 < 24.0.1 || >= 25.0.0-alpha.1 < 25.0.0-alpha.2 patched 22.3.6, 23.2.3, 24.0.1, 25.0.0-alpha.2
- Credits: MarshallOfSound, nornagon

### Impact
Apps using `contextIsolation` and `contextBridge` are affected.

This is a context isolation bypass, meaning that code running in the main world context in the renderer can reach into the isolated Electron context and perform privileged actions.

### Workarounds
This issue is exploitable under either of two conditions:
* If an API exposed to the main world via `contextBridge` can return an object or array that contains a JS object which cannot be serialized, for instance, a canvas rendering context. This would normally result in an exception being thrown `Error: object could not be cloned`.
* If an API exposed to the main world via `contextBridge` has a return value that throws a user-generated exception while being sent over the bridge, for instance a dynamic getter property on an object that throws an error when being computed.

The app side workaround is to ensure that such a case is not possible. Ensure all values returned from a function exposed over the context bridge are [supported](https://www.electronjs.org/docs/latest/api/context-bridge#parameter--error--return-type-support) and that any objects returned from functions do not have dynamic getters that can throw exceptions.

Auditing your exposed API is likely to be quite difficult so we strongly recommend you update to a patched version of Electron.

### Fixed Versions
* `25.0.0-alpha.2`
* `24.0.1`
* `23.2.3`
* `22.3.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-7x97-j373-85x5 — Out-of-package code execution when launched with arbitrary cwd
- CVE: CVE-2023-39956 | Severity: medium | CVSS: 6.1 `CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:L/I:H/A:L` | CWE: 
- Published: 2023-09-06T08:39:47Z | URL: https://github.com/electron/electron/security/advisories/GHSA-7x97-j373-85x5
- Affected npm/electron: vulnerable < 22.3.19 || >= 23.0.0-alpha.1 < 23.3.13 || >= 24.0.0-alpha.1 < 24.7.1 || >= 25.0.0-alpha.1 < 25.5.0 || >= 26.0.0-alpha.1 < 26.0.0-beta.13 patched 26.0.0-beta.13, 25.5.0, 24.7.1, 23.3.13, 22.3.19
- Credits: SimonSiefke, MarshallOfSound

### Impact
Apps that are launched as command line executables are impacted.  E.g. if your app exposes itself in the path as `myapp --help`

Specifically this issue can only be exploited if the following conditions are met:
* Your app is launched with an attacker-controlled working directory
* The attacker has the ability to write files to that working directory

This makes the risk quite low, in fact normally issues of this kind are considered outside of our threat model as similar to Chromium we exclude [Physically Local Attacks](https://github.com/electron/electron/security/advisories/GHSA-7x97-j373-85x5#:~:text=Physically%20Local%20Attacks) but given the ability for this issue to bypass certain protections like ASAR Integrity it is being treated with higher importance.  Please bear this in mind when reporting similar issues in the future.

### Workarounds
There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions
* `26.0.0-beta.13`
* `25.5.0`
* `24.7.1`
* `23.3.13`
* `22.3.19`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-7m48-wc93-9g85 — ASAR Integrity bypass via filetype confusion
- CVE: CVE-2023-44402 | Severity: medium | CVSS: 6.1 `CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:L/I:H/A:L` | CWE: 
- Published: 2023-12-01T19:45:51Z | URL: https://github.com/electron/electron/security/advisories/GHSA-7m48-wc93-9g85
- Affected npm/electron: vulnerable < 22.3.24 || >= 23.0.0-alpha.1 < 23.3.14 || >= 24.0.0-alpha.1 < 24.8.3 || >= 25.0.0-alpha.1 < 25.8.1 || >= 26.0.0-alpha.1 < 26.2.1 || >= 27.0.0-alpha.1 < 27.0.0-alpha.7 patched 22.3.24, 24.8.3, 25.8.1, 26.2.1, 27.0.0-alpha.7
- Credits: MarshallOfSound

### Impact
This only impacts apps that have the `embeddedAsarIntegrityValidation` and `onlyLoadAppFromAsar` [fuses](https://www.electronjs.org/docs/latest/tutorial/fuses) enabled.  Apps without these fuses enabled are not impacted.  This issue is specific to macOS as these fuses are only currently supported on macOS.

Specifically this issue can only be exploited if your app is launched from a filesystem the attacker has write access too.  i.e. the ability to edit files inside the `resources` folder in your app installation on Windows which these fuses are supposed to protect against.

### Workarounds
There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions
* `27.0.0-alpha.7`
* `26.2.1`
* `25.8.1`
* `24.8.3`
* `22.3.24`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-2hfc-r8fq-92h7 — Resource injection in the issue-opened.yml workflow leads to execution of arbitrary JavaScript code within a privileged workflow
- CVE: None | Severity: medium | CVSS: 6.4 `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:L/I:L/A:N` | CWE: CWE-99
- Published: 2024-03-27T18:56:27Z | URL: https://github.com/electron/electron/security/advisories/GHSA-2hfc-r8fq-92h7
- Affected actions/electron/electron/.github/workflows/issue-opened.yml: vulnerable 4f76fff97879ee8f9b2d0dcfd43e686ff8757c69 patched c86e4cb9ce7546324970ceb6e85ad7001df4318c
- Credits: 0xn3va

### Summary

The [issue-opened.yml](https://github.com/electron/electron/blob/4f76fff97879ee8f9b2d0dcfd43e686ff8757c69/.github/workflows/issue-opened.yml) workflow injects a user-controlled data from an issue's body to the `script` parameter of the `actions/github-script` action. Since the `script` parameter accepts a JavaScript code for execution it allows a user to inject arbitrary JavaScript code and gain access to the `ISSUE_TRIAGE_GH_APP_CREDS` encrypted secret and the GitHub App token.

### Details

The [issue-opened.yml](https://github.com/electron/electron/blob/4f76fff97879ee8f9b2d0dcfd43e686ff8757c69/.github/workflows/issue-opened.yml) workflow uses the expression `${{ github.event.issue.body }}` to pass an issue's body to the JavaScript code:

```yaml
# https://github.com/electron/electron/blob/4f76fff97879ee8f9b2d0dcfd43e686ff8757c69/.github/workflows/issue-opened.yml
name: Issue Opened

on:
  issues:
    types:
      - opened

permissions: {}

jobs:
  # ...
  set-labels:
    if: ${{ contains(github.event.issue.labels.*.name, 'bug :beetle:') }}
    runs-on: ubuntu-latest
    steps:
      # ...
      - name: Add labels
        uses: actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea # v7.0.1
        with:
          github-token: ${{ steps.generate-token.outputs.token }}
          script: |
            // ...

            const tree = fromMarkdown(`${{ github.event.issue.body }}`);

            // ...
```

It means that user-controlled data will be directly injected to the JavaScript code before execution.

### PoC

> I used a private test environment to avoid vulnerability disclosure.

As an owner:

1. Create a new repository.
2. Create the `.github/ISSUE_TEMPLATE/bug_report.yml` file and copy content from https://github.com/electron/electron/blob/4f76fff97879ee8f9b2d0dcfd43e686ff8757c69/.github/ISSUE_TEMPLATE/bug_report.yml
3. Go to `Issues > Labels` and add new label with name `bug :beetle:`
4. Create the `.github/workflows/issue-opened.yml` file with the following content (I removed unnecessary jobs and steps because they do not affect exploitation but complicate the reproduction):

```yaml
name: Issue Opened

on:
  issues:
    types:
      - opened

permissions: {}

jobs:
  set-labels:
    if: ${{ contains(github.event.issue.labels.*.name, 'bug :beetle:') }}
    runs-on: ubuntu-latest
    steps:
      - run: npm install mdast-util-from-markdown@2.0.0 unist-util-select@5.1.0
      - name: Add labels
        uses: actions/github-script@60a0d83039c74a4aee543508d2ffcb1c3799cdea # v7.0.1
        with:
          github-token: ${{ github.token }}
          script: |
            const { fromMarkdown } = await import('${{ github.workspace }}/node_modules/mdast-util-from-markdown/index.js');
            const { select } = await import('${{ github.workspace }}/node_modules/unist-util-select/index.js');

            const [ owner, repo ] = '${{ github.repository }}'.split('/');
            const issue_number = ${{ github.event.issue.number }};

            const tree = fromMarkdown(`${{ github.event.issue.body }}`);

            const labels = [];

            const gistUrl = select('heading:has(> text[value="Testcase Gist URL"]) + paragraph > text', tree)?.value.trim();
            if (gistUrl !== undefined && gistUrl.startsWith('https://gist.github.com/')) {
              labels.push('has-repro-gist');
            }

            if (labels.length) {
              await github.rest.issues.addLabels({
                owner,
                repo,
                issue_number,
                labels,
              });
            }
```

As an attacker:

1. Go to `Issues` and click `New issue`.
2. Click `Get started` for the `Bug Report` tamplate.
3. Scroll down and add the following payload to the `Additional Information` field:

    ```
    `);console.log(btoa(btoa(process.env['INPUT_GITHUB-TOKEN'])));//
    ```

4. Click `Submit new issue`.
5. Wait for the `Issue Opened` workflow to complete.
6. Check out the workflow logs, they will contain the GitHub token in base64, like this:

<img width="724" alt="Screenshot 2024-03-27 at 13 12 10" src="https://github.com/electron/electron/assets/47100179/01b2dc60-de8c-4d7f-a96a-edf519fd4cff">

### Impact

This vulnerability allows an attacker to gain unauthorized access to the GitHub App token issued by the `electron/github-app-auth-action` action in runtime and to the `ISSUE_TRIAGE_GH_APP_CREDS` encrypted secret.

The GitHub App token can be directly accessed from environment variables as shown in the PoC. Meanwhile, the `ISSUE_TRIAGE_GH_APP_CREDS` can be exfiltrated from memory, see https://0xn3va.gitbook.io/cheat-sheets/ci-cd/github/actions#exfiltrating-secrets-from-memory

Both tokens can be used to gain read and write access to the `electron/electron` repos issue and projects scopes.

## GHSA-6r2x-8pq8-9489 — Heap Buffer Overflow in NativeImage::CreateFromPath
- CVE: CVE-2024-46993 | Severity: medium | CVSS: 5.5 `CVSS:3.1/AV:L/AC:H/PR:L/UI:R/S:U/C:H/I:L/A:L` | CWE: CWE-122
- Published: 2025-06-30T14:41:42Z | URL: https://github.com/electron/electron/security/advisories/GHSA-6r2x-8pq8-9489
- Affected npm/electron: vulnerable < 28.3.2 || >= 29.0.0-alpha.1 < 29.3.3 || >= 30.0.0-alpha.1 < 30.0.3 patched 28.3.2, 29.3.3, 30.0.3
- Credits: francobel

### Impact
The `nativeImage.createFromPath()` and `nativeImage.createFromBuffer()` functions call a function downstream that is vulnerable to a heap buffer overflow. An Electron program that uses either of the affected functions is vulnerable to a buffer overflow if an attacker is in control of the image's height, width, and contents.

### Workaround
There are no app-side workarounds for this issue. You must update your Electron version to be protected.

### Patches

- `v28.3.2`
- `v29.3.3`
- `v30.0.3`

### For More Information

If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org).

## GHSA-xw5q-g62x-2qjc — ASAR Integrity bypass by just modify the content
- CVE: CVE-2024-46992 | Severity: high | CVSS: 7.8 `CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H` | CWE: 
- Published: 2025-06-30T16:19:54Z | URL: https://github.com/electron/electron/security/advisories/GHSA-xw5q-g62x-2qjc
- Affected npm/electron: vulnerable >= 30.0.0-alpha.1 < 30.0.5 || >= 31.0.0-alpha.1 < 31.0.0-beta.1 patched 30.0.5,31.0.0-beta.1
- Credits: Just-Hack-For-Fun

### Impact
This only impacts apps that have the `embeddedAsarIntegrityValidation` and `onlyLoadAppFromAsar` [fuses](https://www.electronjs.org/docs/latest/tutorial/fuses) enabled. Apps without these fuses enabled are not impacted. This issue is specific to Windows, apps using these fuses on macOS are unimpacted.

Specifically this issue can only be exploited if your app is launched from a filesystem the attacker has write access too. i.e. the ability to edit files inside the .app bundle on macOS which these fuses are supposed to protect against.

### Workarounds
There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions
* `30.0.5`
* `31.0.0-beta.1`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-vmqv-hx8q-j7mg — ASAR Integrity Bypass via resource modification
- CVE: CVE-2025-55305 | Severity: medium | CVSS: 6.1 `CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:L/I:H/A:L` | CWE: CWE-94, CWE-829
- Published: 2025-09-03T18:41:13Z | URL: https://github.com/electron/electron/security/advisories/GHSA-vmqv-hx8q-j7mg
- Affected npm/electron: vulnerable < 35.7.5 || >= 36.0.0-alpha.1 < 36.8.1 || >= 37.0.0-alpha.1 < 37.3.1 || >= 38.0.0-alpha.1 < 38.0.0-beta.6 patched 35.7.5, 36.8.1, 37.3.1, 38.0.0-beta.6
- Credits: dariushoule

### Impact
This only impacts apps that have the `embeddedAsarIntegrityValidation` and `onlyLoadAppFromAsar` [fuses](https://www.electronjs.org/docs/latest/tutorial/fuses) enabled.  Apps without these fuses enabled are not impacted.

Specifically this issue can only be exploited if your app is launched from a filesystem the attacker has write access too.  i.e. the ability to edit files inside the `resources` folder in your app installation on Windows which these fuses are supposed to protect against.

### Workarounds
There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions
* `38.0.0-beta.6`
* `37.3.1`
* `36.8.1`
* `35.7.5`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-4p4r-m79c-wq3v — HTTP Response Header Injection in custom protocol handlers and webRequest
- CVE: CVE-2026-34767 | Severity: medium | CVSS: 5.9 `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:H/A:N` | CWE: CWE-74, CWE-113
- Published: 2026-04-02T19:14:35Z | URL: https://github.com/electron/electron/security/advisories/GHSA-4p4r-m79c-wq3v
- Affected npm/electron: vulnerable < 38.8.6 patched 38.8.6
- Affected npm/electron: vulnerable >= 39.0.0-alpha.1, < 39.8.3 patched 39.8.3
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.8.3 patched 40.8.3
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.0.3 patched 41.0.3

### Impact
Apps that register custom protocol handlers via `protocol.handle()` / `protocol.registerSchemesAsPrivileged()` or modify response headers via `webRequest.onHeadersReceived` may be vulnerable to HTTP response header injection if attacker-controlled input is reflected into a response header name or value.

An attacker who can influence a header value may be able to inject additional response headers, affecting cookies, content security policy, or cross-origin access controls.

Apps that do not reflect external input into response headers are not affected.

### Workarounds
Validate or sanitize any untrusted input before including it in a response header name or value.

### Fixed Versions
* `41.0.3`
* `40.8.3`
* `39.8.3`
* `38.8.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-9899-m83m-qhpj — USB device selection not validated against filtered device list
- CVE: CVE-2026-34766 | Severity: low | CVSS: 3.3 `CVSS:3.1/AV:L/AC:H/PR:L/UI:R/S:U/C:L/I:L/A:N` | CWE: CWE-862
- Published: 2026-04-02T19:15:34Z | URL: https://github.com/electron/electron/security/advisories/GHSA-9899-m83m-qhpj
- Affected npm/electron: vulnerable < 38.8.6 patched 38.8.6
- Affected npm/electron: vulnerable >= 39.0.0-alpha.1, < 39.8.0 patched 39.8.0
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.7.0 patched 40.7.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.0.0-beta.8 patched 41.0.0-beta.8

### Impact
The `select-usb-device` event callback did not validate the chosen device ID against the filtered list that was presented to the handler. An app whose handler could be influenced to select a device ID outside the filtered set would grant access to a device that did not match the renderer's requested `filters` or was listed in `exclusionFilters`.

The WebUSB security blocklist remained enforced regardless, so security-sensitive devices on the blocklist were not affected. The practical impact is limited to apps with unusual device-selection logic.

### Workarounds
There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions
* `41.0.0-beta.8`
* `40.7.0`
* `39.8.0`
* `38.8.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-jfqx-fxh3-c62j — Unquoted executable path in app.setLoginItemSettings on Windows
- CVE: CVE-2026-34768 | Severity: low | CVSS: 3.9 `CVSS:3.1/AV:L/AC:H/PR:H/UI:N/S:U/C:L/I:L/A:L` | CWE: CWE-428
- Published: 2026-04-02T19:15:55Z | URL: https://github.com/electron/electron/security/advisories/GHSA-jfqx-fxh3-c62j
- Affected npm/electron: vulnerable < 38.8.6 patched 38.8.6
- Affected npm/electron: vulnerable >= 39.0.0-alpha.1, < 39.8.1 patched 39.8.1
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.8.0 patched 40.8.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.0.0-beta.8 patched 41.0.0-beta.8

### Impact
On Windows, `app.setLoginItemSettings({openAtLogin: true})` wrote the executable path to the `Run` registry key without quoting. If the app is installed to a path containing spaces, an attacker with write access to an ancestor directory may be able to cause a different executable to run at login instead of the intended app.

On a default Windows install, standard system directories are protected against writes by standard users, so exploitation typically requires a non-standard install location.

### Workarounds
Install the application to a path without spaces, or to a location where all ancestor directories are protected against unauthorized writes.

### Fixed Versions
* `41.0.0-beta.8`
* `40.8.0`
* `39.8.1`
* `38.8.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-jjp3-mq3x-295m — Use-after-free in PowerMonitor on Windows and macOS
- CVE: CVE-2026-34770 | Severity: high | CVSS: 7.0 `CVSS:3.1/AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H` | CWE: CWE-416
- Published: 2026-04-02T19:17:23Z | URL: https://github.com/electron/electron/security/advisories/GHSA-jjp3-mq3x-295m
- Affected npm/electron: vulnerable < 38.8.6 patched 38.8.6
- Affected npm/electron: vulnerable >= 39.0.0-alpha.1, < 39.8.1 patched 39.8.1
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.8.0 patched 40.8.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.0.0-beta.8 patched 41.0.0-beta.8

### Impact
Apps that use the `powerMonitor` module may be vulnerable to a use-after-free. After the native `PowerMonitor` object is garbage-collected, the associated OS-level resources (a message window on Windows, a shutdown handler on macOS) retain dangling references. A subsequent session-change event (Windows) or system shutdown (macOS) dereferences freed memory, which may lead to a crash or memory corruption.

All apps that access `powerMonitor` events (`suspend`, `resume`, `lock-screen`, etc.) are potentially affected. The issue is not directly renderer-controllable.

### Workarounds
There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions
* `41.0.0-beta.8`
* `40.8.0`
* `39.8.1`
* `38.8.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-9wfr-w7mm-pc7f — Renderer command-line switch injection via undocumented commandLineSwitches webPreference
- CVE: CVE-2026-34769 | Severity: high | CVSS: 7.7 `CVSS:3.1/AV:L/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H` | CWE: CWE-88, CWE-912
- Published: 2026-04-02T19:18:19Z | URL: https://github.com/electron/electron/security/advisories/GHSA-9wfr-w7mm-pc7f
- Affected npm/electron: vulnerable < 38.8.6 patched 38.8.6
- Affected npm/electron: vulnerable >= 39.0.0-alpha.1, < 39.8.0 patched 39.8.0
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.7.0 patched 40.7.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.0.0-beta.8 patched 41.0.0-beta.8

### Impact
An undocumented `commandLineSwitches` webPreference allowed arbitrary switches to be appended to the renderer process command line. Apps that construct `webPreferences` by spreading untrusted configuration objects may inadvertently allow an attacker to inject switches that disable renderer sandboxing or web security controls.

Apps are only affected if they construct `webPreferences` from external or untrusted input without an allowlist. Apps that use a fixed, hardcoded `webPreferences` object are not affected.

### Workarounds
Do not spread untrusted input into `webPreferences`. Use an explicit allowlist of permitted preference keys when constructing `BrowserWindow` or `webContents` options from external configuration.

### Fixed Versions
* `41.0.0-beta.8`
* `40.7.0`
* `39.8.0`
* `38.8.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-8337-3p73-46f4 — Use-after-free in WebContents fullscreen, pointer-lock, and keyboard-lock permission callbacks
- CVE: CVE-2026-34771 | Severity: high | CVSS: 7.5 `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H` | CWE: CWE-416
- Published: 2026-04-02T19:18:49Z | URL: https://github.com/electron/electron/security/advisories/GHSA-8337-3p73-46f4
- Affected npm/electron: vulnerable < 38.8.6 patched 38.8.6
- Affected npm/electron: vulnerable >= 39.0.0-alpha.1, < 39.8.0 patched 39.8.0
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.7.0 patched 40.7.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.0.0-beta.8 patched 41.0.0-beta.8

### Impact
Apps that register an asynchronous `session.setPermissionRequestHandler()` may be vulnerable to a use-after-free when handling fullscreen, pointer-lock, or keyboard-lock permission requests. If the requesting frame navigates or the window closes while the permission handler is pending, invoking the stored callback dereferences freed memory, which may lead to a crash or memory corruption.

Apps that do not set a permission request handler, or whose handler responds synchronously, are not affected.

### Workarounds
Respond to permission requests synchronously, or deny fullscreen, pointer-lock, and keyboard-lock requests if an asynchronous flow is required.

### Fixed Versions
* `41.0.0-beta.8`
* `40.7.0`
* `39.8.0`
* `38.8.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-9w97-2464-8783 — Use-after-free in download save dialog callback
- CVE: CVE-2026-34772 | Severity: medium | CVSS: 5.8 `CVSS:3.1/AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:L` | CWE: CWE-416
- Published: 2026-04-02T19:19:06Z | URL: https://github.com/electron/electron/security/advisories/GHSA-9w97-2464-8783
- Affected npm/electron: vulnerable < 38.8.6 patched 38.8.6
- Affected npm/electron: vulnerable >= 39.0.0-alpha.1, < 39.8.0 patched 39.8.0
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.7.0 patched 40.7.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.0.0-beta.7 patched 41.0.0-beta.7

### Impact
Apps that allow downloads and programmatically destroy sessions may be vulnerable to a use-after-free. If a session is torn down while a native save-file dialog is open for a download, dismissing the dialog dereferences freed memory, which may lead to a crash or memory corruption.

Apps that do not destroy sessions at runtime, or that do not permit downloads, are not affected.

### Workarounds
Avoid destroying sessions while a download save dialog may be open. Cancel pending downloads before session teardown.

### Fixed Versions
* `41.0.0-beta.7`
* `40.7.0`
* `39.8.0`
* `38.8.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-532v-xpq5-8h95 — Use-after-free in offscreen child window paint callback
- CVE: CVE-2026-34774 | Severity: high | CVSS: 8.1 `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H` | CWE: CWE-416
- Published: 2026-04-02T19:19:20Z | URL: https://github.com/electron/electron/security/advisories/GHSA-532v-xpq5-8h95
- Affected npm/electron: vulnerable < 39.8.1 patched 39.8.1
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.7.0 patched 40.7.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.0.0 patched 41.0.0

### Impact
Apps that use offscreen rendering and allow child windows via `window.open()` may be vulnerable to a use-after-free. If the parent offscreen `WebContents` is destroyed while a child window remains open, subsequent paint frames on the child dereference freed memory, which may lead to a crash or memory corruption.

Apps are only affected if they use offscreen rendering (`webPreferences.offscreen: true`) and their `setWindowOpenHandler` permits child windows. Apps that do not use offscreen rendering, or that deny child windows, are not affected.

### Workarounds
Deny child window creation from offscreen renderers in your `setWindowOpenHandler`, or ensure child windows are closed before the parent is destroyed.

### Fixed Versions
* `41.0.0`
* `40.7.0`
* `39.8.1`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-mwmh-mq4g-g6gr — Registry key path injection in app.setAsDefaultProtocolClient on Windows
- CVE: CVE-2026-34773 | Severity: medium | CVSS: 4.7 `CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:H/A:N` | CWE: CWE-20, CWE-74
- Published: 2026-04-02T19:19:34Z | URL: https://github.com/electron/electron/security/advisories/GHSA-mwmh-mq4g-g6gr
- Affected npm/electron: vulnerable < 38.8.6 patched 38.8.6
- Affected npm/electron: vulnerable >= 39.0.0-alpha.1, < 39.8.1 patched 39.8.1
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.8.1 patched 40.8.1
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.0.0 patched 41.0.0

### Impact
On Windows, `app.setAsDefaultProtocolClient(protocol)` did not validate the protocol name before writing to the registry. Apps that pass untrusted input as the protocol name may allow an attacker to write to arbitrary subkeys under `HKCU\Software\Classes\`, potentially hijacking existing protocol handlers.

Apps are only affected if they call `app.setAsDefaultProtocolClient()` with a protocol name derived from external or untrusted input. Apps that use a hardcoded protocol name are not affected.

### Workarounds
Validate the protocol name matches `/^[a-zA-Z,a-zA-Z0-9+.-]*$/` before passing it to `app.setAsDefaultProtocolClient()`.

### Fixed Versions
* `41.0.0`
* `40.8.1`
* `39.8.1`
* `38.8.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-3c8v-cfp5-9885 — Out-of-bounds read in second-instance IPC on macOS and Linux
- CVE: CVE-2026-34776 | Severity: medium | CVSS: 5.3 `CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:N/A:L` | CWE: CWE-125
- Published: 2026-04-02T19:19:48Z | URL: https://github.com/electron/electron/security/advisories/GHSA-3c8v-cfp5-9885
- Affected npm/electron: vulnerable < 38.8.6 patched 38.8.6
- Affected npm/electron: vulnerable >= 39.0.0-alpha.1, < 39.8.1 patched 39.8.1
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.8.1 patched 40.8.1
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.0.0 patched 41.0.0

### Impact
On macOS and Linux, apps that call `app.requestSingleInstanceLock()` were vulnerable to an out-of-bounds heap read when parsing a crafted second-instance message. Leaked memory could be delivered to the app's `second-instance` event handler.

This issue is limited to processes running as the same user as the Electron app.

Apps that do not call `app.requestSingleInstanceLock()` are not affected. Windows is not affected by this issue.

### Workarounds
There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions
* `41.0.0`
* `40.8.1`
* `39.8.1`
* `38.8.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-r5p7-gp4j-qhrx — Incorrect origin passed to permission request handler for iframe requests
- CVE: CVE-2026-34777 | Severity: medium | CVSS: 5.4 `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:N` | CWE: CWE-346
- Published: 2026-04-02T19:20:18Z | URL: https://github.com/electron/electron/security/advisories/GHSA-r5p7-gp4j-qhrx
- Affected npm/electron: vulnerable < 38.8.6 patched 38.8.6
- Affected npm/electron: vulnerable >= 39.0.0-alpha.1, < 39.8.1 patched 39.8.1
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.8.1 patched 40.8.1
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.0.0 patched 41.0.0

### Impact
When an iframe requests `fullscreen`, `pointerLock`, `keyboardLock`, `openExternal`, or `media` permissions, the origin passed to `session.setPermissionRequestHandler()` was the top-level page's origin rather than the requesting iframe's origin. Apps that grant permissions based on the origin parameter or `webContents.getURL()` may inadvertently grant permissions to embedded third-party content.

The correct requesting URL remains available via `details.requestingUrl`. Apps that already check `details.requestingUrl` are not affected.

### Workarounds
In your `setPermissionRequestHandler`, inspect `details.requestingUrl` rather than the origin parameter or `webContents.getURL()` when deciding whether to grant `fullscreen`, `pointerLock`, `keyboardLock`, `openExternal`, or `media` permissions.

### Fixed Versions
* `41.0.0`
* `40.8.1`
* `39.8.1`
* `38.8.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-xwr5-m59h-vwqr — nodeIntegrationInWorker not correctly scoped in shared renderer processes
- CVE: CVE-2026-34775 | Severity: medium | CVSS: 6.8 `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:N` | CWE: CWE-653
- Published: 2026-04-02T19:20:37Z | URL: https://github.com/electron/electron/security/advisories/GHSA-xwr5-m59h-vwqr
- Affected npm/electron: vulnerable < 38.8.6 patched 38.8.6
- Affected npm/electron: vulnerable >= 39.0.0-alpha.1, < 39.8.4 patched 39.8.4
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.8.4 patched 40.8.4
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.0.0 patched 41.0.0

### Impact
The `nodeIntegrationInWorker` webPreference was not correctly scoped in all configurations. In certain process-sharing scenarios, workers spawned in frames configured with `nodeIntegrationInWorker: false` could still receive Node.js integration.

Apps are only affected if they enable `nodeIntegrationInWorker`. Apps that do not use `nodeIntegrationInWorker` are not affected.

### Workarounds
Avoid enabling `nodeIntegrationInWorker` in apps that also open child windows or embed content with differing webPreferences.

### Fixed Versions
* `41.0.0`
* `40.8.4`
* `39.8.4`
* `38.8.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-5rqw-r77c-jp79 — AppleScript injection in app.moveToApplicationsFolder on macOS
- CVE: CVE-2026-34779 | Severity: medium | CVSS: 6.5 `CVSS:3.1/AV:L/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:L` | CWE: CWE-78
- Published: 2026-04-02T19:21:44Z | URL: https://github.com/electron/electron/security/advisories/GHSA-5rqw-r77c-jp79
- Affected npm/electron: vulnerable < 38.8.6 patched 38.8.6
- Affected npm/electron: vulnerable >= 39.0.0-alpha.1, < 39.8.1 patched 39.8.1
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.8.0 patched 40.8.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.0.0-beta.8 patched 41.0.0-beta.8

### Impact
On macOS, `app.moveToApplicationsFolder()` used an AppleScript fallback path that did not properly handle certain characters in the application bundle path. Under specific conditions, a crafted launch path could lead to arbitrary AppleScript execution when the user accepted the move-to-Applications prompt.

Apps are only affected if they call `app.moveToApplicationsFolder()`. Apps that do not use this API are not affected.

### Workarounds
There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions
* `41.0.0-beta.8`
* `40.8.0`
* `39.8.1`
* `38.8.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-xj5x-m3f3-5x3h — Service worker can spoof executeJavaScript IPC replies
- CVE: CVE-2026-34778 | Severity: medium | CVSS: 5.9 `CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:L/I:H/A:N` | CWE: CWE-290, CWE-345
- Published: 2026-04-02T19:21:52Z | URL: https://github.com/electron/electron/security/advisories/GHSA-xj5x-m3f3-5x3h
- Affected npm/electron: vulnerable < 38.8.6 patched 38.8.6
- Affected npm/electron: vulnerable >= 39.0.0-alpha.1, < 39.8.1 patched 39.8.1
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.8.1 patched 40.8.1
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.0.0 patched 41.0.0

### Impact
A service worker running in a session could spoof reply messages on the internal IPC channel used by `webContents.executeJavaScript()` and related methods, causing the main-process promise to resolve with attacker-controlled data.

Apps are only affected if they have service workers registered and use the result of `webContents.executeJavaScript()` (or `webFrameMain.executeJavaScript()`) in security-sensitive decisions.

### Workarounds
Do not trust the return value of `webContents.executeJavaScript()` for security decisions. Use dedicated, validated IPC channels for security-relevant communication with renderers.

### Fixed Versions
* `41.0.0`
* `40.8.1`
* `39.8.1`
* `38.8.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-jfqg-hf23-qpw2 — Context Isolation bypass via contextBridge VideoFrame transfer
- CVE: CVE-2026-34780 | Severity: high | CVSS: 8.3 `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H` | CWE: CWE-668, CWE-1188
- Published: 2026-04-02T19:28:25Z | URL: https://github.com/electron/electron/security/advisories/GHSA-jfqg-hf23-qpw2
- Affected npm/electron: vulnerable >= 39.0.0-alpha.1, < 39.8.0 patched 39.8.0
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.7.0 patched 40.7.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.0.0-beta.8 patched 41.0.0-beta.8

### Impact
Apps that pass `VideoFrame` objects (from the WebCodecs API) across the `contextBridge` are vulnerable to a context isolation bypass. An attacker who can execute JavaScript in the main world (for example, via XSS) can use a bridged `VideoFrame` to gain access to the isolated world, including any Node.js APIs exposed to the preload script.

Apps are only affected if a preload script returns, resolves, or passes a `VideoFrame` object to the main world via `contextBridge.exposeInMainWorld()`. Apps that do not bridge `VideoFrame` objects are not affected.

### Workarounds
Do not pass `VideoFrame` objects across `contextBridge`. If your app needs to transfer video frame data, serialize it to an `ArrayBuffer` or `ImageBitmap` before bridging.

### Fixed Versions
* `41.0.0-beta.8`
* `40.7.0`
* `39.8.0`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-8x5q-pvf5-64mp — Use-after-free in offscreen shared texture release() callback
- CVE: CVE-2026-34764 | Severity: low | CVSS: 2.3 `CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:U/C:N/I:N/A:L` | CWE: CWE-416
- Published: 2026-04-03T08:27:29Z | URL: https://github.com/electron/electron/security/advisories/GHSA-8x5q-pvf5-64mp
- Affected npm/electron: vulnerable >= 33.0.0-alpha.1, < 39.8.5 patched 39.8.5
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.8.5 patched 40.8.5
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.1.0 patched 41.1.0
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-alpha.5 patched 42.0.0-alpha.5
- Credits: daffainfo

### Impact
Apps that use offscreen rendering with GPU shared textures may be vulnerable to a use-after-free. Under certain conditions, the `release()` callback provided on a `paint` event texture can outlive its backing native state, and invoking it after that point dereferences freed memory in the main process, which may lead to a crash or memory corruption.

Apps are only affected if they use offscreen rendering with `webPreferences.offscreen: { useSharedTexture: true }`. Apps that do not enable shared-texture offscreen rendering are not affected.

### Workarounds
Ensure `texture.release()` is called promptly after the texture has been consumed, before the texture object becomes unreachable.

### Fixed Versions
* `42.0.0-alpha.5`
* `41.1.0`
* `40.8.5`
* `39.8.5`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)


## GHSA-f3pv-wv63-48x8 — Named window.open targets not scoped to the opener's browsing context
- CVE: CVE-2026-34765 | Severity: medium | CVSS: 6.0 `CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:L/I:L/A:L` | CWE: CWE-668
- Published: 2026-04-06T20:23:26Z | URL: https://github.com/electron/electron/security/advisories/GHSA-f3pv-wv63-48x8
- Affected npm/electron: vulnerable < 39.8.5 patched 39.8.5
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.8.5 patched 40.8.5
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.1.0 patched 41.1.0
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-alpha.5 patched 42.0.0-alpha.5
- Credits: HO-9, HanJeouk

### Impact
When a renderer calls `window.open()` with a target name, Electron did not correctly scope the named-window lookup to the opener's browsing context group. A renderer could navigate an existing child window that was opened by a different, unrelated renderer if both used the same target name. If that existing child was created with more permissive `webPreferences` (via `setWindowOpenHandler`'s `overrideBrowserWindowOptions`), content loaded by the second renderer inherits those permissions.

Apps are only affected if they open multiple top-level windows with differing trust levels **and** use `setWindowOpenHandler` to grant child windows elevated `webPreferences` such as a privileged preload script. Apps that do not elevate child window privileges, or that use a single top-level window, are not affected.

Apps that additionally grant `nodeIntegration: true` or `sandbox: false` to child windows (contrary to the [security recommendations](https://www.electronjs.org/docs/latest/tutorial/security)) may be exposed to arbitrary code execution.

### Workarounds
Deny `window.open()` in renderers that load untrusted content by returning `{ action: 'deny' }` from `setWindowOpenHandler`. Avoid granting child windows more permissive `webPreferences` than their opener.

### Fixed Versions
* `42.0.0-alpha.5`
* `41.1.0`
* `40.8.5`
* `39.8.5`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)


## GHSA-f37v-82c4-4x64 — Crash in clipboard.readImage() on malformed clipboard image data
- CVE: CVE-2026-34781 | Severity: low | CVSS: 2.8 `CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:N/I:N/A:L` | CWE: CWE-476
- Published: 2026-04-06T20:23:31Z | URL: https://github.com/electron/electron/security/advisories/GHSA-f37v-82c4-4x64
- Affected npm/electron: vulnerable < 39.8.5 patched 39.8.5
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.8.5 patched 40.8.5
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.1.0 patched 41.1.0
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-alpha.5 patched 42.0.0-alpha.5
- Credits: frostb1ten

### Impact
Apps that call `clipboard.readImage()` may be vulnerable to a denial of service. If the system clipboard contains image data that fails to decode, the resulting null bitmap is passed unchecked to image construction, triggering a controlled abort and crashing the process.

Apps are only affected if they call `clipboard.readImage()`. Apps that do not read images from the clipboard are not affected. This issue does not allow memory corruption or code execution.

### Workarounds
Validate that the clipboard contains image data via `clipboard.availableFormats()` before calling `clipboard.readImage()`. Note this only narrows the window — upgrading to a fixed version is recommended.

### Fixed Versions
* `42.0.0-alpha.5`
* `41.1.0`
* `40.8.5`
* `39.8.5`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)


## GHSA-q6m5-f73j-m9mc — Buffer performs incorrect byte length calculations resulting in heap buffer under/overflow
- CVE: CVE-2026-54257 | Severity: critical | CVSS: None `None` | CWE: 
- Published: 2026-06-03T21:59:12Z | URL: https://github.com/electron/electron/security/advisories/GHSA-q6m5-f73j-m9mc
- Affected npm/electron: vulnerable 42.3.1,42.3.2 patched 42.3.3

### Impact
Most apps will crash and some may perform incorrect buffer allocations in the Node.js `Buffer` API resulting in unexpected truncation or allocation.

### Workarounds
No workarounds. Do not use these impacted Electron releases

### Fixed Versions
* `42.3.3`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)


## GHSA-9f4c-93c8-jc8g — Sandboxed iframe can bypass the allow-popups restriction via the OpenURL navigation path
- CVE: CVE-2026-70608 | Severity: high | CVSS: 7.2 `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:N` | CWE: CWE-693, CWE-1021
- Published: 2026-07-27T23:28:49Z | URL: https://github.com/electron/electron/security/advisories/GHSA-9f4c-93c8-jc8g
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.1 patched 42.0.1
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 41.10.3 patched 41.10.3
- Affected npm/electron: vulnerable < 39.8.10 patched 39.8.10
- Credits: Ciarands

### Impact
A sandboxed iframe without the `allow-popups` keyword could still open a new window (or trigger `setWindowOpenHandler`) with no user interaction, because new-window navigations taking the OpenURL path did not apply the iframe sandbox popup restriction.

Apps that embed untrusted content in sandboxed iframes and rely on the absence of `allow-popups` to prevent window creation are affected. Apps that deny window creation in `setWindowOpenHandler`, or that do not embed untrusted content in sandboxed iframes, are not affected.

### Workarounds
Return `{ action: 'deny' }` from `setWindowOpenHandler` for any content you do not trust, rather than relying on the iframe sandbox alone.

### Fixed Versions
* `42.0.1`
* `41.10.3`
* `39.8.10`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)



## GHSA-5c9j-mhmv-5xgx — shell.openPath path validation bypass via embedded null byte
- CVE: CVE-2026-70603 | Severity: medium | CVSS: 6.0 `CVSS:3.1/AV:L/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:N` | CWE: CWE-20, CWE-158
- Published: 2026-07-27T23:28:55Z | URL: https://github.com/electron/electron/security/advisories/GHSA-5c9j-mhmv-5xgx
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-beta.1 patched 42.0.0-beta.1
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.1.1 patched 41.1.1
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.9.0 patched 40.9.0
- Affected npm/electron: vulnerable < 39.8.6 patched 39.8.6
- Credits: yassine-doyensec, ikkisoft, maxence-Doyensec

### Impact
`shell.openPath()` did not reject paths containing embedded null bytes. Apps that perform string-only validation of file paths (for example, checking the file extension) before passing them to `shell.openPath()` could be bypassed, allowing an attacker-controlled path to open a different file than the one that passed validation.

Apps are only affected if they pass paths derived from untrusted input to `shell.openPath()` and rely on string-based validation without a filesystem check. Node's `fs` APIs already reject paths containing null bytes, so apps that call `fs.existsSync()`, `fs.stat()`, or similar before `shell.openPath()` are not affected. Apps that do not call `shell.openPath()` with untrusted input are not affected.

### Workarounds
Reject any path containing a null byte before passing it to `shell.openPath()`:
```js
if (filePath.includes('\0')) throw new Error('invalid path');
```

### Fixed Versions
* `42.0.0-beta.1`
* `41.1.1`
* `40.9.0`
* `39.8.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-v3j7-r9gq-3gjw — Custom protocol with supportFetchAPI but not corsEnabled allows cross-origin reads
- CVE: CVE-2026-70604 | Severity: high | CVSS: 7.4 `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:N/A:N` | CWE: CWE-942
- Published: 2026-07-27T23:29:07Z | URL: https://github.com/electron/electron/security/advisories/GHSA-v3j7-r9gq-3gjw
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0 patched 42.0.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.4.0 patched 41.4.0
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.9.3 patched 40.9.3
- Affected npm/electron: vulnerable < 39.8.10 patched 39.8.10
- Credits: proxydom

### Impact
A custom scheme registered with `supportFetchAPI: true` but without `corsEnabled: true` was not subject to CORS enforcement. A page loaded from a remote origin could therefore `fetch()` or `XMLHttpRequest` that scheme cross-origin and read the full response body, rather than the read being blocked.

Apps are only affected if they register such a scheme, serve sensitive data from it, and load untrusted content in the same session. Apps that do not load untrusted content are not affected. Schemes registered with `corsEnabled: true` are unchanged by this fix: that option opts the scheme in to cross-origin `fetch()`, and responses from its handler are readable by any origin in the session by design.

### Workarounds
Do not load untrusted content in sessions that can reach the scheme. `corsEnabled: true` is not a mitigation; it permits cross-origin reads rather than restricting them. *(Corrected 2026-09-03: an earlier version of this advisory suggested setting `corsEnabled: true` and validating the request `Origin` in the handler. That advice was incorrect.)*

### Fixed Versions
* `42.0.0`
* `41.4.0`
* `40.9.3`
* `39.8.10`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)



## GHSA-r4w5-6pfg-jxp5 — ProtocolResponse.url reuses the default session cache instead of the registering session
- CVE: CVE-2026-70606 | Severity: medium | CVSS: 5.9 `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:L/A:N` | CWE: CWE-668
- Published: 2026-07-27T23:29:11Z | URL: https://github.com/electron/electron/security/advisories/GHSA-r4w5-6pfg-jxp5
- Affected npm/electron: vulnerable >= 43.0.0-alpha.1, < 43.0.0 patched 43.0.0
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.5.1 patched 42.5.1
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.9.1 patched 41.9.1
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.10.6 patched 40.10.6
- Credits: rushitgit

### Impact
When a custom protocol handler returned a `ProtocolResponse` with a `url` and no `session`, Electron made the upstream request through `defaultSession` instead of the session that handled the protocol. A cached response could then be reused across otherwise isolated session partitions.

Apps that use `ProtocolResponse.url`, omit `ProtocolResponse.session`, and rely on separate sessions to isolate content are affected. Apps that set an explicit `session`, or that do not isolate content across sessions, are not affected.

### Workarounds
Set `ProtocolResponse.session` explicitly so the request uses the intended session's cache.

### Fixed Versions
* `43.0.0`
* `42.5.1`
* `41.9.1`
* `40.10.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)


## GHSA-h7rp-cf8h-j98x — Context isolation bypass via prototype hijack
- CVE: CVE-2026-70601 | Severity: high | CVSS: 7.5 `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:L/A:N` | CWE: CWE-693
- Published: 2026-07-27T23:48:16Z | URL: https://github.com/electron/electron/security/advisories/GHSA-h7rp-cf8h-j98x
- Affected npm/electron: vulnerable < 39.8.9 patched 39.8.9
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.9.2 patched 40.9.2
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.2.2 patched 41.2.2
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-beta.5 patched 42.0.0-beta.5

### Impact
Apps that expose Promise-returning functions to web content via `contextBridge` may be vulnerable to a context isolation bypass. Untrusted web content could obtain access to the isolated preload world and, through it, every capability the preload script has. In renderers without a sandbox, or with `nodeIntegration` enabled, this may escalate to Node.js access.

Apps are affected if they expose Promise-returning functions via `contextBridge` — the standard pattern for wrapping `ipcRenderer.invoke` — in windows that load untrusted content. Apps that never load untrusted content in those windows are not affected.

### Workarounds
There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions
* `42.0.0-beta.5`
* `41.2.2`
* `40.9.2`
* `39.8.9`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-f2r8-jv7c-xqmp — DevTools embedder handler executes arbitrary files via shell open
- CVE: CVE-2026-70611 | Severity: medium | CVSS: 6.9 `CVSS:3.1/AV:L/AC:H/PR:H/UI:R/S:C/C:H/I:H/A:N` | CWE: CWE-78
- Published: 2026-07-27T23:48:36Z | URL: https://github.com/electron/electron/security/advisories/GHSA-f2r8-jv7c-xqmp
- Affected npm/electron: vulnerable < 39.8.9 patched 39.8.9
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.9.2 patched 40.9.2
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.2.1 patched 41.2.1
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-beta.3 patched 42.0.0-beta.3

### Impact
The DevTools "reveal in file manager" action could launch the target file rather than reveal it. An attacker with a separate means of running script inside the DevTools frontend (such as a malicious DevTools extension) could use this to execute native code outside the sandbox.

Apps are only affected if DevTools is opened for windows exposed to untrusted content or untrusted DevTools extensions. Apps that do not open DevTools in that context are not affected.

### Workarounds
Do not open DevTools for windows that load untrusted content, and do not load untrusted DevTools extensions.

### Fixed Versions
* `42.0.0-beta.3`
* `41.2.1`
* `40.9.2`
* `39.8.9`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-m55f-7gqj-fr98 — Extension tab APIs operate across session boundaries
- CVE: CVE-2026-70602 | Severity: medium | CVSS: 6.6 `CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:C/C:H/I:L/A:N` | CWE: CWE-284
- Published: 2026-07-27T23:48:43Z | URL: https://github.com/electron/electron/security/advisories/GHSA-m55f-7gqj-fr98
- Affected npm/electron: vulnerable < 39.8.8 patched 39.8.8
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.9.0 patched 40.9.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.2.1 patched 41.2.1
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-beta.3 patched 42.0.0-beta.3

### Impact
Extension tab and scripting APIs were not scoped to the extension's own `session`. A malicious or compromised extension loaded into one session could navigate, script, and read from windows belonging to a different session.

Apps are only affected if they load Chrome extensions via `session.loadExtension` and rely on separate sessions to isolate that extension from other content. Apps that do not load extensions, or that use a single session, are not affected.

### Workarounds
Only load extensions from sources you trust; do not rely on session separation alone to contain an extension.

### Fixed Versions
* `42.0.0-beta.3`
* `41.2.1`
* `40.9.0`
* `39.8.8`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-jm7p-cc5g-qwxx — Parent process code-sign check is spoofable
- CVE: CVE-2026-70597 | Severity: medium | CVSS: 6.3 `CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:N` | CWE: CWE-367
- Published: 2026-07-27T23:49:35Z | URL: https://github.com/electron/electron/security/advisories/GHSA-jm7p-cc5g-qwxx
- Affected npm/electron: vulnerable < 39.8.8 patched 39.8.8
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.9.0 patched 40.9.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.2.1 patched 41.2.1
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-beta.3 patched 42.0.0-beta.3

### Impact
On macOS, the check Electron uses to confirm it was launched by a same-signed parent process could be bypassed by a local process. Apps that enable the fuse-based hardening restricting `ELECTRON_RUN_AS_NODE` and `NODE_OPTIONS` to same-signed parents rely on this check; a local attacker could bypass it and run their own code inside the signed app, inheriting its TCC permissions and keychain access.

Apps are only affected if they enable those macOS fuse-based restrictions. Apps that do not enable them are not affected.

### Workarounds
There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions
* `42.0.0-beta.3`
* `41.2.1`
* `40.9.0`
* `39.8.8`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-9pf5-hg6p-4pwp — Permission Check Handler Receives Main Frame Origin Instead of Requesting Iframe Origin
- CVE: CVE-2026-70599 | Severity: medium | CVSS: 5.9 `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N` | CWE: CWE-346
- Published: 2026-07-27T23:49:48Z | URL: https://github.com/electron/electron/security/advisories/GHSA-9pf5-hg6p-4pwp
- Affected npm/electron: vulnerable < 39.8.7 patched 39.8.7
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.9.0 patched 40.9.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.2.0 patched 41.2.0
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-beta.1 patched 42.0.0-beta.1
- Credits: offset

### Impact
For serial-port and media (camera / microphone) permission checks made from an iframe, the `requestingOrigin` passed to `session.setPermissionCheckHandler` was the top-level frame's origin rather than the requesting frame's. Origin-based handler logic could therefore grant a cross-origin iframe device access intended only for the top-level origin.

Apps are only affected if they use `setPermissionCheckHandler` with origin-based logic and embed cross-origin iframes with delegated device permissions. Apps that base the decision on `details.securityOrigin`, or that do not embed such iframes, are not affected.

### Workarounds
Check `details.securityOrigin` instead of `requestingOrigin` for these permissions, or do not delegate device permissions to untrusted iframes.

### Fixed Versions
* `42.0.0-beta.1`
* `41.2.0`
* `40.9.0`
* `39.8.7`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-v64r-4m7r-3mvq — HTTP redirect followed into local file loader
- CVE: CVE-2026-70605 | Severity: medium | CVSS: 5.9 `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:N` | CWE: CWE-918
- Published: 2026-07-27T23:49:57Z | URL: https://github.com/electron/electron/security/advisories/GHSA-v64r-4m7r-3mvq
- Affected npm/electron: vulnerable < 39.8.8 patched 39.8.8
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.9.0 patched 40.9.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.2.1 patched 41.2.1
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-beta.3 patched 42.0.0-beta.3

### Impact
When following HTTP redirects, `net.fetch()` and `net.request()` did not restrict which schemes a redirect could target. A remote server could redirect a request to a local resource, and if the app returns or forwards the response body, local file contents could be disclosed.

Apps are only affected if they make `net` requests to attacker-influenced URLs with redirects followed (the default) and expose the response body. Apps that only request fixed, trusted URLs are not affected.

### Workarounds
Set `redirect: 'error'` or `redirect: 'manual'` on requests to untrusted URLs and validate any redirect target before following it.

### Fixed Versions
* `42.0.0-beta.3`
* `41.2.1`
* `40.9.0`
* `39.8.8`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-4f78-qhmw-8j8m — DevTools JavaScript Injection via Unsanitized Dock State Parameter
- CVE: CVE-2026-70609 | Severity: medium | CVSS: 5.7 `CVSS:3.1/AV:N/AC:H/PR:H/UI:R/S:U/C:H/I:H/A:N` | CWE: CWE-94, CWE-116
- Published: 2026-07-27T23:50:09Z | URL: https://github.com/electron/electron/security/advisories/GHSA-4f78-qhmw-8j8m
- Affected npm/electron: vulnerable < 39.8.7 patched 39.8.7
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.9.0 patched 40.9.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.2.0 patched 41.2.0
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-beta.1 patched 42.0.0-beta.1
- Credits: hackerman70000

### Impact
The `mode` option of `webContents.openDevTools()` was not sanitized before use by the DevTools frontend. If an attacker can influence this value, script under their control may run in the DevTools context, which in unsandboxed configurations has access to Node.js.

Apps are only affected if untrusted input can reach the `mode` argument of `openDevTools()`, or if untrusted content can call `openDevTools()` on a `<webview>` it embeds. Apps that only ever pass a fixed dock mode are not affected.

### Workarounds
Only pass fixed, allowlisted values (`right`, `bottom`, `undocked`, `detach`) as the DevTools `mode`, and do not expose `openDevTools` to untrusted content.

### Fixed Versions
* `42.0.0-beta.1`
* `41.2.0`
* `40.9.0`
* `39.8.7`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-p2rr-rvmm-c5fp — Sandboxed iframes can launch external protocol handlers
- CVE: CVE-2026-70612 | Severity: medium | CVSS: 5.4 `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:L/I:L/A:N` | CWE: CWE-284
- Published: 2026-07-27T23:50:20Z | URL: https://github.com/electron/electron/security/advisories/GHSA-p2rr-rvmm-c5fp
- Affected npm/electron: vulnerable < 39.8.8 patched 39.8.8
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.9.0 patched 40.9.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.2.1 patched 41.2.1
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-beta.3 patched 42.0.0-beta.3

### Impact
Requests to open external protocol URLs from web content did not take iframe sandbox restrictions into account, so a sandboxed iframe could cause an OS-registered external application to be launched. The frame's sandbox state was also not made available to the app's permission handlers.

Apps are only affected if they render untrusted content in sandboxed iframes and grant the `openExternal` permission (granted by default when no `setPermissionRequestHandler` is installed). Apps whose permission handler denies `openExternal` for untrusted content are not affected.

### Workarounds
Install a `setPermissionRequestHandler` that denies the `openExternal` permission for untrusted content.

### Fixed Versions
* `42.0.0-beta.3`
* `41.2.1`
* `40.9.0`
* `39.8.8`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-ff2p-hmqr-hxm4 — contextBridge object copy incorrectly honours setters on prototype
- CVE: CVE-2026-70610 | Severity: medium | CVSS: 5.4 `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:L/I:L/A:N` | CWE: CWE-1321
- Published: 2026-07-27T23:50:42Z | URL: https://github.com/electron/electron/security/advisories/GHSA-ff2p-hmqr-hxm4
- Affected npm/electron: vulnerable < 39.8.9 patched 39.8.9
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.9.2 patched 40.9.2
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.2.2 patched 41.2.2
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-beta.4 patched 42.0.0-beta.4

### Impact
Objects copied across the `contextBridge` boundary from untrusted content could carry an attacker-influenced prototype, enabling prototype-pollution-style attacks against preload code despite context isolation being enabled.

Apps are only affected if their preload code accepts object arguments from untrusted content and reads properties from them without own-property checks. Apps that only accept primitive arguments, or that validate object arguments, are not affected.

### Workarounds
Validate objects received from untrusted content with own-property checks (`Object.hasOwn`), or copy them onto a null-prototype object before use.

### Fixed Versions
* `42.0.0-beta.4`
* `41.2.2`
* `40.9.2`
* `39.8.9`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-v93f-fgjr-hjrj — window.open features string controls some window options considered privileged
- CVE: CVE-2026-70607 | Severity: medium | CVSS: 5.3 `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N` | CWE: CWE-20
- Published: 2026-07-27T23:51:42Z | URL: https://github.com/electron/electron/security/advisories/GHSA-v93f-fgjr-hjrj
- Affected npm/electron: vulnerable < 39.8.8 patched 39.8.8
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.9.0 patched 40.9.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.2.1 patched 41.2.1
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-beta.3 patched 42.0.0-beta.3

### Impact
Some window options supplied by web content in the `window.open()` features string were applied to the new `BrowserWindow` without an allowlist. Untrusted content could set window options it should not control, including options that cause the main process to access attacker-chosen file or network paths.

Apps are only affected if untrusted content can call `window.open()` and the app does not override child window options via `setWindowOpenHandler`. Apps that deny `window.open()` for untrusted content, or set `overrideBrowserWindowOptions` explicitly, are not affected.

### Workarounds
Return `{ action: 'deny' }` from `setWindowOpenHandler` for untrusted content, or supply `overrideBrowserWindowOptions` so every window option is set explicitly.

### Fixed Versions
* `42.0.0-beta.3`
* `41.2.1`
* `40.9.0`
* `39.8.8`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-pfmc-3mgc-p6fp — Off-screen rendering trusts GPU-supplied geometry over shared-memory size
- CVE: CVE-2026-70598 | Severity: low | CVSS: 3.9 `CVSS:3.1/AV:L/AC:H/PR:H/UI:N/S:C/C:L/I:N/A:L` | CWE: CWE-125
- Published: 2026-07-27T23:51:50Z | URL: https://github.com/electron/electron/security/advisories/GHSA-pfmc-3mgc-p6fp
- Affected npm/electron: vulnerable < 39.8.10 patched 39.8.10
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.9.0 patched 40.9.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.2.1 patched 41.2.1
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-beta.3 patched 42.0.0-beta.3

### Impact
In offscreen rendering mode, frame data received from the GPU process was not fully validated by the main process. A compromised GPU process could cause the main process to read out-of-bounds memory while producing `paint` event images, disclosing memory or crashing the app.

Apps are only affected if they use offscreen rendering (`webPreferences.offscreen`) and an attacker has separately gained code execution in the GPU process. Apps that do not use offscreen rendering are not affected.

### Workarounds
There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions
* `42.0.0-beta.3`
* `41.2.1`
* `40.9.0`
* `39.8.10`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-x8rc-wpg4-grpf — Cross-origin iframe can position native autofill popup
- CVE: CVE-2026-70600 | Severity: low | CVSS: 3.1 `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:N/I:L/A:N` | CWE: CWE-1021
- Published: 2026-07-27T23:52:01Z | URL: https://github.com/electron/electron/security/advisories/GHSA-x8rc-wpg4-grpf
- Affected npm/electron: vulnerable < 39.8.8 patched 39.8.8
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1, < 40.9.0 patched 40.9.0
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.2.1 patched 41.2.1
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-beta.3 patched 42.0.0-beta.3

### Impact
The native autofill popup could be positioned by a cross-origin iframe outside that iframe's bounds, over the embedding page's UI, enabling clickjacking or spoofing of trusted UI.

Apps are only affected if they embed untrusted content in iframes within windows that also display trusted UI. Apps that do not embed untrusted third-party content are not affected.

### Workarounds
Do not embed untrusted content in iframes inside windows that display trusted UI.

### Fixed Versions
* `42.0.0-beta.3`
* `41.2.1`
* `40.9.0`
* `39.8.8`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-qmv3-fv6v-rmhq — Sandboxed preload code cache can be poisoned by a compromised renderer
- CVE: CVE-2026-102677 | Severity: high | CVSS: 7.8 `CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H` | CWE: CWE-20, CWE-345
- Published: 2026-08-29T00:32:33Z | URL: https://github.com/electron/electron/security/advisories/GHSA-qmv3-fv6v-rmhq
- Affected npm/electron: vulnerable >= 42.3.3, < 42.10.0 patched 42.10.0
- Affected npm/electron: vulnerable >= 43.0.0-beta.1, < 43.4.2 patched 43.4.2
- Affected npm/electron: vulnerable >= 44.0.0-alpha.1, < 44.0.0-beta.6 patched 44.0.0-beta.6
- Credits: varisys

### Impact

The cache Electron keeps for sandboxed preload scripts did not verify that a cached entry matched the preload it was served for. A compromised renderer could use this to run its own code in the preload context on a later load.

Apps are only affected if they load untrusted content. Apps that do not load untrusted content are not affected.

### Workarounds

There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions

* `44.0.0-beta.6`
* `43.4.2`
* `42.10.0`

### For more information

If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)


## GHSA-9qh4-3jw8-366w — <webview> can enable Node.js integration in Web Workers despite embedder restrictions
- CVE: CVE-2026-102676 | Severity: high | CVSS: 8.3 `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H` | CWE: CWE-269, CWE-1188
- Published: 2026-08-29T00:32:40Z | URL: https://github.com/electron/electron/security/advisories/GHSA-9qh4-3jw8-366w
- Affected npm/electron: vulnerable < 41.10.6 patched 41.10.6
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.9.2 patched 42.9.2
- Affected npm/electron: vulnerable >= 43.0.0-alpha.1, < 43.4.1 patched 43.4.1
- Affected npm/electron: vulnerable >= 44.0.0-alpha.1, < 44.0.0-beta.5 patched 44.0.0-beta.5
- Credits: XlabAITeam, keenanwgn, pkuGenuine, liangjs

### Impact

A `<webview>` could enable Node.js integration in its Web Workers even when its embedder had Node.js integration disabled, giving guest content more privilege than the embedder allowed.

Apps are only affected if they enable the `<webview>` tag and the embedder is unsandboxed. Apps that do not use `<webview>`, or that keep the embedder sandboxed, are not affected.

### Workarounds

Remove `nodeIntegrationInWorker` from the guest preferences in a `will-attach-webview` handler, or do not enable the `<webview>` tag when loading untrusted content.

### Fixed Versions

* `44.0.0-beta.5`
* `43.4.1`
* `42.9.2`
* `41.10.6`

### For more information

If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)


## GHSA-j84w-jfhq-vhvj — File and HTTP protocol handlers allow cross-origin reads without corsEnabled
- CVE: CVE-2026-102675 | Severity: high | CVSS: 7.4 `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:N/A:N` | CWE: CWE-346
- Published: 2026-08-29T00:32:46Z | URL: https://github.com/electron/electron/security/advisories/GHSA-j84w-jfhq-vhvj
- Affected npm/electron: vulnerable < 41.10.6 patched 41.10.6
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.9.2 patched 42.9.2
- Affected npm/electron: vulnerable >= 43.0.0-alpha.1, < 43.4.1 patched 43.4.1
- Affected npm/electron: vulnerable >= 44.0.0-alpha.1, < 44.0.0-beta.5 patched 44.0.0-beta.5
- Credits: manus-use

### Impact

Responses served through `protocol.registerFileProtocol` or `protocol.registerHttpProtocol` for a custom scheme registered with `supportFetchAPI: true` but without `corsEnabled: true` could be read cross-origin by web content. This completes the fix for CVE-2026-70604.

Apps are only affected if they register such a scheme, serve it through one of those handlers, and load untrusted content in the same session. Apps that do not load untrusted content are not affected. Schemes registered with `corsEnabled: true` are unchanged by this fix: that option opts the scheme in to cross-origin `fetch()`, and responses from its handler are readable by any origin in the session by design.

### Workarounds

Do not load untrusted content in sessions that can reach the scheme. `corsEnabled: true` is not a mitigation; it permits cross-origin reads rather than restricting them. *(Corrected 2026-09-03: an earlier version of this advisory listed `corsEnabled: true` as a workaround. That advice was incorrect.)*

### Fixed Versions

* `44.0.0-beta.5`
* `43.4.1`
* `42.9.2`
* `41.10.6`

### For more information

If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)



## GHSA-gr2m-v5gq-v685 — Windows opened from a sandboxed top-level document do not inherit its sandbox restrictions
- CVE: CVE-2026-102674 | Severity: high | CVSS: 8.2 `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:L/A:N` | CWE: CWE-266, CWE-693
- Published: 2026-08-29T00:32:54Z | URL: https://github.com/electron/electron/security/advisories/GHSA-gr2m-v5gq-v685
- Affected npm/electron: vulnerable < 41.10.6 patched 41.10.6
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.9.2 patched 42.9.2
- Affected npm/electron: vulnerable >= 43.0.0-alpha.1, < 43.4.1 patched 43.4.1
- Affected npm/electron: vulnerable >= 44.0.0-alpha.1, < 44.0.0-beta.5 patched 44.0.0-beta.5
- Credits: Mickey777777

### Impact

Windows opened from a sandboxed top-level document did not inherit that document's HTML `sandbox` restrictions, so content that was meant to run sandboxed could open a window with the app's full origin. GHSA-hq2x-r82h-9wj4 covers the same issue for sandboxed iframes.

Apps are only affected if they render untrusted content in a sandboxed top-level document that allows popups. Apps that deny popups from untrusted content with `setWindowOpenHandler` are not affected.

### Workarounds

Return `{ action: 'deny' }` from `setWindowOpenHandler` for windows opened by untrusted content.

### Fixed Versions

* `44.0.0-beta.5`
* `43.4.1`
* `42.9.2`
* `41.10.6`

### For more information

If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)


## GHSA-hq2x-r82h-9wj4 — Electron drops inherited HTML sandbox restrictions for popups opened through OpenURLFromTab
- CVE: CVE-2026-102673 | Severity: high | CVSS: 8.2 `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:L/A:N` | CWE: CWE-346, CWE-693
- Published: 2026-08-29T00:33:03Z | URL: https://github.com/electron/electron/security/advisories/GHSA-hq2x-r82h-9wj4
- Affected npm/electron: vulnerable < 41.10.4 patched 41.10.4
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.5.2 patched 42.5.2
- Affected npm/electron: vulnerable >= 43.0.0-alpha.1, < 43.0.0 patched 43.0.0
- Credits: varisys

### Impact

Popups opened from a sandboxed iframe through a link (for example `target="_blank"` or a middle-click) did not inherit the iframe's HTML `sandbox` restrictions. Content that was meant to run sandboxed could open a popup with the embedding app's full origin, gaining access to that origin's cookies, storage, and same-origin scripting.

Apps are only affected if they embed untrusted content in iframes sandboxed with `allow-scripts allow-popups`. Apps that do not embed untrusted content in sandboxed iframes are not affected.

### Workarounds

Use `setWindowOpenHandler` on the parent `WebContents` to deny or constrain popups opened from sandboxed frames, or do not apply `allow-popups` to sandboxed iframes that render untrusted content.

### Fixed Versions

* `43.0.0`
* `42.5.2`
* `41.10.4`

### For more information

If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-vv43-5jgx-7qv8 — Local race condition in Squirrel.Mac update installation on macOS
- CVE: CVE-2026-102672 | Severity: medium | CVSS: 6.7 `CVSS:3.1/AV:L/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:H` | CWE: CWE-367
- Published: 2026-08-29T05:44:34Z | URL: https://github.com/electron/electron/security/advisories/GHSA-vv43-5jgx-7qv8
- Affected npm/electron: vulnerable < 39.8.10 patched 39.8.10
- Affected npm/electron: vulnerable >= 40.0.0-alpha.1 patched 
- Affected npm/electron: vulnerable >= 41.0.0-alpha.1, < 41.10.5 patched 41.10.5
- Affected npm/electron: vulnerable >= 42.0.0-alpha.1, < 42.0.0-beta.2 patched 42.0.0-beta.2
- Credits: sgretas

### Impact

On macOS, Electron bundles the Squirrel.Mac auto-update framework, whose privileged `ShipIt` helper performs the final step of an update as root. A local attacker could cause that helper to overwrite a different application's files, as root, instead of the app that started the update. Exploitation requires local access to the machine.

Apps are only affected on macOS if they ship Squirrel.Mac-based auto-updates. Apps on other platforms, or that do not use Squirrel.Mac auto-updates, are not affected.

### Workarounds

There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions

* `42.0.0-beta.2`
* `41.10.5`
* `39.8.10`

### For more information

If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)


## GHSA-fw47-9c62-h3vw — HID and USB permission checks can be attributed to the wrong origin
- CVE: CVE-2026-113800 | Severity: medium | CVSS: 5.4 `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:L/I:L/A:N` | CWE: CWE-346
- Published: 2026-10-15T21:22:47Z | URL: https://github.com/electron/electron/security/advisories/GHSA-fw47-9c62-h3vw
- Affected npm/electron: vulnerable >= 45.0.0-alpha.1, < 45.0.0-alpha.5 patched 45.0.0-alpha.5
- Affected npm/electron: vulnerable >= 44.0.0-alpha.1, < 44.3.0 patched 44.3.0
- Affected npm/electron: vulnerable >= 43.0.0-alpha.1, < 43.7.0 patched 43.7.0
- Affected npm/electron: vulnerable < 42.11.3 patched 42.11.3
- Credits: HuzaifaAbdulRehman

### Impact
For `hid` and `usb` permission checks made from an iframe, `session.setPermissionCheckHandler` was given the top-level frame's origin and details instead of the requesting frame's. Apps that allow these permissions based on origin could grant an embedded frame access intended for the top-level page.

You're only affected if you use `setPermissionCheckHandler` with origin-based logic for `hid` or `usb` and embed cross-origin iframes with `allow="hid"` or `allow="usb"`. Apps that don't delegate those features to untrusted iframes are not affected.

### Workarounds
Don't add `allow="hid"` / `allow="usb"` to untrusted iframes, or make the decision in your `select-hid-device` / `select-usb-device` handler using `details.frame`.

### Fixed Versions
* `45.0.0-alpha.5`
* `44.3.0`
* `43.7.0`
* `42.11.3`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-997q-gvvc-jwmx — openExternal permission requests can be attributed to the wrong origin
- CVE: CVE-2026-114121 | Severity: medium | CVSS: 5.4 `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:L/I:L/A:N` | CWE: CWE-346
- Published: 2026-10-15T21:22:52Z | URL: https://github.com/electron/electron/security/advisories/GHSA-997q-gvvc-jwmx
- Affected npm/electron: vulnerable < 42.11.3 patched 42.11.3
- Affected npm/electron: vulnerable >= 43.0.0-alpha.1, < 43.7.0 patched 43.7.0
- Affected npm/electron: vulnerable >= 44.0.0-alpha.1, < 44.3.0 patched 44.3.0
- Affected npm/electron: vulnerable >= 45.0.0-alpha.1, < 45.0.0-alpha.5 patched 45.0.0-alpha.5
- Credits: scofaild23

### Impact
Requests to open external protocol URLs could be attributed to a document other than the one that asked for them, so the `requestingUrl` passed to `session.setPermissionRequestHandler` was a trusted origin for a launch untrusted content had requested. An origin-based handler could therefore let untrusted content launch an OS-registered external application.

Apps are only affected if they grant `openExternal` based on the requesting origin and let untrusted content open or navigate windows. Apps whose permission handler denies `openExternal` for untrusted content are not affected.

### Workarounds
Deny the `openExternal` permission for untrusted content, or deny the windows it opens with `setWindowOpenHandler`.

### Fixed Versions
* `45.0.0-alpha.5`
* `44.3.0`
* `43.7.0`
* `42.11.3`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-h3v5-h239-pg29 — Off-screen rendering on macOS trusts GPU-supplied frame geometry
- CVE: CVE-2026-114124 | Severity: low | CVSS: 3.9 `CVSS:3.1/AV:L/AC:H/PR:H/UI:N/S:C/C:L/I:N/A:L` | CWE: CWE-125
- Published: 2026-10-15T21:22:58Z | URL: https://github.com/electron/electron/security/advisories/GHSA-h3v5-h239-pg29
- Affected npm/electron: vulnerable < 42.11.6 patched 42.11.6
- Affected npm/electron: vulnerable >= 43.0.0-alpha.1, < 43.7.3 patched 43.7.3
- Affected npm/electron: vulnerable >= 44.0.0-alpha.1, < 44.4.3 patched 44.4.3
- Affected npm/electron: vulnerable >= 45.0.0-alpha.1, < 45.0.0-alpha.9 patched 45.0.0-alpha.9
- Credits: manus-pi

### Impact
In offscreen rendering mode on macOS, frame data received from the GPU process was not fully validated by the main process. A compromised GPU process could cause the main process to read out-of-bounds memory while producing `paint` event images, disclosing memory or crashing the app. GHSA-pfmc-3mgc-p6fp covers the same issue on the other capture paths.

Apps are only affected if they use offscreen rendering (`webPreferences.offscreen`) on macOS and an attacker has separately gained code execution in the GPU process. Apps that do not use offscreen rendering are not affected.

### Workarounds
There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions
* `45.0.0-alpha.9`
* `44.4.3`
* `43.7.3`
* `42.11.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-3qxv-5xgr-q7w9 — Frame subscription trusts GPU-supplied frame geometry
- CVE: CVE-2026-114122 | Severity: low | CVSS: 3.9 `CVSS:3.1/AV:L/AC:H/PR:H/UI:N/S:C/C:L/I:N/A:L` | CWE: CWE-125
- Published: 2026-10-15T21:23:12Z | URL: https://github.com/electron/electron/security/advisories/GHSA-3qxv-5xgr-q7w9
- Affected npm/electron: vulnerable < 42.11.6 patched 42.11.6
- Affected npm/electron: vulnerable >= 43.0.0-alpha.1, < 43.7.3 patched 43.7.3
- Affected npm/electron: vulnerable >= 44.0.0-alpha.1, < 44.4.3 patched 44.4.3
- Affected npm/electron: vulnerable >= 45.0.0-alpha.1, < 45.0.0-alpha.9 patched 45.0.0-alpha.9
- Credits: manus-pi

### Impact
Frame data received from the GPU process for `webContents.beginFrameSubscription` was not fully validated by the main process. A compromised GPU process could cause the main process to read out-of-bounds memory while producing the captured frame images, disclosing memory or crashing the app.

Apps are only affected if they use `webContents.beginFrameSubscription` and an attacker has separately gained code execution in the GPU process. Apps that do not subscribe to captured frames are not affected.

### Workarounds
There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions
* `45.0.0-alpha.9`
* `44.4.3`
* `43.7.3`
* `42.11.6`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-x562-297c-g43g — Pointer lock permission requests can be attributed to the wrong frame
- CVE: CVE-2026-113798 | Severity: medium | CVSS: 5.4 `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:L/A:L` | CWE: CWE-346
- Published: 2026-10-15T21:27:06Z | URL: https://github.com/electron/electron/security/advisories/GHSA-x562-297c-g43g
- Affected npm/electron: vulnerable >= 45.0.0-alpha.1, < 45.0.0-alpha.13 patched 45.0.0-alpha.13
- Affected npm/electron: vulnerable >= 44.0.0-alpha.1, < 44.5.0 patched 44.5.0
- Affected npm/electron: vulnerable >= 43.0.0-alpha.1, < 43.7.6 patched 43.7.6
- Affected npm/electron: vulnerable < 42.11.9 patched 42.11.9
- Credits: manus-pi, manus-use

### Impact
For `pointerLock` permission requests made from some cross-origin iframes, `session.setPermissionRequestHandler()` was given the top-level frame's `requestingUrl` and `isMainFrame` instead of the requesting frame's. Apps that grant pointer lock based on the requesting origin could grant it to embedded content under the top-level page's identity.

Apps are only affected if they embed untrusted content in iframes and decide `pointerLock` requests by origin in `setPermissionRequestHandler`. Apps that do not embed untrusted content, or that deny `pointerLock` for it, are not affected.

### Workarounds
Deny the `pointerLock` permission for web contents that embed untrusted frames.

### Fixed Versions
* `45.0.0-alpha.13`
* `44.5.0`
* `43.7.6`
* `42.11.9`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-98mx-cjp9-gchm — Extension tabs.query returns tab URLs and titles without the tabs permission
- CVE: CVE-2026-113797 | Severity: low | CVSS: 3.1 `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:N/A:N` | CWE: CWE-862
- Published: 2026-10-15T21:27:09Z | URL: https://github.com/electron/electron/security/advisories/GHSA-98mx-cjp9-gchm
- Affected npm/electron: vulnerable >= 45.0.0-alpha.1, < 45.0.0-alpha.4 patched 45.0.0-alpha.4
- Affected npm/electron: vulnerable >= 44.0.0-alpha.1, < 44.1.1 patched 44.1.1
- Affected npm/electron: vulnerable >= 43.0.0-alpha.1, < 43.5.1 patched 43.5.1
- Affected npm/electron: vulnerable < 42.11.1 patched 42.11.1

### Impact
`chrome.tabs.query()` returned each tab's `url` and `title` to extensions that held neither the `tabs` permission nor matching host permissions, so any loaded extension could read the URL and title of every webContents in its session.

Apps are only affected if they load extensions (`session.extensions.loadExtension`) that they do not fully trust. Apps that load no extensions, or only trusted ones, are not affected.

### Workarounds
Do not load untrusted or unvalidated extensions. In general you should only load trusted extensions.

### Fixed Versions
* `45.0.0-alpha.4`
* `44.1.1`
* `43.5.1`
* `42.11.1`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-22mq-c535-7vv9 — Out-of-package denial-of-service for CommonJS Electron apps packaged with ASAR
- CVE: None | Severity: medium | CVSS: 5.5 `CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H` | CWE: CWE-427
- Published: 2026-10-15T21:30:18Z | URL: https://github.com/electron/electron/security/advisories/GHSA-22mq-c535-7vv9
- Affected npm/electron: vulnerable >= 36.0.0-alpha.1, < 36.0.0-alpha.5 patched 36.0.0-alpha.5
- Affected npm/electron: vulnerable >= 35.0.0-alpha.1, < 35.1.0 patched 35.1.0
- Credits: erickzhao

### Impact
A CommonJS app packaged in an ASAR archive could be prevented from launching by a `package.json` in a directory above the app, for example one that is malformed or declares `"type": "module"`. Because that file is outside the app's own package, a local user able to write to an ancestor directory of the install location could stop the app from starting.

Apps are only affected on Electron 35 and 36 if their main-process entry point is CommonJS and packaged in an ASAR archive. Apps whose entry point is an ES module are not affected.

### Workarounds
There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions
* `36.0.0-alpha.5`
* `35.1.0`

### For more information
If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

## GHSA-2p8c-gr87-2676 — SameSite cookie restrictions are not applied to windows opened from links
- CVE: CVE-2026-113796 | Severity: medium | CVSS: 4.2 `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:L/I:L/A:N` | CWE: CWE-352
- Published: 2026-10-15T22:04:51Z | URL: https://github.com/electron/electron/security/advisories/GHSA-2p8c-gr87-2676
- Affected npm/electron: vulnerable >= 45.0.0-alpha.1, < 45.0.0-alpha.6 patched 45.0.0-alpha.6
- Affected npm/electron: vulnerable >= 44.0.0-alpha.1, < 44.3.0 patched 44.3.0
- Affected npm/electron: vulnerable >= 43.0.0-alpha.1, < 43.7.0 patched 43.7.0
- Affected npm/electron: vulnerable < 42.11.3 patched 42.11.3
- Credits: mingijunggrape

### Impact

Pages opened into a new window from a link were loaded as if the app itself had navigated there rather than the page that contained the link, so the request was treated as same-site: `SameSite=Strict` cookies were sent and `Sec-Fetch-Site` did not identify the initiating page. Content shown in the app could use this to make a credentialed top-level request to another site that relies on SameSite cookies as a CSRF defence.

Apps are only affected if they load untrusted content and allow it to open new windows. Apps that deny new windows from untrusted content with `setWindowOpenHandler` are not affected.

### Workarounds

Return `{ action: 'deny' }` from `setWindowOpenHandler` for windows opened by untrusted content.

### Fixed Versions

* `45.0.0-alpha.6`
* `44.3.0`
* `43.7.0`
* `42.11.3`

### For more information

If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)


## GHSA-jr5w-w6x2-84p9 — Mitigation for compromised eMudhra intermediate certificates
- CVE: CVE-2026-115570 | Severity: high | CVSS: 7.4 `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N` | CWE: CWE-299
- Published: 2026-10-22T04:37:15Z | URL: https://github.com/electron/electron/security/advisories/GHSA-jr5w-w6x2-84p9
- Affected npm/electron: vulnerable >= 45.0.0-alpha.1, < 45.0.0-beta.6 patched 45.0.0-beta.6
- Affected npm/electron: vulnerable >= 44.0.0-alpha.1, < 44.9.1 patched 44.9.1
- Affected npm/electron: vulnerable >= 43.0.0-alpha.1, < 43.8.1 patched 43.8.1
- Affected npm/electron: vulnerable < 42.11.16 patched 42.11.16
- Credits: MarshallOfSound

### Impact

A set of eMudhra intermediate certificates were compromised and are being blocked by browsers and other TLS clients. This Electron update adds the same block to both Chromium networking and Node.js `tls`, `https` and `fetch`. On earlier versions, an attacker holding a certificate issued through these intermediates and able to intercept network traffic could impersonate a TLS server to an app.

Apps are only affected if they make TLS connections over a network an attacker can intercept. Apps that make no network connections are not affected.

Other software has shipped the same mitigation, including Go (CVE-2026-111943) and Firefox (CVE-2026-113470).

### Workarounds

There are no app side workarounds, you must update to a patched version of Electron.

### Fixed Versions

* `45.0.0-beta.6`
* `44.9.1`
* `43.8.1`
* `42.11.16`

### For more information

If you have any questions or comments about this advisory, email us at [security@electronjs.org](mailto:security@electronjs.org)

