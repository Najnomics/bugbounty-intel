# Windows Sandbox Attack Surface Analysis - Project Zero

Source: https://projectzero.google/2015/11/windows-sandbox-attack-surface-analysis.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by James Forshaw, Quartermaster of Tools


Analysing the attack surface of user-mode sandboxed applications is a good way to hunt for elevation of privilege vulnerabilities. Much of the task of enumerating the attack surface could be done manually, but that’s a very tedious and error prone procedure. Obviously automating that process as much as possible is important both for initial analysis as well as detecting potential regressions.


TL;DR; I’ve released my tools I use internally to test out sandboxed code and determine the likely attack surface exposed to an attacker if a sandboxed process is compromised. You can get the source code from [https://github.com/google/sandbox-attacksurface-analysis-tools](https://github.com/google/sandbox-attacksurface-analysis-tools). This blog post will describe a few common use cases so that you can use them to do your own sandbox analysis.

# Background

Writing a user-mode sandbox is a difficult challenge for various different reasons (see my  Shmoocon/Nullcon [presentation](https://www.youtube.com/watch?v=TN7429iGMU8) I did this year for some examples, in fact I was planning on releasing the tools for Shmoocon but it didn’t happen in time). However in most user-mode implementations, such as Chrome, IE or Edge the sandboxing is done through assigning a restrictive process token so that only a very small number of securable resources can be accessed, ideally no resources at all should be accessible.


An obvious example of a securable resource is the file system. We’d like to know, for example, which locations a sandboxed process can access for read and/or write. A well known tool which comes to mind is [AccessChk](https://technet.microsoft.com/en-gb/sysinternals/bb664922.aspx) from Sysinternals ( Microsoft these days). AccessChk allows us to enumerate the security of the file system (as well as many of the secured resources such as the registry or object manager) but only tells you whether you could write to a resource based on a user or group account. For example, running the command ‘accesschk.exe -w users c:\windows’ will show you what files or directories a process that runs with the BUILTIN\Users group can access. However, that doesn’t really help us when it comes to a sandboxed application, which might have a restrictive token that results in a more complex access checking model.


For example, Chrome and Adobe Reader use [Restricted Tokens](<https://msdn.microsoft.com/en-us/library/windows/desktop/aa379316(v=vs.85).aspx>) to limit what resources the sandboxed process can access; this changes how the normal kernel access check works. And then there are Mandatory Integrity Labels, which also change what resources you can write to. You can summarise the access check for a restricted token in the below diagram.


And let’s not forget the introduction of LowBox tokens in Windows 8, which have a similar, but different access checks. And what if you mix both LowBox and restricted tokens? In general this is too complex to replicate accurately; fortunately, Windows provides a means of calculating the granted access to a resource which allows us to to automate a lot of the analysis of various different resources. For that reason I developed my own set of tools to do this which I’ve released as open-source under an Apache v2 license at [https://github.com/google/sandbox-attacksurface-analysis-tools](https://github.com/google/sandbox-attacksurface-analysis-tools). In the rest of this blog post I’ll describe some of the tools, giving simple examples of use and why you might want to use them.

## The Check\* Tools

The core of the suite is the Check\* tools. Their purpose is to determine whether the process token for a particular sandboxed application can be used to get access to a specific secured resource. For example CheckFileAccess will scan a given location on the file system comparing the Security Descriptor of a file or directory against the process token and determine whether the process would have read and/or write access.


The core to the operation of the tools is the [AccessCheck](<https://msdn.microsoft.com/en-us/library/windows/desktop/aa374815(v=vs.85).aspx>) function exposed by the Win32 APIs. This is actually a kernel system call, NtAccessCheck under the hood, and uses the same algorithms as a normal access check performed during the opening of an existing resource. Therefore we can be reasonably confident that the result of operation would match what we’d be able to get access to. The AccessCheck function takes an impersonation token; in this case we’ll use the primary token of a specified process (ideally sandboxed), convert it to an impersonation token, and pass the Security Descriptor for the resource we are interested in. We can then request the kernel determines the maximum allowed permissions for that token.


The following table is a list of the available tools for analysing different types of resources. They all take a command --pid parameter, which specifies the PID of a process to base the security check on.


| Name | Description | 
| CheckDeviceAccess | Checks allowed access to Device Objects such as \Device\HarddiskVolume1 | 
| CheckFileAccess | Checks allowed access to the file system. | 
| CheckNetworkAccess | Checks allowed access to connecting or binding network sockets. This is for testing AppContainer lockdown. | 
| CheckObjectManagerAccess | Checks allowed access to resources and directories in the object manager namespace. | 
| CheckProcessAccess | Checks allowed access to processes. | 
| CheckRegistryAccess | Checks allowed access to the registry. | 


For example if you want to check what files and directories a sandboxed process can write to on the C: drive you can run the following command:

CheckFileAcccess -w -r -p \<PID> C:\


The -w parameter specifies only display files or directories with at least one Write permission available (for example Write File, or Add File for directories, or a standard right such as Write DACL). The -r parameter performs the check recursively and the -p specifies the PID of the sandboxed process to test. It’s recommended to run the tool as an administrator as that ensures the tool can recurse into as many directories as possible. If we do this for the Chrome GPU process we find some interesting entries such as being able to write to c:\ProgramData\Microsoft\Windows\DRM.


The CheckDeviceAccess tool deviates from most of the others as it has to actually attempt to open a device node while impersonating the sandboxed token. This is because while the device object itself might have a Security Descriptor, Windows devices by default are considered to be file systems. This means that if you have a device object with the name \Device\Harddisk1 you can also try and access \Device\Harddisk1\SomeName and depending on how the device was registered it might be up to the driver itself to enforce security when accessing SomeName. The only reliable way of determining whether this is the case for a particular device object is to just open the path and see if it works.


A simple example is just to recursively check all Device objects in the object manager namespace using the command:

CheckDeviceAccess -r -l -p \<PID> \


The -l parameter will try and map the device name to a symbolic link; this is quite useful for automatically named devices (which look like \Device\00000abc) as the symbolic link is generally more descriptive. For the Chrome renderer sandbox this simple command shows we can access devices such as the NTFS file system driver and AFD (which is the socket driver) but admittedly only if you access it through the namespace. Code running within the Chrome renderer sandbox cannot open any Device object itself.


Of course not all Devices can be tested in this manner; by default, the tool tries to open DeviceName\Dummy but some drivers require a specific path name otherwise they won’t open (you can change Dummy using the --suffix parameter). Still it gives you a quick list of drivers to go hunting for sandbox escape vulnerabilities.

## And the Best of the Rest

Not all the tools in the suite are for checking direct access checking, I’ll summarise a few of the other tools which you might find useful.

#### DumpProcessMitigations

This tool dumps a list of process mitigations which have been applied through the [SetProcessMitigationPolicy](<https://msdn.microsoft.com/en-us/library/windows/desktop/hh769088(v=vs.85).aspx>) API. This only works on Windows 8 and above. Examples of mitigations that could be enabled include Win32k Syscall Disable, Forced ASLR and Custom Font Disable. For example, to dump all processes with Win32k System Call Disable Policy run the following command as an Administrator:

DumpProcessMitigations -t DisallowWin32kSystemCalls

#### EditSection

This is a GUI tool which allows you to view the contents of a shared memory section, modify it in a hex editor, and execute a couple of ways of corrupting the section to test for trivial security issues. A section can be opened through its object name or via extracting handles from a running process. I developed this tool for investigating the Chrome section issue I documented in my blog [here](/2014/10/did-man-with-no-name-feel-insecure.html).


#### GetHandles

This is just a generic command line tool to dump open handles in all processes in the system. While that in itself wouldn’t differentiate it from other similar tools already available (such as SysInternals [Handle](https://technet.microsoft.com/en-gb/sysinternals/bb896655) utility) it does have one interesting feature. You can group handles by certain properties such as the address of the kernel mode object. This allows you to find instances where an object is shared between two processes at different privilege levels (say between a browser process and its sandboxes tabs) which might allow for privilege escalation attacks to occur. For example running the following command as an Administrator will dump the section objects shared between different Chrome processes.


GetHandles.exe -n chrome -t Section -g object -s partial


This will produce output similar to the following, which shows two section objects shared between different processes:

Object: FFFFC00128086060

11020/0x2B0C/chrome 4/0x4:              Section 00000006 (unknown)

10264/0x2818/chrome 15636/0x3D14:       Section 000F0007 (unknown)


Object: FFFFC00135F82A00

13644/0x354C/chrome 4/0x4:              Section 00000006 (unknown)

10264/0x2818/chrome 11956/0x2EB4:       Section 000F0007 (unknown)


There’s also the CommonObjects tool, which does a similar job but doesn’t have as many other features.

#### TokenViewer

This GUI tool allows you to inspect and manipulate access tokens as well as do some basic tests of what you can do with that token (such as opening files). You can either look at the token for a specific process (or even open token handles inside those processes) or you can create ones using common APIs.
