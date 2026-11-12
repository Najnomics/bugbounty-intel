# In-Console-Able - Project Zero

Source: https://projectzero.google/2015/05/in-console-able.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by James Forshaw, giving the security community a shoulder to cry on.


TL;DR; this blog post describes an [unfixed](https://code.google.com/p/google-security-research/issues/detail?id=213) bug in Windows 8.1 which allows you to escape restrictive job objects in order to help to develop a sandbox escape chain in Chrome or similar sandboxes.

If you’re trying to develop a secure application sandbox in user-mode you’re at the mercies of the underlying operating system. While you can try and use every available security feature, sometimes the OS developer ends up subverting your efforts. This was the topic of my presentation at [Shmoocon](https://ia601501.us.archive.org/15/items/shmoocon-2015-videos-playlist/Windows%20Sandbox%20Paradox%20%5BSC2015%5D.mp4) and [Nullcon](http://nullcon.net/website/archives/ppt/goa-15/the-windows-sandbox-paradox.pdf), focusing on the difficulty of securing a user-mode sandbox on Windows.

Exploiting a modern sandboxed application typically requires a chain of bugs to fully compromise the application and escape the sandbox. Some of these bugs might not in themselves seem very serious, but chained together they lead to a complete compromise. This blog post will focus on a specific [issue](https://code.google.com/p/google-security-research/issues/detail?id=213) that Microsoft decided not to fix, and which has an impact on sandboxes such as that used in Chrome. I wasn’t able to present it at the conference, so I’ll go into some depth here on how the bug works, how much it compromised sandbox security and how to practically exploit it.

## Windows Job Objects

Let’s first describe what a [Job object](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684161%28v=vs.85%29.aspx) on Windows actually is and what Chrome uses it for. Strictly speaking, a Job object isn’t a security feature at all; instead, it is a way of grouping related processes together and restricting the type and amount of common resources the processes are allowed to use. If you’re from a Unix background it’s similar to [ulimit](http://man7.org/linux/man-pages/man3/ulimit.3.html), but in many ways more powerful. In certain circumstances you can use it to restrict what a process can do; for example, Chrome renderers have the following Job object set:


This Job object restricts access to various UI features, such as the clipboard, but it also limits the number of active processes to 1. This means that even if it wanted to, the renderer would be blocked from creating any new child processes, and this restriction is enforced in the kernel. This is only much of a barrier when running with a restrictive token. Otherwise, when running as a normal user you can use system services such as WMI or the Task Scheduler to escape.

There are some vulnerabilities which benefit from being able to create new processes (for example [this](https://code.google.com/p/google-security-research/issues/detail?id=198)) so while breaking out of the Job object wouldn’t be an immediate sandbox escape it’d be useful as part of a chain of exploits. So now let’s go into the vulnerability which allows you to break out of the Job object.

## Console Driver Vulnerability

In early versions of Windows (that is, XP and earlier) the console window was actually handled by the Client Server Runtime Subsystem, better known as CSRSS. This subsystem implements the user-mode components of the Win32 windowing system. But this had disadvantages, not least of which you couldn’t apply themes to the window correctly, which is why the console window always looked out of place on XP. So in later versions of Windows a new process, conhost.exe, was introduced, which would be spawned on the user’s desktop to handle the console window. However, CSRSS was still involved in creating the new instance of the conhost process.

That all changed in Windows 8.1. Instead of CSRSS being responsible, a new kernel driver, condrv.sys was introduced. The driver exposes the device object \Device\ConDrv, which is accessible from any user context, even one as seriously locked down as the Chrome renderer. In fact there’s no known way of removing access to the driver. Commands are sent to the driver using device IO control codes. The command of interest is CdpLaunchServerProcess which is responsible for creating the conhost executable. Calling this directly is a bit involved, especially on 64-bit versions of Windows, so instead we can just call the Windows API [AllocConsole](https://msdn.microsoft.com/en-us/library/windows/desktop/ms681944%28v=vs.85%29.aspx) and it will do it for us.

Let’s look at the code that CdpLaunchServerProcess calls to create a new instance of the conhost.exe process.

NTSTATUS CdpCreateProcess(PHANDLE handle, 

HANDLE token\_handle, 

PRTL\_USER\_PROCESS\_PARAMETERS pp) {  

HANDLE thread\_handle;

NTSTATUS result;    

PROCESS\_ATTRIBUTE\_LIST attrib\_list;


SetProcessExecutable(&attrib\_list, L"\\SystemRoot\\System32\\Conhost.exe");

SetProcessToken(&attrib\_list, token\_handle);


result = ZwCreateUserProcess(

handle,

&thread\_handle,

...,

PROCESS\_BREAKAWAY\_JOB,  // Process Flags

CREATE\_SUSPENDED,       // Thread Flags

...,                         

&attrib\_list);


if ( result \< 0 ) 

\*handle = NULL;

else

ObCloseHandle(thread\_handle, 0);    


return result;

}

There are two very important things to note in this snippet of code which is directly related to the vulnerability. First, it’s calling a [Zw](https://www.osronline.com/article.cfm?id=257) form of the system call NtCreateUserProcess. This prefix indicates that the system call will be dispatched as if it was a system call coming from kernel mode as opposed to user mode. This is important as it means that any security checks are bypassed within the process creation. If the driver called the normal Nt form, it wouldn’t be possible to escape from something like the Chrome renderer as without this the conhost.exe file cannot be opened (the open would result in access denied) making this function fail pretty quickly.

The second important thing is the passing of the PROCESS\_BREAKAWAY\_JOB flag for the process flags. While the function isn’t documented, by reverse engineering the kernel code you’ll find this flag indicates that the new process should not be in the same job as the parent. This means that a restrictive job object can be escaped. During the processing of this flag in the kernel a check is made for SeTcbPrivilege; however, as the check is running as if coming from kernel mode (again due to the Zw function call) this check is bypassed regardless of the caller.

The end result is this:

- File security checks are bypassed leading to the conhost process being created.
- The restrictive job is escaped due to the passing of the PROCESS\_BREAKAWAY\_JOB flag.

For some users of restrictive job objects, such as Chrome GPU processes or Adobe Reader, all you need to exploit this issue is to call AllocConsole. But as we’ll see it isn’t quite so simple in Chrome Renderers.

## Exploiting the Issue in a Chrome Renderer

We want to try and exploit this from Chrome renderers, which are the most locked down sandboxed processes used in Chrome. The first challenge is to get code running inside the context of the renderer to test the exploit.

### Custom Test Code in a Renderer

The obvious thought is to use a [DLL injector](https://github.com/tyranid/IE11SandboxEscapes/blob/master/InjectDll/InjectDll.cpp), unfortunately this is easier said than done. The primary token for a renderer process is so restrictive it’s almost impossible to get it to open a file on disk so while you can inject a new thread to load the DLL the file open will fail.

Now you can just recompile Chromium with a few tweaks to the sandbox policy to allow access to an arbitrary location on the disk, but from M37 onwards there’s a way we can cheat and just use a release build. M37 added support for DirectWrite font rendering, in order to facilitate this a sandbox policy rule was added to allow read access to the Windows font folder. Therefore if we drop our DLL into %windir%\Fonts we can get it to load. A bit hacky sure, but it works. Of course to do this you already need to have code executing as an administrator on the system so it’s not a threat to Chrome’s security. We’ll also need to tweak a few build settings for the DLL, assuming you’re using Visual Studio, specifically:

- Removing the manifest as that doesn’t play nice with the restrictive sandbox
- Statically linking the DLL as you’ll not easily be able to open other DLLs once initialized

### Testing the Exploit

With a DLL file which can be opened by the Chrome renderer we can inject a thread, call LoadLibrary and get code executing within the process. As a first test let’s try and call AllocConsole and see what happens. If we take a look using [Process Monitor](https://technet.microsoft.com/en-us/library/bb896645.aspx) we see the conhost process being created but it never executes, in fact it exits almost immediately with a negative exit status.


If we convert the exit status to an unsigned integer we get 0xC0000022 which corresponds to STATUS\_ACCESS\_DENIED. Clearly something isn’t happy and killing the process. To understand what’s going wrong let’s look at some more code after the process creation.

NTSTATUS CdpLaunchServerProcess(

FILE\_OBJECT\* ConsoleFile, 

PRTL\_USER\_PROCESS\_PARAMETERS pp) {

HANDLE hToken;

HANDLE hProcess;

NTSTATUS status;

PACCESS\_TOKEN tokenobj = PsReferencePrimaryToken();

ObOpenObjectByPointer(tokenobj, ..., &hToken);


status = CdpCreateProcess(&hProcess, &hToken, pp);

if (status >= STATUS\_SUCCESS) {

HANDLE hConsoleFile;

status = ObOpenObjectByPointer(ConsoleFile, 

0, 0, GENERIC\_ALL, IoFileObjectType,

UserMode, &hConsoleFile);   

if (status >= STATUS\_SUCCESS) {

// Modify process command line...

ZwResumeProcess(hProcess);

}

}


if (status \< STATUS\_SUCCESS) {

ZwTerminateProcess(hProcess, status);

}


return status;

}

What this code does is create the process, then it creates a new handle to the current console device object so it can pass it on the command line to the conhost process. Looking at the control flow about the only way the process could be terminated in the way we observed (with ZwTerminateProcess) is if ObOpenObjectByPointer returns STATUS\_ACCESS\_DENIED when trying to create a new handle. But how can that be, we opened the device file originally, shouldn’t it also be able to be reopened with the same access rights? Well no, because the FILE\_OBJECT has an associated Security Descriptor and the DACL doesn’t give our heavily restrictive token GENERIC\_ALL access. As we can see in the following screenshot we’re missing an entry for the renderer’s token restricted SID (S-1-0-0) which would allow the restricted token check to succeed.


Don’t be fooled by the RESTRICTED group entry. The RESTRICTED group is just a convention when using restricted tokens, unless the token is created with that group as a restricted SID it does nothing. So does that mean we can never exploit this bug in Chrome? Of course not, we just need to understand how the FILE\_OBJECT’s DACL came to be set.

Unlike files and registry keys which typically inherit their DACL from the parent container, kernel objects instead get their default DACL from a special field in the current access token. We can modify the current token’s default DACL by passing an appropriate [structure](<https://msdn.microsoft.com/en-us/library/windows/desktop/aa379623(v=vs.85).aspx>) to [SetTokenInformation](<https://msdn.microsoft.com/en-us/library/windows/desktop/aa379591(v=vs.85).aspx>) with TokenDefaultDacl as the information class. We can do this without needing any special privileges. But what DACL to set? If we look at the access token’s enabled groups we only have the current user SID and the logon SID. However as the token is also a restricted token we need to give access to a restricted SID (S-1-0-0, the NULL SID) otherwise the access check will still fail. So let’s change the default DACL to specify full access to the logon SID and the NULL SID.

void SetCurrentDacl()

{

HANDLE hToken;

if (OpenProcessToken(GetCurrentProcess(), TOKEN\_ALL\_ACCESS, &hToken))

{       

WCHAR sddl\[256\];

PSECURITY\_DESCRIPTOR psd = nullptr;


StringCchPrintf(sddl, \_countof(sddl),

L"D:(A;;GA;;;%ls)(A;;GA;;;S-1-0-0)", GetLogonSid());


if (ConvertStringSecurityDescriptorToSecurityDescriptor(sddl, 

SDDL\_REVISION\_1, &psd, nullptr))

{

BOOL present;

BOOL defaulted;

PACL dacl;

GetSecurityDescriptorDacl(psd, &present, &dacl, &defaulted);


TOKEN\_DEFAULT\_DACL default\_dacl;

default\_dacl.DefaultDacl = dacl;


SetTokenInformation(hToken, TokenDefaultDacl, 

&default\_dacl, sizeof(default\_dacl));               


LocalFree(psd);

}       

}

}

Now after setting the current DACL we can try again, but AllocConsole still fails. However looking at the error code we’ve at least got past the initial problem. Process Monitor shows the process exit code as STATUS\_DLL\_NOT\_FOUND, which tells us what’s happening.

When the process’s first thread runs it doesn’t actually start directly at the process entry point. Instead it runs a special piece of code inside NTDLL to initialize the current process, [LdrInitializeThunk](http://www.nynaeve.net/?p=205). As the Ldr prefix suggests (it’s short for Loader) this function is responsible for scanning the process’s imported DLLs, loading them into memory and calling their initialization functions. In this case the process token is so restrictive we cannot even open the typical DLL files. Fortunately there’s a time window between the process being created and the initial thread being resumed with ZwResumeProcess. If we can capture the process within that window we can just initialize the process as an empty shell. But how can we do this?

### Capturing New Process

The obvious way of exploiting this would be to open the new process during the timing window then call NtSuspendProcess on the handle. This would work because suspend/resume operations are reference counted. The process starts with a suspension count of 1, as the kernel driver created the initial thread with the CREATE\_SUSPENDED flag, so if we can call NtSuspendProcess quickly we can increment that to 2. The driver then decrements the count by calling ZwResumeProcess, however this only drops the count to 1 and the kernel will leave the thread suspended. We can then manipulate the new process to remove the initialization code and run outside of the job object.

But there’s a big problem with this plan. Normally when you create a new process a handle to the process is returned, but this isn’t the case here as the kernel driver closes the kernel-only handle before returning to the caller. Therefore we need to open the process by its PID, but guessing that could be tricky. Modern versions of Windows do not just keep incrementing the PID, instead reusing old PIDs after a certain period of time. We can just keep guessing but every wrong guess is time wasted. You’ll find that a brute force approach is pretty much impossible to use.

So are we stuck? Of course not, we just need to use further undocumented features. The kernel exposes a system call, NtGetNextProcess which as the name suggests gets the next process. But next to what? If you’ve done any Windows internals you’ll know that process objects are chained together in a big linked list in the kernel. This system call takes the handle to a process object and finds the next process in the chain that can be opened by the current user.


Turns out by default there are no other processes that the current process can open in the list, even itself due to that pesky default DACL. This means normally NtGetNextProcess always fails. When the new conhost process is created however it inherits the new modified default DACL that we can access, this means we can just sit in a very small loop calling NtGetNextProcess until it succeeds. The returned handle is almost certainly conhost so we can quickly suspend the process, and now can take as much time as we like. We need to do this in a thread as AllocConsole will block, but that’s not a problem. So for example:

HANDLE GetConhostProcess()

{       

HANDLE hCurr = nullptr;


while (!hCurr)

{

hCurr = nullptr;

if (NtGetNextProcess(hCurr, MAXIMUM\_ALLOWED,

0, 0, &hCurr) == 0)

{

NtSuspendProcess(hCurr);

return hCurr;

}

}


return 0;

}

So with a handle to the conhost process we can modify the LdrInitializeThunk method to prevent it failing and inject some shellcode. You’ll only have the services of NTDLL as no other DLL will get mapped in. Still the goal has been met, you can now escape a restrictive Job object, even in such a locked down process. What you now do with that power is up to you.

## Conclusions

So what use is this? Well not a lot really, at least from a direct escape of the sandbox. It just weakens the defences a little and opens up the attack surface for exploiting other issues. I can understand why Microsoft wouldn’t want to fix it, it acts in this manner for backwards compatibility reasons and changing it would be difficult. That said I believe it could be made to work within the security context of the current process calling the API as few applications ever make use of such restrictive tokens as application sandboxes.

Also Chrome works to make further efforts to mitigate security issues. For example while the Job breakout removes the imposed Job UI restrictions Chrome now uses win32k lockdown on all affected platforms, which as far as I can tell can’t be disabled even in child processes. Security mitigations continue to evolve, taking advantage of new features of a platform, however security regressions are inevitable. A well developed sandbox shouldn’t rely on any one platform feature to be secure, as that functionality could break at any time.
