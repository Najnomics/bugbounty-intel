# Windows Drivers are True’ly Tricky - Project Zero

Source: https://projectzero.google/2015/10/windows-drivers-are-truely-tricky.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by James Forshaw, Driving for Bugs


Auditing a product for security vulnerabilities can be a difficult challenge, and there’s no guarantee you’ll catch all vulnerabilities even when you do. This post describes an [issue](https://code.google.com/p/google-security-research/issues/detail?id=538) I identified in the Windows Driver code for Truecrypt, which has already gone through a security [audit](https://opencryptoaudit.org/reports/iSec_Final_Open_Crypto_Audit_Project_TrueCrypt_Security_Assessment.pdf). The issue allows an application running as a normal user or within a low-integrity sandbox to remap the main system drive and elevate privileges to SYSTEM or even the kernel. I hope to show why the bug in question might have been missed. I don’t provide any guarantees that there are no more bugs left to find.

It’s worth noting that this vulnerability didn’t have a direct impact on the security of the encrypted drive volumes at rest. Before I delve into the details let’s take a look at an aspect of the Windows NT operating system that’ll be very important later.

## The History of DosDevices

Under MS-DOS and versions of Windows that ran on top of it drive letters were generally assigned in a specific order based on the device and disk partition type. In Windows NT this isn’t the case. As I mentioned in my previous [post](/2015/08/windows-10hh-symbolic-link-mitigations.html) on symbolic links, the drive letters you see in Windows Explorer are really symbolic links under the hood which point the drive letter (say C:) to the mounted device object (say \Device\HarddiskVolume4). The OS is free to assign these drive letters in an arbitrary order.


The OS needs a known location to store these symbolic links so in the original Windows NT 3.1 an object directory was added to the root of the object manager namespace called DosDevices. This directory stored all the drive and device symbolic links for the system. There was only a single directory for all users, but for the original versions of Windows NT this didn’t matter as you could only ever have one interactive user logged on at one time. When calling a Win32 API which takes a DOS path it’s converted to an absolute drive path and the DosDevices prefix is appended before passing to the native NT system call.

Over the subsequent versions of the OS the implementation of DosDevices changed. First in NT 4 the name was changed from DosDevices to ??. This was presumably for performance reasons as the kernel could quickly check for the prefix using two 32 bit integer comparisons for the 4 unicode characters \??\. To ensure old code still worked DosDevices now became a symbolic link pointing to the new shorter path.

The biggest change, however, happened in Windows XP (well technically with the introduction of Terminal Services but XP was the first consumer OS with this support). XP shipped with Fast User-Switching and remote desktop support, which allowed multiple interactive users to be logged in the same machine at the same time. This required that DosDevices supported per-user objects, because it would be annoying and potentially dangerous to allow the sharing of user specific drive mapping. To achieve this a per-user object directory is created under \Sessions\0\DosDevices with a name which corresponds to the user’s logon ID.


So how does this per-user directory get referenced? By creating a fake DosDevices object directory. First the original ?? directory was renamed to GLOBAL?? and ?? now became a virtual directory. When reading from the directory, say resolving a drive letter, the per-user directory is checked. If the per-user directory doesn’t contain a corresponding entry the kernel falls back to checking the global directory, if no entry is found there then the kernel generates an appropriate error such as STATUS\_OBJECT\_NAME\_NOT\_FOUND. An interesting case is what happens when a process creates a new object in the virtual directory. Only the per-user directory is taken into account so any new object creation to \?? will result in that object being added to the per-user directory. The access control on GLOBAL?? is set so that only administrators can modify objects within it, however a normal user is free to modify their own per-user directory.

To add a further complication Windows 2000 introduced the concept of a per-process DosDevices directory. This can be specified by calling the system call NtSetInformationProcess with the ProcessDeviceMap information class passing the handle to a new object directory. On Windows 2000 this just replaces the ?? directory lookup entirely, however on XP and above the fallback to GLOBAL?? still occurs. This is only used when the lookup is occurring within the same process, no other process on the system see the new DosDevices map.

Here’s a condensed history of the major changes in how DosDevices works across NT operating systems.


## Details of the Vulnerability

So with that bit of history out of the way let’s look at the vulnerability itself. The opened issue can be found [here](https://code.google.com/p/google-security-research/issues/detail?id=538). The Truecrypt driver exposes a number of different IOCTLs to a user-mode application to perform its various tasks such as mount and unmounting encrypted disk images and enumerating information. The vulnerability is due to bugs in  the mounting and unmounting of Truecrypt volumes, corresponding to the IOCTLs TC\_IOCTL\_MOUNT\_VOLUME and TC\_IOCTL\_DISMOUNT\_VOLUME. All the vulnerable code is contained in the Driver\Ntdriver.c file in the Truecrypt [source code](https://www.grc.com/misc/truecrypt/TrueCrypt%207.1a%20Source.zip).

When a drive is mounted in Windows there are a few ways that a drive letter can be assigned. The most common way is by registering the drive with the Mount Manager driver. This requires the caller to be an administrator, and all registration information will go into the Registry. The alternative is the symbolic link for the drive can be created manually using the [IoCreateSymbolicLink](<https://msdn.microsoft.com/en-us/library/windows/hardware/ff549043(v=vs.85).aspx>) API. Ultimately though it must go into one of the DosDevices locations otherwise normal user-mode application would not be able to pick up the drive letter.

The Truecrypt driver supports both ways of mounting the drive, it can use the Mount Manager to mount the drive (if the bMountManager flag is set in the structure passed to the driver), however, just in case it also manually creates the link as shown:

// We create symbolic link even if mount manager is notified of

// arriving volume as it apparently sometimes fails to create the link

CreateDriveLink (mount->nDosDriveNo);

From user-mode we can only specify a number from 0 to 25 as nDosDriveNo which represents the drive letters A through Z. Now let’s look at what CreateDriveLink is doing:

#define DOS\_MOUNT\_PREFIX L"\\DosDevices\\"

void TCGetDosNameFromNumber (LPWSTR dosname, int nDriveNo) {

WCHAR tmp\[3\] =

{0, ':', 0};

int j = nDriveNo + (WCHAR) 'A';


tmp\[0\] = (short) j;

wcscpy (dosname, (LPWSTR) DOS\_MOUNT\_PREFIX);

wcscat (dosname, tmp);

}

NTSTATUS CreateDriveLink (int nDosDriveNo) {

WCHAR dev\[128\], link\[128\];

UNICODE\_STRING deviceName, symLink;

NTSTATUS ntStatus;


TCGetNTNameFromNumber (dev, nDosDriveNo);

TCGetDosNameFromNumber (link, nDosDriveNo);


RtlInitUnicodeString (&deviceName, dev);

RtlInitUnicodeString (&symLink, link);


// Delete \DosDevices\X:

ntStatus = IoCreateSymbolicLink (&symLink, &deviceName);

return ntStatus;

}

Ignore the horrible looking string manipulation in TCGetDosNameFromNumber as it’s not relevant to the vulnerability. What the code is doing is building a path for the drive letter symbolic link to \DosDevices\X: where X is the drive letter determined simply by adding the drive number to the character ‘A’.

In theory we could redefine the C: drive, perhaps that could be used to elevate privileges? Well sadly not, if you go back to my description of DosDevices on XP and later versions of Windows you’ll notice that when writing to the DosDevices directory (which is really a symbolic link to the virtual ?? directory) it will create the symbolic link for the drive in the per-user directory  which doesn’t really gain you much. You’re only overriding the current user’s view of the drive. This is useful to escape a sandbox (assuming you can access the Truecrypt device) but as a normal user you can already write to the per-user DosDevices directory. That seems like a dead end, perhaps it’s worth taking a look at the unmount process instead.

When unmounting a Truecrypt volume you only need to pass the drive number. Unmounting an existing device will delete the original symbolic link using RemoveDriveLink.

NTSTATUS RemoveDriveLink (int nDosDriveNo) {

WCHAR link\[256\];

UNICODE\_STRING symLink;

NTSTATUS ntStatus;


TCGetDosNameFromNumber (link, nDosDriveNo);

RtlInitUnicodeString (&symLink, link);


// Delete \DosDevices\X:

ntStatus = IoDeleteSymbolicLink (&symLink);

return ntStatus;

}

// We always remove symbolic link as mount manager might fail to do so

RemoveDriveLink (extension->nDosDriveNo);

NTSTATUS IoDeleteSymbolicLink(PUNICODE\_STRING SymbolicLinkName) {

NTSTATUS status;

OBJECT\_ATTRIBUTES ObjectAttributes; 

HANDLE Handle;


InitializeObjectAttributes(&ObjectAttributes, SymbolicLinkName, ...);


status = ZwOpenSymbolicLinkObject(&Handle, DELETE, &ObjectAttributes);

if (NT\_SUCCESS(status)) {

status = ZwMakeTemporaryObject(Handle);

if (NT\_SUCCESS(status))

ZwClose(Handle);

}

return status;

}

We can see IoDeleteSymbolicLink is opening the symbolic link object for DELETE access. It then calls ZwMakeTemporaryObject to drop the reference count of the object by 1 (which was added when creating the symbolic link in the first place). As no other handles are open to the object it gets deleted from the object namespace which removes the name. Crucially though this is a “Read” operation, even though we’re asking for DELETE permissions it's only opening an existing object, this means that the virtual ?? directory will first try to open in the per-user directory, then fallback to the global directory. The result is if the drive letter can’t be found in the per-user directory it will actually open the global symbolic link, then delete it.

So seems like we’re getting somewhere, we’ve got a primitive to delete an existing drive letter in the global directory. However we need to have already mounted a Truecrypt volume to the corresponding drive letter in order to delete it. If we try and do this the mount process fails, what’s stopping us defining a new C: drive? During the mount process the function IsDriveLetterAvailable is called, if it returns TRUE then the letter is available for use. If the function returns FALSE then the command refuses to mount the volume as the specified drive letter.

BOOL IsDriveLetterAvailable (int nDosDriveNo) {

OBJECT\_ATTRIBUTES objectAttributes;

UNICODE\_STRING objectName;

WCHAR link\[128\];

HANDLE handle;


TCGetDosNameFromNumber (link, nDosDriveNo);

RtlInitUnicodeString (&objectName, link);

InitializeObjectAttributes (&objectAttributes, &objectName,

OBJ\_KERNEL\_HANDLE | OBJ\_CASE\_INSENSITIVE, NULL, NULL);


// Test opening \DosDevices\X:

if (NT\_SUCCESS (ZwOpenSymbolicLinkObject (&handle, GENERIC\_READ,

&objectAttributes))) {

ZwClose (handle);

return FALSE;

}


return TRUE;

}

All IsDriveLetterAvailable does is call ZwOpenSymbolicLinkObject to try and open any existing symbolic link with the drive letter name. As we saw with the IoDeleteSymbolicLink case this is a read operation so the virtual directory fallback will occur. If the global drive letter entry exists we can’t mount the device to use the unmount to delete the drive letter. Seems like we’re at an impasse unless we can bypass this check.

Notice that the result of ZwOpenSymbolicLinkObject is just checked to return a successful status using the NT\_SUCCESS macro. This causes the logic of the function to be incorrect. The intent of the function is to say “Does no symbolic link object with this name exist?” However because of the sinking of error cases what it actually results in is asking “Does opening a symbolic link object with this name fail?” Those are subtly different questions and obviously we can get it to return the answer we like.

When the symbolic link doesn’t exist the API returns STATUS\_OBJECT\_NAME\_NOT\_FOUND; that was the intent of the check. However, to bypass the check we can just find any other way of getting the API to fail, IsDriveLetterAvailable will return TRUE, and we can mount an arbitrary drive letter even if it already exists. A common trick in these cases is to change the access control on the object so that the function would return STATUS\_ACCESS\_DENIED, however as the code is using the Zw variant of the system call all access checks are bypassed. Instead all we need to do is create a different object type with the same name in the virtual DosDevices directory. As ZwOpenSymbolicLinkObject  will verify the object type this will result in the API returning the error status STATUS\_OBJECT\_TYPE\_MISMATCH instead. We do have a race condition here between when the drive letter check occurs and when the symbolic link is created which we need to win by deleting the invalid object, however that’s a pretty easy this to do through brute force or abusing file OPLOCKs.

So we can combine these small bugs into remounting the C: drive to an arbitrary Truecrypt volume, well almost. We have just one problem left, how to actually get the mount process to write to the GLOBAL?? directory. Turns out this is probably the easiest part of all. IoCreateSymbolicLink doesn’t perform any security checks when creating the link so we can get it to write to an object directory we wouldn’t normally be able to control. However when setting the per-process using NtSetInformationProcess we only need a handle with DIRECTORY\_TRAVERSE permissions. As this is a read permission we can open GLOBAL?? from a low-privileged user, set it as the per-process DosDevices directory then get the Truecrypt driver to write to it.

So the final exploit chain is as follows:

1. Create a new kernel object in the per-user DosDevices directory with the name of the drive letter to override.
2. Mount a Truecrypt volume as that drive number then win the race between IsDriveLetterAvailable and CreateDriveLink.
3. Manually delete the symbolic link in the per-user directory (it’s our directory so we can do this) then unmount the drive. This will cause IoDeleteSymbolicLink to delete the global drive letter.
4. Assign GLOBAL?? as the per-process DosDevices directory, remount the volume as the letter to override.
5. Exploit the remapped drive letter to elevate privileges such as starting a scheduled task or service.

I’ve summarised the operations in the diagram below.


Performing the sequence of operations results in the global C: drive mapped to our arbitrary Truecrypt volume, and from that you can trivially elevate privileges as any system service, or even the kernel will think

## Conclusions

So why might this issue have been missed? Well obviously the root cause was the lack of knowledge of the attack vector but you could be forgiven for this because of typical idiomatic Windows driver code which isn’t usually exploitable. Take a look at pretty much any DriverEntry method for a Windows driver. When the driver starts it needs to create a new device object, typically with [IoCreateDevice](<https://msdn.microsoft.com/en-us/library/windows/hardware/ff548397(v=vs.85).aspx>). Then the code will also create a symbolic link in the DosDevices directory using IoCreateSymbolicLink to make it easier for user-mode applications to access the device.

The Truecrypt implementation for this is in the function TCCreateRootDeviceObject, which creates a symbolic link called \DosDevices\TrueCrypt. Why isn’t this vulnerable to a similar issue? Whenever a driver starts, even if it was loaded by a user, the initial thread running DriverEntry runs within the System process, which is a special process on the NT operating system where system kernel threads execute. By running in the system process context it’s not possible, at least without Administrator privileges, to influence the DosDevices location either via the per-user directory or the per-process directory.

This might lead a developer, and even an auditor to think that IoCreateSymbolicLink does something special to guard against this attack. As we’ve seen it doesn’t. The issue wouldn’t have been exploitable if the symbolic link creation occurred in a system thread but that’s up to the developer. It also wouldn’t have been vulnerable prior to Windows 2000, but that’s hardly a consolation. When the behaviour of something so fundamental to the NT operating system like how DOS style devices letters is handled isn’t well documented or things like the per-process device map trips up Microsoft it’s hard to blame the developers and auditors when bugs sneak through.
