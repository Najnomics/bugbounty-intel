# From Named Pipe to SYSTEM

- **Source URL:** https://sneharghya.medium.com/from-named-pipe-to-system-how-i-found-a-local-privilege-escalation-in-a-major-windows-application-6a77a179a461
- **Fetched from:** https://sneharghya.medium.com/from-named-pipe-to-system-how-i-found-a-local-privilege-escalation-in-a-major-windows-application-6a77a179a461?source=rss-848087c942a5------2
- **Fetched:** 2026-11-25
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/14933 (id 14933)
- **Method:** medium-rss-feed (full content:encoded) readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
- **Author/Published (RSS):** Sneharghya Roy / Sun, 04 Oct 2026 15:48:13 GMT

A local privilege-escalation vulnerability in a **major Windows tax and financial software product**, chaining an overly permissive named pipe, a misconfigured .NET Remoting endpoint, a SYSTEM-level file-write primitive, and a Windows lock-screen DLL load into a SYSTEM shell.

*The vulnerability was discovered and reported through a* ***private bug-bounty program.*** *The original service and pipe names have been partially redacted because they contain vendor-specific identifiers. The technical details and exploitation flow are otherwise unchanged.*

I was scanning named-pipe DACLs using Sysinternals accesschk, which is a quick one-liner:

accesschk.exe -accepteula -w \pipe\\\* 2>$null

Most pipes on a Windows machine are either locked down to specific service accounts or exposed to Everyone for legitimate reasons. You learn to filter through the noise pretty quickly.

Then I came across this:

\\.\Pipe\UpdateServicev5.Spc.Esd.Client.Common.Utilities.5.3.2.0

Medium Mandatory Level (Default) \[No-Write-Up\]

RW Everyone

FILE\_ALL\_ACCESS

RW NT AUTHORITY\SYSTEM

FILE\_ALL\_ACCESS

RW BUILTIN\Administrators

READ\_CONTROL

WRITE\_DAC

FILE\_ALL\_ACCESS for Everyone immediately caught my attention. It wasn't Authenticated Users, it wasn't BUILTIN\Users, and it certainly wasn't some standard Windows pipe I already knew about. This belonged to a third-party application.

The pipe name also suggested that it was related to an update or client service, so I made a note of it and started looking at what was actually listening on the other end.

The first question with an interesting named pipe is fairly straightforward: which process owns it?

I used Sysinternals handle.exe:

handle.exe -a "UpdateService"

The answer was:

UpdateService.exe   pid: 2992   type: File   \Device\NamedPipe\...

UpdateService.exe pid: 2992 type: File \Device\NamedPipe\...

So the pipe belonged to UpdateService.exe. I then checked the service configuration:

sc.exe qc UpdateServiceV5

The relevant part was:

SERVICE\_START\_NAME : LocalSystem

START\_TYPE : 2 AUTO\_START (DELAYED)

Bingo. A third-party service running as **LocalSystem**, booting automatically, and serving up an unrestricted named pipe.

At this point I had the two ingredients that make a named-pipe vulnerability particularly interesting: an IPC endpoint accessible to an unprivileged local user and a SYSTEM-level process sitting at the other end.

The next question was whether the permissions actually translated into a usable connection.

Theoretical bad ACLs are fun, but Windows can be weird about enforcement. I opened a non-elevated PowerShell session to test if the pipe would actually talk to me:

```
$pipe = New-Object System.IO.Pipes.NamedPipeClientStream(".", "UpdateServicev5.Spc.Esd.Client.Common.Utilities.5.3.2.0", [System.IO.Pipes.PipeDirection]::InOut)
$pipe.Connect(3000)
$pipe.IsConnected
```
And the result was simply True.

Well, that was interesting. There was no authentication challenge, no token validation, and no rejection. A standard user had successfully opened a full-duplex connection to an IPC endpoint belonging to a SYSTEM process.

So the ACL wasn’t just theoretically wrong. It was actually usable.

Now I needed to figure out what I could make the service do.

Connecting to a pipe is useless if you’re sending gibberish.

I peeked inside the service binary using strings.exe to see if I could quickly identify what tech stack I was dealing with:

v4.0.30319

BSJB

**.NET Framework 4.8 !**

That made the next part considerably easier. No wrestling with x64 assembly or IDA Pro for a good chunk of my day. Once strings.exe confirmed it was a .NET assembly, I immediately popped the binaries into **dnSpy.**

After tracing the service’s assembly references, I found the relevant implementation in the GAC:

C:\Windows\Microsoft.NET\assembly\GAC\_64\

xxxxx.Spc.Esd.WinClient.Ipc.Remoting.UpdateServiceWorker\

v4.0\_5.3.2.0\_\_3ff6b78e2989595a\

xxxxx.Spc.Esd.WinClient.Ipc.Remoting.UpdateServiceWorker.dll

Notice that namespace? Ipc.Remoting.

This wasn’t a custom binary protocol. This was ancient, legendary **.NET Remoting over Named Pipes**.

In the server implementation, I found:

dictionary\["authorizedGroup"\] = OSUtilities.GetLocalizedEveryoneAccountName();

I read this a few times because the implications were pretty clear.

They literally grabbed the localized string for “Everyone”, handed it to the IPC channel, and registered an object called **ElevatedBitsFileTransferor**.

I think the name speaks for itself.

I dug into ElevatedBitsFileTransferor and found this clean little method:

public void StartForegroundJobInBackground(string esdJobId, List\<FileResource> files)

{

BitsFileTransferor fileTransferor = this.GetFileTransferor(null);

foreach (FileResource resource in files)

{

fileTransferor.Add(resource);

}

fileTransferor.StartForegroundJobInBackground(esdJobId);

}

The FileResource object contained:

public class FileResource

{

public string DestinationFilePath { get; set; }

public string RemoteFilePath { get; set; }

public FileReferenceData FileReference { get; set; }

}

Spot the bug? The caller controls DestinationFilePath.

There were zero path checks, zero authorization validations, and zero sanitation routines. The service took your input, spun up BITS (Background Intelligent Transfer Service), and downloaded the file under its own LocalSystem token.

I couldn’t write to C:\Program Files\, but I could ask ElevatedBitsFileTransferor nicely to do it for me.

I threw together a tiny C# client referencing the app’s GAC assemblies to talk to the exposed endpoint:

ChannelServices.RegisterChannel(new IpcClientChannel(), false);

string url = "ipc://UpdateServicev5.Spc.Esd.Client.Common.Utilities.5.3.2.0/ElevatedBitsFileTransferor";

ElevatedBitsFileTransferor remote = (ElevatedBitsFileTransferor)RemotingServices.Connect(

typeof(ElevatedBitsFileTransferor), url);

Console.WriteLine("Available: " + remote.Available);

It connected cleanly from an unprivileged user process.

Asked it to drop a harmless test file inside C:\Windows\System32. **Success.** The file appeared, owned by NT AUTHORITY\SYSTEM.

I had a solid, arbitrary SYSTEM file-write primitive. But of course, you don’t stop at just that, I wanted SYSTEM shell to complete the flex.

An arbitrary file write is great, but it’s even better if you can coax a SYSTEM process into executing it.

There are quite a few pre-existing phantom DLL opportunities in Windows where native applications attempt to load DLLs from protected directories such as System32 or other system locations. Some of these are useful for privilege-escalation research, but many of the interesting ones require the machine to be restarted before the relevant SYSTEM process performs the DLL lookup again.

Technically, that’s not a particularly difficult obstacle. A local user can restart a machine.

But I wanted a cleaner PoC. If I could trigger the DLL load without rebooting, it would demonstrate the chain much more directly (and look considerably more like 1337 haxxor).

So I started looking for a DLL-loading opportunity that I could trigger on demand.

This is where ProcMon became useful. I filtered for NAME NOT FOUND results associated with osk.exe, the Windows On-Screen Keyboard, and watched which DLL paths it attempted to access when launched.

Eventually, I found an interesting lookup involving:

C:\Program Files\Common Files\microsoft shared\ink\HID.DLL

The file wasn’t present by default.

More importantly, osk.exe when launched directly from the Windows lock screen, it executes with NT AUTHORITY\SYSTEM privileges.

Now that I had my target path, I pointed my PoC tool at C:\Program Files\Common Files\microsoft shared\ink\HID.DLL to drop the malicious DLL into place.

I ran the PoC, and the terminal output confirmed the file drop succeeded:

I hit Win+L, clicked Ease of Access, popped the On-Screen Keyboard, and a shiny, unrestricted cmd.exe running as SYSTEM appeared right on the lock screen.

There was one last hilarious detail buried in the server configuration:

new BinaryServerFormatterSinkProvider

{

TypeFilterLevel = TypeFilterLevel.Full

}

For the uninitiated, TypeFilterLevel.Full in .NET Remoting is basically like hanging a sign that says *"Please Deserialization-Attack Me."* It relaxes object type restrictions during deserialization, making it wildly susceptible to gadget chains (think ysoserial.net).

Also, someone clearly knew TypeFilterLevel was a security risk and explicitly added "typeFilterLevel"\] = "Low" to the channel dictionary. But then, right on the next line, they instantiated BinaryServerFormatterSinkProvider with TypeFilterLevel = TypeFilterLevel.Full.

Whether it was dead code left behind or a genuine mistake, the point remains: **they tried to lock the door, but left it wide open anyway.**

In fact, even Microslop [explicitly warns](https://learn.microsoft.com/en-us/dotnet/standard/serialization/binaryformatter-security-guide) on their documentation that BinaryFormatter is dangerous, insecure, and *"can't be made secure"*. When \**they\** post a red-alert caution box begging developers to stop using a feature because it’s inherently broken, you know you've done something special.

Could I have spent three hours crafting an unauthenticated deserialization exploit directly over the pipe? Absolutely.

Did I? **Nope.** I already had a working privileged file write, an on-demand DLL hijack, and a SYSTEM shell sitting on my desktop. (Ya, who am I kidding, I ran out of Claude tokens for the day).

Looking back, this wasn’t really one isolated mistake. It was several security assumptions lining up in exactly the wrong way.

The IPC endpoint trusted Everyone, despite belonging to a privileged service. The service itself ran as LocalSystem. It exposed remoting objects that performed privileged operations, including file-transfer functionality. The destination path wasn't sufficiently restricted, and the resulting operation was performed under the service's privileged security context.

On top of that, the remoting channel was configured with TypeFilterLevel.Full, creating another potentially dangerous attack surface.

None of those details are particularly exciting in isolation.

Put them together, though, and you end up with an unprivileged local user being able to cross the security boundary into SYSTEM.
