# Windows 11’s “Checking for Updates” Freeze Isn’t a Bug. It’s These 3 Things.

- **Source URL:** https://medium.com/@rama.geek/windows-11s-checking-for-updates-freeze-isn-t-a-bug-it-s-these-3-things-ca7f7be3ab37
- **Fetched from:** https://medium.com/@rama.geek/windows-11s-checking-for-updates-freeze-isn-t-a-bug-it-s-these-3-things-ca7f7be3ab37?source=rss-42535406987f------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14922 (id 14922)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Palla Sridhar / Thu, 24 Sep 2026 03:41:46 GMT

Frozen. Spinning. Going nowhere.

That’s what “Checking for updates” looks like when Windows 11 stalls out. No error. No progress bar. Just an endless circle, spinning in place.

Frustrating, sure. But fixable. Almost always fixable.

Below, nine real fixes. Fastest first. Deepest last. Skip straight to whichever fits your situation. For a more detailed reference, this guide expands on [WindowsTechIT’s breakdown of Windows 11 stuck checking for updates](https://www.windowstechit.com/59047/windows-11-stuck-checking-for-updates/), worth a bookmark for future update headaches.

Patience matters here.

A spinning circle with no percentage means Windows hasn’t started downloading anything yet. It’s still trying to reach Microsoft’s servers.

Give it ten minutes. Fifteen, tops.

Still spinning after that? Now it’s actually stuck. Time to act.

Simple. Quick. Often enough on its own.

Open Settings. Go to System, then Troubleshoot, then Other troubleshooters. Run Windows Update.

It checks the service status. Scans for corrupted cache files. Flags pending restarts. Fixes plenty, automatically, no command line required.

Try this first. Save the deeper fixes for later.

Two names to know: wuauserv and BITS.

Press Windows + R. Type services.msc. Hit Enter.

Find Windows Update in the list. Right-click. Restart it. Already stopped? Start it instead.

Next, find Background Intelligent Transfer Service. Same treatment. Restart it too.

Why both? Simple. wuauserv checks for updates. BITS downloads them. Stall either one, and the whole process freezes silently. Restart both together. Not just one.

This single step unsticks more frozen updates than anything else on this list.

Still stuck? Dig deeper.

Windows stores update files in one place: C:\Windows\SoftwareDistribution. A single interrupted download here can leave Windows permanently confused.

Stop the Windows Update and BITS services first. Always first.

Then delete everything inside the Download subfolder. Restart both services. Check for updates again.

Windows rebuilds the folder automatically. No manual repair needed. No selective fix required. Just clear it out and start fresh.

Barely known. Quietly powerful.

Windows Update Medic Service repairs broken update components on its own, in the background, without asking.

Open an elevated Command Prompt. Run **sc query wuauserv** to confirm the service isn’t disabled. Then restart your PC.

Often, that’s it. Component corruption, gone. No extra steps needed.

Still nothing? Go nuclear. Carefully.

Open Command Prompt as administrator. Stop three services: wuauserv, bits, and cryptsvc.

Rename two folders: SoftwareDistribution and catroot2. Just add “.bak” to each.

Restart all three services. Check for updates.

Windows rebuilds everything from scratch. Every cache. Every component. A clean slate, forced from the ground up.

Order matters here. A lot.

Recurring update failures usually point somewhere deeper: damaged system files, not a stuck service.

First, System File Checker. Open Command Prompt as administrator. Run **sfc /scannow**. Let it finish. Fully. Don’t interrupt it.

Next, DISM. Run **DISM /Online /Cleanup-Image /RestoreHealth**.

Sequence matters. SFC repairs files using the Windows image as a source. DISM repairs that image first. Run DISM before SFC, and both tools work worse. Run SFC first, always.

Not a spinning circle this time. A number. Frozen at zero.

Usually means one thing: low disk space. Especially on the small EFI system partition.

Free up at least 20GB. On your main drive. Before repeating anything above.

Disk space first. Troubleshooting second.

Sometimes it’s not Windows at all. It’s the network.

Check your internet in a browser first. Working fine? Good. Now check for interference.

**VPN or proxy active?** Disconnect the VPN temporarily. Using a manual proxy? Switch to “Automatically detect settings” under Settings, Network & Internet, Proxy.

**Clock off by a few minutes?** That’s enough to break security certificates silently. Go to Settings, Time & language, Date & time. Turn on “Set time automatically.” Sync now.

**On a work or school laptop?** Group Policy might be blocking updates deliberately. Press Windows + R, type gpedit.msc, and check Computer Configuration, Administrative Templates, Windows Components, Windows Update. Something enabled and unfamiliar? Flag it to IT. Don’t change it yourself.

Antivirus tools. Startup apps. Background utilities.

Any one of them can quietly block Windows Update’s connection.

Run a clean boot. Open System Configuration (msconfig). Go to Services. Check “Hide all Microsoft services.” Disable everything left. Restart. Check for updates.

Problem gone? Something you disabled was the culprit. Re-enable one at a time to find it.

September 2026’s Patch Tuesday brought KB5124008. Confirmed. Cumulative. Covers both 24H2 and 25H2.

Press Windows + R. Type winver. Hit Enter. Check your build number.

Waiting on this specific update? Might just be slow, not stuck. Worth confirming before assuming the worst.

Still on Windows 11 23H2? Check whether it’s reached end of servicing first. No point troubleshooting an update that’s no longer offered.

A few habits, worth breaking immediately:

Running DISM before SFC. Weaker results, every time.

Force-restarting the moment the circle appears. Wait first. Restart services second. Force-restart last.

Clearing SoftwareDistribution without stopping services first. Fails silently. Gets blocked halfway.

Ignoring low disk space. Repeating the same fix, over and over, without freeing anything up.

Leaving a VPN connected while troubleshooting, then blaming Windows Update for a problem the VPN itself caused.

Stuck updates aren’t random. Almost always, three culprits: a stalled service, a corrupted cache, or a connection issue.

Start simple. Run the troubleshooter. Restart the two key services.

Still stuck? Go deeper. Clear the cache. Reset the components. Run SFC, then DISM.

Nothing files, nothing personal, ever touched. Just update data, cleared and rebuilt.

Patience helps. The right sequence helps more. For the complete troubleshooting reference — including full command syntax and additional edge cases — check the [original guide on WindowsTechIT](https://www.windowstechit.com/59047/windows-11-stuck-checking-for-updates/).
