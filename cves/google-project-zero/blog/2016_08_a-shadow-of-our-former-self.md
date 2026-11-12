# A Shadow of our Former Self - Project Zero

Source: https://projectzero.google/2016/08/a-shadow-of-our-former-self.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by James Forshaw of Google Project Zero

“Necessity is the Mother of Invention” as it’s said, and this is no more true than when looking for and exploiting security vulnerabilities. When new exploit mitigations are introduced, either a way of bypassing the mitigation is needed or an alternative approach must be found. I’ve described in the [past](https://vimeo.com/album/3416096/video/133002251) some of the fun tricks you could do with symbolic links on Windows, and also how Microsoft made them [difficult](/2015/08/windows-10hh-symbolic-link-mitigations.html) to use from sandboxes. I wanted to a find a way to bypass these mitigations and in the process found a new technique introduced in Windows 8 to get back some symbolic link capability in sandboxes.


This post describes the exploitation technique which allowed me to recover some of the mitigated functionality to exploit file planting or TOCTOU attacks from a sandbox, how it could be used to exploit an example vulnerably [CVE-2016-3219](https://bugs.chromium.org/p/project-zero/issues/detail?id=779), and a quick overview of the fix Microsoft have introduced in [MS16-092](https://technet.microsoft.com/library/security/MS16-092) to block the trick in a sandbox.

## Shadow Object Directories

While I was delving deep into the object manager I noticed a new system call for creating object directories, NtCreateDirectoryObjectEx. Compared to the old NtCreateDirectoryObject system call the Ex variant took an additional two parameters, a HANDLE to a directory object and some additional flags. Curious about what the additional HANDLE was for I spent a short bit of time reverse engineering it resulting in the following:


NTSTATUS NtCreateDirectoryObjectEx(

\_Out\_     PHANDLE Handle,

\_In\_      ACCESS\_MASK DesiredAccess, 

\_In\_      POBJECT\_ATTRIBUTES ObjectAttributes,

\_In\_opt\_  HANDLE ShadowDirectoryHandle,

\_In\_      ULONG Flags) {


OBJECT\_DIRECTORY\* ShadowDirectory = nullptr;

if (ShadowDirectoryHandle) {

ObReferenceObjectByHandle(ShadowDirectoryHandle, 

DIRECTORY\_QUERY | DIRECTORY\_TRAVERSE,

ObpDirectoryObjectType, &ShadowDirectory);

}


OBJECT\_DIRECTORY\* NewDirectory = nullptr;

ObCreateObject(ObpDirectoryObjectType, ObjectAttributes, &NewDirectory);    

if (ShadowDirectory) {

NewDirectory->Flags = DIRECTORY\_FLAG\_SHADOW\_PRESENT;

NewDirectory->ShadowDirectory = ShadowDirectory;

}


// ...

}


This got me intrigued, what was the purpose of this Shadow Directory Handle? Was it even used? A quick way to find out is to just place a breakpoint on the function in a kernel debugger and see who’s calling it.


kd> bp nt!NtCreateDirectoryObjectEx

kd> g

... Wait some time

Breakpoint 1 hit

nt!NtCreateDirectoryObjectEx:

823a86b8 8bff            mov     edi,edi


kd> kc

00 nt!NtCreateDirectoryObjectEx

01 nt!KiSystemServicePostCall

02 ntdll!KiFastSystemCallRet

03 ntdll!NtCreateDirectoryObjectEx

04 KERNELBASE!BasepCreateLowBoxObjectDirectories

05 KERNELBASE!BasepCreateLowBox

06 KERNELBASE!CreateProcessInternalW

07 KERNELBASE!CreateProcessAsUserW

...


Interesting, seems like it’s something to do with Low Box/AppContainer process creation. Let’s look at the ShadowDirectoryHandle to see where it’s pointing to:


kd> !handle poi(@esp+10) 1

0264: Object: 8f33ef50  GrantedAccess: 00020003


kd> !object 8f33ef50 21

Object: 8f33ef50  Type: (84d4ccb8) Directory

ObjectHeader: 8f33ef38 (new version)

HandleCount: 12  PointerCount: 353

Directory Object: 8f33e728  Name: \Sessions\1\BaseNamedObjects


So the shadow directory is pointing to our session’s BaseNamedObjects directory. Let’s see where it’s creating the new directory.


kd> !obja poi(@esp+c)

Obja +061be0b8 at 061be0b8:

Name is S-1-15-2-3624051433-2125758914-1423191267-1740899205-1073925389-...

OBJ\_INHERIT

OBJ\_OPENIF


kd> !handle poi(poi(@esp+c)+4) 2

0a8c: Object: 8f2362d8  GrantedAccess: 0000000f Entry: a74cf518


kd> !object 8f2362d8 21

Object: 8f2362d8  Type: (84d4ccb8) Directory

ObjectHeader: 8f2362c0 (new version)

HandleCount: 2  PointerCount: 39

Directory Object: 8f33e728  Name: \Sessions\1\AppContainerNamedObjects


So that all correlates with the stack trace. We’re creating the Low Box object directories for an AppContainer process, and the shadow is pointing at the main session BaseNamedObjects. It would seem likely that this directory is used as a fallback if a resource can’t be found in the Low Box specific directory, to ensure global resources could be accessed between normal applications and the AppContainer process. This isn’t particularly surprising functionality, I’ve [mentioned](/2015/10/windows-drivers-are-truely-tricky.html) a number of times in the past that this is the same behaviour used for the per-user DOS device directory. To erase all doubt we can look at where this gets used, the handily named ObpGetShadowDirectory.


OBJECT\_DIRECTORY\* ObpGetShadowDirectory(OBJECT\_DIRECTORY \*Directory)

{

if (Directory->Flags & DIRECTORY\_FLAG\_SHADOW\_PRESENT)

return Directory->ShadowDirectory;


DEVICE\_MAP\* device\_map = Directory->DeviceMap;

if (device\_map)

return device\_map->GlobalDosDevicesDirectory;


return nullptr;

}


Clearly this is a generalization of the original DOS devices fallback, in fact if you look at Windows 7 ObpGetShadowDirectory exists but it only returns the Global DOS devices directory. So the behaviour is going to be the same. When creating a new resource inside the directory it will write to the target directory (if it’s allowed by the DACL of course) even if there exists the same object in the shadow. When opening a resource it will first lookup the name in the directory, if it’s not found it will look into the shadow instead.


Ultimately we can abuse this to create object directory symbolic links. Even more importantly if we look back at the implementation of NtCreateDirectoryObjectEx we’ll notice it only requests read permissions on the shadow directory handle, this means we can point it almost anywhere in the object manager hierarchy.


There are some limitations to this technique however. First it requires that the resource be accessed by the privileged application using an object manager path. This isn’t usually a problem if you can specify a full path and the \\?\ prefix to escape into the object manager namespace. Secondly like with NTFS Mount Points you can use this to control the name of the final resource, you can only affect its lookup. So it’s not as good as the old symbolic links but you have to make do. Let’s see it in action to exploit [CVE-2016-3219](https://bugs.chromium.org/p/project-zero/issues/detail?id=779).

## Double Trouble

The vulnerability is [Issue 779](https://bugs.chromium.org/p/project-zero/issues/detail?id=779) in the Project Zero issue tracker, and is an issue with the verification of a font path when the Windows 10 [Custom Font Disable Mitigation Policy](<https://msdn.microsoft.com/en-gb/library/windows/desktop/mt706244(v=vs.85).aspx>) is enabled. This mitigation policy is supposed to block loading custom fonts into the kernel, which [might](/2015/07/one-font-vulnerability-to-rule-them-all.html) [have](/2015/08/one-font-vulnerability-to-rule-them-all.html) [exploitable](/2015/08/one-font-vulnerability-to-rule-them-all_13.html) [vulnerabilities](/2015/08/one-font-vulnerability-to-rule-them-all_21.html). The offending code in the Win32k driver looks something like the following:


int WIN32K::bLoadFont(...) {

int load\_option = GetCurrentProcessFontLoadingOption();

bool system\_font = true;

if (load\_option) {

HANDLE hFile = hGetHandleFromFilePath(FontPath);

BOOL system\_font = bIsFileInSystemFontsDir(hFile);

ZwClose(hFile);

if (!system\_font) {

LogFontLoadAttempt(FontPath);

if (load\_option != CUSTOM\_FONT\_LOG\_ONLY)

return 0;

}

}

// Reopen path here

HANDLE hFont = hGetHandleFromFilePath(FontPath); 

// Map font as section

}


What this code does is open the path to the font file (which is provided verbatim by the user process). It then checks that the file is within the \Windows\Fonts path on the system drive by opening the path and querying the file object’s name. If this check passes it then closes the file handle. The code then reopens the original font path to pass it to the font processing code. There’s an obvious race between the font file path being checked and it being used as the actual file. As we can’t easily use other types of symbolic links we’ll exploit it using the directory shadows.


The key thing to understand about how to use the shadow directories to exploit TOCTOU vulnerabilities is the lookup order, namely that you can place an object in the top directory which aliases one in the shadow with no ill effect, however when you remove that object the lookup process will fall through to the shadow. So let’s say we want to construct a path such that when it’s first opened the kernel will open the file C:\Windows\Fonts\somefont.ttf but after the check it opens a totally unrelated font which is the one we control. Assuming we can write to a path C:\ABC (it doesn’t need to be the root, but it makes our paths smaller for this example) we can construct something like the following:


Notice we’ve got two shadow directories set up, both pointing to \Devices. The devices directory contains the device nodes for the hard drive volumes, for example in this case the C: drive is mapped to HarddiskVolume1. It’ll be important that we use paths with no special character such as a colon for reasons that we’ll see in a minute. Now we can request Win32k to load our font using our object manager path. The kernel will follow the hierarchy of object manager directories until it gets to ABC, at this point it tries to lookup HarddiskVolume1 but it doesn’t exist. It therefore falls back to the shadow. As the shadow does have HarddiskVolume1 it’s now finished and the kernel asks the file system to look up file \Windows\Fonts\somefont.ttf. This can be verified as being inside the Windows system fonts directory. Note that from the kernel’s perspective all the previous path information is lost when the file is opened. This ensures that when querying the name it only sees what we want it to see.


Now for the exploit. We can use an oplock on the system font file so we get signaled when Win32k is trying to open the file for its initial check. Again by this point the original path is lost and the file system driver is committed to opening the system font, so when we get signaled we can manipulate the object manager directory hierarchy to change which font is opened. In this case we can just delete the HarddiskVolume1 directory inside SWITCH. This results in the following:


Now when the kernel looks up the path it reaches SWITCH but there’s no longer the HarddiskVolume1 directory to follow. So it’ll drop to looking in the shadow directory where it does indeed find a device with that name. This results in the kernel requesting the path \ABC\HarddiskVolume1\Windows\Fonts\somefont.ttf from the file system driver. This is clearly a different path and as we specified we control the directory \ABC we can build a chain of file system directories to satisfy the remaining path. This is why we had to avoid special characters. The colon can be used in NTFS to separate a stream name, however a stream name can’t contain backslashes.


The end result is the kernel opens a system font file to check whether it’s allowed to load the font but then opens a user controlled font when it goes to actually use it, this bypasses the process mitigation policy and it’s job done.

## Behavioural Changes

In the July Updates Microsoft issued a fix, [MS16-092](https://technet.microsoft.com/library/security/MS16-092), which blocked using these tricks to get privilege escalation from a sandbox. Like the [fixes](/2015/08/windows-10hh-symbolic-link-mitigations.html) for the Object Manager symbolic links, shadow directories can still be created however a flag will be set if being created under a sandbox token which is checked when looking up the shadow directory. By doing this a privileged application (even if just normal user privilege) will not follow the shadow directory, in theory preventing this being abused.


OBJECT\_DIRECTORY\* ObpGetShadowDirectory(OBJECT\_DIRECTORY \*Directory,

BOOLEAN InSandbox)

{

if (Directory->Flags & DIRECTORY\_FLAG\_SHADOW\_PRESENT)

if (!(Directory->Flags & DIRECTORY\_FLAG\_SANDBOX) || InSandbox)

return Directory->ShadowDirectory;


// ...

}

There’s no denying that a substantial amount of code went into Windows 8 to add support for AppContainers. While Microsoft’s [SDL](https://www.microsoft.com/en-us/sdl/) has gone some way towards eliminating common security mistakes (though clearly not as well as we’d like) it’s sometimes hard to fully understand the security implications of a decision until after it’s shipped. It’s understandable that when the shadow directories were designed there was no obvious security implication. It only became a problem after the other avenues of creating symbolic links in sandboxes were eliminated. There’s no good reason to use them to elevate privileges if you already have normal object manager symbolic links.
