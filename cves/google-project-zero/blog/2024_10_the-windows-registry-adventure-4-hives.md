# The Windows Registry Adventure #4: Hives and the registry layout - Project Zero

Source: https://projectzero.google/2024/10/the-windows-registry-adventure-4-hives.html
Captured verbatim (article body extracted from HTML) on 2026-11-12.

---

Posted by Mateusz Jurczyk, Google Project Zero


To a normal user or even a Win32 application developer, the registry layout may seem simple: there are five root keys that we know from Regedit (abbreviated as HKCR, HKLM, HKCU, HKU and HKCC), and each of them contains a nested tree structure that serves a specific role in the system. But as one tries to dig deeper and understand how the registry really works internally, things may get confusing really fast. What are hives? How do they map or relate to the top-level keys? Why are some HKEY root keys pointing inside of other root keys (e.g. HKCU being located under HKU)? These are all valid questions, but they are difficult to answer without fully understanding the interactions between the user-mode Registry API and the kernel-mode registry interface, so let's start there.

## The high-level view

A simplified diagram of the execution flow taken when an application creates a registry key is shown below:


In this example, Application.exe is a desktop program calling the documented [RegCreateKeyEx](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regcreatekeyexw) function, which is exported by KernelBase.dll. The KernelBase.dll library implements RegCreateKeyEx by translating the high-level API parameters passed by the caller (paths, flags, etc.) to internal ones understood by the kernel. It then invokes the [NtCreateKey](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwcreatekey) system call through a thin wrapper provided by ntdll.dll, and the execution finally reaches the Windows kernel, where all of the actual work on the internal registry representation is performed.


The declaration of the RegCreateKeyEx function is as follows:


`LSTATUS RegCreateKeyExW(`

\[in\] HKEY hKey,

\[in\] LPCWSTR lpSubKey,

DWORD Reserved,

\[in, optional\] LPWSTR lpClass,

\[in\] DWORD dwOptions,

\[in\] REGSAM samDesired,

\[in, optional\] const LPSECURITY\_ATTRIBUTES lpSecurityAttributes,

\[out\] PHKEY phkResult,

\[out, optional\] LPDWORD lpdwDisposition

);


As the first two arguments imply, many registry operations (and especially key opening/creation) are performed on a pair of a base key handle and a relative key path. HKEY is a dedicated type for registry key handles, but it is functionally equivalent to the standard HANDLE type. It can either contain a regular handle to a key object (as managed by the NT Object Manager), or one of a few possible pseudo-handles described in the [Predefined Keys](https://learn.microsoft.com/en-us/windows/win32/sysinfo/predefined-keys) list. They are defined in winreg.h with the following numeric values:


#define HKEY\_CLASSES\_ROOT (( HKEY ) (ULONG\_PTR)((LONG)0x80000000) )

#define HKEY\_CURRENT\_USER (( HKEY ) (ULONG\_PTR)((LONG)0x80000001) )

#define HKEY\_LOCAL\_MACHINE (( HKEY ) (ULONG\_PTR)((LONG)0x80000002) )

#define HKEY\_USERS (( HKEY ) (ULONG\_PTR)((LONG)0x80000003) )

#define HKEY\_PERFORMANCE\_DATA (( HKEY ) (ULONG\_PTR)((LONG)0x80000004) )

#define HKEY\_PERFORMANCE\_TEXT (( HKEY ) (ULONG\_PTR)((LONG)0x80000050) )

#define HKEY\_PERFORMANCE\_NLSTEXT (( HKEY ) (ULONG\_PTR)((LONG)0x80000060) )

#define HKEY\_CURRENT\_CONFIG (( HKEY ) (ULONG\_PTR)((LONG)0x80000005) )

#define HKEY\_DYN\_DATA (( HKEY ) (ULONG\_PTR)((LONG)0x80000006) )

#define HKEY\_CURRENT\_USER\_LOCAL\_SETTINGS (( HKEY ) (ULONG\_PTR)((LONG)0x80000007) )

As we can see, they all have the highest bit set, which is normally reserved for kernel-mode handles. Thanks to this, the values can never collide with legitimate user-mode handles, and can be freely used as special pseudo-handles. It is the responsibility of the Registry API to translate these values into their corresponding low-level registry paths before calling into the kernel. In other words, predefined keys are a strictly user-mode concept, and the kernel itself has no awareness of them. If someone decided to write a program interacting with the registry directly through system calls rather than the API, they wouldn't have any use of the HKEY\_\* constants whatsoever.


This explains why the top-level keys don't necessarily represent mutually exclusive subtrees – none of them inherently represent any specific part of the registry, and their meaning is purely conventional. It is up to KernelBase.dll to decide how it handles each of these keys, and this is further highlighted by the existence of the [RegOverridePredefKey](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regoverridepredefkey) function, which allows an application to remap them in the context of the local process. In literature, root keys are sometimes described as being "links" to specific registry paths, and while conceptually correct, this may confuse readers who know about the existence of symbolic links, which is a separate, unrelated mechanism. In fact, if we count all the different ways in which access to a registry key can be transparently redirected to another path (either in the user or kernel part of the interface), we end up with at least four:

1. User-mode Registry API interpreting top-level keys and translating them into specific internal paths, as discussed above.
2. Kernel-mode Configuration Manager following symbolic links in the registry, i.e. keys created with the [REG\_OPTION\_CREATE\_LINK](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regcreatekeyexw#REG_OPTION_CREATE_LINK) flag and with a value named "SymbolicLinkValue" of type REG\_LINK.
3. Kernel-mode Configuration Manager applying [Registry Virtualization](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-virtualization) to a specific legacy application, and thus redirecting reads/writes to/from subkeys of HKEY\_LOCAL\_MACHINE\Software to HKEY\_USERS\\\<SID>\_Classes\VirtualStore\Machine\Software.
4. The user-mode Registry API and kernel-mode Configuration Manager working together to handle so-called "predefined-handle keys" (marked by flag 0x40 in CM\_KEY\_NODE.Flags). This is a special, undocumented type of key that works similarly to symbolic links, but instead of redirecting to an arbitrary registry path, they redirect to specific 32-bit predefined handles (i.e. one of the HKEY\_\* keys). They were historically a source of numerous security bugs, and were eventually deprecated in July/December 2023 to address Project Zero issues [#2445](https://bugs.chromium.org/p/project-zero/issues/detail?id=2445) + [#2452](https://bugs.chromium.org/p/project-zero/issues/detail?id=2452) (CVE-2023-35356) and [#2492](https://bugs.chromium.org/p/project-zero/issues/detail?id=2492) (CVE-2023-35633).


This goes to show the extent of legacy/compatibility mechanisms maintained in Windows, and the degree of collaboration between the user-mode and kernel parts of the registry code. But coming back to the subject of top-level keys, it is worth having some general idea of their role in the system going forward. A number of existing resources do a great job of explaining exactly this (see my [previous post](/2024/06/the-windows-registry-adventure-3.html) for references), so I will only provide a very brief overview below. Overall, the most important takeaway is the fact that HKEY\_LOCAL\_MACHINE and HKEY\_USERS are the two integral keys that can be used to access almost all data in the globally visible registry view. The other HKEY\_\* keys are derivatives of these two (with the exception of HKEY\_PERFORMANCE\_\* which aren't even real keys), and exist mostly for convenience.

| Top-level key | Internal registry path | Description | 
| HKEY\_CLASSES\_ROOT | Merged view of: \Registry\Machine\Software\Classes \Registry\User\\\<SID>\_Classes | The key contains file name extension associations and COM class registration information. The merging of the two keys is performed in KernelBase.dll, see OpenClassesRootInternal, BaseRegQueryAndMergeValues and other neighboring functions, as well as the [HKEY\_CLASSES\_ROOT Key](https://learn.microsoft.com/en-us/windows/win32/sysinfo/hkey-classes-root-key) and [Merged View of HKEY\_CLASSES\_ROOT](https://learn.microsoft.com/en-us/windows/win32/sysinfo/merged-view-of-hkey-classes-root) official articles. | 
| HKEY\_CURRENT\_USER | \Registry\User\\\<SID> | Stores configuration associated with the current user. | 
| HKEY\_LOCAL\_MACHINE | \Registry\Machine | Stores global, system-wide configuration. | 
| HKEY\_USERS | \Registry\User | Stores information about all users currently logged in the system. | 
| HKEY\_PERFORMANCE\_DATA | - | Not a real key: a pseudo-key that allows applications to query performance information through the Registry API. | 
| HKEY\_PERFORMANCE\_TEXT | - | Not a real key: can be used to query performance information through the Registry API, described in US English. | 
| HKEY\_PERFORMANCE\_NLSTEXT | - | Not a real key: can be used to query performance information through the Registry API, described in the local system language. | 
| HKEY\_CURRENT\_CONFIG | \Registry\Machine\System\CurrentControlSet\Hardware Profiles\Current | Stores information about the current hardware profile. | 
| HKEY\_DYN\_DATA | - | A deprecated equivalent of HKEY\_PERFORMANCE\_DATA which only existed in Windows 9x. It was designed to be a general store for dynamically generated information, such as performance counters or hardware configuration. | 
| HKEY\_CURRENT\_USER\_LOCAL\_SETTINGS | \Registry\User\\\<SID>\_Classes\Local Settings | Stores configuration associated with the current user that is local to the machine and not subject to the roaming profile. | 


In terms of security, the top-level keys and their subtrees are generally protected in line with common sense. Nearly all subkeys of HKEY\_LOCAL\_MACHINE (i.e. global system settings) are only writable by Administrators and the system itself. Some of the subtrees are readable by normal users (e.g. HKLM\Software or HKLM\System), while others don't allow any access to restricted accounts (e.g. HKLM\SAM, which stores user credentials). Furthermore, normal users have full access to their own user hives (HKU\\\<SID> and HKU\\\<SID>\_Classes) and no access to other users' hives, while Administrators have unrestricted access to all of the user hives under HKU.


All in all, this is to ensure that each user has their own local hive to store data in, and can read non-sensitive system configuration, while Administrators have full control over everything in the registry so that they can administer the system effectively. With a basic understanding of the high-level structure of the registry, let's find out more about how it works under the hood.

## The low-level view

If the Windows kernel doesn't use predefined keys in the same way as the user-mode API does, then the question becomes – where does the registry tree start? You have probably already guessed the answer based on this and previous blog posts: it's the \Registry object in the global NT object namespace. Internally, it is a volatile key in a virtual "master" hive (pointed to by nt!CmpMasterHive), with both the key and the hive existing only in memory for organizational purposes. Their setup takes place early in the boot process in the internal CmInitSystem1 function, and the \Registry object can be seen in tools for exploring the object manager namespace, such as [WinObj](https://learn.microsoft.com/en-us/sysinternals/downloads/winobj):



This is essentially the entry point to access any registry key in the system. Whenever the object manager is involved with an operation on a path starting with \Registry, it knows to pass execution to the CmpParseKey function, which takes over the operation, parses the remainder of the path, tries to open or create the given key and returns the object to the caller. Since \Registry is a normal key for most intents and purposes, we can query it in WinDbg:

```
 
```

kd> !reg querykey \Registry



Found KCB = ffff8f818bad92f0 :: \REGISTRY


Hive         ffff8f818ba88000

KeyNode      ffff8f818bada024


[SubKeyAddr]         [SubKeyName]

ffff8f818bada244     A

ffff8f818bada16c     MACHINE

ffff8f818bada1d4     USER

ffff8f818bada2c4     WC


Use '!reg keyinfo ffff8f818ba88000 <SubKeyAddr>' to dump the subkey details


[ValueType]         [ValueName]                   [ValueData]

Key has no Values

 

As the output shows, the root key has four subkeys: A, MACHINE, USER and WC. Two of them are already known to us: "Machine" corresponds to HKEY\_LOCAL\_MACHINE, and "User" corresponds to HKEY\_USERS. Furthermore, "A" serves as the root for all private hives loaded as application hives (using the [RegLoadAppKey](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regloadappkeyw) API). The key and any of its subkeys cannot be opened through their fully qualified path (\Registry\A\...) regardless of their security descriptor or the privileges of the caller, because CmpParseKey detects and denies such requests with the STATUS\_ACCESS\_DENIED error code. This is to guarantee that all app hives remain private and can only be accessed through the handles returned by RegLoadAppKey. Lastly, "WC" likely stands for "Windows Containers" and is the mount point for differencing hives loaded as part of Windows containerization support (introduced in Windows 10 1607). The key is world-readable and isn't subject to any special protections, but it is not mapped to any predefined keys either, so it is only accessible via system calls and not through the official API (with the exception of symbolic links).


A diagram of the low-level view of the registry and how the high-level predefined keys map to it is shown below:



Evidently, the internal registry layout is much more structured than its high-level counterpart, and follows a few basic rules:

- The first and second levels of the tree are predetermined and always the same.
- The third level consists solely of root keys of active hives loaded in the system.
- The fourth and further levels are nested subkeys of the hives.


On a typical installation of Windows, there are usually dozens of hives loaded in the system at any given time, storing a variety of configuration data. Having already used the term "hives" extensively in this and the previous blog posts, let's discuss in more detail what they are and how they work.

## Hive files

What better way to describe a registry hive than to quote an official definition from a Microsoft article ([Registry Hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives)):

| A hive is a logical group of keys, subkeys, and values in the registry that has a set of supporting files loaded into memory when the operating system is started or a user logs in. | 


In other words, a hive is a standalone database encoded in the regf format that serves a specific purpose in the operating system (if you're curious about the origin of the name, check [Why is a registry file called a "hive"?](https://devblogs.microsoft.com/oldnewthing/20030808-00/?p=42943)). Hives can be classified based on where they reside (on disk, in memory, or both):

- File-backed

- Unloaded: a hive that is stored persistently on disk but not actively loaded in the system.
- Loaded: a hive that is both stored on disk and currently used by Windows. The in-memory and on-disk representations of the database are continuously synchronized by the kernel to ensure its consistency in the event of a sudden power loss or other system failures.

- Volatile: an ephemeral hive that is not stored on disk and only lives in memory until the next system reboot. Examples include the master hive (corresponding to the \Registry global root) and the hardware hive mounted at \Registry\Machine\HARDWARE. They are not particularly important from a security perspective but their existence is worth noting for completeness.


A majority of hives are file-backed, because their purpose is precisely to store data across long periods of time and multiple reboots. Interestingly, whenever we observe a hive on disk (which may require the "Show hidden files, folders, and drives" option to be checked and "Hide protected operating system files" to be unchecked in Explorer), it is usually not a single file but a collection of files with a common name prefix. For instance, let's have a look at the NTUSER hive in a user's home directory in Windows 11:



All of these files are related to a single hive. Let's briefly go over each file type visible in the screenshot:

- .DAT – this is the core hive file and the only one that is strictly required. The .dat extension is frequently seen in the context of hive files (other less common variants: .hiv and .hve), but it is only customary and the kernel will happily load a hive from any file regardless of its name (for example, none of the system hive files in C:\Windows\system32\config have any extension at all). While the hive is active, the kernel locks the file, preventing it from being simultaneously operated on by any other program.
- .LOG1 and .LOG2 – log files maintained by the Configuration Manager to safeguard the low-level recoverability of the hive. When they are used, every write operation to the hive is first written to a log file, and later flushed to the hive file itself. For a deeper analysis of the logging mechanism, please refer to the Registry chapter in the [Windows Internals](https://www.microsoftpressstore.com/store/windows-internals-part-2-9780135462331) book (specifically the "Stable storage" and "Incremental logging" sections). Although hive files are typically accompanied by .LOG1/.LOG2 files in most real-life scenarios, it is also possible to have a single .LOG file (by loading the hive with the REG\_HIVE\_SINGLE\_LOG flag), or prevent the kernel from creating them completely by using the REG\_OPEN\_READ\_ONLY or REG\_IMMUTABLE flags.
- .regtrans-ms and .blf – additional log files related to the [Kernel Transaction Manager](https://learn.microsoft.com/en-us/windows/win32/ktm/kernel-transaction-manager-portal) and transactional registry. They store information about pending operations performed on transacted keys opened with the [RegCreateKeyTransacted](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regcreatekeytransactedw) or [RegOpenKeyTransacted](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regopenkeytransactedw) API functions, and are used to roll-forward these operations in case of a sudden system reboot. They are created at the request of the Configuration Manager, but are internally managed by the [Common Log File System](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/introduction-to-the-common-log-file-system) driver. They are enabled for system hives (all hives under HKLM have their transaction logs collectively saved in C:\Windows\system32\config\TxR), and for user-specific hives (NTUSER.DAT and UsrClasses.dat), but they are always disabled for application hives (\Registry\A\...) and differencing hives (\Registry\WC\...). It is also possible to force the loading of a hive with disabled transactions by using the REG\_HIVE\_NO\_RM flag.


In summary, a single hive may be associated with up to 10 files on disk. I won't go into the details of their binary formats as this will be discussed in future posts, but it's interesting to note that each file type has been affected by some security issues in the past (see examples for [.DAT](<https://project-zero.issues.chromium.org/issues?q=id:(42450251%20%7C%2042452400%20%7C%2042451423%20%7C%2042451425%20%7C%2042451427%20%7C%2042451449%20%7C%2042451463%20%7C%2042451465%20%7C%2042451478%20%7C%2042451494%20%7C%2042451502%20%7C%2042451588%20%7C%2042451596%20%7C%2042451601%20%7C%2042451640)>), [.LOG1/.LOG2](<https://project-zero.issues.chromium.org/issues?q=id:(42452405%20%7C%2042450541%20%7C%2042450609%20%7C%2042451598%20%7C%2042451600)>) and [and .regtrans-ms/.blf](<https://project-zero.issues.chromium.org/issues?q=id:(42450872%20%7C%2042451149%20%7C%2042451150%20%7C%2042451559%20%7C%2042451560)>)). Let's now review some of the default hives that are commonly loaded in Windows, and how we can enumerate and examine them.

## The hive list and memory mappings

Internally, the Windows kernel maintains a linked list of active hives in the system, starting with the global nt!CmpHiveListHead object. But what's interesting is that the information is also made globally visible through the registry itself: there is a special key at \Registry\Machine\System\CurrentControlSet\Control\hivelist where the kernel maintains a single string value per loaded hive, with its name indicating the registry mount point and its data specifying the low-level path on disk. All active file-backed hives in the system except application hives are listed there, and inspecting the list is as simple as finding the "hivelist" key in Regedit:



Here, we can see the standard system hives mounted under \Registry\Machine, several user hives under \Registry\User (some of them for system accounts and some for the current user), and a number of differencing hives at \Registry\WC. A similar, but much more detailed list of hives may be obtained by using the !reg hivelist command in WinDbg:


kd> !reg hivelist


-------------------------------------------------------------------------------------------------------------------------------------------------

|     HiveAddr     |Stable Length|    Stable Map    |Volatile Length|    Volatile Map    |MappedViews        | FileName

-------------------------------------------------------------------------------------------------------------------------------------------------

| ffff8f818ba88000 |       2000  | ffff8f818ba88128 |       1000    |  ffff8f818ba883a0  | ffff8f818bad5000  | <NONAME>

| ffff8f818ba62000 |     d8c000  | ffff8f818badc000 |      41000    |  ffff8f818ba623a0  | ffff8f818badb000  | SYSTEM

| ffff8f818bb87000 |      24000  | ffff8f818bb87128 |      10000    |  ffff8f818bb873a0  | ffff8f818bb5a000  | <NONAME>

| ffff8f818c813000 |    4c4b000  | ffff8f818e482000 |     330000    |  ffff8f8190b98000  | ffff8f818e470000  | emRoot\System32\Config\SOFTWARE

| ffff8f818e578000 |       8000  | ffff8f818e578128 |          0    |  0000000000000000  | ffff8f818e4f9000  | kVolume1\EFI\Microsoft\Boot\BCD

| ffff8f818c75b000 |      74000  | ffff8f818c75b128 |       1000    |  ffff8f818c75b3a0  | ffff8f818e5d4000  | temRoot\System32\Config\DEFAULT

| ffff8f818e773000 |       9000  | ffff8f818e773128 |       1000    |  ffff8f818e7733a0  | ffff8f818e9be000  | emRoot\System32\Config\SECURITY

| ffff8f818e9a8000 |       d000  | ffff8f818e9a8128 |          0    |  0000000000000000  | ffff8f818ea2c000  | \SystemRoot\System32\Config\SAM

| ffff8f818ec68000 |      2f000  | ffff8f818ec68128 |       1000    |  ffff8f818ec683a0  | ffff8f818ea54000  | files\NetworkService\NTUSER.DAT

| ffff8f818ee2e000 |      30000  | ffff8f818ee2e128 |          0    |  0000000000000000  | ffff8f818edf9000  | rofiles\LocalService\NTUSER.DAT

| ffff8f818ee63000 |      72000  | ffff8f818ee63128 |          0    |  0000000000000000  | ffff8f818ee48000  | \SystemRoot\System32\Config\BBI

| ffff8f8190370000 |     19b000  | ffff8f8190370128 |       4000    |  ffff8f81903703a0  | ffff8f81903e7000  | \??\C:\Users\user\ntuser.dat

| ffff8f8190373000 |     2cf000  | ffff8f81903fb000 |          0    |  0000000000000000  | ffff8f81903eb000  | \Microsoft\Windows\UsrClass.dat

| ffff8f8191a2e000 |       7000  | ffff8f8191a2e128 |          0    |  0000000000000000  | ffff8f8191a8c000  | 5n1h2txyewy\ActivationStore.dat

| ffff8f8191a30000 |      1c000  | ffff8f8191a30128 |          0    |  0000000000000000  | ffff8f8191a93000  | 5n1h2txyewy\ActivationStore.dat

| ffff8f8191a32000 |      78000  | ffff8f8191a32128 |          0    |  0000000000000000  | ffff8f8191a9a000  | 5n1h2txyewy\ActivationStore.dat

| ffff8f8191bf7000 |     1f3000  | ffff8f8191bf7128 |          0    |  0000000000000000  | ffff8f8191bfb000  | \AppCompat\Programs\Amcache.hve

[...]


This output is missing registry paths, but provides us with the file names, and also contains addresses of the corresponding HHIVE/CMHIVE structures and information about the stable/volatile spaces of each hive. It also shows all active hives in the system, including app hives and volatile hives. For example, the first and third items on the list are the \Registry and \Registry\Machine\HARDWARE hives, respectively – since neither of them are file-backed, their FileName columns state "\<NONAME>".


The final way to enumerate hives in the system is by listing section objects. In modern versions of Windows, most registry hives are mapped in the user address space of a special, thin process named Registry (you can find it in Task Manager), using [sections](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/section-objects-and-views). The two notable exceptions are the SYSTEM hive and any hives that don't exist on disk at the time of the loading (i.e. are created from scratch using the NtLoadKey\* call). But for all other hives, we can have them printed out in WinDbg by finding the Registry process, switching to its context, and issuing the !vad command to display its associated virtual address descriptors (VADs):

kd> !process 0 0

**** NT ACTIVE PROCESS DUMP ****

PROCESS ffffb3047dcf4040

SessionId: none  Cid: 0004    Peb: 00000000  ParentCid: 0000

DirBase: 001ae002  ObjectTable: ffff8f818ba85f00  HandleCount: 3193.

Image: System


PROCESS ffffb3047ddc0080

SessionId: none  Cid: 0040    Peb: 00000000  ParentCid: 0004

DirBase: 02db7002  ObjectTable: ffff8f818ba02c00  HandleCount:   0.

Image: Registry


[...]


kd> .process ffffb3047ddc0080

Implicit process is now ffffb304`7ddc0080

WARNING: .cache forcedecodeuser is not enabled


kd> !vad

VAD             Level         Start             End              Commit

ffffb3047e3653e0  6        28700000        287001ff               0 Mapped       READONLY           \Windows\System32\config\SOFTWARE

ffffb3047e364a80  5        28700200        287003ff               0 Mapped       READONLY           \Windows\System32\config\SOFTWARE

ffffb3047e365020  6        28700400        287005ff               0 Mapped       READONLY           \Windows\System32\config\SOFTWARE

ffffb3047e364760  4        28700600        287007ff               0 Mapped       READONLY           \Windows\System32\config\SOFTWARE

ffffb3047e364e40  6        28700800        287009ff               0 Mapped       READONLY           \Windows\System32\config\SOFTWARE

ffffb3047e364d00  5        28700a00        28700bff               0 Mapped       READONLY           \Windows\System32\config\SOFTWARE

ffffb3047e3646c0  6        28700c00        28700dff               2 Mapped       READONLY           \Windows\System32\config\SOFTWARE

ffffb3047e364800  3        28700e00        28700fff               2 Mapped       READONLY           \Windows\System32\config\SOFTWARE

ffffb3047e3648a0  6        28701000        287011ff               0 Mapped       READONLY           \Windows\System32\config\SOFTWARE

ffffb3047e365160  5        28701200        287013ff               0 Mapped       READONLY           \Windows\System32\config\SOFTWARE

ffffb3048058e450  6        28701400        2870147f             114 Mapped       READONLY           \Windows\System32\config\BBI

ffffb30480f68890  4        28701480        2870167f              19 Mapped       READONLY           \Users\user\NTUSER.DAT

ffffb30480f690b0  5        28701680        2870187f               5 Mapped       READONLY           \Users\user\AppData\Local\Microsoft\Windows\UsrClass.dat

ffffb30480f69e70  2        28701880        2870197f               2 Mapped       READONLY           \Users\user\AppData\Local\Microsoft\Windows\UsrClass.dat

[...]

ffffb3047e364580  6        2877fca0        2877fe9f               0 Mapped       READONLY           \Windows\System32\config\SOFTWARE

ffffb3047e364c60  5        2877fea0        2877feaf               8 Mapped       READONLY           \EFI\Microsoft\Boot\BCD

ffffb3047e366b00  6        2877feb0        2877ff2f              19 Mapped       READONLY           \Windows\System32\config\DEFAULT

ffffb3047e372ae0  3        2877ff30        2877ff3f               0 Mapped       READONLY           \Windows\System32\config\SECURITY

ffffb3047e3745c0  5        2877ff40        2877ff4f               0 Mapped       READONLY           \Windows\System32\config\SAM

[...]


There may be multiple VADs associated with a single hive, because hives are mapped in a fragmented manner and may dynamically grow over time. The address ranges specified by the "Start" and "End" columns correspond to the "pcell" addresses returned by the !reg cellindex WinDbg command when multiplied by 0x1000 (the page size). For example, the BCD hive is mapped between 0x2877fea0000 and 0x2877feaffff. The first page (the 4 KiB hive header) is typically not mapped, but we can see the raw data of the first bin residing at address 0x2877fea1000:


```
 
```
kd> db 0x2877fea1000

00000287`7fea1000  68 62 69 6e 00 00 00 00-00 10 00 00 00 00 00 00  hbin............

00000287`7fea1010  00 00 00 00 a5 7a 66 c9-8b 03 da 01 00 00 00 00  .....zf.........

00000287`7fea1020  a0 ff ff ff 6e 6b 2c 00-c1 e4 70 f6 e3 8b da 01  ....nk,...p.....

00000287`7fea1030  03 00 00 00 48 04 00 00-02 00 00 00 00 00 00 00  ....H...........

00000287`7fea1040  48 02 00 00 ff ff ff ff-00 00 00 00 ff ff ff ff  H...............

00000287`7fea1050  68 01 00 00 ff ff ff ff-16 00 00 00 00 00 00 00  h...............

00000287`7fea1060  00 00 00 00 00 00 00 00-00 00 00 00 0c 00 00 00  ................

00000287`7fea1070  4e 65 77 53 74 6f 72 65-52 6f 6f 74 00 00 00 00  NewStoreRoot....

## Default system hives

Knowing the basic structure of the registry tree and how we can enumerate hives, let's now briefly discuss the role and properties of the default hives that we'll find in a clean installation of Windows:

| Registry path | Description | 
| \Registry\A\{RANDOM GUID} | Application hives may contain any information the client program decides to save, but two of its primary uses are by Universal Windows Platform (UWP) applications to store information about their WinRT classes (in a file called ActivationStore.dat) and their private settings (backed by settings.dat). The lifespan of app hives is tied to their active references, so whenever all handles to the hive are closed (or the process terminates), the hive is automatically unloaded. The security rights set on the keys in app hives are generally irrelevant, because they cannot be opened by any process that doesn't have a valid handle to the hive to start with, thanks to the extra checks hardcoded in CmpParseKey. | 
| \Registry\Machine\BCD00000000 | The hive contains the Boot Configuration Database (BCD) that replaced the boot.ini file in Windows Vista. It is backed by a hidden \EFI\Microsoft\Boot\BCD file, and can be modified indirectly with the [bcdedit](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/bcdedit) command line utility. Full access is granted to administrators, and no access is granted to normal users. | 
| \Registry\Machine\HARDWARE | The hive contains a specification of the system's legacy hardware (such as a keyboard or mouse). As previously mentioned, it is a volatile hive without a backing file, which is dynamically generated during boot in the internal CmpInitializeHardwareConfiguration function. It grants full access to administrators and read access to normal users. | 
| \Registry\Machine\SAM | The hive contains information managed by the Security Account Manager (SAM), such as user passwords and group definitions. It is backed by the C:\Windows\system32\config\SAM file, and it is the only hive with lazy flushing disabled, meaning that it must be manually synchronized with the backing file by the SAM Server using syscalls like NtFlushKey and NtRestoreKey. It grants full access to the LocalSystem account and no access to any of the users, so even administrators cannot modify or browse it by default. | 
| \Registry\Machine\SECURITY | The hive contains security-critical information such as security policies and user right assignments. It is backed by C:\Windows\system32\config\SECURITY, and similarly to SAM, it only grants access to the LocalSystem account. | 
| \Registry\Machine\SOFTWARE | The hive is a general-purpose store for system-wide configuration of both Windows built-in components and third-party software. It is generally the only hive in HKLM where legitimate programs ever need to write to, and for this reason it is the only one subject to registry virtualization. It is backed by the C:\Windows\system32\config\SOFTWARE file, and a majority of its keys are user-readable and admin-writable. However, there are some exceptions to this rule: firstly, there are several default keys with more permissive rights (e.g. user-writable) and some default keys with more restrictive rights (e.g. only readable by specific users and not broadly accessible). Secondly, the responsibility to set adequate security of the keys is shared by all applications using the hive, but in practice, their behavior isn't always consistent with Windows (i.e. they may set more or less permissive rights than we would normally expect). | 
| \Registry\Machine\SYSTEM | The hive is a store for system-wide configuration that is required to boot the system, such as information about device drivers and system services. It is backed by the C:\Windows\system32\config\SYSTEM file and it is first loaded in memory before the Windows kernel itself, by a copy of the Configuration Manager found in the winload.exe/winload.efi executables. It is also the only system hive mapped in kernel paged pool and not in the user-space of the special Registry process. Similarly to SOFTWARE, most of its keys are user-readable and admin-writable, but there are some notable exceptions to this rule. | 
| \Registry\User\\\<SID> | The user hives are meant to store user-specific configuration; when a new user is created, the user hive starts off with a basic structure and grows larger as applications save their settings over time. They are typically backed by the NTUSER.DAT file in the user directory, but can also be overridden by NTUSER.MAN by taking advantage of the [Mandatory User Profiles](https://learn.microsoft.com/en-us/windows/win32/shell/mandatory-user-profiles). Their security is arranged such that they are accessible by the associated user and administrators, but not other users in the system. A special case of user hives are the hives corresponding to system-specific accounts which are mounted and globally visible under \Registry\User: \Registry\User\.DEFAULT – the user hive of the LocalSystem account, backed by C:\Windows\system32\config\DEFAULT. If you think this is a confusing name, I agree, and so does Raymond Chen in his [The .Default user is not the default user](https://devblogs.microsoft.com/oldnewthing/20070302-00/?p=27783) blog post. \Registry\User\S-1-5-18 – this is the SID of the LocalSystem account, so the key is simply a symbolic link to \Registry\User\.DEFAULT. \Registry\User\S-1-5-19 – the user hive of the LocalService account, backed by C:\Windows\ServiceProfiles\LocalService\NTUSER.DAT. \Registry\User\S-1-5-20 – the user hive of the NetworkService account, backed by C:\Windows\ServiceProfiles\NetworkService\NTUSER.DAT. | 
| \Registry\User\\\<SID>\_Classes | The "classes" hive is the second one that gets automatically loaded once a user logs into the system. It is responsible for storing the user-specific file extension associations and COM class registrations, which are then merged with \Registry\Machine\Software\Classes by the Registry API and exposed as the HKEY\_CLASSES\_ROOT top-level key. It is additionally used by the registry virtualization mechanism, and is pointed to by the \Registry\User\\\<SID>\Software\Classes symbolic link. The hive is backed by C:\Users\\\<USER>\AppData\Local\Microsoft\Windows\UsrClass.dat, and has the same security properties as the regular user hive: it is only accessible by the owner user and administrators. | 
| \Registry\WC\Silo{...} | Differencing hives are a new technology introduced in Windows 10 Anniversary Update to support registry containerization in various Windows technologies such as Helium containers (application silos, used e.g. by MSIX packaged apps) or Argon containers (server silos, used e.g. by Docker). They are managed by the AppInfo service through VRegDriver – a special module built into ntoskrnl.exe that is tightly integrated with the Configuration Manager and exposes an IOCTL interface to operate on delta hives. Many default Windows components and programs (e.g. the Widgets app, Paint, Notepad) run in the context of app silos, so there are typically a number of hives mounted under \Registry\WC at any given time. Other than that, there isn't much that can be said about them as a whole, as their backing files and security settings can vary greatly depending on multiple factors. These special hives will be discussed in more detail in future blog posts. | 


There are a few other system hives that can be found in C:\Windows\system32\config\ on modern versions of Windows that aren't discussed above:

- BBI – likely Background Broker Infrastructure, loaded during boot as an app hive by the Background Tasks Infrastructure Service (bisrv.dll).
- COMPONENTS – contains information associated with Windows Update and the Component Based Servicing (CBS) stack. It isn't always active, but instead, it is loaded and unloaded on demand whenever a component installation or update takes place.
- DRIVERS – driver information store, loaded by the kernel on demand at \Registry\Machine\DRIVERS.
- ELAM – Early Launch Anti-Malware, briefly loaded during boot at \Registry\Machine\ELAM.


Note that these hives exist, but they aren't particularly interesting in the context of this research. Now, equipped with the knowledge of how the default Windows hives function, let's see what operations can be performed on them as whole objects.

## Hive operations

The Windows kernel provides several system calls for operating on registry hives, which are summarized in the following table:

| Syscall name(s) | Description | 
| NtCompressKey | Compresses the specific hive in-place by defragmenting allocated cells. | 
| NtLoadKey\* | Loads an existing hive or creates a new one, and mounts it in the global tree view. Documented counterparts: [RegLoadKey](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regloadkeyw) and [RegLoadAppKey](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regloadappkeyw). The interface is internally used by the 'File > Load Hive...' option in Regedit. | 
| NtReplaceKey | Replaces the backing file of a specific active hive with another file on the next system boot. Documented counterpart: [RegReplaceKey](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regreplacekeyw). | 
| NtRestoreKey | Copies data from a hive file to the global registry tree. This operation is similar to loading, but doesn't maintain any synchronization between the in-memory and on-disk representations after the hive is loaded (restored). Documented counterpart: [RegRestoreKey](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regrestorekeyw). This interface is internally used by the 'File > Import...' option in Regedit. | 
| NtSaveKey\*, NtSaveMergedKeys | Saves the specific subtree to a file on disk in the regf format. Documented counterparts: [RegSaveKey](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regsavekeyw) and [RegSaveKeyEx](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regsavekeyexw). This interface is internally used by the 'File > Export...' option in Regedit. Interestingly, the sole purpose of NtSaveMergedKeys seems to be to provide a NtSaveKey-like functionality for HKEY\_CLASSES\_ROOT, which, as mentioned earlier, is a special merged view of \Registry\Machine\Software\Classes and \Registry\User\\\<SID>\_Classes implemented in user-mode. | 
| NtUnloadKey\* | Unloads a registry hive and unmounts it from the global view. Documented counterpart: [RegUnLoadKey](https://learn.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regunloadkeyw). This interface is internally used by the 'File > Unload Hive...' option in Regedit. | 


The above services provide some valuable insight into what actions can be performed on hives. A careful reader will notice that this list is longer than the table of basic hive operations shown in [blog post #2](/2024/04/the-windows-registry-adventure-2.html), which is because all of these syscalls (other than NtLoadKey\* with the REG\_APP\_HIVE flag) require administrative privileges (SeBackupPrivilege or SeRestorePrivilege) and are not a widely accessible attack surface. Furthermore, most of them see little to no use in a typical system run time. The only notable exception is NtRestoreKey, which is part of the "RXact" user-mode transaction mechanism used for operating on the SAM hive by the SAM Service, as mentioned in the [Windows Kernel registry quota exhaustion may lead to permanent corruption of the SAM database](https://github.com/googleprojectzero/p0tools/tree/master/WinRegLowSeverityBugs/Reports/15_Registry_quota_exhausted_SAM_corruption) report (CVE-2024-26181).


From a strictly security perspective, the most critical hive-related operation is their loading. Let's dive deeper into how it works.

## Loading hives

There are currently three distinct ways in which registry hives are loaded in Windows:

1. Internally by the kernel at boot time. This applies to most of the hives under \Registry\Machine, as well as \Registry\User\.DEFAULT. There is also an optional hive named "OSDATA" that gets loaded under \Registry\Machine\OSDATA if it exists at C:\Windows\system32\config\OSDATA. It is unclear what its role is, and I was unable to find much information during a quick web search. It seems to be used by user-mode libraries whenever [RtlIsStateSeparationEnabled](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-rtlisstateseparationenabled) returns TRUE, which implies it may be somehow related to [State Separation](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/factoryos/state-separation?view=windows-11).
2. Using one of the NtLoadKey-family system calls, which may be invoked from the kernel, a privileged user-mode service, or a normal user application. In the latter two cases, the request usually comes through a corresponding Registry API function such as RegLoadKey or (more likely) RegLoadAppKey.
3. Through the IOCTL interface of the VRegDriver, in order to load a differencing hive under \Registry\WC. This path is taken exclusively by system services responsible for the initialization of application and server silos, such as the AppInfo service.


The first option isn't particularly important because it happens seamlessly before we can influence the system in any way, and we are simply left with the outcome (but if you're curious to learn more, here are some good starting points: CmInitSystem1, CmpInitializeSystemHive, NtInitializeRegistry, CmpInitializeSystemHivesLoad, CmpFinishSystemHivesLoad). Furthermore, option #3 is related to container support and thus mostly outside of the scope of this post, but we will briefly cover it later. Right now, let's focus on the standard interfaces that Windows exposes for loading hives (option #2), as this is where the magic happens.


The primary Registry API function for loading hives is RegLoadKey, whose Unicode version has the following declaration:


LSTATUS RegLoadKeyW(

[in]           HKEY    hKey,

[in, optional] LPCWSTR lpSubKey,

[in]           LPCWSTR lpFile

);


It's quite clear that the function offers limited customization options, as it only takes a handle to the root key, the name of the subkey that will become the mount point, and the path of the hive file to load. In Windows Vista, a second API function called RegLoadAppKey was introduced, designed specifically to allow the caller to load application hives:


LSTATUS RegLoadAppKeyW(

[in]  LPCWSTR lpFile,

[out] PHKEY   phkResult,

[in]  REGSAM  samDesired,

[in]  DWORD   dwOptions,

DWORD   Reserved

);


In this case, we lose the ability to specify the path of the hive mount point, which is irrelevant because app hives cannot be accessed through fully-qualified paths anyway. On the other hand, we gain some customizability as we can pass the REG\_PROCESS\_APPKEY flag via dwOptions, and there is also a Reserved parameter that may be used to further extend the functionality in the future.


Both of these documented functions internally rely on NtLoadKey-family system calls, such as NtLoadKey, NtLoadKey2, NtLoadKeyEx or NtLoadKey3 (admittedly quite an unconventional progression). New iterations have been historically added in subsequent versions of Windows to extend the functionality of the previous syscalls. In the case of NtLoadKeyEx, the definition of this singular system call even changed between Windows Server 2003 and Windows Vista to accommodate new options, which is unusual, as syscall definitions tend to be stable. These developments are illustrated in the image below:



Let's have a closer look at the prototype of NtLoadKeyEx, whose arguments most clearly reflect the evolution of the interface. While the latest NtLoadKey3 function introduced further advancements by making it possible to specify additional impersonation tokens, its definition references an undocumented structure and is thus less suitable as an example. If you're curious to learn more about this newest syscall, see James's [Silent Exploit Mitigations for the 1%](https://www.tiraniddo.dev/2020/05/silent-exploit-mitigations-for-1.html) blog post. Meanwhile, NtLoadKeyEx is defined as follows:


NTSTATUS NtLoadKeyEx(

POBJECT_ATTRIBUTES TargetKey,  // since NtLoadKey   (Windows NT 3.1)

POBJECT_ATTRIBUTES SourceFile, // since NtLoadKey   (Windows NT 3.1)

ULONG Flags,                   // since NtLoadKey2  (Windows NT 4.0)

HANDLE TrustClassKey,          // since NtLoadKeyEx (Windows Server 2003)

HANDLE Event,                  // since NtLoadKeyEx (Windows Vista)

DWORD DesiredAccess,           // since NtLoadKeyEx (Windows Vista)

PHANDLE RootHandle,            // since NtLoadKeyEx (Windows Vista)

PIO_STATUS_BLOCK IoStatus      // since NtLoadKeyEx (Windows Vista)

);


Here's an overview of the semantics of the parameters:

- TargetKey – specifies the new mount point of the hive, e.g. \Registry\User\\\<SID>. Corresponds to the combination of hKey/lpSubKey arguments in RegLoadKey.
- SourceFile – specifies the path of the hive on a file system in the internal NT format, e.g. \??\C:\Users\\\<USER>\NTUSER.DAT. Directly corresponds to the lpFile argument in RegLoadKey.
- Flags – specifies a set of options for loading the hive.
- TrustClassKey – specifies an existing hive within the same "trust class" as the loading hive. Trust classes, introduced in Windows Server 2003, define strict rules for which hives can link to each other, preventing symbolic link attacks (for example, disallowing links from HKCU to HKLM).


The last four arguments are only used for app hives or hives for which the caller explicitly requests an open handle (REG\_APP\_HIVE or REG\_LOAD\_HIVE\_OPEN\_HANDLE flags set):

- Event – specifies an event object that gets signaled when the hive is unloaded. Internally, it gets added to a dynamically allocated array pointed to by CMHIVE.UnloadEventArray. It is most meaningful for application hives, which get automatically unloaded when all references are closed, so the event makes it possible for applications to get notified about this fact and perform any follow up actions.
- DesiredAccess – specifies the access rights requested for the returned root key. It directly corresponds to the samDesired argument in RegLoadAppKey.
- RootHandle – a pointer to a variable that receives the handle to the root key of the hive. This is the same handle that gets returned by RegLoadAppKey.
- IoStatus – an I/O status block that used to be passed to NtCreateFile when opening the hive file. It is currently unused.


The most interesting parameter is probably Flags, which takes a combination of options for loading the hive, and is very illustrative of what is actually possible with the interface. The supported flags are defined in the Windows SDK, both in the user-mode (winnt.h) and kernel-mode headers (wdm.h). The flag namespace is actually shared between the NtLoadKey\* syscalls and NtRestoreKey, so I crossed out the flags that are not relevant to loading (mask 0xB):


//

// Key restore & hive load flags

//


#define REG_WHOLE_HIVE_VOLATILE         (0x00000001L) // Restore whole hive volatile

#define REG_REFRESH_HIVE                (0x00000002L) // Unwind changes to last flush

#define REG_NO_LAZY_FLUSH               (0x00000004L) // Never lazy flush this hive

#define REG_FORCE_RESTORE               (0x00000008L) // Force the restore process even when we have open handles on subkeys

#define REG_APP_HIVE                    (0x00000010L) // Loads the hive visible to the calling process

#define REG_PROCESS_PRIVATE             (0x00000020L) // Hive cannot be mounted by any other process while in use

#define REG_START_JOURNAL               (0x00000040L) // Starts Hive Journal

#define REG_HIVE_EXACT_FILE_GROWTH      (0x00000080L) // Grow hive file in exact 4k increments

#define REG_HIVE_NO_RM                  (0x00000100L) // No RM is started for this hive (no transactions)

#define REG_HIVE_SINGLE_LOG             (0x00000200L) // Legacy single logging is used for this hive

#define REG_BOOT_HIVE                   (0x00000400L) // This hive might be used by the OS loader

#define REG_LOAD_HIVE_OPEN_HANDLE       (0x00000800L) // Load the hive and return a handle to its root kcb

#define REG_FLUSH_HIVE_FILE_GROWTH      (0x00001000L) // Flush changes to primary hive file size as part of all flushes

#define REG_OPEN_READ_ONLY              (0x00002000L) // Open a hive's files in read-only mode

#define REG_IMMUTABLE                   (0x00004000L) // Load the hive, but don't allow any modification of it

#define REG_NO_IMPERSONATION_FALLBACK   (0x00008000L) // Do not fall back to impersonating the caller if hive file access fails


As shown, there are a total of 13 available flags with clear names and comments explaining their purpose. However, not all 8192 combinations of them are valid. Rules and dependencies exist – for example, application hives (REG\_APP\_HIVE) cannot be loaded with lazy flushing disabled (REG\_NO\_LAZY\_FLUSH). In the next sections, we will explore these limitations, covering the required client privileges, supported flags and allowed mount points.

### Standard hive loading

The most important distinction for the NtLoadKey\* system calls is whether the hive is being loaded as an app hive (REG\_APP\_HIVE flag set) or not. If it's not, then it's considered as "standard" hive loading, the only type that existed prior to Windows Vista.

#### Privileges

The official documentation for RegLoadKey states that both SeRestorePrivilege and SeBackupPrivilege privileges are required to use the function. In practice, however, only SeRestorePrivilege is checked. This is still a privilege that is granted to administrators only, so loading any globally visible hives is not possible for a normal user. As evidence, attempting to use the 'File > Load Hive...' option in Regedit without administrative privileges results in an 'Insufficient privileges' error. This might also explain, at least in part, why the Configuration Manager may not be entirely robust against malformed hives. The original developers likely assumed the code would need to gracefully handle random data corruption, but not necessarily malicious files from untrusted sources.


It is also worth keeping in mind that while a local attacker cannot directly load a normal hive, they may be able to entice the Profile Service to load it on their behalf thanks to [Mandatory User Profiles](https://learn.microsoft.com/en-us/windows/win32/shell/mandatory-user-profiles). This mechanism causes the system to prioritize the NTUSER.MAN hive file (if it exists in the user directory) over NTUSER.DAT, and loads it as the user hive when the user signs in. It is thus possible to plant a specially crafted hive under NTUSER.MAN, log out, and log back in to have it loaded by Windows. This comes with some limitations, as the hive needs to have a valid, basic structure expected of the HKCU, and the attacker must be able to create files in %USERPROFILE% and to log in and out (so it precludes certain sandbox escapes etc.). Nevertheless, it may be a valid attack vector, and it was in fact used to demonstrate the practical exploitability of issues [#2047](https://bugs.chromium.org/p/project-zero/issues/detail?id=2047), [#2048](https://bugs.chromium.org/p/project-zero/issues/detail?id=2048), [#2297](https://bugs.chromium.org/p/project-zero/issues/detail?id=2297), [#2366](https://bugs.chromium.org/p/project-zero/issues/detail?id=2366), [#2419](https://bugs.chromium.org/p/project-zero/issues/detail?id=2419), [#2445](https://bugs.chromium.org/p/project-zero/issues/detail?id=2445) and [#2492](https://bugs.chromium.org/p/project-zero/issues/detail?id=2492). An even more extreme idea of this kind could involve two local, cooperating users who grant each other access to their respective NTUSER.DAT files and modify them while the other user is signed out (when the hive is not locked). However this is even less practical so we won't spend more time on this scenario.

#### Mount Points

One of the core invariants of the Windows registry is that hives may only be mounted within the master hive (CmpMasterHive). This is enforced by CmpDoParseKey when trying to link the new hive into the global tree, and it means that hives cannot be loaded relative to other hives. If we look at the list of the top-level HKEY keys, the only two that represent the master hive are HKEY\_LOCAL\_MACHINE and HKEY\_USERS. And indeed, the 'File > Load Hive...' option in Regedit is only enabled when the focus is on one of the two keys, otherwise it is grayed out:



As mentioned earlier, the current convention is that all hives in the system are typically mounted on the third level of the global registry tree, i.e. below one of \Registry\{A,MACHINE,USER,WC}. However, there is nothing preventing a privileged program from loading a hive directly under the \Registry root, too.

#### Flags

In standard hive loading, there are almost no restrictions on the flags that can be used. The only requirement is that if the REG\_FLUSH\_HIVE\_FILE\_GROWTH flag is set, then both REG\_HIVE\_SINGLE\_LOG and REG\_BOOT\_HIVE must be set, too.

#### Unloading

Normal hives stay loaded until they are manually unloaded or the system is shut down. The former can be achieved with the RegUnLoadKey API, or one of the underlying system calls: NtUnloadKey (since Windows NT 3.1), NtUnloadKeyEx (since Windows XP), or NtUnloadKey2 (since Windows Server 2003). Their prototypes are shown below:


NTSTATUS NtUnloadKey(

POBJECT_ATTRIBUTES TargetKey

);


NTSTATUS NtUnloadKeyEx(

POBJECT_ATTRIBUTES TargetKey,

HANDLE Event

);


NTSTATUS NtUnloadKey2(

POBJECT_ATTRIBUTES TargetKey,

ULONG Flags

);


The first syscall simply takes the path of the target key, the second adds an event that will be signaled when the hive is actually unloaded (in case any references to it are still open and the system call returns STATUS\_PENDING), and the third one makes it possible to pass a REG\_FORCE\_UNLOAD (0x1) flag to force the unload even if any handles are open. All of them require SeRestorePrivilege to call successfully, so a local attacker has no way of using them directly.

### Application hive loading

Application hives are undoubtedly one of the most security-relevant aspects of the registry, as they allow normal users to load fully controlled binary hives in the system. They played a crucial role in my research, having been useful in demonstrating the practical exploitability of 15 vulnerabilities reported to Microsoft.


In technical terms, every hive that is loaded with the REG\_APP\_HIVE flag is an app hive, and they get special treatment from the kernel in several respects. Let's examine some of the apphive-specific behaviors in the sections below.

#### Privileges

Contrary to normal hives, loading application hives requires no specific privileges from the caller. The only precondition is that the client has access to at least one file that is encoded as a regf, and the kernel can also open the file with the security token of the process for reading, and potentially writing. This is a trivial prerequisite if the attacker starts with full control over a local user account in the system, but may be potentially more difficult in more constrained environments such as security sandboxes.


Another consideration specific to application hives are their security descriptors. The documentation of the RegLoadAppKey function states:

| All keys inside the hive must have the same security descriptor, otherwise the function will fail. This security descriptor must grant the caller the access specified by the samDesired parameter or the function will fail. You cannot use the RegSetKeySecurity function on any key inside the hive. | 


This doesn't matter much from a security perspective, because if the caller is attempting to load the hive, they most likely already have write access to that file. So regardless of its contents, if the caller is determined to load the hive, they can just modify it accordingly (e.g. change the security descriptors). But it is interesting to note that the above statement is only partially correct: indeed, no new security descriptors can be added to an active app hive, either through a RegSetKeySecurity call or by creating a new key with a custom descriptor (e.g. with a RegCreateKeyEx call with a non-NULL lpSecurityAttributes parameter). However, it is not quite right that RegLoadAppKey will fail if there is more than one security descriptor: currently, there are no such restrictions enforced and app hives can be successfully loaded with any number of descriptors. Furthermore, only KEY\_READ access is checked rather than the samDesired mask specified by the caller, and only against the root key instead of all keys in the hive (this ties to there potentially being more than one descriptor). This has been reported to Microsoft in [Windows Kernel enforcement of registry app hive security is inconsistent with documentation](https://github.com/googleprojectzero/p0tools/tree/master/WinRegLowSeverityBugs/Reports/20_App_hive_security_inconsistencies), and has been acknowledged as a discrepancy between documentation and implementation, but it is unclear if/when any steps will be taken to address it.

#### Mount Points

Application hives are subject to even stricter requirements with regards to mount points than normal hives: not only do they have to be mounted in the master hive, but it has to be specifically under \Registry\A. This "A" key is unique in that it and its subkeys are explicitly protected from opening by name. The check takes place in CmpParseKey, and the specific routine responsible for verifying the path is CmpDoesParseEnterRegistryA. Some of these rigorous checks were added and/or refined in response to James's issues [#865](https://bugs.chromium.org/p/project-zero/issues/detail?id=865) and [#870](https://bugs.chromium.org/p/project-zero/issues/detail?id=870) discovered in 2016. This means that the only way to obtain a handle to a key within \Registry\A is through the RootHandle argument to NtLoadKeyEx / NtLoadKey3, which ensures maximum privacy for the application hives. Since the names of the mount points are not used for anything, the only important property is that they don't collide with each other. This is guaranteed by KernelBase.dll in the internal BuildRootKeyName function, which picks the mount point name by generating a random 128-bit number and formatting it as a GUID string.


Another interesting feature of app hives is their ability to be shared between processes. If multiple processes load the same hive without the REG\_PROCESS\_APPKEY flag, they'll all access the same underlying data. In practice, if an app hive is first loaded at \Registry\A\Test1, and another program tries to load the same hive at \Registry\A\Test2, the kernel will effectively reuse the existing "Test1" hive, providing the caller with a handle to it. Because the mount point is irrelevant to the client after loading, this approach is both safe and efficient.

#### Flags

In addition to the flag restrictions imposed on normal hives, application hives disallow REG\_NO\_LAZY\_FLUSH (0x4), REG\_START\_JOURNAL (0x40) and REG\_BOOT\_HIVE (0x400), which means that REG\_FLUSH\_HIVE\_FILE\_GROWTH (0x1000) is also prohibited. This leaves 0xEBB0 as the supported set of flags.


It's also worth noting that even though it is allowed, REG\_HIVE\_NO\_RM (0x100) doesn't do anything for app hives because KTM transactions are disabled for them anyway. Furthermore, there seems to be a minor bug where specifying both the REG\_APP\_HIVE (0x10) and REG\_LOAD\_HIVE\_OPEN\_HANDLE (0x800) flags will cause the hive to stay loaded indefinitely. This proved useful as an exploitation primitive in issue [#2378](https://bugs.chromium.org/p/project-zero/issues/detail?id=2378), but in general it simply leads to a memory leak and locking the hive file until the next reboot.

#### Unloading

Application hives don't need to be manually unloaded with any of the NtUnloadKey\* system calls, but instead they are automatically unloaded when all handles to the hive's keys are closed. Internally, this is achieved by checking if the reference count of the root key's KCB has dropped to a near-zero value, and scheduling the CmpLateUnloadHiveWorker function to perform the actual cleanup.

### Differencing hive loading

Differencing hives are the third major category of hives and the most recent one, introduced in Windows 10 1607. They are similar to application hives in that they are invisible to the naked eye (you won't typically see them in Regedit), but they are also much more complex, both for loading and operating on. Let's see how they compare to the other types of hives we have discussed so far.

#### Privileges

I have to start by saying that it is impossible to load a differencing hive with any of the standard NtLoadKey-family syscalls. These special hives need to be overlaid on top of other hives, and must also be configured as either writethrough or not. Instead of adding yet another system call or extending an existing one to accommodate these settings, Microsoft decided to take a different approach. This explains why none of the REG\_\* flags listed above reference differencing hives in any way.


In order to support registry containerization, the vendor added a driver called "VRegDriver" that is built into the ntoskrnl.exe executable image. It consists of two main parts: an IOCTL interface accessible at \Device\VRegDriver allowing communication with other system components, and a [registry callback](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/filtering-registry-calls) (VrpRegistryCallback) that implements the namespace redirection functionality. The generic IOCTL handler is VrpIoctlDeviceDispatch, and it supports nine different operations. One of them is 0x220008, handled by VrpHandleIoctlLoadDifferencingHive. This is the IOCTL used by the AppInfo service to load differencing hives on behalf of a starting Centennial application, and it does so by taking an undocumented structure on input, extracting the necessary information from it and calling directly into the internal CmLoadDifferencingKey routine to load the hive – the same one that NtLoadKey\* use, too. (On a side note, there is a similar IOCTL 0x220020 handled by VrpHandleIoctlLoadDifferencingHiveForHost, but it's currently unclear how it's used or how it differs from 0x220008.)


Given all this, directly loading a differencing hive requires the ability to open the \Device\VRegDriver object (only accessible to administrators), as well as having the SeBackupPrivilege and SeRestorePrivilege rights (enforced by the IOCTL handler). Thus, it's clear that the option is not available to normal users. Alternatively, one can take advantage of the legitimate uses of the mechanism – bundle a malicious hive with a MSIX-packaged app or a Docker container that gets installed on the victim machine, and have it loaded as part of normal system operation. Naturally, this significantly limits the attack's practicality and also imposes further constraints on how the hive is loaded.


That said, loading custom differencing hives may not be necessarily required to exploit vulnerabilities related to layered keys. The \Registry\WC key is not locked down the same way as \Registry\A is, so it can be freely enumerated, and its subkeys can be opened and accessed according to their security descriptors. Furthermore, there are a number of default programs in Windows that make use of differencing hives, and in many cases an attacker can simply reuse one of them for their own purposes. For example, out of the [10 bugs](<https://project-zero.issues.chromium.org/issues?q=id:(42451588%20%7C%2042451589%20%7C%2042451590%20%7C%2042451592%20%7C%2042451596%20%7C%2042451607%20%7C%2042451608%20%7C%2042451609%20%7C%2042451611%20%7C%2042451625)>) I found that involved layered keys, only [2](<https://project-zero.issues.chromium.org/issues?q=id:(42451596%20%7C%2042451625)>) of them required the ability to load custom differencing hives.

#### Mount Points

None of the kernel-mode components enforce any specific requirements with regards to the differencing hive mount points, other than them being located in the master hive (as for every other hive). This means that in theory, they could be loaded anywhere within \Registry or one of its four subkeys. In practice, all services using these hives for their intended purpose always load them under \Registry\WC.

#### Flags

Let's take a look at my reverse-engineered definition of the input structure expected by VrpHandleIoctlLoadDifferencingHive on Windows 11, which can be found in the [CreateAndLoadDifferencingHive.cpp](https://bugs.chromium.org/p/project-zero/issues/attachmentText?aid=608460) proof-of-concept exploit for issue [#2479](https://bugs.chromium.org/p/project-zero/issues/detail?id=2479):


struct VRP_LOAD_DIFFERENCING_HIVE_INPUT {

/* +0x00 */HANDLE hJob;

/* +0x08 */DWORD Unused1;

/* +0x0c */DWORD DiffHiveFlags;

/* +0x10 */DWORD LoadFlags;

/* +0x14 */WORD  MountPointLength;

/* +0x16 */WORD  HivePathLength;

/* +0x18 */WORD  BaseLayerPathLength;

/* +0x1a */WORD  Unused2;

/* +0x1c */DWORD Unused3;

/* +0x20 */HANDLE hToken;

/* +0x28 */WCHAR Buffer[1];

};


Here at offset 0x10, LoadFlags represents the same information that is normally passed via the Flags argument to NtLoadKey\* system calls. The set of legal flags for differencing hives is very narrow and consists of only three of them: REG\_HIVE\_NO\_RM (0x100), REG\_OPEN\_READ\_ONLY (0x2000) and REG\_IMMUTABLE (0x4000).


Moreover, there is also an extra DiffHiveFlags member at offset 0xc that specifies the flags specific to differencing hives. So far, I have observed three supported flags and deduced their meaning to be as follows:


#define DIFF_HIVE_ADD_TO_TRUST_CLASS 1

#define DIFF_HIVE_WRITETHROUGH       2

#define DIFF_HIVE_TRUSTED            4


The first and third flags are related to trust classes and the following of symbolic links, while the second one defines whether the hive is writethrough, which is a special type of differencing hive that redirects all write operations on its keys to the lower layers. If DIFF\_HIVE\_WRITETHROUGH is set in DiffHiveFlags, then REG\_IMMUTABLE must be set in LoadFlags.

#### Unloading

According to my experimentation, differencing hives are generally unloaded when the corresponding silo is destroyed: either by a system service invoking the 0x220018 IOCTL (VrpHandleIoctlUnloadDynamicallyLoadedHives) tearing down the container, or automatically when cleaning up the corresponding job object, which ends up in the internal VrpUnloadDifferencingHive routine. Eventually, both functions call ZwUnloadKey\* (a kernel-mode wrapper around NtUnloadKey\*), following the standard hive unloading procedure.

## Conclusion

In this post, I tried to shed some light on the structure of the registry tree, both at the high-level (WinAPI) and low-level (internal system libraries and the kernel). As shown, the relationship between these two views is complicated and contains many unexpected quirks. At the same time, becoming familiar with this design is invaluable for understanding some of the more advanced registry features and their security ramifications. I haven't been able to find a resource that systematically covers this subject, so I hope the blog post was helpful. In the next installment in the series, I will explain the internal structure of the hives and the many things that may surprise you there.
